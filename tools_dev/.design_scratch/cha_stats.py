"""Scratch: invoke-site counts, CHA fan-out with/without `new`-based instantiation, accessor/bridge counts."""
import collections
import json
import os
import struct
import sys

sys.path.insert(0, os.path.dirname(__file__))
import cf

ROOT = '/Users/darshan/Desktop/yang/work/final_java_only'
APPS = sys.argv[1:] or ['Aegis', 'AmazeFileManager', 'AnkiDroid', 'AnyMemo', 'Currency', 'Diary', 'hash-checker',
                        'LibreTorrent', 'Markor', 'MMEX', 'Omni-Notes', 'openlauncher', 'Vanilla-Music']
ACC_STATIC, ACC_PRIVATE, ACC_FINAL, ACC_ABSTRACT, ACC_INTERFACE, ACC_SYNTHETIC, ACC_BRIDGE = (
    0x0008, 0x0002, 0x0010, 0x0400, 0x0200, 0x1000, 0x0040)

for app in APPS:
    cfj = json.load(open(os.path.join(ROOT, app, 'app/class_files.json')))
    base = os.path.join(ROOT, app, 'app')
    classes = {}
    for v in cfj.values():
        for d in v['classfiles']:
            for p in cf.class_files(os.path.join(base, d)):
                c = cf.parse(p)
                classes[c.name] = c
    subs = collections.defaultdict(set)
    for c in classes.values():
        for s in [c.super] + c.interfaces:
            if s:
                subs[s].add(c.name)

    def all_subs(n):
        out, st = set(), [n]
        while st:
            x = st.pop()
            for y in subs.get(x, ()):
                if y not in out:
                    out.add(y)
                    st.append(y)
        return out

    decl = {(c.name, m[1], m[2]): m[0] for c in classes.values() for m in c.methods}

    def resolve(t, name, desc):
        x = t
        while x in classes:
            if (x, name, desc) in decl and not decl[(x, name, desc)] & ACC_ABSTRACT:
                return x
            x = classes[x].super
        return None

    inst = set()
    st = collections.Counter()
    fan = collections.Counter()
    fan_inst = collections.Counter()
    for c in classes.values():
        for acc, name, desc, at in c.methods:
            code, sub, _ = cf.code_of(c, at)
            if code is None:
                continue
            if acc & ACC_BRIDGE:
                st['bridge methods'] += 1
            if name.startswith('access$'):
                st['access$ methods'] += 1
            for pc, op, opnd in cf.walk(code):
                if op == 0xbb:
                    inst.add(c.cls(struct.unpack('>H', opnd[:2])[0]))
    for c in classes.values():
        if 'JacocoInstrument' in c.name:
            continue
        for acc, name, desc, at in c.methods:
            code, sub, _ = cf.code_of(c, at)
            if code is None:
                continue
            for pc, op, opnd in cf.walk(code):
                if op not in (0xb6, 0xb7, 0xb8, 0xb9):
                    continue
                owner, n, d = cf.ref(c, struct.unpack('>H', opnd[:2])[0])
                kind = {0xb6: 'virtual', 0xb7: 'special', 0xb8: 'static', 0xb9: 'interface'}[op]
                app_owner = owner in classes
                st['%s %s' % (kind, 'app' if app_owner else 'ext')] += 1
                if kind in ('virtual', 'interface') and app_owner:
                    ts = {owner} | all_subs(owner)
                    impl = {resolve(t, n, d) for t in ts if t in classes and not classes[t].access & (ACC_ABSTRACT | ACC_INTERFACE)}
                    impl.discard(None)
                    impl_i = {resolve(t, n, d) for t in ts if t in inst}
                    impl_i.discard(None)
                    fan[min(len(impl), 10)] += 1
                    fan_inst[min(len(impl_i), 10)] += 1
                if kind in ('virtual', 'interface') and not app_owner:
                    ts = all_subs(owner)
                    impl = {resolve(t, n, d) for t in ts}
                    impl.discard(None)
                    if impl:
                        st['ext-owner sites with app impls'] += 1
    print('== %-16s classes %d  inst(new) %d' % (app, len(classes), len(inst)), dict(sorted(st.items())))
    print('   app-owner virtual/interface fan-out (all concrete): ', dict(sorted(fan.items())))
    print('   app-owner virtual/interface fan-out (new-instantiated):', dict(sorted(fan_inst.items())))
    sys.stdout.flush()
