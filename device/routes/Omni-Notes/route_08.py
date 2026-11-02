"""Device route script route_08 for Omni-Notes.

Method: LogDelegate.w(String)
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 E7e3c321b E89ba0d21 Eb4f41bd1 Eb5b36c1c E15489aeb E4306cbbb
    E7d8539a9 E1f9e6935 E51dad05c E47f06889 E0303252f E66006fe9 E82d31de0
    E71c00ccb Ede33b03c E3a1de1ee E371a589d E68a53dad Eb47bdb88 E4ec276f0
    E3207e171
Printed route: the trigger graph path for LogDelegate.w(String)
    (graphs/Omni-Notes/out/omni-notes_trigger_graph.json, paths entry;
    sample_30_routes.txt has no block for this method — it does carry the
    shared export prefix, steps 1-27 of the NotificationsHelper block, which
    differ from this route only in the final edge). Ref BackupHelper.java:112-121.
Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    android.permission.READ_EXTERNAL_STORAGE, android.permission.WRITE_EXTERNAL_STORAGE
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

One block per route edge, in route order. Lifecycle, page, explicit-call, and
framework edges with no user action get a comment, not an action. Every action
names an edge id of this route (the harness enforces it). The note with an
attachment the route needs (STATE "a note has an attachment (the backup
copies the attachments)") is created as STATE steps folded into the
E89ba0d21 block, before that edge's own drawer tap, following the precedent
for STATE steps in other device scripts; it is marked STATE there, not
presented as the E89ba0d21 trigger itself.

CAVEAT (see report): LogDelegate.w fires only inside the
FileNotFoundException catch of BackupHelper.exportAttachments
(BackupHelper.java:112-120), i.e. for an attachment whose file is missing
at backup time. A note attachment created through the UI is copied into
the app's private attachment directory by AttachmentTask, so its file
exists at backup time and the catch may not fire on a real run. This
script drives the containing export loop as far as the UI allows; whether
w is actually reached needs a missing-file precondition the harness
cannot create (no file-delete action), which is a decision for the
device lead / merger, not something this script can fake.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af '
            'Ef86ebfe1 E7e3c321b E89ba0d21 Eb4f41bd1 Eb5b36c1c E15489aeb '
            'E4306cbbb E7d8539a9 E1f9e6935 E51dad05c E47f06889 E0303252f '
            'E66006fe9 E82d31de0 E71c00ccb Ede33b03c E3a1de1ee E371a589d '
            'E68a53dad Eb47bdb88 E4ec276f0 E3207e171').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_08', EDGE_IDS, a.log,
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
    # open the drawer. STATE first (this route needs a note with an
    # attachment): create a note the way route_01 creates one — long-press
    # the + button (res/layout/fab.xml id fab), tap the title field
    # (res/layout/fragment_detail.xml id detail_title) and the content field
    # (res/layout/fragment_detail_content.xml id detail_content), type, then
    # tap "Attachment" in the toolbar menu (menu_detail.xml, title
    # "Attachment"), tap "Files" in the attachment popup
    # (res/layout/attachment_dialog.xml id files, text "Files"), pick
    # photo_1.jpg in the system picker (Pictures fixture), then Back saves
    # the note and returns to the list. UNCERTAINTY: the system picker's
    # navigation to photo_1.jpg is not grounded in app res (see report).
    r.long_tap('E89ba0d21', res_id='it.feio.android.omninotes:id/fab')
    r.tap('E89ba0d21', res_id='it.feio.android.omninotes:id/detail_title')
    r.type_text('Route08 note', 'E89ba0d21')
    r.tap('E89ba0d21', res_id='it.feio.android.omninotes:id/detail_content')
    r.type_text('Route08 attachment note', 'E89ba0d21')
    r.tap('E89ba0d21', text='Attachment')
    r.tap('E89ba0d21', text='Files')
    r.tap('E89ba0d21', text='photo_1.jpg')
    r.back('E89ba0d21')
    # The edge's own trigger: open the drawer via the toolbar navigation
    # icon. UNCERTAINTY: the icon's content description is set by
    # ActionBarDrawerToggle from R.string.drawer_open ("drawer open",
    # NavigationDrawerFragment.java:172-177); it is not verified on device.
    r.tap('E89ba0d21', desc='drawer open')
    # Eb4f41bd1 onDrawerOpened@NOTES -> S_DRAWER@NOTES: the drawer is open, no action.
    r.comment('The drawer is open', 'Eb4f41bd1')
    # Eb5b36c1c S_DRAWER@NOTES -> CategoryMenuTask.lambda$null$0: tap Settings
    # at the bottom of the drawer (res/layout/drawer_category_list_footer.xml
    # id settings; res_id avoids the textAllCaps "SETTINGS" display form).
    r.tap('Eb5b36c1c', res_id='it.feio.android.omninotes:id/settings')
    # E15489aeb lambda$null$0 -> SettingsActivity.<init>: intent, no action.
    r.comment('startActivity(SettingsActivity)', 'E15489aeb')
    # E4306cbbb SettingsActivity.<init> -> S_SETTINGS: the settings root is shown, no action.
    r.comment('The settings root is shown', 'E4306cbbb')
    # E7d8539a9 S_SETTINGS -> SettingsActivity.onPreferenceStartFragment@DATA:
    # tap "Data" (res/xml/settings.xml, title "Data").
    r.tap('E7d8539a9', text='Data')
    # E1f9e6935 onPreferenceStartFragment@DATA -> S_SETTINGS_DATA: the sub-screen
    # opens on top of the root, no action.
    r.comment('The Data sub-screen opens on top of the root', 'E1f9e6935')
    # E51dad05c S_SETTINGS_DATA -> SettingsActivity.onPreferenceStartFragment@SYNC:
    # tap "Sync and Backups" (res/xml/settings_data.xml, title
    # "Sync and Backups"; the trigger-graph gui text says "Sync").
    r.tap('E51dad05c', text='Sync and Backups')
    # E47f06889 onPreferenceStartFragment@SYNC -> S_SETTINGS_SYNC: the sub-screen
    # opens, no action.
    r.comment('The Sync sub-screen opens', 'E47f06889')
    # E0303252f S_SETTINGS_SYNC -> SettingsFragment.lambda$onResume$1: tap the
    # export preference (res/xml/settings_sync_import_export.xml key
    # settings_export_data, title "Backup"; the trigger-graph gui text says
    # "Export").
    r.tap('E0303252f', text='Backup')
    # E66006fe9 lambda$onResume$1 -> SettingsFragment.lambda$null$0:
    # WRITE_EXTERNAL_STORAGE is granted by run_app.sh, so export(view) runs, no action.
    r.comment('WRITE_EXTERNAL_STORAGE granted: export(view)', 'E66006fe9')
    # E82d31de0 lambda$null$0 -> SettingsFragment.export: explicit call, no action.
    r.comment('export(view)', 'E82d31de0')
    # E71c00ccb SettingsFragment.export -> S_DLG_EXPORT: the backup-name dialog
    # opens; the default name is the dialog's hint, so no typing is needed, no action.
    r.comment('The backup-name dialog opens (default name from its hint)', 'E71c00ccb')
    # Ede33b03c S_DLG_EXPORT -> SettingsFragment.lambda$export$32: tap Confirm
    # (SettingsFragment.java:662, positiveText R.string.confirm = "Confirm").
    r.tap('Ede33b03c', text='Confirm')
    # E3a1de1ee lambda$export$32 -> BackupHelper.startBackupService: explicit call, no action.
    r.comment('BackupHelper.startBackupService(name)', 'E3a1de1ee')
    # E371a589d startBackupService -> DataBackupIntentService.onHandleIntent@EXPORT:
    # IntentService worker thread, no action.
    r.comment('IntentService.onHandleIntent runs on a worker thread', 'E371a589d')
    # E68a53dad onHandleIntent@EXPORT -> DataBackupIntentService.exportData:
    # the export action, no action.
    r.comment('The export action', 'E68a53dad')
    # Eb47bdb88 exportData -> BackupHelper.exportAttachments(File,NotificationsHelper):
    # explicit call, no action.
    r.comment('Direct call', 'Eb47bdb88')
    # E4ec276f0 exportAttachments(File,NotificationsHelper) ->
    # exportAttachments(NotificationsHelper,File,List,List): explicit call, no action.
    r.comment('Direct call', 'E4ec276f0')
    # E3207e171 exportAttachments(NotificationsHelper,File,List,List) -> LogDelegate.w(String):
    # explicit call inside the attachment-copy loop; w fires only for an
    # attachment whose file is missing (BackupHelper.java:112-120) — see the
    # header caveat. No user action; the coverage lookup detects the target.
    r.comment('Attachment-copy loop; w is the missing-file catch branch', 'E3207e171')
    r.done()


if __name__ == '__main__':
    main()
