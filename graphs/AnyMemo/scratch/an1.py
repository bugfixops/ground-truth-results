import csv, json, collections, sys
G = '/Users/darshan/Desktop/yang/work/graphs/AnyMemo'
rows = list(csv.DictReader(open(G + '/out/methods.csv')))
verdict = {r['method']: r['verdict'] for r in rows}
auto = json.load(open(G + '/auto_calls.json'))
ml = json.load(open(G + '/method_list.json'))
flags = collections.Counter(f for r in ml for f in r['flags'])
print('flags', dict(flags))
callers = collections.defaultdict(list)
for c in auto['calls']:
    callers[c['dst']].append(c['src'])
lamb = collections.defaultdict(list)
for l in auto['lambdas']:
    lamb[l['dst']].append(l['src'])
U = [m for m, v in verdict.items() if v == 'UNRESOLVED']
print('unresolved', len(U))
cls_cnt = collections.Counter(m.split('.')[0] for m in U)
print('by class (top):', cls_cnt.most_common(80))
nocall = [m for m in U if not callers.get(m) and not lamb.get(m)]
print('unresolved with NO bytecode caller and NO lambda creator:', len(nocall))
allcallers_U = [m for m in U if callers.get(m) and all(verdict.get(x, 'NOTIN') == 'UNRESOLVED' for x in callers[m])]
print('unresolved whose callers are all UNRESOLVED (closed):', len(allcallers_U))
frontier = [m for m in U if any(verdict.get(x, 'NOTIN') == 'REACHABLE' for x in callers.get(m, []))]
print('unresolved with a REACHABLE bytecode caller (should be empty unless suppressed):', len(frontier))
for m in frontier[:40]:
    print('  F', m, [x for x in callers[m] if verdict.get(x) == 'REACHABLE'][:3])
other = collections.Counter()
for m in U:
    for x in callers.get(m, []):
        if verdict.get(x, 'NOTIN') not in ('UNRESOLVED',):
            other[verdict.get(x, 'NOTIN')] += 1
print('callers of U outside U by verdict', other)
notin = [x for m in U for x in callers.get(m, []) if x not in verdict]
print('callers of U not in method table', len(notin), notin[:5])
