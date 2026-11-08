import json, sys
# Lists each UNRESOLVED key with its incoming edges: src, src verdict, edge kind.
# Usage: python3 -I callers_now.py  (run from work/)
G = json.load(open('graphs/AnyMemo/out/anymemo_trigger_graph.json'))
V = G['verdict']
ins = {}
for ed in G['edges']:
    ins.setdefault(ed['dst'], []).append((ed['src'], ed['kind']))
keys = [l.strip() for l in open('graphs/AnyMemo/scratch/unres_now.txt') if l.strip()]
roots = []
for k in keys:
    srcs = ins.get(k, [])
    desc = ', '.join('%s[%s|%s]' % (s, V.get(s, '?')[:1] if s in V else 'S', kind) for s, kind in srcs)
    if not any(V.get(s) == 'REACHABLE' or s.startswith('S_') for s, _ in srcs):
        roots.append(k)
    print('%s <- %s' % (k, desc if desc else 'NO INCOMING EDGE'))
print('---- keys with no REACHABLE or page caller (roots): %d' % len(roots))
for r in roots:
    print('ROOT ' + r)
