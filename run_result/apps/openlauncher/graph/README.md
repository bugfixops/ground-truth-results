# openlauncher 0.3.1: method-level trigger graph (schema 2)

How every method of **openlauncher** is triggered, in the standard configuration: the instrumented debug build (`tingsu/openlauncher@instrument-version-0.3.1`, commit `30e58f59371c`, APK sha256 `00352a14...`), an API 27 emulator, permissions and fixtures as in `final_java_only`. Labels follow `handoff/SCHEMA_V2.md`: REACHABLE or UNREACHABLE, ENV and STATE gates, edge classes (explicit, standard, non-standard), and how each label was confirmed.

## What is in this folder

| File | What it is |
|---|---|
| `openlauncher_trigger_graph.json` | pages, methods, `verdict`, `labels` (per-method fields), `edges` (with `edge_class`, `env_kinds`, `state_kinds`, stable ids), `paths` (verified paths only), `verification` (counts) |
| `methods.csv` | one row per method: verdict, UNREACHABLE reason, ENV and STATE kinds and texts, edge classes on the best route, whether an explicit/standard-only route exists, how the label was confirmed, path status, and the derived best route (`shortest_path`, `route_edge_ids`) |
| `../verification.csv` | the audit log: one row per label, edge or path that was checked, with result, how, and where (file:line) |
| `sanity_check.csv` | tool coverage (Monkey / APE, API 27) next to the labels; a one-way check only, it never sets a label |
| `openlauncher_trigger_graph.html`, `build_report.txt` | the viewer and the validation report |

## Numbers

- **900 methods**, **43 pages** (including pseudo pages), **1515 edges**. Verdicts: **728 REACHABLE**, **172 UNREACHABLE**.
- UNREACHABLE by reason: closed_by_configuration 19, framework_never_calls 10, no_trigger_in_app 143.
- ENV gates (methods): hardware 3, other_app 18, permission 5, system_event 3, time 1. STATE gates (methods): data 90, session 2, settings 36. Methods with no gate: 571.
- Edge classes: explicit 984, non_standard 129, page 102, standard 300. Non-standard edges: 129 (ButterKnife: the generated DebouncingOnClickListener calls doClick; ButterKnife: the generated Home$$ViewBinder is loaded by name; ButterKnife: the generated binder is loaded by name; CircularReveal library animator calls the AnimatorListener; CompoundButton calls the OnCheckedChangeListener; DragSc).
- 724 reachable methods have a non-standard edge on their best route; 254 have no explicit-or-standard-only route at all.
- Labels confirmed by: INFERRED 724, SOURCE 176 (SOURCE: every edge of the best route cites a source line, in the app or in the Android 8.1 / library source; INFERRED: some edge rests on inference or on another app).

## How much to trust it

Verification log (`verification.csv`), counts of what was checked and found:

| Checked | Rows | Correct | Errors found (fixed) | Unclear |
|---|---:|---:|---:|---:|
| labels | 199 | 199 | 0 | 0 |
| edges (framework and other claims read against source) | 37 | 34 | 3 | 0 |
| paths (stratified sample, read step by step) | 27 | 26 | 1 | 0 |

Device replay on the emulator (API 27): 5 of 27 routes reached their target method; 5 of these ran the whole script and are `DEVICE_OK`. The other routes are unclear (not reached, script stopped, or unscriptable), never wrong; see `../device/results.csv`.

Path status over all reachable methods: DEVICE_OK 5, SOURCE_OK 22, UNCHECKED 701.
The rows are the items that were individually checked, not a random sample of all labels; see the notes below for how they were chosen and what the unclear rows wait for.

Edges whose evidence is not a source line (182 of 1515): E5443509f (Home.<init> -> Home.<clinit>); E5245b855 (S_ENTRY -> FiveSecsDelayContentProvider.query); Ee0bafc0f (S_ENTRY -> FiveSecsDelayContentProvider.insert); E8d693829 (S_ENTRY -> FiveSecsDelayContentProvider.update); E4d2b8aaa (S_ENTRY -> FiveSecsDelayContentProvider.getType); E8828e57a (S_ENTRY -> FiveSecsDelayContentProvider.delete); E15938fe2 (S_ENTRY -> DeviceAdminReceiver.<init>); E52bc2f77 (DeviceAdminReceiver.<init> -> DeviceAdminReceiver.onReceive); E1d6f1e01 (S_ENTRY -> ShortcutReceiver.onReceive); E5aa97973 (Init.onCreate -> S_INTRO); E8b7dd43a (S_INTRO -> Init.onSkipButtonPressed); E0fe9628f (S_INTRO -> Init.onFinishButtonPressed) ...

Sanity check against tool coverage (never used to set a label): 520 methods ran in the 1-hour Monkey / APE runs on API 27; **0** of them are labelled UNREACHABLE.

## What the re-audit changed (compared with the schema 1 graph)

- **Full rewrite, not a patch.** The schema 1 generated draft (`generated_draft_graph_def.py.txt`) was never built and is kept only for the method-name inventory it gave; every section of `graph_def.py` (entry points, lifecycle, pages, GUI handlers, framework callbacks, gates, the UNREACHABLE dict) was written by hand from the app sources (`src/main` plus the three vendored libraries `smoothviewpager`, `materialpreffragment`, `launcheranim` under `app/libs/`, which DATASET.txt's `source_dirs:4/class_dirs:1` confirms are compiled into this APK). `DEAD` / `FRAMEWORK_ONLY` do not appear anywhere (`grep -c "DEAD\|FRAMEWORK_ONLY" graph_def.py` is 0).
- **Labels.** 900 methods: 728 REACHABLE, 172 UNREACHABLE (143 `no_trigger_in_app` - mostly the dead `DatabaseHelper` class, the `@Deprecated` `SettingsFragment` and `QuickCenterItem.NoteItem`/`SearchHeader`, the orphan `MinibarEditFragment`, and static-utility no-arg constructors; 19 `closed_by_configuration` - the `Home$CallLogObserver`/`QuickCenterItem.ContactItem` cluster, closed because `READ_CALL_LOG` is commented out of the manifest; 10 `framework_never_calls` - Drawable/Animator callbacks the app never triggers). Every UNREACHABLE method has an authored kind, reason and source reference (no `unclassified`). `tools/scan_unreachable.py openlauncher --all --callers` found 2 of 172 with a bytecode caller outside the unreachable set (`Home$CallLogObserver.<init>` and `.onChange(boolean)`, called from `Home.initQuickCenter` / `Home.onRequestPermissionsResult`); both callers are already named and explained in the existing reason text, so no change was needed.
- **Gates.** 30 ENV texts and 21 STATE texts (`ENV_KINDS_OF` / `STATE_KINDS_OF`), covering the device-admin flow, the legacy `INSTALL_SHORTCUT` broadcast, the Kustom live-wallpaper content provider, package broadcasts, runtime permissions, and in-app state (saved desktop/dock JSON, a folder existing, settings that need a restart, a first-resume check). Gesture prose (swipe, pinch, long-press) stays in the guard / trigger text, never in a STATE.
- **Framework claims (FW-SRC).** Every `FW-SRC` citation in the file was checked this session against the real AOSP 8.1.0_r1 source: 28 distinct framework files (`ActivityThread`, `Activity`, `ContextImpl`, `Dialog`, `LoadedApk`, `AppWidgetHost`, `ClipData`, `ContentProvider`, `Intent`, `AsyncTask`, `BaseBundle`, `Bundle`, `Handler`, `Parcel`, `GestureDetector`, `LayoutInflater`, `View`, `ViewGroup`, `ViewPropertyAnimator`, `ViewRootImpl`, `AbsListView`, `AdapterView`, `TextView`, `AlarmManagerService`, `ActivityRecord`, `ActivityManagerService`, `PackageManagerService`, `DragState`, `WindowManagerService`), about 60 distinct cited line-range groups, all already present under `work/fw_src/android-8.1.0_r1/` from earlier apps' sessions (same tag, reused as-is). Every citation was dumped and read against the prose claim next to it; all matched (0 errors - see `verification.csv` edge rows and `check_citations.py`).
- **One real error found and fixed while reading the sample paths:** the `DialogUtils$9.onSelection -> DialogUtils.copy` edge carried `env=ENV_STORAGE_FAIL` ("a backup or restore step throws"), the opposite of its own guard ("do not throw"); reading `DialogUtils.java:146-182` in full showed the two *following* page edges were also backwards for the same reason (`System.exit(1)` at line 179 is outside the Restore try/catch, so it always runs for Restore regardless of whether the copy threw; Backup never exits at all, so it always returns to the settings screen regardless of throw). Fixed: the ENV gate was dropped (and its now-unused definition removed), and the two guards were simplified to the plain "item is Backup" / "item is Restore". See `LESSONS.md` and the `verification.csv` note on this edge/path.

## How the checked paths were chosen

`python3 -I tools/verify_sample.py openlauncher 30` draws a stratified sample of reachable methods by what their best route needs (non-standard edge, INFERRED label, STATE gate, ENV gate, a long route, a plain route), seed 20261025; it returned 27 distinct methods (the strata have fewer members than 30 in this app). The sample was drawn once before the DialogUtils fix and once after (identical 27 methods both times - the fix did not change which route was cheapest for any of them). Each of the 27 was read step by step with a locally patched copy of `show_route.py` (see Limits) against the printed source lines, including every guard, `if`/`catch` condition and ENV/STATE gate (`tools/cases.py` `CS.guard_of`). 27 of 27 paths checked, 1 fixed (the `DialogUtils.copy` route above - the route itself was already correct, but its evidence/guard text and two sibling edges were wrong), 26 correct, 0 wrong, 0 unclear: path error rate 1/27 = 0.037 (`tools/build_graph.py`'s own verification summary agrees: "verification path: checked 27, errors found 1 (rate 0.037)"). All 27 are `confirmed_by SOURCE` except where a route runs through a library (MaterialDialogs, ButterKnife, the support FragmentManager/DrawerLayout/PopupMenu, FastAdapter/RecyclerView, the support FragmentPagerAdapter, DragScrollBar), which stays INFERRED since none of those library sources are in this dataset. Label rows cover the 27 sampled reachable methods plus all 172 UNREACHABLE methods (199 label rows, 0 errors). Edge rows cover the 3 edges fixed in the DialogUtils cluster plus one row per distinct FW-SRC citation read (34 more, all correct): 37 edge rows, 3 fixed (rate 0.081 - all three are the one DialogUtils cluster, not three independent mistakes).

## What waits for a device (API 27)

- **Device run 41593209101-1 (2026-11-03, Google APIs, API 27, x86).** 5 of 27 routes reached their target method; 5 of them ran the whole script and are now `DEVICE_OK`. The other routes are unclear (not reached, script stopped, or unscriptable), never wrong; the reason for each route is in `handoff/DEVICE_RUN_SUMMARY.md`. What is listed below still waits for a device.

Nothing here is `confirmed_by DEVICE` (0 of 900). What an emulator replay should settle: that the system widget picker and a widget's own configure activity really return `RESULT_OK`/`RESULT_CANCELED` the way `Home.onActivityResult` assumes; that `org.kustom.wallpaper` / `org.kustom.widget` (or a stand-in package with the same name) can actually reach `FiveSecsDelayContentProvider.delete` from outside the app; that the legacy `com.android.launcher.action.INSTALL_SHORTCUT` broadcast is still delivered on API 27 (it predates the modern pinned-shortcut API); that dragging an icon out of the app drawer onto the desktop behaves as `DragState`/`WindowManagerService` suggest (ENTERED/EXITED/DROP ordering); that activating/deactivating OpenLauncher as a device administrator in Settings actually fires `DeviceAdminReceiver`; and that a real low-memory condition calls `onLowMemory` the way `ActivityThread.handleLowMemory` claims. No method is closed by the API level: nothing here is gated on an `SDK_INT` check that fails on 27.

## Hazard candidates (from reading the code, not reproduced)

- **`AppItemView.onLongClick` chain can never trigger the cross-user drag permission path** - not a bug, but worth recording since it was visible while reading the cited lines: `DragState.notifyDropLw` (`services/core/java/com/android/server/wm/DragState.java:515-525`) builds a `DragAndDropPermissionsHandler` only when `View.DRAG_FLAG_GLOBAL` is set, which this app never sets (`widget/AppItemView.java:332` passes flags `0` to every `startDrag` call), so that branch of the framework code is dead weight for this app on every device.
- **`DialogUtils.backupDialog`'s Restore branch always calls `System.exit(1)`, even when the copy failed** (`util/DialogUtils.java:174-179`): a failed Restore still kills the process, so the user sees only a brief failure Toast before the app disappears, with no further indication that the restore did not happen - a sequence worth checking on a device, not just the source.
- **`Home$CallLogObserver`/`QuickCenterItem.ContactItem` are permanently dead code**, not merely low coverage: `READ_CALL_LOG` is commented out of the manifest (`AndroidManifest.xml:4-8`, "TODO activate later again"), so the whole call-log quick-center row can never be built in this build, not just untested by Monkey/APE.
- **`ENV_LANDSCAPE`** (`Home` is locked to portrait by `android:screenOrientation` but a route needs a landscape configuration delivered to it) is marked INFERRED because `WindowManagerService`'s own orientation-lock enforcement was not read; worth a closer look if a future session has time, since it gates more than one callback.

## Limits

- **A real tool bug was found and worked around, not fixed in `tools/`** (out of scope for this app's folder): `tools/show_route.py`'s regex for extracting a `SRC`/`FW-SRC` citation (`r'(?:FW-)?SRC\s+([^\s;]+(?:\s*\([^)]*\))?)'`) stops at the first whitespace, so a line reference written `File.java:747, 751-760` (comma then space, the house style used throughout this file for multi-range citations) is truncated to `747,` and then crashes `snippet()` on the dangling empty segment after the trailing comma. Worked around with `graphs/openlauncher/show_route_fixed.py`, a copy of the tool with the extraction regex changed to match the whole `File.java:N(-M)(, N(-M))*` token directly and `snippet()` made to skip empty segments; used for every route read this session. `tools/check_citations.py`'s own `LINES` regex already handles the comma-space form correctly, so citation checking itself was never affected - only the route-printing tool crashed.
- **MaterialDialogs, ButterKnife, the support FragmentManager/DrawerLayout/PopupMenu/ActionBar, FastAdapter/RecyclerView, the support `ViewPager`'s `FragmentPagerAdapter`, and the DragScrollBar library are not in this dataset**, so every step through one of them is INFERRED: 724 of 900 labels are confirmed INFERRED, 176 SOURCE. A path marked `SOURCE_OK` in `verification.csv` means every *app* step on it was read against the source; a library step on the same route is still INFERRED in the edge evidence.
- **701 of 728 reachable routes are `UNCHECKED`** - only the 27 sampled were read step by step. The derived "best" route (fewest ENV gates, then STATE gates, then steps) can be an unusual one (e.g. `Home.handleLauncherPause@DESKTOP` rather than a UI action); every step of the 27 checked routes matched the source exactly once read, including guards and gates, but the other 701 were not individually read.
- **Bytecode-derived edges (637 of 1515) carry no guard by default**; guards were added by hand only where a sampled route, or an obviously conditional call site noticed while writing the UNREACHABLE dict, needed one. A route not in the sample could in principle still hide an un-added guard.
- The three vendored libraries (`smoothviewpager`, `materialpreffragment`, `launcheranim`) are cited as `SRC` (their source is in the dataset and was read), not `INFERRED`, matching the existing convention for other apps' vendored copies.
- The standard configuration is `flavorDefault`, debug build (DATASET.txt provenance and `app/build/intermediates/javac/flavorDefaultDebug` agree); there is only one flavor in this project, so no cross-flavor ambiguity.
- **check 7 counts 1 line (graph_def.py:942), which is AsyncTask code text, not a placeholder.** Line 942 is the `HideAppsFragment.onCreateView -> HideAppsFragment$AsyncWorkerList.onPreExecute` edge, whose guard is `taskList.getStatus() == PENDING (first time)` - the `AsyncTask.Status.PENDING` check from `HideAppsFragment.java:66-69`. The word PENDING there is the framework status constant in a real guard, not a pending-work page id, so it is left as written.

## JSON shape (short)

```
{ "schema": 2, "title", "screens": {page: description}, "methods": [...], "verdict": {method: REACHABLE|UNREACHABLE},
  "labels": {method: {unreachable: {kind, text}, env: [{kinds, text}], state: [{kinds, text}], route_edge_classes, explicit_standard_route,
                      confirmed_by, source_ref, path_status}},
  "edges": [ {id, src, dst, kind, edge_class, via, trigger, gui[], guard, reads[], writes[], note, needs_state, state_kinds, env, env_kinds, evidence, class_basis} ],
  "paths": [ {method, edges[], edge_classes, explicit_standard_only, env, state, verified_by, ref} ], "verification": {...} }
```

`src`/`dst` are methods (`Class.method`, overloads as `Class.method(Type,Type)`) or pages (`S_...`). A suffix `@CONTEXT` is the same method or page in a specific context. Edge ids are a hash of the edge content, so they stay stable when other edges change.
