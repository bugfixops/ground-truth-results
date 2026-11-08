#!/usr/bin/env python3
"""
Check which unknown nodes exist in method_list.json.
"""

import json

# Read unknown nodes
with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/unknown_nodes.txt', 'r') as f:
    unknown_nodes = [line.strip() for line in f if line.strip()]

# Read method_list.json
with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/method_list.json', 'r') as f:
    method_list = json.load(f)

# Build a set of method names for fast lookup
method_names = set(m['short'] for m in method_list)

# Check each unknown node
exists = []
not_exists = []

for node in unknown_nodes:
    if node in method_names:
        exists.append(node)
    else:
        not_exists.append(node)

print(f"Unknown nodes that EXIST in method_list.json: {len(exists)}")
for node in exists[:20]:
    print(f"  {node}")
if len(exists) > 20:
    print(f"  ... and {len(exists) - 20} more")

print(f"\nUnknown nodes that DO NOT EXIST in method_list.json: {len(not_exists)}")
for node in not_exists[:20]:
    print(f"  {node}")
if len(not_exists) > 20:
    print(f"  ... and {len(not_exists) - 20} more")

# Save the lists
with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/unknown_exists.txt', 'w') as f:
    f.write('\n'.join(exists))

with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/unknown_not_exists.txt', 'w') as f:
    f.write('\n'.join(not_exists))

print(f"\nSaved exists to unknown_exists.txt ({len(exists)} methods)")
print(f"Saved not_exists to unknown_not_exists.txt ({len(not_exists)} methods)")
