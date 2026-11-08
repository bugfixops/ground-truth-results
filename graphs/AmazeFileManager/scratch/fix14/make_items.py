import re, json, collections, sys
sys.path.insert(0, '/Users/darshan/Desktop/yang/work/tools')
import build_graph as B
GDIR = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager'
G = open(GDIR + '/graph_def.py', encoding='utf-8').read().split('\n')
ed = {}
for l in open(GDIR + '/scratch/fix14/edge_lines.tsv'):
    p = l.rstrip('\n').split('\t')
    ed[p[0]] = int(p[1])
errs = []
for l in open(GDIR + '/scratch/build_finish_14.txt'):
    mm = re.match(r'\s+ERROR (E[0-9a-f]+(?:-\d+)?): unknown (src|dst) node (.*)$', l.rstrip('\n'))
    if mm:
        errs.append((mm.group(1), mm.group(2), mm.group(3)))
import ast
TREE = ast.parse('\n'.join(G))
SPAN = {}
for st in TREE.body:
    if isinstance(st, ast.Expr) and isinstance(st.value, ast.Call) and getattr(st.value.func, 'id', '') == 'e':
        SPAN[st.lineno] = (st.lineno, st.end_lineno)
def stmt(line):
    a, b = SPAN[line]
    return '\n'.join(G[a - 1:b])
items = collections.OrderedDict()
for eid, side, name in errs:
    base = eid.split('-')[0]
    line = ed[eid] if eid in ed else ed[base]
    s = stmt(line)
    key = (s,)
    it = items.setdefault(s, {'lines': [], 'ids': [], 'bad': [], 'line': line})
    it['lines'].append(line); it['ids'].append(eid); it['bad'].append('%s=%s' % (side, name))
out = []
for n, (s, it) in enumerate(items.items(), 1):
    out.append({'item': 'U%03d' % n, 'lines': it['lines'], 'ids': it['ids'], 'bad': sorted(set(it['bad'])), 'stmt': s})
json.dump(out, open(GDIR + '/scratch/fix14/unknown_items.json', 'w'), indent=1)
print('error rows', len(errs), 'unique statements', len(out))
print(collections.Counter(len(o['lines']) for o in out))
