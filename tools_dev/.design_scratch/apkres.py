"""Scratch: resources.arsc id->name map and binary AndroidManifest.xml decoding, stdlib only."""
import struct
import sys
import zipfile


def string_pool(b, off):
    typ, hsz, size = struct.unpack_from('<HHI', b, off)
    count, scount, flags, sstart, stystart = struct.unpack_from('<IIIII', b, off + 8)
    utf8 = bool(flags & 0x100)
    offs = struct.unpack_from('<%dI' % count, b, off + hsz)
    base = off + sstart
    out = []
    for o in offs:
        p = base + o
        if utf8:
            n = b[p]; p += 1
            if n & 0x80:
                p += 1
            ln = b[p]; p += 1
            if ln & 0x80:
                ln = ((ln & 0x7f) << 8) | b[p]; p += 1
            out.append(b[p:p + ln].decode('utf-8', 'replace'))
        else:
            ln = struct.unpack_from('<H', b, p)[0]; p += 2
            if ln & 0x8000:
                ln = ((ln & 0x7fff) << 16) | struct.unpack_from('<H', b, p)[0]; p += 2
            out.append(b[p:p + 2 * ln].decode('utf-16-le', 'replace'))
    return out, off + size


def arsc_names(data):
    typ, hsz, size, npk = struct.unpack_from('<HHII', data, 0)
    off = hsz
    names = {}
    gpool = None
    while off < len(data):
        ctype, chsz, csize = struct.unpack_from('<HHI', data, off)
        if ctype == 0x0001:
            gpool, _ = string_pool(data, off)
        elif ctype == 0x0200:
            pid = struct.unpack_from('<I', data, off + 8)[0]
            pname = data[off + 12:off + 12 + 256].decode('utf-16-le').split('\x00')[0]
            type_str_off, last_pub_type, key_str_off = struct.unpack_from('<III', data, off + 268)
            types, _ = string_pool(data, off + type_str_off)
            keys, _ = string_pool(data, off + key_str_off)
            p = off + chsz
            end = off + csize
            while p < end:
                t2, h2, s2 = struct.unpack_from('<HHI', data, p)
                if t2 == 0x0201:
                    tid, flags = data[p + 8], data[p + 9]
                    ecount, estart = struct.unpack_from('<II', data, p + 12)
                    idx_base = p + h2
                    for i in range(ecount):
                        if flags & 0x01:  # sparse
                            idx, eoff = struct.unpack_from('<HH', data, idx_base + 4 * i)
                            eoff *= 4
                        elif flags & 0x02:  # offset16
                            eoff = struct.unpack_from('<H', data, idx_base + 2 * i)[0]
                            if eoff == 0xffff:
                                continue
                            eoff *= 4; idx = i
                        else:
                            eoff = struct.unpack_from('<I', data, idx_base + 4 * i)[0]
                            if eoff == 0xffffffff:
                                continue
                            idx = i
                        e = p + estart + eoff
                        esz, eflags, ekey = struct.unpack_from('<HHI', data, e)
                        rid = (pid << 24) | (tid << 16) | idx
                        names[rid] = (types[tid - 1], keys[ekey])
                p += s2
        off += csize
    return names


def axml(data):
    """Yield ('start', line, name, {attr: value}) / ('end', line, name)."""
    typ, hsz, size = struct.unpack_from('<HHI', data, 0)
    off = hsz
    strings = []
    resmap = []
    out = []
    while off < len(data):
        ctype, chsz, csize = struct.unpack_from('<HHI', data, off)
        if ctype == 0x0001:
            strings, _ = string_pool(data, off)
        elif ctype == 0x0180:
            n = (csize - chsz) // 4
            resmap = list(struct.unpack_from('<%dI' % n, data, off + chsz))
        elif ctype == 0x0102:
            line = struct.unpack_from('<I', data, off + 8)[0]
            ns, name, aoff, asz, acount = struct.unpack_from('<iiHHH', data, off + 16)
            attrs = {}
            a = off + 16 + aoff
            for i in range(acount):
                ans, aname, araw, vsize, vres0, vtype, vdata = struct.unpack_from('<iiiHBBI', data, a + i * asz)
                key = strings[aname] if aname >= 0 else '?'
                if vtype == 0x03:
                    val = strings[vdata] if vdata < len(strings) else vdata
                elif vtype == 0x01:
                    val = '@0x%08x' % vdata
                elif vtype == 0x12:
                    val = vdata != 0
                else:
                    val = strings[araw] if araw >= 0 else vdata
                attrs[key] = val
            out.append(('start', line, strings[name], attrs))
        elif ctype == 0x0103:
            line = struct.unpack_from('<I', data, off + 8)[0]
            ns, name = struct.unpack_from('<ii', data, off + 16)
            out.append(('end', line, strings[name]))
        off += csize
    return out


if __name__ == '__main__':
    z = zipfile.ZipFile(sys.argv[1])
    names = arsc_names(z.read('resources.arsc'))
    print('arsc entries', len(names), 'pkgs', sorted({hex(k >> 24) for k in names}))
    import collections
    print(collections.Counter(t for t, n in names.values()).most_common(12))
    for want in sys.argv[2:]:
        print(want, names.get(int(want, 16)))
    ev = axml(z.read('AndroidManifest.xml'))
    for e in ev:
        if e[0] == 'start' and e[2] in ('activity', 'activity-alias', 'service', 'receiver', 'provider', 'application', 'action', 'category'):
            a = e[3]
            print(e[1], e[2], a.get('name'), {k: v for k, v in a.items() if k in ('exported', 'theme', 'launchMode', 'targetActivity', 'enabled', 'process')})
