"""Scratch: R references (getstatic R$x vs inlined ints), framework ids, reflection/native/string dispatch stats."""
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
REFL = {('java/lang/Class', 'forName'), ('java/lang/Class', 'newInstance'), ('java/lang/Class', 'getMethod'),
        ('java/lang/Class', 'getDeclaredMethod'), ('java/lang/reflect/Method', 'invoke'),
        ('java/lang/reflect/Constructor', 'newInstance'), ('java/lang/Class', 'getConstructor'),
        ('java/lang/Class', 'getDeclaredConstructor'), ('android/content/res/Resources', 'getIdentifier'),
        ('java/lang/Class', 'getField'), ('java/lang/Class', 'getDeclaredField')}
for app in APPS:
    cfj = json.load(open(os.path.join(ROOT, app, 'app/class_files.json')))
    base = os.path.join(ROOT, app, 'app')
    classes = {}
    for v in cfj.values():
        for d in v['classfiles']:
            for p in cf.class_files(os.path.join(base, d)):
                c = cf.parse(p)
                classes[c.name] = c
    st = collections.Counter()
    rref = collections.Counter()
    fw = collections.Counter()
    refl = collections.Counter()
    natives = 0
    start_kinds = collections.Counter()
    for c in classes.values():
        if 'JacocoInstrument' in c.name:
            continue
        for acc, name, desc, at in c.methods:
            if acc & 0x0100:
                natives += 1
            code, sub, _ = cf.code_of(c, at)
            if code is None:
                continue
            for pc, op, opnd in cf.walk(code):
                if op in (0x12, 0x13):
                    ix = opnd[0] if op == 0x12 else struct.unpack('>H', opnd[:2])[0]
                    e = c.pool[ix]
                    if e[0] == 'int':
                        v = e[1] & 0xffffffff
                        if v >> 24 == 0x7f:
                            st['ldc 0x7f'] += 1
                        elif v >> 24 == 0x01 and (v >> 16) & 0xff in (0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10):
                            fw['0x%08x' % v] += 1
                    elif e[0] == 'class':
                        st['ldc class'] += 1
                elif op == 0xb2:
                    owner, n, d = cf.ref(c, struct.unpack('>H', opnd[:2])[0])
                    sn = owner.rsplit('/', 1)[-1]
                    if sn == 'R' or sn.startswith('R$'):
                        rref[owner] += 1
                elif op in (0xb6, 0xb7, 0xb8, 0xb9):
                    owner, n, d = cf.ref(c, struct.unpack('>H', opnd[:2])[0])
                    if (owner, n) in REFL:
                        refl[owner.rsplit('/', 1)[-1] + '.' + n] += 1
                    if n in ('startActivity', 'startActivityForResult', 'startService', 'bindService', 'sendBroadcast',
                             'startForegroundService', 'sendOrderedBroadcast', 'getActivity', 'getBroadcast', 'getService',
                             'getForegroundService', 'setClass', 'setClassName', 'setComponent', 'launch', 'registerReceiver',
                             'startActivities', 'navigate', 'enqueue', 'enqueueUniqueWork', 'schedule', 'setExact', 'set',
                             'setRepeating', 'setInexactRepeating', 'setAndAllowWhileIdle', 'setExactAndAllowWhileIdle'):
                        start_kinds[owner.rsplit('/', 1)[-1] + '.' + n] += 1
    print('== %s %s natives=%d' % (app, dict(st), natives))
    print('   getstatic R refs:', rref.most_common(6))
    print('   framework ids (0x01..):', fw.most_common(12))
    print('   reflection:', dict(refl))
    print('   start/intent-ish calls:', start_kinds.most_common(18))
