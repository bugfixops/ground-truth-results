#!/usr/bin/env python3
"""
Fix UNREACHABLE-with-incoming-edges warnings.
Strategy:
1. Load graph to determine which methods are REACHABLE
2. For each UNREACHABLE method with incoming edges:
   - Check if ANY incoming edge comes from a REACHABLE source
   - If yes → need to verify edge from source, then DELETE UNREACHABLE entry
   - If no (all from UNREACHABLE) → KEEP UNREACHABLE, log reason
3. Generate report for human review and edits to apply
"""

import json
import re
import ast
import subprocess

# Load trigger graph  
print("Loading trigger graph...")
with open('graphs/AmazeFileManager/out/amazefilemanager_trigger_graph.json') as f:
    graph = json.load(f)

edges_by_id = {e['id']: e for e in graph['edges']}

# Load graph_def.py to determine REACHABLE status
print("Parsing graph_def.py...")
with open('graphs/AmazeFileManager/graph_def.py', 'r') as f:
    graph_def_content = f.read()

# Extract UNREACHABLE dict (all explicitly marked methods)
unreachable_methods = set()
for match in re.finditer(r"UNREACHABLE\['([^']+)'\]\s*=", graph_def_content):
    unreachable_methods.add(match.group(1))

print(f"Found {len(unreachable_methods)} explicitly UNREACHABLE methods")

# All methods in graph
all_methods = set(graph['methods'])

# Methods with edges are potentially REACHABLE
methods_with_incoming = set()
for edge in graph['edges']:
    methods_with_incoming.add(edge['dst'])

# REACHABLE = methods that are NOT in UNREACHABLE dict
# (Note: some UNRESOLVED methods may also be in this set, but they're not our concern here)
potentially_reachable = methods_with_incoming - unreachable_methods

print(f"Total methods: {len(all_methods)}")
print(f"Methods with incoming edges: {len(methods_with_incoming)}")
print(f"Potentially REACHABLE (have edges, not in UNREACHABLE): {len(potentially_reachable)}")

# Parse warnings
warnings = []
with open('graphs/AmazeFileManager/scratch/unreachable_warnings.txt') as f:
    for line in f:
        match = re.search(r'(\S+) is UNREACHABLE but has incoming edges \[(.*?)\]', line)
        if match:
            method = match.group(1)
            edge_ids = [e.strip("' ") for e in match.group(2).split(',')]
            warnings.append((method, edge_ids))

print(f"\nProcessing {len(warnings)} warnings...")

# Analyze each
to_delete = []  # UNREACHABLE entries to delete (method becomes REACHABLE)
to_keep = []     # UNREACHABLE entries to keep (all sources unreachable)
to_review = []   # Needs manual inspection

for method, edge_ids in warnings:
    # Get incoming edges
    incoming = []
    for eid in edge_ids:
        if eid in edges_by_id:
            edge = edges_by_id[eid]
            src = edge['src']
            # Is source REACHABLE?
            src_reachable = (src in potentially_reachable)
            incoming.append({
                'id': eid,
                'src': src,
                'src_reachable': src_reachable,
                'kind': edge.get('kind', ''),
                'evidence': edge.get('evidence', '')[:100]  # Truncate
            })
    
    # Decision logic
    has_reachable_source = any(e['src_reachable'] for e in incoming)
    
    if has_reachable_source:
        # At least one incoming edge from REACHABLE → candidate for deletion
        # BUT needs source verification
        reachable_sources = [e for e in incoming if e['src_reachable']]
        to_delete.append({
            'method': method,
            'reason': 'Has incoming edges from REACHABLE sources',
            'reachable_sources': [e['src'] for e in reachable_sources],
            'edge_count': len(edge_ids),
            'sample_evidence': reachable_sources[0]['evidence'] if reachable_sources else ''
        })
    else:
        # All sources are UNREACHABLE → keep the UNREACHABLE entry
        to_keep.append({
            'method': method,
            'reason': 'All incoming edges from UNREACHABLE sources',
            'source_count': len(set(e['src'] for e in incoming)),
            'edge_count': len(edge_ids)
        })

# Save results
print(f"\nResults:")
print(f"  To DELETE (become REACHABLE): {len(to_delete)}")
print(f"  To KEEP (stay UNREACHABLE): {len(to_keep)}")

with open('graphs/AmazeFileManager/scratch/unreachable_to_delete.json', 'w') as f:
    json.dump(to_delete, f, indent=2)

with open('graphs/AmazeFileManager/scratch/unreachable_to_keep.json', 'w') as f:
    json.dump(to_keep, f, indent=2)

# Generate human-readable report
with open('graphs/AmazeFileManager/scratch/unreachable_fix_report.txt', 'w') as f:
    f.write("UNREACHABLE WARNING FIX REPORT\n")
    f.write("=" * 80 + "\n\n")
    
    f.write(f"PART 1: DELETE UNREACHABLE ENTRIES ({len(to_delete)} methods)\n")
    f.write("-" * 80 + "\n")
    f.write("These methods have incoming edges from REACHABLE sources.\n")
    f.write("Action: Delete UNREACHABLE entry (method becomes REACHABLE)\n\n")
    
    for item in to_delete:
        f.write(f"Method: {item['method']}\n")
        f.write(f"  Edges: {item['edge_count']}\n")
        f.write(f"  REACHABLE sources: {', '.join(item['reachable_sources'][:5])}\n")
        if len(item['reachable_sources']) > 5:
            f.write(f"    ... and {len(item['reachable_sources']) - 5} more\n")
        f.write(f"  Sample evidence: {item['sample_evidence']}\n")
        f.write("\n")
    
    f.write("\n" + "=" * 80 + "\n\n")
    f.write(f"PART 2: KEEP UNREACHABLE ENTRIES ({len(to_keep)} methods)\n")
    f.write("-" * 80 + "\n")
    f.write("These methods only have incoming edges from UNREACHABLE sources.\n")
    f.write("Action: Keep UNREACHABLE entry, update reason if needed\n\n")
    
    for item in to_keep:
        f.write(f"Method: {item['method']}\n")
        f.write(f"  Edges: {item['edge_count']} from {item['source_count']} UNREACHABLE sources\n")
        f.write("\n")

print(f"\nSaved reports to:")
print(f"  unreachable_to_delete.json")
print(f"  unreachable_to_keep.json")
print(f"  unreachable_fix_report.txt")
