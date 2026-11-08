import json, sys

BASE = '/Users/darshan/Desktop/yang/work/graphs/AnkiDroid/'
g = json.load(open(BASE + 'out/ankidroid_trigger_graph.json'))
a = json.load(open(BASE + 'auto_calls.json'))

def v(n):
    return g['verdict'].get(n)

for node in sys.argv[1:]:
    print('=' * 90)
    print(node, '| verdict:', v(node))
    print('  IN:')
    for e in g['edges']:
        if e['dst'] == node:
            print('    %s -> %s kind=%s cls=%s via=%s srcverdict=%s trig=%s' % (
                e['src'], e['dst'], e['kind'], e.get('edge_class'), e.get('via'), v(e['src']), e['trigger'][:110]))
    print('  OUT:')
    for e in g['edges']:
        if e['src'] == node:
            print('    %s -> %s kind=%s cls=%s dstverdict=%s trig=%s' % (
                e['src'], e['dst'], e['kind'], e.get('edge_class'), v(e['dst']), e['trigger'][:110]))
    for c in a['calls']:
        if c['src'] == node:
            print('    AUTO-OUT %s -> %s %s:%s dispatch=%s dstverdict=%s' % (c['src'], c['dst'], c['file'], c['line'], c['dispatch'], v(c['dst'])))
