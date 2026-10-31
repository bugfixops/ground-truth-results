import csv, json, collections
G='/Users/darshan/Desktop/yang/work/graphs/Markor/'
g=json.load(open(G+'out/markor_trigger_graph.json'))
rows=list(csv.DictReader(open(G+'out/methods.csv')))
verd={r['method']:r['verdict'] for r in rows}
at=[x for x in g['edges'] if '@' in x['src'] or '@' in x['dst']]
print('edges with @:', len(at), 'kinds', collections.Counter(x['kind'] for x in at).most_common(4))
print('method rows with @:', sum(1 for k in verd if '@' in k))
print('sample', [(x['src'],x['dst'],x['kind']) for x in at[:3]])
b=lambda n:n.split('@')[0]
adj=collections.defaultdict(set)
for x in g['edges']:
    if x['kind']!='REGISTER': adj[x['src']].add(x['dst'])
reach={'S_ENTRY'}; st=['S_ENTRY']
while st:
    x=st.pop()
    for y in adj.get(x,()):
        if y not in reach: reach.add(y); st.append(y)
rv={k for k,v in verd.items() if v=='REACHABLE'}
print('full-name reach size', len(reach), 'REACHABLE verdict', len(rv))
print('verdict REACHABLE but not in full reach:', len(rv-reach), list(rv-reach)[:3])
print('full reach (non-page, method-like) not REACHABLE:', len({k for k in reach if not k.startswith('S_') and '@' not in k and verd.get(k)!='REACHABLE'}), list({k for k in reach if not k.startswith('S_') and '@' not in k and verd.get(k)!='REACHABLE'})[:4])
