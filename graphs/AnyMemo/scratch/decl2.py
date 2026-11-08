# usage: decl2.py <path-under-java-root-or-basename> name ... : prints the line number(s) where each method is declared (and the closing line guess)
import sys, os, re
JROOT='/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java'
target=sys.argv[1]; names=sys.argv[2:]
p=None
for dp,dn,fn in os.walk(JROOT):
    for f in fn:
        if f==target or os.path.join(dp,f).endswith(target):
            p=os.path.join(dp,f); break
    if p: break
if not p: sys.exit('no file '+target)
L=open(p,encoding='utf-8',errors='replace').read().split('\n')
print(os.path.relpath(p,JROOT).replace('org/liberty/android/fantastischmemo/','')+' ('+str(len(L))+' lines)')
for n in names:
    hits=[i+1 for i,l in enumerate(L) if re.search(r'\b'+re.escape(n)+r'\s*\(', l) and re.search(r'(public|private|protected|void|static|boolean|int|String|View|Object|\w+>?)\s+'+re.escape(n)+r'\s*\(', l) and not l.strip().startswith(('//','*','return','if','else','}'))]
    print('  %s: %s'%(n, ','.join(map(str,hits)) if hits else 'NOT DECLARED HERE'))
