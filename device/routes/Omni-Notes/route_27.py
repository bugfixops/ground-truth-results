"""Device route script route_27 for Omni-Notes.

Method: OmniNotes.getAppContext
Edge ids: Ea3d8b925 E728b7322 E9d299ee9 Ea84851e2 E471c5340 E7143b84b
Printed route: graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/sample_30_routes.txt
    is NOT the source for this route's step list in the form printed for the
    sampled routes; the step list here is the ROUTES.csv edge list checked
    against graphs/Omni-Notes/out/omni-notes_trigger_graph.json (same edges,
    same order) and against out/methods.csv (OmniNotes.getAppContext,
    shortest_path S_ENTRY > OmniNotes.<init> > OmniNotes.onCreate >
    NotificationsHelper.initNotificationChannels > NotificationChannels.<clinit>
    > NotificationChannels$1.<init> > OmniNotes.getAppContext).
    Source refs (ROUTES.csv): OmniNotes.java:80-93; NotificationChannels.java:34-45;
    IntroActivity.java:48-51.
Permissions (ROUTES.csv): none (run_app.sh grants nothing for this route).
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

NOTE ON THE FIRST EDGE: unlike routes 28-31, this route does NOT start
S_ENTRY -> MainActivity.<init>. Its first edge is S_ENTRY -> OmniNotes.<init>
(the process starts; trigger-graph evidence AndroidManifest.xml:47-55). Launching
MainActivity starts the process, so Application.onCreate runs before any activity
UI; the launch call below is therefore logged against Ea3d8b925. No tap is
needed or invented: the whole chain runs inside Application.onCreate and the
NotificationChannels static initialiser. A first-run IntroActivity overlay may
appear after MainActivity.onCreate, but it is downstream of this chain and is
not dismissed here — this route needs no activity UI at all.

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

EDGE_IDS = ('Ea3d8b925 E728b7322 E9d299ee9 Ea84851e2 E471c5340 '
            'E7143b84b').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_27', EDGE_IDS, a.log,
               dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    # Ea3d8b925 S_ENTRY -> OmniNotes.<init>: the process starts. Launching
    # MainActivity starts the process, so OmniNotes.<init> and onCreate run.
    r.launch('it.feio.android.omninotes/.MainActivity', 'Ea3d8b925')
    # E728b7322 OmniNotes.<init> -> OmniNotes.onCreate: lifecycle, no action.
    r.comment('The system calls Application.onCreate', 'E728b7322')
    # E9d299ee9 OmniNotes.onCreate -> NotificationsHelper.initNotificationChannels:
    # explicit call, no action. Guard: initLeakCanary() is false in the app's own
    # process (true only in LeakCanary's analyzer process, OmniNotes.java:83-85).
    r.comment('onCreate reaches initNotificationChannels (app process, not LeakCanary analyzer)', 'E9d299ee9')
    # Ea84851e2 NotificationsHelper.initNotificationChannels -> NotificationChannels.<clinit>:
    # class initialisation on first use, no action. Guard: SDK_INT > 26, true on API 27.
    r.comment('First use of NotificationChannels runs its static initialiser (API 27)', 'Ea84851e2')
    # E471c5340 NotificationChannels.<clinit> -> NotificationChannels$1.<init>:
    # explicit call in the static initialiser (NotificationChannels.java:34), no action.
    r.comment('Static initialiser builds the channel list', 'E471c5340')
    # E7143b84b NotificationChannels$1.<init> -> OmniNotes.getAppContext:
    # explicit call (NotificationChannels.java:43), no user action; the coverage
    # lookup detects the target.
    r.comment('Channel construction calls OmniNotes.getAppContext()', 'E7143b84b')
    r.done()


if __name__ == '__main__':
    main()
