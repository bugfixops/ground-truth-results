import json, sys
base = '/Users/darshan/Desktop/yang/work/graphs/AnkiDroid/'
tsv = open(base + 'scratch/batches_ai.tsv').read().splitlines()
row = [r for r in tsv[1:] if r.split('\t')[0] == '138'][0].split('\t')
methods = row[3].split(';')
ml = json.load(open(base + 'method_list.json'))
shorts = {m['short']: m for m in ml}
g = json.load(open(base + 'out/ankidroid_trigger_graph.json'))
ver = g['verdict']; lab = g['labels']
auto = json.load(open(base + 'auto_calls.json'))['calls']
print('methods in batch:', len(methods))
for m in methods:
    s = m
    if s not in shorts:
        cands = [k for k in shorts if k.startswith(m.rstrip('();').split('(')[0] + '(')]
        print('NOT IN method_list:', m, 'cands', cands[:5]); continue
    info = shorts[s]
    v = ver.get(s); l = lab.get(s)
    inc = [e for e in g['edges'] if e['dst'] == s]
    ac = [c for c in auto if c['dst'] == s]
    print(f"== {s} | desc={info['desc']} flags={info['flags']} class={info['class']}")
    print(f"   verdict={v} label={l}")
    for e in inc[:8]:
        print(f"   IN {e['kind']} {e['src']} -> {e['dst']} [{e.get('env')}|{e.get('state_kinds')}] id={e['id']} cls={e.get('edge_class')}")
    for c in ac[:8]:
        print(f"   AUTO {c['src']} -> {c['dst']} {c['file']}:{c['line']} disp={c['dispatch']}")
