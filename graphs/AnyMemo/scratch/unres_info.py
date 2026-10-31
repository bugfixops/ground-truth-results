import json, csv, collections, sys
g=json.load(open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/out/anymemo_trigger_graph.json',encoding='utf-8'))
verdict=g['verdict']
inc=collections.defaultdict(list); outg=collections.defaultdict(list)
for i,e in enumerate(g['edges']):
    inc[e['dst']].append((e['src'],e['kind'],i))
    outg[e['src']].append((e['dst'],e['kind'],i))
un=[m for m,v in verdict.items() if v=='UNRESOLVED']
un.sort()
with open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch/unres_info.txt','w') as f:
    for m in un:
        callers=inc.get(m,[])
        cs='; '.join(f"{s}[{k}]" for s,k,_ in callers[:4])
        callees=outg.get(m,[])
        ce='; '.join(f"{d}[{k}]" for d,k,_ in callees[:3])
        f.write(f"{m} | IN {len(callers)}: {cs} | OUT {len(callees)}: {ce}\n")
print(len(un))
