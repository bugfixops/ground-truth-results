#!/usr/bin/env python3
"""
Print context for edge repair proposals - Helper 1.
For each edge ID, extract the e(...) definition from graph_def.py and print cited source lines.
"""

import json
import re
import subprocess
import sys

APP_SRC = "/Users/darshan/Desktop/yang/work/final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java"
GRAPH_DEF = "/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py"
METHOD_LIST = "/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/method_list.json"

# Load method_list for parameter lookups
with open(METHOD_LIST) as f:
    methods = json.load(f)

# Load grouped edges to get all edge IDs we need to check
with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/repair_proposals/helper1_grouped.json') as f:
    grouped = json.load(f)

# Extract all unique edge IDs (strip -2, -3 suffixes for lookup)
edge_ids = set()
for name, edges in grouped.items():
    for eid, side in edges:
        base_eid = eid.split('-')[0]  # E99ef4327-2 -> E99ef4327
        edge_ids.add(base_eid)

print(f"Checking {len(edge_ids)} unique edge IDs")

# Read graph_def.py
with open(GRAPH_DEF) as f:
    graph_def_content = f.read()

# For each bad name, collect edges and print context
edge_defs_found = {}
edge_defs_not_found = []

for bad_name in sorted(grouped.keys()):
    print(f"\n{'='*80}")
    print(f"BAD NAME: {bad_name}")
    print(f"{'='*80}")
    
    edges = grouped[bad_name]
    print(f"Edge references: {len(edges)}")
    
    # Check if any edge definitions exist in graph_def.py
    edges_found = []
    edges_missing = []
    
    for eid, side in edges:
        base_eid = eid.split('-')[0]
        
        # Search for edge definition in graph_def.py
        # Pattern: e('..., '..., id='E...'
        pattern = rf"e\([^)]*\bid=['\"]?{re.escape(base_eid)}['\"]?"
        match = re.search(pattern, graph_def_content)
        
        if match:
            # Extract the full e(...) call
            start = match.start()
            # Find the closing parenthesis (balanced)
            depth = 0
            pos = start
            while pos < len(graph_def_content):
                if graph_def_content[pos] == '(':
                    depth += 1
                elif graph_def_content[pos] == ')':
                    depth -= 1
                    if depth == 0:
                        break
                pos += 1
            
            if depth == 0:
                edge_def = graph_def_content[start:pos+1]
                edges_found.append((eid, side, base_eid, edge_def))
        else:
            edges_missing.append((eid, side, base_eid))
    
    if edges_found:
        print(f"\nFound {len(edges_found)} edge definitions in graph_def.py:")
        for eid, side, base_eid, edge_def in edges_found[:3]:  # Show first 3
            print(f"\n  Edge {eid} ({side}):")
            # Extract key parts
            lines = edge_def.split('\n')
            for line in lines[:5]:  # First 5 lines
                print(f"    {line}")
            if len(lines) > 5:
                print(f"    ... ({len(lines)-5} more lines)")
    
    if edges_missing:
        print(f"\nNOT FOUND in graph_def.py: {len(edges_missing)} edges")
        for eid, side, base_eid in edges_missing[:5]:
            print(f"  {eid} ({side}) - base: {base_eid}")
    
    # Look up canonical candidates for this bad name
    # Strip full package path if present
    simple_name = bad_name.split('.')[-1] if '.' in bad_name else bad_name
    
    # Search in method_list for potential matches
    candidates = []
    for m in methods:
        if simple_name in m['name'] or simple_name in m['short']:
            candidates.append(m['short'])
    
    if candidates:
        print(f"\nCanonical candidates from method_list.json ({len(candidates)}):")
        for c in candidates[:10]:
            print(f"  - {c}")

print(f"\n{'='*80}")
print(f"SUMMARY")
print(f"{'='*80}")
print(f"Total bad names: {len(grouped)}")
print(f"Edges found in graph_def.py: {len([e for edges in edge_defs_found.values() for e in edges])}")
print(f"Edges NOT in graph_def.py: {sum(len(grouped[name]) for name in grouped.keys())}")
