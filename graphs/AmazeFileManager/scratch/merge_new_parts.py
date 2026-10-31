#!/usr/bin/env python3
"""
Merge label_b017, b018, b020, b021 with normalization and proper error tracking.
"""

import subprocess
import sys
import re
import ast

parts_to_merge = ['label_b017', 'label_b018', 'label_b020', 'label_b021']

def normalize_edge_kinds(content):
    """Normalize invalid edge kinds."""
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

def validate_python_syntax(content):
    """Check if content is valid Python."""
    try:
        ast.parse(content)
        return True, None
    except SyntaxError as e:
        return False, str(e)

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

build_num = 43  # Starting from 043

for part_name in parts_to_merge:
    print(f"\n{'='*70}")
    print(f"Merging {part_name}...")
    print(f"{'='*70}")
    
    part_path = f'/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/parts/{part_name}.py'
    
    # Check if exists
    try:
        with open(part_path, 'r') as f:
            part_content = f.read()
    except FileNotFoundError:
        print(f"  WARNING: {part_path} not found, skipping")
        continue
    
    # Normalize edge kinds
    original_content = part_content
    part_content = normalize_edge_kinds(part_content)
    
    if part_content != original_content:
        print(f"  Normalized edge kinds in {part_name}")
    
    # Validate syntax
    valid, error = validate_python_syntax(part_content)
    if not valid:
        print(f"  ERROR: Syntax error in {part_name}: {error}")
        print(f"  Skipping this part")
        continue
    
    # Backup before merge
    backup_path = f'/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py.bak_before_{part_name}'
    with open(backup_path, 'w') as f:
        f.writelines(graph_lines)
    print(f"  Backed up to {backup_path}")
    
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
    
    # py_compile check
    import py_compile
    try:
        py_compile.compile('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py', doraise=True)
        print(f"  ✓ py_compile passed")
    except py_compile.PyCompileError as e:
        print(f"  ERROR: py_compile failed: {e}")
        # Restore from backup
        with open(backup_path, 'r') as f:
            graph_lines = f.readlines()
        with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py', 'w') as f:
            f.writelines(graph_lines)
        print(f"  Restored from backup, skipping {part_name}")
        continue
    
    # Update for next iteration
    graph_lines = new_lines
    unreachable_idx = len(new_lines) - len(graph_lines[unreachable_idx:])
    
    # Build
    print(f"  Building...")
    result = subprocess.run(
        ['python3', '-I', 'tools/build_graph.py', 'graphs/AmazeFileManager', 'amazefilemanager'],
        cwd='/Users/darshan/Desktop/yang/work',
        capture_output=True,
        text=True,
        timeout=120
    )
    
    # Extract verdicts
    r, u, unres, edges, errors, warnings = 0, 0, 0, 0, 0, 0
    for line in result.stdout.split('\n'):
        if line.startswith('verdicts:'):
            match = re.search(r'REACHABLE (\d+).*UNREACHABLE (\d+).*UNRESOLVED (\d+)', line)
            if match:
                r, u, unres = int(match.group(1)), int(match.group(2)), int(match.group(3))
        if 'edges ' in line and line.startswith('methods'):
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
    
    # Check for build failure
    if 'Traceback' in result.stdout or result.returncode != 0:
        print(f"  ERROR: Build failed!")
        print(f"  Output preview: {result.stdout[:500]}")
        # Restore from backup
        with open(backup_path, 'r') as f:
            graph_lines = f.readlines()
        with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py', 'w') as f:
            f.writelines(graph_lines)
        print(f"  Restored from backup, skipping {part_name}")
        continue
    
    # Log C7 line
    c7_line = f"- Build {build_num:03d}: R={r} U={u} UNRES={unres} edges={edges} errors={errors} warnings={warnings} (merged {part_name})"
    print(f"  {c7_line}")
    
    # Append to AGENT_NOTES
    with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/AGENT_NOTES.md', 'r') as f:
        notes = f.read()
    
    # Find Build 042 line and append after it
    if '- Build 042:' in notes:
        notes = notes.replace(
            '- Build 042: 2026-10-27 22:XX R=1324 U=15 UNRES=1642 edges=7184 errors=2533 warnings=7 (merged label_b005-b012: +265 edges)',
            f'- Build 042: 2026-10-27 22:XX R=1324 U=15 UNRES=1642 edges=7184 errors=2533 warnings=7 (merged label_b005-b012: +265 edges)\n{c7_line}'
        )
    else:
        # Append at end of build history
        notes += f'\n{c7_line}'
    
    with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/AGENT_NOTES.md', 'w') as f:
        f.write(notes)
    
    build_num += 1

print(f"\n{'='*70}")
print(f"Completed merging available parts")
print(f"{'='*70}")
