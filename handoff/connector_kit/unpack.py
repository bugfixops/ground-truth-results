"""Rebuild a working tree from the bundle parts in handoff/workspace_bundle/ (standard library only).

Usage: python3 -I unpack.py <bundle_dir> <target_dir> [bundle ...]
  <bundle_dir>  local folder holding MANIFEST.json and the <bundle>/<bundle>.partNNN.txt files, fetched
                byte for byte from branch work-2026-10-31, handoff/workspace_bundle/
  <target_dir>  where the repo-relative files are written (use your working copy root)
  bundle ...    optional: only these bundles (default: all in the manifest)

Every part, every whole bundle and every file is checked against its SHA-256. Any mismatch stops the run
with the name of the bad part or file: fetch that part again, then rerun.
"""
import base64
import hashlib
import json
import os
import sys


def main(argv):
    bdir, target = argv[1], argv[2]
    man = json.load(open(os.path.join(bdir, 'MANIFEST.json')))
    names = argv[3:] or list(man['bundles'])
    total = 0
    for name in names:
        b = man['bundles'][name]
        blob = bytearray()
        for p in b['parts']:
            path = os.path.join(bdir, p['file'])
            if not os.path.isfile(path):
                raise SystemExit('MISSING part %s' % p['file'])
            data = open(path, 'rb').read()
            if len(data) != p['bytes'] or hashlib.sha256(data).hexdigest() != p['sha256']:
                raise SystemExit('BAD part %s (size %d, expected %d): fetch it again' % (p['file'], len(data), p['bytes']))
            blob += data
        if hashlib.sha256(bytes(blob)).hexdigest() != b['sha256']:
            raise SystemExit('BAD bundle %s after joining its parts' % name)
        pos = blob.index(b'\n') + 1
        if bytes(blob[:pos]) != b'GTRBUNDLE 1\n':
            raise SystemExit('bundle %s: unknown format' % name)
        n = 0
        while True:
            end = blob.index(b'\n', pos)
            line = bytes(blob[pos:end]).decode('utf-8')
            pos = end + 1
            if line == 'END':
                break
            tag, path, size, sha, enc = line.split('\t')
            if tag != 'FILE' or path.startswith('/') or '..' in path.split('/'):
                raise SystemExit('bundle %s: bad entry %r' % (name, line))
            size = int(size)
            if enc == 'utf8':
                data = bytes(blob[pos:pos + size])
                pos += size + 1
            else:
                end = blob.index(b'\n', pos)
                data = base64.b64decode(bytes(blob[pos:end]))
                pos = end + 1
            if len(data) != size or hashlib.sha256(data).hexdigest() != sha:
                raise SystemExit('BAD file %s in bundle %s' % (path, name))
            out = os.path.join(target, path)
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, 'wb').write(data)
            n += 1
        if n != b['files']:
            raise SystemExit('bundle %s: %d files written, manifest says %d' % (name, n, b['files']))
        total += n
        print('%-17s OK  %5d files' % (name, n))
    print('all bundles OK: %d files written under %s' % (total, target))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
