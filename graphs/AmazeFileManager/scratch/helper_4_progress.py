#!/usr/bin/env python3
"""Track progress for helper 4"""
import json
import sys

# Load methods
with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/helper_4_methods.json', 'r') as f:
    methods_data = json.load(f)

# Load classes
with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/helper_4_classes.txt', 'r') as f:
    classes_list = [line.strip() for line in f if line.strip()]

# Count
total_methods = sum(len(methods) for methods in methods_data.values())
total_classes = len(methods_data)

print(f"Total classes: {total_classes}")
print(f"Total methods: {total_methods}")
print(f"\nClasses list total: {len(classes_list)}")

# Verify alignment
print(f"\nVerifying classes match...")
methods_classes = set(methods_data.keys())
list_classes = set(classes_list)

if methods_classes == list_classes:
    print("✓ Classes align perfectly")
else:
    print("✗ Mismatch!")
    print(f"  In methods but not list: {methods_classes - list_classes}")
    print(f"  In list but not methods: {list_classes - methods_classes}")
