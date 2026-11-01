#!/usr/bin/env python3
"""Diary route_27: QueryHandler.<clinit>.

Method: QueryHandler.<clinit>
Edge ids, in route order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E2c10b318
    Ef5543c23 E243e9b87
Printed route file: overnight/stream-D/Diary/scratch/route_steps.txt
    (section "QueryHandler.<clinit>").
Edge details: graphs/Diary/out/diary_trigger_graph.json.
Permissions (ROUTES.csv): none.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): none.
Standard configuration: run_app.sh does pm clear before this script.
"Add events" is showAsAction="never" (res/menu/main.xml:85-87, title
    res/values/strings.xml:33), so it lives in the overflow menu.
Why no permission grant is needed: Diary.addEvents() calls
    QueryHandler.queryEvents directly with no permission gate
    (Diary.java:1858-1876). Class initialisation runs when the class
    is first used, i.e. when queryEvents is invoked, whatever the
    query itself returns (empty on a calendar-less emulator is fine:
    <clinit> has already run by then).
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
    "Ee6b8aa80", "Edd0b9192", "Ee63879c9", "Ea885d6f1", "E002e1746",
    "E2c10b318", "Ef5543c23", "E243e9b87",
]
COMPONENT = "org.billthefarmer.diary/.Diary"


def main():
    parser = argparse.ArgumentParser(description="Diary route_27 replay")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(args.package, "route_27", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # Ee6b8aa80 -- Tap the Diary icon in the launcher
    # (MAIN/LAUNCHER intent filter). Driven as am start.
    r.launch(COMPONENT, "Ee6b8aa80")

    # Edd0b9192 -- The system instantiates Diary, then onCreate.
    # Lifecycle edge: no user action.
    r.comment("system instantiates Diary, then onCreate", "Edd0b9192")

    # Ee63879c9 -- onStart -> onResume. Lifecycle edge: no action.
    r.comment("onStart -> onResume", "Ee63879c9")

    # Ea885d6f1 -- Diary visible with the MarkdownView.
    # Page arrival: wait for the MarkdownView (res/layout/main.xml
    # @+id/markdown).
    r.wait_for("Ea885d6f1", res_id="markdown")

    # E002e1746 -- Tap an action bar icon or an item under More
    # options. Here: open the overflow menu.
    r.tap("E002e1746", desc="More options")

    # E2c10b318 -- switch case R.id.addEvents (Diary.java:699-700).
    r.tap("E2c10b318", text="Add events")

    # Ef5543c23 -- addEvents -> QueryHandler.queryEvents. The tap
    # above runs addEvents, which invokes queryEvents directly
    # (Diary.java:1866-1869); no separate action.
    r.comment("addEvents invokes QueryHandler.queryEvents",
              "Ef5543c23")

    # E243e9b87 -- First use of class QueryHandler in this
    # process: <clinit> runs on the queryEvents invocation above.
    # No user action; the query result itself is irrelevant.
    r.comment("first use of QueryHandler: <clinit> runs",
              "E243e9b87")

    r.done()


if __name__ == "__main__":
    main()
