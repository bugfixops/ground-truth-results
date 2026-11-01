#!/usr/bin/env python3
"""AmazeFileManager route_14: ImmutableEntry.getValue.

Method: ImmutableEntry.getValue
Edge ids in order:
    Edd3316a5 Ef5b5e2c8 E58fb795c E0d85d17b E6cc6219b
Printed route: graphs/AmazeFileManager/scratch/route_print/
    ImmutableEntry.getValue.txt, verdict REACHABLE, 5 edges.
    The print's edge list matches methods.csv route_edge_ids
    and the d1_routes_draft.csv route_14 row exactly (no mismatch).
Permissions: READ_EXTERNAL_STORAGE (the editor only reads the
    fixture file; no save happens on this route).
Fixtures: amaze_search.txt (this directory), pushed to
    /sdcard/Download/amaze_search.txt. It contains the word
    "amaze" on four lines, so the search below is guaranteed at
    least one match; getValue is reached only when onPostExecute
    iterates a non-empty match list (SearchTextTask.java:88-95).
Setup: none beyond the standard config.
Standard configuration: run_app.sh starts from `pm clear` and grants
    only the ROUTES.csv permissions (READ_EXTERNAL_STORAGE here).

Mapping notes (printed source):
  - Entry is an ACTION_VIEW text/* intent from another app
    (AndroidManifest.xml:129-144 for TextEditorActivity, mime
    text/* at :138). The script simulates that intent with
    start_intent against a file:// URI for the pushed fixture;
    EditableFileAbstraction takes the SCHEME_FILE branch for a
    file:// URI (EditableFileAbstraction.java, "file" case), and
    load() reads it via ReadFileTask (TextEditorActivity.java:220,
    :288-291). The editor needs a non-null intent data URI or it
    toasts and finishes (TextEditorActivity.java:190-197), so the
    data URI is mandatory, not optional.
  - The print collapses onCreate/load/reveal into one edge
    (TextEditorActivity.<init> -> SearchTextTask.<init>, evidence
    TextEditorActivity.java:449 in afterTextChanged). The
    intermediate actions are: wait for the editor EditText
    (R.id.fname, res/layout/search.xml), tap the Find menu item
    (menu/text.xml item R.id.find, title @string/find =
    "Find in page", res/values/strings.xml:271, showAsAction
    ifRoom, so the toolbar button exposes that title as its
    content-desc), tap the search box (R.id.search_box,
    res/layout/actionmode_textviewer.xml, found through
    TextEditorActivity.java:151), then type the search term.
    afterTextChanged fires only for the search box's own text
    (TextEditorActivity.java:448: the hashCode guard against
    searchEditText.getText()), and constructs the task at :449.
    Note revealSearchView first clears the search box
    (TextEditorActivity.java:479, setText("")), which
    fires an empty-text task; that task is harmless because
    SearchTextTask.doInBackground breaks immediately when the
    search length is 0 (SearchTextTask.java:60-61), so it cannot
    reach getValue -- only the typed-term task can.
  - getValue is reached in onPostExecute only for real matches:
    doInBackground adds one MapEntry(new ImmutableEntry<>(i, ...))
    per match (SearchTextTask.java:67-69), and onPostExecute
    calls keyMapEntry.getValue() at :91 and :95 inside the loop
    over those entries. The fixture guarantees matches for the
    typed term "amaze".
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
    "Edd3316a5", "Ef5b5e2c8", "E58fb795c", "E0d85d17b", "E6cc6219b",
]

PKG = "com.amaze.filemanager.debug"
EDITOR = PKG + "/com.amaze.filemanager.activities.TextEditorActivity"
FIXTURE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "amaze_search.txt")
DEVICE_PATH = "/sdcard/Download/amaze_search.txt"


def main(argv=None):
    parser = argparse.ArgumentParser(description="AmazeFileManager route_14")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_14", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # Edd3316a5 S_ENTRY -> TextEditorActivity.<init>: push the
    # search fixture, then simulate another app opening it with
    # ACTION_VIEW text/plain (manifest TextEditorActivity
    # filter AndroidManifest.xml:129-144).
    r.push_fixture(FIXTURE, "Edd3316a5", dest=DEVICE_PATH)
    r.start_intent("Edd3316a5", action="android.intent.action.VIEW",
                   data="file://" + DEVICE_PATH, mime="text/plain",
                   component=EDITOR)
    # Ef5b5e2c8 TextEditorActivity.<init> -> SearchTextTask.<init>:
    # the print collapses onCreate/load/reveal here. Wait for the
    # editor to load (mInput, R.id.fname), reveal the search view
    # via the Find menu item (case R.id.find,
    # TextEditorActivity.java:388-390, reveal branch), focus the
    # search box (R.id.search_box), and type the term. Typing
    # fires afterTextChanged, which constructs SearchTextTask
    # (TextEditorActivity.java:448-449).
    r.wait_for("Ef5b5e2c8", res_id="fname")
    r.tap("Ef5b5e2c8", desc="Find in page")
    r.tap("Ef5b5e2c8", res_id="search_box")
    r.type_text("amaze", "Ef5b5e2c8")
    # E58fb795c SearchTextTask.<init> ->
    # SearchTextTask.doInBackground: AsyncTask.execute dispatches
    # the worker. No user action.
    r.comment("SearchTextTask.execute dispatches doInBackground",
              "E58fb795c")
    # E0d85d17b SearchTextTask.doInBackground ->
    # SearchTextTask.onPostExecute: framework posts the result
    # back to the main thread. No user action.
    r.comment("framework posts result to onPostExecute", "E0d85d17b")
    # E6cc6219b SearchTextTask.onPostExecute ->
    # ImmutableEntry.getValue: onPostExecute iterates the match
    # list and calls keyMapEntry.getValue() (SearchTextTask.java:91,
    # :95). Matches exist because the fixture contains "amaze".
    # No user action. This is the target edge.
    r.comment("onPostExecute iterates matches, calls keyMapEntry.getValue "
              "at SearchTextTask.java:91,95", "E6cc6219b")
    r.screenshot("route_14_search", "E6cc6219b")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
