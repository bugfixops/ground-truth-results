import ast
import os
import shutil

W = '/Users/darshan/Desktop/yang/work'
os.chdir(W)
S = 'graphs/AmazeFileManager/scratch/'
G = 'graphs/AmazeFileManager/graph_def.py'

src = open(G, encoding='utf-8').read()
lines = src.split('\n')
tree = ast.parse(src)


def about(v):
    return isinstance(v, str) and (v.startswith('AboutActivity.') or v == 'S_ABOUT')


drop = set()
for st in tree.body:
    if isinstance(st, ast.Expr) and isinstance(st.value, ast.Call) and getattr(st.value.func, 'id', '') == 'e':
        a = st.value.args
        if len(a) >= 2 and isinstance(a[0], ast.Constant) and isinstance(a[1], ast.Constant):
            if about(a[0].value) or about(a[1].value):
                drop.add((st.lineno, st.end_lineno))

for s, e_ in drop:
    assert lines[s - 1].startswith('e('), (s, lines[s - 1][:80])

drop_lines = set()
for s, e_ in drop:
    drop_lines.update(range(s, e_ + 1))

for i, l in enumerate(lines, 1):
    if l == "    'S_ABOUT': 'AboutActivity: about screen with app info',":
        drop_lines.add(i)
    if l in ('# AboutActivity (no intent-filter, in-app only)', '# AboutActivity routes'):
        drop_lines.add(i)

out = [l for i, l in enumerate(lines, 1) if i not in drop_lines]
text = '\n'.join(out)
ast.parse(text)
shutil.copy(G, S + 'graph_def_before_finish_14.py') if not os.path.exists(S + 'graph_def_before_finish_14.py') else None
open(G, 'w', encoding='utf-8').write(text)
print('removed top-level e() statements', len(drop), 'lines', len(drop_lines))
