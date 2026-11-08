import sys, os, glob
J = '/Users/darshan/Desktop/yang/work/final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/'
def find(rel):
    for pat in [J + 'app/src/main/java/' + rel, J + 'commons_compress_7z/src/main/java/' + rel]:
        if os.path.exists(pat):
            return pat
    return None
for spec in sys.argv[1:]:
    rel, rng = spec.split(':')
    a, b = [int(x) for x in rng.split('-')]
    p = find(rel)
    print('##', rel, '(', p and 'found' or 'MISSING', ')')
    if not p:
        continue
    L = open(p, encoding='utf-8', errors='replace').read().split('\n')
    for i in range(a - 1, min(b, len(L))):
        print('%5d %s' % (i + 1, L[i][:150]))
