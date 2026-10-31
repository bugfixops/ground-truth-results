import json,re,os
d=json.load(open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/out/anymemo_trigger_graph.json'))
amap=json.load(open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch/anon_map2.json'))
ANON=re.compile(r'\$\d+$')
def cls(m): return m.rsplit('.',1)[0] if '.' in m else m
def ranges(ev):
    out=[]
    for f,body in re.findall(r'SRC ([\w/.$#-]+\.java):([\d,\- ]+)', ev or ''):
        for part in body.split(','):
            part=part.strip()
            if not part: continue
            if '-' in part:
                a,b=part.split('-'); out.append((os.path.basename(f),int(a),int(b)))
            else: out.append((os.path.basename(f),int(part),int(part)))
    return out
flag=[];ok=0
for e in d['edges']:
    hit=None
    for side in ('src','dst'):
        c=cls(e[side])
        if c in amap: hit=(side,c)
    if not hit: continue
    side,c=hit
    a=amap[c]; f=os.path.basename(a['file'])
    rs=ranges(e.get('evidence'))
    if any(rf==f and lo<=a['end'] and hi>=a['new'] for rf,lo,hi in rs):
        ok+=1
    else:
        flag.append((e['id'],e['edge_class'],e['src'],e['dst'],c,f"{a['file']}:{a['new']}-{a['end']}",e.get('evidence') or ''))
print('edges with anon end',ok+len(flag),'ok',ok,'flagged',len(flag))
with open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch/anon_flags.txt','w') as fo:
    for x in flag: fo.write(' | '.join(str(y) for y in x)+'\n')
