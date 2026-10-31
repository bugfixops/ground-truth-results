import glob
import os
import re

ROOT = '/Users/darshan/Desktop/yang/work/graphs/AnkiDroid'
row = None
with open(ROOT + '/scratch/batches_ai.tsv', encoding='utf-8') as fh:
    for line in fh:
        f = line.rstrip('\n').split('\t')
        if f and f[0] == '149':
            row = f
            break
assert row is not None
classes = row[2].split(';')
methods = row[3].split(';')
print('part', row[0], 'n_declared', row[1], 'n_methods', len(methods), 'n_classes', len(classes))

sources = []
for p in sorted(glob.glob(ROOT + '/parts/*.md')) + sorted(glob.glob(ROOT + '/parts/*.py')):
    sources.append(p)
sources.append(ROOT + '/graph_def.py')

texts = {}
for p in sources:
    with open(p, encoding='utf-8', errors='replace') as fh:
        texts[p] = fh.read().split('\n')

for m in methods:
    base = m.split('(')[0]
    hits = []
    for p, lines in texts.items():
        if p.endswith('graph_def.py') or p.endswith('.py'):
            pass
        for i, ln in enumerate(lines, 1):
            if base in ln:
                short = os.path.basename(p)
                hits.append((short, i))
    # keep unique file names with first lines
    byfile = {}
    for short, i in hits:
        byfile.setdefault(short, []).append(i)
    summary = '; '.join('%s:%s' % (k, ','.join(str(x) for x in v[:6]) + ('...' if len(v) > 6 else ''))
                        for k, v in byfile.items())
    print(m, '|', summary if summary else 'NO HITS')
