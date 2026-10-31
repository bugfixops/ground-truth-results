#!/usr/bin/env python3
"""
Merge label_b005 through label_b012 into graph_def.py, normalizing edge kinds and building after each.
"""

import subprocess
import sys
import re

parts_to_merge = [
    'label_b005', 'label_b006', 'label_b007', 'label_b008',
    'label_b009', 'label_b010', 'label_b011', 'label_b012'
]

def normalize_edge_kinds(content):
    """Normalize invalid edge kinds to valid schema-2 kinds."""
    replacements = {
        "'EXPLICIT'": "'CALL'",
        "'DIRECT'": "'CALL'",
        "'CONSTRUCTED'": "'CALL'",
        "'INFERRED'": "'CALL'",
        "'IMPLICIT'": "'CALL'",
        "'FW-CALL'": "'FRAMEWORK'",
        "'LAMBDA'": "'CALL'",
        "'NEW'": "'CALL'",
        "'SUPER'": "'CALL'",
        "'FIELD'": "'CALL'",
        "'CALLS'": "'CALL'",
        "'FRAMEWORK_CALLS'": "'FRAMEWORK'",
    }
    
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    return content

def get_build_verdicts():
    """Run build and extract verdict counts."""
    result = subprocess.run(
        ['python3', '-I', 'tools/build_graph.py', 'graphs/AmazeFileManager', 'amazefilemanager'],
        cwd='/Users/darshan/Desktop/yang/work',
        capture_output=True,
        text=True
    )
    
    for line in result.stdout.split('\n'):
        if line.startswith('verdicts:'):
            # Extract R, U, UNRES counts
            match = re.search(r'REACHABLE (\d+).*UNREACHABLE (\d+).*UNRESOLVED (\d+)', line)
            if match:
                return int(match.group(1)), int(match.group(2)), int(match.group(3))
        if line.startswith('edges'):
            match = re.search(r'edges (\d+)', line)
            if match:
                edges = int(match.group(1))
        if line.startswith('errors:'):
            match = re.search(r'errors: (\d+)', line)
            if match:
                errors = int(match.group(1))
        if line.startswith('warnings:'):
            match = re.search(r'warnings: (\d+)', line)
            if match:
                warnings = int(match.group(1))
    
    return None, None, None

# Read graph_def.py
with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py', 'r') as f:
    graph_lines = f.readlines()

# Find UNREACHABLE section
unreachable_idx = None
for i, line in enumerate(graph_lines):
    if '# ================================================================== L. UNREACHABLE' in line:
        unreachable_idx = i
        break

if unreachable_idx is None:
    print("ERROR: Could not find UNREACHABLE section")
    sys.exit(1)

build_num = 35  # Starting from build 035

for part_name in parts_to_merge:
    print(f"\n{'='*60}")
    print(f"Merging {part_name}...")
    print(f"{'='*60}")
    
    # Read part
    part_path = f'/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/parts/{part_name}.py'
    with open(part_path, 'r') as f:
        part_content = f.read()
    
    # Normalize edge kinds
    original_content = part_content
    part_content = normalize_edge_kinds(part_content)
    
    if part_content != original_content:
        print(f"  Normalized edge kinds in {part_name}")
    
    # Insert before UNREACHABLE section
    new_lines = graph_lines[:unreachable_idx]
    new_lines.append(f'\n# ---- {part_name} ----\n')
    new_lines.append(part_content)
    if not part_content.endswith('\n'):
        new_lines.append('\n')
    new_lines.append('\n')
    new_lines.extend(graph_lines[unreachable_idx:])
    
    # Write back
    with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py', 'w') as f:
        f.writelines(new_lines)
    
    # Update for next iteration
    graph_lines = new_lines
    unreachable_idx = len(new_lines) - len(graph_lines[unreachable_idx:])
    
    # Build
    print(f"  Building...")
    result = subprocess.run(
        ['python3', '-I', 'tools/build_graph.py', 'graphs/AmazeFileManager', 'amazefilemanager'],
        cwd='/Users/darshan/Desktop/yang/work',
        capture_output=True,
        text=True
    )
    
    # Extract verdicts
    r, u, unres, edges, errors, warnings = 0, 0, 0, 0, 0, 0
    for line in result.stdout.split('\n'):
        if line.startswith('verdicts:'):
            match = re.search(r'REACHABLE (\d+).*UNREACHABLE (\d+).*UNRESOLVED (\d+)', line)
            if match:
                r, u, unres = int(match.group(1)), int(match.group(2)), int(match.group(3))
        if line.startswith('edges'):
            match = re.search(r'edges (\d+)', line)
            if match:
                edges = int(match.group(1))
        if line.startswith('errors:'):
            match = re.search(r'errors: (\d+)', line)
            if match:
                errors = int(match.group(1))
        if line.startswith('warnings:'):
            match = re.search(r'warnings: (\d+)', line)
            if match:
                warnings = int(match.group(1))
    
    # Log C7 line
    c7_line = f"- Build {build_num:03d}: 2026-10-27 22:XX R={r} U={u} UNRES={unres} edges={edges} errors={errors} warnings={warnings} (merged {part_name})"
    print(f"  {c7_line}")
    
    # Append to AGENT_NOTES
    with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/AGENT_NOTES.md', 'r') as f:
        notes = f.read()
    
    # Find Build 034 line and append after it
    notes = notes.replace(
        '- Build 034: 2026-10-27 22:XX R=1324 U=15 UNRES=1642 edges=6919 errors=2282 warnings=7 (merged label_1-3: Glide/adapters/AsyncTasks, +75R -75UNRES -63errors)',
        f'- Build 034: 2026-10-27 22:XX R=1324 U=15 UNRES=1642 edges=6919 errors=2282 warnings=7 (merged label_1-3: Glide/adapters/AsyncTasks, +75R -75UNRES -63errors)\n{c7_line}'
    )
    
    with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/AGENT_NOTES.md', 'w') as f:
        f.write(notes)
    
    build_num += 1

print(f"\n{'='*60}")
print(f"Merged all 8 parts (b005-b012)")
print(f"{'='*60}")
