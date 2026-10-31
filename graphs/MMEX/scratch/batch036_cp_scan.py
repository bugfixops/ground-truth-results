"""Read-only constant-pool scan of the app's compiled classes (batch 036 evidence).

For every .class file under the app build output, list each Methodref, InterfaceMethodref and
Fieldref whose owner class is one of the batch 036 targets. A reference that is absent from every
constant pool cannot be executed by the app code (javap is not usable here: no Java runtime).
"""
import os
import struct
import sys

ROOT = 'final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes'
TARGETS = ('FormatUtilities', 'FormatUtilities_Factory', 'FormatUtilities_MembersInjector',
           'FilterDatePeriods', 'HttpMethods', 'InfoKeys', 'ExportToCsvFile')


def parse_cp(data):
    n = struct.unpack_from('>H', data, 8)[0]
    pos = 10
    cp = [None] * n
    i = 1
    while i < n:
        tag = data[pos]
        if tag == 1:
            ln = struct.unpack_from('>H', data, pos + 1)[0]
            cp[i] = ('utf8', data[pos + 3:pos + 3 + ln].decode('utf-8', 'replace'))
            pos += 3 + ln
        elif tag in (3, 4):
            cp[i] = ('num', None)
            pos += 5
        elif tag in (5, 6):
            cp[i] = ('num', None)
            pos += 9
            i += 1
        elif tag in (7, 8, 16, 19, 20):
            cp[i] = (tag, struct.unpack_from('>H', data, pos + 1)[0])
            pos += 3
        elif tag in (9, 10, 11, 12, 17, 18):
            a, b = struct.unpack_from('>HH', data, pos + 1)
            cp[i] = (tag, a, b)
            pos += 5
        elif tag == 15:
            cp[i] = (tag, data[pos + 1], struct.unpack_from('>H', data, pos + 2)[0])
            pos += 4
        else:
            raise ValueError('bad tag %d at %d' % (tag, pos))
        i += 1
    return cp, pos


def utf(cp, idx):
    e = cp[idx]
    return e[1] if e and e[0] == 'utf8' else '?'


def cls_name(cp, idx):
    e = cp[idx]
    return utf(cp, e[1]) if e and e[0] == 7 else '?'


def nat(cp, idx):
    e = cp[idx]
    return utf(cp, e[1]), utf(cp, e[2])


def main():
    hits = []
    files = 0
    for dp, _, fns in os.walk(ROOT):
        for fn in fns:
            if not fn.endswith('.class'):
                continue
            path = os.path.join(dp, fn)
            files += 1
            data = open(path, 'rb').read()
            cp, _ = parse_cp(data)
            owner_of = {}
            for idx, e in enumerate(cp):
                if e and e[0] in (9, 10, 11):
                    owner = cls_name(cp, e[1]).split('/')[-1]
                    if owner in TARGETS:
                        name, desc = nat(cp, e[2])
                        kind = {9: 'Fieldref', 10: 'Methodref', 11: 'InterfaceMethodref'}[e[0]]
                        hits.append((os.path.relpath(path, ROOT), kind, owner, name, desc))
    print('class files scanned: %d' % files)
    print('references to batch 036 owners (file | kind | owner.name desc):')
    for h in sorted(hits):
        print('%s | %s | %s.%s %s' % h)
    print('total references: %d' % len(hits))


if __name__ == '__main__':
    sys.exit(main())
