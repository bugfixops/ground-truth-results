#!/usr/bin/env python3
"""
Delete all edges with unknown src or dst nodes and requeue them.
Parse the build errors, find the e() calls, requeue them, then delete them.
"""

import re
import sys

def parse_unknown_edges_from_build(build_file):
    """Extract all edge IDs and unknown node info from build errors"""
    unknown_edges = []
    
    with open(build_file, 'r') as f:
        for line in f:
            # Format: ERROR <EdgeID>: unknown src|dst node <NodeName>
            match = re.match(r'\s*ERROR\s+([^:]+):\s+unknown\s+(src|dst)\s+node\s+(.+)', line)
            if match:
                edge_id = match.group(1)
                src_or_dst = match.group(2)
                node_name = match.group(3).strip()
                unknown_edges.append((edge_id, src_or_dst, node_name))
    
    return unknown_edges

def find_edge_by_pattern(text, src_pattern=None, dst_pattern=None):
    """Find all e() calls matching src and/or dst pattern"""
    matching_edges = []
    
    # Pattern to match e('src', 'dst', ...) across multiple lines
    edge_pattern = r"e\('([^']*)',\s*'([^']*)',\s*'([^']*)',\s*'([^']*)'[^)]*\)"
    
    for match in re.finditer(edge_pattern, text, re.MULTILINE | re.DOTALL):
        src = match.group(1)
        dst = match.group(2)
        kind = match.group(3)
        desc = match.group(4)
        
        # Check if this edge matches our pattern
        if src_pattern and src == src_pattern:
            matching_edges.append((match.start(), match.end(), src, dst, kind, desc))
        elif dst_pattern and dst == dst_pattern:
            matching_edges.append((match.start(), match.end(), src, dst, kind, desc))
    
    return matching_edges

def delete_edges_with_unknown_nodes(text, unknown_nodes):
    """Delete all e() calls that reference any unknown node"""
    lines = text.split('\n')
    deleted_edges = []
    deleted_indices = set()
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if this line starts an e() call
        if line.strip().startswith('e('):
            # Collect the full e() call (may span multiple lines)
            edge_lines = [line]
            edge_start_idx = i
            paren_count = line.count('(') - line.count(')')
            j = i + 1
            
            while paren_count > 0 and j < len(lines):
                edge_lines.append(lines[j])
                paren_count += lines[j].count('(') - lines[j].count(')')
                j += 1
            
            edge_text = '\n'.join(edge_lines)
            edge_end_idx = j - 1
            
            # Check if this edge references any unknown node
            should_delete = False
            for node_name in unknown_nodes:
                # Match the node name in quotes
                if f"'{node_name}'" in edge_text:
                    should_delete = True
                    break
            
            if should_delete:
                # Extract edge info for requeueing
                quotes = re.findall(r"'([^']*)'", edge_text)
                if len(quotes) >= 4:
                    src, dst, kind, desc = quotes[0], quotes[1], quotes[2], quotes[3]
                    
                    # Extract evidence if present
                    evidence_match = re.search(r"evidence\s*=\s*'([^']*)'", edge_text)
                    evidence = evidence_match.group(1) if evidence_match else desc
                    
                    deleted_edges.append(('AUTO', src, dst, kind, evidence))
                
                # Mark these line indices for deletion
                for idx in range(edge_start_idx, edge_end_idx + 1):
                    deleted_indices.add(idx)
                
                i = j
                continue
        
        i += 1
    
    # Build new text without deleted lines
    new_lines = [line for idx, line in enumerate(lines) if idx not in deleted_indices]
    new_text = '\n'.join(new_lines)
    
    return new_text, deleted_edges

def main():
    graph_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py'
    build_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/build_repair_09.txt'
    requeue_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/requeue_from_repair.txt'
    
    print("Parsing unknown edge errors from build output...")
    unknown_edge_info = parse_unknown_edges_from_build(build_path)
    print(f"Found {len(unknown_edge_info)} unknown-node errors")
    
    # Extract unique unknown node names
    unknown_nodes = set(node_name for _, _, node_name in unknown_edge_info)
    print(f"Found {len(unknown_nodes)} unique unknown node names")
    
    print("\nReading graph_def.py...")
    with open(graph_path, 'r') as f:
        text = f.read()
    
    original_edge_count = text.count('\ne(')
    
    print("\nDeleting edges with unknown nodes...")
    new_text, deleted_edges = delete_edges_with_unknown_nodes(text, unknown_nodes)
    
    final_edge_count = new_text.count('\ne(')
    print(f"Deleted {original_edge_count - final_edge_count} edges")
    
    print("\nWriting updated graph_def.py...")
    with open(graph_path, 'w') as f:
        f.write(new_text)
    
    print(f"Appending {len(deleted_edges)} edges to requeue file...")
    with open(requeue_path, 'a') as f:
        for edge_id, src, dst, kind, evidence in deleted_edges:
            # Escape tabs in evidence
            evidence = evidence.replace('\t', ' ')
            f.write(f"{edge_id}\t{src}\t{dst}\t{kind}\t{evidence}\n")
    
    print("\nDone!")

if __name__ == '__main__':
    main()
