import ast
import csv
import glob
import json
import os
import shutil
import sys
from collections import Counter, defaultdict

W = '/Users/darshan/Desktop/yang/work/'
BASE = W + 'graphs/AmazeFileManager/'
S = BASE + 'scratch/'
G = BASE + 'graph_def.py'

dry = '--dry' in sys.argv
build_no = sys.argv[sys.argv.index('--build') + 1] if '--build' in sys.argv else '17'
tsv_files = [a for a in sys.argv[1:] if a.endswith('.tsv')]

items = {it['item']: it for it in json.load(open(BASE + 'scratch/fix14/unknown_items.json', encoding='utf-8'))}

renames = defaultdict(dict)
deletes = set()
unsure = []
for f in tsv_files:
    for r in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t'):
        if r['action'] == 'RENAME':
            renames[r['item']][r['side']] = r['new_name']
        elif r['action'] == 'DELETE':
            deletes.add(r['item'])
        else:
            unsure.append((r['item'], r['side']))

print('delete takes precedence over rename for', sorted(i for i in deletes if i in renames))

src = open(G, encoding='utf-8').read()
lines = src.split('\n')
tree = ast.parse(src)

by_text = {}
for it_id, it in items.items():
    by_text.setdefault(it['stmt'], []).append(it_id)

plan = []
matched = Counter()
for st in tree.body:
    if not (isinstance(st, ast.Expr) and isinstance(st.value, ast.Call) and getattr(st.value.func, 'id', '') == 'e'):
        continue
    seg = '\n'.join(lines[st.lineno - 1:st.end_lineno])
    ids = by_text.get(seg)
    if not ids:
        continue
    for it_id in ids:
        matched[it_id] += 1
    if any(i in deletes for i in ids):
        plan.append(('delete', st.lineno, st.end_lineno, seg, ids))
        continue
    needed = {}
    for it_id in ids:
        for side, nm in renames.get(it_id, {}).items():
            needed[side] = nm
    if not needed:
        continue
    seg_b = seg.encode('utf-8')
    starts = [0]
    for ln in seg.split('\n'):
        starts.append(starts[-1] + len(ln.encode('utf-8')) + 1)
    call = ast.parse(seg).body[0].value
    reps = []
    for side, idx in (('src', 0), ('dst', 1)):
        if side not in needed:
            continue
        node = call.args[idx]
        assert isinstance(node, ast.Constant) and isinstance(node.value, str), (seg[:80], side)
        a = starts[node.lineno - 1] + node.col_offset
        b = starts[node.end_lineno - 1] + node.end_col_offset
        reps.append((a, b, ("'" + needed[side] + "'").encode('utf-8')))
    for a, b, new in sorted(reps, reverse=True):
        seg_b = seg_b[:a] + new + seg_b[b:]
    plan.append(('rename', st.lineno, st.end_lineno, seg_b.decode('utf-8'), ids))

not_matched = [i for i in items if matched[i] == 0 and (i in renames or i in deletes)]
print('plan: delete', sum(1 for p in plan if p[0] == 'delete'), 'rename', sum(1 for p in plan if p[0] == 'rename'))
print('item statements with copies matched', len(matched), 'targets not matched', len(not_matched), not_matched[:10])
print('unsure rows left unchanged', len(unsure))

if dry:
    sys.exit(0)

out_lines = list(lines)
for kind, s, e_, newseg, ids in sorted(plan, key=lambda p: p[1], reverse=True):
    if kind == 'delete':
        del out_lines[s - 1:e_]
    else:
        out_lines[s - 1:e_] = newseg.split('\n')
text = '\n'.join(out_lines)
ast.parse(text)
backup = S + 'graph_def_before_finish_%s.py' % build_no
if not os.path.exists(backup):
    shutil.copy(G, backup)
open(G, 'w', encoding='utf-8').write(text)
print('written', G, 'backup', backup)
