**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 108 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 108 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior batch-108 proposal
  (`~/workspace/libretorrent-batch108-proposal.md`) was used as an INPUT / lead list only;
  every row below was re-checked against source freshly printed in this pass (see below),
  and no prior verdict was copied as a result.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 108 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-108 rows are `TODO_CANDIDATE_REACHABLE` in the plan (candidates, not evidence),
in plan order. Plan order is followed exactly, including the non-numeric order of rows 23–24:
row 23 is `lambda$subscribeTags$10`, row 24 is `lambda$subscribeTags$9`. Method names and
JVM descriptors in the table below match the plan row for row.

## Printed source used in this pass

Fresh connector fetches from branch `work-2026-10-31`, one file at a time with pauses,
saved in `~/workspace/b107-108-src/` (all under
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/` unless noted):

- `ui/main/MainActivity.java` — SHA `b98a504934ed4480…`, 811 lines, printed in full fresh.
  Key sites verified fresh: `onCreate` :136-189 (`cleanGarbageFragments` :187, `initLayout` :188);
  `initLayout` :191-228 (`initDrawer` :226); `initDrawer` :230-291 (collapse listener :233,
  expand listener :237, `this::onDrawerItemSelected` :250, `onDrawerGroupsCreated` :252,
  addTagButton click :273-275, tagsGroupHeader click :282-290); `onPostCreate` :373-379;
  `onStart` :381-390 (`subscribeAlertDialog` :384, `subscribeMsgViewModel` :385,
  `subscribeNeedStartEngine` :387, `subscribeTags` :388); `onStop` :392-397;
  `onDestroy` :399-404; `subscribeAlertDialog` :406-435 (`openChangelogLink` :416,
  `initAboutDialog` :419); `subscribeMsgViewModel` :437-461 (`getCurrentDetailFragment` :450);
  `subscribeNeedStartEngine` :463-468 (filter :466, subscribe :467);
  `subscribeTags` :470-488 (flatMapSingle :473, subscribe :481, `setInitSelection` :483);
  `setInitSelection` :490-557 (filter :515, subscribe :518); `saveGroupExpandState` :559-580
  (called :235, :239); `onDrawerGroupsCreated` :582-601 (`applyExpandState` :599);
  `applyExpandState` :603-608; `onDrawerItemSelected` :610-631 (`saveSelectionState` :627);
  `saveSelectionState` :633-638; `cleanGarbageFragments` :640-655;
  `getCurrentDetailFragment` :687-695; `onCreateOptionsMenu` :698-705 (`initSearch` :701,
  `setOnMenuItemClickListener(this::onOptionsItemSelected)` :702); `initSearch` :707-726
  (close listener :709); `onOptionsItemSelected` :738-759 (log branch :754-755 → `showLog()`);
  `showAboutDialog` :761-774 (called :745); `initAboutDialog` :776-793;
  `openChangelogLink` :795-799; `showLog` :801-803; `onFragmentFinished` :806-811;
  `implements FragmentCallback` :98; static `TAG` :99 (non-constant `getSimpleName()`).
- `ui/log/SessionLogFilterDialog.java` — SHA `54f31c23062f5352…`, 120 lines, printed in full fresh:
  `onResume` :69-86 (back-key listener :74). This is batch 108 row 1 only; the rest of this
  class is batch 107 rows 32–40.
- `ui/log/LogActivity.java` — SHA `d91948db981d67d0…`, 470 lines, for the row-1 trunk only:
  `showFilterDialog` :250-256 (`newInstance` :254, `show` :255).
- `src/main/AndroidManifest.xml` — SHA `b011d74750a72c16…`, 295 lines. MainActivity declared :43
  with MAIN :53 / LAUNCHER :54; LogActivity declared :239; LogSettingsActivity declared :242.

No fresh HTTP 429 was hit in this pass. No connector `search_code` result was used as
evidence anywhere in this file.

## Lambda numbering — verified from fresh source order, not guessed

In fresh MainActivity, the top-level-class lambdas in file order are: collapse :233,
expand :237, addTagButton click :274, tagsGroupHeader click :282, subscribeAlertDialog :408,
subscribeMsgViewModel blank-fragment :444, torrents-deleted :449, subscribeNeedStartEngine
filter :466, subscribe :467, subscribeTags flatMapSingle :473, subscribe :481,
setInitSelection filter :515, subscribe :518, initSearch close :709. The two lambdas at
:330/:338 sit inside an anonymous TagsAdapter listener and are therefore excluded from the
MainActivity top-level count. That sequence matches every plan lambda name in this batch
($0, $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13). **Bytecode confirmation is still
owed at merge; no .class file was printed in this session.** Labels are unaffected by a
numbering swap within a group.

## Conventions recorded, not decided

- `confirmed_by` in this file is per-row: SOURCE = a printed direct in-app call site naming
  the method; INFERRED = reached only through unprinted framework/library dispatch
  (activity lifecycle, menu lifecycle, view-click dispatch, RecyclerView/adapter-library
  dispatch, Rx dispatch, JVM class initialisation) where the registration, show, entry, or
  method-reference site is printed. Labels are unaffected; only `confirmed_by` would change
  at merge under a whole-route INFERRED convention.
- **Strict-entry:** the launcher entry IS printed (manifest :43, MAIN :53 / LAUNCHER :54), so
  there is no strict-entry caveat for MainActivity.onCreate itself. Framework dispatch steps
  for lifecycle/callback rows are still INFERRED where the framework, not app code, performs
  the call.
- **FLAGGED — batch 108 row 30, `MainActivity.onFragmentFinished` (see table):** this row rests
  ONLY on the FragmentCallback contract. No printed in-app fragment caller of
  `MainActivity.onFragmentFinished` was found in any file freshly printed in this session
  (MainActivity.java, SessionLogFilterDialog.java, LogActivity.java, AndroidManifest.xml),
  and no `search_code` result was used to search for one. It is kept REACHABLE proposed
  INFERRED here on the contract (MainActivity `implements FragmentCallback` :98, body
  :806-811 handling DetailTorrentFragment + two-pane → `torrentDetailsClosed`), following
  the contract-only treatment used for sibling FragmentCallback rows. **It reverts to OPEN if
  the merger requires a printed fragment caller** — the merger must pick one convention for
  all FragmentCallback rows (cf. batch 99 row 2, batch 107/108 sibling rows, batch 114).
  This flag does not decide that convention, and it does not change any other row.

## Row verdicts (plan order)

| # | Method | Verdict | confirmed_by | Printed route / citation |
|---|---|---|---|---|
| 1 | SessionLogFilterDialog.onResume | REACHABLE proposed | INFERRED | Framework DialogFragment lifecycle after show() LogActivity.java:255 (showFilterDialog); body SessionLogFilterDialog.java:69-86 registers the back-key listener :74. Dispatch not printed. (Dialog rows 32-40 of batch 107 give the rest of this class; this row is batch 108 row 1 by plan split.) |
| 2 | MainActivity.<clinit> | REACHABLE proposed | INFERRED | Class load on launcher start; static TAG MainActivity.java:99 (getSimpleName(), not a compile-time constant) plus TAG_ABOUT_DIALOG :101, TAG_PERM_DENIED_DIALOG :102, ACTION_ADD_TORRENT_SHORTCUT :104. JVM step not printed. |
| 3 | MainActivity.<init> | REACHABLE proposed | INFERRED | Implicit default constructor; framework instantiates the MAIN/LAUNCHER activity (AndroidManifest.xml:43, :53-54). Framework step not printed. |
| 4 | MainActivity.applyExpandState | REACHABLE proposed | SOURCE | Called MainActivity.java:599 from onDrawerGroupsCreated; definition :603-608 (expandGroup / collapseGroup on drawerItemManager). |
| 5 | MainActivity.cleanGarbageFragments | REACHABLE proposed | SOURCE | Called MainActivity.java:187 from onCreate; definition :640-655 (removes DetailTorrentFragment/BlankFragment on large-screen devices). |
| 6 | MainActivity.getCurrentDetailFragment | REACHABLE proposed | SOURCE | Called MainActivity.java:450 from subscribeMsgViewModel torrents-deleted handler; definition :687-695 (two-pane check, findFragmentById). |
| 7 | MainActivity.initAboutDialog | REACHABLE proposed | SOURCE | Called MainActivity.java:419 from subscribeAlertDialog DIALOG_SHOWN branch; definition :776-793 (fills version/description views). |
| 8 | MainActivity.initDrawer | REACHABLE proposed | SOURCE | Called MainActivity.java:226 from initLayout; definition :230-291 (drawer manager, adapter, tags list, listeners). |
| 9 | MainActivity.initLayout | REACHABLE proposed | SOURCE | Called MainActivity.java:188 from onCreate; definition :191-228 (setContentView path via findViewById, toolbar, initDrawer :226, viewModel.resetSearch). |
| 10 | MainActivity.initSearch | REACHABLE proposed | SOURCE | Called MainActivity.java:701 from onCreateOptionsMenu; definition :707-726 (SearchView listeners, query hint, searchable info). |
| 11 | MainActivity.lambda$initDrawer$0 | REACHABLE proposed | INFERRED | Registered MainActivity.java:233 setOnGroupCollapseListener; body :234-235 saveGroupExpandState(groupPosition, false). Library listener dispatch not printed. |
| 12 | MainActivity.lambda$initDrawer$1 | REACHABLE proposed | INFERRED | Registered MainActivity.java:237 setOnGroupExpandListener; body :238-239 saveGroupExpandState(groupPosition, true). Library listener dispatch not printed. |
| 13 | MainActivity.lambda$initDrawer$2 | REACHABLE proposed | INFERRED | Registered MainActivity.java:273-275 addTagButton.setOnClickListener((v) -> startActivity AddTagActivity); framework click dispatch not printed. |
| 14 | MainActivity.lambda$initDrawer$3 | REACHABLE proposed | INFERRED | Registered MainActivity.java:282 tagsGroupHeader.setOnClickListener; body :283-290 toggles tagsExpandable and persists drawer_tags_is_expanded. Framework click dispatch not printed. |
| 15 | MainActivity.lambda$initSearch$13 | REACHABLE proposed | INFERRED | Registered MainActivity.java:709 searchView.setOnCloseListener; body :710-712 viewModel.resetSearch(), returns false. Framework SearchView dispatch not printed. |
| 16 | MainActivity.lambda$setInitSelection$11 | REACHABLE proposed | INFERRED | Registered MainActivity.java:515 filter in setInitSelection's Observable chain; body :515-516 (item instanceof TagItem && info.id == selectedTagId). Rx dispatch not printed. |
| 17 | MainActivity.lambda$setInitSelection$12 | REACHABLE proposed | INFERRED | Registered MainActivity.java:518 subscribe in the same chain; body :519-525 tagsAdapter.setSelectedItem + viewModel.setTagFilter(tag(...), true). Rx dispatch not printed. |
| 18 | MainActivity.lambda$subscribeAlertDialog$4 | REACHABLE proposed | INFERRED | Registered MainActivity.java:408 dialogViewModel.observeEvents().subscribe; body :409-434 dispatches TAG_ABOUT_DIALOG events to openChangelogLink :416 / initAboutDialog :419 and perm-denied events. Rx dispatch not printed. |
| 19 | MainActivity.lambda$subscribeMsgViewModel$5 | REACHABLE proposed | INFERRED | Registered MainActivity.java:444 observeTorrentDetailsClosed().subscribe((__) -> showBlankFragment()); Rx dispatch not printed. |
| 20 | MainActivity.lambda$subscribeMsgViewModel$6 | REACHABLE proposed | INFERRED | Registered MainActivity.java:449 observeTorrentsDeleted().subscribe; body :450-455 getCurrentDetailFragment check then showBlankFragment. Rx dispatch not printed. |
| 21 | MainActivity.lambda$subscribeNeedStartEngine$7 | REACHABLE proposed | INFERRED | Registered MainActivity.java:466 filter((needStart) -> needStart); Rx dispatch not printed. Passthrough gate for row 22. |
| 22 | MainActivity.lambda$subscribeNeedStartEngine$8 | REACHABLE proposed | INFERRED | Registered MainActivity.java:467 subscribe((needStart) -> viewModel.startEngine()); Rx dispatch not printed. |
| 23 | MainActivity.lambda$subscribeTags$10 | REACHABLE proposed | INFERRED | Plan order row 23 (see plan-order note). Registered MainActivity.java:481 subscribe; body :482-486 setInitSelection(items) if adapter empty, then tagsAdapter.submitList(items). Rx dispatch not printed. |
| 24 | MainActivity.lambda$subscribeTags$9 | REACHABLE proposed | INFERRED | Plan order row 24. Registered MainActivity.java:473 flatMapSingle; body :474-480 builds EmptyTagItem + NoTagsItem + TagItem list from the tag list. Rx dispatch not printed. |
| 25 | MainActivity.onCreate | REACHABLE proposed | INFERRED | MAIN/LAUNCHER entry, AndroidManifest.xml:43, :53-54; framework activity lifecycle dispatch not printed. Body :136-189 (permission manager, cleanGarbageFragments :187, initLayout :188). |
| 26 | MainActivity.onCreateOptionsMenu | REACHABLE proposed | INFERRED | Framework menu lifecycle; body :698-705 (toolbar.inflateMenu, initSearch :701, setOnMenuItemClickListener :702). Dispatch not printed. |
| 27 | MainActivity.onDestroy | REACHABLE proposed | INFERRED | Framework activity lifecycle; body :399-404 (viewModel.requestStopEngine if non-null, super.onDestroy). Dispatch not printed. |
| 28 | MainActivity.onDrawerGroupsCreated | REACHABLE proposed | SOURCE | Called MainActivity.java:252 from initDrawer; definition :582-601 (per-group status/sort/date filters, applyExpandState :599). |
| 29 | MainActivity.onDrawerItemSelected | REACHABLE proposed | INFERRED | Passed as method reference MainActivity.java:250 to DrawerExpandableAdapter constructor (this::onDrawerItemSelected); adapter-library dispatch not printed. Body :610-631 (status/sort/date filter + saveSelectionState :627). |
| 30 | MainActivity.onFragmentFinished | REACHABLE proposed | INFERRED | **FLAGGED — contract only, see conventions section.** FragmentCallback interface method; no printed in-app fragment caller in any file freshly printed in this session — invoked by fragments through the FragmentCallback contract. Body :806-811 (DetailTorrentFragment + two-pane -> torrentDetailsClosed). Dispatch not printed. **Reverts to OPEN if the merger requires a printed fragment caller.** |
| 31 | MainActivity.onOptionsItemSelected | REACHABLE proposed | INFERRED | Registered MainActivity.java:702 toolbar.setOnMenuItemClickListener(this::onOptionsItemSelected); framework/menu dispatch not printed. Body :738-759 (feed/settings/about/shutdown/pause/resume/log branches; log branch :754-755 -> showLog()). |
| 32 | MainActivity.onPostCreate | REACHABLE proposed | INFERRED | Framework activity lifecycle; body :373-379 (toggle.syncState). Dispatch not printed. |
| 33 | MainActivity.onStart | REACHABLE proposed | INFERRED | Framework activity lifecycle; body :381-390 (subscribeAlertDialog :384, subscribeMsgViewModel :385, subscribeNeedStartEngine :387, subscribeTags :388). Dispatch not printed. |
| 34 | MainActivity.onStop | REACHABLE proposed | INFERRED | Framework activity lifecycle; body :392-397 (disposables.clear, super.onStop). Dispatch not printed. |
| 35 | MainActivity.openChangelogLink | REACHABLE proposed | SOURCE | Called MainActivity.java:416 from subscribeAlertDialog lambda (NEGATIVE_BUTTON_CLICKED on about dialog); definition :795-799 (ACTION_VIEW intent with about_changelog_link). |
| 36 | MainActivity.saveGroupExpandState | REACHABLE proposed | SOURCE | Called from rows 11/12 (MainActivity.java:235, :239); definition :559-580 (persists drawer_status/sorting/time expanded flags). |
| 37 | MainActivity.saveSelectedTag | REACHABLE proposed | SOURCE | Called MainActivity.java:309 (tagsClickListener onTagSelected) and :333 (delete-tag success); definition :352-371 (persists drawer_tags_selected_item). |
| 38 | MainActivity.saveSelectionState | REACHABLE proposed | SOURCE | Called MainActivity.java:627 from onDrawerItemSelected; definition :633-638 (persists prefKey -> item.id). |
| 39 | MainActivity.setInitSelection | REACHABLE proposed | SOURCE | Called MainActivity.java:483 from subscribeTags lambda (row 23's body); definition :490-557 (empty/no-tags/tag-id branches, Rx filter/subscribe rows 16/17). |
| 40 | MainActivity.showAboutDialog | REACHABLE proposed | SOURCE | Called MainActivity.java:745 from onOptionsItemSelected (about_menu branch); definition :761-774 (BaseAlertDialog.newInstance + show, TAG_ABOUT_DIALOG). |

## Totals — mechanically verified

- Total: 40 rows, sequence 1–40 intact, in plan order (including rows 23/24 in plan order).
- REACHABLE proposed: 40 (SOURCE 14, INFERRED 26).
- UNREACHABLE proposed: 0.
- OPEN: 0.
- SOURCE rows: 4, 5, 6, 7, 8, 9, 10, 28, 35, 36, 37, 38, 39, 40 = 14.
- INFERRED rows: 1, 2, 3, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34 = 26.
- 14 + 26 = 40. Verified for merge: 0 / 40.

## Gaps the merger must close before merging

1. **Row 30 `onFragmentFinished`:** print a fragment caller (e.g. a fragment's `finish()` /
   FragmentCallback invocation naming MainActivity), or adopt the contract-only convention
   for all FragmentCallback rows. Until then the row is conditional (see flag above).
2. **Lambda numbering:** confirm $0–$13 against bytecode at merge; no .class file was printed here.
3. Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run here.
4. No row in this batch was flipped to UNREACHABLE, so no full-repo grep is owed for a
   UNREACHABLE claim in this batch.
