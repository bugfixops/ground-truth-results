import json, sys
d = json.load(open('/Users/darshan/Desktop/yang/work/graphs/Aegis/out/aegis_trigger_graph.json'))
pat = sys.argv[1:]
for x in d['edges']:
    s = json.dumps(x, ensure_ascii=False)
    if any(p in (x.get('src','') + ' ' + x.get('dst','')) for p in pat):
        print(x.get('id'), x.get('kind'), x.get('cls'), '|', x.get('src'), '->', x.get('dst'), '| guard:', (x.get('guard') or '')[:140], '| needs:', x.get('needs_state'), '| env:', x.get('env'))
