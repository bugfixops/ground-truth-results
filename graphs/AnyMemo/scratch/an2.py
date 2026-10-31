import csv, json, collections
G = '/Users/darshan/Desktop/yang/work/graphs/AnyMemo'
rows = list(csv.DictReader(open(G + '/out/methods.csv')))
verdict = {r['method']: r['verdict'] for r in rows}
auto = json.load(open(G + '/auto_calls.json'))
callers = collections.defaultdict(list)
for c in auto['calls']:
    callers[c['dst']].append(c['src'])
lamb = collections.defaultdict(list)
for l in auto['lambdas']:
    lamb[l['dst']].append(l['src'])
def cls(m):
    return m.split('.')[0] if '.' in m else m
tot = collections.Counter(); rch = collections.Counter(); un = collections.Counter(); nocall = collections.Counter()
for m, v in verdict.items():
    c = cls(m); tot[c] += 1
    if v == 'REACHABLE': rch[c] += 1
    if v == 'UNRESOLVED':
        un[c] += 1
        if not callers.get(m) and not lamb.get(m): nocall[c] += 1
out = []
for c in sorted(un, key=lambda c: -un[c]):
    out.append('%s %d/%d/%d nc%d' % (c, tot[c], rch[c], un[c], nocall[c]))
print('CLASS total/reach/unres/nocaller (classes with unresolved)')
print('; '.join(out))
allU = sum(un.values())
print('classes entirely unresolved:', [c for c in un if rch[c] == 0])
