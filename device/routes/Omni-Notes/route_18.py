"""Device route script route_18 for Omni-Notes.

Method: DateUtils.prettyTime(Long,Locale)
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 E7e3c321b E01d0dfd6 Ee5d1ab81 E8a16cf02 E06a839c2
    Efe5c8631 E15401fce E639c8687 E5893d44c Ea9e0a788 Eeec72651
    E44b7f1a8 E0b50a073
Printed route: NOT in graphs/Omni-Notes/scratch/overnight-20261101/
    scratch-outputs/sample_30_routes.txt (checked: no prettyTime entry
    there; that file holds routes 19, 20, 21 of this batch). Edge
    triggers/gui below come from graphs/Omni-Notes/out/
    omni-notes_trigger_graph.json, and the source refs from ROUTES.csv:
    DetailFragment.java:638-654; DateHelper.java:112-118;
    DateUtils.java:186-191. Chain verified contiguous, S_ENTRY to the
    method, against the trigger graph.
Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    none.
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

Prettified-dates preference: the guard on E44b7f1a8 is "the
prettified-dates preference is on (default on; DateHelper.java:112-115)".
It is default on in res/xml/settings_interface.xml
(settings_prettified_dates, defaultValue true), and
DetailFragment.initViewFooter reads PREF_PRETTIFIED_DATES with default
true (DetailFragment.java:638-654). This script therefore does NOT
navigate to Settings and does NOT tap the toggle: a blind tap would
risk turning the default-on preference OFF, breaking the guard, and
no Settings step is part of this route's edge chain. The footer date
rendering on the newly opened note runs through the guard as printed.

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
            'Ef86ebfe1 E7e3c321b E01d0dfd6 Ee5d1ab81 E8a16cf02 E06a839c2 '
            'Efe5c8631 E15401fce E639c8687 E5893d44c Ea9e0a788 Eeec72651 '
            'E44b7f1a8 E0b50a073').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_18', EDGE_IDS, a.log,
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
    # E06a839c2 S_DETAIL@NEW -> DetailFragment.onTouch: the printed trigger is
    # an edge swipe on the editor (DetailFragment.java:1903-1953; guard: the
    # swipe starts within 30 px of the screen edge and moves 100 px,
    # SWIPE_MARGIN = 30, SWIPE_OFFSET = 100). LIMITATION, NOT AN ACTION:
    # the harness has no swipe primitive (tap is a single point, long_tap
    # swipes a point onto itself, scroll_to swipes vertically at x = 500),
    # so no harness call can perform this edge swipe, and none is faked
    # here. The target is still reached on a real run through the first
    # editor opened at E8a16cf02, whose onActivityCreated runs the same
    # init -> initViews -> initViewFooter -> getFormattedDate chain, so
    # coverage of prettyTime does not depend on this swipe succeeding.
    r.comment('HARNESS GAP: edge swipe (30 px margin, 100 px move) has no '
              'harness swipe primitive; first editor already runs the '
              'footer chain', 'E06a839c2')
    # Efe5c8631 DetailFragment.onTouch -> DetailFragment.<init>: an edge swipe
    # replaces the editor with a new DetailFragment; follows the swipe, no action.
    r.comment('Edge swipe replaces the editor with a new DetailFragment', 'Efe5c8631')
    # E15401fce DetailFragment.<init> -> DetailFragment.onActivityCreated:
    # lifecycle, no action.
    r.comment('Fragment lifecycle callback', 'E15401fce')
    # E639c8687 DetailFragment.onActivityCreated -> DetailFragment.init:
    # explicit call, no action.
    r.comment('init()', 'E639c8687')
    # E5893d44c DetailFragment.init -> DetailFragment.initViews: explicit call, no action.
    r.comment('initViews()', 'E5893d44c')
    # Ea9e0a788 DetailFragment.initViews -> DetailFragment.initViewFooter:
    # explicit call, no action.
    r.comment('initViewFooter()', 'Ea9e0a788')
    # Eeec72651 DetailFragment.initViewFooter -> DateHelper.getFormattedDate:
    # explicit call, no action.
    r.comment('getFormattedDate(creation/lastModification)', 'Eeec72651')
    # E44b7f1a8 DateHelper.getFormattedDate -> DateUtils.prettyTime(Long):
    # explicit call; guard: the prettified-dates preference is on (default on).
    r.comment('Prettified-dates preference on (default): prettyTime(Long)', 'E44b7f1a8')
    # E0b50a073 DateUtils.prettyTime(Long) -> DateUtils.prettyTime(Long,Locale):
    # interface dispatch, no user action; the coverage lookup detects the target.
    r.comment('Direct call dispatching to prettyTime(Long,Locale)', 'E0b50a073')
    r.done()


if __name__ == '__main__':
    main()
