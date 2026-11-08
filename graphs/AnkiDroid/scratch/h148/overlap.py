import glob
import os
import re

BASE = '/Users/darshan/Desktop/yang/work/graphs/AnkiDroid'
methods = [m.strip() for m in open(os.path.join(BASE, 'scratch/h148/methods.txt')) if m.strip()]

md_hits = {m: [] for m in methods}
for path in sorted(glob.glob(os.path.join(BASE, 'parts/*.md'))):
    for ln, line in enumerate(open(path, encoding='utf-8'), 1):
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if not cells:
            continue
        first = cells[0]
        if first in md_hits:
            label = cells[1] if len(cells) > 1 else ''
            kind = cells[2] if len(cells) > 2 else ''
            md_hits[first].append((os.path.basename(path), ln, label, kind))

py_files = [os.path.join(BASE, 'graph_def.py')] + sorted(glob.glob(os.path.join(BASE, 'parts/*.py')))
py_hits = {m: [] for m in methods}
unreach_hits = {m: [] for m in methods}
edge_re = re.compile(r"e\(\s*'([^']*)'\s*,\s*'([^']*)'\s*,\s*'([^']*)'")
for path in py_files:
    for ln, line in enumerate(open(path, encoding='utf-8'), 1):
        for m in methods:
            if ("UNREACHABLE['%s']" % m) in line or ('UNREACHABLE["%s"]' % m) in line:
                unreach_hits[m].append((os.path.basename(path), ln, line.strip()[:160]))
        for mo in edge_re.finditer(line):
            src, dst, kind = mo.group(1), mo.group(2), mo.group(3)
            for m in methods:
                if dst == m:
                    py_hits[m].append((os.path.basename(path), ln, src, kind))

for m in methods:
    print('==', m)
    for h in md_hits[m]:
        print('   MD ', h[0], h[1], h[2], h[3])
    for h in unreach_hits[m]:
        print('   UNR', h[0], h[1], h[2])
    for h in py_hits[m]:
        print('   EDGE', h[0], h[1], h[2], '->', m, h[3])
