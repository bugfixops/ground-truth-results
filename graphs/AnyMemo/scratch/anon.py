"""Number anonymous classes the way javac does (per enclosing class, in source order) and give each its line range."""
import os,re,json,sys
SRC='/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo'
PKG='org.liberty.android.fantastischmemo'
def strip(text):
    # remove comments and string/char literals, keep newlines
    out=[];i=0;n=len(text)
    while i<n:
        c=text[i]
        if text.startswith('//',i):
            j=text.find('\n',i); j=n if j<0 else j; out.append(' '*(j-i)); i=j; continue
        if text.startswith('/*',i):
            j=text.find('*/',i)+2; seg=text[i:j]; out.append(re.sub(r'[^\n]',' ',seg)); i=j; continue
        if c=='"' or c=="'":
            j=i+1
            while j<n and text[j]!=c:
                j+= 2 if text[j]=='\\' else 1
            seg=text[i:j+1]; out.append(c+re.sub(r'[^\n]',' ',seg[1:-1])+c); i=j+1; continue
        out.append(c); i+=1
    return ''.join(out)
def scan(path, pkgpath):
    raw=open(path,encoding='utf-8',errors='replace').read()
    s=strip(raw)
    # tokens we need: class/interface/enum declarations, 'new X(' ... ')' '{' , braces
    res=[]   # (binary name, file line of new, open-brace index)
    stack=[] # entries: dict(name, kind, depth, counter)
    depth=0
    pending_named=None
    top=os.path.basename(path)[:-5]
    decl=re.compile(r'\b(class|interface|enum)\s+(\w+)')
    newre=re.compile(r'\bnew\s+[\w.$]+(\s*<[^;{}()]*?>)?\s*\(')
    # map positions of declarations and anonymous creations
    events=[]
    for m in decl.finditer(s): events.append((m.start(),'decl',m.group(2)))
    for m in newre.finditer(s):
        # find matching paren
        i=m.end()-1; d=0; j=i
        while j<len(s):
            if s[j]=='(': d+=1
            elif s[j]==')':
                d-=1
                if d==0: break
            j+=1
        k=j+1
        while k<len(s) and s[k] in ' \t\r\n': k+=1
        if k<len(s) and s[k]=='{':
            events.append((k,'anon',m.start()))
    events.sort()
    # walk braces
    ev=0; cur=[('TOP',0)]  # stack of (binary name, brace depth at which body opened)
    counters={}
    pend=None
    out=[]
    brace_stack=[]  # list of (binary) pushed at '{'
    bi=0
    evi=0
    pos_events=events
    pending_decl=None
    for idx,ch in enumerate(s):
        # handle events at this index
        while evi<len(pos_events) and pos_events[evi][0]==idx:
            p,kind,val=pos_events[evi]
            if kind=='decl':
                pending_decl=val
            elif kind=='anon':
                pending_anon=(val)
            evi+=1
        if ch=='{':
            if pending_decl is not None and not (pending_anon if 'pending_anon' in dir() else False):
                parent=cur[-1][0]
                name=(top if parent=='TOP' else parent)+('' if parent=='TOP' else '')
                # named nested: Outer$Inner, top-level: Top
                bn = top if not cur[-1][0] or cur[-1][0]=='TOP' else cur[-1][0]+'$'+pending_decl
                if cur[-1][0]=='TOP': bn=top if pending_decl==top else top+'$'+pending_decl
                cur.append((bn,'decl',pending_decl)); pending_decl=None
            elif 'pending_anon' in dir() and pending_anon is not None:
                encl=cur[-1][0]
                counters[encl]=counters.get(encl,0)+1
                bn='%s$%d'%(encl,counters[encl])
                line=s.count('\n',0,pending_anon)+1
                out.append((bn,line,s.count('\n',0,idx)+1))
                cur.append((bn,'anon',None)); pending_anon=None
            else:
                cur.append((cur[-1][0],'block',None))
            brace_stack.append(len(cur))
        elif ch=='}':
            if len(cur)>1: cur.pop()
            if brace_stack: brace_stack.pop()
    return out
if __name__=='__main__':
    res={}
    for root,dirs,fs in os.walk(SRC):
        for f in fs:
            if f.endswith('.java'):
                p=os.path.join(root,f)
                rel=os.path.relpath(p,SRC)
                for bn,line,bline in scan(p,rel):
                    res[bn]=(rel,line)
    json.dump(res,open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch/anon_map.json','w'),indent=0)
    print(len(res))
