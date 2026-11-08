import json
import os
import re
import sys

sys.path.insert(0, 'tools')
import build_graph as bg

n = sys.argv[1]
P = 'graphs/MMEX/parts/label_%s.py' % n
MD = 'graphs/MMEX/parts/label_%s.md' % n
B = 'graphs/MMEX/scratch/batches/batch_%s.txt' % n

rows = json.load(open('graphs/MMEX/method_list.json'))
names, _ = bg.method_names(rows)
names = set(names)
owned = set(l.strip() for l in open(B) if l.strip() and not l.startswith('#'))

auto_pairs = {(c['src'], c['dst']) for c in json.load(open('graphs/MMEX/auto_calls.json'))['calls']}

edges, unreach = [], {}


def collect(src, dst, kind, trigger, **kw):
    edges.append((src, dst, kind))


def gui(src, dst, text, kind='GUI', **kw):
    collect(src, dst, kind, text)


def sup(*pairs):
    pass


ns = {'SCREENS': {}, 'e': collect, 'gui': gui, 'sup': sup, 'env_text': lambda t, k: t,
      'state_text': lambda t, k: t, 'UNREACHABLE': unreach}
exec(compile(open(P).read(), P, 'exec'), ns)

problems = []
for src, dst, kind in edges:
    if dst.startswith('S_'):
        pass
    elif dst not in names:
        problems.append('edge dst not a method: %s' % dst)
    elif dst not in owned:
        problems.append('edge dst not owned by batch: %s' % dst)
    if not (src in names or src.startswith('S_')):
        problems.append('edge src unknown: %s' % src)
    if kind == 'GUI' and not src.startswith('S_'):
        problems.append('GUI edge must go page -> method: %s -> %s' % (src, dst))
    if kind == 'ENTERS' and not dst.startswith('S_'):
        problems.append('ENTERS edge must end on a page: %s -> %s' % (src, dst))
    if kind == 'CALL' and (src, dst) in auto_pairs:
        problems.append('CALL duplicates auto_calls.json: %s -> %s' % (src, dst))
for k, v in unreach.items():
    if k not in owned:
        problems.append('UNREACHABLE key not owned: %s' % k)
    if len(v) != 4:
        problems.append('UNREACHABLE tuple length %d: %s' % (len(v), k))

md_rows = {}
for line in open(MD):
    if not line.startswith('| ') or line.startswith('| method') or line.startswith('|---'):
        continue
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    method = cells[0].strip('`')
    label = cells[1] if len(cells) > 1 else ''
    md_rows.setdefault(method, []).append(label)
for m in owned:
    if m not in md_rows:
        problems.append('no row for method: %s' % m)
    elif len(md_rows[m]) != 1:
        problems.append('%d rows for method: %s' % (len(md_rows[m]), m))
for m, labs in md_rows.items():
    if m not in owned:
        problems.append('row for method not in batch: %s' % m)
    if labs[0] not in ('REACHABLE', 'UNREACHABLE', 'INCOMPLETE'):
        problems.append('bad label %r for %s' % (labs[0], m))

status_first = open(MD).readline().strip()
status_last = [l for l in open(MD) if l.strip()][-1].strip()
print('batch', n, 'owned', len(owned), 'rows', len(md_rows), 'edges', len(edges),
      'unreachable', len(unreach))
print('first:', status_first)
print('last:', status_last)
print('reachable rows', sum(1 for v in md_rows.values() if v[0] == 'REACHABLE'),
      'unreachable rows', sum(1 for v in md_rows.values() if v[0] == 'UNREACHABLE'))
for p in problems:
    print('PROBLEM', p)
if not problems:
    print('no problems')
