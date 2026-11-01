"""Vanilla-Music route_14: MiniPlaybackActivity.onClick.

Edge ids (ROUTES.csv, in order):
  E47380ade E3aea4024 E8ee3f512 E8e6e45c2 Ea1ca8276 E752a94e4
  Ed925da4c E1b290ff6 Eeba89555 Efd552d40

Printed route source:
  verification.csv path row (MiniPlaybackActivity.onClick): "Steps
  read: PlaybackService.onCreate -> createNotificationAction (ENV:
  notification tapped, STATE: notification action = "open mini
  popup") -> PendingIntent.getActivity(MiniPlaybackActivity) ->
  onResume@MiniPlaybackActivity (the fixed variant, distinct from
  onResume@AudioPickerActivity) -> S_MINI -> tap the cover -> onClick."
  ROUTES.csv row: source "PlaybackService.java:475,2086-2089;
  MiniPlaybackActivity.java:37-51,47-48,54-58", env other_app,
  state settings.
Permissions: none (ROUTES.csv). Fixtures: none (STATE file gates: none).
Setup (run_app.sh, before this script): push fixtures/Music + media scan.

Settings path (read from source, never invented):
  - Settings opens PreferencesActivity (PlaybackActivity.java:412,
    MENU_PREFS, R.string.settings = "Settings"). The bottom-bar
    overflow button that also opens it is built programmatically in
    BottomBarControls.enableOptionsMenu and has no id, text, or
    content-desc in res/layout/bottombar_controls.xml, so this script
    opens PreferencesActivity by direct component launch instead of
    guessing fixed coordinates for the overflow button.
  - Preference headers (res/xml/preference_headers.xml): "Notifications"
    (R.string.notifications) opens the NotificationsFragment.
  - Notifications screen (res/xml/preference_notifications.xml):
    "Notification action" (R.string.notification_action_title) with
    entries "Open library (default)", "Open mini popup",
    "Open full player", ... (R.string.open_mini_popup = "Open mini
    popup", the non-default value this route needs).
  - PlaybackService re-reads the preference live: onSharedPreference
    changed (PlaybackService.java:873-875) calls createNotificationAction
    + updateNotification, so changing the setting after the service
    has started still rebuilds the notification action before the
    notification is tapped.
  - API 33+ caveat (ROUTES_NOTES.md): no route edge names
    POST_NOTIFICATIONS, so it is not granted here, but on API 33+
    images setup must grant it or no notification exists to tap.
  - Song row "Morning Light": fixture 01 Morning Light.mp3, ID3 title
    "Morning Light" (verified with ffprobe on the setup fixtures).
    Tapping the song row on the Tracks tab plays it, which creates
    the playback notification.
  - Mini playback cover res_id "cover_view"
    (res/layout/mini_playback.xml); MiniPlaybackActivity.onClick
    handles R.id.cover_view by opening FullPlaybackActivity.

Notification-shade step (Ed925da4c), stated with what was used:
  - The harness has no swipe-down or raw-shell action, so the shade
    is pulled with key navigation: harness key() sending
    KEYCODE_NOTIFICATION (a real Android KeyEvent constant), which is
    the key/menu-navigation route the task allows when no harness
    action covers the shade. Whether the replay image maps that key
    to shade expansion is UNVERIFIED on a device -- if it does not,
    run_app must pull the shade with
      adb shell cmd statusbar expand-notifications
    (a raw-shell command the harness cannot issue) and then tap the
    notification card. The tap target used here is the notification
    card's app-name text "Vanilla Music" (R.string.app_name): on AOSP
    the app-name label sits inside the notification card, so tapping
    its centre lands on the card and fires the card's content intent
    (the mini-popup PendingIntent). If the replay image's shade
    renders the app name outside the tappable card, tap the card body
    instead.

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
PREFS_ACTIVITY = (
    "ch.blinkenlights.android.vanilla/"
    "ch.blinkenlights.android.vanilla.PreferencesActivity"
)
EDGE_IDS = [
    "E47380ade", "E3aea4024", "E8ee3f512", "E8e6e45c2", "Ea1ca8276",
    "E752a94e4", "Ed925da4c", "E1b290ff6", "Eeba89555", "Efd552d40",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    r = Runner(package=args.package, route="route_14", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, outdir=args.outdir)

    # E47380ade -- ENTRY: MAIN / LAUNCHER intent starts LibraryActivity.
    # run_app.sh does pm clear and the setup step before this script.
    r.launch(PACKAGE_ACTIVITY, "E47380ade")

    # E3aea4024 -- LIFECYCLE: Activity lifecycle callback (onStart).
    # No user action; the launch above drives it.
    r.comment("lifecycle onStart, no user action", "E3aea4024")

    # E8ee3f512 -- CALL: LibraryActivity.onStart -> PlaybackActivity
    # .onStart. Direct call; no user action.
    r.comment("onStart dispatch, no user action", "E8ee3f512")

    # E8e6e45c2 -- INTENT: startService(PlaybackService), guard
    # PlaybackService.hasInstance() is false. Fired by onStart; no
    # user action.
    r.comment("startService fired by onStart, no user action", "E8e6e45c2")

    # Ea1ca8276 -- LIFECYCLE: the system creates the service and calls
    # onCreate. No user action.
    r.comment("service onCreate, no user action", "Ea1ca8276")

    # E752a94e4 -- CALL: PlaybackService.onCreate ->
    # PlaybackService.createNotificationAction. The action value comes
    # from the notification_action preference, so this block sets it
    # first (Settings > Notifications > Notification action >
    # "Open mini popup", the non-default value), then plays a song so
    # the notification exists. The preference change rebuilds the
    # notification action live (PlaybackService onSharedPreference
    # changed). Two backs: NotificationsFragment -> headers list ->
    # LibraryActivity.
    r.launch(PREFS_ACTIVITY, "E752a94e4")
    r.wait_for("E752a94e4", text="Notifications")
    r.tap("E752a94e4", text="Notifications")
    r.wait_for("E752a94e4", text="Notification action")
    r.tap("E752a94e4", text="Notification action")
    r.tap("E752a94e4", text="Open mini popup")
    r.back("E752a94e4")
    r.back("E752a94e4")
    r.tap("E752a94e4", text="Tracks")
    r.wait_for("E752a94e4", text="Morning Light")
    r.tap("E752a94e4", text="Morning Light")

    # Ed925da4c -- INTENT: notification action "open mini popup":
    # PendingIntent.getActivity(MiniPlaybackActivity). ENV: the user
    # taps a button of the playback notification (the notification
    # shade fires the PendingIntent). STATE: notification action set
    # to "open mini popup" (done in the block above). Shade pull uses
    # key navigation (KEYCODE_NOTIFICATION) because the harness has
    # no swipe-down or raw-shell action; see the docstring for the
    # unverified-mapping caveat and the statusbar fallback. The tap
    # lands on the Vanilla Music notification card in the shade.
    r.key("KEYCODE_NOTIFICATION", "Ed925da4c")
    r.tap("Ed925da4c", text="Vanilla Music")

    # E1b290ff6 -- LIFECYCLE: Activity lifecycle callback (onResume
    # @MiniPlaybackActivity, the fixed variant). No user action; the
    # PendingIntent above drives it.
    r.comment("lifecycle onResume mini variant, no user action",
              "E1b290ff6")

    # Eeba89555 -- ENTERS S_MINI: MiniPlaybackActivity is resumed and
    # shown. The mini layout's cover view proves it.
    r.wait_for("Eeba89555", res_id="cover_view")

    # Efd552d40 -- GUI: tap the cover (the CoverView calls
    # performClick). This is the target method (MiniPlaybackActivity
    # .onClick for R.id.cover_view).
    r.tap("Efd552d40", res_id="cover_view")
    r.screenshot("route_14_done", "Efd552d40")

    r.done()


if __name__ == "__main__":
    main()
