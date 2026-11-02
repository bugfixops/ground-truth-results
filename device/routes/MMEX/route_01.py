"""MMEX route_01: DbModule_ProvideSqlBriteFactory.get.

Method: DbModule_ProvideSqlBriteFactory.get
Edge ids (in route order):
    E71c76102 E2e074fc1 E5d5a9c2f Eff22f7d2 Ed2488d54 E025b8cae
    E02874fba Eb67eeff0 E47458fa6 E5088b239 E8d4447d7 E735ef13f
    E4c5a74a5 Eda7c2af3 E15484870 E1a87ef70 E395cc156 Ec1927c7b
    E4ed0c88b Ee49dd0ee Ec6878fc1 E12dd1c09 Ef5f10483 E7b93cac7
    E7f59a892 Ecc6f8612 E128a3843
Printed route source:
    graphs/MMEX/scratch/route_print_final2/DbModule_ProvideSqlBriteFactory.get.txt
    (27 steps; edge list verified identical to the verification.csv
    path row for DbModule_ProvideSqlBriteFactory.get, result correct).
Launch component: com.money.manager.ex/.home.MainActivity, the
    MAIN/LAUNCHER activity (AndroidManifest.xml:136-143, package
    com.money.manager.ex at AndroidManifest.xml:19).
Permissions: none. The print header has env=-, so no ENV permission
    gate applies; the manifest declares only normal install-time
    permissions plus READ/WRITE_EXTERNAL_STORAGE, USE_FINGERPRINT and
    WAKE_LOCK, none of which this route gates on.
Fixtures: none (no STATE file gate in the print header).
Setup: setup_route_01.py bootstrap (first-run tutorial off + app-created
database); budget + category rows are a follow-up seed, not satisfied here.
State preconditions (read before judging the real run): the route
    assumes a valid database is present and the first-run tutorial
    already dismissed -- on a literal pm-clear first launch
    MainActivity.showPrerequisite() diverts to TutorialActivity
    (home/MainActivity.java:184, 1478-1490) and the home screen never
    appears, so the run harness must clear that prerequisite first.
    It also needs at least one budget (for the budget-row tap) and at
    least one category (so the budget-detail loader delivers a row to
    BudgetAdapter.bindView); a fresh database created by
    MmxOpenHelper.onCreate (database/MmxOpenHelper.java:94-103) holds
    only tables, a base currency and a date format, so those rows
    must come from prior in-app data creation, not from this script.
Run (from the repo root, once merged to device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_01.py --package
    com.money.manager.ex --log steps/route_01.log
    --outdir <outdir> [--dry-run] [--adb adb]
Draft location: finish/work/MMEX/device-draft/g1/route_01.py; the
    import below resolves once the file sits under device/routes/MMEX/
    as in the Currency template scripts.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "E5d5a9c2f", "Eff22f7d2", "Ed2488d54",
    "E025b8cae", "E02874fba", "Eb67eeff0", "E47458fa6", "E5088b239",
    "E8d4447d7", "E735ef13f", "E4c5a74a5", "Eda7c2af3", "E15484870",
    "E1a87ef70", "E395cc156", "Ec1927c7b", "E4ed0c88b", "Ee49dd0ee",
    "Ec6878fc1", "E12dd1c09", "Ef5f10483", "E7b93cac7", "E7f59a892",
    "Ecc6f8612", "E128a3843",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_01", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E71c76102: Tap the MMEX icon in the launcher
        # (MAIN/LAUNCHER intent filter, AndroidManifest.xml:136-143).
        r.launch("com.money.manager.ex/.home.MainActivity",
                 edge="E71c76102")
        # E2e074fc1: The system instantiates MainActivity, then
        # calls onCreate.
        r.comment("system instantiates MainActivity, then onCreate",
                  edge="E2e074fc1")
        # E5d5a9c2f: onCreate calls initHomeFragment
        # (home/MainActivity.java:238).
        r.comment("MainActivity.onCreate calls initHomeFragment",
                  edge="E5d5a9c2f")
        # Eff22f7d2: initHomeFragment commits HomeFragment; the home
        # screen is shown.
        r.comment("initHomeFragment commits HomeFragment (home shown)",
                  edge="Eff22f7d2")
        # Ed2488d54: Open the drawer, then tap a top-level drawer
        # item with no sub-items. The Menu key toggles the drawer
        # (home/MainActivity.java:407-419, KEYCODE_MENU branch), and
        # the Budgets group item text is @string/budgets = "Budgets"
        # (res/values/strings.xml:561; item built at
        # home/MainActivity.java:1090-1093, case at 654-657).
        r.key("MENU", edge="Ed2488d54")
        r.tap(text="Budgets", edge="Ed2488d54")
        # E025b8cae: The tap posts the drawer-item Runnable with a
        # 200 ms delay; the framework runs run().
        r.comment("drawer Runnable posted (200 ms delay), framework "
                  "runs run()", edge="E025b8cae")
        # E02874fba: run() calls onDrawerMenuAndOptionMenuSelected
        # with the tapped group item.
        r.comment("run() calls onDrawerMenuAndOptionMenuSelected "
                  "with the group item", edge="E02874fba")
        # Eb67eeff0: case R.id.menu_budgets starts BudgetsActivity.
        r.comment("case menu_budgets starts BudgetsActivity",
                  edge="Eb67eeff0")
        # E47458fa6: The system instantiates BudgetsActivity, then
        # onCreate.
        r.comment("system instantiates BudgetsActivity, then onCreate",
                  edge="E47458fa6")
        # E5088b239: onCreate sets the layout and createFragments
        # adds BudgetListFragment; the budget list is shown.
        r.comment("BudgetsActivity shows the budget list",
                  edge="E5088b239")
        # E8d4447d7: Tap a budget row. BudgetListFragment builds its
        # rows from android.R.layout.simple_list_item_1 with the
        # budget year name in android.R.id.text1
        # (budget/BudgetListFragment.java:227); the first matching
        # text1 node is the first budget row, and the row text itself
        # is database data, so no literal text is asserted here.
        # Precondition: at least one budget exists (see docstring).
        r.tap(res_id="text1", edge="E8d4447d7")
        # E735ef13f: onListItemClick posts BudgetSelectedEvent on
        # EventBus (budget/BudgetListFragment.java:215).
        r.comment("onListItemClick posts BudgetSelectedEvent",
                  edge="E735ef13f")
        # E4c5a74a5: BudgetsActivity.onEvent calls
        # showBudgetDetails (budget/BudgetsActivity.java:84).
        r.comment("onEvent calls showBudgetDetails",
                  edge="E4c5a74a5")
        # Eda7c2af3: showBudgetDetails calls
        # BudgetDetailFragment.newInstance
        # (budget/BudgetsActivity.java:137).
        r.comment("showBudgetDetails calls BudgetDetailFragment "
                  "newInstance", edge="Eda7c2af3")
        # E15484870: newInstance constructs the fragment
        # (budget/BudgetDetailFragment.java:59).
        r.comment("newInstance constructs BudgetDetailFragment",
                  edge="E15484870")
        # E1a87ef70: showFragment commits the transaction; the
        # FragmentManager calls onCreate.
        r.comment("fragment transaction commits; onCreate called",
                  edge="E1a87ef70")
        # E395cc156: onCreate -> onCreateView.
        r.comment("BudgetDetailFragment onCreate -> onCreateView",
                  edge="E395cc156")
        # Ec1927c7b: onCreateView -> onViewCreated, which starts the
        # budget loader via displayBudget.
        r.comment("onViewCreated starts the budget loader "
                  "(displayBudget)", edge="Ec1927c7b")
        # E4ed0c88b: onViewCreated calls displayBudget
        # (budget/BudgetDetailFragment.java:122).
        r.comment("onViewCreated calls displayBudget",
                  edge="E4ed0c88b")
        # Ee49dd0ee: displayBudget initLoader starts the loader;
        # LoaderManager calls onCreateLoader.
        r.comment("initLoader starts the budget detail loader",
                  edge="Ee49dd0ee")
        # Ec6878fc1: The loader delivers its cursor; LoaderManager
        # calls onLoadFinished.
        r.comment("loader delivers cursor; onLoadFinished called",
                  edge="Ec6878fc1")
        # E12dd1c09: changeCursor makes the adapter valid and it has
        # rows, so CursorAdapter.getView calls bindView per row.
        # Precondition: at least one category row (see docstring).
        r.comment("changeCursor -> adapter bindView per visible row",
                  edge="E12dd1c09")
        # Ef5f10483: bindView calls getActualAmount
        # (budget/BudgetAdapter.java:141).
        r.comment("bindView calls getActualAmount",
                  edge="Ef5f10483")
        # E7b93cac7: getActualAmount calls getAmountForCategory
        # (budget/BudgetAdapter.java:213).
        r.comment("getActualAmount calls getAmountForCategory",
                  edge="E7b93cac7")
        # E7f59a892: getAmountForCategory calls loadTotalFor
        # (budget/BudgetAdapter.java:256).
        r.comment("getAmountForCategory calls loadTotalFor",
                  edge="E7f59a892")
        # Ecc6f8612: loadTotalFor calls databaseLazy.get()
        # (budget/BudgetAdapter.java:278), which runs the Dagger
        # DbModule_ProvideDatabaseFactory provider.
        r.comment("databaseLazy.get() runs ProvideDatabaseFactory",
                  edge="Ecc6f8612")
        # E128a3843: The generated ProvideDatabaseFactory passes its
        # Provider<SqlBrite> argument into DbModule.provideDatabase
        # (db/DbModule.java:61), reaching
        # DbModule_ProvideSqlBriteFactory.get. TARGET REACHED.
        r.comment("Provider<SqlBrite> argument reaches "
                  "DbModule_ProvideSqlBriteFactory.get (target)",
                  edge="E128a3843")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
