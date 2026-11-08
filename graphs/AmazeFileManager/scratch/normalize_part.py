#!/usr/bin/env python3
"""Normalize edge kind abbreviations in helper parts to full names expected by builder."""
import sys
import re

# Mapping from abbreviations to full kind names
# Based on graph_def.py valid kinds: CALL, CONSTRUCTED, DIRECT, ENTRY, EXPLICIT, FRAMEWORK, INFERRED, LIFECYCLE
ABBREV_MAP = {
    'FW': 'FRAMEWORK',
    'UI': 'EXPLICIT',
    'LC': 'LIFECYCLE',
    'ENT': 'ENTRY',
    # Note: CALL, DIRECT, INFERRED, CONSTRUCTED have no common abbreviations seen
}

def normalize_edge_kinds(content):
    """Replace abbreviated edge kinds in e() calls with full names."""
    lines = content.split('\n')
    normalized = []
    changes = []
    
    for i, line in enumerate(lines, 1):
        # Match e('src', 'dst', 'KIND', ...) pattern
        match = re.match(r"^e\('([^']*)', '([^']*)', '([^']*)'", line)
        if match:
            src, dst, kind = match.groups()
            if kind in ABBREV_MAP:
                old_kind = kind
                new_kind = ABBREV_MAP[kind]
                line = line.replace(f"'{old_kind}'", f"'{new_kind}'", 1)
                changes.append(f"Line {i}: {old_kind} → {new_kind} in {src} → {dst}")
        normalized.append(line)
    
    return '\n'.join(normalized), changes

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} input.py output.py")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    with open(input_path, 'r') as f:
        content = f.read()
    
    normalized, changes = normalize_edge_kinds(content)
    
    with open(output_path, 'w') as f:
        f.write(normalized)
    
    if changes:
        print(f"Normalized {len(changes)} edge kinds:")
        for change in changes[:10]:  # Show first 10
            print(f"  {change}")
        if len(changes) > 10:
            print(f"  ... and {len(changes) - 10} more")
    else:
        print("No abbreviations found - file already uses full kind names")
