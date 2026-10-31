#!/usr/bin/env python3
"""Fix regression by restoring entire e() calls from backup for problematic edges."""

import re
import json

def load_error_edge_ids(build_file):
    """Extract edge IDs with bad kinds and missing evidence."""
    bad_kinds = []
    missing_evidence = []
    with open(build_file, 'r') as f:
        for line in f:
            if 'bad kind LAMBDA' in line or 'bad kind CALLBACK' in line:
                match = re.search(r'ERROR (E[a-f0-9]+):', line)
                if match:
                    bad_kinds.append(match.group(1))
            elif 'missing/invalid evidence label' in line:
                match = re.search(r'ERROR (E[a-f0-9]+):', line)
                if match:
                    missing_evidence.append(match.group(1))
    return bad_kinds, missing_evidence

def extract_e_calls(content):
    """Extract all e() calls with their line ranges. Returns dict: (src, dst) -> (start_line, end_line, text)"""
    lines = content.split('\n')
    edges = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"^\s*e\s*\(", line):
            start_line = i
            # Collect multi-line e() call
            full_call = line
            depth = line.count('(') - line.count(')')
            j = i + 1
            while depth > 0 and j < len(lines):
                full_call += '\n' + lines[j]
                depth += lines[j].count('(') - lines[j].count(')')
                j += 1
            end_line = j - 1
            
            # Extract src, dst
            match = re.match(r"\s*e\s*\(\s*(['\"])([^'\"]+)\1\s*,\s*(['\"])([^'\"]+)\3", full_call)
            if match:
                src = match.group(2)
                dst = match.group(4)
                edges[(src, dst)] = (start_line, end_line, full_call)
            
            i = j
        else:
            i += 1
    
    return edges

def main():
    build_file = 'build_finish_00.txt'
    current_file = '../graph_def.py'
    backup_file = 'graph_def_before_cleanup_03.py'
    output_file = '../graph_def.py.fixed_clean'
    
    print("Loading error edge IDs...")
    bad_kinds, missing_evidence = load_error_edge_ids(build_file)
    print(f"Found {len(bad_kinds)} bad kind edge IDs, {len(missing_evidence)} missing evidence edge IDs")
    
    # Load JSON to map edge IDs to (src, dst)
    print("\nLoading edge mapping from JSON...")
    with open('../out/amazefilemanager_trigger_graph.json', 'r') as f:
        graph_json = json.load(f)
    
    edges_to_fix = set()
    for eid in bad_kinds + missing_evidence:
        for edge in graph_json.get('edges', []):
            if edge['id'] == eid:
                src = edge['src']
                dst = edge['dst']
                edges_to_fix.add((src, dst))
                break
    
    print(f"Edges to fix: {len(edges_to_fix)}")
    
    # Load backup and current files
    print("\nExtracting edges from backup...")
    with open(backup_file, 'r') as f:
        backup_content = f.read()
    backup_edges = extract_e_calls(backup_content)
    print(f"Found {len(backup_edges)} edges in backup")
    
    print("\nExtracting edges from current file...")
    with open(current_file, 'r') as f:
        current_content = f.read()
    current_edges = extract_e_calls(current_content)
    print(f"Found {len(current_edges)} edges in current file")
    
    # Build replacement map: line_range in current -> replacement text from backup
    current_lines = current_content.split('\n')
    lines_to_replace = {}  # start_line -> (end_line, replacement_text)
    
    fixed = 0
    not_found = 0
    for key in edges_to_fix:
        if key in backup_edges and key in current_edges:
            backup_text = backup_edges[key][2]
            current_start, current_end, _ = current_edges[key]
            lines_to_replace[current_start] = (current_end, backup_text)
            fixed += 1
            print(f"  Will replace {key[0]} -> {key[1]}")
        elif key not in backup_edges:
            print(f"  WARNING: No backup for {key[0]} -> {key[1]}")
            not_found += 1
        elif key not in current_edges:
            print(f"  WARNING: Not in current file: {key[0]} -> {key[1]}")
            not_found += 1
    
    # Apply replacements
    print("\nApplying replacements...")
    output_lines = []
    i = 0
    while i < len(current_lines):
        if i in lines_to_replace:
            end_line, replacement = lines_to_replace[i]
            output_lines.append(replacement)
            i = end_line + 1
        else:
            output_lines.append(current_lines[i])
            i += 1
    
    # Write output
    with open(output_file, 'w') as f:
        f.write('\n'.join(output_lines))
    
    print(f"\nFixed: {fixed}")
    print(f"Not found: {not_found}")
    print(f"Fixed file written to {output_file}")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
