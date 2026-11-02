#!/usr/bin/env python3
"""Replay script for hash-checker route_07.

Method: WebFragment.getMenuResId
Edge ids (exact, from ROUTES.csv, in route order):
    E372472a8 E3101d0cd Edeb6bd90 E56501d6f E9e141121 E3755babd
    E9574aba4 E3ac2e1c9 E59c1e403 E79b435a7 E98e98419 E30bb0ca3
    E58fc7a37 E0848626c Eed97dffc E329fd909 Eb87d737f E07bec56b
    E33bc58cc Ec8dd5d3f Ea6ffa5e2 E0f814afb E4b722c5e E9c05dfdc
    E48baef20 E85c92c29 E429186ad E645d374b
Printed route file:
    graphs/hash-checker/scratch/route_print/WebFragment.getMenuResId.txt
Permissions: (none)
Fixtures: (none)
Setup: any file as input (fixtures)

Flow: launch, tap the Settings action-bar item, tap the "Privacy Policy"
preference, tap the single "Privacy Policy" link row in the privacy
sheet; MainActivity shows WebFragment, whose menu creation calls
getMenuResId (returning menu_webview).

Action-bar items are icon-only, so they are tapped by content-desc
(their menu title) with a resource-id fallback: tap_menu tries the
desc first and, only if the node is not found on a real device, falls
back to the menu item id. In dry-run mode the desc tap is planned and
the fallback never triggers.

Every action carries one of this route's edge ids (the harness raises
for any other id). Lifecycle / call / framework edges with no user
action are recorded with runner.comment.

Activity assumption: the manifest package is
com.smlnskgmail.jaman.hashchecker and .MainActivity is the activity
class under the flavor applicationId passed as --package.
"""

import argparse
import os
import sys

# Repo root is 3 levels up from this script's directory
# (device/routes/hash-checker/): hash-checker -> routes -> device -> root.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness.harness import Runner  # noqa: E402


def tap_menu(runner, edge, desc, res_id):
    """Tap an icon-only action-bar item by content-desc, else by id."""
    try:
        runner.tap(edge, desc=desc)
    except LookupError:
        runner.tap(edge, res_id=res_id)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    pkg = args.package
    runner = Runner(
        package=args.package, route="route_07",
        edge_ids=["E372472a8", "E3101d0cd", "Edeb6bd90", "E56501d6f",
                  "E9e141121", "E3755babd", "E9574aba4", "E3ac2e1c9",
                  "E59c1e403", "E79b435a7", "E98e98419", "E30bb0ca3",
                  "E58fc7a37", "E0848626c", "Eed97dffc", "E329fd909",
                  "Eb87d737f", "E07bec56b", "E33bc58cc", "Ec8dd5d3f",
                  "Ea6ffa5e2", "E0f814afb", "E4b722c5e", "E9c05dfdc",
                  "E48baef20", "E85c92c29", "E429186ad", "E645d374b"],
        log_path=args.log, dry_run=args.dry_run, adb=args.adb)
    try:
        # E372472a8: S_ENTRY -> MainActivity.<init>
        # Trigger: tap the launcher icon (MAIN + LAUNCHER intent filter).
        runner.launch(pkg + "/com.smlnskgmail.jaman.hashchecker.MainActivity",
                      "E372472a8")
        # E3101d0cd: MainActivity.<init> -> MainActivity.onCreate
        # Lifecycle: the system instantiates MainActivity, then onCreate.
        runner.comment("lifecycle: MainActivity.onCreate", "E3101d0cd")
        # Edeb6bd90: MainActivity.onCreate -> BaseActivity.onCreate@MainActivity
        # Call: super.onCreate(savedInstanceState) (MainActivity.java:52).
        runner.comment("call: super.onCreate", "Edeb6bd90")
        # E56501d6f: BaseActivity.onCreate@MainActivity -> MainActivity.create
        # Call: BaseActivity.onCreate calls create() (BaseActivity.java:19).
        runner.comment("call: MainActivity.create", "E56501d6f")
        # E9e141121: MainActivity.create -> MainActivity.showFragment@CALC
        # Call: showFragment(mainFragment) (MainActivity.java:93).
        runner.comment("call: showFragment HashCalculatorFragment", "E9e141121")
        # E3755babd: MainActivity.showFragment@CALC
        #   -> HashCalculatorFragment.onAttach
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: HashCalculatorFragment.onAttach", "E3755babd")
        # E9574aba4: HashCalculatorFragment.onAttach
        #   -> BaseFragment.onCreateView@HashCalculatorFragment
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: BaseFragment.onCreateView", "E9574aba4")
        # E3ac2e1c9: BaseFragment.onCreateView@HashCalculatorFragment
        #   -> HashCalculatorFragment.onViewCreated
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: HashCalculatorFragment.onViewCreated",
                       "E3ac2e1c9")
        # E59c1e403: HashCalculatorFragment.onViewCreated
        #   -> BaseFragment.onResume@HashCalculatorFragment
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: BaseFragment.onResume", "E59c1e403")
        # E79b435a7: BaseFragment.onResume@HashCalculatorFragment -> S_MAIN_EMPTY
        # The fragment is visible: the empty calculator screen.
        runner.comment("enters: calculator screen, no source yet", "E79b435a7")
        # E98e98419: S_MAIN_EMPTY -> MainActivity.onOptionsItemSelected@SETTINGS
        # Trigger: tap the Settings icon in the action bar
        # (menu_main.xml menu_main_section_settings, title "Settings").
        tap_menu(runner, "E98e98419", "Settings",
                 pkg + ":id/menu_main_section_settings")
        # E30bb0ca3: MainActivity.onOptionsItemSelected@SETTINGS
        #   -> MainActivity.showFragment@SETTINGS
        # Call: MainActivity.java:130.
        runner.comment("call: showFragment SettingsFragment", "E30bb0ca3")
        # E58fc7a37: MainActivity.showFragment@SETTINGS -> SettingsFragment.onAttach
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: SettingsFragment.onAttach", "E58fc7a37")
        # E0848626c: SettingsFragment.onAttach
        #   -> SettingsFragment.onCreatePreferences
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: SettingsFragment.onCreatePreferences",
                       "E0848626c")
        # Eed97dffc: SettingsFragment.onCreatePreferences
        #   -> SettingsFragment.onViewCreated
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: SettingsFragment.onViewCreated", "Eed97dffc")
        # E329fd909: SettingsFragment.onViewCreated -> SettingsFragment.onResume
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: SettingsFragment.onResume", "E329fd909")
        # Eb87d737f: SettingsFragment.onResume -> S_SETTINGS
        # The fragment is visible: the settings list.
        runner.wait_for("Eb87d737f", text="Privacy Policy")
        # E07bec56b: S_SETTINGS -> SettingsFragment.lambda$initPrivacyPolicy$2
        # Trigger: tap the "Privacy Policy" preference row
        # (settings.xml key_privacy_policy, title settings_title_privacy_policy).
        runner.tap("E07bec56b", text="Privacy Policy")
        # E33bc58cc: SettingsFragment.lambda$initPrivacyPolicy$2
        #   -> S_SHEET_PRIVACY
        # The privacy policy bottom sheet opens (single link row).
        runner.wait_for("E33bc58cc", text="Privacy Policy")
        # Ec8dd5d3f: S_SHEET_PRIVACY -> BaseListHolder.lambda$bind$0@WEB_PRIVACY
        # Trigger: tap the link row (WebLink.PRIVACY_POLICY, whose title is
        # also "Privacy Policy"; WebLinksListAdapter.java:55-67).
        runner.tap("Ec8dd5d3f", text="Privacy Policy")
        # Ea6ffa5e2: BaseListHolder.lambda$bind$0@WEB_PRIVACY
        #   -> WebLinksListAdapter$WebLinksListHolder.callItemClick@PRIVACY
        # Call: the row tap invokes the holder click (BaseListHolder.java:44).
        runner.comment("call: WebLinksListHolder.callItemClick", "Ea6ffa5e2")
        # E0f814afb: WebLinksListAdapter$WebLinksListHolder.callItemClick@PRIVACY
        #   -> MainActivity.showFragment@WEB
        # Call: privacy-policy links open WebFragment in-app
        # (WebLinksListAdapter.java:60).
        runner.comment("call: showFragment WebFragment", "E0f814afb")
        # E4b722c5e: MainActivity.showFragment@WEB -> WebFragment.onAttach
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: WebFragment.onAttach", "E4b722c5e")
        # E9c05dfdc: WebFragment.onAttach -> BaseFragment.onCreateView@WebFragment
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: BaseFragment.onCreateView (Web)", "E9c05dfdc")
        # E48baef20: BaseFragment.onCreateView@WebFragment
        #   -> WebFragment.onViewCreated
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: WebFragment.onViewCreated", "E48baef20")
        # E85c92c29: WebFragment.onViewCreated -> BaseFragment.onResume@WebFragment
        # Lifecycle: FragmentManager runs the fragment lifecycle after commit.
        runner.comment("lifecycle: BaseFragment.onResume (Web)", "E85c92c29")
        # E429186ad: BaseFragment.onResume@WebFragment
        #   -> BaseFragment.onCreateOptionsMenu@WebFragment
        # Framework: FragmentActivity offers the options menu to the added
        # fragments, which call onCreateOptionsMenu.
        runner.comment("framework: onCreateOptionsMenu offered to WebFragment",
                       "E429186ad")
        # E645d374b: BaseFragment.onCreateOptionsMenu@WebFragment
        #   -> WebFragment.getMenuResId  [TARGET]
        # Call: BaseFragment.java:69; returns R.menu.menu_webview.
        runner.comment("target: WebFragment.getMenuResId", "E645d374b")
    finally:
        runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
