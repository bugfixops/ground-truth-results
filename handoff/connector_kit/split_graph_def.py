"""Split a large graph_def.py into modules below the GitHub connector's ~1 MB limit.

Usage (from the repo root): python3 -I handoff/connector_kit/split_graph_def.py graphs/<App> [max_bytes]

The cut points are top-level statement boundaries (found with ast), so no statement is split.
The first chunk stays in graph_def.py (it holds TITLE, STRICT, USE_AUTO and the other settings);
the rest go to graphs/<App>/graph_def_mod/NN.py. A loader appended to graph_def.py runs the
modules in name order, in the same namespace, exactly as if they were still one file.
If graph_def_mod/ already exists, its modules are joined back first, so the script can be re-run
whenever a module grows past max_bytes. Check after every split: the build output
(out/methods.csv, out/<prefix>_trigger_graph.json) must be byte-identical to the build before the split.
"""
import ast
import os
import sys

LOADER_MARK = '# ---- graph_def_mod loader (handoff/connector_kit/split_graph_def.py)'
LOADER = LOADER_MARK + '''
# The rest of this graph is in graph_def_mod/NN.py (each file below 1 MB, so the GitHub connector can read and write it).
# The modules run in name order, in this same namespace, exactly as if they were one file. GDIR is set by tools/build_graph.py.
import os as _gdmod_os
for _gdmod_name in sorted(_gdmod_os.listdir(_gdmod_os.path.join(GDIR, 'graph_def_mod'))):
    if _gdmod_name.endswith('.py'):
        _gdmod_path = _gdmod_os.path.join(GDIR, 'graph_def_mod', _gdmod_name)
        exec(compile(open(_gdmod_path, encoding='utf-8').read(), _gdmod_path, 'exec'))
del _gdmod_os, _gdmod_name, _gdmod_path
'''


def joined_source(gdir):
    main = open(os.path.join(gdir, 'graph_def.py'), encoding='utf-8').read()
    if LOADER_MARK not in main:
        return main
    head = main.split(LOADER_MARK)[0]
    mdir = os.path.join(gdir, 'graph_def_mod')
    parts = [open(os.path.join(mdir, n), encoding='utf-8').read() for n in sorted(os.listdir(mdir)) if n.endswith('.py')]
    return head + ''.join(parts)


def main(argv):
    gdir = argv[1]
    limit = int(argv[2]) if len(argv) > 2 else 600000
    src = joined_source(gdir)
    lines = src.splitlines(keepends=True)
    tree = ast.parse(src)
    starts = [n.lineno for n in tree.body]
    # include comments/blank lines that precede a statement in that statement's chunk
    bounds = []
    for i, st in enumerate(tree.body):
        begin = 1 if i == 0 else tree.body[i - 1].end_lineno + 1
        bounds.append((begin, st.end_lineno))
    tail_begin = tree.body[-1].end_lineno + 1 if tree.body else 1
    chunks, cur, size = [], [], 0
    for begin, end in bounds:
        text = ''.join(lines[begin - 1:end])
        if cur and size + len(text.encode('utf-8')) > limit:
            chunks.append(''.join(cur))
            cur, size = [], 0
        cur.append(text)
        size += len(text.encode('utf-8'))
    cur.append(''.join(lines[tail_begin - 1:]))
    chunks.append(''.join(cur))
    for c in chunks:
        if len(c.encode('utf-8')) > 900000:
            raise SystemExit('a single top-level statement is larger than 900 KB; split it by hand')
    mdir = os.path.join(gdir, 'graph_def_mod')
    if len(chunks) == 1:
        open(os.path.join(gdir, 'graph_def.py'), 'w', encoding='utf-8').write(chunks[0])
        if os.path.isdir(mdir):
            for n in os.listdir(mdir):
                os.remove(os.path.join(mdir, n))
            os.rmdir(mdir)
        print('%s: one chunk (%d bytes), no modules needed' % (gdir, len(chunks[0].encode('utf-8'))))
        return 0
    os.makedirs(mdir, exist_ok=True)
    for n in os.listdir(mdir):
        os.remove(os.path.join(mdir, n))
    head = chunks[0]
    if not head.endswith('\n'):
        head += '\n'
    open(os.path.join(gdir, 'graph_def.py'), 'w', encoding='utf-8').write(head + '\n' + LOADER)
    for i, c in enumerate(chunks[1:], 1):
        open(os.path.join(mdir, '%02d.py' % i), 'w', encoding='utf-8').write(c)
    print('%s: graph_def.py %d bytes + %d modules: %s' % (
        gdir, os.path.getsize(os.path.join(gdir, 'graph_def.py')), len(chunks) - 1,
        ', '.join('%02d.py %d' % (i, len(c.encode('utf-8'))) for i, c in enumerate(chunks[1:], 1))))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
