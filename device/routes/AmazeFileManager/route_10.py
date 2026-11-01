#!/usr/bin/env python3
"""AmazeFileManager route_10: PasteHelper.writeToParcel.

Method: PasteHelper.writeToParcel
Edge ids in order:
    E795acdbd E32e65cb4
Printed route: the PasteHelper.writeToParcel section of the Amaze
    route print (scratch/route_print/PasteHelper.writeToParcel.txt),
    verdict REACHABLE, 2 edges, final-sample route_table verdict
    CORRECT ("No fix needed").
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (manifest
    declaration; the ROUTES.csv permissions column for this route).
    run_app.sh grants only the ROUTES.csv permissions, so the script
    itself performs no grant.
Fixtures: one local file named pastefixture.txt, pushed by the run
    harness to external storage before this script runs (work-emulator
    setup for this app is "push fixtures"), so that it appears in the
    folder MainActivity opens by default. The script deliberately does
    NOT call push_fixture: no fixture file lives in this helper dir,
    and inventing a local path would fail a real run. The script waits
    for the fixture name and fails loudly if it is not listed.
Setup: a pending copy (state_kinds session in the draft ROUTES.csv
    row). The script CREATES that state first via UI, before the
    route's final steps: long-press the fixture row to select it, then
    tap Copy in the contextual menu. Only then does it drive the
    lifecycle step that parcels the helper.
Standard configuration: run_app.sh starts from `pm clear` and grants
    only the ROUTES.csv permissions (WRITE_EXTERNAL_STORAGE here).

Mapping notes (printed source):
  - MainActivity is the MAIN/LAUNCHER activity
    (AndroidManifest.xml:58-65); the script launches
    <package>/.activities.MainActivity.
  - List long-press selects: RecyclerAdapter.java:543-549 sets a row
    long-click listener that calls toggleChecked; toggleChecked
    (RecyclerAdapter.java:162-199, esp. 192-197) starts the support
    ActionMode when nothing is selected yet. The ActionMode inflates
    R.menu.contextual (MainFragment.java:482-496).
  - Contextual Copy creates the pending state: menu/contextual.xml
    gives item R.id.cpy the title @string/copy, and strings.xml:93
    gives copy = "Copy"; MainFragment.java:719-728 handles R.id.cpy
    by building new PasteHelper(op, copies) and calling
    getMainActivity().setPaste(pasteHelper), so after this tap
    MainActivity.pasteHelper is non-null.
  - HOME drives the route's first edge: pressing HOME moves
    MainActivity out of the foreground, and the framework calls
    onSaveInstanceState before onStop. MainActivity.java:1077-1078
    then runs only because pasteHelper is non-null:
    if (pasteHelper != null)
        outState.putParcelable(PASTEHELPER_BUNDLE, pasteHelper);
    The Bundle parcel step is the route's second edge
    (E32e65cb4), logged with r.comment because no further user
    action drives it. This is navigation away from the activity,
    NOT rotation or process death, so the harness HOME key is a
    legitimate trigger for writeToParcel (contrast route_09, where
    the matching read-back needs recreation with saved state).
  - No fixed coordinates are used: every tap is by exact row/menu
    text, which the layout and menu sources verify.
"""

import argparse
import os
import sys

# This script lives in helper/d3-r06-r10/, three levels below the
# AmazeFileManager work dir that contains the device/ package; the
# template's path arithmetic assumed a device/ location, so the
# equivalent root is computed from this file instead.
sys.path.insert(
    0,
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E795acdbd", "E32e65cb4",
]

FIXTURE_NAME = "pastefixture.txt"


def main(argv=None):
    parser = argparse.ArgumentParser(description="AmazeFileManager route_10")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_10", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # E795acdbd S_ENTRY -> MainActivity.onSaveInstanceState: setup
    # for this edge (the edge itself is entered by the HOME key at
    # the end of this block). Launch MainActivity first.
    r.launch(args.package + "/.activities.MainActivity", "E795acdbd")
    # Setup, still logged under E795acdbd (Runner requires every
    # action to carry an edge id from this route): wait for the
    # run-harness fixture in the default folder listing.
    r.wait_for("E795acdbd", text=FIXTURE_NAME)
    # Long-press the fixture row: RecyclerAdapter.java:543-549
    # long-click -> toggleChecked -> ActionMode (contextual menu).
    r.long_tap("E795acdbd", text=FIXTURE_NAME)
    # Tap Copy in the contextual menu: menu/contextual.xml R.id.cpy
    # title @string/copy = "Copy" (strings.xml:93); MainFragment
    # .java:719-728 builds the PasteHelper and setPaste()s it, so
    # MainActivity.pasteHelper is now non-null (the pending-copy
    # state this route requires).
    r.tap("E795acdbd", text="Copy")
    # HOME key: MainActivity leaves the foreground, so the framework
    # calls onSaveInstanceState -- this enters edge E795acdbd's
    # destination. No rotation, kill, or other unsupported op is used.
    r.key("HOME", "E795acdbd")
    # E32e65cb4 MainActivity.onSaveInstanceState ->
    # PasteHelper.writeToParcel: MainActivity.java:1077-1078 puts the
    # non-null pasteHelper into the outState Bundle, which parcels
    # it. Framework step; no user action. This is the target edge.
    r.comment("onSaveInstanceState putParcelable parcels pasteHelper",
              "E32e65cb4")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
