# per UNRESOLVED class: count unresolved / reachable methods, and textual references to the class name outside its own file
import json, re, os, collections, sys
BASE='/Users/darshan/Desktop/yang/work/graphs/AnyMemo'
APP='/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main'
G=json.load(open(BASE+'/out/anymemo_trigger_graph.json'))
V=G['verdict']
def base(k): return k.split('(')[0]
files=[]
for dp,dn,fn in os.walk(APP):
    for f in fn:
        if f.endswith('.java') or f.endswith('.xml'):
            p=os.path.join(dp,f); files.append(p)
texts={p:open(p,encoding='utf-8',errors='replace').read().split('\n') for p in files}
def refs(simple, own):
    out=[]
    pat=re.compile(r'\b%s\b'%re.escape(simple))
    for p,L in texts.items():
        if p==own: continue
        for i,l in enumerate(L):
            if pat.search(l) and not l.strip().startswith(('import ','package ')):
                out.append((os.path.relpath(p,APP),i+1,l.strip()[:110]))
    return out
cls=collections.defaultdict(lambda:[0,0])
for m,v in V.items():
    c=base(m).rpartition('.')[0]
    if v=='UNRESOLVED': cls[c][0]+=1
    elif v=='REACHABLE': cls[c][1]+=1
if __name__=='__main__':
    target=sys.argv[1:] or sorted(c for c in cls if cls[c][0]>0)
    for c in target:
        top=c.split('$')[0].split('.')[-1]
        own=None
        for p in files:
            if os.path.basename(p)==top+'.java': own=p
        r=refs(top, own) if own else [('NO SOURCE',0,'')]
        print('== %s unres=%d reach=%d refs=%d'%(c,cls[c][0],cls[c][1],len(r)))
        for x in r[:6]: print('   %s:%d %s'%x)
