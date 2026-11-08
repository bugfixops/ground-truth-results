import json, sys
sys.path.insert(0, '/Users/darshan/Desktop/yang/work/tools')
import build_graph as B
GDIR = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager'
rows = json.load(open(GDIR + '/method_list.json'))
names, by_name = B.method_names(rows)
st = {}
for l in open(GDIR + '/scratch/fix14/name_status.tsv'):
    p = l.rstrip('\n').split('\t'); st[p[1]] = p[2]
items = json.load(open(GDIR + '/scratch/fix14/unknown_items.json'))
def cands(n):
    base = n.split('(')[0]
    if '(' in n:
        return [c for c in names if c == n] or [c for c in names if c.split('(')[0] == base and c.split('(')[0] == base]
    return [c for c in names if c == n or c.split('(')[0] == n]
ov = [i for i in items if all(st.get(b.split('=', 1)[1]) == 'OVERLOAD' for b in i['bad'])]
na = [i for i in items if not all(st.get(b.split('=', 1)[1]) == 'OVERLOAD' for b in i['bad'])]
def out(items_, tag):
    chunks = []
    size = 40
    n = (len(items_) + size - 1) // size
    per = -(-len(items_) // n)
    for k in range(n):
        part = items_[k * per:(k + 1) * per]
        rec = []
        for it in part:
            d = dict(it)
            d['candidates'] = {b.split('=', 1)[1]: cands(b.split('=', 1)[1]) for b in it['bad']}
            d['kind'] = 'OVERLOAD' if it in ov else 'NOT_IN_APP'
            rec.append(d)
        fn = '%s/scratch/fix14/batches/%s%d.json' % (GDIR, tag, k + 1)
        json.dump(rec, open(fn, 'w'), indent=1)
        chunks.append((fn, len(rec)))
    return chunks
print(out(ov, 'O'))
print(out(na, 'N'))
