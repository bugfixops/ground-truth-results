#!/usr/bin/env python3
"""
Delete UNREACHABLE entries for Glide methods that have incoming edges.
Per pages.md analysis, these 30 methods ARE reachable via bytecode.
"""

import re

# From pages.md Category A: Glide methods with incoming edges
GLIDE_METHODS_TO_DELETE = [
    'GlideOptions.<init>',
    'GlideOptions.apply',
    'GlideOptions.autoClone',
    'GlideOptions.centerCrop',
    'GlideOptions.centerInside',
    'GlideOptions.circleCrop',
    'GlideOptions.decode',
    'GlideOptions.diskCacheStrategy',
    'GlideOptions.dontAnimate',
    'GlideOptions.dontTransform',
    'GlideOptions.downsample',
    'GlideOptions.encodeFormat',
    'GlideOptions.encodeQuality',
    'GlideOptions.error(int)',
    'GlideOptions.error(Drawable)',
    'GlideOptions.fitCenter',
    'GlideOptions.format',
    'GlideOptions.frame',
    'GlideOptions.override(int)',
    'GlideOptions.override(int,int)',
    'GlideOptions.placeholder(int)',
    'GlideOptions.placeholder(Drawable)',
    'GlideOptions.priority',
    'GlideOptions.set',
    'GlideOptions.signature',
    'GlideOptions.sizeMultiplier',
    'GlideOptions.skipMemoryCache',
    'GlideOptions.timeout',
    'GlideOptions.transform(Transformation)',
    'GlideRequest.<init>(Class,RequestBuilder)',
    'GlideRequest.apply',
]

def delete_unreachable_entry(text, method_name):
    """Delete a specific UNREACHABLE dictionary entry"""
    # Pattern: 'MethodName': (tuple...),
    # Need to match the full entry including the tuple
    pattern = rf"^\s*'{re.escape(method_name)}':\s*\([^)]+\),?\s*$"
    
    lines = text.split('\n')
    new_lines = []
    skip_next = False
    deleted = False
    
    for i, line in enumerate(lines):
        # Check if this line is the UNREACHABLE entry for this method
        if re.match(pattern, line):
            deleted = True
            # Skip this line and any continuation
            continue
        
        new_lines.append(line)
    
    return '\n'.join(new_lines), deleted

def main():
    graph_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py'
    conflicts_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/conflicts.md'
    
    print("Reading graph_def.py...")
    with open(graph_path, 'r') as f:
        text = f.read()
    
    deleted_count = 0
    conflict_log = []
    
    print(f"\nProcessing {len(GLIDE_METHODS_TO_DELETE)} Glide UNREACHABLE entries...")
    for method in GLIDE_METHODS_TO_DELETE:
        new_text, deleted = delete_unreachable_entry(text, method)
        if deleted:
            text = new_text
            deleted_count += 1
            conflict_log.append(f"| {method} | DELETE UNREACHABLE | Bytecode edges exist, method IS reachable | Multiple | Deleted UNREACHABLE entry |")
            print(f"  ✓ Deleted: {method}")
        else:
            print(f"  ✗ Not found: {method}")
    
    print(f"\nDeleted {deleted_count} UNREACHABLE entries")
    
    print("\nWriting updated graph_def.py...")
    with open(graph_path, 'w') as f:
        f.write(text)
    
    print(f"Appending {len(conflict_log)} entries to conflicts.md...")
    with open(conflicts_path, 'a') as f:
        f.write('\n## Glide Methods - UNREACHABLE but has incoming edges\n\n')
        for entry in conflict_log:
            f.write(entry + '\n')
    
    print("\nDone!")

if __name__ == '__main__':
    main()
