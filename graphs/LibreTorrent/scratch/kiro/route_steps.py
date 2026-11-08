"""Compact step list for one sampled method: python3 -I graphs/LibreTorrent/scratch/kiro/route_steps.py '<method>'"""
import csv, json, glob, sys
lab = {r['method']: r for r in csv.DictReader(open('graphs/LibreTorrent/out/methods.csv', encoding='utf-8'))}
g = json.load(open(glob.glob('graphs/LibreTorrent/out/*_trigger_graph.json')[0], encoding='utf-8'))
E = {x['id']: x for x in g['edges']}
r = lab[sys.argv[1]]
print(sys.argv[1], 'steps', r['steps_from_launch'], 'env', r['env_kinds'], 'state', r['state_kinds'])
for n, i in enumerate(r['route_edge_ids'].split(), 1):
    x = E[i]
    print('%2d %s %s -> %s [%s/%s]%s%s%s%s' % (n, i, x['src'], x['dst'], x['kind'], x['edge_class'],
          ' auto' if x.get('auto') else '', ' G:' + x['guard'] if x.get('guard') else '',
          ' S:' + x['needs_state'] if x.get('needs_state') else '', ' ENV:' + x['env'] if x.get('env') else ''))
    print('     ' + (x['evidence'] or '')[:230])
