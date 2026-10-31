import ast
import collections
import os
import re
import shutil

W = '/Users/darshan/Desktop/yang/work'
os.chdir(W)
S = 'graphs/AmazeFileManager/scratch/'
G = 'graphs/AmazeFileManager/graph_def.py'
JROOT = 'final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java'

java = set()
for root, _, files in os.walk(JROOT):
    for f in files:
        if f.endswith('.java'):
            java.add(f[:-5])

rows = {}
for x in open(S + 'node_names.tsv' if False else 'graphs/AmazeFileManager/scratch/decisions/node_names.tsv', encoding='utf-8').read().split('\n')[1:]:
    if x:
        rows[x.split('\t')[0]] = x.split('\t')[1]
nodes = set(rows)

work = [x.split('\t') for x in open(S + 'work_items.tsv', encoding='utf-8').read().split('\n')[1:] if x]
unknown = collections.defaultdict(list)
for w in work:
    if w[0] != 'error-edge':
        continue
    m = re.match(r'unknown (src|dst) node (.+)$', w[6])
    if m:
        unknown[m.group(2)].append((int(w[2]), int(w[3]), m.group(1), w[1]))


def norm(n):
    if '/' in n:
        n = n.split('/')[-1]
    parts = n.split('.')
    while len(parts) > 1 and parts[0][:1].islower():
        parts = parts[1:]
    return '.'.join(parts)


cat = {}
target = {}
for n in unknown:
    if n.startswith('S_'):
        cat[n] = 'pseudo'
        continue
    m = norm(n)
    base = m.split('(')[0]
    cands = [x for x in nodes if x == base or x.startswith(base + '(')]
    if len(cands) == 1:
        cat[n] = 'map'
        target[n] = cands[0]
        continue
    if len(cands) > 1:
        cat[n] = 'ambiguous'
        continue
    outer = base.split('.')[0].split('$')[0]
    cat[n] = 'app-missing' if outer in java else 'library'

summary = collections.Counter()
for n, c in cat.items():
    summary[c] += len(unknown[n])
print('by category (occurrences):', dict(summary))

ops = collections.defaultdict(lambda: {'delete': False, 'repl': {}})
for n, c in cat.items():
    for start, end, side, eid in unknown[n]:
        if c == 'library':
            ops[(start, end)]['delete'] = True
        elif c == 'map':
            ops[(start, end)]['repl'][n] = target[n]

gsrc = open(G, encoding='utf-8').read()
lines = gsrc.split('\n')
for (start, end), op in sorted(ops.items(), reverse=True):
    if op['delete']:
        del lines[start - 1:end]
        continue
    seg = '\n'.join(lines[start - 1:end])
    for old, new in op['repl'].items():
        seg = seg.replace("'%s'" % old, "'%s'" % new)
    lines[start - 1:end] = seg.split('\n')
text = '\n'.join(lines)
ast.parse(text)
shutil.copy(G, S + 'graph_def_before_apply_11.py')
open(G, 'w', encoding='utf-8').write(text)
with open(S + 'name_plan.tsv', 'w', encoding='utf-8') as fh:
    for n, c in sorted(cat.items(), key=lambda kv: (kv[1], -len(unknown[kv[0]]))):
        fh.write('%s\t%s\t%d\t%s\n' % (c, n, len(unknown[n]), target.get(n, '')))
print('applied: statements touched', len(ops))
