"""Device route script route_10 for Omni-Notes.

Method: ListFragment.lambda$null$11
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 E7e3c321b E89ba0d21 Eb4f41bd1 Ec31c30d8 E019e67d4 Eccf28a6b
    E08562d26 E2512e0de E0ece6056 E14dd6414 Ef5b969b2 E4e300f9e Ecca2d816
Printed route: graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/sample_30_routes.txt
    (ListFragment.lambda$null$11, 20 steps; ListFragment.java:1352-1364;
    BaseActivity.java:115-134)
Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    none.
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

One block per route edge, in route order. Lifecycle, page, explicit-call, and
framework edges with no user action get a comment, not an action. Every action
names an edge id of this route (the harness enforces it). The trashed note
the route needs (STATE "a trashed note exists, so the Trash entry shows in
the drawer") is created as STATE steps folded into the E89ba0d21 block,
before that edge's own drawer tap, following the precedent for STATE steps
in other device scripts; it is marked STATE there, not presented as the
E89ba0d21 trigger itself.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af '
            'Ef86ebfe1 E7e3c321b E89ba0d21 Eb4f41bd1 Ec31c30d8 E019e67d4 '
            'Eccf28a6b E08562d26 E2512e0de E0ece6056 E14dd6414 Ef5b969b2 '
            'E4e300f9e Ecca2d816').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_10', EDGE_IDS, a.log,
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
    # open the drawer. STATE first (this route needs a trashed note): create
    # a note the way route_01 creates one — long-press the + button
    # (res/layout/fab.xml id fab), tap the title field
    # (res/layout/fragment_detail.xml id detail_title) and the content field
    # (res/layout/fragment_detail_content.xml id detail_content), type, then
    # Back saves the note — then long-press the note to open the CAB and tap
    # Trash in it (menu_list.xml id menu_trash, title "Trash"; the item has
    # an icon, so this taps by content description — see report).
    r.long_tap('E89ba0d21', res_id='it.feio.android.omninotes:id/fab')
    r.tap('E89ba0d21', res_id='it.feio.android.omninotes:id/detail_title')
    r.type_text('Route10 note', 'E89ba0d21')
    r.tap('E89ba0d21', res_id='it.feio.android.omninotes:id/detail_content')
    r.type_text('Route10 trashed note', 'E89ba0d21')
    r.back('E89ba0d21')
    r.long_tap('E89ba0d21', text='Route10 note')
    r.tap('E89ba0d21', desc='Trash')
    # The edge's own trigger: open the drawer via the toolbar navigation
    # icon. UNCERTAINTY: the icon's content description is set by
    # ActionBarDrawerToggle from R.string.drawer_open ("drawer open",
    # NavigationDrawerFragment.java:172-177); it is not verified on device.
    r.tap('E89ba0d21', desc='drawer open')
    # Eb4f41bd1 onDrawerOpened@NOTES -> S_DRAWER@NOTES: the drawer is open, no action.
    r.comment('The drawer is open', 'Eb4f41bd1')
    # Ec31c30d8 S_DRAWER@NOTES -> MainMenuTask.lambda$onPostExecute$0@TRASH:
    # tap "Trash" in the drawer (res/values/arrays.xml navigation_list).
    r.tap('Ec31c30d8', text='Trash')
    # E019e67d4 lambda$onPostExecute$0@TRASH -> S_LIST@TRASH: updateNavigation(TRASH),
    # the drawer closes and the list reloads for Trash, no action.
    r.comment('updateNavigation(TRASH): the list reloads for Trash', 'E019e67d4')
    # Eccf28a6b S_LIST@TRASH -> ListFragment.lambda$initListView$3@START_TRASH:
    # long-press the trashed note (its title is the row text in
    # res/layout/note_layout.xml, id note_title).
    r.long_tap('Eccf28a6b', text='Route10 note')
    # E08562d26 lambda$initListView$3@START_TRASH -> S_LIST_CAB@TRASH: one note
    # is selected, the contextual action bar replaces the toolbar, no action.
    r.comment('One note selected: the contextual action bar replaces the toolbar', 'E08562d26')
    # E2512e0de S_LIST_CAB@TRASH -> ListFragment$ModeCallback.onActionItemClicked@DELETE:
    # tap "Delete" in the action bar (menu_list.xml id menu_delete, title
    # "Delete"; the item has an icon, so this taps by content description —
    # see report).
    r.tap('E2512e0de', desc='Delete')
    # E0ece6056 onActionItemClicked@DELETE -> ListFragment.performAction@C_DELETE:
    # explicit call, no action.
    r.comment('performAction(item, mode)', 'E0ece6056')
    # E14dd6414 performAction@C_DELETE -> ListFragment.deleteNotes: the delete
    # branch of the action switch, no action.
    r.comment('The delete branch of the action switch', 'E14dd6414')
    # Ef5b969b2 ListFragment.deleteNotes -> S_DLG_DELETE_NOTES: the confirmation
    # opens, no action.
    r.comment('The delete confirmation opens', 'Ef5b969b2')
    # E4e300f9e S_DLG_DELETE_NOTES -> ListFragment.lambda$deleteNotes$12: tap OK
    # (ListFragment.java:1356, positiveText R.string.ok = "Ok").
    r.tap('E4e300f9e', text='Ok')
    # Ecca2d816 lambda$deleteNotes$12 -> ListFragment.lambda$null$11: the password
    # validator runs at once when no selected note is locked
    # (BaseActivity.java:115-134); no locked note and no password-on-access
    # preference, so no password dialog appears. No action; the coverage
    # lookup detects the target.
    r.comment('Password validator runs at once: no locked note', 'Ecca2d816')
    r.done()


if __name__ == '__main__':
    main()
