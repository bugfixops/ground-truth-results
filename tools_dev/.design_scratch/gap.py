"""Scratch: compare list_methods-style universe with JaCoCo per app; categorize the gap."""
import collections
import json
import os
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(__file__))
import cf

ROOT = '/Users/darshan/Desktop/yang/work/final_java_only'
APPS = sys.argv[1:] or ['Aegis', 'AmazeFileManager', 'AnkiDroid', 'AnyMemo', 'Currency', 'Diary', 'hash-checker',
                        'LibreTorrent', 'Markor', 'MMEX', 'Omni-Notes', 'openlauncher', 'Vanilla-Music']
ACC_STATIC, ACC_BRIDGE, ACC_NATIVE, ACC_ABSTRACT, ACC_SYNTHETIC, ACC_ENUM, ACC_PRIVATE, ACC_INTERFACE = (
    0x0008, 0x0040, 0x0100, 0x0400, 0x1000, 0x4000, 0x0002, 0x0200)


def jacoco(app):
    keys = {}
    for run in ('monkey', 'ape'):
        for c in ET.parse(os.path.join(ROOT, app, run, 'report/report.xml')).getroot().iter('class'):
            cn = c.get('name')
            for m in c.findall('method'):
                k = (cn, m.get('name'), m.get('desc'))
                keys.setdefault(k, c.get('sourcefilename'))
    return keys


def trivial_ctor(code):
    # aload_0; invokespecial #x; return
    return code is not None and len(code) == 5 and code[0] == 0x2a and code[1] == 0xb7 and code[4] == 0xb1


for app in APPS:
    cfj = json.load(open(os.path.join(ROOT, app, 'app/class_files.json')))
    dirs = [os.path.join(ROOT, app, 'app', d) for v in cfj.values() for d in v['classfiles']]
    classes = {}
    for d in dirs:
        for p in cf.class_files(d):
            c = cf.parse(p)
            c.dir = d
            if c.name in classes:
                print('  DUPLICATE CLASS', c.name)
            classes[c.name] = c
    jac = jacoco(app)
    jac_noji = {k for k in jac if 'JacocoInstrument' not in k[0]}
    lm = {}
    for c in classes.values():
        p = c.path
        if 'JacocoInstrument' in p or '/R$' in p or 'BuildConfig' in p:
            continue
        for acc, name, desc, at in c.methods:
            if acc & (ACC_ABSTRACT | ACC_NATIVE):
                continue
            if acc & ACC_BRIDGE or name.startswith('access$'):
                continue
            if acc & ACC_SYNTHETIC and not name.startswith('lambda$'):
                continue
            lm[(c.name, name, desc)] = (c, acc, at)
    only_lm = sorted(set(lm) - jac_noji)
    only_jac = sorted(jac_noji - set(lm))
    cat = collections.Counter()
    ex = collections.defaultdict(list)
    for k in only_lm:
        c, acc, at = lm[k]
        cname, name, desc = k
        canns = [a for _, a in cf.annotations(c, c.attrs)]
        manns = [a for _, a in cf.annotations(c, at)]
        code, sub, _ = cf.code_of(c, at)
        if c.access & ACC_SYNTHETIC:
            r = 'synthetic class'
        elif any('Generated' in a.rsplit('/', 1)[-1] for a in canns):
            r = 'class @*Generated* ' + ','.join(sorted({a for a in canns if 'Generated' in a}))
        elif any('Generated' in a.rsplit('/', 1)[-1] for a in manns):
            r = 'method @*Generated*'
        elif c.access & ACC_ENUM and name == 'values' and desc.startswith('()['):
            r = 'enum values()'
        elif c.access & ACC_ENUM and name == 'valueOf' and desc.startswith('(Ljava/lang/String;)'):
            r = 'enum valueOf(String)'
        elif c.access & ACC_ENUM and name == '<init>' and desc.startswith('(Ljava/lang/String;I') :
            r = 'enum ctor'
        elif name == '<init>' and desc == '()V' and acc & ACC_PRIVATE and trivial_ctor(code):
            r = 'private empty no-arg ctor'
        else:
            r = 'OTHER'
        cat[r] += 1
        ex[r].append('%s.%s%s' % (cname.rsplit('/', 1)[-1], name, desc))
    cat2 = collections.Counter()
    ex2 = collections.defaultdict(list)
    for k in only_jac:
        cname = k[0]
        if cname.endswith('/BuildConfig'):
            r = 'BuildConfig'
        elif cname not in classes:
            r = 'class not in class dirs'
        else:
            c = classes[cname]
            acc = [m for m in c.methods if m[1] == k[1] and m[2] == k[2]]
            if not acc:
                r = 'method not in class'
            else:
                a = acc[0][0]
                r = 'flags 0x%04x' % a
        cat2[r] += 1
        ex2[r].append('%s.%s%s' % (cname.rsplit('/', 1)[-1], k[1], k[2]))
    print('== %s: classes %d, list_methods-style %d, jacoco(non-JI) %d' % (app, len(classes), len(lm), len(jac_noji)))
    for r, n in cat.most_common():
        print('   only-in-list  %5d  %s   e.g. %s' % (n, r, ', '.join(ex[r][:4])))
    for r, n in cat2.most_common():
        print('   only-in-jacoco %5d  %s   e.g. %s' % (n, r, ', '.join(ex2[r][:4])))
    sys.stdout.flush()
