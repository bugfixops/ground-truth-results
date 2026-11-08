**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 79 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 79 only, max 40 methods, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior batch-79 proposal
  (`~/workspace/libretorrent-batch79-proposal.md`, 40 REACHABLE / 0 / 0) was used as an
  INPUT / lead list only; every row below was re-judged against the source freshly
  printed in this pass, and no prior verdict was copied as a result.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 79 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-79 rows are `TODO_CANDIDATE_REACHABLE` in the plan. The table below is in
plan order, sequence 1–40 intact, descriptors as in the plan (omitted from the table
for readability; the merger must match by method name + plan row, not by class alone).

## Printed source used in this pass

Fresh connector fetches from branch `work-2026-10-31`, one file at a time with pauses,
saved in `~/workspace/b7980-src/` (all under
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`
unless noted; SHA-256 of the saved copies):

- `ui/addtorrent/AddTorrentActivity.java` — 577 lines, SHA-256 `41e027a5…`.
- `ui/addtorrent/AddTorrentFilesFragment.java` — 197 lines (prior proposal said 198;
  citations below are against this fresh 197-line copy), SHA-256 `c5538420…`.
- `ui/addtorrent/AddTorrentInfoFragment.java` — 244 lines, SHA-256 `85a15039…`.
- `ui/addtorrent/AddTorrentPagerAdapter.java` — 56 lines, SHA-256 `3f03d9da…`.
- `ui/addtorrent/AddTorrentMutableParams.java` — 171 lines, SHA-256 `ae4c366b…`
  (used only for the $2 onPropertyChanged trigger note, row 20).
- `ui/addtorrent/AddTorrentViewModel.java` — 574 lines, SHA-256 `46c7152d…`
  (used only for the ViewModelProvider construction chain, row 22/39 trunk).
- `src/main/AndroidManifest.xml` — 295 lines, SHA-256 `b011d747…`
  (entry, see Strict-entry below).

No fresh HTTP 429 was hit in this pass. No connector `search_code` result was used as
evidence of absence anywhere in this file.

## Shared trunk (printed this session)

AndroidManifest.xml:62-64 declares `AddTorrentActivity`, `android:exported="true"`,
with SEND (DEFAULT) and VIEW (DEFAULT + BROWSABLE, `application/x-bittorrent` /
`.torrent` file) intent filters — an external-intent entry point, printed fresh here.
AddTorrentActivity.onCreate:97-139 → initLayout:138 and observeDecodeState:139.
initLayout:277-303 sets `new AddTorrentPagerAdapter(this)` and the ViewPager adapter,
then a TabLayoutMediator whose tab-config lambda is row 1.
AddTorrentPagerAdapter.createFragment:41-46 → `AddTorrentInfoFragment.newInstance()` (:44)
and `AddTorrentFilesFragment.newInstance()` (:46).
AddTorrentActivity.onCreate:103-104 obtains the shared ViewModel via
`new ViewModelProvider(this)` / `provider.get(AddTorrentViewModel.class)`; the two
fragments obtain the same ViewModel the same way (FilesFragment onViewCreated,
InfoFragment onViewCreated:101).

## confirmed_by convention in this file

- `SOURCE` = a direct app-to-app call site naming the method is printed in app source
  (including a printed construction site for `<init>` rows, and a printed listener
  body that calls the method).
- `INFERRED` = the method is reached only through unprinted framework/library dispatch
  (activity/fragment lifecycle, menu/back dispatch, LiveData/Rx, TabLayoutMediator
  attach, View-click/adapter callbacks, data-binding Observable dispatch, JVM class
  initialisation) where the registration, show, or construction site is printed.
  This is the per-row convention, not the whole-route convention used in some earlier
  batches; labels are unaffected, only `confirmed_by` would change at merge if the
  merger adopts the whole-route convention.
- No row uses `DYN`, `FW-MEMORY`, or `UNVERIFIED` as `confirmed_by`.

## Table — 40 rows, plan order

| # | Method | Label proposed | confirmed_by | Printed citation / reason |
|---|---|---|---|---|
| 1 | AddTorrentActivity.lambda$initLayout$0 | REACHABLE | INFERRED | AddTorrentActivity.java:291-303: TabLayoutMediator tab-config lambda inside initLayout:277-303, called from onCreate:138; TabLayoutMediator attach dispatch INFERRED. |
| 2 | AddTorrentActivity.lambda$observeDecodeState$1 | REACHABLE | INFERRED | AddTorrentActivity.java:305-326: LiveData observer lambda in observeDecodeState; LiveData dispatch INFERRED; body calls onStartDecode:317 / onStopDecode:323. |
| 3 | AddTorrentActivity.observeDecodeState | REACHABLE | SOURCE | AddTorrentActivity.java:139, called from onCreate. Definition :305-326. |
| 4 | AddTorrentActivity.onBackPressed | REACHABLE | INFERRED | AddTorrentActivity.java:573-576 override, calls finish(); framework back dispatch INFERRED. |
| 5 | AddTorrentActivity.onCreate | REACHABLE | INFERRED | AddTorrentActivity.java:97-139 body printed; framework activity dispatch INFERRED (entry is the manifest SEND/VIEW filters above, not a MAIN/LAUNCHER filter — see Strict-entry). |
| 6 | AddTorrentActivity.onOptionsItemSelected | REACHABLE | INFERRED | AddTorrentActivity.java:552-570 override; framework menu dispatch INFERRED; add-menu branch calls addTorrent. |
| 7 | AddTorrentActivity.onPrepareOptionsMenu | REACHABLE | INFERRED | AddTorrentActivity.java:540-550 override; framework menu dispatch INFERRED. |
| 8 | AddTorrentActivity.onStart | REACHABLE | INFERRED | AddTorrentActivity.java:179-184 body printed; lifecycle dispatch INFERRED; calls subscribeAlertDialog:183, subscribeParamsChanged:184. |
| 9 | AddTorrentActivity.onStartDecode | REACHABLE | SOURCE | AddTorrentActivity.java:329-334, called from observe lambda:317. |
| 10 | AddTorrentActivity.onStop | REACHABLE | INFERRED | AddTorrentActivity.java:170-176 body printed; lifecycle dispatch INFERRED; calls unsubscribeParamsChanged:174. |
| 11 | AddTorrentActivity.onStopDecode | REACHABLE | SOURCE | AddTorrentActivity.java:336-347, called from observe lambda:323. |
| 12 | AddTorrentActivity.showAddErrorDialog | REACHABLE | SOURCE | AddTorrentActivity.java:419-446, called from handleAddException:411,413,415. |
| 13 | AddTorrentActivity.subscribeAlertDialog | REACHABLE | SOURCE | AddTorrentActivity.java:187-190, called from onStart:183. |
| 14 | AddTorrentActivity.subscribeParamsChanged | REACHABLE | SOURCE | AddTorrentActivity.java:193-195, called from onStart:184. |
| 15 | AddTorrentActivity.unsubscribeParamsChanged | REACHABLE | SOURCE | AddTorrentActivity.java:197-199, called from onStop:174. |
| 16 | AddTorrentActivity$1.<init> | REACHABLE | SOURCE | Anonymous PermissionManager.Callback constructed in onCreate:105-129; <init> runs at that construction site. $1 = first anonymous class in source order. |
| 17 | AddTorrentActivity$1.onNotificationResult | REACHABLE | INFERRED | Body AddTorrentActivity.java:120-125 printed; invoked by PermissionManager, whose dispatch code was not printed. |
| 18 | AddTorrentActivity$1.onStorageResult | REACHABLE | INFERRED | Body AddTorrentActivity.java:107-118 printed; invoked by PermissionManager, dispatch not printed. |
| 19 | AddTorrentActivity$2.<init> | REACHABLE | SOURCE | Field onMutableParamsChanged declared AddTorrentActivity.java:201-203; registered subscribeParamsChanged:194, removed unsubscribeParamsChanged:198. $2 = second anonymous class in source order (OnPropertyChangedCallback field). |
| 20 | AddTorrentActivity$2.onPropertyChanged | REACHABLE | INFERRED | Body AddTorrentActivity.java:204-233 printed; data-binding Observable dispatch INFERRED; triggered by MutableParams setters calling notifyPropertyChanged (e.g. AddTorrentMutableParams.java:74,91,115). |
| 21 | AddTorrentFilesFragment.<clinit> | REACHABLE | INFERRED | No explicit static block in the fresh file; static fields are non-constant initialisers (TAG = getSimpleName() at :55, TAG_LIST_FILES_STATE at :57), so class initialisation precedes newInstance (row 25); JVM class-load dispatch INFERRED. If the merger requires an explicit static block, this row reverts to OPEN — recorded, not decided. |
| 22 | AddTorrentFilesFragment.<init> | REACHABLE | SOURCE | Default constructor called by newInstance, AddTorrentFilesFragment.java:68-76 (`new AddTorrentFilesFragment()`), itself called by PagerAdapter:46. |
| 23 | AddTorrentFilesFragment.lambda$subscribeAdapter$0 | REACHABLE | INFERRED | AddTorrentFilesFragment.java:114-118 flatMapSingle lambda in subscribeAdapter; Rx dispatch INFERRED; maps children to DownloadableFileItem. |
| 24 | AddTorrentFilesFragment.lambda$subscribeAdapter$1 | REACHABLE | INFERRED | AddTorrentFilesFragment.java:120-124 subscribe lambda in subscribeAdapter; Rx dispatch INFERRED; calls adapter.submitList:122 + updateFileSize:123. |
| 25 | AddTorrentFilesFragment.newInstance | REACHABLE | SOURCE | AddTorrentFilesFragment.java:68-76, called by AddTorrentPagerAdapter.java:46. |
| 26 | AddTorrentFilesFragment.onAttach | REACHABLE | INFERRED | AddTorrentFilesFragment.java:87-93 body printed; FragmentManager lifecycle dispatch INFERRED. |
| 27 | AddTorrentFilesFragment.onCreateView | REACHABLE | INFERRED | AddTorrentFilesFragment.java:79-84 body printed; FragmentManager lifecycle dispatch INFERRED; inflates fragment_add_torrent_files. |
| 28 | AddTorrentFilesFragment.onItemCheckedChanged | REACHABLE | INFERRED | AddTorrentFilesFragment.java:192-196 body printed; adapter ClickListener dispatch INFERRED (adapter constructed with `this` in onViewCreated:139-140). Calls updateFileSize:195. |
| 29 | AddTorrentFilesFragment.onItemClicked | REACHABLE | INFERRED | AddTorrentFilesFragment.java:183-189 body printed; same adapter-callback dispatch INFERRED. |
| 30 | AddTorrentFilesFragment.onResume | REACHABLE | INFERRED | AddTorrentFilesFragment.java:174-180 body printed; lifecycle dispatch INFERRED. |
| 31 | AddTorrentFilesFragment.onSaveInstanceState | REACHABLE | INFERRED | AddTorrentFilesFragment.java:156-162 body printed; lifecycle dispatch INFERRED. |
| 32 | AddTorrentFilesFragment.onStart | REACHABLE | INFERRED | AddTorrentFilesFragment.java:104-109 body printed; lifecycle dispatch INFERRED; calls subscribeAdapter:108. |
| 33 | AddTorrentFilesFragment.onStop | REACHABLE | INFERRED | AddTorrentFilesFragment.java:96-101 body printed; lifecycle dispatch INFERRED. |
| 34 | AddTorrentFilesFragment.onViewCreated | REACHABLE | INFERRED | AddTorrentFilesFragment.java:128-141 body printed; lifecycle dispatch INFERRED; constructs DownloadableFilesAdapter(this):139-140. |
| 35 | AddTorrentFilesFragment.onViewStateRestored | REACHABLE | INFERRED | AddTorrentFilesFragment.java:165-171 body printed; lifecycle dispatch INFERRED. |
| 36 | AddTorrentFilesFragment.subscribeAdapter | REACHABLE | SOURCE | AddTorrentFilesFragment.java:111-125, called from onStart:108. |
| 37 | AddTorrentFilesFragment.updateFileSize | REACHABLE | SOURCE | AddTorrentFilesFragment.java:143-153, called from subscribe lambda:123 and onItemCheckedChanged:195. |
| 38 | AddTorrentInfoFragment.<clinit> | REACHABLE | INFERRED | No explicit static block in the fresh file; static fields are non-constant initialisers (TAG = getSimpleName() at :65, TAG_OPEN_DIR_ERROR_DIALOG at :67), so class initialisation precedes newInstance (batch 80 row 4); JVM class-load dispatch INFERRED. Same revert-to-OPEN condition as row 21, recorded not decided. |
| 39 | AddTorrentInfoFragment.<init> | REACHABLE | SOURCE | Default constructor called by newInstance, AddTorrentInfoFragment.java:74-81 (`new AddTorrentInfoFragment()`), itself called by PagerAdapter:44. |
| 40 | AddTorrentInfoFragment.checkNameField | REACHABLE | SOURCE | AddTorrentInfoFragment.java:234-243, called from $1.afterTextChanged:117 (batch 80 row 14, fresh print in this pass). |

## Counts — mechanically verified

- Rows in table: 40, sequence 1–40 intact, in plan order.
- REACHABLE proposed: 40.
- UNREACHABLE proposed: 0.
- OPEN: 0.
- confirmed_by: SOURCE 15 / INFERRED 25.
- **Verified for merge: 0 rows.** This part is UNVERIFIED until the main agent
  spot-checks 1 in 5, runs `py_compile`, and the Mac build/C1 return.

## Strict-entry caveat — CLOSED in this pass (with one nuance)

The prior proposal's strict-entry caveat (launcher/intent step into AddTorrentActivity
not printed) is closed by the fresh manifest print: AddTorrentActivity is exported
with SEND and VIEW intent filters (AndroidManifest.xml:62-72+). The activity →
pager → fragment chain is printed end-to-end above, so no row in this batch reverts
under an entry rule that accepts a manifest-registered external-intent entry.
Nuance, recorded not decided: the manifest has no MAIN/LAUNCHER filter for
AddTorrentActivity, so under a stricter rule requiring a launcher MAIN entry for
every route, these rows would still revert to OPEN. The merger must pick that rule;
this file does not decide it.

## Gaps the merger must close before merging

1. **Lambda/anonymous numbering is by source order, NOT verified against bytecode**
   — merger must confirm, especially AddTorrentActivity$1/$2 and FilesFragment
   lambda$subscribeAdapter$0/$1. A swap within a group would not change any label.
2. **Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1** — not run here.
3. **No UNREACHABLE row is claimed:** no saved full-repo grep was run, so absence
   of a caller is never used as evidence here; that matters only if a future
   revision flips a row, since all 40 rows here have a printed caller or
   registration site.

## Not claimed

No build, sampler, grep, or C1 check was run — a true git clone of the repo fails
in this VM with no credential device (named missing check, not passed); build and
C1 run on the user's Mac after a push, so both are marked "not run" here.
Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]) (task instruction). Nothing was edited in `graph_def.py`, `out/`,
`PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.
