#!/usr/bin/env python3
"""Apply fixes to graph_def.py by comparing with backup."""

import re
import json
import ast

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

def main():
    build_file = 'build_finish_00.txt'
    current_file = '../graph_def.py'
    backup_file = 'graph_def_before_cleanup_03.py'
    output_file = '../graph_def.py.fixed'
    
    print("Loading error edge IDs...")
    bad_kinds, missing_evidence = load_error_edge_ids(build_file)
    print(f"Found {len(bad_kinds)} bad kind edge IDs, {len(missing_evidence)} missing evidence edge IDs")
    
    # Load JSON to map edge IDs to (src, dst)
    print("\nLoading edge mapping from JSON...")
    with open('../out/amazefilemanager_trigger_graph.json', 'r') as f:
        graph_json = json.load(f)
    
    edge_id_to_info = {}
    for edge in graph_json.get('edges', []):
        eid = edge['id']
        src = edge['src']
        dst = edge['dst']
        kind = edge.get('kind', '')
        edge_id_to_info[eid] = {'src': src, 'dst': dst, 'kind': kind}
    
    print(f"Loaded {len(edge_id_to_info)} edges from JSON")
    
    # Collect edges to fix: {(src, dst): {'needs_kind': bool, 'needs_evidence': bool, 'current_kind': str}}
    edges_to_fix = {}
    for eid in bad_kinds:
        if eid in edge_id_to_info:
            info = edge_id_to_info[eid]
            key = (info['src'], info['dst'])
            if key not in edges_to_fix:
                edges_to_fix[key] = {'needs_kind': False, 'needs_evidence': False, 'current_kind': info['kind']}
            edges_to_fix[key]['needs_kind'] = True
    
    for eid in missing_evidence:
        if eid in edge_id_to_info:
            info = edge_id_to_info[eid]
            key = (info['src'], info['dst'])
            if key not in edges_to_fix:
                edges_to_fix[key] = {'needs_kind': False, 'needs_evidence': False, 'current_kind': info.get('kind', '')}
            edges_to_fix[key]['needs_evidence'] = True
    
    print(f"\nEdges to fix: {len(edges_to_fix)}")
    
    # Load backup file to build lookup table
    print("\nBuilding lookup from backup file...")
    backup_lookup = {}
    with open(backup_file, 'r') as f:
        backup_lines = f.readlines()
    
    i = 0
    while i < len(backup_lines):
        line = backup_lines[i]
        if re.match(r"^\s*e\s*\(", line):
            # Collect multi-line e() call
            full_call = line
            depth = line.count('(') - line.count(')')
            j = i + 1
            while depth > 0 and j < len(backup_lines):
                full_call += backup_lines[j]
                depth += backup_lines[j].count('(') - backup_lines[j].count(')')
                j += 1
            
            # Extract src, dst, kind, evidence
            # e('src', 'dst', 'kind', ...
            match = re.match(r"\s*e\s*\(\s*['\"]([^'\"]+)['\"]\s*,\s*['\"]([^'\"]+)['\"]\s*,\s*['\"]([^'\"]+)['\"]", full_call)
            if match:
                src = match.group(1)
                dst = match.group(2)
                kind = match.group(3)
                
                # Extract evidence
                evidence_match = re.search(r"evidence\s*=\s*(.+?)(?:,\s*\w+\s*=|\)\s*$)", full_call, re.DOTALL)
                evidence = evidence_match.group(1).strip() if evidence_match else None
                
                backup_lookup[(src, dst)] = {'kind': kind, 'evidence': evidence}
            
            i = j
        else:
            i += 1
    
    print(f"Built lookup with {len(backup_lookup)} edges from backup")
    
    # Now process current file
    print("\nProcessing current file...")
    with open(current_file, 'r') as f:
        current_lines = f.readlines()
    
    fixed_lines = []
    fixes_applied = {'kind': 0, 'evidence': 0, 'not_found': 0}
    i = 0
    while i < len(current_lines):
        line = current_lines[i]
        if re.match(r"^\s*e\s*\(", line):
            # Collect multi-line e() call
            start_i = i
            full_call = line
            depth = line.count('(') - line.count(')')
            j = i + 1
            while depth > 0 and j < len(current_lines):
                full_call += current_lines[j]
                depth += current_lines[j].count('(') - current_lines[j].count(')')
                j += 1
            
            # Extract src, dst, kind
            match = re.match(r"\s*e\s*\(\s*['\"]([^'\"]+)['\"]\s*,\s*['\"]([^'\"]+)['\"]\s*,\s*['\"]([^'\"]+)['\"]", full_call)
            if match:
                src = match.group(1)
                dst = match.group(2)
                current_kind = match.group(3)
                
                key = (src, dst)
                if key in edges_to_fix:
                    # This edge needs fixing
                    fix_info = edges_to_fix[key]
                    if key in backup_lookup:
                        backup_info = backup_lookup[key]
                        
                        # Fix kind
                        if fix_info['needs_kind'] and backup_info['kind']:
                            full_call = full_call.replace(f"'{current_kind}'", f"'{backup_info['kind']}'", 1)
                            full_call = full_call.replace(f'"{current_kind}"', f'"{backup_info["kind"]}"', 1)
                            fixes_applied['kind'] += 1
                        
                        # Fix evidence
                        if fix_info['needs_evidence'] and backup_info['evidence']:
                            # Check if evidence exists
                            if 'evidence=' in full_call:
                                # Replace existing evidence
                                full_call = re.sub(r"evidence\s*=\s*(.+?)(?=,\s*\w+\s*=|\))", 
                                                   f"evidence={backup_info['evidence']}", full_call, count=1)
                            else:
                                # Add evidence before the closing paren
                                full_call = re.sub(r"(\))\s*$", f", evidence={backup_info['evidence']}\\1", full_call, flags=re.MULTILINE)
                            fixes_applied['evidence'] += 1
                    else:
                        fixes_applied['not_found'] += 1
                        print(f"WARNING: No backup for {src} -> {dst}")
            
            fixed_lines.append(full_call)
            i = j
        else:
            fixed_lines.append(line)
            i += 1
    
    # Write output
    with open(output_file, 'w') as f:
        f.writelines(fixed_lines)
    
    print(f"\nFixes applied:")
    print(f"  Kind fixes: {fixes_applied['kind']}")
    print(f"  Evidence fixes: {fixes_applied['evidence']}")
    print(f"  Not found in backup: {fixes_applied['not_found']}")
    print(f"\nFixed file written to {output_file}")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
