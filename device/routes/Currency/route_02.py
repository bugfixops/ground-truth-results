#!/usr/bin/env python3
"""Currency route_02: AboutPreference.onBindDialogView.

Method: AboutPreference.onBindDialogView
Edge ids in order:
    E012ed474 Ee88066da Ef071a802 E4dd486ed E871f7284 Ed703ed01
    E089dafed E4ca94f24 E1725dbe1 Eb6828daa E49d83399 E383a2d57
    E2e1feed1 Ed6e8977b E2c2000b9
Printed route: graphs/Currency/scratch/route_print/AboutPreference.onBindDialogView.txt
    (REACHABLE, SOURCE_OK, ref AboutPreference.java:50).
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none.
Setup: network (ECB); cert issue on API<=27 images (ROUTES.csv setup
    column; no network step is needed on this route).
Launcher: org.billthefarmer.currency/.Main (AndroidManifest.xml:18-25,
    MAIN/LAUNCHER). run_app.sh already does pm clear, permission
    grants, fixture pushes, and per-app setup before this script, so
    the script performs only the route actions starting from launch.

Mapping notes:
  - Navigation to Settings is identical to route_01: the navigation
    icon (Main.java:288, icon only, no app-set description) is tapped
    by the AOSP Toolbar navigation button's framework content
    description "Navigate up" (verify against a live uiautomator
    dump before a real run; see route_01 notes), then the "Settings"
    text item in the PopupMenu (res/menu/navigation.xml).
  - The Settings list shows the preference rows from
    res/xml/preferences.xml; the About row title is "About"
    (res/values/strings.xml:69, pref_about). Tapping it opens the
    About dialog (dialogLayout @layout/about), and the framework
    binds the dialog view, which runs AboutPreference.
    onBindDialogView (AboutPreference.java:50). That final edge is
    driven by the tap itself, so no comment is needed for it beyond
    the tap block.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E012ed474", "Ee88066da", "Ef071a802", "E4dd486ed", "E871f7284",
    "Ed703ed01", "E089dafed", "E4ca94f24", "E1725dbe1", "Eb6828daa",
    "E49d83399", "E383a2d57", "E2e1feed1", "Ed6e8977b", "E2c2000b9",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Currency route_02")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_02", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E012ed474 S_ENTRY -> Main.<init>: launch the MAIN/LAUNCHER
    # activity (AndroidManifest.xml:18-25).
    r.launch(args.package + "/.Main", edge="E012ed474")
    # Ee88066da Main.<init> -> Main.onCreate: the system instantiates
    # Main, then calls onCreate (Main.java:242). No user action.
    r.comment("system instantiates Main, then onCreate",
              edge="Ee88066da")
    # Ef071a802 Main.onCreate -> Main.onResume: onStart -> onResume
    # (Main.java:369). No user action.
    r.comment("onStart -> onResume", edge="Ef071a802")
    # E4dd486ed Main.onResume -> S_MAIN_DISPLAY: Main becomes visible
    # in DISPLAY_MODE (Main.java:351-352; pm clear leaves no
    # selection). No user action.
    r.comment("Main visible in DISPLAY_MODE", edge="E4dd486ed")
    # E871f7284 S_MAIN_DISPLAY -> Main.lambda$onCreate$0: tap the
    # navigation icon at the left of the action bar (Main.java:288).
    r.tap(edge="E871f7284", desc="Navigate up")
    # Ed703ed01 Main.lambda$onCreate$0 -> S_NAV_POPUP: popup.show()
    # (Main.java:291-294). Automatic after the tap. No further action.
    r.comment("PopupMenu shown (Settings / Help)", edge="Ed703ed01")
    # E089dafed S_NAV_POPUP -> Main.onMenuItemClick: tap the Settings
    # item in the popup (res/menu/navigation.xml, Main.java:818).
    r.tap(edge="E089dafed", text="Settings")
    # E4ca94f24 Main.onMenuItemClick -> Main.onSettingsClick: switch
    # case R.id.action_settings (Main.java:829-830). Automatic after
    # the tap. No further action.
    r.comment("switch case R.id.action_settings", edge="E4ca94f24")
    # E1725dbe1 Main.onSettingsClick -> SettingsActivity.<init>:
    # startActivity(SettingsActivity) (Main.java:1132-1133).
    # Automatic after the tap. No further action.
    r.comment("startActivity(SettingsActivity)", edge="E1725dbe1")
    # Eb6828daa SettingsActivity.<init> -> SettingsActivity.onCreate:
    # the system instantiates SettingsActivity, then onCreate
    # (SettingsActivity.java:41). No user action.
    r.comment("system instantiates SettingsActivity, then onCreate",
              edge="Eb6828daa")
    # E49d83399 SettingsActivity.onCreate -> SettingsFragment.<init>:
    # replace(android.R.id.content, new SettingsFragment())
    # (SettingsActivity.java:79-81). No user action.
    r.comment("fragment transaction replaces content with "
              "SettingsFragment", edge="E49d83399")
    # E383a2d57 SettingsFragment.<init> -> SettingsFragment.onCreate:
    # the fragment transaction commits, fragment onCreate runs. No
    # user action.
    r.comment("fragment transaction commits: fragment onCreate",
              edge="E383a2d57")
    # E2e1feed1 SettingsFragment.onCreate -> SettingsFragment.onResume:
    # the fragment resumes with the activity. No user action.
    r.comment("fragment resumes with the activity", edge="E2e1feed1")
    # Ed6e8977b SettingsFragment.onResume -> S_SETTINGS: the Settings
    # list is shown (SettingsFragment.java:76-81). No user action.
    r.comment("Settings list shown", edge="Ed6e8977b")
    # E2c2000b9 S_SETTINGS -> AboutPreference.onBindDialogView: tap
    # the About row (res/xml/preferences.xml, title "About"); the
    # dialog view is bound when the dialog is shown
    # (AboutPreference.java:50). This is the target edge.
    r.tap(edge="E2c2000b9", text="About")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
