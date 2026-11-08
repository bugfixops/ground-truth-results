"""Scratch: list invoke / new instructions of a .class file with their LineNumberTable line.
Usage: python3 haiku_classparse.py CLASSFILE METHOD_REGEX CALLEE_REGEX
  METHOD_REGEX '-' lists method names only. CALLEE_REGEX is matched against 'owner.name desc' or 'new owner'."""
import re
import struct
import sys

OPNAME = {0xb6: 'invokevirtual', 0xb7: 'invokespecial', 0xb8: 'invokestatic', 0xb9: 'invokeinterface', 0xbb: 'new'}


def oplen(code, o):
    op = code[o]
    if op == 0xaa:
        p = (o + 4) & ~3
        _, low, high = struct.unpack('>iii', code[p:p + 12])
        return p + 12 + 4 * (high - low + 1) - o
    if op == 0xab:
        p = (o + 4) & ~3
        _, npairs = struct.unpack('>ii', code[p:p + 8])
        return p + 8 + 8 * npairs - o
    if op == 0xc4:
        return 6 if code[o + 1] == 0x84 else 4
    if op in (0x10, 0x12, 0x15, 0x16, 0x17, 0x18, 0x19, 0x36, 0x37, 0x38, 0x39, 0x3a, 0xa9, 0xbc):
        return 2
    if op in (0x11, 0x13, 0x14, 0x84, 0xb2, 0xb3, 0xb4, 0xb5, 0xb6, 0xb7, 0xb8, 0xbb, 0xbd, 0xc0, 0xc1, 0xc6, 0xc7) or 0x99 <= op <= 0xa8:
        return 3
    if op in (0xb9, 0xba, 0xc8, 0xc9):
        return 5
    if op == 0xc5:
        return 4
    return 1


def parse(path):
    d = open(path, 'rb').read()
    p = 8
    n, = struct.unpack('>H', d[p:p + 2])
    p += 2
    cp = [None] * n
    i = 1
    while i < n:
        t = d[p]
        p += 1
        if t == 1:
            ln, = struct.unpack('>H', d[p:p + 2])
            p += 2
            cp[i] = ('U', d[p:p + ln].decode('utf-8', 'replace'))
            p += ln
        elif t in (3, 4):
            cp[i] = ('I', None)
            p += 4
        elif t in (5, 6):
            cp[i] = ('L', None)
            p += 8
            i += 1
        elif t in (7, 8, 16, 19, 20):
            cp[i] = ('R', struct.unpack('>H', d[p:p + 2])[0])
            p += 2
        elif t in (9, 10, 11, 12, 17, 18):
            cp[i] = ('M', struct.unpack('>HH', d[p:p + 4]))
            p += 4
        elif t == 15:
            cp[i] = ('MH', None)
            p += 3
        else:
            raise ValueError('constant tag %d at %d' % (t, p))
        i += 1

    def utf(ix):
        return cp[ix][1]

    def cls(ix):
        return utf(cp[ix][1])

    def ref(ix):
        ci, nti = cp[ix][1]
        ni, di = cp[nti][1]
        return cls(ci), utf(ni), utf(di)

    p += 6
    ic, = struct.unpack('>H', d[p:p + 2])
    p += 2 + 2 * ic
    for _ in range(2):  # fields, then methods (fields are skipped)
        cnt, = struct.unpack('>H', d[p:p + 2])
        p += 2
        if _ == 0:
            for _f in range(cnt):
                p += 6
                ac, = struct.unpack('>H', d[p:p + 2])
                p += 2
                for _a in range(ac):
                    _, al = struct.unpack('>HI', d[p:p + 6])
                    p += 6 + al
            continue
        methods = []
        for _m in range(cnt):
            acc, ni, di, ac = struct.unpack('>HHHH', d[p:p + 8])
            p += 8
            name, desc, code = utf(ni), utf(di), None
            for _a in range(ac):
                an, al = struct.unpack('>HI', d[p:p + 6])
                if utf(an) == 'Code':
                    cl, = struct.unpack('>I', d[p + 6 + 4:p + 6 + 8])
                    cb = d[p + 6 + 8:p + 6 + 8 + cl]
                    q = p + 6 + 8 + cl
                    ec, = struct.unpack('>H', d[q:q + 2])
                    q += 2 + 8 * ec
                    sa, = struct.unpack('>H', d[q:q + 2])
                    q += 2
                    lnt = []
                    for _s in range(sa):
                        sn, sl = struct.unpack('>HI', d[q:q + 6])
                        q += 6
                        if utf(sn) == 'LineNumberTable':
                            cnt2, = struct.unpack('>H', d[q:q + 2])
                            for k in range(cnt2):
                                spc, ln2 = struct.unpack('>HH', d[q + 2 + 4 * k:q + 6 + 4 * k])
                                lnt.append((spc, ln2))
                        q += sl
                    code = (cb, sorted(lnt))
                p += 6 + al
            methods.append((name, desc, code))
    return cp, methods, ref, cls


def line_of(lnt, o):
    best = None
    for spc, ln in lnt:
        if spc <= o:
            best = ln
    return best


def main(argv):
    path, mre, cre = argv[1], argv[2], argv[3]
    cp, methods, ref, cls = parse(path)
    if mre == '-':
        for name, desc, code in methods:
            print(name, desc, 'has_code' if code else 'abstract')
        return
    for name, desc, code in methods:
        if not re.fullmatch(mre, name) or code is None:
            continue
        cb, lnt = code
        print('== %s%s  (code bytes=%d, line entries=%d)' % (name, desc, len(cb), len(lnt)))
        o = 0
        while o < len(cb):
            op = cb[o]
            if op in OPNAME:
                ix, = struct.unpack('>H', cb[o + 1:o + 3])
                if op == 0xbb:
                    tag = 'new %s' % cls(ix)
                else:
                    owner, mname, mdesc = ref(ix)
                    tag = '%s.%s%s' % (owner, mname, mdesc)
                    tag = '%s %s' % (OPNAME[op], tag)
                if re.search(cre, tag):
                    print('   off=%-4d line=%-4s %s' % (o, line_of(lnt, o), tag))
            o += oplen(cb, o)


if __name__ == '__main__':
    main(sys.argv)
