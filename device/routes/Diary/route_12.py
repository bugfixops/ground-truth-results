#!/usr/bin/env python3
"""Diary route_12: QueryHandler.onInsertComplete (ENV other + other_app).

Method: QueryHandler.onInsertComplete
Edges (in route order):
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 Ea16497b4 E7b97a38b
    Ea3a04808 E0edc1077 E73406bfe E9e5808e9 E5e97f516 Ecab87f2c
    E8515bd78 E06a409c9
Printed route: overnight/stream-D/Diary/scratch/route_steps.txt, section
    "QueryHandler.onInsertComplete"; edge details in
    graphs/Diary/out/diary_trigger_graph.json (same edge ids).
Permissions (ROUTES.csv, merger-updated): WRITE_EXTERNAL_STORAGE;READ_EXTERNAL_STORAGE;WRITE_CALENDAR;READ_CALENDAR. Setup grants below are not a
    varied gate (see ROUTES_NOTES.md for this row): save() returns
    early without WRITE_EXTERNAL_STORAGE (Diary.java:2256-2265), and
    the Calendar provider needs READ/WRITE_CALENDAR, so all four are
    granted up front instead of answering a permission dialog
    mid-script. Without them the route cannot reach eventCheck at all.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): none.

EXTERNAL PRECONDITIONS -- NOT SET BY THIS SCRIPT, READ BEFORE USE:
  (a) 24-hour locale (edge Ecab87f2c). eventCheck parses the typed
      time with DateFormat.SHORT (Diary.java:1305-1323); in a 12-hour
      locale such as en-US, "10:30" fails to parse and insertEvent is
      never called. The D2 harness has no locale action: changing the
      device locale over adb needs persist.sys.locale plus a reboot,
      which no harness call performs, and the Settings language UI
      needs a drag to make a newly added language primary, which the
      harness cannot do either. The run environment must therefore
      provision a 24-hour locale (e.g. en-GB, de-DE) before this
      script runs. On a default en-US emulator this route will NOT
      reach onInsertComplete; if the device lead cannot provision
      the locale, this route should be reclassified unscriptable.
  (b) A calendar exists (edge E06a409c9). onQueryComplete returns
      early when the Calendars query has no rows (QueryHandler.java:
      124-126), so onInsertComplete is never reached without at
      least one calendar row in the Calendar provider. The harness
      cannot create a calendar row (no provider-write action, and a
      calendar app needs an account first). The run environment must
      provision one before this script runs.

Mapping judgment calls (see HELPER_REPORT.md for full citations):
  - The printed double-tap (edge Ea16497b4) cannot be driven by the
    harness, which has no double-tap action (two slow adb taps are
    not a reliable double-tap for GestureDetector). The script taps
    the edit ImageButton (res/layout/main.xml, id "edit") instead:
    its click runs animateEdit and sets shown = false
    (Diary.java:1027-1061), the same S_DIARY_EDIT state the
    double-tap reaches (Diary.java:3491-3540, shown = false).
  - The typed line is inserted at the cursor into whatever text is
    already shown; EVENT_PATTERN is MULTILINE (Diary.java:161), so
    the "@ HH:MM title" line matches even when concatenated with
    pre-existing text, and insertEvent still fires.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner  # noqa: E402

PKG_COMPONENT = "org.billthefarmer.diary/.Diary"
EDGES = ["Ee6b8aa80", "Edd0b9192", "Ee63879c9", "Ea885d6f1",
         "Ea16497b4", "E7b97a38b", "Ea3a04808", "E0edc1077",
         "E73406bfe", "E9e5808e9", "E5e97f516", "Ecab87f2c",
         "E8515bd78", "E06a409c9"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", default=".")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    a = ap.parse_args()
    r = Runner(package=a.package, route="route_12", edge_ids=EDGES,
                log_path=a.log, dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    try:
        # Edge Ee6b8aa80: Tap the Diary icon in the launcher
        # (MAIN/LAUNCHER intent filter).
        r.launch(PKG_COMPONENT, edge="Ee6b8aa80")
        # SETUP grants (see docstring): storage + calendar, needed
        # before any save/eventCheck can run.
        r.grant("android.permission.WRITE_EXTERNAL_STORAGE",
                edge="Ee6b8aa80")
        r.grant("android.permission.READ_EXTERNAL_STORAGE",
                edge="Ee6b8aa80")
        r.grant("android.permission.WRITE_CALENDAR",
                edge="Ee6b8aa80")
        r.grant("android.permission.READ_CALENDAR",
                edge="Ee6b8aa80")
        # Edge Edd0b9192: The system instantiates Diary, then
        # onCreate. Lifecycle edge, no user action.
        r.comment("system instantiates Diary, then onCreate",
                  edge="Edd0b9192")
        # Edge Ee63879c9: onStart -> onResume. Lifecycle edge, no
        # user action.
        r.comment("onStart -> onResume", edge="Ee63879c9")
        # Edge Ea885d6f1: Diary visible with the MarkdownView.
        # Enters-page edge, no user action.
        r.comment("Diary visible with MarkdownView",
                  edge="Ea885d6f1")
        # Edge Ea16497b4: Double-tap the text: the editor opens at
        # that position. Printed trigger is a double-tap; the
        # harness has no double-tap action, so tap the edit
        # ImageButton (res/layout/main.xml, id "edit"), which
        # reaches the same edit state (see docstring).
        r.tap(res_id="edit", edge="Ea16497b4")
        # Edge E7b97a38b: EditText and Accept button shown
        # (shown = false). Enters-page edge, follows the edit tap;
        # no further action.
        r.comment("EditText and Accept button shown",
                  edge="E7b97a38b")
        # Edge Ea3a04808: Typing an event line notifies the
        # TextWatcher. Tap the entry text to focus it, then type
        # the printed event line "@ 10:30 Dentist" (Diary.java:
        # 1077-1086, 1305-1349; assets/help.md:217-224). The typed
        # time must parse under the provisioned 24-hour locale.
        r.tap(res_id="text", edge="Ea3a04808")
        r.type_text("@ 10:30 Dentist", edge="Ea3a04808")
        # Edge E0edc1077: changed = true with an event line in the
        # text. Follows typing via the TextWatcher (Diary.java:
        # 1084-1086); no user action.
        r.comment("changed=true with event line in text",
                  edge="E0edc1077")
        # Edge E73406bfe: Tap the Accept button: the entry is
        # saved. Accept ImageButton, res/layout/main.xml, id
        # "accept" (Diary.java:992-1017).
        r.tap(res_id="accept", edge="E73406bfe")
        # Edge E9e5808e9: changed: save(). Called by the Accept
        # click (Diary.java:995-998); no user action.
        r.comment("Accept click calls save()", edge="E9e5808e9")
        # Edge E5e97f516: eventCheck(text) (storage permission
        # granted). Called by save() (Diary.java:2270); no user
        # action. The grants above satisfy the permission gate.
        r.comment("save() calls eventCheck(text)",
                  edge="E5e97f516")
        # Edge Ecab87f2c: QueryHandler.insertEvent(start, start +
        # 1 h, title) for the typed "@ HH:MM title" line. This
        # fires only if the typed time parses under a 24-hour
        # SHORT format (Diary.java:1305-1323) -- see the EXTERNAL
        # PRECONDITIONS note in the docstring: the locale is
        # provisioned by the run environment, not by this script.
        r.comment("eventCheck calls insertEvent (24h locale needed)",
                  edge="Ecab87f2c")
        # Edge E8515bd78: startQuery(EVENT_INSERT, values,
        # Calendars.CONTENT_URI): find a calendar id. Called by
        # insertEvent (QueryHandler.java:107-116); no user action.
        r.comment("insertEvent queries Calendars for an id",
                  edge="E8515bd78")
        # Edge E06a409c9: EVENT_INSERT: first calendar id;
        # startInsert(EVENT_REMIND, Events) -> onInsertComplete.
        # Reached only if at least one calendar exists
        # (QueryHandler.java:131-144) -- see the EXTERNAL
        # PRECONDITIONS note: the calendar is provisioned by the
        # run environment, not by this script.
        r.comment("first calendar id: startInsert -> onInsertComplete",
                  edge="E06a409c9")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
