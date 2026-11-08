# LibreTorrent batch 88 — Phase 2 spot-check — UNVERIFIED (spot-check only, not a merge verdict)

- Batch: 88. Work file checked: `~/workspace/overnight/stream-A/work/batch88-merge-ready.md` (UNVERIFIED proposal, not a result).
- Rows checked (17): sample rows 1, 6, 11, 16, 21, 26, 31, 36, plus every row whose label changed in the file (11 OPEN → REACHABLE SOURCE flips on fresh child-fragment/ViewModel-internal prints): 18, 20, 23, 27, 30, 33, 35, 37, 40. (Rows 31 and 36 are in both sets, counted once.)
- Method: re-derived from already-fetched source on disk (`~/workspace/b8788-src/`); no GitHub connector fetch was needed, no 429 hit, no file missing.
- No edit was made to the merge-ready file. No push. Build/sampler/C1: not run (not this task).
- Strict-entry caveat: as in batch 87, no launcher → MainActivity step was freshly printed in this pass; under a strict printed-launcher rule all REACHABLE rows would revert to OPEN. That convention is undecided and NOT decided here. Child fragments anchor at DetailTorrentFragment via DetailPagerAdapter set on the ViewPager2 (Fragment:186-187).

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence (file:line, local copy) |
|---|---|---|---|---|
| 1 | DetailTorrentFragment.showFreeSpaceErrorToast | REACHABLE / SOURCE | PASS | Caller DetailTorrentFragment.java:294 (subscribeFreeSpaceError lambda); def :404-410 (Snackbar error_free_space). |
| 6 | DetailTorrentFragment.subscribeTorrentInfo | REACHABLE / SOURCE | PASS | Called from onStart DetailTorrentFragment.java:228; def :251-276. |
| 11 | DetailTorrentFragment$1.onPageSelected | REACHABLE / INFERRED | PASS | Def DetailTorrentFragment.java:395-398 (sets currentFragPos); ViewPager2 callback registered :187; dispatch unprinted → INFERRED correct. |
| 16 | DetailTorrentViewModel.<clinit> | REACHABLE / INFERRED | PASS | Non-constant TAG DetailTorrentViewModel.java:82 (`class.getSimpleName()`); first use via `provider.get(DetailTorrentViewModel.class)` DetailTorrentFragment.java:164-165. Convention (ix) recorded, not decided — the row stands as filed under it. |
| 18 | DetailTorrentViewModel.addTag | REACHABLE / SOURCE | PASS | Caller DetailTorrentInfoFragment.java:139 (selectTag ActivityResult callback `viewModel.addTag(tag)`); def DetailTorrentViewModel.java:151-153. The OPEN → REACHABLE flip is supported. |
| 20 | DetailTorrentViewModel.applyPriority | REACHABLE / SOURCE | PASS | Callers DetailTorrentFilesFragment.java:353 (onItemCheckedChanged, singletonList) and :502 (priority-dialog subscribe); def DetailTorrentViewModel.java:326-336. Flip supported. |
| 21 | DetailTorrentViewModel.checkFreeSpace | REACHABLE / SOURCE | PASS | Caller DetailTorrentViewModel.java:507 (checkParamsChanged); def :425-429. Private method, internal caller printed. |
| 23 | DetailTorrentViewModel.chooseDirectory | REACHABLE / SOURCE | PASS | Caller DetailTorrentFilesFragment.java:338 (onItemClicked, non-file item `viewModel.chooseDirectory(item.name)`); def DetailTorrentViewModel.java:245-254. Flip supported. |
| 26 | DetailTorrentViewModel.deleteTorrent | REACHABLE / SOURCE | PASS | Caller DetailTorrentFragment.java:593 (`viewModel.deleteTorrent(withFiles.isChecked())`); def DetailTorrentViewModel.java:361-363. |
| 27 | DetailTorrentViewModel.deleteTrackers | REACHABLE / SOURCE | PASS | Caller chain: DetailTorrentTrackersFragment.java:368 (private deleteTrackers → `viewModel.deleteTrackers(urls)`), called from subscribeAlertDialog POSITIVE :279; def DetailTorrentViewModel.java:345-347. Flip supported. |
| 30 | DetailTorrentViewModel.getChildren | REACHABLE / SOURCE | PASS | Caller DetailTorrentViewModel.java:608 (updateChildren → `getChildren(curDir)`), via updateCurDir :604 ← chooseDirectory :253 (REACHABLE via FilesFragment:338); def :230-243. Flip supported. |
| 31 | DetailTorrentViewModel.getDirChildren | REACHABLE / SOURCE | PASS | Caller DetailTorrentFilesFragment.java:156 (subscribeAdapter `viewModel.getDirChildren()`), called from onStart :150; def DetailTorrentViewModel.java:163-165. Flip supported. |
| 33 | DetailTorrentViewModel.getFilePath | REACHABLE / SOURCE | PASS | Caller DetailTorrentFilesFragment.java:340 (onItemClicked, file item `viewModel.getFilePath(item.name)`); def DetailTorrentViewModel.java:262-292. Flip supported. |
| 35 | DetailTorrentViewModel.getFilesPriority | REACHABLE / SOURCE | PASS | Caller DetailTorrentFilesFragment.java:449 (priority-dialog subscribe `viewModel.getFilesPriority(fileNames)`); def DetailTorrentViewModel.java:294-324. Flip supported. |
| 36 | DetailTorrentViewModel.getStreamUrl | REACHABLE / SOURCE | PASS | Caller DetailTorrentFilesFragment.java:522 (shareStreamUrl `viewModel.getStreamUrl(fileIndex)`); def DetailTorrentViewModel.java:338-343 (→ TorrentStreamServer.makeStreamUrl, a different method, not conflated). Flip supported. |
| 37 | DetailTorrentViewModel.getTags | REACHABLE / SOURCE | PASS | Caller DetailTorrentInfoFragment.java:150 (tagsListener.onAddTagClick `viewModel.getTags()`); def DetailTorrentViewModel.java:143-145. Flip supported. |
| 40 | DetailTorrentViewModel.isFile | REACHABLE / SOURCE | PASS | Caller DetailTorrentFilesFragment.java:375 (onPrepareActionMode `viewModel.isFile(it.next().name)`); def DetailTorrentViewModel.java:256-260. Flip supported. |

## Totals

- PASS: 17 / 17. FAIL: 0 / 17.

## Proposed corrections

- None. No row label or confirmed_by needs changing on the evidence checked; all 11 flips are supported by printed call sites.
