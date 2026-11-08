"""Device route script route_28 for Omni-Notes.

Method: BaseActivity.onCreate
Edge ids: Ea7466154 E626b84e7 E0c3ffffe
Printed route: graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/sample_30_routes.txt
    (BaseActivity.onCreate, 3 steps; path row result correct, confirmed_by SOURCE,
    ref MainActivity.java:93-94: Launcher -> MainActivity.<init> -> onCreate,
    whose first statement is super.onCreate (MainActivity.java:94)).
Permissions (ROUTES.csv): none (run_app.sh grants nothing for this route).
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

Startup route: launch the app and let the startup chain run. No tap is invented;
every edge after the launch is a lifecycle or explicit call.

One block per route edge, in route order. Lifecycle, page, explicit-call, and
framework edges with no user action get a comment, not an action. Every action
names an edge id of this route (the harness enforces it).
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ea7466154 E626b84e7 E0c3ffffe').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_28', EDGE_IDS, a.log,
               dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    # Ea7466154 S_ENTRY -> MainActivity.<init>: launcher starts MainActivity.
    r.launch('it.feio.android.omninotes/.MainActivity', 'Ea7466154')
    # E626b84e7 MainActivity.<init> -> MainActivity.onCreate: lifecycle, no action.
    r.comment('Activity lifecycle callback', 'E626b84e7')
    # E0c3ffffe MainActivity.onCreate -> BaseActivity.onCreate: explicit call,
    # first statement of onCreate is super.onCreate (MainActivity.java:94);
    # no user action; the coverage lookup detects the target.
    r.comment('super.onCreate() dispatches to BaseActivity.onCreate', 'E0c3ffffe')
    r.done()


if __name__ == '__main__':
    main()
