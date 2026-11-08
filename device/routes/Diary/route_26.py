#!/usr/bin/env python3
"""Diary route_26: Diary.onDateSet(CustomCalendarView,int,int,int).

Method: Diary.onDateSet(CustomCalendarView,int,int,int)
Edge ids, in route order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E8b5a6aee
    Ef473e7f6 Ea3c861d0 Efbe01b83
Printed route file: overnight/stream-D/Diary/scratch/route_steps.txt
    (section "Diary.onDateSet(CustomCalendarView,int,int,int)").
Edge details: graphs/Diary/out/diary_trigger_graph.json.
Permissions (ROUTES.csv): none.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): none.
Standard configuration: run_app.sh does pm clear before this script.
    "Use custom calendar" defaults true (preferences.xml,
    Diary.java:244/1266), so no settings change is needed: goToDate
    takes the custom branch (Ef473e7f6) by default.
ASSUMPTION (auditor-confirmed from printed library source): the custom
    calendar dialog is constructed with currEntry's date
    (Diary.java:1731-1736: CustomCalendarDialog(this, this, year,
    month, date)), so the shown date is the selected date and tapping
    OK confirms it, firing onDateSet. Printed v1.06 library source
    (graphs/Diary/.plan/fw_src/libs/CustomCalendarView-v1.06/
    CustomCalendarDialog.java): the constructor sets the stored date
    from the passed year/month/day (:60-61), and the OK handler
    (BUTTON_POSITIVE, :111-118) calls listener.onDateSet
    unconditionally with that stored date (listener != null guard
    only) — no day-selection precondition. The dialog class is not in the
    final_java_only app slice, but the v1.06 source above confirms the
    assumption; if a real run ever showed OK disabled until a day pick
    (contradicting v1.06), add one day-cell tap before the existing
    OK tap as a live-run check only (the OK tap below stays).
"Go to date..." is showAsAction="ifRoom" with an icon
    (res/menu/main.xml:47-50, title res/values/strings.xml:26), so the
    script tries the icon content-desc first and falls back to the
    overflow text on LookupError (same pattern as route_18).
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
    "E8b5a6aee", "Ef473e7f6", "Ea3c861d0", "Efbe01b83",
]
COMPONENT = "org.billthefarmer.diary/.Diary"


def main():
    parser = argparse.ArgumentParser(description="Diary route_26 replay")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(args.package, "route_26", EDGE_IDS, args.log,
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
    # options. Here: "Go to date..." (ifRoom icon; fall back to
    # the overflow text if the icon is not shown).
    try:
        r.tap("E002e1746", desc="Go to date\u2026")
    except LookupError:
        r.tap("E002e1746", text="Go to date\u2026")

    # E8b5a6aee -- switch case R.id.goToDate. Consequence of the
    # previous tap; no separate action.
    r.comment("switch case R.id.goToDate", "E8b5a6aee")

    # Ef473e7f6 -- custom (default): showCustomCalendarDialog
    # (currEntry). Consequence of goToDate with pref_custom on
    # (the default); no separate action.
    r.comment("custom (default): showCustomCalendarDialog(currEntry)",
              "Ef473e7f6")

    # Ea3c861d0 -- dialog.show(): CustomCalendarDialog over Diary.
    # Page arrival: wait for the dialog's OK button.
    r.wait_for("Ea3c861d0", text="OK")

    # Efbe01b83 -- Pick a day and tap OK. The dialog was
    # constructed with currEntry's date (Diary.java:1731-1736), so
    # OK confirms the shown date and fires onDateSet. See the
    # ASSUMPTION note in the header for the real-run check.
    r.tap("Efbe01b83", text="OK")

    r.done()


if __name__ == "__main__":
    main()
