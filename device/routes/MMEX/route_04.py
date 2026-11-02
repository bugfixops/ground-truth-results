"""MMEX route_04: AllDataListFragment.displayRunningBalances -- CONVERTED
(retry).

Method: AllDataListFragment.displayRunningBalances
Edge ids (in route order):
    E71c76102 E2e074fc1 E5d5a9c2f Eff22f7d2 E76c8c62d Ee424c2e8
    Ebc409bd4 Ebb57ba7f E5e7583d5 E6cd10559 E994a6b75 Edad2b982
    E1dd987db Ea773e4f7 E5b32226d E8fff51bb Ec61a85d5 E389c8c33
    Eb2d9679c E681ef2c6 E559fcfcd E0fa71f9a Efa1f37dd Ecac14a18
Printed route source:
    graphs/MMEX/scratch/route_print_final2/AllDataListFragment.displayRunningBalances.txt
    (24 steps; header env=- state=account;settings). These edge ids
    match, in order, the verification.csv path row for
    AllDataListFragment.displayRunningBalances exactly (checked by
    the g1 draft; no discrepancy).
Permissions: none (print header env=-; no ENV permission gate).
Fixtures: none (no STATE file gate).
Setup: setup_route_04.py (bootstrap + one account named "RetryCheck",
    default type Cash, i.e. non-investment). The previous
    unscriptable reason (res_id first-match collision on the home
    list) is removed by the known name: tap(text="RetryCheck")
    resolves the child row, whose text differs from every group
    header. Groups expand by default on fresh preferences
    (HomeFragment.java:747-759), so no expansion tap is needed.
    No transaction rows are needed: the tail
    AccountTransactionListFragment.onEvent forwards whatever
    balances the task computed (AccountTransactionListFragment.java:
    409-413) with no non-empty guard.
Run (from the repo root, after the merger drops this file into
    device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_04.py --package
    com.money.manager.ex --log steps/route_04.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "E5d5a9c2f", "Eff22f7d2", "E76c8c62d",
    "Ee424c2e8", "Ebc409bd4", "Ebb57ba7f", "E5e7583d5", "E6cd10559",
    "E994a6b75", "Edad2b982", "E1dd987db", "Ea773e4f7", "E5b32226d",
    "E8fff51bb", "Ec61a85d5", "E389c8c33", "Eb2d9679c", "E681ef2c6",
    "E559fcfcd", "E0fa71f9a", "Efa1f37dd", "Ecac14a18",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_04", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E71c76102: Launch the MAIN/LAUNCHER activity.
        r.launch("com.money.manager.ex/.home.MainActivity",
                 edge="E71c76102")
        # E2e074fc1: Framework calls MainActivity.onCreate.
        r.comment("framework calls MainActivity.onCreate",
                  edge="E2e074fc1")
        # E5d5a9c2f: onCreate calls initHomeFragment (:238).
        r.comment("MainActivity.onCreate calls initHomeFragment",
                  edge="E5d5a9c2f")
        # Eff22f7d2: HomeFragment committed; home screen shown.
        r.comment("home screen shown (HomeFragment committed)",
                  edge="Eff22f7d2")
        # E76c8c62d: Tap the seeded account child row. The row's
        # text is the setup-known name "RetryCheck"
        # (home/HomeFragment.java:686-706: onChildClick posts the
        # account event at 704; the account exists because setup
        # created it, and its group is expanded by default).
        r.tap(text="RetryCheck", edge="E76c8c62d")
        # Ee424c2e8: onChildClick posts RequestAccountFragmentEvent
        # (non-investment branch, HomeFragment.java:701-703).
        r.comment("child click posts RequestAccountFragmentEvent",
                  edge="Ee424c2e8")
        # Ebc409bd4: MainActivity.onEvent shows the account fragment
        # (:456). No user action.
        r.comment("onEvent shows account fragment", edge="Ebc409bd4")
        # Ebb57ba7f: showAccountFragment creates the list fragment
        # (:786). No user action.
        r.comment("showAccountFragment creates list fragment",
                  edge="Ebb57ba7f")
        # E5e7583d5: newInstance creates the fragment (:103).
        r.comment("newInstance creates fragment", edge="E5e7583d5")
        # E6cd10559: FragmentManager attaches the fragment.
        r.comment("fragment attached", edge="E6cd10559")
        # E994a6b75: Framework calls onCreate after onAttach.
        r.comment("framework calls onCreate", edge="E994a6b75")
        # Edad2b982: Framework calls onCreateView after onCreate.
        r.comment("framework calls onCreateView", edge="Edad2b982")
        # E1dd987db: onCreateView shows the account transaction list
        # (AccountTransactionListFragment.java:163, 850).
        r.comment("account transaction list shown", edge="E1dd987db")
        # Ea773e4f7: Open the options menu and choose the status
        # filter, then "None". The fragment inflates
        # menu_transaction_status_selector.xml (AccountTransaction-
        # ListFragment.java:237-240): parent item title
        # @string/status_filter = "Filter by Status"
        # (strings.xml:577), child @string/status_none = "None"
        # (strings.xml:161). The MENU key opens the overflow menu;
        # the parent tap opens its submenu.
        r.key("MENU", edge="Ea773e4f7")
        r.tap(text="Filter by Status", edge="Ea773e4f7")
        r.tap(text="None", edge="Ea773e4f7")
        # E5b32226d: onOptionsItemSelected dispatches to
        # isStatusSelectionHandled (:292). No user action.
        r.comment("menu dispatch calls isStatusSelectionHandled",
                  edge="E5b32226d")
        # E8fff51bb: isStatusSelectionHandled toggles the filter and
        # calls loadTransactions (:587). No user action.
        r.comment("status handler calls loadTransactions",
                  edge="E8fff51bb")
        # Ec61a85d5: loadTransactions calls loadData on the child
        # AllData fragment (:330). No user action.
        r.comment("loadTransactions calls AllData loadData",
                  edge="Ec61a85d5")
        # E389c8c33: The loader delivers its cursor to onLoadFinished
        # (AllDataListFragment.java:262, 521-533). No user action.
        r.comment("loader delivers cursor to onLoadFinished",
                  edge="E389c8c33")
        # Eb2d9679c: onLoadFinished forwards to the parent callbacks
        # (:264). No user action.
        r.comment("onLoadFinished forwards to parent", edge="Eb2d9679c")
        # E681ef2c6: The parent's onLoadFinished (detail loader id)
        # calls populateRunningBalance (:375). No user action.
        r.comment("parent onLoadFinished calls populateRunningBalance",
                  edge="E681ef2c6")
        # E559fcfcd: populateRunningBalance executes the balance task
        # (:644); the framework runs doInBackground. No user action.
        r.comment("balance task executed", edge="E559fcfcd")
        # E0fa71f9a: Framework posts the task result to onPostExecute.
        # No user action.
        r.comment("framework calls task onPostExecute",
                  edge="E0fa71f9a")
        # Efa1f37dd: onPostExecute posts RunningBalanceCalculatedEvent
        # (CalculateRunningBalanceTask2.java:99). No user action.
        r.comment("onPostExecute posts balance event",
                  edge="Efa1f37dd")
        # Ecac14a18: The fragment's onEvent calls displayRunning-
        # Balances on the child fragment (:412) -- target reached.
        r.comment("onEvent calls displayRunningBalances (target "
                  "reached)", edge="Ecac14a18")
    finally:
        r.done()


if __name__ == "__main__":
    main()
