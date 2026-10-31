import csv, sys

BASE = '/Users/darshan/Desktop/yang/work/graphs/AnkiDroid'
rows = [l.strip() for l in open(BASE + '/scratch/h145/rows.txt', encoding='utf-8') if l.strip()]
want = set(rows)
found = {}
with open(BASE + '/out/methods.csv', encoding='utf-8', newline='') as fh:
    for r in csv.DictReader(fh):
        if r['method'] in want:
            found[r['method']] = r
for m in rows:
    r = found.get(m)
    if r is None:
        print('MISSING_IN_METHODS_CSV', m)
        continue
    print('%s | verdict=%s | kind=%s | incoming=%s | path=%s | route_classes=%s | explicit=%s | conf=%s | src=%s' % (
        m, r['verdict'], r['unreachable_kind'] or '-', r['incoming_edges'], (r['shortest_path'] or '')[:150],
        r['route_edge_classes'], r['explicit_standard_route'], r['confirmed_by'], r['source_ref']))
print('total rows printed', len(rows), 'found', len(found))
