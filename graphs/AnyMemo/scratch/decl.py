import json, os, re, csv, sys
G='/Users/darshan/Desktop/yang/work/graphs/AnyMemo'
APP='/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java'
ALL=[]
for root,_,fs in os.walk(APP):
    for f in fs:
        if f.endswith('.java'): ALL.append(os.path.join(root,f))
BYNAME={}
for p in ALL: BYNAME.setdefault(os.path.basename(p)[:-5],[]).append(p)
def unresolved():
    rows=[r for r in csv.DictReader(open(G+'/out/methods.csv',encoding='utf-8')) if r['verdict']=='UNRESOLVED']
    return [r['method'] for r in rows]
def locate(m):
    cls=m.rsplit('.',1)[0]; mm=m.rsplit('.',1)[1]
    top=cls.split('$')[0]
    name=re.sub(r'\(.*','',mm)
    files=BYNAME.get(top,[])
    if not files: return None,None,False,cls
    f=files[0]
    lines=open(f,encoding='utf-8',errors='replace').read().split('\n')
    if name in ('<init>','<clinit>'): return os.path.relpath(f,APP),0,False,cls
    pat=re.compile(r'\b'+re.escape(name)+r'\s*\(')
    for i,l in enumerate(lines):
        if pat.search(l) and not re.search(r'\b(return|new|=|\.)\s*'+re.escape(name)+r'\s*\(', l.strip()) and not l.strip().startswith('//'):
            prev=lines[i-1].strip() if i>0 else ''
            ov = prev.startswith('@Override') or (i>1 and lines[i-2].strip().startswith('@Override'))
            return os.path.relpath(f,APP),i+1,ov,cls
    return os.path.relpath(f,APP),None,False,cls
if __name__=='__main__':
    out=[]
    for m in unresolved():
        f,ln,ov,cls=locate(m)
        out.append({'method':m,'file':f,'line':ln,'override':ov})
    json.dump(out,open(G+'/scratch/decl.json','w'),indent=0)
    print(len(out),'override',sum(o['override'] for o in out),'noline',sum(1 for o in out if o['line'] is None),'nofile',sum(1 for o in out if o['file'] is None))
