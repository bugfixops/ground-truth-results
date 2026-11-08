# for each simple class name: count 'new Name(' / 'Name.class' / 'extends Name' / XML mentions in app src (read only)
import os,re,sys
ROOT='/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main'
files=[]
for d,_,fs in os.walk(ROOT):
    for f in fs:
        if f.endswith(('.java','.xml','.kt')): files.append(os.path.join(d,f))
txt={f:open(f,encoding='utf-8',errors='replace').read() for f in files}
for name in sys.argv[1:]:
    pats={'new':re.compile(r'new\s+'+re.escape(name)+r'\s*[(<]'),'cls':re.compile(r'\b'+re.escape(name)+r'\.class\b'),
          'ext':re.compile(r'extends\s+'+re.escape(name)+r'\b'),'xml':re.compile(r'\b'+re.escape(name)+r'\b'),'mref':re.compile(re.escape(name)+r'::new')}
    out=[]
    for k in ('new','cls','ext','mref'):
        hits=[(os.path.relpath(f,ROOT),txt[f].count('\n',0,m.start())+1) for f in files if f.endswith('.java') for m in pats[k].finditer(txt[f])]
        if hits: out.append(k+':'+','.join('%s:%d'%h for h in hits[:3]))
    xh=[os.path.relpath(f,ROOT) for f in files if f.endswith('.xml') and pats['xml'].search(txt[f])]
    if xh: out.append('xml:'+','.join(xh[:3]))
    print(name, ' | '.join(out) if out else 'NO SITE')
