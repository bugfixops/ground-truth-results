"""Pack the files the tools need into text bundles cut into parts below the GitHub connector's ~1 MB limit.

Usage (from the repo root): python3 -I handoff/connector_kit/make_bundles.py <out_dir> [part_bytes]
Writes <out_dir>/<bundle>/<bundle>.partNNN.txt and <out_dir>/MANIFEST.json.
Bundles: common (tools, handoff/examples, handoff/connector_kit, fw_src) and one per app (graph inputs + app sources).
Bundle format: a header line "GTRBUNDLE 1", then per file a line "FILE\t<path>\t<size>\t<sha256>\t<utf8|b64>",
the content (raw UTF-8, or base64 for files that are not valid UTF-8), and a newline; the last line is "END".
Unpack with handoff/connector_kit/unpack.py.
"""
import base64
import glob
import hashlib
import json
import os
import sys

APPS = ['Currency', 'Diary', 'hash-checker', 'Omni-Notes', 'openlauncher', 'Vanilla-Music', 'Markor', 'AnyMemo',
        'Aegis', 'AmazeFileManager', 'AnkiDroid', 'MMEX', 'LibreTorrent']
GRAPH_FILES = ['graph_def.py', 'method_list.json', 'auto_calls.json', 'calls_all.json', 'verification.csv',
               'make_verification.py', 'readme_notes.md', 'LESSONS.md', 'AGENT_NOTES.md']
SRC_EXT = ('.java', '.kt', '.xml', '.gradle', '.pro', '.properties', '.txt', '.json')
MARKER = ('Marker only. tools/show_route.py built_flavors() reads the name of this folder to know which product flavor\n'
          'the dataset APK was built from; the class files themselves are not in the repo.\n')
SKIP_DIRS = {'build', 'androidTest', 'test', '.git', 'JacocoInstrument', 'report', 'monkey', 'ape', 'combined'}


def common_files():
    out = []
    for f in sorted(os.listdir('tools')):
        p = os.path.join('tools', f)
        if os.path.isfile(p) and f.endswith(('.py', '.sh', '.html')) and 'backup' not in f:
            out.append(p)
    for d in ('handoff/examples', 'handoff/connector_kit', 'handoff/ci'):
        for f in sorted(os.listdir(d)):
            p = os.path.join(d, f)
            if os.path.isfile(p) and not f.endswith('.pyc'):
                out.append(p)
    for dp, dn, fn in os.walk('fw_src'):
        dn.sort()
        for f in sorted(fn):
            out.append(os.path.join(dp, f))
    return out


def app_files(app):
    g = os.path.join('graphs', app)
    out = [os.path.join(g, f) for f in GRAPH_FILES if os.path.isfile(os.path.join(g, f))]
    for sub in ('graph_def_mod', 'parts' if app == 'LibreTorrent' else None,
                'scratch/merge-ready' if app == 'LibreTorrent' else None):
        if sub and os.path.isdir(os.path.join(g, sub)):
            out += [os.path.join(g, sub, f) for f in sorted(os.listdir(os.path.join(g, sub)))
                    if os.path.isfile(os.path.join(g, sub, f))]
    if app == 'Markor':
        out += [os.path.join(g, 'scratch', f) for f in ('hier.json', 'textcount.json', 'dotcount.json', 'route_guards.json')]
    if app == 'LibreTorrent':
        for f in ('gates.md',):
            if os.path.isfile(os.path.join(g, 'scratch', f)):
                out.append(os.path.join(g, 'scratch', f))
    root = os.path.join('final_java_only', app, 'app')
    for d in sorted(glob.glob(os.path.join(root, '*', 'app', 'build', 'intermediates', 'javac', '*Debug'))):
        out.append((os.path.join(d, 'FLAVOR_MARKER.txt'), MARKER.encode('utf-8')))
    for f in sorted(os.listdir(root)):
        p = os.path.join(root, f)
        if os.path.isfile(p) and f.endswith(('.txt', '.json')):
            out.append(p)
    for dp, dn, fn in os.walk(root):
        dn[:] = sorted(d for d in dn if d not in SKIP_DIRS)
        if dp == root:
            continue
        for f in sorted(fn):
            if f.endswith(SRC_EXT):
                out.append(os.path.join(dp, f))
    return out


def pack(paths):
    chunks = [b'GTRBUNDLE 1\n']
    for p in paths:
        if isinstance(p, tuple):
            p, data = p
        else:
            data = open(p, 'rb').read()
        try:
            data.decode('utf-8')
            enc, body = 'utf8', data
        except UnicodeDecodeError:
            enc, body = 'b64', base64.b64encode(data)
        head = 'FILE\t%s\t%d\t%s\t%s\n' % (p, len(data), hashlib.sha256(data).hexdigest(), enc)
        chunks += [head.encode('utf-8'), body, b'\n']
    chunks.append(b'END\n')
    return b''.join(chunks)


def main(argv):
    out_dir = argv[1]
    part = int(argv[2]) if len(argv) > 2 else 700000
    manifest = {'format': 'GTRBUNDLE 1', 'part_bytes': part, 'bundles': {}}
    sets = [('common', common_files())] + [(a, app_files(a)) for a in APPS]
    for name, paths in sets:
        blob = pack(paths)
        d = os.path.join(out_dir, name)
        os.makedirs(d, exist_ok=True)
        parts = []
        for i in range(0, len(blob), part):
            piece = blob[i:i + part]
            fn = '%s.part%03d.txt' % (name, i // part + 1)
            open(os.path.join(d, fn), 'wb').write(piece)
            parts.append({'file': '%s/%s' % (name, fn), 'bytes': len(piece), 'sha256': hashlib.sha256(piece).hexdigest()})
        manifest['bundles'][name] = {'files': len(paths), 'bytes': len(blob),
                                     'sha256': hashlib.sha256(blob).hexdigest(), 'parts': parts}
        print('%-17s %5d files %6.1f MB %3d parts' % (name, len(paths), len(blob) / 1e6, len(parts)))
    json.dump(manifest, open(os.path.join(out_dir, 'MANIFEST.json'), 'w'), indent=1)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
