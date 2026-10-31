import json, re, sys, glob, os
G='/Users/darshan/Desktop/yang/work/graphs/AnyMemo'
SRC='/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo/'
CL=json.load(open(G+'/scratch/class_lines.json'))
def blocks(path):
    L=open(path,encoding='utf-8',errors='replace').read().split('\n')
    out=[]
    for i,l in enumerate(L):
        if re.search(r'\bnew\s+[\w.<>]+\s*\([^;]*\)\s*\{\s*$', l) or re.search(r'\bnew\s+[\w.<>]+\s*\(\s*$', l) or re.search(r'\bnew\s+[\w.<>]+\s*\([^;]*\)\s*\{', l):
            # brace match from the first '{' at or after line i
            depth=0; started=False; end=None
            for j in range(i, min(i+400,len(L))):
                s=re.sub(r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'','',L[j])
                for ch in s:
                    if ch=='{': depth+=1; started=True
                    elif ch=='}':
                        depth-=1
                if started and depth==0:
                    end=j+1; break
            out.append((i+1,end))
    return out
if __name__=='__main__':
    top=sys.argv[1]   # e.g. ui/PreviewEditActivity
    path=SRC+top+'.java'
    rel=top.replace('/','.')
    bl=blocks(path)
    print('blocks in',top)
    for s,e in bl: print('  block %d-%s' % (s, e))
    names=sorted(k for k in CL if k.startswith('org.liberty.android.fantastischmemo.'+rel.split('.')[-1] + '$') or k.startswith('org.liberty.android.fantastischmemo.'+rel.replace('.','.')+'$'))
    for k in names:
        ls=CL[k]
        if not ls: continue
        mn=ls[0]; mx=ls[-1]
        inside=[ (s,e) for s,e in bl if s-1<=mn<=(e or 0)+1]
        print('  %s lines %d-%d -> block %s' % (k.split('.')[-1], mn, mx, inside[:2]))
