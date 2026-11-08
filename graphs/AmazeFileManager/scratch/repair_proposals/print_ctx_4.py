#!/usr/bin/env python3
"""
Print context for edges in in_4.txt
For each edge ID, extract from graph_def.py and print source evidence
"""

import json
import re
import subprocess
import sys

APP_SRC = "final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java"
FW_SRC = "fw_src/android-8.1.0_r1"

# Load data
with open('graphs/AmazeFileManager/method_list.json') as f:
    methods = json.load(f)

with open('graphs/AmazeFileManager/scratch/build_resume_72_name_resolution.json') as f:
    resolutions = json.load(f)['resolutions']

with open('graphs/AmazeFileManager/auto_calls.json') as f:
    auto_calls = json.load(f)['calls']

# Parse in_4.txt
edge_issues = {}
with open('graphs/AmazeFileManager/scratch/repair_proposals/in_4.txt') as f:
    for line in f:
        m = re.match(r'ERROR (E[0-9a-f-]+): unknown (src|dst) node (.+)$', line.strip())
        if m:
            edge_id, side, bad_name = m.groups()
            if edge_id not in edge_issues:
                edge_issues[edge_id] = {}
            edge_issues[edge_id][side] = bad_name

def find_edge_in_graph(edge_id, bad_name):
    """Find the e(...) call in graph_def.py that has this edge_id or this bad name"""
    # First try to find by searching for the bad name in src or dst position
    try:
        # Search for lines with the bad name as src or dst
        result = subprocess.run(
            ['grep', '-n', f"'{bad_name}'", 'graphs/AmazeFileManager/graph_def.py'],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            # Look for e( calls
            for line in lines:
                if 'e(' in line:
                    line_num = line.split(':')[0]
                    # Get context around this line
                    ctx_result = subprocess.run(
                        ['sed', '-n', f'{line_num},+10p', 'graphs/AmazeFileManager/graph_def.py'],
                        capture_output=True, text=True, timeout=5
                    )
                    if ctx_result.returncode == 0:
                        # Check if this is the right edge by looking for evidence
                        return ctx_result.stdout
    except:
        pass
    return None

def extract_evidence_from_edge_def(edge_text):
    """Extract evidence string from e(...) call"""
    # Look for evidence='...' or evidence="..."
    match = re.search(r"evidence\s*=\s*['\"]([^'\"]+)['\"]", edge_text, re.DOTALL)
    if match:
        return match.group(1)
    # Try multiline
    match = re.search(r"evidence\s*=\s*['\"](.+?)['\"]", edge_text, re.DOTALL)
    if match:
        return match.group(1)
    return None

def extract_file_lines(evidence):
    """Extract file:line references from evidence"""
    # Pattern: path/file.java:lines
    pattern = r'([a-zA-Z_/$0-9.#-]+\.java):(\d+(?:-\d+)?(?:,\s*\d+(?:-\d+)?)*)'
    matches = re.findall(pattern, evidence)
    return matches

def print_source_lines(file_path, line_spec):
    """Print source lines using sed"""
    parts = re.split(r',\s*', line_spec)
    output = []
    
    for part in parts:
        if '-' in part:
            start, end = part.split('-')
            cmd = ['sed', '-n', f'{start},{end}p', file_path]
        else:
            cmd = ['sed', '-n', f'{part}p', file_path]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
            if result.returncode == 0 and result.stdout.strip():
                output.append(f"{file_path}:{part}")
                for line in result.stdout.strip().split('\n'):
                    output.append(f"  {line}")
        except:
            output.append(f"Could not read {file_path}:{part}")
    
    return '\n'.join(output) if output else "No source"

def get_candidates(bad_name):
    """Get canonical candidates for bad name"""
    res = resolutions.get(bad_name, {})
    canonical = res.get('canonical')
    candidates = res.get('candidates', [])
    
    if canonical:
        return [canonical]
    return candidates

def find_matching_auto_call(src_name, file_name, line_num):
    """Find auto_calls entry matching src, file, line"""
    for call in auto_calls:
        if call.get('file') == file_name and call.get('line') == line_num:
            if call.get('src', '').startswith(src_name.split('(')[0]):
                return call
    return None

# Process all edges
print("=" * 80)
print("EDGE CONTEXT REPORT FOR in_4.txt")
print("=" * 80)

for edge_id in sorted(edge_issues.keys()):
    issues = edge_issues[edge_id]
    print(f"\nEdge: {edge_id}")
    print(f"Issues: {issues}")
    
    # Try to find edge in graph_def.py using the bad name
    for side, bad_name in issues.items():
        print(f"\n  {side.upper()}: {bad_name}")
        
        edge_def = find_edge_in_graph(edge_id, bad_name)
        if edge_def:
            print(f"\n  Edge definition found:")
            print("  " + edge_def[:500].replace('\n', '\n  '))
            
            evidence = extract_evidence_from_edge_def(edge_def)
            if evidence:
                print(f"\n  Evidence: {evidence[:200]}")
                
                file_lines = extract_file_lines(evidence)
                if file_lines:
                    print(f"\n  Source citations: {len(file_lines)}")
                    for file_ref, line_spec in file_lines:
                        # Determine full path
                        if 'FW-SRC' in evidence or file_ref.startswith('core/'):
                            file_path = f"{FW_SRC}/{file_ref}"
                        else:
                            if not file_ref.startswith('com/'):
                                file_path = f"{APP_SRC}/com/amaze/filemanager/{file_ref}"
                            else:
                                file_path = f"{APP_SRC}/{file_ref}"
                        
                        print(f"\n  {print_source_lines(file_path, line_spec)}")
        
        # Show candidates
        candidates = get_candidates(bad_name)
        if candidates:
            print(f"\n  Candidates for {bad_name}:")
            for i, cand in enumerate(candidates, 1):
                print(f"    {i}. {cand}")

print("\n" + "=" * 80)
