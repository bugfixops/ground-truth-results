#!/usr/bin/env python3
"""
Process a chunk of UNREACHABLE-with-incoming-edges warnings.
For each method, determine if it should become REACHABLE or stay UNREACHABLE.
"""

import json
import re
import subprocess
import sys

if len(sys.argv) < 3:
    print("Usage: python3 process_unreachable_chunk.py <start_idx> <end_idx>")
    sys.exit(1)

start_idx = int(sys.argv[1])
end_idx = int(sys.argv[2])

# Load trigger graph
print(f"Loading trigger graph for chunk {start_idx}-{end_idx}...")
with open('graphs/AmazeFileManager/out/amazefilemanager_trigger_graph.json') as f:
    graph = json.load(f)

edges_by_id = {e['id']: e for e in graph['edges']}
edges_by_dst = {}
for e in graph['edges']:
    dst = e['dst']
    if dst not in edges_by_dst:
        edges_by_dst[dst] = []
    edges_by_dst[dst].append(e)

# Parse warnings
warnings = []
with open('graphs/AmazeFileManager/scratch/unreachable_warnings.txt') as f:
    for line in f:
        match = re.search(r'(\S+) is UNREACHABLE but has incoming edges \[(.*?)\]', line)
        if match:
            method = match.group(1)
            edge_ids = [e.strip("' ") for e in match.group(2).split(',')]
            warnings.append((method, edge_ids))

# Process chunk
chunk = warnings[start_idx:end_idx]
print(f"Processing {len(chunk)} methods...")

decisions = []
for method, edge_ids in chunk:
    print(f"\nChecking {method} ({len(edge_ids)} incoming edges)...")
    
    # Get incoming edges
    incoming_sources = []
    for edge_id in edge_ids:
        if edge_id in edges_by_id:
            edge = edges_by_id[edge_id]
            incoming_sources.append({
                'id': edge_id,
                'src': edge['src'],
                'evidence': edge.get('evidence', ''),
                'kind': edge.get('kind', '')
            })
    
    # Collect unique sources
    unique_sources = list(set([e['src'] for e in incoming_sources]))
    
    decision = {
        'method': method,
        'edge_count': len(edge_ids),
        'unique_sources': unique_sources,
        'source_count': len(unique_sources),
        'edges': incoming_sources[:10],  # Store first 10 for reference
        'action': 'ANALYZE',  # To be determined by human review
        'reason': 'Needs source inspection'
    }
    
    decisions.append(decision)

# Save decisions to JSON
output_file = f'graphs/AmazeFileManager/scratch/unreachable_chunk_{start_idx}_{end_idx}.json'
with open(output_file, 'w') as f:
    json.dump(decisions, f, indent=2)

print(f"\nSaved {len(decisions)} decisions to {output_file}")

# Print summary
print(f"\nSummary:")
print(f"  Methods analyzed: {len(decisions)}")
print(f"  Total incoming edges: {sum(d['edge_count'] for d in decisions)}")
print(f"  Avg sources per method: {sum(d['source_count'] for d in decisions) / len(decisions):.1f}")
