# W2 check for AmazeFileManager (Kiro). Usage, from the repo root:
#   python3 -I graphs/AmazeFileManager/scratch/reaudit/check_w2.py graphs/AmazeFileManager/out
# AmazeFileManager has no first-run screen (pages listed below; S_PERM is the
# storage permission prompt, a GUI action) and its two state texts are kept,
# so W2 changes nothing in the graph. The check confirms: every state text on
# a REACHABLE best route is decided in state_gates.csv; no page is a
# setup-only screen; SETUP_ONLY is empty, so the build report has no
# 'setup-only nodes' line (the builder prints it only when the set is not empty).
import collections
import csv
import json
import sys

outdir = sys.argv[1]
g = json.load(open(outdir + '/amazefilemanager_trigger_graph.json', encoding='utf-8'))
rows = list(csv.DictReader(open(outdir + '/methods.csv', encoding='utf-8')))
E = {e['id']: e for e in g['edges']}
dec = {r['needs_state']: r['decision'] for r in csv.DictReader(open(
    'graphs/AmazeFileManager/scratch/reaudit/state_gates.csv', encoding='utf-8'))}
fail = 0
cnt = collections.Counter()
for r in rows:
    if r['verdict'] != 'REACHABLE':
        continue
    for t in {(E.get(i) or {}).get('needs_state') for i in (r['route_edge_ids'] or '').split()} - {None}:
        cnt[t] += 1
undecided = [t for t in cnt if t not in dec]
print('1. state texts on REACHABLE best routes:', dict(cnt), '| undecided:', undecided)
fail += bool(undecided)
print('2. pages:', [s if isinstance(s, str) else s.get('id') for s in g['screens']])
rep = open(outdir + '/build_report.txt', encoding='utf-8').read()
ok = 'setup-only nodes' not in rep
print('3. SETUP_ONLY empty (no setup-only line in the build report):', ok)
fail += not ok
print('4. verdicts:', dict(collections.Counter(r['verdict'] for r in rows)))
print('RESULT:', 'FAIL' if fail else 'PASS')
