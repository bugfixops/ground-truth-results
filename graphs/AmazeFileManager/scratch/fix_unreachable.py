#!/usr/bin/env python3
"""
Fix UNREACHABLE entries per pages.md:
1. Rename JVM signature forms to canonical names (9 GlideRequests + 2 DatapointParcelable)
2. Delete UNREACHABLE entries for methods that have incoming edges (Glide methods that ARE reachable)
"""

import re

# JVM signature to canonical name mappings
JVM_TO_CANONICAL = {
    'GlideRequests.load(Landroid/graphics/Bitmap;)Lcom/amaze/filemanager/GlideRequest;': 'GlideRequests.load(Bitmap)',
    'GlideRequests.load(Landroid/graphics/drawable/Drawable;)Lcom/amaze/filemanager/GlideRequest;': 'GlideRequests.load(Drawable)',
    'GlideRequests.load(Landroid/net/Uri;)Lcom/amaze/filemanager/GlideRequest;': 'GlideRequests.load(Uri)',
    'GlideRequests.load(Ljava/io/File;)Lcom/amaze/filemanager/GlideRequest;': 'GlideRequests.load(File)',
    'GlideRequests.load(Ljava/lang/Integer;)Lcom/amaze/filemanager/GlideRequest;': 'GlideRequests.load(Integer)',
    'GlideRequests.load(Ljava/lang/Object;)Lcom/amaze/filemanager/GlideRequest;': 'GlideRequests.load(Object)',
    'GlideRequests.load(Ljava/lang/String;)Lcom/amaze/filemanager/GlideRequest;': 'GlideRequests.load(String)',
    'GlideRequests.load(Ljava/net/URL;)Lcom/amaze/filemanager/GlideRequest;': 'GlideRequests.load(URL)',
    'GlideRequests.load([B)Lcom/amaze/filemanager/GlideRequest;': 'GlideRequests.load(byte[])',
    'DatapointParcelable.<init>(Landroid/os/Parcel;)V': 'DatapointParcelable.<init>(Parcel)',
    'DatapointParcelable.<init>(Ljava/lang/String;IIJJJZ)V': 'DatapointParcelable.<init>(String,int,int,long,long,long,boolean)',
}

# Glide methods to delete - these have incoming edges so they're REACHABLE
GLIDE_TO_DELETE = [
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

def main():
    graph_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py'
    
    with open(graph_path, 'r') as f:
        lines = f.readlines()
    
    modified_lines = []
    deleted_count = 0
    renamed_count = 0
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check for JVM signature renames
        renamed = False
        for jvm_sig, canonical in JVM_TO_CANONICAL.items():
            if f"UNREACHABLE['{jvm_sig}']" in line:
                line = line.replace(f"'{jvm_sig}'", f"'{canonical}'")
                renamed = True
                renamed_count += 1
                print(f"Renamed: {jvm_sig} → {canonical}")
                break
        
        # Check for Glide entries to delete
        should_delete = False
        for method_to_delete in GLIDE_TO_DELETE:
            if f"UNREACHABLE['{method_to_delete}']" in line:
                # Skip this line and any continuation lines until we hit the next UNREACHABLE or end of dict
                print(f"Deleting UNREACHABLE entry: {method_to_delete}")
                should_delete = True
                deleted_count += 1
                break
        
        if should_delete:
            # Skip lines until we find the next line that starts a new entry or ends the dict
            while i < len(lines):
                current = lines[i]
                i += 1
                # Stop if we hit the next UNREACHABLE entry or closing brace
                if i < len(lines) and (lines[i].strip().startswith("'") or lines[i].strip().startswith('}')):
                    break
            continue
        
        modified_lines.append(line)
        i += 1
    
    with open(graph_path, 'w') as f:
        f.writelines(modified_lines)
    
    print(f"\nSummary:")
    print(f"  Renamed: {renamed_count} JVM signatures")
    print(f"  Deleted: {deleted_count} Glide UNREACHABLE entries")

if __name__ == '__main__':
    main()
