"""Device route script route_26 for Omni-Notes.

Method: LanguageHelper.getLocale
Edge ids: Ea7466154 E3da28cbd Ec15bdfef Ef2537c86
Printed route: graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/sample_30_routes.txt
    does NOT contain this method (only 30 of 33 routes are printed there);
    edge list and trigger/gui text below come from ROUTES.csv and
    graphs/Omni-Notes/out/omni-notes_trigger_graph.json instead
    (LanguageHelper.java:45-60; BaseActivity.java:72-75).
Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    none (ROUTES.csv route_26 permission column is empty).
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

One block per route edge, in route order. Lifecycle and explicit-call edges
with no user action get a comment, not an action. Every action names an edge
id of this route (the harness enforces it).

STORED-LANGUAGE MECHANISM (read from LanguageHelper.java:45-60 and
SettingsFragment.java:348-357): the final edge's guard is "a language is
passed in, or the language preference is already stored". On the first
start after pm clear the preference is empty and updateLanguage(ctx, null)
takes the default-locale branch, which does NOT call getLocale. So the
script first stores a language through Settings -- Settings > Interface >
Language, choosing "English (English)" -- and then relaunches the app
within this same script. Choosing the language calls
LanguageHelper.updateLanguage(activity, "en_US") (which stores PREF_LANG)
and then SystemHelper.restartApp, which is System.exit(0)
(SettingsFragment.java:355-356; SystemHelper.java:34-43); the script's
second launch is therefore a fresh process whose attachBaseContext reads
the stored preference and takes the getLocale(language) branch. The
setup actions are logged against Ea7466154 (the launch edge) because the
harness requires every action to name an edge id of this route; the
route's own launch is the second launch below.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ea7466154 E3da28cbd Ec15bdfef Ef2537c86').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_26', EDGE_IDS, a.log,
               dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    # --- Pre-route setup: store a language through Settings.
    # Setup launch (fresh process after pm clear; its own attachBaseContext
    # takes the default-locale branch and does not reach getLocale).
    r.launch('it.feio.android.omninotes/.MainActivity', 'Ea7466154')
    # Open the navigation drawer: tap the toolbar navigation icon.
    # UNCERTAINTY: no id or text for this icon exists in res/layout; the
    # ActionBarDrawerToggle created in NavigationDrawerFragment.java sets
    # its content description from R.string.drawer_open ("drawer open",
    # res/values/strings.xml:414).
    r.tap('Ea7466154', desc='drawer open')
    # Tap "Settings" in the drawer footer (res/layout/drawer_category_list_footer.xml,
    # TextView id settings; CategoryMenuTask.java:129-135 starts SettingsActivity).
    r.tap('Ea7466154', res_id='it.feio.android.omninotes:id/settings')
    # Tap "Interface" on the settings root (res/xml/settings.xml
    # PreferenceScreen key settings_interface, title
    # @string/settings_screen_interface = "Interface"; SettingsActivity
    # opens the fragment with xmlName=settings_interface).
    r.tap('Ea7466154', text='Interface')
    # Tap "Language" (res/xml/settings_interface.xml ListPreference key
    # settings_language, title @string/settings_choose_language = "Language").
    r.tap('Ea7466154', text='Language')
    # Choose "English (English)" in the language list dialog
    # (res/values/arrays.xml languages / languages_codes: "English (English)"
    # pairs with en_US). The change listener stores PREF_LANG=en_US via
    # updateLanguage and then exits the process (System.exit(0)), so the
    # next launch below is a fresh process with a stored language.
    r.tap('Ea7466154', text='English (English)')
    # Ea7466154 S_ENTRY -> MainActivity.<init>: relaunch after the language
    # choice (fresh process; the stored preference now exists).
    r.launch('it.feio.android.omninotes/.MainActivity', 'Ea7466154')
    # E3da28cbd MainActivity.<init> -> BaseActivity.attachBaseContext:
    # lifecycle, no action.
    r.comment('Activity lifecycle callback', 'E3da28cbd')
    # Ec15bdfef BaseActivity.attachBaseContext -> LanguageHelper.updateLanguage:
    # explicit call, no action (BaseActivity.java:73).
    r.comment('updateLanguage(newBase, null)', 'Ec15bdfef')
    # Ef2537c86 LanguageHelper.updateLanguage -> LanguageHelper.getLocale:
    # explicit call, no user action; the coverage lookup detects the target.
    # Guard holds: the language preference is stored (en_US, chosen above),
    # so updateLanguage takes the getLocale(language) branch
    # (LanguageHelper.java:50-58).
    r.comment('Stored language branch: getLocale(language)', 'Ef2537c86')
    r.done()


if __name__ == '__main__':
    main()
