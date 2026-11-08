import json
import sys

sys.path.insert(0, 'tools')
import build_graph as bg

rows = json.load(open('graphs/MMEX/method_list.json'))
names, by_name = bg.method_names(rows)
owned = [l.strip() for l in open('graphs/MMEX/scratch/batches/batch_036.txt')
         if l.strip() and not l.startswith('#')]

# map batch short names to node names: the batch file uses name(params) for overloads
short_to_node = {}
for n, r in zip(names, rows):
    short_to_node.setdefault(r['short'], []).append(n)

ac = json.load(open('graphs/MMEX/auto_calls.json'))


def node_for(batch_name):
    # batch lines look like Class.method or Class.method(T1,T2) ; the node name is the same form
    if batch_name in set(names):
        return batch_name
    cls_m = batch_name.split('(')[0]
    cands = [n for n in names if n.split('(')[0] == cls_m or n.endswith('.' + cls_m)]
    return cands


for b in owned:
    cand = node_for(b)
    if isinstance(cand, str):
        cand = [cand]
    print('== ', b, '->', cand)
    for c in cand:
        r = by_name.get(c)
        if r:
            print('   method_list:', r['class'], r['short'], r['desc'], r.get('flags'))
        print('   callers (auto CALL dst):')
        for x in ac['calls']:
            if x['dst'] == c:
                print('      %s  %s:%s %s via=%s' % (x['src'], x['file'], x['line'], x['dispatch'], x['via']))
        print('   callees (auto CALL src):')
        for x in ac['calls']:
            if x['src'] == c:
                print('      -> %s  %s:%s %s via=%s' % (x['dst'], x['file'], x['line'], x['dispatch'], x['via']))
        for l in ac['lambdas']:
            if l['src'] == c or l['dst'] == c:
                print('   lambda:', l)
        for f in ac.get('framework_calls', []):
            if (isinstance(f, dict) and (f.get('src') == c or f.get('dst') == c)):
                print('   framework_call:', f)
        rv = ac.get('receiver_variants', [])
        if c in rv:
            print('   receiver_variant: yes')
