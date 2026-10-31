"""Scratch: verify filter rules both ways, name clashes, generated-code signals, bytecode stats."""
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
ACC_PUBLIC, ACC_PRIVATE, ACC_STATIC, ACC_BRIDGE, ACC_NATIVE, ACC_INTERFACE, ACC_ABSTRACT, ACC_SYNTHETIC, ACC_ENUM = (
    0x0001, 0x0002, 0x0008, 0x0040, 0x0100, 0x0200, 0x0400, 0x1000, 0x4000)


def jacoco(app):
    keys = set()
    for run in ('monkey', 'ape'):
        for c in ET.parse(os.path.join(ROOT, app, run, 'report/report.xml')).getroot().iter('class'):
            for m in c.findall('method'):
                keys.add((c.get('name'), m.get('name'), m.get('desc')))
    return keys


def is_gen_ann(c, attrs):
    return any('Generated' in a.rsplit('/', 1)[-1] for _, a in cf.annotations(c, attrs))


def private_empty_noarg(acc, name, desc, code):
    return (name == '<init>' and desc == '()V' and acc & ACC_PRIVATE and code is not None and len(code) == 5
            and code[0] == 0x2a and code[1] == 0xb7 and code[4] == 0xb1)


def enum_empty_ctor(c, acc, name, desc, code):
    if not (c.access & ACC_ENUM and name == '<init>' and desc == '(Ljava/lang/String;I)V'):
        return False
    # aload_0 aload_1 iload_2 invokespecial Enum.<init> return
    return code is not None and len(code) == 7 and code[:3] == b'\x2a\x2b\x1c' and code[3] == 0xb7 and code[6] == 0xb1


for app in APPS:
    cfj = json.load(open(os.path.join(ROOT, app, 'app/class_files.json')))
    base = os.path.join(ROOT, app, 'app')
    dirs = [os.path.join(base, d) for v in cfj.values() for d in v['classfiles']]
    srcdirs = [os.path.join(base, d) for v in cfj.values() for d in v['sourcefiles']]
    classes = {}
    for d in dirs:
        for p in cf.class_files(d):
            c = cf.parse(p)
            classes[c.name] = c
    jac = jacoco(app)
    print('== %s  (%d classes) majors %s' % (app, len(classes), dict(collections.Counter(c.major for c in classes.values()))))
    # rule checks both ways
    viol = collections.Counter()
    rule_hits = collections.Counter()
    gen_ann_classes = set()
    for c in classes.values():
        if 'JacocoInstrument' in c.name:
            continue
        cg = is_gen_ann(c, c.attrs)
        if cg:
            gen_ann_classes.add(c.name)
        for acc, name, desc, at in c.methods:
            code, sub, _ = cf.code_of(c, at)
            if code is None:
                continue
            k = (c.name, name, desc)
            inj = k in jac
            rules = []
            if c.access & ACC_SYNTHETIC: rules.append('synthetic-class')
            if acc & ACC_SYNTHETIC and not name.startswith('lambda$'): rules.append('synthetic-method')
            if acc & ACC_SYNTHETIC and name.startswith('lambda$'): rules.append('lambda')
            if cg: rules.append('class-generated-ann')
            if is_gen_ann(c, at): rules.append('method-generated-ann')
            if c.access & ACC_ENUM and name == 'values' and desc.startswith('()['): rules.append('enum-values')
            if c.access & ACC_ENUM and name == 'valueOf' and desc.startswith('(Ljava/lang/String;)L'): rules.append('enum-valueOf')
            if enum_empty_ctor(c, acc, name, desc, code): rules.append('enum-empty-ctor')
            if private_empty_noarg(acc, name, desc, code): rules.append('private-empty-noarg')
            if c.name.endswith('/BuildConfig'): rules.append('BuildConfig')
            for r in rules:
                rule_hits[(r, inj)] += 1
            if not rules and not inj:
                viol['unexplained-missing'] += 1
                print('   UNEXPLAINED missing from JaCoCo:', c.name, name, desc, hex(acc), hex(c.access))
    print('   rule -> (reported, not reported):',
          {r: (rule_hits[(r, True)], rule_hits[(r, False)]) for r in sorted({r for r, _ in rule_hits})})
    # JaCoCo entries not in class dirs
    miss = [k for k in jac if k[0] not in classes]
    if miss:
        print('   JaCoCo classes not in class dirs:', len(miss), sorted({k[0] for k in miss})[:5])
    # SourceFile check
    nosrc = collections.Counter()
    nosrc_ex = collections.defaultdict(list)
    for c in classes.values():
        if 'JacocoInstrument' in c.name:
            continue
        sf = None
        for nm, b in c.attrs:
            if nm == 'SourceFile':
                sf = c.utf(struct.unpack_from('>H', b, 0)[0])
        pkg = c.name.rsplit('/', 1)[0] if '/' in c.name else ''
        found = sf and any(os.path.isfile(os.path.join(s, pkg, sf)) for s in srcdirs)
        if not found:
            top = c.name.split('$')[0].rsplit('/', 1)[-1]
            key = 'gen-ann' if c.name.split('$')[0] in gen_ann_classes or c.name in gen_ann_classes else 'no-ann'
            nosrc[key] += 1
            nosrc_ex[key].append(c.name.rsplit('/', 1)[-1] + ('' if sf else ' [no SourceFile]'))
    print('   classes whose SourceFile is not in the source dirs:', dict(nosrc))
    for k, v in nosrc_ex.items():
        print('     %s: %s' % (k, ', '.join(sorted(v)[:40])))
    # simple-name clashes among classes that have reported methods (universe)
    uni_classes = {k[0] for k in jac if 'JacocoInstrument' not in k[0] and not k[0].endswith('/BuildConfig')}
    by_simple = collections.defaultdict(list)
    for cn in uni_classes:
        by_simple[cn.rsplit('/', 1)[-1]].append(cn)
    clashes = {s: sorted(v) for s, v in by_simple.items() if len(v) > 1}
    print('   simple-name clashes (universe classes):', len(clashes))
    for s, v in sorted(clashes.items()):
        print('     %s: %s' % (s, v))
    sys.stdout.flush()
