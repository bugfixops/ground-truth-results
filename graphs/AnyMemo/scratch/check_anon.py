import json,re,os,sys
d=json.load(open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/out/anymemo_trigger_graph.json'))
amap=json.load(open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch/anon_map.json'))
ANON=re.compile(r'\$\d+(\$|$)')
def cls(m): return m.split('.')[0] if '.' in m else m
def ranges(ev):
    out=[]
    for f,body in re.findall(r'SRC ([\w/.$#-]+\.java):([\d,\- ]+)', ev or ''):
        for part in body.split(','):
            part=part.strip()
            if not part: continue
            if '-' in part:
                a,b=part.split('-'); out.append((f,int(a),int(b)))
            else: out.append((f,int(part),int(part)))
    return out
flag=[];ok=0;nocite=[]
for e in d['edges']:
    for side in ('src','dst'):
        m=e[side]
        c=cls(m)
        if not ANON.search(c) or c not in amap: continue
        f,line=amap[c]
        rs=ranges(e.get('evidence'))
        if not rs:
            nocite.append((e['id'],e['src'],e['dst'],e.get('evidence')));continue
        same=[r for r in rs if os.path.basename(r[0])==os.path.basename(f)]
        if any(a<=line<=b for _,a,b in same):
            ok+=1
        else:
            flag.append((e['id'],e['edge_class'],e['src'],e['dst'],c,f"{f}:{line}",e.get('evidence')))
        break
print('ok',ok,'flagged',len(flag),'no SRC cite',len(nocite))
for x in flag: print(' | '.join(str(y) for y in x)[:400])
print('--- no SRC cite')
for x in nocite[:60]: print(' | '.join(str(y) for y in x)[:300])
