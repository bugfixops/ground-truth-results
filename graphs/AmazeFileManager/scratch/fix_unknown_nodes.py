#!/usr/bin/env python3
"""
Fix unknown node errors by:
1. Commenting out edges that reference methods not in method_list.json
2. Creating a TODO list for methods that exist but need labels
"""

import json
import re

# Read the lists we created
with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/unknown_exists.txt', 'r') as f:
    exists = set(line.strip() for line in f if line.strip())

with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/unknown_not_exists.txt', 'r') as f:
    not_exists = set(line.strip() for line in f if line.strip())

print(f"Methods that exist but need labels: {len(exists)}")
print(f"Methods that don't exist (edges to remove): {len(not_exists)}")

# Read graph_def.py
graph_def_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py'
with open(graph_def_path, 'r') as f:
    lines = f.readlines()

# Process line by line, commenting out edges that reference non-existent methods
output_lines = []
commented_count = 0
edge_pattern = re.compile(r"^\s*e\(")

for i, line in enumerate(lines):
    # Check if this is an edge definition
    if edge_pattern.match(line):
        # Check if any non-existent method is referenced in this line
        should_comment = False
        for method in not_exists:
            # Escape special regex characters in method name
            escaped = re.escape(method)
            # Look for the method name in quotes
            if re.search(rf"['\"]" + escaped + rf"['\"]", line):
                should_comment = True
                break
        
        if should_comment:
            output_lines.append("# REMOVED (unknown node): " + line)
            commented_count += 1
        else:
            output_lines.append(line)
    else:
        output_lines.append(line)

print(f"\nCommented out {commented_count} edges referencing non-existent methods")

# Write back
with open(graph_def_path, 'w') as f:
    f.writelines(output_lines)

# Write TODO list for methods that exist
todo_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/nodes_need_labels.txt'
with open(todo_path, 'w') as f:
    f.write("# These 40 methods exist in method_list.json but have no label in graph_def.py\n")
    f.write("# They need either:\n")
    f.write("#   - REACHABLE edges\n")
    f.write("#   - UNREACHABLE[] assignment with kind, reason, ref, confirmed_by\n\n")
    for method in sorted(exists):
        f.write(f"{method}\n")

print(f"Wrote TODO list to nodes_need_labels.txt")
print(f"\nDone. Rebuild to check for remaining errors.")
