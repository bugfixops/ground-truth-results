#!/usr/bin/env python3
"""AmazeFileManager route_09: PasteHelper.<init>(Parcel).

Method: PasteHelper.<init>(Parcel)
Edge ids in order:
    E380fe171 E03c72cf9 E745b85ef Ed18978e9 E6a0c67c7 E2032b774
Printed route: MainActivity.java:366 (source ref); edge list
identical to the AmazeFileManager ROUTES.csv route_09 row and to
the trigger graph.
Permissions: android.permission.WRITE_EXTERNAL_STORAGE only (the
app's declared set), pre-granted by run_app.sh: the copy flow
reads the Download file list.
Fixtures: amaze_search.txt, pushed by run_app.sh to
/sdcard/Download/amaze_search.txt before the script (repo fixture
entry in ROUTES.csv); the script does NOT push it.
Setup: run_app.sh pushes the fixture before the script (see above).
Standard configuration: run_app.sh starts from `pm clear` and grants
only the ROUTES.csv permissions.

Mapping notes (printed source):
  - PRECONDITION (the whole route): MainActivity.onSaveInstanceState
    saves the paste helper only when it is non-null
    (MainActivity.java:1077-1079: if (pasteHelper != null)
    outState.putParcelable(PASTEHELPER_BUNDLE, pasteHelper)).
    The paste helper becomes non-null when the user copies (or
    cuts) a file: MainFragment's action-mode Copy handler builds
    new PasteHelper(OPERATION_COPY, copies) and calls
    getMainActivity().setPaste(pasteHelper)
    (MainFragment.java:719-729). This script therefore copies a
    file BEFORE recreating, so the saved state carries the parcel.
  - RECREATION: MainActivity declares NO android:configChanges
    (AndroidManifest.xml:56-65), so rotation destroys and
    recreates it (default behavior). The recreated instance's
    MainActivity$1 data-loading task runs onPostExecute, which
    reads the bundle when savedInstanceState != null
    (MainActivity.java:425: pasteHelper =
    savedInstanceState.getParcelable(PASTEHELPER_BUNDLE)) and
    Bundle.getParcelable unparcels it through
    PasteHelper$1.createFromParcel (E6a0c67c7), whose body
    constructs PasteHelper from the Parcel (E2032b774, target).
  - COPY UI: the contextual action-mode Copy item shows ONLY its
    icon (contextual.xml:28-31: showAsAction="always" without
    withText), so it has no "Copy" text to tap — AppCompat
    exposes the item title as the button's content-desc, so the
    script waits for and taps desc="Copy". If the real run shows
    no such desc, the wait fails loudly (unclear, never wrong).
  - The copy + rotate steps are preconditions for E6a0c67c7 (the
    recreated onPostExecute reading the bundle), so they are
    logged under that edge; the first instance's task edges
    (E03c72cf9/E745b85ef/Ed18978e9) are automatic comments.
  - This route was unscriptable ("no rotate/kill/destroy-while-
    stopped op") until the harness gained rotate(); it converts
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
    "E2032b774",
]

PKG = "com.amaze.filemanager.debug"
MAIN = PKG + "/com.amaze.filemanager.activities.MainActivity"
SOURCE_DIR = "/sdcard/Download"
FILE_ROW = "amaze_search.txt"


def main(argv=None):
    parser = argparse.ArgumentParser(description="AmazeFileManager route_09")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_09", EDGE_IDS, args.log,
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
    # E6a0c67c7 (precondition): copy a file so pasteHelper is
    # non-null, then rotate so the recreated instance's
    # onPostExecute reads PASTEHELPER_BUNDLE from saved state.
    # Navigate to Download (path extra, as in route_28).
    r.start_intent("E6a0c67c7", extras={"path": SOURCE_DIR},
                   component=MAIN)
    r.wait_for("E6a0c67c7", text=FILE_ROW, timeout=30)
    # Long-press the row: action mode opens; tap Copy (icon-only
    # button, content-desc "Copy") -> setPaste(pasteHelper).
    r.long_tap("E6a0c67c7", text=FILE_ROW)
    r.wait_for("E6a0c67c7", desc="Copy", timeout=30)
    r.tap("E6a0c67c7", desc="Copy")
    # Rotate: MainActivity has no configChanges, so this destroys
    # and recreates it; onSaveInstanceState saves the non-null
    # pasteHelper into PASTEHELPER_BUNDLE first.
    r.rotate("E6a0c67c7", orientation="landscape")
    # E6a0c67c7 (automatic part): the recreated instance's
    # onPostExecute reads the bundle; getParcelable unparcels
    # through PasteHelper$1.createFromParcel.
    r.comment("recreated onPostExecute reads PASTEHELPER_BUNDLE; "
              "getParcelable unparcels via createFromParcel",
              "E6a0c67c7")
    # E2032b774 PasteHelper$1.createFromParcel -> PasteHelper.<init>
    # (Parcel): CREATOR.createFromParcel constructs PasteHelper
    # from the Parcel. Automatic; this is the target edge.
    r.comment("createFromParcel constructs PasteHelper from Parcel",
              "E2032b774")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
