#!/usr/bin/env python3
"""Diary route_15: Diary.addMedia(Intent) (ENV other_app: SEND path).

Method: Diary.addMedia(Intent)
Edges (in route order):
    Ee4ee499a E182e5f1e Eafcda211 Ebcf16a13 E4699aafc Ee6b69ad4
    E50bb88c9 E57e91fb9
Printed route: overnight/stream-D/Diary/scratch/route_steps.txt, section
    "Diary.addMedia"; edge details in
    graphs/Diary/out/diary_trigger_graph.json (same edge ids).
Permissions (ROUTES.csv): none.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): none. The custom calendar dialog is the default:
    Diary.java:244 initialises custom = true and getPreferences
    reads PREF_CUSTOM default true (Diary.java:1266), so goToDate
    shows the custom dialog (Diary.java:1721-1725), not the date
    picker.

Mapping judgment calls (see HELPER_REPORT.md for full citations):
  - The printed trigger for edge Ee4ee499a is another app sharing
    text/plain to Diary and the user picking Diary. The script
    issues the same SEND intent over adb with Diary as the
    explicit component (start_intent), which is the harness form
    of "an intent from another app"; the intent matches Diary's
    SEND text/plain filter (AndroidManifest.xml:60-67). The shared
    text is plain prose (not a URL), so addMedia takes its
    append-text branch (Diary.java:1560-1590) rather than the
    addLink branch for http(s) text.
  - The printed trigger for edge E50bb88c9 is "Pick a day and tap
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
EDGES = ["Ee4ee499a", "E182e5f1e", "Eafcda211", "Ebcf16a13",
         "E4699aafc", "Ee6b69ad4", "E50bb88c9", "E57e91fb9"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", default=".")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    a = ap.parse_args()
    r = Runner(package=a.package, route="route_15", edge_ids=EDGES,
                log_path=a.log, dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    try:
        # Edge Ee4ee499a: Another app shares text/plain to Diary:
        # text, a link, or a text file in EXTRA_STREAM. Issued over
        # adb as an explicit SEND intent with mime text/plain and
        # EXTRA_TEXT, matching the manifest filter
        # (AndroidManifest.xml:60-67). Shared text is plain prose,
        # not a URL, so addMedia appends it (Diary.java:1560-1590).
        r.start_intent(edge="Ee4ee499a",
                       action="android.intent.action.SEND",
                       mime="text/plain",
                       extras={"android.intent.extra.TEXT":
                               "Shared note for Diary"},
                       component=PKG_COMPONENT)
        # Edge E182e5f1e: The system instantiates Diary, then
        # onCreate. Lifecycle edge, no user action.
        r.comment("system instantiates Diary, then onCreate",
                  edge="E182e5f1e")
        # Edge Eafcda211: mediaCheck(intent) for the received
        # intent. Called by onCreate (Diary.java:515); no user
        # action.
        r.comment("onCreate calls mediaCheck(intent)",
                  edge="Eafcda211")
        # Edge Ebcf16a13: SEND / SEND_MULTIPLE / VIEW: haveMedia =
        # true; goToDate(currEntry) asks where to put it. mediaCheck
        # sets haveMedia for SEND intents and calls goToDate
        # (Diary.java:1293-1300); no user action.
        r.comment("SEND intent: haveMedia=true, goToDate(currEntry)",
                  edge="Ebcf16a13")
        # Edge E4699aafc: custom (default):
        # showCustomCalendarDialog(currEntry). Called by goToDate
        # (Diary.java:1721-1725); no user action.
        r.comment("goToDate shows custom calendar dialog",
                  edge="E4699aafc")
        # Edge Ee6b69ad4: dialog.show(): CustomCalendarDialog over
        # Diary. Shown by showCustomCalendarDialog (Diary.java:
        # 1731-1739); no user action.
        r.comment("CustomCalendarDialog shown over Diary",
                  edge="Ee6b69ad4")
        # Edge E50bb88c9: Pick a day and tap OK. Tap the dialog's
        # positive button, whose text is android.R.string.ok
        # (CustomCalendarDialog.java:64-67); the handler passes the
        # dialog date (default: currEntry) to onDateSet
        # (CustomCalendarDialog.java:107-120). See docstring for
        # why no day tap is used.
        r.tap(text="OK", edge="E50bb88c9")
        # Edge E57e91fb9: haveMedia (set by mediaCheck):
        # addMedia(getIntent()) inserts the received item. Called
        # by onDateSet (Diary.java:829-836); no user action. This
        # is the route target: the text/plain branch appends the
        # shared text to the entry (Diary.java:1560-1590).
        r.comment("onDateSet calls addMedia(getIntent())",
                  edge="E57e91fb9")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
