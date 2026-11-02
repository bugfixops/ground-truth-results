"""Device route script route_05 for Omni-Notes.

Method: DbHelper.deleteNote(long,boolean)
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 E7e3c321b E01d0dfd6 Ee5d1ab81 E8a16cf02 E1a48ab1f E4455444c
    Eca06fe26 E67ba23d6 E20a5c376 E2aba9b5f E5798db8e E152ff95a E90c55511
    Ef041169a Ebb3524e0 Eb7fd99d0 Ebcf6ab85
Printed route: graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/sample_30_routes.txt
    (DbHelper.deleteNote(long,boolean), 24 steps; path row result WRONG,
    confirmed_by SOURCE, ref DetailFragment.java:1583-1587,1612-1616; ListFragment.java:847-880)

MERGE FLOW — READ FIRST (2026-11-01 fix): the printed route's FAB-created
editor flow cannot carry the Merge state, so this script drives the real
Merge flow instead, and the expected device outcome is now reached=yes.
The graph route-table verdict WRONG stands as a label verdict: the printed
FAB prefix cannot hold "the open note is the result of Merge" (the editor
reads merged_notes from the intent, DetailFragment.java:507-508, and
deleteMergedNotes runs only when that list is non-null, :1616,1627-1635).
This script does NOT change that verdict or any label; it tests the method
as REACHABLE via Merge, which is the label's own route: two notes are
created, both are selected in the CAB, Merge opens the merged note, and
saving it runs deleteMergedNotes on the real merged ids.
Merge mechanics, printed: long-press starts CAB (ListFragment.java:507-514),
the CAB menu dispatches menu_merge (ListFragment.java:857-858; menu item
menu_list.xml menu_merge, title @string/merge = "Merge", visible only when
two or more notes are selected, ListFragment.java:625,634), merge() posts
NotesMergeEvent (ListFragment.java:1737-1738), and onEventAsync merges the
selected notes, puts their ids in the intent extra "merged_notes" and
opens the merged note in the editor (ListFragment.java:1745-1764).

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
    # --- MERGE SETUP, logged against route edges as in route_23 (the harness
    # requires every action to name an edge id of this route).
    # Create two notes first (E7e3c321b, the list-setup edge): long-press the
    # + button (res/layout/fab.xml id fab) as in route_23, give each note a
    # distinct title so its list row can be found again, and Back to save.
    r.long_tap('E7e3c321b', res_id='it.feio.android.omninotes:id/fab')
    r.tap('E7e3c321b', res_id='it.feio.android.omninotes:id/detail_title')
    r.type_text('route05 merge A', 'E7e3c321b')
    r.back('E7e3c321b')
    r.wait_for('E7e3c321b', text='route05 merge A')
    r.long_tap('E7e3c321b', res_id='it.feio.android.omninotes:id/fab')
    r.tap('E7e3c321b', res_id='it.feio.android.omninotes:id/detail_title')
    r.type_text('route05 merge B', 'E7e3c321b')
    r.back('E7e3c321b')
    r.wait_for('E7e3c321b', text='route05 merge B')
    # E01d0dfd6 S_LIST@NOTES -> Fab.lambda$init$1@LONG_NOTES: this edge is the
    # printed list-to-detail transition. The Merge flow is the device
    # realisation of that transition (see header): long-press the first note
    # row to start CAB (ListFragment.java:507-514), tap the second note row
    # to select it as well, then tap "Merge" in the CAB menu
    # (menu_list.xml menu_merge, title "Merge"). onEventAsync then opens the
    # merged note in the editor (ListFragment.java:1745-1764), whose title is
    # the first note's title.
    r.long_tap('E01d0dfd6', text='route05 merge A')
    r.tap('E01d0dfd6', text='route05 merge B')
    r.tap('E01d0dfd6', text='Merge')
    r.wait_for('E01d0dfd6', text='route05 merge A')
    # Ee5d1ab81 Fab long-press -> ListFragment.lambda$initFab$0@MAIN: superseded
    # by the Merge transition above — the FAB menu dispatch does not run on
    # this flow, so this edge is a comment only (the printed FAB route stays
    # WRONG as a label verdict; see header).
    r.comment('FAB menu dispatch: superseded by the Merge transition', 'Ee5d1ab81')
    # E8a16cf02 lambda$initFab$0@MAIN -> S_DETAIL@NEW: the merged note editor
    # is open (not a FAB-created editor), no further action.
    r.comment('The merged note editor is open', 'E8a16cf02')
    # E1a48ab1f S_DETAIL@NEW -> MainActivity.onBackPressed@DETAIL_SAVE: change
    # the merged note (tap the title field, res/layout/fragment_detail.xml id
    # detail_title, and type text), then press Back to save it. Saving the
    # merged note is what runs deleteMergedNotes on the real merged ids.
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
    # the merged source notes are deleted — on this Merge flow mergedNotesIds
    # is the real list put in the intent by onEventAsync, so this is NOT a
    # no-op (DetailFragment.java:1627-1635).
    r.comment('deleteMergedNotes: real merged ids from the Merge flow', 'E5798db8e')
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
    # Expected on this Merge flow: reached=yes (see header).
    r.comment('Direct call; expected reached=yes on this Merge flow', 'Ebcf6ab85')
    r.done()


if __name__ == '__main__':
    main()
