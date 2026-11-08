#!/usr/bin/env python3
"""
Fix Step 3 errors: GUI edges and bad kinds.
"""

import re

print("Loading graph_def.py...")
with open('graphs/AmazeFileManager/graph_def.py', 'r') as f:
    content = f.read()

# Step 3a: Fix GUI edges (method->method should be CALL/CALLBACK for callbacks, or LAMBDA for lambdas)
print("\nStep 3a: Fixing GUI edges...")
gui_fixes = 0

# Find all e() calls with 'GUI' kind
e_pattern = r"e\('([^']+)',\s*'([^']+)',\s*'([^']+)',\s*'GUI'"
matches = list(re.finditer(e_pattern, content))

for match in matches:
    src, dst, kind = match.groups()
    # Check if either src or dst is a page (starts with S_)
    if not (src.startswith('S_') or dst.startswith('S_')):
        # This is method->method, not page->method
        # Determine correct kind
        if 'lambda$' in dst:
            new_kind = 'LAMBDA'
        elif 'afterTextChanged' in dst or 'onTextChanged' in dst or 'beforeTextChanged' in dst:
            new_kind = 'CALLBACK'
        elif '$' in dst and not 'lambda$' in dst:
            # Inner class method, likely callback
            new_kind = 'CALLBACK'
        else:
            new_kind = 'CALL'
        
        # Replace
        old_text = match.group(0)
        new_text = f"e('{src}', '{dst}', '{new_kind}'"
        content = content.replace(old_text, new_text, 1)
        gui_fixes += 1

print(f"  Fixed {gui_fixes} GUI edges")

# Step 3b: Fix bad kinds
print("\nStep 3b: Fixing bad kinds...")
kind_map = {
    'DIRECT': 'CALL',
    'INTRA': 'CALL',
    'NEVER': 'CALL',
    'EXPLICIT': 'CALL'
}

bad_kind_fixes = 0
for old_kind, new_kind in kind_map.items():
    pattern = rf"e\('([^']+)',\s*'([^']+)',\s*'{old_kind}'"
    matches = list(re.finditer(pattern, content))
    
    for match in matches:
        old_text = match.group(0)
        src, dst = match.groups()
        new_text = f"e('{src}', '{dst}', '{new_kind}'"
        content = content.replace(old_text, new_text, 1)
        bad_kind_fixes += 1

print(f"  Fixed {bad_kind_fixes} bad kinds")

# Save changes
print("\nWriting updated graph_def.py...")
with open('graphs/AmazeFileManager/graph_def.py', 'w') as f:
    f.write(content)

print(f"\nTotal fixes:")
print(f"  GUI edges: {gui_fixes}")
print(f"  Bad kinds: {bad_kind_fixes}")
print(f"  Total: {gui_fixes + bad_kind_fixes}")
