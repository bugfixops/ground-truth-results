import json,csv,collections,glob,sys
app=sys.argv[1]
g=json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json'%app)[0],encoding='utf-8'))
E={e['id']:e for e in g['edges']}
c=collections.Counter(); ex=collections.defaultdict(list)
for r in csv.DictReader(open('graphs/%s/out/methods.csv'%app,encoding='utf-8')):
    if r['verdict']!='REACHABLE': continue
    for i in r['route_edge_ids'].split():
        if E[i].get('env'):
            c[i]+=1; ex[i].append(r['method']); break
print(app,'methods with env on best route:',sum(c.values()))
for i,n in c.most_common(int(sys.argv[2]) if len(sys.argv)>2 else 15):
    e=E[i]; print(' %4d %s %s %s -> %s | %s | %s'%(n,i,e['kind'],e['src'],e['dst'],(e['env'] or '')[:70],ex[i][:2]))
