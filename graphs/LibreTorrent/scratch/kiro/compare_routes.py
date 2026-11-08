"""Compare the new LibreTorrent sample with the routes judged in the first-draw table.
Run from the repo root:
  python3 -I graphs/LibreTorrent/scratch/kiro/compare_routes.py <old_methods.csv> <old_route_table.md>
For each method of the new graphs/LibreTorrent/scratch/sample_30.txt it prints one line:
  NEW            the method was not in the old table: judge every step
  SAME ROUTE     same nodes, same ENV and STATE as the judged route: the old verdict may be carried over
  CHANGED ROUTE  the route differs from the judged one: judge every step again"""
import csv
import re
import sys

old = {r['method']: r for r in csv.DictReader(open(sys.argv[1], encoding='utf-8'))}
new = {r['method']: r for r in csv.DictReader(open('graphs/LibreTorrent/out/methods.csv', encoding='utf-8'))}
judged = {}
for line in open(sys.argv[2], encoding='utf-8'):
    m = re.match(r'^\|\s*\d+\s*\|\s*([^|]+?)\s*\|[^|]*\|\s*\d+\s*\|\s*(CORRECT|WRONG|UNCLEAR|BLOCKED)\s*\|', line)
    if m:
        judged[m.group(1)] = m.group(2)
lines = open('graphs/LibreTorrent/scratch/sample_30.txt', encoding='utf-8').read().splitlines()[1:]
sample = [l.split()[-1] for l in lines if l.strip()]
KEYS = ('shortest_path', 'env_kinds', 'state_kinds')
for i, meth in enumerate(sample, 1):
    if meth not in judged:
        status = 'NEW            judge every step'
    elif meth in old and all(old[meth][k] == new[meth][k] for k in KEYS):
        status = 'SAME ROUTE     old verdict %s may be carried over' % judged[meth]
    else:
        status = 'CHANGED ROUTE  judge every step again (old verdict %s)' % judged[meth]
    print('%2d  %-62s %s' % (i, meth, status))
