#!/usr/bin/env python3
"""
Extract edge details and print source context for repair_proposals/in_3.txt
"""

import json
import os
import re
import subprocess
import sys

WORK_DIR = '/Users/darshan/Desktop/yang/work'
GRAPH_DEF = f'{WORK_DIR}/graphs/AmazeFileManager/graph_def.py'
APP_SRC = f'{WORK_DIR}/final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java'
METHOD_LIST = f'{WORK_DIR}/graphs/AmazeFileManager/method_list.json'
IN_FILE = f'{WORK_DIR}/graphs/AmazeFileManager/scratch/repair_proposals/in_3.txt'

# Load method_list.json
with open(METHOD_LIST) as f:
    methods = json.load(f)

def param_names(desc):
    """'(Landroid/content/Context;I)Z' -> 'Context,int'"""
    JVM = {'I': 'int', 'J': 'long', 'Z': 'boolean', 'F': 'float', 'D': 'double',  
           'B': 'byte', 'C': 'char', 'S': 'short', 'V': 'void'}
    args, i, out = desc[1:desc.index(')')], 0, []
    while i < len(args):
        dims = 0
        while i < len(args) and args[i] == '[':
            dims += 1
            i += 1
        if i >= len(args):
            break
        if args[i] == 'L':
            j = args.index(';', i)
            name = args[i + 1:j].rsplit('/', 1)[-1].split('$')[-1]
            i = j + 1
        else:
            name = JVM.get(args[i], '?')
            i += 1
        out.append(name + '[]' * dims)
    return ','.join(out)

def find_candidates(node_name):
    """Find all methods in method_list.json that match the base name"""
    # Strip package prefix if present
    base = node_name.split('.')[-2] + '.' + node_name.split('.')[-1] if '.' in node_name else node_name
    
    # Handle different formats
    if '<init>' in base or '<clinit>' in base:
        class_part = base.split('.')[0]
        method_part = base.split('.')[-1]
    else:
        parts = base.rsplit('.', 1)
        if len(parts) == 2:
            class_part, method_part = parts
        else:
            return []
    
    candidates = []
    for m in methods:
        short = m['short']
        if method_part in short and class_part in short:
            param_str = param_names(m['desc'])
            if param_str:
                candidates.append(f"{short}({param_str})")
            else:
                candidates.append(short)
    
    return candidates

def print_source_lines(filepath, line_ranges):
    """Print source lines from file"""
    if not filepath:
        return "(no source file)"
    
    # Convert to full path - need to find the file in the package structure
    if not filepath.startswith('/'):
        # Try finding it
        cmd = f'find "{APP_SRC}" -name "{filepath}" -type f'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            filepath = result.stdout.strip().split('\n')[0]
        else:
            return f"(file not found: {filepath})"
    
    if not os.path.exists(filepath):
        return f"(file not found: {filepath})"
    
    output = []
    for line_range in line_ranges:
        if ':' in line_range:
            parts = line_range.split(':')
            fname = parts[0]
            lines = parts[1]
        else:
            lines = line_range
            fname = filepath
        
        if '-' in lines:
            start, end = lines.split('-')
            cmd = f'sed -n "{start},{end}p" "{filepath}"'
        elif ',' in lines:
            # Multiple line numbers
            line_nums = lines.split(',')
            output.append(f"\n{fname}:")
            for ln in line_nums:
                cmd = f'sed -n "{ln}p" "{filepath}"'
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    output.append(f"  {ln}: {result.stdout.rstrip()}")
            continue
        else:
            cmd = f'sed -n "{lines}p" "{filepath}"'
        
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            output.append(f"\n{fname}:{lines}:")
            output.append(result.stdout.rstrip())
    
    return '\n'.join(output) if output else "(no output)"

# Parse in_3.txt
edges_to_check = {}
with open(IN_FILE) as f:
    for line in f:
        if 'ERROR' in line and 'unknown' in line:
            parts = line.strip().split()
            edge_id = parts[1].rstrip(':')
            idx = line.find('node ')
            if idx > 0:
                node_name = line[idx+5:].strip()
                side = 'src' if 'unknown src' in line else 'dst'
                
                if edge_id not in edges_to_check:
                    edges_to_check[edge_id] = []
                edges_to_check[edge_id].append((side, node_name))

# Read graph_def.py and extract edges
print(f"Processing {len(edges_to_check)} unique edge IDs...")
print("=" * 80)

edge_data = {}
with open(GRAPH_DEF) as f:
    content = f.read()
    
    # Find all e(...) calls
    # Pattern: e('src', 'dst', 'KIND', 'description', evidence='...')
    pattern = r"e\('([^']+)',\s*'([^']+)',\s*'([^']+)',\s*'([^']+)'(?:,\s*evidence='([^']+)')?\)"
    
    for match in re.finditer(pattern, content):
        src, dst, kind, desc, evidence = match.groups()
        evidence = evidence or ''
        
        # Store for later lookup
        edge_key = f"{src}|{dst}|{kind}"
        if edge_key not in edge_data:
            edge_data[edge_key] = []
        edge_data[edge_key].append({
            'src': src, 'dst': dst, 'kind': kind, 
            'desc': desc, 'evidence': evidence
        })

# Process each edge
processed = 0
for edge_id, node_issues in sorted(edges_to_check.items()):
    print(f"\n{'='*80}")
    print(f"EDGE: {edge_id}")
    
    for side, node_name in node_issues:
        print(f"\n  Side: {side}")
        print(f"  Bad node: {node_name}")
        
        # Find candidates
        candidates = find_candidates(node_name)
        if candidates:
            print(f"\n  Candidates from method_list.json:")
            for c in candidates[:5]:  # Show first 5
                print(f"    - {c}")
            if len(candidates) > 5:
                print(f"    ... and {len(candidates)-5} more")
        else:
            print(f"  (No candidates found in method_list.json)")
        
        # Try to find the edge in graph_def
        # This is a heuristic since we don't have edge IDs in graph_def
        print(f"\n  Looking for edges with {side}={node_name}...")
        found = False
        for key, edge_list in edge_data.items():
            for edge in edge_list:
                if edge[side] == node_name:
                    print(f"    Found: {edge['src']} -> {edge['dst']} [{edge['kind']}]")
                    print(f"    Description: {edge['desc']}")
                    print(f"    Evidence: {edge['evidence']}")
                    
                    # Parse and print evidence
                    if edge['evidence'] and edge['evidence'] != 'INFERRED framework lifecycle':
                        if edge['evidence'].startswith('SRC '):
                            parts = edge['evidence'][4:].split(':')
                            if len(parts) >= 2:
                                filepath = parts[0]
                                line_spec = ':'.join(parts[1:])
                                lines = print_source_lines(filepath, [line_spec])
                                print(f"\n    Source context:")
                                print(lines)
                    
                    found = True
                    break
            if found:
                break
        
        if not found:
            print(f"    (Edge not found in graph_def.py - may use different node name)")
    
    processed += 1
    if processed >= 20:  # Limit output for first run
        print(f"\n\n... stopping after {processed} edges (first batch)")
        break

print(f"\n{'='*80}")
print(f"Processed {processed} edges")
