#!/usr/bin/env python3
"""AnyMemo route_25: DaggerAppComponents$ActivityComponentsBuilder.activity.

Method: DaggerAppComponents$ActivityComponentsBuilder.activity
Edge ids (in route order):
    Eddc920eb Ee33f0797 E39ee9f7c E9cbf2d10 Ebcd9e20d
Printed route file:
    graphs/AnyMemo/scratch/route_print/DaggerAppComponents_ActivityComponentsBuilder.activity.txt
    (5 edges, verdict REACHABLE).
Permissions: none (ROUTES.csv permissions cell is empty).
Fixtures: none (ROUTES.csv fixtures cell is empty).
Setup: none. This is a process-start / first-activity route:
    AnyMemo.onCreate calls activityComponents() (AnyMemo.java:117),
    which on its first call in the activity builds the Dagger
    activity components. No deck, card, or UI state is needed, and
    no permission or fixture is granted or pushed by this script.
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
    "Eddc920eb", "Ee33f0797", "E39ee9f7c", "E9cbf2d10", "Ebcd9e20d",
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

    r = Runner(package=args.package, route="route_25", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # Eddc920eb: MAIN / LAUNCHER intent starts AnyMemo.
        r.launch(args.package + "/" + COMPONENT, edge="Eddc920eb")
        # Ee33f0797: Activity lifecycle / framework callback.
        r.comment("system instantiates AnyMemo, then calls onCreate",
                  edge="Ee33f0797")
        # E39ee9f7c: Direct call (AnyMemo.java:117).
        r.comment("AnyMemo.onCreate calls BaseActivity.activityComponents",
                  edge="E39ee9f7c")
        # E9cbf2d10: Direct call; the cached field activityComponents
        # is still null, i.e. the first call in this activity
        # (BaseActivity.java:78-79).
        r.comment("activityComponents calls AMApplication.activityComponents",
                  edge="E9cbf2d10")
        # Ebcd9e20d: Virtual/interface call dispatching through
        # DaggerAppComponents$ActivityComponentsBuilder.activity
        # (AMApplication.java:82) -- TARGET reached on first launch.
        r.comment("AMApplication.activityComponents calls "
                  "DaggerAppComponents$ActivityComponentsBuilder.activity "
                  "(target edge)", edge="Ebcd9e20d")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
