#!/usr/bin/env python3
"""AmazeFileManager route_17: ReadFileTask$ReturnedValues.<init>(int).

Method: ReadFileTask$ReturnedValues.<init>(int)
Edge ids in order:
    Edd3316a5 E02683734 E9310cdcd Ee495bc45 E5c4cc446
Printed route: graphs/AmazeFileManager/scratch/route_print/
    ReadFileTask_ReturnedValues.<init>(int).txt, verdict REACHABLE,
    5 edges. The print's edge list matches methods.csv
    route_edge_ids and the d1_routes_draft.csv route_17 row
    exactly (no mismatch).
Permissions: none. No file is successfully read on this route: the
    read fails inside the content resolver before any storage
    permission is consulted, and TextEditorActivity has no
    first-run permission gate of its own.
Fixtures: none, deliberately. The failing read is arranged by
    pointing the VIEW intent at a MediaStore row that does not
    exist (see below); pushing a real file would take the success
    path instead.
Setup: none beyond the standard config.
Standard configuration: run_app.sh starts from `pm clear` and grants
    only the ROUTES.csv permissions (none here).

Mapping notes (printed source):
  - Entry is an ACTION_VIEW text/* intent from another app
    (AndroidManifest.xml:129-144 for TextEditorActivity, mime
    text/* at :138). The script simulates that intent with
    start_intent against a content:// URI.
  - Which constructor call sites feed <init>(int): ONLY the two
    catch branches of ReadFileTask.doInBackground
    (ReadFileTask.java:52-118). The success path returns
    new ReturnedValues(String, File) at :118, so a normal
    text-file open can never reach the target. The printed edge
    cites :115, the IOException branch: return new
    ReturnedValues(EXCEPTION_IO). The sibling failure branch at
    :112 returns new ReturnedValues(EXCEPTION_STREAM_NOT_FOUND)
    for a null input stream.
  - How this script hits the printed :115 site: the intent data
    is content://media/external/images/media/999999999, a
    MediaStore row id that does not exist on the emulator.
    EditableFileAbstraction takes the SCHEME_CONTENT branch
    (EditableFileAbstraction.java:32-34): its DISPLAY_NAME query
    returns an empty cursor, the getString throws, the generic
    Exception catch falls back to the last path segment, and no
    exception escapes the constructor. Then load() runs
    ReadFileTask with SCHEME_CONTENT, and
    contentResolver.openInputStream(uri) throws
    FileNotFoundException -- an IOException -- for the missing
    row, which the catch (IOException e) branch at
    ReadFileTask.java:113-115 turns into
    new ReturnedValues(EXCEPTION_IO) at :115. The load callback
    then toasts the IO error and finishes the activity
    (TextEditorActivity.java:330-333), so the script ends there.
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
    "Edd3316a5", "E02683734", "E9310cdcd", "Ee495bc45", "E5c4cc446",
]

PKG = "com.amaze.filemanager.debug"
EDITOR = PKG + "/com.amaze.filemanager.activities.TextEditorActivity"
# A MediaStore image row that does not exist on the emulator, so
# openInputStream throws FileNotFoundException (an IOException).
MISSING_CONTENT_URI = "content://media/external/images/media/999999999"


def main(argv=None):
    parser = argparse.ArgumentParser(description="AmazeFileManager route_17")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_17", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # Edd3316a5 S_ENTRY -> TextEditorActivity.<init>: simulate
    # another app opening a text file with ACTION_VIEW
    # (manifest TextEditorActivity filter
    # AndroidManifest.xml:129-144). The data URI names a
    # nonexistent MediaStore row on purpose: the read must fail
    # (see header) because only the catch branches construct
    # ReturnedValues(int).
    r.start_intent("Edd3316a5", action="android.intent.action.VIEW",
                   data=MISSING_CONTENT_URI, mime="text/plain",
                   component=EDITOR)
    # E02683734 TextEditorActivity.<init> -> TextEditorActivity
    # .onCreate: the framework instantiates the activity, then
    # onCreate runs. No user action.
    r.comment("system instantiates TextEditorActivity, then onCreate",
              "E02683734")
    # E9310cdcd TextEditorActivity.onCreate -> TextEditorActivity
    # .load: onCreate calls load() when there is no saved state
    # (TextEditorActivity.java:220). No user action.
    r.comment("onCreate calls load() (no saved state)", "E9310cdcd")
    # Ee495bc45 TextEditorActivity.load -> ReadFileTask
    # .doInBackground: load constructs ReadFileTask and executes
    # it (TextEditorActivity.java:291); AsyncTask dispatches
    # doInBackground. No user action.
    r.comment("load executes ReadFileTask; AsyncTask dispatches "
              "doInBackground", "Ee495bc45")
    # E5c4cc446 ReadFileTask.doInBackground ->
    # ReadFileTask$ReturnedValues.<init>(int): the SCHEME_CONTENT
    # branch calls contentResolver.openInputStream on the missing
    # MediaStore row, which throws FileNotFoundException; the
    # catch (IOException e) branch returns
    # new ReturnedValues(EXCEPTION_IO) (ReadFileTask.java:115).
    # The load callback toasts the IO error and finishes the
    # activity, so there is no further UI step.
    r.comment("openInputStream throws for the missing row; catch "
              "(IOException) returns ReturnedValues(EXCEPTION_IO)",
              "E5c4cc446")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
