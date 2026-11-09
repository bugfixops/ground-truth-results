#!/usr/bin/env python3
"""W9 review aid (Kiro): print the drawn methods of audit_draw.csv with what decides their class. Read-only.

Usage, from the repo root, on a FRESH build (out/ of the commit is stale until the final CI):
    python3 -I tools_dev/audit_print.py <App> [<first> <count>]
For each drawn method: the graph class, the method's env and state texts, then every step of the best route that
carries an env gate, a state gate or a non-standard class, with its evidence, and the last two steps of the route.
The route ids are taken from the current out/methods.csv; a mismatch with the draw is printed as ROUTE CHANGED.
"""
import csv
import glob
import json
import sys

app = sys.argv[1]
first = int(sys.argv[2]) if len(sys.argv) > 2 else 0
count = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 6
G = 'graphs/%s/' % app
g = json.load(open(glob.glob(G + 'out/*_trigger_graph.json')[0], encoding='utf-8'))
E = {e['id']: e for e in g['edges']}
M = {r['method']: r for r in csv.DictReader(open(G + 'out/methods.csv', encoding='utf-8'))}
draw = list(csv.DictReader(open(G + 'scratch/reaudit/audit_draw.csv', encoding='utf-8')))


def short(x, n=170):
    x = (x or '').replace('\n', ' ')
    return x if len(x) <= n else x[:n] + '...'


for d in draw[first:first + count]:
    m = M.get(d['method'])
    print('#' * 100)
    if m is None:
        print(d['class'], d['order'], d['method'], 'NOT IN methods.csv')
        continue
    ids = m['route_edge_ids'].split()
    print('%s %s %s | verdict %s | steps %s' % (d['class'], d['order'], d['method'], m['verdict'], len(ids)))
    if ids != d['route_edge_ids'].split():
        print('  ROUTE CHANGED since the draw')
    print('  env  [%s] %s' % (m['env_kinds'], short(m['env'], 240)))
    print('  state[%s] %s' % (m['state_kinds'], short(m['state'], 240)))
    print('  classes %s | explicit_standard_route %s' % (m['route_edge_classes'], m['explicit_standard_route']))
    for i, eid in enumerate(ids, 1):
        x = E.get(eid)
        if x is None:
            print('  %2d %s MISSING' % (i, eid))
            continue
        gated = x.get('env') or x.get('needs_state') or x.get('edge_class') not in (None, 'explicit', 'standard', 'page')
        if gated or i > len(ids) - 2:
            print('  %2d %s %s -> %s [%s, %s]' % (i, eid, x['src'], x['dst'], x['kind'], x.get('edge_class')))
            if x.get('env'):
                print('       env: %s' % short(x['env']))
            if x.get('needs_state'):
                print('       state: %s' % short(x['needs_state']))
            if x.get('guard'):
                print('       guard: %s' % short(x['guard']))
            print('       ev: %s' % short(x.get('evidence'), 140))
