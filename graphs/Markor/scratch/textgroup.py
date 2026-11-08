import json, re, os, collections
G='/Users/darshan/Desktop/yang/work/graphs/Markor/'
ROOT='/Users/darshan/Desktop/yang/final_java_only/Markor/app/Markor-#v2.16.1/app'
man={l.split('\t')[0]:l.split('\t')[1].strip() for l in open(G+'scratch/manual_list.txt')}
want=[(k,v) for k,v in man.items() if 'name used in text' in v]
files=[]
for d,dirs,fs in os.walk(ROOT):
    dirs[:]=[x for x in dirs if x not in ('build','.gradle')]
    for f in fs:
        if f.endswith(('.java','.kt','.xml')): files.append(os.path.join(d,f))
txt={p:open(p,encoding='utf-8',errors='replace').read().split('\n') for p in files}
for k,v in sorted(want):
    name=k.split('(')[0].split('.')[-1]
    hits=[]
    for p,ls in txt.items():
        for i,l in enumerate(ls,1):
            if re.search(r'(?<![\w$])'+re.escape(name)+r'\b',l) and not re.search(r'(void|boolean|int|String|Object|public|private|protected|static)\s+[\w<>\[\],. ]*\b'+re.escape(name)+r'\s*\(',l):
                hits.append('%s:%d %s'%(os.path.relpath(p,ROOT).split('/')[-1],i,l.strip()[:70]))
    print(k.split('(')[0][:60], '|', (hits[0] if hits else 'NONE'), '|', len(hits))
