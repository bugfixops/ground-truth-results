"""Scratch: inspect Hilt classes, enum ctor anomalies, generated annotations."""
import collections
import json
import os
import struct
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(__file__))
import cf

ROOT = '/Users/darshan/Desktop/yang/work/final_java_only'


def load(app):
    cfj = json.load(open(os.path.join(ROOT, app, 'app/class_files.json')))
    base = os.path.join(ROOT, app, 'app')
    classes = {}
    for v in cfj.values():
        for d in v['classfiles']:
            for p in cf.class_files(os.path.join(base, d)):
                c = cf.parse(p)
                classes[c.name] = c
    jac = set()
    for run in ('monkey', 'ape'):
        for c in ET.parse(os.path.join(ROOT, app, run, 'report/report.xml')).getroot().iter('class'):
            for m in c.findall('method'):
                jac.add((c.get('name'), m.get('name'), m.get('desc')))
    return classes, jac


classes, jac = load('Aegis')
hilt = sorted(n for n in classes if n.rsplit('/', 1)[-1].startswith('Hilt_'))
print('Aegis Hilt_ classes:', len(hilt))
for n in hilt[:3]:
    c = classes[n]
    print(' ', n, 'super', c.super, 'anns', cf.annotations(c, c.attrs))
    for acc, name, desc, at in c.methods:
        print('     %-40s %-50s acc=0x%04x jacoco=%s' % (name, desc[:50], acc, (n, name, desc) in jac))
# who extends Hilt_ classes
ext = [(n, c.super) for n, c in classes.items() if c.super and c.super.rsplit('/', 1)[-1].startswith('Hilt_')]
print('classes extending Hilt_*:', len(ext), ext[:3])
# a sample generated-annotated class
for n in ('com/beemdevelopment/aegis/AegisModule_ProvideAppDatabaseFactory',):
    c = classes.get(n)
    if c:
        print(n, cf.annotations(c, c.attrs))
# annotation types used across Aegis classes (class-level)
cnt = collections.Counter()
for c in classes.values():
    for vis, a in cf.annotations(c, c.attrs):
        cnt[(vis[7:14], a)] += 1
print('class annotations:', cnt.most_common(25))
# Hilt aggregated deps classes
for n in sorted(classes):
    if n.startswith('hilt_aggregated_deps') or n.startswith('dagger/'):
        c = classes[n]
        print(' agg', n, [m[1] for m in c.methods], cf.annotations(c, c.attrs)[:2], [(n, m[1], m[2]) in jac for m in c.methods])
        break

for app in ('AnyMemo', 'LibreTorrent'):
    classes, jac = load(app)
    for c in classes.values():
        if not c.access & 0x4000:
            continue
        for acc, name, desc, at in c.methods:
            if name == '<init>' and desc == '(Ljava/lang/String;I)V':
                code, sub, _ = cf.code_of(c, at)
                if code is not None and len(code) == 7 and (c.name, name, desc) in jac:
                    print(app, 'reported enum ctor', c.name, 'cls acc 0x%04x m acc 0x%04x' % (c.access, acc), code.hex())
