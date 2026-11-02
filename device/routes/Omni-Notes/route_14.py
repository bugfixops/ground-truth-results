"""Device route script route_14 for Omni-Notes.

Method: DataBackupIntentService.deleteData
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 E7e3c321b E89ba0d21 Eb4f41bd1 Eb5b36c1c E15489aeb E4306cbbb
    E7d8539a9 E1f9e6935 E51dad05c E47f06889 Ed1a1b5fa Eb3d3e1bc Eaa4dc4e5
    E580104d9 Eef2ea939 E7e0a24a4 Ee925a6f2 Ef289bf9e Ef4fbd583
Printed route: graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/sample_30_routes.txt
    (DataBackupIntentService.deleteData, 26 steps; path row result fixed,
    confirmed_by SOURCE, ref SettingsFragment.java:159-166,595-615;
    DataBackupIntentService.java:75-83)
Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    android.permission.READ_EXTERNAL_STORAGE, android.permission.WRITE_EXTERNAL_STORAGE
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

One block per route edge, in route order. Lifecycle, page, explicit-call, and
framework edges with no user action get a comment, not an action. Every action
names an edge id of this route (the harness enforces it).

Setup note (export first): no fixture creates the backup folder, so the
script creates it through the app on the Sync screen, before the route's
Import step. The export taps are logged under E47f06889 (arrival on the
S_SETTINGS_SYNC screen, where they happen); they are NOT a route edge of the
delete flow, and the delete flow itself then uses its own edges in order.
The export names the backup "route14backup" (typed into the export dialog's
export_file_name field, res/layout/dialog_backup_layout.xml) so the backup
listed in the import dialog has a known, tappable/long-pressable name
instead of the default timestamp name.

Selectors: "Data" (settings_screen_data), "Sync and Backups"
(settings_screen_sync_import_export), "Backup" (settings_export),
"Restore or delete backups" (settings_import), "Confirm" (confirm) all from
res/values/strings.xml and res/xml/settings*.xml; the drawer Settings row
from res/layout/drawer_category_list_footer.xml (id settings).
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af '
            'Ef86ebfe1 E7e3c321b E89ba0d21 Eb4f41bd1 Eb5b36c1c E15489aeb '
            'E4306cbbb E7d8539a9 E1f9e6935 E51dad05c E47f06889 Ed1a1b5fa '
            'Eb3d3e1bc Eaa4dc4e5 E580104d9 Eef2ea939 E7e0a24a4 Ee925a6f2 '
            'Ef289bf9e Ef4fbd583').split()

BACKUP_NAME = 'route14backup'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_14', EDGE_IDS, a.log,
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
    # tap the drawer (hamburger) icon. UNCERTAIN: the toolbar layout carries
    # no navigation icon of its own; ActionBarDrawerToggle (constructed with
    # R.string.drawer_open, "drawer open") sets the toolbar navigation
    # content description, so "drawer open" is the best-grounded selector,
    # but the live dump must be checked on the first real run.
    r.tap('E89ba0d21', desc='drawer open')
    # Eb4f41bd1 onDrawerOpened -> S_DRAWER@NOTES: drawer open, no action.
    r.comment('The drawer is open', 'Eb4f41bd1')
    # Eb5b36c1c S_DRAWER@NOTES -> CategoryMenuTask.lambda$null$0: tap the
    # Settings row in the drawer footer (id settings).
    r.tap('Eb5b36c1c', res_id='it.feio.android.omninotes:id/settings')
    # E15489aeb lambda$null$0 -> SettingsActivity.<init>: intent, no action.
    r.comment('startActivity(SettingsActivity)', 'E15489aeb')
    # E4306cbbb SettingsActivity.<init> -> S_SETTINGS: settings root shown, no action.
    r.comment('The settings root is shown', 'E4306cbbb')
    # E7d8539a9 S_SETTINGS -> SettingsActivity.onPreferenceStartFragment@DATA:
    # tap "Data" (settings_screen_data).
    r.tap('E7d8539a9', text='Data')
    # E1f9e6935 onPreferenceStartFragment@DATA -> S_SETTINGS_DATA: sub-screen, no action.
    r.comment('The Data sub-screen opens on top of the root', 'E1f9e6935')
    # E51dad05c S_SETTINGS_DATA -> SettingsActivity.onPreferenceStartFragment@SYNC:
    # tap "Sync and Backups" (settings_screen_sync_import_export).
    r.tap('E51dad05c', text='Sync and Backups')
    # E47f06889 onPreferenceStartFragment@SYNC -> S_SETTINGS_SYNC: sub-screen, no action.
    r.comment('The Sync sub-screen opens', 'E47f06889')
    # --- Setup on the Sync screen (logged under E47f06889, see header) ---
    # Export first so a backup folder exists: tap "Backup"
    # (settings_export), type the fixed backup name, tap "Confirm".
    # UNCERTAIN (race): the backup service runs asynchronously after
    # Confirm; the harness has no sleep step, so the Import tap below
    # follows immediately. On a slow device the import list may still be
    # empty at that moment.
    r.tap('E47f06889', text='Backup')
    r.tap('E47f06889', res_id='it.feio.android.omninotes:id/export_file_name')
    r.type_text(BACKUP_NAME, 'E47f06889')
    r.tap('E47f06889', text='Confirm')
    # Ed1a1b5fa S_SETTINGS_SYNC -> SettingsFragment.lambda$onResume$2:
    # tap "Restore or delete backups" (settings_import).
    r.tap('Ed1a1b5fa', text='Restore or delete backups')
    # Eb3d3e1bc lambda$onResume$2 -> SettingsFragment.importNotes: storage
    # granted (run_app.sh), importNotes() runs, no action.
    r.comment('WRITE_EXTERNAL_STORAGE granted: importNotes()', 'Eb3d3e1bc')
    # Eaa4dc4e5 SettingsFragment.importNotes -> S_DLG_IMPORT: the backup list
    # opens, no action; then wait until our exported backup is listed.
    r.comment('The backup list opens', 'Eaa4dc4e5')
    r.wait_for('Eaa4dc4e5', text=BACKUP_NAME, timeout=60)
    # E580104d9 S_DLG_IMPORT -> RecyclerViewItemClickSupport$2.onLongClick@IMPORT:
    # long-press the backup we just exported.
    r.long_tap('E580104d9', text=BACKUP_NAME)
    # Eef2ea939 onLongClick@IMPORT -> SettingsFragment.lambda$null$30:
    # OnItemLongClickListener dispatch, no action.
    r.comment('OnItemLongClickListener.onItemLongClick', 'Eef2ea939')
    # E7e0a24a4 lambda$null$30 -> S_DLG_BACKUP_DELETE: the delete
    # confirmation opens, no action.
    r.comment('The delete confirmation opens', 'E7e0a24a4')
    # Ee925a6f2 S_DLG_BACKUP_DELETE -> SettingsFragment.lambda$null$29:
    # tap "Confirm" (confirm) in the delete dialog.
    r.tap('Ee925a6f2', text='Confirm')
    # Ef289bf9e lambda$null$29 -> DataBackupIntentService.onHandleIntent@DELETE:
    # IntentService worker thread, no action.
    r.comment('IntentService.onHandleIntent runs on a worker thread', 'Ef289bf9e')
    # Ef4fbd583 onHandleIntent@DELETE -> DataBackupIntentService.deleteData:
    # the delete action; the coverage lookup detects the target.
    r.comment('The delete action dispatches to deleteData', 'Ef4fbd583')
    r.done()


if __name__ == '__main__':
    main()
