import json
import re
from collections import Counter, defaultdict

BASE = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/'
d = json.load(open(BASE + 'out/amazefilemanager_trigger_graph.json', encoding='utf-8'))
verdict = d['verdict']
edges = d['edges']
print('edge keys', sorted(edges[0].keys()))
by_id = {}
for e in edges:
    if 'id' in e:
        by_id[e['id']] = e

warned = {}
for line in open(BASE + 'scratch/build_finish_16.txt', encoding='utf-8'):
    m = re.search(r'WARN (.+?) is UNREACHABLE but has incoming edges \[(.*)\]', line)
    if m:
        warned[m.group(1)] = re.findall(r"'([^']+)'", m.group(2))

cls = Counter()
rows = defaultdict(list)
for meth, ids in warned.items():
    srcs = []
    for i in ids:
        e = by_id.get(i)
        if e is None:
            srcs.append((i, '?', '?'))
            continue
        s = e['src']
        srcs.append((i, s, verdict.get(s, 'PSEUDO' if s.startswith('S_') else 'NOT_IN_METHODS')))
    v = {x[2] for x in srcs}
    if 'REACHABLE' in v:
        k = 'LIVE_SOURCE'
    elif v <= {'UNREACHABLE'}:
        k = 'DEAD_SOURCE_ONLY'
    else:
        k = 'OTHER:' + ','.join(sorted(v))
    cls[k] += 1
    rows[k].append((meth, srcs))

print('warned', len(warned), dict(cls))
for k in sorted(rows):
    print('==', k, len(rows[k]))
    for meth, srcs in rows[k][:60]:
        print('  ', meth, '<-', [(s, v) for _, s, v in srcs][:4])
