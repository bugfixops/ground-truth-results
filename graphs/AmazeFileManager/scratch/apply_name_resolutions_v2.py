#!/usr/bin/env python3
"""
Apply name resolutions from resolve_names.py to graph_def.py using regex.

This script uses careful regex matching to replace node names in e() calls
without reformatting the entire file.
"""

import json
import re
import os
import sys

def load_resolutions(resolution_file):
    """Load the resolution JSON"""
    with open(resolution_file) as f:
        return json.load(f)

def escape_regex(s):
    """Escape special regex characters"""
    return re.escape(s)

def apply_resolutions_regex(graph_def_path, resolutions_data, output_path=None):
    """
    Apply resolutions using regex replacement.
    Only replace exact matches of node names in e() call string literals.
    """
    
    # Build rename map from resolved cases only
    rename_map = {}
    for bad_name, info in resolutions_data['resolutions'].items():
        if info['classification'] == 'resolved' and info['canonical']:
            rename_map[bad_name] = info['canonical']
    
    print(f'Loaded {len(rename_map)} resolved name mappings')
    
    # Read the file
    with open(graph_def_path, encoding='utf-8') as f:
        content = f.read()
    
    # Track changes
    changes_made = []
    
    # For each bad_name -> canonical mapping
    for bad_name, canonical in sorted(rename_map.items(), key=lambda x: -len(x[0])):
        # Create regex patterns for both quoted forms
        # Pattern: match the bad_name as a complete string literal in an e() call
        # We need to be careful about:
        # 1. Single vs double quotes
        # 2. The name being part of a larger identifier
        # 3. Only matching in e() calls (roughly - we'll match e(...'name'...))
        
        # Escape the name for use in regex
        escaped_bad = escape_regex(bad_name)
        
        # Pattern 1: Single-quoted strings in e() calls
        pattern1 = rf"(\be\s*\([^)]*?)'({escaped_bad})'([^)]*?\))"
        # Pattern 2: Double-quoted strings in e() calls  
        pattern2 = rf'(\be\s*\([^)]*?)"({escaped_bad})"([^)]*?\))'
        
        # Count replacements for this name
        count = 0
        
        # Replace single-quoted occurrences
        def replace_single(match):
            nonlocal count
            count += 1
            return f"{match.group(1)}'{canonical}'{match.group(3)}"
        
        def replace_double(match):
            nonlocal count
            count += 1
            return f'{match.group(1)}"{canonical}"{match.group(3)}'
        
        content = re.sub(pattern1, replace_single, content)
        content = re.sub(pattern2, replace_double, content)
        
        if count > 0:
            changes_made.append((bad_name, canonical, count))
            print(f'  {bad_name} -> {canonical} ({count} replacements)')
    
    # Write output
    if output_path is None:
        output_path = graph_def_path
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    total_replacements = sum(c[2] for c in changes_made)
    print(f'\nApplied {len(changes_made)} unique renamings ({total_replacements} total replacements) to {output_path}')
    return changes_made

def create_ambiguous_file(resolutions_data, output_path):
    """Create ambiguous_remaining.txt for manual resolution"""
    
    ambiguous = [(name, info) for name, info in resolutions_data['resolutions'].items() 
                 if info['classification'] == 'ambiguous']
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('# Ambiguous node names requiring manual resolution\n')
        f.write(f'# Total: {len(ambiguous)} names\n')
        f.write('# For each ambiguous name, inspect the edge context (source file and line)\n')
        f.write('# to determine which overload is correct.\n\n')
        
        for bad_name, info in sorted(ambiguous):
            f.write(f'\n## {bad_name}\n')
            f.write(f'Reason: {info["reason"]}\n')
            f.write('Candidates:\n')
            for candidate in info['candidates']:
                f.write(f'  - {candidate}\n')
    
    print(f'Created {output_path} with {len(ambiguous)} ambiguous cases')

def main(argv):
    if len(argv) < 3:
        print('Usage: python3 -I apply_name_resolutions_v2.py <resolution.json> <graph_def.py>')
        return 1
    
    resolution_file = argv[1]
    graph_def_path = argv[2]
    
    # Load resolutions
    resolutions_data = load_resolutions(resolution_file)
    
    # Apply automatic resolutions
    changes = apply_resolutions_regex(graph_def_path, resolutions_data)
    
    # Create ambiguous file
    scratch_dir = os.path.dirname(resolution_file)
    ambiguous_file = os.path.join(scratch_dir, 'ambiguous_remaining.txt')
    create_ambiguous_file(resolutions_data, ambiguous_file)
    
    # Write changes log
    changes_log = os.path.join(scratch_dir, 'name_resolution_changes.txt')
    with open(changes_log, 'w', encoding='utf-8') as f:
        f.write(f'# Name resolution changes applied\n')
        f.write(f'# Total: {sum(c[2] for c in changes)} replacements for {len(changes)} unique names\n\n')
        for bad, canonical, count in changes:
            f.write(f'{bad} -> {canonical} ({count} occurrences)\n')
    
    print(f'\nChanges logged to {changes_log}')
    print('\nSummary:')
    print(f'  Resolved and applied: {len(changes)} unique names')
    print(f'  Ambiguous (manual work): {len([1 for v in resolutions_data["resolutions"].values() if v["classification"]=="ambiguous"])}')
    print(f'  Not a node (left as is): {len([1 for v in resolutions_data["resolutions"].values() if v["classification"]=="not_a_node"])}')
    
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
