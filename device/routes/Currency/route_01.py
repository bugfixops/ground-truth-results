#!/usr/bin/env python3
"""Currency route_01: AboutPreference.<init>.

Method: AboutPreference.<init>
Edge ids in order:
    E012ed474 Ee88066da Ef071a802 E4dd486ed E871f7284 Ed703ed01
    E089dafed E4ca94f24 E1725dbe1 Eb6828daa E49d83399 E383a2d57
    Ec05657b8
Printed route: graphs/Currency/scratch/route_print/AboutPreference.<init>.txt
    (REACHABLE, SOURCE_OK, ref SettingsFragment.java:48).
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none.
Setup: network (ECB); cert issue on API<=27 images (ROUTES.csv setup
    column; no network step is needed on this route).
Launcher: org.billthefarmer.currency/.Main (AndroidManifest.xml:18-25,
    MAIN/LAUNCHER). run_app.sh already does pm clear, permission
    grants, fixture pushes, and per-app setup before this script, so
    the script performs only the route actions starting from launch.

Mapping notes:
  - Main sets only the navigation icon (Main.java:288,
    toolbar.setNavigationIcon(R.drawable.ic_menu_white_24dp)); no
    app-set text, id, or content description exists for it in source.
    The script taps the AOSP Toolbar navigation button by its
    framework content description "Navigate up". Verify that
    description against a live uiautomator dump before a real run;
    it is the one selector on this route not fixed by app source.
  - The navigation PopupMenu (Main.java:291-294, res/menu/
    navigation.xml) shows the text items "Settings" and "Help"
    (res/values/strings.xml:8,7); tapping "Settings" drives
    Main.onMenuItemClick case R.id.action_settings (Main.java:829).
  - SettingsActivity replaces its content with SettingsFragment
    (SettingsActivity.java:79-81); SettingsFragment.onCreate inflates
    res/xml/preferences.xml (SettingsFragment.java:48), and the
    framework constructs AboutPreference(Context, AttributeSet) for
    the org.billthefarmer.currency.AboutPreference element there.
    That final edge has no user action, so it is logged with
    r.comment.
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
    "E49d83399", "E383a2d57", "Ec05657b8",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Currency route_01")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_01", edge_ids=EDGE_IDS,
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
    # Ec05657b8 SettingsFragment.onCreate -> AboutPreference.<init>:
    # addPreferencesFromResource(R.xml.preferences) inflates the
    # AboutPreference element, constructed by the framework through
    # reflection (SettingsFragment.java:48). Framework action; no
    # user action. This is the target edge.
    r.comment("framework inflates AboutPreference from preferences.xml",
              edge="Ec05657b8")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
