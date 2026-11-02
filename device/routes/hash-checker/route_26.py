"""Device replay script for hash-checker route_26.

Method: SharedPreferencesSettings.getStringPreference
Edge ids (in route order, exactly as in ROUTES.csv): E34de2c31 E7aab529b Eba28b1bc E6b01433c E8a7036af
Printed route file: graphs/hash-checker/scratch/route_print/SharedPreferencesSettings.getStringPreference.txt
Permissions: (none)
Fixtures: (none)
Setup: any file as input (fixtures)

Assumptions: runs on the fresh install / cleared data that run_app.sh
guarantees with pm clear. No fixture push, permission grant, or pm clear
is done here; run_app.sh does those before invoking this script.
Launching MainActivity triggers Application creation first, so the
App.onCreate chain runs before any activity UI appears. The remaining
edges are framework-lifecycle or internal calls with no user action,
so they are recorded with comment() blocks, one block per route edge,
in route order. No UI labels are invented: this route needs no tap,
text entry, or scroll beyond the launch.
"""

import argparse
import os
import sys

# Repo root is 3 levels up from this script's final location
# device/routes/hash-checker/ (file -> hash-checker -> routes ->
# device -> root).
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(_SCRIPT_DIR))))
from device.harness.harness import Runner


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    runner = Runner(package=args.package, route='route_26',
                    edge_ids=['E34de2c31', 'E7aab529b', 'Eba28b1bc', 'E6b01433c', 'E8a7036af'],
                    log_path=args.log, dry_run=args.dry_run,
                    adb=args.adb)

    # Edge E34de2c31: S_ENTRY -> App.<init>: Android starts the app process; the Application object is created before any component (AndroidManifest.xml:9, android:name=".App"). Launching MainActivity triggers Application creation first.
    runner.launch(args.package +
                  "/com.smlnskgmail.jaman.hashchecker.MainActivity",
                  'E34de2c31')

    # Edge E7aab529b: App.<init> -> App.onCreate: Application.onCreate runs right after construction (App.java:53). Framework lifecycle; no user action.
    runner.comment('App.<init> -> App.onCreate: Application.onCreate runs right after construction (App.java:53). Framework lifecycle; no user action.', 'E7aab529b')

    # Edge Eba28b1bc: App.onCreate -> SharedPreferencesSettings.getSelectedTheme: settings.getSelectedTheme().getThemeResId() (App.java:68). Internal call; no user action.
    runner.comment('App.onCreate -> SharedPreferencesSettings.getSelectedTheme: settings.getSelectedTheme().getThemeResId() (App.java:68). Internal call; no user action.', 'Eba28b1bc')

    # Edge E6b01433c: SharedPreferencesSettings.getSelectedTheme -> SharedPreferencesSettings.getTheme: direct call (SharedPreferencesSettings.java:103). Internal call; no user action.
    runner.comment('SharedPreferencesSettings.getSelectedTheme -> SharedPreferencesSettings.getTheme: direct call (SharedPreferencesSettings.java:103). Internal call; no user action.', 'E6b01433c')

    # Edge E8a7036af: SharedPreferencesSettings.getTheme -> SharedPreferencesSettings.getStringPreference: direct call (SharedPreferencesSettings.java:117). Target method; internal call; no user action.
    runner.comment('SharedPreferencesSettings.getTheme -> SharedPreferencesSettings.getStringPreference: direct call (SharedPreferencesSettings.java:117). Target method; internal call; no user action.', 'E8a7036af')

    runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
