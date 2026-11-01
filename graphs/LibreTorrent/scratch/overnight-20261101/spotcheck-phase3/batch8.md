# Spot-check — batch 8 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

All eight cite the complete-tree grep 2026-11-01 (SHA 110b8bad, greps/batch5-9-complete-tree-grep.txt): zero direct app-code calls to the named class's (inflate|bind) across the complete app Java tree, plus a saved bare-class-name grep.

- 8/1 FragmentDetailTorrentInfoBinding.bind(View) — UNREACHABLE no_trigger_in_app INFERRED — PASS.
- 8/6 FragmentDetailTorrentInfoBinding.inflate(LayoutInflater,Object) — UNREACHABLE no_trigger_in_app INFERRED — PASS.
- 8/11 FragmentDetailTorrentPeerListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object) — UNREACHABLE no_trigger_in_app INFERRED — PASS.
- 8/16 FragmentDetailTorrentPiecesBinding.inflate(LayoutInflater,ViewGroup,boolean) — UNREACHABLE no_trigger_in_app INFERRED — PASS.
- 8/21 FragmentDetailTorrentStateBinding.inflate(LayoutInflater) — UNREACHABLE no_trigger_in_app INFERRED — PASS.
- 8/26 FragmentDetailTorrentTrackerListBinding.bind(View,Object) — UNREACHABLE no_trigger_in_app INFERRED — PASS.
- 8/31 FragmentFeedBinding.bind(View) — UNREACHABLE no_trigger_in_app INFERRED — PASS.
- 8/36 FragmentFeedBinding.inflate(LayoutInflater,Object) — UNREACHABLE no_trigger_in_app INFERRED — PASS.

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
