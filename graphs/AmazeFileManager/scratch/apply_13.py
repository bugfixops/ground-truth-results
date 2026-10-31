import ast
import collections
import os
import re
import shutil

W = '/Users/darshan/Desktop/yang/work'
os.chdir(W)
S = 'graphs/AmazeFileManager/scratch/'
D = S + 'decisions11/'
G = 'graphs/AmazeFileManager/graph_def.py'

base = open(S + 'snapshot_13.py', encoding='utf-8').read()
lines = base.split('\n')
tree = ast.parse(base)
names = {x.split('\t')[0] for x in open(S + 'decisions/node_names.tsv', encoding='utf-8').read().split('\n')[1:] if x}


def tsv(path, n):
    out = []
    for x in open(path, encoding='utf-8').read().split('\n')[1:]:
        if not x:
            continue
        f = x.split('\t')
        assert len(f) == n, (path, x)
        out.append(f)
    return out


def items_unknown(path):
    d = {}
    for x in open(path, encoding='utf-8').read().split('\n'):
        if not x:
            continue
        eid, start, end, src, dst, msg = x.split('\t')
        m = re.match(r'unknown (src|dst) node (.+)$', msg)
        assert m, msg
        d[(eid, m.group(1))] = (int(start), int(end), m.group(2))
    return d


def items_warn(path):
    d = {}
    for x in open(path, encoding='utf-8').read().split('\n'):
        if not x:
            continue
        kind, eid, start, end, src, dst, method = x.split('\t')
        d[(eid, method)] = (kind, int(start) if start else None, int(end) if end else None, src, dst)
    return d


ARG = r"('[^'\n]*')"
deletes = set()
repl = collections.defaultdict(dict)
pairs = set()
drop_methods = set()
counts = collections.Counter()


def add_map(span, idx, old, new):
    prev = repl[span].get(idx)
    assert prev is None or prev == (old, new), (span, idx, prev, old, new)
    repl[span][idx] = (old, new)


def add_delete(span):
    deletes.add(span)


for path, src_items in (
        (D + 'A_ambiguous.tsv', items_unknown(S + 'items_A_ambiguous.tsv')),
        (D + 'B_app_missing_pseudo.tsv', items_unknown(S + 'items_B_app_missing_pseudo.tsv'))):
    for eid, side, action, target, reason in tsv(path, 5):
        if (eid, side) not in src_items:
            raise SystemExit('no item for %s %s in %s' % (eid, side, path))
        start, end, old = src_items[(eid, side)]
        idx = 0 if side == 'src' else 1
        counts[(path.split('/')[-1], action)] += 1
        if action == 'map':
            assert target in names, (eid, target)
            add_map((start, end), idx, old, target)
        elif action == 'delete':
            add_delete((start, end))
        elif action != 'keep_unresolved':
            raise SystemExit('bad action %s' % action)

warn_items = items_warn(S + 'items_C_warn_other.tsv')
warn_items.update(items_warn(S + 'items_D_glide.tsv'))
for path in (D + 'C_warn_other.tsv', D + 'D_glide.tsv'):
    for eid, kind, action, method, reason in tsv(path, 5):
        key = (eid, method)
        if key not in warn_items:
            raise SystemExit('no warn item for %s %s' % key)
        wkind, start, end, src, dst = warn_items[key]
        assert wkind == kind, (key, wkind, kind)
        counts[(path.split('/')[-1], action)] += 1
        if action == 'drop_edge':
            assert kind == 'warn-edge', key
            add_delete((start, end))
        elif action == 'drop_unreachable':
            drop_methods.add(method)
        elif action == 'sup':
            pairs.add((src, dst))
        elif action != 'keep_unresolved':
            raise SystemExit('bad action %s' % action)

top = []
for st in tree.body:
    if isinstance(st, ast.Expr) and isinstance(st.value, ast.Call) and getattr(st.value.func, 'id', '') == 'e':
        a = st.value.args
        if len(a) >= 2 and all(isinstance(x, ast.Constant) for x in a[:2]):
            top.append((st.lineno, st.end_lineno, a[0].value, a[1].value))

for s, e_, a0, a1 in top:
    if (a0, a1) == ('SevenZipExtractor.extractEverything', 'SevenZFile.read(byte[])'):
        add_delete((s, e_))
        counts['manual-delete-bogus-sevenz'] += 1
    if a0 == 'ExtractService.onStartCommand' and a1 in ('CompressedHelper.getExtractorInstance', 'CompressedHelper.getFileName'):
        add_map((s, e_), 0, a0, 'ExtractService$DoWork.doInBackground')
        counts['manual-src-doInBackground'] += 1
    if (a0, a1) == ('AboutActivity.onCreate', 'AboutActivity.onClick'):
        add_map((s, e_), 0, a0, 'S_ABOUT')
        counts['manual-gui-page-src'] += 1

direct = collections.defaultdict(list)
dict_keys = set()
for st in tree.body:
    if isinstance(st, ast.Assign) and len(st.targets) == 1 and isinstance(st.targets[0], ast.Subscript) \
            and getattr(st.targets[0].value, 'id', '') == 'UNREACHABLE' and isinstance(st.targets[0].slice, ast.Constant):
        direct[st.targets[0].slice.value].append((st.lineno, st.end_lineno))
    if isinstance(st, ast.Assign) and len(st.targets) == 1 and isinstance(st.targets[0], ast.Name) \
            and st.targets[0].id == 'UNREACHABLE' and isinstance(st.value, ast.Dict):
        dict_keys |= {k.value for k in st.value.keys if isinstance(k, ast.Constant)}

manual_unreachable = {'CompressedExplorerFragment.onSaveInstanceState', 'LayoutElementParcelable.writeToParcel'}
pops = []
for m in sorted(drop_methods | manual_unreachable):
    for span in direct.get(m, []):
        add_delete(span)
    if m in dict_keys:
        pops.append(m)
    counts['drop_unreachable'] += 1

for span in sorted(deletes & set(repl)):
    raise SystemExit('conflict: delete and map on %s' % (span,))

ARG_RE = re.compile(r"e\(\s*" + ARG + r"\s*,\s*" + ARG)


def apply_stmt(text, rep):
    m = ARG_RE.match(text)
    assert m, text[:120]
    spans = [m.span(1), m.span(2)]
    out = text
    for idx in sorted(rep, reverse=True):
        old, new = rep[idx]
        s, e_ = spans[idx]
        assert ast.literal_eval(out[s:e_]) == old, (out[s:e_], old)
        out = out[:s] + repr(new) + out[e_:]
    return out


edits = {}
for span in deletes:
    edits[span] = None
for span, rep in repl.items():
    if span not in edits:
        edits[span] = rep

for (s, e_) in sorted(edits, reverse=True):
    if edits[(s, e_)] is None:
        lines[s - 1:e_] = []
    else:
        text = '\n'.join(lines[s - 1:e_])
        assert text.startswith('e('), text[:80]
        lines[s - 1:e_] = apply_stmt(text, edits[(s, e_)]).split('\n')

manual_routes = """e('CompressedExplorerFragment.onActivityCreated', 'CompressedExplorerFragment.onSaveInstanceState', 'LIFECYCLE', 'Framework calls onSaveInstanceState to save fragment state', evidence='SRC fragments/CompressedExplorerFragment.java:225 public void onSaveInstanceState(Bundle outState); same convention as MainFragment.onActivityCreated -> onSaveInstanceState at MainFragment.java:397')

e('MainFragment.onSaveInstanceState', 'LayoutElementParcelable.writeToParcel', 'FRAMEWORK', 'Bundle.putParcelableArrayList stores LIST_ELEMENTS; the framework marshals each element by calling writeToParcel', evidence='SRC fragments/MainFragment.java:415 outState.putParcelableArrayList("list", LIST_ELEMENTS); LIST_ELEMENTS declared at line 153 as ArrayList<LayoutElementParcelable>; INFERRED Bundle marshalling (platform source not read)')
"""

helper_routes = ''
for name in ('D_glide_routes.py', 'E_pages_routes.py'):
    if os.path.exists(D + name):
        part = open(D + name, encoding='utf-8').read().strip('\n') + '\n'
        ast.parse(part)
        helper_routes += part + '\n'

text = '\n'.join(lines).rstrip('\n') + '\n\n' + manual_routes + '\n' + helper_routes + '\n'
if pairs:
    text += 'sup(\n'
    for s_, d_ in sorted(pairs):
        text += '    (%r, %r),\n' % (s_, d_)
    text += ')\n'
for m in pops:
    text += 'UNREACHABLE.pop(%r, None)\n' % m
ast.parse(text)

shutil.copy(G, S + 'graph_def_before_apply_13.py')
open(G, 'w', encoding='utf-8').write(text)
print('ops', dict(counts))
print('deleted statements', len(deletes), 'mapped statements', len(repl), 'sup pairs', len(pairs), 'pops', len(pops))
