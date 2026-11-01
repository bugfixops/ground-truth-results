# Spot-check — LibreTorrent batch 67 (Phase 2)

- Source file checked (read-only, NOT edited): `~/workspace/overnight/stream-A/work/batch67-merge-ready.md`
- Branch: work-2026-10-31, repo bugfixops/ground-truth-results. No pushes, no edits to any merge-ready file. Batch 67 itself was NOT edited by this spot-check (per the task's linkage note, batch 68 row 1 was judged together with batch 67 row 40 in the source files, but no file was changed here).
- Method: re-derived each checked row from already-fetched local source (no connector fetch needed, so no 429). Build/sampler/C1: not run (not this task).
- Batch totals re-verified from the label column: 40 rows, sequence 1–40 intact, 29 REACHABLE / 1 UNREACHABLE / 10 OPEN — matches the Phase 1c header (OPEN: 5, 7, 8, 10, 15, 19, 22, 27, 31, 38).
- Conventions (D4a/D4c/D4d/D4f) were applied as recorded in `~/workspace/overnight/stream-A/DECISIONS.md`; no convention was decided here.
- IMPORTANT: all three FAILs below are rationale-text defects. No checked LABEL is wrong.

## Rows checked (11)
Sample rows 1, 6, 11, 16, 21, 26, 31, 36, plus Phase 1c flips 19, 31 (D4d) and 40 (D4c), plus must-include extras row 7 (D4c-scope question) and row 40.

## Verdicts

| Row | Method | Label in file | Verdict | Evidence |
|---|---|---|---|---|
| 1 | FragmentDetailTorrentPeerListBindingImpl.<clinit> | REACHABLE, INFERRED | PASS | DetailTorrentPeersFragment.java:84 inflate of fragment_detail_torrent_peer_list (202-line fetch, verified); field use only at :124–125/:138/:140–142, no setter — as cited. Corpus layout fragment_detail_torrent_peer_list.xml: 28 lines, no `<data>`, 0 two-way bindings (1 static `@{` dimen) — verified. |
| 6 | FragmentDetailTorrentPeerListBindingImpl.invalidateAll | REACHABLE, INFERRED | PASS | Same :84 anchor as row 1. invalidateAll REACHABLE standing for batches 65–70 under D4e; "Called by the generated Impl constructor on the row-2 construction" is consistent with that basis. |
| 7 | FragmentDetailTorrentPeerListBindingImpl.onFieldChange | OPEN, — | PASS | OPEN is correctly recorded and D4c was correctly NOT extrapolated to this row: the Phase 1c header states explicitly that only row 40 is listed for batch 67 in DECISIONS.md D4c, and row 7 is left OPEN. DECISIONS.md D4c flip list for batch 67 names only 67/40 — confirmed. Note (not a FAIL): the row body's older conditional text ("under the generic-framework-callback convention this flips to REACHABLE…") predates the D4c scoping and was not cleaned up, but the label and the Phase 1c header are unambiguous, so the row must stay OPEN unless the coordinator separately extends D4c's scope. No extrapolation is made here. |
| 11 | FragmentDetailTorrentPiecesBindingImpl.<clinit> | REACHABLE, INFERRED | PASS | DetailTorrentPiecesFragment.java:71 inflate, :109 setViewModel (143-line fetch, verified). Corpus layout fragment_detail_torrent_pieces.xml declares viewModel — verified. |
| 16 | FragmentDetailTorrentPiecesBindingImpl.invalidateAll | REACHABLE, INFERRED | PASS | Same :71/:109 anchors as row 11. "Called by the generated Impl constructor and by setViewModel" is consistent with the D4e standing basis for batches 65–70. |
| 19 | FragmentDetailTorrentPiecesBindingImpl.setVariable | OPEN, — | FAIL (rationale only; label correct) | Label OPEN correct per D4d (listed in DECISIONS.md D4d flips, 67/19). Row text ends "Called by the generated setViewModel (row 20) to register the viewModel variable" — the backwards direction D4d rejects: setVariable CALLS the typed setter, not vice versa. Anchors verified as row 11. |
| 21 | FragmentDetailTorrentStateBinding.<init> | REACHABLE, INFERRED | PASS | DetailTorrentStateFragment.java:73 inflate, :86 setViewModel (88-line fetch, verified). Corpus layout fragment_detail_torrent_state.xml declares viewModel — verified. Abstract ctor via Impl <init>, INFERRED, correctly stated. |
| 26 | FragmentDetailTorrentStateBindingImpl.executeBindings | REACHABLE, INFERRED | PASS | Same :73/:86 anchors as row 21; rebind after setViewModel, INFERRED, correctly stated. |
| 31 | FragmentDetailTorrentStateBindingImpl.setVariable | OPEN, — | FAIL (rationale only; label correct) | Label OPEN correct per D4d (listed in DECISIONS.md D4d flips, 67/31). Row text ends "Called by the generated setViewModel (row 32)" — the backwards D4d-rejected direction, as row 19. Anchors verified as row 21. |
| 36 | FragmentDetailTorrentTrackerListBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE, INFERRED | PASS | DetailTorrentTrackersFragment.java:105 inflate (406-line fetch, verified); field use only at :158–159/:172/:174/:176/:180–182, no setter — verified. Corpus layout fragment_detail_torrent_tracker_list.xml: 28 lines, no `<data>` — verified. 3-arg called by row 35 (2-arg), correct direction. |
| 40 | FragmentDetailTorrentTrackerListBindingImpl.onFieldChange | UNREACHABLE, INFERRED | FAIL (rationale only; label correct) | Label UNREACHABLE is correct per D4c: DECISIONS.md D4c flip list names 67/40 (companion of 68/1), and the preconditions hold — layout declares no variable (verified as row 36), TrackersFragment uses fields only (verified as row 36), 0 `.onFieldChange` hits in the 252-file grep, and the D4c include check finds no parent passing a variable. BUT the row body as printed still says "OPEN, not UNREACHABLE" and twice "Still OPEN because the generic-framework-callback convention is undecided… This pass does not decide", and — unlike the batch 68 D4c rows — it carries NO Phase 1c D4c annotation in the row. The row therefore contradicts its own label. The linkage to batch 68 row 1 is correctly noted in the row and in the batch 68 file; batch 67 was not edited here. |

## Totals
- Checked: 11. PASS: 8. FAIL: 3 (all rationale-only; 0 label errors).

## Proposed corrections (for the coordinator; labels unchanged)
- Rows 19, 31: replace the trailing "Called by the generated setViewModel (row …)" sentence with the D4d direction: setVariable CALLS the typed setter, so the printed setViewModel call is zero evidence setVariable ran; no printed `.setVariable(` call for this binding, so the row stays OPEN.
- Row 40: append a Phase 1c D4c annotation in the form used by the batch 68 D4c rows ("PHASE 1c 2026-11-01: D4c applied — OPEN to UNREACHABLE no_trigger_in_app INFERRED (no-variable, no-parent binding; see DECISIONS.md D4c)") and qualify the "OPEN, not UNREACHABLE" / "Still OPEN" sentences as superseded by that decision. Label unchanged. Do NOT extend this correction to row 7: row 7 stays OPEN unless the coordinator separately decides D4c's scope covers it.
