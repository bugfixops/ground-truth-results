#!/usr/bin/env python3
"""AmazeFileManager route_16: TextEditorActivity$2.onAnimationEnd.

Method: TextEditorActivity$2.onAnimationEnd
Edge ids in order:
    Edd3316a5 E02683734 E74bea51a E0b7a1038 E2b8c1c4e E79c59c72
Printed route: graphs/AmazeFileManager/scratch/route_print/
    TextEditorActivity_2.onAnimationEnd.txt, verdict REACHABLE,
    6 edges. The print's edge list matches methods.csv
    route_edge_ids and the d1_routes_draft.csv route_16 row
    exactly (no mismatch).
Permissions: READ_EXTERNAL_STORAGE (the editor only reads the
    fixture file; no save happens on this route).
Fixtures: amaze_text_fixture.txt (this directory), pushed to
    /sdcard/Download/amaze_text_fixture.txt.
Setup: none beyond the standard config.
Standard configuration: run_app.sh starts from `pm clear` and grants
    only the ROUTES.csv permissions (READ_EXTERNAL_STORAGE here).

Mapping notes (printed source):
  - Entry is an ACTION_VIEW text/* intent from another app
    (AndroidManifest.xml:129-144 for TextEditorActivity, mime
    text/* at :138). The script simulates that intent with
    start_intent against a file:// URI for the pushed fixture;
    EditableFileAbstraction takes the SCHEME_FILE branch for a
    file:// URI (EditableFileAbstraction.java:58-64).
  - The Find menu item is the reveal trigger: onOptionsItemSelected
    case R.id.find (TextEditorActivity.java:388-390) calls
    hideSearchView() if the search view is shown, else
    revealSearchView(). The search view starts hidden
    (res/layout/actionmode_textviewer.xml: searchview
    android:visibility="gone"), so the first Find tap takes the
    reveal branch. The item is res/menu/text.xml: find, title
    "Find in page" (res/values/strings.xml:271), showAsAction
    "ifRoom", so the toolbar action item carries that title as
    its content description and is tapped by desc.
  - revealSearchView() (TextEditorActivity.java:457-488) starts a
    600 ms circular-reveal animator and registers the anonymous
    AnimatorListenerAdapter ($2) at :481-488; the framework then
    calls its onAnimationEnd (:483-487), which requests focus
    for the search box and shows the soft input. No tap drives
    the final edge; it fires when the animation completes.
  - The harness import below searches upward for the directory
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
    "Edd3316a5", "E02683734", "E74bea51a", "E0b7a1038", "E2b8c1c4e",
    "E79c59c72",
]

PKG = "com.amaze.filemanager.debug"
EDITOR = PKG + "/com.amaze.filemanager.activities.TextEditorActivity"
FIXTURE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "amaze_text_fixture.txt")
DEVICE_PATH = "/sdcard/Download/amaze_text_fixture.txt"


def main(argv=None):
    parser = argparse.ArgumentParser(description="AmazeFileManager route_16")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_16", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # Edd3316a5 S_ENTRY -> TextEditorActivity.<init>: push the
    # text fixture, then simulate another app opening it with
    # ACTION_VIEW text/plain (manifest TextEditorActivity
    # filter AndroidManifest.xml:129-144).
    r.push_fixture(FIXTURE, "Edd3316a5", dest=DEVICE_PATH)
    r.start_intent("Edd3316a5", action="android.intent.action.VIEW",
                   data="file://" + DEVICE_PATH, mime="text/plain",
                   component=EDITOR)
    # E02683734 TextEditorActivity.<init> -> TextEditorActivity
    # .onCreate: the framework instantiates the activity, then
    # onCreate runs. Wait for the editor view (mInput,
    # R.id.fname) so the async file load has produced the editor.
    r.wait_for("E02683734", res_id="fname", timeout=30)
    # E74bea51a TextEditorActivity.onCreate ->
    # TextEditorActivity.onOptionsItemSelected: tap the Find
    # toolbar item; the framework dispatches onOptionsItemSelected.
    r.tap("E74bea51a", desc="Find in page")
    # E0b7a1038 TextEditorActivity.onOptionsItemSelected ->
    # TextEditorActivity.revealSearchView: case R.id.find
    # (TextEditorActivity.java:388-390). The search view starts
    # hidden, so this tap takes the reveal branch. No further
    # user action; the case body calls revealSearchView().
    r.comment("case R.id.find takes the reveal branch (search view "
              "starts hidden)", "E0b7a1038")
    # E2b8c1c4e TextEditorActivity.revealSearchView ->
    # TextEditorActivity$2.<init>: revealSearchView starts the
    # circular-reveal animator and registers the $2 listener
    # (TextEditorActivity.java:481-488). No user action.
    r.comment("revealSearchView registers the $2 animation listener",
              "E2b8c1c4e")
    # E79c59c72 TextEditorActivity$2.<init> ->
    # TextEditorActivity$2.onAnimationEnd: the animation framework
    # calls onAnimationEnd when the 600 ms reveal completes
    # (TextEditorActivity.java:483-487). No user action.
    r.comment("animation framework calls onAnimationEnd on completion",
              "E79c59c72")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
