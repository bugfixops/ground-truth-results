# LibreTorrent batch 85 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 85 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior batch-85 proposal was used as an
  INPUT / lead list only; every row below was checked against source freshly fetched in this pass
  (see "Printed source used"), and no prior verdict was copied as a result.
- No fresh HTTP 429 was hit in this pass. All 14 definition/caller files below were fetched
  one at a time with pauses. A directory-listing attempt for `res/layout` was still running when
  these files were written and was NOT used as evidence for any row.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 85 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,733 lines incl. header, plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-85 rows are `TODO_CANDIDATE_REACHABLE` in the plan — candidates, not evidence.
Method names, JVM descriptors, and order below match the plan row for row (checked by script
against the plan copy in this pass).

## Printed source used in this pass (fresh connector fetches, branch work-2026-10-31)

Base path for all files:
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`

- `ui/createtorrent/CreateTorrentViewModel.java` — SHA `99b9dff0612bec420822da85ed1d2dc56d34d4ac`, 406 lines
- `ui/createtorrent/CreateTorrentDialog.java` — SHA `bfb6fc626ae6deb509bd5c485549a83c8ddb892`, 561 lines
- `ui/customviews/ColorView.java` — SHA `76be715f8c22742c075355fff69f23e25f23ba62`, 105 lines
- `ui/customviews/EmptyRecyclerView.java` — SHA `83e8cb5216a1fd2d1771b7b2ade431cd40c07c55`, 99 lines
- `ui/customviews/ExpansionHeader.java` — SHA `e61a18648c10257aa75265294f4054704695d7b4`, 186 lines
- `ui/customviews/FixHintTextInputEditText.java` — SHA `ab825b19bddde9a04fe6c02cf380b2c5d991b1cc`, 59 lines
- `ui/customviews/RecyclerViewDividerDecoration.java` — SHA `fed8168bf4ed3128644fd0859c5d95b479df74c0`, 66 lines
- `ui/customviews/SwitchBar.java` — SHA `6c95abe297e8d41b98beeed68e9e77d3039efe3b`, 75 lines
- `ui/customviews/ThemedSpeedDialView.java` — SHA `ca89b36814c6c273ed23043178d32af040c52044`, 85 lines
- `ui/customviews/ThemedSwipeRefreshLayout.java` — SHA `4450b3f2fe25c21b0f28826887b7f7b4722ccb85`, 44 lines
- `ui/detailtorrent/BlankFragment.java` — SHA `2f3134195251a8814221290bf506d9b291d4807d`, 55 lines
- `ui/detailtorrent/DetailPagerAdapter.java` — SHA `df5ff38c24b0661b60b64357ac8cec1ae7235224`, 76 lines
- `ui/detailtorrent/DetailTorrentActivity.java` — SHA `0ce85b2597300c719bb2e97c7da9e209e7575a39`, 120 lines
- `ui/detailtorrent/DetailTorrentFragment.java` — SHA `c24e0912e62088e962894f04ee427bbe317e83e7`, 832 lines

All 14 SHAs are byte-identical to the SHAs recorded in the prior batch 85/86 proposals —
so the prior line numbers were confirmed fresh here, not merely carried forward.
Saved copies: `~/workspace/b8586-src/`.

## Counts — mechanically verified

- **40 rows, sequence 1–40 intact, in plan order.**
- **24 REACHABLE proposed / 0 UNREACHABLE proposed / 16 OPEN.**
- Among the REACHABLE rows: **SOURCE 14 / INFERRED 10**.
- **0 rows verified for merge.** Main-agent spot-check (1 in 5), `py_compile`, build, and Mac
  build/C1 are all still outstanding — never claimed passed here.

## Shared printed route — CreateTorrentViewModel (rows 1–24)

- `CreateTorrentDialog.java:177-178` — `ViewModelProvider provider = new ViewModelProvider(activity);`
  `viewModel = provider.get(CreateTorrentViewModel.class);` — ViewModel construction runs here.
- ViewModel ctor `:101-114`: `engine.observeNeedStartEngine()` `:106`,
  `mutableParams.getSeedPath().addOnPropertyChangedCallback(dirPathCallback)` `:112`,
  `state.setValue(new BuildState(UNKNOWN, null))` `:113`.
- Dialog spinner listeners: `:233` `viewModel.setPiecesSizeIndex(...)`,
  `:247` `viewModel.setTorrentVersionIndex(...)`.
- Dialog `:295` `viewModel.getState().observe(this, (state) -> {...})`.
- Dialog `:338-345` `buildTorrent()` → `viewModel.buildTorrent()`; dialog `:546` calls its own `buildTorrent()`.
- ViewModel `buildTorrent()` `:151-175`: `builder = makeBuilder()` `:157`,
  `resetPercentProgress()` `:165`, `builder.observeProgress().subscribe(this::makePercentProgress)` `:169`,
  `builder.build().subscribe(this::onBuildSuccess, this::onBuildError)` `:173`.
- `makeBuilder()` `:177-209` calls `getPieceSizeByIndex(...)` `:191`,
  `getTorrentVersionByIndex(...)` `:192`, `makeCreator()` `:196`,
  and the file-name filter lambda `:199-209`.
- `getAndValidateTrackers()` `:264-276` calls `normalizeAndValidateUrl(url)` `:270` and
  throws `new InvalidTrackerException(url)` `:273`;
  `getAndValidateWebSeeds()` `:281-292` calls `normalizeAndValidateUrl(url)` `:286` and
  throws `new InvalidWebSeedException(url)` `:289`.
- `buildTorrent()` catch `:158-161` calls `onBuildError(e)` `:160`;
  `onBuildSuccess` `:211-226` calls `onBuildError(e)` `:219`.
- Dialog handle-finish `:389-391`: `if (viewModel.mutableParams.isStartSeeding())
  disposables.add(viewModel.downloadTorrent()...)`.
- `downloadTorrent()` `:352-388`: `Completable.create((emitter) -> {...})` with inner
  `engine.observeEngineRunning().subscribe((isRunning) -> {... engine.addTorrent(...); ...})`.

## Why rows 25–40 are OPEN, not UNREACHABLE

`ColorView.java`, `EmptyRecyclerView.java`, and `ExpansionHeader.java` were freshly printed in full,
so their internal call chains are known — but NO host site was printed in this pass: no layout XML
naming `ColorView` / `EmptyRecyclerView` / `ExpansionHeader`, no `new ColorView(...)` /
`new EmptyRecyclerView(...)`, no findViewById cast, and a grep of the freshly printed
`DetailTorrentFragment`, `DetailTorrentActivity`, and `CreateTorrentDialog` for
`ColorView|EmptyRecyclerView|ExpansionHeader|SwitchBar|ThemedSpeedDial|ThemedSwipe|FixHint|
RecyclerViewDividerDecoration|BlankFragment` returned zero hits. A custom View's
`(Context,AttributeSet)` ctor runs only via LayoutInflater, and its `onDraw`/`onSizeChanged`/
`setAdapter`/observer callbacks run only after inflation/attachment. Without a printed host site,
these rows cannot be called REACHABLE, and without a saved full-repo grep they cannot be called
UNREACHABLE. One host-site grep flips each chain together:

- ColorView chain: ctor `:43` → `onSizeChanged` `:76-81`, `onDraw` `:84-91` (framework, after inflation);
  `setColor` `:95-99` / `getColor` `:102-104` have no printed caller at all.
- EmptyRecyclerView chain: ctors `:59` (2-arg) / `:64` (3-arg); `setAdapter` `:80-92` registers the
  anonymous `AdapterDataObserver` `:33-52`, whose `onChanged` `:36-38` / `onItemRangeInserted` `:42-44` /
  `onItemRangeRemoved` `:48-50` each call `checkEmpty` `:69-78`; `setEmptyView` `:94-97` also calls
  `checkEmpty` `:97`. All host-gated.
- ExpansionHeader ctors (rows 39–40): `(Context,AttributeSet)` `:63-67` and
  `(Context,AttributeSet,int)` `:70-74` each call `init` `:126-158` (see batch 86 file for the
  `init` chain: inflate `R.layout.expansion_header` `:142`, `setTextAppearance` `:147`,
  `setExpanded(expanded, false)` `:148`).

## Conventions recorded per row, not decided

- `confirmed_by` convention in this file (per-row, not whole-route): SOURCE = a direct app-to-app
  call site naming the method is printed in app source (including a printed listener body that
  calls it); INFERRED = the method is reached only through unprinted framework/library dispatch
  (lifecycle, Rx, databinding, JVM enum init) where registration or the enclosing call is printed.
  Labels are unaffected by this convention; only `confirmed_by` would change at merge if the
  merger adopts the whole-route convention used in some earlier batches.
- Strict-entry: the step that shows `CreateTorrentDialog` itself was not printed in this pass
  (`CreateTorrentDialog.newInstance` at Dialog `:87` has no printed caller in the files fetched
  here — the same gap as batch 19); the route is anchored at the dialog. Under a strict
  entry-route rule requiring a printed launcher-to-dialog step, rows 1–24 revert to OPEN.
  The merger must pick one strict-entry convention for all batches; it is not decided here.
- Lambda numbering: plan rows 4/5 are `lambda$downloadTorrent$3` (inner subscribe lambda,
  signature `(Uri,Uri,CompletableEmitter,Boolean)V`) and `$4` (outer `Completable.create` lambda,
  `(Uri,Uri,CompletableEmitter)V`). This matches the plan descriptors, not source order
  (outer lambda text precedes inner lambda text in `downloadTorrent()` `:374-386`); merger must
  confirm `$3`/`$4` against bytecode if disputed. Both are REACHABLE either way via
  `downloadTorrent()` called at Dialog `:391`.
- No UNREACHABLE row is proposed in this batch at all, so no UNREACHABLE kind, gate, or
  `closed_by_api_level` claim is made here. In particular, no OPEN row is flipped on absence:
  no connector `search_code` 0-result was used as evidence of absence in this pass.

| # | Method | Label | confirmed_by | Citations |
|---|---|---|---|---|
| 1 | CreateTorrentViewModel.getPieceSizeByIndex | REACHABLE | SOURCE | CreateTorrentViewModel.java:333-335; called makeBuilder() :191 |
| 2 | CreateTorrentViewModel.getState | REACHABLE | SOURCE | CreateTorrentViewModel.java:126-129; called CreateTorrentDialog.java:295 |
| 3 | CreateTorrentViewModel.getTorrentVersionByIndex | REACHABLE | SOURCE | CreateTorrentViewModel.java:338-351; called makeBuilder() :192 |
| 4 | CreateTorrentViewModel.lambda$downloadTorrent$3 | REACHABLE | INFERRED | Inner Rx subscribe lambda in downloadTorrent(); downloadTorrent() called CreateTorrentDialog.java:391; Rx dispatch INFERRED, body SOURCE |
| 5 | CreateTorrentViewModel.lambda$downloadTorrent$4 | REACHABLE | INFERRED | Outer Completable.create lambda in downloadTorrent(); same caller :391; Rx dispatch INFERRED, body SOURCE |
| 6 | CreateTorrentViewModel.lambda$makeBuilder$2 | REACHABLE | INFERRED | FileNameFilter lambda in makeBuilder() :199-209; invoked by TorrentBuilder during build(); library dispatch INFERRED |
| 7 | CreateTorrentViewModel.lambda$new$0 | REACHABLE | INFERRED | Ctor filter lambda :106-109; ctor runs via provider.get() CreateTorrentDialog.java:178; Rx dispatch INFERRED |
| 8 | CreateTorrentViewModel.lambda$new$1 | REACHABLE | INFERRED | Ctor subscribe lambda :110; same ctor route; Rx dispatch INFERRED |
| 9 | CreateTorrentViewModel.makeBuilder | REACHABLE | SOURCE | CreateTorrentViewModel.java:177-209; called buildTorrent() :157 |
| 10 | CreateTorrentViewModel.makeCreator | REACHABLE | SOURCE | CreateTorrentViewModel.java:252-262; called makeBuilder() :196 |
| 11 | CreateTorrentViewModel.makePercentProgress | REACHABLE | INFERRED | CreateTorrentViewModel.java:242-245; only via Rx subscribe buildTorrent() :169; Rx dispatch INFERRED |
| 12 | CreateTorrentViewModel.normalizeAndValidateUrl | REACHABLE | SOURCE | CreateTorrentViewModel.java:306-321; called :270 (trackers) and :286 (web seeds) |
| 13 | CreateTorrentViewModel.onBuildError | REACHABLE | SOURCE | CreateTorrentViewModel.java:228-240; called directly :160 and :219 |
| 14 | CreateTorrentViewModel.onBuildSuccess | REACHABLE | INFERRED | CreateTorrentViewModel.java:211-226; only via Rx method ref buildTorrent() :173; Rx dispatch INFERRED |
| 15 | CreateTorrentViewModel.onCleared | REACHABLE | INFERRED | CreateTorrentViewModel.java:118-124; ViewModel lifecycle callback, provider clears on dialog/activity destroy; framework dispatch INFERRED, not printed |
| 16 | CreateTorrentViewModel.resetPercentProgress | REACHABLE | SOURCE | CreateTorrentViewModel.java:247-250; called buildTorrent() :165 |
| 17 | CreateTorrentViewModel.setPiecesSizeIndex | REACHABLE | SOURCE | CreateTorrentViewModel.java:136-142; called CreateTorrentDialog.java:233 |
| 18 | CreateTorrentViewModel.setTorrentVersionIndex | REACHABLE | SOURCE | CreateTorrentViewModel.java:144-150; called CreateTorrentDialog.java:247 |
| 19 | CreateTorrentViewModel$1.<init> | REACHABLE | SOURCE | dirPathCallback field initializer CreateTorrentViewModel.java:391-404; runs with ctor; registered :112 |
| 20 | CreateTorrentViewModel$1.onPropertyChanged | REACHABLE | INFERRED | CreateTorrentViewModel.java:394-403; databinding Observable callback dispatch INFERRED; registered :112, removed onCleared :122 |
| 21 | CreateTorrentViewModel$BuildState.<init> | REACHABLE | SOURCE | CreateTorrentViewModel.java:74-78; constructed :113, :153, :225, :239 |
| 22 | CreateTorrentViewModel$BuildState$Status.<clinit> | REACHABLE | INFERRED | Enum constants CreateTorrentViewModel.java:69; JVM enum init on first BuildState use :113 |
| 23 | CreateTorrentViewModel$InvalidTrackerException.<init> | REACHABLE | SOURCE | CreateTorrentViewModel.java:85-89; thrown getAndValidateTrackers() :273; gate: STATE data (invalid tracker URL typed) |
| 24 | CreateTorrentViewModel$InvalidWebSeedException.<init> | REACHABLE | SOURCE | CreateTorrentViewModel.java:95-99; thrown getAndValidateWebSeeds() :289; gate: STATE data (invalid web-seed URL typed) |
| 25 | ColorView.<init> | OPEN | — | ColorView.java:43-45 definition only; no printed layout/Java host site; NOT UNREACHABLE without a saved full-repo grep |
| 26 | ColorView.getColor | OPEN | — | ColorView.java:102-104; no printed caller |
| 27 | ColorView.onDraw | OPEN | — | ColorView.java:84-91; framework callback, host-gated (see above) |
| 28 | ColorView.onSizeChanged | OPEN | — | ColorView.java:76-81; framework callback, host-gated |
| 29 | ColorView.setColor | OPEN | — | ColorView.java:95-99; no printed caller |
| 30 | EmptyRecyclerView.<init>(Context,AttributeSet) | OPEN | — | EmptyRecyclerView.java:59-62; no printed layout/Java host site |
| 31 | EmptyRecyclerView.<init>(Context,AttributeSet,int) | OPEN | — | EmptyRecyclerView.java:64-67; no printed layout/Java host site |
| 32 | EmptyRecyclerView.checkEmpty | OPEN | — | EmptyRecyclerView.java:69-78; called by setAdapter :91, setEmptyView :97, observer :38/:44/:50 — all host-gated |
| 33 | EmptyRecyclerView.setAdapter | OPEN | — | EmptyRecyclerView.java:80-92; no printed host caller |
| 34 | EmptyRecyclerView.setEmptyView | OPEN | — | EmptyRecyclerView.java:94-97; no printed host caller |
| 35 | EmptyRecyclerView$1.<init> | OPEN | — | Anonymous AdapterDataObserver EmptyRecyclerView.java:33-52; instantiated as field initializer, runs only if view instantiated — host-gated |
| 36 | EmptyRecyclerView$1.onChanged | OPEN | — | EmptyRecyclerView.java:36-38; RecyclerView adapter-observer dispatch, registered only by setAdapter :89 — host-gated |
| 37 | EmptyRecyclerView$1.onItemRangeInserted | OPEN | — | EmptyRecyclerView.java:42-44; same registration — host-gated |
| 38 | EmptyRecyclerView$1.onItemRangeRemoved | OPEN | — | EmptyRecyclerView.java:48-50; same registration — host-gated |
| 39 | ExpansionHeader.<init>(Context,AttributeSet) | OPEN | — | ExpansionHeader.java:63-67 calls init :67; no printed layout/Java host site |
| 40 | ExpansionHeader.<init>(Context,AttributeSet,int) | OPEN | — | ExpansionHeader.java:70-74 calls init :74; no printed layout/Java host site |

## Still owed before merge

- Saved full-repo grep for the 16 OPEN rows (layout XML naming ColorView/EmptyRecyclerView/ExpansionHeader,
  or a `new`/findViewById host site); one hit flips each chain together as described above.
- Printed launcher-to-CreateTorrentDialog step, if the strict entry-route rule is applied (rows 1-24).
- Bytecode confirmation of lambda$downloadTorrent$3/$4 numbering (rows 4-5).
- Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — all not run.
