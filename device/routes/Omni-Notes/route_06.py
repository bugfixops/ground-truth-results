"""Device route script route_06 for Omni-Notes.

Method: Attachment.<init>(BaseAttachment)
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 E7e3c321b E89ba0d21 Eb4f41bd1 Eb5b36c1c E15489aeb E4306cbbb
    E7d8539a9 E1f9e6935 E51dad05c E47f06889 Ed1a1b5fa Eb3d3e1bc Eaa4dc4e5
    E6f7ab928 E357d731e E19da0381 E1f7207ea E867516ae E6dbf71eb Ecd757080
    Eae8e194c E55ee284f E4f0497a0 Ed4308bfb
Printed route: graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/sample_30_routes.txt
    (Attachment.<init>(BaseAttachment), 31 steps; path row result fixed,
    confirmed_by SOURCE, ref DataBackupIntentService.java:75-87,121-137;
    BackupHelper.java:145-176; Note.java:152-159)
Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    android.permission.READ_EXTERNAL_STORAGE, android.permission.WRITE_EXTERNAL_STORAGE
Fixtures: Pictures/photo_1.jpg (the attachment picked for the note created
    in the pre-route setup below; ROUTES.csv already lists it). Setup
    (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

One block per route edge, in route order. Lifecycle, page, explicit-call, and
framework edges with no user action get a comment, not an action. Every action
names an edge id of this route (the harness enforces it).

Pre-route setup (2026-11-01 fix): the final edge fires only if the imported
note JSON has an attachments array (Note.java:152-159, buildFromJson loops
getAttachmentsList into Attachment.<init>). A fresh-database export contains
no attachment-bearing note, so the script FIRST creates a note with an
attachment (the route_08 attachment sequence: FAB note, Attachment > Files >
photo_1.jpg, Back saves it), THEN exports it, so the backup named
route06backup contains an attachment-bearing note and its JSON has the
attachments array. The export also creates the backup folder under
/sdcard/Omni Notes that the import dialog needs. Setup actions are logged
against route edges as in route_23 (E7e3c321b for the note creation on the
list screen, Eaa4dc4e5 for the export that the import-dialog edge's guard
requires).

Selector notes as in route_02: drawer toggle content-desc "Open navigation
drawer", drawer Settings res id settings, the "Sync" screen rendered as
"Sync and Backups", and the "Import" preference rendered as
"Restore or delete backups" (strings.xml settings_import).
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
            'Eb3d3e1bc Eaa4dc4e5 E6f7ab928 E357d731e E19da0381 E1f7207ea '
            'E867516ae E6dbf71eb Ecd757080 Eae8e194c E55ee284f E4f0497a0 '
            'Ed4308bfb').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_06', EDGE_IDS, a.log,
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
    # --- Pre-route setup (see header): create a note with an attachment
    # first, so the export below contains an attachment-bearing note.
    # Long-press the + button (res/layout/fab.xml id fab), tap the title
    # field (res/layout/fragment_detail.xml id detail_title) and the content
    # field (res/layout/fragment_detail_content.xml id detail_content), type,
    # tap "Attachment" in the toolbar menu (menu_detail.xml), tap "Files" in
    # the attachment popup (res/layout/attachment_dialog.xml id files), pick
    # photo_1.jpg in the system picker (Pictures fixture), then Back saves
    # the note and returns to the list. AttachmentTask copies the picked file
    # into the app's private attachment directory, so the saved note has a
    # real attachment (StorageHelper.createAttachmentFromUri).
    r.long_tap('E7e3c321b', res_id='it.feio.android.omninotes:id/fab')
    r.tap('E7e3c321b', res_id='it.feio.android.omninotes:id/detail_title')
    r.type_text('Route06 attachment note', 'E7e3c321b')
    r.tap('E7e3c321b', res_id='it.feio.android.omninotes:id/detail_content')
    r.type_text('Route06 note with attachment', 'E7e3c321b')
    r.tap('E7e3c321b', text='Attachment')
    r.tap('E7e3c321b', text='Files')
    r.tap('E7e3c321b', text='photo_1.jpg')
    r.back('E7e3c321b')
    r.wait_for('E7e3c321b', text='Route06 attachment note')
    # Then export that note (logged against Eaa4dc4e5, SettingsFragment.importNotes
    # -> S_DLG_IMPORT, whose guard is "a backup folder exists under
    # /sdcard/Omni Notes (Settings > Sync > Export)"): Settings > Data > Sync
    # and Backups > "Backup" (settings_export) opens the export dialog
    # (res/layout/dialog_backup_layout.xml); type a fixed backup name,
    # route06backup, into the export name field (res id export_file_name) and
    # tap "Confirm", so the backup created has a known name for the import
    # list below. Then back out to the list and run the printed import route.
    r.tap('Eaa4dc4e5', desc='Open navigation drawer')
    r.tap('Eaa4dc4e5', res_id='it.feio.android.omninotes:id/settings')
    r.tap('Eaa4dc4e5', text='Data')
    r.tap('Eaa4dc4e5', text='Sync and Backups')
    r.tap('Eaa4dc4e5', text='Backup')
    r.tap('Eaa4dc4e5', res_id='it.feio.android.omninotes:id/export_file_name')
    r.type_text('route06backup', 'Eaa4dc4e5')
    r.tap('Eaa4dc4e5', text='Confirm')
    # Back out to the notes list (audit fix 2026-11-01): SettingsActivity's
    # onCreate replaces the root fragment with NO back-stack entry, while each
    # preference tap (Data, then Sync) goes through onPreferenceStartFragment
    # with addToBackStack (SettingsActivity.java:125-139), so two fragment
    # entries sit on the stack and the custom backStack list is never
    # populated, so onBackPressed falls through to super and pops one entry
    # per press (SettingsActivity.java:78-82). Two backs land on the settings
    # root with SettingsActivity still foreground; a third back finishes
    # SettingsActivity and returns to the MainActivity list, which the main
    # route's drawer tap below requires.
    r.back('Eaa4dc4e5')
    r.back('Eaa4dc4e5')
    r.back('Eaa4dc4e5')
    r.wait_for('Eaa4dc4e5', text='Route06 attachment note')
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
    # Ed1a1b5fa S_SETTINGS_SYNC -> SettingsFragment.lambda$onResume$2:
    # tap "Restore or delete backups" (settings_sync_import_export.xml, settings_import).
    r.tap('Ed1a1b5fa', text='Restore or delete backups')
    # Eb3d3e1bc lambda$onResume$2 -> SettingsFragment.importNotes:
    # WRITE_EXTERNAL_STORAGE is granted, importNotes() runs, no action.
    r.comment('WRITE_EXTERNAL_STORAGE granted: importNotes()', 'Eb3d3e1bc')
    # Eaa4dc4e5 SettingsFragment.importNotes -> S_DLG_IMPORT: the backup list
    # opens; the pre-route export created the route06backup folder.
    r.comment('The backup list opens (route06backup, created by the export above)', 'Eaa4dc4e5')
    # E6f7ab928 S_DLG_IMPORT -> RecyclerViewItemClickSupport$1.onClick@IMPORT:
    # tap the backup created by the pre-route export.
    r.tap('E6f7ab928', text='route06backup')
    # E357d731e onClick@IMPORT -> SettingsFragment.lambda$null$28:
    # OnItemClickListener.onItemClick, no action.
    r.comment('OnItemClickListener.onItemClick', 'E357d731e')
    # E19da0381 lambda$null$28 -> S_DLG_IMPORT_CONFIRM: the restore
    # confirmation opens, no action.
    r.comment('The restore confirmation opens', 'E19da0381')
    # E1f7207ea S_DLG_IMPORT_CONFIRM -> SettingsFragment.lambda$null$27:
    # tap "Confirm" (strings.xml confirm).
    r.tap('E1f7207ea', text='Confirm')
    # E867516ae lambda$null$27 -> DataBackupIntentService.onHandleIntent@IMPORT:
    # IntentService worker thread, no action.
    r.comment('IntentService.onHandleIntent runs on a worker thread', 'E867516ae')
    # E6dbf71eb onHandleIntent@IMPORT -> DataBackupIntentService.importData@IMPORT:
    # the import action branch, no action.
    r.comment('The import action branch', 'E6dbf71eb')
    # Ecd757080 DataBackupIntentService.importData@IMPORT -> BackupHelper.importNotes:
    # the notes of the backup folder are imported (normal import, not legacy).
    r.comment('The notes of the backup folder are imported', 'Ecd757080')
    # Eae8e194c BackupHelper.importNotes -> BackupHelper.importNote: direct call;
    # guard: the backup folder holds a note file named <13 digits>.json.
    r.comment('Direct call (backup holds a <13 digits>.json note file)', 'Eae8e194c')
    # E55ee284f BackupHelper.importNote -> BackupHelper.getImportNote: direct call, no action.
    r.comment('Direct call', 'E55ee284f')
    # E4f0497a0 BackupHelper.getImportNote -> Note.buildFromJson: direct call;
    # guard: the note file is not empty.
    r.comment('Direct call (note file is not empty)', 'E4f0497a0')
    # Ed4308bfb Note.buildFromJson -> Attachment.<init>(BaseAttachment): direct
    # call; guard: the note JSON has an attachments array — satisfied by the
    # pre-route setup, which exported an attachment-bearing note (see header).
    # The coverage lookup detects the target; expected reached=yes.
    r.comment('Direct call; guard satisfied by the exported attachment note', 'Ed4308bfb')
    r.done()


if __name__ == '__main__':
    main()
