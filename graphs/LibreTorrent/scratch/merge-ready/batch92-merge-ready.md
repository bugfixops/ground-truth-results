**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

**OPEN-CLOSING REVISION 2026-11-01 (UNVERIFIED, no push, no merge): 0 label changes. Counts before = after: 39 REACHABLE / 0 UNREACHABLE / 1 OPEN (row 35).**
**OPEN-CLOSING ROUND 2 REVISION 2026-11-01 (UNVERIFIED, no push, no merge): 0 label changes. Counts before = after: 39 REACHABLE / 0 UNREACHABLE / 1 OPEN (row 35). Saved 252-file greps in /home/hatch/workspace/b90929495969799102-openclose2-src/ (grep_class_TorrentContentFileItem.txt 52 lines; grep_toString_calls.txt: the only toString line on this type is the internal super.toString() at TorrentContentFileItem.java:105) support, but do NOT by themselves close, row 35 — same undecided toString-dispatch question as batch 90 rows 16/28; see the CONDITIONAL table in row 35. Round-1 citation-drift corrections PRESERVED, not reverted (adapter construction :207, animator :213, setItemAnimator :219, SelectionTracker storage :227, tracker state save :309, Parcel ctor span :47-54). Build: not run. C1: not run. 0 rows verified for merge.**
Fresh source for this pass saved in ~/workspace/b90929495969799102-openclose-src/ (branch work-2026-10-31, one file at a time with ~25 s pauses, no fresh HTTP 429; each file plus its raw connector JSON saved; fresh-corpus grep in grep_fresh_corpus.txt — a PRINTED-SUBSET grep only, NOT a saved full-repo grep, so it cannot flip any row to UNREACHABLE).
Fresh files re-verified for the OPEN row: `ui/detailtorrent/pages/files/TorrentContentFileItem.java` (110 lines, SHA 379ce0f1a956307715428b67cd6acdd96f101ada), `ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java` (543 lines, SHA a1f2ccc63a8b38c9ddf7ba95c6cb60db5b7f56b7), `ui/detailtorrent/pages/files/TorrentContentFilesAdapter.java` (338 lines, SHA 419495fa9500071f9d3b7d1385218018e87a67de).
Row 35: toString definition re-confirmed fresh at TorrentContentFileItem.java:102-108 (super.toString() at :105 is the file's only other toString line); zero toString hits in fresh DetailTorrentFilesFragment.java; the adapter's Selectable methods (:95 getItemKey, :104 getItemPosition, inner KeyProvider :267-286) are for the item key, not a toString call. Lead-only cross-check (NOT fresh evidence, NOT a full-repo grep): a grep over the parent's 252-file app-Java reconstruction finds no toString call on this type in app Java. Stays OPEN; named target: a saved full-repo grep for a toString call or concatenation site. Build: not run. C1: not run. 0 rows verified for merge.


# LibreTorrent batch 92 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file. No tool coverage, old generated graphs,
or build REACHABLE counts used as evidence.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 92 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior proposal
  (`~/workspace/libretorrent-batch92-proposal.md`) was used as an INPUT / lead list only;
  every row below was checked against source freshly printed in this pass (see below),
  and no prior verdict was copied as a result. The one prior OPEN row (row 35,
  `TorrentContentFileItem.toString`) was freshly re-checked and stays OPEN — see row 35.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 92 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,733 lines incl. header, plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-92 rows are `TODO_CANDIDATE_REACHABLE` in the plan with current label
"REACHABLE (generator candidate, no hand route yet)" — candidates, not evidence.
Plan order preserved below; method names below match the plan exactly, in order.

## Printed source used in this pass (fresh connector fetches, branch work-2026-10-31, one file at a time with pauses)

All under `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`,
saved in `~/workspace/b9192-src/`:

- `ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java` — fresh, 543 lines.
  onAttach :120, onDetach :129, onStop :138, onStart :146 (subscribeAdapter :148,
  subscribeAlertDialog :149), subscribeAdapter :154-167 (map `TorrentContentFileItem::new`
  :160, submitList :163, updateFileSize :164), subscribeAlertDialog :170-191,
  onViewCreated :193-289 (adapter `new TorrentContentFilesAdapter(this)` :207, animator :213,
  SelectionTracker :225-247, observer :249, actionModeCallback :256/:279),
  onSaveInstanceState :305-312, onViewStateRestored :315-321, onResume :324-330,
  onItemClicked :333-349 (success consumer :343-346, error ref :345),
  onItemCheckedChanged :351-356, setActionModeTitle :358-361 (callers :257/:265/:280),
  initPriorityDialog :436, changePriority :477, shareStreamUrl :509-524,
  openFile :527-533, handleOpenFileError :535. No `toString` caller in this file
  (grep over the fresh copy returns no `toString` line at all).
- `ui/detailtorrent/pages/files/TorrentContentFilesAdapter.java` — fresh, 337 lines.
  TAG :54, diffCallback :109, areContentsTheSame :112, equalsContent call :115,
  ViewHolder bind click listeners :166-175 (onItemClicked :171, onItemCheckedChanged :175),
  ClickListener interface :254-259. No `toString` caller in this file.
- `ui/detailtorrent/pages/files/TorrentContentFileItem.java` — fresh, 110 lines.
  `<init>(Tree)` :38-45, `<init>(Parcel)` :47-54, describeContents :57-60,
  writeToParcel :63-70, CREATOR :72-86, createFromParcel :76-79, newArray :82-85,
  equalsContent :88-97, toString :102-108 (definition only; its only `toString` line
  inside the file is the `super.toString()` call at :105, which is internal, not a route).
- `ui/detailtorrent/DetailPagerAdapter.java` — fresh, 76 lines. FILES_FRAG_POS :41,
  createFragment :53, Files newInstance :60 — the pager anchor for the fragment rows.
- `ui/detailtorrent/pages/DetailTorrentInfoFragment.java` and
  `ui/detailtorrent/pages/DetailTorrentStateFragment.java` — fresh (324 / 87 lines);
  fetched for the shared batch-91 trunk, not needed for any batch-92 row directly.

NOT freshly fetched in this pass: `DetailTorrentFragment.java` (pager section) and
`DetailTorrentActivity.java`. See strict-entry caveat.

## Shared trunk

DetailPagerAdapter.createFragment returns DetailTorrentFilesFragment.newInstance()
(FILES_FRAG_POS) — fresh, DetailPagerAdapter :53/:60. ViewPager2 instantiates the
fragment; its lifecycle methods then run, and onViewCreated builds the adapter,
SelectionTracker, observers, and action-mode callback.

## confirmed_by convention used here — recorded, NOT decided (undecided convention)

- SOURCE: a named method with a printed direct in-app call site, or a fragment
  lifecycle method of a fragment whose pager host is printed above.
- INFERRED: compiler-generated `<init>`/`<clinit>`, anonymous-class/listener callbacks,
  and framework dispatch (RecyclerView, SelectionTracker, ActionMode, Parcelable),
  where registration/creation is printed but the dispatching call is not.
- This is the per-row convention. If the merger adopts the whole-route INFERRED
  convention used in some earlier batches (e.g. batch 14), labels are unaffected;
  only the confirmed_by of SOURCE rows whose route crosses unprinted framework/Rx
  dispatch would change to INFERRED. The merger must pick one convention for all
  batches; this file does not decide it.

## Strict-entry caveat — recorded, NOT decided (undecided convention)

The step that creates/shows DetailTorrentFragment itself (e.g. DetailTorrentActivity)
was NOT printed in this pass. Under a strict launcher-entry rule every REACHABLE row
below reverts to OPEN. Labels below are proposed on the pager anchor, as prior detail
batches did. Prior batches 87-88 printed DetailTorrentActivity.onCreate :67-71 as a
lead only; it was NOT re-printed here and is NOT used as fresh evidence in this file.

## Anonymous numbering — NOT bytecode-verified

FilesFragment anonymous classes match source order: $1 = DefaultItemAnimator (:213),
$2 = SelectionPredicate (:226), $3 = SelectionObserver (:249), $4 = ActionMode.Callback
(field :363). Confirm against bytecode at merge if disputed; no bytecode was read.
A swap within a group would not change any label.

## Parcelable rows — weakest INFERRED, recorded

Rows 33, 36, 38, 39 (describeContents, writeToParcel, createFromParcel, newArray) are
INFERRED via the Parcelable contract plus the printed SelectionTracker storage
(FilesFragment :227 `StorageStrategy.createParcelableStorage(TorrentContentFileItem.class)`)
and onSaveInstanceState :309. No printed direct caller names any of them. If the merger
requires a printed parcel/unparcel site, those four rows revert to OPEN — labels for
the rest of the batch are unaffected. Row 31 (`<init>(Parcel)`) is SOURCE, not INFERRED,
because createFromParcel's printed body at Item :76-79 directly calls it.

## Counts — proposed, NOT verified

- REACHABLE proposed: 39 / 40 (SOURCE 18 / INFERRED 21)
- UNREACHABLE proposed: 0
- OPEN: 1 (TorrentContentFileItem.toString — row 35, see below)
- Verified for merge: 0

Counts were mechanically verified after writing (40 table rows, sequence 1-40 intact,
in plan order). No UNREACHABLE row is claimed: no saved full-repo grep was run
(connector search_code 0 results are not evidence of absence and were not used),
and no row was flipped to UNREACHABLE.

## Per-method table (plan order)

| # | Method | Label | confirmed_by | Printed route / citation |
|---|---|---|---|---|
| 1 | DetailTorrentFilesFragment.onItemCheckedChanged | REACHABLE | SOURCE | FilesFragment.java:351-356 (applies priority, updateFileSize). Adapter ViewHolder.bind priority click listener calls listener.onItemCheckedChanged(item, isChecked) (Adapter.java:173-175); listener is the fragment, passed at FilesFragment.java:207 `new TorrentContentFilesAdapter(this)`. ClickListener interface Adapter.java:254-259. |
| 2 | DetailTorrentFilesFragment.onItemClicked | REACHABLE | SOURCE | FilesFragment.java:333-349. Adapter ViewHolder.bind item click listener calls listener.onItemClicked(item) (Adapter.java:166-171); same registration as row 1. |
| 3 | DetailTorrentFilesFragment.onResume | REACHABLE | SOURCE | FilesFragment.java:324-330; restores listFilesState; pager-hosted lifecycle. |
| 4 | DetailTorrentFilesFragment.onSaveInstanceState | REACHABLE | SOURCE | FilesFragment.java:305-312; saves layoutManager state + selectionTracker state; pager-hosted lifecycle. |
| 5 | DetailTorrentFilesFragment.onStart | REACHABLE | SOURCE | FilesFragment.java:146-151: onStart calls subscribeAdapter() and subscribeAlertDialog(). |
| 6 | DetailTorrentFilesFragment.onStop | REACHABLE | SOURCE | FilesFragment.java:138-143: onStop clears disposables; pager-hosted lifecycle. |
| 7 | DetailTorrentFilesFragment.onViewCreated | REACHABLE | SOURCE | FilesFragment.java:193-289; builds adapter, animator, SelectionTracker, observers, action-mode callback; pager-hosted lifecycle. |
| 8 | DetailTorrentFilesFragment.onViewStateRestored | REACHABLE | SOURCE | FilesFragment.java:315-321; restores listFilesState from saved bundle; pager-hosted lifecycle. |
| 9 | DetailTorrentFilesFragment.openFile | REACHABLE | SOURCE | FilesFragment.java:527-533; called from onItemClicked subscribe consumer (batch 91 row 33), FilesFragment.java:343-346. |
| 10 | DetailTorrentFilesFragment.setActionModeTitle | REACHABLE | SOURCE | FilesFragment.java:358-361; called from $3.onSelectionChanged (:257, :265) and $3.onSelectionRestored (:280). |
| 11 | DetailTorrentFilesFragment.shareStreamUrl | REACHABLE | SOURCE | FilesFragment.java:509-524; called from $4.onActionItemClicked share_stream_url_menu branch, :400-403. |
| 12 | DetailTorrentFilesFragment.showPriorityDialog | REACHABLE | SOURCE | FilesFragment.java:416-433; called from $4.onActionItemClicked change_priority_menu branch, :397-399. |
| 13 | DetailTorrentFilesFragment.subscribeAdapter | REACHABLE | SOURCE | FilesFragment.java:154-167; called from onStart :148. |
| 14 | DetailTorrentFilesFragment.subscribeAlertDialog | REACHABLE | SOURCE | FilesFragment.java:170-191; called from onStart :149. |
| 15 | DetailTorrentFilesFragment.updateFileSize | REACHABLE | SOURCE | FilesFragment.java:292-301; called from subscribeAdapter consumer :164 and from onItemCheckedChanged :355. |
| 16 | DetailTorrentFilesFragment$1.<init> | REACHABLE | INFERRED | Anonymous DefaultItemAnimator, created in onViewCreated, FilesFragment.java:213; instantiated when the fragment view is created. |
| 17 | DetailTorrentFilesFragment$1.canReuseUpdatedViewHolder | REACHABLE | INFERRED | Anonymous method FilesFragment.java:215-219 (returns true); RecyclerView calls it via animator set at :219; framework dispatch INFERRED. |
| 18 | DetailTorrentFilesFragment$2.<init> | REACHABLE | INFERRED | Anonymous SelectionTracker.SelectionPredicate, created in onViewCreated, FilesFragment.java:226; built into selectionTracker at :225-247. |
| 19 | DetailTorrentFilesFragment$2.canSelectMultiple | REACHABLE | INFERRED | Predicate method FilesFragment.java:242-245 (returns true); SelectionTracker framework dispatch INFERRED, predicate registered :226-247. |
| 20 | DetailTorrentFilesFragment$2.canSetStateAtPosition | REACHABLE | INFERRED | Predicate method FilesFragment.java:236-240 (returns true); same dispatch/registration as row 19. |
| 21 | DetailTorrentFilesFragment$2.canSetStateForKey | REACHABLE | INFERRED | Predicate method FilesFragment.java:230-234 (rejects PARENT_DIR); same dispatch/registration as row 19. |
| 22 | DetailTorrentFilesFragment$3.<init> | REACHABLE | INFERRED | Anonymous SelectionTracker.SelectionObserver, created in onViewCreated, FilesFragment.java:249; added via selectionTracker.addObserver at :249. |
| 23 | DetailTorrentFilesFragment$3.onSelectionChanged | REACHABLE | INFERRED | Observer method FilesFragment.java:251-273; starts/finishes actionMode, updates title; SelectionTracker dispatch INFERRED. |
| 24 | DetailTorrentFilesFragment$3.onSelectionRestored | REACHABLE | INFERRED | Observer method FilesFragment.java:275-282; starts actionMode, updates title; same dispatch as row 23. |
| 25 | DetailTorrentFilesFragment$4.<init> | REACHABLE | INFERRED | Anonymous ActionMode.Callback, field initialiser FilesFragment.java:363; started via activity.startSupportActionMode(actionModeCallback) at :256 and :279. |
| 26 | DetailTorrentFilesFragment$4.onActionItemClicked | REACHABLE | INFERRED | Callback method FilesFragment.java:394-405; routes to showPriorityDialog / shareStreamUrl; ActionMode framework dispatch INFERRED. |
| 27 | DetailTorrentFilesFragment$4.onCreateActionMode | REACHABLE | INFERRED | Callback method FilesFragment.java:384-392; inflates action-mode menu; same dispatch as row 26. |
| 28 | DetailTorrentFilesFragment$4.onDestroyActionMode | REACHABLE | INFERRED | Callback method FilesFragment.java:408-413; clears selection, resets action-mode state; same dispatch as row 26. |
| 29 | DetailTorrentFilesFragment$4.onPrepareActionMode | REACHABLE | INFERRED | Callback method FilesFragment.java:366-381; toggles share_stream_url_menu visibility; same dispatch as row 26. |
| 30 | TorrentContentFileItem.<clinit> | REACHABLE | INFERRED | Static CREATOR field, TorrentContentFileItem.java:72-86; class initialiser runs on first active use, e.g. FilesFragment.java:160 method reference TorrentContentFileItem::new and :227 StorageStrategy.createParcelableStorage(TorrentContentFileItem.class). |
| 31 | TorrentContentFileItem.<init>(Parcel) | REACHABLE | SOURCE | TorrentContentFileItem.java:47-54; called directly by $1.createFromParcel at :76-79 (`new TorrentContentFileItem(source)`). |
| 32 | TorrentContentFileItem.<init>(TorrentContentFileTree) | REACHABLE | SOURCE | TorrentContentFileItem.java:38-45; called via method reference TorrentContentFileItem::new in FilesFragment.subscribeAdapter, FilesFragment.java:160 (fresh print; proposal cited :157-160). |
| 33 | TorrentContentFileItem.describeContents | REACHABLE | INFERRED | TorrentContentFileItem.java:57-60 (returns 0). Parcelable contract method; framework calls it when parceling items, e.g. SelectionTracker storage created at FilesFragment.java:227 and onSaveInstanceState :309. No printed direct caller; dispatch INFERRED, not SOURCE. See Parcelable caveat above. |
| 34 | TorrentContentFileItem.equalsContent | REACHABLE | SOURCE | TorrentContentFileItem.java:88-97; called directly by Adapter diffCallback.areContentsTheSame, Adapter.java:112-115 (`oldItem.equalsContent(newItem)`); diffCallback is passed to ListAdapter at Adapter.java:61 and runs on adapter.submitList (FilesFragment.java:163). |
| 35 | TorrentContentFileItem.toString | OPEN | — | TorrentContentFileItem.java:102-108. Freshly re-checked in this pass: no caller printed in any freshly fetched file (FilesFragment, Adapter, Item itself — grep over the fresh FilesFragment copy returns no `toString` line at all; the Item file's only `toString` line besides the definition is the internal `super.toString()` call at :105). Do NOT flip to UNREACHABLE: toString is plausibly called by logging/concatenation elsewhere; needs a saved full-repo grep. Highest-priority grep target for this batch. This is the task's named OPEN row, and it stays OPEN. 2026-11-01 OPEN-closing re-check (fresh): definition re-confirmed TorrentContentFileItem.java:102-108; zero toString hits in fresh DetailTorrentFilesFragment.java; adapter Selectable methods are key methods, not toString. Stays OPEN; named target: saved full-repo grep for a toString/concat site. 2026-11-01 OPEN-closing ROUND 2 — CONDITIONAL TABLE (convention NOT decided, row stays OPEN): (a) IF the merger adopts the 252-file app-Java grep as sufficient for toString rows → UNREACHABLE, kind no_trigger_in_app (saved grep_class_TorrentContentFileItem.txt: all 52 hits are construction, parcel, selection, adapter/diff sites — no .toString() call, log, or concatenation site on this type; the only toString line in its own file is the internal super.toString() at :105). (b) IF the merger requires coverage of implicit dispatch (concatenation, logging, List.toString element dispatch, databinding text, generated code) or a project toString-dispatch rule → stays OPEN. Resolver: the merger's one toString-dispatch rule, applied project-wide. |
| 36 | TorrentContentFileItem.writeToParcel | REACHABLE | INFERRED | TorrentContentFileItem.java:63-70. Parcelable contract method; framework calls it when parceling items via the SelectionTracker storage (FilesFragment.java:227, :309). No printed direct caller; dispatch INFERRED. See Parcelable caveat above. |
| 37 | TorrentContentFileItem$1.<init> | REACHABLE | INFERRED | Anonymous Parcelable.Creator, TorrentContentFileItem.java:72-73; instantiated at class initialisation (row 30). |
| 38 | TorrentContentFileItem$1.createFromParcel | REACHABLE | INFERRED | Creator method TorrentContentFileItem.java:76-79; framework calls it when unparceling items restored by SelectionTracker storage; no printed direct caller, dispatch INFERRED. See Parcelable caveat above. |
| 39 | TorrentContentFileItem$1.newArray | REACHABLE | INFERRED | Creator method TorrentContentFileItem.java:82-85; framework calls it when unparceling item arrays; same dispatch basis as row 38. See Parcelable caveat above. |
| 40 | TorrentContentFilesAdapter.<clinit> | REACHABLE | INFERRED | Static TAG and diffCallback fields, Adapter.java:54 and :109; class initialiser runs on first active use, i.e. `new TorrentContentFilesAdapter(this)` at FilesFragment.java:207. |

## What is NOT claimed / still owed

- No UNREACHABLE row: no saved full-repo grep was run; connector search_code 0 results
  are not evidence of absence and were not used.
- Row 35 (toString) stays OPEN pending that grep — it is the only OPEN row in this batch,
  and the only row in either batch 91 or 92 that is not proposed REACHABLE.
- Strict-entry step (launcher -> DetailTorrentActivity -> DetailTorrentFragment) not freshly
  printed; see caveat above — under a strict rule all 39 REACHABLE rows revert to OPEN.
- Build, sampler, C1, and full-repo grep all still owed on a full checkout (git clone
  fails in this VM; named missing check, not passed).
- Main-agent spot-check (1 in 5), py_compile, build, Mac build/C1 — not run.
- 0/40 verified for merge. Nothing merged, nothing pushed. No fresh HTTP 429 was hit
  in this pass (five fresh connector fetches, one file at a time with ~20 s pauses).
