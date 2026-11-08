"""Scratch generator: INFERRED Dagger edges for the @Inject fields of AnyMemo 10.12.2.

Run from work/:  python3 -I graphs/AnyMemo/scratch/gen_dagger.py
Writes graphs/AnyMemo/scratch/chunk3_dagger.txt (python lines of e(...) calls) and prints a report.
Each edge: injectX (field level, from DaggerAppComponents Impl) -> the provider target
(@Provides method in modules, or the @Inject constructor of the (bound) type); then each
constructor/provides node -> its own dependencies (edge from the parent node).
"""
import json, os, re, glob

ROOT = '/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo'
G = json.load(open('graphs/AnyMemo/out/anymemo_trigger_graph.json'))
keys = set(G['verdict'])
existing = set((e['src'], e['dst']) for e in G['edges'])

files = {}
for dp, dn, fn in os.walk(ROOT):
    for f in fn:
        if f.endswith('.java'):
            files.setdefault(f[:-5], []).append(os.path.join(dp, f))

def read(p):
    return open(p, encoding='utf-8', errors='replace').read()

def rel(p):
    return os.path.relpath(p, ROOT)

SILENT = {'Activity', 'Context', 'BaseActivity', 'AMApplication', 'Application'}

# ---- @Binds and @Provides declarations in modules/
binds = {}   # interface simple name -> (impl simple name, module, line)
prov = {}    # return simple name -> (module, method, [param types], line)
for p in sorted(glob.glob(os.path.join(ROOT, 'modules', '*.java'))):
    mod = os.path.basename(p)[:-5]
    lines = read(p).split('\n')
    for i, line in enumerate(lines):
        if '@Binds' in line:
            sig = ' '.join(lines[i:i + 3]).split(';')[0]
            m = re.search(r'(\w+)\s+(\w+)\s*\(\s*(?:final\s+)?(\w+)\s+\w+\s*\)', sig)
            if m:
                binds[m.group(1)] = (m.group(3), mod, i + 1)
        if re.search(r'@Provides\b', line):
            sig = ' '.join(lines[i:i + 6]).split('{')[0]
            m = re.search(r'(\w+)\s+(provides?\w*)\s*\(([^)]*)\)', sig)
            if m:
                params = []
                for prm in m.group(3).split(','):
                    prm = re.sub(r'@\w+(\([^)]*\))?', '', prm).replace('final ', '').strip()
                    if prm:
                        params.append(prm.split()[0].split('<')[0].split('.')[-1])
                prov[m.group(1)] = (mod, m.group(2), params, i + 1)

def find_key(cls, meth, params=None):
    base = cls + '.' + meth
    if base in keys:
        return base
    if params is None:
        return None
    want = base + '(' + ','.join(params) + ')'
    return want if want in keys else None

def inject_ctor(t):
    ps = files.get(t)
    if not ps or len(ps) != 1:
        return None
    text = read(ps[0])
    m = re.search(r'@Inject\s+(?:public\s+|protected\s+|private\s+)?' + re.escape(t) + r'\s*\(([^)]*)\)', text)
    if not m:
        return None
    line = text[:m.start()].count('\n') + 1
    params = []
    for prm in m.group(1).split(','):
        prm = re.sub(r'@\w+(\([^)]*\))?', '', prm).replace('final ', '').strip()
        if prm:
            params.append(prm.split()[0].split('<')[0].split('.')[-1])
    return params, rel(ps[0]), line

def resolve(t):
    """Return (key, info) for the object Dagger builds for type t, or (None, reason)."""
    if t in SILENT:
        return None, 'silent'
    if t in binds:
        t = binds[t][0]
    if t in prov:
        mod, meth, params, line = prov[t]
        key = find_key(mod, meth)
        if key is None:
            return None, 'provides not a unique key: %s.%s' % (mod, meth)
        return key, ('provides', mod, meth, params, line)
    c = inject_ctor(t)
    if c:
        params, path, line = c
        key = find_key(t, '<init>', params)
        if key is None:
            return None, 'ctor key missing: %s.<init>(%s)' % (t, ','.join(params))
        return key, ('ctor', t, params, path, line)
    return None, 'no @Inject ctor or @Provides for %s' % t

out, report, seen = [], [], set()

def add_edge(src, dst, trig, ev):
    if src not in keys or dst not in keys:
        report.append('MISSING NODE %s -> %s' % (src, dst))
        return
    if src == dst or (src, dst) in existing or (src, dst) in seen:
        return
    seen.add((src, dst))
    out.append("e(%r, %r, 'CALL', %r,\n  evidence=FW_DAGGER + %r)" % (src, dst, trig, ev))

expanded = set()

def expand(key, info):
    if key in expanded:
        return
    expanded.add(key)
    kind = info[0]
    if kind == 'ctor':
        _, t, params, path, line = info
        pairs = [(p, 'Dagger passes the %s dependency of the @Inject constructor of %s' % (p, t),
                  'SRC %s:%d (@Inject constructor)' % (path, line)) for p in params]
    else:
        _, mod, meth, params, line = info
        pairs = [(p, 'Dagger passes the %s parameter of %s.%s' % (p, mod, meth),
                  'SRC modules/%s.java:%d (@Provides parameter)' % (mod, line)) for p in params]
    for p, trig, ev in pairs:
        k2, info2 = resolve(p)
        if k2 is None:
            if info2 != 'silent':
                report.append('  dep %s of %s: %s' % (p, key, info2))
            continue
        add_edge(key, k2, trig, ev)
        expand(k2, info2)

# ---- injection points: @Inject fields declared at class level (4-space indent)
fields = []
for name, paths in sorted(files.items()):
    if len(paths) != 1:
        continue
    text = read(paths[0])
    for m in re.finditer(r'\n( {4})@Inject\s+((?:Provider<[^>]*>|[\w.]+(?:<[^;=(){}]*>)?))\s+(\w+)\s*;', text):
        line = text[:m.start()].count('\n') + 2
        fields.append((name, m.group(2), m.group(3), rel(paths[0]), line))
    for m in re.finditer(r'\n( {8,})@Inject\s', text):
        report.append('nested @Inject skipped in %s (line %d)' % (name, text[:m.start()].count('\n') + 2))

for cls, ftype, fname, path, line in fields:
    cands = [k for k in keys if k.startswith('DaggerAppComponents$') and k.endswith('.inject' + cls)]
    if len(cands) != 1:
        report.append('no unique inject%s (%s)' % (cls, cands))
        continue
    src = cands[0]
    t = ftype
    m = re.match(r'Provider<(.*)>$', t)
    if m:
        t = m.group(1)
    if '<' in t:
        report.append('generic field skipped: %s.%s %s' % (cls, fname, ftype))
        continue
    t = t.split('.')[-1]
    k2, info = resolve(t)
    if k2 is None:
        if info != 'silent':
            report.append('field %s.%s (%s): %s' % (cls, fname, t, info))
        continue
    trig = 'Dagger creates the @Inject field %s of %s' % (fname, cls)
    ev = 'SRC %s:%d (@Inject field)' % (path, line)
    add_edge(src, k2, trig, ev)
    expand(k2, info)

with open('graphs/AnyMemo/scratch/chunk3_dagger.txt', 'w') as f:
    f.write('\n'.join(out) + '\n')

print('fields found:', len(fields))
print('new edges:', len(out))
for r in report:
    print(r)
