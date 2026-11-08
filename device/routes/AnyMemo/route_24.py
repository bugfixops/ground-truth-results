#!/usr/bin/env python3
"""AnyMemo route_24: NotificationChannelUtil.createConversationNotificationChannel.

Method: NotificationChannelUtil.createConversationNotificationChannel
Edge ids (in route order):
    Ef3365f92 Eccdaf854 E76a773c7 E59c50255 E53a88770
Printed route file:
    graphs/AnyMemo/scratch/route_print/NotificationChannelUtil.createConversationNotificationChannel.txt
    (5 edges, verdict REACHABLE).
Permissions: none (ROUTES.csv permissions cell is empty).
Fixtures: none (ROUTES.csv fixtures cell is empty).
Setup: none. This is a process-start route: launching the launcher
    activity starts the app process, and the Application runs before
    any activity, so the target fires during launch itself. No deck,
    card, or UI state is needed, and no permission or fixture is
    granted or pushed by this script (run_app.sh owns that phase).
Launch component: org.liberty.android.fantastischmemopro /
    org.liberty.android.fantastischmemo.ui.AnyMemo (the launcher
    activity from AndroidManifest.xml:23-46); starting it starts the
    process whose Application is AMApplication.
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
    "Ef3365f92", "Eccdaf854", "E76a773c7", "E59c50255", "E53a88770",
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

    r = Runner(package=args.package, route="route_24", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # Ef3365f92: The process starts (any component of the app is
        # about to run) -- launching the launcher activity starts it.
        r.launch(args.package + "/" + COMPONENT, edge="Ef3365f92")
        # Eccdaf854: the system calls Application.attachBaseContext
        # before onCreate.
        r.comment("system calls AMApplication.attachBaseContext",
                  edge="Eccdaf854")
        # E76a773c7: the system calls Application.onCreate once, after
        # every ContentProvider in the manifest is created.
        r.comment("system calls AMApplication.onCreate",
                  edge="E76a773c7")
        # E59c50255: Direct call (AMApplication.java:72).
        r.comment("AMApplication.onCreate calls createNotificationChannels",
                  edge="E59c50255")
        # E53a88770: Direct call (API 26+ guard, always true on API 27)
        # -- TARGET NotificationChannelUtil.createConversationNotificationChannel
        # reached during process start.
        r.comment("createNotificationChannels calls "
                  "createConversationNotificationChannel (target edge)",
                  edge="E53a88770")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
