import collections
import json
import sys

BASE = '/Users/darshan/Desktop/yang/work/graphs/AnkiDroid/out/ankidroid_trigger_graph.json'
d = json.load(open(BASE, encoding='utf-8'))
verdict = d['verdict']
edges = d['edges']
methods = [m.strip() for m in open('/Users/darshan/Desktop/yang/work/graphs/AnkiDroid/scratch/h148/methods.txt') if m.strip()]

out_by_src = collections.defaultdict(list)
in_by_dst = collections.defaultdict(list)
for ed in edges:
    out_by_src[ed['src']].append(ed)
    in_by_dst[ed['dst']].append(ed)

# BFS from S_ENTRY, skipping REGISTER (the builder does not follow REGISTER for reachability)
seen = {'S_ENTRY'}
q = collections.deque(['S_ENTRY'])
while q:
    n = q.popleft()
    for ed in out_by_src.get(n, []):
        if ed['kind'] == 'REGISTER':
            continue
        if ed['dst'] not in seen:
            seen.add(ed['dst'])
            q.append(ed['dst'])

print('edges total', len(edges), 'seen nodes', len(seen))
mismatch = 0
for m in methods:
    v = verdict.get(m, 'MISSING')
    r = m in seen
    flag = '' if ((v == 'REACHABLE') == r) else '  <-- BFS differs'
    if flag:
        mismatch += 1
    print('%-70s verdict=%-12s bfs_reach=%s%s' % (m, v, r, flag))
print('mismatches', mismatch)
