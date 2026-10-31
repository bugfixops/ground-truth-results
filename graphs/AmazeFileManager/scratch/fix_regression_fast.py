#!/usr/bin/env python3
"""Fix regression from cleanup_03: restore valid kinds and evidence labels using regex."""

import json
import re
import hashlib

def load_error_edge_ids(build_file):
    """Extract edge IDs with bad kinds and missing evidence."""
    bad_kinds = set()
    missing_evidence = set()
    with open(build_file, 'r') as f:
        for line in f:
            if 'bad kind LAMBDA' in line or 'bad kind CALLBACK' in line:
                match = re.search(r'ERROR (E[a-f0-9]+):', line)
                if match:
                    bad_kinds.add(match.group(1))
            elif 'missing/invalid evidence label' in line:
                match = re.search(r'ERROR (E[a-f0-9]+):', line)
                if match:
                    missing_evidence.add(match.group(1))
    return bad_kinds, missing_evidence

def extract_e_calls_regex(filepath):
    """Extract e() calls using regex - returns list of (lineno, src, dst, kind, evidence_str)"""
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    edges = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Look for e(
        if re.match(r"^\s*e\s*\(", line):
            # Multi-line call - collect until we find the closing paren
            full_call = line
            depth = line.count('(') - line.count(')')
            j = i + 1
            while depth > 0 and j < len(lines):
                full_call += lines[j]
                depth += lines[j].count('(') - lines[j].count(')')
                j += 1
            
            # Parse the call
            match = re.match(r"\s*e\s*\(\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,", full_call, re.DOTALL)
            if match:
                src = match.group(1).strip().strip('\'"')
                dst = match.group(2).strip().strip('\'"')
                kind = match.group(3).strip().strip('\'"')
                
                # Extract evidence
                evidence_match = re.search(r"evidence\s*=\s*(.+?)(?:,\s*\w+\s*=|\))", full_call, re.DOTALL)
                evidence = evidence_match.group(1).strip() if evidence_match else None
                
                edges.append((i + 1, src, dst, kind, evidence, full_call))
            
            i = j
        else:
            i += 1
    
    return edges

def main():
    build_file = 'build_finish_00.txt'
    current_file = '../graph_def.py'
    backup_file = 'graph_def_before_cleanup_03.py'
    
    print("Loading error edge IDs from build file...")
    bad_kinds, missing_evidence = load_error_edge_ids(build_file)
    print(f"Found {len(bad_kinds)} bad kind edge IDs, {len(missing_evidence)} missing evidence edge IDs")
    
    # Load JSON to map edge IDs to (src, dst)
    print("\nLoading edge mapping from trigger graph JSON...")
    with open('../out/amazefilemanager_trigger_graph.json', 'r') as f:
        graph_json = json.load(f)
    
    edge_id_to_srcdst = {}
    for edge in graph_json.get('edges', []):
        eid = edge['id']
        src = edge['src'].split('@')[0]  # Remove context suffixes
        dst = edge['dst'].split('@')[0]
        edge_id_to_srcdst[eid] = (src, dst)
    
    print(f"Loaded {len(edge_id_to_srcdst)} edges from JSON")
    
    # Map bad_kinds and missing_evidence to (src, dst) pairs
    bad_kind_pairs = set()
    for eid in bad_kinds:
        if eid in edge_id_to_srcdst:
            bad_kind_pairs.add(edge_id_to_srcdst[eid])
    
    missing_ev_pairs = set()
    for eid in missing_evidence:
        if eid in edge_id_to_srcdst:
            missing_ev_pairs.add(edge_id_to_srcdst[eid])
    
    print(f"\nMapped {len(bad_kind_pairs)} bad kind edges to (src,dst) pairs")
    print(f"Mapped {len(missing_ev_pairs)} missing evidence edges to (src,dst) pairs")
    
    # Extract edges from backup file
    print("\nExtracting edges from backup file...")
    backup_edges = extract_e_calls_regex(backup_file)
    print(f"Found {len(backup_edges)} edges in backup")
    
    # Build backup lookup: (src, dst) -> (kind, evidence)
    backup_lookup = {}
    for lineno, src, dst, kind, evidence, full_call in backup_edges:
        backup_lookup[(src, dst)] = (kind, evidence)
    
    # Extract edges from current file
    print("\nExtracting edges from current file...")
    current_edges = extract_e_calls_regex(current_file)
    print(f"Found {len(current_edges)} edges in current file")
    
    # Generate fixes
    fixes = []
    
    for lineno, src, dst, kind, evidence, full_call in current_edges:
        key = (src, dst)
        
        needs_kind_fix = key in bad_kind_pairs
        needs_evidence_fix = key in missing_ev_pairs
        
        if needs_kind_fix or needs_evidence_fix:
            if key in backup_lookup:
                backup_kind, backup_evidence = backup_lookup[key]
                fixes.append({
                    'lineno': lineno,
                    'src': src,
                    'dst': dst,
                    'current_kind': kind,
                    'current_evidence': evidence,
                    'fix_kind': backup_kind if needs_kind_fix else None,
                    'fix_evidence': backup_evidence if needs_evidence_fix else None,
                    'full_call': full_call
                })
            else:
                # No backup found - log it
                print(f"WARNING: No backup found for edge {src} -> {dst} at line {lineno}")
                fixes.append({
                    'lineno': lineno,
                    'src': src,
                    'dst': dst,
                    'current_kind': kind,
                    'current_evidence': evidence,
                    'fix_kind': None,
                    'fix_evidence': None,
                    'full_call': full_call,
                    'warning': 'NO_BACKUP_FOUND'
                })
    
    # Write fixes to JSON
    with open('regression_fixes.json', 'w') as f:
        json.dump(fixes, f, indent=2)
    
    print(f"\nGenerated {len(fixes)} fixes")
    print("Fixes written to regression_fixes.json")
    
    # Print summary
    kind_fixes = sum(1 for f in fixes if f.get('fix_kind'))
    evidence_fixes = sum(1 for f in fixes if f.get('fix_evidence'))
    no_backup = sum(1 for f in fixes if f.get('warning') == 'NO_BACKUP_FOUND')
    
    print(f"\nSummary:")
    print(f"  {kind_fixes} kind fixes")
    print(f"  {evidence_fixes} evidence fixes")
    print(f"  {no_backup} edges with no backup found")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
