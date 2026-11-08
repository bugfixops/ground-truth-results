import ast, glob, os, sys

BASE = '/Users/darshan/Desktop/yang/work/graphs/AnkiDroid'
pat = sys.argv[1]
files = [os.path.join(BASE, 'graph_def.py')] + sorted(glob.glob(os.path.join(BASE, 'parts', '*.py')))
for f in files:
    src = open(f, encoding='utf-8').read()
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'e':
            args = node.args
            vals = []
            for a in args[:3]:
                vals.append(a.value if isinstance(a, ast.Constant) else ast.dump(a)[:40])
            if len(vals) >= 2 and (pat in str(vals[0]) or pat in str(vals[1])):
                print('%s:%d: %s -> %s [%s]' % (os.path.basename(f), node.lineno, vals[0], vals[1], vals[2] if len(vals) > 2 else ''))
        if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name) and node.value.id == 'UNREACHABLE':
            sl = node.slice
            if isinstance(sl, ast.Constant) and pat in str(sl.value):
                print('%s:%d: UNREACHABLE[%s]' % (os.path.basename(f), node.lineno, sl.value))
