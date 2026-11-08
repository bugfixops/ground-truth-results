#!/usr/bin/env python3
"""Diary route_30: Diary.getDay.

Method: Diary.getDay
Edge ids, in route order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 E5a0aa591 Efca6c74a E7fa15fb7
Printed route file: overnight/stream-D/Diary/scratch/route_steps.txt
    (section "Diary.getDay").
Edge details: graphs/Diary/out/diary_trigger_graph.json.
Permissions (ROUTES.csv): none.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): none.
Standard configuration: run_app.sh does pm clear before this script.
Launch-only script, on purpose: Diary.onResume unconditionally
    evaluates getFile().lastModified() against the saved value
    (Diary.java:554, inside onResume at Diary.java:537), and
    getFile() -> getFile(currEntry) -> getDay(...) (Diary.java:2026,
    2032-2037). The comparison runs on every launch's onResume, so
    the whole chain fires during the launch itself, whatever the
    comparison outcome is. No taps are needed or made.
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
    "Ee6b8aa80", "Edd0b9192", "Ee63879c9", "E5a0aa591", "Efca6c74a",
    "E7fa15fb7",
]
COMPONENT = "org.billthefarmer.diary/.Diary"


def main():
    parser = argparse.ArgumentParser(description="Diary route_30 replay")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(args.package, "route_30", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # Ee6b8aa80 -- Tap the Diary icon in the launcher
    # (MAIN/LAUNCHER intent filter). Driven as am start.
    r.launch(COMPONENT, "Ee6b8aa80")

    # Edd0b9192 -- The system instantiates Diary, then onCreate.
    # Lifecycle edge: no user action.
    r.comment("system instantiates Diary, then onCreate", "Edd0b9192")

    # Ee63879c9 -- onStart -> onResume. Lifecycle edge: no action.
    r.comment("onStart -> onResume", "Ee63879c9")

    # E5a0aa591 -- onResume -> getFile(): the "reload if modified"
    # check (Diary.java:554) calls getFile() on every onResume.
    # Consequence of the launch; no separate action.
    r.comment("onResume evaluates getFile().lastModified()",
              "E5a0aa591")

    # Efca6c74a -- getFile() -> getFile(currEntry)
    # (Diary.java:2026-2029). Consequence; no separate action.
    r.comment("getFile() delegates to getFile(currEntry)",
              "Efca6c74a")

    # E7fa15fb7 -- getFile(Calendar) -> getDay(y, m, d)
    # (Diary.java:2032-2037). The target; consequence of the
    # chain above, reached during the launch's onResume.
    r.comment("getFile(Calendar) calls getDay(y, m, d)",
              "E7fa15fb7")

    r.done()


if __name__ == "__main__":
    main()
