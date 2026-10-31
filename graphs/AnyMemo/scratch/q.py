# usage: q.py METHOD [METHOD ...]   (exact short name, e.g. Card.equals); prints verdict, in/out edges
import json, sys, collections
g = json.load(open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/out/anymemo_trigger_graph.json'))
E = g['edges']
def base(n): return n.split('@')[0]
inn = collections.defaultdict(list); out = collections.defaultdict(list)
for x in E:
    inn[base(x['dst'])].append(x); out[base(x['src'])].append(x)
W = int(__import__('os').environ.get('W', '110'))
for m in sys.argv[1:]:
    hits = [k for k in g['methods'] if k == m or k.startswith(m + '(') or k.endswith('.' + m) or k.endswith(m)]
    hits = [k for k in hits if k.split('(')[0].endswith(m.split('(')[0]) or k == m]
    if not hits:
        hits = [k for k in g['methods'] if m in k][:5]
    for k in hits[:4]:
        print('==', k, '| verdict', g['verdict'].get(k), '| label', json.dumps(g['labels'].get(k))[:200])
        for x in inn.get(k, []):
            print('   IN ', x['id'], x['src'], x['kind'], x['edge_class'], 'auto' if x.get('auto') else 'hand', (x.get('evidence') or '')[:W])
        for x in out.get(k, [])[:12]:
            print('   OUT', x['id'], x['dst'], x['kind'], x['edge_class'], 'auto' if x.get('auto') else 'hand', (x.get('evidence') or '')[:W])
        if len(out.get(k, [])) > 12: print('   OUT ... %d more' % (len(out[k]) - 12))
