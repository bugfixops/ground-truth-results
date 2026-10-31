import json, sys, re

BASE = '/Users/darshan/Desktop/yang/work/graphs/AnkiDroid/'
g = json.load(open(BASE + 'out/ankidroid_trigger_graph.json'))
a = json.load(open(BASE + 'auto_calls.json'))
ml = json.load(open(BASE + 'method_list.json'))
batch = [l.strip() for l in open(BASE + 'scratch/label_139/batch.txt') if l.strip()]

def strip(s):
    return s.split('(')[0]

mlmap = {}
for r in ml:
    mlmap.setdefault(r['short'], []).append(r)

def verdict(m):
    return g['verdict'].get(m)

def callers(m):
    base = strip(m)
    out = []
    for c in a['calls']:
        d = c['dst']
        if d == base or d == m or (d.split('(')[0] == base and '(' in m and False):
            out.append(c)
    return out

only = sys.argv[1:] if len(sys.argv) > 1 else batch
for m in only:
    base = strip(m)
    print('=' * 100)
    print(m, '| verdict:', verdict(m), '| label:', (g['labels'].get(m) or {}).get('route_edge_classes'))
    for r in mlmap.get(base, []):
        if r['short'] == base:
            print('  ML:', r['class'], r['name'], r['desc'], r['flags'])
    for c in callers(m):
        print('  CALLER(auto): %s -> %s  %s:%s dispatch=%s via=%s | caller verdict=%s' % (
            c['src'], c['dst'], c['file'], c['line'], c['dispatch'], c['via'], verdict(c['src'])))
    # receiver variants and impl
    for rv in a['receiver_variants']:
        if rv.split('@')[0] == base or rv.split('@')[0].split('.')[-1] == base.split('.')[-1] and rv.split('.')[0] == base.split('.')[0]:
            pass
    for e in g['edges']:
        if e['dst'] == m or e['dst'] == base:
            print('  EDGE-IN: %s -> %s kind=%s cls=%s verdict(src)=%s trig=%s' % (e['src'], e['dst'], e['kind'], e.get('edge_class'), verdict(e['src']), e['trigger'][:90]))
    # framework calls out of m
    fc = a['framework_calls'].get(base)
    if fc:
        print('  FWCALLS from base:', fc)
    print('  LABEL:', json.dumps(g['labels'].get(m))[:400])
