import json,re,collections,subprocess
G='/Users/darshan/Desktop/yang/work/graphs/AnyMemo'
APP='/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src'
R=json.load(open(G+'/scratch/classify.json'))
KW={'return','new','throw','else','case','yield'}
DECL=re.compile(r'(?<![\w.])((?:[\w<>\[\],.?]+)\s+)(\w+)\s*\(')
def is_decl(line,name):
    for m in re.finditer(r'(?<![\w.])'+re.escape(name)+r'\s*\(', line):
        pre=line[:m.start()].rstrip()
        if not pre: continue
        tok=re.search(r'([\w>\]]+)$', pre)
        if tok is None: continue
        t=tok.group(1)
        if t in KW: continue
        if re.search(r'[=(,!&|?:+\-*/]\s*$', pre): continue
        return True
    return False
cache={}
def hits(name):
    if name in cache: return cache[name]
    p=subprocess.run(['grep','-rn','--include=*.java','-w',name,APP],capture_output=True,text=True)
    out=[]
    for l in p.stdout.splitlines():
        f,ln,txt=l.split(':',2)
        rel=f.replace(APP+'/','')
        if re.search(r'(?<![\w.])'+re.escape(name)+r'\s*\(', txt) and not is_decl(txt,name): out.append((rel,int(ln),txt.strip()[:140]))
    cache[name]=out; return out
for x in R:
    name=x['name']
    h=hits(name) if not name.startswith('<') else []
    x['call_main']=[t for t in h if t[0].startswith('main/')]
    x['call_test']=[t for t in h if not t[0].startswith('main/')]
json.dump(R,open(G+'/scratch/classify.json','w'),indent=0)
roots=[x for x in R if x['root']]
c=collections.Counter()
for x in roots:
    k=('main' if x['call_main'] else 'nomain')+'/'+('test' if x['call_test'] else 'notest')
    c[k]+=1
print(c)
