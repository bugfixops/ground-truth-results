# LibreTorrent batch 84 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler or full-repo grep was run or claimed.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 84 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels re-derived from printed source. The earlier batch 84 proposal
  (`~/workspace/libretorrent-batch84-proposal.md`) was used as an INPUT / lead list only;
  every row below was re-judged against source re-read in this pass, and seven of its
  eight OPEN rows changed on fresh printed evidence (see Changes vs prior proposal).

## Membership — verified first, not guessed

Exactly the 40 rows of batch 84 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`,
taken from the local plan copy `~/workspace/agent27-plan.tsv` (lines 3291–3330,
plan blob SHA `0104806dd666c840049b3db52823d4b384fa1c92` as recorded for the branch copy).
All 40 rows are `TODO_CANDIDATE_REACHABLE` in the plan — a candidate, not evidence.
Rows: `CreateTorrentDialog$2.onTextChanged` (1 row), `$3` and `$4` listener classes
(6 rows), `CreateTorrentMutableParams` (23 rows), and the first 10 `CreateTorrentViewModel` rows.

## Printed source used in this pass

Base path (all files):
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`
except the layout, which is under `src/main/res/layout/`.

- `ui/createtorrent/CreateTorrentDialog.java` — 561 lines, re-read in full this pass
  from `~/workspace/b83-src/CreateTorrentDialog.java`; every citation below was
  re-verified by grep in this pass.
- `ui/createtorrent/CreateTorrentMutableParams.java` — 190 lines, re-read in full this pass
  (the earlier proposal said 191; the file on disk is 190 lines — a one-line counting
  difference, no citation changes).
- `ui/createtorrent/CreateTorrentViewModel.java` — 406 lines, re-read in full this pass
  (the earlier proposal said 407; same one-line counting difference).
- `ui/createtorrent/CreateTorrentActivity.java` — 140 lines, FRESH connector fetch
  this session from branch `work-2026-10-31`, saved at
  `~/workspace/b83-src/CreateTorrentActivity.java`. It closes the dialog-display step
  for this batch too (Activity:83–86, see batch 83 file).
- `src/main/res/layout/dialog_create_torrent.xml` — 283 lines, FRESH connector fetch
  this session from branch `work-2026-10-31` (SHA `cb379a10cdb154d5d69e51659781f0cd0a257844`),
  saved at `~/workspace/b83-src/dialog_create_torrent.xml`. This is the new evidence
  that resolves seven OPEN rows (see Changes below).

Line numbers below are "Dialog:" = CreateTorrentDialog.java, "Params:" =
CreateTorrentMutableParams.java, "ViewModel:" = CreateTorrentViewModel.java,
"Activity:" = CreateTorrentActivity.java, "Layout:" = dialog_create_torrent.xml.

## Changes vs prior proposal (seven OPEN rows resolved, one stays OPEN)

The prior proposal left eight rows OPEN: the six @Bindable setters, `toString`, and
`getBuildProgress`. A grep of the three Java files in this pass confirms those eight
still have NO direct app-code caller in the Java files (the six setters occur only at
their definitions, Params:70/82/94/130/142/154; `getBuildProgress` only at its
definition, ViewModel:131; `toString` only at its definition, Params:174–190, plus an
unrelated `e.toString()` in Dialog:154).

**Resolved to REACHABLE INFERRED by the freshly printed layout — the six setters and
`getBuildProgress`:**

- The dialog inflates this exact layout and hands it the ViewModel: Dialog:186–188
  (`binding = DataBindingUtil.inflate(i, R.layout.dialog_create_torrent, null, false);`
  `binding.setLifecycleOwner(this); binding.setViewModel(viewModel);`).
  The layout declares `<variable name="viewModel" type="…CreateTorrentViewModel" />`
  (Layout:9–11), so layout expressions on `viewModel.…` resolve through the ViewModel
  and its public `mutableParams` field (ViewModel:59).
- Two-way bindings `@={…}` — the generated binding code calls the setter when the view
  changes and the getter when the model changes. The generated binding class itself was
  NOT printed, so these rows are INFERRED, not SOURCE (same precedent as batch 75–76,
  where `AddFeedMutableParams.setNotDownloadImmediately` was judged REACHABLE INFERRED
  only via a printed two-way binding). The convention is recorded here, not decided for
  the project: if the merger requires a printed generated binding class, all seven
  layout-resolved rows below revert to OPEN.
  - `setStartSeeding`: Layout:113 `android:checked="@={viewModel.mutableParams.startSeeding}"`.
  - `setPrivateTorrent`: Layout:120 `android:checked="@={viewModel.mutableParams.privateTorrent}"`.
  - `setSkipFiles`: Layout:149 `android:text="@={viewModel.mutableParams.skipFiles}"`.
  - `setTrackerUrls`: Layout:177 `android:text="@={viewModel.mutableParams.trackerUrls}"`.
  - `setWebSeedUrls`: Layout:205 `android:text="@={viewModel.mutableParams.webSeedUrls}"`.
  - `setComments`: Layout:276 `android:text="@={viewModel.mutableParams.comments}"`.
- One-way binding for `getBuildProgress`: Layout:36
  `android:progress="@{viewModel.buildProgress.intValue()}"`. Data binding resolves the
  `buildProgress` property through the getter `getBuildProgress()` (ViewModel:131–134,
  returning the `buildProgress` LiveData field), observed by the generated binding.
  Generated code not printed → INFERRED, with the same revert condition as above.
  (For contrast, `getState` is SOURCE in batch 83 via the direct Dialog:295 observe call;
  `getBuildProgress` has no such direct call and rests on the layout alone.)
- Note on `setWebSeedUrls`: unlike the other five setters it does NOT call
  `notifyPropertyChanged` (Params:94–99), but the two-way binding still calls the setter
  on view change, so the label is unaffected; the missing notification only affects
  model→view refresh, which is not a route question.

**Stays OPEN — `CreateTorrentMutableParams.toString` (row 30):**
No printed caller in any file printed in this pass, no layout binding, no generated
binding. It stays OPEN, NOT UNREACHABLE: a `toString` is plausibly reached via logging
or string concatenation, and no saved full-repo grep was run. Highest-priority grep
target for this batch. A connector `search_code` call was NOT used for this row at all.

**Strict-entry caveat, narrowed (not removed):** as in batch 83, the dialog-display step
is now printed (Activity:83–86: `CreateTorrentDialog.newInstance()` + `show()`), but the
step that starts `CreateTorrentActivity` itself is NOT printed in this pass. Under a
strict launcher-entry rule, all 39 REACHABLE rows revert to OPEN until that starter is
printed; under the dialog-anchored convention used by sibling batches, all 39 stand.

## confirmed_by convention used here

- SOURCE: a caller site naming the method is printed in app source in one of the Java files above.
- INFERRED: the method is reached only through unprinted framework/library dispatch
  (spinner listener, TextWatcher, ViewModelProvider class-load/construction, or generated
  data-binding code) where the registration / inflate / setViewModel site is printed.
  This is the per-row convention, not the whole-route convention used in some earlier
  batches; labels are unaffected, only `confirmed_by` would change at merge if the merger
  adopts the whole-route convention.

## Judgements — 39 REACHABLE proposed / 0 UNREACHABLE / 1 OPEN

| # | Method | Label | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | CreateTorrentDialog$2.onTextChanged | REACHABLE | INFERRED | Body Dialog:220 (empty); second TextWatcher registered Dialog:212 (webSeedUrls); TextWatcher framework dispatch not printed. Companion rows $2.<init>/after/before are batch 83 rows 38–40. |
| 2 | CreateTorrentDialog$3.<init> | REACHABLE | SOURCE | Compiler-generated; construction site `new AdapterView.OnItemSelectedListener()` for piecesSize Dialog:228. |
| 3 | CreateTorrentDialog$3.onItemSelected | REACHABLE | INFERRED | Body Dialog:230–234 calls `viewModel.setPiecesSizeIndex(…)`; registered Dialog:228; spinner framework dispatch not printed. |
| 4 | CreateTorrentDialog$3.onNothingSelected | REACHABLE | INFERRED | Body Dialog:236–239 (comment "Nothing"); registered Dialog:228; framework dispatch not printed. |
| 5 | CreateTorrentDialog$4.<init> | REACHABLE | SOURCE | Compiler-generated; construction site `new AdapterView.OnItemSelectedListener()` for torrentVersion Dialog:242. |
| 6 | CreateTorrentDialog$4.onItemSelected | REACHABLE | INFERRED | Body Dialog:244–248 calls `viewModel.setTorrentVersionIndex(…)`; registered Dialog:242; spinner framework dispatch not printed. |
| 7 | CreateTorrentDialog$4.onNothingSelected | REACHABLE | INFERRED | Body Dialog:250–253 (comment "Nothing"); registered Dialog:242; framework dispatch not printed. |
| 8 | CreateTorrentMutableParams.<init> | REACHABLE | SOURCE | No explicit constructor in file; default constructor invoked by ViewModel field initialiser ViewModel:59 (`new CreateTorrentMutableParams()`). Field initialisers Params:35–45 run in it. |
| 9 | CreateTorrentMutableParams.getComments | REACHABLE | SOURCE | Called by ViewModel.makeBuilder ViewModel:197 (`.setComment(mutableParams.getComments())`); definition Params:125–128. |
| 10 | CreateTorrentMutableParams.getPieceSizeIndex | REACHABLE | SOURCE | Called by Dialog:227 (setSelection) and ViewModel.makeBuilder ViewModel:191; definition Params:101–104. |
| 11 | CreateTorrentMutableParams.getSavePath | REACHABLE | SOURCE | Called by Dialog:382 (handleFinish) and ViewModel:182,213,230,359,361,363; definition Params:161–164. |
| 12 | CreateTorrentMutableParams.getSeedPath | REACHABLE | SOURCE | Called by Dialog:513,530 (`.set(data.getData())` on the returned ObservableField) and ViewModel:112,179,355,396; definition Params:47–50. |
| 13 | CreateTorrentMutableParams.getSeedPathName | REACHABLE | SOURCE | Called by Dialog:314 (add-button seed-path empty check); definition Params:53–56. Also bound one-way at Layout:63 (`@{viewModel.mutableParams.seedPathName}`). |
| 14 | CreateTorrentMutableParams.getSkipFiles | REACHABLE | SOURCE | Called by ViewModel.decodeSkipFilesList ViewModel:326–327; definition Params:65–68. |
| 15 | CreateTorrentMutableParams.getTorrentVersionIndex | REACHABLE | SOURCE | Called by ViewModel.makeBuilder ViewModel:192; definition Params:113–116. |
| 16 | CreateTorrentMutableParams.getTrackerUrls | REACHABLE | SOURCE | Called by ViewModel.getAndValidateTrackers ViewModel:268; definition Params:77–80. |
| 17 | CreateTorrentMutableParams.getWebSeedUrls | REACHABLE | SOURCE | Called by ViewModel.getAndValidateWebSeeds ViewModel:284; definition Params:89–92. |
| 18 | CreateTorrentMutableParams.isPrivateTorrent | REACHABLE | SOURCE | Called by ViewModel.makeBuilder ViewModel:195 (`.setAsPrivate(…)`); definition Params:149–152. |
| 19 | CreateTorrentMutableParams.isStartSeeding | REACHABLE | SOURCE | Called by Dialog.handleFinish Dialog:389; definition Params:137–140. |
| 20 | CreateTorrentMutableParams.setComments | REACHABLE | INFERRED | Changed from OPEN in the prior proposal. Two-way binding Layout:276 `android:text="@={viewModel.mutableParams.comments}"`, via Dialog:187–188 inflate + setViewModel; generated binding code not printed. Definition Params:130–134 (@Bindable, notifyPropertyChanged). |
| 21 | CreateTorrentMutableParams.setPieceSizeIndex | REACHABLE | SOURCE | Called by ViewModel.setPiecesSizeIndex ViewModel:141, which is called by $3.onItemSelected Dialog:233; definition Params:106–110. |
| 22 | CreateTorrentMutableParams.setPrivateTorrent | REACHABLE | INFERRED | Changed from OPEN in the prior proposal. Two-way binding Layout:120 `android:checked="@={viewModel.mutableParams.privateTorrent}"`, via Dialog:187–188; generated binding not printed. Definition Params:154–158 (@Bindable). |
| 23 | CreateTorrentMutableParams.setSavePath | REACHABLE | SOURCE | Called by choosePathToSave callback Dialog:545; definition Params:166–170. |
| 24 | CreateTorrentMutableParams.setSeedPathName | REACHABLE | SOURCE | Called by ViewModel dirPathCallback ViewModel:400; definition Params:58–62. |
| 25 | CreateTorrentMutableParams.setSkipFiles | REACHABLE | INFERRED | Changed from OPEN in the prior proposal. Two-way binding Layout:149 `android:text="@={viewModel.mutableParams.skipFiles}"`, via Dialog:187–188; generated binding not printed. Definition Params:70–74 (@Bindable). |
| 26 | CreateTorrentMutableParams.setStartSeeding | REACHABLE | INFERRED | Changed from OPEN in the prior proposal. Two-way binding Layout:113 `android:checked="@={viewModel.mutableParams.startSeeding}"`, via Dialog:187–188; generated binding not printed. Definition Params:142–146 (@Bindable). |
| 27 | CreateTorrentMutableParams.setTorrentVersionIndex | REACHABLE | SOURCE | Called by ViewModel.setTorrentVersionIndex ViewModel:148, which is called by $4.onItemSelected Dialog:247; definition Params:118–122. |
| 28 | CreateTorrentMutableParams.setTrackerUrls | REACHABLE | INFERRED | Changed from OPEN in the prior proposal. Two-way binding Layout:177 `android:text="@={viewModel.mutableParams.trackerUrls}"`, via Dialog:187–188; generated binding not printed. Definition Params:82–86 (@Bindable). |
| 29 | CreateTorrentMutableParams.setWebSeedUrls | REACHABLE | INFERRED | Changed from OPEN in the prior proposal. Two-way binding Layout:205 `android:text="@={viewModel.mutableParams.webSeedUrls}"`, via Dialog:187–188; generated binding not printed. Definition Params:94–99 (@Bindable, no notifyPropertyChanged — see Changes). |
| 30 | CreateTorrentMutableParams.toString | OPEN | — | Definition Params:174–190 (overrides Object.toString, builds field dump). NO caller in any printed file, no layout binding. OPEN pending a saved full-repo grep; NOT UNREACHABLE on this evidence. |
| 31 | CreateTorrentViewModel.<clinit> | REACHABLE | INFERRED | Static initialisation (TAG field ViewModel:57) runs on first class load, triggered by `ViewModelProvider.get(CreateTorrentViewModel.class)` Dialog:180–181; class-load dispatch not printed. |
| 32 | CreateTorrentViewModel.<init> | REACHABLE | INFERRED | Body ViewModel:101–116 (engine/fs setup, seed-path callback registration, state/buildProgress initial values); constructed by `ViewModelProvider.get(…)` Dialog:180–181; provider dispatch not printed from fw_src. |
| 33 | CreateTorrentViewModel.buildTorrent | REACHABLE | SOURCE | Called by Dialog.buildTorrent Dialog:345; body ViewModel:151–176 (makeBuilder, progress/build subscribes). Same anchor as batch 19. |
| 34 | CreateTorrentViewModel.decodeSkipFilesList | REACHABLE | SOURCE | Called by the fileNameFilter lambda inside makeBuilder ViewModel:199 (filter set at ViewModel:198); definition ViewModel:323–331. |
| 35 | CreateTorrentViewModel.decodeUrls | REACHABLE | SOURCE | Called by getAndValidateTrackers ViewModel:268 and getAndValidateWebSeeds ViewModel:284; definition ViewModel:297–304. |
| 36 | CreateTorrentViewModel.downloadTorrent | REACHABLE | SOURCE | Called by Dialog.handleFinish Dialog:391; body ViewModel:352–384. |
| 37 | CreateTorrentViewModel.finish | REACHABLE | SOURCE | Called by Dialog.finish Dialog:557; body ViewModel:386–389 (disposables.clear()). |
| 38 | CreateTorrentViewModel.getAndValidateTrackers | REACHABLE | SOURCE | Called by makeBuilder ViewModel:194; definition ViewModel:264–279. |
| 39 | CreateTorrentViewModel.getAndValidateWebSeeds | REACHABLE | SOURCE | Called by makeBuilder ViewModel:195; definition ViewModel:281–295. |
| 40 | CreateTorrentViewModel.getBuildProgress | REACHABLE | INFERRED | Changed from OPEN in the prior proposal. Layout:36 `android:progress="@{viewModel.buildProgress.intValue()}"`, via Dialog:187–188 inflate + setViewModel; data binding resolves `buildProgress` through `getBuildProgress()` (ViewModel:131–134). Generated binding not printed, so INFERRED; reverts to OPEN if the merger requires a printed generated binding class. |

## Counts

- 40 rows judged: 39 REACHABLE proposed, 0 UNREACHABLE, 1 OPEN.
- OPEN row: `CreateTorrentMutableParams.toString` only.
- confirmed_by split (proposed rows): SOURCE 25 (rows 2, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 23, 24, 27, 33, 34, 35, 36, 37, 38, 39), INFERRED 14 (rows 1, 3, 4, 6, 7, 20, 22, 25, 26, 28, 29, 31, 32, 40).
- 0 rows verified for merge. Main-agent spot-check (1 in 5), `py_compile`, build, and Mac build/C1 are all NOT RUN here.

## Still owed before merge

1. Saved full-repo grep for `CreateTorrentMutableParams.toString` (row 30) before any
   OPEN → UNREACHABLE flip — it must not be flipped on absence in the printed files alone.
2. Printed generated binding class for `dialog_create_torrent`, if the merger requires it
   instead of the printed layout + inflate + setViewModel chain — otherwise rows 20, 22, 25,
   26, 28, 29, and 40 revert to OPEN under that stricter convention (labels for the other
   32 REACHABLE rows are unaffected).
3. Printed starter of CreateTorrentActivity — the remaining strict-entry link; under a
   strict launcher-entry rule all 39 REACHABLE rows revert to OPEN until it is printed.
4. Build, sampler, and C1 on a full checkout (clone still unavailable in this VM — named
   missing check, not passed; build/C1 run on the user's Mac after push, marked not run here).
