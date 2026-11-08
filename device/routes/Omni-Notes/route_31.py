"""Device route script route_31 for Omni-Notes.

Method: MediaStoreFactory.<init>
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 E7e3c321b E89ba0d21 Eb4f41bd1 Eb5b36c1c E15489aeb E4306cbbb
    E7d8539a9 E1f9e6935 E51dad05c E47f06889 E4fa5a179 Edb933e2f E821c0225
    E7dd46cd4 E21ccede7
Printed route: route_print_MediaStoreFactory.txt in this directory (CONSTRUCTED
    from the trigger graph, NOT read step by step from a sample print:
    MediaStoreFactory.<init> is not sampled in sample_30_routes.txt. The
    constructed file records, per edge, id, src, dst, trigger, gui, guard and
    evidence from graphs/Omni-Notes/out/omni-notes_trigger_graph.json, plus the
    shortest_path from graphs/Omni-Notes/out/methods.csv. Source refs
    (ROUTES.csv): FileHelper.java:75-86; SettingsFragment.java:684-685.)
Permissions (ROUTES.csv): none (run_app.sh grants nothing for this route).
Fixtures: Download/archive.zip — run_app.sh pushes it to /sdcard/Download/archive.zip
    before this script runs; the script picks it in the system picker by tapping
    its name. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

Selector grounding (layout/menu/strings XML or printed handler source only):
- Drawer toggle: NavigationDrawerFragment.java builds an ActionBarDrawerToggle on
  the toolbar with R.string.drawer_open ("drawer open", strings.xml) as the open
  description, so the toggle is tapped by content-desc "drawer open". See the
  uncertainty note in D3_27-31_REPORT.md: AppCompat renders the toggle desc from
  that string, but the exact dump value on the emulator is unverified.
- Settings: drawer_category_list_footer.xml id "settings" (included in the drawer
  as settings_view), tapped by res_id, not by its all-caps rendered text.
- Data: settings.xml preference title @string/settings_screen_data = "Data".
- Sync: the trigger shorthand "Sync" is the settings_data.xml preference whose
  title is @string/settings_screen_sync_import_export = "Sync and Backups";
  the script taps the full rendered title.
- Import: settings_sync_import_export.xml preference key
  settings_import_from_springpad, title @string/settings_import_from_springpad
  = "Import notes from Springpad"; the script taps the full rendered title
  (the trigger shorthand is "Import from Springpad").
- Picker file: the pushed fixture name "archive.zip", tapped by text in the
  system document picker (ROUTES_NOTES.md picker rule).
No fixed coordinates are used. No grant() or pm clear call is made.

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
            'E4306cbbb E7d8539a9 E1f9e6935 E51dad05c E47f06889 E4fa5a179 '
            'Edb933e2f E821c0225 E7dd46cd4 E21ccede7').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_31', EDGE_IDS, a.log,
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
    # E7e3c321b ListFragment.init -> S_LIST@NOTES: list set up on the default
    # Notes navigation, no action.
    r.comment('List set up on the default Notes navigation', 'E7e3c321b')
    # E89ba0d21 S_LIST@NOTES -> NavigationDrawerFragment$1.onDrawerOpened@NOTES:
    # open the drawer via the toolbar toggle (ActionBarDrawerToggle, desc from
    # R.string.drawer_open = "drawer open").
    r.tap('E89ba0d21', desc='drawer open')
    # Eb4f41bd1 onDrawerOpened -> S_DRAWER@NOTES: drawer open, no action.
    r.comment('The drawer is open', 'Eb4f41bd1')
    # Eb5b36c1c S_DRAWER@NOTES -> CategoryMenuTask.lambda$null$0: tap Settings
    # at the bottom of the drawer (drawer_category_list_footer.xml id settings).
    r.tap('Eb5b36c1c', res_id='it.feio.android.omninotes:id/settings')
    # E15489aeb lambda$null$0 -> SettingsActivity.<init>: startActivity, no action.
    r.comment('startActivity(SettingsActivity)', 'E15489aeb')
    # E4306cbbb SettingsActivity.<init> -> S_SETTINGS: settings root shown, no action.
    r.comment('The settings root is shown', 'E4306cbbb')
    # E7d8539a9 S_SETTINGS -> onPreferenceStartFragment@DATA: tap "Data"
    # (settings.xml title @string/settings_screen_data).
    r.tap('E7d8539a9', text='Data')
    # E1f9e6935 onPreferenceStartFragment@DATA -> S_SETTINGS_DATA: sub-screen
    # opens on top of the root, no action.
    r.comment('The Data sub-screen opens on top of the root', 'E1f9e6935')
    # E51dad05c S_SETTINGS_DATA -> onPreferenceStartFragment@SYNC: tap "Sync and
    # Backups" (settings_data.xml title @string/settings_screen_sync_import_export;
    # the trigger shorthand is "Sync").
    r.tap('E51dad05c', text='Sync and Backups')
    # E47f06889 onPreferenceStartFragment@SYNC -> S_SETTINGS_SYNC: sub-screen
    # opens, no action.
    r.comment('The Sync sub-screen opens', 'E47f06889')
    # E4fa5a179 S_SETTINGS_SYNC -> SettingsFragment.lambda$onResume$5: tap
    # "Import notes from Springpad" (settings_sync_import_export.xml title
    # @string/settings_import_from_springpad; trigger shorthand "Import from
    # Springpad"). This fires ACTION_GET_CONTENT, application/zip.
    r.tap('E4fa5a179', text='Import notes from Springpad')
    # Edb933e2f lambda$onResume$5 -> S_EXT_PICKER@SPRINGPAD: the system picker
    # opens (ACTION_GET_CONTENT), no action.
    r.comment('The system document picker opens (ACTION_GET_CONTENT, application/zip)', 'Edb933e2f')
    # E821c0225 S_EXT_PICKER@SPRINGPAD -> SettingsFragment.onActivityResult@SPRINGPAD:
    # pick the pushed fixture in the system picker by tapping its name.
    r.tap('E821c0225', text='archive.zip')
    # E7dd46cd4 onActivityResult@SPRINGPAD -> FileHelper.getPath: explicit call
    # resolving the zip path, no action.
    r.comment('onActivityResult resolves the zip path via FileHelper.getPath', 'E7dd46cd4')
    # E21ccede7 FileHelper.getPath -> MediaStoreFactory.<init>: explicit call when
    # isMediaDocument(uri) (media-provider document URI); no user action; the
    # coverage lookup detects the target.
    r.comment('Media-provider document URI: MediaStoreFactory.<init>', 'E21ccede7')
    r.done()


if __name__ == '__main__':
    main()
