"""Device route script route_22 for Omni-Notes.

Method: Stats.getCharsMax
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 E7e3c321b E89ba0d21 Eb4f41bd1 Eb5b36c1c E15489aeb E4306cbbb
    E4bc4bf24 E25517ff9 E83a5fe0d E4e2638a1 E95a0513f E01e2f52a E1787b7c4
    E52a5aa28
Printed route: graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/sample_30_routes.txt
    does NOT contain this method (only 30 of 33 routes are printed there);
    edge list and trigger/gui text below come from ROUTES.csv and
    graphs/Omni-Notes/out/omni-notes_trigger_graph.json instead
    (StatsActivity.java:35-84; settings.xml:111-117).
Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    none (ROUTES.csv route_22 permission column is empty).
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
            'Ef86ebfe1 E7e3c321b E89ba0d21 Eb4f41bd1 Eb5b36c1c E15489aeb '
            'E4306cbbb E4bc4bf24 E25517ff9 E83a5fe0d E4e2638a1 E95a0513f '
            'E01e2f52a E1787b7c4 E52a5aa28').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_22', EDGE_IDS, a.log,
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
    # tap the toolbar navigation (hamburger) icon. UNCERTAINTY: no id or text
    # for this icon exists in res/layout; the ActionBarDrawerToggle created in
    # NavigationDrawerFragment.java sets its content description from
    # R.string.drawer_open ("drawer open", res/values/strings.xml:414).
    r.tap('E89ba0d21', desc='drawer open')
    # Eb4f41bd1 onDrawerOpened@NOTES -> S_DRAWER@NOTES: drawer is open, no action.
    r.comment('The navigation drawer is open', 'Eb4f41bd1')
    # Eb5b36c1c S_DRAWER@NOTES -> CategoryMenuTask.lambda$null$0: tap "Settings"
    # in the drawer footer (res/layout/drawer_category_list_footer.xml,
    # TextView id settings, text @string/settings = "Settings").
    r.tap('Eb5b36c1c', res_id='it.feio.android.omninotes:id/settings')
    # E15489aeb lambda$null$0 -> SettingsActivity.<init>: intent, no action.
    r.comment('startActivity(SettingsActivity)', 'E15489aeb')
    # E4306cbbb SettingsActivity.<init> -> S_SETTINGS: settings root shown, no action.
    r.comment('The settings root is shown', 'E4306cbbb')
    # E4bc4bf24 S_SETTINGS -> StatsActivity.<init>: tap "Statistics"
    # (res/xml/settings.xml:111-117, Preference title
    # @string/settings_statistics = "Statistics", intent to StatsActivity).
    r.tap('E4bc4bf24', text='Statistics')
    # E25517ff9 StatsActivity.<init> -> StatsActivity.onCreate: lifecycle, no action.
    r.comment('Activity lifecycle callback', 'E25517ff9')
    # E83a5fe0d StatsActivity.onCreate -> StatsActivity.initData: explicit call, no action.
    r.comment('initData()', 'E83a5fe0d')
    # E4e2638a1 StatsActivity.initData -> StatsActivity$1StatsTask.<init>:
    # explicit call, no action.
    r.comment('new StatsTask()', 'E4e2638a1')
    # E95a0513f StatsTask.<init> -> StatsTask.doInBackground: AsyncTask
    # executeOnExecutor, no user action.
    r.comment('StatsTask executes on the thread pool', 'E95a0513f')
    # E01e2f52a StatsTask.doInBackground -> StatsTask.onPostExecute: statistics
    # delivered on the main thread, no user action.
    r.comment('Statistics delivered on the main thread', 'E01e2f52a')
    # E1787b7c4 StatsTask.onPostExecute -> StatsActivity.populateViews:
    # explicit call, no user action.
    r.comment('populateViews(result)', 'E1787b7c4')
    # E52a5aa28 StatsActivity.populateViews -> Stats.getCharsMax: explicit call,
    # no user action; the coverage lookup detects the target
    # (StatsActivity.java:84 sets stat_chars_max from getCharsMax()).
    r.comment('populateViews reads getCharsMax() for stat_chars_max', 'E52a5aa28')
    r.done()


if __name__ == '__main__':
    main()
