import json, re, sys, collections
sys.path.insert(0, 'tools')
import build_graph as bg
G = 'graphs/AmazeFileManager'
rows = json.load(open(G + '/method_list.json'))
names, by_name = bg.method_names(rows)
bad = collections.Counter()
for line in open(G + '/scratch/build_finish_07.txt', encoding='utf-8'):
    m = re.match(r'  ERROR \w+: unknown (src|dst) node (.+)$', line.rstrip())
    if m:
        bad[m.group(2)] += 1
known = set(names)
rep = []
for n, c in bad.most_common():
    if n in known:
        rep.append((c, n, 'KNOWN?!', []))
        continue
    cands = sorted(x for x in known if x.split('(')[0] == n.split('(')[0] and x.split('(')[0].split('#')[0] == n.split('(')[0])
    rep.append((c, n, len(cands), cands[:6]))
for c, n, k, cands in rep:
    print(c, n, k, cands if isinstance(k, int) else '')
print('distinct', len(bad), 'total', sum(bad.values()))
