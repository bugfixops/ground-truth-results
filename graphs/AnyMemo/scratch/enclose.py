"""Scratch: print the enclosing declarations of file:line pairs (indentation based). Run from work/."""
import re, sys
ROOT = '/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo/'
SKIP = re.compile(r'^\s*(if|for|while|switch|try|catch|else|return|new|do|synchronized)\b')
DECL = re.compile(r'\(')
def ind(s):
    return len(s) - len(s.lstrip(' '))
for arg in sys.argv[1:]:
    rel, ln = arg.rsplit(':', 1)
    ln = int(ln)
    lines = open(ROOT + rel, encoding='utf-8', errors='replace').read().split('\n')
    cur = ind(lines[ln - 1])
    chain = []
    i = ln - 2
    level = cur
    while i >= 0 and len(chain) < 4:
        s = lines[i]
        if s.strip() and ind(s) < level and not s.strip().startswith(('}', '//', '*', '@')):
            t = s.strip()
            if re.search(r'\b(class|interface)\b', t):
                chain.append('CLASS L%d: %s' % (i + 1, t[:110]))
                level = ind(s)
            elif DECL.search(t) and t.endswith('{') and not SKIP.match(t):
                chain.append('METHOD L%d: %s' % (i + 1, t[:110]))
                level = ind(s)
            elif t.endswith('{') and re.search(r'new \S+\s*\(', t):
                chain.append('ANON L%d: %s' % (i + 1, t[:110]))
                level = ind(s)
        i -= 1
    print(arg, '->')
    for c in chain:
        print('   ', c)
