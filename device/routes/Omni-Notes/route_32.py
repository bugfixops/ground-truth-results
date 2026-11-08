"""Device route script route_32 for Omni-Notes.

Method: DynamicNavigationLookupTable.<init>
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 Ec8760433 E77ad74f6 Ea72b76f0 E35dec0d3 E7fc93c0a E1004211f
    E7733bc48 E1a57b86a Ea6288be6 Ece232ca1 E9d7d1624
Printed route: route_print_DynamicNavigationLookupTable.txt (in this
    directory), constructed from the trigger graph
    (graphs/Omni-Notes/out/omni-notes_trigger_graph.json, edge ids in
    ROUTES.csv order, plus the shortest_path from out/methods.csv), NOT
    copied step by step from a sample print. Cross-check note: the same
    18 steps also appear as a LONG section in
    graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/sample_30_routes.txt
    (lines 1560-1619); see D3_32-33_REPORT.md. The constructed file above
    is the cited printed route for this script.
Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    none (ROUTES.csv route_32 permission column is empty)
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

One block per route edge, in route order. Lifecycle, page, explicit-call, and
framework edges with no user action get a comment, not an action. Every action
names an edge id of this route (the harness enforces it).

Why this script has no taps: every edge after the launch is an automatic
cold-start chain. ListFragment.init calls initNotesList (ListFragment.java:255),
which loads all notes; the load posts NotesLoadedEvent, the drawer fragment
rebuilds its menus, and MainMenuTask runs in the background. Opening the
navigation drawer is NOT on this route and does not cause MainMenuTask, so
no drawer tap is scripted. MainMenuTask.checkSkippableItem calls
DynamicNavigationLookupTable.getInstance() before its switch whenever the
dynamic-menu preference is on, and that preference defaults to true
(MainMenuTask.java:120-126), so the singleton constructor runs on the first
loop iteration over the navigation entries (res/values/arrays.xml:
Notes, Archive, Reminders, Trash, Uncategorized). No selector is used, so
no selector needs grounding in layout/menu/strings XML.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af '
            'Ef86ebfe1 Ec8760433 E77ad74f6 Ea72b76f0 E35dec0d3 E7fc93c0a '
            'E1004211f E7733bc48 E1a57b86a Ea6288be6 Ece232ca1 '
            'E9d7d1624').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_32', EDGE_IDS, a.log,
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
    # Ec8760433 ListFragment.init -> ListFragment.initNotesList: direct call, no action.
    r.comment('init() calls initNotesList(intent)', 'Ec8760433')
    # E77ad74f6 ListFragment.initNotesList -> NoteLoaderTask.doInBackground@ALL:
    # cold-start default branch loads all notes (getAllNotes), async, no action.
    r.comment('Default navigation: NoteLoaderTask loads all notes', 'E77ad74f6')
    # Ea72b76f0 NoteLoaderTask.doInBackground@ALL -> NoteLoaderTask.onPostExecute:
    # the list of notes is delivered on the main thread, no action.
    r.comment('The loaded notes are delivered on the main thread', 'Ea72b76f0')
    # E35dec0d3 NoteLoaderTask.onPostExecute -> NavigationDrawerFragment.onEvent(NotesLoadedEvent):
    # EventBus delivery to the drawer fragment, no user action.
    r.comment('NotesLoadedEvent reaches the drawer fragment via EventBus', 'E35dec0d3')
    # E7fc93c0a NavigationDrawerFragment.onEvent(NotesLoadedEvent) -> NavigationDrawerFragment.refreshMenus:
    # the drawer menus are rebuilt after a load, no action.
    r.comment('The drawer menus are rebuilt after the load', 'E7fc93c0a')
    # E1004211f NavigationDrawerFragment.refreshMenus -> NavigationDrawerFragment.buildMainMenu:
    # direct call, no action.
    r.comment('refreshMenus() calls buildMainMenu()', 'E1004211f')
    # E7733bc48 NavigationDrawerFragment.buildMainMenu -> MainMenuTask.doInBackground:
    # buildMainMenu executes a MainMenuTask on the thread-pool executor, no action.
    r.comment('A MainMenuTask is executed on the thread-pool executor', 'E7733bc48')
    # E1a57b86a MainMenuTask.doInBackground -> MainMenuTask.buildMainMenu:
    # direct call, no action.
    r.comment('doInBackground() calls buildMainMenu()', 'E1a57b86a')
    # Ea6288be6 MainMenuTask.buildMainMenu -> MainMenuTask.checkSkippableItem:
    # the menu builder loops the navigation entries and checks each one, no action.
    r.comment('buildMainMenu() loops the navigation entries, checking each', 'Ea6288be6')
    # Ece232ca1 MainMenuTask.checkSkippableItem -> DynamicNavigationLookupTable.getInstance:
    # dynamic menu defaults on, so getInstance() runs before the switch on the
    # first loop iteration; no drawer tap is needed or on this route.
    r.comment('Dynamic menu on (default): getInstance() before the switch', 'Ece232ca1')
    # E9d7d1624 DynamicNavigationLookupTable.getInstance -> DynamicNavigationLookupTable.<init>:
    # fresh process, so the singleton is null and the constructor runs;
    # the coverage lookup detects the target.
    r.comment('Fresh process: singleton null, constructor runs', 'E9d7d1624')
    r.done()


if __name__ == '__main__':
    main()
