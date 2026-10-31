#!/usr/bin/env python3
"""
Contract framework-hop nodes in graph_def.py.

For each framework-hop node U (class not in method_list, or method not declared in class):
1. For every pair A->U and U->B, add A->B (framework dispatch inference)
2. Remove all edges touching U
3. If U has no incoming edges (fake root), check if it should route from S_ENTRY or real page
4. If U has incoming edges only (sink), remove those edges

Usage: python3 -I contract_framework_hops.py <test|full>
"""

import ast
import collections
import json
import os
import sys

# Working directory: /Users/darshan/Desktop/yang/work
GRAPH_DIR = 'graphs/AmazeFileManager'
GRAPH_DEF = f'{GRAPH_DIR}/graph_def.py'
METHOD_LIST = f'{GRAPH_DIR}/method_list.json'
FRAMEWORK_HOP_LIST = f'{GRAPH_DIR}/scratch/framework_hop_nodes.txt'
GENERATED_BAD_EDGES = f'{GRAPH_DIR}/scratch/generated_bad_edges.txt'
SCRATCH_DIR = f'{GRAPH_DIR}/scratch'

def load_framework_hops():
    """Load framework-hop node list"""
    hops = {}
    with open(FRAMEWORK_HOP_LIST, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('\t')
            if len(parts) >= 2:
                node_name = parts[0].strip()
                reason = parts[1].strip()
                hops[node_name] = reason
    return hops

def load_method_list():
    """Load method_list.json and build index"""
    rows = json.load(open(METHOD_LIST))
    methods_by_short = collections.defaultdict(list)
    for r in rows:
        methods_by_short[r['short']].append(r)
    return rows, methods_by_short

def parse_graph_def():
    """Parse graph_def.py and extract edge calls"""
    with open(GRAPH_DEF, 'r', encoding='utf-8') as f:
        source = f.read()
    
    tree = ast.parse(source, GRAPH_DEF)
    
    edges = []
    unreachable_entries = []
    
    # Find all e(...) calls at module level
    for node in ast.walk(tree):
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            call = node.value
            # Check if it's e(...) call
            if isinstance(call.func, ast.Name) and call.func.id == 'e':
                # Extract edge info
                if len(call.args) >= 4:
                    try:
                        src = ast.literal_eval(call.args[0])
                        dst = ast.literal_eval(call.args[1])
                        kind = ast.literal_eval(call.args[2])
                        evidence = ast.literal_eval(call.args[3])
                        
                        # Extract keyword args
                        kwargs = {}
                        for kw in call.keywords:
                            try:
                                kwargs[kw.arg] = ast.literal_eval(kw.value)
                            except:
                                pass
                        
                        edges.append({
                            'src': src,
                            'dst': dst,
                            'kind': kind,
                            'evidence': evidence,
                            'kwargs': kwargs,
                            'lineno': node.lineno,
                            'node': node
                        })
                    except:
                        pass
        
        # Find UNREACHABLE['...'] assignments
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Subscript):
                    if isinstance(target.value, ast.Name) and target.value.id == 'UNREACHABLE':
                        try:
                            method = ast.literal_eval(target.slice)
                            value = ast.literal_eval(node.value)
                            unreachable_entries.append({
                                'method': method,
                                'value': value,
                                'lineno': node.lineno
                            })
                        except:
                            pass
    
    return source, edges, unreachable_entries

def build_edge_index(edges, framework_hops):
    """Build index of edges by source and destination"""
    incoming = collections.defaultdict(list)
    outgoing = collections.defaultdict(list)
    
    for edge in edges:
        src = edge['src']
        dst = edge['dst']
        
        incoming[dst].append(edge)
        outgoing[src].append(edge)
    
    return incoming, outgoing

def infer_edges(framework_hops, edges, incoming, outgoing, screens):
    """For each framework-hop node, create inferred A->B edges"""
    inferred = []
    fake_root_actions = []  # Log fake root analysis
    
    for hop_node in framework_hops:
        in_edges = incoming.get(hop_node, [])
        out_edges = outgoing.get(hop_node, [])
        
        # Handle fake roots (no incoming edges)
        if not in_edges and out_edges:
            # Check if this should route from S_ENTRY or a real page
            # For now, log them for manual inspection - Step 1 says to check cited source
            fake_root_actions.append({
                'node': hop_node,
                'outgoing': len(out_edges),
                'action': 'MANUAL_INSPECTION_NEEDED'
            })
            continue
        
        # Handle sinks (no outgoing edges)
        if in_edges and not out_edges:
            # These incoming edges will be removed
            continue
        
        # Handle dispatchers (both incoming and outgoing)
        if in_edges and out_edges:
            # Create A->B for each A->U, U->B pair
            for in_edge in in_edges:
                for out_edge in out_edges:
                    src = in_edge['src']
                    dst = out_edge['dst']
                    
                    # Determine kind: if src is a page (S_*), use incoming kind; else use outgoing kind
                    if src.startswith('S_'):
                        kind = in_edge['kind']
                    else:
                        kind = out_edge['kind']
                    
                    # Combine guard/env/needs_state
                    kwargs = {}
                    
                    # Merge guard
                    in_guard = in_edge['kwargs'].get('guard')
                    out_guard = out_edge['kwargs'].get('guard')
                    if in_guard and out_guard:
                        kwargs['guard'] = in_guard + ' and ' + out_guard
                    elif in_guard:
                        kwargs['guard'] = in_guard
                    elif out_guard:
                        kwargs['guard'] = out_guard
                    
                    # Merge env
                    in_env = in_edge['kwargs'].get('env')
                    out_env = out_edge['kwargs'].get('env')
                    if in_env and out_env:
                        kwargs['env'] = in_env if in_env == out_env else in_env + '; ' + out_env
                    elif in_env:
                        kwargs['env'] = in_env
                    elif out_env:
                        kwargs['env'] = out_env
                    
                    # Merge needs_state
                    in_state = in_edge['kwargs'].get('needs_state')
                    out_state = out_edge['kwargs'].get('needs_state')
                    if in_state and out_state:
                        kwargs['needs_state'] = in_state if in_state == out_state else in_state + '; ' + out_state
                    elif in_state:
                        kwargs['needs_state'] = in_state
                    elif out_state:
                        kwargs['needs_state'] = out_state
                    
                    # Combine evidence
                    in_evidence = in_edge['evidence']
                    out_evidence = out_edge['evidence']
                    evidence = f"{in_evidence}; {out_evidence}; INFERRED framework dispatch through {hop_node} (not an app method)"
                    
                    inferred.append({
                        'src': src,
                        'dst': dst,
                        'kind': kind,
                        'evidence': evidence,
                        'kwargs': kwargs,
                        'hop_node': hop_node
                    })
    
    return inferred, fake_root_actions

def format_edge_call(edge):
    """Format edge as e(...) call"""
    args = [
        repr(edge['src']),
        repr(edge['dst']),
        repr(edge['kind']),
        repr(edge['evidence'])
    ]
    
    kwargs_parts = []
    if 'guard' in edge['kwargs']:
        kwargs_parts.append(f"guard={repr(edge['kwargs']['guard'])}")
    if 'env' in edge['kwargs']:
        kwargs_parts.append(f"env={repr(edge['kwargs']['env'])}")
    if 'needs_state' in edge['kwargs']:
        kwargs_parts.append(f"needs_state={repr(edge['kwargs']['needs_state'])}")
    
    if kwargs_parts:
        return f"e({', '.join(args)}, {', '.join(kwargs_parts)})"
    else:
        return f"e({', '.join(args)})"

def remove_edges_touching_hops(source_lines, edges, framework_hops):
    """Remove all edges touching framework-hop nodes using AST-precise removal"""
    # Build set of line numbers to remove
    lines_to_remove = set()
    
    for edge in edges:
        if edge['src'] in framework_hops or edge['dst'] in framework_hops:
            lines_to_remove.add(edge['lineno'])
    
    # Remove lines (1-indexed)
    output_lines = []
    for i, line in enumerate(source_lines, 1):
        if i not in lines_to_remove:
            output_lines.append(line)
    
    return output_lines

def test_run(framework_hops, limit=20):
    """Test on first N framework-hop nodes"""
    print(f"Testing on first {limit} framework-hop nodes...")
    test_hops = dict(list(framework_hops.items())[:limit])
    return test_hops

def main(argv):
    if len(argv) < 2 or argv[1] not in ('test', 'full'):
        print(__doc__)
        return 1
    
    mode = argv[1]
    
    # Load framework hops
    print("Loading framework-hop node list...")
    framework_hops = load_framework_hops()
    print(f"Loaded {len(framework_hops)} framework-hop nodes")
    
    if mode == 'test':
        framework_hops = test_run(framework_hops, limit=20)
    
    # Parse graph_def.py
    print("Parsing graph_def.py...")
    source, edges, unreachable_entries = parse_graph_def()
    print(f"Found {len(edges)} edges, {len(unreachable_entries)} UNREACHABLE entries")
    
    # Build edge index
    print("Building edge index...")
    incoming, outgoing = build_edge_index(edges, framework_hops)
    
    # Extract screen names from graph_def
    screens = set()
    for edge in edges:
        if edge['src'].startswith('S_'):
            screens.add(edge['src'])
        if edge['dst'].startswith('S_'):
            screens.add(edge['dst'])
    
    # Infer new edges
    print("Inferring edges through framework-hop nodes...")
    inferred_edges, fake_root_actions = infer_edges(framework_hops, edges, incoming, outgoing, screens)
    print(f"Inferred {len(inferred_edges)} new edges")
    print(f"Found {len(fake_root_actions)} fake roots needing manual inspection")
    
    # Remove edges touching framework-hop nodes
    print("Removing edges touching framework-hop nodes...")
    source_lines = source.splitlines(keepends=True)
    output_lines = remove_edges_touching_hops(source_lines, edges, framework_hops)
    
    # Insert inferred edges at the end before UNREACHABLE section
    # Find line with "UNREACHABLE = {"
    insert_pos = None
    for i, line in enumerate(output_lines):
        if line.strip().startswith('UNREACHABLE = {'):
            insert_pos = i
            break
    
    if insert_pos is None:
        print("ERROR: Could not find 'UNREACHABLE = {' line")
        return 1
    
    # Insert inferred edges before UNREACHABLE
    inferred_section = [
        '\n',
        f'# ---- Inferred edges through framework-hop nodes (contracted {len(framework_hops)} nodes)\n',
        '\n'
    ]
    
    for edge in inferred_edges:
        inferred_section.append(format_edge_call(edge) + '\n')
    
    output_lines = output_lines[:insert_pos] + inferred_section + output_lines[insert_pos:]
    
    # Write output
    output_path = GRAPH_DEF if mode == 'full' else GRAPH_DEF.replace('.py', f'_contract_{mode}.py')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)
    
    print(f"\nWrote contracted graph to: {output_path}")
    print(f"Added {len(inferred_edges)} inferred edges")
    print(f"Removed edges touching {len(framework_hops)} framework-hop nodes")
    
    # Log statistics
    fake_roots = []
    sinks = []
    dispatchers = []
    
    for hop_node, reason in framework_hops.items():
        in_edges = incoming.get(hop_node, [])
        out_edges = outgoing.get(hop_node, [])
        
        if not in_edges and not out_edges:
            continue
        elif not in_edges:
            fake_roots.append((hop_node, reason, out_edges))
        elif not out_edges:
            sinks.append((hop_node, reason, in_edges))
        else:
            dispatchers.append((hop_node, len(in_edges), len(out_edges)))
    
    print(f"\nFramework-hop node categories:")
    print(f"  Dispatchers (A->U->B): {len(dispatchers)}")
    print(f"  Fake roots (no incoming): {len(fake_roots)}")
    print(f"  Sinks (no outgoing): {len(sinks)}")
    
    if fake_roots:
        print(f"\nFake roots that need manual inspection:")
        for node, reason, out_edges in fake_roots[:10]:
            print(f"  {node}: {len(out_edges)} outgoing edges")
            print(f"    Reason: {reason}")
    
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
