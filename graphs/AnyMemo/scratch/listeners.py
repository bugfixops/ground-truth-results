import json,collections,csv,os,sys
a=json.load(open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/auto_calls.json'))
unres=set(l.strip() for l in open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch/unresolved.txt') if l.strip())
verdict={r['method']:r['verdict'] for r in csv.DictReader(open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/out/methods.csv'))}
SRC='/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo'
files={}
for root,dirs,fs in os.walk(SRC):
    for f in fs:
        if f.endswith('.java'): files.setdefault(f,[]).append(os.path.join(root,f))
def line_of(fname,n):
    paths=files.get(fname,[])
    if len(paths)!=1: return ('AMBIG %d'%len(paths))
    L=open(paths[0],encoding='utf-8',errors='replace').read().split('\n')
    return L[n-1].strip()[:150] if 0<n<=len(L) else '?'
news=collections.defaultdict(list)   # dst class.<init> -> [(src,file,line)]
for c in a['calls']:
    if c['dst'].split('(')[0].endswith('.<init>') and c['src'] in verdict or True:
        news[c['dst'].split('(')[0]].append((c['src'],c['file'],c['line']))
out=[]
for m in sorted(unres):
    if '$' not in m.split('.')[0] or m.split('(')[0].split('.')[-1] in ('<init>','<clinit>'): continue
    cls=m.split('.')[0]; name=m.split('(')[0].split('.')[-1]
    cr=news.get(cls+'.<init>',[])
    if not cr: out.append('%s | NO-NEW-SITE'%m); continue
    for src,f,ln in cr:
        out.append('%s | %s [%s] | %s:%s | %s'%(m, src, verdict.get(src,'?'), f, ln, line_of(f,ln)))
open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch/listeners.txt','w').write('\n'.join(out))
print(len(out))
