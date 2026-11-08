**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 87 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 87 only, LibreTorrent labels only, no other batch/app, no device replay, no Aegis.
- Task: labels only, from printed source. The prior proposal
  (`~/workspace/libretorrent-batch87-proposal.md`) was used as an INPUT / lead list only;
  rows below were re-judged in this session against source freshly fetched from the branch,
  and no proposal verdict was copied as a result.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 87 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, plan git blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92` (local copy `~/workspace/agent27-plan.tsv`;
raw sha1 `afedc8af26f…` is the same file — the git blob SHA differs from the raw file hash by
construction, not by content), all status TODO_CANDIDATE_REACHABLE, all current label
"REACHABLE (generator candidate, no hand route yet)" — candidates, not evidence.
Method names, JVM descriptors, and order in the table below match the plan row for row
(tables generated from the plan TSV in this session, so names/descriptors/order cannot drift).

## Sources freshly printed in this pass (branch work-2026-10-31, GitHub connector, one file at a time with ~20-30 s pauses, no fresh HTTP 429)

Saved in `~/workspace/b8788-src/` (base path for all files:
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`):
- `ui/detailtorrent/DetailTorrentFragment.java` — 832 lines, connector SHA `c24e0912e62088e962894f04ee427bbe317e83e7`, byte-identical to the prior proposal's copy.
- `ui/detailtorrent/DetailTorrentActivity.java` — 120 lines, connector SHA `0ce85b2597300c719bb2e97c7da9e209e7575a39`.
- `ui/detailtorrent/DetailTorrentViewModel.java` — 610 lines, connector SHA `6e4ef82f455957298bfb6bf4513c4a35c799a1a6`, byte-identical to the prior proposal's copy.
- `ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java` — 543 lines, connector SHA `a1f2ccc63a8b38c9ddf7ba95c6cb60db5b7f56b7`.
- `ui/detailtorrent/pages/DetailTorrentInfoFragment.java` — 324 lines, connector SHA `f7d056f5f960c5a7097cf50385ed0ac92dc0595e`, byte-identical to the prior proposal's copy.
- `ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java` — 406 lines, connector SHA `48d5a5360febbf5e8ac10f6b08d106d88aff0126`.
- `ui/main/MainActivity.java` — 811 lines, connector SHA `d21f8b70fb50fa09c7b3708243c4f251176f4517`, byte-identical to the batch 109-110 copy.
- One clean file-not-found, NOT a 429 and NOT retried in a loop: `ui/detailtorrent/pages/info/DetailTorrentInfoFragment.java`
  does not exist; the info fragment is at `ui/detailtorrent/pages/DetailTorrentInfoFragment.java` (fetched fresh above).
- True git clone: NOT attempted and NOT passed — a true git clone fails in this VM (no credential device);
  all evidence here is connector-fetched branch files, named as such. No `search_code` result was used
  anywhere in this pass, and no `search_code` 0 was used as evidence of absence.

## What changed vs the prior proposal (39 REACHABLE / 0 UNREACHABLE / 1 OPEN)

Exactly one verdict changed, on fresh evidence: row 22 `DetailTorrentFragment.newInstance` flips OPEN ->
REACHABLE SOURCE (MainActivity:656, two-pane branch of showDetailTorrent; see table). All other 39 rows keep
their proposal verdicts, but every citation was re-checked against the freshly fetched Fragment/Activity prints
(SHA-identical to the proposal copies, so line numbers carry over unchanged) — no proposal verdict was copied
without that check. No row was flipped to UNREACHABLE: no saved full-repo grep was run, and none is claimed.

## Table

| # | Method | JVM descriptor | Label | confirmed_by | Printed route / citation |
|---|---|---|---|---|---|
| 1 | DetailTorrentFragment.addTrackersDialog | `()V` | REACHABLE | SOURCE | Fragment:470 onOptionsItemSelected -> addTrackersDialog(); def :518-533 (BaseAlertDialog). |
| 2 | DetailTorrentFragment.checkAddTrackersField | `(Ljava/util/List;Lcom/google/android/material/textfield/TextInputLayout;Lcom/google/android/material/textfield/TextInputEditText;)Z` | REACHABLE | SOURCE | Fragment:709 and :714 addTrackers() -> checkAddTrackersField(urls, fieldLayout, field); def :644-687. |
| 3 | DetailTorrentFragment.deleteTorrent | `()V` | REACHABLE | SOURCE | Fragment:307 subscribeAlertDialog POSITIVE + TAG_DELETE_TORRENT_DIALOG -> deleteTorrent(); def :586-594 -> viewModel.deleteTorrent. |
| 4 | DetailTorrentFragment.deleteTorrentDialog | `()V` | REACHABLE | SOURCE | Fragment:460 onOptionsItemSelected -> deleteTorrentDialog(); def :478-496. |
| 5 | DetailTorrentFragment.finish | `(Landroid/content/Intent;Lorg/proninyaroslav/libretorrent/ui/FragmentCallback$ResultCode;)V` | REACHABLE | SOURCE | Fragment:824 onBackPressed -> finish(...,BACK); :262 subscribeTorrentInfo error lambda -> finish(...,CANCEL); def :827-831 -> (FragmentCallback)activity.onFragmentFinished (interface cast; host impls freshly printed: DetailTorrentActivity:108-118, MainActivity:806). FragmentCallback convention (viii) recorded, not decided: the finish() row itself has printed callers; only the interface dispatch step is unprinted. |
| 6 | DetailTorrentFragment.getTorrentId | `()Ljava/lang/String;` | REACHABLE | SOURCE | Activity:102 subscribeTorrentDeleted lambda -> detailTorrentFragment.getTorrentId(); def Fragment:124-127. |
| 7 | DetailTorrentFragment.handleTorrentInfo | `(Landroidx/core/util/Pair;)V` | REACHABLE | SOURCE | Fragment:268 subscribeTorrentInfo method ref this::handleTorrentInfo; def :356-379. |
| 8 | DetailTorrentFragment.initAddTrackersDialog | `()V` | REACHABLE | SOURCE | Fragment:347 subscribeAlertDialog DIALOG_SHOWN + TAG_ADD_TRACKERS_DIALOG -> initAddTrackersDialog(); def :608-641. |
| 9 | DetailTorrentFragment.initSpeedLimitDialog | `()V` | REACHABLE | SOURCE | Fragment:349 DIALOG_SHOWN + TAG_SPEED_LIMIT_DIALOG -> initSpeedLimitDialog(); def :739-764. |
| 10 | DetailTorrentFragment.lambda$addTrackers$10 | `(Ljava/lang/String;)Z` | REACHABLE | INFERRED | Fragment:~706 addTrackers() Observable.fromArray(...).filter((s) -> !s.isEmpty()); lambda number by source order, NOT bytecode-verified. |
| 11 | DetailTorrentFragment.lambda$new$11 | `(Landroidx/activity/result/ActivityResult;)V` | REACHABLE | INFERRED | Fragment:795-820 saveTorrentFileChoose ActivityResultLauncher callback -> saveErrorTorrentFileDialog / viewModel.copyTorrentFile; lambda number by source order, NOT bytecode-verified. |
| 12 | DetailTorrentFragment.lambda$onViewCreated$0 | `(Landroid/view/View;)V` | REACHABLE | INFERRED | Fragment:183 toolbar.setNavigationOnClickListener((v) -> onBackPressed()); lambda number by source order, NOT bytecode-verified. |
| 13 | DetailTorrentFragment.lambda$onViewCreated$1 | `(Lcom/google/android/material/tabs/TabLayout$Tab;I)V` | REACHABLE | INFERRED | Fragment:188-209 TabLayoutMediator callback (tab, position) -> setText per DetailPagerAdapter position; lambda number by source order, NOT bytecode-verified. |
| 14 | DetailTorrentFragment.lambda$subscribeAlertDialog$9 | `(Lorg/proninyaroslav/libretorrent/ui/BaseAlertDialog$Event;)V` | REACHABLE | INFERRED | Fragment:299-351 subscribeAlertDialog dialogViewModel.observeEvents().subscribe((event) -> switch on type/tag) -> deleteTorrent/shareMagnet/addTrackers/setSpeedLimit/init dialogs; lambda number by source order, NOT bytecode-verified. |
| 15 | DetailTorrentFragment.lambda$subscribeFreeSpaceError$8 | `(Ljava/lang/Boolean;)V` | REACHABLE | INFERRED | Fragment:290-295 subscribeFreeSpaceError .subscribe(__ -> showFreeSpaceErrorToast()); lambda number by source order, NOT bytecode-verified. |
| 16 | DetailTorrentFragment.lambda$subscribeMsgViewModel$7 | `(Ljava/lang/Boolean;)V` | REACHABLE | INFERRED | Fragment:278-287 subscribeMsgViewModel .subscribe((inActionMode) -> setTabLayoutColor(...)); lambda number by source order, NOT bytecode-verified. |
| 17 | DetailTorrentFragment.lambda$subscribeTorrentInfo$2 | `(Lorg/proninyaroslav/libretorrent/core/model/data/metainfo/TorrentMetaInfo;)V` | REACHABLE | INFERRED | Fragment:256-263 observeTorrentMetaInfo .subscribe((metaInfo) -> viewModel.updateInfo(metaInfo), error lambda); lambda number by source order, NOT bytecode-verified. |
| 18 | DetailTorrentFragment.lambda$subscribeTorrentInfo$3 | `(Ljava/lang/Throwable;)V` | REACHABLE | INFERRED | Fragment:260-263 meta-info error lambda -> finish(...,CANCEL); lambda number by source order, NOT bytecode-verified. |
| 19 | DetailTorrentFragment.lambda$subscribeTorrentInfo$4 | `(Ljava/lang/Throwable;)V` | REACHABLE | INFERRED | Fragment:265-269 observeTorrentInfoPair error lambda (onNext is method ref handleTorrentInfo); lambda number by source order, NOT bytecode-verified. |
| 20 | DetailTorrentFragment.lambda$subscribeTorrentInfo$5 | `(Lorg/proninyaroslav/libretorrent/core/model/data/AdvancedTorrentInfo;)V` | REACHABLE | INFERRED | Fragment:271-275 observeAdvancedTorrentInfo .subscribe((info) -> viewModel.updateInfo(info), error lambda); lambda number by source order, NOT bytecode-verified. |
| 21 | DetailTorrentFragment.lambda$subscribeTorrentInfo$6 | `(Ljava/lang/Throwable;)V` | REACHABLE | INFERRED | Fragment:275 advanced-info error lambda (log only); lambda number by source order, NOT bytecode-verified. |
| 22 | DetailTorrentFragment.newInstance | `(Ljava/lang/String;)Lorg/proninyaroslav/libretorrent/ui/detailtorrent/DetailTorrentFragment;` | REACHABLE | SOURCE | FLIP vs prior proposal (OPEN -> REACHABLE, fresh in this pass): MainActivity:656 showDetailTorrent two-pane branch (Utils.isTwoPane) -> DetailTorrentFragment.newInstance(id), then fragment replace :665-668; showDetailTorrent itself subscribed at MainActivity:440 (msgViewModel.observeTorrentDetailsOpened -> this::showDetailTorrent); def Fragment:115-121 (new DetailTorrentFragment + setTorrentId). Single-pane branch :670-672 instead starts DetailTorrentActivity — the newInstance route is two-pane only, a printed configuration branch, not OPEN. |
| 23 | DetailTorrentFragment.onAttach | `(Landroid/content/Context;)V` | REACHABLE | INFERRED | Def Fragment:139-145; standard Fragment lifecycle, host Activity:67-68 finds the fragment; framework dispatch NOT printed from fw_src. |
| 24 | DetailTorrentFragment.onBackPressed | `()V` | REACHABLE | SOURCE | Fragment:456 menu home -> onBackPressed(); :183 nav click lambda -> onBackPressed(); def :822-825 -> finish(...,BACK). |
| 25 | DetailTorrentFragment.onCreateOptionsMenu | `(Landroid/view/Menu;Landroid/view/MenuInflater;)V` | REACHABLE | INFERRED | Def Fragment:413-418 inflates R.menu.detail_torrent; setHasOptionsMenu at :179 (single-pane branch); framework menu dispatch NOT printed from fw_src. |
| 26 | DetailTorrentFragment.onCreateView | `(Landroid/view/LayoutInflater;Landroid/view/ViewGroup;Landroid/os/Bundle;)Landroid/view/View;` | REACHABLE | INFERRED | Def Fragment:148-153 DataBindingUtil.inflate fragment_detail_torrent; standard framework lifecycle. |
| 27 | DetailTorrentFragment.onOptionsItemSelected | `(Landroid/view/MenuItem;)Z` | REACHABLE | SOURCE | Fragment:174 toolbar.setOnMenuItemClickListener(this::onOptionsItemSelected) in two-pane branch; def :452-476 dispatches to delete/share/save/addTrackers/speedLimit dialogs. Single-pane path is framework menu dispatch via setHasOptionsMenu :179 (not printed from fw_src); label stands on the printed registration + definition. |
| 28 | DetailTorrentFragment.onPrepareOptionsMenu | `(Landroid/view/Menu;)V` | REACHABLE | INFERRED | Def Fragment:421-426 -> prepareOptionsMenu(menu); framework dispatch NOT printed from fw_src. |
| 29 | DetailTorrentFragment.onSaveInstanceState | `(Landroid/os/Bundle;)V` | REACHABLE | INFERRED | Def Fragment:243-249 puts torrent id + currentFragPos; standard framework lifecycle. |
| 30 | DetailTorrentFragment.onStart | `()V` | REACHABLE | INFERRED | Def Fragment:224-233 -> subscribeTorrentInfo/AlertDialog/MsgViewModel/FreeSpaceError; standard framework lifecycle. |
| 31 | DetailTorrentFragment.onStop | `()V` | REACHABLE | INFERRED | Def Fragment:235-240 disposables.clear(); standard framework lifecycle. |
| 32 | DetailTorrentFragment.onViewCreated | `(Landroid/view/View;Landroid/os/Bundle;)V` | REACHABLE | INFERRED | Def Fragment:156-222: ViewModelProvider, viewModel.setTorrentId, toolbar/menu, pager adapter, dialog fragment lookup; framework lifecycle after onCreateView. |
| 33 | DetailTorrentFragment.prepareOptionsMenu | `(Landroid/view/Menu;)V` | REACHABLE | SOURCE | Fragment:425 onPrepareOptionsMenu -> prepareOptionsMenu; :375 handleTorrentInfo -> prepareOptionsMenu (two-pane); def :428-450. |
| 34 | DetailTorrentFragment.saveErrorTorrentFileDialog | `(Ljava/lang/Exception;)V` | REACHABLE | SOURCE | Fragment:803 and :817 lambda$new$11 result handler -> saveErrorTorrentFileDialog(null / e); def :548-564. |
| 35 | DetailTorrentFragment.setSpeedLimit | `()V` | REACHABLE | SOURCE | Fragment:324 dialog POSITIVE + TAG_SPEED_LIMIT_DIALOG -> setSpeedLimit(); def :766-793 -> viewModel.setSpeedLimit. |
| 36 | DetailTorrentFragment.setTabLayoutColor | `(I)V` | REACHABLE | SOURCE | Fragment:282 subscribeMsgViewModel lambda -> setTabLayoutColor(...); def :381-386 (two-pane early return :382-383; the method still runs). |
| 37 | DetailTorrentFragment.setTorrentId | `(Ljava/lang/String;)V` | REACHABLE | SOURCE | Activity:71 onCreate -> setTorrentId(intent extra); Fragment:118 newInstance -> setTorrentId; def Fragment:129-132. |
| 38 | DetailTorrentFragment.shareMagnet | `(Z)V` | REACHABLE | SOURCE | Fragment:310 dialog POSITIVE magnet dialog -> shareMagnet(true); :332 NEGATIVE -> shareMagnet(false); def :596-606 -> viewModel.makeMagnet + share Intent. |
| 39 | DetailTorrentFragment.shareMagnetDialog | `()V` | REACHABLE | SOURCE | Fragment:466 onOptionsItemSelected -> shareMagnetDialog(); def :498-515. |
| 40 | DetailTorrentFragment.showFiles | `()V` | REACHABLE | SOURCE | Activity:73-75 ACTION_OPEN_FILES -> detailTorrentFragment.showFiles(); def Fragment:134-137 sets currentFragPos = FILES_FRAG_POS. |

- **Counts (mechanically verified): 40 REACHABLE proposed / 0 UNREACHABLE proposed / 0 OPEN, out of 40.**
- Among REACHABLE: SOURCE 20 / INFERRED 20.
- **0 / 40 verified for merge.** Main-agent spot-check (1 in 5), `py_compile`, build, sampler, full-repo grep, and Mac build/C1 are all outstanding and are marked not run, never passed.

## Conventions recorded per row, NOT decided (merger must pick one, project-wide)

- **Strict-entry:** all REACHABLE rows in this batch anchor at DetailTorrentActivity / DetailTorrentFragment /
  its ViewModel / its pager child fragments (Info, Files, Trackers) / MainActivity.showDetailTorrent.
  No launcher -> MainActivity step was freshly printed in THIS pass (batches 109-110 printed it, but that
  print is not fresh evidence here). Under a strict printed-launcher-entry rule all REACHABLE rows revert
  to OPEN; under the sibling-batch anchor convention they stand as tabled.
- **confirmed_by:** per-row SOURCE (a printed app-code line names the method, including a printed call site inside
  a lambda/callback body or an internal call from a REACHABLE method) vs INFERRED (unprinted framework/library/
  Rx/ViewPager2/TextWatcher/WorkManager dispatch, ViewModelProvider instantiation, <clinit>, or lambda/anonymous
  numbering). Under a whole-route INFERRED convention, SOURCE rows crossing unprinted dispatch would read
  INFERRED; labels are unaffected.
- **Lambda / anonymous numbering:** source-order / construction-order only, NOT bytecode-verified. A swap within a
  group would not change any label (all bodies in each group sit inside a single printed registration/subscription).
- **FragmentCallback (convention viii family):** batch 87 row 5 `finish()` dispatches via an interface cast
  (`(FragmentCallback)activity.onFragmentFinished`, Fragment:830); host implementations are freshly printed
  (DetailTorrentActivity:108-118, MainActivity:806). The row is SOURCE on its printed callers (:262, :824);
  only the interface-dispatch step is unprinted. This is NOT the same row as the `onFragmentFinished` rows
  in batches 82/86/108/114 (those are the host-side method itself).
- **<clinit> on first-use (convention ix):** batch 88 row 16 rests on non-constant `TAG = getSimpleName()`
  (ViewModel:82) plus first use via `provider.get` (Fragment:164-165). Whether that suffices project-wide is
  undecided; the row reverts to OPEN if the merger requires more.
- **Two-pane configuration branch:** batch 87 row 22 (`newInstance`) and the two-pane-only paths (Fragment:174
  toolbar listener, :166 clearData gate) run only when `Utils.isTwoPane` is true; the single-pane branch instead
  starts DetailTorrentActivity. That is a printed configuration branch, not an OPEN verdict — the rows are
  REACHABLE on the two-pane configuration, and the merger must not treat a config branch as absence.

## Still owed before merge

- Saved full-repo grep before any OPEN -> UNREACHABLE flip (no OPEN rows remain in this batch, and no
  UNREACHABLE is claimed, so no grep is owed for a flip — but the merger's usual full-repo consistency grep
  for the batch is still outstanding).
- Printed launcher -> MainActivity step, if the merger applies the strict-entry rule.
- Lambda/anonymous numbering confirmed against bytecode, if the merger requires it.
- Main-agent spot-check 1 in 5, `py_compile`, build, sampler, Mac build/C1 — all not run.
- Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]); pushed UNVERIFIED before [L] at user request 2026-11-01.

