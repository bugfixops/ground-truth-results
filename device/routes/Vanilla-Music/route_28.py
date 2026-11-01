"""Device replay script for Vanilla-Music route_28.

Method: Song.hashCode
Edge ids: E47380ade E3aea4024 E8ee3f512 E8e6e45c2 Ea1ca8276 Ec1036aa5
    Ea66f65e5 Ee881b439 Ead1a4bd0 E32c7773c E61cc58d1
Printed route source: graphs/Vanilla-Music/verification.csv path row
    (result correct; ref PlaybackActivity.java:124-127;
    PlaybackService.java:520,1000-1014,1080; SongTimeline.java:507;
    Song.java:319) and device/routes/Vanilla-Music/ROUTES.csv route_28.
Permissions (ROUTES.csv): none. Fixtures: none (no STATE file gate).
Setup: push fixtures/Music + media scan (run_app setup step).
Standard config: run_app does pm clear before this script; the script
    starts by launching the app. The rest of the route is service and
    state-machine dispatch with no UI step: onStart starts the service,
    updateState -> MSG_PROCESS_STATE -> processNewState -> setFinishAction
    -> Song.equals -> Song.hashCode. There is no screen assertion for
    the target; the JaCoCo coverage lookup in run_app.sh is what
    confirms the method ran.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ["E47380ade", "E3aea4024", "E8ee3f512", "E8e6e45c2", "Ea1ca8276",
            "Ec1036aa5", "Ea66f65e5", "Ee881b439", "Ead1a4bd0", "E32c7773c",
            "E61cc58d1"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", default=None)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    r = Runner(package=a.package, route="route_28", edge_ids=EDGE_IDS,
               log_path=a.log, dry_run=a.dry_run, outdir=a.outdir)
    # E47380ade: S_ENTRY -> LibraryActivity.<init>
    # MAIN / LAUNCHER intent starts LibraryActivity.
    r.launch("ch.blinkenlights.android.vanilla/.LibraryActivity",
             "E47380ade")
    # E3aea4024: LibraryActivity.<init> -> onStart. Lifecycle; no action.
    r.comment("lifecycle: onStart runs on launch", "E3aea4024")
    # E8ee3f512: onStart -> PlaybackActivity.onStart. Direct call.
    r.comment("direct call: onStart chains to PlaybackActivity", "E8ee3f512")
    # E8e6e45c2: PlaybackActivity.onStart -> PlaybackService.<init>.
    # startService: the service is created and started; no action.
    r.comment("service start: onStart starts PlaybackService", "E8e6e45c2")
    # Ea1ca8276: PlaybackService.<init> -> onCreate. System creates it.
    r.comment("service lifecycle: onCreate runs on service start",
              "Ea1ca8276")
    # Ec1036aa5: onCreate -> updateState. Direct call.
    r.comment("direct call: onCreate updates state", "Ec1036aa5")
    # Ea66f65e5: updateState -> handleMessage@MSG_PROCESS_STATE.
    r.comment("message dispatch: MSG_PROCESS_STATE branch runs", "Ea66f65e5")
    # Ee881b439: handleMessage@MSG_PROCESS_STATE -> processNewState.
    r.comment("call made in the message branch", "Ee881b439")
    # Ead1a4bd0: processNewState -> setFinishAction. Direct call.
    r.comment("direct call: new state sets the finish action", "Ead1a4bd0")
    # E32c7773c: setFinishAction -> Song.equals. Direct call.
    r.comment("direct call: finish action compares songs", "E32c7773c")
    # E61cc58d1: Song.equals -> Song.hashCode. Direct call; target.
    # No UI assertion exists for this internal call; coverage confirms it.
    r.comment("direct call: equals invokes hashCode (target)", "E61cc58d1")
    r.done()


if __name__ == "__main__":
    main()
