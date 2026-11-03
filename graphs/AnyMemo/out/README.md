# AnyMemo 10.12.2: method-level trigger graph (schema 2)

How every method of **AnyMemo** is triggered, in the standard configuration: the instrumented debug build (`helloworld1/AnyMemo@10.12.2`, commit `8887e8211de3`, APK sha256 `f85a35e9...`), an API 27 emulator, permissions and fixtures as in `final_java_only`. Labels follow `handoff/SCHEMA_V2.md`: REACHABLE or UNREACHABLE, ENV and STATE gates, edge classes (explicit, standard, non-standard), and how each label was confirmed.

## What is in this folder

| File | What it is |
|---|---|
| `anymemo_trigger_graph.json` | pages, methods, `verdict`, `labels` (per-method fields), `edges` (with `edge_class`, `env_kinds`, `state_kinds`, stable ids), `paths` (verified paths only), `verification` (counts) |
| `methods.csv` | one row per method: verdict, UNREACHABLE reason, ENV and STATE kinds and texts, edge classes on the best route, whether an explicit/standard-only route exists, how the label was confirmed, path status, and the derived best route (`shortest_path`, `route_edge_ids`) |
| `../verification.csv` | the audit log: one row per label, edge or path that was checked, with result, how, and where (file:line) |
| `sanity_check.csv` | tool coverage (Monkey / APE, API 27) next to the labels; a one-way check only, it never sets a label |
| `anymemo_trigger_graph.html`, `build_report.txt` | the viewer and the validation report |

## Numbers

- **2207 methods**, **77 pages** (including pseudo pages), **4492 edges**. Verdicts: **1966 REACHABLE**, **241 UNREACHABLE**.
- UNREACHABLE by reason: branch_never_taken 7, framework_never_calls 18, no_trigger_in_app 216.
- ENV gates (methods): hardware 63, network 113, other_app 193, permission 1799, system_event 23, time 13. STATE gates (methods): account 79, data 531, file 5, session 984, settings 14. Methods with no gate: 80.
- Edge classes: explicit 3252, non_standard 356, page 168, standard 716. Non-standard edges: 356 (AbsListView.obtainView calls the adapter getView; ActionMode (AppCompat, library); ArrayAdapter.remove(T) -> List.remove(Object) -> Category.equals (AOSP 8.1.0_r1); AsyncTaskLoader (androidx library); CardDao interface; setHelper is inherited from AbstractHelperDaoImpl (interface dispatch not follow).
- 1838 reachable methods have a non-standard edge on their best route; 546 have no explicit-or-standard-only route at all.
- Labels confirmed by: INFERRED 1957, SOURCE 250 (SOURCE: every edge of the best route cites a source line, in the app or in the Android 8.1 / library source; INFERRED: some edge rests on inference or on another app).

## How much to trust it

Verification log (`verification.csv`), counts of what was checked and found:

| Checked | Rows | Correct | Errors found (fixed) | Unclear |
|---|---:|---:|---:|---:|
| labels | 271 | 271 | 0 | 0 |
| edges (framework and other claims read against source) | 45 | 38 | 7 | 0 |
| paths (stratified sample, read step by step) | 60 | 35 | 0 | 25 |

Path status over all reachable methods: DEVICE_OK 5, UNCHECKED 1961.
The rows are the items that were individually checked, not a random sample of all labels; see the notes below for how they were chosen and what the unclear rows wait for.

Edges whose evidence is not a source line (836 of 4492): E612d7778 (AMApplication.<init> -> AMApplication.<clinit>); E21a1ff1d (CardProvider.<init> -> CardProvider.<clinit>); E1597aa9e (CardProvider.onCreate -> CardProvider.query); Eda12bfa1 (CardProvider.onCreate -> CardProvider.insert); E45e40cab (CardProvider.onCreate -> CardProvider.update); Ed29a3dd6 (CardProvider.onCreate -> CardProvider.delete); E897c4318 (CardProvider.onCreate -> CardProvider.getType); E9d821a48 (DatabasesProvider.onCreate -> DatabasesProvider.query); E9f0e5ffe (DatabasesProvider.onCreate -> DatabasesProvider.insert); E5c2dcaf1 (DatabasesProvider.onCreate -> DatabasesProvider.update); E6cf94e21 (DatabasesProvider.onCreate -> DatabasesProvider.delete); E16059cda (DatabasesProvider.onCreate -> DatabasesProvider.getType) ...

Sanity check against tool coverage (never used to set a label): 1271 methods ran in the 1-hour Monkey / APE runs on API 27; **0** of them are labelled UNREACHABLE.

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

## JSON shape (short)

```
{ "schema": 2, "title", "screens": {page: description}, "methods": [...], "verdict": {method: REACHABLE|UNREACHABLE},
  "labels": {method: {unreachable: {kind, text}, env: [{kinds, text}], state: [{kinds, text}], route_edge_classes, explicit_standard_route,
                      confirmed_by, source_ref, path_status}},
  "edges": [ {id, src, dst, kind, edge_class, via, trigger, gui[], guard, reads[], writes[], note, needs_state, state_kinds, env, env_kinds, evidence, class_basis} ],
  "paths": [ {method, edges[], edge_classes, explicit_standard_only, env, state, verified_by, ref} ], "verification": {...} }
```

`src`/`dst` are methods (`Class.method`, overloads as `Class.method(Type,Type)`) or pages (`S_...`). A suffix `@CONTEXT` is the same method or page in a specific context. Edge ids are a hash of the edge content, so they stay stable when other edges change.
