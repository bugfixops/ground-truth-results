"""MMEX route_06: SplitRecurringCategoriesRepository.insert.

Method: SplitRecurringCategoriesRepository.insert
Edge ids (in route order):
    E71c76102 E2e074fc1 E5d5a9c2f Eff22f7d2 Ed2488d54 E025b8cae
    E3d93887f Eb35a6f3f E26b2d52c Edd72655c Ee8a5d5ca E970cca1e
    E9ee59986 Ec0590f83 Ef0a01e04 Eac972c5b E6c07b78f E22ad5956
    Eb6a8f0db E1118ea65 Eddb47239 E274e03b1 Ecf182680
Printed route source:
    graphs/MMEX/scratch/route_print_final2/SplitRecurringCategoriesRepository.insert.txt
    (23 steps; header env=- state=-). These edge ids match, in
    order, the ROUTES.csv row for SplitRecurringCategoriesRepository.insert
    exactly (checked by the helper against device-fix/routes/ROUTES.csv).
Permissions: none (print header env=-; no ENV permission gate, so no
    permission from the manifest is granted by this route).
Fixtures: none (no STATE file gate).
Setup: setup_route_06.py (bootstrap + known non-investment account
    "RetryRecur"). The previous unscriptable reason (fresh database
    has no account to save against; form-entry tap sequence
    ungrounded) is removed by the seeded account plus the form
    grounding in GROUNDING_06.md: the account is picked from the
    edit form's spinner, the payee is created inline through the
    payee picker's FAB dialog, the categories are the app's own
    tables_v1 seeds ("Bills"/"Telephone", "Food"/"Groceries"), and
    the two split entries are created fresh in the split form, so
    both have null ids and take the insert branch at
    RecurringTransactionEditActivity.java:578-580.
Why TWO splits (not one): a single split returned from the split
    form is converted into a regular transaction on the spot
    (EditTransactionCommonFunctions.onSplitConfirmed, size == 1
    branch) and again in saveData (convertOneSplitIntoRegular-
    Transaction), leaving mSplitTransactions empty, so
    saveSplitCategories would loop over nothing and insert would
    never fire. Two splits keep the split flag set through save.
Why tap_row_action for the second split: both split rows share the
    res_ids textViewCategory and editTextTotAmount
    (res/layout/item_splittransaction.xml:62, 90), so a plain
    res_id tap always resolves the first row. After the first row
    is set to $10.00, the second row is the only row whose amount
    still reads "$0.00" (USD base currency, tables_v1.sql:219),
    so tap_row_action(row_text="$0.00", ...) anchors the second
    row's own amount node; the harness picks the res_id node
    closest to that anchor (within 100 px) and fails loudly with
    LookupError if none is close, so a missed anchor can never
    silently retarget the first row. See GROUNDING_06.md risks.
Harness note: every Runner call used here exists in the landed
    b3-sweep harness (launch, comment, tap, tap_row_action,
    wait_for, type_text, done). No rotate, drag, or multi-touch
    call is used.
Run (from the repo root, after the merger drops this file into
    device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_06.py --package
    com.money.manager.ex --log steps/route_06.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "E5d5a9c2f", "Eff22f7d2", "Ed2488d54",
    "E025b8cae", "E3d93887f", "Eb35a6f3f", "E26b2d52c", "Edd72655c",
    "Ee8a5d5ca", "E970cca1e", "E9ee59986", "Ec0590f83", "Ef0a01e04",
    "Eac972c5b", "E6c07b78f", "E22ad5956", "Eb6a8f0db", "E1118ea65",
    "Eddb47239", "E274e03b1", "Ecf182680",
]

ACCT_NAME = "RetryRecur"
PAYEE_NAME = "RetryPayee"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_06", edge_ids=EDGE_IDS,
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
        # (MainActivity.java:1308-1324). No user action beyond
        # waiting for the seeded account row to be visible.
        r.wait_for(text=ACCT_NAME, edge="Eff22f7d2", timeout=30)
        # Ed2488d54: Open the drawer, then tap a top-level drawer
        # item with no sub-items. The drawer toggle's content
        # description is R.string.open = "Open"
        # (MainActivity.java:1296; res/values/strings.xml:193),
        # and the recurring item's text is
        # R.string.recurring_transactions = "Scheduled Transactions"
        # (MainActivity.java:1084-1085; res/values/strings.xml:399).
        # The group-click guard (children null, MainActivity.java:
        # 941-942) holds for this item per the printed route.
        r.tap(desc="Open", edge="Ed2488d54")
        r.tap(text="Scheduled Transactions", edge="Ed2488d54")
        # E025b8cae: The tap posts the drawer item Runnable with a
        # 200 ms delay; the framework runs run() when the delay
        # ends (MainActivity.java:953-957). No user action.
        r.comment("drawer Runnable posted (200 ms delay), framework "
                  "runs run()", edge="E025b8cae")
        # E3d93887f: run() calls onDrawerMenuAndOptionMenuSelected
        # for the recurring-transactions group item
        # (MainActivity.java:957). No user action.
        r.comment("run() calls onDrawerMenuAndOptionMenuSelected "
                  "for RECURRING", edge="E3d93887f")
        # Eb35a6f3f: The recurring case calls
        # showFragment(RecurringTransactionListFragment.class)
        # (MainActivity.java:651-652). No user action.
        r.comment("RECURRING case calls showFragment(list class)",
                  edge="Eb35a6f3f")
        # E26b2d52c: showFragment(Class) creates (or finds) the
        # fragment and shows it via showFragment(Fragment)
        # (MainActivity.java:734-752). No user action.
        r.comment("showFragment(Class) calls showFragment(Fragment)",
                  edge="E26b2d52c")
        # Edd72655c: showFragment(Fragment) shows the fragment with
        # its class name as tag (MainActivity.java:758-759).
        # No user action.
        r.comment("showFragment(Fragment) calls "
                  "showFragment(Fragment, tag)", edge="Edd72655c")
        # Ee8a5d5ca: showFragment(Fragment, String) shows the
        # fragment via showFragment_Internal
        # (MainActivity.java:768-770). No user action.
        r.comment("showFragment(Fragment, tag) calls "
                  "showFragment_Internal", edge="Ee8a5d5ca")
        # E970cca1e: showFragment_Internal replaces fragmentMain and
        # commits (MainActivity.java:1446-1466); the framework then
        # calls RecurringTransactionListFragment.onActivityCreated.
        # No user action.
        r.comment("showFragment_Internal commits; framework calls "
                  "list onActivityCreated", edge="E970cca1e")
        # E9ee59986: onActivityCreated builds the recurring list
        # (RecurringTransactionListFragment.java:94-114) and makes
        # the FAB visible (:112). No user action beyond waiting
        # for the FAB.
        r.wait_for(res_id="fab", edge="E9ee59986", timeout=30)
        # Ec0590f83: Tap the add (floating action) button. The FAB
        # click listener is wired in BaseListFragment.
        # setupFloatingActionButton (:238-244) to
        # onFloatingActionButtonClicked, which starts the editor
        # with a null id (RecurringTransactionListFragment.java:
        # 126-128).
        r.tap(res_id="fab", edge="Ec0590f83")
        # Ef0a01e04: onFloatingActionButtonClicked calls
        # startRecurringTransactionEditActivity directly
        # (RecurringTransactionListFragment.java:128). No action.
        r.comment("FAB handler calls "
                  "startRecurringTransactionEditActivity",
                  edge="Ef0a01e04")
        # Eac972c5b: startRecurringTransactionEditActivity starts
        # RecurringTransactionEditActivity with ACTION_INSERT for a
        # null id (RecurringTransactionListFragment.java:447-458).
        # No user action.
        r.comment("editor started with ACTION_INSERT",
                  edge="Eac972c5b")
        # E6c07b78f: The framework calls
        # RecurringTransactionEditActivity.onCreate. No action.
        r.comment("framework calls editor onCreate",
                  edge="E6c07b78f")
        # E22ad5956: onCreate shows the edit form
        # (RecurringTransactionEditActivity.java:98, setContentView
        # R.layout.activity_edit_recurring_transaction). No user
        # action beyond waiting for the account spinner.
        r.wait_for(res_id="spinnerAccount", edge="E22ad5956", timeout=30)
        # Eb6a8f0db: Tap the save icon in the toolbar.
        # onOptionsItemSelected maps MenuHelper.save to
        # onActionDoneClick (RecurringTransactionEditActivity.java:
        # 166-175; MenuHelper.java:37, 87-89). BEFORE that tap, the
        # form must satisfy every saveData gate, so the account,
        # payee, and two fresh splits are entered here, all logged
        # under this edge (multiple actions per edge, as in
        # route_03's long-press + menu tap under one edge):
        # -- Account: spinnerAccount (activity_edit_recurring_
        #    transaction.xml, spinnerAccount) is populated from the
        #    seeded account list by initAccountSelectors
        #    (EditTransactionCommonFunctions.java:267-283); its
        #    dropdown items carry the account names, and picking
        #    one sets transactionEntity.accountId (:330-355).
        #    Exactly one account is seeded, so this tap is
        #    unambiguous.
        r.tap(res_id="spinnerAccount", edge="Eb6a8f0db")
        r.wait_for(text=ACCT_NAME, edge="Eb6a8f0db", timeout=30)
        r.tap(text=ACCT_NAME, edge="Eb6a8f0db")
        # -- Payee: textViewPayee opens PayeeActivity with
        #    ACTION_PICK (EditTransactionCommonFunctions.java:
        #    570-584). The payee list FAB opens the new-payee
        #    dialog (PayeeListFragment.java:431-433); typing a name
        #    and tapping OK creates the payee and returns it to the
        #    form at once when picking (:389-403). validateData
        #    requires a payee for a non-transfer transaction
        #    (EditTransactionCommonFunctions.java:1175-1179).
        r.tap(res_id="textViewPayee", edge="Eb6a8f0db")
        r.wait_for(res_id="fab", edge="Eb6a8f0db", timeout=30)
        r.tap(res_id="fab", edge="Eb6a8f0db")
        r.wait_for(res_id="editTextPayeeName", edge="Eb6a8f0db",
                   timeout=30)
        r.tap(res_id="editTextPayeeName", edge="Eb6a8f0db")
        r.type_text(PAYEE_NAME, edge="Eb6a8f0db")
        r.tap(text="OK", edge="Eb6a8f0db")
        r.wait_for(text=PAYEE_NAME, edge="Eb6a8f0db", timeout=30)
        # -- Splits: splitButton opens the split form
        #    (EditTransactionCommonFunctions.java:598-618,
        #    1511-1528). showSplitCategoriesForm seeds the form
        #    with one initial split built from the transaction
        #    (createSplitFromTransaction, :1337-1348: id unset,
        #    amount 0, category NOT_SET unless the transaction has
        #    one). That first row is completed, a second row is
        #    added with the split form's FAB, and the second row is
        #    completed via tap_row_action (see docstring).
        r.tap(res_id="splitButton", edge="Eb6a8f0db")
        r.wait_for(res_id="splitsRecyclerView", edge="Eb6a8f0db",
                   timeout=30)
        # Split row 1, category: tap its category field
        # (item_splittransaction.xml:62 textViewCategory) to open
        # the category picker (SplitCategoriesAdapter.java:180-186
        # posts CategoryRequestedEvent; SplitCategoriesActivity.
        # java:217-224 shows the picker). Tap group "Bills" to
        # expand it, then child "Telephone"; the child click
        # finishes the picker at once
        # (CategoryListFragment.java:665-678). Seeded rows:
        # tables_v1.sql:108-110 (Bills id 1, Telephone id 2).
        r.tap(res_id="textViewCategory", edge="Eb6a8f0db")
        r.wait_for(text="Bills", edge="Eb6a8f0db", timeout=30)
        r.tap(text="Bills", edge="Eb6a8f0db")
        r.wait_for(text="Telephone", edge="Eb6a8f0db", timeout=30)
        r.tap(text="Telephone", edge="Eb6a8f0db")
        r.wait_for(text="Bills : Telephone", edge="Eb6a8f0db",
                   timeout=30)
        # Split row 1, amount: tap its amount field
        # (item_splittransaction.xml:90 editTextTotAmount) to open
        # the calculator (SplitCategoriesAdapter.java:159-176;
        # SplitCategoriesActivity.java:207-213). Digit buttons
        # carry their digit as text and "=" is buttonKeyEqual
        # (activity_calculator.xml:137-164); the result returns to
        # onAmountEntered (:275-284), which stores +10 for a
        # Withdrawal parent (CommonSplitCategoryLogic.java:59-65).
        r.tap(res_id="editTextTotAmount", edge="Eb6a8f0db")
        r.wait_for(res_id="buttonKeyEqual", edge="Eb6a8f0db", timeout=30)
        r.tap(text="1", edge="Eb6a8f0db")
        r.tap(text="0", edge="Eb6a8f0db")
        r.tap(res_id="buttonKeyEqual", edge="Eb6a8f0db")
        r.wait_for(text="$10.00", edge="Eb6a8f0db", timeout=30)
        # Split row 2: add it with the split form's FAB
        # (activity_split_categories.xml:69 fab;
        # SplitCategoriesActivity.java:191-193, 222-231). The new
        # row is created by SplitItemFactory (id unset, amount 0).
        r.tap(res_id="fab", edge="Eb6a8f0db")
        r.wait_for(text="$0.00", edge="Eb6a8f0db", timeout=30)
        # Split row 2, category: anchored on its own "$0.00"
        # amount node (row 1 now reads "$10.00"). Picker group
        # "Food", child "Groceries" (tables_v1.sql:116-117:
        # Food id 9, Groceries id 10); display "Food : Groceries"
        # (CategoryService.java:89-110).
        r.tap_row_action(row_text="$0.00", res_id="textViewCategory",
                         edge="Eb6a8f0db")
        r.wait_for(text="Food", edge="Eb6a8f0db", timeout=30)
        r.tap(text="Food", edge="Eb6a8f0db")
        r.wait_for(text="Groceries", edge="Eb6a8f0db", timeout=30)
        r.tap(text="Groceries", edge="Eb6a8f0db")
        r.wait_for(text="Food : Groceries", edge="Eb6a8f0db",
                   timeout=30)
        # Split row 2, amount: anchored on "$0.00" again (still
        # unset until this tap's calculator result lands).
        r.tap_row_action(row_text="$0.00", res_id="editTextTotAmount",
                         edge="Eb6a8f0db")
        r.wait_for(res_id="buttonKeyEqual", edge="Eb6a8f0db", timeout=30)
        r.tap(text="2", edge="Eb6a8f0db")
        r.tap(text="0", edge="Eb6a8f0db")
        r.tap(res_id="buttonKeyEqual", edge="Eb6a8f0db")
        r.wait_for(text="$20.00", edge="Eb6a8f0db", timeout=30)
        # Split form save: toolbar item titled "Save"
        # (SplitCategoriesActivity.java:109-122; MenuHelper.java:
        # 87-89; strings.xml:772). onActionDoneClick validates both
        # categories are set and the total (+30) is not negative
        # (:149-169), then returns both splits to the edit form
        # (:170-177); onSplitConfirmed with two splits sets the
        # split flag and the transaction amount to the split sum
        # (EditTransactionCommonFunctions.java:1413-1443).
        r.tap(text="Save", edge="Eb6a8f0db")
        r.wait_for(res_id="splitButton", edge="Eb6a8f0db", timeout=30)
        # The save tap itself: toolbar save icon, as above.
        r.tap(text="Save", edge="Eb6a8f0db")
        # E1118ea65: onOptionsItemSelected calls onActionDoneClick
        # directly (RecurringTransactionEditActivity.java:171).
        # No user action.
        r.comment("onOptionsItemSelected calls onActionDoneClick",
                  edge="E1118ea65")
        # Eddb47239: onActionDoneClick calls saveData
        # (RecurringTransactionEditActivity.java:208). No action.
        r.comment("onActionDoneClick calls saveData",
                  edge="Eddb47239")
        # E274e03b1: saveData calls saveSplitCategories
        # (RecurringTransactionEditActivity.java:544). Gates
        # already satisfied: transaction saved first (so it has an
        # id for setTransId), two splits so
        # convertOneSplitIntoRegularTransaction does not fire
        # (:1245-1255, size != 1) and isSplitSelected stays true,
        # so removeAllSplitCategories is skipped (:540-543).
        r.comment("saveData calls saveSplitCategories",
                  edge="E274e03b1")
        # Ecf182680: saveSplitCategories inserts each split whose id
        # is null or NOT_SET (RecurringTransactionEditActivity.
        # java:571-580). Both splits here were created fresh in the
        # split form (initial split via createSplitFromTransaction,
        # second via SplitItemFactory), neither ever saved, so both
        # take the insert branch -- target reached.
        r.comment("saveSplitCategories inserts the two new splits "
                  "(target reached)", edge="Ecf182680")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
