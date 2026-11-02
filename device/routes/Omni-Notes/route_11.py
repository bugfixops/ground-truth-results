"""Device route script route_11 for Omni-Notes.

Method: CategoryBaseAdapter.isSelected
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 Ec8760433 E77ad74f6 Ea72b76f0 E35dec0d3 E7fc93c0a E3a7050d7
    Ed97d541a E9ad476c5 E4c082c59 Ed64c618a
Printed route: the trigger graph path for CategoryBaseAdapter.isSelected
    (graphs/Omni-Notes/out/omni-notes_trigger_graph.json, paths entry;
    sample_30_routes.txt has no block for this method). Ref
    CategoryBaseAdapter.java:100-103.
Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    none.
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

One block per route edge, in route order. This route has NO gui edge at all:
every edge is lifecycle, call, async, or framework, so the cold-start chain
below is comments only. The category the route needs (STATE "at least one
category exists (create it from a note or the CAB: Category > Add
category)") cannot exist on a fresh, cleared process, so it is created as
STATE steps folded into the E4c082c59 block — the edge whose guard is that
category list binding — followed by opening the drawer so the category
rows actually bind (CategoryBaseAdapter.getView -> isSelected). The real
getView/isSelected firing therefore happens on the post-creation list
reload plus drawer open, not on the cold-start chain (which runs before
any category exists); the STATE steps are marked STATE, not presented as
the E4c082c59 trigger itself. Every action names an edge id of this route
(the harness enforces it).
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af '
            'Ef86ebfe1 Ec8760433 E77ad74f6 Ea72b76f0 E35dec0d3 E7fc93c0a '
            'E3a7050d7 Ed97d541a E9ad476c5 E4c082c59 Ed64c618a').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_11', EDGE_IDS, a.log,
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
    # Ec8760433 ListFragment.init -> ListFragment.initNotesList: explicit call, no action.
    r.comment('initNotesList()', 'Ec8760433')
    # E77ad74f6 initNotesList -> NoteLoaderTask.doInBackground@ALL: async, no action.
    r.comment('NoteLoaderTask executes with the all query', 'E77ad74f6')
    # Ea72b76f0 NoteLoaderTask.doInBackground@ALL -> NoteLoaderTask.onPostExecute:
    # async delivery on the main thread, no action.
    r.comment('The list of notes is delivered on the main thread', 'Ea72b76f0')
    # E35dec0d3 NoteLoaderTask.onPostExecute -> NavigationDrawerFragment.onEvent(NotesLoadedEvent):
    # framework EventBus delivery, no action.
    r.comment('NotesLoadedEvent reaches the drawer fragment', 'E35dec0d3')
    # E7fc93c0a onEvent(NotesLoadedEvent) -> NavigationDrawerFragment.refreshMenus:
    # explicit call, no action.
    r.comment('The drawer menus are rebuilt after a load', 'E7fc93c0a')
    # E3a7050d7 refreshMenus -> NavigationDrawerFragment.buildCategoriesMenu:
    # explicit call, no action.
    r.comment('buildCategoriesMenu()', 'E3a7050d7')
    # Ed97d541a buildCategoriesMenu -> CategoryMenuTask.doInBackground: async, no action.
    r.comment('CategoryMenuTask executes', 'Ed97d541a')
    # E9ad476c5 CategoryMenuTask.doInBackground -> CategoryMenuTask.onPostExecute:
    # async delivery on the main thread, no action.
    r.comment('The categories are delivered on the main thread', 'E9ad476c5')
    # E4c082c59 CategoryMenuTask.onPostExecute -> CategoryBaseAdapter.getView:
    # the category list binds the rows. STATE first (this edge needs at
    # least one category): create a note the way route_01 creates one —
    # long-press the + button (res/layout/fab.xml id fab), tap the title
    # field (res/layout/fragment_detail.xml id detail_title) and the
    # content field (res/layout/fragment_detail_content.xml id
    # detail_content), type — then tap "Category" in the toolbar menu
    # (menu_detail.xml, title "Category"), tap "Add category" in the
    # categorize dialog (DetailFragment.java:1255, positiveText
    # R.string.add_category), tap the category title field
    # (res/layout/activity_category.xml id category_title), type a name
    # (saveCategory returns early for an empty name,
    # CategoryActivity.java:138-141), tap Save
    # (res/layout/activity_category.xml id save), then Back saves the note
    # and returns to the list (the list reload re-runs the loader chain
    # above), then open the drawer so the category rows bind. The drawer
    # tap uses the toolbar navigation icon's content description, set by
    # ActionBarDrawerToggle from R.string.drawer_open ("drawer open",
    # NavigationDrawerFragment.java:172-177) — not verified on device
    # (see report).
    r.long_tap('E4c082c59', res_id='it.feio.android.omninotes:id/fab')
    r.tap('E4c082c59', res_id='it.feio.android.omninotes:id/detail_title')
    r.type_text('Route11 note', 'E4c082c59')
    r.tap('E4c082c59', res_id='it.feio.android.omninotes:id/detail_content')
    r.type_text('Route11 category note', 'E4c082c59')
    r.tap('E4c082c59', text='Category')
    r.tap('E4c082c59', text='Add category')
    r.tap('E4c082c59', res_id='it.feio.android.omninotes:id/category_title')
    r.type_text('Route11cat', 'E4c082c59')
    r.tap('E4c082c59', res_id='it.feio.android.omninotes:id/save')
    r.back('E4c082c59')
    r.tap('E4c082c59', desc='drawer open')
    # The edge's own trigger: the category list binds the rows.
    r.comment('The category list binds the rows', 'E4c082c59')
    # Ed64c618a CategoryBaseAdapter.getView -> CategoryBaseAdapter.isSelected:
    # explicit call, no action; the coverage lookup detects the target.
    r.comment('Direct call (CategoryBaseAdapter.java:103)', 'Ed64c618a')
    r.done()


if __name__ == '__main__':
    main()
