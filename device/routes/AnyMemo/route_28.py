#!/usr/bin/env python3
"""AnyMemo route_28: DaggerAppComponents$ActivityComponentsBuilder.build.

Method: DaggerAppComponents$ActivityComponentsBuilder.build
Edge ids (in route order):
    Eddc920eb Ee33f0797 E39ee9f7c E9cbf2d10 Ea2e9a0fa
Printed route file:
    graphs/AnyMemo/scratch/route_print/DaggerAppComponents_ActivityComponentsBuilder.build.txt
    (5 edges, verdict REACHABLE).
Permissions: none (ROUTES.csv permissions cell is empty), so this
    script never calls grant().
Fixtures: none (ROUTES.csv fixtures cell is empty), so this script
    never calls push_fixture().
Setup: run_app.sh runs this script after pm clear (fresh install).
    No deck/card/category state is needed: this is a process-start
    route. Launching the launcher activity starts the process, the
    framework instantiates AnyMemo and calls onCreate, whose first
    line (ui/AnyMemo.java:117) calls activityComponents(), which
    reaches AMApplication.activityComponents() and its build() call
    (AMApplication.java:83) on the first call, when the cached field
    is still null (BaseActivity.java:78). No UI interaction beyond
    the launch is required, and no fixture is needed.

UI facts used: none beyond the launcher component from
    AndroidManifest.xml:23-46 (activity .ui.AnyMemo, MAIN/LAUNCHER).
    Every edge after the launch is a lifecycle/framework or direct
    call edge with no user action, so each gets a comment() call.
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
    _here = os.path.abspath(__file__)
    _dir = os.path.dirname(_here)
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
    "Eddc920eb", "Ee33f0797", "E39ee9f7c", "E9cbf2d10", "Ea2e9a0fa",
]

COMPONENT = "org.liberty.android.fantastischmemo.ui.AnyMemo"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_28", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # Eddc920eb: S_ENTRY -> AnyMemo.<init> (MAIN / LAUNCHER intent
        # starts AnyMemo; AndroidManifest.xml:23-46).
        r.launch(args.package + "/" + COMPONENT, edge="Eddc920eb")
        # Ee33f0797: AnyMemo.<init> -> AnyMemo.onCreate (Activity
        # lifecycle callback dispatched by the framework).
        r.comment("system instantiates AnyMemo, then calls onCreate",
                  edge="Ee33f0797")
        # E39ee9f7c: AnyMemo.onCreate -> BaseActivity.activityComponents
        # (direct call, AnyMemo.java:117: activityComponents().inject(this)).
        r.comment("AnyMemo.onCreate calls activityComponents()",
                  edge="E39ee9f7c")
        # E9cbf2d10: BaseActivity.activityComponents ->
        # AMApplication.activityComponents (direct call,
        # BaseActivity.java:79; guard: cached activityComponents field
        # still null, i.e. the first call in this activity).
        r.comment("BaseActivity.activityComponents delegates to "
                  "AMApplication.activityComponents (first call)",
                  edge="E9cbf2d10")
        # Ea2e9a0fa: AMApplication.activityComponents ->
        # DaggerAppComponents$ActivityComponentsBuilder.build -- TARGET
        # (direct call, AMApplication.java:83: .build()).
        r.comment("AMApplication.activityComponents calls "
                  "ActivityComponentsBuilder.build (target edge)",
                  edge="Ea2e9a0fa")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
