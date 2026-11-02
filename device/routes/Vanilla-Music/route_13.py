"""Vanilla-Music route_13: AudioPickerActivity$AudioPickerWorker
.getCursorForAnyContent.

Edge ids (ROUTES.csv, in order):
  E1d7b888a Eeed2d31a E05fcb9f9 E733ad1b8 E71822e10

Printed route source:
  verification.csv path row (AudioPickerActivity$AudioPickerWorker
  .getCursorForAnyContent): "Steps read: ACTION_VIEW with an audio
  URI (ENV other_app) -> onCreate -> mWorker.execute(uri) (ENV
  permission: the storage check passed, intent has a URI) ->
  doInBackground -> getSongForUri -> getCursorForAnyContent.
  AsyncTask.execute -> doInBackground is the standard AsyncTask
  dispatch (FW-SRC AsyncTask.java cited)."
  ROUTES.csv row: source "AndroidManifest.xml:211-235;
  AudioPickerActivity.java:93,114,187-191,190,211", env
  other_app;permission.
Permissions (ROUTES.csv): android.permission.READ_EXTERNAL_STORAGE,
  android.permission.WRITE_EXTERNAL_STORAGE (granted here before the
  intent; run_app.sh also grants the ROUTES.csv set during setup).
  API caveat (ROUTES_NOTES.md ambiguity 1): the graph's permission
  prose is framed for API 27; on API 30+ / 33+ the needed set differs
  (media permissions), but both CSV permissions are declared in the
  manifest, so granting them here is safe on any image.
Fixtures: none (STATE file gates: none).
Setup (run_app.sh, before this script): push fixtures/Music + media scan.

URI choice, stated with why: getSongForUri (AudioPickerActivity.java)
  routes by scheme and host -- scheme "file" goes to
  getCursorForFileQuery, scheme "content" with host "media" goes to
  getCursorForMediaContent, and only scheme "content" with a NON-media
  host reaches getCursorForAnyContent. A file:// URI for a setup-pushed
  track would therefore NOT reach this route's target method, and a
  MediaStore content://media/... URI would not either. This script
  sends the setup-pushed track through the external-storage documents
  provider (host com.android.externalstorage.documents, document id
  primary:Music/01 Morning Light.mp3), which is a content:// non-media
  URI whose stream the provider serves from /sdcard/Music. If the
  replay image's documents provider rejects that exact document-id
  form, run_app must substitute any other content:// non-media URI
  that opens the same file (for example one issued by a file-manager
  provider on the image); the file:// and content://media forms are
  NOT substitutes for this route.
  The intent names AudioPickerActivity explicitly as its component:
  without it, a chooser could appear if another app on the image also
  handles audio VIEW intents, and the route path is identical either
  way (the activity is exported with the matching intent filter,
  AndroidManifest.xml:211-235).
  The activity may finish after the worker runs if the cached copy
  cannot be resolved to a media row; that does not block the target,
  which runs inside doInBackground before resolution completes. So
  the final block records a screenshot and dump instead of asserting
  a resolved song title.

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

PKG = "ch.blinkenlights.android.vanilla"
PICKER_ACTIVITY = (
    "ch.blinkenlights.android.vanilla/"
    "ch.blinkenlights.android.vanilla.AudioPickerActivity"
)
# Setup-pushed track, via the external-storage documents provider:
# content://, host != "media", so getSongForUri takes the
# getCursorForAnyContent branch. See the docstring for the fallback.
AUDIO_URI = (
    "content://com.android.externalstorage.documents/document/"
    "primary%3AMusic%2F01%20Morning%20Light.mp3"
)
EDGE_IDS = [
    "E1d7b888a", "Eeed2d31a", "E05fcb9f9", "E733ad1b8", "E71822e10",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    args = ap.parse_args()

    r = Runner(package=args.package, route="route_13", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)

    # E1d7b888a -- ENTRY: another app opens an audio file with
    # ACTION_VIEW (file:// or content:// data). Storage is granted
    # first so the permission check in onCreate passes, then the
    # ACTION_VIEW intent is sent from adb (the other-app stand-in).
    r.grant("android.permission.READ_EXTERNAL_STORAGE", "E1d7b888a")
    r.grant("android.permission.WRITE_EXTERNAL_STORAGE", "E1d7b888a")
    r.start_intent("E1d7b888a", action="android.intent.action.VIEW",
                   data=AUDIO_URI, mime="audio/*",
                   component=PICKER_ACTIVITY)

    # Eeed2d31a -- LIFECYCLE: Activity lifecycle callback (onCreate).
    # No user action; the intent above drives it.
    r.comment("lifecycle onCreate, no user action", "Eeed2d31a")

    # E05fcb9f9 -- ASYNC: mWorker.execute(uri): the task runs
    # doInBackground on a pool thread. Guard (permission check passed,
    # intent has a URI) is satisfied by the grants and the intent
    # above; dispatch only.
    r.comment("worker execute dispatch, guard satisfied", "E05fcb9f9")

    # E733ad1b8 -- CALL: doInBackground -> getSongForUri. Direct call;
    # no user action.
    r.comment("getSongForUri dispatch, no user action", "E733ad1b8")

    # E71822e10 -- CALL: getSongForUri -> getCursorForAnyContent
    # (content:// URI, non-media host). This is the target method; it
    # runs inside doInBackground, so evidence is a screenshot/dump
    # rather than a resolved-song assertion (see docstring).
    r.screenshot("route_13_done", "E71822e10")
    r.dump_ui("route_13_done", "E71822e10")

    r.done()


if __name__ == "__main__":
    main()
