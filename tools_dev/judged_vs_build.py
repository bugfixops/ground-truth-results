#!/usr/bin/env python3
"""Review 4 (Kiro): check that every STATE or ENV row of scratch/reaudit/w7_judged.csv is on the built edges.
Usage, from the repo root, after a fresh build: python3 -I tools_dev/judged_vs_build.py <App> [-v]
Rows are matched by (src, dst, kind); a row with a match= text only to the edges whose trigger contains it. Prints the rows whose
edges carry no gate of the row's type (a STATE row needs needs_state, an ENV row needs env) and the rows that match no edge."""
import csv, glob, json, sys
app = sys.argv[1]
g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % app)[0], encoding='utf-8'))
by = {}
for e in g['edges']:
    by.setdefault((e['src'], e['dst'], e['kind']), []).append(e)
none = nogate = n = 0
for r in csv.DictReader(open('graphs/%s/scratch/reaudit/w7_judged.csv' % app, encoding='utf-8')):
    if r['decision'] not in ('STATE', 'ENV'): continue
    n += 1
    es = by.get((r['src'], r['dst'], r['kind']), [])
    if r.get('match'): es = [e for e in es if r['match'] in (e.get('trigger') or '')]
    if not es:
        none += 1
        if '-v' in sys.argv: print('no edge:', r['step'], r['src'], '->', r['dst'], r['kind'])
        continue
    key = 'needs_state' if r['decision'] == 'STATE' else 'env'
    miss = [e for e in es if not e.get(key)]
    if miss:
        nogate += 1
        print('no %s gate:' % key, r['step'], r['src'], '->', r['dst'], r['kind'], '(%d of %d edges)' % (len(miss), len(es)))
print('%s: %d STATE/ENV rows, %d match no edge, %d with a bare edge' % (app, n, none, nogate))
