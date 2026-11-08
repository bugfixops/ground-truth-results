# Spot-check — LibreTorrent batch 62 (Phase 2)

- Source file checked (read-only, NOT edited): `~/workspace/overnight/stream-A/work/batch62-merge-ready.md`
- Branch: work-2026-10-31, repo bugfixops/ground-truth-results. No pushes, no edits to any merge-ready file.
- Method: re-derived each checked row from already-fetched local source (no connector fetch needed, so no 429). Build/sampler/C1: not run (not this task).
- Batch totals re-verified from the label column: 40 rows, sequence 1–40 intact, 33 REACHABLE proposed / 0 UNREACHABLE / 7 OPEN — matches the Phase 1c header (OPEN: 4, 9, 15, 30, 35, 37, 39).
- Conventions (D4a/D4d/D4e/D4g) were applied as recorded in `~/workspace/overnight/stream-A/DECISIONS.md`; no convention was decided here.
- IMPORTANT: every FAIL below is a confirmed_by-column or rationale-text defect. No checked LABEL is wrong.

## Rows checked (13)
Sample rows 1, 6, 11, 16, 21, 26, 31, 36, plus Phase 1c flips 4, 30 (D4a), 15, 39 (D4d), 10, 36 (D4e).

## Verdicts

| Row | Method | Label in file | Verdict | Evidence |
|---|---|---|---|---|
| 1 | DialogAddTagBindingImpl$1.<init> | REACHABLE proposed, confirmed_by "—" (INFERRED in a stray extra column) | FAIL (column only; label correct) | Anchors verified: dialog_add_tag.xml sole `@={}` at :27 (local count 1); AddTagDialog.java:128 inflate, :129 setViewModel. Label REACHABLE under D4g is correct, but the table has 4 columns (Method / Proposed label / confirmed_by / Route) and this row inserts an extra "—", so confirmed_by reads "—" instead of INFERRED. Same defect affects all 14 $N rows (1, 2, 17–28); only 1, 21, 26 were in the checked set. |
| 4 | DialogCreateTorrentBinding.getViewModel | OPEN, — | FAIL (rationale only; label correct) | Label OPEN is correct per D4a (listed in DECISIONS.md D4a flips, 62/4) and no printed app caller exists (CreateTorrentDialog.java uses setViewModel :187, never getViewModel). But the row text still reads "Read by generated executeBindings of the Impl created at CreateTorrentDialog:185" — the getter-read mechanism D4a explicitly rejects (executeBindings reads the mViewModel field, not the getter). The row carries no D4a annotation, so as printed it argues for the old label. |
| 6 | DialogCreateTorrentBindingImpl.<init>(DataBindingComponent,View) | REACHABLE proposed, INFERRED | PASS | CreateTorrentDialog.java:185 inflate (561-line fetch), verified locally. |
| 10 | DialogCreateTorrentBindingImpl.invalidateAll | REACHABLE proposed, INFERRED | PASS | D4e flip, listed in DECISIONS.md D4e flips (62/10); Phase 1c header documents it. Row text "No printed caller" is true and does not contradict the ctor-internal D4e basis. Note (not a FAIL): unlike batch 61, no in-row D4e annotation was added; coordinator may add one for consistency. |
| 11 | DialogCreateTorrentBindingImpl.onChangeViewModelBuildProgress | REACHABLE proposed, INFERRED | PASS | CreateTorrentDialog.java:186 setLifecycleOwner, :187 setViewModel, verified. CreateTorrentViewModel.java: buildProgress field :61, setValue :114, postValue :244/:249, getBuildProgress() :131–133 — all verified locally, satisfying the stated revert condition. Dispatch remains generated, hence INFERRED, correctly stated. |
| 15 | DialogCreateTorrentBindingImpl.setVariable | OPEN, — | PASS (with note) | Label OPEN correct per D4d (listed in DECISIONS.md D4d flips, 62/15); Phase 1c header documents it. Row text ("Generic variable dispatch…") is vague but does not assert the backwards direction D4d rejects. Note: aligning this wording to the D4d form used in batch 61 rows 25/39 would remove ambiguity. |
| 16 | DialogCreateTorrentBindingImpl.setViewModel | REACHABLE proposed, INFERRED | PASS | CreateTorrentDialog.java:187 `binding.setViewModel(viewModel)`, verified locally. |
| 21 | DialogCreateTorrentBindingImpl$3.<init> | REACHABLE proposed, confirmed_by "—" (INFERRED in stray extra column) | FAIL (column only; label correct) | Anchors verified: dialog_create_torrent.xml exactly 6 `@={}` at :113, :120, :149, :177, :205, :276 (local count); plan has 12 $N rows for this Impl = 6 classes — D4g count-match. CreateTorrentDialog.java:185/186/187 verified. Defect is the same extra-"—" column defect as row 1. |
| 26 | DialogCreateTorrentBindingImpl$5.onChange | REACHABLE proposed, confirmed_by "—" (INFERRED in stray extra column) | FAIL (column only; label correct) | Same anchors and same column defect as row 21. |
| 30 | DialogErrorBinding.getDetailError | OPEN, — | FAIL (rationale only; label correct) | Label OPEN correct per D4a (listed in DECISIONS.md D4a flips, 62/30). ErrorReportDialog.java:68 inflate, :69 setDetailError verified; no getter call. But row text still reads "Read by generated executeBindings of the Impl created at :68, to bind the detailError set at :69" — the getter-read mechanism D4a rejects, with no D4a annotation in the row. |
| 31 | DialogErrorBindingImpl.<clinit> | REACHABLE proposed, INFERRED | PASS | ErrorReportDialog.java:68 inflate, verified locally (84-line local fetch; line numbers match the file's citation). |
| 36 | DialogErrorBindingImpl.invalidateAll | REACHABLE proposed, INFERRED | PASS | D4e flip, listed in DECISIONS.md D4e flips (62/36); same note as row 10 about the absent in-row annotation. |
| 39 | DialogErrorBindingImpl.setVariable | OPEN, — | PASS (with note) | Label OPEN correct per D4d (listed in DECISIONS.md D4d flips, 62/39); same wording-alignment note as row 15. |

## Totals
- Checked: 13. PASS: 8. FAIL: 5 (all column/rationale-only; 0 label errors).

## Proposed corrections (do NOT edit the merge-ready file here; for the coordinator)
1. Rows 1, 21, 26 (and, unchecked but identically affected, rows 2, 17–20, 22–25, 27, 28): set confirmed_by to INFERRED and delete the stray "—" column so the row matches the 4-column table header.
2. Row 4: replace "Read by generated executeBindings of the Impl created at CreateTorrentDialog:185" with a D4a note: executeBindings reads the mViewModel field, not the getter; no printed app caller; stays OPEN. Label unchanged.
3. Row 30: same replacement, for getDetailError: executeBindings reads the field, not the getter; no printed app caller; stays OPEN. Label unchanged.
4. Optional consistency: add in-row D4e annotations to rows 10 and 36 (as batch 61 rows 21/36 have) and D4d wording alignment to rows 15 and 39.
