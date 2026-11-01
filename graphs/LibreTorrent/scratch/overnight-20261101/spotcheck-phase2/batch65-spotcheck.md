# Spot-check — LibreTorrent batch 65 (Phase 2)

- Source file checked (read-only, NOT edited): `~/workspace/overnight/stream-A/work/batch65-merge-ready.md`
- Branch: work-2026-10-31, repo bugfixops/ground-truth-results. No pushes, no edits to any merge-ready file.
- Method: re-derived each checked row from already-fetched local source (no connector fetch needed, so no 429). Build/sampler/C1: not run (not this task).
- Batch totals re-verified from the label column: 40 rows, sequence 1–40 intact, 29 REACHABLE / 3 UNREACHABLE / 8 OPEN — matches the Phase 1c header (OPEN: 3, 6, 11, 16, 22, 27, 33, 38).
- Conventions (D4a/D4b/D4d/D4f) were applied as recorded in `~/workspace/overnight/stream-A/DECISIONS.md`; no convention was decided here.
- IMPORTANT: every FAIL below is a rationale-text defect. No checked LABEL is wrong.

## Rows checked (11)
Sample rows 1, 6, 11, 16, 21, 26, 31, 36, plus Phase 1c flips 3, 16, 27, 38 (D4d).

## Verdicts

| Row | Method | Label in file | Verdict | Evidence |
|---|---|---|---|---|
| 1 | FragmentAddTorrentFilesBindingImpl.onChangeViewModelMutableParams | REACHABLE, INFERRED | PASS | AddTorrentFilesFragment.java:81 inflate, :135 setViewModel (197-line fetch, verified). fragment_add_torrent_files.xml declares viewModel and binds viewModel.info.fileCount (:25/:49/:57) and viewModel.mutableParams.storageFreeSpace (:33) — all verified in the corpus layout. AddTorrentMutableParams.java: extends BaseObservable (:31), ObservableField dirPath (:37), @Bindable getters at :65/:82/:94/:106/:118/:130/:142 — all verified. AddTorrentViewModel.java mutableParams setters (:227/:235/:344/:357/:358) and info.set (:242/:293/:331) verified. |
| 3 | FragmentAddTorrentFilesBindingImpl.setVariable | OPEN, — | FAIL (rationale only; label correct) | Label OPEN correct per D4d (listed in DECISIONS.md D4d flips, 65/3). But the row text ends "Generated dispatch point behind binding.setViewModel(:135)" — the exact backwards wording DECISIONS.md D4d quotes as wrong ("setVariable is the generated dispatch point behind binding.setViewModel") and overrides: setVariable CALLS the typed setter, not vice versa. As printed, the row argues for the old REACHABLE label. |
| 6 | FragmentAddTorrentInfoBinding.getViewModel | OPEN, — | PASS (with note) | Label OPEN correct per D4a standing list (65/6). The row's first rationale sentence ("generated executeBindings reads the mViewModel field, not the getter") already agrees with D4a, and the 252-file grep (0 getViewModel hits) is on file. Note: the row's later conditional ("if the merger adopts the executeBindings-read-path rule, this flips to REACHABLE") is now superseded by D4a's field-read adoption, recorded in the Phase 1c header; the conditional text was not cleaned up. |
| 11 | FragmentAddTorrentInfoBindingImpl.hasPendingBindings | OPEN, — | PASS | Label OPEN correct per D4f (65/11). 252-file grep: 0 hasPendingBindings / 0 executePendingBindings hits; named resolver (printed generated/library rebind body) correctly stated, no UNREACHABLE claimed. |
| 16 | FragmentAddTorrentInfoBindingImpl.setVariable | OPEN, — | FAIL (rationale only; label correct) | Label OPEN correct per D4d (65/16). Row text ends "Generated dispatch point behind binding.setViewModel(:103)" — the same backwards wording as row 3, rejected by D4d. Anchors themselves verified: AddTorrentInfoFragment.java:93 inflate, :103 setViewModel (244-line fetch). |
| 21 | FragmentAddTorrentInfoBindingLargeLandNotouchImpl.executeBindings | REACHABLE, INFERRED | PASS | D4b all-configurations gate adopted in DECISIONS.md: a config-qualified Impl on a matching device is REACHABLE. Anchors verified: AddTorrentInfoFragment.java:93/:103 as row 16; variant layouts layout-large-land-notouch and layout-sw600dp-land fragment_add_torrent_info are byte-identical in the local fetch (same md5 763a6a719aae9c525a970736e4545321). |
| 26 | FragmentAddTorrentInfoBindingLargeLandNotouchImpl.setLifecycleOwner | UNREACHABLE, INFERRED | PASS | Reason no_trigger_in_app. Verified: sole `.setLifecycleOwner(` hit in the whole 252-file corpus is CreateTorrentDialog.java:186 (DialogCreateTorrentBinding, not this binding); AddTorrentInfoFragment.java contains no setLifecycleOwner call; 0 LiveData hits in any corpus layout. The row itself flags the revert condition (merger requiring a printed library body for the no-framework-trigger premise) and the variant-config kind caveat — both correctly stated, and the label stands under D4b either way. |
| 27 | FragmentAddTorrentInfoBindingLargeLandNotouchImpl.setVariable | OPEN, — | FAIL (rationale only; label correct) | Label OPEN correct per D4d (65/27). Row text ends "Generated dispatch point behind binding.setViewModel(:103), for the configuration-selected variant" — the backwards D4d-rejected wording, as rows 3 and 16. |
| 31 | FragmentAddTorrentInfoBindingSw600dpLandImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE, INFERRED | PASS | Same anchors as row 21 (AddTorrentInfoFragment.java:93/:103; byte-identical variant layouts). 3-arg called by 2-arg generated ctor, correctly stated. |
| 36 | FragmentAddTorrentInfoBindingSw600dpLandImpl.onFieldChange | REACHABLE, INFERRED | PASS | Same anchors as row 21; variable set via printed typed setter (:103) + layout binds viewModel observables + printed inflate satisfies the D4i standing rule (65/36 is in the D4i standing list). |
| 38 | FragmentAddTorrentInfoBindingSw600dpLandImpl.setVariable | OPEN, — | FAIL (rationale only; label correct) | Label OPEN correct per D4d (65/38). Row text ends "Generated dispatch point behind binding.setViewModel(:103), for the configuration-selected variant" — the backwards D4d-rejected wording, as rows 3, 16, 27. |

## Totals
- Checked: 11. PASS: 7. FAIL: 4 (all rationale-only; 0 label errors).

## Proposed corrections (for the coordinator; labels unchanged)
- Rows 3, 16, 27, 38: replace the trailing "Generated dispatch point behind binding.setViewModel(:…)" sentence with the D4d direction: in generated code setVariable CALLS the typed setter, so the printed setViewModel call is zero evidence setVariable ran; no printed `.setVariable(` call and no `bind:` pass-through for this binding is printed, so the row stays OPEN.
- Row 6 (optional cleanup): qualify the read-path conditional as superseded by D4a field-read adoption.
