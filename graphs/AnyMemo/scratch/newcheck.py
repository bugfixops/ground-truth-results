# for a class simple name: count 'new X(' / 'X.class' / 'X::new' / string "X" in app java and res/xml, excluding its own file
import os, re, sys
APP='/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main'
def scan(simple, own_basename=None):
    hits=[]
    pn=re.compile(r'new\s+(?:[\w.]+\.)?%s\s*(?:<[^>]*>)?\s*\(' % re.escape(simple))
    pc=re.compile(r'\b%s\.class\b' % re.escape(simple))
    ps=re.compile(r'"(?:[\w.]+\.)?%s"' % re.escape(simple))
    pm=re.compile(r'\b%s::new\b' % re.escape(simple))
    for dp,dn,fn in os.walk(APP):
        for f in fn:
            if not (f.endswith('.java') or f.endswith('.xml')): continue
            if f==own_basename: continue
            p=os.path.join(dp,f)
            for i,l in enumerate(open(p,encoding='utf-8',errors='replace')):
                if pn.search(l) or pc.search(l) or ps.search(l) or pm.search(l):
                    hits.append('%s:%d %s'%(os.path.relpath(p,APP),i+1,l.strip()[:120]))
    return hits
if __name__=='__main__':
    for name in sys.argv[1:]:
        h=scan(name, name+'.java')
        print('== %s new/class/string refs: %d'%(name,len(h)))
        for x in h[:5]: print('   '+x)
