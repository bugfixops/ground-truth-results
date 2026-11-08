import json, sys
# usage: python3 -I q.py METHOD [METHOD ...]  -> verdict, label, incoming edges (src, kind, verdict of src)
g = json.load(open('/Users/darshan/Desktop/yang/work/graphs/AnkiDroid/out/ankidroid_trigger_graph.json'))
V = g['verdict']
inc = {}
out = {}
for x in g['edges']:
    inc.setdefault(x['dst'], []).append(x)
    out.setdefault(x['src'], []).append(x)
mode = 'in'
args = sys.argv[1:]
if args and args[0] in ('--out', '--in'):
    mode = args[0][2:]
    args = args[1:]
for m in args:
    print('==', m, V.get(m))
    rows = (inc if mode == 'in' else out).get(m, [])
    for x in rows[:12]:
        other = x['src'] if mode == 'in' else x['dst']
        print('   %s %s %s %s | %s' % ('<-' if mode == 'in' else '->', other, x['kind'], V.get(other), (x.get('evidence') or '')[:110]))
    print('   total', len(rows))
