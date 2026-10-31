import json, glob
g = json.load(open(glob.glob('graphs/AnyMemo/out/*_trigger_graph.json')[0]))
E = g['edges']
targets = sorted({x['dst'] for x in E if x['dst'].endswith('.onActivityResult') or '.onActivityResult@' in x['dst']})
for t in targets:
    inc = [x for x in E if x['dst'] == t]
    print(t, 'verdict=', g['labels'][t]['verdict'] if 'verdict' in g['labels'][t] else g['labels'][t].get('verdict'))
    for x in inc:
        print('    <-', x['id'], x['src'], x['kind'], x.get('edge_class'), '| guard=', (x.get('guard') or '')[:60], '| needs=', (x.get('needs_state') or '')[:60], '|', (x.get('trigger') or '')[:70])
