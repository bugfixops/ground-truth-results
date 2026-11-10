#!/usr/bin/env python3
"""Round 2 cause C scan (Kiro, 2026-11-10): virtual-call edges into a base method that subtypes override.

For every never-run REACHABLE method C.m of the app (out/sanity_check.csv monkey_hit 0 and ape_hit 0), every edge
S -> C.m of kind CALL is listed when the same source S also has CALL edges to X.m (same simple name) for other classes
X: a dispatch fan-out, where C.m runs only for an object whose class is C itself or a subtype that does not override m.
The row says how many fan-out siblings there are and whether C is declared abstract or has a 'new C(' in the app
source; a person then reads whether any object that reaches S can run C.m (every created subtype overrides m and no
override calls super.m, or the only non-overriding subtypes never reach S). Confirmed rows go to round2_rules.py
(DEAD_DISPATCH) with file:line.
Usage, from the repo root:  python3 -I tools_dev/dispatch_scan.py <App>
Writes graphs/<App>/scratch/reaudit/dispatch_scan.csv."""
import collections
import csv
import glob
import json
import os
import re
import sys

app = sys.argv[1]
g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % app)[0], encoding='utf-8'))
san = {r['method']: r for r in csv.DictReader(open('graphs/%s/out/sanity_check.csv' % app, encoding='utf-8'))}
meth = {r['method']: r for r in csv.DictReader(open('graphs/%s/out/methods.csv' % app, encoding='utf-8'))}
src_text = {}
for p in glob.glob('final_java_only/%s/app/**/src/main/java/**/*.java' % app, recursive=True):
    src_text[p] = None


def never_run(m):
    s = san.get(m)
    return s is not None and str(s.get('monkey_hit', '0')) in ('0', '') and str(s.get('ape_hit', '0')) in ('0', '')


def name(m):
    return m.split('@')[0].split('(')[0].rsplit('.', 1)[-1]


def cls(m):
    return m.split('@')[0].split('(')[0].rsplit('.', 1)[0]


def grep(rx):
    hits = []
    for p in src_text:
        if src_text[p] is None:
            src_text[p] = open(p, encoding='utf-8', errors='replace').read()
        for i, l in enumerate(src_text[p].split('\n'), 1):
            if re.search(rx, l):
                hits.append('%s:%d' % (os.path.basename(p), i))
    return hits


out_by_src = collections.defaultdict(list)
for e in g['edges']:
    if e['kind'] == 'CALL':
        out_by_src[e['src']].append(e)
rows = []
for s, es in out_by_src.items():
    by_name = collections.defaultdict(list)
    for e in es:
        by_name[name(e['dst'])].append(e)
    for n, group in by_name.items():
        if len(group) < 2 or n.startswith('<') or n.startswith('lambda$'):
            continue
        for e in group:
            m = e['dst'].split('@')[0]
            if meth.get(m, {}).get('verdict') != 'REACHABLE' or not never_run(m):
                continue
            c = cls(m).split('$')[-1].split('.')[-1]
            sub = grep(r'\bextends\s+[\w.$]*\b%s\b' % re.escape(c))
            if not sub:
                continue
            new = grep(r'\bnew\s+[\w.]*\b%s\s*\(' % re.escape(c))
            abstract = grep(r'\babstract\s+class\s+%s\b' % re.escape(c))
            supr = grep(r'\bsuper\.%s\s*\(' % re.escape(n))
            rows.append([e['id'], s, m, len(group) - 1, len(sub), 'yes' if abstract else 'no',
                         ' '.join(new[:4]) or '-', ' '.join(supr[:4]) or '-', (e.get('evidence') or '')[:100]])
path = 'graphs/%s/scratch/reaudit/dispatch_scan.csv' % app
with open(path, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['edge', 'src', 'base_method', 'siblings', 'subclasses', 'abstract', 'new_base', 'super_calls', 'evidence'])
    w.writerows(rows)
print('%s: %d dispatch edges into a never-run base method with subclasses (%d methods)' % (
    app, len(rows), len({r[2] for r in rows})))
