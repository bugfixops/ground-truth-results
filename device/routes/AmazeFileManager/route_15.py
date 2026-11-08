#!/usr/bin/env python3
"""AmazeFileManager route_15: TextEditorActivity$3.onAnimationEnd.

Method: TextEditorActivity$3.onAnimationEnd
Edge ids in order:
    Edd3316a5 E02683734 E74bea51a E49f6aa22 E63b4b663 E52012ad4
Printed route: graphs/AmazeFileManager/scratch/route_print/
    TextEditorActivity_3.onAnimationEnd.txt, verdict REACHABLE,
    6 edges. The print's edge list matches methods.csv
    route_edge_ids and the d1_routes_draft.csv route_15 row
    exactly (no mismatch).
Permissions: READ_EXTERNAL_STORAGE (the editor only reads the
    fixture file; no save happens on this route).
Fixtures: amaze_search.txt (this directory), pushed to
    /sdcard/Download/amaze_search.txt. Any readable text file
    would do; the same fixture as route_14 is reused so the
    editor opens on real content.
Setup: none beyond the standard config.
Standard configuration: run_app.sh starts from `pm clear` and grants
    only the ROUTES.csv permissions (READ_EXTERNAL_STORAGE here).

Mapping notes (printed source):
  - Entry is an ACTION_VIEW text/* intent from another app
    (AndroidManifest.xml:129-144 for TextEditorActivity, mime
    text/* at :138). The script simulates that intent with
    start_intent against a file:// URI for the pushed fixture;
    the editor needs a non-null intent data URI or it toasts
    and finishes (TextEditorActivity.java:190-197).
  - The hide path is driven by tapping the Find menu item twice.
    onOptionsItemSelected case R.id.find toggles on visibility
    (TextEditorActivity.java:388-390): if the search view is
    shown, hideSearchView(); otherwise revealSearchView(). The
    first tap therefore reveals (creating the $2 listener of
    route_16, not this route's target), and only the second tap,
    taken while the view is shown, takes the hide branch. The
    menu item is R.id.find in menu/text.xml, title @string/find
    = "Find in page" (res/values/strings.xml:271), showAsAction
    ifRoom, so the toolbar button exposes that title as its
    content-desc.
  - Do NOT use the search view's close button (R.id.close) here:
    its onClick handler sets the search view GONE directly
    (TextEditorActivity.java:585-588, case R.id.close) and never
    calls hideSearchView, so the $3 listener is never created.
    Only the Find menu item's hide branch reaches it.
  - hideSearchView builds a circular-reveal animator with a
    600 ms duration (TextEditorActivity.java:513-517) and
    registers the $3 AnimatorListenerAdapter at :518-526; the
    framework fires onAnimationEnd when that animation ends,
    and the body sets the search view GONE and hides the soft
    input (:521-524). The harness has no sleep op, so the script
    ends with a wait for the editor (R.id.fname) and a screenshot
    on the target edge; the 600 ms animation completes on the
    device regardless, but the replay runner must allow settle
    time after the final tap before collecting coverage.
  - The harness import searches upward for the directory
    containing device/harness/harness.py instead of the template's
    fixed four-level climb, because this helper copy lives one
    level shallower than device/routes/<App>/; the same file
    therefore imports unchanged after the merger moves it there.
"""

import argparse
import os
import sys

_here = os.path.abspath(__file__)
for _depth in (3, 4):
    _root = _here
    for _ in range(_depth):
        _root = os.path.dirname(_root)
    if os.path.isfile(os.path.join(_root, "device", "harness", "harness.py")):
        sys.path.insert(0, _root)
        break
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "Edd3316a5", "E02683734", "E74bea51a", "E49f6aa22", "E63b4b663",
    "E52012ad4",
]

PKG = "com.amaze.filemanager.debug"
EDITOR = PKG + "/com.amaze.filemanager.activities.TextEditorActivity"
FIXTURE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "amaze_search.txt")
DEVICE_PATH = "/sdcard/Download/amaze_search.txt"


def main(argv=None):
    parser = argparse.ArgumentParser(description="AmazeFileManager route_15")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_15", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # Edd3316a5 S_ENTRY -> TextEditorActivity.<init>: push the
    # fixture, then simulate another app opening it with
    # ACTION_VIEW text/plain (manifest TextEditorActivity
    # filter AndroidManifest.xml:129-144).
    r.push_fixture(FIXTURE, "Edd3316a5", dest=DEVICE_PATH)
    r.start_intent("Edd3316a5", action="android.intent.action.VIEW",
                   data="file://" + DEVICE_PATH, mime="text/plain",
                   component=EDITOR)
    # E02683734 TextEditorActivity.<init> ->
    # TextEditorActivity.onCreate: framework lifecycle. Wait for
    # the editor to load (mInput, R.id.fname, res/layout/search.xml).
    r.wait_for("E02683734", res_id="fname")
    # E74bea51a TextEditorActivity.onCreate ->
    # TextEditorActivity.onOptionsItemSelected: tap Find twice.
    # First tap reveals the search view (case R.id.find,
    # TextEditorActivity.java:388-390, reveal branch -- this
    # creates the $2 listener, not the target). Second tap, with
    # the view now shown, takes the hide branch that leads to
    # hideSearchView. The close button (R.id.close) is deliberately
    # NOT used: it sets the view GONE directly and never creates
    # the $3 listener (TextEditorActivity.java:585-588).
    r.tap("E74bea51a", desc="Find in page")
    r.tap("E74bea51a", desc="Find in page")
    # E49f6aa22 TextEditorActivity.onOptionsItemSelected ->
    # TextEditorActivity.hideSearchView: the second Find tap
    # takes the hide branch (TextEditorActivity.java:389).
    # No further action.
    r.comment("second Find tap takes hide branch at "
              "TextEditorActivity.java:389", "E49f6aa22")
    # E63b4b663 TextEditorActivity.hideSearchView ->
    # TextEditorActivity$3.<init>: hideSearchView registers the
    # $3 AnimatorListenerAdapter (TextEditorActivity.java:518-526).
    # No user action.
    r.comment("hideSearchView registers $3 listener at "
              "TextEditorActivity.java:518", "E63b4b663")
    # E52012ad4 TextEditorActivity$3.<init> ->
    # TextEditorActivity$3.onAnimationEnd: the framework fires
    # onAnimationEnd when the 600 ms hide animation ends
    # (TextEditorActivity.java:513-517); the body sets the search
    # view GONE (:521). No user action. This is the target edge.
    # The harness has no sleep op, so the replay runner must allow
    # settle time after the final tap before collecting coverage.
    r.comment("framework fires onAnimationEnd after 600 ms hide "
              "animation (TextEditorActivity.java:516-517)", "E52012ad4")
    r.wait_for("E52012ad4", res_id="fname")
    r.screenshot("route_15_search_hidden", "E52012ad4")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
