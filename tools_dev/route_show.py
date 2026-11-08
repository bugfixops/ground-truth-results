#!/usr/bin/env python3
"""Review aid (Kiro): for each step id given, print its W7 reason, the gui/library targets whose built route uses the
step, and the built route of the first target step by step with guard and gates. Read-only.
Usage, from the repo root: python3 -I tools_dev/route_show.py <App> <step> [<step> ...]"""
import csv, glob, json, sys

app = sys.argv[1]
G = 'graphs/%s/' % app
g = json.load(open(glob.glob(G + 'out/*_trigger_graph.json')[0], encoding='utf-8'))
E = {e['id']: e for e in g['edges']}
by_key = {}
for e in g['edges']:
    by_key.setdefault((e['src'], e['dst'], e['kind']), set()).add(e['id'])
M = {r['method']: r for r in csv.DictReader(open(G + 'out/methods.csv', encoding='utf-8'))}
J = {r['step']: r for r in csv.DictReader(open(G + 'scratch/reaudit/w7_judged.csv', encoding='utf-8'))}
for s in sys.argv[2:]:
    r = J.get(s)
    if r is None:
        e = E[s]
        r = {'src': e['src'], 'dst': e['dst'], 'kind': e['kind'], 'text': '(not judged)'}
    ids = by_key.get((r['src'], r['dst'], r['kind']), set())
    t = sorted(m for m, x in M.items() if x['verdict'] == 'REACHABLE' and not x['env'] and not x['state']
               and ids & set(x['route_edge_ids'].split()))
    print('=' * 100)
    print(s, r['src'], '->', r['dst'], r['kind'], '| ids', sorted(ids))
    print('reason:', r['text'])
    print('targets (%d):' % len(t), ', '.join(t[:12]))
    if not t:
        continue
    for k, i in enumerate(M[t[0]]['route_edge_ids'].split(), 1):
        e = E[i]
        print('%3d%s %s %s -> %s [%s] %s' % (k, '*' if i in ids else ' ', i, e['src'][:50], e['dst'][:50], e['kind'],
                                             (e.get('trigger') or '')[:70]))
        if e.get('guard'):
            print('       guard:', str(e['guard'])[:120])
        if e.get('env') or e.get('needs_state'):
            print('       env:', str(e.get('env'))[:80], '| state:', str(e.get('needs_state'))[:80])
