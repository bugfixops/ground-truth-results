#!/usr/bin/env python3
"""Review of 6d94e9c4 item 2 aid (Kiro): sort the hits of kiro_scripts/cited_line_in_caller.py. Read-only.

Usage, from the repo root, on a fresh build:
    python3 -I tools_dev/cited_triage.py <App> > triage.txt
For each CALL edge whose first single-line SRC citation lies outside every method of the src name, it prints:
  BODY   the src method's body (all overloads, by the same indent heuristic) contains a call to the dst simple
         name ("name(" or "new Class("): the call is real; the citation only points elsewhere (callee definition,
         a supporting line). These are noise for the edge, but the citation can still be corrected.
  REAL   the body has no such call, and an edge from a node whose method holds the cited line (any variant,
         lambda or inner class of the same file) to the same dst exists: the edge is a wrong copy of that step.
  READ   neither: the source must be read by hand.
Each line: class, used-by count, id, src -> dst, cited file:line, the method that holds the line, hand/auto, the
first 120 characters of the evidence. The dst simple name is the part after the last '.', without '(...)'; for
<init> it is 'new <Class>'.
"""
import collections
import csv
import glob
import json
import os
import re
import sys

app = sys.argv[1]
ROOT = {'Aegis': 'Aegis/app', 'AmazeFileManager': 'AmazeFileManager/app', 'AnkiDroid': 'AnkiDroid/app',
        'LibreTorrent': 'LibreTorrent/app', 'MMEX': 'MMEX/app'}[app]
base = os.path.join('final_java_only', ROOT)
files = collections.defaultdict(list)
for p in glob.glob(base + '/**/*.java', recursive=True):
    files[os.path.basename(p)].append(p)
HDR = re.compile(r'^(\s*)(?:@\w+(?:\([^)]*\))?\s+)*(?:(?:public|private|protected|static|final|synchronized|abstract|native|default)\s+)*'
                 r'(?:<[^>]+>\s+)?[\w.<>\[\], ?]+\s+(\w+)\s*\([^;]*$')
cache = {}


def spans(path):
    if path in cache:
        return cache[path]
    L = open(path, encoding='utf-8', errors='replace').read().split('\n')
    out = collections.defaultdict(list)
    for i, l in enumerate(L):
        m = HDR.match(l)
        if not m:
            continue
        ind, name = len(m.group(1)), m.group(2)
        if name in ('if', 'for', 'while', 'switch', 'catch', 'return', 'new', 'else', 'synchronized'):
            continue
        j, seen = i, '{' in l
        while not seen and j < min(i + 6, len(L) - 1):
            j += 1
            seen = '{' in L[j]
        if not seen:
            continue
        k = j + 1
        while k < len(L) and not (len(L[k]) - len(L[k].lstrip()) == ind and L[k].lstrip().startswith('}')):
            k += 1
        out[name].append((i + 1, k + 1))
    cache[path] = (out, L)
    return cache[path]


g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % app)[0], encoding='utf-8'))
M = {r['method']: r for r in csv.DictReader(open('graphs/%s/out/methods.csv' % app, encoding='utf-8'))}
use = collections.Counter()
for r in M.values():
    for i in r['route_edge_ids'].split():
        use[i] += 1
by_dst = collections.defaultdict(list)
for e in g['edges']:
    by_dst[e['dst']].append(e)
rows = []
for e in g['edges']:
    if e['kind'] != 'CALL':
        continue
    s = e['src']
    if s.startswith('S_') or '<init>' in s or '<clinit>' in s or 'lambda$' in s or '@' in s:
        continue
    cls, _, mname = s.rpartition('.')
    if '$' in cls:
        continue
    mname = mname.split('(')[0]
    m = re.search(r'SRC (?:[\w/#.\-]+/)?([A-Za-z0-9_$]+\.java):(\d+)(?![\d-])(?!,)', e.get('evidence') or '')
    if not m:
        continue
    fn, ln = m.group(1), int(m.group(2))
    cand = [p for p in files.get(fn, []) if os.path.basename(p) == cls.split('.')[-1] + '.java'] or files.get(fn, [])
    if not cand:
        continue
    inside = any(a <= ln <= b for p in cand for (a, b) in spans(p)[0].get(mname, []))
    if inside or not any(mname in spans(p)[0] for p in cand):
        continue
    dcls, _, dm = e['dst'].rpartition('.')
    dm = dm.split('(')[0]
    pat = re.compile(r'new\s+%s\b' % re.escape(dcls.split('$')[-1])) if dm == '<init>' else re.compile(r'\b%s\s*\(' % re.escape(dm))
    holder, body_has = '?', False
    own = [p for p in files.get(cls.split('.')[-1] + '.java', [])]
    for p in own:
        sp, L = spans(p)
        for (a, b) in sp.get(mname, []):
            if any(pat.search(L[x - 1]) for x in range(a + 1, b + 1)):
                body_has = True
    for p in cand:
        sp, L = spans(p)
        best = sorted((b - a, nm) for nm, lst in sp.items() for (a, b) in lst if a <= ln <= b)
        if best:
            holder = best[0][1]
    stem = cls.split('.')[-1]
    other = [x for x in by_dst[e['dst']] if x['id'] != e['id'] and (holder != '?') and
             (x['src'].split('@')[0].endswith('.' + holder) or ('lambda$' + holder) in x['src']) and
             x['src'].split('.')[0].split('$')[0] == stem]
    kind = 'BODY' if body_has else ('REAL' if other else 'READ')
    rows.append((kind, use[e['id']], e['id'], s, e['dst'], '%s:%d' % (fn, ln), holder, 'auto' if e.get('auto') else 'hand',
                 (e.get('evidence') or '')[:120], ' '.join(x['id'] + ' ' + x['src'] for x in other[:2])))
c = collections.Counter(r[0] for r in rows)
print('%s: %d hits; %s' % (app, len(rows), dict(c)))
for r in sorted(rows, key=lambda r: (r[0], -r[1])):
    print('%s %4d %s %s -> %s | %s in %s | %s | %s || %s' % r)
