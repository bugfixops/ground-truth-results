import json
import os
import shutil

os.chdir('/Users/darshan/Desktop/yang/work')
S = 'graphs/AmazeFileManager/scratch/'
G = 'graphs/AmazeFileManager/graph_def.py'

verdict = json.load(open('graphs/AmazeFileManager/out/amazefilemanager_trigger_graph.json', encoding='utf-8'))['verdict']
rows = [l.split('\t') for l in open(S + 'work_items.tsv', encoding='utf-8').read().split('\n')[1:] if l]
pairs = set()
skipped_glide = 0
for r in rows:
    if r[0] != 'warn-edge-auto':
        continue
    src, dst = r[4], r[5]
    if verdict.get(src) != 'UNREACHABLE':
        continue
    if dst.startswith('GlideOptions') or dst.startswith('GlideRequest'):
        skipped_glide += 1
        continue
    pairs.add((src, dst))

shutil.copy(G, S + 'graph_def_before_apply_12.py')
text = open(G, encoding='utf-8').read().rstrip('\n') + '\n\n'
text += '# Auto calls made from methods that are UNREACHABLE: the callers cannot run, so these calls are not routes.\n'
text += 'sup(\n'
for s_, d_ in sorted(pairs):
    text += '    (%r, %r),\n' % (s_, d_)
text += ')\n'
open(G, 'w', encoding='utf-8').write(text)
print('suppressed pairs', len(pairs), 'glide pairs left for review', skipped_glide)
