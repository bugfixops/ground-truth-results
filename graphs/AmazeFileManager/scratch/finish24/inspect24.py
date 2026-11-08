import json, os, sys

W = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager'
S = W + '/scratch/finish24'

src = open(S + '/../finish22/edge_map.py', encoding='utf-8').read()
src = src.replace("OUT = os.path.join(WORK, GDIR, 'scratch/finish22')", "OUT = os.path.join(WORK, GDIR, 'scratch/finish24')")
open(S + '/edge_map24.py', 'w', encoding='utf-8').write(src)

if '--map' in sys.argv:
    os.system('python3 -I ' + S + '/edge_map24.py > ' + S + '/edge_map24.log 2>&1')

d = json.load(open(W + '/out/amazefilemanager_trigger_graph.json'))
v = d['verdict']
print('UNRESOLVED:', sorted(m for m, x in v.items() if x == 'UNRESOLVED'))
rows = {}
with open(S + '/edge_lines.tsv', encoding='utf-8') as f:
    h = next(f)
    for ln in f:
        p = ln.rstrip('\n').split('\t', 8)
        rows[p[0]] = p
for eid in ['E7950fe86', 'E80cd9ff5', 'E54d2e078', 'E9a62bab6', 'Ea4caaf12', 'Eef677b84']:
    r = rows.get(eid)
    print('REVIEW', eid, r[1:6] if r else 'MISSING', (r[8][:160] if r else ''))
