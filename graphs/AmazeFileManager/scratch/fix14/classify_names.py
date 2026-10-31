import json, sys, collections, re
sys.path.insert(0, '/Users/darshan/Desktop/yang/work/tools')
import build_graph as B
W = '/Users/darshan/Desktop/yang/work/'
rows = json.load(open(W + 'graphs/AmazeFileManager/method_list.json'))
names, by_name = B.method_names(rows)
canon = set(names)
bare = collections.defaultdict(list)
for n in names:
    bare[n.split('(')[0].split('#')[0]].append(n)
unk = collections.Counter()
for l in open(W + 'graphs/AmazeFileManager/scratch/unknown_names_14.txt'):
    c, n = l.split(' ', 1)
    unk[n.strip()] = int(c)
out = []
for n, c in sorted(unk.items(), key=lambda x: -x[1]):
    if n in canon:
        status = 'CANON'
        cands = [n]
    else:
        cands = bare.get(n, [])
        if cands:
            status = 'OVERLOAD' if len(cands) > 1 or '(' not in cands[0] else 'BASE_ONLY'
        else:
            status = 'NOT_IN_APP'
    out.append((c, n, status, '; '.join(cands[:8])))
for row in out:
    print('\t'.join(map(str, row)))
