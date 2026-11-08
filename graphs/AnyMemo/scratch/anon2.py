"""Anonymous classes per file: binary name (javac order = source order per enclosing class), new-line, body end line."""
import os,re,json
from anon import strip
SRC='/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo'
NEW=re.compile(r'\bnew\s+[\w.$]+(\s*<[^;{}()]*?>)?\s*\(')
DECL=re.compile(r'\b(class|interface|enum)\s+(\w+)')
def match_paren(s,i):
    d=0;j=i
    while j<len(s):
        if s[j]=='(': d+=1
        elif s[j]==')':
            d-=1
            if d==0: return j
        j+=1
    return j
def scan(path):
    raw=open(path,encoding='utf-8',errors='replace').read()
    s=strip(raw)
    top=os.path.basename(path)[:-5]
    anon_at={}  # index of '{' -> line of new
    for m in NEW.finditer(s):
        j=match_paren(s,m.end()-1)
        k=j+1
        while k<len(s) and s[k] in ' \t\r\n': k+=1
        if k<len(s) and s[k]=='{':
            anon_at[k]=s.count('\n',0,m.start())+1
    decl_at={}
    for m in DECL.finditer(s):
        # next '{' after the declaration header
        k=s.find('{',m.end())
        if k>=0: decl_at[k]=m.group(2)
    stack=[]   # entries: [name, kind, start_line, counter_dict_for_children]
    counters={}
    res=[]
    line=1
    root={'name':top,'counter':{}}
    stack=[root]
    for idx,ch in enumerate(s):
        if ch=='\n': line+=1; continue
        if ch=='{':
            parent=stack[-1]
            if idx in anon_at:
                pn=parent['name']
                parent['counter'].setdefault('n',0)
                parent['counter']['n']+=1
                bn='%s$%d'%(pn,parent['counter']['n'])
                ent={'name':bn,'counter':{},'kind':'anon','new':anon_at[idx]}
                res.append(ent)
            elif idx in decl_at:
                ent={'name':(top if parent is root else parent['name'])+('' if parent is root and decl_at[idx]==top else ('$'+decl_at[idx] if parent is not root or decl_at[idx]!=top else '')),'counter':{},'kind':'decl','new':None}
                if parent is root and decl_at[idx]==top: ent['name']=top
                elif parent is root: ent['name']=top+'$'+decl_at[idx]
                else: ent['name']=parent['name']+'$'+decl_at[idx]
                res.append(ent)
            else:
                ent={'name':parent['name'],'counter':parent['counter'],'kind':'block','new':None}
            ent['start']=line
            stack.append(ent)
        elif ch=='}':
            if len(stack)>1:
                ent=stack.pop()
                ent['end']=line
    return res
if __name__=='__main__':
    out={}
    for root,dirs,fs in os.walk(SRC):
        for f in fs:
            if not f.endswith('.java'): continue
            p=os.path.join(root,f); rel=os.path.relpath(p,SRC)
            for ent in scan(p):
                if ent['kind']=='anon':
                    out[ent['name']]={'file':rel,'new':ent['new'],'start':ent['start'],'end':ent['end']}
    json.dump(out,open('/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch/anon_map2.json','w'),indent=0)
    print(len(out))
    for k in ['CardEditor$1','CardEditor$3','CardEditor$8','AnyMemo$4','AnyMemo$1','QACardActivity$8']:
        print(k,out.get(k))
