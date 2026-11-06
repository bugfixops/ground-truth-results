"""List lines that would break the publishing rule of the 2026-11-03 review: the repository must not name where the
independent sample comes from, or quote results of that work. The terms are stored encoded, so that this file does not
name them itself. Ordinary app text (for example AnkiDroid's "cards to study") is not flagged.

Usage (from the repo root):
  python3 -I tools_dev/check_terms.py <file> [<file> ...]
  python3 -I tools_dev/check_terms.py --since <commit>     # every file changed since <commit>, except app sources
Exit status 0 when nothing is flagged, 1 otherwise.
"""
import base64
import json
import re
import subprocess
import sys

_ENC = 'WyIoP2kpXFxicGFwZXJzP1xcYiIsICJcXGJJQ1NUXFxiIiwgIig/aSlcXGIoPzp0aGV8b3VyfHRoaXN8dGhhdHxhfHRoZWlyfHlvdXIpIHN0dWR5XFxiIiwgIig/aSlcXGJzdHVkaWVzXFxiIl0='
PATTERNS = [re.compile(p) for p in json.loads(base64.b64decode(_ENC).decode())]
SKIP = ('final_java_only/', 'fw_src/')


def flagged(text):
    return [i for i, line in enumerate(text.splitlines(), 1) if any(p.search(line) for p in PATTERNS)]


def main(argv):
    if len(argv) >= 2 and argv[0] == '--since':
        out = subprocess.run(['git', 'diff', '--name-only', argv[1], '--'], capture_output=True, text=True).stdout.split()
        files = [f for f in out if not f.startswith(SKIP)]
    else:
        files = argv
    bad = 0
    for f in files:
        try:
            text = open(f, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        for n in flagged(text):
            print('%s:%d: flagged by the publishing rule' % (f, n))
            bad += 1
    print('nothing flagged in %d file(s)' % len(files) if not bad else '%d line(s) flagged' % bad)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
