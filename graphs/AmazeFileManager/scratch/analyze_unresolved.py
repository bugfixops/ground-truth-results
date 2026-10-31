#!/usr/bin/env python3
"""
Analyze unresolved methods to split into:
(a) methods with NO incoming edge at all (truly unlabeled)
(b) methods whose incoming edges all come from unreachable/unresolved sources (chain-blocked)
"""

import sys
import json
import re

G = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager'

# Read the build file to get unresolved methods
unresolved = set()
with open(f'{G}/scratch/unresolved_methods_step5.txt', 'r') as f:
    for line in f:
        # ERROR method has no path and no UNREACHABLE entry: ClassName.methodName
        match = re.search(r'ERROR method has no path and no UNREACHABLE entry: (.+)', line)
        if match:
            unresolved.add(match.group(1))

print(f"Total unresolved methods: {len(unresolved)}")

# Read graph JSON to find incoming edges
graph_json_path = f'{G}/out/amazefilemanager_trigger_graph.json'
with open(graph_json_path, 'r') as f:
    graph_data = json.load(f)

# Build incoming edge map
incoming = {}  # method -> list of (source_method, edge_id)
for edge in graph_data.get('edges', []):
    dst = edge.get('dst')
    src = edge.get('src')
    eid = edge.get('id')
    if dst:
        if dst not in incoming:
            incoming[dst] = []
        incoming[dst].append((src, eid))

# Read verdicts from graph JSON
verdicts = {}  # method -> verdict (REACHABLE, UNREACHABLE, UNRESOLVED)
for node in graph_data.get('nodes', []):
    method = node.get('id')
    verdict = node.get('verdict', 'UNRESOLVED')
    verdicts[method] = verdict

# Categorize unresolved methods
no_incoming = []  # (a) truly unlabeled
chain_blocked = []  # (b) all incoming from unreachable/unresolved

for method in sorted(unresolved):
    if method not in incoming or len(incoming[method]) == 0:
        no_incoming.append(method)
    else:
        # Check if all incoming edges are from UNREACHABLE or UNRESOLVED sources
        all_blocked = True
        blocker_sources = []
        for src, eid in incoming[method]:
            src_verdict = verdicts.get(src, 'UNRESOLVED')
            if src_verdict == 'REACHABLE':
                all_blocked = False
                break
            else:
                blocker_sources.append((src, src_verdict))
        
        if all_blocked:
            chain_blocked.append((method, blocker_sources))
        else:
            # This shouldn't happen for methods with "no path" error
            print(f"WARNING: {method} has REACHABLE incoming but still unresolved")
            no_incoming.append(method)  # Treat as truly unlabeled

print(f"\n(a) Methods with NO incoming edge: {len(no_incoming)}")
print(f"(b) Methods chain-blocked by unreachable/unresolved sources: {len(chain_blocked)}")
print(f"Total: {len(no_incoming) + len(chain_blocked)}")

# Save results
with open(f'{G}/scratch/unresolved_split_a.txt', 'w') as f:
    for method in no_incoming:
        f.write(f"{method}\n")

with open(f'{G}/scratch/unresolved_split_b.txt', 'w') as f:
    for method, blockers in chain_blocked:
        f.write(f"{method}\n")

# Group chain-blocked by their nearest blocker
blocker_groups = {}  # blocker -> list of blocked methods
for method, blocker_sources in chain_blocked:
    # Find the nearest unlabeled/unrouted upstream method
    for src, verdict in blocker_sources:
        if src in unresolved:
            # This is a direct blocker
            if src not in blocker_groups:
                blocker_groups[src] = []
            blocker_groups[src].append(method)
            break
    else:
        # No direct blocker found, use first source
        if blocker_sources:
            src, verdict = blocker_sources[0]
            if src not in blocker_groups:
                blocker_groups[src] = []
            blocker_groups[src].append(method)

# Sort by number of methods unblocked
sorted_blockers = sorted(blocker_groups.items(), key=lambda x: len(x[1]), reverse=True)

with open(f'{G}/scratch/unresolved_blockers.txt', 'w') as f:
    f.write(f"# Chain-blocked methods grouped by blocker\n")
    f.write(f"# Format: blocker_method -> count of blocked methods\n\n")
    for blocker, blocked in sorted_blockers:
        f.write(f"\n{blocker} -> {len(blocked)} methods\n")
        for method in sorted(blocked):
            f.write(f"  {method}\n")

print(f"\nSaved:")
print(f"  {G}/scratch/unresolved_split_a.txt")
print(f"  {G}/scratch/unresolved_split_b.txt")
print(f"  {G}/scratch/unresolved_blockers.txt")
