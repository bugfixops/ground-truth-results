#!/usr/bin/env python3
"""Vanilla-Music route_02: MediaScanner$MediaScanPlan$Step.<init>.

Method: MediaScanner$MediaScanPlan$Step.<init>
Edge ids in order (ROUTES.csv row route_02, verbatim):
    E47380ade E0fd35a14 Edb19c27c Eb3fb41dd E07460e2c E3d7f5df7
    E0a456cba E6757882b E4f573111 E7f45f4ed E2b03ae61 Ef5fc8ee9
    Ea80fe1e6 E38e95511 E83813753
Printed route source: the MediaScanner$MediaScanPlan$Step.<init> path
    row of graphs/Vanilla-Music/verification.csv (ref
    LibraryActivity.java:176-178; LibraryPagerAdapter.java:407,767,
    688; MediaAdapter.java:374; QueryTask.java:71; MediaLibrary.java:
    372,122; MediaScanner.java:151-155,239,377,782) plus the route_02
    row of device/routes/Vanilla-Music/ROUTES.csv. Steps read:
    launcher -> onCreate -> pager.setAdapter (ViewPager asks for the
    first pages, INFERRED) -> instantiateItem -> setPrimaryItem ->
    requeryIfNeeded -> postRunQuery -> handleMessage(MSG_RUN_QUERY) ->
    adapter.query() -> QueryTask.runQuery -> MediaLibrary.queryLibrary
    -> getBackend() (lazy init) -> MediaScanner.startQuickScan ->
    handleMessage(MSG_GUESS_QUICKSCAN) -> guessQuickScanPlan ->
    addNextStep -> new Step(...).
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none (ROUTES.csv fixtures column empty; no STATE file gate).
Setup: push fixtures/Music + media scan (run_app.sh does pm clear and
    the setup step before this script, so the script starts by
    launching the app).

UI mapping (layout XML and strings.xml read, nothing invented):
  - Launcher activity is LibraryActivity (AndroidManifest.xml:73-90,
    MAIN/LAUNCHER); component is <package>/.LibraryActivity.
  - The library-content wait target is the artist row "Aria North":
    the setup fixtures carry ID3v2.3 tags (verified by reading the
    fixture files: "01 Morning Light.mp3" has TIT2 "Morning Light",
    TPE1 "Aria North", TALB "Daybreak"), and the default first tab
    is Artists (LibraryPagerAdapter TITLES / DEFAULT_TAB_ORDER and
    LibraryActivity.java:194-198, default library_page = 0), so an
    "Aria North" row on screen proves the pager query committed and
    the library is populated. The quick scan that builds the scan
    plan runs during that same first query (MediaLibrary.getBackend
    lazy init), before rows render, so the wait is a safe
    post-condition for the target edge. There is no visible UI marker
    for the Step itself; it is an internal scan-plan object, so the
    final edge block records a UI dump instead of asserting text.
"""

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, _ROOT)

from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E47380ade", "E0fd35a14", "Edb19c27c", "Eb3fb41dd", "E07460e2c",
    "E3d7f5df7", "E0a456cba", "E6757882b", "E4f573111", "E7f45f4ed",
    "E2b03ae61", "Ef5fc8ee9", "Ea80fe1e6", "E38e95511", "E83813753",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Vanilla-Music route_02")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_02", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E47380ade S_ENTRY -> LibraryActivity.<init>: MAIN / LAUNCHER
    # intent starts LibraryActivity.
    r.launch(args.package + "/.LibraryActivity", "E47380ade")
    # E0fd35a14 LibraryActivity.<init> -> LibraryActivity.onCreate:
    # Activity lifecycle callback. Launch triggers the library pager
    # query and the quick scan; wait for a scanned artist row so the
    # script does not finish before the library is populated.
    r.wait_for("E0fd35a14", text="Aria North", timeout=60)
    # Edb19c27c LibraryActivity.onCreate ->
    # LibraryPagerAdapter.setPrimaryItem: pager.setAdapter(...): the
    # ViewPager calls PagerAdapter.setPrimaryItem (INFERRED, androidx
    # source not read). Framework-driven; no user action.
    r.comment("ViewPager setAdapter calls setPrimaryItem", "Edb19c27c")
    # Eb3fb41dd LibraryPagerAdapter.setPrimaryItem ->
    # LibraryPagerAdapter.requeryIfNeeded: Direct call. Automatic.
    r.comment("setPrimaryItem calls requeryIfNeeded", "Eb3fb41dd")
    # E07460e2c LibraryPagerAdapter.requeryIfNeeded ->
    # LibraryPagerAdapter.postRunQuery: Direct call. Automatic.
    r.comment("requeryIfNeeded calls postRunQuery", "E07460e2c")
    # E3d7f5df7 LibraryPagerAdapter.postRunQuery ->
    # LibraryPagerAdapter.handleMessage: mWorkerHandler.sendMessage
    # (MSG_RUN_QUERY, adapter): the query runs on the worker thread.
    # Automatic.
    r.comment("worker handler runs MSG_RUN_QUERY", "E3d7f5df7")
    # E0a456cba LibraryPagerAdapter.handleMessage -> MediaAdapter.query:
    # Virtual/interface call that can dispatch to this implementation
    # (through MediaAdapter.query). Automatic.
    r.comment("handleMessage dispatches adapter.query", "E0a456cba")
    # E6757882b MediaAdapter.query -> QueryTask.runQuery: Direct call.
    # Automatic.
    r.comment("query calls QueryTask.runQuery", "E6757882b")
    # E4f573111 QueryTask.runQuery -> MediaLibrary.queryLibrary:
    # Direct call. Automatic.
    r.comment("runQuery calls queryLibrary", "E4f573111")
    # E7f45f4ed MediaLibrary.queryLibrary -> MediaLibrary.getBackend:
    # Direct call (lazy init). Automatic.
    r.comment("queryLibrary calls getBackend", "E7f45f4ed")
    # E2b03ae61 MediaLibrary.getBackend ->
    # MediaScanner.startQuickScan: Direct call. Automatic.
    r.comment("getBackend starts quick scan", "E2b03ae61")
    # Ef5fc8ee9 MediaScanner.startQuickScan ->
    # MediaScanner.handleMessage: mHandler.sendMessageDelayed
    # (MSG_GUESS_QUICKSCAN, delay). Automatic.
    r.comment("quick scan posts MSG_GUESS_QUICKSCAN", "Ef5fc8ee9")
    # Ea80fe1e6 MediaScanner.handleMessage ->
    # MediaScanner.guessQuickScanPlan: Direct call. Automatic.
    r.comment("handleMessage calls guessQuickScanPlan", "Ea80fe1e6")
    # E38e95511 MediaScanner.guessQuickScanPlan ->
    # MediaScanner$MediaScanPlan.addNextStep: Direct call. Automatic.
    r.comment("guessQuickScanPlan calls addNextStep", "E38e95511")
    # E83813753 MediaScanner$MediaScanPlan.addNextStep ->
    # MediaScanner$MediaScanPlan$Step.<init>: Direct call. The Step is
    # internal (no UI marker); record a UI dump as run evidence.
    r.dump_ui("library", "E83813753")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
