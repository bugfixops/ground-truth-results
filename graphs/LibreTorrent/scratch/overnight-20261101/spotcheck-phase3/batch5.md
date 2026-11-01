# Spot-check — batch 5 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

All eight cite the complete-tree grep 2026-11-01 (SHA 110b8bad, greps/batch5-9-complete-tree-grep.txt): zero direct app-code calls to the named class's (inflate|bind) across the complete app Java tree, plus a saved bare-class-name grep. The D29 tension rows (batch 5 rows 19–20, AddTorrentInfoBinding.bind) are NOT sample rows and are not judged here; they are listed in verdicts_applied_table.json as not_flipped_by_user_statement.

- 5/1 ActivityAddTorrentBinding.bind(View) — UNREACHABLE no_trigger_in_app INFERRED — PASS.
- 5/6 ActivityAddTorrentBinding.inflate(LayoutInflater,Object) — UNREACHABLE no_trigger_in_app INFERRED — PASS.
- 5/11 ActivityFilemanagerDialogBinding.inflate(LayoutInflater,ViewGroup,boolean,Object) — UNREACHABLE no_trigger_in_app INFERRED — PASS.
- 5/16 ActivityLogBinding.inflate(LayoutInflater,ViewGroup,boolean) — UNREACHABLE no_trigger_in_app INFERRED — PASS.
- 5/21 AddTorrentInfoBinding.inflate(LayoutInflater) — UNREACHABLE no_trigger_in_app INFERRED — PASS.
- 5/26 DetailTorrentAppbarBinding.bind(View,Object) — UNREACHABLE no_trigger_in_app INFERRED — PASS.
- 5/31 DialogAddFeedChannelBinding.bind(View) — UNREACHABLE no_trigger_in_app INFERRED — PASS.
- 5/36 DialogAddFeedChannelBinding.inflate(LayoutInflater,Object) — UNREACHABLE no_trigger_in_app INFERRED — PASS.

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
