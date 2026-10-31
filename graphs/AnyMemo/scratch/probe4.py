import json,collections,os,re,sys
ROOT='/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo'
G=json.load(open('graphs/AnyMemo/out/anymemo_trigger_graph.json'))
V=G['verdict']; inc=collections.defaultdict(list)
for e in G['edges']: inc[e['dst']].append(e)
U=sorted(k for k,v in V.items() if v=='UNRESOLVED')
files=[]
for dp,dn,fn in os.walk(ROOT):
    for f in fn:
        if f.endswith('.java'): files.append(os.path.join(dp,f))
texts={p:open(p,encoding='utf-8',errors='replace').read().split('\n') for p in files}
mode=sys.argv[1]
for k in U:
    if mode=='noinc' and inc.get(k): continue
    if mode=='inc' and not inc.get(k): continue
    base=k.split('(')[0]
    if '<' in base: continue
    name=base.split('.')[-1]
    hits=[]
    for p,ls in texts.items():
        for i,l in enumerate(ls):
            if re.search(r'\b'+re.escape(name)+r'\s*\(', l) and not re.search(r'(void|public|private|protected|static|\w+\s+'+re.escape(name)+r'\s*\([^)]*\)\s*\{?\s*$)', l.strip()[:200]) :
                hits.append('%s:%d' % (os.path.relpath(p,ROOT), i+1))
    print(k, len(hits), hits[:4])
