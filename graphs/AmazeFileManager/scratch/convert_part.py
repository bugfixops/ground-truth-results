#!/usr/bin/env python3
"""
Convert repair part files to graph_def.py format.
Handles EDGES.append(edge(...)), EDGES = {} dict, and EDGES = [] list formats.
"""
import ast
import re
import sys
import os

# Valid edge kinds from schema-2
VALID_KINDS = {'FRAMEWORK', 'EXPLICIT', 'LIFECYCLE', 'SYSTEM', 'INTENT', 'RESULT', 'ENTERS', 'CALL', 'ASYNC', 'GUI'}

def normalize_kind(kind):
    """Normalize edge kind to valid schema-2 kind."""
    kind = kind.upper().strip()
    # Map common variations
    kind_map = {
        'DIRECT': 'CALL',
        'CONSTRUCTED': 'CALL',
        'CALLS': 'CALL',
        'FW': 'FRAMEWORK',
        'UI': 'GUI',
        'CALLBACK': 'CALL',
        'INTRA': 'CALL',
        'ENTRY': 'LIFECYCLE',  # Entry points are typically lifecycle events
        'IMPLICIT': 'FRAMEWORK',  # Implicit framework calls
    }
    normalized = kind_map.get(kind, kind)
    if normalized not in VALID_KINDS:
        print(f"WARNING: Unknown kind '{kind}' -> using 'CALL'", file=sys.stderr)
        return 'CALL'
    return normalized

def parse_part_file(part_path):
    """Parse a part file and extract edges and UNREACHABLE entries."""
    with open(part_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    edges = []
    unreachable = {}
    
    try:
        tree = ast.parse(content)
    except SyntaxError as e:
        print(f"ERROR: Failed to parse {part_path}: {e}", file=sys.stderr)
        return edges, unreachable
    
    # Extract EDGES.append(edge(...)) calls
    for node in ast.walk(tree):
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            call = node.value
            # Check for EDGES.append(edge(...))
            if (isinstance(call.func, ast.Attribute) and 
                call.func.attr == 'append' and
                isinstance(call.func.value, ast.Name) and
                call.func.value.id == 'EDGES' and
                len(call.args) == 1 and
                isinstance(call.args[0], ast.Call)):
                
                inner_call = call.args[0]
                if isinstance(inner_call.func, ast.Name) and inner_call.func.id == 'edge':
                    edge = extract_edge_from_call(inner_call)
                    if edge:
                        edges.append(edge)
        
        # Check for direct e(...) calls
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            call = node.value
            if isinstance(call.func, ast.Name) and call.func.id == 'e':
                edge = extract_e_call(call)
                if edge:
                    edges.append(edge)
        
        # Check for EDGES dict assignments
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Subscript):
                    if (isinstance(target.value, ast.Name) and 
                        target.value.id == 'EDGES' and
                        isinstance(node.value, ast.Dict)):
                        edge = extract_edge_from_dict(node.value)
                        if edge:
                            edges.append(edge)
        
        # Check for UNREACHABLE assignments
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Subscript):
                    if (isinstance(target.value, ast.Name) and 
                        target.value.id == 'UNREACHABLE'):
                        method = extract_string(target.slice)
                        value = extract_unreachable_value(node.value)
                        if method and value:
                            unreachable[method] = value
    
    return edges, unreachable

def extract_edge_from_call(call):
    """Extract edge from edge(...) function call."""
    edge = {}
    # Parse positional args: src, dst, kind, summary/trigger, evidence
    if len(call.args) >= 3:
        edge['src'] = extract_string(call.args[0])
        edge['dst'] = extract_string(call.args[1])
        edge['kind'] = extract_string(call.args[2])
    
    if len(call.args) >= 4:
        edge['trigger'] = extract_string(call.args[3])
    
    if len(call.args) >= 5:
        edge['evidence'] = extract_string(call.args[4])
    
    # Parse keyword args
    for keyword in call.keywords:
        key = keyword.arg
        if key in ['summary', 'trigger'] and 'trigger' not in edge:
            edge['trigger'] = extract_string(keyword.value)
        elif key == 'evidence':
            edge['evidence'] = extract_string(keyword.value)
        elif key == 'gui':
            edge['gui'] = extract_list(keyword.value)
        elif key == 'guard':
            edge['guard'] = extract_string(keyword.value)
        elif key == 'note':
            edge['note'] = extract_string(keyword.value)
        elif key == 'needs_state':
            edge['needs_state'] = extract_string(keyword.value)
        elif key == 'env':
            edge['env'] = extract_string(keyword.value)
    
    if not all(k in edge for k in ['src', 'dst', 'kind']):
        return None
    
    return edge

def extract_e_call(call):
    """Extract edge from e(...) call (already in correct format)."""
    edge = {}
    if len(call.args) >= 3:
        edge['src'] = extract_string(call.args[0])
        edge['dst'] = extract_string(call.args[1])
        edge['kind'] = extract_string(call.args[2])
    if len(call.args) >= 4:
        edge['trigger'] = extract_string(call.args[3])
    
    for keyword in call.keywords:
        key = keyword.arg
        if key == 'evidence':
            edge['evidence'] = extract_string(keyword.value)
        elif key == 'gui':
            edge['gui'] = extract_list(keyword.value)
        elif key == 'guard':
            edge['guard'] = extract_string(keyword.value)
    
    return edge if edge.get('src') and edge.get('dst') and edge.get('kind') else None

def extract_edge_from_dict(dict_node):
    """Extract edge from dict literal."""
    edge = {}
    for key, value in zip(dict_node.keys, dict_node.values):
        key_str = extract_string(key)
        if key_str in ['src', 'dst', 'kind', 'trigger', 'text', 'summary', 'evidence', 'guard', 'note']:
            edge[key_str] = extract_string(value)
    
    # Map 'text' to 'trigger'
    if 'text' in edge and 'trigger' not in edge:
        edge['trigger'] = edge['text']
    
    return edge if edge.get('src') and edge.get('dst') and edge.get('kind') else None

def extract_unreachable_value(node):
    """Extract UNREACHABLE value (tuple of strings)."""
    if isinstance(node, ast.Tuple):
        return tuple(extract_string(elt) for elt in node.elts)
    return None

def extract_string(node):
    """Extract string value from AST node."""
    if isinstance(node, ast.Constant):
        return str(node.value) if node.value is not None else None
    elif hasattr(ast, 'Str') and isinstance(node, ast.Str):  # Python < 3.8
        return node.s
    elif isinstance(node, ast.Name):
        return node.id
    return None

def extract_list(node):
    """Extract list of strings from AST node."""
    if isinstance(node, ast.List):
        return [extract_string(elt) for elt in node.elts if extract_string(elt)]
    return []

def load_existing_edges(graph_def_path):
    """Load existing edges from graph_def.py to detect duplicates."""
    existing = set()
    try:
        with open(graph_def_path, 'r', encoding='utf-8') as f:
            content = f.read()
        tree = ast.parse(content)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
                call = node.value
                if isinstance(call.func, ast.Name) and call.func.id == 'e':
                    if len(call.args) >= 3:
                        src = extract_string(call.args[0])
                        dst = extract_string(call.args[1])
                        kind = extract_string(call.args[2])
                        if src and dst and kind:
                            existing.add((src, dst, normalize_kind(kind)))
    except Exception as e:
        print(f"WARNING: Could not parse graph_def.py: {e}", file=sys.stderr)
    
    return existing

def format_edge_as_e_call(edge):
    """Format edge as e(...) call string."""
    src = edge.get('src', '')
    dst = edge.get('dst', '')
    kind = normalize_kind(edge.get('kind', 'CALL'))
    trigger = edge.get('trigger', f'{src} -> {dst}')
    
    # Escape quotes in strings
    src = src.replace("'", "\\'")
    dst = dst.replace("'", "\\'")
    trigger = trigger.replace("'", "\\'")
    
    lines = [f"e('{src}', '{dst}', '{kind}',"]
    lines.append(f"  '{trigger}',")
    
    # Add optional parameters as keywords
    if edge.get('gui'):
        gui_items = ', '.join(f"'{g}'" for g in edge['gui'])
        lines.append(f"  gui=[{gui_items}],")
    
    if edge.get('guard'):
        guard = edge['guard'].replace("'", "\\'")
        lines.append(f"  guard='{guard}',")
    
    if edge.get('note'):
        note = edge['note'].replace("'", "\\'")
        lines.append(f"  note='{note}',")
    
    if edge.get('needs_state'):
        needs_state = edge['needs_state'].replace("'", "\\'")
        lines.append(f"  needs_state='{needs_state}',")
    
    if edge.get('env'):
        env = edge['env'].replace("'", "\\'")
        lines.append(f"  env='{env}',")
    
    if edge.get('evidence'):
        evidence = edge['evidence'].replace("'", "\\'")
        lines.append(f"  evidence='{evidence}')")
    else:
        # Replace trailing comma with closing paren
        lines[-1] = lines[-1].rstrip(',') + ')'
    
    return '\n'.join(lines)

def convert_part(part_num, work_dir):
    """Convert a part file to graph_def.py format."""
    part_path = os.path.join(work_dir, f'graphs/AmazeFileManager/parts/repair_rp{part_num:02d}.py')
    md_path = os.path.join(work_dir, f'graphs/AmazeFileManager/parts/repair_rp{part_num:02d}.md')
    out_path = os.path.join(work_dir, f'graphs/AmazeFileManager/parts/repair_rp{part_num:02d}_converted.py')
    graph_def_path = os.path.join(work_dir, 'graphs/AmazeFileManager/graph_def.py')
    
    if not os.path.exists(part_path):
        print(f"ERROR: Part file not found: {part_path}", file=sys.stderr)
        return False
    
    print(f"Converting repair_rp{part_num:02d}...")
    
    # Parse the part file
    edges, unreachable = parse_part_file(part_path)
    print(f"  Found {len(edges)} edges, {len(unreachable)} UNREACHABLE entries")
    
    # Load existing edges to check for duplicates
    existing = load_existing_edges(graph_def_path)
    print(f"  Loaded {len(existing)} existing edges from graph_def.py")
    
    # Filter out duplicates
    new_edges = []
    dup_count = 0
    for edge in edges:
        key = (edge.get('src'), edge.get('dst'), normalize_kind(edge.get('kind', 'CALL')))
        if key not in existing:
            new_edges.append(edge)
        else:
            dup_count += 1
    
    print(f"  Filtered out {dup_count} duplicate edges, {len(new_edges)} remain")
    
    # Write converted file
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(f"# Converted from repair_rp{part_num:02d}.py\n")
        f.write(f"# Original: {len(edges)} edges, Duplicates removed: {dup_count}, New: {len(new_edges)}\n\n")
        
        for edge in new_edges:
            f.write(format_edge_as_e_call(edge))
            f.write('\n\n')
        
        if unreachable:
            f.write("# UNREACHABLE entries\n\n")
            for method, value in unreachable.items():
                f.write(f"UNREACHABLE['{method}'] = {repr(value)}\n")
    
    # Verify it compiles
    import py_compile
    try:
        py_compile.compile(out_path, doraise=True)
        print(f"  ✓ Compiled successfully: {out_path}")
        return True
    except py_compile.PyCompileError as e:
        print(f"  ✗ Compilation failed: {e}", file=sys.stderr)
        return False

if __name__ == '__main__':
    work_dir = '/Users/darshan/Desktop/yang/work'
    
    if len(sys.argv) < 2:
        print("Usage: convert_part.py <part_number>")
        sys.exit(1)
    
    part_num = int(sys.argv[1])
    success = convert_part(part_num, work_dir)
    sys.exit(0 if success else 1)
