import glob
import os

os.chdir('/Users/darshan/Desktop/yang/work')
row = None
with open('graphs/AnkiDroid/scratch/batches_ai.tsv', encoding='utf-8') as fh:
    for line in fh:
        f = line.rstrip('\n').split('\t')
        if f[0] == '147':
            row = f
            break
methods = row[3].split(';')
print('count', len(methods))
files = (sorted(glob.glob('graphs/AnkiDroid/parts/*.md'))
         + ['graphs/AnkiDroid/graph_def.py']
         + sorted(glob.glob('graphs/AnkiDroid/parts/*.py')))
texts = {}
for fn in files:
    with open(fn, encoding='utf-8') as fh:
        texts[fn] = fh.read().split('\n')
for m in methods:
    base = m.split('(')[0]
    print('==', m, '| base:', base)
    for fn in files:
        for i, l in enumerate(texts[fn], 1):
            if base in l:
                print('  %s:%d: %s' % (os.path.basename(fn), i, l.strip()[:170]))
