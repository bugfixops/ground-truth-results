#!/usr/bin/env python3
"""Diary route_13: Diary.addMap (ENV other_app: geo/map path).

Method: Diary.addMap
Edges (in route order):
    Ec0dffe3e E5b1dcd66 Ea80f69ad E76de4a23 Eefca3ed5 E37be136f
    E8810303d Ed6828399 E69496a12
Printed route: overnight/stream-D/Diary/scratch/route_steps.txt, section
    "Diary.addMap"; edge details in
    graphs/Diary/out/diary_trigger_graph.json (same edge ids).
Permissions (ROUTES.csv): none.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): none. The custom calendar dialog is the default:
    Diary.java:244 initialises custom = true and getPreferences
    reads PREF_CUSTOM default true (Diary.java:1266), so goToDate
    shows the custom dialog (Diary.java:1721-1725), not the date
    picker.

Mapping judgment calls (see HELPER_REPORT.md for full citations):
  - The printed trigger for edge Ec0dffe3e is another app opening a
    geo: link and the user picking Diary. The script issues the
    same intent over adb with Diary as the explicit component
    (start_intent), which is the harness form of "an intent from
    another app"; no chooser tap is needed or possible once the
    component is named, and the intent matches Diary's VIEW geo
    BROWSABLE filter (AndroidManifest.xml:75-82).
  - The printed trigger for edge E8810303d is "Pick a day and tap
    OK". The script taps OK only: the dialog constructor pre-sets
    its date field to the passed currEntry date
    (CustomCalendarDialog.java:58-62), and the positive-button
    handler passes that date to onDateSet (CustomCalendarDialog.
    java:107-120), so OK alone reaches onDateSet. Tapping a day
    number would be ambiguous (the calendar grid repeats day
    numbers, including overflow days), so no day tap is used.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner  # noqa: E402

PKG_COMPONENT = "org.billthefarmer.diary/.Diary"
EDGES = ["Ec0dffe3e", "E5b1dcd66", "Ea80f69ad", "E76de4a23",
         "Eefca3ed5", "E37be136f", "E8810303d", "Ed6828399",
         "E69496a12"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", default=".")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    a = ap.parse_args()
    r = Runner(package=a.package, route="route_13", edge_ids=EDGES,
                log_path=a.log, dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    try:
        # Edge Ec0dffe3e: Another app opens a geo: URI with Diary
        # (VIEW geo, BROWSABLE). Issued over adb as an explicit
        # VIEW intent for Diary's MAIN activity with a geo: URI,
        # matching the manifest filter (AndroidManifest.xml:75-82).
        # The geo: URI has no type, which is what routes it to
        # addMap later (Diary.java:1551-1558).
        r.start_intent(edge="Ec0dffe3e",
                       action="android.intent.action.VIEW",
                       data="geo:51.5,-0.12",
                       component=PKG_COMPONENT)
        # Edge E5b1dcd66: The system instantiates Diary, then
        # onCreate. Lifecycle edge, no user action.
        r.comment("system instantiates Diary, then onCreate",
                  edge="E5b1dcd66")
        # Edge Ea80f69ad: mediaCheck(intent) for the received
        # intent. Called by onCreate (Diary.java:515); no user
        # action.
        r.comment("onCreate calls mediaCheck(intent)",
                  edge="Ea80f69ad")
        # Edge E76de4a23: SEND / SEND_MULTIPLE / VIEW: haveMedia =
        # true; goToDate(currEntry) asks where to put it. mediaCheck
        # sets haveMedia for VIEW intents and calls goToDate
        # (Diary.java:1293-1300); no user action.
        r.comment("VIEW intent: haveMedia=true, goToDate(currEntry)",
                  edge="E76de4a23")
        # Edge Eefca3ed5: custom (default):
        # showCustomCalendarDialog(currEntry). Called by goToDate
        # (Diary.java:1721-1725); no user action.
        r.comment("goToDate shows custom calendar dialog",
                  edge="Eefca3ed5")
        # Edge E37be136f: dialog.show(): CustomCalendarDialog over
        # Diary. Shown by showCustomCalendarDialog (Diary.java:
        # 1731-1739); no user action.
        r.comment("CustomCalendarDialog shown over Diary",
                  edge="E37be136f")
        # Edge E8810303d: Pick a day and tap OK. Tap the dialog's
        # positive button, whose text is android.R.string.ok
        # (CustomCalendarDialog.java:64-67); the handler passes the
        # dialog date (default: currEntry) to onDateSet
        # (CustomCalendarDialog.java:107-120). See docstring for
        # why no day tap is used.
        r.tap(text="OK", edge="E8810303d")
        # Edge Ed6828399: haveMedia (set by mediaCheck):
        # addMedia(getIntent()) inserts the received item. Called
        # by onDateSet (Diary.java:829-836); no user action.
        r.comment("onDateSet calls addMedia(getIntent())",
                  edge="Ed6828399")
        # Edge E69496a12: type == null and scheme geo: addMap(uri).
        # addMedia dispatches to addMap for a typeless geo: intent
        # (Diary.java:1551-1558); no user action. This is the
        # route target.
        r.comment("typeless geo intent: addMedia calls addMap(uri)",
                  edge="E69496a12")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
