import re, sys
S='/Users/darshan/Desktop/yang/work/final_java_only/MMEX/app/MMEX-#v2024.06.14/app/src/main/java/com/money/manager/ex/'
pat = re.compile(r'^\s*(?:@\w+\s+)*(?:public |private |protected |static |final |synchronized |abstract )*[\w<>\[\], .?]+\s+(\w+)\s*\([^;]*$')
ctor = re.compile(r'^\s*(?:public |private |protected )?([A-Z]\w*)\s*\([^;]*$')
def enclosing(path, line):
    lines = open(S+path, encoding='utf-8', errors='replace').read().split('\n')
    for i in range(line-1, -1, -1):
        t = lines[i]
        if t.strip().startswith(('if','for','while','switch','return','} else','else','catch','try')):
            continue
        m = pat.match(t) or ctor.match(t)
        if m and not t.strip().endswith(';') and ('{' in t or (i+1 < len(lines) and '{' in lines[i+1]) or t.rstrip().endswith(',')):
            return '%s:%d %s' % (path, i+1, t.strip()[:110])
    return 'none'
for arg in sys.argv[1:]:
    p, l = arg.rsplit(':', 1)
    print(enclosing(p, int(l)), '  <- line', l)
