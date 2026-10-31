"""One line per route step for the given methods (scratch helper; run from work/).

Usage: python3 -I graphs/AnyMemo/scratch/route_lines.py <Cls.method> ...
Reads out/anymemo_trigger_graph.json (edges by id) and out/methods.csv (route_edge_ids).
Prints: step, edge id, kind/class, src -> dst, guard, env, state, evidence (cut to 150 chars).
"""
import csv
import glob
import json
import sys

g = json.load(open(glob.glob('graphs/AnyMemo/out/*_trigger_graph.json')[0]))
by_id = {e['id']: e for e in g['edges']}
rows = {}
with open(glob.glob('graphs/AnyMemo/out/methods.csv')[0], newline='') as f:
    rdr = csv.DictReader(f)
    for r in rdr:
        rows[r.get('method') or r.get('name') or list(r.values())[0]] = r

for m in sys.argv[1:]:
    r = rows.get(m)
    if r is None:
        print('## %s: not in methods.csv' % m)
        continue
    ids = (r.get('route_edge_ids') or '').split()
    lab = g['labels'].get(m, {})
    print('## %s | %s | confirmed_by=%s | steps=%d | env=%s state=%s' % (
        m, r.get('status') or r.get('verdict') or '', lab.get('confirmed_by'), len(ids),
        lab.get('env'), lab.get('state')))
    for i, eid in enumerate(ids, 1):
        e = by_id[eid]
        env = ','.join(e.get('env_kinds') or []) or ('-' if not e.get('env') else 'Y')
        st = ','.join(e.get('state_kinds') or []) or ('-' if not e.get('needs_state') else 'Y')
        ev = (e.get('evidence') or '')[:150]
        print('%2d %s %s/%s %s -> %s | guard=%s | env=%s | state=%s | ev=%s' % (
            i, eid, e['kind'], e.get('edge_class'), e['src'], e['dst'],
            (e.get('guard') or '-')[:90], env, st, ev))
