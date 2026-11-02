"""Device route script route_30 for Omni-Notes.

Method: LanguageHelper.setLocale
Edge ids: Ea7466154 E3da28cbd Ec15bdfef E636604a4
Printed route: graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/sample_30_routes.txt
    (LanguageHelper.setLocale, 4 steps; path row result correct, confirmed_by SOURCE,
    ref LanguageHelper.java:60; BaseActivity.java:73: attachBaseContext calls
    updateLanguage (BaseActivity.java:73), which ends in setLocale on every
    branch (LanguageHelper.java:60)).
Permissions (ROUTES.csv): none (run_app.sh grants nothing for this route).
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

HOW THE LOCALE IS SET (read from the printed route, followed exactly): there is
no language-preference tap in this route. On every cold start, before onCreate,
the framework calls BaseActivity.attachBaseContext, which calls
LanguageHelper.updateLanguage(newBase, null) (BaseActivity.java:72-74); with a
null language argument, updateLanguage reads the stored PREF_LANG (empty on a
fresh install, so it stores Locale.getDefault()) and then calls setLocale on
every branch (LanguageHelper.java:45-60). So launching the app is the whole
route: no settings tap, no language choice, and no invented tap. A settings
language change would be a different route (it would end in a recreate, not in
this attachBaseContext chain).

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

EDGE_IDS = ('Ea7466154 E3da28cbd Ec15bdfef E636604a4').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_30', EDGE_IDS, a.log,
               dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    # Ea7466154 S_ENTRY -> MainActivity.<init>: launcher starts MainActivity.
    r.launch('it.feio.android.omninotes/.MainActivity', 'Ea7466154')
    # E3da28cbd MainActivity.<init> -> BaseActivity.attachBaseContext: lifecycle,
    # no action. The framework calls attachBaseContext before onCreate.
    r.comment('Activity lifecycle callback: attachBaseContext before onCreate', 'E3da28cbd')
    # Ec15bdfef BaseActivity.attachBaseContext -> LanguageHelper.updateLanguage:
    # explicit call (BaseActivity.java:73), no action.
    r.comment('attachBaseContext calls LanguageHelper.updateLanguage(newBase, null)', 'Ec15bdfef')
    # E636604a4 LanguageHelper.updateLanguage -> LanguageHelper.setLocale:
    # explicit call (LanguageHelper.java:60), reached on every branch; no user
    # action; the coverage lookup detects the target.
    r.comment('updateLanguage ends in setLocale on every branch', 'E636604a4')
    r.done()


if __name__ == '__main__':
    main()
