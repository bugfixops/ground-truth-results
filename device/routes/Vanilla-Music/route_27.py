"""Device replay script for Vanilla-Music route_27.

Method: MediaUtils.getCursorForFileQuery
Edge ids: E47380ade E29472d10 E80427a98 E54b8ef2f E87e2a8b0 Ecc4f5b3c
    Ee6ca0a88 E285c0ada E651af531 E22acec54 E99e07df4
Printed route source: graphs/Vanilla-Music/verification.csv path row
    (result fixed; ref LibraryPagerAdapter.java:344,893-903,861-868,895,
    901; LibraryActivity.java:472-482,420; PlaybackService.java:1844-1847,
    1562,1814; SongTimeline.java:763) and
    device/routes/Vanilla-Music/ROUTES.csv route_27.
Permissions (ROUTES.csv): none. Fixtures: none (no STATE file gate).
Setup: push fixtures/Music + media scan (run_app setup step); the
    library must be populated before the header row is tapped.
Standard config: run_app does pm clear before this script; the script
    starts by launching the app.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ["E47380ade", "E29472d10", "E80427a98", "E54b8ef2f", "E87e2a8b0",
            "Ecc4f5b3c", "Ee6ca0a88", "E285c0ada", "E651af531", "E22acec54",
            "E99e07df4"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", default=None)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    r = Runner(package=a.package, route="route_27", edge_ids=EDGE_IDS,
               log_path=a.log, dry_run=a.dry_run, outdir=a.outdir)
    # E47380ade: S_ENTRY -> LibraryActivity.<init>
    # MAIN / LAUNCHER intent starts LibraryActivity.
    r.launch("ch.blinkenlights.android.vanilla/.LibraryActivity",
             "E47380ade")
    # E29472d10: LibraryActivity.<init> -> onResume@LibraryActivity.
    # Activity lifecycle callback; no user action.
    r.comment("lifecycle: onResume runs on launch", "E29472d10")
    # E80427a98: onResume@LibraryActivity -> S_LIBRARY.
    # LibraryActivity is resumed and shown (default tab Artists).
    # The Play all header row proves the library screen is shown.
    r.wait_for("E80427a98", text="Play all", timeout=30)
    # E54b8ef2f: S_LIBRARY -> LibraryPagerAdapter.onItemClick.
    # Tap the play-all header row at the top of the list. The header
    # text is R.string.play_all ("Play all"); the header row itself
    # carries no resource id (inflated draggable_row via addHeaderView).
    r.tap("E54b8ef2f", text="Play all")
    # E87e2a8b0: onItemClick -> onItemClicked@HDR (header row branch).
    r.comment("header branch: onItemClicked(createHeaderIntent(view))",
              "E87e2a8b0")
    # Ecc4f5b3c: onItemClicked@HDR -> pickSongs (row cannot expand).
    r.comment("direct call: header row is played via pickSongs",
              "Ecc4f5b3c")
    # Ee6ca0a88: pickSongs -> PlaybackService.addSongs. Direct call.
    r.comment("direct call: pickSongs hands the songs to the service",
              "Ee6ca0a88")
    # E285c0ada: addSongs -> handleMessage@MSG_QUERY. Message branch.
    r.comment("message dispatch: MSG_QUERY branch runs", "E285c0ada")
    # E651af531: handleMessage@MSG_QUERY -> runQuery. Call in branch.
    r.comment("call made in the message branch", "E651af531")
    # E22acec54: runQuery -> SongTimeline.addSongs. Direct call.
    r.comment("direct call: runQuery adds the songs to the timeline",
              "E22acec54")
    # E99e07df4: addSongs -> MediaUtils.getCursorForFileQuery. Direct call.
    r.comment("direct call: timeline query reads the file cursor",
              "E99e07df4")
    r.done()


if __name__ == "__main__":
    main()
