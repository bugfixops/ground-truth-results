#!/usr/bin/env python3
"""
Classify fake root framework-hop nodes into C1 (genuine entry), C2 (app-internal), or C3 (neither).
"""

import ast
import collections
import json
import re
import sys
import xml.etree.ElementTree as ET

GRAPH_DIR = 'graphs/AmazeFileManager'
MANIFEST = 'final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/AndroidManifest.xml'
METHOD_LIST = f'{GRAPH_DIR}/method_list.json'
FRAMEWORK_HOP_LIST = f'{GRAPH_DIR}/scratch/framework_hop_nodes.txt'
GRAPH_DEF = f'{GRAPH_DIR}/graph_def.py'

def load_framework_hops():
    hops = {}
    with open(FRAMEWORK_HOP_LIST) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('\t')
            if len(parts) >= 2:
                hops[parts[0].strip()] = parts[1].strip()
    return hops

def parse_manifest():
    """Extract genuine entry points from manifest"""
    tree = ET.parse(MANIFEST)
    root = tree.getroot()
    
    # Namespace handling
    ns = {'android': 'http://schemas.android.com/apk/res/android'}
    
    entries = {}
    
    # Application class
    app_elem = root.find('.//application')
    if app_elem is not None:
        app_name = app_elem.get('{http://schemas.android.com/apk/res/android}name')
        if app_name:
            # Convert to simple name
            simple_name = app_name.split('.')[-1]
            entries[f'{simple_name}.onCreate'] = ('C1_application', f'application android:name="{app_name}"', 0)
    
    # Activities with intent filters
    for activity in root.findall('.//activity'):
        name = activity.get('{http://schemas.android.com/apk/res/android}name')
        exported = activity.get('{http://schemas.android.com/apk/res/android}exported', 'false')
        
        if name:
            simple_name = name.split('.')[-1]
            intent_filters = activity.findall('intent-filter')
            
            if intent_filters or exported == 'true':
                # Lifecycle callbacks for this activity
                for cb in ['onCreate', 'onStart', 'onResume', 'onNewIntent']:
                    entries[f'{simple_name}.{cb}'] = ('C1_activity', f'activity android:name="{name}"', 0)
    
    # Services
    for service in root.findall('.//service'):
        name = service.get('{http://schemas.android.com/apk/res/android}name')
        exported = service.get('{http://schemas.android.com/apk/res/android}exported', 'false')
        
        if name:
            simple_name = name.split('.')[-1]
            if exported == 'true' or service.findall('intent-filter'):
                for cb in ['onCreate', 'onStartCommand', 'onBind']:
                    entries[f'{simple_name}.{cb}'] = ('C1_service', f'service android:name="{name}"', 0)
    
    # Receivers
    for receiver in root.findall('.//receiver'):
        name = receiver.get('{http://schemas.android.com/apk/res/android}name')
        exported = receiver.get('{http://schemas.android.com/apk/res/android}exported', 'false')
        
        if name:
            simple_name = name.split('.')[-1]
            if exported == 'true' or receiver.findall('intent-filter'):
                entries[f'{simple_name}.onReceive'] = ('C1_receiver', f'receiver android:name="{name}"', 0)
    
    return entries

def load_method_list():
    """Load method list and build class index"""
    rows = json.load(open(METHOD_LIST))
    
    # Build index of classes and their <init> methods
    classes_with_init = set()
    for row in rows:
        if row['name'] == '<init>':
            simple_class = row['class'].split('/')[-1]
            classes_with_init.add(simple_class)
    
    return rows, classes_with_init

def parse_edges():
    with open(GRAPH_DEF, 'r') as f:
        source = f.read()
    tree = ast.parse(source, GRAPH_DEF)
    
    edges = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            call = node.value
            if isinstance(call.func, ast.Name) and call.func.id == 'e':
                if len(call.args) >= 4:
                    try:
                        edges.append({
                            'src': ast.literal_eval(call.args[0]),
                            'dst': ast.literal_eval(call.args[1]),
                            'kind': ast.literal_eval(call.args[2]),
                            'evidence': ast.literal_eval(call.args[3]),
                            'lineno': node.lineno
                        })
                    except:
                        pass
    return edges

def extract_class(method_name):
    """Extract class name from method name"""
    if '.' not in method_name:
        return None
    parts = method_name.split('.')
    # Handle inner classes: Foo$Bar.method -> Foo$Bar
    class_part = parts[0]
    return class_part

def classify_fake_root(node_name, manifest_entries, classes_with_init):
    """Classify a fake root node as C1, C2, or C3"""
    
    # Check C1: manifest entry
    if node_name in manifest_entries:
        kind, evidence, line = manifest_entries[node_name]
        return 'C1', kind, evidence
    
    # Check C2: app-internal component with <init>
    class_name = extract_class(node_name)
    if class_name and class_name in classes_with_init:
        return 'C2', 'app_internal', f'{class_name}.<init> exists in method_list.json'
    
    # C3: neither
    return 'C3', 'no_entry_or_init', 'No manifest entry and no <init> in method_list.json'

def main():
    print("Loading framework-hop nodes...")
    framework_hops = load_framework_hops()
    
    print("Parsing manifest...")
    manifest_entries = parse_manifest()
    print(f"Found {len(manifest_entries)} manifest entries")
    
    print("Loading method list...")
    rows, classes_with_init = load_method_list()
    print(f"Found {len(classes_with_init)} classes with <init>")
    
    print("Parsing graph_def.py edges...")
    edges = parse_edges()
    
    # Build edge index
    incoming = collections.defaultdict(list)
    outgoing = collections.defaultdict(list)
    
    for edge in edges:
        incoming[edge['dst']].append(edge)
        outgoing[edge['src']].append(edge)
    
    # Identify fake roots (outgoing only, no incoming)
    fake_roots = []
    for hop_node in framework_hops:
        if hop_node not in incoming and hop_node in outgoing:
            fake_roots.append(hop_node)
    
    print(f"\nFound {len(fake_roots)} fake root nodes")
    
    # Classify each fake root
    classifications = []
    c1_count = 0
    c2_count = 0
    c3_count = 0
    
    for node in fake_roots:
        class_name = extract_class(node)
        category, kind, evidence = classify_fake_root(node, manifest_entries, classes_with_init)
        
        classifications.append({
            'node': node,
            'class': class_name,
            'category': category,
            'kind': kind,
            'evidence': evidence,
            'outgoing_edges': len(outgoing[node])
        })
        
        if category == 'C1':
            c1_count += 1
        elif category == 'C2':
            c2_count += 1
        else:
            c3_count += 1
    
    # Write classification report
    output_path = f'{GRAPH_DIR}/scratch/fake_root_classes.md'
    with open(output_path, 'w') as f:
        f.write('# Fake Root Classification\n\n')
        f.write(f'Total fake roots: {len(fake_roots)}\n\n')
        f.write(f'- C1 (genuine entry): {c1_count}\n')
        f.write(f'- C2 (app-internal): {c2_count}\n')
        f.write(f'- C3 (neither): {c3_count}\n\n')
        
        f.write('## C1: Genuine External Entry\n\n')
        f.write('| Node | Class | Kind | Evidence | Out Edges |\n')
        f.write('|------|-------|------|----------|----------|\n')
        for item in classifications:
            if item['category'] == 'C1':
                f.write(f"| {item['node']} | {item['class']} | {item['kind']} | {item['evidence']} | {item['outgoing_edges']} |\n")
        
        f.write('\n## C2: App-Internal Component\n\n')
        f.write('| Node | Class | Evidence | Out Edges |\n')
        f.write('|------|-------|----------|----------|\n')
        for item in classifications:
            if item['category'] == 'C2':
                f.write(f"| {item['node']} | {item['class']} | {item['evidence']} | {item['outgoing_edges']} |\n")
        
        f.write('\n## C3: Neither (Remove)\n\n')
        f.write('| Node | Class | Reason | Out Edges |\n')
        f.write('|------|-------|--------|----------|\n')
        for item in classifications:
            if item['category'] == 'C3':
                f.write(f"| {item['node']} | {item['class']} | {item['kind']} | {item['outgoing_edges']} |\n")
    
    print(f"\nClassification written to: {output_path}")
    print(f"\nSummary:")
    print(f"  C1 (genuine entry): {c1_count}")
    print(f"  C2 (app-internal): {c2_count}")
    print(f"  C3 (neither): {c3_count}")
    
    # Write JSON for programmatic use
    json_path = output_path.replace('.md', '.json')
    with open(json_path, 'w') as f:
        json.dump({
            'summary': {
                'total': len(fake_roots),
                'c1': c1_count,
                'c2': c2_count,
                'c3': c3_count
            },
            'classifications': classifications
        }, f, indent=2)
    
    print(f"JSON data written to: {json_path}")
    
    # Spot-check samples
    print("\n=== SPOT CHECK: 5 C1 samples ===")
    c1_samples = [item for item in classifications if item['category'] == 'C1'][:5]
    for item in c1_samples:
        print(f"\n{item['node']}:")
        print(f"  Evidence: {item['evidence']}")
    
    print("\n=== SPOT CHECK: 5 C2 samples ===")
    c2_samples = [item for item in classifications if item['category'] == 'C2'][:5]
    for item in c2_samples:
        print(f"\n{item['node']}:")
        print(f"  Class: {item['class']}")
        print(f"  Evidence: {item['evidence']}")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
