"""Device replay script for hash-checker route_30.

Method: SharedPreferencesSettings.getBooleanPreference
Edge ids (in route order, exactly as in ROUTES.csv): E34de2c31 E7aab529b E30c477d4 E8135e8c2
Printed route file: graphs/hash-checker/scratch/route_print/SharedPreferencesSettings.getBooleanPreference.txt
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

    runner = Runner(package=args.package, route='route_30',
                    edge_ids=['E34de2c31', 'E7aab529b', 'E30c477d4', 'E8135e8c2'],
                    log_path=args.log, dry_run=args.dry_run,
                    adb=args.adb)

    # Edge E34de2c31: S_ENTRY -> App.<init>: Android starts the app process; the Application object is created before any component (AndroidManifest.xml:9, android:name=".App"). Launching MainActivity triggers Application creation first.
    runner.launch(args.package +
                  "/com.smlnskgmail.jaman.hashchecker.MainActivity",
                  'E34de2c31')

    # Edge E7aab529b: App.<init> -> App.onCreate: Application.onCreate runs right after construction (App.java:53). Framework lifecycle; no user action.
    runner.comment('App.<init> -> App.onCreate: Application.onCreate runs right after construction (App.java:53). Framework lifecycle; no user action.', 'E7aab529b')

    # Edge E30c477d4: App.onCreate -> SharedPreferencesSettings.isShortcutsIsCreated: if (!settings.isShortcutsIsCreated()) (App.java:76). The call itself is unconditional on every launch; only the shortcut-creation branch inside is guarded. Internal call; no user action.
    runner.comment('App.onCreate -> SharedPreferencesSettings.isShortcutsIsCreated: if (!settings.isShortcutsIsCreated()) (App.java:76). The call itself is unconditional on every launch; only the shortcut-creation branch inside is guarded. Internal call; no user action.', 'E30c477d4')

    # Edge E8135e8c2: SharedPreferencesSettings.isShortcutsIsCreated -> SharedPreferencesSettings.getBooleanPreference: return getBooleanPreference(...) (SharedPreferencesSettings.java:159). Target method; internal call; no user action.
    runner.comment('SharedPreferencesSettings.isShortcutsIsCreated -> SharedPreferencesSettings.getBooleanPreference: return getBooleanPreference(...) (SharedPreferencesSettings.java:159). Target method; internal call; no user action.', 'E8135e8c2')

    runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
