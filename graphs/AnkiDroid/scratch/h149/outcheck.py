import csv
import sys

ROOT = '/Users/darshan/Desktop/yang/work/graphs/AnkiDroid'
row = None
with open(ROOT + '/scratch/batches_ai.tsv', encoding='utf-8') as fh:
    for line in fh:
        f = line.rstrip('\n').split('\t')
        if f and f[0] == '149':
            row = f
            break
methods = row[3].split(';')
want = set(methods)
found = set()
csv.field_size_limit(10 ** 9)
with open(ROOT + '/out/methods.csv', encoding='utf-8', newline='') as fh:
    rd = csv.DictReader(fh)
    for r in rd:
        m = r['method']
        if m in want:
            found.add(m)
            print('%s | verdict=%s | inc=%s | path=%s | kind=%s | conf=%s | src=%s | short=%s' % (
                m, r['verdict'], r['incoming_edges'], r['path_status'], r['unreachable_kind'],
                r['confirmed_by'], r['source_ref'][:80], r['shortest_path'][:160]))
print('not found in methods.csv:', [m for m in methods if m not in found])
