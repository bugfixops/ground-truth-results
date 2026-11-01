"""Route route_23: VanillaMediaPlayer.setDataSource (REWORK).

Printed route source: graphs/Vanilla-Music/verification.csv path row
"VanillaMediaPlayer.setDataSource" ("Steps read: onStart starts
PlaybackService -> onCreate -> setCurrentSong(0) ->
SongTimeline.shiftCurrentSong -> changed ->
PlaybackService.timelineChanged -> handleMessage(MSG_GAPLESS_UPDATE)
-> triggerGaplessUpdate -> prepareMediaPlayer ->
VanillaMediaPlayer.setDataSource") and
device/routes/Vanilla-Music/ROUTES.csv row route_23 (source:
PlaybackActivity.java:124-127; PlaybackService.java:521,1326,
1922-1923,1604,819,668; SongTimeline.java:724,1052).

Edge ids, in order:
  E47380ade, E3aea4024, E8ee3f512, E8e6e45c2, Ea1ca8276, E4507ab7d,
  Ea8a7ea8d, Ec9aed208, Ebc00a1d8, E467e73e0, E2605fb72, E4fbbd6e1,
  Eb25f681d.

Permissions: none (ROUTES.csv permissions cell is empty).
Fixtures: none (STATE file gates: none).
Setup (done by run_app.sh before this script): push fixtures/Music +
media scan (15 files: 12 mp3 + 3 wav).

WHY THE ORIGINAL SCRIPT FAILED (auditor-proven, d3-16-30 audit):
the original only launched and waited for "Artists". Two printed
guards in PlaybackService.triggerGaplessUpdate then certainly fail
on a fresh pm-clear run:
  1. triggerGaplessUpdate returns early unless the player is
     initialized (PlaybackService.java:792-794:
     "if (mMediaPlayerInitialized != true) return;").
  2. It requires a next song (:801-807: "getSong(1) != null",
     finish action not REPEAT_CURRENT / STOP_CURRENT, and
     "!mTimeline.isEndOfQueue()").
After pm clear there is no playback and no queue, so both fail and
the script would record reached=no for a REACHABLE method.
CORRECTION of the original header's wrong claim: the setup scan
populates the media LIBRARY (database), not the playback QUEUE
(timeline). The queue comes from playback actions (here, the
play-all tap) or restored saved state, and pm clear wipes the
latter. Nothing in this script relies on a queue surviving pm clear.

REWORK SEQUENCE (this script, route_23 only):
  1. Launch, wait for "Artists", then tap the "Play all" header row.
     This builds the playback queue from the scanned library (all
     fixture songs; 15 files, so at least 2 songs are queued) and
     starts playback. This is the queue guard's fix: getSong(1) is
     non-null afterwards, and the queue is nowhere near its end.
  2. Swipe the panel to the controls stage and tap "next". This
     triggers the printed route's exact middle: PlaybackActivity
     onClick case R.id.next calls shiftCurrentSong(SHIFT_NEXT_SONG)
     (PlaybackActivity.java:215-217), which reaches
     PlaybackService.shiftCurrentSong -> setCurrentSong ->
     SongTimeline.shiftCurrentSong -> changed ->
     PlaybackService.timelineChanged. The shift also runs
     processSong, which sets mMediaPlayerInitialized = true
     (PlaybackService.java:1378) and immediately re-sends
     MSG_GAPLESS_UPDATE (:1380-1381); timelineChanged separately
     sends MSG_GAPLESS_UPDATE delayed 100 ms (:1922-1923). So the
     gapless branch fires twice over, both times with the player
     initialized and a next song present -- the two guards that
     failed in the original are both satisfied before the branch
     runs.
  3. The remaining edges are comment-only: the handler branch calls
     triggerGaplessUpdate, whose guards now pass (gapless playback
     is not disabled by default, PrefDefaults.java:84; the fresh
     finish action is FINISH_STOP = 0, SongTimeline.java:54, which
     is neither REPEAT_CURRENT = 2 nor STOP_CURRENT = 3), so it
     calls prepareMediaPlayer(mPreparedMediaPlayer, nextSong.path)
     (:819), and prepareMediaPlayer calls mp.setDataSource(path)
     (:667-670) -- the target. A final screenshot + UI dump give
     the 100 ms delayed message time to fire before run_app.sh
     takes its coverage dump.

UI facts used (read from layout XML / strings, never invented):
- The default library tab title is "Artists"
  (res/values/translatable.xml artists).
- The play-all header row text is "Play all"
  (res/values/translatable.xml play_all; LibraryActivity.updateHeaders
  sets the header text to it under the default action; same header
  tap as audited routes 21 and 27).
- The controls-stage "next" button is res/layout/controls.xml id
  "next" (content-desc @string/next_song = "Next track",
  translatable.xml:309). The swipe-up uses scroll_to targeting
  that id, as in audited route_18: scroll_to swipes up until its
  target appears, and returns without swiping if the button is
  already in the dump.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness.harness import Runner


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_23", edge_ids=[
        "E47380ade", "E3aea4024", "E8ee3f512", "E8e6e45c2", "Ea1ca8276",
        "E4507ab7d", "Ea8a7ea8d", "Ec9aed208", "Ebc00a1d8", "E467e73e0",
        "E2605fb72", "E4fbbd6e1", "Eb25f681d",
    ], log_path=args.log, dry_run=args.dry_run, outdir=args.outdir)

    # E47380ade -- MAIN / LAUNCHER intent starts LibraryActivity.
    # Wait for library content after launch, then SETUP (not the
    # launch edge's trigger): tap the "Play all" header row. This
    # builds the playback queue from the scanned library and starts
    # playback, fixing the original's missing queue: after this tap
    # getSong(1) is non-null (15 fixture songs queued) and the
    # queue is nowhere near its end. The setup scan alone does NOT
    # build a queue -- it populates the media library only.
    r.launch(args.package + "/.LibraryActivity", "E47380ade")
    r.wait_for("E47380ade", text="Artists")
    r.tap("E47380ade", text="Play all")

    # E3aea4024 -- Activity lifecycle callback (LibraryActivity
    # onStart). No user action.
    r.comment("lifecycle-onStart-no-user-action", "E3aea4024")

    # E8ee3f512 -- Direct call: LibraryActivity.onStart ->
    # PlaybackActivity.onStart.
    r.comment("direct-call-no-user-action", "E8ee3f512")

    # E8e6e45c2 -- startService(new Intent(this,
    # PlaybackService.class)): the service is created and started;
    # guard PlaybackService.hasInstance() is false (the service does
    # not run yet -- run_app.sh runs pm clear before this script, so
    # no service instance survives into the route).
    r.comment("startService-guard-service-not-running", "E8e6e45c2")

    # Ea1ca8276 -- the system creates the service and calls onCreate.
    # No user action.
    r.comment("lifecycle-service-onCreate-no-user-action", "Ea1ca8276")

    # E4507ab7d -- Direct call: PlaybackService.onCreate ->
    # setCurrentSong(0). NOTE why launch alone was insufficient:
    # onCreate's setCurrentSong(0) runs while the timeline is still
    # empty (no queue after pm clear), so the song is null and
    # setCurrentSong returns early, before processSong ever runs --
    # mMediaPlayerInitialized stays false. The play-all tap in the
    # launch block above is what supplies the queue this edge's
    # chain needs; the next tap below re-runs the chain with the
    # queue present.
    r.comment("direct-call-onCreate-setCurrentSong-empty-queue-note",
              "E4507ab7d")

    # Ea8a7ea8d -- Direct call: setCurrentSong ->
    # SongTimeline.shiftCurrentSong. USER ACTION that produces this
    # edge's chain: swipe the panel to the controls stage
    # (scroll_to swipes up until the "next" button appears, as in
    # audited route_18) and tap "next". PlaybackActivity.onClick
    # case R.id.next calls shiftCurrentSong(SHIFT_NEXT_SONG)
    # (PlaybackActivity.java:215-217), reaching
    # PlaybackService.shiftCurrentSong -> setCurrentSong ->
    # SongTimeline.shiftCurrentSong. The shift runs processSong,
    # which sets mMediaPlayerInitialized = true
    # (PlaybackService.java:1378) -- fixing the original's first
    # failed guard -- while the queue built by the play-all tap
    # keeps getSong(1) non-null -- fixing the second.
    r.scroll_to("Ea8a7ea8d", res_id="next")
    r.wait_for("Ea8a7ea8d", res_id="next")
    r.tap("Ea8a7ea8d", res_id="next")

    # Ec9aed208 -- Direct call: shiftCurrentSong -> changed.
    # Follows from the "next" tap: the shift delta is
    # SHIFT_NEXT_SONG, not SHIFT_KEEP_SONG, so
    # shiftCurrentSongInternal calls changed()
    # (SongTimeline.java:724 region; changed() at :1052).
    r.comment("direct-call-shift-changed-follows-next-tap", "Ec9aed208")

    # Ebc00a1d8 -- Virtual/interface call: changed ->
    # PlaybackService.timelineChanged. timelineChanged removes any
    # pending MSG_GAPLESS_UPDATE and sends it delayed 100 ms
    # (PlaybackService.java:1922-1923). The final screenshot/dump
    # below give that message time to fire.
    r.comment("virtual-call-timelineChanged-gapless-delayed-100ms",
              "Ebc00a1d8")

    # E467e73e0 -- the branch of PlaybackService that handles
    # MSG_GAPLESS_UPDATE runs. The handler message is posted by
    # timelineChanged (and, immediately, by processSong after the
    # player is initialized); no user action.
    r.comment("handler-MSG_GAPLESS_UPDATE-no-user-action", "E467e73e0")

    # E2605fb72 -- call made in the message branch:
    # handleMessage@MSG_GAPLESS_UPDATE -> triggerGaplessUpdate.
    # Its guards now pass: mMediaPlayerInitialized is true
    # (processSong, :1378), getSong(1) is non-null (play-all queue
    # of 15 songs, position now 1 after the "next" tap, so a
    # further song remains), the finish action is the fresh
    # default FINISH_STOP (SongTimeline.java:54), not
    # REPEAT_CURRENT or STOP_CURRENT, and gapless playback is not
    # disabled by default (PrefDefaults.java:84).
    r.comment("message-branch-call-guards-now-satisfied", "E2605fb72")

    # E4fbbd6e1 -- Direct call: triggerGaplessUpdate ->
    # prepareMediaPlayer (with the next song's path,
    # PlaybackService.java:819).
    r.comment("direct-call-no-user-action", "E4fbbd6e1")

    # Eb25f681d -- Direct call: prepareMediaPlayer ->
    # VanillaMediaPlayer.setDataSource (target;
    # prepareMediaPlayer calls mp.setDataSource(path) then
    # mp.prepare(), PlaybackService.java:667-670). Final
    # screenshot + UI dump: evidence for the live run and time
    # for the 100 ms delayed MSG_GAPLESS_UPDATE to fire before
    # run_app.sh takes its coverage dump.
    r.screenshot("gapless-fired", "Eb25f681d")
    r.dump_ui("gapless-fired", "Eb25f681d")
    r.comment("direct-call-target-reached", "Eb25f681d")

    r.done()


if __name__ == "__main__":
    main()
