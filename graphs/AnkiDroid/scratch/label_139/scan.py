import ast, glob, sys, os
BASE = '/Users/darshan/Desktop/yang/work/graphs/AnkiDroid/'
pats = sys.argv[1:]
files = [BASE + 'graph_def.py'] + sorted(glob.glob(BASE + 'parts/*.py'))
for f in files:
    try:
        tree = ast.parse(open(f).read(), f)
    except Exception as ex:
        print('PARSE-FAIL', f, ex); continue
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
            continue
        name = node.func.id
        args = [a.value if isinstance(a, ast.Constant) else ast.dump(a)[:60] for a in node.args]
        kw = {k.arg: (k.value.value if isinstance(k.value, ast.Constant) else '?') for k in node.keywords}
        if name == 'e' and len(args) >= 3:
            src, dst, kind = args[0], args[1], args[2]
        elif name == 'gui' and len(args) >= 2:
            src, dst, kind = args[0], args[1], 'GUI'
        else:
            continue
        s = '%s -> %s %s' % (src, dst, kind)
        if any(p in s for p in pats):
            print('%s:%d  %s  line=%s' % (os.path.basename(f), node.lineno, s, kw.get('evidence', '')[:0]))
