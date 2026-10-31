import json,re,collections,os
G='/Users/darshan/Desktop/yang/work/graphs/AnyMemo'
APP='/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src'
R=json.load(open(G+'/scratch/classify.json'))
import subprocess
def decl_sites(name, cls):
    p=subprocess.run(['grep','-rn','--include=*.java','-w',name,APP],capture_output=True,text=True)
    out=[]
    for l in p.stdout.splitlines():
        f,ln,txt=l.split(':',2)
        if re.search(r'(?<![\w.])'+re.escape(name)+r'\s*\(', txt):
            out.append((f,int(ln),txt))
    return out
srccache={}
def lines_of(f):
    if f not in srccache: srccache[f]=open(f,encoding='utf-8',errors='replace').read().split('\n')
    return srccache[f]
def class_header(f, simple):
    L=lines_of(f)
    for i,l in enumerate(L):
        m=re.search(r'\b(class|interface|enum)\s+'+re.escape(simple)+r'\b([^{]*)', l)
        if m: return m.group(2)[:160]
    return ''
KW={'return','new','throw','else','case'}
def is_decl(line,name):
    for m in re.finditer(r'(?<![\w.])'+re.escape(name)+r'\s*\(', line):
        pre=line[:m.start()].rstrip()
        if not pre: continue
        t=re.search(r'([\w>\]]+)$', pre)
        if t is None or t.group(1) in KW: continue
        if re.search(r'[=(,!&|?:+\-*/]\s*$', pre): continue
        return True
    return False
for x in R:
    if not x['root'] or x['call_main'] or x['call_test'] or x['name'].startswith('<'): continue
    x['decl']=None; x['override']=False; x['extends']=''
    cls_simple=x['cls'].split('.')[-1]
    for f,ln,txt in decl_sites(x['name'],x['cls']):
        if not is_decl(txt,x['name']): continue
        if not f.startswith(APP+'/main/'): continue
        L=lines_of(f)
        prev=L[ln-2] if ln>=2 else ''
        x['decl']=f"{f.replace(APP+'/','')}:{ln}"
        x['override']= '@Override' in prev or '@Override' in txt
        base=cls_simple.split('$')[0]
        x['extends']=class_header(f, base)
        break
json.dump(R,open(G+'/scratch/classify.json','w'),indent=0)
c=collections.Counter()
for x in R:
    if not (x['root'] and not x['call_main'] and not x['call_test'] and not x['name'].startswith('<')): continue
    c[('override' if x.get('override') else 'plain') + ('' if x.get('decl') else ' nodecl')]+=1
print(c)
