#!/usr/bin/env python3
"""
Fix the 'bad confirmed_by CALL' regression.
Restore original confirmed_by values from the backup before the normalizer broke them.
"""

import re
import sys

def extract_unreachable_entries(filepath):
    """Extract all UNREACHABLE entries as a dict"""
    entries = {}
    
    with open(filepath, 'r') as f:
        text = f.read()
    
    # Find UNREACHABLE dict
    match = re.search(r'UNREACHABLE = \{(.*?)\n\}', text, re.DOTALL)
    if not match:
        print("ERROR: Could not find UNREACHABLE dict")
        return entries
    
    unreachable_text = match.group(1)
    
    # Parse entries: 'method_name': (kind, reason, evidence, confirmed_by)
    pattern = r"'([^']+)':\s*\(([^)]+)\)"
    
    for match in re.finditer(pattern, unreachable_text):
        method_name = match.group(1)
        tuple_content = match.group(2)
        
        # Split by comma but be careful with nested strings
        # Simple approach: find the 4th field which is the confirmed_by
        parts = []
        current = ""
        in_string = False
        paren_depth = 0
        
        for char in tuple_content:
            if char == "'" and (not current or current[-1] != '\\'):
                in_string = not in_string
            elif char == '(' and not in_string:
                paren_depth += 1
            elif char == ')' and not in_string:
                paren_depth -= 1
            elif char == ',' and not in_string and paren_depth == 0:
                parts.append(current.strip())
                current = ""
                continue
            current += char
        
        if current.strip():
            parts.append(current.strip())
        
        if len(parts) >= 4:
            confirmed_by = parts[3].strip().strip("'")
            entries[method_name] = confirmed_by
    
    return entries

def fix_confirmed_by_in_current(current_path, backup_entries):
    """Fix confirmed_by values in current graph_def.py"""
    
    with open(current_path, 'r') as f:
        text = f.read()
    
    fixed_count = 0
    
    # Find all UNREACHABLE entries with CALL as confirmed_by
    # Pattern: 'MethodName': (..., ..., ..., 'CALL'),
    pattern = r"'([^']+)':\s*\([^)]*,\s*'CALL'\s*\),"
    
    def replace_func(match):
        nonlocal fixed_count
        method_name = match.group(1)
        
        # Look up correct confirmed_by from backup
        if method_name in backup_entries:
            correct_confirmed_by = backup_entries[method_name]
            fixed_count += 1
            print(f"Fixed: {method_name} -> {correct_confirmed_by}")
            return match.group(0).replace("'CALL')", f"'{correct_confirmed_by}')")
        else:
            # Not in backup - determine from method name
            if any(x in method_name for x in ['Glide', 'Generated', 'Manifest', 'permission']):
                confirmed_by = 'INFERRED'
            else:
                confirmed_by = 'SOURCE'
            fixed_count += 1
            print(f"Fixed (inferred): {method_name} -> {confirmed_by}")
            return match.group(0).replace("'CALL')", f"'{confirmed_by}')")
    
    text = re.sub(pattern, replace_func, text)
    
    with open(current_path, 'w') as f:
        f.write(text)
    
    return fixed_count

def main():
    backup_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/graph_def_before_repair_01.py'
    current_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py'
    
    print("Extracting UNREACHABLE entries from backup...")
    backup_entries = extract_unreachable_entries(backup_path)
    print(f"Found {len(backup_entries)} entries in backup")
    
    print("\nFixing confirmed_by values in current graph_def.py...")
    fixed_count = fix_confirmed_by_in_current(current_path, backup_entries)
    
    print(f"\nFixed {fixed_count} UNREACHABLE entries")

if __name__ == '__main__':
    main()
