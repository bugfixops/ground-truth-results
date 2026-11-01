# LibreTorrent batch 69 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
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


## Per-method table (plan order)

| # | Method | Label | confirmed_by | Printed route / citation |
|---|---|---|---|---|
| 1 | ItemFeedItemsListBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE | INFERRED | Called by batch-68 row-40 2-arg <init> in generated code; layout inflated at FeedItemsAdapter:67-70 (fresh this session). |
| 2 | ItemFeedItemsListBindingImpl.executeBindings | REACHABLE | INFERRED | Framework rebind after generated invalidateAll on the batch-68 row-40 construction. |
| 3 | ItemFeedItemsListBindingImpl.hasPendingBindings | OPEN | — | No printed caller in the printed corpus. |
| 4 | ItemFeedItemsListBindingImpl.invalidateAll | REACHABLE | INFERRED | Called by the generated Impl constructor on the batch-68 row-40 construction. |
| 5 | ItemFeedItemsListBindingImpl.onFieldChange | OPEN | — | No variable set on this binding in printed code, so no observable registration is printed. |
| 6 | ItemFeedItemsListBindingImpl.setVariable | OPEN | — | No printed setVariable call on this binding. |
| 7 | ItemLogListBinding.<init> | REACHABLE | INFERRED | Called by ItemLogList Impl <init> (rows 9-10) in generated code; layout inflated at LogAdapter:51-55 (fresh). |
| 8 | ItemLogListBindingImpl.<clinit> | REACHABLE | INFERRED | First reference via LogAdapter:51 inflate (fresh). |
| 9 | ItemLogListBindingImpl.<init>(DataBindingComponent,View) | REACHABLE | INFERRED | Mapper result of LogAdapter:51 inflate (fresh, generated, not printed). |
| 10 | ItemLogListBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE | INFERRED | Called by row 9 in generated code (pattern, body not printed). |
| 11 | ItemLogListBindingImpl.executeBindings | REACHABLE | INFERRED | Framework rebind after generated invalidateAll on the row-9 construction. |
| 12 | ItemLogListBindingImpl.hasPendingBindings | OPEN | — | No printed caller in the printed corpus. |
| 13 | ItemLogListBindingImpl.invalidateAll | REACHABLE | INFERRED | Called by the generated Impl constructor on the row-9 construction. |
| 14 | ItemLogListBindingImpl.onFieldChange | OPEN | — | No variable set in printed code (LogAdapter uses only fields). |
| 15 | ItemLogListBindingImpl.setVariable | OPEN | — | No printed setVariable call on this binding. |
| 16 | ItemPeersListBinding.<init> | REACHABLE | INFERRED | Called by ItemPeersList Impl <init> (rows 18-19) in generated code; layout inflated at PeerListAdapter:62-66 (fresh this session). |
| 17 | ItemPeersListBindingImpl.<clinit> | REACHABLE | INFERRED | First reference via PeerListAdapter:62 inflate (fresh). |
| 18 | ItemPeersListBindingImpl.<init>(DataBindingComponent,View) | REACHABLE | INFERRED | Mapper result of PeerListAdapter:62 inflate (fresh, generated, not printed). |
| 19 | ItemPeersListBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE | INFERRED | Called by row 18 in generated code (pattern, body not printed). |
| 20 | ItemPeersListBindingImpl.executeBindings | REACHABLE | INFERRED | Framework rebind after generated invalidateAll on the row-18 construction. |
| 21 | ItemPeersListBindingImpl.hasPendingBindings | OPEN | — | No printed caller in the printed corpus. |
| 22 | ItemPeersListBindingImpl.invalidateAll | REACHABLE | INFERRED | Called by the generated Impl constructor on the row-18 construction. |
| 23 | ItemPeersListBindingImpl.onFieldChange | OPEN | — | No variable set / observable registration printed for this binding. |
| 24 | ItemPeersListBindingImpl.setVariable | OPEN | — | No printed setVariable call on this binding. |
| 25 | ItemTorrentContentFileBinding.<init> | REACHABLE | INFERRED | Called by ItemTorrentContentFile Impl <init> (rows 27-28) in generated code; layout inflated at TorrentContentFilesAdapter:76-80 (fresh this session). |
| 26 | ItemTorrentContentFileBindingImpl.<clinit> | REACHABLE | INFERRED | First reference via TorrentContentFilesAdapter:76 inflate (fresh). |
| 27 | ItemTorrentContentFileBindingImpl.<init>(DataBindingComponent,View) | REACHABLE | INFERRED | Mapper result of TorrentContentFilesAdapter:76 inflate (fresh, generated, not printed). |
| 28 | ItemTorrentContentFileBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE | INFERRED | Called by row 27 in generated code (pattern, body not printed). |
| 29 | ItemTorrentContentFileBindingImpl.executeBindings | REACHABLE | INFERRED | Framework rebind after generated invalidateAll on the row-27 construction. |
| 30 | ItemTorrentContentFileBindingImpl.hasPendingBindings | OPEN | — | No printed caller in the printed corpus. |
| 31 | ItemTorrentContentFileBindingImpl.invalidateAll | REACHABLE | INFERRED | Called by the generated Impl constructor on the row-27 construction. |
| 32 | ItemTorrentContentFileBindingImpl.onFieldChange | OPEN | — | No variable set / observable registration printed for this binding. |
| 33 | ItemTorrentContentFileBindingImpl.setVariable | OPEN | — | No printed setVariable call on this binding. |
| 34 | ItemTorrentDownloadableFileBinding.<init> | REACHABLE | INFERRED | Called by ItemTorrentDownloadableFile Impl <init> (rows 36-37) in generated code; layout inflated at DownloadableFilesAdapter:60-61 (fresh). |
| 35 | ItemTorrentDownloadableFileBindingImpl.<clinit> | REACHABLE | INFERRED | First reference via DownloadableFilesAdapter:60 inflate (fresh). |
| 36 | ItemTorrentDownloadableFileBindingImpl.<init>(DataBindingComponent,View) | REACHABLE | INFERRED | Mapper result of DownloadableFilesAdapter:60 inflate (fresh, generated, not printed). |
| 37 | ItemTorrentDownloadableFileBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE | INFERRED | Called by row 36 in generated code (pattern, body not printed). |
| 38 | ItemTorrentDownloadableFileBindingImpl.executeBindings | REACHABLE | INFERRED | Framework rebind after generated invalidateAll on the row-36 construction. |
| 39 | ItemTorrentDownloadableFileBindingImpl.hasPendingBindings | OPEN | — | No printed caller in the printed corpus. |
| 40 | ItemTorrentDownloadableFileBindingImpl.invalidateAll | REACHABLE | INFERRED | Called by the generated Impl constructor on the row-36 construction. |
