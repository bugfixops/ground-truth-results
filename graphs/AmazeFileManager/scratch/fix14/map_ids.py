import json, sys, os, re
sys.path.insert(0, '/Users/darshan/Desktop/yang/work/tools')
import build_graph as B
W = '/Users/darshan/Desktop/yang/work/'
GDIR = W + 'graphs/AmazeFileManager'
rows = json.load(open(GDIR + '/method_list.json'))
methods, by_name = B.method_names(rows)
edges = []
spans = []

def e(src, dst, kind, trigger, gui=(), guard=None, reads=(), writes=(), note=None,
      needs_state=None, evidence=None, env=None, auto=False, cls=None, via=None, env_kinds=(), state_kinds=()):
    fr = sys._getframe(1)
    x = {'src': src, 'dst': dst, 'kind': kind, 'trigger': trigger, 'gui': list(gui),
         'guard': guard, 'reads': list(reads), 'writes': list(writes), 'note': note,
         'needs_state': needs_state, 'evidence': evidence, 'env': env,
         'edge_class': cls, 'via': via, 'env_kinds': list(env_kinds), 'state_kinds': list(state_kinds)}
    if auto:
        x['auto'] = True
    edges.append(x)
    spans.append(fr.f_lineno)

sups = []
def sup(*pairs):
    sups.extend(pairs)

ns = {'e': e, 'sup': sup, 'SCREENS': {}, 'DEAD': {}, 'FRAMEWORK_ONLY': {}, 'UNREACHABLE': {}, 'TITLE': '', 'NOTES': {},
      'USE_AUTO': False, 'SUPPRESS': set(), 'AUTO': None, 'impl': lambda *a, **k: None, 'METHODS': list(methods),
      'GDIR': GDIR, 'TOOLS': W + 'tools', 'AUTO_DEAD': None, 'COVERAGE': None, 'CLASSIFY': None, 'EDIT': None,
      'ENV_KINDS_OF': {}, 'STATE_KINDS_OF': {}, 'STRICT': False, 'HTML': True, 'FRAMEWORK_NODES': {}}
src_path = GDIR + '/graph_def.py'
exec(compile(open(src_path, encoding='utf-8').read(), src_path, 'exec'), ns)
B.assign_ids(edges)
out = []
for x, ln in zip(edges, spans):
    out.append((x['id'], ln, x['src'], x['dst'], x['kind']))
with open(GDIR + '/scratch/fix14/edge_lines.tsv', 'w') as f:
    for r in out:
        f.write('\t'.join(map(str, r)) + '\n')
print('edges', len(edges), 'sups', len(sups))
