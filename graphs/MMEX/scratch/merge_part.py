import sys

n = sys.argv[1]
G = 'graphs/MMEX/graph_def.py'
P = 'graphs/MMEX/parts/label_%s.py' % n
tag = '# ---- part %s (2026-10-29)' % n
s = open(G).read()
assert s.count(tag) == 0, 'part already merged'
part = open(P).read()
open(G, 'w').write(s.rstrip('\n') + '\n\n' + tag + '\n' + part.rstrip('\n') + '\n')
print('merged', n, len(part))
