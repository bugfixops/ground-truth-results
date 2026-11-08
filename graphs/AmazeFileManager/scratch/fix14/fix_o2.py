import csv
import os
import shutil

W = '/Users/darshan/Desktop/yang/work/'
BASE = W + 'graphs/AmazeFileManager/'
R = W + 'final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/'
T = BASE + 'scratch/fix14/decisions/O2.tsv'
MAP = {
    'SevenZipHelperTask.java': 'com/amaze/filemanager/asynchronous/asynctasks/compress/SevenZipHelperTask.java',
    'CompressedHelperTask.java': 'com/amaze/filemanager/asynchronous/asynctasks/compress/CompressedHelperTask.java',
    'MainActivity.java': 'com/amaze/filemanager/activities/MainActivity.java',
    'DataUtils.java': 'com/amaze/filemanager/utils/DataUtils.java',
    'Drawer.java': 'com/amaze/filemanager/ui/views/drawer/Drawer.java',
    'MainFragment.java': 'com/amaze/filemanager/fragments/MainFragment.java',
}

shutil.copy(T, BASE + 'scratch/fix14/decisions/O2_before_fix.tsv')
rd = csv.DictReader(open(T, encoding='utf-8'), delimiter='\t')
fields = rd.fieldnames
rows = list(rd)
cache = {}
changed = []
for r in rows:
    if r['source_file'] in MAP:
        r['source_file'] = MAP[r['source_file']]
    if r['action'] != 'RENAME':
        continue
    path = next((x + r['source_file'] for x in [R, R + '../../../'] if os.path.exists(x + r['source_file'])), None)
    if path is None:
        continue
    if path not in cache:
        cache[path] = open(path, encoding='utf-8', errors='replace').read().split('\n')
    L = cache[path]
    cited = [int(x) for x in r['source_line'].split(',')]
    raw = {n: L[n - 1] for n in cited if 1 <= n <= len(L)}
    parts = [p.strip() for p in r['printed_line'].split(' || ')]
    if r['printed_line'].strip() in {v.strip() for v in raw.values()}:
        parts = [r['printed_line'].strip()]
    callee = r['new_name'].split('(')[0].split('.')[-1]
    matched = [p for p in parts if p != '(blank)' and p in {v.strip() for v in raw.values()}]
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
