"""Print EVERY check-2 problem for LibreTorrent (tools/check_citations.py prints only the first 40).
Run from the repo root after a build: python3 -I graphs/LibreTorrent/scratch/kiro/check2_all.py"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.getcwd(), 'tools'))
import check_citations as cc  # noqa: E402

app = 'LibreTorrent'
g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % app)[0], encoding='utf-8'))
index = [(c, cc.files_in(c)) for c in cc.caches(app)]
texts = [(x['id'], x['evidence'] or '') for x in g['edges']]
texts += [(m, l['unreachable']['text']) for m, l in g['labels'].items() if l.get('unreachable')]
seen, n = set(), 0
for owner, ev in texts:
    for style, rx in (('root', cc.ROOT_STYLE), ('tag', cc.TAG_STYLE)):
        for m in rx.finditer(ev):
            path, spec = m.group(1), re.sub(r'\s+', '', m.group(2))
            if (path, spec) in seen:
                continue
            seen.add((path, spec))
            full = cc.resolve(path, style, index)
            if not full:
                n += 1
                print('%s: file not held: %s:%s' % (owner, path, spec))
                continue
            lines = open(full, encoding='utf-8', errors='replace').read().split('\n')
            if any(not 1 <= a <= b <= len(lines) for a, b in cc.line_ranges(spec)):
                n += 1
                print('%s: %s has %d lines, cited %s' % (owner, path, len(lines), spec))
print('total problems: %d' % n)
