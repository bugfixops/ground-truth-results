#!/usr/bin/env python3
"""
Delete UNREACHABLE entries for methods that have incoming edges from REACHABLE sources.
"""

import json
import re
import sys

if len(sys.argv) < 3:
    print("Usage: python3 delete_unreachable_entries.py <start_idx> <end_idx>")
    sys.exit(1)

start_idx = int(sys.argv[1])
end_idx = int(sys.argv[2])

# Load methods to delete
with open('graphs/AmazeFileManager/scratch/unreachable_to_delete.json') as f:
    to_delete = json.load(f)

chunk = to_delete[start_idx:end_idx]
methods_to_delete = set([item['method'] for item in chunk])

print(f"Deleting UNREACHABLE entries for {len(methods_to_delete)} methods (indices {start_idx}-{end_idx})...")

# Load graph_def.py
with open('graphs/AmazeFileManager/graph_def.py', 'r') as f:
    lines = f.readlines()

# Find and mark lines to delete
deleted_count = 0
lines_to_delete = set()
i = 0

while i < len(lines):
    line = lines[i]
    
    # Check if this line is an UNREACHABLE assignment for one of our methods
    match = re.match(r"UNREACHABLE\['([^']+)'\]\s*=\s*\(", line)
    if match:
        method = match.group(1)
        if method in methods_to_delete:
            # Mark this line and any continuation lines
            lines_to_delete.add(i)
            print(f"  Deleting: {method} (line {i+1})")
            deleted_count += 1
            
            # Check if it's a multi-line tuple
            if not line.strip().endswith(')'):
                # Multi-line - find closing paren
                j = i + 1
                while j < len(lines) and ')' not in lines[j-1]:
                    lines_to_delete.add(j)
                    j += 1
                # Also delete the line with the closing paren if it's continuation
                if j < len(lines) and lines[j].strip() and not lines[j].strip().startswith('UNREACHABLE') and not lines[j].strip().startswith('e('):
                    lines_to_delete.add(j)
    i += 1

# Create new content without deleted lines
new_lines = [lines[i] for i in range(len(lines)) if i not in lines_to_delete]

# Write back
with open('graphs/AmazeFileManager/graph_def.py', 'w') as f:
    f.writelines(new_lines)

print(f"\nDeleted {deleted_count} UNREACHABLE entries ({len(lines_to_delete)} lines total)")
print(f"Methods that should now become REACHABLE:")
for method in sorted(methods_to_delete):
    print(f"  - {method}")
