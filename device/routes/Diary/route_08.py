"""Diary route_08: Diary.lambda$sortFiles$0.

Method: Diary.lambda$sortFiles$0
Edge ids, in route order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea9a2d993 Eadd8ec43 Ea5e57b91
    Ebf1d2b5a E31daa2a0 Ea16ba1a8
Printed route file: overnight/stream-D/Diary/scratch/route_steps.txt
    (section "Diary.lambda$sortFiles$0", ref Diary.java:305-306).
Permissions (ROUTES.csv, merger-updated): WRITE_EXTERNAL_STORAGE;READ_EXTERNAL_STORAGE (SETUP grants for saving/reading entries).
Fixtures: none (ROUTES.csv fixtures column empty).
Setup: none from ROUTES.csv (setup column empty); the STATE data
    the route needs is established by this script itself (see below),
    not by a fixture: ROUTES.csv state_kinds is "data" with the gate
    "the diary folder already holds entry files (entries saved on
    earlier visits)".
STATE ESTABLISHED BY THIS SCRIPT: two day-entry files in one month
    folder, so Arrays.sort in Diary.sortFiles (Diary.java:300-307)
    has at least 2 elements and calls the comparator. The script
    saves one entry for today and one for yesterday through the app
    itself (Edit button res/layout/main.xml @+id/edit, text field
    @+id/text, Accept button @+id/accept; accept saves, Diary.java:
    992-1010). If today is the 1st of the month, yesterday is in the
    previous month, so instead it saves entries for yesterday and
    the day before yesterday: the fresh launch's getPrevEntry chain
    then recurses into that month folder (Diary.java:2082-2092),
    which holds 2 files either way. After setup the script finishes
    the activity with Back and relaunches, so the route body below
    runs a fresh onCreate -> onResume -> setDate(today) chain
    (Diary.java:500-512, 539-551) whose prevDay/listDays/sortFiles
    steps reach the comparator.
Standard configuration: run_app.sh clears the package before this
    script; storage permissions are granted up front (see grant block) and no fixtures pushed.

Mapping notes:
- Launcher tap (Ee6b8aa80) is driven as am start via r.launch: the
  harness has no launcher-UI action, and starting the MAIN/LAUNCHER
  activity is the adb equivalent (AndroidManifest.xml:52-59).
- Setup actions are logged under the first edge (Ee6b8aa80) and
  marked STATE SETUP; they are not route steps, but every harness
  action needs an edge id of the route, and the setup must precede
  the route body's fresh launch.
- Date navigation uses "Go to date..." (res/menu/main.xml,
  res/values/strings.xml:26) and the standard DatePickerDialog
  (Diary.java:1721-1733). Its day cells carry a content description
  of the form "31 October 2026" (day, full month name, year); the
  script computes the target day from the host clock, assuming the
  emulator clock matches it (the CI emulator default). If the
  emulator locale differs, the month name in the description is the
  step to adjust. The dialog is confirmed with "OK".
- Back in view mode finishes Diary (Diary.java: onBackPressed falls
  through to super.onBackPressed when the MarkdownView cannot go
  back), so Back + relaunch gives a fresh launch.
"""

import argparse
import os
import sys
from datetime import date, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness.harness import Runner

COMPONENT = "org.billthefarmer.diary/org.billthefarmer.diary.Diary"
SETUP_EDGE = "Ee6b8aa80"

EDGE_IDS = [
    "Ee6b8aa80", "Edd0b9192", "Ee63879c9", "Ea9a2d993", "Eadd8ec43",
    "Ea5e57b91", "Ebf1d2b5a", "E31daa2a0", "Ea16ba1a8",
]


def _day_desc(d):
    """DatePicker day-cell content description, e.g. '31 October 2026'."""
    return "%d %s %d" % (d.day, d.strftime("%B"), d.year)


def _save_entry(r, text):
    """Type and save an entry for the currently shown day."""
    r.tap(SETUP_EDGE, res_id="edit")
    r.tap(SETUP_EDGE, res_id="text")
    r.type_text(text, SETUP_EDGE)
    r.tap(SETUP_EDGE, res_id="accept")


def _go_to_day(r, d):
    """Navigate to day d via Go to date... and the DatePickerDialog."""
    r.tap(SETUP_EDGE, desc="More options")
    r.tap(SETUP_EDGE, text="Go to date\u2026")
    r.tap(SETUP_EDGE, desc=_day_desc(d))
    r.tap(SETUP_EDGE, text="OK")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(args.package, "route_08", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    try:
        # Ee6b8aa80 -- Tap the Diary icon in the launcher
        # (MAIN/LAUNCHER intent filter). Driven as am start. This
        # first launch also hosts the STATE SETUP below.
        r.launch(COMPONENT, "Ee6b8aa80")

        # MERGER EDIT (SETUP grants): Diary.save() returns early without
        # WRITE_EXTERNAL_STORAGE (Diary.java:2248-2265); entry reads on
        # shared storage need READ_EXTERNAL_STORAGE. Granted before any
        # setup save so the setup entries persist. Logged under Ee6b8aa80.
        r.grant("android.permission.WRITE_EXTERNAL_STORAGE", "Ee6b8aa80")
        r.grant("android.permission.READ_EXTERNAL_STORAGE", "Ee6b8aa80")

        # STATE SETUP (not route steps; logged under Ee6b8aa80):
        # create two day-entry files in one month folder.
        today = date.today()
        if today.day == 1:
            # Yesterday and the day before are both in last month.
            _go_to_day(r, today - timedelta(days=1))
            _save_entry(r, "setup entry one")
            _go_to_day(r, today - timedelta(days=2))
            _save_entry(r, "setup entry two")
        else:
            _save_entry(r, "setup entry one")
            _go_to_day(r, today - timedelta(days=1))
            _save_entry(r, "setup entry two")
        # Finish the activity so the route body below is a fresh
        # launch (onCreate -> onResume -> setDate(today)).
        r.back(SETUP_EDGE)

        # ROUTE BODY -- fresh launch.
        # Ee6b8aa80 -- Tap the Diary icon in the launcher.
        r.launch(COMPONENT, "Ee6b8aa80")

        # Edd0b9192 -- The system instantiates Diary, then onCreate.
        # Lifecycle edge: no user action.
        r.comment("system instantiates Diary, then onCreate", "Edd0b9192")

        # Ee63879c9 -- onStart -> onResume. Lifecycle edge: no action.
        # onResume calls setDate(currEntry) (Diary.java:551); a fresh
        # launch sets currEntry to today (Diary.java:500-512).
        r.comment("onStart -> onResume", "Ee63879c9")

        # Ea9a2d993 -- setDate(currEntry) (Diary.java:551).
        # Internal call; no user action.
        r.comment("setDate(currEntry)", "Ea9a2d993")

        # Eadd8ec43 -- prevEntry = getPrevEntry(y, m, d)
        # (Diary.java:2516-2519). Internal call; no user action.
        r.comment("prevEntry = getPrevEntry(y, m, d)", "Eadd8ec43")

        # Ea5e57b91 -- prevDay(year, month, day): nearest day file in
        # the month folder (Diary.java:2082-2092). Internal call.
        r.comment("prevDay(year, month, day)", "Ea5e57b91")

        # Ebf1d2b5a -- listDays(monthDir) (Diary.java:2068-2075).
        # Internal call; no user action.
        r.comment("listDays(monthDir)", "Ebf1d2b5a")

        # E31daa2a0 -- sortFiles(dir.listFiles(filter))
        # (Diary.java:328-331). Internal call; no user action.
        r.comment("sortFiles(dir.listFiles(filter))", "E31daa2a0")

        # Ea16ba1a8 -- Arrays.sort(files, comparator): reverse name
        # order (Diary.java:300-307). Library behaviour: sort calls
        # the comparator for arrays with at least 2 elements, which
        # the STATE SETUP above guarantees. No user action.
        r.comment("Arrays.sort calls comparator (>= 2 day files)",
                  "Ea16ba1a8")
    finally:
        r.done()


if __name__ == "__main__":
    main()
