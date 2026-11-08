#!/usr/bin/env python3
"""Device route script for Currency route_09.

Method: HelpActivity.onOptionsItemSelected
Edge ids, in order: E012ed474 Ee88066da Ef071a802 E4dd486ed E871f7284
    Ed703ed01 E089dafed Ed89cea6b Ebaddd7d9 Ede1ffb06 Ee407b707
    E38662657
Printed route file: graphs/Currency/scratch/route_print/HelpActivity.onOptionsItemSelected.txt
Permissions: none
Fixtures: none
Setup: network (ECB); cert issue on API<=27 images

Navigation note: Main's navigation icon is the framework Toolbar
navigation button (Main.java:288, toolbar found by the android
"action_bar" id). It has no text and no app res_id in the source, so
it is tapped by the standard AOSP navigation content description
"Navigate up". If a real-device dump shows that button with an empty
description, the merger should replace that one tap with a top-left
fixed-coordinate tap (with a why string) instead; see REPORT.md.
HelpActivity's own Up arrow is the framework ActionBar home-as-up
button (HelpActivity.java:97-99, setDisplayHomeAsUpEnabled(true)),
which carries the same standard "Navigate up" description.
"""

import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from device.harness import Runner  # noqa: E402

EDGE_IDS = ["E012ed474", "Ee88066da", "Ef071a802", "E4dd486ed", "E871f7284",
            "Ed703ed01", "E089dafed", "Ed89cea6b", "Ebaddd7d9", "Ede1ffb06",
            "Ee407b707", "E38662657"]
LAUNCHER = "org.billthefarmer.currency/.Main"


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    r = Runner(package=args.package, route="route_09", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, outdir=args.outdir,
               adb=args.adb)
    try:
        # E012ed474: Tap the Currency icon in the launcher
        # (MAIN/LAUNCHER intent filter; Main is the launcher activity
        # in AndroidManifest.xml).
        r.launch(LAUNCHER, edge="E012ed474")

        # Ee88066da: Main.<init> -> Main.onCreate. Lifecycle edge:
        # the system instantiates Main, then calls onCreate. No user
        # action exists.
        r.comment("lifecycle: system instantiates Main, then onCreate",
                  edge="Ee88066da")

        # Ef071a802: Main.onCreate -> Main.onResume (onStart -> onResume).
        # Lifecycle edge: no user action exists.
        r.comment("lifecycle: onStart -> onResume", edge="Ef071a802")

        # E4dd486ed: Main.onResume -> S_MAIN_DISPLAY. Main becomes
        # visible in DISPLAY_MODE (fresh pm clear leaves the select
        # list empty, Main.java:351-352). No user action exists.
        r.comment("automatic: Main visible in DISPLAY_MODE",
                  edge="E4dd486ed")

        # E871f7284: S_MAIN_DISPLAY -> Main.lambda$onCreate$0. Tap the
        # navigation icon at the left of the action bar
        # (Main.java:288-295, ic_menu_white_24dp). See the header note
        # on the "Navigate up" description.
        r.tap(desc="Navigate up", edge="E871f7284")

        # Ed703ed01: Main.lambda$onCreate$0 -> S_NAV_POPUP. The tap
        # shows a PopupMenu inflated from res/menu/navigation.xml
        # (Settings / Help). Wait for the Help item to appear.
        r.wait_for(text="Help", edge="Ed703ed01")

        # E089dafed: S_NAV_POPUP -> Main.onMenuItemClick. Tap "Help"
        # in the popup (navigation.xml item action_help, title
        # @string/help = "Help").
        r.tap(text="Help", edge="E089dafed")

        # Ed89cea6b: Main.onMenuItemClick -> Main.onHelpClick. Switch
        # case R.id.action_help (Main.java:825-826). Automatic
        # consequence of tapping Help. No user action exists.
        r.comment("automatic: popup case action_help calls onHelpClick",
                  edge="Ed89cea6b")

        # Ebaddd7d9: Main.onHelpClick -> HelpActivity.<init>. Intent
        # edge: startActivity(HelpActivity) (Main.java:1122-1123).
        # Automatic consequence of onHelpClick.
        r.comment("automatic: onHelpClick starts HelpActivity",
                  edge="Ebaddd7d9")

        # Ede1ffb06: HelpActivity.<init> -> HelpActivity.onCreate.
        # Lifecycle edge: the system instantiates HelpActivity, then
        # onCreate. No user action exists.
        r.comment("lifecycle: system instantiates HelpActivity, then "
                  "onCreate", edge="Ede1ffb06")

        # Ee407b707: HelpActivity.onCreate -> S_HELP. Help text is
        # shown (layout help.xml, TextView id "help") with an Up arrow
        # (HelpActivity.java:86-99). Wait for the help TextView.
        r.wait_for(res_id="help", edge="Ee407b707")

        # E38662657: S_HELP -> HelpActivity.onOptionsItemSelected.
        # Tap the Up arrow (HelpActivity.java:99,104): the framework
        # ActionBar home-as-up button, content-desc "Navigate up".
        # Its handler finishes the activity (android.R.id.home case).
        r.tap(desc="Navigate up", edge="E38662657")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
