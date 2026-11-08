"""Scratch: prototype the v2 universe + naming rules; count clashes, overload collisions, generated."""
import collections
import json
import os
import struct
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(__file__))
import cf

ROOT = '/Users/darshan/Desktop/yang/work/final_java_only'
APPS = sys.argv[1:] or ['Aegis', 'AmazeFileManager', 'AnkiDroid', 'AnyMemo', 'Currency', 'Diary', 'hash-checker',
                        'LibreTorrent', 'Markor', 'MMEX', 'Omni-Notes', 'openlauncher', 'Vanilla-Music']
JVM = {'I': 'int', 'J': 'long', 'Z': 'boolean', 'F': 'float', 'D': 'double', 'B': 'byte', 'C': 'char', 'S': 'short', 'V': 'void'}


def param_names(desc, full=False):
    args, i, out = desc[1:desc.index(')')], 0, []
    while i < len(args):
        dims = 0
        while args[i] == '[':
            dims += 1; i += 1
        if args[i] == 'L':
            j = args.index(';', i)
            name = args[i + 1:j] if full else args[i + 1:j].rsplit('/', 1)[-1].split('$')[-1]
            if full:
                name = name.replace('/', '.')
            i = j + 1
        else:
            name = JVM[args[i]]; i += 1
        out.append(name + '[]' * dims)
    return ','.join(out)


def src_index(app_root):
    idx = set()
    for dp, dn, fn in os.walk(app_root):
        dn[:] = [d for d in dn if d != 'build']
        for f in fn:
            if f.endswith('.java'):
                idx.add(os.path.join(dp, f))
    suffixes = collections.defaultdict(set)
    return idx


for app in APPS:
    cfj = json.load(open(os.path.join(ROOT, app, 'app/class_files.json')))
    base = os.path.join(ROOT, app, 'app')
    classes = {}
    for v in cfj.values():
        for d in v['classfiles']:
            for p in cf.class_files(os.path.join(base, d)):
                c = cf.parse(p)
                classes[c.name] = c
    jac = {}
    sets = {}
    for run in ('monkey', 'ape'):
        s = set()
        for c in ET.parse(os.path.join(ROOT, app, run, 'report/report.xml')).getroot().iter('class'):
            for m in c.findall('method'):
                s.add((c.get('name'), m.get('name'), m.get('desc')))
        sets[run] = s
    same = sets['monkey'] == sets['ape']
    jacset = sets['monkey'] | sets['ape']
    uni = set()
    for k in jacset:
        if 'JacocoInstrument' in k[0] or k[0].rsplit('/', 1)[-1] in ('BuildConfig', 'R') or k[0].rsplit('/', 1)[-1].startswith('R$'):
            continue
        uni.add(k)
    flagged = set()
    for c in classes.values():
        if 'JacocoInstrument' in c.name:
            continue
        for acc, name, desc, at in c.methods:
            code, sub, _ = cf.code_of(c, at)
            if (code is not None and name == '<init>' and desc == '()V' and acc & 2 and len(code) == 5
                    and code[0] == 0x2a and code[1] == 0xb7 and code[4] == 0xb1 and (c.name, name, desc) not in jacset
                    and not c.access & 0x1000
                    and not any('Generated' in a.rsplit('/', 1)[-1] for _, a in cf.annotations(c, c.attrs))):
                flagged.add((c.name, name, desc))
    universe = uni | flagged
    # generated: source file not found anywhere in the checkout (excluding build dirs)
    allsrc = set()
    for dp, dn, fn in os.walk(base):
        dn[:] = [d for d in dn if d != 'build']
        for f in fn:
            if f.endswith('.java'):
                allsrc.add(os.path.join(dp, f).replace(os.sep, '/'))
    suffix_ok = set()
    for p in allsrc:
        suffix_ok.add(p)
    def has_src(c):
        sf = None
        for nm, b in c.attrs:
            if nm == 'SourceFile':
                sf = c.utf(struct.unpack_from('>H', b, 0)[0])
        if not sf:
            return False
        rel = (c.name.rsplit('/', 1)[0] + '/' if '/' in c.name else '') + sf
        return any(p.endswith('/' + rel) for p in allsrc)
    gen_classes = {n for n in {k[0] for k in universe} if not has_src(classes[n])}
    gen_methods = sum(1 for k in universe if k[0] in gen_classes)
    # naming
    owners = {k[0] for k in universe}
    top = collections.defaultdict(set)
    for n in owners:
        simple = n.rsplit('/', 1)[-1]
        pkg = n.rsplit('/', 1)[0] if '/' in n else ''
        top[simple.split('$')[0]].add(pkg)
    prefix = {}
    for t, pkgs in top.items():
        if len(pkgs) < 2:
            continue
        for p in pkgs:
            segs = p.split('/') if p else []
            k = 1
            while True:
                mine = '/'.join(segs[-k:]) if segs else '(default)'
                others = ['/'.join(q.split('/')[-k:]) if q else '(default)' for q in pkgs if q != p]
                if mine not in others or k >= len(segs):
                    break
                k += 1
            prefix[(p, t)] = mine
    def cls_disp(n):
        simple = n.rsplit('/', 1)[-1]
        pkg = n.rsplit('/', 1)[0] if '/' in n else ''
        pre = prefix.get((pkg, simple.split('$')[0]))
        return (pre + '/' + simple) if pre else simple
    rows = sorted(universe)
    short = {k: cls_disp(k[0]) + '.' + k[1] for k in rows}
    cnt = collections.Counter(short.values())
    names = {}
    for k in rows:
        names[k] = short[k] if cnt[short[k]] == 1 else '%s(%s)' % (short[k], param_names(k[2]))
    c2 = collections.Counter(names.values())
    coll = [k for k in rows if c2[names[k]] > 1]
    for k in coll:
        names[k] = '%s(%s)' % (short[k], param_names(k[2], full=True))
    c3 = collections.Counter(names.values())
    coll3 = [k for k in rows if c3[names[k]] > 1]
    # compare to current scheme
    cur = collections.Counter(k[0].rsplit('/', 1)[-1] + '.' + k[1] for k in rows)
    curn = [k[0].rsplit('/', 1)[-1] + '.' + k[1] if cur[k[0].rsplit('/', 1)[-1] + '.' + k[1]] == 1 else
            '%s(%s)' % (k[0].rsplit('/', 1)[-1] + '.' + k[1], param_names(k[2])) for k in rows]
    merged = len(curn) - len(set(curn))
    changed = sum(1 for k, cn in zip(rows, curn) if names[k] != cn)
    print('%-16s jacoco ape==monkey:%s  universe %d (jacoco %d + flagged %d)  generated classes %d methods %d  '
          'clash-tops %d prefixed-classes %d  overload-fallback %d  unresolved %d  current-scheme merges %d  names changed vs current %d'
          % (app, same, len(universe), len(uni), len(flagged), len(gen_classes), gen_methods,
             sum(1 for t, p in top.items() if len(p) > 1), sum(1 for n in owners if cls_disp(n) != n.rsplit('/', 1)[-1]),
             len(coll), len(coll3), merged, changed))
    for k in coll[:6]:
        print('     overload fallback:', names[k])
    for (p, t), pre in sorted(prefix.items()):
        print('     prefix %s/%s' % (pre, t))
    if app == 'LibreTorrent':
        db = [k for k in universe if k[0] in gen_classes and ('Binding' in k[0] or k[0].endswith('/BR') or 'DataBinderMapper' in k[0] or 'DataBindingComponent' in k[0] or 'DataBindingTriggerClass' in k[0])]
        print('     LibreTorrent databinding methods:', len(db))
    sys.stdout.flush()
