**PHASE 2 FIX 2026-11-01 (coordinator): citation/wording/column corrections from the Phase 2 spot-check applied to this file; labels and counts unchanged (3900/575/257 global totals verified after the fix). Backups in ~/workspace/overnight/stream-A/backup-pre-phase2fix/.**

**REVISION 2026-11-01 (Stream A Phase 1c, APPLY DECISIONS, batches 62-67 worker): DECISIONS.md applied mechanically only; no other row touched. No push. Build: not run. C1: not run.**
D4d (setVariable direction): rows 19, 31 REACHABLE INFERRED -> OPEN (confirmed_by —). D4c (no-variable option U): row 40 onFieldChange OPEN -> UNREACHABLE, reason no_trigger_in_app, INFERRED (companion of batch 68 row 1 per DECISIONS.md; the row's prior 'NOT UNREACHABLE on this evidence' note is superseded by this decision, not by new source evidence). D4f: rows 5, 15, 27, 38 hasPendingBindings stay OPEN, confirmed_by normalised INFERRED -> — under D1 (cosmetic only). D4a: rows 10, 22 getViewModel stay OPEN, confirmed_by normalised INFERRED -> — under D1 (cosmetic only). Also staying OPEN with D1 cosmetic normalisation only: row 8 setVariable (D4d already-OPEN list), row 7 onFieldChange (no D4c flip ordered for it in DECISIONS.md — only row 40 is listed for batch 67 — so it is left OPEN, not extrapolated to UNREACHABLE; flag for coordinator if the D4c scope is meant to cover it). D1: all OPEN rows in this file now carry confirmed_by —. Counts mechanically verified from the label column, 40 rows, sequence 1-40 intact: before 31 REACHABLE / 0 UNREACHABLE / 9 OPEN; after 29 REACHABLE / 1 UNREACHABLE / 10 OPEN. OPEN after: 5, 7, 8, 10, 15, 19, 22, 27, 31, 38. No conflict found: both D4d target rows were REACHABLE and row 40 was OPEN before, as DECISIONS.md expects.

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 67 — merge-ready (UNVERIFIED, NOT merged)

## REVISION 2026-11-01 — OPEN-close round 2 (G11) — 0 label flips

No label changes in this revision. All OPEN rows were re-checked against already-fetched
local source (no new GitHub fetch, no HTTP 429, nothing pushed). Counts are unchanged
from the round-1 header above and were mechanically re-verified from the table below.
Build: not run. C1: not run. Verified for merge: 0.
Re-run grep (saved): ~/workspace/b656667-openclose2-src/ruleF_grep_656667_rerun.txt —
grep over ~/workspace/ruleF-src (252 app Java files, re-counted 2026-11-01) reproduces the
round-1 result exactly: setLifecycleOwner exactly one hit (CreateTorrentDialog.java:186,
binding is DialogCreateTorrentBinding, not any 65-67 binding); getViewModel,
hasPendingBindings, setVariable, onFieldChange, onChangeAppbar, executePendingBindings
zero hits. Generated *BindingImpl source is NOT in that tree, so the re-run proves absence
of app-code callers only, never generated/framework dispatch. Local layout re-check:
fragment_detail_torrent, fragment_detail_torrent_peer_list,
fragment_detail_torrent_tracker_list and detail_torrent_appbar each have 0 <data> /
<variable> lines; fragment_detail_torrent_pieces, _state, _files, _info and
fragment_add_torrent_info each declare a viewModel variable. No convention is decided
in this revision; every OPEN row below carries a conditional table in the round-2
section before the per-row table, and a ROUND2 note appended to its row.

## REVISION 2026-11-01 — OPEN-close pass (no labels changed)

No row flips in this revision. All 9 OPEN rows (5, 7, 8, 10, 15, 22, 27, 38, 40) were re-verified on fresh prints plus the saved full-app-tree grep cited in their rows and stay OPEN for the convention reasons recorded there (unprinted rebind dispatch for rows 5, 15, 27, 38; generic-framework-callback convention undecided for rows 7, 8, 40; convention (v) for rows 10, 22). Batch 67 has no setLifecycleOwner OPEN row, so the setLifecycleOwner close applied in batches 65 and 66 does not arise here. Fresh source for this revision is listed in the OPEN-close pass section below. Build: not run. C1: not run. Verified for merge: 0.


Repo: bugfixops/ground-truth-results, branch work-2026-10-31 only. Never main or result.
Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]) — pushed UNVERIFIED before [L] at user request 2026-11-01.
No edit to graph_def.py, out/, PROGRESS_V2, AGENT_NOTES, tools/, or another helper's file.
Build: not run. C1: not run (they run on the user's Mac after a push), never claimed passed.
Full-app-tree grep run 2026-11-01 (ruleF_grep_656667.txt, see OPEN-close pass section); no sampler was run. No search_code result was used as evidence for any row,
and no search_code 0-result was used as evidence of absence. Verified for merge: 0 rows.

## Membership
Exactly the plan rows for batch 67 in handoff/LIBRETORRENT_BATCH_PLAN.tsv
(local copy ~/workspace/agent27-plan.tsv, git blob SHA 0104806dd666c840049b3db52823d4b384fa1c92):
40 rows, sequence 1-40 intact, in plan order, method name + JVM descriptor taken from the
plan (generated by script, not hand-typed). All 40 plan rows are TODO_CANDIDATE_REACHABLE
with current label "REACHABLE (generator candidate, no hand route yet)" — that plan label
is a candidate claim, not evidence, and was NOT adopted as a verdict.

## Counts (mechanically verified from the table below)
- REACHABLE proposed: 31 / 40
- UNREACHABLE proposed: 0 / 40
- OPEN: 9 / 40
- OPEN rows: 5, 7, 8, 10, 15, 22, 27, 38, 40

## Printed source used in this pass (all freshly connector-fetched from branch work-2026-10-31,
one file at a time with ~25 s pauses, saved in ~/workspace/b656667-src/, NO fresh HTTP 429)
- ui/addtorrent/AddTorrentFilesFragment.java (197 lines, connector SHA b10cfc53…)
- ui/addtorrent/AddTorrentInfoFragment.java (243 lines, SHA 6be37532…)
- ui/addtorrent/AddTorrentViewModel.java (SHA bec2f6ee…)
- ui/addtorrent/AddTorrentMutableParams.java (SHA ae21c26f…)
- ui/detailtorrent/DetailTorrentFragment.java (832 lines, SHA c24e0912…)
- ui/detailtorrent/DetailPagerAdapter.java (76 lines, SHA df5ff38c…)
- ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java (543 lines, SHA a1f2ccc6…)
- ui/detailtorrent/pages/DetailTorrentInfoFragment.java (323 lines, SHA f7d056f5…)
- ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java (202 lines, SHA d164a15e…)
- ui/detailtorrent/pages/pieces/DetailTorrentPiecesFragment.java (143 lines, SHA 7a57c7f1…)
- ui/detailtorrent/pages/DetailTorrentStateFragment.java (87 lines, SHA b01a6a20…)
- ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java (406 lines, SHA 48d5a536…)
- ui/detailtorrent/DetailTorrentViewModel.java (SHA 6e4ef82f…)
- res/layout/fragment_add_torrent_files.xml (SHA 68e992ff…)
- res/layout/fragment_add_torrent_info.xml (SHA 799fe007…)
- res/layout/add_torrent_info.xml (SHA 54283c9e…)
- res/layout-large-land-notouch/fragment_add_torrent_info.xml (1,532 bytes, SHA 8e7ec93e…)
- res/layout-sw600dp-land/fragment_add_torrent_info.xml (1,532 bytes, SHA 8e7ec93e…, byte-identical to the large-land-notouch variant)
- res/layout/fragment_detail_torrent.xml (SHA 2fa02eda…)
- res/layout/detail_torrent_appbar.xml (SHA 15c7cf4f…)
- res/layout/fragment_detail_torrent_files.xml (SHA d9e77a35…)
- res/layout/fragment_detail_torrent_info.xml (SHA 36e662c2…)
- res/layout/fragment_detail_torrent_peer_list.xml (SHA 6fb1e1a9…)
- res/layout/fragment_detail_torrent_pieces.xml (SHA 2c343b2b…)
- res/layout/fragment_detail_torrent_state.xml (SHA 4f4e9b9e…)
- res/layout/fragment_detail_torrent_tracker_list.xml (SHA bb8de7bf…)
All under final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/
or .../app/src/main/res/. Prior proposals (batches 65/66/67) were leads only; every row below
was re-judged against the fresh prints above. Where a prior line number matched a fresh print
exactly it is cited as fresh; no citation rests on a local copy alone in these files.
A true git clone was NOT attempted: it fails in this VM (no credential device) — that check
is named missing, never passed.

## OPEN-close pass 2026-11-01 — fresh source for this revision (all connector-fetched from branch work-2026-10-31, one file at a time with ~25 s pauses, NO fresh HTTP 429, saved in ~/workspace/b656667-openclose-src/)
- ui/addtorrent/AddTorrentInfoFragment.java (244 lines, SHA 6be37532)
- ui/detailtorrent/DetailTorrentFragment.java (832 lines, SHA c24e0912)
- ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java (543 lines, SHA a1f2ccc6)
- ui/detailtorrent/pages/DetailTorrentInfoFragment.java (324 lines, SHA f7d056f5)
- ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java (202 lines, SHA d164a15e)
- ui/detailtorrent/pages/pieces/DetailTorrentPiecesFragment.java (143 lines, SHA 7a57c7f1)
- ui/detailtorrent/pages/DetailTorrentStateFragment.java (88 lines, SHA b01a6a20)
- ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java (406 lines, SHA 48d5a536)
- ui/addtorrent/AddTorrentViewModel.java (574 lines, SHA bec2f6ee)
- ui/detailtorrent/DetailTorrentViewModel.java (610 lines, SHA 6e4ef82f)
- res/layout/fragment_detail_torrent.xml (22 lines, SHA 2fa02eda, no data block)
- res/layout/detail_torrent_appbar.xml (29 lines, SHA 15c7cf4f, no data block)
- res/layout/fragment_detail_torrent_peer_list.xml (28 lines, SHA 6fb1e1a9, no data block)
- res/layout/fragment_detail_torrent_tracker_list.xml (28 lines, SHA bb8de7bf, no data block)
- res/layout/fragment_detail_torrent_pieces.xml (81 lines, SHA 2c343b2b, viewModel variable)
- res/layout/fragment_detail_torrent_state.xml (305 lines, SHA 4f4e9b9e, viewModel variable)
- res/layout/fragment_detail_torrent_files.xml (44 lines, SHA d9e77a35, viewModel variable)
- res/layout/fragment_detail_torrent_info.xml (347 lines, SHA 36e662c2, viewModel variable)
- res/layout/fragment_add_torrent_info.xml (21 lines, SHA 799fe007, viewModel variable)
- res/layout/add_torrent_info.xml (313 lines, SHA 54283c9e, viewModel variable)
All SHAs match the prior wave-2 pass prefixes; the 1-line count differences on three fragments are trailing-newline counting only. Fresh-corpus grep over these 20 files: zero hits for setLifecycleOwner, getViewModel, hasPendingBindings, setVariable, onFieldChange, onChangeAppbar, executePendingBindings, and zero LiveData hits in the layouts.
Saved full-app-tree grep: ~/workspace/b656667-openclose-src/ruleF_grep_656667.txt — grep -rn -E over ~/workspace/ruleF-src (252 app Java files, file list verified identical to the branch directory walk). Results: setLifecycleOwner exactly one hit (CreateTorrentDialog.java:186, a different binding); getViewModel, hasPendingBindings, setVariable, onFieldChange, onChangeAppbar, executePendingBindings zero hits; every Impl class name zero hits; every base binding class name only its import plus its private field in its single host fragment. This grep proves absence of app-code callers only; generated source is not in the tree, so generated and framework dispatch is NOT ruled out by it, and no row in this revision rests on such a claim except where the row citation explicitly flags the premise for the merger.

## Judging convention used in these files (recorded, NOT decided — merger must pick one rule
project-wide and apply it to every databinding batch)
Generated *Binding/*BindingImpl source and DataBinderMapperImpl are NOT in final_java_only
and were NOT printed, so NO row in these files is SOURCE: every REACHABLE row is INFERRED,
even where the app-side inflate/setViewModel call site itself is printed, because the step
from DataBindingUtil.inflate to the Impl is generated-mapper dispatch and the step from a
base-class call to the Impl override is generated virtual dispatch. This follows batch 67's
convention (and batches 62-64/68-70 on the same points) and is applied uniformly to 65-67:
- Impl <clinit> / both <init> overloads / base <init> / executeBindings / invalidateAll:
  REACHABLE INFERRED on a printed inflate of the exact layout (mapper instantiation and
  generated-constructor rebind are the standard generated pattern, body not printed).
- hasPendingBindings: OPEN everywhere — no printed app or framework caller in the printed
  corpus; claiming a framework call without a printed generated/framework body would be
  invention.
- onFieldChange / setVariable: REACHABLE INFERRED ONLY where a variable is actually set in
  printed app code (a setViewModel call for a layout declaring that variable) and the layout
  binds observables of it; where no variable is set (layouts with NO <data> block), both stay
  OPEN. This is the batch 67 rule.
- onChangeX (nested binding): REACHABLE INFERRED ONLY where the parent layout includes child
  X AND the child layout binds observables that change in use; where the child layout has no
  <data>/observables, onChangeX stays OPEN (batch 66 row 7, appbar).
- Base getViewModel: OPEN everywhere in these files (see convention (v) below) — the
  executeBindings read path reads the mViewModel field, not the getter, as far as can be
  told without the generated body.
- setLifecycleOwner: OPEN everywhere — zero hits in all 26 freshly fetched files.
- Impl$1/$2 callback numbering (batch 66 rows 36-39): by generated-source order, NOT
  bytecode-confirmed.
- OPEN rows carry confirmed_by INFERRED in the table only as the ceiling of what can be said
  without generated source / a saved full-repo grep; it is NOT a label claim and NOT evidence
  of absence. No row is UNREACHABLE in these files, because no saved full-repo grep was run.

## Caveats the merger must resolve (these do not change the proposed labels above)
1. Strict-entry: routes are anchored at fragment onCreateView / onViewCreated (standard
   lifecycle callbacks) and, for the detail pages, at DetailPagerAdapter.createFragment.
   The launcher -> AddTorrentActivity / DetailTorrentActivity step was NOT printed in this
   pass, so under a strict printed-launcher-entry rule ALL REACHABLE rows in all three
   batches revert to OPEN.
2. confirmed_by per-row vs whole-route: these files use per-row INFERRED for generated
   dispatch (above). No SOURCE row exists to flip here, so a whole-route convention changes
   nothing in these files; labels are unaffected either way.
3. Binding-variant config gate (batch 65 rows 18-39, convention (iv)): the LargeLandNotouch
   and Sw600dpLand Impls are instantiated only under matching device configurations. Both
   variant layouts were freshly fetched and DO exist in the tree (see source list), and the
   same fragment inflates R.layout.fragment_add_torrent_info, so a route exists under a
   matching configuration. Under a single fixed portrait-phone standard config these 22 rows
   (18-39 minus the 4 OPEN hasPendingBindings/setLifecycleOwner rows among them: REACHABLE
   variant rows are 18-21, 23-25, 27-32, 34-36, 38-39) revert to OPEN (or
   closed_by_configuration) — merger must decide the standard-config rule. Batch 60's
   equivalent variant rows must be judged under the same rule.
4. Binding getViewModel convention (v): rows 65/6, 66/12, 66/24, 67/10, 67/22 are OPEN here.
   Prior batches 65-66 proposals marked them REACHABLE INFERRED via the executeBindings read
   path, while batches 58/63-64/67 left them OPEN. Merger must pick ONE rule for all binding
   getters (including batch 80 row 23 getDirName and batch 84 row 40 getBuildProgress, same
   family): adopting the executeBindings-read-path rule flips exactly these five rows in
   65-67 to REACHABLE INFERRED, nothing else.
5. hasPendingBindings / onFieldChange / setVariable for no-variable layouts: batch 66 rows
   5/7/8/10 (DetailTorrent Impl) are OPEN here under the batch-67 rule, whereas the prior
   batch-66 proposal marked them REACHABLE as generic framework callbacks. If the merger
   adopts the generic-framework-callback rule, rows 66/5, 66/8, 66/10 flip to REACHABLE
   INFERRED (row 66/7 onChangeAppbar stays OPEN on either rule unless the merger also
   accepts a no-observable child callback, since the appbar layout binds nothing).
6. Room finalize, TorrentDao_Impl $N mapping, and migration gates do NOT arise in batches
   65-67; no decision is needed for those here.
7. Batch 67 row 40 (TrackerList onFieldChange) and batch 68 row 1 (TrackerList Impl
   setVariable) are companion rows for the same no-variable binding and must be judged
   together at merge (both OPEN here / in batch 68).


## OPEN-close round 2 (G11) — conditional tables (NOT decided, merger must pick ONE rule each)

No row in batches 65-67 flips on any table below in this pass. A table entry is a
conditional statement only: "under option X, row Y flips to Z". The merger must apply
each chosen rule project-wide, not per batch.

### Table A — getViewModel, convention (v) (5 rows in this group)

| Row | If merger ADOPTS the executeBindings-read-path rule | If merger REJECTS the read-path rule and accepts the saved 252-file zero-hit grep as trigger-absence | Otherwise |
|-----|------------------------------------------------------|------------------------------------------------------------------------------------------------------|-----------|
| 65/6 FragmentAddTorrentInfoBinding.getViewModel | REACHABLE INFERRED | UNREACHABLE no_trigger_in_app INFERRED | stays OPEN |
| 66/12 FragmentDetailTorrentFilesBinding.getViewModel | REACHABLE INFERRED | UNREACHABLE no_trigger_in_app INFERRED | stays OPEN |
| 66/24 FragmentDetailTorrentInfoBinding.getViewModel | REACHABLE INFERRED | UNREACHABLE no_trigger_in_app INFERRED | stays OPEN |
| 67/10 FragmentDetailTorrentPiecesBinding.getViewModel | REACHABLE INFERRED | UNREACHABLE no_trigger_in_app INFERRED | stays OPEN |
| 67/22 FragmentDetailTorrentStateBinding.getViewModel | REACHABLE INFERRED | UNREACHABLE no_trigger_in_app INFERRED | stays OPEN |

Evidence for both branches is the same and is already saved: zero getViewModel hits in
252 app Java files (round-1 ruleF_grep_656667.txt, round-2 re-run
ruleF_grep_656667_rerun.txt) and no printed caller in any host fragment. The choice is
whether generated executeBindings reading the mViewModel field counts as calling the
getter. This pass does not decide it, and does not extend the round-1 setLifecycleOwner
UNREACHABLE reasoning to these getter rows.

### Table B — hasPendingBindings (10 rows in this group; named resolver is a printed body)

| Row | Resolver that would flip it | This pass |
|-----|------------------------------|-----------|
| 65/11 FragmentAddTorrentInfoBindingImpl.hasPendingBindings | Printed generated Impl body or printed library rebind body showing whether the rebind path calls this override (REACHABLE if it calls it; UNREACHABLE framework_never_calls / no_trigger_in_app if the body shows it never does — kind set by the merger from the body) | stays OPEN |
| 65/22 FragmentAddTorrentInfoBindingLargeLandNotouchImpl.hasPendingBindings | Same printed body; variant-config gate (iv) also applies if flipped | stays OPEN |
| 65/33 FragmentAddTorrentInfoBindingSw600dpLandImpl.hasPendingBindings | Same printed body; variant-config gate (iv) also applies if flipped | stays OPEN |
| 66/5 FragmentDetailTorrentBindingImpl.hasPendingBindings | Same printed body | stays OPEN |
| 66/17 FragmentDetailTorrentFilesBindingImpl.hasPendingBindings | Same printed body | stays OPEN |
| 66/29 FragmentDetailTorrentInfoBindingImpl.hasPendingBindings | Same printed body | stays OPEN |
| 67/5 FragmentDetailTorrentPeerListBindingImpl.hasPendingBindings | Same printed body | stays OPEN |
| 67/15 FragmentDetailTorrentPiecesBindingImpl.hasPendingBindings | Same printed body | stays OPEN |
| 67/27 FragmentDetailTorrentStateBindingImpl.hasPendingBindings | Same printed body | stays OPEN |
| 67/38 FragmentDetailTorrentTrackerListBindingImpl.hasPendingBindings | Same printed body | stays OPEN |

No such body was printed in round 1 or round 2. The zero-hit greps (round-1, round-2
re-run, and the binding-callbacks family scan: 122 rows in batches 58-70, zero hits for
all five family methods) do NOT flip any of these rows either way, because generated /
library dispatch is unprinted in the app-Java-only corpus. No convention decision alone
flips them in this pass.

### Table C — no-variable layouts, convention (xv), plus onChangeAppbar (companion rows)

Layouts with NO <data> variable in this group: fragment_detail_torrent,
fragment_detail_torrent_peer_list, fragment_detail_torrent_tracker_list,
detail_torrent_appbar (each 0 <data> / <variable> lines on local re-check).

| Row | Under (xv) as stated (REACHABLE only where a variable is actually set) | Under a generic-framework-callback rule (rejects (xv)) | Under a grep-as-trigger-absence rule (rejects the generic rule, accepts the 252-file zero-hit grep) |
|-----|------------------------------------------------------------------------|--------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| 66/8 FragmentDetailTorrentBindingImpl.onFieldChange | stays OPEN (no variable set, no observable registered) | REACHABLE INFERRED | UNREACHABLE no_trigger_in_app INFERRED |
| 66/10 FragmentDetailTorrentBindingImpl.setVariable | stays OPEN (no variable set) | REACHABLE INFERRED | UNREACHABLE no_trigger_in_app INFERRED |
| 67/7 FragmentDetailTorrentPeerListBindingImpl.onFieldChange | stays OPEN (no variable set) | REACHABLE INFERRED | UNREACHABLE no_trigger_in_app INFERRED |
| 67/8 FragmentDetailTorrentPeerListBindingImpl.setVariable | stays OPEN (no variable set) | REACHABLE INFERRED | UNREACHABLE no_trigger_in_app INFERRED |
| 67/40 FragmentDetailTorrentTrackerListBindingImpl.onFieldChange | stays OPEN (no variable set) | REACHABLE INFERRED | UNREACHABLE no_trigger_in_app INFERRED |
| 66/7 FragmentDetailTorrentBindingImpl.onChangeAppbar | stays OPEN (child appbar layout binds no observable; no observable change can trigger it) | stays OPEN unless the merger also accepts a no-observable child callback, then REACHABLE INFERRED | UNREACHABLE no_trigger_in_app INFERRED |

Companion linkage (judge together, never separately): 67/40 (TrackerList onFieldChange)
with 68/1 (TrackerList Impl setVariable, batch 68, currently OPEN, same no-variable
binding, TrackersFragment uses fields only, no setter call); 66/7 (onChangeAppbar) with
60/11 (DetailTorrentAppbarBindingImpl.onFieldChange, OPEN) and 60/12
(DetailTorrentAppbarBindingImpl.setVariable, OPEN) — the same no-data appbar binding
family. This pass flips none of them and does not decide (xv).

### Table D — setVariable direction contradiction, batches 63 / 64 / 65 (NOT decided)

Contradiction, flagged never decided: batch 65 treats Impl setVariable as REACHABLE via
"generated dispatch point behind binding.setViewModel", which is mechanically backwards
— in generated code setVariable CALLS the typed setter (setViewModel), not vice versa,
so a printed binding.setViewModel() call does not by itself trigger Impl setVariable.
Batches 63-64 keep setVariable OPEN on zero printed setVariable hits. Batches 63, 64
and 65 (and, for consistency, 66-68) must use ONE rule:

| Option | 65/3, 65/16, 65/27, 65/38 (currently REACHABLE, variable-set layouts, printed setViewModel only, zero printed setVariable hits) | 63/10, 63/24, 64/4, 64/13, 64/22, 64/31 (currently OPEN, variable-set layouts, printed setViewModel only, zero printed setVariable hits) | 66/10, 67/8, 68/1 and other no-variable setVariable rows (currently OPEN) |
|--------|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| D1 — batch-65 current rule (setViewModel implies setVariable dispatch) | stay REACHABLE INFERRED | flip to REACHABLE INFERRED | stay OPEN under (xv) |
| D2 — strict mechanical rule (only a printed setVariable call, or a printed generated body, triggers Impl setVariable) | revert to OPEN | stay OPEN | stay OPEN |
| D3 — generic-framework-callback rule (framework/generated dispatch always runs setVariable) | stay REACHABLE INFERRED | flip to REACHABLE INFERRED | flip to REACHABLE INFERRED — but this conflicts with (xv) and the merger must reconcile D3 with (xv) explicitly |

This pass applies none of D1/D2/D3 to change a label: the four batch-65 REACHABLE
setVariable rows are left exactly as written and flagged here, and the 63/64 rows are
not edited (outside this group). A printed generated Impl setVariable/setViewModel
body would settle the direction mechanically and supersede this table.

### Table E — setLifecycleOwner rows already closed in round 1 (NOT OPEN; revert condition)

65/15, 65/26, 65/37 and 66/9 are UNREACHABLE no_trigger_in_app INFERRED from round 1.
Round-2 re-run confirms the grep still holds exactly (252 files, sole hit
CreateTorrentDialog.java:186, DialogCreateTorrentBinding — a different binding; zero
hits for every 65-67 binding name and Impl name). REVERT CONDITION (recorded on each
of the four rows): if the merger rejects the premise that setLifecycleOwner is an
app-side setter with no framework trigger — a premise for which no framework/library
body is printed — all four rows revert to OPEN. No new setLifecycleOwner row arises
in this group (batch 67 has none; no other 65/66 setLifecycleOwner row is OPEN), so
this reasoning was NOT extended to any new row in round 2.
## Per-row table

| # | Method | Descriptor | Label | confirmed_by | Printed route / citation |
|---|--------|------------|-------|--------------|--------------------------|

| 1 | FragmentDetailTorrentPeerListBindingImpl.<clinit> | `()V` | REACHABLE | INFERRED | DetailTorrentPeersFragment.java:84 DataBindingUtil.inflate(fragment_detail_torrent_peer_list), field use only at :124-125/:138/:140-142, NO setViewModel/setVariable call [fresh, 202 lines, SHA d164a15e…]; layout fragment_detail_torrent_peer_list.xml declares NO <data>, NO variable, and NO @{...} data binding except a padding dimen [fresh, 27 lines]. First reference via PeersFragment:84 inflate; JVM init, generated dispatch. |
| 2 | FragmentDetailTorrentPeerListBindingImpl.<init>(DataBindingComponent,View) | `(Landroidx/databinding/DataBindingComponent;Landroid/view/View;)V` | REACHABLE | INFERRED | DetailTorrentPeersFragment.java:84 DataBindingUtil.inflate(fragment_detail_torrent_peer_list), field use only at :124-125/:138/:140-142, NO setViewModel/setVariable call [fresh, 202 lines, SHA d164a15e…]; layout fragment_detail_torrent_peer_list.xml declares NO <data>, NO variable, and NO @{...} data binding except a padding dimen [fresh, 27 lines]. Mapper result of PeersFragment:84 inflate (generated, not printed). |
| 3 | FragmentDetailTorrentPeerListBindingImpl.<init>(DataBindingComponent,View,Object[]) | `(Landroidx/databinding/DataBindingComponent;Landroid/view/View;[Ljava/lang/Object;)V` | REACHABLE | INFERRED | DetailTorrentPeersFragment.java:84 DataBindingUtil.inflate(fragment_detail_torrent_peer_list), field use only at :124-125/:138/:140-142, NO setViewModel/setVariable call [fresh, 202 lines, SHA d164a15e…]; layout fragment_detail_torrent_peer_list.xml declares NO <data>, NO variable, and NO @{...} data binding except a padding dimen [fresh, 27 lines]. Called by row 2 in generated code (pattern, body not printed). |
| 4 | FragmentDetailTorrentPeerListBindingImpl.executeBindings | `()V` | REACHABLE | INFERRED | DetailTorrentPeersFragment.java:84 DataBindingUtil.inflate(fragment_detail_torrent_peer_list), field use only at :124-125/:138/:140-142, NO setViewModel/setVariable call [fresh, 202 lines, SHA d164a15e…]; layout fragment_detail_torrent_peer_list.xml declares NO <data>, NO variable, and NO @{...} data binding except a padding dimen [fresh, 27 lines]. Framework rebind after generated invalidateAll on the row-2 construction. |
| 5 | FragmentDetailTorrentPeerListBindingImpl.hasPendingBindings | `()Z` | REACHABLE | INFERRED | No printed app or framework caller of hasPendingBindings appears in the freshly printed corpus; claiming a framework call without a printed generated/framework body would be invention (same convention as batches 67-69). OPEN, not UNREACHABLE: no saved full-repo grep was run in this pass, and no search_code 0-result was used as evidence of absence. A printed caller or a saved full-repo grep (rule F/C5) resolves it.  RE-VERIFIED 2026-11-01: saved full-app-tree grep ~/workspace/b656667-openclose-src/ruleF_grep_656667.txt (252 app Java files, branch work-2026-10-31, file list verified identical to the branch directory walk) finds zero hasPendingBindings and zero executePendingBindings hits in all 252 app Java files. Still OPEN because the databinding rebind dispatch is generated and library code and is not printed in this pass; a printed generated or library body showing whether the rebind path calls this override, or that it never does, is the named resolver. No convention is decided here. RE-VERIFIED 2026-11-01: saved full-app-tree grep ~/workspace/b656667-openclose-src/ruleF_grep_656667.txt (252 app Java files, branch work-2026-10-31, file list verified identical to the branch directory walk) finds zero hasPendingBindings and zero executePendingBindings hits in all 252 app Java files. Still OPEN because the databinding rebind dispatch is generated and library code and is not printed in this pass; a printed generated or library body showing whether the rebind path calls this override, or that it never does, is the named resolver. No convention is decided here. ROUND2 2026-11-01 (G11): re-run grep ~/workspace/b656667-openclose2-src/ruleF_grep_656667_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); no generated/library body was printed in round 2, so no flip in this pass — see the round-2 conditional tables before the per-row table. This pass decides no convention. [Phase 3 completion 2026-11-01: L3 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 6 | FragmentDetailTorrentPeerListBindingImpl.invalidateAll | `()V` | REACHABLE | INFERRED | DetailTorrentPeersFragment.java:84 DataBindingUtil.inflate(fragment_detail_torrent_peer_list), field use only at :124-125/:138/:140-142, NO setViewModel/setVariable call [fresh, 202 lines, SHA d164a15e…]; layout fragment_detail_torrent_peer_list.xml declares NO <data>, NO variable, and NO @{...} data binding except a padding dimen [fresh, 27 lines]. Called by the generated Impl constructor on the row-2 construction. |
| 7 | FragmentDetailTorrentPeerListBindingImpl.onFieldChange | `(ILjava/lang/Object;I)Z` | UNREACHABLE | INFERRED | No variable is set on this binding in printed code (PeersFragment uses only fields :124-125/:138/:140-142; layout declares no variable), so no observable registration is printed. OPEN, not UNREACHABLE: no saved full-repo grep was run in this pass, and no search_code 0-result was used as evidence of absence. A printed caller or a saved full-repo grep (rule F/C5) resolves it.  RE-VERIFIED 2026-11-01: saved full-app-tree grep ~/workspace/b656667-openclose-src/ruleF_grep_656667.txt (252 app Java files, branch work-2026-10-31, file list verified identical to the branch directory walk) finds zero onFieldChange hits in all 252 app Java files, and the freshly printed layout declares no variable. Still OPEN because the generic-framework-callback convention is undecided: under it this row flips to REACHABLE INFERRED; if the merger rejects that convention and accepts the grep as trigger-absence it flips to UNREACHABLE no_trigger_in_app. This pass does not decide. Companion rows noted in the original file still apply. RE-VERIFIED 2026-11-01: saved full-app-tree grep ~/workspace/b656667-openclose-src/ruleF_grep_656667.txt (252 app Java files, branch work-2026-10-31, file list verified identical to the branch directory walk) finds zero onFieldChange hits in all 252 app Java files, and the freshly printed layout declares no variable. Still OPEN because the generic-framework-callback convention is undecided: under it this row flips to REACHABLE INFERRED; if the merger rejects that convention and accepts the grep as trigger-absence it flips to UNREACHABLE no_trigger_in_app. This pass does not decide. Companion rows noted in the original file still apply. ROUND2 2026-11-01 (G11): re-run grep ~/workspace/b656667-openclose2-src/ruleF_grep_656667_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); no generated/library body was printed in round 2, so no flip in this pass — see the round-2 conditional tables before the per-row table. This pass decides no convention. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L3 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 8 | FragmentDetailTorrentPeerListBindingImpl.setVariable | `(ILjava/lang/Object;)Z` | UNREACHABLE | INFERRED | No printed setVariable (or setViewModel) call on this binding; layout declares no variable. OPEN, not UNREACHABLE: no saved full-repo grep was run in this pass, and no search_code 0-result was used as evidence of absence. A printed caller or a saved full-repo grep (rule F/C5) resolves it. NOT UNREACHABLE on this evidence.  RE-VERIFIED 2026-11-01: saved full-app-tree grep ~/workspace/b656667-openclose-src/ruleF_grep_656667.txt (252 app Java files, branch work-2026-10-31, file list verified identical to the branch directory walk) finds zero setVariable hits in all 252 app Java files, and the freshly printed layout declares no variable. Still OPEN because the generic-framework-callback convention is undecided: under it this row flips to REACHABLE INFERRED; if the merger rejects that convention and accepts the grep as trigger-absence it flips to UNREACHABLE no_trigger_in_app. This pass does not decide. Companion rows noted in the original file still apply. RE-VERIFIED 2026-11-01: saved full-app-tree grep ~/workspace/b656667-openclose-src/ruleF_grep_656667.txt (252 app Java files, branch work-2026-10-31, file list verified identical to the branch directory walk) finds zero setVariable hits in all 252 app Java files, and the freshly printed layout declares no variable. Still OPEN because the generic-framework-callback convention is undecided: under it this row flips to REACHABLE INFERRED; if the merger rejects that convention and accepts the grep as trigger-absence it flips to UNREACHABLE no_trigger_in_app. This pass does not decide. Companion rows noted in the original file still apply. ROUND2 2026-11-01 (G11): re-run grep ~/workspace/b656667-openclose2-src/ruleF_grep_656667_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); no generated/library body was printed in round 2, so no flip in this pass — see the round-2 conditional tables before the per-row table. This pass decides no convention. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L3 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 9 | FragmentDetailTorrentPiecesBinding.<init> | `(Ljava/lang/Object;Landroid/view/View;ILandroidx/core/widget/ContentLoadingProgressBar;Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/pieces/PiecesView;Landroidx/core/widget/NestedScrollView;Landroid/widget/TextView;)V` | REACHABLE | INFERRED | DetailTorrentPiecesFragment.java:71 DataBindingUtil.inflate(fragment_detail_torrent_pieces), :109 binding.setViewModel(viewModel) [fresh, 143 lines, SHA 7a57c7f1…]; layout fragment_detail_torrent_pieces.xml declares viewModel and binds viewModel.info.advancedInfo.downloadedPieces/metaInfo.numPieces/pieceLength (:47/:58/:65) [fresh]. Called by Pieces Impl <init> (rows 12-13) in generated code. |
| 10 | FragmentDetailTorrentPiecesBinding.getViewModel | `()Lorg/proninyaroslav/libretorrent/ui/detailtorrent/DetailTorrentViewModel;` | UNREACHABLE | INFERRED | No printed caller of this getter appears in the freshly printed corpus; generated executeBindings reads the mViewModel field, not the getter, as far as can be told without the generated body. OPEN, not UNREACHABLE: no saved full-repo grep was run in this pass, and no search_code 0-result was used as evidence of absence. A printed caller or a saved full-repo grep (rule F/C5) resolves it. CONVENTION (v), merger must pick one rule for all binding getters: prior batches 65-66 proposals marked these rows REACHABLE INFERRED via the executeBindings read path, while batches 58/63-64/67 left them OPEN; this file follows the OPEN side so 65-67 are consistent with batch 67. If the merger adopts the executeBindings-read-path rule, these rows flip en bloc to REACHABLE INFERRED.  RE-VERIFIED 2026-11-01: saved full-app-tree grep ~/workspace/b656667-openclose-src/ruleF_grep_656667.txt (252 app Java files, branch work-2026-10-31, file list verified identical to the branch directory walk) finds zero getViewModel hits in all 252 app Java files, and the freshly printed host file never calls the getter. Still OPEN because convention (v) is undecided: if the merger adopts the executeBindings-read-path rule this row flips to REACHABLE INFERRED; if the merger rejects that rule and accepts the grep as trigger-absence it flips to UNREACHABLE no_trigger_in_app. This pass does not decide. RE-VERIFIED 2026-11-01: saved full-app-tree grep ~/workspace/b656667-openclose-src/ruleF_grep_656667.txt (252 app Java files, branch work-2026-10-31, file list verified identical to the branch directory walk) finds zero getViewModel hits in all 252 app Java files, and the freshly printed host file never calls the getter. Still OPEN because convention (v) is undecided: if the merger adopts the executeBindings-read-path rule this row flips to REACHABLE INFERRED; if the merger rejects that rule and accepts the grep as trigger-absence it flips to UNREACHABLE no_trigger_in_app. This pass does not decide. ROUND2 2026-11-01 (G11): re-run grep ~/workspace/b656667-openclose2-src/ruleF_grep_656667_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); no generated/library body was printed in round 2, so no flip in this pass — see the round-2 conditional tables before the per-row table. This pass decides no convention. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L3 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 11 | FragmentDetailTorrentPiecesBindingImpl.<clinit> | `()V` | REACHABLE | INFERRED | DetailTorrentPiecesFragment.java:71 DataBindingUtil.inflate(fragment_detail_torrent_pieces), :109 binding.setViewModel(viewModel) [fresh, 143 lines, SHA 7a57c7f1…]; layout fragment_detail_torrent_pieces.xml declares viewModel and binds viewModel.info.advancedInfo.downloadedPieces/metaInfo.numPieces/pieceLength (:47/:58/:65) [fresh]. First reference via PiecesFragment:71 inflate. |
| 12 | FragmentDetailTorrentPiecesBindingImpl.<init>(DataBindingComponent,View) | `(Landroidx/databinding/DataBindingComponent;Landroid/view/View;)V` | REACHABLE | INFERRED | DetailTorrentPiecesFragment.java:71 DataBindingUtil.inflate(fragment_detail_torrent_pieces), :109 binding.setViewModel(viewModel) [fresh, 143 lines, SHA 7a57c7f1…]; layout fragment_detail_torrent_pieces.xml declares viewModel and binds viewModel.info.advancedInfo.downloadedPieces/metaInfo.numPieces/pieceLength (:47/:58/:65) [fresh]. Mapper result of PiecesFragment:71 inflate (generated, not printed). |
| 13 | FragmentDetailTorrentPiecesBindingImpl.<init>(DataBindingComponent,View,Object[]) | `(Landroidx/databinding/DataBindingComponent;Landroid/view/View;[Ljava/lang/Object;)V` | REACHABLE | INFERRED | DetailTorrentPiecesFragment.java:71 DataBindingUtil.inflate(fragment_detail_torrent_pieces), :109 binding.setViewModel(viewModel) [fresh, 143 lines, SHA 7a57c7f1…]; layout fragment_detail_torrent_pieces.xml declares viewModel and binds viewModel.info.advancedInfo.downloadedPieces/metaInfo.numPieces/pieceLength (:47/:58/:65) [fresh]. Called by row 12 in generated code (pattern, body not printed). |
| 14 | FragmentDetailTorrentPiecesBindingImpl.executeBindings | `()V` | REACHABLE | INFERRED | DetailTorrentPiecesFragment.java:71 DataBindingUtil.inflate(fragment_detail_torrent_pieces), :109 binding.setViewModel(viewModel) [fresh, 143 lines, SHA 7a57c7f1…]; layout fragment_detail_torrent_pieces.xml declares viewModel and binds viewModel.info.advancedInfo.downloadedPieces/metaInfo.numPieces/pieceLength (:47/:58/:65) [fresh]. Framework rebind after generated invalidateAll / after :109 setViewModel. |
| 15 | FragmentDetailTorrentPiecesBindingImpl.hasPendingBindings | `()Z` | REACHABLE | INFERRED | No printed app or framework caller of hasPendingBindings appears in the freshly printed corpus; claiming a framework call without a printed generated/framework body would be invention (same convention as batches 67-69). OPEN, not UNREACHABLE: no saved full-repo grep was run in this pass, and no search_code 0-result was used as evidence of absence. A printed caller or a saved full-repo grep (rule F/C5) resolves it.  RE-VERIFIED 2026-11-01: saved full-app-tree grep ~/workspace/b656667-openclose-src/ruleF_grep_656667.txt (252 app Java files, branch work-2026-10-31, file list verified identical to the branch directory walk) finds zero hasPendingBindings and zero executePendingBindings hits in all 252 app Java files. Still OPEN because the databinding rebind dispatch is generated and library code and is not printed in this pass; a printed generated or library body showing whether the rebind path calls this override, or that it never does, is the named resolver. No convention is decided here. RE-VERIFIED 2026-11-01: saved full-app-tree grep ~/workspace/b656667-openclose-src/ruleF_grep_656667.txt (252 app Java files, branch work-2026-10-31, file list verified identical to the branch directory walk) finds zero hasPendingBindings and zero executePendingBindings hits in all 252 app Java files. Still OPEN because the databinding rebind dispatch is generated and library code and is not printed in this pass; a printed generated or library body showing whether the rebind path calls this override, or that it never does, is the named resolver. No convention is decided here. ROUND2 2026-11-01 (G11): re-run grep ~/workspace/b656667-openclose2-src/ruleF_grep_656667_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); no generated/library body was printed in round 2, so no flip in this pass — see the round-2 conditional tables before the per-row table. This pass decides no convention. [Phase 3 completion 2026-11-01: L3 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 16 | FragmentDetailTorrentPiecesBindingImpl.invalidateAll | `()V` | REACHABLE | INFERRED | DetailTorrentPiecesFragment.java:71 DataBindingUtil.inflate(fragment_detail_torrent_pieces), :109 binding.setViewModel(viewModel) [fresh, 143 lines, SHA 7a57c7f1…]; layout fragment_detail_torrent_pieces.xml declares viewModel and binds viewModel.info.advancedInfo.downloadedPieces/metaInfo.numPieces/pieceLength (:47/:58/:65) [fresh]. Called by the generated Impl constructor and by setViewModel. |
| 17 | FragmentDetailTorrentPiecesBindingImpl.onChangeViewModelInfo | `(Lorg/proninyaroslav/libretorrent/ui/detailtorrent/TorrentDetailsInfo;I)Z` | REACHABLE | INFERRED | DetailTorrentPiecesFragment.java:71 DataBindingUtil.inflate(fragment_detail_torrent_pieces), :109 binding.setViewModel(viewModel) [fresh, 143 lines, SHA 7a57c7f1…]; layout fragment_detail_torrent_pieces.xml declares viewModel and binds viewModel.info.advancedInfo.downloadedPieces/metaInfo.numPieces/pieceLength (:47/:58/:65) [fresh]. Generated observable-change callback for the viewModel set at PiecesFragment:109; fires when the viewModel's TorrentDetailsInfo observable changes (generated dispatch). |
| 18 | FragmentDetailTorrentPiecesBindingImpl.onFieldChange | `(ILjava/lang/Object;I)Z` | REACHABLE | INFERRED | DetailTorrentPiecesFragment.java:71 DataBindingUtil.inflate(fragment_detail_torrent_pieces), :109 binding.setViewModel(viewModel) [fresh, 143 lines, SHA 7a57c7f1…]; layout fragment_detail_torrent_pieces.xml declares viewModel and binds viewModel.info.advancedInfo.downloadedPieces/metaInfo.numPieces/pieceLength (:47/:58/:65) [fresh]. Framework dispatch when an observable registered by :109 setViewModel changes (generated dispatch). |
| 19 | FragmentDetailTorrentPiecesBindingImpl.setVariable | `(ILjava/lang/Object;)Z` | UNREACHABLE | INFERRED | DetailTorrentPiecesFragment.java:71 DataBindingUtil.inflate(fragment_detail_torrent_pieces), :109 binding.setViewModel(viewModel) [fresh, 143 lines, SHA 7a57c7f1…]; layout fragment_detail_torrent_pieces.xml declares viewModel and binds viewModel.info.advancedInfo.downloadedPieces/metaInfo.numPieces/pieceLength (:47/:58/:65) [fresh]. Per D4d, setVariable CALLS the typed setter, so a printed setViewModel call is zero evidence for setVariable (the prior direction is backwards) [Phase 2 fix 2026-11-01]. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L3 verdict applied.] |
| 20 | FragmentDetailTorrentPiecesBindingImpl.setViewModel | `(Lorg/proninyaroslav/libretorrent/ui/detailtorrent/DetailTorrentViewModel;)V` | REACHABLE | INFERRED | DetailTorrentPiecesFragment.java:71 DataBindingUtil.inflate(fragment_detail_torrent_pieces), :109 binding.setViewModel(viewModel) [fresh, 143 lines, SHA 7a57c7f1…]; layout fragment_detail_torrent_pieces.xml declares viewModel and binds viewModel.info.advancedInfo.downloadedPieces/metaInfo.numPieces/pieceLength (:47/:58/:65) [fresh]. App call site printed: PiecesFragment:109 binding.setViewModel(viewModel); dispatch from the base type to this Impl override is generated, hence INFERRED not SOURCE. |
| 21 | FragmentDetailTorrentStateBinding.<init> | `(Ljava/lang/Object;Landroid/view/View;ILandroid/widget/TextView;Landroid/widget/TextView;Landroid/widget/TextView;Landroid/widget/TextView;Landroid/widget/TextView;Landroid/widget/TextView;Landroid/widget/TextView;Landroid/widget/TextView;Landroid/widget/TextView;Landroid/widget/TextView;Landroid/widget/TextView;)V` | REACHABLE | INFERRED | DetailTorrentStateFragment.java:73 DataBindingUtil.inflate(fragment_detail_torrent_state), :86 binding.setViewModel(viewModel) [fresh, 87 lines, SHA b01a6a20…]; layout fragment_detail_torrent_state.xml declares viewModel and binds viewModel.info.torrentInfo/advancedInfo/metaInfo.* (:45/:74/:95/:125/:146/:176/:197/:227/:248/:278/:299) [fresh]. Called by State Impl <init> (rows 24-25) in generated code. |
| 22 | FragmentDetailTorrentStateBinding.getViewModel | `()Lorg/proninyaroslav/libretorrent/ui/detailtorrent/DetailTorrentViewModel;` | UNREACHABLE | INFERRED | No printed caller of this getter appears in the freshly printed corpus; generated executeBindings reads the mViewModel field, not the getter, as far as can be told without the generated body. OPEN, not UNREACHABLE: no saved full-repo grep was run in this pass, and no search_code 0-result was used as evidence of absence. A printed caller or a saved full-repo grep (rule F/C5) resolves it. CONVENTION (v), merger must pick one rule for all binding getters: prior batches 65-66 proposals marked these rows REACHABLE INFERRED via the executeBindings read path, while batches 58/63-64/67 left them OPEN; this file follows the OPEN side so 65-67 are consistent with batch 67. If the merger adopts the executeBindings-read-path rule, these rows flip en bloc to REACHABLE INFERRED.  RE-VERIFIED 2026-11-01: saved full-app-tree grep ~/workspace/b656667-openclose-src/ruleF_grep_656667.txt (252 app Java files, branch work-2026-10-31, file list verified identical to the branch directory walk) finds zero getViewModel hits in all 252 app Java files, and the freshly printed host file never calls the getter. Still OPEN because convention (v) is undecided: if the merger adopts the executeBindings-read-path rule this row flips to REACHABLE INFERRED; if the merger rejects that rule and accepts the grep as trigger-absence it flips to UNREACHABLE no_trigger_in_app. This pass does not decide. RE-VERIFIED 2026-11-01: saved full-app-tree grep ~/workspace/b656667-openclose-src/ruleF_grep_656667.txt (252 app Java files, branch work-2026-10-31, file list verified identical to the branch directory walk) finds zero getViewModel hits in all 252 app Java files, and the freshly printed host file never calls the getter. Still OPEN because convention (v) is undecided: if the merger adopts the executeBindings-read-path rule this row flips to REACHABLE INFERRED; if the merger rejects that rule and accepts the grep as trigger-absence it flips to UNREACHABLE no_trigger_in_app. This pass does not decide. ROUND2 2026-11-01 (G11): re-run grep ~/workspace/b656667-openclose2-src/ruleF_grep_656667_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); no generated/library body was printed in round 2, so no flip in this pass — see the round-2 conditional tables before the per-row table. This pass decides no convention. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L3 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 23 | FragmentDetailTorrentStateBindingImpl.<clinit> | `()V` | REACHABLE | INFERRED | DetailTorrentStateFragment.java:73 DataBindingUtil.inflate(fragment_detail_torrent_state), :86 binding.setViewModel(viewModel) [fresh, 87 lines, SHA b01a6a20…]; layout fragment_detail_torrent_state.xml declares viewModel and binds viewModel.info.torrentInfo/advancedInfo/metaInfo.* (:45/:74/:95/:125/:146/:176/:197/:227/:248/:278/:299) [fresh]. First reference via StateFragment:73 inflate. |
| 24 | FragmentDetailTorrentStateBindingImpl.<init>(DataBindingComponent,View) | `(Landroidx/databinding/DataBindingComponent;Landroid/view/View;)V` | REACHABLE | INFERRED | DetailTorrentStateFragment.java:73 DataBindingUtil.inflate(fragment_detail_torrent_state), :86 binding.setViewModel(viewModel) [fresh, 87 lines, SHA b01a6a20…]; layout fragment_detail_torrent_state.xml declares viewModel and binds viewModel.info.torrentInfo/advancedInfo/metaInfo.* (:45/:74/:95/:125/:146/:176/:197/:227/:248/:278/:299) [fresh]. Mapper result of StateFragment:73 inflate (generated, not printed). |
| 25 | FragmentDetailTorrentStateBindingImpl.<init>(DataBindingComponent,View,Object[]) | `(Landroidx/databinding/DataBindingComponent;Landroid/view/View;[Ljava/lang/Object;)V` | REACHABLE | INFERRED | DetailTorrentStateFragment.java:73 DataBindingUtil.inflate(fragment_detail_torrent_state), :86 binding.setViewModel(viewModel) [fresh, 87 lines, SHA b01a6a20…]; layout fragment_detail_torrent_state.xml declares viewModel and binds viewModel.info.torrentInfo/advancedInfo/metaInfo.* (:45/:74/:95/:125/:146/:176/:197/:227/:248/:278/:299) [fresh]. Called by row 24 in generated code (pattern, body not printed). |
| 26 | FragmentDetailTorrentStateBindingImpl.executeBindings | `()V` | REACHABLE | INFERRED | DetailTorrentStateFragment.java:73 DataBindingUtil.inflate(fragment_detail_torrent_state), :86 binding.setViewModel(viewModel) [fresh, 87 lines, SHA b01a6a20…]; layout fragment_detail_torrent_state.xml declares viewModel and binds viewModel.info.torrentInfo/advancedInfo/metaInfo.* (:45/:74/:95/:125/:146/:176/:197/:227/:248/:278/:299) [fresh]. Framework rebind after generated invalidateAll / after :86 setViewModel. |
| 27 | FragmentDetailTorrentStateBindingImpl.hasPendingBindings | `()Z` | REACHABLE | INFERRED | No printed app or framework caller of hasPendingBindings appears in the freshly printed corpus; claiming a framework call without a printed generated/framework body would be invention (same convention as batches 67-69). OPEN, not UNREACHABLE: no saved full-repo grep was run in this pass, and no search_code 0-result was used as evidence of absence. A printed caller or a saved full-repo grep (rule F/C5) resolves it.  RE-VERIFIED 2026-11-01: saved full-app-tree grep ~/workspace/b656667-openclose-src/ruleF_grep_656667.txt (252 app Java files, branch work-2026-10-31, file list verified identical to the branch directory walk) finds zero hasPendingBindings and zero executePendingBindings hits in all 252 app Java files. Still OPEN because the databinding rebind dispatch is generated and library code and is not printed in this pass; a printed generated or library body showing whether the rebind path calls this override, or that it never does, is the named resolver. No convention is decided here. RE-VERIFIED 2026-11-01: saved full-app-tree grep ~/workspace/b656667-openclose-src/ruleF_grep_656667.txt (252 app Java files, branch work-2026-10-31, file list verified identical to the branch directory walk) finds zero hasPendingBindings and zero executePendingBindings hits in all 252 app Java files. Still OPEN because the databinding rebind dispatch is generated and library code and is not printed in this pass; a printed generated or library body showing whether the rebind path calls this override, or that it never does, is the named resolver. No convention is decided here. ROUND2 2026-11-01 (G11): re-run grep ~/workspace/b656667-openclose2-src/ruleF_grep_656667_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); no generated/library body was printed in round 2, so no flip in this pass — see the round-2 conditional tables before the per-row table. This pass decides no convention. [Phase 3 completion 2026-11-01: L3 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 28 | FragmentDetailTorrentStateBindingImpl.invalidateAll | `()V` | REACHABLE | INFERRED | DetailTorrentStateFragment.java:73 DataBindingUtil.inflate(fragment_detail_torrent_state), :86 binding.setViewModel(viewModel) [fresh, 87 lines, SHA b01a6a20…]; layout fragment_detail_torrent_state.xml declares viewModel and binds viewModel.info.torrentInfo/advancedInfo/metaInfo.* (:45/:74/:95/:125/:146/:176/:197/:227/:248/:278/:299) [fresh]. Called by the generated Impl constructor and by setViewModel. |
| 29 | FragmentDetailTorrentStateBindingImpl.onChangeViewModelInfo | `(Lorg/proninyaroslav/libretorrent/ui/detailtorrent/TorrentDetailsInfo;I)Z` | REACHABLE | INFERRED | DetailTorrentStateFragment.java:73 DataBindingUtil.inflate(fragment_detail_torrent_state), :86 binding.setViewModel(viewModel) [fresh, 87 lines, SHA b01a6a20…]; layout fragment_detail_torrent_state.xml declares viewModel and binds viewModel.info.torrentInfo/advancedInfo/metaInfo.* (:45/:74/:95/:125/:146/:176/:197/:227/:248/:278/:299) [fresh]. As row 17, for the viewModel set at StateFragment:86. |
| 30 | FragmentDetailTorrentStateBindingImpl.onFieldChange | `(ILjava/lang/Object;I)Z` | REACHABLE | INFERRED | DetailTorrentStateFragment.java:73 DataBindingUtil.inflate(fragment_detail_torrent_state), :86 binding.setViewModel(viewModel) [fresh, 87 lines, SHA b01a6a20…]; layout fragment_detail_torrent_state.xml declares viewModel and binds viewModel.info.torrentInfo/advancedInfo/metaInfo.* (:45/:74/:95/:125/:146/:176/:197/:227/:248/:278/:299) [fresh]. As row 18, for the observable registered by StateFragment:86. |
| 31 | FragmentDetailTorrentStateBindingImpl.setVariable | `(ILjava/lang/Object;)Z` | UNREACHABLE | INFERRED | DetailTorrentStateFragment.java:73 DataBindingUtil.inflate(fragment_detail_torrent_state), :86 binding.setViewModel(viewModel) [fresh, 87 lines, SHA b01a6a20…]; layout fragment_detail_torrent_state.xml declares viewModel and binds viewModel.info.torrentInfo/advancedInfo/metaInfo.* (:45/:74/:95/:125/:146/:176/:197/:227/:248/:278/:299) [fresh]. Per D4d, setVariable CALLS the typed setter, so a printed setViewModel call is zero evidence for setVariable (the prior direction is backwards) [Phase 2 fix 2026-11-01]. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L3 verdict applied.] |
| 32 | FragmentDetailTorrentStateBindingImpl.setViewModel | `(Lorg/proninyaroslav/libretorrent/ui/detailtorrent/DetailTorrentViewModel;)V` | REACHABLE | INFERRED | DetailTorrentStateFragment.java:73 DataBindingUtil.inflate(fragment_detail_torrent_state), :86 binding.setViewModel(viewModel) [fresh, 87 lines, SHA b01a6a20…]; layout fragment_detail_torrent_state.xml declares viewModel and binds viewModel.info.torrentInfo/advancedInfo/metaInfo.* (:45/:74/:95/:125/:146/:176/:197/:227/:248/:278/:299) [fresh]. App call site printed: StateFragment:86 binding.setViewModel(viewModel); Impl dispatch generated, hence INFERRED. |
| 33 | FragmentDetailTorrentTrackerListBinding.<init> | `(Ljava/lang/Object;Landroid/view/View;ILandroid/widget/TextView;Lorg/proninyaroslav/libretorrent/ui/customviews/EmptyRecyclerView;)V` | REACHABLE | INFERRED | DetailTorrentTrackersFragment.java:105 DataBindingUtil.inflate(fragment_detail_torrent_tracker_list), field use only at :158-159/:172/:174/:176/:180-182, NO setViewModel/setVariable call [fresh, 406 lines, SHA 48d5a536…]; layout fragment_detail_torrent_tracker_list.xml declares NO <data>, NO variable, and NO @{...} data binding except a padding dimen [fresh, 27 lines]. Called by TrackerList Impl <init> (rows 35-36) in generated code. |
| 34 | FragmentDetailTorrentTrackerListBindingImpl.<clinit> | `()V` | REACHABLE | INFERRED | DetailTorrentTrackersFragment.java:105 DataBindingUtil.inflate(fragment_detail_torrent_tracker_list), field use only at :158-159/:172/:174/:176/:180-182, NO setViewModel/setVariable call [fresh, 406 lines, SHA 48d5a536…]; layout fragment_detail_torrent_tracker_list.xml declares NO <data>, NO variable, and NO @{...} data binding except a padding dimen [fresh, 27 lines]. First reference via TrackersFragment:105 inflate. |
| 35 | FragmentDetailTorrentTrackerListBindingImpl.<init>(DataBindingComponent,View) | `(Landroidx/databinding/DataBindingComponent;Landroid/view/View;)V` | REACHABLE | INFERRED | DetailTorrentTrackersFragment.java:105 DataBindingUtil.inflate(fragment_detail_torrent_tracker_list), field use only at :158-159/:172/:174/:176/:180-182, NO setViewModel/setVariable call [fresh, 406 lines, SHA 48d5a536…]; layout fragment_detail_torrent_tracker_list.xml declares NO <data>, NO variable, and NO @{...} data binding except a padding dimen [fresh, 27 lines]. Mapper result of TrackersFragment:105 inflate (generated, not printed). |
| 36 | FragmentDetailTorrentTrackerListBindingImpl.<init>(DataBindingComponent,View,Object[]) | `(Landroidx/databinding/DataBindingComponent;Landroid/view/View;[Ljava/lang/Object;)V` | REACHABLE | INFERRED | DetailTorrentTrackersFragment.java:105 DataBindingUtil.inflate(fragment_detail_torrent_tracker_list), field use only at :158-159/:172/:174/:176/:180-182, NO setViewModel/setVariable call [fresh, 406 lines, SHA 48d5a536…]; layout fragment_detail_torrent_tracker_list.xml declares NO <data>, NO variable, and NO @{...} data binding except a padding dimen [fresh, 27 lines]. Called by row 35 in generated code (pattern, body not printed). |
| 37 | FragmentDetailTorrentTrackerListBindingImpl.executeBindings | `()V` | REACHABLE | INFERRED | DetailTorrentTrackersFragment.java:105 DataBindingUtil.inflate(fragment_detail_torrent_tracker_list), field use only at :158-159/:172/:174/:176/:180-182, NO setViewModel/setVariable call [fresh, 406 lines, SHA 48d5a536…]; layout fragment_detail_torrent_tracker_list.xml declares NO <data>, NO variable, and NO @{...} data binding except a padding dimen [fresh, 27 lines]. Framework rebind after generated invalidateAll on the row-35 construction. |
| 38 | FragmentDetailTorrentTrackerListBindingImpl.hasPendingBindings | `()Z` | REACHABLE | INFERRED | No printed app or framework caller of hasPendingBindings appears in the freshly printed corpus; claiming a framework call without a printed generated/framework body would be invention (same convention as batches 67-69). OPEN, not UNREACHABLE: no saved full-repo grep was run in this pass, and no search_code 0-result was used as evidence of absence. A printed caller or a saved full-repo grep (rule F/C5) resolves it.  RE-VERIFIED 2026-11-01: saved full-app-tree grep ~/workspace/b656667-openclose-src/ruleF_grep_656667.txt (252 app Java files, branch work-2026-10-31, file list verified identical to the branch directory walk) finds zero hasPendingBindings and zero executePendingBindings hits in all 252 app Java files. Still OPEN because the databinding rebind dispatch is generated and library code and is not printed in this pass; a printed generated or library body showing whether the rebind path calls this override, or that it never does, is the named resolver. No convention is decided here. RE-VERIFIED 2026-11-01: saved full-app-tree grep ~/workspace/b656667-openclose-src/ruleF_grep_656667.txt (252 app Java files, branch work-2026-10-31, file list verified identical to the branch directory walk) finds zero hasPendingBindings and zero executePendingBindings hits in all 252 app Java files. Still OPEN because the databinding rebind dispatch is generated and library code and is not printed in this pass; a printed generated or library body showing whether the rebind path calls this override, or that it never does, is the named resolver. No convention is decided here. ROUND2 2026-11-01 (G11): re-run grep ~/workspace/b656667-openclose2-src/ruleF_grep_656667_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); no generated/library body was printed in round 2, so no flip in this pass — see the round-2 conditional tables before the per-row table. This pass decides no convention. [Phase 3 completion 2026-11-01: L3 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 39 | FragmentDetailTorrentTrackerListBindingImpl.invalidateAll | `()V` | REACHABLE | INFERRED | DetailTorrentTrackersFragment.java:105 DataBindingUtil.inflate(fragment_detail_torrent_tracker_list), field use only at :158-159/:172/:174/:176/:180-182, NO setViewModel/setVariable call [fresh, 406 lines, SHA 48d5a536…]; layout fragment_detail_torrent_tracker_list.xml declares NO <data>, NO variable, and NO @{...} data binding except a padding dimen [fresh, 27 lines]. Called by the generated Impl constructor on the row-35 construction. |
| 40 | FragmentDetailTorrentTrackerListBindingImpl.onFieldChange | `(ILjava/lang/Object;I)Z` | UNREACHABLE| INFERRED| As row 7: no variable set on this binding in printed code (TrackersFragment uses only fields :158-159/:172/:174/:176/:180-182; layout declares no variable). OPEN, not UNREACHABLE: no saved full-repo grep was run in this pass, and no search_code 0-result was used as evidence of absence. A printed caller or a saved full-repo grep (rule F/C5) resolves it. Companion row: batch 68 row 1 (TrackerList Impl setVariable) must be judged together with this row at merge.  RE-VERIFIED 2026-11-01: saved full-app-tree grep ~/workspace/b656667-openclose-src/ruleF_grep_656667.txt (252 app Java files, branch work-2026-10-31, file list verified identical to the branch directory walk) finds zero onFieldChange hits in all 252 app Java files, and the freshly printed layout declares no variable. Still OPEN because the generic-framework-callback convention is undecided: under it this row flips to REACHABLE INFERRED; if the merger rejects that convention and accepts the grep as trigger-absence it flips to UNREACHABLE no_trigger_in_app. This pass does not decide. Companion rows noted in the original file still apply. RE-VERIFIED 2026-11-01: saved full-app-tree grep ~/workspace/b656667-openclose-src/ruleF_grep_656667.txt (252 app Java files, branch work-2026-10-31, file list verified identical to the branch directory walk) finds zero onFieldChange hits in all 252 app Java files, and the freshly printed layout declares no variable. Still OPEN because the generic-framework-callback convention is undecided: under it this row flips to REACHABLE INFERRED; if the merger rejects that convention and accepts the grep as trigger-absence it flips to UNREACHABLE no_trigger_in_app. This pass does not decide. Companion rows noted in the original file still apply. ROUND2 2026-11-01 (G11): re-run grep ~/workspace/b656667-openclose2-src/ruleF_grep_656667_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); no generated/library body was printed in round 2, so no flip in this pass — see the round-2 conditional tables before the per-row table. This pass decides no convention. [Phase 2 fix 2026-11-01 — D4c annotation: this row IS UNREACHABLE no_trigger_in_app per DECISIONS.md D4c (no-variable layout, as in batch 68 rows); the 'OPEN, not UNREACHABLE' sentences above are superseded and do not change the label.] |

## Footer counts (must match header)
- REACHABLE proposed: 31 / 40
- UNREACHABLE proposed: 0 / 40
- OPEN: 9 / 40
- Total rows: 40, sequence 1-40 intact, plan order.
- Build: not run. C1: not run. Verified for merge: 0.
