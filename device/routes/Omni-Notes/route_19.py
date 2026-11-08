"""Device route script route_19 for Omni-Notes.

Method: Category.<init>(Parcel)
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 E7e3c321b E01d0dfd6 Ee5d1ab81 E8a16cf02 Ea13ecca1
    E8425722d E48ac97e0 E49ce8c51 Ee4302599 Ea8f42099 Ee6a56786
    Ee27fa102 Ef3501eaf E1cee5491
Printed route: graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/
    sample_30_routes.txt (Category.<init>(Parcel), 21 steps; path row result
    fixed, confirmed_by SOURCE, ref CategoryActivity.java:135-159;
    DetailFragment.java:1438-1443)
Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    none.
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

One block per route edge, in route order. Lifecycle, page, explicit-call, and
framework edges with no user action get a comment, not an action. Every action
names an edge id of this route (the harness enforces it).

NOTE on log lines: the Ea8f42099 block makes three harness calls (tap the
title field, type a name, tap Save) because the guard on the edge leaving
saveCategory requires a non-empty name (CategoryActivity.java:138-141:
saveCategory returns early for an empty name). The route log therefore
has 23 lines for 21 edges; the two extra lines are that mandatory name
entry, not extra route steps.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af '
            'Ef86ebfe1 E7e3c321b E01d0dfd6 Ee5d1ab81 E8a16cf02 Ea13ecca1 '
            'E8425722d E48ac97e0 E49ce8c51 Ee4302599 Ea8f42099 Ee6a56786 '
            'Ee27fa102 Ef3501eaf E1cee5491').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_19', EDGE_IDS, a.log,
               dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    # Ea7466154 S_ENTRY -> MainActivity.<init>: launcher starts MainActivity.
    r.launch('it.feio.android.omninotes/.MainActivity', 'Ea7466154')
    # E89791c67 MainActivity.<init> -> MainActivity.onResume: lifecycle, no action.
    r.comment('Activity lifecycle callback', 'E89791c67')
    # Edf932a3c MainActivity.onResume -> MainActivity.checkPassword: cold start,
    # no password gate, no action.
    r.comment('Cold start: isPasswordAccepted false, checkPassword runs', 'Edf932a3c')
    # E075b4776 MainActivity.checkPassword -> MainActivity.init: explicit call, no action.
    r.comment('No password gate: init()', 'E075b4776')
    # E2436b969 MainActivity.init -> ListFragment.<init>: explicit call, no action.
    r.comment('init() adds the list fragment', 'E2436b969')
    # E54b170af ListFragment.<init> -> ListFragment.onActivityCreated: lifecycle, no action.
    r.comment('Fragment lifecycle callback', 'E54b170af')
    # Ef86ebfe1 ListFragment.onActivityCreated -> ListFragment.init: explicit call, no action.
    r.comment('init()', 'Ef86ebfe1')
    # E7e3c321b ListFragment.init -> S_LIST@NOTES: list set up, no action.
    r.comment('List set up on the default Notes navigation', 'E7e3c321b')
    # E01d0dfd6 S_LIST@NOTES -> Fab.lambda$init$1@LONG_NOTES: long-press the + button
    # (FloatingActionsMenu add button, res/layout/fab.xml id fab).
    r.long_tap('E01d0dfd6', res_id='it.feio.android.omninotes:id/fab')
    # Ee5d1ab81 Fab long-press -> ListFragment.lambda$initFab$0@MAIN: menu dispatch, no action.
    r.comment('onFabItemClick(fab_expand_menu_button)', 'Ee5d1ab81')
    # E8a16cf02 lambda$initFab$0@MAIN -> S_DETAIL@NEW: a new note opens, no action.
    r.comment('A new note is opened', 'E8a16cf02')
    # Ea13ecca1 S_DETAIL@NEW -> DetailFragment.onOptionsItemSelected@CATEGORY:
    # tap "Category" in the toolbar menu (menu_detail.xml, title "Category").
    r.tap('Ea13ecca1', text='Category')
    # E8425722d onOptionsItemSelected@CATEGORY -> DetailFragment.categorizeNote:
    # menu branch, no action.
    r.comment('The category branch of the menu switch', 'E8425722d')
    # E48ac97e0 DetailFragment.categorizeNote -> S_DLG_CATEGORIZE_DETAIL:
    # the categorize dialog opens, no action.
    r.comment('The categorize dialog opens', 'E48ac97e0')
    # E49ce8c51 S_DLG_CATEGORIZE_DETAIL -> DetailFragment.lambda$categorizeNote$15:
    # tap "Add category" (positive button, string add_category, DetailFragment.java:1259-1263).
    r.tap('E49ce8c51', text='Add category')
    # Ee4302599 lambda$categorizeNote$15 -> S_CATEGORY@NEW_DETAIL:
    # startActivityForResult(CategoryActivity, CATEGORY), no action.
    r.comment('CategoryActivity opens for a new category', 'Ee4302599')
    # Ea8f42099 S_CATEGORY@NEW_DETAIL -> CategoryActivity_ViewBinding$2.doClick@NEW_DETAIL:
    # tap Save. The name field must be non-empty or saveCategory returns
    # early (CategoryActivity.java:138-141), so first tap the title field
    # (res/layout/activity_category.xml id category_title) and type a name.
    # Save button: res/layout/activity_category.xml id save (text "Ok").
    r.tap('Ea8f42099', res_id='it.feio.android.omninotes:id/category_title')
    r.type_text('TestCategory', 'Ea8f42099')
    r.tap('Ea8f42099', res_id='it.feio.android.omninotes:id/save')
    # Ee6a56786 CategoryActivity_ViewBinding$2.doClick -> CategoryActivity.saveCategory:
    # ButterKnife dispatch, no action.
    r.comment('target.saveCategory()', 'Ee6a56786')
    # Ee27fa102 CategoryActivity.saveCategory -> DetailFragment.onActivityResult@CATEGORY:
    # result OK with the category, no action.
    r.comment('Result OK with the category; CategoryActivity finishes', 'Ee27fa102')
    # Ef3501eaf DetailFragment.onActivityResult@CATEGORY -> Category$1.createFromParcel:
    # intent.getParcelableExtra("category") reads the CREATOR by reflection, no action.
    r.comment('getParcelableExtra("category") via Parcel CREATOR', 'Ef3501eaf')
    # E1cee5491 Category$1.createFromParcel -> Category.<init>(Parcel):
    # explicit call, no user action; the coverage lookup detects the target.
    r.comment('new Category(parcel)', 'E1cee5491')
    r.done()


if __name__ == '__main__':
    main()
