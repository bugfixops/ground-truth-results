"""MMEX route_27: MmxContentProvider.logUpdate.

Method: MmxContentProvider.logUpdate
Edge ids (in route order):
    E71c76102 E2e074fc1 E00ecbc65 Ef6141ef2 E123c236d Efd0fc8b4
    Eb647565c Ef2826f2c E84eb47fd
Printed route source:
    graphs/MMEX/scratch/route_print_final2/MmxContentProvider.logUpdate.txt
    (9 steps; edges above verified identical to the verification.csv
    path row for MmxContentProvider.logUpdate).
Permissions: none (print header env=-, so no ENV permission gate;
    no permission is granted by this script).
Fixtures: none (print header state=-; no STATE file gate; no
    $WEMU/fixtures file is needed).
Setup: none (apps.csv MMEX setup is "none (minSdk 22)").
State precondition NOT created by this script (read before replay):
    MainActivity.onCreate calls populateScheduledTransactions only
    after showPrerequisite() returns false (home/MainActivity.java:184-187;
    definition :1478-1499: tutorial already dismissed, since
    BehaviourSettings.getShowTutorial defaults to true, and a valid
    database already configured and present on disk). Then the
    recurring-transaction notification setting must be on (default
    true) and the QueryBillDeposits cursor must return at least one
    due bill (DAYSLEFT <= 0) (home/MainActivity.java:1234-1264), and
    moveNextOccurrence must take the update path: a non-null recurring
    transaction whose recurrence is not ONCE
    (servicelayer/RecurringTransactionService.java:176-240). On a
    pm-clear run with no first-run setup, onCreate stops at the
    prerequisite gate and this chain does not fire; that is a state
    precondition, not a script step, and no tap is invented for it.
    The remaining edges are internal calls / framework delivery with
    no user action, so they are comment-only below.
Run (from the repo root, once placed in device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_27.py --package
    com.money.manager.ex --log steps/route_27.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "E00ecbc65", "Ef6141ef2", "E123c236d",
    "Efd0fc8b4", "Eb647565c", "Ef2826f2c", "E84eb47fd",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_27", edge_ids=EDGE_IDS,
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
        # Ef6141ef2: Internal call, no user action:
        # populateScheduledTransactions moves each due scheduled
        # transaction to its next occurrence
        # (home/MainActivity.java:1281-1282).
        r.comment("populateScheduledTransactions calls "
                  "RecurringTransactionService.moveNextOccurrence "
                  "(MainActivity.java:1281-1282)",
                  edge="Ef6141ef2")
        # E123c236d: Internal call, no user action: moveNextOccurrence
        # saves the recurring transaction with its next occurrence
        # date (RecurringTransactionService.java:240).
        r.comment("RecurringTransactionService.moveNextOccurrence calls "
                  "RecurringTransactionRepository.update "
                  "(RecurringTransactionService.java:240)",
                  edge="E123c236d")
        # Efd0fc8b4: Internal call, no user action: update forwards
        # to RepositoryBase.update
        # (RecurringTransactionRepository.java:107).
        r.comment("RecurringTransactionRepository.update calls "
                  "RepositoryBase.update (RecurringTransactionRepository.java:107)",
                  edge="Efd0fc8b4")
        # Eb647565c: Internal call, no user action: update forwards
        # to the 3-arg overload (RepositoryBase.java:180).
        r.comment("RepositoryBase.update forwards to the 3-arg overload "
                  "(RepositoryBase.java:180)",
                  edge="Eb647565c")
        # Ef2826f2c: Framework edge, no user action: update calls
        # ContentResolver.update on the MMEX URI and the framework
        # delivers it to MmxContentProvider.update
        # (datalayer/RepositoryBase.java:183-190).
        r.comment("ContentResolver.update delivered to "
                  "MmxContentProvider.update (RepositoryBase.java:183-190)",
                  edge="Ef2826f2c")
        # E84eb47fd: Internal call, no user action: update logs the
        # change for a TABLE dataset
        # (MmxContentProvider.java:205; guards :202, :204).
        r.comment("MmxContentProvider.update calls logUpdate "
                  "(MmxContentProvider.java:205)",
                  edge="E84eb47fd")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
