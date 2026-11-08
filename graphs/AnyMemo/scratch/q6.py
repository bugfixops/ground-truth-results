import json, glob, sys
g = json.load(open(glob.glob('graphs/AnyMemo/out/*_trigger_graph.json')[0]))
names = sys.argv[1:]
for x in g['edges']:
    if any(x['dst'] == n or x['src'] == n for n in names):
        print(x['id'], x['src'], '->', x['dst'], x['kind'], x.get('edge_class'), '| guard=', x.get('guard'), '| needs=', x.get('needs_state'), '| env=', x.get('env'), '| ev=', (x.get('evidence') or '')[:120])
