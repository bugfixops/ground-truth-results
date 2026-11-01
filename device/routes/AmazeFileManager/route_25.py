#!/usr/bin/env python3
"""AmazeFileManager route_25: CompressedExplorerFragment.onDestroyView.

Method: CompressedExplorerFragment.onDestroyView
Edge ids in order:
    E380fe171 Ec83d9c18 E45a4d528 E421bafb2 E50bfb580 Ef14e2b2b
    E6f8babbf E222d5cb1 E04be16b9 Efafabe30
Printed route: graphs/AmazeFileManager/scratch/route_print/
    CompressedExplorerFragment.onDestroyView.txt, verdict
    REACHABLE, 10 edges. Edge list identical to methods.csv
    route_edge_ids for CompressedExplorerFragment.onDestroyView
    and to d1_routes_draft.csv route_25.
Permissions: android.permission.READ_EXTERNAL_STORAGE and
    android.permission.WRITE_EXTERNAL_STORAGE, pre-granted by
    run_app.sh (the app's standard set; the archive is read from
    /sdcard and the fragment's cache entry lives under the app
    cache dir).
Fixtures: one archive file, supplied by the replay setup as
    fixtures/sample.zip (a minimal zip containing one text entry)
    and pushed by this script to /sdcard/Download/sample.zip.
    The script does NOT create the fixture itself: the harness
    push_fixture step copies the setup-supplied file, so a
    missing setup file fails loudly at the push step instead of
    silently scripting a different archive.
Setup: none beyond the standard config plus the fixture above.
Standard configuration: run_app.sh starts from `pm clear` and grants
    only the ROUTES.csv permissions.

Mapping notes (printed source):
  - ENV other_app: the route requires a zip/rar VIEW intent from
    another app (route_table.md note for this method; the edge
    carries no env field). The script reproduces that with
    start_intent: ACTION_VIEW, data file:///sdcard/Download/
    sample.zip, MIME application/zip, component MainActivity.
    MainActivity declares exactly this filter
    (AndroidManifest.xml: VIEW + application/zip, application/rar,
    application/x-gzip, application/x-rar-compressed,
    application/x-bzip2, application/x-xz,
    application/x-7z-compressed).
  - MainActivity.onCreate calls checkForExternalIntent(intent)
    (MainActivity.java:319). For ACTION_VIEW with a non-folder
    MIME type it sets openzip = true and zippath to the intent
    URI (MainActivity.java:510-526); goToMain then calls
    openCompressed(zippath) when openzip is set
    (MainActivity.java:797-798); openCompressed creates the
    CompressedExplorerFragment (MainActivity.java:1244).
  - CompressedExplorerFragment lifecycle (all framework after
    the fragment transaction): onCreate
    (CompressedExplorerFragment.java:128-131), onCreateView
    (:133-147), onActivityCreated (:163-222, which reads the
    archive path from the fragment arguments and seeds
    files[0] with the external-cache path for the archive name),
    onResume (:367-373), onPause (:375-380), onDestroyView
    (:354-365).
  - The destroy driver is a REAL navigation, not an assertion:
    pressing BACK while the archive fragment is at its root path
    runs MainActivity.onBackPressed's CompressedExplorerFragment
    branch (MainActivity.java:719-734): canGoBack() is false at
    the root (CompressedExplorerFragment.java:490-492, root
    relative path), so BACK either removes the fragment
    (transaction.remove, :728-731) or, in the openzip case,
    finishes the activity (:724-726). Either branch drives
    onPause -> onDestroyView. The script presses BACK once and
    logs the following onDestroyView edge as a comment, because
    the framework runs it as a consequence of that navigation.
  - Note on onDestroyView's body: it deletes files[0] only if
    that cache entry exists (CompressedExplorerFragment.java:
    361-363). The target of this route is onDestroyView itself,
    so the script does not depend on the cache file existing.
  - No fixed coordinates are used anywhere in this script.
"""

import argparse
import os
import sys

# Locate the app root (the directory containing device/harness/)
# from wherever this script is checked out: the helper output dir
# or the merged device/routes/AmazeFileManager/ location. The
# template's fixed four-dirname climb assumes only the merged
# location, so this ancestor search replaces it.
_here = os.path.dirname(os.path.abspath(__file__))
_root = _here
while not os.path.exists(os.path.join(_root, "device", "harness",
                                      "harness.py")):
    _parent = os.path.dirname(_root)
    if _parent == _root:
        raise RuntimeError("device/harness/harness.py not found above %s"
                           % _here)
    _root = _parent
sys.path.insert(0, _root)
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E380fe171", "Ec83d9c18", "E45a4d528", "E421bafb2", "E50bfb580",
    "Ef14e2b2b", "E6f8babbf", "E222d5cb1", "E04be16b9", "Efafabe30",
]

# Fixture supplied by the replay setup (see header). Destination
# is under Download, one of the standard fixture locations for
# this app's work-emulator setup.
FIXTURE_LOCAL = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "fixtures", "sample.zip")
FIXTURE_DEVICE_PATH = "/sdcard/Download/sample.zip"


def main(argv=None):
    parser = argparse.ArgumentParser(description="AmazeFileManager route_25")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_25", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # E380fe171 S_ENTRY -> MainActivity.onCreate: push the archive
    # fixture first (setup for the entry edge), then send the
    # other-app VIEW intent below, which is what launches
    # MainActivity in this route.
    r.push_fixture(FIXTURE_LOCAL, "E380fe171",
                   dest=FIXTURE_DEVICE_PATH)
    # Ec83d9c18 MainActivity.onCreate ->
    # MainActivity.checkForExternalIntent: the other-app VIEW
    # intent launches MainActivity (manifest VIEW filter for
    # application/zip) and onCreate calls checkForExternalIntent
    # (MainActivity.java:319). The intent itself is the action
    # for this edge; onCreate is automatic on receipt.
    r.start_intent("Ec83d9c18", action="android.intent.action.VIEW",
                   data="file://" + FIXTURE_DEVICE_PATH,
                   mime="application/zip",
                   component=args.package + "/.activities.MainActivity")
    # E45a4d528 MainActivity.checkForExternalIntent ->
    # MainActivity.openCompressed: for ACTION_VIEW with a
    # non-folder MIME type, checkForExternalIntent sets openzip
    # and zippath (MainActivity.java:510-526) and goToMain calls
    # openCompressed(zippath) (MainActivity.java:797-798).
    # Automatic after the intent; no further action.
    r.comment("VIEW zip sets openzip; goToMain calls openCompressed",
              "E45a4d528")
    # E421bafb2 MainActivity.openCompressed ->
    # CompressedExplorerFragment.<init>: openCompressed creates
    # the fragment (MainActivity.java:1244) and commits the
    # transaction. No user action.
    r.comment("openCompressed creates CompressedExplorerFragment",
              "E421bafb2")
    # E50bfb580 CompressedExplorerFragment.<init> ->
    # CompressedExplorerFragment.onCreate: framework fragment
    # lifecycle (CompressedExplorerFragment.java:128-131).
    # No user action.
    r.comment("framework runs CompressedExplorerFragment.onCreate",
              "E50bfb580")
    # Ef14e2b2b CompressedExplorerFragment.onCreate ->
    # CompressedExplorerFragment.onCreateView: framework fragment
    # lifecycle (CompressedExplorerFragment.java:133-147).
    # No user action.
    r.comment("framework runs CompressedExplorerFragment.onCreateView",
              "Ef14e2b2b")
    # E6f8babbf CompressedExplorerFragment.onCreateView ->
    # CompressedExplorerFragment.onActivityCreated: framework
    # fragment lifecycle (CompressedExplorerFragment.java:163-222).
    # No user action.
    r.comment("framework runs CompressedExplorerFragment."
              "onActivityCreated", "E6f8babbf")
    # E222d5cb1 CompressedExplorerFragment.onActivityCreated ->
    # CompressedExplorerFragment.onResume: framework fragment
    # lifecycle (CompressedExplorerFragment.java:367-373).
    # No user action.
    r.comment("framework runs CompressedExplorerFragment.onResume",
              "E222d5cb1")
    # E04be16b9 CompressedExplorerFragment.onResume ->
    # CompressedExplorerFragment.onPause: press BACK while the
    # archive fragment is at its root path. MainActivity.
    # onBackPressed's archive branch (MainActivity.java:719-734)
    # removes the fragment (or finishes the activity in the
    # openzip case); either way the fragment pauses. This is a
    # real navigation, not an asserted destroy.
    r.back("E04be16b9")
    # Efafabe30 CompressedExplorerFragment.onPause ->
    # CompressedExplorerFragment.onDestroyView: the BACK
    # navigation above drives the fragment teardown
    # (CompressedExplorerFragment.java:354-365). This is the
    # target edge. No further action, and no assertion is used
    # to claim the destroy: the BACK press is the driver.
    r.comment("BACK navigation drives CompressedExplorerFragment."
              "onDestroyView", "Efafabe30")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
