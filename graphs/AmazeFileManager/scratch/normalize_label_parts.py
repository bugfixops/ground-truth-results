#!/usr/bin/env python3
"""
Normalize invalid edge kinds in label_1, label_2, label_3 .py files before merging.

Invalid kinds to fix:
- FW-CALL → FRAMEWORK
- LAMBDA → CALL
- NEW → CALL
- SUPER → CALL
- FIELD → CALL (field access via bytecode)
- CALLS → CALL
- FRAMEWORK_CALLS → FRAMEWORK
"""

import sys

files_to_fix = [
    '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/parts/label_2.py',
    '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/parts/label_3.py',
]

for file_path in files_to_fix:
    print(f"\nProcessing {file_path}...")
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    original = content
    
    # Normalize invalid kinds
    replacements = {
        "'FW-CALL'": "'FRAMEWORK'",
        "'LAMBDA'": "'CALL'",
        "'NEW'": "'CALL'",
        "'SUPER'": "'CALL'",
        "'FIELD'": "'CALL'",
        "'CALLS'": "'CALL'",
        "'FRAMEWORK_CALLS'": "'FRAMEWORK'",
    }
    
    for old, new in replacements.items():
        count = content.count(old)
        if count > 0:
            print(f"  {old} → {new}: {count} occurrences")
            content = content.replace(old, new)
    
    if content != original:
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"  ✓ Updated {file_path}")
    else:
        print(f"  ✓ No changes needed")

print("\nDone normalizing label parts.")
