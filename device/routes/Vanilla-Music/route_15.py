"""Vanilla-Music route_15: AudioSearchActivity.onSearchCompleted.

Edge ids (ROUTES.csv, in order):
  E88dba2a9 Ead834c23 E43c53a39 E1aa732d6 E35daf840

Printed route source:
  verification.csv path row (AudioSearchActivity.onSearchCompleted):
  "Steps read: MEDIA_PLAY_FROM_SEARCH (ENV other_app) -> onCreate ->
  mWorker.execute(query) (ENV permission) -> doInBackground ->
  onPostExecute (standard AsyncTask postResult dispatch) ->
  onSearchCompleted (access$100 bridge, consistent with a private
  method)."
  ROUTES.csv row: source "AndroidManifest.xml:237-244;
  AudioSearchActivity.java:40-57,70-94,92", env other_app;permission.
Permissions (ROUTES.csv): android.permission.READ_EXTERNAL_STORAGE,
  android.permission.WRITE_EXTERNAL_STORAGE (granted here before the
  intent; run_app.sh also grants the ROUTES.csv set during setup).
  API caveat (ROUTES_NOTES.md ambiguity 1): the graph's permission
  prose is framed for API 27; on API 30+ / 33+ the needed set differs
  (media permissions), but both CSV permissions are declared in the
  manifest, so granting them here is safe on any image.
Fixtures: none (STATE file gates: none).
Setup (run_app.sh, before this script): push fixtures/Music + media scan.

Intent details (read from AudioSearchActivity.java:40-57):
  - The action must be android.media.action.MEDIA_PLAY_FROM_SEARCH
    (MediaStore.INTENT_ACTION_MEDIA_PLAY_FROM_SEARCH); any other
    action makes onCreate finish immediately.
  - onCreate reads intent.getExtras().getString(SearchManager.QUERY),
    so the intent MUST carry the "query" string extra -- a missing
    extras bundle would crash on getExtras(). The query text used
    here is "Morning Light" (the ID3 title of fixture 01 Morning
    Light.mp3, verified with ffprobe). The target runs regardless of
    whether the query matches a song: onPostExecute always calls
    onSearchCompleted, and onSearchCompleted only finishes the
    activity, so an empty result does not block the target.
  - No component is set: the activity is exported with exactly this
    intent filter (AndroidManifest.xml:237-244), so filter dispatch
    from adb is the other-app stand-in (ROUTES_NOTES.md ambiguity 4).
  - onSearchCompleted finishes the activity, so there is no
    post-target UI to wait for or screenshot meaningfully; the final
    block is a comment, and coverage (run_app.sh's JaCoCo dump) is
    the evidence for this route.

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

EDGE_IDS = [
    "E88dba2a9", "Ead834c23", "E43c53a39", "E1aa732d6", "E35daf840",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    args = ap.parse_args()

    r = Runner(package=args.package, route="route_15", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)

    # E88dba2a9 -- ENTRY: another app sends MEDIA_PLAY_FROM_SEARCH.
    # Storage is granted first so the permission check in onCreate
    # passes, then the search intent is sent from adb (the other-app
    # stand-in) with the required "query" extra.
    r.grant("android.permission.READ_EXTERNAL_STORAGE", "E88dba2a9")
    r.grant("android.permission.WRITE_EXTERNAL_STORAGE", "E88dba2a9")
    r.start_intent("E88dba2a9",
                   action="android.media.action.MEDIA_PLAY_FROM_SEARCH",
                   extras={"query": "Morning Light"})

    # Ead834c23 -- LIFECYCLE: Activity lifecycle callback (onCreate).
    # No user action; the intent above drives it.
    r.comment("lifecycle onCreate, no user action", "Ead834c23")

    # E43c53a39 -- ASYNC: mWorker.execute(query): the task runs
    # doInBackground on a pool thread. Guards (action is
    # MEDIA_PLAY_FROM_SEARCH, permission check passed) are satisfied
    # by the intent and grants above; dispatch only.
    r.comment("worker execute dispatch, guards satisfied", "E43c53a39")

    # E1aa732d6 -- ASYNC: the result is delivered on the main thread
    # (onPostExecute). Standard AsyncTask dispatch; no user action.
    r.comment("onPostExecute dispatch, no user action", "E1aa732d6")

    # E35daf840 -- CALL: onPostExecute -> onSearchCompleted (through
    # access$100). This is the target method; it finishes the
    # activity, so there is no post-target UI to capture (see
    # docstring). Dispatch only.
    r.comment("onSearchCompleted dispatch from onPostExecute, target",
              "E35daf840")

    r.done()


if __name__ == "__main__":
    main()
