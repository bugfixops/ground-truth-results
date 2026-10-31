#!/usr/bin/env python3
"""
Process blocker_group_4.txt and generate proposals for each blocker.

For each blocker, either:
(a) Propose real routes with e() edges (with printed source lines)
(b) Mark as UNREACHABLE with grep proof

Usage: python3 -I process_group_4.py
"""

import json
import os
import re
import subprocess
from pathlib import Path

# Paths
WORK_DIR = Path("/Users/darshan/Desktop/yang/work")
GRAPH_DIR = WORK_DIR / "graphs/AmazeFileManager"
APP_ROOT = WORK_DIR / "final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java"
FW_ROOT = WORK_DIR / "fw_src/android-8.1.0_r1"
BLOCKER_FILE = GRAPH_DIR / "scratch/final_label/blocker_group_4.txt"
OUTPUT_FILE = GRAPH_DIR / "scratch/final_label/blocker_props_4.md"

# Load method list
with open(GRAPH_DIR / "method_list.json") as f:
    method_list = json.load(f)
    print(f"Loaded {len(method_list)} methods")

# Create method lookup
method_by_short = {}
for m in method_list:
    short = m['short']
    if short not in method_by_short:
        method_by_short[short] = []
    method_by_short[short].append(m)

def find_java_file(class_path):
    """Find Java source file for a class path like com/amaze/filemanager/ui/dialogs/RenameBookmark"""
    # Try app source
    java_file = APP_ROOT / f"{class_path}.java"
    if java_file.exists():
        return java_file, "APP"
    
    # Try framework
    java_file = FW_ROOT / f"{class_path}.java"
    if java_file.exists():
        return java_file, "FW"
    
    return None, None

def read_source_lines(file_path, start=None, end=None):
    """Read lines from a source file"""
    try:
        with open(file_path) as f:
            lines = f.readlines()
            if start is None:
                return ''.join(lines)
            elif end is None:
                return lines[start-1].rstrip() if start <= len(lines) else ""
            else:
                return ''.join(lines[start-1:end]).rstrip()
    except Exception as e:
        return f"ERROR reading {file_path}: {e}"

def grep_in_app(pattern):
    """Grep for pattern in app source"""
    try:
        result = subprocess.run(
            ['grep', '-rn', pattern, str(APP_ROOT)],
            capture_output=True, text=True, timeout=10
        )
        return result.stdout
    except Exception as e:
        return f"ERROR: {e}"

def parse_blockers():
    """Parse blocker_group_4.txt"""
    with open(BLOCKER_FILE) as f:
        content = f.read()
    
    blocker_pattern = r'^(\S+) -> (\d+)$'
    lines = content.strip().split('\n')
    blockers = []
    current_blocker = None
    
    for line in lines:
        if line.startswith('#') or not line.strip():
            continue
        m = re.match(blocker_pattern, line)
        if m:
            if current_blocker:
                blockers.append(current_blocker)
            current_blocker = {'blocker': m.group(1), 'count': int(m.group(2)), 'dependents': []}
        elif line.strip() and current_blocker:
            current_blocker['dependents'].append(line.strip())
    
    if current_blocker:
        blockers.append(current_blocker)
    
    return blockers

def analyze_blocker(blocker_name):
    """Analyze a single blocker and return proposal"""
    
    # Special case: S_EDITTEXT_watch and other S_ screens
    if blocker_name.startswith('S_'):
        return analyze_screen_node(blocker_name)
    
    # Check if it's in method_list
    if blocker_name in method_by_short:
        methods = method_by_short[blocker_name]
        if len(methods) == 1:
            return analyze_method(methods[0], blocker_name)
        else:
            return {
                'status': 'AMBIGUOUS',
                'reason': f'Multiple overloads found ({len(methods)}), need disambiguation',
                'methods': [m['class'] + '.' + m['name'] + m['desc'] for m in methods]
            }
    
    # Not in method_list - might be inherited, framework, or pseudo-node
    return {
        'status': 'NOT_IN_METHOD_LIST',
        'reason': 'Not found in method_list.json - likely inherited, framework, or pseudo-node'
    }

def analyze_screen_node(screen_name):
    """Analyze a screen pseudo-node"""
    # These should be in SCREENS dict and have incoming edges
    return {
        'status': 'SCREEN_NODE',
        'proposal_type': 'a',
        'reason': f'{screen_name} is a pseudo-screen node that needs to be added to SCREENS dict and have incoming edges',
        'action': 'Add to SCREENS and create GUI edges from methods that trigger this screen/event'
    }

def analyze_method(method_info, short_name):
    """Analyze a method from method_list"""
    class_path = method_info['class']
    method_name = method_info['name']
    
    # Find source file
    java_file, location = find_java_file(class_path)
    
    if java_file is None:
        # No source found - check if it's library code
        if any(lib in class_path for lib in ['org/tukaani', 'org/apache', 'net/schmizz', 'jcifs', 'org/nanohttpd']):
            return {
                'status': 'LIBRARY_CODE',
                'proposal_type': 'unknown',
                'reason': f'Part of library package: {class_path.split("/")[0:3]}',
                'action': 'Determine if reachable through library usage or mark UNREACHABLE'
            }
        else:
            return {
                'status': 'NO_SOURCE',
                'reason': f'Source file not found for {class_path}'
            }
    
    return {
        'status': 'HAS_SOURCE',
        'proposal_type': 'a',
        'class': class_path,
        'method': method_name,
        'file': str(java_file),
        'location': location,
        'action': f'Read {java_file.name} to determine how {method_name} is called'
    }

def main():
    blockers = parse_blockers()
    print(f"\nFound {len(blockers)} blockers\n")
    
    # Analyze each blocker
    results = []
    for b in blockers:
        blocker_name = b['blocker']
        print(f"Analyzing: {blocker_name}")
        analysis = analyze_blocker(blocker_name)
        results.append({
            'blocker': blocker_name,
            'count': b['count'],
            'dependents': b['dependents'],
            'analysis': analysis
        })
    
    # Write summary
    with open(OUTPUT_FILE, 'w') as f:
        f.write("# Blocker Proposals for Group 4\n\n")
        f.write("STATUS: ANALYZED - ready for manual proposal creation\n\n")
        f.write(f"Total blockers: {len(blockers)}\n\n")
        f.write("## Summary by Status\n\n")
        
        # Group by status
        by_status = {}
        for r in results:
            status = r['analysis']['status']
            if status not in by_status:
                by_status[status] = []
            by_status[status].append(r)
        
        for status, items in sorted(by_status.items()):
            f.write(f"### {status}: {len(items)} blockers\n\n")
            for item in items:
                f.write(f"- {item['blocker']} ({item['count']} dependents)\n")
            f.write("\n")
        
        # Detailed analysis
        f.write("\n## Detailed Analysis\n\n")
        for i, r in enumerate(results, 1):
            f.write(f"### {i}. {r['blocker']} -> {r['count']} dependents\n\n")
            f.write(f"**Dependents:** {', '.join(r['dependents'])}\n\n")
            f.write(f"**Status:** {r['analysis']['status']}\n\n")
            
            if 'reason' in r['analysis']:
                f.write(f"**Reason:** {r['analysis']['reason']}\n\n")
            
            if 'action' in r['analysis']:
                f.write(f"**Action:** {r['analysis']['action']}\n\n")
            
            if 'file' in r['analysis']:
                f.write(f"**Source:** {r['analysis']['file']}\n\n")
            
            f.write("---\n\n")
    
    print(f"\nWrote analysis to {OUTPUT_FILE}")
    
    # Print summary
    print("\n## Status Summary:")
    for status, items in sorted(by_status.items()):
        print(f"  {status}: {len(items)}")

if __name__ == '__main__':
    main()
