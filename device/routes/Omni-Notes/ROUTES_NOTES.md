# Omni-Notes — ROUTES notes (D1)

Scope: one row per `path` row in `graphs/Omni-Notes/verification.csv`, in that
file's order (33 rows: 3 correct, 29 fixed, 1 wrong). `env_kinds` /
`state_kinds` are copied from `graphs/Omni-Notes/out/methods.csv` for each
method. Every method, edge list, and source below comes from those two files,
checked against `graphs/Omni-Notes/out/omni-notes_trigger_graph.json`.
Drycheck (`device/drycheck.py`, device lead's staged tool) on this file with no
scripts present: the 2 unscriptable rows PASS; the 31 scripted rows fail ONLY
with "missing script" — every edge chain is contiguous from S_ENTRY to its
method, every method exists in methods.csv, every permission is declared, every
fixture exists. Route_01 dry-runs clean (see below).

## Permissions: only location and storage, mapped from gate texts

Manifest `final_java_only/Omni-Notes/app/Omni-Notes-#745/omniNotes/src/main/AndroidManifest.xml`
declares, among others, `ACCESS_FINE_LOCATION`, `ACCESS_COARSE_LOCATION`,
`READ_EXTERNAL_STORAGE`, `WRITE_EXTERNAL_STORAGE` (all dangerous runtime
permissions; INTERNET, ACCESS_NETWORK_STATE, RECEIVE_BOOT_COMPLETED, VIBRATE,
WAKE_LOCK, RECORD_AUDIO are also declared but no route gates on them).
Gate text "the location permission is granted" maps to
`ACCESS_FINE_LOCATION;ACCESS_COARSE_LOCATION` (both location permissions; the
app declares both and SmartLocation may use either provider). Gate text "the
storage permission is granted" maps to
`READ_EXTERNAL_STORAGE;WRITE_EXTERNAL_STORAGE`. run_app.sh grants ROUTES.csv
permissions before each script runs, so scripts must NOT call grant().

Permission rows: route_01, route_04 (location); route_06, route_08, route_14
(storage). All other rows: empty (nothing omitted — no other route has an ENV
permission gate in methods.csv).

## Fixtures: one zip, for the three Springpad/picker routes

`$WEMU/fixtures/Download/archive.zip` (a zip archive) is the stand-in Springpad
export zip for routes 02, 03, 31 (STATE file: "A Springpad export zip is
available to pick"). run_app.sh pushes it to `/sdcard/Download/archive.zip`;
the script picks it in the system document picker by tapping its name. No other
route lists a fixture: STATE file gates for the backup routes (06, 14) name a
folder, not a file (see below), and all other STATE kinds are created through
the app UI (a note, a tag, a category, a trashed note, a reminder), not by
pushing a file.

## Setup: app-level value on every row

`setup` is `push fixtures/Pictures` on all 33 rows: the app-level first-run
setup from `ci/apps.csv` for Omni-Notes (its setup column). run_app.sh reads
the column but does not execute it; a per-app `setup.py` is not shipped, so
the value is a note, following the Currency precedent of a constant setup
value. The Pictures fixtures exist under `$WEMU/fixtures/Pictures/`
(photo_1.jpg to photo_6.jpg) for attachment flows that need a picture.

## Status: 31 scripted, 2 unscriptable (6.06%, within the 10% cap)

Unscriptable rows (no script; drycheck passes them on the non-empty reason):
Converted route (formerly unscriptable, now scripted):
- route_12 `IdeogramsWordCounter.<init>`: converted to scripted by the new
  harness primitive set_locale() plus the fresh launch run_app.sh already
  provides. The converted script sets the system locale to ja_JP before
  launch (so CountFactory takes the ideogram branch) and restores the locale
  to en-US after (locale restored to en-US after the run, since the system
  locale is global and pm clear does not reset it). Live-run uncertainty if
  the CI image lacks ja-JP: unclear, never wrong.
- route_13 `TextHelper.getAlternativeTitle`: needs the DashClock or Pushbullet
  host app installed and calling the extension; neither host app is available
  on the AOSP emulator.
- route_17 `UpgradeProcessor.<init>`: needs an older-version database on disk
  (install an old build with data, then update); no old-version database
  fixture exists in `$WEMU/fixtures`.

Special scripted rows (read before writing these scripts):
- route_05 `DbHelper.deleteNote(long,boolean)` (route-table verdict wrong):
  the script implements the best route as printed (FAB-created editor flow),
  NOT the real Merge path. The Merge STATE cannot hold on a FAB editor, so
  the expected device outcome is reached=no with script_status=ok — an honest
  device result for a wrong route, not a label contradiction (the label is
  REACHABLE via Merge; the device run tests the route, not the label).
- route_15 `DetailFragment.removeAttachment(Attachment)` (method UNREACHABLE,
  empty edge list, path row kept for the first-graph error record): the script
  launches the app and finishes (no edges to implement). Expected outcome:
  reached=no, script_status=ok — the run empirically confirms non-reachability.
- route_06, route_14 (backup folder under `/sdcard/Omni Notes`): no fixture
  creates that folder (run_app.sh pushes fixtures only to `/sdcard/<path>`),
  so the script creates it through the app: run an export first (which
  creates the folder and a backup), then the import/delete flow.
- route_16 `BitmapHelper.getImageBitmap` (ENV time): set a reminder a minute
  ahead, wait for the alarm notification (long wait_for timeout, inside the
  10-minute script budget), tap it.
- route_02, route_03, route_31 (picker): the fixture zip is already on the
  device at `/sdcard/Download/archive.zip`; the script drives the import UI
  and picks `archive.zip` in the system picker.

## Scripts and the harness

Scripts live next to this file as `route_NN.py` and follow the
`route_01.py` template (header docstring with method, edge ids, printed route
file, permissions, fixtures, setup; one block per edge in route order;
lifecycle/framework edges get `comment`, not an action). The harness is the
device lead's staged `device/harness/harness.py` (Runner API: launch, tap,
long_tap, type_text, key, back, scroll_to, wait_for, start_intent, broadcast,
grant, deny, push_fixture, screenshot, dump_ui, assert_text, comment, done;
scripts take `--package --log --outdir --dry-run` or `--adb`). Scripts import
it via the repo-root-relative path trick in the template (three levels up from
`device/routes/<App>/route_NN.py`); they must NOT call grant() or pm clear
(run_app.sh does both). Selectors come from layout/menu/strings XML under
`final_java_only/Omni-Notes/app/Omni-Notes-#745/omniNotes/src/main/res/` and
the printed handler source; fixed coordinates only with a why string.
Route_01 dry-run proof (2026-11-01): exit 0, 26 log lines (launch + 3 taps +
22 comments), drycheck route_01 PASS with --load-scripts.

## Fixture additions at D3 merge time (merger's own decisions, 2026-11-01)

- route_06 fixtures now include `Pictures/photo_1.jpg`: the imported note JSON
  needs an attachments array for `Attachment.<init>(BaseAttachment)` to run
  during import, so the script first creates a note with a photo attachment
  and exports it, then imports. Without a real attachment the import path
  would not reach the target.
- route_16 fixtures now include `Pictures/photo_1.jpg`: an untouched sketch is
  dropped silently by `SketchFragment.save()` (bitmap null), so no image
  attachment exists and `BitmapHelper.getImageBitmap` is not reached. The
  script instead attaches a photo, giving a real image attachment.

## Unresolved flags carried verbatim (not fixed in D1)

These flags are carried forward unresolved; D1 does not fix them:
- route_05 wrong-chain question (Merge-state no-op; expected reached=no)
- route_06 attachment caveat (fresh-database export has no attachments array; photo fixture does not close it; expected reached=no unless a note-with-attachment creation step is added)
- route_08 missing-file precondition (LogDelegate.w only in the FileNotFound catch; needs a harness/file-delete decision; expected reached=no, unclear not wrong)
