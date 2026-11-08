"""Device route script route_02 for Omni-Notes.

Method: SpringImportHelper.lambda$importDataFromSpringpad$0
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 E7e3c321b E89ba0d21 Eb4f41bd1 Eb5b36c1c E15489aeb E4306cbbb
    E7d8539a9 E1f9e6935 E51dad05c E47f06889 E4fa5a179 Edb933e2f E821c0225
    E4458616b E9552e9d0 E87530cf4 Ee549a73a
Printed route: graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/sample_30_routes.txt
    (SpringImportHelper.lambda$importDataFromSpringpad$0, 24 steps; path row result fixed,
    confirmed_by SOURCE, ref SettingsFragment.java:240-255,683-691; DataBackupIntentService.java:75-87)
Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    none listed for route_02 in ROUTES.csv.
Fixtures: Download/archive.zip (pushed by run_app.sh to /sdcard/Download/archive.zip;
    no push_fixture call in this script). Setup (ROUTES.csv): push fixtures/Pictures
    (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

One block per route edge, in route order. Lifecycle, page, explicit-call, and
framework edges with no user action get a comment, not an action. Every action
names an edge id of this route (the harness enforces it).

Selector notes: the drawer toggle uses content-desc "Open navigation drawer"
(strings.xml navigation_drawer_open); the drawer Settings row uses res id
settings (res/layout/drawer_category_list_footer.xml); the "Sync" screen title
is rendered as "Sync and Backups" (strings.xml settings_screen_sync_import_export),
so that text is tapped, not the trigger-graph shorthand "Sync".
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af '
            'Ef86ebfe1 E7e3c321b E89ba0d21 Eb4f41bd1 Eb5b36c1c E15489aeb '
            'E4306cbbb E7d8539a9 E1f9e6935 E51dad05c E47f06889 E4fa5a179 '
            'Edb933e2f E821c0225 E4458616b E9552e9d0 E87530cf4 '
            'Ee549a73a').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_02', EDGE_IDS, a.log,
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
    # tap the drawer toggle (content-desc "Open navigation drawer").
    r.tap('E89ba0d21', desc='Open navigation drawer')
    # Eb4f41bd1 onDrawerOpened -> S_DRAWER@NOTES: drawer is open, no action.
    r.comment('The drawer is open', 'Eb4f41bd1')
    # Eb5b36c1c S_DRAWER@NOTES -> CategoryMenuTask.lambda$null$0: tap Settings
    # at the bottom of the drawer (footer res id settings).
    r.tap('Eb5b36c1c', res_id='it.feio.android.omninotes:id/settings')
    # E15489aeb lambda$null$0 -> SettingsActivity.<init>: intent, no action.
    r.comment('startActivity(SettingsActivity)', 'E15489aeb')
    # E4306cbbb SettingsActivity.<init> -> S_SETTINGS: settings root shown, no action.
    r.comment('The settings root is shown', 'E4306cbbb')
    # E7d8539a9 S_SETTINGS -> SettingsActivity.onPreferenceStartFragment@DATA:
    # tap "Data" (settings.xml, settings_screen_data).
    r.tap('E7d8539a9', text='Data')
    # E1f9e6935 onPreferenceStartFragment@DATA -> S_SETTINGS_DATA: sub-screen opens, no action.
    r.comment('The Data sub-screen opens', 'E1f9e6935')
    # E51dad05c S_SETTINGS_DATA -> SettingsActivity.onPreferenceStartFragment@SYNC:
    # tap "Sync and Backups" (settings_data.xml, settings_screen_sync_import_export).
    r.tap('E51dad05c', text='Sync and Backups')
    # E47f06889 onPreferenceStartFragment@SYNC -> S_SETTINGS_SYNC: sub-screen opens, no action.
    r.comment('The Sync sub-screen opens', 'E47f06889')
    # E4fa5a179 S_SETTINGS_SYNC -> SettingsFragment.lambda$onResume$5:
    # tap "Import notes from Springpad" (settings_sync_import_export.xml).
    r.tap('E4fa5a179', text='Import notes from Springpad')
    # Edb933e2f lambda$onResume$5 -> S_EXT_PICKER@SPRINGPAD: the system picker
    # opens (ACTION_GET_CONTENT, application/zip), no action.
    r.comment('The system picker opens for a zip', 'Edb933e2f')
    # E821c0225 S_EXT_PICKER@SPRINGPAD -> SettingsFragment.onActivityResult@SPRINGPAD:
    # pick the fixture zip pushed by run_app.sh, by tapping its name.
    r.tap('E821c0225', text='archive.zip')
    # E4458616b onActivityResult@SPRINGPAD -> DataBackupIntentService.onHandleIntent@SPRINGPAD:
    # IntentService worker thread, no action.
    r.comment('IntentService.onHandleIntent runs on a worker thread', 'E4458616b')
    # E9552e9d0 onHandleIntent@SPRINGPAD -> DataBackupIntentService.importDataFromSpringpad:
    # the springpad action branch, no action.
    r.comment('The springpad action branch', 'E9552e9d0')
    # E87530cf4 importDataFromSpringpad -> SpringImportHelper.importDataFromSpringpad:
    # direct call, no action.
    r.comment('Direct call', 'E87530cf4')
    # Ee549a73a importDataFromSpringpad -> SpringImportHelper.lambda$importDataFromSpringpad$0:
    # framework/library runs the lambda; the coverage lookup detects the target.
    r.comment('The library / Handler runs the lambda', 'Ee549a73a')
    r.done()


if __name__ == '__main__':
    main()
