# Spot-check — batch 11 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). This batch file contains only 9 rows, so sample rows 11, 16, 21, 26, 31, 36 are ABSENT (not checked, not counted). No work file edited.

## Changed rows (0)

None.

## Sample rows (2 present)

- 11/1 SettingsFragment.newInstance — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition SettingsFragment.java:63-70; no printed app caller in the files printed in this pass.
- 11/6 AddTagButton.\<init\>(Context,AttributeSet,int) — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition AddTagButton.java:49-56; only the 1-arg construction is printed (TorrentTagsList.java:79); no printed XML tag and no printed 3-arg construction.

## Absent sample rows (not counted)

11, 16, 21, 26, 31, 36 — no such rows in this 9-row batch file.

Totals: checked 2 (0 changed + 2 sample-only) — PASS 2, FAIL-prose 0, FAIL-label 0.
