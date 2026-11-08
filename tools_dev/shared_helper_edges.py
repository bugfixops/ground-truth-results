#!/usr/bin/env python3
"""Review 4 fix 2 (Kiro): list edges that start at a shared helper and end in another class's lambda or $N class.
Usage, from the repo root: python3 -I tools_dev/shared_helper_edges.py <App> [min_classes]
An edge src -> dst is listed when dst is a lambda or a nested/anonymous class method (name has lambda$ or the class has $),
dst's top-level class differs from src's, and src has callers (edges into src) from at least min_classes (default 2) classes.
and dst's top-level class is one of those caller classes (the callback or lambda belongs to one caller).
Such an edge lets every caller of the helper reach dst. Prints the count of distinct caller classes and the callers."""
import collections, glob, json, sys
app = sys.argv[1]; mn = int(sys.argv[2]) if len(sys.argv) > 2 else 2
g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % app)[0], encoding='utf-8'))
def cls(m):
    return m.split('@')[0].split('(')[0].rsplit('.', 1)[0]
def top(m):
    return cls(m).split('$')[0]
callers = collections.defaultdict(list)
for e in g['edges']:
    callers[e['src'] if False else e['dst']].append(e)
out = []
for e in g['edges']:
    s, d = e['src'], e['dst']
    if top(s) == top(d) or not ('lambda$' in d or '$' in cls(d)): continue
    cs = {top(x['src']) for x in callers.get(s, []) if x['src'] not in ('S_ENTRY',)}
    # the shape of review 4 fix 2: dst belongs to ONE of the callers (it is that caller's lambda or anonymous class)
    if len(cs) >= mn and top(d) in cs: out.append((len(cs), e['id'], s, d, e['kind'], sorted(cs)[:6]))
out.sort(reverse=True)
src_count = collections.Counter(x[2] for x in out)
print('%s: %d edges; by source (largest first):' % (app, len(out)))
for s, n in src_count.most_common(12): print('  %3d %s' % (n, s))
if '-v' in sys.argv:
    for r in out: print(r)
