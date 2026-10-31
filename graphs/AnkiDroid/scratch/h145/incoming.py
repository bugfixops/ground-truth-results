import json, sys

BASE = '/Users/darshan/Desktop/yang/work/graphs/AnkiDroid'
doc = json.load(open(BASE + '/out/ankidroid_trigger_graph.json', encoding='utf-8'))
print('top keys:', sorted(doc.keys()))
edges = doc.get('edges')
if edges is None:
    for k, v in doc.items():
        if isinstance(v, list) and v and isinstance(v[0], dict) and 'src' in v[0]:
            edges = v
            print('edge list key:', k)
print('first edge keys:', sorted(edges[0].keys()) if edges else None)
print('first edge:', json.dumps(edges[0])[:400] if edges else None)
targets = [l.strip() for l in open(BASE + '/scratch/h145/targets.txt', encoding='utf-8') if l.strip()]
tset = set(targets)
for t in targets:
    inc = [x for x in edges if x.get('dst') == t]
    print('== %s incoming=%d' % (t, len(inc)))
    for x in inc:
        print('   %s -> %s kind=%s cls=%s guard=%s ev=%s' % (x.get('src'), x.get('dst'), x.get('kind'), x.get('class'),
              str(x.get('guard'))[:80], str(x.get('evidence'))[:120]))
