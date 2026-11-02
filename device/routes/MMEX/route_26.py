"""MMEX route_26: MmxContentProvider.prepareQuery.

Method: MmxContentProvider.prepareQuery
Edge ids (in route order):
    E71c76102 E2e074fc1 E00ecbc65 Ef39d531e Eb2c12012 Edd046923
    Ec5c3a14a Ef50e85c8 Eb152b23a Ec32826bf
Printed route source:
    graphs/MMEX/scratch/route_print_final2/MmxContentProvider.prepareQuery.txt
    (10 steps; edges above verified identical to the verification.csv
    path row for MmxContentProvider.prepareQuery).
Permissions: none (print header env=-, so no ENV permission gate;
    no permission is granted by this script).
Fixtures: none (print header state=-; no STATE file gate; no
    $WEMU/fixtures file is needed).
Setup: setup_route_26.py bootstrap (app-created database + tutorial off + databasepath).
State precondition NOT created by this script (read before replay):
    MainActivity.onCreate calls populateScheduledTransactions only
    after showPrerequisite() returns false (home/MainActivity.java:184-187;
    definition :1478-1499: tutorial already dismissed, since
    BehaviourSettings.getShowTutorial defaults to true, and a valid
    database already configured and present on disk, since
    isDatabaseAvailable requires a non-empty stored path whose file
    exists). Then the recurring-transaction notification setting must
    be on (default true) and the QueryBillDeposits cursor must return
    at least one due bill (DAYSLEFT <= 0) with id != NOT_SET
    (home/MainActivity.java:1234-1264;
    datalayer/RecurringTransactionRepository.java:63-69). On a
    pm-clear run with no first-run setup, onCreate stops at the
    prerequisite gate and this chain does not fire; that is a state
    precondition, not a script step, and no tap is invented for it.
    The remaining edges are internal calls / framework delivery with
    no user action, so they are comment-only below.
Run (from the repo root, once placed in device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_26.py --package
    com.money.manager.ex --log steps/route_26.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "E00ecbc65", "Ef39d531e", "Eb2c12012",
    "Edd046923", "Ec5c3a14a", "Ef50e85c8", "Eb152b23a", "Ec32826bf",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_26", edge_ids=EDGE_IDS,
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
        # E00ecbc65: Internal call, no user action: onCreate calls
        # populateScheduledTransactions (MainActivity.java:244) once
        # the prerequisite gate passes (see docstring).
        r.comment("MainActivity.onCreate calls "
                  "populateScheduledTransactions (MainActivity.java:244)",
                  edge="E00ecbc65")
        # Ef39d531e: Internal call, no user action:
        # populateScheduledTransactions loads each due scheduled
        # transaction (home/MainActivity.java:1264).
        r.comment("populateScheduledTransactions loads the due "
                  "scheduled transaction (MainActivity.java:1264)",
                  edge="Ef39d531e")
        # Eb2c12012: Internal call, no user action: load returns the
        # first bill deposit (RecurringTransactionRepository.java:69).
        r.comment("RecurringTransactionRepository.load calls first "
                  "(RecurringTransactionRepository.java:69)",
                  edge="Eb2c12012")
        # Edd046923: Internal call, no user action: first opens a
        # cursor (RecurringTransactionRepository.java:75).
        r.comment("RecurringTransactionRepository.first calls "
                  "RepositoryBase.openCursor (RecurringTransactionRepository.java:75)",
                  edge="Edd046923")
        # Ec5c3a14a: Internal call, no user action: openCursor
        # overload forwards (RepositoryBase.java:70).
        r.comment("RepositoryBase.openCursor forwards to the 4-arg "
                  "overload (RepositoryBase.java:70)",
                  edge="Ec5c3a14a")
        # Ef50e85c8: Framework edge, no user action: openCursor calls
        # ContentResolver.query on the MMEX URI and the framework
        # delivers it to MmxContentProvider.query
        # (datalayer/RepositoryBase.java:73-75).
        r.comment("ContentResolver.query delivered to "
                  "MmxContentProvider.query (RepositoryBase.java:73-75)",
                  edge="Ef50e85c8")
        # Eb152b23a: Internal call, no user action: query calls
        # query_internal (MmxContentProvider.java:143).
        r.comment("MmxContentProvider.query calls query_internal "
                  "(MmxContentProvider.java:143)",
                  edge="Eb152b23a")
        # Ec32826bf: Internal call, no user action: query_internal
        # calls prepareQuery for a Dataset source
        # (MmxContentProvider.java:395; guards :385-388, :393).
        r.comment("MmxContentProvider.query_internal calls prepareQuery "
                  "(MmxContentProvider.java:395)",
                  edge="Ec32826bf")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
