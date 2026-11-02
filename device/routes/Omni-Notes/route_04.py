"""Device route script route_04 for Omni-Notes.

Method: DetailFragment.onLocationUnavailable
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 E7e3c321b E01d0dfd6 Ee5d1ab81 E8a16cf02 E06a839c2 Efe5c8631
    E15401fce E639c8687 E5893d44c Ecf43ebf8 E8050f4c2 E6c823805 E303c2c53
    E835daba1 E7a04967d
Printed route: graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/sample_30_routes.txt
    (DetailFragment.onLocationUnavailable, 22 steps; path row result fixed,
    confirmed_by SOURCE, ref DetailFragment.java:699-702,733-736; GeocodeHelper.java:91,104-107)
Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    android.permission.ACCESS_FINE_LOCATION, android.permission.ACCESS_COARSE_LOCATION
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

One block per route edge, in route order. Lifecycle, page, explicit-call, and
framework edges with no user action get a comment, not an action. Every action
names an edge id of this route (the harness enforces it).

Pre-route setup (logged against E8050f4c2, the edge whose guard requires it):
the "Automatic location" preference is off by default (settings_behaviors.xml,
settings_auto_location, defaultValue false), so before the route's note flow
the script opens Settings > Behaviors and taps "Automatic location" to turn
it on, then backs out to the list. No location setup is done: the 2 s timeout
with no fix is the default emulator state, and that timeout is what reaches
onLocationUnavailable.

Approximation, flagged: the printed E06a839c2 trigger is an edge swipe (starts
within 30 px of the screen edge, moves 100 px; DetailFragment.java:1916-1944),
but the harness has no swipe primitive, so the script taps the editor content
(res id detail_content) as the "touch the editor" action. The FAB-created
editor itself also runs initViews -> initViewLocation, so the auto-location
path is exercised even if the swipe rebuild is not literally reproduced.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af '
            'Ef86ebfe1 E7e3c321b E01d0dfd6 Ee5d1ab81 E8a16cf02 E06a839c2 '
            'Efe5c8631 E15401fce E639c8687 E5893d44c Ecf43ebf8 E8050f4c2 '
            'E6c823805 E303c2c53 E835daba1 E7a04967d').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_04', EDGE_IDS, a.log,
               dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    # Ea7466154 S_ENTRY -> MainActivity.<init>: launcher starts MainActivity.
    r.launch('it.feio.android.omninotes/.MainActivity', 'Ea7466154')
    # Pre-route setup, logged against E8050f4c2 (initViewLocation ->
    # getLocation@AUTO), whose guard is "Settings > Behaviors > Auto location
    # is on (default off)": open Settings > Behaviors, turn Automatic
    # location on, then back out to the notes list.
    r.tap('E8050f4c2', desc='Open navigation drawer')
    r.tap('E8050f4c2', res_id='it.feio.android.omninotes:id/settings')
    r.tap('E8050f4c2', text='Behaviors')
    r.tap('E8050f4c2', text='Automatic location')
    r.back('E8050f4c2')
    r.back('E8050f4c2')
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
    # E06a839c2 S_DETAIL@NEW -> DetailFragment.onTouch: touch the editor
    # (printed trigger is an edge swipe; see the header approximation note).
    r.tap('E06a839c2', res_id='it.feio.android.omninotes:id/detail_content')
    # Efe5c8631 DetailFragment.onTouch -> DetailFragment.<init>: an edge swipe
    # replaces the editor with a new DetailFragment, no further action.
    r.comment('An edge swipe replaces the editor with a new DetailFragment', 'Efe5c8631')
    # E15401fce DetailFragment.<init> -> DetailFragment.onActivityCreated: lifecycle, no action.
    r.comment('Fragment lifecycle callback', 'E15401fce')
    # E639c8687 DetailFragment.onActivityCreated -> DetailFragment.init: direct call, no action.
    r.comment('Direct call to init()', 'E639c8687')
    # E5893d44c DetailFragment.init -> DetailFragment.initViews: direct call, no action.
    r.comment('Direct call to initViews()', 'E5893d44c')
    # Ecf43ebf8 DetailFragment.initViews -> DetailFragment.initViewLocation: direct call, no action.
    r.comment('Direct call to initViewLocation()', 'Ecf43ebf8')
    # E8050f4c2 DetailFragment.initViewLocation -> DetailFragment.getLocation@AUTO:
    # a new note gets the current location; auto location was turned on above.
    r.comment('Auto location is on: getLocation(this)', 'E8050f4c2')
    # E6c823805 DetailFragment.getLocation@AUTO -> DetailFragment.lambda$getLocation$7@AUTO:
    # ACCESS_FINE_LOCATION is granted, the callback runs, no action.
    r.comment('ACCESS_FINE_LOCATION granted: the callback runs', 'E6c823805')
    # E303c2c53 lambda$getLocation$7@AUTO -> GeocodeHelper.getLocation@AUTO:
    # explicit call, no action.
    r.comment('GeocodeHelper.getLocation(listener)', 'E303c2c53')
    # E835daba1 GeocodeHelper.getLocation@AUTO -> GeocodeHelper$1.onError@AUTO:
    # no fix within 2 s, the observable times out, no action.
    r.comment('No fix within 2 s: the observable times out', 'E835daba1')
    # E7a04967d GeocodeHelper$1.onError@AUTO -> DetailFragment.onLocationUnavailable:
    # listener.onLocationUnavailable(); wait for its visible message
    # ("Location not found", strings.xml location_not_found) so the 2 s
    # timeout has time to fire before the script ends.
    r.wait_for('E7a04967d', text='Location not found', timeout=30)
    r.done()


if __name__ == '__main__':
    main()
