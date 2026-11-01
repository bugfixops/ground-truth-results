#!/usr/bin/env python3
"""Diary route_11: Diary.lambda$listYears$1 (STATE data: year list).

Method: Diary.lambda$listYears$1
Edges (in route order):
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea9a2d993 Eadd8ec43 Ec14228ed
    E20854818 Ecc51ba5c
Printed route: overnight/stream-D/Diary/scratch/route_steps.txt, section
    "Diary.lambda$listYears$1"; edge details in
    graphs/Diary/out/diary_trigger_graph.json (same edge ids).
Permissions (ROUTES.csv, merger-updated): WRITE_EXTERNAL_STORAGE;READ_EXTERNAL_STORAGE. Setup grants below are not a
    varied gate: save() returns early without WRITE_EXTERNAL_STORAGE
    (Diary.java:2256-2265), so the setup save cannot happen without
    them; they are granted up front instead of answering a permission
    dialog mid-script.
Fixtures (ROUTES.csv): none. The STATE data is app-created (see below),
    not a pushed file, matching ROUTES_NOTES.md for this row.
Setup (ROUTES.csv): none. Script setup (phase A): save one entry
    through the app itself, so the diary folder holds an entry file
    when the route proper runs (phase B). run_app.sh does pm clear
    before the script, which does not clear shared-storage diary
    files, but the script does not rely on that: it creates its own.

How the route is reached (printed sources):
    Launch -> onCreate -> onResume -> setDate(currEntry)
    (Diary.java:551) -> getPrevEntry (Diary.java:2516-2519) ->
    prevYear (Diary.java:2082-2092, via listYears(getHome()),
    Diary.java:2043) -> listYears (Diary.java:311-315) ->
    File.listFiles(FilenameFilter) calls the lambda for each entry
    of the home folder. On a fresh install the home folder is empty,
    so the filter never runs; after phase A saves today's entry the
    home folder holds a year directory, and phase B's setDate chain
    reaches prevYear -> listYears -> the lambda. prevDay and
    prevMonth return -1 on that pass (only today's day file and the
    current month directory exist), so prevYear is reached.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner  # noqa: E402

PKG_COMPONENT = "org.billthefarmer.diary/.Diary"
EDGES = ["Ee6b8aa80", "Edd0b9192", "Ee63879c9", "Ea9a2d993",
         "Eadd8ec43", "Ec14228ed", "E20854818", "Ecc51ba5c"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", default=".")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    a = ap.parse_args()
    r = Runner(package=a.package, route="route_11", edge_ids=EDGES,
                log_path=a.log, dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    try:
        # -- Phase A: STATE setup, logged against the launch edge. --
        # The harness requires every action to name a route edge, and
        # this setup precedes the route proper; it is not itself a
        # route step, and it is labelled SETUP in every comment.

        # Edge Ee6b8aa80: Tap the Diary icon in the launcher
        # (MAIN/LAUNCHER intent filter). Via launch: the launcher
        # tap itself is the entry; the component is Diary's
        # MAIN/LAUNCHER activity (AndroidManifest.xml:52-59).
        r.launch(PKG_COMPONENT, edge="Ee6b8aa80")
        # SETUP grants (see docstring): storage is needed for save().
        r.grant("android.permission.WRITE_EXTERNAL_STORAGE",
                edge="Ee6b8aa80")
        r.grant("android.permission.READ_EXTERNAL_STORAGE",
                edge="Ee6b8aa80")
        # SETUP: open the editor. The edit ImageButton (res/layout/
        # main.xml, id "edit") is shown in view mode (Diary.java:
        # 1696-1709, buttonSwitcher EDIT child when shown); its click
        # runs animateEdit and sets shown = false (Diary.java:
        # 1027-1061), i.e. the edit view the route needs.
        r.tap(res_id="edit", edge="Ee6b8aa80")
        # SETUP: focus the entry text and type one entry line.
        r.tap(res_id="text", edge="Ee6b8aa80")
        r.type_text("Route eleven setup entry", edge="Ee6b8aa80")
        # SETUP: tap Accept (res/layout/main.xml, id "accept"); its
        # click calls save() when changed (Diary.java:992-998), which
        # writes today's entry file under the diary home folder
        # (Diary.java:2285-2310).
        r.tap(res_id="accept", edge="Ee6b8aa80")
        # SETUP: leave Diary (Back on the root page finishes it:
        # entry is true after Accept (Diary.java:1004) and the
        # entry stack is empty, Diary.java:731-741), so phase B
        # starts a fresh activity instance.
        r.back(edge="Ee6b8aa80")

        # -- Phase B: the route proper, one block per edge. --

        # Edge Ee6b8aa80: Tap the Diary icon in the launcher
        # (MAIN/LAUNCHER intent filter).
        r.launch(PKG_COMPONENT, edge="Ee6b8aa80")
        # Edge Edd0b9192: The system instantiates Diary, then
        # onCreate. Lifecycle edge, no user action.
        r.comment("system instantiates Diary, then onCreate",
                  edge="Edd0b9192")
        # Edge Ee63879c9: onStart -> onResume. Lifecycle edge, no
        # user action.
        r.comment("onStart -> onResume", edge="Ee63879c9")
        # Edge Ea9a2d993: setDate(currEntry). Called by onResume
        # (Diary.java:551); no user action.
        r.comment("onResume calls setDate(currEntry)",
                  edge="Ea9a2d993")
        # Edge Eadd8ec43: prevEntry = getPrevEntry(y, m, d) (today
        # if the date is in the future). Called by setDate
        # (Diary.java:2516-2519); no user action.
        r.comment("setDate calls getPrevEntry", edge="Eadd8ec43")
        # Edge Ec14228ed: No month found: prevYear(year), then
        # recursion into that year. Called by getPrevEntry
        # (Diary.java:2082-2092); no user action. prevDay and
        # prevMonth are -1 here (only today's entry exists), so
        # this branch is taken.
        r.comment("no earlier month: getPrevEntry calls prevYear",
                  edge="Ec14228ed")
        # Edge E20854818: listYears(home). Called by prevYear
        # (Diary.java:2043); no user action.
        r.comment("prevYear calls listYears(getHome())",
                  edge="E20854818")
        # Edge Ecc51ba5c: File.listFiles(FilenameFilter) calls the
        # filter lambda for each directory entry. Called by
        # listYears (Diary.java:311-315); no user action. The phase
        # A entry guarantees the home folder is non-empty, so the
        # lambda runs at least once.
        r.comment("listFiles filter lambda runs for home entries",
                  edge="Ecc51ba5c")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
