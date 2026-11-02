"""MMEX route_29: AppSettings.getPreferences.

Method: AppSettings.getPreferences
Edge ids (in route order):
    E71c76102 E2e074fc1 Ee0c1d96c E74cee0fe Ecb944bb8 E80087d60
    Eeab0559c Ebb73a633
Printed route source:
    graphs/MMEX/scratch/route_print_final2/AppSettings.getPreferences.txt
    (8 steps; edges above verified identical to the verification.csv
    path row for AppSettings.getPreferences).
Permissions: none (print header env=-, so no ENV permission gate;
    no permission is granted by this script).
Fixtures: none (no $WEMU/fixtures file is listed: the .mmb file this
    route needs is NOT in $WEMU/fixtures -- see Setup).
Setup: a valid .mmb database file on the device, named in the launch
    intent below. This is not a fixture (none exists in
    $WEMU/fixtures) and not apps.csv setup (MMEX setup is "none
    (minSdk 22)"): the file must be supplied by whoever stages the
    run, and MmxDatabaseUtils.useDatabase rejects a file that is not
    a valid database (utils/MmxDatabaseUtils.java:204-206).
State precondition NOT created by this script (read before replay):
    The intent is handled only after showPrerequisite() returns
    false (home/MainActivity.java:184-187, handleIntent call :210),
    so a valid database must already be configured as well as the
    intent file being valid. handleIntent first starts
    PasswordActivity (inside the printed range
    home/MainActivity.java:1192-1200) and then calls
    changeDatabase; the
    DatabaseMetadataFactory step must not throw
    (home/MainActivity.java:1192-1202). No tap is invented for any
    of this: the only action in this script is the launch intent
    itself, which is the route's own trigger (intent.getData() !=
    null, home/MainActivity.java:1189).
Run (from the repo root, once placed in device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_29.py --package
    com.money.manager.ex --log steps/route_29.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "Ee0c1d96c", "E74cee0fe", "Ecb944bb8",
    "E80087d60", "Eeab0559c", "Ebb73a633",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_29", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E71c76102: Launch the MAIN/LAUNCHER activity WITH a file
        # URI as its intent data. This is the route's trigger, not a
        # plain launcher tap: handleIntent switches database only
        # when intent.getData() != null
        # (home/MainActivity.java:1189). The .mmb path below must be
        # a valid database file staged before the run (see
        # docstring); a plain launch without data cannot reach step 4.
        # AndroidManifest.xml:136-143 (.home.MainActivity, MAIN +
        # LAUNCHER intent filter).
        r.start_intent(edge="E71c76102", action="android.intent.action.VIEW",
                       data="file:///sdcard/Download/database.mmb",
                       component="com.money.manager.ex/.home.MainActivity")
        # E2e074fc1: Lifecycle edge, no user action: the framework
        # creates MainActivity, then calls onCreate.
        r.comment("framework creates MainActivity, then calls onCreate",
                  edge="E2e074fc1")
        # Ee0c1d96c: Internal call, no user action: onCreate handles
        # the launch intent after the prerequisite check passes
        # (home/MainActivity.java:210; gate :184-187).
        r.comment("MainActivity.onCreate calls handleIntent "
                  "(MainActivity.java:210)",
                  edge="Ee0c1d96c")
        # E74cee0fe: Internal call, no user action: handleIntent
        # switches to the database named by the launch intent file
        # URI (home/MainActivity.java:1192-1200; guards :1186, :1189).
        r.comment("MainActivity.handleIntent calls changeDatabase "
                  "(MainActivity.java:1192-1200)",
                  edge="E74cee0fe")
        # Ecb944bb8: Internal call, no user action: changeDatabase
        # calls MmxDatabaseUtils.useDatabase (MainActivity.java:546).
        r.comment("MainActivity.changeDatabase calls "
                  "MmxDatabaseUtils.useDatabase (MainActivity.java:546)",
                  edge="Ecb944bb8")
        # E80087d60: Internal call, no user action: useDatabase sets
        # the database path (MmxDatabaseUtils.java:210).
        r.comment("MmxDatabaseUtils.useDatabase calls "
                  "DatabaseSettings.setDatabasePath "
                  "(MmxDatabaseUtils.java:210)",
                  edge="E80087d60")
        # Eeab0559c: Internal call, no user action: setDatabasePath
        # calls through AppSettings.set (DatabaseSettings.java:38).
        r.comment("DatabaseSettings.setDatabasePath calls "
                  "SettingsBase.set via AppSettings "
                  "(DatabaseSettings.java:38)",
                  edge="Eeab0559c")
        # Ebb73a633: Internal call, no user action: set obtains the
        # SharedPreferences through AppSettings.getPreferences
        # (SettingsBase.java:90).
        r.comment("SettingsBase.set calls AppSettings.getPreferences "
                  "(SettingsBase.java:90)",
                  edge="Ebb73a633")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
