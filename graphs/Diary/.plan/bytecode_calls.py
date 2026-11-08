"""Planning aid (not a deliverable): per-method source line range and outgoing
invoke targets from .class files, so round A (direct calls) and lambda numbering
can be checked against bytecode. Usage:
  python3 -I bytecode_calls.py <classes_dir> > bytecode_calls.txt
Lines:  M <Class.method><desc> lines=<first>-<last>
        -> <kind> <Owner.method><desc> @<line>
invokedynamic targets are resolved through BootstrapMethods to the lambda body.
"""
import os
import struct
import sys

# instruction lengths (excluding opcode byte); -1 = variable
L = [0] * 256
for op in list(range(0x10, 0x11)) + [0x12, 0x15, 0x16, 0x17, 0x18, 0x19, 0x36, 0x37, 0x38, 0x39, 0x3a, 0xa9, 0xbc]:
    L[op] = 1
for op in [0x11, 0x13, 0x14, 0x84, 0xb2, 0xb3, 0xb4, 0xb5, 0xb6, 0xb7, 0xb8, 0xbb, 0xbd, 0xc0, 0xc1] + list(range(0x99, 0xa9)) + [0xc6, 0xc7]:
    L[op] = 2
L[0xc5] = 3
for op in [0xb9, 0xba, 0xc8, 0xc9]:
    L[op] = 4
L[0xaa] = L[0xab] = L[0xc4] = -1


def parse(path):
    d = open(path, 'rb').read()
    n = struct.unpack_from('>H', d, 8)[0]
    pool = [None] * n
    p, i = 10, 1
    while i < n:
        t = d[p]
        p += 1
        if t == 1:
            ln = struct.unpack_from('>H', d, p)[0]
            pool[i] = ('utf', d[p + 2:p + 2 + ln].decode('utf-8', 'replace'))
            p += 2 + ln
        elif t in (3, 4):
            p += 4
        elif t in (5, 6):
            p += 8
            i += 1
        elif t in (7, 8, 16, 19, 20):
            pool[i] = (t, struct.unpack_from('>H', d, p)[0])
            p += 2
        elif t in (9, 10, 11, 12, 17, 18):
            pool[i] = (t,) + struct.unpack_from('>HH', d, p)
            p += 4
        elif t == 15:
            pool[i] = (t, d[p], struct.unpack_from('>H', d, p + 1)[0])
            p += 3
        i += 1
    u = lambda k: pool[k][1]
    this = u(pool[struct.unpack_from('>H', d, p + 2)[0]][1])
    p += 6
    ni = struct.unpack_from('>H', d, p)[0]
    p += 2 + 2 * ni

    def members(p):
        cnt = struct.unpack_from('>H', d, p)[0]
        p += 2
        out = []
        for _ in range(cnt):
            acc, ni_, di, na = struct.unpack_from('>HHHH', d, p)
            p += 8
            attrs = []
            for _ in range(na):
                an, al = struct.unpack_from('>HI', d, p)
                attrs.append((u(an), d[p + 6:p + 6 + al]))
                p += 6 + al
            out.append((acc, u(ni_), u(di), attrs))
        return p, out

    p, _ = members(p)
    p, meths = members(p)
    na = struct.unpack_from('>H', d, p)[0]
    p += 2
    bsm = []
    for _ in range(na):
        an, al = struct.unpack_from('>HI', d, p)
        if u(an) == 'BootstrapMethods':
            b = d[p + 6:p + 6 + al]
            k = struct.unpack_from('>H', b, 0)[0]
            q = 2
            for _ in range(k):
                ref, nargs = struct.unpack_from('>HH', b, q)
                args = struct.unpack_from('>' + 'H' * nargs, b, q + 4)
                bsm.append(args)
                q += 4 + 2 * nargs
        p += 6 + al

    def mref(k):
        e = pool[k]
        cls = u(pool[e[1]][1])
        nt = pool[e[2]]
        return '%s.%s%s' % (cls.rsplit('/', 1)[-1], u(nt[1]), u(nt[2]))

    def indy(k):
        e = pool[k]
        for a in bsm[e[1]]:
            if pool[a] and pool[a][0] == 15:
                return mref(pool[a][2])
        return '?'

    res = []
    for acc, name, desc, attrs in meths:
        code = dict(attrs).get('Code')
        if code is None:
            continue
        clen = struct.unpack_from('>I', code, 4)[0]
        bc = code[8:8 + clen]
        q = 8 + clen
        et = struct.unpack_from('>H', code, q)[0]
        q += 2 + 8 * et
        nat = struct.unpack_from('>H', code, q)[0]
        q += 2
        lnt = []
        for _ in range(nat):
            an, al = struct.unpack_from('>HI', code, q)
            if u(an) == 'LineNumberTable':
                k = struct.unpack_from('>H', code, q + 6)[0]
                for j in range(k):
                    lnt.append(struct.unpack_from('>HH', code, q + 8 + 4 * j))
            q += 6 + al
        lnt.sort()

        def line(pc):
            ln = None
            for s, l_ in lnt:
                if s <= pc:
                    ln = l_
            return ln
        calls = []
        pc = 0
        while pc < len(bc):
            op = bc[pc]
            if op in (0xb6, 0xb7, 0xb8, 0xb9):
                k = struct.unpack_from('>H', bc, pc + 1)[0]
                calls.append(({0xb6: 'virt', 0xb7: 'spec', 0xb8: 'stat', 0xb9: 'intf'}[op], mref(k), line(pc)))
            elif op == 0xba:
                k = struct.unpack_from('>H', bc, pc + 1)[0]
                calls.append(('indy', indy(k), line(pc)))
            if op == 0xaa:
                a = (pc + 4) & ~3
                lo, hi = struct.unpack_from('>ii', bc, a + 4)
                pc = a + 12 + 4 * (hi - lo + 1)
            elif op == 0xab:
                a = (pc + 4) & ~3
                np_ = struct.unpack_from('>i', bc, a + 4)[0]
                pc = a + 8 + 8 * np_
            elif op == 0xc4:
                pc += 6 if bc[pc + 1] == 0x84 else 4
            else:
                pc += 1 + L[op]
        lines = [l_ for _, l_ in lnt]
        res.append((this, name, desc, (min(lines), max(lines)) if lines else None, calls))
    return res


def main():
    root = sys.argv[1]
    for dp, _, fs in sorted(os.walk(root)):
        for f in sorted(fs):
            if not f.endswith('.class') or 'JacocoInstrument' in dp:
                continue
            for cls, name, desc, rng, calls in parse(os.path.join(dp, f)):
                print('M %s.%s%s lines=%s' % (cls.rsplit('/', 1)[-1], name, desc, '%d-%d' % rng if rng else '-'))
                for kind, tgt, ln in calls:
                    print('    -> %s %s @%s' % (kind, tgt, ln))


if __name__ == '__main__':
    main()
