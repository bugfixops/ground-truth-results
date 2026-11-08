#!/usr/bin/env python3
"""
Delete edges that reference unknown node names.
Match by the actual node names (src/dst) rather than edge IDs.
"""

import re
import sys

def extract_unknown_node_names(build_file):
    """Extract all unique unknown node names"""
    unknown_nodes = set()
    
    with open(build_file, 'r') as f:
        for line in f:
            if 'unknown src node' in line or 'unknown dst node' in line:
                parts = line.strip().split()
                if len(parts) >= 5:
                    # Everything after "node" is the node name
                    node_idx = parts.index('node')
                    node_name = ' '.join(parts[node_idx+1:])
                    unknown_nodes.add(node_name)
    
    return sorted(unknown_nodes)

def delete_edges_with_node(text, node_name):
    """Delete all e() calls that reference this node in src or dst position"""
    lines = text.split('\n')
    new_lines = []
    i = 0
    deleted_count = 0
    requeue_info = []
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this line starts an e() call
        if line.strip().startswith('e('):
            # Collect the full e() call (may span multiple lines)
            edge_lines = [line]
            paren_count = line.count('(') - line.count(')')
            j = i + 1
            
            while paren_count > 0 and j < len(lines):
                edge_lines.append(lines[j])
                paren_count += lines[j].count('(') - lines[j].count(')')
                j += 1
            
            edge_text = '\n'.join(edge_lines)
            
            # Check if this edge references the unknown node
            # Match patterns like e('nodename', or e(xxx, 'nodename',
            node_pattern = rf"['\"]({re.escape(node_name)})['\"]"
            
            if re.search(node_pattern, edge_text):
                # This edge references the unknown node - delete it
                deleted_count += 1
                
                # Extract info for requeueing
                quotes = re.findall(r"'([^']*)'", edge_text)
                if len(quotes) >= 3:
                    src, dst, kind = quotes[0], quotes[1], quotes[2]
                    evidence_match = re.search(r"evidence\s*=\s*'([^']*)'", edge_text)
                    evidence = evidence_match.group(1) if evidence_match else 'No evidence'
                    requeue_info.append((src, dst, kind, evidence))
                
                # Skip all lines of this edge
                i = j
                continue
        
        new_lines.append(line)
        i += 1
    
    new_text = '\n'.join(new_lines)
    return new_text, deleted_count, requeue_info

def main():
    graph_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py'
    build_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/build_repair_04.txt'
    requeue_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/requeue_from_repair.txt'
    
    print("Extracting unknown node names from build output...")
    unknown_nodes = extract_unknown_node_names(build_path)
    print(f"Found {len(unknown_nodes)} unique unknown node names")
    
    print("\nReading graph_def.py...")
    with open(graph_path, 'r') as f:
        text = f.read()
    
    original_edge_count = text.count('\ne(')
    total_deleted = 0
    all_requeue_info = []
    
    print("\nProcessing nodes (this may take a while)...")
    for idx, node_name in enumerate(unknown_nodes):  # Process ALL nodes
        if (idx + 1) % 50 == 0:
            print(f"  [{idx+1}/{len(unknown_nodes)}] Processing: {node_name[:60]}...")
        text, deleted, requeue_info = delete_edges_with_node(text, node_name)
        total_deleted += deleted
        all_requeue_info.extend(requeue_info)
    
    final_edge_count = text.count('\ne(')
    
    print(f"\nEdge count: {original_edge_count} → {final_edge_count} ({total_deleted} deleted)")
    
    print("\nWriting updated graph_def.py...")
    with open(graph_path, 'w') as f:
        f.write(text)
    
    print(f"Writing {len(all_requeue_info)} entries to requeue file...")
    with open(requeue_path, 'a') as f:
        for src, dst, kind, evidence in all_requeue_info:
            f.write(f"AUTO\t{src}\t{dst}\t{kind}\t{evidence}\n")
    
    print("\nDone!")

if __name__ == '__main__':
    main()
