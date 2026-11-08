# Spot-check — LibreTorrent batch 69 (Phase 2)

- Source file checked (read-only, NOT edited): `~/workspace/overnight/stream-A/work/batch69-merge-ready.md`
- Branch: work-2026-10-31, repo bugfixops/ground-truth-results. No pushes, no edits to any merge-ready file.
- Method: re-derived each checked row from already-fetched local source (no connector fetch needed, so no 429). Build/sampler/C1: not run (not this task).
- Batch totals re-verified from the label column: 40 rows, sequence 1–40 intact, 27 REACHABLE / 8 UNREACHABLE / 5 OPEN — matches the Phase 1c header (8 D4c flips; hasPendingBindings rows left OPEN under D4f).
- Conventions (D4c/D4f) were applied as recorded in `~/workspace/overnight/stream-A/DECISIONS.md`; no convention was decided here.
- D4c evidence base verified as a whole: `~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt` (0 hits in the 252-file app-Java tree for setVariable/onFieldChange/hasPendingBindings) and `~/workspace/b686970-openclose2-src/include_check_686970.txt` (no layout includes any of the 13 group layouts) — same files as the batch 68 spot-check.

## Rows checked (15)
Sample rows 1, 6, 11, 16, 21, 26, 31, 36, plus Phase 1c D4c flips 5, 6, 14, 15, 23, 24, 32, 33.

## Verdicts

| Row | Method | Label in file | Verdict | Evidence |
|---|---|---|---|---|
| 1 | ItemFeedItemsListBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE, INFERRED | PASS | FeedItemsAdapter.java:67–70 inflate of item_feed_items_list, verified in the corpus file. 3-arg called by the batch-68 row-40 2-arg <init> in generated code — correct delegation direction; batch 68 row 40 is the 2-arg <init> of the same Impl family (cross-batch reference coherent). |
| 5 | ItemFeedItemsListBindingImpl.onFieldChange | UNREACHABLE, INFERRED | PASS | D4c flip (69/5). Corpus layout item_feed_items_list.xml: no `<data>`, 0 variables, 0 expressions. Include check + zero-hit grep as above. Phase 1c D4c annotation present, superseding the "Still OPEN" text. |
| 6 | ItemFeedItemsListBindingImpl.setVariable | UNREACHABLE, INFERRED | PASS | D4c flip (69/6), precedence over D4d correctly applied. Same preconditions as row 5. |
| 11 | ItemLogListBindingImpl.executeBindings | REACHABLE, INFERRED | PASS | Row-9 construction anchor verified: LogAdapter.java:51 inflate of item_log_list (corpus file). Rebind after generated invalidateAll, INFERRED, correctly stated. |
| 14 | ItemLogListBindingImpl.onFieldChange | UNREACHABLE, INFERRED | PASS | D4c flip (69/14). Corpus layout item_log_list.xml: no `<data>`, 0 variables, 0 expressions; LogAdapter uses fields only, as cited. Phase 1c D4c annotation present. |
| 15 | ItemLogListBindingImpl.setVariable | UNREACHABLE, INFERRED | PASS | D4c flip (69/15), precedence over D4d correctly applied. Same preconditions as row 14. |
| 16 | ItemPeersListBinding.<init> | REACHABLE, INFERRED | PASS | PeerListAdapter.java:62–66 inflate of item_peers_list (call spans :62–65, blank :66 — the cited range covers it), verified in the corpus file. Abstract ctor via Impl <init> (rows 18–19), INFERRED, correctly stated. |
| 21 | ItemPeersListBindingImpl.hasPendingBindings | OPEN, — | PASS | OPEN correct per D4f (69/21 is in the D4f stay-OPEN list). Zero hits in the grep re-run (including executePendingBindings); named resolver correctly stated. D4c correctly not applied. |
| 23 | ItemPeersListBindingImpl.onFieldChange | UNREACHABLE, INFERRED | PASS | D4c flip (69/23). Corpus layout item_peers_list.xml: no `<data>`, 0 variables, 0 expressions. Include check + zero-hit grep as above. Phase 1c D4c annotation present. |
| 24 | ItemPeersListBindingImpl.setVariable | UNREACHABLE, INFERRED | PASS | D4c flip (69/24), precedence over D4d correctly applied. Same preconditions as row 23. |
| 26 | ItemTorrentContentFileBindingImpl.<clinit> | REACHABLE, INFERRED | PASS | TorrentContentFilesAdapter.java:76 inflate of item_torrent_content_file, verified in the corpus file. First-reference class-init, INFERRED, correctly stated. |
| 31 | ItemTorrentContentFileBindingImpl.invalidateAll | REACHABLE, INFERRED | PASS | "Called by the generated Impl constructor on the row-27 construction" — consistent with the D4e standing basis for batches 65–70; TorrentContentFilesAdapter.java:76 anchor as row 26. |
| 32 | ItemTorrentContentFileBindingImpl.onFieldChange | UNREACHABLE, INFERRED | PASS | D4c flip (69/32). Corpus layout item_torrent_content_file.xml: no `<data>`, 0 variables, 0 expressions. Include check + zero-hit grep as above. Phase 1c D4c annotation present. |
| 33 | ItemTorrentContentFileBindingImpl.setVariable | UNREACHABLE, INFERRED | PASS | D4c flip (69/33), precedence over D4d correctly applied. Same preconditions as row 32. |
| 36 | ItemTorrentDownloadableFileBindingImpl.<init>(DataBindingComponent,View) | REACHABLE, INFERRED | PASS | DownloadableFilesAdapter.java:60 inflate of item_torrent_downloadable_file (call starts :59), verified in the corpus file. Mapper result, INFERRED, correctly stated. This row is the head of the binding whose onFieldChange/setVariable complete the D4c pair as batch 70 rows 1–2 — cross-batch note in the batch 70 file is coherent. |

## Totals
- Checked: 15. PASS: 15. FAIL: 0.

## Proposed corrections
None. No label, confirmed_by, or citation in the checked rows needs changing.
