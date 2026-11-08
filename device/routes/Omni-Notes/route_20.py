"""Device route script route_20 for Omni-Notes.

Method: DbHelper.deleteCategory
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 E7e3c321b E89ba0d21 Eb4f41bd1 Ecbafdd94 E42e7dc4c
    Eeb2afcb4 Ec82c3d2e Ed93a59e7 E0814a03b E09c2560c Ecfb9ab53
    E6f944352
Printed route: graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/
    sample_30_routes.txt (DbHelper.deleteCategory, 19 steps; path row result
    fixed, confirmed_by SOURCE, ref CategoryActivity.java:162-188;
    CategoryMenuTask.java:144-157)
Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    none.
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

PRECONDITION — a category must exist: the route's long-press edge
(Ecbafdd94) needs at least one category in the drawer (STATE in
methods.csv: "At least one category exists (create it from a note or
the CAB: Category > Add category)"), but run_app.sh clears the app
before each script, so no category survives into this run. This script
therefore creates one first, in a separate pre-phase Runner with no
edge checks (the setup.py mechanism from device/README.md), writing
its own log to <outdir>/route_20_setup.log so the route log keeps
exactly one line per route edge. The pre-phase reuses the route_19
flow (new note -> Category -> Add category -> type name -> Save) and
then presses Back to return to the note list; the category name it
creates, "D3Category", is the exact text the route's long-press taps.
If the merger instead ships a per-app setup.py that creates the
category, delete the pre-phase block and the route block below is
unchanged.

One block per route edge, in route order. Lifecycle, page, explicit-call, and
framework edges with no user action get a comment, not an action. Every route
action names an edge id of this route (the harness enforces it).
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af '
            'Ef86ebfe1 E7e3c321b E89ba0d21 Eb4f41bd1 Ecbafdd94 E42e7dc4c '
            'Eeb2afcb4 Ec82c3d2e Ed93a59e7 E0814a03b E09c2560c Ecfb9ab53 '
            'E6f944352').split()

CATEGORY_NAME = 'D3Category'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    # Pre-phase: create the category the route will delete. Edge checks off
    # (setup-style Runner, placeholder edge label 'setup'); logged
    # separately, never in the route log.
    s = Runner(a.package, 'route_20_setup', None,
               os.path.join(a.outdir, 'route_20_setup.log'),
               dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    s.launch('it.feio.android.omninotes/.MainActivity', 'setup')
    s.long_tap('setup', res_id='it.feio.android.omninotes:id/fab')
    s.tap('setup', text='Category')
    s.tap('setup', text='Add category')
    s.tap('setup', res_id='it.feio.android.omninotes:id/category_title')
    s.type_text(CATEGORY_NAME, 'setup')
    s.tap('setup', res_id='it.feio.android.omninotes:id/save')
    s.back('setup')
    s.done()
    # Route block: one block per edge, in route order.
    r = Runner(a.package, 'route_20', EDGE_IDS, a.log,
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
    # E89ba0d21 S_LIST@NOTES -> NavigationDrawerFragment$1.onDrawerOpened@NOTES:
    # tap the menu icon. The drawer toggle is an ActionBarDrawerToggle on
    # the toolbar (NavigationDrawerFragment.java:172-177) with
    # R.string.drawer_open = "drawer open" (strings.xml), which the
    # toggle sets as the navigation icon's content description.
    r.tap('E89ba0d21', desc='drawer open')
    # Eb4f41bd1 NavigationDrawerFragment$1.onDrawerOpened@NOTES -> S_DRAWER@NOTES:
    # the drawer is open, no action.
    r.comment('The drawer is open', 'Eb4f41bd1')
    # Ecbafdd94 S_DRAWER@NOTES -> CategoryMenuTask.lambda$buildCategoryMenuLongClickEvent$2:
    # long-press the category created in the pre-phase. Drawer rows use
    # res/layout/drawer_list_item.xml with the title set to the category
    # name (CategoryBaseAdapter.java: getView sets txtTitle to
    # category.getName()), so the row text is the created name.
    r.long_tap('Ecbafdd94', text=CATEGORY_NAME)
    # E42e7dc4c lambda$buildCategoryMenuLongClickEvent$2 -> MainActivity.editTag:
    # explicit call, no action.
    r.comment('editTag((Category) item)', 'E42e7dc4c')
    # Eeb2afcb4 MainActivity.editTag -> ListFragment.editCategory: explicit call, no action.
    r.comment('editCategory(tag)', 'Eeb2afcb4')
    # Ec82c3d2e ListFragment.editCategory -> S_CATEGORY@EDIT:
    # startActivityForResult(CategoryActivity) with the category, no action.
    r.comment('CategoryActivity opens for editing', 'Ec82c3d2e')
    # Ed93a59e7 S_CATEGORY@EDIT -> CategoryActivity_ViewBinding$3.doClick:
    # tap Delete. Delete button: res/layout/activity_category.xml id delete
    # (text "Delete"); it is visible for an existing category
    # (CategoryActivity.java populateViews: visible iff name non-empty).
    r.tap('Ed93a59e7', res_id='it.feio.android.omninotes:id/delete')
    # E0814a03b CategoryActivity_ViewBinding$3.doClick -> CategoryActivity.deleteCategory:
    # ButterKnife dispatch, no action.
    r.comment('target.deleteCategory()', 'E0814a03b')
    # E09c2560c CategoryActivity.deleteCategory -> S_DLG_DELETE_CATEGORY:
    # the confirmation dialog opens, no action.
    r.comment('The delete confirmation opens', 'E09c2560c')
    # Ecfb9ab53 S_DLG_DELETE_CATEGORY -> CategoryActivity.lambda$deleteCategory$0:
    # tap Confirm (positive button, string confirm, CategoryActivity.java:170-187).
    r.tap('Ecfb9ab53', text='Confirm')
    # E6f944352 CategoryActivity.lambda$deleteCategory$0 -> DbHelper.deleteCategory:
    # direct call, no user action; the coverage lookup detects the target.
    r.comment('Direct call to db.deleteCategory(category)', 'E6f944352')
    r.done()


if __name__ == '__main__':
    main()
