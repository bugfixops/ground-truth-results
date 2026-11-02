"""Device route script route_24 for Omni-Notes.

Method: NotificationChannels.getChannels
Edge ids: Ea3d8b925 E728b7322 E9d299ee9 Edc764532
Printed route: graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/sample_30_routes.txt
    (NotificationChannels.getChannels, 4 steps; path row result fixed,
    confirmed_by SOURCE, ref OmniNotes.java:80-93,104-110;
    NotificationsHelper.java:55-57)
Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    none (ROUTES.csv route_24 permission column is empty).
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

Startup route: launching the app runs the whole chain; every edge after the
launch is lifecycle or an explicit call, so all of them get a comment, not an
action. NOTE: unlike the other routes here, this route's first edge is
S_ENTRY -> OmniNotes.<init> (the Application), not MainActivity.<init> --
verified in the trigger graph. Launching MainActivity is still the correct
first action: it starts the app process, and Application.onCreate runs
before any activity.

One block per route edge, in route order. Every action names an edge id of
this route (the harness enforces it).
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ea3d8b925 E728b7322 E9d299ee9 Edc764532').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_24', EDGE_IDS, a.log,
               dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    # Ea3d8b925 S_ENTRY -> OmniNotes.<init>: the process starts. Launching
    # MainActivity starts the app process (Application.onCreate runs first).
    r.launch('it.feio.android.omninotes/.MainActivity', 'Ea3d8b925')
    # E728b7322 OmniNotes.<init> -> OmniNotes.onCreate: lifecycle, no action.
    r.comment('The system calls Application.onCreate', 'E728b7322')
    # E9d299ee9 OmniNotes.onCreate -> NotificationsHelper.initNotificationChannels:
    # explicit call, no action. Guard holds on a normal launch: this is the
    # app's own process, so initLeakCanary() is false (true only in
    # LeakCanary's analyzer process, OmniNotes.java:83-85,104-110).
    r.comment('initNotificationChannels() in the app process', 'E9d299ee9')
    # Edc764532 initNotificationChannels -> NotificationChannels.getChannels:
    # explicit call, no user action; the coverage lookup detects the target.
    # Guard holds: SDK_INT > 26 is true on API 27 (NotificationsHelper.java:56).
    r.comment('getChannels() on API 27', 'Edc764532')
    r.done()


if __name__ == '__main__':
    main()
