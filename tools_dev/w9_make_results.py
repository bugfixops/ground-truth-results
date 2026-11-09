#!/usr/bin/env python3
"""W9 (Kiro): turn the per-row check notes into graphs/<App>/scratch/reaudit/audit_result.csv, on a FRESH build.

Usage, from the repo root:  python3 -I tools_dev/w9_make_results.py [<App> ...]
Input: graphs/<App>/scratch/reaudit/w9_check.txt, one line per drawn method:
    <class> <order> <method> ; A ... ; B ... ; <decision>
  decision 'correct', 'unclear (...)' or 'fix: ...' (any text after the last ';').
Result (W9 step 3): correct when the decision is correct, or a fix that left the class as drawn (a route fix);
fixed when the decision was a fix and the class on the current build differs from the drawn class; unclear when
the decision is unclear. (No row is wrong: every wrong label found was corrected in the graph.) ref is the first file:line in the B part, else in the A part, else
the method's source_ref, else (generated code) the nearest file:line on its route. source_read is yes when the B
part names a file:line and the row was a fix or unclear, or its B part is marked "(printed)": the checker printed
and read that source. Correct rows judged from the route's own evidence are source_read no.
"""
import csv
import glob
import json
import re
import sys

APPS = sys.argv[1:] or ['Aegis', 'AmazeFileManager', 'AnkiDroid', 'LibreTorrent', 'MMEX']
REF = re.compile(r'[\w$./-]+\.(?:java|xml):\d+(?:[-,]\d+)*')


def class_of(r):
    if r['verdict'] != 'REACHABLE':
        return 'UNREACHABLE'
    if [k for k in (r['env_kinds'] or '').split(';') if k and k != 'permission']:
        return 'env'
    if r['state_kinds']:
        return 'state'
    if r['explicit_standard_route'] == 'no':
        return 'library'
    return 'gui'


for app in APPS:
    G = 'graphs/%s/' % app
    M = {r['method']: r for r in csv.DictReader(open(G + 'out/methods.csv', encoding='utf-8'))}
    E = {e['id']: e for e in json.load(open(glob.glob(G + 'out/*_trigger_graph.json')[0], encoding='utf-8'))['edges']}
    draw = {(d['class'], d['order']): d for d in csv.DictReader(open(G + 'scratch/reaudit/audit_draw.csv', encoding='utf-8'))}
    out = []
    for line in open(G + 'scratch/reaudit/w9_check.txt', encoding='utf-8'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = [p.strip() for p in line.split(' ; ')]
        cls, order, method = parts[0].split(' ', 2)
        d = draw[(cls, order)]
        assert d['method'] == method, (app, cls, order, method, d['method'])
        a = next((p[2:] for p in parts[1:-1] if p.startswith('A ')), '')
        b = next((p[2:] for p in parts[1:-1] if p.startswith('B ')), '')
        dec = parts[-1]
        r = M[method]
        now = class_of(r)
        if dec.startswith('correct'):
            res = 'correct'
        elif dec.startswith('unclear'):
            res = 'unclear'
        else:
            assert dec.startswith('fix') or 'fix' in dec, (app, method, dec)
            res = 'fixed' if now != cls else 'correct'
        refs = REF.findall(b) or REF.findall(a)
        ref = refs[0] if refs else (r['source_ref'] or '').split(';')[0].strip()
        if not ref:   # generated code: the nearest file:line on the method's route, from the last step backwards
            for eid in reversed(r['route_edge_ids'].split()):
                hit = REF.findall((E.get(eid) or {}).get('evidence') or '')
                if hit:
                    ref = hit[0]
                    break
        note = dec if res != 'correct' or dec == 'correct' else dec + ' (class was right; route fixed)'
        if res == 'fixed':
            note = '%s; class now %s' % (dec, now)
        out.append({'app': app, 'class': cls, 'order': order, 'method': method, 'result': res,
                    'source_read': 'yes' if (REF.search(b) and (res != 'correct' or dec != 'correct' or '(printed)' in b)) else 'no',
                    'ref': ref, 'note': note,
                    'class_now': now})
    with open(G + 'scratch/reaudit/audit_result.csv', 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['app', 'class', 'order', 'method', 'result', 'source_read', 'ref', 'note', 'class_now'])
        w.writeheader()
        w.writerows(out)
    tally = {}
    for o in out:
        tally.setdefault(o['class'], {}).setdefault(o['result'], 0)
        tally[o['class']][o['result']] += 1
    print(app, len(out), tally)
