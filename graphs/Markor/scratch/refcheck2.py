import os, re, sys
# Usage: python3 -I scratch/refcheck2.py Name1 Name2 ...
# Prints, per name, how many source/layout files outside app/build mention it and the first few hits.
ROOT = '/Users/darshan/Desktop/yang/final_java_only/Markor/app/Markor-#v2.16.1'
names = sys.argv[1:]
hits = {n: [] for n in names}
pats = {n: re.compile(r'\b%s\b' % re.escape(n)) for n in names}
for d, dirs, fs in os.walk(ROOT):
    dirs[:] = [x for x in dirs if x not in ('build', '.gradle')]
    for f in fs:
        p = os.path.join(d, f)
        if os.path.getsize(p) > 3000000:
            continue
        try:
            txt = open(p, encoding='utf-8', errors='replace').read()
        except Exception:
            continue
        for n in names:
            if pats[n].search(txt):
                ln = next(i for i, l in enumerate(txt.split('\n'), 1) if pats[n].search(l))
                hits[n].append('%s:%d' % (os.path.relpath(p, ROOT), ln))
for n in names:
    print(n, len(hits[n]), ' '.join(h.split('/')[-1] for h in hits[n][:5]))
