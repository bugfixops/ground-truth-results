"""Scratch: CFG + abstract stack/locals interpretation prototype; consumer stats for lambdas/anon classes/res ids."""
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
TOP = ('TOP',)
UNK = frozenset([('?',)])


def arg_slots(desc):
    """List of slot sizes for args, return size."""
    args, i, out = desc[1:desc.index(')')], 0, []
    while i < len(args):
        ch = args[i]
        if ch == '[':
            while args[i] == '[':
                i += 1
            if args[i] == 'L':
                i = args.index(';', i)
            i += 1
            out.append(1)
        elif ch == 'L':
            i = args.index(';', i) + 1; out.append(1)
        else:
            out.append(2 if ch in 'JD' else 1); i += 1
    r = desc[desc.index(')') + 1:]
    return out, (0 if r == 'V' else 2 if r in ('J', 'D') else 1)


CAT2_LOAD = {0x16, 0x18, 0x1e, 0x1f, 0x20, 0x21, 0x26, 0x27, 0x28, 0x29}
# simple stack effects for ops not handled specially: (pop slots, push slots)
SIMPLE = {}
for op in range(0x2e, 0x36):  # array loads
    SIMPLE[op] = (2, 2 if op in (0x2f, 0x31) else 1)
for op in range(0x4f, 0x57):
    SIMPLE[op] = (4 if op in (0x50, 0x52) else 3, 0)
ARITH = {0x60: (2, 1), 0x61: (4, 2), 0x62: (2, 1), 0x63: (4, 2), 0x64: (2, 1), 0x65: (4, 2), 0x66: (2, 1), 0x67: (4, 2),
         0x68: (2, 1), 0x69: (4, 2), 0x6a: (2, 1), 0x6b: (4, 2), 0x6c: (2, 1), 0x6d: (4, 2), 0x6e: (2, 1), 0x6f: (4, 2),
         0x70: (2, 1), 0x71: (4, 2), 0x72: (2, 1), 0x73: (4, 2), 0x74: (1, 1), 0x75: (2, 2), 0x76: (1, 1), 0x77: (2, 2),
         0x78: (2, 1), 0x79: (3, 2), 0x7a: (2, 1), 0x7b: (3, 2), 0x7c: (2, 1), 0x7d: (3, 2), 0x7e: (2, 1), 0x7f: (4, 2),
         0x80: (2, 1), 0x81: (4, 2), 0x82: (2, 1), 0x83: (4, 2),
         0x85: (1, 2), 0x86: (1, 1), 0x87: (1, 2), 0x88: (2, 1), 0x89: (2, 1), 0x8a: (2, 2), 0x8b: (1, 1), 0x8c: (1, 2),
         0x8d: (1, 2), 0x8e: (2, 1), 0x8f: (2, 2), 0x90: (2, 1), 0x91: (1, 1), 0x92: (1, 1), 0x93: (1, 1),
         0x94: (4, 1), 0x95: (2, 1), 0x96: (2, 1), 0x97: (4, 1), 0x98: (4, 1)}
SIMPLE.update(ARITH)


def push(st, toks, size):
    st.append(frozenset(toks))
    if size == 2:
        st.append(frozenset([TOP]))


def analyze_method(c, mname, mdesc, acc, code, etab, on_invoke, on_put, on_indy):
    insns = list(cf.walk(code))
    index = {pc: k for k, (pc, op, opnd) in enumerate(insns)}
    handlers = [(s, e, h) for s, e, h, t in etab]
    states = {}
    # initial locals
    locals0 = {}
    slot = 0
    if not acc & 0x0008:
        locals0[0] = frozenset([('this',)]); slot = 1
    sizes, _ = arg_slots(mdesc)
    for i, s in enumerate(sizes):
        locals0[slot] = frozenset([('param', i)]); slot += s
    work = [(0, (), locals0)]
    seen_pc = collections.Counter()

    def merge(pc, st, lo):
        old = states.get(pc)
        if old is None:
            states[pc] = (st, lo); return True
        ost, olo = old
        if len(ost) != len(st):
            return False
        nst = tuple(a | b if len(a | b) <= 16 else UNK for a, b in zip(ost, st))
        nlo = dict(olo)
        changed = nst != ost
        for k in set(olo) | set(lo):
            v = olo.get(k, UNK) | lo.get(k, UNK)
            if len(v) > 16:
                v = UNK
            if nlo.get(k) != v:
                nlo[k] = v; changed = True
        if changed:
            states[pc] = (nst, nlo)
        return changed

    merge(0, (), locals0)
    work = [0]
    reported = set()
    while work:
        pc0 = work.pop()
        seen_pc[pc0] += 1
        if seen_pc[pc0] > 50:
            continue
        st, lo = states[pc0]
        st = list(st); lo = dict(lo)
        k = index[pc0]
        while True:
            pc, op, opnd = insns[k]
            nxt = []
            fall = True
            # exception handlers covering pc
            for s, e, h in handlers:
                if s <= pc < e:
                    if merge(h, (frozenset([('exc',)]),), lo):
                        work.append(h)
            def pop(n):
                out = []
                for _ in range(n):
                    out.append(st.pop() if st else UNK)
                return out
            if op <= 0x0f:
                if op == 0x01:
                    push(st, [('null',)], 1)
                elif 0x02 <= op <= 0x08:
                    push(st, [('int', op - 3)], 1)
                elif op in (0x09, 0x0a, 0x0e, 0x0f):
                    push(st, [('num',)], 2)
                elif op in (0x0b, 0x0c, 0x0d):
                    push(st, [('num',)], 1)
            elif op == 0x10:
                push(st, [('int', struct.unpack('>b', opnd[:1])[0])], 1)
            elif op == 0x11:
                push(st, [('int', struct.unpack('>h', opnd[:2])[0])], 1)
            elif op in (0x12, 0x13, 0x14):
                ix = opnd[0] if op == 0x12 else struct.unpack('>H', opnd[:2])[0]
                e = c.pool[ix]
                if e[0] == 'int':
                    push(st, [('int', e[1])], 1)
                elif e[0] == 'string':
                    push(st, [('str', c.utf(e[1]))], 1)
                elif e[0] == 'class':
                    push(st, [('class', c.utf(e[1]))], 1)
                elif e[0] in ('long', 'double'):
                    push(st, [('num',)], 2)
                else:
                    push(st, [('num',)], 1)
            elif 0x15 <= op <= 0x19 or 0x1a <= op <= 0x2d:
                if op <= 0x19:
                    n = opnd[0]; typ = op - 0x15
                else:
                    n = (op - 0x1a) % 4; typ = (op - 0x1a) // 4
                size = 2 if typ in (1, 3) else 1
                push(st, lo.get(n, UNK), size)
            elif 0x36 <= op <= 0x3a or 0x3b <= op <= 0x4e:
                if op <= 0x3a:
                    n = opnd[0]; typ = op - 0x36
                else:
                    n = (op - 0x3b) % 4; typ = (op - 0x3b) // 4
                size = 2 if typ in (1, 3) else 1
                v = pop(size)[-1]
                lo[n] = v
                if size == 2:
                    lo[n + 1] = UNK
            elif op in SIMPLE:
                p, q = SIMPLE[op]
                pop(p)
                if q:
                    push(st, [('num',)], q)
            elif op == 0x57:
                pop(1)
            elif op == 0x58:
                pop(2)
            elif op == 0x59:
                v = st[-1] if st else UNK; st.append(v)
            elif op == 0x5a:
                a, b = pop(2); st += [a, b, a]
            elif op == 0x5b:
                a, b, c3 = pop(3); st += [a, c3, b, a]
            elif op == 0x5c:
                a, b = pop(2); st += [b, a, b, a]
            elif op == 0x5d:
                a, b, c3 = pop(3); st += [b, a, c3, b, a]
            elif op == 0x5e:
                a, b, c3, d = pop(4); st += [b, a, d, c3, b, a]
            elif op == 0x5f:
                a, b = pop(2); st += [a, b]
            elif op == 0x84:
                pass
            elif 0x99 <= op <= 0x9e or op in (0xc6, 0xc7):
                pop(1); nxt.append(pc + struct.unpack('>h', opnd[:2])[0])
            elif 0x9f <= op <= 0xa6:
                pop(2); nxt.append(pc + struct.unpack('>h', opnd[:2])[0])
            elif op in (0xa7, 0xc8):
                off = struct.unpack('>h', opnd[:2])[0] if op == 0xa7 else struct.unpack('>i', opnd[:4])[0]
                nxt.append(pc + off); fall = False
            elif op in (0xa8, 0xc9, 0xa9):
                return 'jsr'
            elif op in (0xaa, 0xab):
                pop(1)
                q = (4 - (pc + 1) % 4) % 4
                b = opnd[q:]
                if op == 0xaa:
                    d, lo_, hi = struct.unpack_from('>iii', b, 0)
                    nxt += [pc + d] + [pc + struct.unpack_from('>i', b, 12 + 4 * j)[0] for j in range(hi - lo_ + 1)]
                else:
                    d, npairs = struct.unpack_from('>ii', b, 0)
                    nxt += [pc + d] + [pc + struct.unpack_from('>i', b, 8 + 8 * j + 4)[0] for j in range(npairs)]
                fall = False
            elif 0xac <= op <= 0xb1 or op == 0xbf:
                fall = False
            elif op in (0xb2, 0xb3, 0xb4, 0xb5):
                owner, name, desc = cf.ref(c, struct.unpack('>H', opnd[:2])[0])
                size = 2 if desc in ('J', 'D') else 1
                if op == 0xb2:
                    push(st, [('field', owner, name)], size)
                elif op == 0xb3:
                    v = pop(size)[-1]; on_put(owner, name, v)
                elif op == 0xb4:
                    pop(1); push(st, [('field', owner, name)], size)
                else:
                    v = pop(size)[-1]; pop(1); on_put(owner, name, v)
            elif op in (0xb6, 0xb7, 0xb8, 0xb9):
                owner, name, desc = cf.ref(c, struct.unpack('>H', opnd[:2])[0])
                sizes, rs = arg_slots(desc)
                args = []
                for s in reversed(sizes):
                    v = pop(s)[-1]; args.append(v)
                args.reverse()
                recv = pop(1)[0] if op != 0xb8 else None
                if (pc, op) not in reported:
                    reported.add((pc, op))
                on_invoke(pc, op, owner, name, desc, recv, args)
                if rs:
                    push(st, [('ret', owner, name, desc)], rs)
            elif op == 0xba:
                ix = struct.unpack('>H', opnd[:2])[0]
                e = c.pool[ix]
                nat = c.pool[e[2]]
                iname, idesc = c.utf(nat[1]), c.utf(nat[2])
                sizes, rs = arg_slots(idesc)
                args = []
                for s in reversed(sizes):
                    args.append(pop(s)[-1])
                args.reverse()
                tok = on_indy(pc, e[1], iname, idesc, args)
                if rs:
                    push(st, [tok], rs)
            elif op == 0xbb:
                push(st, [('new', c.cls(struct.unpack('>H', opnd[:2])[0]), pc)], 1)
            elif op in (0xbc, 0xbd, 0xbe):
                pop(1); push(st, [('arr',)], 1)
            elif op == 0xc0:
                pass
            elif op == 0xc1:
                pop(1); push(st, [('num',)], 1)
            elif op in (0xc2, 0xc3):
                pop(1)
            elif op == 0xc4:
                wop = opnd[0]; n = struct.unpack('>H', opnd[1:3])[0]
                if wop in (0x15, 0x17, 0x19):
                    push(st, lo.get(n, UNK), 1)
                elif wop in (0x16, 0x18):
                    push(st, lo.get(n, UNK), 2)
                elif wop in (0x36, 0x38, 0x3a):
                    lo[n] = pop(1)[-1]
                elif wop in (0x37, 0x39):
                    pop(2); lo[n] = UNK; lo[n + 1] = UNK
                elif wop == 0xa9:
                    return 'jsr'
            elif op == 0xc5:
                dims = opnd[2]; pop(dims); push(st, [('arr',)], 1)
            else:
                pass
            for t in nxt:
                if merge(t, tuple(st), lo):
                    work.append(t)
            if not fall:
                break
            k += 1
            if k >= len(insns):
                break
            npc = insns[k][0]
            if npc in states or any(npc == t for t in nxt):
                if merge(npc, tuple(st), lo):
                    work.append(npc)
                break
    return 'ok'


def main():
    tot = collections.Counter()
    for app in APPS:
        cfj = json.load(open(os.path.join(ROOT, app, 'app/class_files.json')))
        base = os.path.join(ROOT, app, 'app')
        classes = {}
        for v in cfj.values():
            for d in v['classfiles']:
                for p in cf.class_files(os.path.join(base, d)):
                    c = cf.parse(p)
                    classes[c.name] = c
        stats = collections.Counter()
        bsm_kinds = collections.Counter()
        lam_consumer = collections.Counter()
        anon_consumer = collections.Counter()
        resid_consumer = collections.Counter()
        lam_unconsumed = collections.Counter()
        impl_kinds = collections.Counter()
        opcodes = collections.Counter()
        for c in classes.values():
            if 'JacocoInstrument' in c.name:
                continue
            bsms = cf.bootstrap_methods(c)
            for acc, name, desc, at in c.methods:
                code, sub, el = cf.code_of(c, at)
                if code is None:
                    continue
                etab = []
                for nm, b in at:
                    if nm == 'Code':
                        ms, ml, cl = struct.unpack_from('>HHI', b, 0)
                        p = 8 + cl
                        (n,) = struct.unpack_from('>H', b, p); p += 2
                        for j in range(n):
                            etab.append(struct.unpack_from('>HHHH', b, p + 8 * j))
                stats['methods'] += 1
                if any(nm == 'LineNumberTable' for nm, _ in sub):
                    stats['with LNT'] += 1
                for pc, op, opnd in cf.walk(code):
                    opcodes[op] += 1
                lam_tokens = {}
                consumed = set()

                def on_indy(pc, bsm_ix, iname, idesc, args):
                    mh, bargs = bsms[bsm_ix]
                    kind, (o, n, d) = cf.mh_target(c, mh)
                    bsm_kinds['%s.%s' % (o.rsplit('/', 1)[-1], n)] += 1
                    if o == 'java/lang/invoke/LambdaMetafactory':
                        ik, (io, inn, idd) = cf.mh_target(c, bargs[1])
                        impl_kinds[('lambda$' if inn.startswith('lambda$') else 'methodref', ik)] += 1
                        t = ('lambda', c.name, pc, idesc[idesc.index(')') + 1:], iname)
                        lam_tokens[t] = True
                        return t
                    return ('indy', n)

                def on_invoke(pc, op, owner, name, desc, recv, args):
                    allv = list(args) + ([recv] if recv is not None else [])
                    for i, a in enumerate(args):
                        for t in a:
                            if t[0] == 'lambda':
                                consumed.add(t)
                                lam_consumer[(owner.rsplit('/', 1)[-1] + '.' + name, t[3].rsplit('/', 1)[-1][:-1])] += 1
                            elif t[0] == 'new' and t[1] in classes and '$' in t[1] and name != '<init>':
                                cc = classes[t[1]]
                                anon_consumer[(owner.rsplit('/', 1)[-1] + '.' + name)] += 1
                            elif t[0] == 'int' and isinstance(t[1], int) and (t[1] >> 24) & 0xff == 0x7f:
                                resid_consumer[owner.rsplit('/', 1)[-1] + '.' + name] += 1
                    if recv is not None:
                        for t in recv:
                            if t[0] == 'lambda':
                                consumed.add(t)
                                lam_consumer[('<recv>' + owner.rsplit('/', 1)[-1] + '.' + name, t[3].rsplit('/', 1)[-1][:-1])] += 1

                def on_put(owner, name, v):
                    for t in v:
                        if t[0] == 'lambda':
                            consumed.add(t)
                            lam_consumer[('<field>', t[3].rsplit('/', 1)[-1][:-1])] += 1

                r = analyze_method(c, name, desc, acc, code, etab, on_invoke, on_put, on_indy)
                stats['analysis ' + r] += 1
                for t in lam_tokens:
                    if t not in consumed:
                        lam_unconsumed[t[3]] += 1
        print('== %s' % app, dict(stats))
        print('   bsm:', dict(bsm_kinds))
        print('   impl kinds:', dict(impl_kinds))
        print('   opcodes of note:', {hex(k): opcodes[k] for k in (0xaa, 0xab, 0xc4, 0xc5, 0xb9, 0xba, 0x13, 0x14, 0xa8, 0xa9) if opcodes[k]})
        print('   lambda consumers:', lam_consumer.most_common(40))
        print('   lambda unconsumed:', lam_unconsumed.most_common(10))
        print('   anon-class consumers:', anon_consumer.most_common(30))
        print('   res-id consumers:', resid_consumer.most_common(25))
        sys.stdout.flush()


main()
