#!/usr/bin/env python3
"""
Precisely delete e() calls with unknown endpoints using AST parsing.
Only delete top-level e() calls with string literal arguments.
"""

import ast
import re
import sys

def parse_unknown_nodes_from_build(build_file):
    """Extract all unique unknown node names from build errors"""
    unknown_nodes = set()
    
    with open(build_file, 'r') as f:
        for line in f:
            # Format: ERROR <EdgeID>: unknown src|dst node <NodeName>
            match = re.match(r'\s*ERROR\s+[^:]+:\s+unknown\s+(?:src|dst)\s+node\s+(.+)', line)
            if match:
                node_name = match.group(1).strip()
                unknown_nodes.add(node_name)
    
    return unknown_nodes

def find_bad_e_calls(source_code, unknown_nodes):
    """Find all top-level e() calls with unknown endpoints using AST"""
    tree = ast.parse(source_code)
    bad_calls = []
    generated_calls = []
    
    for node in ast.walk(tree):
        # Look for Call nodes where func is Name 'e'
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'e':
            # Check if args contain string literals matching unknown nodes
            if len(node.args) >= 2:
                src_arg = node.args[0]
                dst_arg = node.args[1]
                
                # Only process if both are string literals (Constant or Str)
                src_is_str = isinstance(src_arg, ast.Constant) and isinstance(src_arg.value, str)
                dst_is_str = isinstance(dst_arg, ast.Constant) and isinstance(dst_arg.value, str)
                
                if not (src_is_str or dst_is_str):
                    # This is a generated call (uses variables or f-strings)
                    if hasattr(node, 'lineno'):
                        generated_calls.append(node.lineno)
                    continue
                
                src_name = src_arg.value if src_is_str else None
                dst_name = dst_arg.value if dst_is_str else None
                
                # Check if either endpoint is in unknown_nodes
                if (src_name in unknown_nodes) or (dst_name in unknown_nodes):
                    # Check if this is a top-level call
                    # Walk up to find the parent context
                    is_top_level = False
                    
                    # Find the ExprStmt that contains this call
                    for potential_parent in ast.walk(tree):
                        if isinstance(potential_parent, ast.Expr):
                            if potential_parent.value == node:
                                # Check if this Expr is in module body
                                if potential_parent in tree.body:
                                    is_top_level = True
                                    break
                                # Or in a top-level if block that only has e() calls
                                for if_node in tree.body:
                                    if isinstance(if_node, ast.If):
                                        if potential_parent in if_node.body or potential_parent in if_node.orelse:
                                            is_top_level = True
                                            break
                    
                    if is_top_level:
                        # Extract call info
                        kind = node.args[2].value if len(node.args) > 2 and isinstance(node.args[2], ast.Constant) else 'CALL'
                        desc = node.args[3].value if len(node.args) > 3 and isinstance(node.args[3], ast.Constant) else ''
                        
                        # Look for evidence keyword arg
                        evidence = desc
                        for keyword in node.keywords:
                            if keyword.arg == 'evidence' and isinstance(keyword.value, ast.Constant):
                                evidence = keyword.value.value
                                break
                        
                        bad_calls.append({
                            'lineno': node.lineno,
                            'end_lineno': node.end_lineno,
                            'src': src_name or 'UNKNOWN',
                            'dst': dst_name or 'UNKNOWN',
                            'kind': kind,
                            'evidence': evidence
                        })
    
    return bad_calls, generated_calls

def delete_lines_precisely(source_lines, bad_calls):
    """Delete specific line ranges from source"""
    # Collect all line numbers to delete
    lines_to_delete = set()
    for call_info in bad_calls:
        for line_num in range(call_info['lineno'], call_info['end_lineno'] + 1):
            lines_to_delete.add(line_num)
    
    # Build new source without those lines
    new_lines = []
    for i, line in enumerate(source_lines, start=1):
        if i not in lines_to_delete:
            new_lines.append(line)
    
    return new_lines

def invariant_checks(old_text, new_text, num_deleted):
    """Run invariant checks"""
    checks_passed = True
    
    # 1. UNREACHABLE[' count unchanged
    old_unreachable_count = old_text.count("UNREACHABLE['")
    new_unreachable_count = new_text.count("UNREACHABLE['")
    if old_unreachable_count != new_unreachable_count:
        print(f"  ✗ FAILED: UNREACHABLE[' count changed: {old_unreachable_count} → {new_unreachable_count}")
        checks_passed = False
    else:
        print(f"  ✓ UNREACHABLE[' count unchanged: {old_unreachable_count}")
    
    # 2. UNREACHABLE = line unchanged
    old_unreachable_def = [line for line in old_text.split('\n') if re.match(r'^UNREACHABLE\s*=', line)]
    new_unreachable_def = [line for line in new_text.split('\n') if re.match(r'^UNREACHABLE\s*=', line)]
    if old_unreachable_def != new_unreachable_def:
        print(f"  ✗ FAILED: UNREACHABLE = definition changed")
        checks_passed = False
    else:
        print(f"  ✓ UNREACHABLE = definition unchanged")
    
    # 3. Edge count
    old_edge_count = old_text.count('\ne(')
    new_edge_count = new_text.count('\ne(')
    expected_new_count = old_edge_count - num_deleted
    if new_edge_count != expected_new_count:
        print(f"  ✗ FAILED: Edge count: {old_edge_count} → {new_edge_count}, expected {expected_new_count}")
        checks_passed = False
    else:
        print(f"  ✓ Edge count: {old_edge_count} → {new_edge_count} (deleted {num_deleted})")
    
    # 4. Parse check
    try:
        ast.parse(new_text)
        print(f"  ✓ File still parses")
    except SyntaxError as e:
        print(f"  ✗ FAILED: Syntax error after deletion: {e}")
        checks_passed = False
    
    return checks_passed

def main():
    graph_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py'
    build_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/build_repair_09.txt'
    requeue_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/requeue_from_repair.txt'
    generated_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/generated_bad_edges.txt'
    
    # Get test mode from args
    test_mode = '--test' in sys.argv
    batch_size = 20 if test_mode else None
    
    print("Parsing unknown nodes from build output...")
    unknown_nodes = parse_unknown_nodes_from_build(build_path)
    print(f"Found {len(unknown_nodes)} unique unknown node names")
    
    print("\nReading and parsing graph_def.py...")
    with open(graph_path, 'r') as f:
        source_code = f.read()
        source_lines = source_code.split('\n')
    
    print("Finding bad e() calls...")
    bad_calls, generated_calls = find_bad_e_calls(source_code, unknown_nodes)
    print(f"Found {len(bad_calls)} top-level e() calls with unknown endpoints")
    print(f"Found {len(generated_calls)} generated e() calls (will be listed separately)")
    
    if test_mode:
        print(f"\n*** TEST MODE: Processing first {batch_size} calls only ***")
        bad_calls = bad_calls[:batch_size]
    
    print(f"\nDeleting {len(bad_calls)} e() calls...")
    new_source_lines = delete_lines_precisely(source_lines, bad_calls)
    new_source = '\n'.join(new_source_lines)
    
    print("\nRunning invariant checks...")
    if not invariant_checks(source_code, new_source, len(bad_calls)):
        print("\n✗✗✗ INVARIANT CHECKS FAILED - NOT writing file ✗✗✗")
        return 1
    
    print("\nWriting updated graph_def.py...")
    with open(graph_path, 'w') as f:
        f.write(new_source)
    
    print(f"\nAppending {len(bad_calls)} entries to requeue file...")
    with open(requeue_path, 'a') as f:
        for call_info in bad_calls:
            evidence = call_info['evidence'].replace('\t', ' ').replace('\n', ' ')
            f.write(f"AUTO\t{call_info['src']}\t{call_info['dst']}\t{call_info['kind']}\t{evidence}\n")
    
    if generated_calls:
        print(f"\nWriting {len(generated_calls)} generated call line numbers to {generated_path}...")
        with open(generated_path, 'w') as f:
            f.write(f"# Generated e() calls with unknown endpoints (from loops/functions)\n")
            f.write(f"# Total: {len(generated_calls)}\n")
            for lineno in sorted(generated_calls):
                f.write(f"Line {lineno}\n")
    
    print("\nDone!")
    return 0

if __name__ == '__main__':
    sys.exit(main())
