#!/usr/bin/env python3
"""AmazeFileManager route_13: ProcessViewerFragment$CustomServiceConnection$1.<init>.

Method: ProcessViewerFragment$CustomServiceConnection$1.<init>
Edge ids in order:
    E380fe171 E804b4efa E3119bc2f E1ade216d Ef5ec4fc0 E5c30adbb E91123cce
Printed route: graphs/AmazeFileManager/scratch/route_print/
    ProcessViewerFragment_CustomServiceConnection_1.<init>.txt,
    verdict REACHABLE, 7 edges. The print's edge list matches
    methods.csv route_edge_ids and the d1_routes_draft.csv route_13
    row exactly (no mismatch).
Permissions: READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
    (MainActivity's storage gate, MainActivity.java:436-484; the
    work-emulator baseline had storage granted before start).
Fixtures: none. Setup: none beyond the standard config.
Standard configuration: run_app.sh starts from `pm clear` and grants
    only the ROUTES.csv permissions (the storage pair above).

Mapping notes (printed source):
  - The fragment opens from an intent extra, NOT only from a
    notification tap: MainActivity reads the extra at
    MainActivity.java:309
    (getBooleanExtra(KEY_INTENT_PROCESS_VIEWER, false)), where
    KEY_INTENT_PROCESS_VIEWER is the literal "openprocesses"
    (MainActivity.java:231). The services put the same extra on
    their notification intents (CopyService.java:123 and the
    parallel lines in ExtractService, ZipService, EncryptService,
    DecryptService), which is why the UI map says "notification
    or intent extra" -- but the extra alone is sufficient, so the
    script sends it directly with start_intent and never touches
    system notification UI. With a fresh process (pm clear) the
    onCreate path runs: the background task's onPostExecute takes
    the openProcesses branch and replaces the content frame
    (MainActivity.java:388-397, transaction.replace at :390).
    If the activity were already running (singleInstance), the
    same extra is handled by onNewIntent (MainActivity.java:1588-1596).
  - onResume binds five in-package services (ProcessViewerFragment
    .java:159-171: CopyService, ExtractService, ZipService,
    EncryptService, DecryptService with mCopyConnection and
    friends); the framework calls onServiceConnected when each
    binding succeeds. No fixture or running service is needed for
    the target edge: onServiceConnected unconditionally executes
    the setProgressListener call at ProcessViewerFragment.java:416
    after its data-package loop, so the anonymous
    ProgressListener (the $1 class) is constructed even when no
    service currently reports progress.
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
    "E380fe171", "E804b4efa", "E3119bc2f", "E1ade216d", "Ef5ec4fc0",
    "E5c30adbb", "E91123cce",
]

PKG = "com.amaze.filemanager.debug"
MAIN = PKG + "/com.amaze.filemanager.activities.MainActivity"


def main(argv=None):
    parser = argparse.ArgumentParser(description="AmazeFileManager route_13")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_13", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # E380fe171 S_ENTRY -> MainActivity.onCreate: start MainActivity
    # with the boolean extra the fragment branch reads
    # (MainActivity.java:309, key "openprocesses" at :231).
    # extras_args carries the boolean extra: start_intent's extras
    # dict only emits string extras, so --ez is passed through here.
    r.start_intent("E380fe171", component=MAIN,
                   extras_args=["--ez", "openprocesses", "true"])
    # E804b4efa MainActivity.onCreate -> ProcessViewerFragment.<init>:
    # the background task's onPostExecute takes the openProcesses
    # branch and replaces R.id.content_frame with the fragment
    # (MainActivity.java:388-397, :390). No user action.
    r.comment("onPostExecute openProcesses branch replaces content "
              "frame with ProcessViewerFragment", "E804b4efa")
    # E3119bc2f ProcessViewerFragment.<init> ->
    # ProcessViewerFragment.onCreateView: fragment lifecycle.
    # No user action.
    r.comment("fragment lifecycle: onCreateView", "E3119bc2f")
    # E1ade216d ProcessViewerFragment.onCreateView ->
    # ProcessViewerFragment.onActivityCreated: fragment lifecycle.
    # No user action.
    r.comment("fragment lifecycle: onActivityCreated", "E1ade216d")
    # Ef5ec4fc0 ProcessViewerFragment.onActivityCreated ->
    # ProcessViewerFragment.onResume: fragment lifecycle.
    # No user action.
    r.comment("fragment lifecycle: onResume", "Ef5ec4fc0")
    # E5c30adbb ProcessViewerFragment.onResume ->
    # ProcessViewerFragment$CustomServiceConnection.onServiceConnected:
    # onResume binds 5 services (ProcessViewerFragment.java:159-171);
    # the framework calls onServiceConnected when binding succeeds.
    # No user action.
    r.comment("onResume binds 5 services; framework calls "
              "onServiceConnected on success", "E5c30adbb")
    # E91123cce ProcessViewerFragment$CustomServiceConnection.
    # onServiceConnected -> ProcessViewerFragment$CustomServiceConnection
    # $1.<init>: onServiceConnected unconditionally constructs the
    # anonymous ProgressListener (ProcessViewerFragment.java:416).
    # No user action. This is the target edge.
    r.comment("onServiceConnected constructs anonymous ProgressListener "
              "at ProcessViewerFragment.java:416", "E91123cce")
    r.screenshot("route_13_process_viewer", "E91123cce")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
