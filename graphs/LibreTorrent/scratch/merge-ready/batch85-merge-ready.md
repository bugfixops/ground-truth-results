**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

## Revision note — OPEN-close round 2, 2026-11-01, group G14 (UNVERIFIED, NOT merged)

Original file for this pass copied first to ~/workspace/libretorrent-merge-backup-pre-openclose2/batch85-merge-ready.md (SHA verified identical before editing). No GitHub connector fetch was made in this pass and no 429 was hit; all evidence was already on disk: round-1 ~/workspace/b8586-openclose-src/ definitions/layouts, the ~/workspace/ruleF-src/ 252-file app-Java reconstruction, and the round-1 fw_src LayoutInflater copy in ~/workspace/b10171819-openclose-src/fw_src/. No round-1 REACHABLE flip was reverted. Build: not run. C1: not run. No push.

Counts: BEFORE 37 REACHABLE / 0 UNREACHABLE / 3 OPEN. AFTER 37 / 2 / 1. Flipped 2 rows, both to UNREACHABLE, moving together under the layout-inflation ctor rule (see below):
- 31 EmptyRecyclerView.<init>(Context,AttributeSet,int) -> UNREACHABLE no_trigger_in_app INFERRED.
- 40 ExpansionHeader.<init>(Context,AttributeSet,int) -> UNREACHABLE no_trigger_in_app INFERRED.
Rule stated: LayoutInflater looks up ONLY the (Context,AttributeSet) ctor — fw_src android-8.1.0_r1 LayoutInflater.java (local copy) :88 mConstructorArgs size 2, :90-91 mConstructorSignature {Context.class, AttributeSet.class}, :615 getConstructor(mConstructorSignature), the only getConstructor call in the file; a style= attribute in XML does not change the lookup arity. Each 2-arg ctor calls super(context, attrs) directly, never this(context, attrs, int) (EmptyRecyclerView :59-61 vs :64-66; ExpansionHeader :63-65 vs :70-72), so the already-REACHABLE 2-arg inflation route does not reach the 3-arg ctor. Saved full-repo grep ~/workspace/b8586-openclose2-src/grep_3arg_ctors_full_252_grep.txt (SHA 1d5af1ed4a93efd50af73f09d65fdd8fb3296327190ca510d709ccf12d040c16) over all 252 app Java files: 0 `new X(` hits, 0 `extends X` hits, 0 reflection ctor lookups for either class. Kind/confirmed_by match batch 10's 1-arg ctors of the same classes (UNREACHABLE no_trigger_in_app INFERRED on the same evidence shape); if the merger prefers framework_never_calls for inflation-blocked rows, both rows in this batch (and all five across batches 85/86) change kind together, labels unchanged. Revert condition, all five together: any printed 3-arg construction site flips the affected row(s) to REACHABLE; if the merger requires a fresh branch-fetch full-repo grep (including res/generated) before any UNREACHABLE label resting on absence, all five revert to OPEN together — they never split. Full triage: ~/workspace/b8586-openclose2-src/TRIAGE_NOTE_20261101.md. Note: batch 94's PiecesView 3-arg ctor stays OPEN in its file on the same evidence shape pending its own saved grep; the merger must apply one rule to all 3-arg ctors at merge, and this flip does not decide that rule for batch 94.
Still OPEN (1): 26 ColorView.getColor — round-2 check found no printed caller (see row citation); per the G14 task instruction it needs a printed caller and is NOT flipped on the zero grep. Named resolver: a printed caller on a ColorView receiver (code or layout binding expression).

## Revision note — OPEN-close pass, 2026-11-01 (UNVERIFIED, NOT merged)

Original file copied first to ~/workspace/libretorrent-merge-backup-pre-openclose/batch85-merge-ready.md.
This revision re-derives every OPEN row from source freshly fetched in THIS pass (GitHub connector,
branch work-2026-10-31, one file at a time with ~25 s pauses), saved in ~/workspace/b8586-openclose-src/.
Prior merge-ready file was INPUT only. No row flipped on absence, on a search_code 0, or on a carried citation.

Counts: BEFORE 24 REACHABLE / 0 UNREACHABLE / 16 OPEN. AFTER 37 / 0 / 3. Flipped 13 rows, all to REACHABLE:
- 25 ColorView.<init> (2-arg) -> REACHABLE INFERRED: tags_list_item.xml (fresh, SHA 8ddcd5b0) + drawer_tags_list_item.xml (fresh, SHA e37cfcce) declare ColorView id color; LayoutInflater 2-arg dispatch INFERRED.
- 27 ColorView.onDraw, 28 ColorView.onSizeChanged -> REACHABLE INFERRED: framework callbacks after the same inflation.
- 29 ColorView.setColor -> REACHABLE SOURCE: ui/tag TagsAdapter.java:103 + drawer TagsAdapter.java:191 binding.color.setColor(...) (both fresh).
- 30 EmptyRecyclerView.<init> (2-arg) -> REACHABLE INFERRED: fragment_main.xml (torrent_list), fragment_feed.xml (feed_list), fragment_feed_items.xml (feed_items_list) declare EmptyRecyclerView (all fresh); LayoutInflater 2-arg dispatch INFERRED.
- 32 EmptyRecyclerView.checkEmpty -> REACHABLE SOURCE: called by setAdapter :91, setEmptyView :97, observer :38/:44/:50 (fresh EmptyRecyclerView.java).
- 33 setAdapter -> REACHABLE SOURCE: MainFragment.java:155, FeedFragment.java:135, FeedItemsFragment.java:153 (fresh).
- 34 setEmptyView -> REACHABLE SOURCE: MainFragment.java:151, FeedFragment.java:131, FeedItemsFragment.java:150, LogActivity.java:107 (fresh).
- 35 EmptyRecyclerView$1.<init> -> REACHABLE INFERRED: field-initializer observer, runs at view instantiation (fresh :33).
- 36/37/38 $1.onChanged/onItemRangeInserted/onItemRangeRemoved -> REACHABLE INFERRED: observer dispatch, registered by setAdapter :89 (fresh).
- 39 ExpansionHeader.<init> (2-arg) -> REACHABLE INFERRED: drawer_group_header.xml root tag ExpansionHeader (fresh, SHA 694c2bfd), inflated by DrawerExpandableAdapter.java:78 (fresh); LayoutInflater 2-arg dispatch INFERRED.
Still OPEN (3): 26 ColorView.getColor (no Java caller in the full 252-file app tree — saved grep b8586-openclose-src/getColor_full_corpus_grep.txt; layout binding expressions in the two known ColorView layouts: none, both have no <data> block; needs a saved full-repo grep incl. res/ before any UNREACHABLE flip, and getColor is not layout-driven so a layout hit alone does not close it); 31 EmptyRecyclerView 3-arg ctor (LayoutInflater never calls it; zero Java constructions in the full tree — saved grep customview_construction_grep.txt); 40 ExpansionHeader 3-arg ctor (same ground as 31).
Layout-inflation ctor rule recorded, NOT decided project-wide: a layout naming a custom view flips ONLY its 2-arg ctor to INFERRED; the 3-arg ctor stays OPEN without a printed Java construction. Internal-call confirmed_by: per-row SOURCE (under whole-route INFERRED it would read INFERRED; labels unaffected).
Build: not run. C1: not run. Sampler: not run. No push made in this pass.


# LibreTorrent batch 85 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
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
- **37 REACHABLE / 2 UNREACHABLE / 1 OPEN (2026-11-01 round-2 revision; was 37 / 0 / 3; the pre-round-1 counts previously in this section were stale and are corrected here).**
- Among the 39 labelled rows: **SOURCE 18 / INFERRED 21 (19 REACHABLE INFERRED + 2 UNREACHABLE INFERRED).**
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
| 25 | ColorView.<init> | REACHABLE | INFERRED | tags_list_item.xml declares ColorView id color (fresh, SHA 8ddcd5b0); LayoutInflater 2-arg dispatch INFERRED; TagsAdapter inflates R.layout.tags_list_item (batch 70 print, re-verify at merge if required) |
| 26 | ColorView.getColor | OPEN | — | ColorView.java:102-104; round-2 check 2026-11-01: zero-arg .getColor() grep over 252 app Java files returns only Paint.getColor() inside the definition (:103) and AddTagState.getColor() (AddTagDialog/AddTagViewModel) — no ColorView-receiver call; binding.color sites are setColor (ui/tag TagsAdapter:103, drawer TagsAdapter:191) and setOnClickListener (AddTagDialog:153); both ColorView layouts have no <data> block. Named resolver: a printed caller on a ColorView receiver (code or layout binding expression) |
| 27 | ColorView.onDraw | REACHABLE | INFERRED | Framework onDraw after ColorView inflation from tags_list_item.xml (see row 25) |
| 28 | ColorView.onSizeChanged | REACHABLE | INFERRED | Framework onSizeChanged after ColorView inflation from tags_list_item.xml (see row 25) |
| 29 | ColorView.setColor | REACHABLE | SOURCE | ui/tag TagsAdapter.java:103 binding.color.setColor(item.info.color) + drawer TagsAdapter.java:191 same; binding.color is ColorView in both layouts (tags_list_item.xml + drawer_tags_list_item.xml declare ColorView id color, fresh) |
| 30 | EmptyRecyclerView.<init>(Context,AttributeSet) | REACHABLE | INFERRED | fragment_main.xml declares EmptyRecyclerView id torrent_list; fragment_feed.xml id feed_list; fragment_feed_items.xml id feed_items_list — LayoutInflater 2-arg dispatch INFERRED |
| 31 | EmptyRecyclerView.<init>(Context,AttributeSet,int) | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. LayoutInflater (fw_src android-8.1.0_r1, local copy) :88 mConstructorArgs size 2, :90-91 mConstructorSignature {Context.class, AttributeSet.class}, :615 getConstructor(mConstructorSignature) — inflation looks up ONLY the 2-arg ctor. Saved grep b8586-openclose2-src/grep_3arg_ctors_full_252_grep.txt over 252 app Java files: 0 `new EmptyRecyclerView(` hits, 0 `extends EmptyRecyclerView` hits, 0 reflection ctor lookups. Definition EmptyRecyclerView.java:64-67; 2-arg ctor :59-61 calls super(context, attrs) only, never this(..., int). Reverts to REACHABLE on any printed 3-arg construction site; see round-2 revision note for the all-five-together revert condition. |
| 32 | EmptyRecyclerView.checkEmpty | REACHABLE | SOURCE | Called by setAdapter EmptyRecyclerView.java:91, setEmptyView :97, observer :38/:44/:50 — all REACHABLE in this revision |
| 33 | EmptyRecyclerView.setAdapter | REACHABLE | SOURCE | MainFragment.java:155 binding.torrentList.setAdapter(adapter) (fragment_main.xml declares torrent_list as EmptyRecyclerView, fresh); also FeedFragment.java:135 binding.feedList.setAdapter, FeedItemsFragment.java:153 binding.feedItemsList.setAdapter (feed/feed_items layouts declare EmptyRecyclerView, fresh) |
| 34 | EmptyRecyclerView.setEmptyView | REACHABLE | SOURCE | MainFragment.java:151 binding.torrentList.setEmptyView(binding.emptyViewTorrentList) (fragment_main.xml, fresh); also FeedFragment.java:131, FeedItemsFragment.java:150, LogActivity.java:107 |
| 35 | EmptyRecyclerView$1.<init> | REACHABLE | INFERRED | Field-initializer anonymous AdapterDataObserver, runs at EmptyRecyclerView instantiation (see row 30) |
| 36 | EmptyRecyclerView$1.onChanged | REACHABLE | INFERRED | Observer dispatch, registered by setAdapter EmptyRecyclerView.java:89 |
| 37 | EmptyRecyclerView$1.onItemRangeInserted | REACHABLE | INFERRED | Observer dispatch, registered by setAdapter EmptyRecyclerView.java:89 |
| 38 | EmptyRecyclerView$1.onItemRangeRemoved | REACHABLE | INFERRED | Observer dispatch, registered by setAdapter EmptyRecyclerView.java:89 |
| 39 | ExpansionHeader.<init>(Context,AttributeSet) | REACHABLE | INFERRED | drawer_group_header.xml root tag ExpansionHeader (fresh SHA 694c2bfd), inflated by DrawerExpandableAdapter:78; LayoutInflater 2-arg dispatch INFERRED |
| 40 | ExpansionHeader.<init>(Context,AttributeSet,int) | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. LayoutInflater (fw_src android-8.1.0_r1, local copy) :88 mConstructorArgs size 2, :90-91 mConstructorSignature {Context.class, AttributeSet.class}, :615 getConstructor(mConstructorSignature) — inflation looks up ONLY the 2-arg ctor. Saved grep b8586-openclose2-src/grep_3arg_ctors_full_252_grep.txt over 252 app Java files: 0 `new ExpansionHeader(` hits, 0 `extends ExpansionHeader` hits, 0 reflection ctor lookups. Definition ExpansionHeader.java:70-74 calls init :74; 2-arg ctor :63-65 calls super(context, attrs) only, never this(..., int). Reverts to REACHABLE on any printed 3-arg construction site; see round-2 revision note for the all-five-together revert condition. |

## Still owed before merge (updated 2026-11-01 OPEN-close pass)

- 1 OPEN row remains: 26 ColorView.getColor (named target: a printed caller on a ColorView receiver, code or layout binding expression; Java tree already fully grepped, 252/252, zero ColorView-receiver callers — see round-2 revision note). Rows 31 and 40 flipped to UNREACHABLE in the 2026-11-01 round-2 revision (see revision note).
- Printed launcher-to-CreateTorrentDialog step, if the strict entry-route rule is applied (rows 1-24).
- Bytecode confirmation of lambda$downloadTorrent$3/$4 numbering (rows 4-5).
- Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — all not run.
