import ast
import collections
import json
import os
import re
import subprocess

W = '/Users/darshan/Desktop/yang/work'
S = 'graphs/AmazeFileManager/scratch/'
os.chdir(W)

src = open('tools/build_graph.py', encoding='utf-8').read()
a = "        edges.append(x)\n\n    auto_path"
b = "    assign_ids(edges)\n\n    errors, warnings = [], []"
assert src.count(a) == 1 and src.count(b) == 1
src = src.replace(a, "        x['_ln'] = None if auto else sys._getframe(1).f_lineno\n        edges.append(x)\n\n    auto_path")
src = src.replace(b, "    assign_ids(edges)\n    with open('%sedge_lines.json', 'w') as fh:\n        json.dump({x['id']: x.get('_ln') for x in edges}, fh)\n    os._exit(0)\n\n    errors, warnings = [], []" % S)
open(S + 'build_lines.py', 'w', encoding='utf-8').write(src)
subprocess.run(['python3', '-I', S + 'build_lines.py', 'graphs/AmazeFileManager', 'amazefilemanager'], check=True)

ln = json.load(open(S + 'edge_lines.json'))
gsrc = open('graphs/AmazeFileManager/graph_def.py', encoding='utf-8').read()
tree = ast.parse(gsrc)
top = [st for st in tree.body if isinstance(st, ast.Expr) and isinstance(st.value, ast.Call)
       and getattr(st.value.func, 'id', '') == 'e']
rows = {}
for st in top:
    a_ = st.value.args
    rows.setdefault('_spans', []).append((st.lineno, st.end_lineno))
spans = rows['_spans']


def stmt_at(line):
    for st in top:
        if st.lineno <= line <= st.end_lineno:
            return st
    return None


edge_by_id = {}
missing = 0
for eid, line in ln.items():
    if line is None:
        continue
    st = stmt_at(line)
    if st is None:
        missing += 1
        continue
    a_ = st.value.args
    edge_by_id[eid] = (st.lineno, st.end_lineno,
                       ast.get_source_segment(gsrc, a_[0]) if a_ else '',
                       ast.get_source_segment(gsrc, a_[1]) if len(a_) > 1 else '')
print('edges indexed', len(edge_by_id), 'not at top level', missing)

unreach = []
for st in tree.body:
    if isinstance(st, ast.Assign) and len(st.targets) == 1 and isinstance(st.targets[0], ast.Subscript) \
            and getattr(st.targets[0].value, 'id', '') == 'UNREACHABLE' and isinstance(st.targets[0].slice, ast.Constant):
        unreach.append((st.targets[0].slice.value, st.lineno, st.end_lineno))
print('direct UNREACHABLE assignments', len(unreach))

import sys
build = open(S + sys.argv[1], encoding='utf-8').read().split('\n')
import hashlib
auto_info = {}
seen_ids = collections.Counter()
for x in json.load(open('graphs/AmazeFileManager/out/amazefilemanager_trigger_graph.json', encoding='utf-8'))['edges']:
    key = '|'.join(str(x.get(k) or '') for k in ('src', 'dst', 'kind', 'trigger', 'guard', 'evidence', 'env', 'needs_state'))
    h = 'E' + hashlib.sha1(key.encode('utf-8')).hexdigest()[:8]
    seen_ids[h] += 1
    auto_info[h if seen_ids[h] == 1 else '%s-%d' % (h, seen_ids[h])] = (x['src'], x['dst'], x['kind'])
out = open(S + 'work_items.tsv', 'w', encoding='utf-8')
out.write('kind\tid\tstart\tend\tsrc\tdst\tmessage\n')
for x in build:
    m = re.match(r'\s*ERROR (E[0-9a-f]+(?:-\d+)?): (.*)$', x)
    if m:
        eid, msg = m.group(1), m.group(2)
        base = eid.split('-')[0]
        info = edge_by_id.get(eid)
        if info:
            out.write('error-edge\t%s\t%d\t%d\t%s\t%s\t%s\n' % (eid, info[0], info[1], info[2], info[3], msg))
        else:
            out.write('error-other\t%s\t\t\t\t\t%s\n' % (eid, msg))
        continue
    m = re.match(r'\s*ERROR (.*)$', x)
    if m:
        out.write('error-text\t\t\t\t\t\t%s\n' % m.group(1))
        continue
    m = re.match(r'\s*WARN (\S+) is UNREACHABLE but has incoming edges \[(.*)\]', x)
    if m:
        meth = m.group(1)
        ids = re.findall(r"'([^']+)'", m.group(2))
        for eid in ids:
            info = edge_by_id.get(eid)
            if info:
                out.write('warn-edge\t%s\t%d\t%d\t%s\t%s\t%s\n' % (eid, info[0], info[1], info[2], info[3], meth))
            else:
                a_s = auto_info.get(eid, ('?', '?', '?'))
                out.write('warn-edge-auto\t%s\t\t\t%s\t%s\t%s\n' % (eid, a_s[0], a_s[1], meth))
out.close()
json.dump({k: [a_, b_] for k, a_, b_ in unreach}, open(S + 'unreach_lines.json', 'w'))
print('work items written')
