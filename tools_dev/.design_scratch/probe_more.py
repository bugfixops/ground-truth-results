"""Scratch: APK res layout sanity, accessor/bridge/synthetic-ctor body shapes, Dagger-only callees."""
import collections
import json
import os
import re
import struct
import sys
import xml.etree.ElementTree as ET
import zipfile

sys.path.insert(0, os.path.dirname(__file__))
import cf

ROOT = '/Users/darshan/Desktop/yang/work/final_java_only'
APPS = sys.argv[1:] or ['Aegis', 'AmazeFileManager', 'AnkiDroid', 'AnyMemo', 'Currency', 'Diary', 'hash-checker',
                        'LibreTorrent', 'Markor', 'MMEX', 'Omni-Notes', 'openlauncher', 'Vanilla-Music']
INV = (0xb6, 0xb7, 0xb8, 0xb9)
RES_RE = re.compile(r'^res/[a-z]+(-[A-Za-z0-9+_-]+)?/[A-Za-z0-9_.$-]+$')


def gen_ann(c, attrs):
    return any('Generated' in a.rsplit('/', 1)[-1] for _, a in cf.annotations(c, attrs))


for app in APPS:
    adir = os.path.join(ROOT, app, 'app')
    cfj = json.load(open(os.path.join(adir, 'class_files.json')))
    apk = os.path.join(adir, list(cfj)[0])
    z = zipfile.ZipFile(apk)
    names = z.namelist()
    res = [n for n in names if n.startswith('res/')]
    odd = [n for n in res if not RES_RE.match(n)]
    has = ('resources.arsc' in names, 'AndroidManifest.xml' in names)
    classes = {}
    for v in cfj.values():
        for d in v['classfiles']:
            for p in cf.class_files(os.path.join(adir, d)):
                c = cf.parse(p)
                classes[c.name] = c
    jac = set()
    for run in ('monkey', 'ape'):
        for k in ET.parse(os.path.join(ROOT, app, run, 'report/report.xml')).getroot().iter('class'):
            for m in k.findall('method'):
                jac.add((k.get('name'), m.get('name'), m.get('desc')))
    shapes = collections.Counter()
    gen_cls = {n for n, c in classes.items() if gen_ann(c, c.attrs)}
    callers = collections.defaultdict(set)
    for c in classes.values():
        if 'JacocoInstrument' in c.name:
            continue
        for acc, name, desc, at in c.methods:
            code, sub, _ = cf.code_of(c, at)
            if code is None:
                continue
            invs = []
            other = 0
            for pc, op, opnd in cf.walk(code):
                if op in INV or op == 0xba:
                    if op == 0xba:
                        invs.append(('indy', None, None, None))
                    else:
                        invs.append((op,) + cf.ref(c, struct.unpack('>H', opnd[:2])[0]))
                elif op in (0xb2, 0xb3, 0xb4, 0xb5):
                    other += 1
            for x in invs:
                if x[0] != 'indy' and x[1] in classes:
                    callers[(x[1], x[2], x[3])].add((c.name, name, desc))
            synth = acc & 0x1000 and not name.startswith('lambda$')
            if name.startswith('access$'):
                k = 'access$: %d invokes%s' % (len(invs), ', field ops' if other else '')
                shapes[k] += 1
            elif acc & 0x0040:
                k = 'bridge: %d invokes' % len(invs)
                shapes[k] += 1
            elif synth and name == '<init>':
                shapes['synthetic <init>: %d invokes' % len(invs)] += 1
    # universe methods (JaCoCo-reported, non-JI, non-BuildConfig) whose callers are all in @Generated classes
    only_gen = []
    for k in jac:
        if 'JacocoInstrument' in k[0] or k[0].endswith('/BuildConfig'):
            continue
        cs = callers.get(k, set())
        if cs and all(x[0] in gen_cls for x in cs):
            only_gen.append(k)
    print('== %-16s arsc/manifest %s  res files %d  non-standard res paths %d %s' % (app, has, len(res), len(odd), odd[:3]))
    print('   shapes:', dict(sorted(shapes.items())))
    print('   JaCoCo-reported methods whose only bytecode callers are @Generated classes: %d  e.g. %s' % (
        len(only_gen), ['%s.%s' % (k[0].rsplit('/', 1)[-1], k[1]) for k in sorted(only_gen)[:6]]))
    sys.stdout.flush()
