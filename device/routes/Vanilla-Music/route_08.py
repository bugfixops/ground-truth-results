#!/usr/bin/env python3
"""Vanilla-Music route_08: Limiter.<init>.

Method: Limiter.<init>
Edge ids (in order, from ROUTES.csv):
    E47380ade E29472d10 E80427a98 E89b88b79 E36b45c2b Ec1e9dbd8
    E1697db29 Eb1aa9eb8 E996c730a
Printed route source:
    verification.csv path row (Limiter.<init>, SOURCE):
      ref: SlidingTabLayout.java:217,311-320,313-319;
        LibraryPagerAdapter.java:333; FileSystemAdapter.java:179,360,
        350
      Steps read: launcher -> onResume@LibraryActivity -> S_LIBRARY
        -> tap the Files tab title -> ViewPager.setCurrentItem
        (INFERRED) -> instantiateItem@FILE -> new
        FileSystemAdapter(...) -> buildHomeLimiter ->
        buildLimiter(File) -> new Limiter(...). Steps that run
        through androidx ViewPager rest on INFERRED claims (androidx
        source not read).
    ROUTES.csv row: env_kinds=(none), state_kinds=(none),
      permissions=(none), fixtures=(none),
      setup="push fixtures/Music + media scan", status=scripted.
Permissions: none (ROUTES.csv lists none; storage is granted during
    setup, not by this route).
Fixtures: none (STATE file gates: none).
Setup (run by run_app.sh before this script): pm clear, then push
    fixtures/Music + media scan.
UI steps: launch, wait for the library pager, tap the Files tab
    (tab title R.string.files = "Files", LibraryPagerAdapter
    .TITLES[TYPE_FILE]). The Files page build then runs
    FileSystemAdapter -> buildHomeLimiter -> buildLimiter -> new
    Limiter with no further user action.
Harness notes: launch() takes (component, edge); every other call
    below passes edge= explicitly. All edges after the tab tap are
    framework/adapter/call edges with no user action, so they are
    comment() blocks.
"""

import argparse
import os
import sys

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_ROOT = _SCRIPT_DIR
for _ in range(3):
    _ROOT = os.path.dirname(_ROOT)
# Insert only a root that really contains device/harness: inserting a
# wrong root first would cache a namespace "device" package and break
# the fallback import below.
_CANDIDATES = []
if os.path.isfile(os.path.join(_ROOT, "device", "harness", "harness.py")):
    _CANDIDATES.append(_ROOT)
else:
    # Helper-dir copies (e.g. work/Vanilla-Music/helper/...) are not
    # under device/routes/, so the four-dirname root above is not a
    # repo root there. Fall back to a stage checkout found under an
    # ancestor (device/stage/device/harness). In the merged layout
    # (device/routes/Vanilla-Music/route_NN.py) the primary root
    # contains device/harness and this branch never runs.
    _dir = _SCRIPT_DIR
    while True:
        _cand = os.path.join(_dir, "device", "stage")
        if os.path.isfile(os.path.join(_cand, "device", "harness",
                                       "harness.py")):
            _CANDIDATES.append(_cand)
            break
        _parent = os.path.dirname(_dir)
        if _parent == _dir:
            break
        _dir = _parent
for _c in _CANDIDATES:
    sys.path.insert(0, _c)
from device.harness.harness import Runner

EDGE_IDS = [
    "E47380ade", "E29472d10", "E80427a98", "E89b88b79", "E36b45c2b",
    "Ec1e9dbd8", "E1697db29", "Eb1aa9eb8", "E996c730a",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    args = ap.parse_args()
    r = Runner(package=args.package, route="route_08", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E47380ade -- MAIN / LAUNCHER intent starts LibraryActivity.
    r.launch("%s/.LibraryActivity" % args.package, edge="E47380ade")
    # E29472d10 -- Activity lifecycle callback (no user action).
    r.comment("LibraryActivity onResume (lifecycle)", edge="E29472d10")
    # E80427a98 -- LibraryActivity is resumed and shown (default tab
    # Artists: library_page = 0). Wait for the library pager.
    r.wait_for(edge="E80427a98", res_id="pager", timeout=30)
    # E89b88b79 -- Tap a tab title of the tab strip: the Files tab
    # (R.string.files = "Files").
    r.tap(edge="E89b88b79", text="Files")
    # E36b45c2b -- mViewPager.setCurrentItem(i): the ViewPager
    # creates the page of the tapped tab (and its neighbours).
    # Guard: the tapped tab is of type TYPE_FILE (the Files tab).
    # Framework-driven; no user action beyond the tab tap above.
    r.comment("ViewPager creates FILE page (framework)", edge="E36b45c2b")
    # Ec1e9dbd8 -- the page of this tab type is built.
    r.comment("FileSystemAdapter created for FILE page", edge="Ec1e9dbd8")
    # E1697db29 -- Direct call.
    r.comment("FileSystemAdapter.buildHomeLimiter called", edge="E1697db29")
    # Eb1aa9eb8 -- Direct call.
    r.comment("FileSystemAdapter.buildLimiter(File) called", edge="Eb1aa9eb8")
    # E996c730a -- Direct call to Limiter.<init> (target).
    r.comment("Limiter created (target)", edge="E996c730a")
    r.screenshot("route_08_end", edge="E996c730a")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
