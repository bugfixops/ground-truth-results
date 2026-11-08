"""List the node names the builder gives to methods (same naming as tools/build_graph.method_names).
usage: python3 -I graphs/Markor/scratch/names.py <regex on node name> [more regexes...]"""
import json, re, sys
sys.path.insert(0, '/Users/darshan/Desktop/yang/work/tools')
import build_graph as bg
rows = json.load(open('/Users/darshan/Desktop/yang/work/graphs/Markor/method_list.json'))
names, by_name = bg.method_names(rows)
pats = [re.compile(p) for p in sys.argv[1:]]
for n in names:
    if not pats or any(p.search(n) for p in pats):
        r = by_name[n]
        print(n, '|', r['desc'], '|', ','.join(r.get('flags', [])))
