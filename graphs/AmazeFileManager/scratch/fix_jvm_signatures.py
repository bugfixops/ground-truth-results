#!/usr/bin/env python3
"""
Fix UNREACHABLE entries: Rename JVM signature forms to canonical names
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

def main():
    graph_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py'
    
    with open(graph_path, 'r') as f:
        text = f.read()
    
    renamed_count = 0
    for jvm_sig, canonical in JVM_TO_CANONICAL.items():
        if f"UNREACHABLE['{jvm_sig}']" in text:
            text = text.replace(f"'{jvm_sig}'", f"'{canonical}'", 1)  # Replace only first occurrence (the key)
            renamed_count += 1
            print(f"Renamed: {jvm_sig[:80]}... → {canonical}")
    
    with open(graph_path, 'w') as f:
        f.write(text)
    
    print(f"\nTotal renamed: {renamed_count} JVM signatures")

if __name__ == '__main__':
    main()
