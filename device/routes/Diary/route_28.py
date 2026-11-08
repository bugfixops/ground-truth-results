#!/usr/bin/env python3
"""Diary route_28: Diary.getNextCalendarMonth.

Method: Diary.getNextCalendarMonth
Edge ids in order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E55f6b52d E7a3bcc72
    E38e0b13b
Printed route: Diary.java:3028-3036 (onSwipeUp calls
getNextCalendarMonth); edge list identical to the Diary ROUTES.csv
route_28 row and to diary_trigger_graph.json.
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none listed in ROUTES.csv.
Setup: none (Diary row of work-emulator ci/apps.csv has an empty
setup cell).
Standard configuration: run_app.sh starts from `pm clear` and grants
only the ROUTES.csv permissions (none here).

Mapping notes (printed source):
  - MULTI GATE: Diary.dispatchTouchEvent sets multi = true only
    when event.getPointerCount() > 1 (Diary.java:841-842), and
    GestureListener.onFling returns early when !multi
    (Diary.java:3440-3441). A single-finger fling can therefore
    never reach onSwipeUp/getNextCalendarMonth. This script uses
    the harness two_finger_swipe primitive (sendevent MT protocol):
    two contacts moving together report pointer count 2 for the
    whole gesture, so multi is true when the fling is evaluated.
    multi resets to false at the end of onFling
    (Diary.java:3485), so one gesture suffices.
  - DIRECTION: onFling takes the vertical branch when
    |diffY| >= |diffX|; diffY < 0 (finger moves UP) calls
    onSwipeUp (Diary.java:3471-3475), and onSwipeUp calls
    getNextCalendarMonth (Diary.java:3028-3036). The swipe here
    moves UPWARD (y 1200 -> 600, 600 px, exceeding the
    SWIPE_THRESHOLD of 256 px, Diary.java:3423).
  - THRESHOLDS: SWIPE_THRESHOLD = 256 px and
    SWIPE_VELOCITY_THRESHOLD = 256 px/s (Diary.java:3423-3424).
    The sendevent injection timestamps are kernel time at
    injection; if the detector computes too-low a velocity, the
    fling may not register. That is a live-run uncertainty, not a
    script defect: the JaCoCo result decides reached, and a miss
    is unclear, never wrong.
  - TOUCH DEVICE: the sendevent node comes from the TOUCH_DEVICE
    environment variable (discovered once per run by run_app.sh
    from `getevent -i` via device/touch_device.py), defaulting to
    /dev/input/event0. A wrong node silently does nothing (the
    route is unclear, never wrong). The fling coordinates are
    fixed (a fling has no target node to resolve): the Diary view
    fills the screen, and the two contacts move up together in
    its central area.
  - This route was unscriptable ("multi-pointer fling not
    drivable with the delivered harness") until the harness
    gained two_finger_swipe; it converts on that primitive alone.
"""

import argparse
import os
import sys

sys.path.insert(
    0,
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "Ee6b8aa80", "Edd0b9192", "Ee63879c9", "Ea885d6f1", "E55f6b52d",
    "E7a3bcc72", "E38e0b13b",
]

TOUCH_DEVICE = os.environ.get("TOUCH_DEVICE", "/dev/input/event0")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Diary route_28")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_28", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # Ee6b8aa80 S_ENTRY -> Diary.<init>: Tap the Diary icon in the
    # launcher (MAIN/LAUNCHER intent filter).
    r.launch(args.package + "/.Diary", "Ee6b8aa80")
    # Edd0b9192 Diary.<init> -> Diary.onCreate: system instantiates
    # Diary, then onCreate. No user action.
    r.comment("system instantiates Diary, then onCreate", "Edd0b9192")
    # Ee63879c9 Diary.onCreate -> Diary.onResume: onStart -> onResume.
    # No user action.
    r.comment("onStart -> onResume", "Ee63879c9")
    # Ea885d6f1 Diary.onResume -> S_DIARY_VIEW: Diary visible with
    # the MarkdownView. No deterministic text to wait on from a
    # fresh install (entry content varies), so no wait step.
    r.comment("Diary visible with the MarkdownView", "Ea885d6f1")
    # E55f6b52d S_DIARY_VIEW -> Diary$GestureListener.onFling@MULTI:
    # two contacts moving UP together (multi == true throughout):
    # 600 px upward, exceeding the 256 px swipe threshold.
    r.two_finger_swipe("E55f6b52d", TOUCH_DEVICE,
                       start1=(400, 1200), start2=(600, 1200),
                       end1=(400, 600), end2=(600, 600), steps=10)
    # E7a3bcc72 onFling@MULTI -> Diary.onSwipeUp: vertical fling up.
    # Automatic from the gesture; no user action.
    r.comment("vertical fling up calls onSwipeUp", "E7a3bcc72")
    # E38e0b13b Diary.onSwipeUp -> Diary.getNextCalendarMonth:
    # onSwipeUp calls getNextCalendarMonth (Diary.java:3030).
    # Automatic; this is the target edge.
    r.comment("onSwipeUp calls getNextCalendarMonth", "E38e0b13b")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
