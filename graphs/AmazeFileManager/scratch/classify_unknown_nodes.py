#!/usr/bin/env python3
"""
Classify unknown nodes as FRAMEWORK-HOP or APP-AMBIGUOUS.
"""

import re
import json

def parse_unknown_nodes_from_build(build_file):
    """Extract all unique unknown node names from build errors"""
    unknown_nodes = set()
    
    with open(build_file, 'r') as f:
        for line in f:
            match = re.match(r'\s*ERROR\s+[^:]+:\s+unknown\s+(?:src|dst)\s+node\s+(.+)', line)
            if match:
                node_name = match.group(1).strip()
                unknown_nodes.add(node_name)
    
    return unknown_nodes

def load_method_list(method_list_file):
    """Load method_list.json to check which classes/methods exist"""
    try:
        with open(method_list_file, 'r') as f:
            methods = json.load(f)
        
        # Build a dict of class -> set of method names
        class_methods = {}
        all_method_shorts = set()
        
        for method_entry in methods:
            short = method_entry.get('short', '')
            all_method_shorts.add(short)
            
            # Parse "ClassName.methodName" or "ClassName.methodName(params)"
            if '.' in short:
                parts = short.split('.', 1)
                class_name = parts[0]
                method_name = parts[1].split('(')[0] if '(' in parts[1] else parts[1]
                
                if class_name not in class_methods:
                    class_methods[class_name] = set()
                class_methods[class_name].add(method_name)
        
        return class_methods, all_method_shorts
    except FileNotFoundError:
        print(f"Warning: Could not load {method_list_file}")
        return {}, set()

def classify_unknown_node(node_name, class_methods, all_methods):
    """Classify a node as FRAMEWORK-HOP or APP-AMBIGUOUS"""
    
    # Pseudo-nodes
    if node_name in ['LAUNCHER', 'FRAMEWORK', 'INTENT_FILTER', 'DialogPreference', 'S_ENTRY', 'S_MAIN', 'S_PREFS']:
        return 'FRAMEWORK-HOP', 'pseudo-node'
    
    # Extract class and method
    if '.' not in node_name:
        # Bare class name
        return 'FRAMEWORK-HOP', 'bare class name (no method)'
    
    parts = node_name.split('.')
    class_name = parts[0]
    method_base = parts[1].split('(')[0] if '(' in parts[1] else parts[1]
    
    # Check if class exists in app
    if class_name not in class_methods:
        # Framework classes
        framework_classes = ['Application', 'AndroidAsyncTask', 'AsyncTask', 'ActionMode', 'Context', 
                            'Drawable', 'Thread', 'RecyclerView', 'Parcelable', 'BaseSavedState',
                            'BroadcastReceiver', 'LayoutInflater', 'MediaScannerConnection', 'ImageLoader',
                            'InflaterInputStream', 'DeflaterOutputStream', 'ArrayList', 'HashMap',
                            'GridLayoutManager', 'AppCompatActivity', 'DrawerLayout', 'EventBus',
                            'ScheduledExecutorService', 'ViewTreeObserver', 'SevenMethodConfiguration',
                            'SubnetScanner', 'SmbFile', 'GlideListPreloader', 'CloudStreamServer',
                            'CloudStreamer', 'JVM']
        
        if any(class_name.startswith(fw) or class_name == fw for fw in framework_classes):
            return 'FRAMEWORK-HOP', f'framework class {class_name} not in method_list'
        else:
            # Could be app class with path prefix like "com/amaze/..."
            if '/' in class_name or 'com.amaze' in class_name:
                # Extract short class name
                short_class = class_name.split('/')[-1].split('.')[-1]
                if short_class in class_methods:
                    if method_base in class_methods[short_class]:
                        return 'APP-AMBIGUOUS', f'app class {short_class} has method {method_base}'
            return 'FRAMEWORK-HOP', f'class {class_name} not in method_list'
    
    # Class exists - check if method exists
    if method_base not in class_methods[class_name]:
        return 'FRAMEWORK-HOP', f'method {method_base} not declared in {class_name} (inherited/undeclared)'
    
    # Method exists - check if there are multiple overloads
    matching_overloads = [m for m in all_methods if m.startswith(f'{class_name}.{method_base}')]
    
    if len(matching_overloads) == 1:
        return 'APP-AMBIGUOUS', f'single method but referenced without full signature'
    elif len(matching_overloads) > 1:
        return 'APP-AMBIGUOUS', f'ambiguous: {len(matching_overloads)} overloads exist'
    else:
        return 'FRAMEWORK-HOP', f'method {method_base} exists but no signature match'

def main():
    build_file = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/build_repair_09.txt'
    method_list_file = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/method_list.json'
    
    print("Parsing unknown nodes from build...")
    unknown_nodes = parse_unknown_nodes_from_build(build_file)
    print(f"Found {len(unknown_nodes)} unique unknown nodes")
    
    print("\nLoading method_list.json...")
    class_methods, all_methods = load_method_list(method_list_file)
    print(f"Loaded {len(class_methods)} classes with methods")
    
    print("\nClassifying nodes...")
    framework_hop = []
    app_ambiguous = []
    
    for node in sorted(unknown_nodes):
        classification, reason = classify_unknown_node(node, class_methods, all_methods)
        if classification == 'FRAMEWORK-HOP':
            framework_hop.append((node, reason))
        else:
            app_ambiguous.append((node, reason))
    
    print(f"\n=== CLASSIFICATION RESULTS ===")
    print(f"FRAMEWORK-HOP: {len(framework_hop)}")
    print(f"APP-AMBIGUOUS: {len(app_ambiguous)}")
    
    print(f"\n=== FRAMEWORK-HOP nodes (first 20) ===")
    for node, reason in framework_hop[:20]:
        print(f"  {node:50s} | {reason}")
    
    print(f"\n=== APP-AMBIGUOUS nodes (first 20) ===")
    for node, reason in app_ambiguous[:20]:
        print(f"  {node:50s} | {reason}")
    
    # Write to files for next script
    with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/framework_hop_nodes.txt', 'w') as f:
        for node, reason in framework_hop:
            f.write(f"{node}\t{reason}\n")
    
    with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/app_ambiguous_nodes.txt', 'w') as f:
        for node, reason in app_ambiguous:
            f.write(f"{node}\t{reason}\n")
    
    print(f"\nWrote classification results to scratch/")

if __name__ == '__main__':
    main()
