import os, struct, json, sys
# Reads class-file headers (no javap available) and writes scratch/hier.json:
#   { "net/gsantner/markor/X$Y": {"super": "...", "ifaces": [...], "flags": int} }
# from the test-flavor compiled classes that Gradle left in app/build.
BASE = ('/Users/darshan/Desktop/yang/final_java_only/Markor/app/Markor-#v2.16.1/app/build/'
        'intermediates/javac/flavorAtestDebug/compileFlavorAtestDebugJavaWithJavac/classes')
OUT = '/Users/darshan/Desktop/yang/work/graphs/Markor/scratch/hier.json'


def parse(path):
    data = open(path, 'rb').read()
    pos = 8
    (cp_count,) = struct.unpack('>H', data[pos:pos + 2])
    pos += 2
    utf = {}
    cls = {}
    i = 1
    while i < cp_count:
        tag = data[pos]
        pos += 1
        if tag == 1:
            (ln,) = struct.unpack('>H', data[pos:pos + 2])
            utf[i] = data[pos + 2:pos + 2 + ln].decode('utf-8', 'replace')
            pos += 2 + ln
        elif tag == 7:
            (ni,) = struct.unpack('>H', data[pos:pos + 2])
            cls[i] = ni
            pos += 2
        elif tag in (8, 16, 19, 20):
            pos += 2
        elif tag in (3, 4, 9, 10, 11, 12, 17, 18):
            pos += 4
        elif tag == 15:
            pos += 3
        elif tag in (5, 6):
            pos += 8
            i += 1
        else:
            raise ValueError('bad tag %d in %s' % (tag, path))
        i += 1
    flags, this_i, super_i, n_if = struct.unpack('>HHHH', data[pos:pos + 8])
    pos += 8
    ifaces = []
    for _ in range(n_if):
        (ii,) = struct.unpack('>H', data[pos:pos + 2])
        ifaces.append(utf[cls[ii]])
        pos += 2
    sup = utf[cls[super_i]] if super_i else None
    return utf[cls[this_i]], {'super': sup, 'ifaces': ifaces, 'flags': flags}


res = {}
for d, _, fs in os.walk(BASE):
    for f in fs:
        if f.endswith('.class'):
            try:
                name, info = parse(os.path.join(d, f))
                res[name] = info
            except Exception as ex:
                print('skip', f, ex, file=sys.stderr)
json.dump(res, open(OUT, 'w'), indent=0, sort_keys=True)
print('classes', len(res))
print('Markor classes', sum(1 for k in res if k.startswith('net/gsantner/markor/')))
