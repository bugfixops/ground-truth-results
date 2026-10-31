import json, sys
# Prints the verdict of each key given on the command line: R = REACHABLE, D = UNREACHABLE, X = UNRESOLVED, ABSENT = no such key.
# Usage (from work/): python3 -I graphs/AnyMemo/scratch/vcheck.py 'Key1' 'Key2' ...
G = json.load(open('graphs/AnyMemo/out/anymemo_trigger_graph.json'))
V = G['verdict']
short = {'REACHABLE': 'R', 'UNREACHABLE': 'D', 'UNRESOLVED': 'X'}
for k in sys.argv[1:]:
    print('%-9s %s' % (short.get(V.get(k), 'ABSENT') if k in V else 'ABSENT', k))
