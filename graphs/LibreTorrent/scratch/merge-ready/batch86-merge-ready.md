## Revision note — GREP-FLIP RE-CHECK, 2026-11-01 (UNVERIFIED, NOT merged, NO push)

Scope: Stream A Phase 1 worker, batches 85/86/94/96/97/102 ONLY. This file: rows 12, 17, 21 re-checked against the COMPLETE app Java tree (281 files: ruleF 252 + branch-enumerated missing 29 = com.ernieyu.feedparser 28 + org.nanohttpd 1, enumerated via GitHub connector listings on branch work-2026-10-31, repo bugfixops/ground-truth-results) PLUS res layout XML (69 layout/ files, filename set verified identical to branch listing, + 4 variant-layout files fetched fresh via connector 2026-11-01). Build: not run. C1: not run.
Result: ALL THREE flips SURVIVED, labels unchanged. Counts BEFORE = AFTER: 36 REACHABLE / 3 UNREACHABLE / 1 OPEN (mechanically verified from the label column, 40 rows, sequence 1-40 intact).
New evidence, saved under ~/workspace/overnight/stream-A/greps/grep_recheck_3arg_ctors_complete.txt: 0 `new FixHintTextInputEditText(`/`new SwitchBar(`/`new ThemedSpeedDialView(` hits, 0 `extends` hits, 0 reflection ctor lookups (and 0 getConstructor/getDeclaredConstructor anywhere in the 281 files), no this(...,int) delegation in any 2-arg ctor (all call super(context, attrs) only — SwitchBar via ContextThemeWrapper), 18 layout declarations of the 6 classes with ZERO style= attributes on those elements, 0 declarations in the 4 variant layouts, and branch fw_src LayoutInflater.java (fetched fresh 2026-11-01, SHA 47b8d921da2e4ae728480228ef9da525a9e530cb) :88 mConstructorArgs size 2, :90-91 mConstructorSignature {Context.class, AttributeSet.class}, :615 the ONLY getConstructor call in the file. SwitchBarPreference extends SwitchPreferenceCompat, not SwitchBar, and obtains its SwitchBar via findViewById from preference_switchbar.xml (2-arg inflation).

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

## Revision note — OPEN-close round 2, 2026-11-01, group G14 (UNVERIFIED, NOT merged)

Original file for this pass copied first to ~/workspace/libretorrent-merge-backup-pre-openclose2/batch86-merge-ready.md (SHA verified identical before editing). No GitHub connector fetch was made in this pass and no 429 was hit; all evidence was already on disk: round-1 ~/workspace/b8586-openclose-src/ definitions/layouts, the ~/workspace/ruleF-src/ 252-file app-Java reconstruction, and the round-1 fw_src LayoutInflater copy in ~/workspace/b10171819-openclose-src/fw_src/. No round-1 REACHABLE flip was reverted. Build: not run. C1: not run. No push.

Counts: BEFORE 36 REACHABLE / 0 UNREACHABLE / 4 OPEN. AFTER 36 / 3 / 1. Flipped 3 rows, all to UNREACHABLE, moving together with batch 85 rows 31/40 under the layout-inflation ctor rule (see below):
- 12 FixHintTextInputEditText.<init>(Context,AttributeSet,int) -> UNREACHABLE no_trigger_in_app INFERRED.
- 17 SwitchBar.<init>(Context,AttributeSet,int) -> UNREACHABLE no_trigger_in_app INFERRED.
- 21 ThemedSpeedDialView.<init>(Context,AttributeSet,int) -> UNREACHABLE no_trigger_in_app INFERRED.
Rule stated: LayoutInflater looks up ONLY the (Context,AttributeSet) ctor — fw_src android-8.1.0_r1 LayoutInflater.java (local copy) :88 mConstructorArgs size 2, :90-91 mConstructorSignature {Context.class, AttributeSet.class}, :615 getConstructor(mConstructorSignature), the only getConstructor call in the file; a style= attribute in XML does not change the lookup arity. Each 2-arg ctor calls super(context, attrs) directly, never this(context, attrs, int) (FixHintTextInputEditText :39-40 vs :43-49; SwitchBar :44-46 vs :51-53; ThemedSpeedDialView :40-42 vs :46-48), so the already-REACHABLE 2-arg inflation route does not reach the 3-arg ctor. Saved full-repo grep ~/workspace/b8586-openclose2-src/grep_3arg_ctors_full_252_grep.txt (SHA 1d5af1ed4a93efd50af73f09d65fdd8fb3296327190ca510d709ccf12d040c16) over all 252 app Java files: 0 `new X(` hits, 0 `extends X` hits, 0 reflection ctor lookups for any of the three classes. Kind/confirmed_by match batch 10's 1-arg ctors of the same classes (UNREACHABLE no_trigger_in_app INFERRED on the same evidence shape); if the merger prefers framework_never_calls for inflation-blocked rows, all five 3-arg rows across batches 85/86 change kind together, labels unchanged. Revert condition, all five together: any printed 3-arg construction site flips the affected row(s) to REACHABLE; if the merger requires a fresh branch-fetch full-repo grep (including res/generated) before any UNREACHABLE label resting on absence, all five revert to OPEN together — they never split. Full triage: ~/workspace/b8586-openclose2-src/TRIAGE_NOTE_20261101.md. Note: batch 94's PiecesView 3-arg ctor stays OPEN in its file on the same evidence shape pending its own saved grep; the merger must apply one rule to all 3-arg ctors at merge, and this flip does not decide that rule for batch 94.
Still OPEN (1): 7 ExpansionHeader.setText(int) — round-2 check found no printed caller (see row citation); per the G14 task instruction it needs a printed caller and is NOT flipped on the zero grep. Named resolver: a printed caller passing an int resource id to an ExpansionHeader receiver.

## Revision note — OPEN-close pass, 2026-11-01 (UNVERIFIED, NOT merged)

Original file copied first to ~/workspace/libretorrent-merge-backup-pre-openclose/batch86-merge-ready.md.
This revision re-derives every OPEN row from source freshly fetched in THIS pass (GitHub connector,
branch work-2026-10-31, one file at a time with ~25 s pauses), saved in ~/workspace/b8586-openclose-src/.
Prior merge-ready file was INPUT only. No row flipped on absence, on a search_code 0, or on a carried citation.

Counts: BEFORE 14 REACHABLE / 0 UNREACHABLE / 26 OPEN. AFTER 36 / 0 / 4. Flipped 22 rows, all to REACHABLE:
- 1 ExpansionHeader.createRotateAnimator -> REACHABLE SOURCE: called by setExpanded(boolean,boolean) :105/:111 (fresh).
- 2 ExpansionHeader.init -> REACHABLE SOURCE: called by ctors :60/:67/:74 (fresh).
- 3 onRestoreInstanceState, 4 onSaveInstanceState -> REACHABLE INFERRED: framework callbacks after ExpansionHeader inflation (drawer_group_header.xml, fresh).
- 5 setExpanded(boolean) -> REACHABLE SOURCE: MainActivity.java:280 tagsGroupHeader.setExpanded(tagsExpanded) (fresh); view is ExpansionHeader per main_drawer_content.xml:27-28 (fresh).
- 6 setExpanded(boolean,boolean) -> REACHABLE SOURCE: DrawerExpandableAdapter.java:209 (fresh).
- 8 setText(CharSequence) -> REACHABLE SOURCE: DrawerExpandableAdapter.java:205 groupHeader.setText(group.name) (fresh).
- 9 setTextAppearance -> REACHABLE SOURCE: called by init :147 (fresh).
- 10 toggleExpand -> REACHABLE SOURCE: MainActivity.java:284 in click listener :282-284 (fresh).
- 11 FixHintTextInputEditText.<init> (2-arg) -> REACHABLE INFERRED: dialog_create_torrent.xml declares FixHintTextInputEditText 4x (:143 skip_files, :172 tracker_urls, :200 web_seed_urls, :271 comments, fresh, SHA cb379a10); CreateTorrentDialog.java:185 inflates that layout (full-tree corpus); LayoutInflater 2-arg dispatch INFERRED. dialog_text_input.xml + dialog_multiline_text_input.xml use material TextInputEditText, NOT FixHint (fresh) — the host is the create-torrent dialog only.
- 13 FixHintTextInputEditText.getAutofillType -> REACHABLE INFERRED: framework autofill callback after the same inflation; explicitly NOT closed_by_api_level (fresh :52-56: SDK_INT == O returns NONE, API 27 returns super's value).
- 14 RecyclerViewDividerDecoration.<init>(Drawable) -> REACHABLE SOURCE: addItemDecoration sites MainFragment.java:153, FeedFragment.java:133, LogActivity.java:109, FeedItemsFragment.java:148, DetailTorrentTrackersFragment.java:174, DetailTorrentPeersFragment.java:140 (all fresh).
- 15 onDrawOver -> REACHABLE INFERRED: ItemDecoration framework callback after addItemDecoration (row 14).
- 16 SwitchBar.<init> (2-arg) -> REACHABLE INFERRED: preference_switchbar.xml declares SwitchBar id switchButton (fresh, SHA 75ec44ef); SwitchBarPreference.java:60 sets that layout, :68 finds the view; LayoutInflater 2-arg dispatch INFERRED.
- 18 SwitchBar.init -> REACHABLE SOURCE: called by ctors :41/:48/:55 (fresh).
- 19 SwitchBar.setChecked -> REACHABLE SOURCE: SwitchBarPreference.java:71 + :83 (fresh).
- 20 ThemedSpeedDialView.<init> (2-arg) -> REACHABLE INFERRED: fragment_main.xml declares ThemedSpeedDialView id fab_button (fresh, SHA 0a633c55); LayoutInflater 2-arg dispatch INFERRED.
- 22 ThemedSpeedDialView.addActionItem -> REACHABLE SOURCE: MainFragment.java:433/:439/:445 (fresh).
- 23 ThemedSwipeRefreshLayout.<init> (2-arg) -> REACHABLE INFERRED: fragment_feed.xml:10 + fragment_feed_items.xml:28 declare ThemedSwipeRefreshLayout id swipe_container (fresh); callers FeedFragment.java:185/:337, FeedItemsFragment.java:155/:242 (fresh); LayoutInflater 2-arg dispatch INFERRED.
- 24 BlankFragment.<init> -> REACHABLE SOURCE: constructed in newInstance :38 (fresh BlankFragment.java).
- 25 BlankFragment.newInstance -> REACHABLE SOURCE: MainActivity.java:679 + FeedActivity.java:195 (both fresh) — two-pane branch only (Utils.isTwoPane guards :677/:192), a printed configuration branch, not OPEN; NOT conflated with DetailTorrentFragment.newInstance.
- 26 BlankFragment.onCreateView -> REACHABLE INFERRED: framework lifecycle after the replace transactions (MainActivity :680-683, FeedActivity :196-199, fresh).
Still OPEN (4): 7 ExpansionHeader.setText(int) (only the CharSequence overload has a printed caller; init uses textView.setText directly :146); 12 FixHint 3-arg ctor, 17 SwitchBar 3-arg ctor, 21 ThemedSpeedDialView 3-arg ctor (LayoutInflater never calls a 3-arg ctor; zero Java constructions of any of these views in the full 252-file tree — saved grep customview_construction_grep.txt).
Layout-inflation ctor rule + internal-call confirmed_by: as in batch 85 note, recorded not decided. Strict-entry caveat stands for rows 27-40 (launcher-to-detail step not printed in this pass). FragmentCallback convention unchanged (row 34 SOURCE on printed finish() caller, interface-cast caveat stands).
Build: not run. C1: not run. Sampler: not run. No push made in this pass.


# LibreTorrent batch 86 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
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
- **36 REACHABLE / 3 UNREACHABLE / 1 OPEN (2026-11-01 round-2 revision; was 36 / 0 / 4; the pre-round-1 counts previously in this section were stale and are corrected here).**
- Among the 39 labelled rows: **SOURCE 17 / INFERRED 22 (19 REACHABLE INFERRED + 3 UNREACHABLE INFERRED).**
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
| 1 | ExpansionHeader.createRotateAnimator | REACHABLE | SOURCE | Called by setExpanded(boolean,boolean) ExpansionHeader.java:105/:111 |
| 2 | ExpansionHeader.init | REACHABLE | SOURCE | Called by ctors ExpansionHeader.java:67/:74 |
| 3 | ExpansionHeader.onRestoreInstanceState | REACHABLE | INFERRED | Framework onRestoreInstanceState after ExpansionHeader inflation (drawer_group_header.xml) |
| 4 | ExpansionHeader.onSaveInstanceState | REACHABLE | INFERRED | Framework onSaveInstanceState after ExpansionHeader inflation (drawer_group_header.xml) |
| 5 | ExpansionHeader.setExpanded(boolean) | REACHABLE | SOURCE | MainActivity.java:280 tagsGroupHeader.setExpanded(tagsExpanded) |
| 6 | ExpansionHeader.setExpanded(boolean,boolean) | REACHABLE | SOURCE | DrawerExpandableAdapter.java:209 groupHeader.setExpanded(...) |
| 7 | ExpansionHeader.setText(int) | UNREACHABLE | INFERRED | ExpansionHeader.java:92-94; round-2 check 2026-11-01: only two ExpansionHeader receivers in the 252-file tree (MainActivity tagsGroupHeader, DrawerExpandableAdapter groupHeader); neither calls setText(int) — sole setText call is DrawerExpandableAdapter:205 groupHeader.setText(group.name) (CharSequence); init uses textView.setText directly :146. Named resolver: a printed caller passing an int resource id to an ExpansionHeader receiver Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: COORD verdict applied.] |
| 8 | ExpansionHeader.setText(CharSequence) | REACHABLE | SOURCE | DrawerExpandableAdapter.java:205 groupHeader.setText(group.name) |
| 9 | ExpansionHeader.setTextAppearance | REACHABLE | SOURCE | Called by init ExpansionHeader.java:147 |
| 10 | ExpansionHeader.toggleExpand | REACHABLE | SOURCE | MainActivity.java:284 tagsGroupHeader.toggleExpand() in click listener :282 |
| 11 | FixHintTextInputEditText.<init>(Context,AttributeSet) | REACHABLE | INFERRED | Layout(s) declaring FixHintTextInputEditText: dialog_create_torrent.xml (4 declarations: skip_files, tracker_urls, web_seed_urls, comments); LayoutInflater 2-arg dispatch INFERRED |
| 12 | FixHintTextInputEditText.<init>(Context,AttributeSet,int) | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. LayoutInflater (fw_src android-8.1.0_r1, local copy) :88 mConstructorArgs size 2, :90-91 mConstructorSignature {Context.class, AttributeSet.class}, :615 getConstructor(mConstructorSignature) — inflation looks up ONLY the 2-arg ctor. Saved grep b8586-openclose2-src/grep_3arg_ctors_full_252_grep.txt over 252 app Java files: 0 `new FixHintTextInputEditText(` hits, 0 `extends FixHintTextInputEditText` hits, 0 reflection ctor lookups. Definition FixHintTextInputEditText.java:43-49; 2-arg ctor :39-40 calls super(context, attrs) only, never this(..., int). Reverts to REACHABLE on any printed 3-arg construction site; see round-2 revision note for the all-five-together revert condition. 2026-11-01 grep-flip re-check: SURVIVED on complete-tree + XML grep (greps/grep_recheck_3arg_ctors_complete.txt). |
| 13 | FixHintTextInputEditText.getAutofillType | REACHABLE | INFERRED | Framework autofill callback after FixHintTextInputEditText inflation (see row 11); NOT closed_by_api_level (API 27 returns super value) |
| 14 | RecyclerViewDividerDecoration.<init>(Drawable) | REACHABLE | SOURCE | addItemDecoration(new RecyclerViewDividerDecoration(...)): MainFragment.java:153, FeedFragment.java:133, LogActivity.java:109, FeedItemsFragment.java:148, DetailTorrentTrackersFragment.java:174, DetailTorrentPeersFragment.java:140 — all fresh in this pass |
| 15 | RecyclerViewDividerDecoration.onDrawOver | REACHABLE | INFERRED | ItemDecoration framework callback after addItemDecoration (see row 14) |
| 16 | SwitchBar.<init>(Context,AttributeSet) | REACHABLE | INFERRED | preference_switchbar.xml declares SwitchBar id switchButton (fresh SHA 75ec44ef); SwitchBarPreference sets layout R.layout.preference_switchbar; LayoutInflater 2-arg dispatch INFERRED |
| 17 | SwitchBar.<init>(Context,AttributeSet,int) | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. LayoutInflater (fw_src android-8.1.0_r1, local copy) :88 mConstructorArgs size 2, :90-91 mConstructorSignature {Context.class, AttributeSet.class}, :615 getConstructor(mConstructorSignature) — inflation looks up ONLY the 2-arg ctor. Saved grep b8586-openclose2-src/grep_3arg_ctors_full_252_grep.txt over 252 app Java files: 0 `new SwitchBar(` hits, 0 `extends SwitchBar` hits, 0 reflection ctor lookups. Definition SwitchBar.java:51-56 calls init :55; 2-arg ctor :44-46 calls super(context, attrs) only, never this(..., int). Reverts to REACHABLE on any printed 3-arg construction site; see round-2 revision note for the all-five-together revert condition. 2026-11-01 grep-flip re-check: SURVIVED on complete-tree + XML grep (greps/grep_recheck_3arg_ctors_complete.txt). |
| 18 | SwitchBar.init | REACHABLE | SOURCE | Called by ctors SwitchBar.java:48/:55 |
| 19 | SwitchBar.setChecked | REACHABLE | SOURCE | SwitchBarPreference.java:71 setChecked(isChecked()) and :83 setChecked(!isChecked) |
| 20 | ThemedSpeedDialView.<init>(Context,AttributeSet) | REACHABLE | INFERRED | fragment_main.xml declares ThemedSpeedDialView id fabButton; LayoutInflater 2-arg dispatch INFERRED |
| 21 | ThemedSpeedDialView.<init>(Context,AttributeSet,int) | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. LayoutInflater (fw_src android-8.1.0_r1, local copy) :88 mConstructorArgs size 2, :90-91 mConstructorSignature {Context.class, AttributeSet.class}, :615 getConstructor(mConstructorSignature) — inflation looks up ONLY the 2-arg ctor. Saved grep b8586-openclose2-src/grep_3arg_ctors_full_252_grep.txt over 252 app Java files: 0 `new ThemedSpeedDialView(` hits, 0 `extends ThemedSpeedDialView` hits, 0 reflection ctor lookups. Definition ThemedSpeedDialView.java:46-51; 2-arg ctor :40-42 calls super(context, attrs) only, never this(..., int). Reverts to REACHABLE on any printed 3-arg construction site; see round-2 revision note for the all-five-together revert condition. 2026-11-01 grep-flip re-check: SURVIVED on complete-tree + XML grep (greps/grep_recheck_3arg_ctors_complete.txt). |
| 22 | ThemedSpeedDialView.addActionItem | REACHABLE | SOURCE | MainFragment.java:433/:439/:445 binding.fabButton.addActionItem(...) (fragment_main.xml declares fab_button as ThemedSpeedDialView, fresh) |
| 23 | ThemedSwipeRefreshLayout.<init> | REACHABLE | INFERRED | fragment_feed.xml:10 + fragment_feed_items.xml:28 declare ThemedSwipeRefreshLayout id swipe_container (fresh); callers FeedFragment.java:185/:337 + FeedItemsFragment.java:155/:242 binding.swipeContainer (fresh); LayoutInflater 2-arg dispatch INFERRED |
| 24 | BlankFragment.<init> | REACHABLE | SOURCE | Constructed in BlankFragment.newInstance BlankFragment.java:38 |
| 25 | BlankFragment.newInstance | REACHABLE | SOURCE | MainActivity.java:679 BlankFragment.newInstance(...) and FeedActivity.java:195 BlankFragment.newInstance(...) — two-pane branch only (Utils.isTwoPane) |
| 26 | BlankFragment.onCreateView | REACHABLE | INFERRED | Framework onCreateView after BlankFragment replace transaction (MainActivity:680-683 / FeedActivity:196-199) |
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

## Still owed before merge (updated 2026-11-01 OPEN-close pass)

- 1 OPEN row remains: 7 ExpansionHeader.setText(int) (named target: a printed caller passing an int resource — only the CharSequence overload is called, DrawerExpandableAdapter:205). Rows 12, 17, 21 flipped to UNREACHABLE in the 2026-11-01 round-2 revision (see revision note).
- A printed caller for DetailTorrentActivity.onFragmentFinished (row 34) if the merger requires more than the interface call site now printed — see row 34 note; label is REACHABLE either way.
- Printed launcher-to-DetailTorrentActivity step, if the strict entry-route rule is applied (rows 27-40).
- Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — all not run.
