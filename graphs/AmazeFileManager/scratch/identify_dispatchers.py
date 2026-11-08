#!/usr/bin/env python3
"""Identify dispatcher framework-hop nodes (those with both incoming and outgoing edges)"""

import ast
import collections

GRAPH_DEF = 'graphs/AmazeFileManager/graph_def.py'
FRAMEWORK_HOP_LIST = 'graphs/AmazeFileManager/scratch/framework_hop_nodes.txt'

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

hops = load_framework_hops()
edges = parse_edges()

incoming = collections.defaultdict(list)
outgoing = collections.defaultdict(list)

for edge in edges:
    incoming[edge['dst']].append(edge)
    outgoing[edge['src']].append(edge)

dispatchers = []
for hop in hops:
    if hop in incoming and hop in outgoing:
        dispatchers.append((hop, len(incoming[hop]), len(outgoing[hop])))

print(f"Found {len(dispatchers)} dispatcher nodes:\n")
for hop, in_count, out_count in sorted(dispatchers):
    print(f"{hop}:")
    print(f"  Incoming: {in_count}")
    for edge in incoming[hop]:
        print(f"    {edge['src']} --{edge['kind']}--> {hop} (line {edge['lineno']})")
    print(f"  Outgoing: {out_count}")
    for edge in outgoing[hop]:
        print(f"    {hop} --{edge['kind']}--> {edge['dst']} (line {edge['lineno']})")
    print()
