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
# review 6 fix 1: the pattern now also catches the reasons that put the gate on another step ("is the state of the
# steps that ...", "the gate of E...", "gated on the earlier steps", "the gate sits on an upstream step")
COV = re.compile(r'is the (state|env|gate) of|(state|gate|env) of the steps?|the gate of E|gated (on|at|by) the earli|'
                 r'is gated (on|at|by)|gate (sits|is) on (the|an) (earlier|upstream)|covered|already gated|'
                 r'gated upstream|gate earlier', re.I)
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

# review 7 item 1 (structural test): a NONE row whose reason names another step id as carrying the gate is only
# right when that step is on the built route of every gui/library target that uses the row's step. The named step
# id is matched as its edge (src, dst, kind), so a step whose edge was split into copies (-2 suffix) still counts.
eid_key = {e['id']: (e['src'], e['dst'], e['kind']) for e in g['edges']}
key_ids = {}
for i, k in eid_key.items():
    key_ids.setdefault(k, set()).add(i)
routes = {}
for r in csv.DictReader(open(G + 'out/methods.csv', encoding='utf-8')):
    if r['verdict'] == 'REACHABLE' and not r['env'] and not r['state']:
        routes[r['method']] = set(r['route_edge_ids'].split())
STEP_ID = re.compile(r'\bE[0-9a-f]{8}\b')
# "as for E..." cites a row judged the same way (a like step elsewhere), not a step that carries this step's gate
LIKE = re.compile(r'as for (E[0-9a-f]{8}(?:(?:,| and) E[0-9a-f]{8})*)')
miss = 0
for r in csv.DictReader(open(G + 'scratch/reaudit/w7_judged.csv', encoding='utf-8')):
    if r['decision'] != 'NONE':
        continue
    like = {x for m in LIKE.findall(r['text']) for x in STEP_ID.findall(m)}
    named = [x for x in STEP_ID.findall(r['text']) if x != r['step'] and x in eid_key and x not in like]
    if not named:
        continue
    ids = by_key.get((r['src'], r['dst'], r['kind']), set())
    targets = sorted(m for m, ro in routes.items() if ids & ro)
    for x in named:
        xs = key_ids[eid_key[x]]
        off = [m for m in targets if not (xs & routes[m])]
        if off:
            miss += 1
            print('STRUCT %s names %s, not on the route of %d of %d gui/library targets: %s' % (
                r['step'], x, len(off), len(targets), ', '.join(off[:4])))
print('%s: structural test: %d named-gate steps missing from a gui/library route' % (app, miss))
