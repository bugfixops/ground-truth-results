#!/usr/bin/env python3
"""
Apply framework-hop node contraction to graph_def.py.

This script:
1. Contracts dispatcher nodes (A->U->B) by creating A->B edges
2. Re-sources C2 fake roots from Class.<init>
3. Removes C3 fake root edges
4. Validates the result with ast.parse before writing
"""

import ast
import collections
import json
import sys
from datetime import datetime

GRAPH_DIR = 'graphs/AmazeFileManager'
GRAPH_DEF = f'{GRAPH_DIR}/graph_def.py'
FAKE_ROOT_JSON = f'{GRAPH_DIR}/scratch/fake_root_classes.json'
FRAMEWORK_HOP_LIST = f'{GRAPH_DIR}/scratch/framework_hop_nodes.txt'

def load_classifications():
    """Load fake root classifications"""
    with open(FAKE_ROOT_JSON) as f:
        data = json.load(f)
    
    by_node = {}
    for item in data['classifications']:
        by_node[item['node']] = item
    
    return by_node, data['summary']

def load_framework_hops():
    hops = {}
    with open(FRAMEWORK_HOP_LIST) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('\t')
            if len(parts) >= 2:
                hops[parts[0].strip()] = parts[1].strip()
    return hops

def parse_graph_def():
    """Parse graph_def.py and extract edges with their AST nodes"""
    with open(GRAPH_DEF, 'r') as f:
        source = f.read()
        lines = source.splitlines(keepends=True)
    
    tree = ast.parse(source, GRAPH_DEF)
    
    edges = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            call = node.value
            if isinstance(call.func, ast.Name) and call.func.id == 'e':
                if len(call.args) >= 4:
                    try:
                        # Extract kwargs
                        kwargs = {}
                        for kw in call.keywords:
                            try:
                                kwargs[kw.arg] = ast.literal_eval(kw.value)
                            except:
                                pass
                        
                        edges.append({
                            'src': ast.literal_eval(call.args[0]),
                            'dst': ast.literal_eval(call.args[1]),
                            'kind': ast.literal_eval(call.args[2]),
                            'evidence': ast.literal_eval(call.args[3]),
                            'kwargs': kwargs,
                            'lineno': node.lineno,
                            'end_lineno': node.end_lineno
                        })
                    except:
                        pass
    
    return source, lines, edges

def format_edge_call(edge):
    """Format edge as e(...) call"""
    # Positional args: src, dst, kind, trigger
    args = [
        repr(edge['src']),
        repr(edge['dst']),
        repr(edge['kind']),
        repr(edge.get('trigger', ''))
    ]
    
    # Keyword args: evidence is REQUIRED, plus optional guard/env/needs_state/gui
    kwargs_parts = []
    
    # Evidence is mandatory
    evidence = edge.get('evidence', '')
    if not evidence:
        raise ValueError(f"Edge {edge['src']} -> {edge['dst']} has no evidence")
    kwargs_parts.append(f"evidence={repr(evidence)}")
    
    if 'guard' in edge.get('kwargs', {}):
        kwargs_parts.append(f"guard={repr(edge['kwargs']['guard'])}")
    if 'env' in edge.get('kwargs', {}):
        kwargs_parts.append(f"env={repr(edge['kwargs']['env'])}")
    if 'needs_state' in edge.get('kwargs', {}):
        kwargs_parts.append(f"needs_state={repr(edge['kwargs']['needs_state'])}")
    if 'gui' in edge.get('kwargs', {}):
        kwargs_parts.append(f"gui={repr(edge['kwargs']['gui'])}")
    
    return f"e({', '.join(args)}, {', '.join(kwargs_parts)})"

def main():
    print("Loading classifications...")
    fake_root_classes, summary = load_classifications()
    print(f"  C1: {summary['c1']}, C2: {summary['c2']}, C3: {summary['c3']}")
    
    print("\nLoading framework hops...")
    framework_hops = load_framework_hops()
    
    print("\nParsing graph_def.py...")
    source, lines, edges = parse_graph_def()
    print(f"Found {len(edges)} edges")
    
    # Build edge index
    incoming = collections.defaultdict(list)
    outgoing = collections.defaultdict(list)
    
    for edge in edges:
        incoming[edge['dst']].append(edge)
        outgoing[edge['src']].append(edge)
    
    # Identify node types
    dispatchers = []
    fake_roots_c1 = []
    fake_roots_c2 = []
    fake_roots_c3 = []
    sinks = []
    
    for hop_node in framework_hops:
        in_edges = incoming.get(hop_node, [])
        out_edges = outgoing.get(hop_node, [])
        
        if in_edges and out_edges:
            dispatchers.append(hop_node)
        elif not in_edges and out_edges:
            # Fake root - check classification
            if hop_node in fake_root_classes:
                cat = fake_root_classes[hop_node]['category']
                if cat == 'C1':
                    fake_roots_c1.append(hop_node)
                elif cat == 'C2':
                    fake_roots_c2.append(hop_node)
                else:
                    fake_roots_c3.append(hop_node)
        elif in_edges and not out_edges:
            sinks.append(hop_node)
    
    print(f"\nNode classification:")
    print(f"  Dispatchers (A->U->B): {len(dispatchers)}")
    print(f"  Fake roots C1 (genuine entry): {len(fake_roots_c1)}")
    print(f"  Fake roots C2 (app-internal): {len(fake_roots_c2)}")
    print(f"  Fake roots C3 (remove): {len(fake_roots_c3)}")
    print(f"  Sinks (remove incoming): {len(sinks)}")
    
    # Collect edges to remove (by line number range)
    lines_to_remove = set()
    new_edges = []
    
    # Process dispatchers: create A->B for each A->U->B
    for hop_node in dispatchers:
        in_edges = incoming[hop_node]
        out_edges = outgoing[hop_node]
        
        # Mark all edges touching this node for removal (entire line range)
        for edge in in_edges + out_edges:
            for line_num in range(edge['lineno'], edge['end_lineno'] + 1):
                lines_to_remove.add(line_num)
        
        # Create inferred edges
        for in_edge in in_edges:
            for out_edge in out_edges:
                src = in_edge['src']
                dst = out_edge['dst']
                
                # Determine kind
                if src.startswith('S_'):
                    kind = in_edge['kind']
                else:
                    kind = out_edge['kind']
                
                # Combine kwargs
                kwargs = {}
                in_guard = in_edge['kwargs'].get('guard')
                out_guard = out_edge['kwargs'].get('guard')
                if in_guard and out_guard:
                    kwargs['guard'] = f"({in_guard}) and ({out_guard})"
                elif in_guard:
                    kwargs['guard'] = in_guard
                elif out_guard:
                    kwargs['guard'] = out_guard
                
                in_env = in_edge['kwargs'].get('env')
                out_env = out_edge['kwargs'].get('env')
                if in_env and out_env:
                    kwargs['env'] = in_env if in_env == out_env else f"{in_env}; {out_env}"
                elif in_env:
                    kwargs['env'] = in_env
                elif out_env:
                    kwargs['env'] = out_env
                
                in_state = in_edge['kwargs'].get('needs_state')
                out_state = out_edge['kwargs'].get('needs_state')
                if in_state and out_state:
                    kwargs['needs_state'] = in_state if in_state == out_state else f"{in_state}; {out_state}"
                elif in_state:
                    kwargs['needs_state'] = in_state
                elif out_state:
                    kwargs['needs_state'] = out_state
                
                # Extract trigger text: from A->U if A is page, else from U->B
                if src.startswith('S_'):
                    # Parse trigger from in_edge's evidence
                    trigger = in_edge['evidence']
                else:
                    trigger = out_edge['evidence']
                
                # Combine evidence strings (keyword argument)
                evidence = f"{in_edge['evidence']}; {out_edge['evidence']}; INFERRED framework dispatch through {hop_node} (not an app method)"
                
                new_edges.append({
                    'src': src,
                    'dst': dst,
                    'kind': kind,
                    'trigger': trigger,
                    'evidence': evidence,
                    'kwargs': kwargs,
                    'reason': f'dispatcher_{hop_node}'
                })
    
    print(f"\nCreated {len(new_edges)} inferred edges from dispatchers")
    
    # Process C2 fake roots: re-source from Class.<init>
    for hop_node in fake_roots_c2:
        out_edges = outgoing[hop_node]
        class_name = fake_root_classes[hop_node]['class']
        
        # Mark for removal (entire line range)
        for edge in out_edges:
            for line_num in range(edge['lineno'], edge['end_lineno'] + 1):
                lines_to_remove.add(line_num)
        
        # Re-source from Class.<init>
        new_src = f"{class_name}.<init>"
        for out_edge in out_edges:
            # Determine if it's a lifecycle callback
            method_name = hop_node.split('.')[-1]
            is_lifecycle = method_name in ['onCreate', 'onStart', 'onResume', 'onPause', 'onStop', 
                                           'onDestroy', 'onBind', 'onStartCommand', 'onReceive',
                                           'onBindViewHolder', 'onCreateViewHolder', 'onAttach',
                                           'onCreateView', 'onViewCreated', 'onActivityCreated']
            
            kind = 'LIFECYCLE' if is_lifecycle else 'FRAMEWORK'
            
            # Trigger stays the same
            trigger = out_edge['evidence']
            
            # Evidence gets the label from original and adds inference note
            orig_label = out_edge['evidence'].split()[0] if out_edge['evidence'] else 'INFERRED'
            evidence = f"{out_edge['evidence']}; INFERRED framework calls {hop_node} after construction of {class_name}"
            
            new_edges.append({
                'src': new_src,
                'dst': out_edge['dst'],
                'kind': kind,
                'trigger': trigger,
                'evidence': evidence,
                'kwargs': out_edge['kwargs'],
                'reason': f'c2_fake_root_{hop_node}'
            })
    
    print(f"Re-sourced {len([e for e in new_edges if 'c2_fake_root' in e['reason']])} edges from C2 fake roots")
    
    # Process C3 fake roots: remove edges and log
    c3_removed = []
    for hop_node in fake_roots_c3:
        out_edges = outgoing[hop_node]
        for edge in out_edges:
            for line_num in range(edge['lineno'], edge['end_lineno'] + 1):
                lines_to_remove.add(line_num)
            c3_removed.append((hop_node, edge['dst'], edge['kind']))
    
    print(f"Removed {len(c3_removed)} edges from C3 fake roots")
    
    # Process C1 fake roots: replace with S_ENTRY (though we have 0)
    for hop_node in fake_roots_c1:
        out_edges = outgoing[hop_node]
        for edge in out_edges:
            for line_num in range(edge['lineno'], edge['end_lineno'] + 1):
                lines_to_remove.add(line_num)
        
        # Re-source from S_ENTRY
        for out_edge in out_edges:
            trigger = out_edge['evidence']
            orig_label = out_edge['evidence'].split()[0] if out_edge['evidence'] else 'INFERRED'
            evidence = f"{out_edge['evidence']}; INFERRED genuine entry point from manifest"
            
            new_edges.append({
                'src': 'S_ENTRY',
                'dst': out_edge['dst'],
                'kind': 'ENTRY',
                'trigger': trigger,
                'evidence': evidence,
                'kwargs': out_edge['kwargs'],
                'reason': f'c1_fake_root_{hop_node}'
            })
    
    # Process sinks: remove incoming edges
    for hop_node in sinks:
        in_edges = incoming[hop_node]
        for edge in in_edges:
            for line_num in range(edge['lineno'], edge['end_lineno'] + 1):
                lines_to_remove.add(line_num)
    
    print(f"Removed {len([hop_node for hop_node in sinks for _ in incoming[hop_node]])} edges to sinks")
    
    # Deduplicate edges by (src, dst, kind, guard)
    print(f"\nDeduplicating {len(new_edges)} new edges...")
    seen = set()
    dedup_edges = []
    for edge in new_edges:
        guard = edge['kwargs'].get('guard', '')
        key = (edge['src'], edge['dst'], edge['kind'], guard)
        if key not in seen:
            seen.add(key)
            dedup_edges.append(edge)
    
    print(f"After deduplication: {len(dedup_edges)} edges")
    new_edges = dedup_edges
    
    # Build new file content
    print("\nBuilding new graph_def.py...")
    new_lines = []
    
    for i, line in enumerate(lines, 1):
        if i not in lines_to_remove:
            new_lines.append(line)
    
    # Find insertion point (before UNREACHABLE)
    insert_idx = None
    for i, line in enumerate(new_lines):
        if line.strip().startswith('UNREACHABLE = {'):
            insert_idx = i
            break
    
    if insert_idx is None:
        print("ERROR: Could not find 'UNREACHABLE = {' line")
        return 1
    
    # Insert new edges
    date_str = datetime.now().strftime('%Y-%m-%d')
    insertion = [
        '\n',
        f'# ---- Step 1 cleanup: framework-hop contraction ({date_str})\n',
        f'# Contracted {len(dispatchers)} dispatchers, re-sourced {len(fake_roots_c2)} C2 fake roots,\n',
        f'# removed {len(fake_roots_c3)} C3 fake roots and {len(sinks)} sinks\n',
        '\n'
    ]
    
    for edge in new_edges:
        insertion.append(format_edge_call(edge) + '\n')
    
    insertion.append('\n')
    
    new_lines = new_lines[:insert_idx] + insertion + new_lines[insert_idx:]
    
    # Validate with ast.parse
    new_content = ''.join(new_lines)
    print("Validating with ast.parse...")
    try:
        ast.parse(new_content, GRAPH_DEF)
        print("✓ Syntax valid")
    except SyntaxError as e:
        print(f"✗ Syntax error: {e}")
        print("Not writing file")
        return 1
    
    # Write output
    output_path = GRAPH_DEF
    with open(output_path, 'w') as f:
        f.write(new_content)
    
    print(f"\n✓ Wrote contracted graph to: {output_path}")
    print(f"\nSummary:")
    print(f"  Total new edges: {len(new_edges)}")
    print(f"  Lines removed: {len(lines_to_remove)}")
    print(f"  C3 edges removed (logged): {len(c3_removed)}")
    
    # Write C3 removal log
    log_path = f'{GRAPH_DIR}/scratch/repair_log.md'
    with open(log_path, 'a') as f:
        f.write(f'\n## Step 1 C3 Fake Root Removals ({date_str})\n\n')
        f.write(f'Removed {len(c3_removed)} edges from {len(fake_roots_c3)} C3 fake root nodes:\n\n')
        for hop_node, dst, kind in c3_removed:
            f.write(f'- {hop_node} --{kind}--> {dst} (fake root: no app entry or constructor)\n')
    
    print(f"\n✓ Logged C3 removals to: {log_path}")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
