import sys, json, re, importlib.util, os, collections
spec=importlib.util.spec_from_file_location('su','/Users/darshan/Desktop/yang/work/tools/scan_unreachable.py')
su=importlib.util.module_from_spec(spec); spec.loader.exec_module(su)
G='/Users/darshan/Desktop/yang/work/graphs/AnyMemo'
files=su.sources('AnyMemo')
bypath={}
for p in files:
    if p.endswith('.java'): bypath.setdefault(os.path.basename(p)[:-5], []).append(p)
H=json.load(open(G+'/scratch/heads.json'))['heads']
C={r['method']:r for r in json.load(open(G+'/scratch/classify.json'))}
DECL=re.compile(r'^\s*(?:@\w+\s+)*(?:(?:public|private|protected|static|final|synchronized|abstract|native|default)\s+)*(?:<[^>]+>\s*)?[\w<>\[\],.?\s]*\s+NAME\s*\([^;]*$')
rows=[]
for h in H:
    cls, outer, meth = su.simple(h)
    simp = cls.split('.')[-1]
    name = simp if meth=='<init>' else meth
    name = name.replace('<clinit>','').replace('<init>','')
    if meth=='<clinit>': name=None
    outer_name = simp.split('$')[0]
    cands = bypath.get(outer_name, [])
    decl=None; sup=''; calls=[]
    if cands:
        p=cands[0]
        lines=files[p]
        for i,l in enumerate(lines,1):
            if re.search(r'\bclass\s+'+re.escape(outer_name)+r'\b', l) and not su.is_comment(l):
                m=re.search(r'\bextends\s+([\w.<>, ]+?)(\s+implements|\s*\{|$)', l)
                if m: sup=m.group(1).strip()
                break
        if name:
            dpat=re.compile(DECL.pattern.replace('NAME', re.escape(name)))
            for i,l in enumerate(lines,1):
                if su.is_comment(l): continue
                if dpat.search(l) and (decl is None):
                    decl=(os.path.relpath(p,'/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo/')+':%d'%i) if False else (os.path.basename(p)+':%d'%i)
            pat=re.compile(r'\b'+re.escape(name)+r'\s*\(')
            for q in files_for_name(name) if False else []: pass
        # call candidates across all java files, excluding declaration-like lines
        if name:
            pat=re.compile(r'\b'+re.escape(name)+r'\s*\(')
            for q,ls in files.items():
                if not q.endswith('.java'): continue
                for i,l in enumerate(ls,1):
                    if su.is_comment(l) or not pat.search(l): continue
                    if DECL.pattern and re.match(DECL.pattern.replace('NAME', re.escape(name)), l): continue
                    calls.append('%s:%d %s' % (os.path.basename(q), i, l.strip()[:100]))
        else:
            calls=[]
    rows.append({'m':h,'name':name,'ovr':bool(C.get(h,{}).get('override')),'sup':sup,'decl':decl,'ncalls':len(calls),'calls':calls[:3]})
json.dump(rows, open(G+'/scratch/triage.json','w'), indent=1)
print('rows',len(rows),'with calls',sum(1 for r in rows if r['ncalls']),'no calls',sum(1 for r in rows if not r['ncalls']))
