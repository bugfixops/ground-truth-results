import json, sys, collections
sys.path.insert(0, 'tools')
import build_graph as bg
G = 'graphs/AmazeFileManager'
S = G + '/scratch/'
rows = json.load(open(G + '/method_list.json'))
names, by_name = bg.method_names(rows)
known = set(names)
auto = json.load(open(G + '/auto_calls.json'))
calls = set((c['src'], c['dst']) for c in auto['calls'])
lam = set((l['src'], l['dst']) for l in auto['lambdas'])
t = json.load(open(S + 'unknown_table.json'))
edges = {x['id']: x for x in json.load(open(S + 'edges_trace.json'))}
plan = {}   # occurrence key -> (kind, newname)
left = []
for k, end, eid, kind, n, lines, auto_flag, cands in t:
    x = edges[eid]
    other = x['dst'] if end == 'src' else x['src']
    if k == 'ONE':
        plan[(eid, end, n)] = ('rename', cands[0]); continue
    if k == 'MANY':
        if end == 'dst':
            hit = [c for c in cands if (bg.base(x['src']), c) in calls or (x['src'], c) in calls or (x['src'], c) in lam or (bg.base(x['src']), c) in lam]
        else:
            hit = [c for c in cands if (c, bg.base(x['dst'])) in calls or (c, x['dst']) in calls]
        if len(hit) == 1:
            plan[(eid, end, n)] = ('rename', hit[0])
        else:
            left.append((eid, end, kind, n, x['src'][:60], x['dst'][:60], len(hit), cands[:4], lines))
print('rename plan', len(plan), 'left', len(left))
json.dump({'|'.join(k): v for k, v in plan.items()}, open(S + 'plan_rename.json', 'w'), indent=0)
json.dump(left, open(S + 'plan_left_many.json', 'w'), indent=0)
c = collections.Counter(v[1] for v in plan.values())
print('renames distinct targets', len(c))
for eid, end, kind, n, s, d, h, cands, lines in left[:200]:
    print(eid, end, kind, n, '| src=', s, '| dst=', d, '| hit', h, '| cands', cands, 'line', lines)
