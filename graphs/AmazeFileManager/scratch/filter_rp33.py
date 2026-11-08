#!/usr/bin/env python3
import json
import re

# Load method list
with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/method_list.json') as f:
    methods = set(m['short'] for m in json.load(f))

# Read repair_rp33.py
with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/parts/repair_rp33.py') as f:
    lines = f.readlines()

kept_lines = []
dropped_edges = []
i = 0
while i < len(lines):
    line = lines[i]
    
    # Check if this is an e() call
    if line.startswith("e('") or line.startswith('e("'):
        # Extract src and dst from e('src', 'dst', 'kind',
        match = re.match(r"e\(['\"]([^'\"]+)['\"], ['\"]([^'\"]+)['\"], ", line)
        if match:
            src, dst = match.groups()
            # Check if both exist in method list
            if src in methods and dst in methods:
                # Keep this edge and following lines until the closing paren
                kept_lines.append(line)
                i += 1
                # Keep continuation lines
                while i < len(lines) and not lines[i].strip().endswith(')'):
                    kept_lines.append(lines[i])
                    i += 1
                if i < len(lines):
                    kept_lines.append(lines[i])  # closing line
                    i += 1
            else:
                # Drop this edge
                dropped_edges.append((src, dst))
                i += 1
                # Skip continuation lines
                while i < len(lines) and not lines[i].strip().endswith(')'):
                    i += 1
                if i < len(lines):
                    i += 1  # skip closing line
        else:
            kept_lines.append(line)
            i += 1
    else:
        # Keep all non-edge lines (comments, UNREACHABLE entries, blank lines)
        kept_lines.append(line)
        i += 1

# Write filtered version
with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/parts/repair_rp33_filtered.py', 'w') as f:
    f.writelines(kept_lines)

# Report dropped edges
print(f"Kept {len([l for l in kept_lines if l.startswith('e(')])}/{len([l for l in lines if l.startswith('e(')])} edges")
print(f"Dropped {len(dropped_edges)} edges to non-existent nodes")
for src, dst in dropped_edges[:10]:
    print(f"  {src} -> {dst}")
if len(dropped_edges) > 10:
    print(f"  ... and {len(dropped_edges) - 10} more")
