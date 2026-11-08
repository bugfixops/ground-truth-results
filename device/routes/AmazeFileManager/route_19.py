#!/usr/bin/env python3
"""AmazeFileManager route_19: Indicator$PendingRevealAnimator$1.onAnimationEnd.

Method: Indicator$PendingRevealAnimator$1.onAnimationEnd
Edge ids in order:
    E380fe171 E45d73a86 E7708bb4d E858ed758 E87d702ca Eaf0b6e7a
    E022e525c E5e5ec86b Ee5fbfeac E80182c61 Eba4ef0f3 E35472df8
Printed route: graphs/AmazeFileManager/scratch/route_print/
    Indicator_PendingRevealAnimator_1.onAnimationEnd.txt, verdict
    REACHABLE, 12 edges. The print's edge list matches
    methods.csv route_edge_ids and the d1_routes_draft.csv
    route_19 row exactly (no mismatch).
Permissions: READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
    (MainActivity's storage gate, MainActivity.java:436-484; the
    work-emulator baseline had storage granted before start).
Fixtures: none. Setup: none beyond the standard config. The
    script relies on the fresh-install tab state: with `pm clear`
    the current-tab preference is absent, so TabFragment reads
    DEFAULT_CURRENT_TAB = 1 (PreferenceUtils.java:14) and the
    Indicator syncs its current page to 1 at setViewPager time
    (see below); the swipe then moves to page 0.
Standard configuration: run_app.sh starts from `pm clear` and grants
    only the ROUTES.csv permissions (the storage pair above).

Mapping notes (printed source):
  - The animator chain starts from a real page change, not from
    launch alone. Indicator.setViewPager registers the Indicator
    as the ViewPager's OnPageChangeListener (Indicator.java:164
    -175, listener added at :167) and then calls
    setCurrentPageImmediate, which syncs currentPage to the
    ViewPager's current item (Indicator.java:242-251). That
    current item is 1 on a fresh install: TabFragment sets it
    from the default tab preference (TabFragment.java:106,148,
    DEFAULT_CURRENT_TAB = 1). So onPageSelected must fire for a
    DIFFERENT page, and setSelectedPage returns early when the
    new page equals the current page (Indicator.java:548-553).
  - The only in-app way to change pages is a horizontal swipe
    on the ViewPager (res/layout/tabfragment.xml: the pager is
    a DisablableViewPager filling the screen). The Indicator
    view itself is not tappable: it declares no clickable
    attribute (res/layout-v21/main_toolbar.xml:51-57) and no
    click or touch handler in Indicator.java, and no other code
    calls setCurrentItem (the only setCurrentItem calls in the
    app are TabFragment.java:148,174, both inside onCreateView
    before the Indicator listener is registered at :178).
  - HARNESS GAP, flagged for the device lead: the Amaze harness
    (device/harness/harness.py) exposes no horizontal-swipe
    method -- scroll_to swipes vertically only (harness.py
    :259-277) -- so the single tab-switch swipe below goes
    through Runner._shell, the same single-adb helper every
    public method uses, which means dry-run mode records it as
    a planned command and live runs log it as a step line like
    any other action. If the auditor rejects private-method use,
    the fix is a one-line public Runner.swipe() wrapping this
    exact call; the route itself is drivable and is NOT
    unscriptable. The swipe runs left-to-right (300 -> 900 at
    y=800) because moving a finger rightward drags page 1 off
    to reveal page 0; the reverse direction would move to a
    nonexistent page 2 and change nothing.
  - Once onPageSelected(0) fires, the rest is automatic:
    onPageSelected calls setSelectedPage (Indicator.java:203),
    setSelectedPage creates the move animator (:576), the move
    animator constructs the PendingRetreatAnimator (:587),
    whose constructor builds the PendingRevealAnimator array
    (:708,725), whose constructor registers the $1 listener
    (:778-784); the animation framework then calls the $1
    onAnimationEnd (:780-783), which resets the dot's reveal
    fraction and invalidates. No taps drive those edges.
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
    "E380fe171", "E45d73a86", "E7708bb4d", "E858ed758", "E87d702ca",
    "Eaf0b6e7a", "E022e525c", "E5e5ec86b", "Ee5fbfeac", "E80182c61",
    "Eba4ef0f3", "E35472df8",
]

PKG = "com.amaze.filemanager.debug"
MAIN = PKG + "/com.amaze.filemanager.activities.MainActivity"


def main(argv=None):
    parser = argparse.ArgumentParser(description="AmazeFileManager route_19")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_19", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # E380fe171 S_ENTRY -> MainActivity.onCreate: launch
    # MainActivity (MAIN/LAUNCHER, AndroidManifest.xml:61-65).
    r.launch(MAIN, "E380fe171")
    # E45d73a86 MainActivity.onCreate -> MainActivity.goToMain:
    # onCreate calls goToMain to display the TabFragment
    # (MainActivity.java:414,416,420). Wait for the tab pager
    # view (R.id.pager) so the fragment transaction has run.
    r.wait_for("E45d73a86", res_id="pager", timeout=30)
    # E7708bb4d MainActivity.goToMain -> TabFragment.<init>:
    # goToMain replaces the content frame with a TabFragment
    # (MainActivity.java:784). No user action.
    r.comment("goToMain replaces the content frame with TabFragment",
              "E7708bb4d")
    # E858ed758 TabFragment.<init> -> TabFragment.onCreateView:
    # fragment lifecycle. No user action.
    r.comment("fragment lifecycle: onCreateView", "E858ed758")
    # E87d702ca TabFragment.onCreateView -> Indicator
    # .setViewPager: onCreateView calls indicator.setViewPager
    # (TabFragment.java:178); setViewPager registers the
    # Indicator as page-change listener and syncs its current
    # page to the ViewPager's current item, which is 1 on a
    # fresh install (Indicator.java:167,242-251). No user action.
    r.comment("setViewPager registers the Indicator listener and "
              "syncs current page to 1", "E87d702ca")
    # Eaf0b6e7a Indicator.setViewPager -> Indicator
    # .onPageSelected: switch tabs with a left-to-right swipe
    # on the ViewPager, moving from page 1 to page 0; the
    # ViewPager then calls onPageSelected(0)
    # (Indicator.java:199-208). See the header harness-gap note:
    # the harness has no horizontal-swipe method, so this one
    # step uses Runner._shell, the same adb helper the public
    # methods use (dry-run records it as planned).
    r._shell(["input", "swipe", "300", "800", "900", "800", "300"],
             "Eaf0b6e7a", "swipe", "tab_switch_1_to_0")
    # E022e525c Indicator.onPageSelected -> Indicator
    # .setSelectedPage: onPageSelected calls setSelectedPage
    # (Indicator.java:203). Page 0 differs from the synced
    # current page 1, so the early return at :548 does not fire.
    r.comment("onPageSelected(0) calls setSelectedPage",
              "E022e525c")
    # E5e5ec86b Indicator.setSelectedPage -> Indicator
    # .createMoveSelectedAnimator: setSelectedPage creates the
    # move animator (Indicator.java:576) and starts it.
    # No user action.
    r.comment("setSelectedPage creates and starts the move animator",
              "E5e5ec86b")
    # Ee5fbfeac Indicator.createMoveSelectedAnimator -> Indicator
    # $PendingRetreatAnimator.<init>: the move animator setup
    # constructs the retreat animator (Indicator.java:587).
    # No user action.
    r.comment("move animator setup constructs PendingRetreatAnimator",
              "Ee5fbfeac")
    # E80182c61 Indicator$PendingRetreatAnimator.<init> ->
    # Indicator$PendingRevealAnimator.<init>: the retreat
    # animator constructor builds the reveal animator array
    # (Indicator.java:708,725). No user action.
    r.comment("retreat animator builds the reveal animator array",
              "E80182c61")
    # Eba4ef0f3 Indicator$PendingRevealAnimator.<init> ->
    # Indicator$PendingRevealAnimator$1.<init>: the reveal
    # animator constructor registers the $1 listener
    # (Indicator.java:778-784). No user action.
    r.comment("reveal animator registers the $1 listener", "Eba4ef0f3")
    # E35472df8 Indicator$PendingRevealAnimator$1.<init> ->
    # Indicator$PendingRevealAnimator$1.onAnimationEnd: the
    # animation framework calls onAnimationEnd when the reveal
    # animation completes (Indicator.java:780-783). No user action.
    r.comment("animation framework calls onAnimationEnd on completion",
              "E35472df8")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
