#!/usr/bin/env python3
"""
Fix unknown node errors by removing entire edge definitions (including multi-line).
"""

import json
import re

# Read the lists we created
with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/unknown_not_exists.txt', 'r') as f:
    not_exists = set(line.strip() for line in f if line.strip())

print(f"Methods that don't exist (edges to remove): {len(not_exists)}")

# Read graph_def.py
graph_def_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py'
with open(graph_def_path, 'r') as f:
    content = f.read()

# Find all edge definitions with their line numbers
# Pattern: e('..', '..', 'KIND', '..', ...) spanning multiple lines
edge_pattern = re.compile(r"^e\([^)]+\)$", re.MULTILINE)

# Instead, let's use a different approach - find complete e(...) calls
# This is tricky because they can span multiple lines.
# Let's process the file looking for e( and collecting until we find the matching )

lines = content.split('\n')
output_lines = []
i = 0
removed_count = 0

while i < len(lines):
    line = lines[i]
    
    # Check if this line starts an edge definition
    if re.match(r"^\s*e\(", line):
        # Collect the full edge definition
        edge_lines = [line]
        j = i + 1
        # Count parentheses to find the end
        paren_count = line.count('(') - line.count(')')
        while paren_count > 0 and j < len(lines):
            edge_lines.append(lines[j])
            paren_count += lines[j].count('(') - lines[j].count(')')
            j += 1
        
        # Now edge_lines contains the complete edge definition
        full_edge = '\n'.join(edge_lines)
        
        # Check if any non-existent method is referenced
        should_remove = False
        for method in not_exists:
            # Escape special regex characters
            escaped = re.escape(method)
            # Look for the method name in quotes
            if re.search(rf"['\"]" + escaped + rf"['\"]", full_edge):
                should_remove = True
                break
        
        if should_remove:
            # Comment out all lines of this edge
            for edge_line in edge_lines:
                output_lines.append("# REMOVED (unknown node): " + edge_line)
            removed_count += 1
        else:
            output_lines.extend(edge_lines)
        
        i = j  # Skip to next line after this edge
    else:
        output_lines.append(line)
        i += 1

print(f"\nRemoved {removed_count} complete edge definitions")

# Write back
with open(graph_def_path, 'w') as f:
    f.write('\n'.join(output_lines))

print(f"\nDone. Rebuild to check for remaining errors.")
