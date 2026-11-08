import csv, json, sys, collections
# Usage: python3 -I scratch/cat2.py [class-substring]
# For each UNRESOLVED method (out/methods.csv): a ROOT has no incoming non-REGISTER edge from any method; a CHAIN has one.
# Prints per class: roots and chains, using the built graph json (out/markor_trigger_graph.json).
G = '/Users/darshan/Desktop/yang/work/graphs/Markor/'
g = json.load(open(G + 'out/markor_trigger_graph.json'))
edges = g['edges'] if isinstance(g.get('edges'), list) else []
inc = collections.defaultdict(list)
for x in edges:
    if x['kind'] != 'REGISTER':
        inc[x['dst'].split('@')[0] if False else x['dst']].append(x['src'])
rows = list(csv.DictReader(open(G + 'out/methods.csv')))
unres = [r['method'] for r in rows if r['verdict'] == 'UNRESOLVED']
roots = collections.defaultdict(list)
chains = collections.defaultdict(list)
for m in unres:
    cls = m.split('.', 1)[0]
    if m.split('(')[0] and inc.get(m):
        chains[cls].append(m)
    else:
        roots[cls].append(m)
flt = sys.argv[1:]
print('unresolved', len(unres), 'roots', sum(len(v) for v in roots.values()), 'chains', sum(len(v) for v in chains.values()))
for c in sorted(set(roots) | set(chains), key=lambda k: -(len(roots[k]) + len(chains[k]))):
    if flt and not any(f in c for f in flt):
        continue
    print('%s r=%d c=%d' % (c, len(roots[c]), len(chains[c])))
    if flt:
        for m in roots[c]:
            print('   root', m)
        for m in chains[c]:
            print('   chain', m, 'from', ','.join(sorted(set(s.split('.')[0] for s in inc[m])))[:120])
