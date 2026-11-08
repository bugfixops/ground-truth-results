import collections
import json

BASE = '/Users/darshan/Desktop/yang/work/graphs/AnkiDroid/out/ankidroid_trigger_graph.json'
d = json.load(open(BASE, encoding='utf-8'))
verdict = d['verdict']
edges = d['edges']
out_by_src = collections.defaultdict(list)
in_by_dst = collections.defaultdict(list)
for ed in edges:
    out_by_src[ed['src']].append(ed)
    in_by_dst[ed['dst']].append(ed)
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

import sys
targets = sys.argv[1:]
for t in targets:
    print('== TARGET', t, 'verdict=', verdict.get(t))
    for ed in in_by_dst.get(t, []):
        print('   IN  %s -> %s kind=%s src_reach=%s src_verdict=%s id=%s env=%s state=%s via=%s evid=%s' % (
            ed['src'], ed['dst'], ed['kind'], ed['src'] in seen, verdict.get(ed['src'], '-'), ed['id'],
            ed.get('env'), ed.get('needs_state'), ed.get('via'), (ed.get('evidence') or '')[:110]))
    for ed in out_by_src.get(t, []):
        if ed['kind'] == 'REGISTER':
            continue
        print('   OUT %s -> %s kind=%s dst_reach=%s' % (ed['src'], ed['dst'], ed['kind'], ed['dst'] in seen))
