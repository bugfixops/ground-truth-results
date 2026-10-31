import json, sys, collections
sys.path.insert(0, 'tools')
import build_graph as bg
G = 'graphs/AmazeFileManager'
rows = json.load(open(G + '/method_list.json'))
names, by_name = bg.method_names(rows)
known = set(names)
S = 'graphs/AmazeFileManager/scratch/'
edges = json.load(open(S + 'edges_trace.json'))
screens = set()
def cands(n):
    b = n.split('(')[0]
    return sorted(x for x in known if x.split('(')[0] == b)
out = []
cat = collections.Counter()
for x in edges:
    for end in ('src', 'dst'):
        n = x[end]
        if bg.base(n) in known or bg.is_screen(n):
            continue
        c = cands(n)
        if len(c) == 1:
            k = 'ONE'
        elif len(c) > 1:
            k = 'MANY'
        else:
            k = 'NONE'
        cat[(end, k)] += 1
        out.append((k, end, x['id'], x['kind'], n, x['_lines'][:1], x.get('auto', False), c))
json.dump(out, open(S + 'unknown_table.json', 'w'), indent=0)
for k, v in sorted(cat.items()):
    print(k, v)
print('total', sum(cat.values()))
