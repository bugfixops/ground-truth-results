"""Vanilla-Music route_12: ScheduledLibraryUpdate.finalizeScan.

Edge ids (ROUTES.csv, in order):
  E47380ade E3aea4024 E8ee3f512 E8e6e45c2 Ea1ca8276 E6a38084c
  E562fa552 Ee7dd65dd E3216c038 E4c4e4539 E080ed7e2 Ea27ba51e
  E9c997cdf

Printed route source:
  verification.csv path row (ScheduledLibraryUpdate.finalizeScan):
  "Steps read: PlaybackService.onCreate -> new PlaylistObserver(...)
  (constructor sends MSG_FULL_SYNC_SCAN unconditionally) ->
  fullSyncScan -> Playlist.deletePlaylist -> MediaLibrary.removePlaylist
  -> notifyObserver(PLAYLIST,...) -> ScheduledLibraryUpdate$1.onChange
  (ENV: the job runs, guard: the library update job runs) ->
  finalizeScan (access$100 bridge, consistent with a private method)."
  ROUTES.csv row: source "PlaybackActivity.java:124-127;
  PlaybackService.java:513,441-533; PlaylistObserver.java:143-144,
  236-238,436; Playlist.java:182; MediaLibrary.java:438,355-359;
  ScheduledLibraryUpdate.java:79,139", env hardware;time.
Permissions: none (ROUTES.csv). Fixtures: none (STATE file gates: none).
Setup (run_app.sh, before this script): push fixtures/Music + media scan.

Job gate (ScheduledLibraryUpdate.java:39,51-58): job id 9,
  setRequiresCharging(true), setRequiresDeviceIdle(true),
  setPeriodic(3600000 * 32) -- about 32 hours. This script does NOT
  wait 32 hours: the job is force-run instead (see the Ea27ba51e
  block). The observer that receives the notifying change is
  registered in onStartJob, so the notifying library change must
  happen WHILE the job runs -- hence the order in this script:
  launch first, then the force-run step, then the library change.
  Do NOT rely on the first-launch fullSyncScan (the E3216c038 chain
  below): it precedes job start.

Harness limit, stated explicitly: harness.py exposes NO raw-shell
  action (its actions are launch/key/back/tap/long_tap/type_text/
  scroll_to/wait_for/start_intent/broadcast/grant/deny/push_fixture/
  screenshot/dump_ui/assert_text/comment/done), and neither
  start_intent nor broadcast can run a JobScheduler command. The
  force-run is therefore NOT implemented inside this script: it is
  logged as a comment on Ea27ba51e and must be executed by run_app
  (concurrently, while this script runs) as:
    adb shell cmd jobscheduler run -f <package> 9
  If that command does not register the observer on the replay image,
  that is a harness finding for the device lead, not a script error.

UI labels used, all read from layout XML / strings.xml, never invented:
  - Songs tab label "Tracks" (R.string.songs).
  - Song row "Morning Light": fixture 01 Morning Light.mp3, ID3 title
    "Morning Light" (verified with ffprobe on the setup fixtures).
  - Fancy-menu rows "Add to playlist…" (R.string.add_to_playlist),
    "New playlist…" (R.string.new_playlist), "Create"
    (R.string.create).

Placement: this file is written for device/routes/Vanilla-Music/
  (four dirnames up from there is the repo root, which is what the
  sys.path derivation below assumes). It is delivered in the helper
  directory and must be copied to device/routes/Vanilla-Music/ by the
  merger before run_app.sh / drycheck.py execute it.
"""

import argparse
import os
import sys

_root = os.path.abspath(__file__)
for _ in range(4):
    _root = os.path.dirname(_root)
sys.path.insert(0, _root)

from device.harness.harness import Runner  # noqa: E402

PACKAGE_ACTIVITY = (
    "ch.blinkenlights.android.vanilla/"
    "ch.blinkenlights.android.vanilla.LibraryActivity"
)
EDGE_IDS = [
    "E47380ade", "E3aea4024", "E8ee3f512", "E8e6e45c2", "Ea1ca8276",
    "E6a38084c", "E562fa552", "Ee7dd65dd", "E3216c038", "E4c4e4539",
    "E080ed7e2", "Ea27ba51e", "E9c997cdf",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    args = ap.parse_args()

    r = Runner(package=args.package, route="route_12", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)

    # E47380ade -- ENTRY: MAIN / LAUNCHER intent starts LibraryActivity.
    # run_app.sh does pm clear and the setup step before this script.
    # Launching starts PlaybackService, which schedules job 9.
    r.launch(PACKAGE_ACTIVITY, "E47380ade")

    # E3aea4024 -- LIFECYCLE: Activity lifecycle callback (onStart).
    # No user action; the launch above drives it. The Tracks tab label
    # proves the library is shown.
    r.wait_for("E3aea4024", text="Tracks")

    # E8ee3f512 -- CALL: LibraryActivity.onStart -> PlaybackActivity
    # .onStart. Direct call; no user action.
    r.comment("onStart dispatch, no user action", "E8ee3f512")

    # E8e6e45c2 -- INTENT: startService(PlaybackService), guard
    # PlaybackService.hasInstance() is false (the service does not run
    # yet). Fired by onStart; no user action.
    r.comment("startService fired by onStart, no user action", "E8e6e45c2")

    # Ea1ca8276 -- LIFECYCLE: the system creates the service and calls
    # onCreate. No user action.
    r.comment("service onCreate, no user action", "Ea1ca8276")

    # E6a38084c -- CALL: PlaybackService.onCreate -> new
    # PlaylistObserver(...). Direct call; no user action.
    r.comment("PlaylistObserver construction, no user action", "E6a38084c")

    # E562fa552 -- ASYNC: sendUniqueMessage(MSG_FULL_SYNC_SCAN, 0); the
    # handler thread runs the message. No user action.
    r.comment("MSG_FULL_SYNC_SCAN dispatch, no user action", "E562fa552")

    # Ee7dd65dd -- CALL: message.what == MSG_FULL_SYNC_SCAN ->
    # fullSyncScan. No user action.
    r.comment("fullSyncScan dispatch, no user action", "Ee7dd65dd")

    # E3216c038 -- CALL: fullSyncScan -> Playlist.deletePlaylist.
    # Fires automatically on first launch (the service-creation scan).
    # It precedes job start, so it is NOT the job-time notify below.
    r.comment("first-launch scan deletePlaylist, no user action",
              "E3216c038")

    # E4c4e4539 -- CALL: Playlist.deletePlaylist ->
    # MediaLibrary.removePlaylist. Automatic; no user action.
    r.comment("removePlaylist, automatic, no user action", "E4c4e4539")

    # E080ed7e2 -- CALL: MediaLibrary.removePlaylist ->
    # MediaLibrary.notifyObserver. Automatic; no user action.
    r.comment("notifyObserver, automatic, no user action", "E080ed7e2")

    # Ea27ba51e -- CALL: notifyObserver -> ScheduledLibraryUpdate$1
    # .onChange for the observer of the RUNNING job (registered in
    # onStartJob), guard: the library update job runs. ENV: time
    # passes and the device is idle and charging (job 9, 32h periodic).
    # FORCE-RUN (run_app manual step, NOT a harness action -- the
    # harness has no raw-shell action): while this script runs, run:
    #   adb shell cmd jobscheduler run -f <package> 9
    # Then the library change below notifies the running job's
    # observer. Note the job's own scan also notifies on completion
    # (ScheduledLibraryUpdate.onStartJob starts a library scan), so
    # either notify path can deliver onChange while the job runs.
    r.comment("RUN_APP MANUAL STEP: adb shell cmd jobscheduler run -f "
              "package 9 while this script runs, before the change "
              "below; harness has no raw-shell action", "Ea27ba51e")
    r.tap("Ea27ba51e", text="Tracks")
    r.wait_for("Ea27ba51e", text="Morning Light")
    r.long_tap("Ea27ba51e", text="Morning Light")
    r.tap("Ea27ba51e", text="Add to playlist…")
    r.tap("Ea27ba51e", text="New playlist…")
    r.type_text("Route12", "Ea27ba51e")
    r.tap("Ea27ba51e", text="Create")

    # E9c997cdf -- CALL: ScheduledLibraryUpdate$1.onChange ->
    # ScheduledLibraryUpdate.finalizeScan (through access$100).
    # Dispatch from the observer notify; this is the target method.
    r.comment("finalizeScan dispatch from observer onChange, target",
              "E9c997cdf")
    r.screenshot("route_12_done", "E9c997cdf")
    r.dump_ui("route_12_done", "E9c997cdf")

    r.done()


if __name__ == "__main__":
    main()
