import collections
import json
import os
import re
import shutil

os.chdir('/Users/darshan/Desktop/yang/work')
S = 'graphs/AmazeFileManager/scratch/'
shutil.copy('graphs/AmazeFileManager/graph_def.py', S + 'snapshot_13.py')
verdict = json.load(open('graphs/AmazeFileManager/out/amazefilemanager_trigger_graph.json', encoding='utf-8'))['verdict']
with open(S + 'verdict_13.tsv', 'w', encoding='utf-8') as fh:
    for k, v in sorted(verdict.items()):
        fh.write('%s\t%s\n' % (k, v))
rows = [l.split('\t') for l in open(S + 'work_items.tsv', encoding='utf-8').read().split('\n')[1:] if l]
cls = {}
for line in open(S + 'name_plan.tsv', encoding='utf-8').read().split('\n'):
    if line:
        c, n, cnt, tgt = line.split('\t')[:4]
        cls[n] = c

groups = collections.defaultdict(list)
for r in rows:
    kind = r[0]
    if kind == 'error-edge':
        msg = r[6]
        m = re.match(r'unknown (?:src|dst) node (.+)$', msg)
        c = cls.get(m.group(1), 'unclassified') if m else 'other'
        groups['A_ambiguous' if c == 'ambiguous' else 'B_app_missing_pseudo' if c in ('app-missing', 'pseudo') else 'X_other'].append(
            '\t'.join([r[1], r[2], r[3], r[4], r[5], msg]))
    elif kind == 'error-text':
        groups['E_structural'].append(r[6])
    elif kind in ('warn-edge', 'warn-edge-auto'):
        meth = r[-1]
        if meth.startswith('GlideOptions') or meth.startswith('GlideRequest'):
            groups['D_glide'].append('\t'.join([kind, r[1], r[2], r[3], r[4], r[5], meth]))
        else:
            groups['C_warn_other'].append('\t'.join([kind, r[1], r[2], r[3], r[4], r[5], meth]))
for g, items in groups.items():
    with open(S + 'items_%s.tsv' % g, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(items) + '\n')
    print(g, len(items))
