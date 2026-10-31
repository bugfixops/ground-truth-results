import csv, json, collections, re
G='/Users/darshan/Desktop/yang/work/graphs/Markor/'
g=json.load(open(G+'out/markor_trigger_graph.json'))
rows=list(csv.DictReader(open(G+'out/methods.csv')))
dead=json.load(open(G+'scratch/dead_plan.json'))
manual=dict(l.rstrip('\n').split('\t',1) for l in open(G+'scratch/manual_list.txt'))
b=lambda n:n.split('@')[0]
adj=collections.defaultdict(set); inc=collections.defaultdict(list)
for x in g['edges']:
    s,d=b(x['src']),b(x['dst']); inc[d].append((s,x['kind']))
    if x['kind']!='REGISTER': adj[s].add(d)
reach={'S_ENTRY'}; st=['S_ENTRY']
while st:
    x=st.pop()
    for y in adj.get(x,()):
        if y not in reach: reach.add(y); st.append(y)
verd={r['method']:r['verdict'] for r in rows}
rv=[k for k,v in verd.items() if v=='REACHABLE']
print('REACHABLE verdict not in reach:', sum(1 for k in rv if k not in reach), 'example', [k for k in rv if k not in reach][:3])
print('dead in reach:', [k for k in dead if k in reach][:5])
print('dead keys not in verdict UNRESOLVED:', sum(1 for k in dead if verd.get(k)!='UNRESOLVED'), [k for k in dead if verd.get(k)!='UNRESOLVED'][:3])
# manual 'incoming edges' group: edge kinds and source reach
cnt=collections.Counter()
ex=[]
for k,v in manual.items():
    if v.startswith('has incoming'):
        srcs=inc.get(b(k),[])
        for s,kind in srcs:
            cnt[(kind, s in reach, verd.get(s,'-'))]+=1
        if len(ex)<6: ex.append((k, srcs[:3]))
print('manual-incoming source (kind, src reached, src verdict):', cnt.most_common(12))
for e in ex: print('  ', e)
# sample refs of dead entries
import random
random.seed(1)
for k in random.sample(sorted(dead), 8):
    print('REF', k, '|', dead[k][2], '|', dead[k][3])
