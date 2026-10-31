"""Scratch class-file parser used only to gather facts for DESIGN.md (deleted afterwards)."""
import os
import struct

OPLEN = {}
for op in range(0x00, 0x10): OPLEN[op] = 1
OPLEN[0x10] = 2; OPLEN[0x11] = 3; OPLEN[0x12] = 2; OPLEN[0x13] = 3; OPLEN[0x14] = 3
for op in range(0x15, 0x1a): OPLEN[op] = 2
for op in range(0x1a, 0x36): OPLEN[op] = 1
for op in range(0x36, 0x3b): OPLEN[op] = 2
for op in range(0x3b, 0x84): OPLEN[op] = 1
OPLEN[0x84] = 3
for op in range(0x85, 0x99): OPLEN[op] = 1
for op in range(0x99, 0xa9): OPLEN[op] = 3
OPLEN[0xa9] = 2
for op in range(0xac, 0xb2): OPLEN[op] = 1
for op in range(0xb2, 0xb9): OPLEN[op] = 3
OPLEN[0xb9] = 5; OPLEN[0xba] = 5; OPLEN[0xbb] = 3; OPLEN[0xbc] = 2; OPLEN[0xbd] = 3
OPLEN[0xbe] = 1; OPLEN[0xbf] = 1; OPLEN[0xc0] = 3; OPLEN[0xc1] = 3; OPLEN[0xc2] = 1; OPLEN[0xc3] = 1
OPLEN[0xc5] = 4; OPLEN[0xc6] = 3; OPLEN[0xc7] = 3; OPLEN[0xc8] = 5; OPLEN[0xc9] = 5


class CF:
    pass


def parse(path):
    data = open(path, 'rb').read()
    assert data[:4] == b'\xca\xfe\xba\xbe', path
    c = CF()
    c.path = path
    c.minor, c.major = struct.unpack_from('>HH', data, 4)
    (count,) = struct.unpack_from('>H', data, 8)
    pool = [None] * count
    pos, i = 10, 1
    while i < count:
        tag = data[pos]; pos += 1
        if tag == 1:
            (n,) = struct.unpack_from('>H', data, pos)
            raw = data[pos + 2:pos + 2 + n]
            try:
                s = raw.decode('utf-8')
            except UnicodeDecodeError:
                s = raw.decode('utf-8', 'replace')
            pool[i] = ('utf8', s); pos += 2 + n
        elif tag == 3:
            pool[i] = ('int', struct.unpack_from('>i', data, pos)[0]); pos += 4
        elif tag == 4:
            pool[i] = ('float', None); pos += 4
        elif tag == 5:
            pool[i] = ('long', struct.unpack_from('>q', data, pos)[0]); pos += 8; i += 1
        elif tag == 6:
            pool[i] = ('double', None); pos += 8; i += 1
        elif tag == 7:
            pool[i] = ('class', struct.unpack_from('>H', data, pos)[0]); pos += 2
        elif tag == 8:
            pool[i] = ('string', struct.unpack_from('>H', data, pos)[0]); pos += 2
        elif tag in (9, 10, 11):
            a, b = struct.unpack_from('>HH', data, pos)
            pool[i] = ({9: 'field', 10: 'method', 11: 'imethod'}[tag], a, b); pos += 4
        elif tag == 12:
            a, b = struct.unpack_from('>HH', data, pos)
            pool[i] = ('nat', a, b); pos += 4
        elif tag == 15:
            k = data[pos]; (r,) = struct.unpack_from('>H', data, pos + 1)
            pool[i] = ('mh', k, r); pos += 3
        elif tag == 16:
            pool[i] = ('mt', struct.unpack_from('>H', data, pos)[0]); pos += 2
        elif tag in (17, 18):
            a, b = struct.unpack_from('>HH', data, pos)
            pool[i] = ('dyn' if tag == 17 else 'indy', a, b); pos += 4
        elif tag in (19, 20):
            pos += 2
        else:
            raise ValueError('bad tag %d' % tag)
        i += 1
    c.pool = pool

    def utf(ix):
        return pool[ix][1]

    def cls(ix):
        return utf(pool[ix][1]) if ix else None

    c.utf, c.cls = utf, cls
    c.access, this_i, super_i = struct.unpack_from('>HHH', data, pos); pos += 6
    c.name, c.super = cls(this_i), cls(super_i)
    (ni,) = struct.unpack_from('>H', data, pos); pos += 2
    c.interfaces = [cls(struct.unpack_from('>H', data, pos + 2 * k)[0]) for k in range(ni)]
    pos += 2 * ni

    def attrs(p):
        (n,) = struct.unpack_from('>H', data, p); p += 2
        out = []
        for _ in range(n):
            ni_, ln = struct.unpack_from('>HI', data, p)
            out.append((utf(ni_), data[p + 6:p + 6 + ln]))
            p += 6 + ln
        return p, out

    def members(p):
        (n,) = struct.unpack_from('>H', data, p); p += 2
        out = []
        for _ in range(n):
            acc, nm, ds = struct.unpack_from('>HHH', data, p); p += 6
            p, at = attrs(p)
            out.append((acc, utf(nm), utf(ds), at))
        return p, out

    pos, c.fields = members(pos)
    pos, c.methods = members(pos)
    pos, c.attrs = attrs(pos)
    return c


def annotations(c, attrs):
    """Return list of (visibility, type descriptor) for RuntimeVisible/InvisibleAnnotations."""
    out = []
    for nm, b in attrs:
        if nm not in ('RuntimeVisibleAnnotations', 'RuntimeInvisibleAnnotations'):
            continue
        p = [0]

        def u1():
            v = b[p[0]]; p[0] += 1; return v

        def u2():
            v = struct.unpack_from('>H', b, p[0])[0]; p[0] += 2; return v

        def ev():
            t = chr(u1())
            if t in 'BCDFIJSZsc':
                u2()
            elif t == 'e':
                u2(); u2()
            elif t == '@':
                ann()
            elif t == '[':
                for _ in range(u2()):
                    ev()

        def ann():
            ti = u2()
            for _ in range(u2()):
                u2(); ev()
            return c.utf(ti)

        for _ in range(u2()):
            out.append((nm, ann()))
    return out


def code_of(c, mattrs):
    for nm, b in mattrs:
        if nm == 'Code':
            ms, ml, cl = struct.unpack_from('>HHI', b, 0)
            code = b[8:8 + cl]
            p = 8 + cl
            (el,) = struct.unpack_from('>H', b, p); p += 2 + 8 * el
            (na,) = struct.unpack_from('>H', b, p); p += 2
            sub = []
            for _ in range(na):
                ni_, ln = struct.unpack_from('>HI', b, p)
                sub.append((c.utf(ni_), b[p + 6:p + 6 + ln])); p += 6 + ln
            return code, sub, el
    return None, [], 0


def walk(code):
    """Yield (pc, opcode, operand bytes) for every instruction."""
    pc, n = 0, len(code)
    while pc < n:
        op = code[pc]
        if op == 0xaa:
            q = pc + 1 + ((4 - (pc + 1) % 4) % 4)
            d, lo, hi = struct.unpack_from('>iii', code, q)
            ln = (q - pc) + 12 + 4 * (hi - lo + 1)
        elif op == 0xab:
            q = pc + 1 + ((4 - (pc + 1) % 4) % 4)
            d, npairs = struct.unpack_from('>ii', code, q)
            ln = (q - pc) + 8 + 8 * npairs
        elif op == 0xc4:
            ln = 6 if code[pc + 1] == 0x84 else 4
        else:
            ln = OPLEN.get(op)
            if ln is None:
                raise ValueError('bad opcode 0x%02x at %d' % (op, pc))
        yield pc, op, code[pc + 1:pc + ln]
        pc += ln
    if pc != n:
        raise ValueError('code length mismatch')


def ref(c, ix):
    """Resolve a Fieldref/Methodref/InterfaceMethodref -> (owner, name, desc)."""
    e = c.pool[ix]
    owner = c.cls(e[1])
    nat = c.pool[e[2]]
    return owner, c.utf(nat[1]), c.utf(nat[2])


def bootstrap_methods(c):
    for nm, b in c.attrs:
        if nm == 'BootstrapMethods':
            (n,) = struct.unpack_from('>H', b, 0)
            p, out = 2, []
            for _ in range(n):
                mh, na = struct.unpack_from('>HH', b, p); p += 4
                args = list(struct.unpack_from('>%dH' % na, b, p)); p += 2 * na
                out.append((mh, args))
            return out
    return []


def mh_target(c, ix):
    e = c.pool[ix]
    assert e[0] == 'mh'
    return e[1], ref(c, e[2])


def class_files(root):
    for dp, dn, fn in os.walk(root):
        dn.sort()
        for f in sorted(fn):
            if f.endswith('.class'):
                yield os.path.join(dp, f)
