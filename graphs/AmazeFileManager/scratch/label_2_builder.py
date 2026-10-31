#!/usr/bin/env python3
"""Helper script to build label_2 outputs"""
import json
from datetime import datetime

# Load methods
with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/helper_2_methods.json') as f:
    methods_data = json.load(f)

# Known entry points and reachability
# MainActivity - LAUNCHER activity (entry point)
# PreferencesActivity - launched from MainActivity.Drawer
# AboutActivity - launched from PrefFrag when about preference clicked
# DatabaseViewerActivity - launched from FileUtils for .db files
# TextEditorActivity - has intent-filter for text/* mimetypes (system launches it)
# PermissionsActivity - superclass of MainActivity

# Track labels
md_rows = []
py_edges = []
unreachable_methods = {}

# Process each class
def add_reachable(method_name, reason, source):
    md_rows.append(f"| {method_name} | REACHABLE | | {reason} | {source} |")

def add_unreachable(method_name, kind, reason, source):
    md_rows.append(f"| {method_name} | UNREACHABLE | {kind} | {reason} | {source} |")
    class_method = method_name.replace('ActivityAbout', 'AboutActivity').replace('Dialog', 'Dialog')
    unreachable_methods[class_method] = (kind, reason, source, 'SOURCE')

# Count
total_methods = sum(len(m) for m in methods_data.values())
print(f"Total methods to label: {total_methods}")
print(f"Classes: {len(methods_data)}")

for cls, methods in methods_data.items():
    print(f"{cls}: {len(methods)} methods")
