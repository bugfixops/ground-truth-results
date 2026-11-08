# Stream A Phase 2 spot-check — 93 — UNVERIFIED spot-check, NOT a merge decision
Scope: batch 93 only, LibreTorrent labels only. Source file checked: ~/workspace/overnight/stream-A/work/batch93-merge-ready.md (UNVERIFIED proposal, not a result).
Method: each row below was re-derived from printed source, searched in already-fetched local copies first (~/workspace/overnight/stream-A/corpus/, 281 app-Java files; ~/workspace/b9192-src/; ~/workspace/b90929495969799102-openclose-src/; ~/workspace/overnight/stream-A/greps/). No merge-ready file was edited, no tick written, no push made. Build/sampler/C1: not run (not this task).
Verdict rule used: PASS = the row's label is correct and its controlling evidence (including any dated 2026-11-01 revision note in the file, which supersedes older row text) locates the route. FAIL = the label is wrong, or the stated evidence mislocates the route (wrong caller/branch) with no superseding note. Two things are NOT failed: (a) confirmed_by SOURCE vs INFERRED on lifecycle/framework rows — both are permitted values and the classification convention is not decided here; (b) lambda/anonymous $ numbering, which the work files themselves state is source-order, NOT bytecode-verified, and a swap within a group would not change any label. Off-by-one definition spans are noted as corrections, not failures. A row turning on an undecided project convention is left as-is and flagged, never decided here.
No fresh 429 occurred in this pass (4 connector fetches, batch 99 only, one at a time with ~30 s pauses; no token used).

Rows checked (8): sample rows 1, 6, 11, 16, 21, 26, 31, 36. No Phase-1 label change is listed in this file's dated 2026-11-01 notes, so no extra rows apply.

- Row 1 TorrentContentFilesAdapter.<init> — PASS (REACHABLE, SOURCE). Definition :59-63; constructed DetailTorrentFilesFragment.java:207.
- Row 6 TorrentContentFilesAdapter.setSelectionTracker — PASS (REACHABLE, SOURCE). Definition :66-69; called DetailTorrentFilesFragment.java:286.
- Row 11 TorrentContentFilesAdapter$ItemDetails.getPosition — PASS (REACHABLE, INFERRED). Definition :308-312 (row cites :309-312, off-by-one span, immaterial); SelectionTracker framework reads ItemDetails; no app-code caller printed, dispatch INFERRED.
- Row 16 TorrentContentFilesAdapter$KeyProvider.getKey — PASS (REACHABLE, INFERRED). Definition :278-281; body calls selectable.getItemKey :280; KeyProvider registered in the fragment's tracker builder (FilesFragment.java:225).
- Row 21 TorrentContentFilesAdapter$ViewHolder.lambda$bind$0 — PASS (REACHABLE, INFERRED). Item-view click listener set :166; body calls listener.onItemClicked :171; framework click dispatch INFERRED; $ numbering source-order, not bytecode-verified.
- Row 26 DetailTorrentPeersFragment.lambda$subscribeAdapter$0 — PASS (REACHABLE, INFERRED). flatMapSingle lambda :176-181 (map PeerItem::new :178); subscribeAdapter called by onStart :111; Rx dispatch INFERRED.
- Row 31 DetailTorrentPeersFragment.onItemLongClick — PASS (REACHABLE, SOURCE). Definition :186-191; printed caller PeerListAdapter ViewHolder long-click lambda :138-142; body calls sharePeerIp :188.
- Row 36 DetailTorrentPeersFragment.onViewCreated — PASS (REACHABLE, INFERRED). Definition :115-143; constructs PeerListAdapter :126 and the $1 animator :132; fragment lifecycle dispatch INFERRED.

Totals: 8 rows checked — 8 PASS, 0 FAIL.
Proposed corrections: none (row 11 span :309-312 vs definition :308-312 is immaterial).
