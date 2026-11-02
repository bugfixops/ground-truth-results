"""Device replay script for hash-checker route_27.

Method: SharedPreferencesSettings.getLanguage
Edge ids (in route order, exactly as in ROUTES.csv): E372472a8 E3101d0cd Edeb6bd90 E80d964fd E12c893cb E48ab11f3
Printed route file: graphs/hash-checker/scratch/route_print/SharedPreferencesSettings.getLanguage.txt
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

    runner = Runner(package=args.package, route='route_27',
                    edge_ids=['E372472a8', 'E3101d0cd', 'Edeb6bd90', 'E80d964fd', 'E12c893cb', 'E48ab11f3'],
                    log_path=args.log, dry_run=args.dry_run,
                    adb=args.adb)

    # Edge E372472a8: S_ENTRY -> MainActivity.<init>: tap the launcher icon (MAIN + LAUNCHER intent filter, AndroidManifest.xml:19-33). Launching MainActivity is the entry step.
    runner.launch(args.package +
                  "/com.smlnskgmail.jaman.hashchecker.MainActivity",
                  'E372472a8')

    # Edge E3101d0cd: MainActivity.<init> -> MainActivity.onCreate: the system instantiates MainActivity, then calls onCreate (MainActivity.java:50, thirdPartyStores flavor). Framework lifecycle; no user action.
    runner.comment('MainActivity.<init> -> MainActivity.onCreate: the system instantiates MainActivity, then calls onCreate (MainActivity.java:50, thirdPartyStores flavor). Framework lifecycle; no user action.', 'E3101d0cd')

    # Edge Edeb6bd90: MainActivity.onCreate -> BaseActivity.onCreate@MainActivity: super.onCreate(savedInstanceState) (MainActivity.java:52). Internal call; no user action.
    runner.comment('MainActivity.onCreate -> BaseActivity.onCreate@MainActivity: super.onCreate(savedInstanceState) (MainActivity.java:52). Internal call; no user action.', 'Edeb6bd90')

    # Edge E80d964fd: BaseActivity.onCreate@MainActivity -> LanguageConfigImpl.applyLanguage: langHelper().applyLanguage(this) (BaseActivity.java:17). Internal call; no user action.
    runner.comment('BaseActivity.onCreate@MainActivity -> LanguageConfigImpl.applyLanguage: langHelper().applyLanguage(this) (BaseActivity.java:17). Internal call; no user action.', 'E80d964fd')

    # Edge E12c893cb: LanguageConfigImpl.applyLanguage -> LanguageConfigImpl.currentLanguage: setLanguage(context, currentLanguage()) (LanguageConfigImpl.java:51). Internal call; no user action.
    runner.comment('LanguageConfigImpl.applyLanguage -> LanguageConfigImpl.currentLanguage: setLanguage(context, currentLanguage()) (LanguageConfigImpl.java:51). Internal call; no user action.', 'E12c893cb')

    # Edge E48ab11f3: LanguageConfigImpl.currentLanguage -> SharedPreferencesSettings.getLanguage: return settings.getLanguage() (LanguageConfigImpl.java:57). Target method; internal call; no user action.
    runner.comment('LanguageConfigImpl.currentLanguage -> SharedPreferencesSettings.getLanguage: return settings.getLanguage() (LanguageConfigImpl.java:57). Target method; internal call; no user action.', 'E48ab11f3')

    runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
