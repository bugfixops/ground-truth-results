"""Vanilla-Music route_17: MediaButtonReceiver.runAction.

Edge ids (ROUTES.csv, in order):
  E53636d07 Ee2ad9348 Ee19ae084 Ecbc1cc7a

Printed route source:
  verification.csv path row (MediaButtonReceiver.runAction): "Steps
  read: ACTION_MEDIA_BUTTON (ENV hardware/system_event) -> onReceive
  -> processKey -> runAction. Manifest receiver instantiation +
  onReceive dispatch is standard (FW-SRC ActivityThread cited)."
  ROUTES.csv row: source "AndroidManifest.xml:165-170;
  MediaButtonReceiver.java:176,109", env hardware;system_event.
Permissions: none. Fixtures: none (STATE file gates: none).
Setup (run_app.sh, before this script): push fixtures/Music + media scan.

Delivery choice (stated, with why): the media-button event is delivered
  with `input keyevent` (harness key()), NOT with a direct broadcast to
  the receiver component. The direct-broadcast fallback was considered
  and rejected as the primary: MediaButtonReceiver is exported with an
  ACTION_MEDIA_BUTTON intent-filter (AndroidManifest.xml:165-170), so a
  broadcast would reach onReceive, but onReceive passes
  intent.getParcelableExtra(Intent.EXTRA_KEY_EVENT) to processKey, and
  processKey returns false immediately when the event is null
  (MediaButtonReceiver.java: processKey null check). `am broadcast`
  through the harness can only attach string extras, never a Parcelable
  KeyEvent, so a shell broadcast can never carry the KeyEvent that
  runAction requires. Only a real media key produces a system
  ACTION_MEDIA_BUTTON broadcast carrying a real KeyEvent.
  Fallback if the emulator's media-session routing swallows the key
  event: try the other media keys the receiver handles (KEYCODE_MEDIA_
  NEXT, then KEYCODE_MEDIA_PLAY) and confirm on the replay image which
  one fires runAction (ROUTES_NOTES.md ambiguity 3); there is no
  harness action that can fabricate a KeyEvent extra.
  The app is launched first so PlaybackService / the media session
  exists for the system to route the key event to; the receiver itself
  is manifest-registered and needs no headset or Bluetooth hardware.

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
EDGE_IDS = ["E53636d07", "Ee2ad9348", "Ee19ae084", "Ecbc1cc7a"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    args = ap.parse_args()

    r = Runner(package=args.package, route="route_17", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)

    # E53636d07 -- ENTRY: the system delivers ACTION_MEDIA_BUTTON to
    # the exported receiver (gui: "Press the headset / media button").
    # Launch first so the app's PlaybackService / media session exists
    # for routing, then deliver a real media key: KEYCODE_MEDIA_
    # PLAY_PAUSE with ACTION_DOWN maps in processKey to
    # PlaybackService.ACTION_TOGGLE_PLAYBACK and hence to runAction.
    # No headset hardware is needed: input keyevent is the adb
    # substitute for the headset button.
    r.launch(PACKAGE_ACTIVITY, "E53636d07")
    r.key("KEYCODE_MEDIA_PLAY_PAUSE", "E53636d07")

    # Ee2ad9348 -- LIFECYCLE: BroadcastReceiver.onReceive is called
    # with the intent. System dispatch of the broadcast; no user action.
    r.comment("onReceive dispatch of the media-button broadcast, "
              "no user action", "Ee2ad9348")

    # Ee19ae084 -- CALL: onReceive -> processKey (direct call).
    # The KeyEvent carried by the system broadcast is non-null with
    # ACTION_DOWN, so processKey handles it instead of returning false.
    r.comment("processKey dispatch, no user action", "Ee19ae084")

    # Ecbc1cc7a -- CALL: processKey -> runAction (the target).
    # runAction starts PlaybackService with the action; the dump below
    # is the evidence step (no UI of its own is produced by runAction).
    r.dump_ui("route_17_after_media_key", "Ecbc1cc7a")
    r.screenshot("route_17_after_media_key", "Ecbc1cc7a")

    r.done()


if __name__ == "__main__":
    main()
