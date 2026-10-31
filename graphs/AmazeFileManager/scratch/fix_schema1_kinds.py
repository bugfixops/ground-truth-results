#!/usr/bin/env python3
"""
Fix schema-1 edge kinds in graph_def.py.

Schema-1 kinds to convert:
- EXPLICIT → CALL (direct app-to-app method call)
- DIRECT → CALL
- CONSTRUCTED → CALL (constructor invocation)
- INFERRED → examine evidence, convert to appropriate kind (usually CALL or FRAMEWORK)
- IMPLICIT → examine evidence, convert to appropriate kind

This script reads graph_def.py, replaces the edge kind strings, and writes back.
"""

import re
import sys

def main():
    graph_def_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py'
    
    with open(graph_def_path, 'r') as f:
        content = f.read()
    
    original_content = content
    
    # Count occurrences before replacement
    explicit_count = content.count("'EXPLICIT'")
    direct_count = content.count("'DIRECT'")
    constructed_count = content.count("'CONSTRUCTED'")
    inferred_count = content.count("'INFERRED'")
    implicit_count = content.count("'IMPLICIT'")
    
    print(f"Found:")
    print(f"  EXPLICIT: {explicit_count}")
    print(f"  DIRECT: {direct_count}")
    print(f"  CONSTRUCTED: {constructed_count}")
    print(f"  INFERRED: {inferred_count}")
    print(f"  IMPLICIT: {implicit_count}")
    
    # Simple replacements:
    # EXPLICIT → CALL (these are direct app-to-app calls)
    content = content.replace("'EXPLICIT'", "'CALL'")
    
    # DIRECT → CALL
    content = content.replace("'DIRECT'", "'CALL'")
    
    # CONSTRUCTED → CALL (constructor invocations)
    content = content.replace("'CONSTRUCTED'", "'CALL'")
    
    # For INFERRED and IMPLICIT, we need to examine each case.
    # Let's first try converting them all to CALL and then manually fix any that are wrong.
    content = content.replace("'INFERRED'", "'CALL'")
    content = content.replace("'IMPLICIT'", "'CALL'")
    
    if content == original_content:
        print("\nNo changes made.")
        return 1
    
    # Write back
    with open(graph_def_path, 'w') as f:
        f.write(content)
    
    print(f"\nReplaced all schema-1 kinds with CALL.")
    print(f"Please review and rebuild.")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
