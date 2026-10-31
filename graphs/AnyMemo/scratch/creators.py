# usage: creators.py Simple.Name ... : for each class prints <init> verdict, incoming edges to <init> (src,kind), and app source lines with 'new X(' or 'X.class' or 'X.newInstance'
import json, sys, os, re, collections
G=json.load(open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/out/anymemo_trigger_graph.json'))
V=G['verdict']; E=G['edges']
JROOT='/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java'
files=[]
for dp,dn,fn in os.walk(JROOT):
    for f in fn:
        if f.endswith('.java'): files.append(os.path.join(dp,f))
txt={f:open(f,encoding='utf-8',errors='replace').read().split('\n') for f in files}
def base(k): return k.split('(')[0]
for cls in sys.argv[1:]:
    simple=cls.split('$')[0]
    print('##', cls)
    vs=sorted(set(v for k,v in V.items() if base(k)==cls+'.<init>' or base(k).startswith(cls+'.<init>')))
    print('  <init>:', vs)
    for x in E:
        if base(x['dst'])==cls+'.<init>':
            print('  in <-', x['src'], x['kind'], '['+str(V.get(base(x['src']), V.get(x['src'],'?')))[:3]+']', x['trigger'][:60])
    hits=[]
    for f in files:
        for i,l in enumerate(txt[f]):
            if re.search(r'new\s+'+re.escape(cls.split('$')[-1])+r'\s*[(<]|'+re.escape(cls.split('$')[-1])+r'\.class\b|'+re.escape(cls.split('$')[-1])+r'\.newInstance|"[^"]*'+re.escape(cls.split('$')[-1])+r'"', l):
                if os.path.basename(f)==simple.split('.')[-1]+'.java' and re.search(r'class\s+'+re.escape(cls.split('$')[-1]), l): continue
                hits.append('  %s:%d %s'%(os.path.relpath(f,JROOT).replace('org/liberty/android/fantastischmemo/',''),i+1,l.strip()[:150]))
    print('\n'.join(hits[:8]) if hits else '  (no new/.class/string sites)')
