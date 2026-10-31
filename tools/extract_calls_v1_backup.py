"""Extract direct call edges between app methods from compiled .class files.

Usage: python3 -I extract_calls.py <graph_dir> <classes_dir> [<classes_dir> ...]

Reads <graph_dir>/method_list.json (the method universe) and writes
<graph_dir>/auto_calls.json:
  calls:   [{src, dst, line, file, via, dispatch}]  app method -> app method
  lambdas: [{src, dst, line, file}]                 a lambda / method reference is created in src
                                                    (dst is its body; usually a REGISTER candidate)
  framework_calls: {src: [owner.name, ...]}         framework methods each app method calls (for modelling)

Resolution:
- invokestatic / invokespecial: the declared method, or the nearest app superclass that declares it.
- invokevirtual / invokeinterface on an app type: the resolved method plus every override in app
  subclasses / implementors (class hierarchy analysis); edges added only by CHA have dispatch='cha'.
- Calls through methods outside the universe (synthetic accessors, generated code such as Dagger,
  bridges) are collapsed: the edge goes from the universe caller to the universe callee, and `via`
  names the skipped methods.
Line numbers come from the LineNumberTable, file names from the SourceFile attribute.
"""
import collections
import json
import os
import struct
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_graph import method_names  # noqa: E402

INVOKES = {0xb6: 'virtual', 0xb7: 'special', 0xb8: 'static', 0xb9: 'interface', 0xba: 'dynamic'}
# opcode -> operand byte count (fixed-size instructions); tableswitch/lookupswitch/wide handled apart
OPLEN = {}
for op in list(range(0x00, 0x10)) + list(range(0x1a, 0x36)) + list(range(0x3b, 0x84)) + list(range(0x85, 0x99)) + \
        list(range(0xac, 0xb2)) + [0xbe, 0xbf, 0xc2, 0xc3]:
    OPLEN[op] = 0
for op in [0x10, 0x12, 0x15, 0x16, 0x17, 0x18, 0x19, 0x36, 0x37, 0x38, 0x39, 0x3a, 0xa9, 0xbc]:
    OPLEN[op] = 1
for op in [0x11, 0x13, 0x14, 0x84, 0xb2, 0xb3, 0xb4, 0xb5, 0xb6, 0xb7, 0xb8, 0xbb, 0xbd, 0xc0, 0xc1, 0xc6, 0xc7] + \
        list(range(0x99, 0xa9)):
    OPLEN[op] = 2
OPLEN[0xc5] = 3
for op in [0xb9, 0xba, 0xc8, 0xc9]:
    OPLEN[op] = 4


class ClassInfo:
    pass


def parse_class(path):
    d = open(path, 'rb').read()
    (count,) = struct.unpack_from('>H', d, 8)
    pool, pos, i = [None] * count, 10, 1
    while i < count:
        tag = d[pos]
        pos += 1
        if tag == 1:
            (n,) = struct.unpack_from('>H', d, pos)
            pool[i] = ('utf', d[pos + 2:pos + 2 + n].decode('utf-8', 'replace'))
            pos += 2 + n
        elif tag in (3, 4):
            pos += 4
        elif tag in (5, 6):
            pos += 8
            i += 1
        elif tag in (7, 8, 16, 19, 20):
            pool[i] = (tag, struct.unpack_from('>H', d, pos)[0])
            pos += 2
        elif tag in (9, 10, 11, 12, 17, 18):
            pool[i] = (tag,) + struct.unpack_from('>HH', d, pos)
            pos += 4
        elif tag == 15:
            pool[i] = (15, d[pos]) + struct.unpack_from('>H', d, pos + 1)
            pos += 3
        else:
            raise ValueError('bad tag %d in %s' % (tag, path))
        i += 1
    utf = lambda k: pool[k][1]
    cname = lambda k: utf(pool[k][1])

    def ref(k):  # Methodref / InterfaceMethodref -> (owner, name, desc)
        _, ci, nti = pool[k]
        _, ni, di = pool[nti]
        return cname(ci), utf(ni), utf(di)

    ci = ClassInfo()
    ci.access, this_i, super_i = struct.unpack_from('>HHH', d, pos)
    pos += 6
    ci.name = cname(this_i)
    ci.super = cname(super_i) if super_i else None
    (ni,) = struct.unpack_from('>H', d, pos)
    ci.interfaces = [cname(struct.unpack_from('>H', d, pos + 2 + 2 * j)[0]) for j in range(ni)]
    pos += 2 + 2 * ni

    def attrs(p):
        (n,) = struct.unpack_from('>H', d, p)
        p += 2
        out = []
        for _ in range(n):
            ai, alen = struct.unpack_from('>HI', d, p)
            out.append((utf(ai), p + 6, alen))
            p += 6 + alen
        return p, out

    (nf,) = struct.unpack_from('>H', d, pos)
    pos += 2
    for _ in range(nf):
        pos, _a = attrs(pos + 6)
    (nm,) = struct.unpack_from('>H', d, pos)
    pos += 2
    raw_methods = []
    for _ in range(nm):
        acc, mni, mdi = struct.unpack_from('>HHH', d, pos)
        pos, ma = attrs(pos + 6)
        raw_methods.append((acc, utf(mni), utf(mdi), ma))
    pos, ca = attrs(pos)
    ci.source = None
    bootstrap = []
    for an, ap, alen in ca:
        if an == 'SourceFile':
            ci.source = utf(struct.unpack_from('>H', d, ap)[0])
        elif an == 'BootstrapMethods':
            (nb,) = struct.unpack_from('>H', d, ap)
            p = ap + 2
            for _ in range(nb):
                mh, na = struct.unpack_from('>HH', d, p)
                args = [struct.unpack_from('>H', d, p + 4 + 2 * j)[0] for j in range(na)]
                bootstrap.append((mh, args))
                p += 4 + 2 * na

    def lambda_impl(bsm_index):
        """For a LambdaMetafactory bootstrap, return the (owner, name, desc) of the implementation."""
        mh, args = bootstrap[bsm_index]
        _, _kind, r = pool[mh]
        if ref(r)[1] not in ('metafactory', 'altMetafactory'):
            return None
        for a in args:
            if pool[a] and pool[a][0] == 15:
                return ref(pool[a][2])
        return None

    ci.methods = {}
    for acc, name, desc, ma in raw_methods:
        m = {'access': acc, 'name': name, 'desc': desc, 'calls': [], 'lambdas': []}
        for an, ap, alen in ma:
            if an != 'Code':
                continue
            (clen,) = struct.unpack_from('>I', d, ap + 4)
            code = d[ap + 8:ap + 8 + clen]
            lines = []
            p2 = ap + 8 + clen
            (exl,) = struct.unpack_from('>H', d, p2)
            p2 += 2 + 8 * exl
            _p, cattrs = attrs(p2)
            for can, cap, calen in cattrs:
                if can == 'LineNumberTable':
                    (nl,) = struct.unpack_from('>H', d, cap)
                    lines += [struct.unpack_from('>HH', d, cap + 2 + 4 * j) for j in range(nl)]
            lines.sort()

            def line_at(off):
                ln = None
                for start, l in lines:
                    if start > off:
                        break
                    ln = l
                return ln

            pc = 0
            while pc < len(code):
                op = code[pc]
                if op in INVOKES:
                    (k,) = struct.unpack_from('>H', code, pc + 1)
                    if op == 0xba:
                        _, bsi, nti = pool[k]
                        impl = lambda_impl(bsi)
                        if impl:
                            m['lambdas'].append((impl, line_at(pc)))
                    else:
                        m['calls'].append((INVOKES[op], ref(k), line_at(pc)))
                if op == 0xaa:  # tableswitch
                    p = pc + 1 + (3 - pc % 4)
                    low, high = struct.unpack_from('>ii', code, p + 4)
                    pc = p + 12 + 4 * (high - low + 1)
                elif op == 0xab:  # lookupswitch
                    p = pc + 1 + (3 - pc % 4)
                    (npairs,) = struct.unpack_from('>i', code, p + 4)
                    pc = p + 8 + 8 * npairs
                elif op == 0xc4:  # wide
                    pc += 6 if code[pc + 1] == 0x84 else 4
                else:
                    if op not in OPLEN:
                        raise ValueError('unknown opcode 0x%02x in %s.%s' % (op, ci.name, name))
                    pc += 1 + OPLEN[op]
        ci.methods[(name, desc)] = m
    return ci


def main(argv):
    gdir, cdirs = argv[1], argv[2:]
    classes = {}
    for cdir in cdirs:
        for dp, _ds, fs in os.walk(cdir):
            for f in fs:
                if f.endswith('.class'):
                    ci = parse_class(os.path.join(dp, f))
                    classes[ci.name] = ci
    rows = json.load(open(os.path.join(gdir, 'method_list.json')))
    names, by_name = method_names(rows)
    uname = {}  # (class, name, desc) -> universe node name
    for n in names:
        r = by_name[n]
        uname[(r['class'], r['name'], r['desc'])] = n

    subs = collections.defaultdict(set)  # class -> direct app subtypes
    for c in classes.values():
        for s in [c.super] + c.interfaces:
            if s in classes:
                subs[s].add(c.name)

    def declared_up(owner, name, desc):
        c = owner
        while c in classes:
            if (name, desc) in classes[c].methods:
                return c
            c = classes[c].super
        for c2 in [owner] + list(all_supers(owner)):  # default/interface methods
            if c2 in classes and (name, desc) in classes[c2].methods:
                return c2
        return None

    def all_supers(c):
        seen, stack = set(), [c]
        while stack:
            x = stack.pop()
            if x not in classes:
                continue
            for s in [classes[x].super] + classes[x].interfaces:
                if s and s not in seen:
                    seen.add(s)
                    stack.append(s)
        return seen

    def all_subs(c):
        seen, stack = set(), [c]
        while stack:
            for s in subs.get(stack.pop(), ()):
                if s not in seen:
                    seen.add(s)
                    stack.append(s)
        return seen

    def targets(kind, owner, name, desc):
        """App methods an invoke can reach: [(class, dispatch)]"""
        if owner not in classes:
            return []
        out = []
        decl = declared_up(owner, name, desc)
        if decl and classes[decl].methods[(name, desc)]['access'] & 0x0400 == 0:
            out.append((decl, 'exact'))
        if kind in ('virtual', 'interface') and name != '<init>':
            for s in all_subs(owner):
                if (name, desc) in classes[s].methods and classes[s].methods[(name, desc)]['access'] & 0x0400 == 0:
                    out.append((s, 'cha'))
        return out

    # raw edges between all app methods (universe or not)
    raw = collections.defaultdict(list)  # (cls, name, desc) -> [(callee key, line, dispatch)]
    lambdas = []
    fw = collections.defaultdict(set)
    for c in classes.values():
        for (mn, md), m in c.methods.items():
            key = (c.name, mn, md)
            for kind, (owner, name, desc), line in m['calls']:
                ts = targets(kind, owner, name, desc)
                if not ts and owner not in classes:
                    fw[key].add('%s.%s' % (owner.rsplit('/', 1)[-1], name))
                for tc, disp in ts:
                    raw[key].append(((tc, name, desc), line, disp))
            for (owner, name, desc), line in m['lambdas']:
                lambdas.append((key, (owner, name, desc), line, c.source))

    def short_key(k):
        return '%s.%s' % (k[0].rsplit('/', 1)[-1], k[1])

    calls, seen = [], set()
    for c in classes.values():
        for (mn, md) in c.methods:
            key = (c.name, mn, md)
            if key not in uname:
                continue
            # walk through non-universe methods
            stack = [(t, line, disp, []) for t, line, disp in raw.get(key, [])]
            visited = set()
            while stack:
                t, line, disp, via = stack.pop()
                if t in uname:
                    sig = (uname[key], uname[t])
                    if sig not in seen:
                        seen.add(sig)
                        calls.append({'src': uname[key], 'dst': uname[t], 'file': c.source, 'line': line,
                                      'dispatch': disp, 'via': [short_key(v) for v in via]})
                    continue
                if t in visited or len(via) > 6:
                    continue
                visited.add(t)
                for t2, _l2, d2 in raw.get(t, []):
                    stack.append((t2, line, 'cha' if 'cha' in (disp, d2) else 'exact', via + [t]))

    lam_out = []
    for src, impl, line, srcfile in lambdas:
        if src in uname and impl in uname:
            lam_out.append({'src': uname[src], 'dst': uname[impl], 'file': srcfile, 'line': line})
    fw_out = {uname[k]: sorted(v) for k, v in fw.items() if k in uname}
    out = {'calls': calls, 'lambdas': lam_out, 'framework_calls': fw_out}
    with open(os.path.join(gdir, 'auto_calls.json'), 'w') as f:
        json.dump(out, f, indent=1)
    print('classes %d | universe methods %d | call edges %d (exact %d, cha-only %d, via skipped code %d) | lambda creations %d'
          % (len(classes), len(names), len(calls), sum(1 for x in calls if x['dispatch'] == 'exact'),
             sum(1 for x in calls if x['dispatch'] == 'cha'), sum(1 for x in calls if x['via']), len(lam_out)))


if __name__ == '__main__':
    main(sys.argv)
