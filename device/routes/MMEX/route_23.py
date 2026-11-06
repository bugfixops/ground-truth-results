"""MMEX route_23: DateRange.<init>().

Method: DateRange.<init>()
Edge ids (in route order):
    E71c76102 E2e074fc1 E5d5a9c2f Eff22f7d2 Ebbb78d0f Ee424c2e8
    Ebc409bd4 Ebb57ba7f E5e7583d5 E6cd10559 E994a6b75 Edad2b982
    E1dd987db Ea773e4f7 E43508b78 E3f0cbcb4 Eca2a9c6b E5d608793
    E568f7b56 Eb1779c19 E57e26427 E42bcd793 Ea6a1e9e4 E5b8cbc4b
Printed route source:
    graphs/MMEX/scratch/route_print_final2/DateRange.<init>().txt
    (24 steps; header env=- state=account;settings). These edge ids
    match, in order, the verification.csv path row for
    DateRange.<init>() exactly (checked by the helper; no
    discrepancy).
Permissions: none (print header env=-; no ENV permission gate, so no
    permission from the manifest is granted by this route).
Fixtures: none (no STATE file gate).
Setup: setup_route_23.py (bootstrap + known non-investment account
    "RetryMain"); the reaching tap uses tap(text="RetryMain") per
    audit §1.2, since group and child rows share the res_id.
Harness note: the rotate() call needs the landed device/harness
    (it exists there and in device/stage; Currency route_05 uses it
    the same way). The older AmazeFileManager harness snapshot cited
    in the helper brief has no rotate() method, so a dry run against
    that snapshot fails on this route only.
Run (from the repo root, after the merger drops this file into
    device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_23.py --package
    com.money.manager.ex --log steps/route_23.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "E5d5a9c2f", "Eff22f7d2", "Ebbb78d0f",
    "Ee424c2e8", "Ebc409bd4", "Ebb57ba7f", "E5e7583d5", "E6cd10559",
    "E994a6b75", "Edad2b982", "E1dd987db", "Ea773e4f7", "E43508b78",
    "E3f0cbcb4", "Eca2a9c6b", "E5d608793", "E568f7b56", "Eb1779c19",
    "E57e26427", "E42bcd793", "Ea6a1e9e4", "E5b8cbc4b",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_23", edge_ids=EDGE_IDS,
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
        # Ebbb78d0f: Tap an account row (a child row) in the account
        # list. Child rows inflate res/layout/item_account_bills.xml
        # and carry the account name in @+id/textViewItemAccountName
        # (HomeAccountsExpandableAdapter.java:201-204, 219;
        # item_account_bills.xml:42) — but group rows share that id
        # (getGroupView, ~line 115), so a res_id tap hits the group
        # header, never onChildClick (audit §1.2). setup_route_23.py
        # seeds a known non-investment account "RetryMain", and this
        # tap(text=...) resolves that child row's own text node.
        r.tap(text="RetryMain", edge="Ebbb78d0f")
        # Ee424c2e8: The row tap posts RequestAccountFragmentEvent on
        # the EventBus (HomeFragment.java:704; subscriber registered
        # in MmxBaseFragmentActivity.onStart). Automatic on the tap.
        r.comment("row tap posts RequestAccountFragmentEvent",
                  edge="Ee424c2e8")
        # Ebc409bd4: MainActivity.onEvent calls showAccountFragment
        # (MainActivity.java:456). No user action.
        r.comment("onEvent calls showAccountFragment",
                  edge="Ebc409bd4")
        # Ebb57ba7f: showAccountFragment calls
        # AccountTransactionListFragment.newInstance
        # (MainActivity.java:786). No user action.
        r.comment("showAccountFragment calls newInstance",
                  edge="Ebb57ba7f")
        # E5e7583d5: newInstance constructs the fragment
        # (AccountTransactionListFragment.java:103). No user action.
        r.comment("newInstance constructs the fragment",
                  edge="E5e7583d5")
        # E6cd10559: The FragmentManager attaches the fragment when
        # the transaction commits (MainActivity.java:768-773).
        # No user action.
        r.comment("FragmentManager attaches the fragment",
                  edge="E6cd10559")
        # E994a6b75: The framework calls onCreate after onAttach.
        # No user action.
        r.comment("framework calls fragment onCreate",
                  edge="E994a6b75")
        # Edad2b982: The framework calls onCreateView after onCreate.
        # No user action.
        r.comment("framework calls fragment onCreateView",
                  edge="Edad2b982")
        # E1dd987db: The account transaction list is shown
        # (AccountTransactionListFragment.java:163, 170-174, 850).
        # No user action.
        r.comment("account transaction list shown",
                  edge="E1dd987db")
        # Ea773e4f7: Tap an options menu item of the account
        # transaction list: the filter item. It is inflated from
        # res/menu/menu_transaction_filters.xml:23
        # (@+id/menuTransactionFilters, showAsAction ifRoom) with
        # title @string/filter_options_info = "Filter Options and
        # Info" (res/values/strings.xml:578); an action-bar icon
        # exposes its title as content description.
        r.tap(desc="Filter Options and Info", edge="Ea773e4f7")
        # E43508b78: onOptionsItemSelected calls isFilterSelected
        # (AccountTransactionListFragment.java:295). No user action.
        r.comment("onOptionsItemSelected calls isFilterSelected",
                  edge="E43508b78")
        # E3f0cbcb4: isFilterSelected calls showFilterDialog when the
        # tapped item is menuTransactionFilters
        # (AccountTransactionListFragment.java:596-598).
        # No separate action.
        r.comment("filter item calls showFilterDialog",
                  edge="E3f0cbcb4")
        # Eca2a9c6b: showFilterDialog calls
        # FilterDialogFragment.newInstance
        # (AccountTransactionListFragment.java:830). No user action.
        r.comment("showFilterDialog calls FilterDialogFragment.newInstance",
                  edge="Eca2a9c6b")
        # E5d608793: newInstance constructs the dialog fragment
        # (FilterDialogFragment.java:70). No user action.
        r.comment("newInstance constructs FilterDialogFragment",
                  edge="E5d608793")
        # E568f7b56: The framework calls onCreate for the dialog
        # fragment when it is shown
        # (AccountTransactionListFragment.java:831;
        # FilterDialogFragment.java:82-95). No user action.
        r.comment("framework calls dialog onCreate (shown)",
                  edge="E568f7b56")
        # Eb1779c19: A FragmentManager save/restore event intervenes
        # between the first onCreate and the restored onCreate. The
        # script drives it as a configuration change: rotate to
        # landscape (landed harness rotate(); see docstring).
        r.rotate(edge="Eb1779c19", orientation="landscape")
        # E57e26427: The restored onCreate reads the parcelled
        # arguments with getArguments().getParcelable(ARG_TX_FILTER)
        # (FilterDialogFragment.java:86), which unparcels through the
        # creator. Automatic after the restore; no user action.
        r.comment("restored onCreate reads parcelled filter",
                  edge="E57e26427")
        # E42bcd793: The generated TransactionFilter$$Parcelable
        # createFromParcel calls its read method (INFERRED generated
        # code, no source in the upload). No user action.
        r.comment("generated createFromParcel calls read",
                  edge="E42bcd793")
        # Ea6a1e9e4: The generated TransactionFilter$$Parcelable.read
        # calls DateRange$$Parcelable.read (INFERRED generated code).
        # No user action.
        r.comment("generated read calls DateRange$$Parcelable.read",
                  edge="Ea6a1e9e4")
        # E5b8cbc4b: The generated DateRange$$Parcelable.read calls
        # DateRange.<init>() (INFERRED generated code). No user action.
        r.comment("generated read calls DateRange.<init>()",
                  edge="E5b8cbc4b")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
