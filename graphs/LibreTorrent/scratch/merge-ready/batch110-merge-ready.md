**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 110 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push, so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1 check was run or is claimed in this file. No UNREACHABLE is claimed, so no full-repo grep gap affects these rows.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 110 only, max 40 methods, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior proposal (`~/workspace/libretorrent-batch110-proposal.md`) was used as an INPUT / lead list only; every row below was re-checked against source freshly fetched in this pass, and no proposal verdict was copied as a result. This batch is the continuation of batch 109's MainFragment rows.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 110 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA `0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy). All 40 batch-110 rows are `TODO_CANDIDATE_REACHABLE` in the plan (generator candidates, not evidence), in plan order: MainFragment rows 1–40 (lambdas 1–12, named methods 13–35, $1/$2 anonymous classes 36–40). Descriptors in the table are the plan JVM descriptors, rendered in short form.

## Printed source used in this pass

Fresh connector fetches from branch `work-2026-10-31`, one file at a time with pauses, saved in `~/workspace/b109-110-src/` (same files as batch 109, fetched once and used for both batches in this session):

- `ui/main/MainActivity.java` — fresh, blob SHA `d21f8b70fb50fa09c7b3708243c4f251176f4517`, 811 lines, byte-identical to the local copy in `~/workspace/b27scratch/MainActivity.java`.
- `ui/main/MainFragment.java` — fresh, blob SHA `1fd79b7ac163670dc28de85cbfb5186c3a95ced8`, 637 lines, byte-identical to the local copy in `~/workspace/b27scratch/MainFragment.java`.
- `src/main/AndroidManifest.xml` — fresh, blob SHA `875a8aa7de97caac5d9457836b0ea30f1c3d51ea`, 295 lines, byte-identical to the local copy in `~/workspace/b27scratch/AndroidManifest.xml`.

No fresh HTTP 429 was hit in this pass. No connector `search_code` result was used as evidence for any row.

## Entry trunk — printed, no strict-entry revert

Launcher → MainActivity: `AndroidManifest.xml:43` declares `.ui.main.MainActivity`, with `MAIN`/`LAUNCHER` at :53–55 → `MainActivity.onCreate` → `findFragmentById(R.id.main_fragmentContainer)` at MainActivity.java:184–185 → MainFragment `onAttach` → `onCreateView` → `onViewCreated` (MainFragment.java:125) → `onStart` (MainFragment.java:233) → the five `subscribe*` methods at :237–241. Unlike earlier batches, the launcher step IS printed, so no row in this batch reverts to OPEN under a strict launcher-entry rule.

## confirmed_by convention used here (recorded, not decided)

Per-row immediate-caller rule, as in batch 109: SOURCE = the method is called directly by printed app code (a direct call, or a call written in a printed method/lambda body). INFERRED = the method is only invoked by framework/library dispatch with no printed app call site (Android lifecycle, listener interfaces, Rx operator emission, widget/SelectionTracker/ActivityResult dispatch, JVM class initialisation). This differs from the whole-route INFERRED convention used in some other batches; labels are unaffected, only `confirmed_by` would change at merge if the merger adopts the whole-route convention. That convention choice is UNDECIDED and is not decided here.

## Lambda-numbering cross-check (re-derived, not bytecode-verified)

MainFragment lambda numbers follow class-wide source order in the fresh file, which the proposal's numbering matches exactly: $0 `showAddTorrentMenu` v.post (:216), $1/$2 `observeTorrents` flatMap/error (:289–300), $3 `subscribeAlertDialog` event (:304), $4/$5 `subscribeForceSortAndFilter` filter/subscribe (:327–330), $6/$7 `getAllTorrentsSingle` flatMap/error (:336–348), $8/$9 `subscribeTorrentsDeleted` filter/subscribe (:352–366), $10 `subscribeMsgViewModel` subscribe (:368–376), $11 `initFabSpeedDial` action-selected (:416), $12/$13 batch-109 `deleteTorrents` map/subscribe, $14/$15 batch-109 `forceRecheckTorrents` map/subscribe, $16/$17 batch-109 `forceAnnounceTorrents` map/subscribe, $18 field-initialiser ActivityResult callback (:619). Numbering is source-order inferred, NOT bytecode-verified; labels are unaffected by a swap within a group, and the descriptor matches already checked (captured locals, e.g. batch-109 $13 (Z, List)) pin the identities. Note the `lambda$new$18` name: the torrent-file ActivityResult callback lives in a field initializer, so its compiler-generated name is carried verbatim from the plan, not re-derived.

## Rows

| # | Method | Proposed label | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | MainFragment.lambda$getAllTorrentsSingle$7 (Throwable)V | REACHABLE | INFERRED | Error consumer of the `getAllTorrentsSingle` subscribe (MainFragment.java:333–348); invoked by Rx on error. |
| 2 | MainFragment.lambda$initFabSpeedDial$11 (SpeedDialActionItem)Z | REACHABLE | INFERRED | `setOnActionSelectedListener` lambda in `initFabSpeedDial` (MainFragment.java:416–430, add-link/open-file/create-torrent branches); invoked by the SpeedDial widget on action selection — widget dispatch not printed. |
| 3 | MainFragment.lambda$new$18 (ActivityResult)V | REACHABLE | INFERRED | Callback lambda of `torrentFileChoose = registerForActivityResult(...)` (MainFragment.java:619–637; opens AddTorrentActivity on OK, else `openFileErrorDialog`); invoked by the Activity Result framework — dispatch not printed. |
| 4 | MainFragment.lambda$observeTorrents$1 (List)SingleSource | REACHABLE | INFERRED | FlatMap lambda in `observeTorrents` (MainFragment.java:289–297, filter/map/sort to list); invoked by Rx `flatMapSingle`. |
| 5 | MainFragment.lambda$observeTorrents$2 (Throwable)V | REACHABLE | INFERRED | Error consumer of the `observeTorrents` subscribe (MainFragment.java:285–300); invoked by Rx on error. |
| 6 | MainFragment.lambda$showAddTorrentMenu$0 (View)V | REACHABLE | INFERRED | `v.post(...)` lambda in `showAddTorrentMenu` (MainFragment.java:216–220, register/open/unregister context menu); captured `v` explains the (View) descriptor; invoked by View posting — framework dispatch not printed. |
| 7 | MainFragment.lambda$subscribeAlertDialog$3 (BaseAlertDialog$Event)V | REACHABLE | INFERRED | Event lambda of the `observeEvents` subscribe in `subscribeAlertDialog` (MainFragment.java:304–323; delete-dialog positive click → `deleteTorrents`); invoked by Rx. |
| 8 | MainFragment.lambda$subscribeForceSortAndFilter$4 (Boolean)Z | REACHABLE | INFERRED | Filter lambda in `subscribeForceSortAndFilter` (MainFragment.java:327, `.filter((force) -> force)`); invoked by Rx. |
| 9 | MainFragment.lambda$subscribeForceSortAndFilter$5 (Boolean)V | REACHABLE | INFERRED | Subscribe lambda in `subscribeForceSortAndFilter` (MainFragment.java:330, `disposables.add(getAllTorrentsSingle())`); invoked by Rx. |
| 10 | MainFragment.lambda$subscribeMsgViewModel$10 (Boolean)V | REACHABLE | INFERRED | Subscribe lambda in `subscribeMsgViewModel` (MainFragment.java:368–376, two-pane `adapter.markAsOpen(null)`); invoked by Rx. |
| 11 | MainFragment.lambda$subscribeTorrentsDeleted$8 (String)Z | REACHABLE | INFERRED | Filter lambda in `subscribeTorrentsDeleted` (MainFragment.java:352–362, opened-item id match); invoked by Rx. |
| 12 | MainFragment.lambda$subscribeTorrentsDeleted$9 (String)V | REACHABLE | INFERRED | Subscribe lambda in `subscribeTorrentsDeleted` (MainFragment.java:363–366, two-pane `markAsOpen(null)`); invoked by Rx. |
| 13 | MainFragment.observeTorrents ()Disposable | REACHABLE | SOURCE | Direct call in `subscribeAdapter` (MainFragment.java:282). Definition :285. |
| 14 | MainFragment.onAttach (Context)V | REACHABLE | INFERRED | Lifecycle method at MainFragment.java:224 (sets `activity`); invoked by the framework on fragment attach — no app call site. |
| 15 | MainFragment.onContextItemSelected (MenuItem)Z | REACHABLE | INFERRED | Framework menu callback at MainFragment.java:402 (add-link → `addLinkDialog`, open-file → `openTorrentFileDialog`); invoked by the framework on menu selection. |
| 16 | MainFragment.onCreateContextMenu (ContextMenu, View, ContextMenuInfo)V | REACHABLE | INFERRED | Framework callback at MainFragment.java:393 (inflates `R.menu.main_context`); invoked by the framework. |
| 17 | MainFragment.onCreateView (LayoutInflater, ViewGroup, Bundle)View | REACHABLE | INFERRED | Lifecycle method at MainFragment.java:115 (inflates `fragment_main` binding); invoked by the framework. |
| 18 | MainFragment.onItemClicked (TorrentListItem)V | REACHABLE | INFERRED | `TorrentListAdapter.ClickListener` method at MainFragment.java:379 (two-pane mark-as-open + `msgViewModel.torrentDetailsOpened`); invoked by the adapter on item click — adapter dispatch not printed. |
| 19 | MainFragment.onItemPauseClicked (TorrentListItem)V | REACHABLE | INFERRED | Adapter listener method at MainFragment.java:387 (`viewModel.pauseResumeTorrent`); adapter dispatch not printed. |
| 20 | MainFragment.onResume ()V | REACHABLE | INFERRED | Lifecycle method at MainFragment.java:253 (restores list state); invoked by the framework. |
| 21 | MainFragment.onSaveInstanceState (Bundle)V | REACHABLE | INFERRED | Lifecycle method at MainFragment.java:271 (saves list state + selection); invoked by the framework. |
| 22 | MainFragment.onStart ()V | REACHABLE | INFERRED | Lifecycle method at MainFragment.java:233 (calls the five `subscribe*` methods at :237–241); invoked by the framework. |
| 23 | MainFragment.onStop ()V | REACHABLE | INFERRED | Lifecycle method at MainFragment.java:245 (`disposables.clear()`); invoked by the framework. |
| 24 | MainFragment.onViewCreated (View, Bundle)V | REACHABLE | INFERRED | Lifecycle method at MainFragment.java:125 (builds adapter/animator/selection tracker, `initFabSpeedDial` at :200, shortcut branch → `showAddTorrentMenu` at :203–206); invoked by the framework. |
| 25 | MainFragment.onViewStateRestored (Bundle)V | REACHABLE | INFERRED | Lifecycle method at MainFragment.java:262 (restores `torrentListState`); invoked by the framework. |
| 26 | MainFragment.openFileErrorDialog ()V | REACHABLE | SOURCE | Direct call in the `lambda$new$18` body (MainFragment.java:619–637, non-OK / null-data path). Definition :541. |
| 27 | MainFragment.openTorrentFileDialog ()V | REACHABLE | SOURCE | Direct calls in `onContextItemSelected` open-file branch (MainFragment.java:402–411) and the FAB listener branch (:414–430). Definition :528 (starts FileManagerDialog). |
| 28 | MainFragment.selectAllTorrents ()V | REACHABLE | SOURCE | Direct call in `actionModeCallback.onActionItemClicked` select-all branch (MainFragment.java:475–490). Definition :588 (range-selects all items). |
| 29 | MainFragment.setActionModeTitle (I)V | REACHABLE | SOURCE | Direct calls in the $2 observer bodies (`onSelectionChanged`/`onSelectionRestored`, MainFragment.java:168–195, `setActionModeTitle(selectionTracker.getSelection().size())`). Definition :452. |
| 30 | MainFragment.showAddTorrentMenu ()V | REACHABLE | SOURCE | Direct call in `onViewCreated` shortcut branch (MainFragment.java:203–206, `ACTION_ADD_TORRENT_SHORTCUT`). Definition :210. |
| 31 | MainFragment.subscribeAdapter ()V | REACHABLE | SOURCE | Direct call in `onStart` (MainFragment.java:237). Definition :280. |
| 32 | MainFragment.subscribeAlertDialog ()V | REACHABLE | SOURCE | Direct call in `onStart` (MainFragment.java:238). Definition :302. |
| 33 | MainFragment.subscribeForceSortAndFilter ()V | REACHABLE | SOURCE | Direct call in `onStart` (MainFragment.java:239). Definition :325. |
| 34 | MainFragment.subscribeMsgViewModel ()V | REACHABLE | SOURCE | Direct call in `onStart` (MainFragment.java:241). Definition :368. |
| 35 | MainFragment.subscribeTorrentsDeleted ()V | REACHABLE | SOURCE | Direct call in `onStart` (MainFragment.java:240). Definition :350. |
| 36 | MainFragment$1.<init> (MainFragment)V | REACHABLE | SOURCE | Direct construction `new DefaultItemAnimator() {...}` in `onViewCreated` (MainFragment.java:141–147). $1 = that animator anonymous class. |
| 37 | MainFragment$1.canReuseUpdatedViewHolder (ViewHolder)Z | REACHABLE | INFERRED | Override at MainFragment.java:144 (`return true`); invoked by RecyclerView during item animation — framework dispatch not printed. |
| 38 | MainFragment$2.<init> (MainFragment)V | REACHABLE | SOURCE | Direct construction `new SelectionTracker.SelectionObserver() {...}` in `onViewCreated` (MainFragment.java:165–195, registered via `selectionTracker.addObserver`). $2 = that observer. |
| 39 | MainFragment$2.onSelectionChanged ()V | REACHABLE | INFERRED | Observer method at MainFragment.java:168 (starts/finishes action mode, `setActionModeTitle`); invoked by SelectionTracker — dispatch not printed. |
| 40 | MainFragment$2.onSelectionRestored ()V | REACHABLE | INFERRED | Observer method at MainFragment.java:187 (restarts action mode, `setActionModeTitle`); invoked by SelectionTracker on state restore — dispatch not printed. |

## Counts — mechanically verified

- REACHABLE proposed: 40 (SOURCE 13, INFERRED 27 — counted from the table above)
- UNREACHABLE proposed: 0
- OPEN: 0
- Total: 40/40 judged, sequence 1–40 intact, in plan order.

## Caveats / still owed before merge

- Anonymous-class numbering ($1 animator, $2 selection observer) was matched by construction order in the printed file; the merger should confirm it against bytecode if disputed. Labels are unaffected by a swap within a group.
- No competing `MainFragment` definition was printed elsewhere in this pass; the merger should still confirm no competing definition exists elsewhere in the checkout, as with any batch.
- Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run here.
- **0 rows verified for merge.**
