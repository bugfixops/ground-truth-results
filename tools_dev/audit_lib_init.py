#!/usr/bin/env python3
"""W9 review aid (Kiro): for the drawn library rows, show why explicit_standard_route is 'no'. Read-only.

Usage, from the repo root, on a FRESH build:
    python3 -I tools_dev/audit_lib_init.py <App>
For each drawn library method: whether its own best route has a non-standard edge, then each <init> variant
of its class with its verdict, its route classes and the non-standard edges on that route (with their via).
With ESR_CREATION on, a callback whose class is created only through a non-standard edge counts as library.
"""
import csv
import glob
import json
import sys

app = sys.argv[1]
G = 'graphs/%s/' % app
g = json.load(open(glob.glob(G + 'out/*_trigger_graph.json')[0], encoding='utf-8'))
E = {e['id']: e for e in g['edges']}
M = {r['method']: r for r in csv.DictReader(open(G + 'out/methods.csv', encoding='utf-8'))}
draw = [d for d in csv.DictReader(open(G + 'scratch/reaudit/audit_draw.csv', encoding='utf-8')) if d['class'] == 'library']


def nonstd(ids):
    out = []
    for i, eid in enumerate(ids, 1):
        x = E.get(eid)
        if x and x.get('edge_class') not in (None, 'explicit', 'standard', 'page'):
            out.append('%d %s %s -> %s via %s' % (i, eid, x['src'], x['dst'], (x.get('via') or '')[:150]))
    return out


for d in draw:
    m = M.get(d['method'])
    print('#' * 90)
    print('library', d['order'], d['method'])
    if m is None:
        print('  NOT IN methods.csv')
        continue
    own = nonstd(m['route_edge_ids'].split())
    print('  own route non-standard edges:', len(own))
    for x in own:
        print('    ' + x)
    jc = m['jvm_class']
    inits = [r for r in M.values() if r['jvm_class'] == jc and r['method'].split('.')[-1].split('(')[0] == '<init>']
    if not inits:
        print('  class %s: no <init> rows (static or interface?)' % jc)
    for r in inits:
        ns = nonstd(r['route_edge_ids'].split())
        print('  %s %s esr=%s steps=%s nonstd=%d' % (r['method'], r['verdict'], r['explicit_standard_route'],
                                                     r['steps_from_launch'], len(ns)))
        for x in ns[:3]:
            print('    ' + x)
