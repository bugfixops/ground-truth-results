#!/usr/bin/env python3
"""
Merge label_1, label_2, label_3 into graph_def.py before the UNREACHABLE section.
"""

# Read graph_def.py
with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py', 'r') as f:
    lines = f.readlines()

# Find insertion point (before UNREACHABLE section)
insert_idx = None
for i, line in enumerate(lines):
    if '# ================================================================== L. UNREACHABLE' in line:
        insert_idx = i
        break

if insert_idx is None:
    print("ERROR: Could not find UNREACHABLE section")
    exit(1)

print(f"Found UNREACHABLE section at line {insert_idx + 1}")

# Read the three label parts
parts_to_merge = []
for part_name in ['label_1', 'label_2', 'label_3']:
    part_path = f'/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/parts/{part_name}.py'
    with open(part_path, 'r') as f:
        part_content = f.read()
    parts_to_merge.append((part_name, part_content))
    print(f"Read {part_name}.py ({len(part_content)} bytes)")

# Insert parts before UNREACHABLE section
new_lines = lines[:insert_idx]
new_lines.append('\n')
new_lines.append('# ================================================================== Merged label_1, label_2, label_3\n')
new_lines.append('\n')

for part_name, part_content in parts_to_merge:
    new_lines.append(f'# ---- {part_name} ----\n')
    new_lines.append(part_content)
    if not part_content.endswith('\n'):
        new_lines.append('\n')
    new_lines.append('\n')

new_lines.extend(lines[insert_idx:])

# Write back
with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py', 'w') as f:
    f.writelines(new_lines)

print(f"\nMerged 3 parts into graph_def.py before line {insert_idx + 1}")
print("Build to verify...")
