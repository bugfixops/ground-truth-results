# LibreTorrent batch 109 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push, so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1 check was run or is claimed in this file. No UNREACHABLE is claimed, so no full-repo grep gap affects these rows (a saved full-repo grep is still owed before merging any UNREACHABLE row elsewhere, not here).

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 109 only, max 40 methods, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior proposal (`~/workspace/libretorrent-batch109-proposal.md`) was used as an INPUT / lead list only; every row below was re-checked against source freshly fetched in this pass, and no proposal verdict was copied as a result.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 109 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA `0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy). All 40 batch-109 rows are `TODO_CANDIDATE_REACHABLE` in the plan (generator candidates, not evidence), in plan order: MainActivity rows 1–22, MainFragment rows 23–40. Descriptors in the table are the plan JVM descriptors, rendered in short form.

## Printed source used in this pass

Fresh connector fetches from branch `work-2026-10-31`, one file at a time with pauses, saved in `~/workspace/b109-110-src/` (all under `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/` unless noted):

- `ui/main/MainActivity.java` — fresh, blob SHA `d21f8b70fb50fa09c7b3708243c4f251176f4517`, 811 lines, byte-identical to the local copy in `~/workspace/b27scratch/MainActivity.java`.
- `ui/main/MainFragment.java` — fresh, blob SHA `1fd79b7ac163670dc28de85cbfb5186c3a95ced8`, 637 lines, byte-identical to the local copy in `~/workspace/b27scratch/MainFragment.java`.
- `src/main/AndroidManifest.xml` — fresh, blob SHA `875a8aa7de97caac5d9457836b0ea30f1c3d51ea`, 295 lines, byte-identical to the local copy in `~/workspace/b27scratch/AndroidManifest.xml`.

No fresh HTTP 429 was hit in this pass. No connector `search_code` result was used as evidence for any row.

## Entry trunk — printed, no strict-entry revert

Launcher → MainActivity: `AndroidManifest.xml:43` declares `.ui.main.MainActivity`, with `MAIN`/`LAUNCHER` at :53–55 → `MainActivity.onCreate` → `findFragmentById(R.id.main_fragmentContainer)` at MainActivity.java:184–185 (MainFragment is layout-hosted; no printed `new MainFragment()` exists, which is why MainFragment `<init>` is INFERRED, not SOURCE) → `initLayout` → `showBlankFragment` at MainActivity.java:192. `MainActivity.onStart:383–388` calls all five `subscribe*` methods; `MainFragment.onStart:233–241` calls its five `subscribe*` methods. Unlike earlier batches, the launcher step IS printed, so no row in this batch reverts to OPEN under a strict launcher-entry rule.

## confirmed_by convention used here (recorded, not decided)

Per-row immediate-caller rule, as in the prior proposal: SOURCE = the method is called directly by printed app code (a direct call, or a call written in a printed method/lambda body). INFERRED = the method is only invoked by framework/library dispatch with no printed app call site (Android lifecycle, listener interfaces, Rx operator emission, widget dispatch, JVM class initialisation). This differs from the whole-route INFERRED convention used in some other batches; labels are unaffected, only `confirmed_by` would change at merge if the merger adopts the whole-route convention. That convention choice is UNDECIDED and is not decided here.

## Rows

| # | Method | Proposed label | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | MainActivity.showBlankFragment ()V | REACHABLE | SOURCE | Called directly in `initLayout` (MainActivity.java:192); also `subscribeMsgViewModel:444,452`. Definition :676. |
| 2 | MainActivity.showDetailTorrent (String)V | REACHABLE | INFERRED | Only via Rx method reference `.subscribe(this::showDetailTorrent)` at MainActivity.java:438–440 (details-opened stream); Rx emission not printed. Definition :653. |
| 3 | MainActivity.showLog ()V | REACHABLE | SOURCE | Direct call in `onOptionsItemSelected` log-menu branch, MainActivity.java:755. Definition :801 (starts LogActivity). |
| 4 | MainActivity.subscribeAlertDialog ()V | REACHABLE | SOURCE | Direct call in `onStart`, MainActivity.java:384. Definition :406. |
| 5 | MainActivity.subscribeMsgViewModel ()V | REACHABLE | SOURCE | Direct call in `onStart`, MainActivity.java:385. Definition :437. |
| 6 | MainActivity.subscribeNeedStartEngine ()V | REACHABLE | SOURCE | Direct call in `onStart`, MainActivity.java:387. Definition :463. |
| 7 | MainActivity.subscribeSessionStats ()V | REACHABLE | SOURCE | Direct call in `onStart`, MainActivity.java:386. Definition :456. |
| 8 | MainActivity.subscribeTags ()V | REACHABLE | SOURCE | Direct call in `onStart`, MainActivity.java:388. Definition :470. |
| 9 | MainActivity.updateSessionStats (SessionStats)V | REACHABLE | INFERRED | Only via Rx method reference `.subscribe(this::updateSessionStats)` at MainActivity.java:457–460 (session-stats stream); Rx emission not printed. Definition :529. |
| 10 | MainActivity$1.<init> (MainActivity, FragmentManager)V | REACHABLE | SOURCE | Direct construction `new PermissionManager(this, new PermissionManager.Callback() {...})` in `onCreate`, MainActivity.java:153. $1 = the PermissionManager.Callback anonymous class. |
| 11 | MainActivity$1.onNotificationResult (ZZ)V | REACHABLE | INFERRED | Callback method at MainActivity.java:167; invoked by PermissionManager on a permission result — PermissionManager dispatch code not printed. |
| 12 | MainActivity$1.onStorageResult (ZZ)V | REACHABLE | INFERRED | Callback method at MainActivity.java:155; same PermissionManager dispatch, not printed. |
| 13 | MainActivity$2.<init> (MainActivity, Context)V | REACHABLE | SOURCE | Direct construction `new LinearLayoutManager(this) {...}` in `initLayout`, MainActivity.java:198. $2 = the LinearLayoutManager anonymous subclass (outer + Context ctor args match the descriptor). |
| 14 | MainActivity$2.canScrollVertically ()Z | REACHABLE | INFERRED | Override at MainActivity.java:200 (`return false`, RecyclerView wrapped in ScrollView); invoked by RecyclerView layout, not by printed app code. |
| 15 | MainActivity$3.<init> (MainActivity)V | REACHABLE | SOURCE | Field `tagsClickListener = new TagsAdapter.OnClickListener() {...}` at MainActivity.java:295, passed to `new TagsAdapter(tagsClickListener)` at :271. $3 = that listener. |
| 16 | MainActivity$3.lambda$onTagMenuClicked$0 (TagItem)V | REACHABLE | INFERRED | Success lambda of the `deleteTag` Rx subscribe inside `onTagMenuClicked` (MainActivity.java:326–345): `() -> {...}` capturing local `item` (TagItem), which is why the synthetic descriptor is (TagItem)V; invoked by Rx on success, not by printed app code. |
| 17 | MainActivity$3.lambda$onTagMenuClicked$1 (Throwable)V | REACHABLE | INFERRED | Error lambda of the same `deleteTag` subscribe (MainActivity.java:341–345, logs + Snackbar via `mainFragment.getCoordinatorLayout()`); invoked by Rx on error. |
| 18 | MainActivity$3.onTagMenuClicked (AbstractTagItem, I)V | REACHABLE | INFERRED | Listener method at MainActivity.java:316 (edit/delete tag branches); invoked by TagsAdapter on a tag menu click — TagsAdapter dispatch not printed. |
| 19 | MainActivity$3.onTagSelected (AbstractTagItem)V | REACHABLE | INFERRED | Listener method at MainActivity.java:297 (sets tag filter, saves selection, closes drawer); invoked by TagsAdapter on tag selection — dispatch not printed. |
| 20 | MainActivity$4.<init> (MainActivity)V | REACHABLE | SOURCE | Direct construction `new SearchView.OnQueryTextListener() {...}` via `searchView.setOnQueryTextListener(...)` in `initSearch`, MainActivity.java:714 (`initSearch` definition :707). $4 = that listener. |
| 21 | MainActivity$4.onQueryTextChange (String)Z | REACHABLE | INFERRED | Listener method at MainActivity.java:725 (`viewModel.setSearchQuery`); invoked by SearchView on text change — framework dispatch not printed. |
| 22 | MainActivity$4.onQueryTextSubmit (String)Z | REACHABLE | INFERRED | Listener method at MainActivity.java:716 (`setSearchQuery`, clearFocus); invoked by SearchView on submit. |
| 23 | MainFragment.<clinit> ()V | REACHABLE | INFERRED | JVM class initialisation (e.g. `TAG = MainFragment.class.getSimpleName()` at MainFragment.java:88); class loaded when the launcher activity hosts the fragment. No app call site exists for `<clinit>` by nature. |
| 24 | MainFragment.<init> ()V | REACHABLE | INFERRED | Framework fragment instantiation; MainActivity obtains the fragment via `findFragmentById(R.id.main_fragmentContainer)` at MainActivity.java:184–185, i.e. the fragment is layout-hosted, but no printed `new MainFragment()` exists. |
| 25 | MainFragment.addLinkDialog ()V | REACHABLE | SOURCE | Direct calls in `onContextItemSelected` add-link branch (MainFragment.java:402–411) and in the FAB listener branch (MainFragment.java:414–430). Definition :523 (starts AddLinkActivity). |
| 26 | MainFragment.createTorrentDialog ()V | REACHABLE | SOURCE | Direct call in the FAB listener branch (MainFragment.java:414–430, `main_fab_create_torrent`). Definition :561 (starts CreateTorrentActivity). |
| 27 | MainFragment.deleteTorrents ()V | REACHABLE | SOURCE | Direct call in the dialog-event lambda body in `subscribeAlertDialog` (MainFragment.java:302–323, delete-dialog positive click). Definition :566. |
| 28 | MainFragment.deleteTorrentsDialog ()V | REACHABLE | SOURCE | Direct call in `actionModeCallback.onActionItemClicked` delete-menu branch (MainFragment.java:475–479). Definition :501 (builds and shows the delete dialog at :508–519). |
| 29 | MainFragment.forceAnnounceTorrents ()V | REACHABLE | SOURCE | Direct call in `actionModeCallback.onActionItemClicked` force-announce branch (MainFragment.java:475–490). Definition :608. |
| 30 | MainFragment.forceRecheckTorrents ()V | REACHABLE | SOURCE | Direct call in `actionModeCallback.onActionItemClicked` force-recheck branch (MainFragment.java:475–490). Definition :597. |
| 31 | MainFragment.getAllTorrentsSingle ()Disposable | REACHABLE | SOURCE | Direct call in the subscribe lambda body in `subscribeForceSortAndFilter` (MainFragment.java:330). Definition :333. |
| 32 | MainFragment.getCoordinatorLayout ()CoordinatorLayout | REACHABLE | SOURCE | Direct call in MainActivity's tag-delete error lambda (`mainFragment.getCoordinatorLayout()`, MainActivity.java:341). Definition MainFragment.java:109. |
| 33 | MainFragment.initFabSpeedDial ()V | REACHABLE | SOURCE | Direct call in `onViewCreated` (MainFragment.java:200). Definition :414. |
| 34 | MainFragment.lambda$deleteTorrents$12 (TorrentListItem)String | REACHABLE | INFERRED | Map lambda `selection -> selection.torrentId` in `deleteTorrents` (MainFragment.java:578–582); invoked by Rx `map`, not by printed app code. |
| 35 | MainFragment.lambda$deleteTorrents$13 (Z, List)V | REACHABLE | INFERRED | Subscribe lambda in `deleteTorrents` (`viewModel.deleteTorrents(ids, withFiles)`, MainFragment.java:583); captured `withFiles` explains the (Z, List) descriptor; invoked by Rx on emission. |
| 36 | MainFragment.lambda$forceAnnounceTorrents$16 (TorrentListItem)String | REACHABLE | INFERRED | Map lambda in `forceAnnounceTorrents` (MainFragment.java:613–615); invoked by Rx `map`. |
| 37 | MainFragment.lambda$forceAnnounceTorrents$17 (List)V | REACHABLE | INFERRED | Subscribe lambda in `forceAnnounceTorrents` (`viewModel.forceAnnounceTorrents(ids)`, MainFragment.java:616); invoked by Rx. |
| 38 | MainFragment.lambda$forceRecheckTorrents$14 (TorrentListItem)String | REACHABLE | INFERRED | Map lambda in `forceRecheckTorrents` (MainFragment.java:602–604); invoked by Rx `map`. |
| 39 | MainFragment.lambda$forceRecheckTorrents$15 (List)V | REACHABLE | INFERRED | Subscribe lambda in `forceRecheckTorrents` (`viewModel.forceRecheckTorrents(ids)`, MainFragment.java:605); invoked by Rx. |
| 40 | MainFragment.lambda$getAllTorrentsSingle$6 (List)SingleSource | REACHABLE | INFERRED | FlatMap lambda in `getAllTorrentsSingle` (MainFragment.java:336–343, filter/map/sort to list); invoked by Rx `flatMap`. |

## Counts — mechanically verified

- REACHABLE proposed: 40 (SOURCE 20, INFERRED 20 — counted from the table above)
- UNREACHABLE proposed: 0
- OPEN: 0
- Total: 40/40 judged, sequence 1–40 intact, in plan order.

## Caveats / still owed before merge

- Anonymous-class numbering ($1–$4 in MainActivity, by construction order and constructor descriptors in the printed files) was matched by construction order; the merger should confirm it against bytecode if the numbering is ever disputed. Labels are unaffected by a swap within a group, and the descriptor matches already checked (captured `item` for row 16, captured `withFiles` for row 35) pin the lambda identities.
- Row 33 corrected against the prior proposal: the `initFabSpeedDial` call is at MainFragment.java:200 inside `onViewCreated` (definition :125); the prior proposal's ":125 ff." was the definition site, not the call line.
- No competing `MainActivity`/`MainFragment` definition was printed elsewhere in this pass; the merger should still confirm no competing definition exists elsewhere in the checkout, as with any batch.
- Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run here.
- **0 rows verified for merge.**
