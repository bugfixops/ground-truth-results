"""Device route script route_25 for Omni-Notes.

Method: OmniNotes.getSharedPreferences
Edge ids: Ea7466154 E89791c67 Ea696f465 E1862d567 Ee7e60085 Ef5c7b6c8
Printed route: graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/sample_30_routes.txt
    (OmniNotes.getSharedPreferences, 6 steps; path row result fixed,
    confirmed_by SOURCE, ref BaseActivity.java:96-100;
    LogDelegate.java:48-49,92-94)
Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    none (ROUTES.csv route_25 permission column is empty).
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

Startup route: launching the app runs the whole chain; every edge after the
launch is lifecycle or an explicit call, so all of them get a comment, not an
action. The final edge's guard holds on this fresh process: it is the first
logging call of the process, so the static fileLoggingEnabled is still null
(LogDelegate.java:93-94) and isFileLoggingEnabled reads the preference.

One block per route edge, in route order. Every action names an edge id of
this route (the harness enforces it).
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ea7466154 E89791c67 Ea696f465 E1862d567 Ee7e60085 '
            'Ef5c7b6c8').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_25', EDGE_IDS, a.log,
               dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    # Ea7466154 S_ENTRY -> MainActivity.<init>: launcher starts MainActivity.
    r.launch('it.feio.android.omninotes/.MainActivity', 'Ea7466154')
    # E89791c67 MainActivity.<init> -> MainActivity.onResume: lifecycle, no action.
    r.comment('Activity lifecycle callback', 'E89791c67')
    # Ea696f465 MainActivity.onResume -> BaseActivity.onResume: explicit call, no action.
    r.comment('super.onResume()', 'Ea696f465')
    # E1862d567 BaseActivity.onResume -> LogDelegate.d: explicit call, no action
    # (BaseActivity.java:100 logs the preferences on resume).
    r.comment('LogDelegate.d(prefs.getAll().toString())', 'E1862d567')
    # Ee7e60085 LogDelegate.d -> LogDelegate.isFileLoggingEnabled: explicit call, no action.
    r.comment('isFileLoggingEnabled()', 'Ee7e60085')
    # Ef5c7b6c8 isFileLoggingEnabled -> OmniNotes.getSharedPreferences:
    # explicit call, no user action; the coverage lookup detects the target.
    # Guard holds: first logging call of this fresh process, so the static
    # fileLoggingEnabled is still null (LogDelegate.java:93-94).
    r.comment('First logging call: reads the preference', 'Ef5c7b6c8')
    r.done()


if __name__ == '__main__':
    main()
