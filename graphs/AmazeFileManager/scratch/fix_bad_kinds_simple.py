#!/usr/bin/env python3
"""Fix bad kinds (LAMBDA/CALLBACK) by restoring from backup."""

import re

def main():
    current_file = '../graph_def.py'
    backup_file = 'graph_def_before_cleanup_03.py'
    output_file = '../graph_def.py.fixed'
    
    print("Loading backup file...")
    with open(backup_file, 'r') as f:
        backup_content = f.read()
    
    print("Loading current file...")
    with open(current_file, 'r') as f:
        current_content = f.read()
    
    # Find all e() calls with LAMBDA or CALLBACK in current file
    # Pattern: e('src', 'dst', 'LAMBDA' or 'CALLBACK', ...
    pattern = r"e\s*\(\s*(['\"])([^'\"]+)\1\s*,\s*(['\"])([^'\"]+)\3\s*,\s*(['\"])(LAMBDA|CALLBACK)\5"
    
    matches = list(re.finditer(pattern, current_content))
    print(f"Found {len(matches)} edges with LAMBDA or CALLBACK")
    
    fixed_content = current_content
    fixes_applied = 0
    not_found = 0
    
    for match in matches:
        src = match.group(2)
        dst = match.group(4)
        bad_kind = match.group(6)
        
        # Find this edge in backup
        # Look for e('src', 'dst', 'KIND', ...
        backup_pattern = rf"e\s*\(\s*(['\"]){re.escape(src)}\1\s*,\s*(['\"]){re.escape(dst)}\2\s*,\s*(['\"])([^'\"]+)\3"
        backup_match = re.search(backup_pattern, backup_content)
        
        if backup_match:
            backup_kind = backup_match.group(4)
            print(f"  {src} -> {dst}: {bad_kind} => {backup_kind}")
            
            # Replace in fixed_content
            old_str = match.group(0)
            new_str = old_str.replace(f"'{bad_kind}'", f"'{backup_kind}'").replace(f'"{bad_kind}"', f'"{backup_kind}"')
            fixed_content = fixed_content.replace(old_str, new_str, 1)
            fixes_applied += 1
        else:
            print(f"  WARNING: No backup for {src} -> {dst}")
            not_found += 1
    
    # Write output
    with open(output_file, 'w') as f:
        f.write(fixed_content)
    
    print(f"\nFixes applied: {fixes_applied}")
    print(f"Not found in backup: {not_found}")
    print(f"Fixed file written to {output_file}")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
