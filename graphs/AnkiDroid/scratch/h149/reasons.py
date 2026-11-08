import glob, os
ROOT = '/Users/darshan/Desktop/yang/work/graphs/AnkiDroid'
row = None
with open(ROOT + '/scratch/batches_ai.tsv', encoding='utf-8') as fh:
    for line in fh:
        f = line.rstrip('\n').split('\t')
        if f and f[0] == '149':
            row = f; break
methods = row[3].split(';')
md = {}
for p in sorted(glob.glob(ROOT + '/parts/*.md')):
    with open(p, encoding='utf-8', errors='replace') as fh:
        for ln in fh:
            if not ln.startswith('|'):
                continue
            c = [x.strip() for x in ln.strip().strip('|').split('|')]
            if len(c) >= 4:
                md.setdefault(c[0], []).append((os.path.basename(p), c[1], c[2], c[3][:230]))
for m in methods:
    hits = md.get(m, [])
    if not hits:
        continue
    fn, lab, kind, reason = hits[0]
    print('%s | %s | %s | %s | %s' % (m, fn, lab, kind, reason))
