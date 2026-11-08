import sys, os
J = '/Users/darshan/Desktop/yang/work/final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/'
def find(base, hint):
    hits = []
    for root, dirs, files in os.walk(J):
        if base in files and hint in os.path.join(root, base):
            hits.append(os.path.join(root, base))
    hits.sort(key=lambda p: ('src/main' not in p, 'fdroid' not in p, len(p)))
    return hits[0] if hits else None
for spec in sys.argv[1:]:
    base, rng, hint = (spec.split(':') + [''])[:3]
    p = find(base, hint)
    if not p:
        print('## MISSING', base); continue
    a, b = [int(x) for x in rng.split('-')]
    L = open(p, encoding='utf-8', errors='replace').read().split('\n')
    print('##', p.replace(J, ''), 'lines', a, b)
    for i in range(a - 1, min(b, len(L))):
        print('%5d %s' % (i + 1, L[i][:160]))
