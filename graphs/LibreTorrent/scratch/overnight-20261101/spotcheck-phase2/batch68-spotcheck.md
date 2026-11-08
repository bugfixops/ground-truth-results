# Spot-check — LibreTorrent batch 68 (Phase 2)

- Source file checked (read-only, NOT edited): `~/workspace/overnight/stream-A/work/batch68-merge-ready.md`
- Branch: work-2026-10-31, repo bugfixops/ground-truth-results. No pushes, no edits to any merge-ready file.
- Method: re-derived each checked row from already-fetched local source (no connector fetch needed, so no 429). Build/sampler/C1: not run (not this task).
- Batch totals re-verified from the label column: 40 rows, sequence 1–40 intact, 27 REACHABLE / 9 UNREACHABLE / 4 OPEN — matches the Phase 1c header (9 D4c flips; hasPendingBindings rows left OPEN under D4f).
- Conventions (D4c/D4f) were applied as recorded in `~/workspace/overnight/stream-A/DECISIONS.md`; no convention was decided here.
- D4c evidence base verified as a whole: `~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt` records 0 hits in the 252-file app-Java tree for setVariable, onFieldChange, and hasPendingBindings; `~/workspace/b686970-openclose2-src/include_check_686970.txt` records that no layout in any layout dir includes any of the 13 group layouts (only `<include>` targets are toolbar, main_drawer_content, add_torrent_info, detail_torrent_appbar, with zero `bind:` attributes).

## Rows checked (15)
Sample rows 1, 6, 11, 16, 21, 26, 31, 36, plus Phase 1c D4c flips 1, 9, 10, 18, 19, 27, 28, 36, 37. Must-include extra row 1 (judged together with batch 67 row 40) is inside that set; the linkage is noted in the row, and batch 67 was not edited here.

## Verdicts

| Row | Method | Label in file | Verdict | Evidence |
|---|---|---|---|---|
| 1 | FragmentDetailTorrentTrackerListBindingImpl.setVariable | UNREACHABLE, INFERRED | PASS | D4c flip, listed in DECISIONS.md D4c flips (68/1). Anchors verified: DetailTorrentTrackersFragment.java:105 inflate, trackerList use :158–182, no setter (406-line fetch). Corpus layout fragment_detail_torrent_tracker_list.xml: no `<data>`. Include check + zero-hit grep as above. Row carries the Phase 1c D4c annotation superseding its "Still OPEN" text, and correctly records the companion linkage: "judge together" with batch 67 row 40 (same binding's onFieldChange); under option U both flip to UNREACHABLE, which is what both files now record. |
| 6 | FragmentFeedBindingImpl.executeBindings | REACHABLE, INFERRED | PASS | Row-4 construction anchor verified: FeedFragment.java:99 inflate of fragment_feed (corpus file). Rebind after generated invalidateAll, INFERRED, correctly stated. |
| 9 | FragmentFeedBindingImpl.onFieldChange | UNREACHABLE, INFERRED | PASS | D4c flip (68/9). Corpus layout fragment_feed.xml: no `<data>`, 0 variables (1 static `@{` expression, consistent with D4c's "static dimen sums" note). Include check + zero-hit grep as above. Phase 1c D4c annotation present. |
| 10 | FragmentFeedBindingImpl.setVariable | UNREACHABLE, INFERRED | PASS | D4c flip (68/10). Same preconditions as row 9; Phase 1c D4c annotation present. Note: D4d would otherwise leave a setVariable row OPEN, but D4c takes precedence here per DECISIONS.md composition — correctly applied. |
| 11 | FragmentFeedItemsBinding.<init> | REACHABLE, INFERRED | PASS | FeedItemsFragment.java:111 inflate of fragment_feed_items, verified in the corpus file. Abstract ctor via Impl <init> (rows 13–14), INFERRED, correctly stated. |
| 16 | FragmentFeedItemsBindingImpl.hasPendingBindings | OPEN, — | PASS | OPEN correct per D4f (68/16 is in the D4f stay-OPEN list). Zero hits in the grep re-run (including executePendingBindings); named resolver (printed generated/library rebind body) correctly stated. D4c correctly not applied to this library-query method. |
| 18 | FragmentFeedItemsBindingImpl.onFieldChange | UNREACHABLE, INFERRED | PASS | D4c flip (68/18). Corpus layout fragment_feed_items.xml: no `<data>`, 0 variables, 0 expressions. Include check + zero-hit grep as above. Phase 1c D4c annotation present. |
| 19 | FragmentFeedItemsBindingImpl.setVariable | UNREACHABLE, INFERRED | PASS | D4c flip (68/19), precedence over D4d correctly applied as row 10. Same preconditions as row 18. |
| 21 | FragmentMainBindingImpl.<clinit> | REACHABLE, INFERRED | PASS | MainFragment.java:119 inflate of fragment_main, verified in the corpus file. First-reference class-init, INFERRED, correctly stated. |
| 26 | FragmentMainBindingImpl.invalidateAll | REACHABLE, INFERRED | PASS | "Called by the generated Impl constructor on the row-22 construction" — consistent with the D4e standing basis for batches 65–70; MainFragment.java:119 anchor as row 21. |
| 27 | FragmentMainBindingImpl.onFieldChange | UNREACHABLE, INFERRED | PASS | D4c flip (68/27). Corpus layout fragment_main.xml: no `<data>`, 0 variables. Include check + zero-hit grep as above. Phase 1c D4c annotation present. |
| 28 | FragmentMainBindingImpl.setVariable | UNREACHABLE, INFERRED | PASS | D4c flip (68/28), precedence over D4d correctly applied as row 10. Same preconditions as row 27. |
| 31 | ItemFeedChannelListBindingImpl.<init>(DataBindingComponent,View) | REACHABLE, INFERRED | PASS | FeedChannelListAdapter.java:82 inflate of item_feed_channel_list, verified in the corpus file. Mapper result, generated, INFERRED, correctly stated. |
| 36 | ItemFeedChannelListBindingImpl.onFieldChange | UNREACHABLE, INFERRED | PASS | D4c flip (68/36). Corpus layout item_feed_channel_list.xml: no `<data>`, 0 variables, 0 expressions; adapter uses fields only, as cited. Include check + zero-hit grep as above. Phase 1c D4c annotation present. |
| 37 | ItemFeedChannelListBindingImpl.setVariable | UNREACHABLE, INFERRED | PASS | D4c flip (68/37), precedence over D4d correctly applied as row 10. Same preconditions as row 36. |

## Totals
- Checked: 15. PASS: 15. FAIL: 0.

## Proposed corrections
None. No label, confirmed_by, or citation in the checked rows needs changing. The batch 68 row 1 / batch 67 row 40 linkage is consistently recorded in both files (row 40's own missing in-row annotation is reported in the batch 67 spot-check, not here).
