## What the re-audit changed (compared with the schema 1 graph)

The schema 1 draft was a generated stub that was never hand-reviewed. The schema 2 graph is written by hand from
the AnyMemo 10.12.2 sources, with each framework hop labelled FW-SRC (Android 8.1.0_r1 lines read) or INFERRED
(androidx, Material, Dagger, ORMLite, RxJava and the like, whose source is not in the set).

This round 2 resolved the last six round-1 placeholder methods to real, source-cited verdicts (all six turned out to
be REACHABLE, so UNREACHABLE fell from 247 to 241 and REACHABLE rose from 1960 to 1966):

- CategoryEditorFragment.onDestroy: the OK button (CategoryEditorFragment$1.onClick) calls dismiss()
  (ui/CategoryEditorFragment.java:108); the dialog is destroyed.
- PreviewEditActivity.onDestroy: restartActivity() calls finish() (ui/PreviewEditActivity.java:462), and Back
  finishes the activity (no onBackPressed override).
- QuizLauncherDialogFragment.onDestroy: the launcher has no dismiss() and no setCancelable(false), so the
  default-cancelable dialog is destroyed when the user cancels it (Back / tap outside).
- CardListActivity.onDestroy: no reachable in-app finish(), so the exit is Back (no onBackPressed override).
- CardEditor.onConfigurationChanged / SettingsScreen.onConfigurationChanged: both classes declare the callback
  (ui/CardEditor.java:415-418, ui/SettingsScreen.java:154-157); a rotation edge models it, like OptionScreen.

Round 2 also confirmed that the ten automatic CALL edges the round-1 fixer had listed as "still dropped" are all
present in the build as @AM / @DBX host-variant edges (the per-host clone copies the base automatic CALLs), so
nothing was added for them.

## How the checked paths were chosen

A fixed 30-method sample was drawn from the 1966 reachable methods with the repository tool and a fixed seed
(`tools/verify_sample.py AnyMemo 30 20261025`), so the draw is reproducible and not cherry-picked. For each sampled
method the best route was read step by step against the printed source (edge trigger, guard, and ENV / STATE gate on
each hop). All 30 routes were correct; none needed a fix. The sample and its routes are in scratch/kiro_sample_30_final.txt,
scratch/kiro_routes_all.txt and scratch/kiro_routes_edges.txt.

## What waits for a device (API 27)

Several routes cross outside the app and can only be exercised on a real API 27 device with the right environment,
not in the `-p <app>` baseline runs:

- The system document picker (ACTION_OPEN_DOCUMENT / _TREE / CREATE_DOCUMENT) used by Open/Export/Converter/Settings
  file fields and by the import flow: the baseline cannot start another package, so onActivityResult only ever sees
  RESULT_CANCELED there; the file-chosen (RESULT_OK) branches need a device.
- The AnyMemo download server (anymemo.org) and Dropbox (OAuth2 in an external browser, api.dropboxapi.com): the
  download and upload routes need network and an account.
- Audio: the microphone (RECORD_AUDIO) for the recorder, and a TTS engine for speak-question.
- Rotation / configuration change for CardEditor.onConfigurationChanged and SettingsScreen.onConfigurationChanged.

## Hazard candidates (from reading the code, not reproduced)

Only items whose source lines were printed during this audit are listed; none was reproduced on a device.

- QuizLauncherDialogFragment never calls dismiss() (no dismiss() anywhere in ui/QuizLauncherDialogFragment.java) and
  the Start-quiz button only startActivity(QuizActivity); the launcher dialog is left to the default cancel path.
  Worth a look that the launcher is dismissed as intended after a quiz starts.
- CardListActivity / PreviewEditActivity expose finish() only inside restartActivity() (ui/CardListActivity.java:162,
  ui/PreviewEditActivity.java:462); CardListActivity.restartActivity is unreachable, so the card list relies entirely
  on Back to exit.

## Limits

The framework side is FW-SRC only for Android 8.1.0_r1 platform classes that were read; androidx, Material
Components, Dagger-generated code, ORMLite and RxJava stay INFERRED (their source is not in the set), so lifecycle,
RecyclerView, loader, dialog, DI and Rx hops are inferred, not line-verified. The route checker flags one route:
FileBrowserFragment$3.<init> (the import branch), reported as edge E078aae8d then Eb8b53150. The printed source
lines show the route is right and the flag is a false positive of the `result` text match, not a real contradiction:

- E078aae8d (onOptionsItemSelected -> onActivityResult): the import menu item starts the system document picker at
  ui/FileBrowserFragment.java:311-316 (itemId == R.id.file_browser_importdb; ACTION_OPEN_DOCUMENT;
  startActivityForResult(intent, REQUEST_CODE_IMPORT_DB)). The edge's ENV text notes that the `-p <app>` baseline
  tool runs cannot start another package, so onActivityResult there only ever gets RESULT_CANCELED. That clause
  describes the device-less baseline; it is not a guard.
- Eb8b53150 (onActivityResult -> FileBrowserFragment$3.<init>): the import branch at ui/FileBrowserFragment.java:326
  requires requestCode == REQUEST_CODE_IMPORT_DB AND resultCode == RESULT_OK AND data != null AND data.getData() != null,
  and at :338 newFile.exists(); when so, the overwrite-confirm dialog's positive-button listener
  (FileBrowserFragment$3, constructed at :342, bytecode-cited one line off at :341) is built.

On a real API 27 device the user picks an existing .db file, so the picker returns RESULT_OK with data and
newFile.exists() is true: the :326/:338 guard and the picker result both hold, with no contradiction. The checker is
only matching the explanatory "RESULT_CANCELED" clause in the ENV text of E078aae8d against the RESULT_OK guard of
Eb8b53150. check_routes.py itself notes a hit is "a route to read by hand, not proof of an error". Verdict: correct
(route-check case (a)); the route rests on the printed lines :311-316, :326, :338 and :341-342.

## Overnight stream-D addendum (2026-11-01, local mirror only — not pushed)

Re-verification status (see AGENT_NOTES.md for the full record): labels and the
30-route sample were re-checked for consistency against the branch build
(REACHABLE 1966 / UNREACHABLE 241, errors 0, warnings 0, path SOURCE_OK 30),
but the full local gate build is BLOCKED because the connector cannot fetch
files over ~1 MB (auto_calls.json, out/methods.csv, out/anymemo_trigger_graph.json).
A clearly-labelled NO-AUTO partial build reproduces the UNREACHABLE set exactly
(241) while leaving 1303 methods UNRESOLVED for want of the bytecode edges.
Storage-permission decision (DECISIONS.md D1): WRITE_EXTERNAL_STORAGE stays an
explicit ENV gate on the startup trunk only (ENV_STORAGE_PERM on the three
loadUiComponents edges; S_PERM_STORAGE for the not-granted branch), grounded in
freshly printed AnyMemo.java lines 124-182 — not pre-granted globally, not
re-gated per storage route. Device checks not started; awaiting user tick.
