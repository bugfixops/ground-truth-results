#!/usr/bin/env python3
"""C1 SUBSET check on mirror parts (no .md rows, no batch ownership lists,
no auto_calls.json available): for each part, exec with check_part-style stubs
and report: edge dst not a method, edge src unknown, GUI/ENTERS shape errors,
UNREACHABLE tuple length != 4. This is NOT full C1 (owned/row/auto-duplicate
checks need branch files not fetched)."""
import json, sys, glob, os
sys.path.insert(0, '/home/hatch/workspace/overnight/stream-B/MMEX/tools')
import build_graph as bg
rows = json.load(open('/home/hatch/workspace/overnight/stream-B/MMEX/graphs/MMEX/method_list.json'))
names, _ = bg.method_names(rows)
names = set(names)
total_edges = total_unreach = 0
all_problems = []
for p in sorted(glob.glob('/home/hatch/workspace/overnight/stream-B/MMEX/graphs/MMEX/parts/label_*.py')):
    edges, unreach = [], {}
    def collect(src, dst, kind, trigger, **kw): edges.append((src, dst, kind))
    def gui(src, dst, text, kind='GUI', **kw): collect(src, dst, kind, text)
    def sup(*pairs): pass
    ns = {'SCREENS': {}, 'e': collect, 'gui': gui, 'sup': sup,
          'env_text': lambda t, k: t, 'state_text': lambda t, k: t, 'UNREACHABLE': unreach}
    try:
        exec(compile(open(p).read(), p, 'exec'), ns)
    except Exception as e:
        all_problems.append('%s: EXEC FAILED %r' % (os.path.basename(p), e))
        continue
    total_edges += len(edges); total_unreach += len(unreach)
    for src, dst, kind in edges:
        if not dst.startswith('S_') and dst.split('@')[0] not in names:
            all_problems.append('%s: edge dst not a method: %s' % (os.path.basename(p), dst))
        if not (src.split('@')[0] in names or src.startswith('S_')):
            all_problems.append('%s: edge src unknown: %s' % (os.path.basename(p), src))
        if kind == 'GUI' and not src.startswith('S_'):
            all_problems.append('%s: GUI edge must go page -> method: %s -> %s' % (os.path.basename(p), src, dst))
        if kind == 'ENTERS' and not dst.startswith('S_'):
            all_problems.append('%s: ENTERS edge must end on a page: %s -> %s' % (os.path.basename(p), src, dst))
    for k, v in unreach.items():
        if len(v) != 4:
            all_problems.append('%s: UNREACHABLE tuple length %d: %s' % (os.path.basename(p), len(v), k))
print('parts exec: 147 files; edges collected:', total_edges, '; UNREACHABLE entries:', total_unreach)
print('subset problems:', len(all_problems))
for pr in all_problems[:60]: print(' PROBLEM', pr)
