# LibreTorrent 3.5.2 — source re-audit: method-level trigger graph (schema 2)

How every method of **LibreTorrent** is triggered, in the standard configuration: the instrumented debug build (`proninyaroslav/libretorrent@3.5.2`, commit `d93e92eacebc`, APK sha256 `5e05d2ff...`), an API 27 emulator, permissions and fixtures as in `final_java_only`. Labels follow `handoff/SCHEMA_V2.md`: REACHABLE or UNREACHABLE, ENV and STATE gates, edge classes (explicit, standard, non-standard), and how each label was confirmed.

## What is in this folder

| File | What it is |
|---|---|
| `libretorrent_trigger_graph.json` | pages, methods, `verdict`, `labels` (per-method fields), `edges` (with `edge_class`, `env_kinds`, `state_kinds`, stable ids), `paths` (verified paths only), `verification` (counts) |
| `methods.csv` | one row per method: verdict, UNREACHABLE reason, ENV and STATE kinds and texts, edge classes on the best route, whether an explicit/standard-only route exists, how the label was confirmed, path status, the derived best route (`shortest_path`, `route_edge_ids`), and the full JVM class and descriptor (`jvm_class`, `jvm_descriptor`; the `method` key adds a package prefix only where simple class names clash) |
| `../verification.csv` | the audit log: one row per label, edge or path that was checked, with result, how, and where (file:line) |
| `sanity_check.csv` | tool coverage (Monkey / APE, API 27) next to the labels; a one-way check only, it never sets a label |
| `libretorrent_trigger_graph.html`, `build_report.txt` | the viewer and the validation report |

## Numbers

- **4732 methods**, **1 pages** (including pseudo pages), **7299 edges**. Verdicts: **3955 REACHABLE**, **777 UNREACHABLE**.
- UNREACHABLE by reason: branch_never_taken 15, closed_by_api_level 26, closed_by_configuration 1, framework_never_calls 20, no_trigger_in_app 715.
- ENV gates (methods): hardware 33, network 289, other 43, other_app 133, system_event 10, time 4. STATE gates (methods): data 1088, file 102, session 7, settings 71. Methods with no gate: 2388.
- Edge classes: explicit 4709, non_standard 1877, standard 713. Non-standard edges: 1877 (ACRA report-dialog dispatch; ActionMode creation dispatch; ActionMode dispatch; ActionMode dispatch (action mode started here); ActionMode menu-item dispatch; ActionMode prepare dispatch; ActionMode teardown dispatch; Activity back-press dispatch; AlertDialog onShow dispatch; Android AsyncTask THREA).
- 3543 reachable methods have a non-standard edge on their best route; 3350 have no explicit-or-standard-only route at all.
- Labels confirmed by: INFERRED 4202, SOURCE 530 (SOURCE: every edge of the best route cites a source line, in the app or in the Android 8.1 / library source; INFERRED: some edge rests on inference or on another app).

## How much to trust it

Verification log (`verification.csv`), counts of what was checked and found:

| Checked | Rows | Correct | Errors found (fixed) | Unclear |
|---|---:|---:|---:|---:|
| labels | 865 | 858 | 6 | 1 |
| edges (framework and other claims read against source) | 78 | 53 | 25 | 0 |
| paths (stratified sample, read step by step) | 29 | 20 | 9 | 0 |

Device replay on the emulator (API 27): 7 of 29 routes reached their target method; 7 of these ran the whole script and are `DEVICE_OK`. The other routes are unclear (not reached, script stopped, or unscriptable), never wrong; see `../device/results.csv`.

Path status over all reachable methods: DEVICE_OK 7, SOURCE_OK 7, UNCHECKED 3933, WRONG 8.
The rows are the items that were individually checked, not a random sample of all labels; see the notes below for how they were chosen and what the unclear rows wait for.

Edges whose evidence is not a source line (2182 of 7299): E6f0891c5 (S_ENTRY -> MainApplication.<clinit>); E8228a4c6 (S_ENTRY -> MainActivity.<clinit>); E0f555379 (S_ENTRY -> AddTorrentActivity.<clinit>); E6c221f79 (S_ENTRY -> SettingsActivity.<clinit>); E70444373 (MainActivity.initDrawer -> DrawerExpandableAdapter.onBindChildViewHolder); E79785310 (MainActivity.initDrawer -> MainActivity.lambda$initDrawer$0); Eea644f43 (MainActivity.initDrawer -> MainActivity.lambda$initDrawer$0); Ecebe3a05 (MainActivity.initDrawer -> MainActivity.lambda$initDrawer$1); Ed0bb2c8b (MainActivity.initDrawer -> MainActivity.lambda$initDrawer$1); Ec7ef9327 (MainActivity$3.onTagMenuClicked -> MainActivity$3.lambda$onTagMenuClicked$0); E83e4ed2d (MainActivity$3.onTagMenuClicked -> MainActivity$3.lambda$onTagMenuClicked$0); E34551cd4 (MainActivity$3.onTagMenuClicked -> MainActivity$3.lambda$onTagMenuClicked$1) ...

Sanity check against tool coverage (never used to set a label): 2080 methods ran in the 1-hour Monkey / APE runs on API 27; **2** of them are labelled UNREACHABLE.

# LibreTorrent logs — readme notes (Kiro final local state, 2026-11-03)

Docs only. Every fact below comes from a build or file of the local branch `kiro-libretorrent`
(`graphs/LibreTorrent/scratch/kiro/KIRO_REPORT.md` lists the commits and the printed numbers).
The first-draw notes (B6 logs step, graph `a9e8b93d`) are superseded; their route table is kept as
`scratch/route_table_first_draw.md`.

## What the re-audit changed (compared with the schema 1 graph)

Re-audit of November 2026 (rounds of W2 to W7, see handoff/MUSE_REAUDIT_SUMMARY.md):

- Launcher start (W3): MainActivity's launcher entries lose their env gate; five in-app starts are added; exported-entry routes 3,918 to 9.
- A torrent row exists only after a torrent is added: the row-binding edge needs data (W3).
- Library class (W5): data-binding mappers and two Rx error consumers are non_standard.
- Outside data (W6): the torrent stream server and Room migrations are env.
- Guards (W7, round 1): an empty file selection and a paused torrent need state (LibreTorrent-16, -19).

The graph is the schema-2 rebuild from printed source: 121 batch parts plus two Kiro parts
(`k01_warnings.py`, `k02_check8.py`) merged in `graph_def.py`. Final build: 4732 methods,
7303 edges, REACHABLE 3967 / UNREACHABLE 765 / UNRESOLVED 0; labels confirmed by SOURCE 621,
INFERRED 4111; errors 0, warnings 0.

Changes made on top of the first-draw graph (`a9e8b93d`: R3882 / U764 / UNRES86):

- Part b121 labels the last 86 methods: 85 REACHABLE through missing delivery edges from callers
  that were already REACHABLE (Handler post, AlarmManager delivery, TextWatcher, Observable
  callbacks, RxJava stages, clicks, ActivityResult), and `TorrentInputStream.toUnsignedByte`
  UNREACHABLE (ruling D2). `DialogSelectTagBindingImpl.hasPendingBindings` is REACHABLE through the
  existing INFERRED edge from `SelectTagDialog.onCreateDialog` (ruling D3). Stale line numbers on 17
  select-tag edges were corrected (K4).
- Citation form (K1): app files under `libretorrent/core/` are cited by file name; generated
  binding/Room classes are cited as INFERRED generated code. With the one-line fix in
  `tools/check_citations.py`, check 2 is 65 distinct citations, 0 problems.
- Check 4 is 0: the 7 try-with-resources `close()` edges cite the whole block (K3).
- The 95 data-binding edges are `non_standard` (K2, same rule as AnyMemo).
- The 16 "UNREACHABLE but has incoming edges" warnings are cleared by suppressing or dropping edges
  whose caller never runs on API 27 (k01, K6). No label changed.
- Every check-8 reason names its bytecode caller (k02; 33 named, 0 missing;
  `scratch/check8_explained.md`).

## How the checked paths were chosen

- Sample command: `python3 -I tools/verify_sample.py LibreTorrent 30 20261025`, drawn on the
  labels-gate graph (commit `58a3600a`). It gives 29 routes, not 30: the sampler header reads
  "29 of 3967 reachable methods". The STATE stratum (quota 3) has a pool for the first time (the
  select-tag row tap carries the gate `adapter.getItemCount() > 0`), but only 2 methods carry a
  STATE gate, so one STATE place stays empty. The 29 routes total 457 steps and 306 distinct edges.
- The sample was drawn before the log step (`make_verification.py` and the new `verification.csv`).
  The log step's label rows could change which methods the sampler picks on the final graph; a
  redraw with the same command after the log step was checked and gave the same 29 methods in the
  same order, so the judged routes are current.
- Judging: Appendix D of the Kiro handover. Each step needs action TRUE and condition TRUE in one
  run (fresh install, API 27, instrumented debug build, only the earlier steps of the same route).
  A printed line that contradicts a step makes it FALSE (route WRONG); a step that depends on code
  not in the upload or on state no earlier step creates is UNCLEAR. 22 routes are the same route
  as in the first draw and carry its verdict; 7 are new and were judged step by step
  (`scratch/kiro/judgments/`).
- Result: CORRECT 18, WRONG 9, UNCLEAR 2, fixed 0.
- Error rate = (fixed + wrong) / (correct-only + fixed + wrong), where fixed = WRONG in an earlier
  draw and CORRECT in the final draw, correct-only = CORRECT minus fixed, every route counted once,
  UNCLEAR reported separately. Here (0 + 9) / (18 + 0 + 9) = 9/27 ≈ 0.3333.
- Stopping rule (user decision, as for AnkiDroid and Aegis): the final draw is judged once, with no
  fix round. WRONG routes stay WRONG with their reasons and count in the rate.

## What waits for a device (API 27)

- **Re-audit, last real run 42560435293-1 (2026-11-09, API 27).** The sampled routes were re-verified first (Step 3), and the dry run had 0 FAIL. 7 of 29 routes reached their target (17 scripts ran to the end, 12 are unscriptable); the others are unclear, never wrong. Five device routes are no longer the best route (TrackerInfo.infoHashStatus, SelectTagDialog.onTagClicked, tag.TagsAdapter$ViewHolder.lambda$bind$0, TorrentDownloadImpl.pieces, SaveLogWorker.lambda$showSuccessToast$1) and could not be replayed again (the re-audit allows two real runs). What is listed below still waits for a device.

- **Device run 41593209101-1 (2026-11-03, Google APIs, API 27, x86).** 7 of 29 routes reached their target method; 7 of them ran the whole script and are now `DEVICE_OK`. The other routes are unclear (not reached, script stopped, or unscriptable), never wrong; the reason for each route is in `handoff/DEVICE_RUN_SUMMARY.md`. What is listed below still waits for a device.

Nothing in this file is a device result. The device scripts in `device/routes/LibreTorrent/`
(one per scripted row of `ROUTES.csv`) passed only the dry run (`device/drycheck.py`); no emulator
was used. The judged premises (a fresh install of `org.proninyaroslav.libretorrent.debug` on an
Android 8.1 emulator, runtime permissions granted only where a route needs them) are what a later
device run must confirm. Routes judged WRONG have no script; their rows are
`unscriptable: route WRONG as drawn (see route_table.md)`.

## Hazard candidates (from reading the code, not reproduced)

Reading hazards from the judgments; none was reproduced on a device.

- SAF dispatch needs a content:// dir that the app never stores (routes 5, 20, 22 and first-draw
  row 19): the resolver picks SafFsModule only for scheme content (`FsModuleResolverImpl.java:42-49`,
  `SafFileSystem.java:191-198`), while every save path the app writes is file://
  (`SettingsRepositoryImpl.java:102-103`, `StorageSettingsFragment.java:227-239,267`,
  `FileManagerViewModel.java:282`). First-draw row 5 (`SafFileSystem$FakePath.normalizeRelativePath`,
  not in the final sample) shares the step judged FALSE in final route 5; it is likely WRONG too.
- Fragment-commit versus header-click path (route 12 and first-draw row 10): `setFragment` from
  `SettingsFragment.onViewCreated` commits AppearanceSettingsFragment, never the Network page.
- Interface calls resolved to one implementation: automatic edges map every dialog's
  `FragmentCallback.onFragmentFinished` call to `SelectTagActivity.onFragmentFinished`, and the
  KeyProvider `selectable.getItemKey` calls to every Selectable adapter. Such edges can join
  screens that never meet in one run.
- Rows that need user data: tapping a torrent row or a tag row needs a torrent or tag the route
  does not create (routes 9 and 10 are UNCLEAR for the tag; the first-draw judges accepted the
  torrent row as a premise).
- GC finalization (route 3), dialog-mode mixing (routes 4 and 6), worker action dispatch (route 7)
  and the cancel-versus-add button listener (route 11) are carried over from the first draw.

## Limits

- The route rate is measured on 27 judged routes (29 minus 2 UNCLEAR); the 22 carried-over verdicts
  were not re-judged step by step. Their edge lists were compared with the first-draw graph
  (`scratch/kiro/same_route_diff.txt`): same nodes, kinds, guards and gates; only citation text
  changed.
- No helper agent ran (host memory stayed critical and the requested helper model was not
  available), so every judgment had one reader and no independent audit.
- `AddTorrentInfoFragment.showOpenDirErrorDialog` and `DetailTorrentInfoFragment.showOpenDirErrorDialog`
  are REACHABLE through a guard (`data == null`) that the printed lines suggest never holds while the
  public Download directory exists; left for the reviewer.
- 4111 of 4732 labels are INFERRED; 10 of them stay INFERRED by ruling LT-4A-STAYS-INFERRED.
- The tools change (`tools/check_citations.py` line 20) needs the reviewer's approval before push.

## JSON shape (short)

```
{ "schema": 2, "title", "screens": {page: description}, "methods": [...], "verdict": {method: REACHABLE|UNREACHABLE},
  "labels": {method: {unreachable: {kind, text}, env: [{kinds, text}], state: [{kinds, text}], route_edge_classes, explicit_standard_route,
                      confirmed_by, source_ref, path_status}},
  "edges": [ {id, src, dst, kind, edge_class, via, trigger, gui[], guard, reads[], writes[], note, needs_state, state_kinds, env, env_kinds, evidence, class_basis} ],
  "paths": [ {method, edges[], edge_classes, explicit_standard_only, env, state, verified_by, ref} ], "verification": {...} }
```

`src`/`dst` are methods (`Class.method`, overloads as `Class.method(Type,Type)`) or pages (`S_...`). A suffix `@CONTEXT` is the same method or page in a specific context. Edge ids are a hash of the edge content, so they stay stable when other edges change.
