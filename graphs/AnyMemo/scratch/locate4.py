"""Scratch: print the declaration line of each 'Outer$Inner.meth' key (run from work/). Args are keys."""
import os, re, sys
ROOT = '/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo/'
files = {}
for dp, dn, fn in os.walk(ROOT):
    for f in fn:
        if f.endswith('.java'):
            files.setdefault(f[:-5], []).append(os.path.join(dp, f))
DECL_PREFIX = r'^\s*(?:@\w+\s+)*(?:(?:public|private|protected|static|final|synchronized|abstract|native)\s+)*(?:[\w<>\[\],.? ]+\s+)?'
for key in sys.argv[1:]:
    base = re.sub(r'\(.*$', '', key)
    cls, _, meth = base.rpartition('.')
    segs = cls.split('$')
    outer = segs[0]
    inner = segs[-1]
    paths = files.get(outer, [])
    if not paths:
        print('%-70s NO FILE for %s' % (key, outer)); continue
    if len(paths) > 1:
        print('%-70s AMBIG %s' % (key, paths))
    path = paths[0]
    lines = open(path, encoding='utf-8', errors='replace').read().split('\n')
    start = 0
    if len(segs) > 1 and not inner.isdigit():
        for i, l in enumerate(lines):
            if re.search(r'\b(class|interface)\s+' + re.escape(inner) + r'\b', l):
                start = i; break
    name = outer if meth == '<init>' else meth
    if meth == '<init>':
        pat = re.compile(r'\bnew\s+' + re.escape(inner) + r'\s*\(|' + DECL_PREFIX + re.escape(inner) + r'\s*\(') if not inner.isdigit() else None
    else:
        pat = re.compile(DECL_PREFIX + re.escape(meth) + r'\s*\(')
    hit = None
    if pat is not None:
        for i in range(start, len(lines)):
            l = lines[i]
            if re.search(r'\breturn\b|\bthrow\b| = |^\s*\.|\bif\s*\(', l):
                continue
            if pat.search(l):
                hit = i; break
    rel = os.path.relpath(path, ROOT)
    if hit is None:
        print('%-70s %s (no declaration line found)' % (key, rel)); continue
    print('%-70s %s:%d  %s' % (key, rel, hit + 1, lines[hit].strip()[:90]))
