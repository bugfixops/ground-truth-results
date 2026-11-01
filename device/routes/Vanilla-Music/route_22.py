"""Route route_22: MediaScanner$MediaScanPlan.clear.

Printed route source: graphs/Vanilla-Music/verification.csv path row
"MediaScanner$MediaScanPlan.clear" ("Steps read: tap the bottom-bar
overflow -> popup menu -> Settings -> tap "Media library" header ->
tap "Cancel" (scan running) -> cancelButtonPressed ->
MediaLibrary.abortLibraryScan -> MediaScanner.abortScan ->
MediaScanPlan.clear") and device/routes/Vanilla-Music/ROUTES.csv row
route_22 (source: BottomBarControls.java:157-181,106-111,198-203,
157-158,120-123; PlaybackActivity.java:403,408-424;
PreferencesMediaLibrary.java:191-207,197,377; MediaLibrary.java:279;
MediaScanner.java:162).

Edge ids, in order:
  E47380ade, E29472d10, E80427a98, E65584de0, E95b25aef, E38459d6f,
  Ef8b94848, Eb3a597bc, E46a6b4b8, E700804fd, Ef4c93f9d, Eb42d7ef6,
  Ed506425b, E56f48812, E54524c93, Eb931f7eb, E3c4009a2, Eb0a54342,
  E4b539f85.

Permissions: none (ROUTES.csv permissions cell is empty).
Fixtures: none (STATE file gates: none).
Setup (done by run_app.sh before this script): push fixtures/Music +
media scan. This script therefore starts by launching the app.

Ordering scripted (timing-sensitive): on the Media library settings
screen this script taps "Start scan" FIRST to start a fresh scan, and
then taps "Cancel" immediately, while that scan is running, so the
cancel path aborts a live scan and clears the plan. The setup scan
has already finished before this script runs, so cancelling without
starting a fresh scan first would not exercise the abort path.

UI facts used (read from layout XML / strings / handler source,
never invented):
- The overflow button is built in code (BottomBarControls.java:156,
  getImageButton): a programmatic ImageButton with no res id, no
  text, and no content-description, so it is tapped by fixed
  coordinates (see the why string on that tap).
- The overflow menu entry is "Settings"
  (res/values/translatable.xml settings; PlaybackActivity.java:403
  adds MENU_PREFS with R.string.settings).
- The settings header is "Media library"
  (res/xml/preference_headers.xml title @string/media_library;
  res/values/translatable.xml media_library).
- The scan buttons are "Start scan" and "Cancel"
  (res/layout/medialibrary_preferences.xml start_button /
  cancel_button; res/values/translatable.xml media_scan_start /
  cancel).
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

    r = Runner(package=args.package, route="route_22", edge_ids=[
        "E47380ade", "E29472d10", "E80427a98", "E65584de0", "E95b25aef",
        "E38459d6f", "Ef8b94848", "Eb3a597bc", "E46a6b4b8", "E700804fd",
        "Ef4c93f9d", "Eb42d7ef6", "Ed506425b", "E56f48812", "E54524c93",
        "Eb931f7eb", "E3c4009a2", "Eb0a54342", "E4b539f85",
    ], log_path=args.log, dry_run=args.dry_run, outdir=args.outdir)

    # E47380ade -- MAIN / LAUNCHER intent starts LibraryActivity.
    r.launch(args.package + "/.LibraryActivity", "E47380ade")

    # E29472d10 -- Activity lifecycle callback (onResume).
    # No user action: the framework resumes the activity after launch.
    r.comment("lifecycle-onResume-no-user-action", "E29472d10")

    # E80427a98 -- LibraryActivity is resumed and shown (default tab
    # Artists: library_page = 0). Wait for the tab title so the
    # library screen (with its bottom bar) is on screen.
    r.wait_for("E80427a98", text="Artists")

    # E65584de0 -- Tap the overflow (three dots) button at the right
    # end of the bottom bar.
    # Fixed coordinates because no id/text/desc exists: the button is
    # a programmatic ImageButton (BottomBarControls.getImageButton,
    # no setContentDescription, no android:id). Geometry for the
    # replay image (Pixel 2, 1080x1920, density 2.625): the button is
    # 36dp wide at the right end with a 4dp spacer (menuMargin() is
    # true), so its centre is about x = 1080 - 11 - 47 = 1022; the
    # bottom-bar row is 56sp tall at the bottom of the screen, so
    # its centre is about y = 1920 - 73 = 1847. Confirm from a live
    # UI dump on the replay image and adjust if the profile differs.
    r.tap("E65584de0", x=1021, y=1847,
          why="overflow button is a programmatic ImageButton with no "
              "res id, text, or content-desc (BottomBarControls.java "
              "getImageButton); Pixel 2 1080x1920 geometry, see header")

    # E95b25aef -- call made in the click branch: onClick@POPUP ->
    # openMenu. Follows automatically from the overflow tap.
    r.comment("openMenu-follows-overflow-tap", "E95b25aef")

    # E38459d6f -- mPopupMenu.show(): the overflow menu is open.
    # Wait for the Settings entry so the menu is on screen.
    r.wait_for("E38459d6f", text="Settings")

    # Ef8b94848 -- Tap an entry of the overflow menu (the Settings
    # entry, guard item id == MENU_PREFS on the next edge).
    r.tap("Ef8b94848", text="Settings")

    # Eb3a597bc -- the item MENU_PREFS of the overflow menu was
    # tapped -> onOptionsItemSelected@PREFS. Follows from the tap.
    r.comment("MENU_PREFS-branch-follows-tap", "Eb3a597bc")

    # E46a6b4b8 -- startActivity(new Intent(this,
    # PreferencesActivity.class)). Follows from the menu selection.
    r.comment("intent-to-PreferencesActivity-no-user-action", "E46a6b4b8")

    # E700804fd -- Activity lifecycle callback (PreferencesActivity
    # onCreate). No user action.
    r.comment("lifecycle-onCreate-no-user-action", "E700804fd")

    # Ef4c93f9d -- the list of settings headers is shown. Wait for
    # the Media library header so the headers list is on screen.
    r.wait_for("Ef4c93f9d", text="Media library")

    # Eb42d7ef6 -- Tap the "Media library" header.
    r.tap("Eb42d7ef6", text="Media library")

    # Ed506425b -- Fragment lifecycle callback
    # (PreferencesMediaLibrary onViewCreated). No user action.
    r.comment("lifecycle-onViewCreated-no-user-action", "Ed506425b")

    # E56f48812 -- the scan controls and statistics are shown. Wait
    # for the Start scan button so the controls are on screen.
    r.wait_for("E56f48812", text="Start scan")

    # E54524c93 -- Tap "Start", "Cancel", "Edit" or a checkbox.
    # ORDERING (timing-sensitive): tap "Start scan" first to start a
    # fresh scan, then tap "Cancel" immediately, while that scan is
    # still running. Both taps belong to this one onClick edge: the
    # first starts the scan, the second is the cancel that the rest
    # of the route follows. The harness has no sleep primitive, so
    # the two taps are issued back-to-back; on the live run the
    # scan must still be running when Cancel lands (see REPORT.md).
    r.tap("E54524c93", text="Start scan")
    r.tap("E54524c93", text="Cancel")

    # Eb931f7eb -- Direct call: onClick -> cancelButtonPressed.
    r.comment("direct-call-no-user-action", "Eb931f7eb")

    # E3c4009a2 -- Direct call: cancelButtonPressed ->
    # MediaLibrary.abortLibraryScan.
    r.comment("direct-call-no-user-action", "E3c4009a2")

    # Eb0a54342 -- Direct call: abortLibraryScan -> abortScan.
    r.comment("direct-call-no-user-action", "Eb0a54342")

    # E4b539f85 -- Direct call: abortScan -> MediaScanPlan.clear
    # (target).
    r.comment("direct-call-target-reached", "E4b539f85")

    r.done()


if __name__ == "__main__":
    main()
