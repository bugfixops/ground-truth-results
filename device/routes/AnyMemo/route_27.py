#!/usr/bin/env python3
"""AnyMemo route_27: BaseActivity.updateInterfaceLanguage.

Method: BaseActivity.updateInterfaceLanguage
Edge ids (in route order):
    Eddc920eb Ee33f0797 E44e2260f Ed26c5394
Printed route file:
    graphs/AnyMemo/scratch/route_print/BaseActivity.updateInterfaceLanguage.txt
    (4 edges, verdict REACHABLE).
Permissions: none (ROUTES.csv permissions cell is empty).
Fixtures: none (ROUTES.csv fixtures cell is empty).
Setup: none. This is a process-start / lifecycle route:
    AnyMemo.onCreate calls super.onCreate() (AnyMemo.java:118),
    and BaseActivity.onCreate calls updateInterfaceLanguage()
    (BaseActivity.java:43). No deck, card, or UI state is needed,
    and no permission or fixture is granted or pushed by this
    script.
Launch component: org.liberty.android.fantastischmemopro /
    org.liberty.android.fantastischmemopro.ui.AnyMemo (the launcher
    activity from AndroidManifest.xml:23-46).
"""

import argparse
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

try:
    from device.harness.harness import Runner
except ImportError:  # test-root fallback: load harness.py by path
    _HARNESS = None
    _dir = os.path.dirname(os.path.abspath(__file__))
    for _i in range(6):
        _cand = os.path.join(_dir, "device", "harness", "harness.py")
        if os.path.isfile(_cand):
            _HARNESS = _cand
            break
        _dir = os.path.dirname(_dir)
    if _HARNESS is None:
        raise
    _spec = importlib.util.spec_from_file_location("anymemo_harness",
                                                   _HARNESS)
    _mod = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_mod)
    Runner = _mod.Runner

EDGE_IDS = [
    "Eddc920eb", "Ee33f0797", "E44e2260f", "Ed26c5394",
]

COMPONENT = "org.liberty.android.fantastischmemopro.ui.AnyMemo"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_27", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # Eddc920eb: MAIN / LAUNCHER intent starts AnyMemo.
        r.launch(args.package + "/" + COMPONENT, edge="Eddc920eb")
        # Ee33f0797: Activity lifecycle / framework callback.
        r.comment("system instantiates AnyMemo, then calls onCreate",
                  edge="Ee33f0797")
        # E44e2260f: Direct call (AnyMemo.java:118, super.onCreate()).
        r.comment("AnyMemo.onCreate calls BaseActivity.onCreate",
                  edge="E44e2260f")
        # Ed26c5394: Direct call (BaseActivity.java:43) -- TARGET
        # BaseActivity.updateInterfaceLanguage reached on launch.
        r.comment("BaseActivity.onCreate calls updateInterfaceLanguage "
                  "(target edge)", edge="Ed26c5394")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
