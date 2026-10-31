#!/usr/bin/env python3
"""Fix missing/invalid evidence labels by restoring from backup."""

import re
import json

def load_error_edge_ids(build_file):
    """Extract edge IDs with missing evidence."""
    missing_evidence = []
    with open(build_file, 'r') as f:
        for line in f:
            if 'missing/invalid evidence label' in line:
                match = re.search(r'ERROR (E[a-f0-9]+):', line)
                if match:
                    missing_evidence.append(match.group(1))
    return missing_evidence

def main():
    build_file = 'build_finish_00.txt'
    input_file = '../graph_def.py.fixed'  # Already has kind fixes
    backup_file = 'graph_def_before_cleanup_03.py'
    output_file = '../graph_def.py.fixed2'
    
    print("Loading error edge IDs...")
    missing_evidence = load_error_edge_ids(build_file)
    print(f"Found {len(missing_evidence)} missing evidence edge IDs")
    
    # Load JSON to map edge IDs to (src, dst)
    print("\nLoading edge mapping from JSON...")
    with open('../out/amazefilemanager_trigger_graph.json', 'r') as f:
        graph_json = json.load(f)
    
    edge_id_to_srcdst = {}
    for edge in graph_json.get('edges', []):
        eid = edge['id']
        src = edge['src']
        dst = edge['dst']
        edge_id_to_srcdst[eid] = (src, dst)
    
    print(f"Loaded {len(edge_id_to_srcdst)} edges from JSON")
    
    # Map missing_evidence to (src, dst) pairs
    missing_ev_pairs = set()
    for eid in missing_evidence:
        if eid in edge_id_to_srcdst:
            missing_ev_pairs.add(edge_id_to_srcdst[eid])
    
    print(f"Mapped {len(missing_ev_pairs)} missing evidence edges to (src,dst) pairs")
    
    # Load backup file and extract evidence for each edge
    print("\nExtracting evidence from backup...")
    with open(backup_file, 'r') as f:
        backup_content = f.read()
    
    backup_evidence = {}
    # Pattern: e('src', 'dst', 'kind', 'trigger', ... evidence='...' ...)
    # Match evidence with either single or double quotes
    pattern = r"e\s*\(\s*(['\"])([^'\"]+)\1\s*,\s*(['\"])([^'\"]+)\3\s*,\s*[^,]+\s*,[^,]+(?:,.*?)?evidence\s*=\s*(['\"])(.+?)\5"
    matches = re.finditer(pattern, backup_content, re.DOTALL)
    
    for match in matches:
        src = match.group(2)
        dst = match.group(4)
        quote_char = match.group(5)
        evidence = match.group(6)
        # Reconstruct full evidence string with quotes
        evidence_str = f"{quote_char}{evidence}{quote_char}"
        # Store with key, only first occurrence
        key = (src, dst)
        if key not in backup_evidence:
            backup_evidence[key] = evidence_str
    
    print(f"Found evidence for {len(backup_evidence)} edges in backup")
    
    # Load input file
    print("\nLoading input file...")
    with open(input_file, 'r') as f:
        input_content = f.read()
    
    # Fix missing evidence
    print("\nFixing missing evidence...")
    fixed_content = input_content
    fixes_applied = 0
    not_found = 0
    no_evidence_in_backup = 0
    
    for src, dst in missing_ev_pairs:
        if (src, dst) in backup_evidence:
            backup_ev = backup_evidence[(src, dst)]
            
            # Find this edge in input_content
            # Pattern: e('src', 'dst', 'kind', 'trigger', ...
            edge_pattern = rf"e\s*\(\s*(['\"]){re.escape(src)}\1\s*,\s*(['\"]){re.escape(dst)}\2\s*,\s*(['\"])([^'\"]+)\3\s*,\s*([^,)]+)(?:,[^)]*?)?\)"
            edge_match = re.search(edge_pattern, fixed_content, re.DOTALL)
            
            if edge_match:
                old_call = edge_match.group(0)
                
                # Check if evidence already exists
                if 'evidence=' in old_call:
                    # Replace existing evidence - match the full evidence value including quotes and any content
                    new_call = re.sub(r"evidence\s*=\s*(['\"])(?:[^'\"\\]|\\.)*?\1", 
                                      f"evidence={backup_ev}", old_call, count=1)
                else:
                    # Add evidence before the closing paren
                    new_call = old_call.rstrip()
                    if new_call.endswith(')'):
                        new_call = new_call[:-1] + f", evidence={backup_ev})"
                
                fixed_content = fixed_content.replace(old_call, new_call, 1)
                fixes_applied += 1
                print(f"  Fixed {src} -> {dst}")
            else:
                print(f"  WARNING: Could not find edge {src} -> {dst} in input file")
                not_found += 1
        else:
            print(f"  WARNING: No evidence in backup for {src} -> {dst}")
            no_evidence_in_backup += 1
    
    # Write output
    with open(output_file, 'w') as f:
        f.write(fixed_content)
    
    print(f"\nFixes applied: {fixes_applied}")
    print(f"Not found in input: {not_found}")
    print(f"No evidence in backup: {no_evidence_in_backup}")
    print(f"Fixed file written to {output_file}")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
