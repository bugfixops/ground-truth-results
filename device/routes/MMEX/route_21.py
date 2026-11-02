"""MMEX route_21: DefinedDateRange$1.<init>.

Method: DefinedDateRange$1.<init>
Edge ids (in route order):
    E71c76102 E2e074fc1 E5d5a9c2f Eff22f7d2 Ed2488d54 E025b8cae
    E02874fba Ec35ca2a7 E3a7e070b Eb967ab5b E9d54d4ff E1f261187
    Eeb991f01 E1bff1ecc E85002a00 E8393db65 E931a290d Ead211413
    E0d84e708 Ea1f3a9f7
Printed route source:
    graphs/MMEX/scratch/route_print_final2/DefinedDateRange_1.<init>.txt
    (20 steps; header env=- state=-). These edge ids match, in order,
    the verification.csv path row for DefinedDateRange$1.<init>
    exactly (checked by the helper; no discrepancy).
Permissions: none (print header env=-; no ENV permission gate, so no
    permission from the manifest is granted by this route).
Fixtures: none (no STATE file gate).
Setup: none (apps.csv MMEX setup is effectively none).
Run (from the repo root, after the merger drops this file into
    device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_21.py --package
    com.money.manager.ex --log steps/route_21.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "E5d5a9c2f", "Eff22f7d2", "Ed2488d54",
    "E025b8cae", "E02874fba", "Ec35ca2a7", "E3a7e070b", "Eb967ab5b",
    "E9d54d4ff", "E1f261187", "Eeb991f01", "E1bff1ecc", "E85002a00",
    "E8393db65", "E931a290d", "Ead211413", "E0d84e708", "Ea1f3a9f7",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_21", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E71c76102: Launch the MAIN/LAUNCHER activity.
        # AndroidManifest.xml:136-143: .home.MainActivity with MAIN +
        # LAUNCHER intent filter.
        r.launch("com.money.manager.ex/.home.MainActivity",
                 edge="E71c76102")
        # E2e074fc1: The framework calls MainActivity.onCreate after
        # creating the activity instance. No user action.
        r.comment("framework calls MainActivity.onCreate",
                  edge="E2e074fc1")
        # E5d5a9c2f: MainActivity.onCreate calls initHomeFragment
        # directly (MainActivity.java:238). No user action.
        r.comment("MainActivity.onCreate calls initHomeFragment",
                  edge="E5d5a9c2f")
        # Eff22f7d2: initHomeFragment commits HomeFragment into the
        # content container, showing the home screen
        # (MainActivity.java:1308-1324). No user action.
        r.comment("home screen shown (HomeFragment committed)",
                  edge="Eff22f7d2")
        # Ed2488d54: Open the drawer, then tap a top-level drawer item
        # with no sub-items: Settings. Drawer toggle content
        # description is R.string.open = "Open" (MainActivity.java:1296;
        # res/values/strings.xml:193). Drawer item text is
        # getString(R.string.settings) = "Settings"
        # (MainActivity.java:1107; res/values/strings.xml:189).
        r.tap(desc="Open", edge="Ed2488d54")
        r.tap(text="Settings", edge="Ed2488d54")
        # E025b8cae: The group-click tap posts a Runnable with a 200 ms
        # delay; the framework runs it (MainActivity.java:948-962).
        # No user action beyond the tap above.
        r.comment("drawer Runnable runs after 200 ms delay",
                  edge="E025b8cae")
        # E02874fba: run() calls onDrawerMenuAndOptionMenuSelected
        # with the tapped group item (MainActivity.java:953-957).
        # No separate action.
        r.comment("Runnable calls onDrawerMenuAndOptionMenuSelected",
                  edge="E02874fba")
        # Ec35ca2a7: case R.id.menu_settings starts SettingsActivity
        # (MainActivity.java:664-665). Consequence of the Settings
        # tap, not a second launch.
        r.comment("case menu_settings starts SettingsActivity",
                  edge="Ec35ca2a7")
        # E3a7e070b: The framework calls SettingsActivity.onCreate
        # after the constructor. No user action.
        r.comment("framework calls SettingsActivity.onCreate",
                  edge="E3a7e070b")
        # Eb967ab5b: The settings list is shown with the default
        # SettingsFragment (SettingsActivity.java:67-69; the
        # PerDatabaseFragment branch needs an extra this intent does
        # not carry). No user action.
        r.comment("settings list shown (default SettingsFragment)",
                  edge="Eb967ab5b")
        # E9d54d4ff: Tap the look and feel preference. Its title is
        # @string/preferences_dispaly = "Look & Feel"
        # (res/xml/preferences.xml look-feel Preference entry;
        # res/values/strings.xml:54; listener set in
        # SettingsFragment.java:70-80, onPreferenceClick at 76).
        r.tap(text="Look & Feel", edge="E9d54d4ff")
        # E1f261187: onPreferenceClick starts LookFeelSettingsActivity
        # (SettingsFragment.java:77). Consequence of the tap above.
        r.comment("look-and-feel tap starts LookFeelSettingsActivity",
                  edge="E1f261187")
        # Eeb991f01: The framework calls
        # LookFeelSettingsActivity.onCreate. No user action.
        r.comment("framework calls LookFeelSettingsActivity.onCreate",
                  edge="Eeb991f01")
        # E1bff1ecc: onCreate sets the setting fragment to a new
        # LookFeelPreferenceFragment (LookFeelSettingsActivity.java:28).
        # No user action.
        r.comment("onCreate sets LookFeelPreferenceFragment",
                  edge="E1bff1ecc")
        # E85002a00: The framework calls
        # LookFeelPreferenceFragment.onCreate. Waiting for the
        # "Show Transaction" preference title confirms the fragment
        # inflated its preferences (res/xml/preferences_look_and_feel.xml:34-35;
        # res/values/strings.xml:227 "Show Transaction").
        r.wait_for(text="Show Transaction", edge="E85002a00", timeout=30)
        # E8393db65: onCreate builds the DefinedDateRanges that supply
        # the show-transactions entries, inside the non-null check on
        # the ListPreference (LookFeelPreferenceFragment.java:109-114).
        # No user action.
        r.comment("onCreate builds DefinedDateRanges for lstShow",
                  edge="E8393db65")
        # E931a290d: DefinedDateRanges.<init> calls initialize
        # (DefinedDateRanges.java:33). No user action.
        r.comment("DefinedDateRanges.<init> calls initialize",
                  edge="E931a290d")
        # Ead211413: initialize calls create for ALL_TIME
        # (DefinedDateRanges.java:156). No user action.
        r.comment("initialize calls create(ALL_TIME)",
                  edge="Ead211413")
        # E0d84e708: create constructs a DefinedDateRange
        # (DefinedDateRanges.java:163), running its static initializer.
        # No user action.
        r.comment("create constructs DefinedDateRange (<clinit>)",
                  edge="E0d84e708")
        # Ea1f3a9f7: The static initializer creates the CREATOR
        # anonymous class, whose constructor is DefinedDateRange$1.<init>
        # (DefinedDateRange.java:56). No user action.
        r.comment("DefinedDateRange.<clinit> creates CREATOR ($1)",
                  edge="Ea1f3a9f7")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
