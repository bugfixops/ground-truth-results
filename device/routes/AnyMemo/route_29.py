#!/usr/bin/env python3
"""AnyMemo route_29: NotificationChannelUtil.createCardPlayerNotificationChannel.

Method: NotificationChannelUtil.createCardPlayerNotificationChannel
Edge ids (in route order):
    Ef3365f92 Eccdaf854 E76a773c7 E59c50255 E79c07339
Printed route file:
    graphs/AnyMemo/scratch/route_print/NotificationChannelUtil.createCardPlayerNotificationChannel.txt
    (5 edges, verdict REACHABLE).
Permissions: none (ROUTES.csv permissions cell is empty), so this
    script never calls grant().
Fixtures: none (ROUTES.csv fixtures cell is empty), so this script
    never calls push_fixture().
Setup: run_app.sh runs this script after pm clear (fresh install).
    No deck/card/category state is needed: this is a process-start
    route. Launching the launcher activity starts the process, the
    framework creates the application (manifest android:name
    ".common.AMApplication", AndroidManifest.xml:20), and
    AMApplication.onCreate (AMApplication.java:72) calls
    notificationChannelUtil.createNotificationChannels(), which
    calls createCardPlayerNotificationChannel()
    (NotificationChannelUtil.java:41) whenever SDK_INT >= O (API 26+;
    always true on API 27). No UI interaction beyond the launch is
    required, and no fixture is needed.

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
    "Ef3365f92", "Eccdaf854", "E76a773c7", "E59c50255", "E79c07339",
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

    r = Runner(package=args.package, route="route_29", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # Ef3365f92: S_ENTRY -> AMApplication.<init> (process start:
        # launching the launcher activity creates the application
        # first; AndroidManifest.xml:20 names .common.AMApplication).
        r.launch(args.package + "/" + COMPONENT, edge="Ef3365f92")
        # Eccdaf854: AMApplication.<init> -> AMApplication.attachBaseContext
        # (Application lifecycle callback, AMApplication.java:56-60).
        r.comment("system creates AMApplication, attachBaseContext",
                  edge="Eccdaf854")
        # E76a773c7: AMApplication.attachBaseContext -> AMApplication.onCreate
        # (Application lifecycle callback, AMApplication.java:62-73).
        r.comment("AMApplication.onCreate runs at process start",
                  edge="E76a773c7")
        # E59c50255: AMApplication.onCreate ->
        # NotificationChannelUtil.createNotificationChannels (direct
        # call, AMApplication.java:72).
        r.comment("AMApplication.onCreate calls createNotificationChannels",
                  edge="E59c50255")
        # E79c07339: NotificationChannelUtil.createNotificationChannels ->
        # NotificationChannelUtil.createCardPlayerNotificationChannel -- TARGET
        # (direct call, NotificationChannelUtil.java:41; guard SDK_INT >= O,
        # always true on API 27).
        r.comment("createNotificationChannels calls "
                  "createCardPlayerNotificationChannel (target edge)",
                  edge="E79c07339")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
