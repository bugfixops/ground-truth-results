# LibreTorrent batch 86 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 86 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior batch-86 proposal was used as an
  INPUT / lead list only; every row below was checked against source freshly fetched in this pass
  (see "Printed source used"), and no prior verdict was copied as a result.
- No fresh HTTP 429 was hit in this pass. All 14 definition/caller files below were fetched
  one at a time with pauses. A directory-listing attempt for `res/layout` was still running when
  these files were written and was NOT used as evidence for any row.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 86 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,733 lines incl. header, plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-86 rows are `TODO_CANDIDATE_REACHABLE` in the plan — candidates, not evidence.
Method names, JVM descriptors, and order below match the plan row for row (checked by script
against the plan copy in this pass).

## Printed source used in this pass (fresh connector fetches, branch work-2026-10-31)

Same 14 files as batch 85, same SHAs (all byte-identical to the SHAs recorded in the prior
batch 85/86 proposals — so the prior line numbers were confirmed fresh here, not merely
carried forward). Saved copies: `~/workspace/b8586-src/`.

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

## Counts — mechanically verified

- **40 rows, sequence 1–40 intact, in plan order.**
- **14 REACHABLE proposed / 0 UNREACHABLE proposed / 26 OPEN.**
- Among the REACHABLE rows: **SOURCE 4 / INFERRED 10** (see row 34 note — this differs from the
  prior proposal's SOURCE 3 / INFERRED 11; the label for row 34 is unchanged).
- **0 rows verified for merge.** Main-agent spot-check (1 in 5), `py_compile`, build, and Mac
  build/C1 are all still outstanding — never claimed passed here.

## Shared printed route — detail torrent (rows 27–40)

- `DetailTorrentActivity.onCreate` `:53-78`: `setContentView(R.layout.activity_detail_torrent)` `:65`,
  `detailTorrentFragment = (DetailTorrentFragment)getSupportFragmentManager().findFragmentById(...)` `:67-69`,
  `detailTorrentFragment.setTorrentId(...)` `:71`,
  ACTION_OPEN_FILES → `detailTorrentFragment.showFiles()` `:73-75`.
  Note: `onCreate` finishes immediately on two-pane devices (`Utils.isTwoPane` `:59-62`), so the
  activity-hosted fragment route below is the single-pane route; the fragment is also hosted by
  MainActivity in two-pane mode (not a batch-86 row, not judged here).
- `DetailTorrentFragment.onViewCreated` `:157-221`: `adapter = new DetailPagerAdapter(this)` `:185`,
  `binding.fragmentViewpager.setAdapter(adapter)` `:186`, TabLayoutMediator attach `:188-211`.
- `DetailPagerAdapter.createFragment` `:53-71` returns the six page fragments by position;
  `getItemCount` `:73-75` returns NUM_FRAGMENTS = 6. ViewPager2 calls both after `setAdapter` —
  framework dispatch, INFERRED.
- `DetailTorrentActivity.onStart` `:88-93` calls `subscribeTorrentDeleted()` `:92`;
  `subscribeTorrentDeleted` `:95-105` subscribes `infoProvider.observeTorrentsDeleted()` with
  lambda `(id) -> { if (...) finish(); }` `:100-104`.
- `DetailTorrentFragment` dialog-event handlers at `:322`/`:336` call `addTrackers(false)` /
  `addTrackers(true)`; `addTrackers(boolean)` body `:689-736` calls `viewModel.addTrackers(...)` `:736`
  (the `viewModel.addTrackers` call itself is at the end of the printed body; the exact line
  inside `:689-736` was not re-numbered in this pass beyond the prior proposal's `:736`).

## Why rows 1–26 are OPEN, not UNREACHABLE

Every definition file for rows 1–23 was freshly printed in full, so the internal chains are known,
but NO host site was printed in this pass: no layout XML naming `ExpansionHeader` /
`FixHintTextInputEditText` / `SwitchBar` / `ThemedSpeedDialView` / `ThemedSwipeRefreshLayout`,
no `new ...` / findViewById / `addItemDecoration` / `addActionItem` host call, and a grep of the
freshly printed `DetailTorrentFragment`, `DetailTorrentActivity`, and `CreateTorrentDialog` for
these class names returned zero hits. Without a printed host site these rows cannot be called
REACHABLE, and without a saved full-repo grep they cannot be called UNREACHABLE.
One host-site grep flips each chain:

- ExpansionHeader: ctors (batch 85 `:63`/`:70`) → `init` `:126-158` →
  `inflate(context, R.layout.expansion_header, this)` `:142`, `setTextAppearance(...)` `:147`,
  `setExpanded(expanded, false)` `:148`; `setExpanded(boolean)` `:82-84` →
  `setExpanded(boolean,boolean)` `:97-115` → `createRotateAnimator` `:117-124` (`:105`/`:111`);
  `toggleExpand` `:77-79` → `setExpanded(!expanded, true)`; `onSaveInstanceState` `:164-173` /
  `onRestoreInstanceState` `:175-185` (framework, `onRestore` calls `setExpanded` `:179`).
  `setText(CharSequence)` `:87-89` and `setText(int)` `:92-94` have NO printed caller at all —
  `init` writes `textView.setText(text)` directly `:146`, not via these methods.
- FixHintTextInputEditText: ctors `:39-41` / `:43-49`; `getAutofillType` `:52-58` returns
  `AUTOFILL_TYPE_NONE` only when `Build.VERSION.SDK_INT == Build.VERSION_CODES.O` (26); at API 27
  it returns `super`'s value — so this row is NOT `closed_by_api_level`, it is host-gated OPEN
  (framework calls it only for an inflated view under autofill).
- RecyclerViewDividerDecoration: `(Drawable)` ctor `:39-42`; `onDrawOver` `:50-...` is a
  `RecyclerView.ItemDecoration` framework callback, running only if a host calls
  `addItemDecoration` — no such site printed.
- SwitchBar: ctors `:44-49` / `:51-56` each call `init` `:58-67`; `setChecked` `:69-74` overrides
  SwitchCompat and updates the on/off text — no printed caller (host settings code / user toggle,
  not printed).
- ThemedSpeedDialView: ctors `:40-44` / `:46-51`; `addActionItem` `:55-83` overrides the library
  method and re-themes the item before `super.addActionItem(...)` `:83` — no printed host caller.
- ThemedSwipeRefreshLayout: ctor `:32-43` only; it just sets colour schemes in the ctor.
- BlankFragment: `newInstance` `:36-43` constructs `new BlankFragment()` `:38`, but NO printed
  caller of `newInstance` exists in this pass, and `DetailPagerAdapter` (the detail pager actually
  used) does NOT use `BlankFragment` — its six positions return DetailTorrentInfo/State/Files/
  Trackers/Peers/Pieces fragments (`:56-66`). So `<init>`, `newInstance`, and `onCreateView`
  (`:47-54`, inflates `R.layout.fragment_blank`) are all OPEN pending a printed `newInstance`
  caller; this is the highest-priority grep target in the batch, and it must NOT be conflated
  with `DetailTorrentFragment.newInstance` (a different class, batch 87 territory).

## Row 34 — onFragmentFinished — re-derivation change, flagged as instructed

The prior proposal flagged row 34 as resting only on the `FragmentCallback` contract, with no
printed fragment caller. Fresh printing in this pass FOUND a printed fragment caller that the
prior pass missed:

- `DetailTorrentFragment.finish(Intent, ResultCode)` `:828-831`:
  `if (activity instanceof FragmentCallback) ((FragmentCallback)activity).onFragmentFinished(this, intent, code);`
  (called from `onBackPressed` `:822-825` via `finish(new Intent(), ResultCode.BACK)`).
- `DetailTorrentActivity` implements `FragmentCallback` (`DetailTorrentActivity.java:40-41`) and
  hosts this fragment (`:67-71`).

Row 34 is therefore upgraded in this file from INFERRED-contract-only to **SOURCE** under the
per-row convention used in this file (a printed app-code call site naming the method, with the
host class printed as implementing the interface — the same basis on which batch 118 marked
`SelectTagActivity.onFragmentFinished` SOURCE via `SelectTagDialog.finish`). The LABEL is
unchanged (REACHABLE either way). Caveats, recorded not decided: dispatch is through the
`FragmentCallback` interface cast, not a direct `DetailTorrentActivity.onFragmentFinished(...)`
call; and in two-pane mode the fragment's host is MainActivity, not DetailTorrentActivity, so
the single-pane host route above is the route that closes this row. If the merger requires a
direct named-class call site, row 34 reverts to INFERRED — label unchanged.

## Conventions recorded per row, not decided

- `confirmed_by` convention in this file (per-row, not whole-route): SOURCE = a direct app-to-app
  call site naming the method is printed in app source (including a printed listener body that
  calls it, and the interface call site in row 34 above); INFERRED = the method is reached only
  through unprinted framework/library dispatch (lifecycle, ViewPager2, Rx, JVM class init)
  where registration or the enclosing call is printed. Labels are unaffected by this convention;
  only `confirmed_by` would change at merge if the merger adopts the whole-route convention
  used in some earlier batches.
- Strict-entry: the Intent/step that starts `DetailTorrentActivity` from the torrent list was not
  printed in this pass; the route is anchored at the activity/fragment. Under a strict
  entry-route rule requiring a printed launcher-to-detail step, rows 27–40 revert to OPEN.
  The merger must pick one strict-entry convention for all batches; it is not decided here.
- No UNREACHABLE row is proposed in this batch at all, so no UNREACHABLE kind, gate, or
  `closed_by_api_level` claim is made here — including for `FixHintTextInputEditText.getAutofillType`
  (see above: NOT `closed_by_api_level` at API 27). No OPEN row is flipped on absence:
  no connector `search_code` 0-result was used as evidence of absence in this pass.

| # | Method | Label | confirmed_by | Citations |
|---|---|---|---|---|
| 1 | ExpansionHeader.createRotateAnimator | OPEN | — | ExpansionHeader.java:117-124; called by setExpanded :105/:111 — host-gated chain |
| 2 | ExpansionHeader.init | OPEN | — | ExpansionHeader.java:126-158; called by ctors :67/:74 — host-gated |
| 3 | ExpansionHeader.onRestoreInstanceState | OPEN | — | ExpansionHeader.java:175-185; framework callback, host-gated; calls setExpanded :179 |
| 4 | ExpansionHeader.onSaveInstanceState | OPEN | — | ExpansionHeader.java:164-173; framework callback, host-gated |
| 5 | ExpansionHeader.setExpanded(boolean) | OPEN | — | ExpansionHeader.java:82-84; calls 2-arg :84; no printed host caller |
| 6 | ExpansionHeader.setExpanded(boolean,boolean) | OPEN | — | ExpansionHeader.java:97-115; called by init :148, toggleExpand :79, onRestore :179 — all host-gated |
| 7 | ExpansionHeader.setText(int) | OPEN | — | ExpansionHeader.java:92-94; no printed caller (init uses textView.setText directly :146) |
| 8 | ExpansionHeader.setText(CharSequence) | OPEN | — | ExpansionHeader.java:87-89; no printed caller |
| 9 | ExpansionHeader.setTextAppearance | OPEN | — | ExpansionHeader.java:154-161; called by init :147 — host-gated |
| 10 | ExpansionHeader.toggleExpand | OPEN | — | ExpansionHeader.java:77-79; no printed host caller (presumably a click handler, not printed) |
| 11 | FixHintTextInputEditText.<init>(Context,AttributeSet) | OPEN | — | FixHintTextInputEditText.java:39-41; no printed layout/Java host site |
| 12 | FixHintTextInputEditText.<init>(Context,AttributeSet,int) | OPEN | — | FixHintTextInputEditText.java:43-49; no printed layout/Java host site |
| 13 | FixHintTextInputEditText.getAutofillType | OPEN | — | FixHintTextInputEditText.java:52-58; framework callback, host-gated; API note above — NOT closed_by_api_level |
| 14 | RecyclerViewDividerDecoration.<init>(Drawable) | OPEN | — | RecyclerViewDividerDecoration.java:39-42; no printed `new`/addItemDecoration site |
| 15 | RecyclerViewDividerDecoration.onDrawOver | OPEN | — | RecyclerViewDividerDecoration.java:50-...; ItemDecoration framework callback, runs only if decoration added — no site printed |
| 16 | SwitchBar.<init>(Context,AttributeSet) | OPEN | — | SwitchBar.java:44-49 calls init :48; no printed layout/Java host site |
| 17 | SwitchBar.<init>(Context,AttributeSet,int) | OPEN | — | SwitchBar.java:51-56 calls init :55; no printed layout/Java host site |
| 18 | SwitchBar.init | OPEN | — | SwitchBar.java:58-67; called by ctors :48/:55 — host-gated |
| 19 | SwitchBar.setChecked | OPEN | — | SwitchBar.java:69-74; no printed caller |
| 20 | ThemedSpeedDialView.<init>(Context,AttributeSet) | OPEN | — | ThemedSpeedDialView.java:40-44; no printed layout/Java host site |
| 21 | ThemedSpeedDialView.<init>(Context,AttributeSet,int) | OPEN | — | ThemedSpeedDialView.java:46-51; no printed layout/Java host site |
| 22 | ThemedSpeedDialView.addActionItem | OPEN | — | ThemedSpeedDialView.java:55-83; no printed host caller |
| 23 | ThemedSwipeRefreshLayout.<init> | OPEN | — | ThemedSwipeRefreshLayout.java:32-43; no printed layout/Java host site |
| 24 | BlankFragment.<init> | OPEN | — | BlankFragment.java:38 constructs it inside newInstance, but newInstance has no printed caller |
| 25 | BlankFragment.newInstance | OPEN | — | BlankFragment.java:36-43; no printed caller; DetailPagerAdapter does not use it (:53-71) |
| 26 | BlankFragment.onCreateView | OPEN | — | BlankFragment.java:47-54; framework callback, runs only if fragment attached via newInstance — unprinted |
| 27 | DetailPagerAdapter.<init> | REACHABLE | SOURCE | DetailPagerAdapter.java:47-49; constructed DetailTorrentFragment.java:185 |
| 28 | DetailPagerAdapter.createFragment | REACHABLE | INFERRED | DetailPagerAdapter.java:53-71; ViewPager2 framework dispatch after setAdapter DetailTorrentFragment.java:186 |
| 29 | DetailPagerAdapter.getItemCount | REACHABLE | INFERRED | DetailPagerAdapter.java:73-75; same ViewPager2 dispatch |
| 30 | DetailTorrentActivity.<clinit> | REACHABLE | INFERRED | Static TAG/constants DetailTorrentActivity.java:43-46; JVM init when activity class loads on start |
| 31 | DetailTorrentActivity.<init> | REACHABLE | INFERRED | Framework instantiation on activity start; activity finds its fragment :67-71 |
| 32 | DetailTorrentActivity.lambda$subscribeTorrentDeleted$0 | REACHABLE | INFERRED | Rx subscribe lambda DetailTorrentActivity.java:100-104; subscribeTorrentDeleted called onStart :92; Rx dispatch INFERRED |
| 33 | DetailTorrentActivity.onCreate | REACHABLE | INFERRED | DetailTorrentActivity.java:53-78; framework lifecycle; strict-entry caveat above |
| 34 | DetailTorrentActivity.onFragmentFinished | REACHABLE | SOURCE | DetailTorrentActivity.java:108-122; printed fragment caller DetailTorrentFragment.java:828-831 via FragmentCallback cast, host implements FragmentCallback DetailTorrentActivity.java:40-41 — see row 34 note; reverts to INFERRED if merger requires a direct named-class call |
| 35 | DetailTorrentActivity.onStart | REACHABLE | INFERRED | DetailTorrentActivity.java:88-93; framework lifecycle; calls subscribeTorrentDeleted :92 |
| 36 | DetailTorrentActivity.onStop | REACHABLE | INFERRED | DetailTorrentActivity.java:80-86; framework lifecycle; clears disposables :84 |
| 37 | DetailTorrentActivity.subscribeTorrentDeleted | REACHABLE | SOURCE | DetailTorrentActivity.java:95-105; called onStart :92 |
| 38 | DetailTorrentFragment.<clinit> | REACHABLE | INFERRED | Static TAG constants DetailTorrentFragment.java:92-100; JVM init when fragment class loads via activity layout/FragmentManager |
| 39 | DetailTorrentFragment.<init> | REACHABLE | INFERRED | Framework fragment instantiation; fragment found by id in DetailTorrentActivity.java:67-71 |
| 40 | DetailTorrentFragment.addTrackers | REACHABLE | SOURCE | DetailTorrentFragment.java:689-736; called by dialog-event handlers :322 (replace=false) and :336 (replace=true) |

## Still owed before merge

- Saved full-repo grep for the 26 OPEN rows, in priority order: (1) BlankFragment.newInstance caller;
  (2) layout XML naming ExpansionHeader / FixHintTextInputEditText / SwitchBar / ThemedSpeedDialView /
  ThemedSwipeRefreshLayout / ColorView / EmptyRecyclerView; (3) host callers of ExpansionHeader.setText /
  toggleExpand, SwitchBar.setChecked, ThemedSpeedDialView.addActionItem, RecyclerViewDividerDecoration
  construction, ColorView.setColor/getColor, EmptyRecyclerView.setAdapter/setEmptyView.
- A printed caller for DetailTorrentActivity.onFragmentFinished (row 34) if the merger requires more than
  the interface call site now printed — see row 34 note; label is REACHABLE either way.
- Printed launcher-to-DetailTorrentActivity step, if the strict entry-route rule is applied (rows 27-40).
- Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — all not run.
