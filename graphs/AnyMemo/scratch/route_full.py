"""Full route printer for verification (scratch). Every step, no dedupe.
Usage (from work/): python3 -I graphs/AnyMemo/scratch/route_full.py <method> [<method> ...]
Per step: id, kind/class, src -> dst, trigger, guard, env, needs_state, evidence; for a bytecode-cited call the enclosing
source conditions (cases.guard_of) on the next line.
"""
import csv, glob, json, re, sys
sys.path.insert(0, 'tools')
sys.path.insert(0, 'graphs/AnyMemo/scratch')
sys.path.insert(0, 'tools')
import cases
import show_route

APP = 'AnyMemo'
g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % APP)[0]))
E = {x['id']: x for x in g['edges']}
rows = {r['method']: r for r in csv.DictReader(open('graphs/%s/out/methods.csv' % APP, encoding='utf-8'))}
CS = cases.Cases(APP)


def gof(fname, line):
    try:
        return CS.guard_of(fname, line)
    except Exception as e:  # noqa
        return ['(guard_of failed: %s)' % e]


for m in sys.argv[1:]:
    r = rows.get(m)
    if not r:
        print('MISSING', m)
        continue
    ids = r['route_edge_ids'].split()
    print('## %s %s steps=%d env=%s state=%s path=%s' % (m, r['verdict'], len(ids), r['env_kinds'] or '-', r['state_kinds'] or '-', r['confirmed_by']))
    for i, eid in enumerate(ids, 1):
        x = E[eid]
        print('%2d %s %s/%s %s -> %s' % (i, eid, x['kind'], x['edge_class'] + ('(' + x['via'] + ')' if x.get('via') else ''), x['src'], x['dst']))
        print('     trig: %s' % x['trigger'])
        if x.get('guard'):
            print('     guard: %s' % x['guard'])
        if x.get('env'):
            print('     env: %s' % x['env'])
        if x.get('needs_state'):
            print('     state: %s' % x['needs_state'])
        ev = x.get('evidence') or ''
        print('     ev: %s' % ev[:300])
        mm = re.search(r'SRC ([\w./$-]+\.java):(\d+)', ev)
        if mm and 'bytecode' in ev:
            print('     in: %s' % ' || '.join(gof(mm.group(1), int(mm.group(2)))))
