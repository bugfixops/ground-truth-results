"""MMEX route_15: TutorialActivity.onOptionsItemSelected.

Method: TutorialActivity.onOptionsItemSelected
Edge ids (in route order):
    E71c76102 E2e074fc1 Eda32c006 E4563886d E40178052 E0c500742
    E13eb2a1c Eacaec855
Printed route source:
    graphs/MMEX/scratch/route_print_final2/TutorialActivity.onOptionsItemSelected.txt
    (8 steps; edge ids above match the verification.csv path row for
    TutorialActivity.onOptionsItemSelected exactly).
Permissions: none (no ENV permission gate on this route; the manifest
    declares INTERNET, ACCESS_NETWORK_STATE, VIBRATE,
    RECEIVE_BOOT_COMPLETED, READ_EXTERNAL_STORAGE,
    WRITE_EXTERNAL_STORAGE, USE_FINGERPRINT and WAKE_LOCK, none of
    which gates this route, so no runtime grant is issued).
Fixtures: none (no STATE file gate; $WEMU/fixtures holds no MMEX
    database, and this route needs none).
Setup: none (apps.csv MMEX setup is effectively none; the route
    relies on the standard pm-clear first-run state, in which the
    tutorial has not been dismissed: BehaviourSettings.getShowTutorial
    defaults to true, so MainActivity.onCreate takes the
    showPrerequisite -> showTutorial branch).
Run (from the repo root):
    python3 -I device/routes/MMEX/route_15.py --package
    com.money.manager.ex --log steps/route_15.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "Eda32c006", "E4563886d", "E40178052",
    "E0c500742", "E13eb2a1c", "Eacaec855",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_15", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E71c76102: Tap the MMEX icon in the launcher
        # (MAIN/LAUNCHER intent filter of .home.MainActivity:
        # AndroidManifest.xml:136-143).
        r.launch("com.money.manager.ex/.home.MainActivity",
                 edge="E71c76102")
        # E2e074fc1: The system instantiates MainActivity, then calls
        # onCreate.
        r.comment("system instantiates MainActivity, then onCreate",
                  edge="E2e074fc1")
        # Eda32c006: MainActivity.onCreate calls showPrerequisite
        # (MainActivity.java:184). After pm clear the tutorial has
        # not been dismissed (BehaviourSettings default true), so
        # showPrerequisite returns true via showTutorial.
        r.comment("MainActivity.onCreate calls showPrerequisite",
                  edge="Eda32c006")
        # E4563886d: showPrerequisite calls showTutorial
        # (MainActivity.java:1481).
        r.comment("showPrerequisite calls showTutorial",
                  edge="E4563886d")
        # E40178052: showTutorial starts TutorialActivity
        # (MainActivity.java:812-817, FLAG_ACTIVITY_CLEAR_TOP).
        # Consequence of the branch above, not a separate adb
        # action, so no second launch is issued.
        r.comment("showTutorial starts TutorialActivity",
                  edge="E40178052")
        # E0c500742: The system instantiates TutorialActivity, then
        # calls onCreate.
        r.comment("system instantiates TutorialActivity, then onCreate",
                  edge="E0c500742")
        # E13eb2a1c: The tutorial screen is shown: setContentView
        # (R.layout.activity_tutorial, TutorialActivity.java:55).
        r.comment("TutorialActivity.onCreate sets activity_tutorial",
                  edge="E13eb2a1c")
        # Eacaec855: Press the menu key, then tap the settings item
        # in the options menu. TutorialActivity uses the
        # Theme.NoTitleBar.Fullscreen theme (AndroidManifest.xml:
        # 314-319), so it has no action bar and the options menu
        # opens only from the menu key; the harness key("MENU")
        # sends KEYCODE_MENU. TutorialActivity.onCreateOptionsMenu
        # inflates R.menu.menu_tutorial (TutorialActivity.java:
        # 99-101); menu_tutorial.xml:22 defines action_settings
        # with title @string/action_settings = "Settings"
        # (strings.xml:486), showAsAction="never", so it appears
        # as the overflow-menu item. onOptionsItemSelected handles
        # R.id.action_settings and returns true
        # (TutorialActivity.java:113-114).
        r.key("MENU", edge="Eacaec855")
        r.tap(text="Settings", edge="Eacaec855")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
