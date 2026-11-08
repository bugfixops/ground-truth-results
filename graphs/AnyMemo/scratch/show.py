# show verdict + incoming (non-REGISTER) edges + outgoing for methods whose key starts with a prefix (read-only over out/ json)
import json, sys, collections
G=json.load(open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/out/anymemo_trigger_graph.json'))
V=G['verdict']; E=G['edges']
def base(k): return k.split('(')[0]
inc=collections.defaultdict(list); outg=collections.defaultdict(list)
for x in E:
    inc[base(x['dst'])].append(x); outg[base(x['src'])].append(x)
mode=sys.argv[1]; pats=sys.argv[2:]
for m in sorted(V):
    if not any(m.startswith(p) for p in pats): continue
    if mode=='v':
        print(m, V[m])
    elif mode=='i':
        ins=[x for x in inc.get(base(m),[]) if x['kind']!='REGISTER']
        print('%s [%s] in=%d'%(m,V[m][:3],len(ins)))
        for x in ins[:4]: print('    <- %s [%s] %s %s'%(x['src'],x['kind'],x['trigger'][:70],(x.get('evidence') or '')[:90]))
    elif mode=='o':
        os_=outg.get(base(m),[])
        print('%s [%s] out=%d'%(m,V[m][:3],len(os_)))
        for x in os_[:12]: print('    -> %s [%s/%s] %s'%(x['dst'],x['kind'],V.get(base(x['dst']),'?')[:3],(x.get('evidence') or '')[:80]))
