import json, re

W = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager'
d = json.load(open(W + '/out/amazefilemanager_trigger_graph.json'))
names = sorted(d['verdict'].keys())
B = open(W + '/scratch/build_finish_24.txt', encoding='utf-8').read().split('\n')
unk = set()
for l in B:
    m = re.match(r'  ERROR (\S+): unknown (src|dst) node (.*)$', l)
    if m:
        unk.add(m.group(3))
for u in sorted(unk):
    base = u.split('@')[0]
    cands = [n for n in names if n == base or n.split('(')[0] == base.split('(')[0] and base.endswith('(') is False and n.split('(')[0] == base]
    if not cands:
        cands = [n for n in names if base.split('.')[0] in n.split('.')[0] and n.split('.')[-1].startswith(base.split('.')[-1][:6])][:6]
    print('UNK', u, '->', cands[:6] if cands else 'NO MATCH')
g = open(W + '/graph_def.py', encoding='utf-8').read()
for s in ['S_UNKNOWN', 'S_PREFERENCES', 'S_PREFERENCE_click', 'S_EDITTEXT_watch']:
    print('DEF', s, [i + 1 for i, l in enumerate(g.split('\n')) if re.search(r"\b%s\b" % s, l)][:6])
