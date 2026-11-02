"""Device route script route_23 for Omni-Notes.

Method: NoteProcessor.afterProcess
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 E7e3c321b E21137a71 E9d602f5d E1bc6a5ff E122830ee E311e6e41
    E3bf9a503 E6cde554f Eab8f789f
Printed route: graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/sample_30_routes.txt
    does NOT contain this method (only 30 of 33 routes are printed there);
    edge list and trigger/gui text below come from ROUTES.csv and
    graphs/Omni-Notes/out/omni-notes_trigger_graph.json instead
    (ListFragment.java:572-575,1688-1715; NoteProcessor.java:40-68).
Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    none (ROUTES.csv route_23 permission column is empty).
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

One block per route edge, in route order. Lifecycle, page, explicit-call, and
framework edges with no user action get a comment, not an action. Every action
names an edge id of this route (the harness enforces it).

PRE-ROUTE SETUP (between the E7e3c321b block and the E21137a71 block): the
route's E122830ee edge carries the STATE "a trash is pending (the undo bar
shows)", and pm clear leaves the list empty, so the script first creates one
note and trashes it. Those setup actions are logged against route edges
(E7e3c321b for the note creation on the list screen, E21137a71 for the
list touches that select and trash the note) because the harness requires
every action to name an edge id of this route; the route's own touch is the
final tap on the list, after the undo bar shows. trashNotes(true) in
ListFragment.java:1272-1304 removes the note, shows the undo bar
(undobar.xml) and sets undoTrash, which is what commitPending() then
commits when the list is touched again.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af '
            'Ef86ebfe1 E7e3c321b E21137a71 E9d602f5d E1bc6a5ff E122830ee '
            'E311e6e41 E3bf9a503 E6cde554f Eab8f789f').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_23', EDGE_IDS, a.log,
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
    # --- Pre-route setup: create one note, then trash it so the undo bar shows.
    # Long-press the + button (FloatingActionsMenu, res/layout/fab.xml id fab),
    # as in the route_01 template, to open a new note editor.
    r.long_tap('E7e3c321b', res_id='it.feio.android.omninotes:id/fab')
    # Tap the title field (res/layout/fragment_detail.xml id detail_title)
    # and give the note a title so its list row can be found again.
    r.tap('E7e3c321b', res_id='it.feio.android.omninotes:id/detail_title')
    r.type_text('Trash me', 'E7e3c321b')
    # Back saves the note (DetailFragment save path) and returns to the list.
    r.back('E7e3c321b')
    r.wait_for('E7e3c321b', text='Trash me')
    # Long-press the note row (ListFragment.java:507 starts CAB mode) ...
    r.long_tap('E21137a71', text='Trash me')
    # ... then tap "Trash" in the contextual menu (res/menu/menu_list.xml
    # menu_trash, title @string/trash = "Trash"; ListFragment.java:867
    # calls trashNotes(true), which shows the undo bar and sets undoTrash).
    r.tap('E21137a71', text='Trash')
    # The undo bar (res/layout/fragment_list.xml id undobar, undobar.xml)
    # must be showing: that is the route's pending-trash state.
    r.wait_for('E21137a71', res_id='it.feio.android.omninotes:id/undobar')
    # E21137a71 S_LIST@NOTES -> InterceptorLinearLayout.onInterceptTouchEvent:
    # touch the notes list again. Any touch dispatched inside list_root
    # (res/layout/fragment_list.xml id list_root) first passes through
    # InterceptorLinearLayout.onInterceptTouchEvent, which calls
    # onViewTouchOccurred even though the list is now empty (the trashed
    # note was removed from the adapter; the empty view sits inside
    # list_root, so the touch still goes through the interceptor).
    r.tap('E21137a71', res_id='it.feio.android.omninotes:id/list_root')
    # E9d602f5d onInterceptTouchEvent -> ListFragment.onViewTouchOccurred:
    # listener dispatch, no action.
    r.comment('OnViewTouchedListener.onViewTouchOccurred', 'E9d602f5d')
    # E1bc6a5ff onViewTouchOccurred -> ListFragment.commitPending: explicit
    # call, no action (ListFragment.java:572-575 calls commitPending()).
    r.comment('commitPending()', 'E1bc6a5ff')
    # E122830ee commitPending -> ListFragment.trashNote: the pending change is
    # applied; guard holds because the undo bar showed (undoTrash true,
    # ListFragment.java:1688-1715).
    r.comment('Pending trash applied: trashNote(notes, true)', 'E122830ee')
    # E311e6e41 trashNote -> NoteProcessor.process@TRASH: explicit call, no action.
    r.comment('new NoteProcessorTrash(notes).process()', 'E311e6e41')
    # E3bf9a503 NoteProcessor.process@TRASH -> NotesProcessorTask.doInBackground@TRASH:
    # AsyncTask executeOnExecutor, no user action.
    r.comment('NotesProcessorTask executes on the thread pool', 'E3bf9a503')
    # E6cde554f doInBackground@TRASH -> onPostExecute@TRASH: processed notes
    # delivered on the main thread, no user action.
    r.comment('Processed notes delivered on the main thread', 'E6cde554f')
    # Eab8f789f onPostExecute@TRASH -> NoteProcessor.afterProcess: explicit
    # call, no user action; the coverage lookup detects the target
    # (NoteProcessor.java:59-67 calls afterProcess(notes)).
    r.comment('afterProcess(notes)', 'Eab8f789f')
    r.done()


if __name__ == '__main__':
    main()
