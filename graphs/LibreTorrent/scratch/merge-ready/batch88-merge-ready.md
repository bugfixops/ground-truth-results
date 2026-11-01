**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 88 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 88 only, LibreTorrent labels only, no other batch/app, no device replay, no Aegis.
- Task: labels only, from printed source. The prior proposal
  (`~/workspace/libretorrent-batch88-proposal.md`) was used as an INPUT / lead list only;
  rows below were re-judged in this session against source freshly fetched from the branch,
  and no proposal verdict was copied as a result.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 88 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, plan git blob SHA
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

## What changed vs the prior proposal (29 REACHABLE / 0 UNREACHABLE / 11 OPEN)

All 11 OPEN rows flip to REACHABLE SOURCE on freshly fetched child-fragment / ViewModel-internal prints (the
prior proposal printed only the Fragment, ViewModel, and Activity, so child-fragment callers were missed):
row 18 addTag (InfoFragment:139), row 20 applyPriority (FilesFragment:353, :502), row 23 chooseDirectory
(FilesFragment:338), row 27 deleteTrackers (TrackersFragment:368, via alert-dialog POSITIVE :279),
row 30 getChildren (ViewModel:608 updateChildren, via chooseDirectory chain), row 31 getDirChildren
(FilesFragment:156), row 33 getFilePath (FilesFragment:340), row 35 getFilesPriority (FilesFragment:449),
row 36 getStreamUrl (FilesFragment:522), row 37 getTags (InfoFragment:150), row 40 isFile (FilesFragment:375).
All other 29 rows keep their proposal verdicts, with every citation re-checked against the freshly fetched
prints (Fragment/Activity/ViewModel SHAs identical to the proposal copies, so line numbers carry over unchanged).
No row was flipped to UNREACHABLE: no saved full-repo grep was run, and none is claimed. Child fragments are
hosted by DetailPagerAdapter (batch 91-92 prints: createFragment returns Info/State/Files/Trackers/Peers/Pieces
fragments) set on the ViewPager2 at Fragment:186-187, so their routes anchor at DetailTorrentFragment itself.

## Table

| # | Method | JVM descriptor | Label | confirmed_by | Printed route / citation |
|---|---|---|---|---|---|
| 1 | DetailTorrentFragment.showFreeSpaceErrorToast | `()V` | REACHABLE | SOURCE | Fragment:294 subscribeFreeSpaceError lambda -> showFreeSpaceErrorToast(); def :404-410 Snackbar error_free_space. |
| 2 | DetailTorrentFragment.speedLimitDialog | `()V` | REACHABLE | SOURCE | Fragment:472 onOptionsItemSelected -> speedLimitDialog(); def :566-584. |
| 3 | DetailTorrentFragment.subscribeAlertDialog | `()V` | REACHABLE | SOURCE | Fragment:229 onStart -> subscribeAlertDialog(); def :297-354. |
| 4 | DetailTorrentFragment.subscribeFreeSpaceError | `()V` | REACHABLE | SOURCE | Fragment:231 onStart -> subscribeFreeSpaceError(); def :290-295. |
| 5 | DetailTorrentFragment.subscribeMsgViewModel | `()V` | REACHABLE | SOURCE | Fragment:230 onStart -> subscribeMsgViewModel(); def :278-287. |
| 6 | DetailTorrentFragment.subscribeTorrentInfo | `()V` | REACHABLE | SOURCE | Fragment:228 onStart -> subscribeTorrentInfo(); def :251-276. |
| 7 | DetailTorrentFragment.torrentSaveChooseDialog | `()V` | REACHABLE | SOURCE | Fragment:468 onOptionsItemSelected -> torrentSaveChooseDialog(); def :535-546 saveTorrentFileChoose.launch. |
| 8 | DetailTorrentFragment$1.<init> | `(Lorg/proninyaroslav/libretorrent/ui/detailtorrent/DetailTorrentFragment;)V` | REACHABLE | INFERRED | Anonymous ViewPager2.OnPageChangeCallback field Fragment:389; registered :187 registerOnPageChangeCallback(viewPagerListener); numbering by construction order in source, NOT bytecode-verified. |
| 9 | DetailTorrentFragment$1.onPageScrollStateChanged | `(I)V` | REACHABLE | INFERRED | Fragment:401 empty override in the $1 callback; standard ViewPager2 callback dispatch, NOT printed from fw_src. |
| 10 | DetailTorrentFragment$1.onPageScrolled | `(IFI)V` | REACHABLE | INFERRED | Fragment:392 empty override in the $1 callback; standard ViewPager2 callback dispatch, NOT printed from fw_src. |
| 11 | DetailTorrentFragment$1.onPageSelected | `(I)V` | REACHABLE | INFERRED | Fragment:395-398 override sets currentFragPos = position; standard ViewPager2 callback dispatch, NOT printed from fw_src. |
| 12 | DetailTorrentFragment$2.<init> | `(Lorg/proninyaroslav/libretorrent/ui/detailtorrent/DetailTorrentFragment;Lcom/google/android/material/textfield/TextInputLayout;Lcom/google/android/material/textfield/TextInputEditText;)V` | REACHABLE | INFERRED | Anonymous TextWatcher in Fragment:618-641 initAddTrackersDialog, registered field.addTextChangedListener(:618); numbering by construction order in source, NOT bytecode-verified. |
| 13 | DetailTorrentFragment$2.afterTextChanged | `(Landroid/text/Editable;)V` | REACHABLE | INFERRED | Fragment:627-640 override clears error label + error spans; standard TextWatcher dispatch via the :618 registration. |
| 14 | DetailTorrentFragment$2.beforeTextChanged | `(Ljava/lang/CharSequence;III)V` | REACHABLE | INFERRED | Fragment:621 empty override; standard TextWatcher dispatch via :618. |
| 15 | DetailTorrentFragment$2.onTextChanged | `(Ljava/lang/CharSequence;III)V` | REACHABLE | INFERRED | Fragment:624 empty override; standard TextWatcher dispatch via :618. |
| 16 | DetailTorrentViewModel.<clinit> | `()V` | REACHABLE | INFERRED | No explicit static block printed; ViewModel:82 static final TAG = DetailTorrentViewModel.class.getSimpleName() is the <clinit> body. Class loaded by Fragment:164-165 provider.get(DetailTorrentViewModel.class); class-load step itself is framework, NOT printed. Convention (ix) recorded, NOT decided: reverts to OPEN if the merger requires more than non-constant TAG + first use. |
| 17 | DetailTorrentViewModel.<init> | `(Landroid/app/Application;)V` | REACHABLE | INFERRED | Fragment:164-165 provider.get(DetailTorrentViewModel.class); def ViewModel:104-117 (super + TorrentInfoProvider/TorrentEngine/repos + callbacks). Instantiation is by ViewModelProvider framework, NOT a direct `new` in printed code. |
| 18 | DetailTorrentViewModel.addTag | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)Lio/reactivex/Completable;` | REACHABLE | SOURCE | FLIP vs prior proposal (OPEN -> REACHABLE, fresh in this pass): InfoFragment:139 selectTag ActivityResultLauncher callback -> viewModel.addTag(tag) (.subscribeOn io, .subscribe()); def ViewModel:151-153 -> repo.addTag. Launcher dispatch is framework; the call site itself is printed. |
| 19 | DetailTorrentViewModel.addTrackers | `(Ljava/util/List;)V` | REACHABLE | SOURCE | Fragment:736 addTrackers() -> viewModel.addTrackers(normalizedUrls); def ViewModel:353-355 -> engine.addTrackers. |
| 20 | DetailTorrentViewModel.applyPriority | `(Ljava/util/List;Lorg/proninyaroslav/libretorrent/core/model/filetree/FilePriority;)V` | REACHABLE | SOURCE | FLIP vs prior proposal (OPEN -> REACHABLE, fresh in this pass): FilesFragment:353 onItemCheckedChanged -> viewModel.applyPriority(singletonList, NORMAL/IGNORE); :502 priority-dialog subscribe -> applyPriority(fileNames, priority); def ViewModel:326-336. |
| 21 | DetailTorrentViewModel.checkFreeSpace | `()Z` | REACHABLE | SOURCE | ViewModel:507 checkParamsChanged (prioritiesChanged case) -> checkFreeSpace(); def :425-429. checkFreeSpace is private; checkParamsChanged itself is reached via mutableParamsCallback :463, registered :112 in <init>. |
| 22 | DetailTorrentViewModel.checkParamsChanged | `(I)V` | REACHABLE | SOURCE | ViewModel:463 mutableParamsCallback.onPropertyChanged -> checkParamsChanged(propertyId); callback registered :112 in <init>; def :478-520. |
| 23 | DetailTorrentViewModel.chooseDirectory | `(Ljava/lang/String;)V` | REACHABLE | SOURCE | FLIP vs prior proposal (OPEN -> REACHABLE, fresh in this pass): FilesFragment:338 onItemClicked (non-file item) -> viewModel.chooseDirectory(item.name); def ViewModel:245-254. |
| 24 | DetailTorrentViewModel.clearData | `()V` | REACHABLE | SOURCE | Fragment:166 onViewCreated, two-pane gate (Utils.isTwoPane) -> viewModel.clearData(); def ViewModel:130-141. |
| 25 | DetailTorrentViewModel.copyTorrentFile | `(Landroid/net/Uri;)V` | REACHABLE | SOURCE | Fragment:809 lambda$new$11 result handler -> viewModel.copyTorrentFile(path); def ViewModel:385-391 -> engine.getBencode + fs.write. |
| 26 | DetailTorrentViewModel.deleteTorrent | `(Z)V` | REACHABLE | SOURCE | Fragment:593 deleteTorrent() -> viewModel.deleteTorrent(withFiles.isChecked()); def ViewModel:361-363 -> engine.deleteTorrents. |
| 27 | DetailTorrentViewModel.deleteTrackers | `(Ljava/util/List;)V` | REACHABLE | SOURCE | FLIP vs prior proposal (OPEN -> REACHABLE, fresh in this pass): TrackersFragment:368 deleteTrackers() private -> viewModel.deleteTrackers(urls); deleteTrackers() called from subscribeAlertDialog POSITIVE :279 (TAG_DELETE_TRACKERS_DIALOG, dialog shown :356); def ViewModel:345-347 -> engine.deleteTrackers. |
| 28 | DetailTorrentViewModel.forceAnnounceTorrent | `()V` | REACHABLE | SOURCE | Fragment:464 onOptionsItemSelected -> viewModel.forceAnnounceTorrent(); def ViewModel:369-371. |
| 29 | DetailTorrentViewModel.forceRecheckTorrent | `()V` | REACHABLE | SOURCE | Fragment:462 onOptionsItemSelected -> viewModel.forceRecheckTorrent(); def ViewModel:365-367. |
| 30 | DetailTorrentViewModel.getChildren | `(Lorg/proninyaroslav/libretorrent/core/model/filetree/TorrentContentFileTree;)Ljava/util/List;` | REACHABLE | SOURCE | FLIP vs prior proposal (OPEN -> REACHABLE, fresh in this pass): ViewModel:608 updateChildren() -> getChildren(curDir); updateChildren called from updateCurDir :604, called from chooseDirectory :253 (REACHABLE via FilesFragment:338), upToParentDirectory :227, and file-tree subscribes :526/:599; def :230-243 (argument used only for the null/file guard; body reads curDir). |
| 31 | DetailTorrentViewModel.getDirChildren | `()Lio/reactivex/Observable;` | REACHABLE | SOURCE | FLIP vs prior proposal (OPEN -> REACHABLE, fresh in this pass): FilesFragment:156 subscribeAdapter -> viewModel.getDirChildren() (subscribeOn computation, map to TorrentContentFileItem, submitList); subscribeAdapter called from onStart :150; def ViewModel:163-165 returns children subject. |
| 32 | DetailTorrentViewModel.getDownloadSpeedLimit | `()I` | REACHABLE | SOURCE | Fragment:754 initSpeedLimitDialog -> viewModel.getDownloadSpeedLimit(); def ViewModel:377-379. |
| 33 | DetailTorrentViewModel.getFilePath | `(Ljava/lang/String;)Lio/reactivex/Single;` | REACHABLE | SOURCE | FLIP vs prior proposal (OPEN -> REACHABLE, fresh in this pass): FilesFragment:340 onItemClicked (file item) -> viewModel.getFilePath(item.name) -> openFile; def ViewModel:262-292. |
| 34 | DetailTorrentViewModel.getFilePriorities | `()[Lorg/proninyaroslav/libretorrent/core/model/data/Priority;` | REACHABLE | SOURCE | ViewModel:505 checkParamsChanged -> getFilePriorities(); def :413-423 (private). |
| 35 | DetailTorrentViewModel.getFilesPriority | `(Ljava/util/List;)Lorg/proninyaroslav/libretorrent/core/model/filetree/FilePriority;` | REACHABLE | SOURCE | FLIP vs prior proposal (OPEN -> REACHABLE, fresh in this pass): FilesFragment:449 priority-dialog subscribe -> viewModel.getFilesPriority(fileNames); def ViewModel:294-324. |
| 36 | DetailTorrentViewModel.getStreamUrl | `(I)Ljava/lang/String;` | REACHABLE | SOURCE | FLIP vs prior proposal (OPEN -> REACHABLE, fresh in this pass): FilesFragment:522 shareStreamUrl -> viewModel.getStreamUrl(fileIndex); shareStreamUrl called from action-mode menu :400; def ViewModel:338-343 -> TorrentStreamServer.makeStreamUrl. NOTE: this row is getStreamUrl itself; batch 42 row 5 (makeStreamUrl) is a different method and is not conflated here. |
| 37 | DetailTorrentViewModel.getTags | `()Lio/reactivex/Single;` | REACHABLE | SOURCE | FLIP vs prior proposal (OPEN -> REACHABLE, fresh in this pass): InfoFragment:150 tagsListener.onAddTagClick -> viewModel.getTags() (flatMap ids, launch SelectTagActivity); listener registered :112 binding.tagsList.setListener(tagsListener); def ViewModel:143-145 -> tagRepo.getByTorrentIdAsync. |
| 38 | DetailTorrentViewModel.getUploadSpeedLimit | `()I` | REACHABLE | SOURCE | Fragment:753 initSpeedLimitDialog -> viewModel.getUploadSpeedLimit(); def ViewModel:373-375. |
| 39 | DetailTorrentViewModel.initMutableParams | `()V` | REACHABLE | SOURCE | ViewModel:213 updateInfo(Torrent, TorrentInfo), firstUpdate gate -> initMutableParams(); def :431-441. updateInfo is reached via Fragment subscribeTorrentInfo (handleTorrentInfo :268, metaInfo subscribe :256). |
| 40 | DetailTorrentViewModel.isFile | `(Ljava/lang/String;)Z` | REACHABLE | SOURCE | FLIP vs prior proposal (OPEN -> REACHABLE, fresh in this pass): FilesFragment:375 onPrepareActionMode -> viewModel.isFile(it.next().name) (gates share_stream_url visibility); def ViewModel:256-260. |

- **Counts (mechanically verified): 40 REACHABLE proposed / 0 UNREACHABLE proposed / 0 OPEN, out of 40.**
- Among REACHABLE: SOURCE 30 / INFERRED 10.
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

