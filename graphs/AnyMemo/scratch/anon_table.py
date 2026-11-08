import json, re, sys, os, collections
sys.path.insert(0, '/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch')
from anon_blocks import blocks, SRC, CL
G = '/Users/darshan/Desktop/yang/work/graphs/AnyMemo'
A = json.load(open(G + '/auto_calls.json'))
calls_by_src = collections.defaultdict(list)
for c in A['calls']:
    calls_by_src[c['src'].split('(')[0].split(' ')[-1]].append((c['line'], c['dst'].split('(')[0].split(' ')[-1]))
def table(top):
    tf = None
    for root, _, fs in os.walk(SRC):
        if top + '.java' in fs: tf = os.path.join(root, top + '.java')
    L = open(tf, encoding='utf-8', errors='replace').read().split('\n')
    bl = blocks(tf)
    rows = []
    for k in CL:
        if not CL[k]: continue
        nm = k.split('.')[-1]
        if not (nm.startswith(top + '$')): continue
        mn, mx = CL[k][0], CL[k][-1]
        cands = [(s, e) for s, e in bl if e and s <= mn and e >= mx]
        b = max(cands, key=lambda t: t[0]) if cands else None
        txt = L[b[0] - 1].strip()[:70] if b else ''
        dsts = sorted({d for (ln, d) in calls_by_src.get(nm, [])})
        rows.append((nm, b, mn, mx, txt, dsts[:5]))
    for r in sorted(rows, key=lambda r: (len(r[0]), r[0])):
        print('%-40s block %-10s lines %d-%d | %s | calls: %s' % (r[0], '%s-%s' % (r[1][0], r[1][1]) if r[1] else '?', r[2], r[3], r[4], ' '.join(r[5])))
if __name__ == '__main__':
    for t in sys.argv[1:]:
        print('==', t); table(t)
