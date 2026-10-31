# per class with unresolved methods: source file, class header (extends/implements), count of 'new Simple(' sites, 'Simple.class' sites, manifest, unresolved methods with incoming
import csv, collections, os, re, sys
ROOT='/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main'
JROOT=ROOT+'/java'
rows=list(csv.DictReader(open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/out/methods.csv')))
def owner(s): return s.split('(')[0].rsplit('.',1)[0]
def mname(s): return s.split('(')[0].rsplit('.',1)[1]
files={}
for dp,dn,fn in os.walk(JROOT):
    for f in fn:
        if f.endswith('.java'): files[os.path.join(dp,f)]=open(os.path.join(dp,f),encoding='utf-8',errors='replace').read()
manifest=open(ROOT+'/AndroidManifest.xml').read() if os.path.exists(ROOT+'/AndroidManifest.xml') else ''
classes=collections.OrderedDict()
for r in rows:
    if r['verdict']!='UNRESOLVED': continue
    classes.setdefault(owner(r['method']),[]).append((mname(r['method']),r['incoming_edges']))
out=[]
for c in classes:
    top=c.split('$')[0]; simple=top.split('.')[-1]
    p=None
    for fp in files:
        if os.path.basename(fp)==simple+'.java': p=fp; break
    hdr=''; newn=0; clsn=0
    if p:
        t=files[p]
        m=re.search(r'\b(class|interface|enum)\s+'+re.escape(simple)+r'\b([^{]*)\{', t, re.S)
        if m: hdr=' '.join(m.group(2).split())[:100]
    for fp,t in files.items():
        newn+=len(re.findall(r'new\s+'+re.escape(c.split('.')[-1].replace('$','.').split('.')[-1])+r'\s*[(<]', t))
        clsn+=len(re.findall(r'\b'+re.escape(simple)+r'\.class\b', t))
    man='MANIFEST' if re.search(r'android:name="[^"]*'+re.escape(simple)+r'"', manifest) else ''
    ms=' '.join('%s(%s)'%(n,i) for n,i in classes[c])
    out.append('%s | %s | hdr[%s] | new=%d | cls=%d | %s | %s'%(c, os.path.relpath(p,JROOT).split('/')[-1] if p else 'NOSRC', hdr, newn, clsn, man, ms))
print('\n'.join(out))
