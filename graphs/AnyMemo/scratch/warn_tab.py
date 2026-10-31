import json, collections
g = json.load(open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/out/anymemo_trigger_graph.json'))
V = g['verdict']
def base(n): return n.split('@')[0]
inn = collections.defaultdict(list)
for x in g['edges']:
    inn[base(x['dst'])].append(x)
for m, v in V.items():
    if v != 'UNREACHABLE': continue
    live = [x for x in inn.get(m, []) if x['kind'] != 'REGISTER']
    for x in live:
        s = base(x['src'])
        print('%-60s <- %-10s %-55s %s %s' % (m[:60], x['id'], s[:55], V.get(s, '?')[:5], ('auto' if x.get('auto') else 'hand') + ' ' + x['kind'] + ' ' + x['edge_class']))
