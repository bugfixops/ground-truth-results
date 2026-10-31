import re,sys
APP='/Users/darshan/Desktop/yang/work/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo/'
DECL=re.compile(r'^\s*(?:(?:public|private|protected|static|final|synchronized|abstract)\s+)*(?:<[^>]+>\s+)?[\w<>\[\],.? ]+\s+(\w+)\s*\([^;]*$')
CTOR=re.compile(r'^\s*(?:public|private|protected)\s+(\w+)\s*\([^;]*$')
def enclosing(rel, line):
    L=open(APP+rel,encoding='utf-8',errors='replace').read().split('\n')
    cls=None
    for i in range(line-1,-1,-1):
        s=L[i]
        m=DECL.match(s)
        if m and not re.match(r'\s*(if|for|while|switch|catch|return|new|else|try)\b',s):
            return ('method',m.group(1),i+1,s.strip()[:90])
        m=re.search(r'new\s+([\w.<>]+)\s*\([^)]*\)\s*\{\s*$',s)
        if m and i+1<line:
            return ('anon-new',m.group(1),i+1,s.strip()[:90])
    return ('?','',0,'')
if __name__=='__main__':
    for a in sys.argv[1:]:
        rel,ln=a.rsplit(':',1)
        print(a, enclosing(rel,int(ln)))
