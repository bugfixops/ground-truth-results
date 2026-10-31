import glob
import os

ROOT = '/Users/darshan/Desktop/yang/work/graphs/AnkiDroid'
row = None
with open(ROOT + '/scratch/batches_ai.tsv', encoding='utf-8') as fh:
    for line in fh:
        f = line.rstrip('\n').split('\t')
        if f and f[0] == '149':
            row = f
            break
methods = row[3].split(';')

md_rows = {}
for p in sorted(glob.glob(ROOT + '/parts/*.md')):
    with open(p, encoding='utf-8', errors='replace') as fh:
        for i, ln in enumerate(fh, 1):
            if not ln.startswith('|'):
                continue
            cells = [c.strip() for c in ln.strip().strip('|').split('|')]
            if len(cells) < 2:
                continue
            md_rows.setdefault(cells[0], []).append((os.path.basename(p), i, cells[1] if len(cells) > 1 else '',
                                                    cells[2] if len(cells) > 2 else '',
                                                    cells[4] if len(cells) > 4 else ''))

for m in methods:
    hits = md_rows.get(m, [])
    # also loose matches on base name without parameter list
    base = m.split('(')[0]
    if base != m:
        hits = hits + md_rows.get(base, [])
    print('==', m)
    if not hits:
        print('   no md row with exact first cell')
    for fn, ln, lab, kind, ref in hits:
        print('   %s:%d | %s | %s | %s' % (fn, ln, lab, kind, ref[:110]))
