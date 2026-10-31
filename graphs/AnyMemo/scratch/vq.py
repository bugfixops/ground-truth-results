import json,sys
G=json.load(open('graphs/AnyMemo/out/anymemo_trigger_graph.json'))
V=G['verdict']
code={'REACHABLE':'R','UNREACHABLE':'D','UNRESOLVED':'U'}
for k in sys.argv[1:]:
    if k in V: print(code[V[k]], k)
    else:
        m=[x for x in V if x.startswith(k+'(')]
        print('?', k, ('overloads: '+', '.join(m)) if m else 'NOKEY')
