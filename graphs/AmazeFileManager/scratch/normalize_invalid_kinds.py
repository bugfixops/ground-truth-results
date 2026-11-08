#!/usr/bin/env python3
"""
Normalize ONLY the invalid schema-1 edge kinds:
- DIRECT → CALL (invalid)
- CONSTRUCTED → CALL (invalid)
- IMPLICIT → CALL (likely app-to-app call)
- INFERRED → need to check each case, but for now convert to CALL

KEEP EXPLICIT - it's valid in schema-2.
"""

import re

graph_def_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py'

with open(graph_def_path, 'r') as f:
    content = f.read()

original_content = content

# Count occurrences
direct_count = content.count("'DIRECT'")
constructed_count = content.count("'CONSTRUCTED'")
inferred_count = content.count("'INFERRED'")
implicit_count = content.count("'IMPLICIT'")
explicit_count = content.count("'EXPLICIT'")

print(f"Found:")
print(f"  EXPLICIT: {explicit_count} (KEEPING - valid)")
print(f"  DIRECT: {direct_count} (invalid, converting to CALL)")
print(f"  CONSTRUCTED: {constructed_count} (invalid, converting to CALL)")
print(f"  INFERRED: {inferred_count} (invalid as kind, converting to CALL)")
print(f"  IMPLICIT: {implicit_count} (invalid, converting to CALL)")

# Replace invalid kinds only
content = content.replace("'DIRECT'", "'CALL'")
content = content.replace("'CONSTRUCTED'", "'CALL'")
content = content.replace("'INFERRED'", "'CALL'")
content = content.replace("'IMPLICIT'", "'CALL'")

# DO NOT replace EXPLICIT - it's valid

if content == original_content:
    print("\nNo changes made.")
else:
    with open(graph_def_path, 'w') as f:
        f.write(content)
    print(f"\nConverted {direct_count + constructed_count + inferred_count + implicit_count} invalid kinds to CALL")
    print(f"KEPT {explicit_count} EXPLICIT edges (valid)")

print("\nDone. Rebuild to verify.")
