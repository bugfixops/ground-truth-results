**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 68 — merge-ready part — UNVERIFIED

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
- ui/feeds/FeedFragment.java — inflate fragment_feed at :99.
- ui/feeditems/FeedItemsFragment.java — inflate fragment_feed_items at :111.
- ui/main/MainFragment.java — inflate fragment_main at :119.
- ui/feeds/FeedChannelListAdapter.java — inflate item_feed_channel_list at :82-85.
- ui/feeditems/FeedItemsAdapter.java — inflate item_feed_items_list at :67-70.
- ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java — inflate
  fragment_detail_torrent_tracker_list at :105; field use only (trackerList :158-182),
  no setVariable call — this is why row 1 stays OPEN.
- Grep over all fresh files above: zero hits for `setVariable` or `setViewModel`.
  That grep is over the printed corpus only, NOT a full-repo grep, and is not used as
  absence evidence for any UNREACHABLE claim (none is claimed).

## Still owed before merge
1. Saved full-repo grep (rule F / C5, class-name grep, output saved in scratch/) for the
   13 OPEN rows — above all the setVariable / onFieldChange rows. No OPEN row may become
   UNREACHABLE on the partial printed corpus alone.
2. Printed launcher/host-creation chain if the merger requires strict entry routes;
   otherwise the 27 REACHABLE rows carry the anchor caveat above.
3. Batch 69 must be judged consistently with rows 38-40 here (it is — see batch69 file).
4. Build, sampler, and C1 on a full checkout (clone still fails in this VM without login;
   not claimed here).


## ROUND-2 REVISION 2026-11-01 (G17) — 0 flips; counts unchanged (27 REACHABLE / 0 UNREACHABLE / 13 OPEN)

**This revision flips no row and decides no convention.** It finishes the one item
left open by round 1, re-runs the rule-F grep, and records CONDITIONAL outcomes
for the 13 OPEN rows. All labels, confirmed_by values, row order, and REACHABLE
rows are exactly as before; only this section and a short ROUND2 note per OPEN
row were added. Original backed up to
`~/workspace/libretorrent-merge-backup-pre-openclose2/batch68-merge-ready.md`.
Build: not run. C1: not run. Nothing pushed.

### 1. The round-1 <include> check is now COMPLETE — result: negative
Round 1 had fetched all 13 group layouts fresh and found none declares a `<data>`
variable, `<import>`, or `<include>`; the one unfinished item was whether any
other layout `<include>`s one of the 13. Completed this pass, full record in
`~/workspace/b686970-openclose2-src/include_check_686970.txt`:
- All 69 files of `res/layout/` (round-1 fetch, verified byte-identical to the
  round-1 top-level 13-layout fetches, 13/13): the only `<include>` targets
  anywhere are `toolbar`, `main_drawer_content`, `add_torrent_info`, and
  `detail_torrent_appbar`. Zero `@layout/` references to any of the 13, and
  zero `bind:` attributes in any file — so no layout passes a variable to an
  included child anywhere in `res/layout/`.
- Fresh connector listings this pass: `res/` holds exactly three layout dirs
  (`layout`, `layout-large-land-notouch`, `layout-sw600dp-land`). Each qualified
  dir holds only `detail_torrent_appbar.xml` (SHA
  `be659cb60ff9d3b2df954eed6c1eb05a3415fa41`, 36 lines, 0 `<include>`, no
  `<data>` — matches batch 60's recorded SHA) and `fragment_add_torrent_info.xml`
  (SHA `8e7ec93e56e894c3305b7a620ac540702c6a1f74`, 38 lines, single `<include>`
  to `add_torrent_info` with an `app:viewModel` pass-through). No qualified
  variant of any of the 13 exists.
- The only `@{...}` expressions in the 13 layouts are three identical static
  resource sums, `android:paddingBottom="@{@dimen/fab_size + @dimen/fab_margin}"`
  (tracker-list :14, feed :20, main :14). They reference no variable and no
  Observable, so they create no observable registration and no onFieldChange route.
- Conclusion: the generated parent-to-child setVariable route is CLOSED for all
  13 bindings on layout evidence. What this does NOT close: generated Impl
  bodies and the databinding-library rebind body are still unprinted, so the
  verdicts below stay convention-dependent.

### 2. Rule-F grep re-run reproduces round 1 exactly
`~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt` (252 app Java
files, branch work-2026-10-31, count verified): `setVariable` 0 hits,
`onFieldChange` 0 hits, `hasPendingBindings` 0 hits, all 13 group Impl class
names 0 hits, `executePendingBindings` 0 hits. `setViewModel` 14 hits, none on
a batch 68/69/70 binding host (LogActivity, SessionLogFilterDialog,
FileManagerDialog, GoToFolderDialog, DetailTorrentInfoFragment,
DetailTorrentStateFragment, DetailTorrentPiecesFragment,
DetailTorrentFilesFragment, CreateTorrentDialog, AddTorrentFilesFragment,
AddTorrentInfoFragment, AddTagDialog, AddLinkDialog, AddFeedDialog). No
connector 429 was hit in this pass (7 read calls, ~30 s pauses); no search_code
result was used.

### 3. CONDITIONAL table — the 13 OPEN rows (no option applied)
The setVariable-direction contradiction (batches 63-64 OPEN on zero hits vs
batch 65 REACHABLE via dispatch behind setViewModel, mechanically backwards
since setVariable CALLS the typed setter) and the generic-framework-callback
question (rule xv: onFieldChange/setVariable REACHABLE only where a variable
is actually set) are both UNDECIDED at project level. This pass applies none
of the options below. A printed generated Impl body or printed
databinding-library dispatch body would supersede this table.

| Option | setVariable rows 1, 10, 19, 28, 37 | onFieldChange rows 9, 18, 27, 36 | hasPendingBindings rows 7, 16, 25, 34 |
|---|---|---|---|
| S — status quo (this file) | stay OPEN | stay OPEN | stay OPEN |
| U — merger accepts combined evidence as trigger-absence (zero tree hits + no variable + no include parent + no typed-setter call on these bindings + only static dimen expressions) | flip to UNREACHABLE no_trigger_in_app INFERRED | flip to UNREACHABLE no_trigger_in_app INFERRED | stay OPEN (variable-freedom does not close a library state query; rebind body still unprinted) |
| R — generic-framework-callback rule (framework/generated dispatch always runs these callbacks) | flip to REACHABLE INFERRED — but conflicts with rule (xv) for these no-variable bindings; merger must reconcile R with (xv) explicitly | flip to REACHABLE INFERRED — same (xv) conflict | stay OPEN (needs the printed rebind body either way) |

Named resolver for hasPendingBindings rows 7, 16, 25, 34 under every option: a
printed generated Impl body or printed databinding-library rebind body showing
whether the rebind path calls this override, or that it never does.

### 4. Companion linkage (judge together, never separately)
Row 1 (FragmentDetailTorrentTrackerListBindingImpl.setVariable) is the companion
of batch 67 row 40 (same binding's onFieldChange). Batch 67's round-2 pass (G11)
kept 67/40 OPEN with an equivalent conditional table. This row is therefore NOT
flipped on 67/40 alone: under option U both flip to UNREACHABLE
no_trigger_in_app; under option R both flip to REACHABLE INFERRED; under S
both stay OPEN. Rows 38-40 (ItemFeedItemsList base/Impl init) are the head of
the ItemFeedItemsList Impl whose callback rows continue in batch 69 rows 1-6;
those rows share this file's option U/R/S outcomes for the same binding.

## Per-method table (plan order)

| # | Method | Label | confirmed_by | Printed route / citation |
|---|---|---|---|---|
| 1 | FragmentDetailTorrentTrackerListBindingImpl.setVariable | OPEN | — | Companion to batch 67 rows 34-40. TrackersFragment uses only fields (fresh: inflate :105, trackerList use :158-182, no setter). No printed setVariable call. Resolves with a printed call site or saved full-repo grep. NOT UNREACHABLE. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. Companion to batch 67 row 40 (same binding's onFieldChange, kept OPEN by G11 round 2): judge together — not flipped on 67/40 alone; under option U both flip to UNREACHABLE no_trigger_in_app, under option R both flip to REACHABLE INFERRED. |
| 2 | FragmentFeedBinding.<init> | REACHABLE | INFERRED | Called by FragmentFeed Impl <init> (rows 4-5) in generated code; layout inflated at FeedFragment:99 (fresh). |
| 3 | FragmentFeedBindingImpl.<clinit> | REACHABLE | INFERRED | First reference via FeedFragment:99 inflate (fresh). |
| 4 | FragmentFeedBindingImpl.<init>(DataBindingComponent,View) | REACHABLE | INFERRED | Mapper result of FeedFragment:99 inflate (fresh, generated, not printed). |
| 5 | FragmentFeedBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE | INFERRED | Called by row 4 in generated code (pattern, body not printed). |
| 6 | FragmentFeedBindingImpl.executeBindings | REACHABLE | INFERRED | Framework rebind after generated invalidateAll on the row-4 construction. |
| 7 | FragmentFeedBindingImpl.hasPendingBindings | OPEN | — | No printed caller in the printed corpus. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method and for executePendingBindings); <include> check completed (include_check_686970.txt, same dir). Still OPEN under every option in the CONDITIONAL table above: named resolver is a printed generated Impl body or printed databinding-library rebind body showing whether the rebind path calls this override. This pass decides no convention. |
| 8 | FragmentFeedBindingImpl.invalidateAll | REACHABLE | INFERRED | Called by the generated Impl constructor on the row-4 construction. |
| 9 | FragmentFeedBindingImpl.onFieldChange | OPEN | — | No variable set on this binding in printed code, so no observable registration is printed. Resolves with a printed setter site or saved full-repo grep. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 10 | FragmentFeedBindingImpl.setVariable | OPEN | — | No printed setVariable call on this binding. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 11 | FragmentFeedItemsBinding.<init> | REACHABLE | INFERRED | Called by FeedItems Impl <init> (rows 13-14) in generated code; layout inflated at FeedItemsFragment:111 (fresh). |
| 12 | FragmentFeedItemsBindingImpl.<clinit> | REACHABLE | INFERRED | First reference via FeedItemsFragment:111 inflate (fresh). |
| 13 | FragmentFeedItemsBindingImpl.<init>(DataBindingComponent,View) | REACHABLE | INFERRED | Mapper result of FeedItemsFragment:111 inflate (fresh, generated, not printed). |
| 14 | FragmentFeedItemsBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE | INFERRED | Called by row 13 in generated code (pattern, body not printed). |
| 15 | FragmentFeedItemsBindingImpl.executeBindings | REACHABLE | INFERRED | Framework rebind after generated invalidateAll on the row-13 construction. |
| 16 | FragmentFeedItemsBindingImpl.hasPendingBindings | OPEN | — | No printed caller in the printed corpus. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method and for executePendingBindings); <include> check completed (include_check_686970.txt, same dir). Still OPEN under every option in the CONDITIONAL table above: named resolver is a printed generated Impl body or printed databinding-library rebind body showing whether the rebind path calls this override. This pass decides no convention. |
| 17 | FragmentFeedItemsBindingImpl.invalidateAll | REACHABLE | INFERRED | Called by the generated Impl constructor on the row-13 construction. |
| 18 | FragmentFeedItemsBindingImpl.onFieldChange | OPEN | — | As row 9: no variable set in printed code. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 19 | FragmentFeedItemsBindingImpl.setVariable | OPEN | — | No printed setVariable call on this binding. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 20 | FragmentMainBinding.<init> | REACHABLE | INFERRED | Called by Main Impl <init> (rows 22-23) in generated code; layout inflated at MainFragment:119 (fresh). |
| 21 | FragmentMainBindingImpl.<clinit> | REACHABLE | INFERRED | First reference via MainFragment:119 inflate (fresh). |
| 22 | FragmentMainBindingImpl.<init>(DataBindingComponent,View) | REACHABLE | INFERRED | Mapper result of MainFragment:119 inflate (fresh, generated, not printed). |
| 23 | FragmentMainBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE | INFERRED | Called by row 22 in generated code (pattern, body not printed). |
| 24 | FragmentMainBindingImpl.executeBindings | REACHABLE | INFERRED | Framework rebind after generated invalidateAll on the row-22 construction. |
| 25 | FragmentMainBindingImpl.hasPendingBindings | OPEN | — | No printed caller in the printed corpus. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method and for executePendingBindings); <include> check completed (include_check_686970.txt, same dir). Still OPEN under every option in the CONDITIONAL table above: named resolver is a printed generated Impl body or printed databinding-library rebind body showing whether the rebind path calls this override. This pass decides no convention. |
| 26 | FragmentMainBindingImpl.invalidateAll | REACHABLE | INFERRED | Called by the generated Impl constructor on the row-22 construction. |
| 27 | FragmentMainBindingImpl.onFieldChange | OPEN | — | As row 9: no variable set in printed code. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 28 | FragmentMainBindingImpl.setVariable | OPEN | — | No printed setVariable call on this binding. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 29 | ItemFeedChannelListBinding.<init> | REACHABLE | INFERRED | Called by ItemChannel Impl <init> (rows 31-32) in generated code; layout inflated at FeedChannelListAdapter:82-85 (fresh). |
| 30 | ItemFeedChannelListBindingImpl.<clinit> | REACHABLE | INFERRED | First reference via FeedChannelListAdapter:82 inflate (fresh). |
| 31 | ItemFeedChannelListBindingImpl.<init>(DataBindingComponent,View) | REACHABLE | INFERRED | Mapper result of FeedChannelListAdapter:82 inflate (fresh, generated, not printed). |
| 32 | ItemFeedChannelListBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE | INFERRED | Called by row 31 in generated code (pattern, body not printed). |
| 33 | ItemFeedChannelListBindingImpl.executeBindings | REACHABLE | INFERRED | Framework rebind after generated invalidateAll on the row-31 construction. |
| 34 | ItemFeedChannelListBindingImpl.hasPendingBindings | OPEN | — | No printed caller in the printed corpus. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method and for executePendingBindings); <include> check completed (include_check_686970.txt, same dir). Still OPEN under every option in the CONDITIONAL table above: named resolver is a printed generated Impl body or printed databinding-library rebind body showing whether the rebind path calls this override. This pass decides no convention. |
| 35 | ItemFeedChannelListBindingImpl.invalidateAll | REACHABLE | INFERRED | Called by the generated Impl constructor on the row-31 construction. |
| 36 | ItemFeedChannelListBindingImpl.onFieldChange | OPEN | — | As row 9: no variable set in printed code (adapter uses only fields). ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 37 | ItemFeedChannelListBindingImpl.setVariable | OPEN | — | No printed setVariable call on this binding. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 38 | ItemFeedItemsListBinding.<init> | REACHABLE | INFERRED | Called by ItemFeedItems Impl <init> (row 40 and batch 69) in generated code; layout inflated at FeedItemsAdapter:67-70 (fresh). |
| 39 | ItemFeedItemsListBindingImpl.<clinit> | REACHABLE | INFERRED | First reference via FeedItemsAdapter:67 inflate (fresh). |
| 40 | ItemFeedItemsListBindingImpl.<init>(DataBindingComponent,View) | REACHABLE | INFERRED | Mapper result of FeedItemsAdapter:67 inflate (fresh, generated, not printed). |
