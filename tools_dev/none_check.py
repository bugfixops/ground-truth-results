#!/usr/bin/env python3
"""W7 check (Kiro, after the reviewer's round-2 check): for each NONE row of graphs/<App>/scratch/reaudit/w7_judged.csv,
count the targets whose current best route (out/methods.csv route_edge_ids) uses the step's edge and whose class is gui
or library (no env and no state on the route). A NONE row is only right when the step's guard holds in the baseline
or is a GUI action on that step; a gate on another edge does not count.
Usage: python3 -I tools_dev/none_check.py <App> [--all] [--covered]
  --all      print rows with 0 affected targets too
  --covered  only rows whose reason says the step is covered by a gate earlier on the route
Prints: step, affected targets, src -> dst, reason (cut)."""
import csv, glob, json, re, sys

app = sys.argv[1]
G = 'graphs/%s/' % app
g = json.load(open(glob.glob(G + 'out/*_trigger_graph.json')[0], encoding='utf-8'))
by_key = {}
for e in g['edges']:
    by_key.setdefault((e['src'], e['dst'], e['kind']), set()).add(e['id'])
uses = {}
for r in csv.DictReader(open(G + 'out/methods.csv', encoding='utf-8')):
    if r['verdict'] != 'REACHABLE' or r['env'] or r['state']:
        continue
    for eid in r['route_edge_ids'].split():
        uses.setdefault(eid, []).append(r['method'])
COV = re.compile(r'covered|already gated|gated upstream|gate earlier', re.I)
rows = []
for r in csv.DictReader(open(G + 'scratch/reaudit/w7_judged.csv', encoding='utf-8')):
    if r['decision'] != 'NONE':
        continue
    if '--covered' in sys.argv and not COV.search(r['text']):
        continue
    ids = by_key.get((r['src'], r['dst'], r['kind']), set())
    t = sorted({m for i in ids for m in uses.get(i, [])})
    rows.append((len(t), r['step'], r['src'], r['dst'], r['text']))
rows.sort(reverse=True)
bad = 0
for n, s, a, b, t in rows:
    if n or '--all' in sys.argv:
        print('%4d %s %s -> %s | %s' % (n, s, a[:45], b[:45], t[:90]))
    bad += 1 if n else 0
print('%s: %d NONE rows checked, %d with gui/library targets routed through them' % (app, len(rows), bad))
