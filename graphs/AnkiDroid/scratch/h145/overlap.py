import glob, os, re, sys

BASE = '/Users/darshan/Desktop/yang/work/graphs/AnkiDroid'
ROW = os.path.join(BASE, 'scratch/h145/rows.txt')
methods = [l.strip() for l in open(ROW, encoding='utf-8') if l.strip()]

md_files = sorted(glob.glob(os.path.join(BASE, 'parts', '*.md')))
py_files = sorted(glob.glob(os.path.join(BASE, 'parts', '*.py')))
gd = os.path.join(BASE, 'graph_def.py')

def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]

out = []
for m in methods:
    out.append('=== ' + m)
    # md rows whose first cell equals the method (label rows)
    for f in md_files:
        for i, line in enumerate(open(f, encoding='utf-8'), 1):
            if not line.startswith('|'):
                continue
            c = cells(line)
            if c and c[0] == m:
                lab = c[1] if len(c) > 1 else ''
                kind = c[2] if len(c) > 2 else ''
                out.append('  MD %s:%d | %s | %s' % (os.path.basename(f), i, lab, kind))
    # py UNREACHABLE entries and e() edges that mention the method
    key = "UNREACHABLE['%s']" % m
    for f in py_files + [gd]:
        for i, line in enumerate(open(f, encoding='utf-8'), 1):
            if key in line:
                out.append('  UNREACH %s:%d: %s' % (os.path.basename(f), i, line.strip()[:160]))
    # e() edges with the method as src or dst (exact quoted name)
    q = "'%s'" % m
    for f in py_files + [gd]:
        for i, line in enumerate(open(f, encoding='utf-8'), 1):
            if line.startswith('e(') and q in line:
                out.append('  EDGE %s:%d: %s' % (os.path.basename(f), i, line.strip()[:200]))
    # any mention in graph_def or py (non-md) that is not an edge line start
out_path = os.path.join(BASE, 'scratch/h145/overlap.txt')
with open(out_path, 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(out) + '\n')
print('written', out_path, len(out), 'lines')
