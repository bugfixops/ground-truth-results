import ast, json, sys
G = 'graphs/AmazeFileManager/graph_def.py'
S = 'graphs/AmazeFileManager/scratch/'
dry = '--apply' not in sys.argv
raw = open(G, 'rb').read()
text = raw.decode('utf-8')
tree = ast.parse(text)
lines_b = raw.split(b'\n')
def off(lineno, col):
    return sum(len(l) + 1 for l in lines_b[:lineno - 1]) + col
plan = json.load(open(S + 'plan_rename.json'))
edges = {x['id']: x for x in json.load(open(S + 'edges_trace.json'))}
# index e() calls by line
calls = {}
for node in ast.walk(tree):
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'e':
        calls.setdefault(node.lineno, []).append(node)
ops, miss = {}, []
for key, (act, new) in plan.items():
    eid, end, old = key.split('|')
    x = edges[eid]
    ok = False
    for ln in x['_lines']:
        for c in calls.get(ln, []):
            idx = 0 if end == 'src' else 1
            if len(c.args) > idx and isinstance(c.args[idx], ast.Constant) and c.args[idx].value == old:
                a = c.args[idx]
                ops[(a.lineno, a.col_offset, a.end_col_offset)] = repr(new)
                ok = True
                break
        if ok:
            break
    if not ok:
        miss.append((eid, end, old, x['_lines'][:2]))
print('ops', len(ops), 'missed', len(miss))
for m in miss[:20]:
    print('MISS', m)
if not dry:
    # byte offsets: AST col offsets are utf-8 byte offsets
    for (ln, c0, c1), new in sorted(ops.items(), reverse=True):
        s = sum(len(l) + 1 for l in lines_b[:ln - 1])
        b0, b1 = s + c0, s + c1
        raw = raw[:b0] + new.encode('utf-8') + raw[b1:]
        lines_b = raw.split(b'\n')
    open(G, 'wb').write(raw)
    print('applied')
