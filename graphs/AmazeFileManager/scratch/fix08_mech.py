import ast, json, sys, re
G = 'graphs/AmazeFileManager/graph_def.py'
apply = '--apply' in sys.argv
raw = open(G, 'rb').read()
tree = ast.parse(raw.decode('utf-8'))
lines_b = raw.split(b'\n')

def short(key):
    k = key.replace('/', '.')
    segs = k.split('.')
    while len(segs) > 1 and segs[0][:1].islower():
        segs = segs[1:]
    return '.'.join(segs)

# collect UNREACHABLE statements and dict entries: (key, line, kind, node)
entries = []
for st in tree.body:
    if isinstance(st, ast.Assign) and len(st.targets) == 1 and isinstance(st.targets[0], ast.Subscript):
        t = st.targets[0]
        if isinstance(t.value, ast.Name) and t.value.id == 'UNREACHABLE' and isinstance(t.slice, ast.Constant):
            entries.append((t.slice.value, st.lineno, 'stmt', st))
    if isinstance(st, ast.Assign) and len(st.targets) == 1 and isinstance(st.targets[0], ast.Name) and st.targets[0].id.startswith('UNREACHABLE') and isinstance(st.value, ast.Dict):
        for k, v in zip(st.value.keys, st.value.values):
            if isinstance(k, ast.Constant):
                entries.append((k.value, k.lineno, 'dict', (k, v)))

const_ops = []   # (line, old, new) : replace the string constant on that line
del_ops = []     # (line, key): delete statement or dict entry
rep_ops = []     # (line, key, text): replace statement lines

def find(line, key):
    return [e for e in entries if e[1] == line and e[0] == key]

# 1. wrong keys -> renames or deletions
DEL = [
    (5990, 'AppConfig.toast'), (6182, 'Archive.lengthOf'), (10871, 'DatapointParcelable.<init>(Landroid/os/Parcel;)V'),
    (12985, 'ScrimInsetsRelativeLayout.draw(Canvas)'), (12991, 'ScrimInsetsRelativeLayout.fitSystemWindows(Rect)'),
    (13003, 'ScrimInsetsRelativeLayout.onAttachedToWindow()'), (13009, 'ScrimInsetsRelativeLayout.onDetachedFromWindow()'),
    (13015, 'ScrimInsetsRelativeLayout.setOnInsetsCallback(OnInsetsCallback)'),
    (15985, 'ScrimInsetsRelativeLayout.draw(Canvas)'), (15986, 'ScrimInsetsRelativeLayout.fitSystemWindows(Rect)'),
    (15987, 'ScrimInsetsRelativeLayout.init(Context,AttributeSet,int)'), (15988, 'ScrimInsetsRelativeLayout.onAttachedToWindow()'),
    (15989, 'ScrimInsetsRelativeLayout.onDetachedFromWindow()'), (15990, 'ScrimInsetsRelativeLayout.setOnInsetsCallback(OnInsetsCallback)'),
    (15257, 'DummyFileGenerator.createFile(File,int)'), (15264, 'DonationViewHolder.<init>(View)'),
    (8639, 'MainActivityHelper.isNewDirectoryRecursive'), (1961, 'com/amaze/filemanager/database/CloudContract.<init>'),
]
REN = [
    (12997, 'ScrimInsetsRelativeLayout.init(Context,AttributeSet,int)', 'ScrimInsetsRelativeLayout.init'),
    (7728, 'FileUtils.scanFile', 'FileUtils.scanFile(Uri,Context)'),
    (7729, 'FileUtils.fileToContentUri', 'FileUtils.fileToContentUri(Context,String,boolean,String)'),
    (8569, 'ComputerParcelable.<init>', 'ComputerParcelable.<init>(Parcel)'),
]
for ln, k in DEL:
    es = find(ln, k)
    if len(es) != 1:
        print('NOT FOUND del', ln, k, len(es)); continue
    del_ops.append((ln, k))
for ln, old, new in REN:
    es = find(ln, old)
    if len(es) != 1:
        print('NOT FOUND ren', ln, old, len(es)); continue
    const_ops.append((ln, old, new))
dellines = {ln for ln, _ in del_ops}
for e in entries:
    if '.' in e[0] and ('com.amaze' in e[0] or 'com/amaze' in e[0]) and e[1] not in dellines:
        const_ops.append((e[1], e[0], short(e[0])))
for ln, k, _ in [(0,0,0)]:
    pass
for name, val_node in []:
    pass
# 2. confirmed_by
for st in tree.body:
    tgt = None
    if isinstance(st, ast.Assign) and len(st.targets) == 1 and isinstance(st.targets[0], ast.Subscript):
        if isinstance(st.value, ast.Tuple):
            tgt = st.value
    if isinstance(st, ast.Assign) and len(st.targets) == 1 and isinstance(st.targets[0], ast.Name) and st.targets[0].id.startswith('UNREACHABLE') and isinstance(st.value, ast.Dict):
        for v in st.value.values:
            if isinstance(v, ast.Tuple) and len(v.elts) == 4 and isinstance(v.elts[3], ast.Constant) and v.elts[3].value == 'CALL':
                if all(d[0] != v.lineno for d in del_ops):
                    const_ops.append((v.elts[3].lineno, 'CALL', 'INFERRED'))
    if tgt is not None and len(tgt.elts) == 4 and isinstance(tgt.elts[3], ast.Constant) and tgt.elts[3].value == 'CALL':
        if all(d[0] != tgt.lineno for d in del_ops):
            const_ops.append((tgt.elts[3].lineno, 'CALL', 'INFERRED'))
# 3. EXPLICIT -> CALL on e() lines
for node in ast.walk(tree):
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'e' and len(node.args) > 2:
        a = node.args[2]
        if isinstance(a, ast.Constant) and a.value == 'EXPLICIT':
            const_ops.append((a.lineno, 'EXPLICIT', 'CALL'))
print('const ops', len(const_ops), 'del ops', len(del_ops), 'renames', len(REN) + sum(1 for e in entries if 'com' in e[0] and '.' in e[0]))
for op in const_ops: print('CONST', op)
for op in del_ops: print('DEL', op)
if apply:
    # byte-level constant edits, from the end
    cons = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            cons.append(node)
    edits = []
    for ln, old, new in const_ops:
        hit = [c for c in cons if c.lineno == ln and c.value == old]
        if len(hit) != 1:
            print('NO CONST MATCH', ln, old, len(hit)); sys.exit(1)
        c = hit[0]
        edits.append((c.lineno, c.col_offset, c.end_col_offset, repr(new)))
    for ln, c0, c1, new in sorted(edits, reverse=True):
        s = sum(len(l) + 1 for l in lines_b[:ln - 1])
        raw = raw[:s + c0] + new.encode('utf-8') + raw[s + c1:]
        lines_b = raw.split(b'\n')
    # line deletions, from the end; recompute entries after constant edits
    tree2 = ast.parse(raw.decode('utf-8'))
    lines = raw.decode('utf-8').split('\n')
    dels = []
    for st in tree2.body:
        if isinstance(st, ast.Assign) and len(st.targets) == 1 and isinstance(st.targets[0], ast.Subscript):
            t = st.targets[0]
            if isinstance(t.value, ast.Name) and t.value.id == 'UNREACHABLE' and isinstance(t.slice, ast.Constant):
                for ln, k in del_ops:
                    if st.lineno == ln and t.slice.value == k:
                        dels.append((st.lineno, st.end_lineno))
        if isinstance(st, ast.Assign) and len(st.targets) == 1 and isinstance(st.targets[0], ast.Name) and st.targets[0].id.startswith('UNREACHABLE') and isinstance(st.value, ast.Dict):
            for k, v in zip(st.value.keys, st.value.values):
                if isinstance(k, ast.Constant):
                    for ln, kk in del_ops:
                        if k.lineno == ln and k.value == kk:
                            dels.append((k.lineno, v.end_lineno))
    print('line deletions', len(dels), len(del_ops))
    for a, b in sorted(dels, reverse=True):
        del lines[a - 1:b]
    open(G, 'w', encoding='utf-8').write('\n'.join(lines))
    print('applied')
