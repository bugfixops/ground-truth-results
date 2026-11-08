"""Prove that apps outside the re-audit did not change: compare their inputs and outputs, byte for byte, with a base
commit. Run from the repo root after a local rebuild (bash handoff/ci/rebuild.sh <apps>) or after pulling a CI commit.

Checked per app: graphs/<App>/graph_def.py, graph_def_mod/*.py, verification.csv, out/methods.csv and
out/*_trigger_graph.json. (README.md, build_report.txt and the HTML viewer are not compared: they carry commit and
tool text that may change without any label changing.)

Usage:
  python3 -I tools_dev/check_unchanged_apps.py                       # the eight apps outside the re-audit, base 46682745
  python3 -I tools_dev/check_unchanged_apps.py --base <commit> --apps Currency Diary
Exit status 0 when every file is identical, 1 otherwise.
"""
import argparse
import glob
import os
import subprocess
import sys

EIGHT = ['Currency', 'Diary', 'hash-checker', 'Omni-Notes', 'openlauncher', 'Vanilla-Music', 'Markor', 'AnyMemo']
BASE = '46682745'


def at(rev, path):
    r = subprocess.run(['git', 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', default=BASE)
    ap.add_argument('--apps', nargs='*', default=EIGHT)
    a = ap.parse_args()
    bad = 0
    for app in a.apps:
        g = 'graphs/%s' % app
        paths = [g + '/graph_def.py', g + '/verification.csv', g + '/out/methods.csv']
        paths += sorted(glob.glob(g + '/graph_def_mod/*.py')) + sorted(glob.glob(g + '/out/*_trigger_graph.json'))
        diffs = []
        for p in paths:
            old = at(a.base, p)
            new = open(p, 'rb').read() if os.path.exists(p) else None
            if old != new:
                diffs.append(p + (' (missing now)' if new is None else ' (new)' if old is None else ''))
        bad += bool(diffs)
        print('%-14s %s' % (app, 'unchanged' if not diffs else 'CHANGED: ' + ', '.join(diffs)))
    print('ALL UNCHANGED' if not bad else '%d app(s) changed' % bad)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
