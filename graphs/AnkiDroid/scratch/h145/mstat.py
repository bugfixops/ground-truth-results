import csv, sys

BASE = '/Users/darshan/Desktop/yang/work/graphs/AnkiDroid'
want = sys.argv[1:]
rows = {}
with open(BASE + '/out/methods.csv', encoding='utf-8', newline='') as fh:
    for r in csv.DictReader(fh):
        rows[r['method']] = r
for m in want:
    r = rows.get(m)
    if r is None:
        # substring search for close names
        close = [k for k in rows if m.split('.')[-1] in k and m.split('.')[0] in k][:6]
        print('NOT FOUND:', m, 'close:', close)
        continue
    print('%s | %s | incoming=%s | path=%s | src=%s' % (m, r['verdict'], r['incoming_edges'],
          (r['shortest_path'] or '')[:160], r['source_ref'][:120]))
