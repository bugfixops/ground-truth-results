#!/usr/bin/env python3
"""AmazeFileManager route_11: PasteHelper$1.createFromParcel.

Method: PasteHelper$1.createFromParcel
Edge ids in order:
    E380fe171 E03c72cf9 E745b85ef Ed18978e9 E6a0c67c7
Printed route: MainActivity.java:366 (source ref); edge list
identical to the AmazeFileManager ROUTES.csv route_11 row and to
the trigger graph. Identical flow to route_09, stopping at
createFromParcel (route_09 continues one edge further into
PasteHelper.<init>(Parcel)).
Permissions: android.permission.WRITE_EXTERNAL_STORAGE only (the
app's declared set), pre-granted by run_app.sh: the copy flow
reads the Download file list.
Fixtures: amaze_search.txt, pushed by run_app.sh to
/sdcard/Download/amaze_search.txt before the script (repo fixture
entry in ROUTES.csv); the script does NOT push it.
Setup: run_app.sh pushes the fixture before the script (see above).
Standard configuration: run_app.sh starts from `pm clear` and grants
only the ROUTES.csv permissions.

Mapping notes (printed source): see route_09's header — same
mechanism. In short: copy a file so MainActivity's pasteHelper is
non-null (MainFragment.java:719-729 -> setPaste), then rotate
(MainActivity declares no configChanges, so it recreates);
onSaveInstanceState saves the paste helper
(MainActivity.java:1077-1079); the recreated instance's
MainActivity$1.onPostExecute reads PASTEHELPER_BUNDLE
(MainActivity.java:425) and Bundle.getParcelable unparcels it
through PasteHelper$1.createFromParcel (E6a0c67c7, target).
The Copy action-mode item is icon-only (contextual.xml:28-31),
so the script taps desc="Copy" (AppCompat exposes the title as
the button's content-desc). The copy + rotate steps are
preconditions for E6a0c67c7 and are logged under that edge.
This route was unscriptable ("no rotation, recreate, or
process-kill op") until the harness gained rotate(); it converts
on that primitive alone.
"""

import argparse
import os
import sys

sys.path.insert(
    0,
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E380fe171", "E03c72cf9", "E745b85ef", "Ed18978e9", "E6a0c67c7",
]

PKG = "com.amaze.filemanager.debug"
MAIN = PKG + "/.activities.MainActivity"
SOURCE_DIR = "/sdcard/Download"
FILE_ROW = "amaze_search.txt"


def main(argv=None):
    parser = argparse.ArgumentParser(description="AmazeFileManager route_11")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_11", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # E380fe171 S_ENTRY -> MainActivity.onCreate: launch MainActivity
    # (MAIN/LAUNCHER intent filter, AndroidManifest.xml:61-65).
    r.launch(MAIN, "E380fe171")
    # E03c72cf9 MainActivity.onCreate -> MainActivity$1.<init>:
    # onCreate creates the data-loading task. Automatic.
    r.comment("onCreate creates the data-loading task", "E03c72cf9")
    # E745b85ef MainActivity$1.<init> -> doInBackground: automatic.
    r.comment("task doInBackground loads data", "E745b85ef")
    # Ed18978e9 doInBackground -> onPostExecute: the FIRST
    # instance's onPostExecute runs with savedInstanceState == null
    # (fresh pm-clear launch), so it takes the null branch, not the
    # parcel branch. Automatic.
    r.comment("first onPostExecute: savedInstanceState null", "Ed18978e9")
    # E6a0c67c7 (precondition + target): copy a file so pasteHelper
    # is non-null, then rotate so the recreated instance's
    # onPostExecute reads PASTEHELPER_BUNDLE from saved state.
    r.start_intent("E6a0c67c7", extras={"path": SOURCE_DIR},
                   component=MAIN)
    r.wait_for("E6a0c67c7", text=FILE_ROW, timeout=30)
    r.long_tap("E6a0c67c7", text=FILE_ROW)
    r.wait_for("E6a0c67c7", desc="Copy", timeout=30)
    r.tap("E6a0c67c7", desc="Copy")
    r.rotate("E6a0c67c7", orientation="landscape")
    # E6a0c67c7 (automatic part): the recreated instance's
    # onPostExecute reads the bundle; getParcelable unparcels
    # through PasteHelper$1.createFromParcel. Target edge.
    r.comment("recreated onPostExecute reads PASTEHELPER_BUNDLE; "
              "getParcelable unparcels via createFromParcel",
              "E6a0c67c7")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
