# Spot-check — LibreTorrent batch 66 (Phase 2)

- Source file checked (read-only, NOT edited): `~/workspace/overnight/stream-A/work/batch66-merge-ready.md`
- Branch: work-2026-10-31, repo bugfixops/ground-truth-results. No pushes, no edits to any merge-ready file.
- Method: re-derived each checked row from already-fetched local source (no connector fetch needed, so no 429). Build/sampler/C1: not run (not this task).
- Batch totals re-verified from the label column: 40 rows, sequence 1–40 intact, 29 REACHABLE / 1 UNREACHABLE / 10 OPEN — matches the Phase 1c header (OPEN: 5, 7, 8, 10, 12, 17, 21, 24, 29, 34).
- Conventions (D4a/D4d/D4f/D4g/D4i) were applied as recorded in `~/workspace/overnight/stream-A/DECISIONS.md`; no convention was decided here.
- IMPORTANT: both FAILs below are rationale-text defects. No checked LABEL is wrong.

## Rows checked (9)
Sample rows 1, 6, 11, 16, 21, 26, 31, 36, plus Phase 1c flips 21, 34 (D4d).

## Verdicts

| Row | Method | Label in file | Verdict | Evidence |
|---|---|---|---|---|
| 1 | FragmentDetailTorrentBindingImpl.<clinit> | REACHABLE, INFERRED | PASS | DetailTorrentFragment.java:150 inflate of fragment_detail_torrent (832-line fetch, verified). fragment_detail_torrent.xml:22 lines, includes detail_torrent_appbar at :10–12 and declares no `<data>` variable — both verified in the corpus layout. First-use class-init, INFERRED, correctly stated. |
| 6 | FragmentDetailTorrentBindingImpl.invalidateAll | REACHABLE, INFERRED | PASS | Same :150 inflate anchor as row 1. invalidateAll REACHABLE standing for batches 65–70 under D4e (DECISIONS.md: "Already-REACHABLE invalidateAll rows in batches 65–70 stand"); "Framework rebind trigger on binding creation" is consistent with that basis. |
| 11 | FragmentDetailTorrentFilesBinding.<init> | REACHABLE, INFERRED | PASS | DetailTorrentFilesFragment.java:114 inflate, :201 setViewModel (543-line fetch, verified). fragment_detail_torrent_files.xml declares viewModel (:8) and binds viewModel.info.metaInfo.fileCount at :31 and :39 — both verified in the corpus layout. Abstract ctor via Impl super-call, INFERRED, correctly stated. |
| 16 | FragmentDetailTorrentFilesBindingImpl.executeBindings | REACHABLE, INFERRED | PASS | Same :114/:201 anchors as row 11; rebind after inflate + setViewModel, INFERRED, correctly stated. |
| 21 | FragmentDetailTorrentFilesBindingImpl.setVariable | OPEN, — | FAIL (rationale only; label correct) | Label OPEN correct per D4d (listed in DECISIONS.md D4d flips, 66/21). Row text ends "Generated dispatch point behind binding.setViewModel(:201)" — the backwards wording D4d rejects (setVariable CALLS the typed setter, not vice versa). Anchors themselves verified as row 11. |
| 26 | FragmentDetailTorrentInfoBindingImpl.<init>(DataBindingComponent,View) | REACHABLE, INFERRED | PASS | DetailTorrentInfoFragment.java:100 inflate, :105 setViewModel (324-line fetch, verified); DetailTorrentViewModel.java reassigns info at :134 and mutableParams at :137 (verified). Mapper-instantiated ctor, INFERRED, correctly stated. |
| 31 | FragmentDetailTorrentInfoBindingImpl.onChangeViewModelInfo | REACHABLE, INFERRED | PASS | Same :100/:105 anchors as row 26; layout binds viewModel.info.* throughout (corpus layout fragment_detail_torrent_info.xml declares viewModel, 15 `@{` expressions, verified in substance). Fires on observed-info change, INFERRED, correctly stated. |
| 34 | FragmentDetailTorrentInfoBindingImpl.setVariable | OPEN, — | FAIL (rationale only; label correct) | Label OPEN correct per D4d (listed in DECISIONS.md D4d flips, 66/34). Row text ends "Generated dispatch point behind binding.setViewModel(:105)" — the backwards D4d-rejected wording, as row 21. |
| 36 | FragmentDetailTorrentInfoBindingImpl$1.<init> | REACHABLE, INFERRED | PASS | Same :100/:105 anchors as row 26. D4g standing list includes 66/36–39 (same inverse-listener family). The row correctly notes "$1/$2 numbering is by generated-source order, NOT bytecode-confirmed". |

## Totals
- Checked: 9. PASS: 7. FAIL: 2 (both rationale-only; 0 label errors).

## Proposed corrections (for the coordinator; labels unchanged)
- Rows 21, 34: replace the trailing "Generated dispatch point behind binding.setViewModel(:…)" sentence with the D4d direction: setVariable CALLS the typed setter, so the printed setViewModel call is zero evidence setVariable ran; no printed `.setVariable(` call for this binding, so the row stays OPEN.
