#!/usr/bin/env python3
"""Fix regression from cleanup_03: restore valid kinds and evidence labels."""

import ast
import json
import re
import sys

# Load edge IDs from build file
def load_error_edges(build_file):
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

# Parse e() calls from a Python file
def extract_edges(filepath):
    """Extract all e() calls from graph_def.py as {edge_id: {src, dst, kind, evidence, ...}}"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Parse as AST
    tree = ast.parse(content, filepath)
    
    edges = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            # Check if it's e(...)
            if isinstance(node.func, ast.Name) and node.func.id == 'e':
                if len(node.args) >= 4:
                    # e(src, dst, kind, trigger, ...)
                    src = ast.get_source_segment(content, node.args[0]) if node.args[0] else None
                    dst = ast.get_source_segment(content, node.args[1]) if node.args[1] else None
                    kind = ast.get_source_segment(content, node.args[2]) if node.args[2] else None
                    trigger = ast.get_source_segment(content, node.args[3]) if node.args[3] else None
                    
                    # Extract evidence from kwargs
                    evidence = None
                    for keyword in node.keywords:
                        if keyword.arg == 'evidence':
                            evidence = ast.get_source_segment(content, keyword.value)
                            break
                    
                    # Create a key based on (src, dst)
                    if src and dst:
                        # Remove quotes
                        src_clean = src.strip('\'"')
                        dst_clean = dst.strip('\'"')
                        key = (src_clean, dst_clean)
                        
                        edges[key] = {
                            'src': src,
                            'dst': dst,
                            'kind': kind,
                            'trigger': trigger,
                            'evidence': evidence,
                            'node': node,
                            'lineno': node.lineno
                        }
    
    return edges, content

# Generate edge ID from src/dst
def compute_edge_id(src, dst):
    """Compute edge ID similar to build_graph.py"""
    import hashlib
    src_clean = src.strip('\'"').strip('@').split('@')[0]
    dst_clean = dst.strip('\'"').strip('@').split('@')[0]
    h = hashlib.sha256(f"{src_clean}->{dst_clean}".encode()).hexdigest()
    return f"E{h[:8]}"

def main():
    build_file = 'build_finish_00.txt'
    current_file = '../graph_def.py'
    backup_file = 'graph_def_before_cleanup_03.py'
    
    print("Loading error edges from build file...")
    bad_kinds, missing_evidence = load_error_edges(build_file)
    print(f"Found {len(bad_kinds)} bad kind errors, {len(missing_evidence)} missing evidence errors")
    
    print("\nExtracting edges from current graph_def.py...")
    current_edges, current_content = extract_edges(current_file)
    print(f"Found {len(current_edges)} edges in current file")
    
    print("\nExtracting edges from backup (graph_def_before_cleanup_03.py)...")
    backup_edges, backup_content = extract_edges(backup_file)
    print(f"Found {len(backup_edges)} edges in backup file")
    
    # Now match edges by edge ID
    # We need to load the JSON output to get actual edge IDs
    print("\nLoading edge mapping from trigger graph JSON...")
    try:
        with open('../out/amazefilemanager_trigger_graph.json', 'r') as f:
            graph_json = json.load(f)
        
        # Build mapping: edge_id -> (src, dst)
        edge_id_map = {}
        for edge in graph_json.get('edges', []):
            eid = edge['id']
            src = edge['src']
            dst = edge['dst']
            edge_id_map[eid] = (src, dst)
        
        print(f"Loaded {len(edge_id_map)} edges from JSON")
        
        # Map bad_kinds and missing_evidence to (src, dst) pairs
        bad_kind_pairs = [(edge_id_map[eid]) for eid in bad_kinds if eid in edge_id_map]
        missing_ev_pairs = [(edge_id_map[eid]) for eid in missing_evidence if eid in edge_id_map]
        
        print(f"\nMapped {len(bad_kind_pairs)} bad kind edges to (src,dst) pairs")
        print(f"Mapped {len(missing_ev_pairs)} missing evidence edges to (src,dst) pairs")
        
        # Create fix recommendations
        fixes = []
        
        for src, dst in bad_kind_pairs:
            # Clean src/dst
            src_clean = src.split('@')[0]
            dst_clean = dst.split('@')[0]
            key = (src_clean, dst_clean)
            
            if key in backup_edges:
                backup_kind = backup_edges[key]['kind']
                fixes.append({
                    'type': 'bad_kind',
                    'src': src,
                    'dst': dst,
                    'fix_kind': backup_kind,
                    'backup_evidence': backup_edges[key].get('evidence')
                })
        
        for src, dst in missing_ev_pairs:
            src_clean = src.split('@')[0]
            dst_clean = dst.split('@')[0]
            key = (src_clean, dst_clean)
            
            if key in backup_edges:
                backup_evidence = backup_edges[key].get('evidence')
                if backup_evidence:
                    fixes.append({
                        'type': 'missing_evidence',
                        'src': src,
                        'dst': dst,
                        'fix_evidence': backup_evidence
                    })
        
        # Write fixes to JSON for the repair script
        with open('regression_fixes.json', 'w') as f:
            json.dump(fixes, f, indent=2)
        
        print(f"\nGenerated {len(fixes)} fixes")
        print("Fixes written to regression_fixes.json")
        
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        print("Run build_graph.py first to generate the JSON output")
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
