# LibreTorrent batch 85 — Phase 2 spot-check — UNVERIFIED (spot-check only, not a merge verdict)

- Batch: 85. Work file checked: `~/workspace/overnight/stream-A/work/batch85-merge-ready.md` (UNVERIFIED proposal, not a result).
- Rows checked (21): sample rows 1, 6, 11, 16, 21, 26, 31, 36, plus every row whose label changed in the file's dated 2026-11-01 revision notes — OPEN-close pass flips to REACHABLE: 25, 27, 28, 29, 30, 32, 33, 34, 35, 37, 38, 39; OPEN-close round-2 flips to UNREACHABLE: 31, 40. (Rows 31 and 36 are in both sets, counted once.) The 2026-11-01 grep-flip re-check changed no label.
- Method: re-derived from already-fetched source on disk (`~/workspace/b8586-src/`, `~/workspace/b8586-openclose-src/`, `~/workspace/ruleF-src/`, `~/workspace/b10171819-openclose-src/fw_src/`, `~/workspace/overnight/stream-A/greps/grep_recheck_3arg_ctors_complete.txt`); no GitHub connector fetch was needed, no 429 hit, no file missing.
- No edit was made to the merge-ready file. No push. Build/sampler/C1: not run (not this task).
- Convention note (NOT decided here): the UNREACHABLE rows 31 and 40 rest on the LayoutInflater 2-arg-only rule plus absence greps, and the file itself records an all-five-together revert condition (with batch 86 rows 12/17/21) and notes batch 94's PiecesView 3-arg ctor stays OPEN on the same evidence shape. The merger must apply one rule to all 3-arg ctors; this spot-check passes rows 31/40 as filed under the file's stated rule and does not decide that project-wide rule.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence (file:line, local copy) |
|---|---|---|---|---|
| 1 | CreateTorrentViewModel.getPieceSizeByIndex | REACHABLE / SOURCE | PASS | Called by makeBuilder() CreateTorrentViewModel.java:191; def :333-335. |
| 6 | CreateTorrentViewModel.lambda$makeBuilder$2 | REACHABLE / INFERRED | PASS | FileNameFilter lambda in makeBuilder() CreateTorrentViewModel.java:199-209; invoked by TorrentBuilder during build(), library dispatch unprinted → INFERRED correct. |
| 11 | CreateTorrentViewModel.makePercentProgress | REACHABLE / INFERRED | PASS | Def CreateTorrentViewModel.java:242-245; only via Rx subscribe buildTorrent() :169 → INFERRED correct. |
| 16 | CreateTorrentViewModel.resetPercentProgress | REACHABLE / SOURCE | PASS | Called by buildTorrent() CreateTorrentViewModel.java:165; def :247-250. |
| 21 | CreateTorrentViewModel$BuildState.<init> | REACHABLE / SOURCE | PASS | Def CreateTorrentViewModel.java:74-78; constructed :113, :153, :225, :239. |
| 25 | ColorView.<init> (2-arg) | REACHABLE / INFERRED | PASS | tags_list_item.xml:14 and drawer_tags_list_item.xml:16 declare ColorView id color; LayoutInflater 2-arg dispatch unprinted → INFERRED correct. (dialog_add_tag.xml:62 is an additional declaration; it does not change the verdict.) |
| 26 | ColorView.getColor | OPEN / — | PASS | Def ColorView.java:102-104 (`circlePaint.getColor()`). Tree grep finds no ColorView-receiver .getColor() call; binding.color sites are setColor only (TagsAdapter :103/:191). OPEN as filed; needs a printed caller, not a zero grep. |
| 27 | ColorView.onDraw | REACHABLE / INFERRED | PASS | Def ColorView.java:84-91; framework callback after ColorView inflation (row 25). |
| 28 | ColorView.onSizeChanged | REACHABLE / INFERRED | PASS | Def ColorView.java:76-81; framework callback after ColorView inflation (row 25). |
| 29 | ColorView.setColor | REACHABLE / SOURCE | PASS | ui/tag TagsAdapter.java:103 and drawer TagsAdapter.java:191 `binding.color.setColor(item.info.color)`; binding.color is ColorView in both layouts. |
| 30 | EmptyRecyclerView.<init> (2-arg) | REACHABLE / INFERRED | PASS | Declared fragment_main.xml:10 (torrent_list), fragment_feed.xml:16 (feed_list), fragment_feed_items.xml:34 (feed_items_list); LayoutInflater 2-arg dispatch → INFERRED correct. |
| 31 | EmptyRecyclerView.<init> (3-arg) | UNREACHABLE / INFERRED | PASS | Kind no_trigger_in_app as filed. Def EmptyRecyclerView.java:64-67; 2-arg ctor :59-61 calls super(context, attrs) only, never this(...,int). fw LayoutInflater.java:88 mConstructorArgs size 2, :90-91 signature {Context, AttributeSet}, :615 the getConstructor call. Saved greps: 0 `new EmptyRecyclerView(` / 0 `extends` / 0 reflection lookups (252-file grep + complete-tree/XML re-check file). See convention note above. |
| 32 | EmptyRecyclerView.checkEmpty | REACHABLE / SOURCE | PASS | Called by setAdapter EmptyRecyclerView.java:91, setEmptyView :97, observer :38/:44/:50 — all on REACHABLE routes. |
| 33 | EmptyRecyclerView.setAdapter | REACHABLE / SOURCE | PASS | MainFragment.java:155, FeedFragment.java:135, FeedItemsFragment.java:153 (bindings resolve to EmptyRecyclerView per the row-30 layouts). |
| 34 | EmptyRecyclerView.setEmptyView | REACHABLE / SOURCE | PASS | MainFragment.java:151, FeedFragment.java:131, FeedItemsFragment.java:150, LogActivity.java:107. |
| 35 | EmptyRecyclerView$1.<init> | REACHABLE / INFERRED | PASS | Field-initialiser observer EmptyRecyclerView.java:33; runs at view instantiation (row 30 route). |
| 36 | EmptyRecyclerView$1.onChanged | REACHABLE / INFERRED | PASS | Observer dispatch, registered by setAdapter EmptyRecyclerView.java:89; def :36-38. |
| 37 | EmptyRecyclerView$1.onItemRangeInserted | REACHABLE / INFERRED | PASS | Same registration; def :42-44. |
| 38 | EmptyRecyclerView$1.onItemRangeRemoved | REACHABLE / INFERRED | PASS | Same registration; def :48-50. |
| 39 | ExpansionHeader.<init> (2-arg) | REACHABLE / INFERRED | PASS | drawer_group_header.xml:2 root tag ExpansionHeader, inflated by DrawerExpandableAdapter.java:78; LayoutInflater 2-arg dispatch → INFERRED correct. |
| 40 | ExpansionHeader.<init> (3-arg) | UNREACHABLE / INFERRED | PASS | Kind no_trigger_in_app as filed. Def ExpansionHeader.java:70-74; 2-arg ctor :63-65 calls super(context, attrs) only, never this(...,int). Same LayoutInflater evidence and same zero-hit saved greps as row 31. See convention note above. |

## Totals

- PASS: 21 / 21. FAIL: 0 / 21.

## Proposed corrections

- None. No row label or confirmed_by needs changing on the evidence checked. The 3-arg-ctor project-wide rule is left for the merger.
