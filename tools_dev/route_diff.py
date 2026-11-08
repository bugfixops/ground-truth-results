#!/usr/bin/env python3
"""W8 point 2 (Kiro): print the sampled routes whose best route changed since they were verified.
Usage: python3 -I tools_dev/route_diff.py <App> [--all] [--only METHOD]
For each non-DEVICE path row of graphs/<App>/verification.csv whose edges differ from the method's current
route_edge_ids in graphs/<App>/out/methods.csv, prints the old and new step lists; a step that was not on the
verified route is marked NEW and printed with its trigger, guard, gates and evidence (those are the steps to check).
Steps kept from the verified route were checked then. Read-only."""
import csv, json, glob, sys

app = sys.argv[1]
show_all = '--all' in sys.argv
only = sys.argv[sys.argv.index('--only') + 1] if '--only' in sys.argv else None
G = 'graphs/%s/' % app
methods = {r['method']: r for r in csv.DictReader(open(G + 'out/methods.csv', encoding='utf-8'))}
g = json.load(open(glob.glob(G + 'out/*_trigger_graph.json')[0], encoding='utf-8'))
E = {x['id']: x for x in g['edges']}
rows = [r for r in csv.DictReader(open(G + 'verification.csv', encoding='utf-8'))
        if r['type'] == 'path' and r['confirmed_by'] != 'DEVICE']
n_changed = 0
for r in rows:
    m = r['item']
    if only and m != only:
        continue
    old = r['edges'].split()
    cur = methods.get(m)
    new = cur['route_edge_ids'].split() if cur else []
    if old == new and not show_all:
        continue
    n_changed += 1
    print('=' * 100)
    print('%s  [old verdict %s, %d steps -> %d steps; now %s]' % (
        m, r['result'], len(old), len(new), cur['verdict'] if cur else 'ABSENT'))
    if cur:
        print('  class now: env=%s | state=%s' % ((cur['env'] or '-')[:90], (cur['state'] or '-')[:90]))
    olds = set(old)
    for i, eid in enumerate(new, 1):
        x = E.get(eid)
        if not x:
            print('  %2d %s MISSING FROM GRAPH' % (i, eid))
            continue
        tag = '   ' if eid in olds else 'NEW'
        print('  %2d %s %s %s -> %s [%s]' % (i, tag, eid, x['src'], x['dst'], x['kind']))
        if tag == 'NEW':
            for k in ('trigger', 'guard', 'needs_state', 'env', 'evidence', 'note'):
                if x.get(k):
                    print('         %s: %s' % (k, str(x[k])[:220]))
    dropped = [e for e in old if e not in set(new)]
    if dropped:
        print('  dropped from the verified route: %s' % ' '.join(dropped))
print('%s: %d of %d sampled routes changed' % (app, n_changed, len(rows)))
