#!/usr/bin/env python3
"""
Analyze UNREACHABLE methods with incoming edges.
For each, check if incoming edges come from REACHABLE or UNREACHABLE sources.
"""

import json
import re
import sys

# Load trigger graph
print("Loading trigger graph...")
with open('graphs/AmazeFileManager/out/amazefilemanager_trigger_graph.json') as f:
    graph = json.load(f)

edges_by_id = {e['id']: e for e in graph['edges']}

# Load method verdicts
print("Loading method verdicts...")
methods = {}
for m in graph['methods']:
    methods[m] = {'verdict': 'UNKNOWN'}

# Parse build output for verdicts
print("Parsing build output...")
with open('graphs/AmazeFileManager/scratch/build_cleanup_02.txt') as f:
    content = f.read()
    
# Extract REACHABLE count
match = re.search(r'REACHABLE (\d+)', content)
if match:
    reachable_count = int(match.group(1))
    print(f"REACHABLE methods: {reachable_count}")

# Parse warnings
print("\nParsing warnings...")
warnings = []
with open('graphs/AmazeFileManager/scratch/unreachable_warnings.txt') as f:
    for line in f:
        match = re.search(r'(\S+) is UNREACHABLE but has incoming edges \[(.*?)\]', line)
        if match:
            method = match.group(1)
            edge_ids = [e.strip("' ") for e in match.group(2).split(',')]
            warnings.append((method, edge_ids))

print(f"Total warnings: {len(warnings)}")

# Analyze each warning
print("\nAnalyzing incoming edges...")
output_lines = []
for method, edge_ids in warnings:
    incoming_sources = []
    for edge_id in edge_ids:
        if edge_id in edges_by_id:
            edge = edges_by_id[edge_id]
            src = edge['src']
            incoming_sources.append(src)
    
    output_lines.append(f"{method}\t{len(edge_ids)}\t{';'.join(incoming_sources[:5])}")

# Save to file
print("\nSaving analysis...")
with open('graphs/AmazeFileManager/scratch/unreachable_analysis.txt', 'w') as f:
    f.write("METHOD\tEDGE_COUNT\tFIRST_5_SOURCES\n")
    for line in output_lines:
        f.write(line + '\n')

print(f"Saved analysis to unreachable_analysis.txt")
print(f"Total methods to check: {len(warnings)}")
