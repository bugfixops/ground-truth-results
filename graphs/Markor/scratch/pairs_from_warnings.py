# Writes scratch/suppress_pairs.json: the AUTO call pairs behind the warned incoming edges of UNREACHABLE methods.
# Usage: python3 -I scratch/pairs_from_warnings.py <build log>
# Hand-written (non-AUTO) warned edges cannot be removed by SUPPRESS; they are printed and must be zero.
import json, re, sys
G = '/Users/darshan/Desktop/yang/work/graphs/Markor/'
log = open(sys.argv[1]).read()
ids = set()
for m in re.finditer(r'incoming edges \[([^\]]*)\]', log):
    ids |= {x.strip(" '") for x in m.group(1).split(',') if x.strip(" '")}
g = json.load(open(G + 'out/markor_trigger_graph.json'))
E = {e['id']: e for e in g['edges']}
pairs, hand = set(), []
for i in sorted(ids):
    e = E[i]
    if e.get('auto') and e['kind'] == 'CALL':
        pairs.add((e['src'], e['dst']))
    else:
        hand.append((i, e['src'], e['dst'], e['kind']))
print('warned ids', len(ids), 'AUTO pairs', len(pairs), 'hand or non-CALL', len(hand))
# Guard: a log with no warnings (e.g. a build that already has SUPPRESS applied) must not overwrite the stored pairs with [].
# Use the build log from before SUPPRESS was applied (build25b) to regenerate them.
if ids:
    json.dump(sorted([list(p) for p in pairs]), open(G + 'scratch/suppress_pairs.json', 'w'), indent=0)
else:
    print('no warned ids in this log: scratch/suppress_pairs.json left unchanged')
for h in hand:
    print('HAND', h)
