import csv
import glob
import json
import os
import sys
from collections import Counter

W = '/Users/darshan/Desktop/yang/work/'
BASE = W + 'graphs/AmazeFileManager/'
R = W + 'final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/'

methods = {r['method'] for r in csv.DictReader(open(BASE + 'out/methods.csv', encoding='utf-8'))}
items = {it['item']: it for it in json.load(open(BASE + 'scratch/fix14/unknown_items.json', encoding='utf-8'))}
print('item keys', sorted(next(iter(items.values())).keys()))
files = sys.argv[1:] or sorted(glob.glob(BASE + 'scratch/fix14/decisions/O*.tsv'))
fails = []
counts = Counter()
seen = set()
cache = {}
for f in files:
    for r in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t'):
        key = (r['item'], r['side'])
        counts[(os.path.basename(f), r['action'])] += 1
        if key in seen:
            fails.append((f, key, 'duplicate row'))
        seen.add(key)
        if r['item'] not in items:
            fails.append((f, key, 'unknown item'))
            continue
        if r['action'] == 'RENAME':
            nm = r['new_name']
            head = nm.split('(')[0].split('.')
            callee = (head[-2] if head[-1] == '<init>' else head[-1]).split('$')[-1]
            if nm not in methods:
                fails.append((f, key, 'new_name not a method: ' + nm))
            cands = items[r['item']].get('candidates') or []
            if cands and nm not in cands:
                fails.append((f, key, 'new_name not in candidates: ' + nm))
            if r['side'] == 'dst' and callee not in r['printed_line'] and not (head[-1] == '<init>' and 'super(' in r['printed_line']):
                fails.append((f, key, 'callee not in printed_line'))
            roots = [R, R + '../../../', W + 'final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/']
            path = next((x + r['source_file'] for x in roots if os.path.exists(x + r['source_file'])), R + r['source_file'])
            if path not in cache:
                cache[path] = open(path, encoding='utf-8', errors='replace').read().split('\n') if os.path.exists(path) else None
            L = cache[path]
            if L is None:
                fails.append((f, key, 'source file missing: ' + r['source_file']))
            else:
                cited = [int(x) for x in r['source_line'].split(',')]
                texts = {L[n - 1].strip() for n in cited if 1 <= n <= len(L)}
                printed = r['printed_line'].strip()
                ok_part = lambda p: ('' if p == '(blank)' else p) in texts
                if len(texts) == 0 or not (ok_part(printed) or all(ok_part(p.strip()) for p in printed.split(' || '))):
                    fails.append((f, key, 'printed_line not a cited source line %s' % r['source_line']))
        elif r['action'] == 'DELETE':
            if not r['reason'].strip():
                fails.append((f, key, 'DELETE without reason'))
print('counts', dict(counts))
print('fails', len(fails))
for x in fails:
    print(' ', os.path.basename(x[0]), x[1], x[2])
