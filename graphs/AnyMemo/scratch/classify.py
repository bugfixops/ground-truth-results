import json,csv,re,collections,subprocess,os
G='/Users/darshan/Desktop/yang/work/graphs/AnyMemo'
APP='/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src'
d=json.load(open(G+'/out/anymemo_trigger_graph.json'))
inc=collections.Counter(e['dst'] for e in d['edges'])
rows=[r for r in csv.DictReader(open(G+'/out/methods.csv',encoding='utf-8')) if r['verdict']=='UNRESOLVED']
res=[]
cache={}
def grep(name):
    if name in cache: return cache[name]
    p=subprocess.run(['grep','-rn','--include=*.java','-w',name,APP],capture_output=True,text=True)
    hits=[]
    for l in p.stdout.splitlines():
        f,ln,txt=l.split(':',2)
        rel=f.replace(APP+'/','')
        hits.append((rel,int(ln),txt.strip()))
    cache[name]=hits
    return hits
for r in rows:
    m=r['method']
    c,rest=m.split('.',1) if '.' in m else (m,'')
    cls=m.rsplit('.',1)[0]
    name=re.sub(r'\(.*','',m.rsplit('.',1)[1]) if '.' in m else m
    if name in ('<init>','<clinit>'): name=cls.split('.')[-1].split('$')[-1]
    hits=grep(name)
    main=[h for h in hits if h[0].startswith('main/')]
    test=[h for h in hits if not h[0].startswith('main/')]
    res.append({'method':m,'cls':cls,'name':name,'root':inc[m]==0,'incoming':inc[m],'main_hits':len(main),'test_hits':len(test),
                'main_sample':[f"{a}:{b}: {t[:110]}" for a,b,t in main[:4]],'test_sample':[f"{a}:{b}" for a,b,t in test[:3]],'decl':r['method']})
json.dump(res,open(G+'/scratch/classify.json','w'),indent=0)
print(len(res),'roots',sum(x['root'] for x in res))
