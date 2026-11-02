"""MMEX route_30: RecentDatabasesProvider.toJson.

Method: RecentDatabasesProvider.toJson
Edge ids (in route order):
    E71c76102 E2e074fc1 Ee128b245 E0afa172d Ebaf2798b E92284171
    E2d19d91e Ec87e03f4
Printed route source:
    graphs/MMEX/scratch/route_print_final2/RecentDatabasesProvider.toJson.txt
    (8 steps; edges above verified identical to the verification.csv
    path row for RecentDatabasesProvider.toJson).
Permissions: none (print header env=-, so no ENV permission gate;
    no permission is granted by this script).
Fixtures: none (print header state=-; no STATE file gate; no
    $WEMU/fixtures file is needed).
Setup: setup_route_30.py bootstrap (first-run tutorial off + app-created
database); recent-list precondition (entry with empty remotePath) remains
a live-run risk, not proven satisfied.
State precondition NOT created by this script (read before replay):
    MainActivity.onCreate calls migrateRecentDatabases only after
    showPrerequisite() returns false (home/MainActivity.java:184-190;
    tutorial already dismissed and a valid database already
    configured). migrateRecentDatabases then reaches getCurrent
    only if the stored recent-databases list contains at least one
    entry with an empty remotePath
    (home/MainActivity.java:1513-1525), and getCurrent reaches add
    only if the configured database path is non-empty and not
    already in the list (home/RecentDatabasesProvider.java:119-130:
    an empty path returns null, an already-listed path returns the
    existing entry without add). On a pm-clear run with no first-run
    setup, onCreate stops at the prerequisite gate and this chain
    does not fire; that is a state precondition, not a script step,
    and no tap is invented for it. The remaining edges are internal
    calls with no user action, so they are comment-only below.
Run (from the repo root, once placed in device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_30.py --package
    com.money.manager.ex --log steps/route_30.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "Ee128b245", "E0afa172d", "Ebaf2798b",
    "E92284171", "E2d19d91e", "Ec87e03f4",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_30", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E71c76102: Launch the MAIN/LAUNCHER activity.
        # AndroidManifest.xml:136-143 (.home.MainActivity, MAIN +
        # LAUNCHER intent filter).
        r.launch("com.money.manager.ex/.home.MainActivity",
                 edge="E71c76102")
        # E2e074fc1: Lifecycle edge, no user action: the framework
        # creates MainActivity, then calls onCreate.
        r.comment("framework creates MainActivity, then calls onCreate",
                  edge="E2e074fc1")
        # Ee128b245: Internal call, no user action: onCreate calls
        # migrateRecentDatabases (MainActivity.java:190) once the
        # prerequisite gate passes (see docstring).
        r.comment("MainActivity.onCreate calls migrateRecentDatabases "
                  "(MainActivity.java:190)",
                  edge="Ee128b245")
        # E0afa172d: Internal call, no user action:
        # migrateRecentDatabases creates/saves the default entry via
        # getCurrent (MainActivity.java:1523).
        r.comment("MainActivity.migrateRecentDatabases calls "
                  "RecentDatabasesProvider.getCurrent "
                  "(MainActivity.java:1523)",
                  edge="E0afa172d")
        # Ebaf2798b: Internal call, no user action: getCurrent adds
        # the default entry (RecentDatabasesProvider.java:130).
        r.comment("RecentDatabasesProvider.getCurrent calls add "
                  "(RecentDatabasesProvider.java:130)",
                  edge="Ebaf2798b")
        # E92284171: Internal call, no user action: add forwards to
        # the keyed overload (RecentDatabasesProvider.java:81).
        r.comment("RecentDatabasesProvider.add forwards to "
                  "add(String, DatabaseMetadata) "
                  "(RecentDatabasesProvider.java:81)",
                  edge="E92284171")
        # E2d19d91e: Internal call, no user action: add saves the
        # list (RecentDatabasesProvider.java:75).
        r.comment("RecentDatabasesProvider.add calls save "
                  "(RecentDatabasesProvider.java:75)",
                  edge="E2d19d91e")
        # Ec87e03f4: Internal call, no user action: save serialises
        # the list (RecentDatabasesProvider.java:171).
        r.comment("RecentDatabasesProvider.save calls toJson "
                  "(RecentDatabasesProvider.java:171)",
                  edge="Ec87e03f4")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
