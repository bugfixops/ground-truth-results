import json, re

W = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager'
S = W + '/scratch/finish24'
names = sorted(json.load(open(W + '/out/amazefilemanager_trigger_graph.json'))['verdict'].keys())
B = open(W + '/scratch/build_finish_24.txt', encoding='utf-8').read().split('\n')
GD = open(W + '/graph_def.py', encoding='utf-8').read().split('\n')
rows = {}
with open(S + '/edge_lines.tsv', encoding='utf-8') as f:
    next(f)
    for ln in f:
        p = ln.rstrip('\n').split('\t', 8)
        rows[p[0]] = p

for l in B:
    m = re.match(r'  ERROR (\S+): unknown (src|dst) node (.*)$', l)
    if not m:
        continue
    eid, end, nm = m.group(1), m.group(2), m.group(3)
    r = rows.get(eid)
    base = nm.split('(')[0]
    cands = [n for n in names if n.split('(')[0] == base or n.split('@')[0].split('(')[0] == base][:8]
    print('%s %s %s | line %s | %s -> %s' % (eid, end, nm, r[1] if r else '?', r[3] if r else '?', r[4] if r else '?'))
    print('      CANDS', cands)

print('--- S_ defs / uses in graph_def.py')
for s in ['S_UNKNOWN', 'S_PREFERENCES', 'S_PREFERENCE_click', 'S_EDITTEXT_watch', 'S_PREFS', 'S_PARCEL_read', 'S_NESTED_SCROLL']:
    hits = [i + 1 for i, l in enumerate(GD) if re.search(r'\b%s\b' % s, l)]
    print(s, len(hits), hits[:4])
    for h in hits[:2]:
        print('   ', h, GD[h - 1].strip()[:140])
