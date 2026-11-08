import csv
import os
import shutil
import sys

W = '/Users/darshan/Desktop/yang/work/'
BASE = W + 'graphs/AmazeFileManager/'
APP = W + 'final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/'
R = APP + 'app/src/main/java/com/amaze/filemanager/'
T = sys.argv[1]

shutil.copy(T, T + '.before_fix')
rd = csv.DictReader(open(T, encoding='utf-8'), delimiter='\t')
fields = rd.fieldnames
rows = list(rd)
cache = {}
changed = []
for r in rows:
    if r['source_file'].startswith(APP):
        r['source_file'] = r['source_file'][len(APP):]
    if r['action'] != 'RENAME':
        continue
    path = next((x + r['source_file'] for x in [R, R + '../../../', APP] if os.path.exists(x + r['source_file'])), None)
    if path is None:
        continue
    if path not in cache:
        cache[path] = open(path, encoding='utf-8', errors='replace').read().split('\n')
    L = cache[path]
    cited = [int(x) for x in r['source_line'].split(',')]
    raw = {n: L[n - 1] for n in cited if 1 <= n <= len(L)}
    texts = {v.strip() for v in raw.values()}
    parts = [p.strip() for p in r['printed_line'].split(' || ')]
    if r['printed_line'].strip() in texts:
        parts = [r['printed_line'].strip()]
    callee = r['new_name'].split('(')[0].split('.')
    callee = callee[-2] if callee[-1] == '<init>' else callee[-1]
    matched = [p for p in parts if p != '(blank)' and p in texts]
    if r['side'] == 'dst':
        matched = [p for p in matched if callee in p] or matched
    if not matched:
        continue
    want = matched[0]
    newline = next(v for n, v in sorted(raw.items()) if v.strip() == want)
    if newline != r['printed_line']:
        changed.append((r['item'], r['side'], r['printed_line'][:50], newline.strip()[:50]))
        r['printed_line'] = newline

w = csv.DictWriter(open(T, 'w', encoding='utf-8', newline=''), fieldnames=fields, delimiter='\t', lineterminator='\n')
w.writeheader()
w.writerows(rows)
print('rows', len(rows), 'printed_line normalised', len(changed))
for c in changed:
    print(' ', c)
