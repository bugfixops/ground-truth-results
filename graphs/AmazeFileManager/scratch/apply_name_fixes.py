#!/usr/bin/env python3
"""
Apply mechanical name fixes to graph_def.py based on name resolution JSON.

Fixes only resolved (unambiguous) mappings from categories b (overload/naming) and e (JVM signature).
Preserves all edge attributes (kind, guard, env, needs_state, evidence) - only changes node names.
"""

import json
import re
import sys

def main():
    resolution_file = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/build_resume_72_name_resolution.json'
    graph_def_file = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py'
    log_file = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/repair_log.md'
    
    # Load resolution data
    with open(resolution_file) as f:
        resolution_data = json.load(f)
    
    # Build mapping of bad_name -> canonical for fixable cases
    name_map = {}
    fixable_categories = ['b', 'e']  # overload/naming and JVM signature
    
    for name, info in resolution_data['resolutions'].items():
        if info['classification'] == 'resolved' and info['category'] in fixable_categories:
            name_map[name] = info['canonical']
    
    print(f'Loaded {len(name_map)} fixable name mappings')
    
    # Load graph_def.py
    with open(graph_def_file, encoding='utf-8') as f:
        content = f.read()
    
    # Track changes
    changes = []
    edge_pattern = re.compile(r"e\('([^']+)',\s*'([^']+)',")
    
    # Find all e() calls and track which ones need fixing
    edges_to_fix = []
    for match in edge_pattern.finditer(content):
        src = match.group(1)
        dst = match.group(2)
        start_pos = match.start()
        
        # Check if src or dst needs fixing
        src_fixed = name_map.get(src)
        dst_fixed = name_map.get(dst)
        
        if src_fixed or dst_fixed:
            edges_to_fix.append({
                'pos': start_pos,
                'src': src,
                'dst': dst,
                'src_fixed': src_fixed or src,
                'dst_fixed': dst_fixed or dst,
                'match': match
            })
    
    print(f'Found {len(edges_to_fix)} edges to fix')
    
    # Apply fixes from end to start (to preserve positions)
    new_content = content
    offset = 0
    
    for edge_info in sorted(edges_to_fix, key=lambda x: x['pos'], reverse=True):
        old_src = edge_info['src']
        old_dst = edge_info['dst']
        new_src = edge_info['src_fixed']
        new_dst = edge_info['dst_fixed']
        
        # Find the full e() call starting at this position
        # We need to replace just the src and dst arguments
        match_obj = edge_info['match']
        old_text = match_obj.group(0)
        
        # Replace src and dst in the matched text
        new_text = old_text
        if old_src != new_src:
            new_text = new_text.replace(f"'{old_src}'", f"'{new_src}'", 1)
            changes.append({
                'edge_id': 'unknown',  # We'll extract from context if needed
                'side': 'src',
                'old': old_src,
                'new': new_src,
                'category': 'b' if old_src in name_map else 'e'
            })
        
        if old_dst != new_dst:
            # Be careful with the replacement order
            if old_src == new_src:
                new_text = new_text.replace(f"'{old_dst}'", f"'{new_dst}'", 1)
            else:
                # After src was replaced, replace dst
                new_text = new_text.replace(f"'{old_dst}'", f"'{new_dst}'", 1)
            
            changes.append({
                'edge_id': 'unknown',
                'side': 'dst',
                'old': old_dst,
                'new': new_dst,
                'category': 'b' if old_dst in name_map else 'e'
            })
        
        # Apply the replacement
        pos = match_obj.start()
        end_pos = match_obj.end()
        new_content = new_content[:pos] + new_text + new_content[end_pos:]
    
    # Write updated graph_def.py
    with open(graph_def_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f'Applied {len(changes)} node name changes')
    
    # Write repair log
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write('# Phase 2a Mechanical Edge Fixes Repair Log\n\n')
        f.write(f'Total changes: {len(changes)}\n')
        f.write(f'Unique edges affected: ~{len(edges_to_fix)}\n\n')
        
        # Count by category
        cat_b = sum(1 for c in changes if c['category'] == 'b')
        cat_e = sum(1 for c in changes if c['category'] == 'e')
        f.write(f'Category breakdown:\n')
        f.write(f'- (b) Overload/naming fixes: {cat_b}\n')
        f.write(f'- (e) JVM signature fixes: {cat_e}\n\n')
        
        f.write('## Changes Applied\n\n')
        f.write('| Edge ID | Side | Old Name | New Name | Category |\n')
        f.write('|---------|------|----------|----------|----------|\n')
        
        for change in changes[:100]:  # Limit to first 100 for readability
            f.write(f"| {change['edge_id']} | {change['side']} | {change['old']} | {change['new']} | {change['category']} |\n")
        
        if len(changes) > 100:
            f.write(f'\n... and {len(changes) - 100} more changes\n')
    
    print(f'Wrote repair log to {log_file}')
    print(f'\nSummary:')
    print(f'  Edges fixed: {len(edges_to_fix)}')
    print(f'  Node name changes: {len(changes)}')
    print(f'  Category (b) overload/naming: {sum(1 for c in changes if c["category"] == "b")}')
    print(f'  Category (e) JVM signature: {sum(1 for c in changes if c["category"] == "e")}')
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
