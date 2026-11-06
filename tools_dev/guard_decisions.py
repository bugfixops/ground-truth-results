#!/usr/bin/env python3
"""W7 decision table (Kiro). Usage, from the repo root, on the build that has the app's W7 edits:
    python3 -I tools_dev/guard_decisions.py <App>
Reads graphs/<App>/scratch/reaudit/guard_steps.csv (written by guard_prescreen.py on the pre-W7 build) and writes
graphs/<App>/scratch/reaudit/guard_decisions.csv with one row per flagged step (flag yes or no_source):
  STATE / ENV   the edge now carries a needs_state / env gate (the W6 or W7 block of graph_def.py wrote it);
  NONE          try and finally are the only blocks around the line and no other guard holds it (rule; no gate);
  STATE/ENV/NONE/DEAD from scratch/reaudit/w7_judged.csv (tools_dev/guard_judge.py) take precedence;
  PENDING       not judged yet.
Rows for hand decisions on edges the pre-screen does not list (ENTERS edges, steps of routes that changed) are
appended from the build: every edge whose needs_state or env text comes from a W7 block (tagged in the note or
listed in _W7_STATE) and is not already a row.
"""
import csv
import glob
import json
import sys

app = sys.argv[1]
S = 'graphs/%s/scratch/reaudit/' % app
g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % app)[0], encoding='utf-8'))
by_key = {}
for e in g['edges']:
    by_key.setdefault((e['src'], e['dst'], e['kind']), []).append(e)
pre = {e['id']: e for e in json.load(open(S + 'pre_w7_edges.json', encoding='utf-8'))}
cur_by_id = {e['id']: e for e in g['edges']}
steps = list(csv.DictReader(open(S + 'guard_steps.csv', encoding='utf-8')))
import os
judged = {}
if os.path.exists(S + 'w7_judged.csv'):
    judged = {r['step']: r for r in csv.DictReader(open(S + 'w7_judged.csv', encoding='utf-8'))}
out = []
seen = set()
for s in steps:
    if s['flag'] == 'no' and s['edge_id'] not in judged:
        continue
    p = pre.get(s['edge_id'])
    cur = cur_by_id.get(s['edge_id'])
    # same id: the gate text did not change; otherwise the edge that replaced it (same key, an id not in the pre build)
    now = [cur] if cur else [e for e in by_key.get((s['src'], s['dst'], s['kind']), []) if e['id'] not in pre]
    st = next((e for e in now if e.get('needs_state') and not (p or {}).get('needs_state')), None)
    ev = next((e for e in now if e.get('env') and not (p or {}).get('env')), None)
    j = judged.get(s['edge_id'])
    if j:
        dec, text, helper = j['decision'], j['text'] + (' (%s)' % j['ref'] if j['ref'] else ''), 'Kiro'
    elif ev:
        dec, text, helper = 'ENV', ev['env'], 'Kiro'
    elif st:
        dec, text, helper = 'STATE', st['needs_state'], 'Kiro'
    elif s['reason'] == 'only inside try/finally blocks':
        # only when try/finally are the ONLY enclosing blocks and no other guard (if, else, loop, switch, catch,
        # ?:, earlier exit) holds the line; guard_prescreen.py records every enclosing guard
        dec, text, helper = 'NONE', 'the call is in a try (or finally) body, which runs on the normal path; no other guard encloses it', 'rule:try-body'
    else:
        dec, text, helper = 'PENDING', '', ''
    out.append([s['edge_id'], s['kind'], s['src'], s['dst'], s['cited'], s['reason'], s['guard_line'], dec, text,
                helper, 'second: pending reviewer' if dec != 'PENDING' else ''])
    seen.add((s['src'], s['dst'], s['kind']))
for e in g['edges']:
    k = (e['src'], e['dst'], e['kind'])
    if k in seen:
        continue
    if e['id'] in pre:
        continue    # unchanged edge (same gate texts)
    p = next((x for x in pre.values() if (x['src'], x['dst'], x['kind']) == k
              and x['id'] not in cur_by_id), None)
    if p is None:
        continue
    if e.get('needs_state') and not p.get('needs_state'):
        out.append([e['id'], e['kind'], e['src'], e['dst'], '', 'hand decision (not in the pre-screen list)', '', 'STATE',
                    e['needs_state'], 'Kiro', 'second: pending reviewer'])
    elif e.get('env') and not p.get('env') and k not in seen:
        out.append([e['id'], e['kind'], e['src'], e['dst'], '', 'hand decision (not in the pre-screen list)', '', 'ENV',
                    e['env'], 'Kiro', 'second: pending reviewer'])
with open(S + 'guard_decisions.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['step', 'kind', 'src', 'dst', 'cited file:line', 'flag reason', 'guard line', 'decision', 'gate text or reason',
                'helper', 'auditor'])
    w.writerows(out)
import collections
print('%s: decision rows %d' % (app, len(out)), dict(collections.Counter(o[7] for o in out)))
