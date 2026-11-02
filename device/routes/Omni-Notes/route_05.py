"""Device route script route_05 for Omni-Notes.

Method: DbHelper.deleteNote(long,boolean)
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 E7e3c321b E01d0dfd6 Ee5d1ab81 E8a16cf02 E1a48ab1f E4455444c
    Eca06fe26 E67ba23d6 E20a5c376 E2aba9b5f E5798db8e E152ff95a E90c55511
    Ef041169a Ebb3524e0 Eb7fd99d0 Ebcf6ab85
Printed route: graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/sample_30_routes.txt
    (DbHelper.deleteNote(long,boolean), 24 steps; path row result WRONG,
    confirmed_by SOURCE, ref DetailFragment.java:1583-1587,1612-1616; ListFragment.java:847-880)

ROUTE-TABLE VERDICT WRONG — READ FIRST: this script implements the best
route as printed (the FAB-created editor flow), NOT the real Merge path.
The Merge STATE ("the open note is the result of Merge, opened from the CAB
with two or more notes selected") cannot hold on a FAB-created editor, so
deleteMergedNotes does nothing on this flow and the expected device outcome
is reached=no with script_status=ok. The device run tests the route, not
the label, which stays REACHABLE via Merge.

Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    none listed for route_05 in ROUTES.csv.
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

One block per route edge, in route order. Lifecycle, page, explicit-call, and
framework edges with no user action get a comment, not an action. Every action
names an edge id of this route (the harness enforces it).
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af '
            'Ef86ebfe1 E7e3c321b E01d0dfd6 Ee5d1ab81 E8a16cf02 E1a48ab1f '
            'E4455444c Eca06fe26 E67ba23d6 E20a5c376 E2aba9b5f E5798db8e '
            'E152ff95a E90c55511 Ef041169a Ebb3524e0 Eb7fd99d0 '
            'Ebcf6ab85').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_05', EDGE_IDS, a.log,
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
    # E1a48ab1f S_DETAIL@NEW -> MainActivity.onBackPressed@DETAIL_SAVE: change
    # the note (tap the title field, res/layout/fragment_detail.xml id
    # detail_title, and type text), then press Back to save it.
    r.tap('E1a48ab1f', res_id='it.feio.android.omninotes:id/detail_title')
    r.type_text('route05 note', 'E1a48ab1f')
    r.back('E1a48ab1f')
    # E4455444c MainActivity.onBackPressed@DETAIL_SAVE -> DetailFragment.saveAndExit@SAVE:
    # goBack = true, saveAndExit(fragment), no action.
    r.comment('goBack = true: saveAndExit(fragment)', 'E4455444c')
    # Eca06fe26 DetailFragment.saveAndExit@SAVE -> DetailFragment.saveNote@SAVE:
    # saveNote(listener), no action.
    r.comment('saveNote(listener)', 'Eca06fe26')
    # E67ba23d6 DetailFragment.saveNote@SAVE -> SaveNoteTask.doInBackground:
    # async task executes, no action.
    r.comment('SaveNoteTask executes', 'E67ba23d6')
    # E20a5c376 SaveNoteTask.doInBackground -> SaveNoteTask.onPostExecute:
    # the saved note is delivered on the main thread, no action.
    r.comment('The saved note is delivered on the main thread', 'E20a5c376')
    # E2aba9b5f SaveNoteTask.onPostExecute -> DetailFragment.onNoteSaved:
    # interface dispatch, no action.
    r.comment('Virtual/interface call dispatching to this implementation', 'E2aba9b5f')
    # E5798db8e DetailFragment.onNoteSaved -> DetailFragment.deleteMergedNotes:
    # the merged source notes are deleted — but on this FAB-created editor
    # there are no merged notes, so this is a no-op (see the header: the
    # route-table verdict is WRONG and the expected outcome is reached=no).
    r.comment('deleteMergedNotes: no-op on a FAB editor (no Merge state)', 'E5798db8e')
    # E152ff95a DetailFragment.deleteMergedNotes -> NoteProcessor.process@DELETE:
    # new NoteProcessorDelete(notes).process(), no action.
    r.comment('new NoteProcessorDelete(notes).process()', 'E152ff95a')
    # E90c55511 NoteProcessor.process@DELETE -> NoteProcessor$NotesProcessorTask.doInBackground@DELETE:
    # task.executeOnExecutor(...), no action.
    r.comment('task.executeOnExecutor(...)', 'E90c55511')
    # Ef041169a NotesProcessorTask.doInBackground@DELETE -> NoteProcessorDelete.processNote:
    # processNote(note) for each note, no action.
    r.comment('processNote(note) for each note', 'Ef041169a')
    # Ebb3524e0 NoteProcessorDelete.processNote -> DbHelper.deleteNote(Note):
    # direct call, no action.
    r.comment('Direct call', 'Ebb3524e0')
    # Eb7fd99d0 DbHelper.deleteNote(Note) -> DbHelper.deleteNote(Note,boolean):
    # direct call, no action.
    r.comment('Direct call', 'Eb7fd99d0')
    # Ebcf6ab85 DbHelper.deleteNote(Note,boolean) -> DbHelper.deleteNote(long,boolean):
    # direct call; the coverage lookup detects the target if it is reached.
    # Expected on this flow: reached=no (see header).
    r.comment('Direct call; expected reached=no on this FAB flow', 'Ebcf6ab85')
    r.done()


if __name__ == '__main__':
    main()
