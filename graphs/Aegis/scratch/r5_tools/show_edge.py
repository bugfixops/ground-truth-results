import json, sys
d = json.load(open('/Users/darshan/Desktop/yang/work/graphs/Aegis/out/aegis_trigger_graph.json'))
want = set(sys.argv[1:])
for x in d['edges']:
    if x.get('id') in want:
        print(json.dumps(x, indent=1, ensure_ascii=False)[:1500])
        print('---')
print('keys:', sorted(d['edges'][0].keys()))
