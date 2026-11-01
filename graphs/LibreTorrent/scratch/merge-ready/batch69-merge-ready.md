**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 69 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: this batch only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Membership: exactly the 40 rows for this batch in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`,
  local copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA
  `0104806dd666c840049b3db52823d4b384fa1c92`), all TODO_CANDIDATE_REACHABLE
  (generator candidates, not evidence), in plan order. Method names in the table were
  generated from that plan copy, not hand-typed.
- Prior proposals (`~/workspace/libretorrent-batch<N>-proposal.md`) were used as INPUTS / lead
  lists only; every row below was re-judged against source printed in this pass (fresh
  connector fetches below, one file at a time with pauses, no fresh HTTP 429 hit).
- Judging convention (batches 67-69, stated so the merger can overturn it): the generated
  *Binding / *BindingImpl .java files and DataBinderMapperImpl are NOT in the
  final_java_only upload, so no generated method body was printed. Every databinding
  REACHABLE row below is therefore INFERRED, even where the app-side inflate call site is
  printed: the step from DataBindingUtil.inflate to the Impl is generated-mapper dispatch,
  and base-to-Impl dispatch is generated virtual dispatch.
  - Impl <clinit> / <init>(component,View) / <init>(component,View,Object[]) / base <init> /
    executeBindings / invalidateAll: REACHABLE INFERRED on a printed inflate.
  - setVariable / onFieldChange / hasPendingBindings: OPEN for every binding in this batch.
    No printed caller, no printed setVariable/setViewModel call, and no observable
    registration is printed for any of these bindings in the corpus printed here. They are
    NOT UNREACHABLE: no saved full-repo grep was run in this session, and a setter could
    exist in an unprinted file.
  - Routes are anchored at the fragment onCreateView / adapter onCreateViewHolder, NOT at
    the launcher: the steps creating the host fragments/activities and attaching the
    adapters were not printed in this session. Under a strict entry-route rule the
    REACHABLE rows revert to OPEN. This strict-entry convention is UNDECIDED at project
    level — recorded per row, not decided here.
  - A connector search_code call in this session returned global non-repo results and was
    disregarded entirely except as a locator lead (see batch 70 header for the one lead it
    produced, which was then verified by a fresh branch fetch); no verdict rests on
    search_code, and no search_code 0-result was used as evidence of absence.
- confirmed_by is SOURCE or INFERRED only, never DYN, FW-MEMORY, or UNVERIFIED.
  OPEN rows carry "—" (no confirmed_by claim).

## Counts — mechanically verified
- **40 rows, sequence 1-40 intact, in plan order.**
- **27 REACHABLE proposed / 0 UNREACHABLE proposed / 13 OPEN**, all REACHABLE INFERRED.
- **0 rows verified for merge.** Verification still requires the main agent's 1-in-5
  spot-check, `py_compile` + build on a full checkout, and the Mac build/C1 return — all
  **not run** here, never claimed passed.

## Printed source used in this pass (fresh, branch work-2026-10-31, saved in ~/workspace/b6870-src/)
This pass closes the prior proposal's freshness gap: the three files it flagged as
carried-forward / prior-session copies are ALL freshly fetched here:
- ui/feeditems/FeedItemsAdapter.java — inflate item_feed_items_list at :67-70.
- ui/detailtorrent/pages/peers/PeerListAdapter.java — inflate item_peers_list at :62-66.
- ui/detailtorrent/pages/files/TorrentContentFilesAdapter.java — inflate
  item_torrent_content_file at :76-80.
Plus, also fresh this session:
- ui/log/LogAdapter.java — inflate item_log_list at :51-55.
- ui/addtorrent/DownloadableFilesAdapter.java — inflate item_torrent_downloadable_file
  at :60-61.
- Grep over all fresh files above: zero hits for `setVariable` or `setViewModel`.
  That grep is over the printed corpus only, NOT a full-repo grep, and is not used as
  absence evidence for any UNREACHABLE claim (none is claimed).

## Still owed before merge
1. Saved full-repo grep for the 13 OPEN rows (hasPendingBindings x5, onFieldChange x4,
   setVariable x4) before any OPEN -> UNREACHABLE flip; none is flipped on absence here.
2. Printed host-fragment/activity creation steps (strict-entry rule) if the merger
   requires a launcher-anchored route; under that rule all 27 REACHABLE rows revert to OPEN.
3. Generated Impl bodies / DataBinderMapperImpl / layout XML — not in final_java_only —
   plus build, sampler, and C1 on a full checkout (git clone still fails without login in
   this VM). Nothing here is verified for merge.


## ROUND-2 REVISION 2026-11-01 (G17) — 0 flips; counts unchanged (27 REACHABLE / 0 UNREACHABLE / 13 OPEN)

**This revision flips no row and decides no convention.** It completes the
round-1 <include> check for this group, re-runs the rule-F grep, and records
CONDITIONAL outcomes for the 13 OPEN rows. All labels, confirmed_by values,
row order, and REACHABLE rows are exactly as before; only this section and a
short ROUND2 note per OPEN row were added. Original backed up to
`~/workspace/libretorrent-merge-backup-pre-openclose2/batch69-merge-ready.md`.
Build: not run. C1: not run. Nothing pushed.

### 1. The round-1 <include> check is now COMPLETE — result: negative
Full record in `~/workspace/b686970-openclose2-src/include_check_686970.txt`:
- All 69 files of `res/layout/` (round-1 fetch, verified byte-identical to the
  round-1 top-level 13-layout fetches, 13/13): the only `<include>` targets
  anywhere are `toolbar`, `main_drawer_content`, `add_torrent_info`, and
  `detail_torrent_appbar`. Zero `@layout/` references to any of the 13 group
  layouts, and zero `bind:` attributes in any file — so no layout passes a
  variable to an included child anywhere in `res/layout/`.
- Fresh connector listings this pass: `res/` holds exactly three layout dirs
  (`layout`, `layout-large-land-notouch`, `layout-sw600dp-land`). Each qualified
  dir holds only `detail_torrent_appbar.xml` (SHA
  `be659cb60ff9d3b2df954eed6c1eb05a3415fa41`, 36 lines, 0 `<include>`, no
  `<data>`) and `fragment_add_torrent_info.xml` (SHA
  `8e7ec93e56e894c3305b7a620ac540702c6a1f74`, 38 lines, single `<include>` to
  `add_torrent_info`). No qualified variant of any of the 13 exists.
- None of the 13 layouts declares a `<data>` variable, `<import>`, or
  `<include>`; the only `@{...}` expressions in the set are three static dimen
  sums referencing no variable and no Observable, so no observable registration
  and no onFieldChange route arises from them.
- Conclusion: the generated parent-to-child setVariable route is CLOSED for all
  13 bindings on layout evidence. What this does NOT close: generated Impl
  bodies and the databinding-library rebind body are still unprinted, so the
  verdicts below stay convention-dependent.

### 2. Rule-F grep re-run reproduces round 1 exactly
`~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt` (252 app Java
files, branch work-2026-10-31, count verified): `setVariable` 0 hits,
`onFieldChange` 0 hits, `hasPendingBindings` 0 hits, all 13 group Impl class
names 0 hits, `executePendingBindings` 0 hits. `setViewModel` 14 hits, none on
a batch 68/69/70 binding host. No connector 429 was hit in this pass (7 read
calls, ~30 s pauses); no search_code result was used.

### 3. CONDITIONAL table — the 13 OPEN rows (no option applied)
The setVariable-direction contradiction (batches 63-64 OPEN on zero hits vs
batch 65 REACHABLE via dispatch behind setViewModel, mechanically backwards
since setVariable CALLS the typed setter) and the generic-framework-callback
question (rule xv: onFieldChange/setVariable REACHABLE only where a variable
is actually set) are both UNDECIDED at project level. This pass applies none
of the options below. A printed generated Impl body or printed
databinding-library dispatch body would supersede this table.

| Option | setVariable rows 6, 15, 24, 33 | onFieldChange rows 5, 14, 23, 32 | hasPendingBindings rows 3, 12, 21, 30, 39 |
|---|---|---|---|
| S — status quo (this file) | stay OPEN | stay OPEN | stay OPEN |
| U — merger accepts combined evidence as trigger-absence (zero tree hits + no variable + no include parent + no typed-setter call on these bindings) | flip to UNREACHABLE no_trigger_in_app INFERRED | flip to UNREACHABLE no_trigger_in_app INFERRED | stay OPEN (variable-freedom does not close a library state query; rebind body still unprinted) |
| R — generic-framework-callback rule (framework/generated dispatch always runs these callbacks) | flip to REACHABLE INFERRED — but conflicts with rule (xv) for these no-variable bindings; merger must reconcile R with (xv) explicitly | flip to REACHABLE INFERRED — same (xv) conflict | stay OPEN (needs the printed rebind body either way) |

Named resolver for hasPendingBindings rows 3, 12, 21, 30, 39 under every
option: a printed generated Impl body or printed databinding-library rebind
body showing whether the rebind path calls this override, or that it never does.

### 4. Cross-batch linkage (judge consistently, never separately)
Rows 1-6 (ItemFeedItemsList Impl) continue the binding whose head rows are
batch 68 rows 38-40; rows 5-6 share batch 68's option U/R/S outcomes for that
binding. Rows 34-40 (ItemTorrentDownloadableFile Impl) are the head of the
Downloadable binding whose onFieldChange/setVariable rows are batch 70 rows
1-2; row 39 (hasPendingBindings) stays OPEN under every option above, while
70/1-2 follow this table's U/R/S options for their binding.

## Per-method table (plan order)

| # | Method | Label | confirmed_by | Printed route / citation |
|---|---|---|---|---|
| 1 | ItemFeedItemsListBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE | INFERRED | Called by batch-68 row-40 2-arg <init> in generated code; layout inflated at FeedItemsAdapter:67-70 (fresh this session). |
| 2 | ItemFeedItemsListBindingImpl.executeBindings | REACHABLE | INFERRED | Framework rebind after generated invalidateAll on the batch-68 row-40 construction. |
| 3 | ItemFeedItemsListBindingImpl.hasPendingBindings | OPEN | — | No printed caller in the printed corpus. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method and for executePendingBindings); <include> check completed (include_check_686970.txt, same dir). Still OPEN under every option in the CONDITIONAL table above: named resolver is a printed generated Impl body or printed databinding-library rebind body showing whether the rebind path calls this override. This pass decides no convention. |
| 4 | ItemFeedItemsListBindingImpl.invalidateAll | REACHABLE | INFERRED | Called by the generated Impl constructor on the batch-68 row-40 construction. |
| 5 | ItemFeedItemsListBindingImpl.onFieldChange | OPEN | — | No variable set on this binding in printed code, so no observable registration is printed. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 6 | ItemFeedItemsListBindingImpl.setVariable | OPEN | — | No printed setVariable call on this binding. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 7 | ItemLogListBinding.<init> | REACHABLE | INFERRED | Called by ItemLogList Impl <init> (rows 9-10) in generated code; layout inflated at LogAdapter:51-55 (fresh). |
| 8 | ItemLogListBindingImpl.<clinit> | REACHABLE | INFERRED | First reference via LogAdapter:51 inflate (fresh). |
| 9 | ItemLogListBindingImpl.<init>(DataBindingComponent,View) | REACHABLE | INFERRED | Mapper result of LogAdapter:51 inflate (fresh, generated, not printed). |
| 10 | ItemLogListBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE | INFERRED | Called by row 9 in generated code (pattern, body not printed). |
| 11 | ItemLogListBindingImpl.executeBindings | REACHABLE | INFERRED | Framework rebind after generated invalidateAll on the row-9 construction. |
| 12 | ItemLogListBindingImpl.hasPendingBindings | OPEN | — | No printed caller in the printed corpus. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method and for executePendingBindings); <include> check completed (include_check_686970.txt, same dir). Still OPEN under every option in the CONDITIONAL table above: named resolver is a printed generated Impl body or printed databinding-library rebind body showing whether the rebind path calls this override. This pass decides no convention. |
| 13 | ItemLogListBindingImpl.invalidateAll | REACHABLE | INFERRED | Called by the generated Impl constructor on the row-9 construction. |
| 14 | ItemLogListBindingImpl.onFieldChange | OPEN | — | No variable set in printed code (LogAdapter uses only fields). ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 15 | ItemLogListBindingImpl.setVariable | OPEN | — | No printed setVariable call on this binding. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 16 | ItemPeersListBinding.<init> | REACHABLE | INFERRED | Called by ItemPeersList Impl <init> (rows 18-19) in generated code; layout inflated at PeerListAdapter:62-66 (fresh this session). |
| 17 | ItemPeersListBindingImpl.<clinit> | REACHABLE | INFERRED | First reference via PeerListAdapter:62 inflate (fresh). |
| 18 | ItemPeersListBindingImpl.<init>(DataBindingComponent,View) | REACHABLE | INFERRED | Mapper result of PeerListAdapter:62 inflate (fresh, generated, not printed). |
| 19 | ItemPeersListBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE | INFERRED | Called by row 18 in generated code (pattern, body not printed). |
| 20 | ItemPeersListBindingImpl.executeBindings | REACHABLE | INFERRED | Framework rebind after generated invalidateAll on the row-18 construction. |
| 21 | ItemPeersListBindingImpl.hasPendingBindings | OPEN | — | No printed caller in the printed corpus. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method and for executePendingBindings); <include> check completed (include_check_686970.txt, same dir). Still OPEN under every option in the CONDITIONAL table above: named resolver is a printed generated Impl body or printed databinding-library rebind body showing whether the rebind path calls this override. This pass decides no convention. |
| 22 | ItemPeersListBindingImpl.invalidateAll | REACHABLE | INFERRED | Called by the generated Impl constructor on the row-18 construction. |
| 23 | ItemPeersListBindingImpl.onFieldChange | OPEN | — | No variable set / observable registration printed for this binding. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 24 | ItemPeersListBindingImpl.setVariable | OPEN | — | No printed setVariable call on this binding. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 25 | ItemTorrentContentFileBinding.<init> | REACHABLE | INFERRED | Called by ItemTorrentContentFile Impl <init> (rows 27-28) in generated code; layout inflated at TorrentContentFilesAdapter:76-80 (fresh this session). |
| 26 | ItemTorrentContentFileBindingImpl.<clinit> | REACHABLE | INFERRED | First reference via TorrentContentFilesAdapter:76 inflate (fresh). |
| 27 | ItemTorrentContentFileBindingImpl.<init>(DataBindingComponent,View) | REACHABLE | INFERRED | Mapper result of TorrentContentFilesAdapter:76 inflate (fresh, generated, not printed). |
| 28 | ItemTorrentContentFileBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE | INFERRED | Called by row 27 in generated code (pattern, body not printed). |
| 29 | ItemTorrentContentFileBindingImpl.executeBindings | REACHABLE | INFERRED | Framework rebind after generated invalidateAll on the row-27 construction. |
| 30 | ItemTorrentContentFileBindingImpl.hasPendingBindings | OPEN | — | No printed caller in the printed corpus. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method and for executePendingBindings); <include> check completed (include_check_686970.txt, same dir). Still OPEN under every option in the CONDITIONAL table above: named resolver is a printed generated Impl body or printed databinding-library rebind body showing whether the rebind path calls this override. This pass decides no convention. |
| 31 | ItemTorrentContentFileBindingImpl.invalidateAll | REACHABLE | INFERRED | Called by the generated Impl constructor on the row-27 construction. |
| 32 | ItemTorrentContentFileBindingImpl.onFieldChange | OPEN | — | No variable set / observable registration printed for this binding. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 33 | ItemTorrentContentFileBindingImpl.setVariable | OPEN | — | No printed setVariable call on this binding. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 34 | ItemTorrentDownloadableFileBinding.<init> | REACHABLE | INFERRED | Called by ItemTorrentDownloadableFile Impl <init> (rows 36-37) in generated code; layout inflated at DownloadableFilesAdapter:60-61 (fresh). |
| 35 | ItemTorrentDownloadableFileBindingImpl.<clinit> | REACHABLE | INFERRED | First reference via DownloadableFilesAdapter:60 inflate (fresh). |
| 36 | ItemTorrentDownloadableFileBindingImpl.<init>(DataBindingComponent,View) | REACHABLE | INFERRED | Mapper result of DownloadableFilesAdapter:60 inflate (fresh, generated, not printed). |
| 37 | ItemTorrentDownloadableFileBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE | INFERRED | Called by row 36 in generated code (pattern, body not printed). |
| 38 | ItemTorrentDownloadableFileBindingImpl.executeBindings | REACHABLE | INFERRED | Framework rebind after generated invalidateAll on the row-36 construction. |
| 39 | ItemTorrentDownloadableFileBindingImpl.hasPendingBindings | OPEN | — | No printed caller in the printed corpus. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method and for executePendingBindings); <include> check completed (include_check_686970.txt, same dir). Still OPEN under every option in the CONDITIONAL table above: named resolver is a printed generated Impl body or printed databinding-library rebind body showing whether the rebind path calls this override. This pass decides no convention. |
| 40 | ItemTorrentDownloadableFileBindingImpl.invalidateAll | REACHABLE | INFERRED | Called by the generated Impl constructor on the row-36 construction. |
