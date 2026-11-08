#!/usr/bin/env python3
"""
Safely delete UNREACHABLE entries for methods that have incoming edges from REACHABLE sources.
"""

import json
import re
import sys

def find_matching_paren(text, start):
    """Find the matching closing paren, handling nested parens."""
    depth = 0
    in_string = False
    escape = False
    i = start
    
    while i < len(text):
        ch = text[i]
        
        if escape:
            escape = False
            i += 1
            continue
        
        if ch == '\\':
            escape = True
            i += 1
            continue
        
        if ch == "'":
            in_string = not in_string
        
        if not in_string:
            if ch == '(':
                depth += 1
            elif ch == ')':
                depth -= 1
                if depth == 0:
                    return i
        
        i += 1
    
    return -1

if len(sys.argv) < 3:
    print("Usage: python3 delete_unreachable_safe.py <start_idx> <end_idx>")
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
    content = f.read()

# For each method, find and remove its UNREACHABLE line(s)
deleted_count = 0
for method in methods_to_delete:
    # Escape special regex characters in method name
    escaped_method = re.escape(method)
    
    # Find the start of the UNREACHABLE entry
    pattern = rf"UNREACHABLE\['{escaped_method}'\]\s*=\s*\("
    
    match = re.search(pattern, content)
    if match:
        # Find the matching closing paren
        start = match.start()
        tuple_start = match.end() - 1  # Position of opening (
        end = find_matching_paren(content, tuple_start)
        
        if end != -1:
            # Delete from start to end+1 (include closing paren)
            # Also remove the newline after if present
            delete_end = end + 1
            if delete_end < len(content) and content[delete_end] == '\n':
                delete_end += 1
            
            print(f"  Deleting: {method}")
            content = content[:start] + content[delete_end:]
            deleted_count += 1
        else:
            print(f"  WARNING: Could not find matching paren for: {method}")
    else:
        print(f"  WARNING: Could not find UNREACHABLE entry for: {method}")

# Write back
with open('graphs/AmazeFileManager/graph_def.py', 'w') as f:
    f.write(content)

print(f"\nDeleted {deleted_count} UNREACHABLE entries")
