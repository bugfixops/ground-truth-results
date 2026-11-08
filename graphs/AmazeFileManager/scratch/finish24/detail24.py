import os, re, sys

W = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager'
JAVA = '/Users/darshan/Desktop/yang/work/final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src'
S = W + '/scratch/finish24'
GD = open(W + '/graph_def.py', encoding='utf-8').read().split('\n')
rows = {}
with open(S + '/edge_lines.tsv', encoding='utf-8') as f:
    next(f)
    for ln in f:
        p = ln.rstrip('\n').split('\t', 8)
        rows[p[0]] = p

B = open(W + '/scratch/build_finish_24.txt', encoding='utf-8').read().split('\n')
errs = []
for l in B:
    m = re.match(r'  ERROR (\S+): unknown (src|dst) node (.*)$', l)
    if m:
        errs.append((m.group(1), m.group(2), m.group(3)))

index = {}
for root, _, files in os.walk(JAVA):
    for fn in files:
        if fn.endswith('.java'):
            index.setdefault(fn, []).append(os.path.join(root, fn))


def src_snip(ev):
    m = re.search(r'([\w$/]+\.java):(\d+)(?:-(\d+))?', ev or '')
    if not m:
        return None
    base = os.path.basename(m.group(1))
    paths = index.get(base, [])
    if not paths:
        return 'NOFILE ' + base
    p = sorted(paths, key=lambda q: ('/main/' not in q, len(q)))[0]
    n = int(m.group(2))
    L = open(p, encoding='utf-8', errors='replace').read().split('\n')
    lo, hi = max(1, n - 4), min(len(L), (int(m.group(3)) if m.group(3) else n) + 4)
    body = ['    %5d %s' % (i, L[i - 1].rstrip()[:150]) for i in range(lo, hi + 1)]
    return p.split('/java/')[-1] + '\n' + '\n'.join(body)


only = sys.argv[1:] if len(sys.argv) > 1 else None
for eid, end, name in errs:
    base = eid
    r = rows.get(base)
    if only and base not in only:
        continue
    if not r:
        print('== %s NO ROW' % eid)
        continue
    ln = int(r[1])
    stmt = '\n'.join('  %5d %s' % (i, GD[i - 1].rstrip()[:160]) for i in range(ln, min(ln + 3, len(GD)) + 1))
    print('== %s line %d %s %s: %s' % (eid, ln, end, name, r[3] + ' -> ' + r[4]))
    print(stmt)
    print('  EV', (r[8] or '')[:260])
    s = src_snip(r[8])
    if s:
        print(s)
