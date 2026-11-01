# Spot-check — LibreTorrent batch 80 (Stream A Phase 2)

- Source file checked: `~/workspace/overnight/stream-A/work/batch80-merge-ready.md` (UNVERIFIED proposal, not a result; not edited).
- Method: each row below was re-derived from already-fetched printed source in `~/workspace/overnight/stream-A/corpus/java/` (no connector fetch needed, no 429, no missing file). No build/sampler/C1 run (not this task).
- Check set: sample rows 1, 6, 11, 16, 21, 26, 31, 36 of the batch's main 40-row table. No dated 2026-11-01 revision note in this file lists a Phase 1 label flip, so no extra changed rows apply.
- Filed labels: all 8 checked rows filed REACHABLE.

## Per-row verdicts

- Row 1 — AddTorrentInfoFragment.lambda$new$1 — PASS. Filed REACHABLE INFERRED. selectTag ActivityResult callback AddTorrentInfoFragment.java:137–148 (first registerForActivityResult in source order); body adds the tag via viewModel.addTag :144. Framework result dispatch unprinted = INFERRED as filed.
- Row 6 — AddTorrentInfoFragment.onCreateView — PASS. Filed REACHABLE INFERRED. Body AddTorrentInfoFragment.java:92–96 (binding inflate :93, returns root :95). Fragment lifecycle dispatch unprinted = INFERRED as filed.
- Row 11 — AddTorrentInfoFragment.showOpenDirErrorDialog — PASS. Filed REACHABLE SOURCE. Body AddTorrentInfoFragment.java:215–231; called from the chooseDir callback at :157 (result not OK / no data branch). Printed call on a printed route = SOURCE as filed.
- Row 16 — AddTorrentInfoFragment$1.onTextChanged — PASS. Filed REACHABLE INFERRED. Empty body AddTorrentInfoFragment.java:112–113; same TextWatcher registration as row 15 (registered :106, onViewCreated). Framework TextWatcher dispatch unprinted = INFERRED as filed.
- Row 21 — AddTorrentInfoFragment$2.onTagRemoved — PASS. Filed REACHABLE INFERRED. Body AddTorrentInfoFragment.java:181–183 (viewModel.removeTag); same tagsListener dispatch as the file notes. Listener dispatch unprinted = INFERRED as filed.
- Row 26 — AddTorrentMutableParams.getSource — PASS. Filed REACHABLE SOURCE. Definition AddTorrentMutableParams.java:45–48; printed callers AddTorrentViewModel.java:269 and :474. Direct printed calls = SOURCE as filed.
- Row 31 — AddTorrentMutableParams.isSequentialDownload — PASS. Filed REACHABLE SOURCE. Definition AddTorrentMutableParams.java:107–110; printed caller AddTorrentActivity.java:209. Direct printed call = SOURCE as filed.
- Row 36 — AddTorrentMutableParams.setIgnoreFreeSpace — PASS. Filed REACHABLE SOURCE. Definition AddTorrentMutableParams.java:136–139; printed caller AddTorrentActivity.java:155. Direct printed call = SOURCE as filed.

## Totals

- Rows checked: 8. PASS: 8. FAIL: 0.

## Proposed corrections

- None. No label or confirmed_by change proposed; the merge-ready file was not edited.
