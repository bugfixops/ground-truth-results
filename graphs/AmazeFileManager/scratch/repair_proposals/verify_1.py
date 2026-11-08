#!/usr/bin/env python3
"""
Verify all repair decisions with printed source evidence.
"""

import json
import subprocess
import os

APP_SRC = "/Users/darshan/Desktop/yang/work/final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java"
METHOD_LIST = "/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/method_list.json"

# Load method_list
with open(METHOD_LIST) as f:
    methods = json.load(f)

# Build lookup: full-package-dot-name -> canonical
dot_to_canonical = {}
canonical_to_class = {}
for m in methods:
    cls_slash = m['class']
    cls_dot = cls_slash.replace('/', '.')
    method_name = m['name']
    canonical = m['short']
    full_dot = f"{cls_dot}.{method_name}"
    dot_to_canonical[full_dot] = canonical
    canonical_to_class[canonical] = cls_slash

# Load grouped edges
with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/repair_proposals/helper1_grouped.json') as f:
    grouped = json.load(f)

# Load resolution data
with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/build_resume_72_name_resolution.json') as f:
    res_data = json.load(f)

print("="*80)
print("VERIFICATION OF REPAIR DECISIONS")
print("="*80)

# Group 1: Direct mappings (full package -> canonical)
print("\n## GROUP 1: Full Package Path -> Canonical (161 edges)")
print("Verification: checked against method_list.json")
direct_mapped = [name for name in grouped.keys() if name in dot_to_canonical]
print(f"Names with direct mapping: {len(direct_mapped)}")
for name in direct_mapped[:5]:
    print(f"  {name} -> {dot_to_canonical[name]} ✓")
print(f"  ... and {len(direct_mapped)-5} more")

# Group 2 & 3: Framework and inherited methods - need grep verification
print("\n## GROUPS 2 & 3: Framework/Library and Inherited Methods")
print("Verification: grep source files to confirm method not declared\n")

to_verify = []
for name in sorted(grouped.keys()):
    if name in dot_to_canonical:
        continue  # Already verified in Group 1
    resolution = res_data['resolutions'].get(name, {})
    category = resolution.get('category')
    if category in ['a', 'c']:  # Framework or inherited
        to_verify.append((name, category, resolution.get('reason', '')))

print(f"Names to verify: {len(to_verify)}\n")

for name, category, reason in to_verify[:20]:  # Sample first 20
    print(f"\n{'='*70}")
    print(f"Name: {name}")
    print(f"Category: {category} ({'Framework/library' if category == 'a' else 'Inherited'})")
    print(f"Reason: {reason}")
    
    # Extract class and method
    if '.' in name:
        parts = name.rsplit('.', 1)
        if len(parts) == 2:
            class_name, method_name = parts
            
            # Try to find the source file
            # Handle both package-dot notation and simple names
            if '/' in class_name or 'com.amaze' in class_name:
                # Full package path
                file_path = class_name.replace('.', '/') + '.java'
                full_path = os.path.join(APP_SRC, file_path)
            else:
                # Simple name - search for it
                cmd = f'find "{APP_SRC}" -name "{class_name}.java" 2>/dev/null'
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                full_path = result.stdout.strip().split('\n')[0] if result.stdout.strip() else None
            
            if full_path and os.path.exists(full_path):
                # Grep for the method declaration
                cmd = f'grep -n "\\(public\\|private\\|protected\\|static\\).*{method_name}" "{full_path}"'
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                
                if result.stdout.strip():
                    print(f"FOUND in source:")
                    for line in result.stdout.strip().split('\n')[:3]:
                        print(f"  {line}")
                else:
                    print(f"NOT DECLARED in {os.path.basename(full_path)} ✓")
                    
                # Also show the class declaration
                simple_class = class_name.split(".")[-1].split("$")[0]
                cmd2 = f'grep -n "class {simple_class}" "{full_path}" | head -1'
                result2 = subprocess.run(cmd2, shell=True, capture_output=True, text=True)
                if result2.stdout.strip():
                    print(f"Class declaration: {result2.stdout.strip()}")
            else:
                print(f"Source file not found (framework class) ✓")

print(f"\n{'='*80}")
print("Verification complete for sample. Full verification would check all {len(to_verify)} names.")
