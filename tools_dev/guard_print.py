#!/usr/bin/env python3
"""W7 judging aid (Kiro): prints PENDING flagged steps of an app in impact order (targets using the step), with
the edge's own trigger/guard text, the cited line and every guard line the pre-screen recorded (an earlier exit
is printed with the line before it, so its condition shows).
Usage, from the repo root: python3 -I tools_dev/guard_print.py <App> <offset> <count>
Steps already in graphs/<App>/scratch/reaudit/w7_judged.csv are skipped."""
import csv
import glob
import json
import os
import re
import sys

sys.path.insert(0, 'tools_dev')
from guard_prescreen import Sources  # noqa: E402

app, off, cnt = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
S = 'graphs/%s/scratch/reaudit/' % app
steps = {r['edge_id']: r for r in csv.DictReader(open(S + 'guard_steps.csv', encoding='utf-8'))}
judged = set()
if os.path.exists(S + 'w7_judged.csv'):
    judged = {r['step'] for r in csv.DictReader(open(S + 'w7_judged.csv', encoding='utf-8'))}
pend = [r for r in csv.DictReader(open(S + 'guard_decisions.csv', encoding='utf-8'))
        if r['decision'] == 'PENDING' and r['step'] not in judged]
pend.sort(key=lambda r: -int((steps.get(r['step']) or {}).get('targets') or 0))
pre = {e['id']: e for e in json.load(open(S + 'pre_w7_edges.json', encoding='utf-8'))}
g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % app)[0], encoding='utf-8'))
cur = {(e['src'], e['dst'], e['kind']): e for e in g['edges']}
byid = {e['id']: e for e in g['edges']}
src = Sources(app)
for r in pend[off:off + cnt]:
    s = steps.get(r['step'], {})
    e = byid.get(r['step']) or cur.get((r['src'], r['dst'], r['kind'])) or {}
    print('### %s %s %s -> %s  (targets %s)' % (r['step'], r['kind'], r['src'], r['dst'], s.get('targets')))
    print('    trigger: %s | guard: %s | env: %s | state: %s' % ((e.get('trigger') or '')[:90], (e.get('guard') or '')[:130],
                                                               (e.get('env') or '')[:40], (e.get('needs_state') or '')[:40]))
    print('    evidence: %s' % (e.get('evidence') or '')[:100])
    m = re.match(r'([\w/$.-]+\.java):(\d+)$', s.get('cited') or '')
    if not m:
        print('    (no app source line)')
        continue
    p = src.find(m.group(1))
    L = src.lines(p) if p else []
    shown = set()
    for gm in re.finditer(r'(?:^| \|\| )([^@|]+)@(\d+):', s.get('guard_text') or ''):
        kind, ln = gm.group(1), int(gm.group(2))
        if kind in ('try', 'finally'):
            continue
        rng = [ln - 1, ln] if kind.startswith('earlier') else [ln]
        for k in rng:
            if 0 < k <= len(L) and k not in shown:
                shown.add(k)
                print('    %5d %-16s %s' % (k, kind if k == ln else '', L[k - 1].strip()[:120]))
    n = int(m.group(2))
    if 0 < n <= len(L):
        print('    %5d %-16s %s' % (n, 'STEP', L[n - 1].strip()[:120]))
