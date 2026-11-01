# Spot-check — batch 59 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (7)

- 59/2 ActivityFilemanagerDialogBindingImpl.hasPendingBindings — REACHABLE INFERRED — FAIL-prose (label and confirmed_by correct per L3 D17: greps/L3/hasPendingBindings_appjava.txt 0 hits + greps/L3/viewdatabinding_rebind_print.txt rendered L686 query; same print verification and version caveat as 58/32). Stale prose: "stays OPEN".
- 59/5 ActivityFilemanagerDialogBindingImpl.setVariable — UNREACHABLE no_trigger_in_app INFERRED — PASS. Per L3 D15: greps/L3/setVariable_appjava.txt 0 hits in 281 app-Java files + greps/L3/includes_full.txt (only variable pass-through is app:viewModel to @layout/add_torrent_info; no include targets this binding's layout); printed setViewModel at FileManagerDialog:143 is zero evidence setVariable ran (D4d direction). Work prose records the Phase 1c D4d decision history ("[Phase 1c 2026-11-01, DECISIONS.md D4d (setVariable direction): REACHABLE -> OPEN. In generated code setVariable CALLS the typed setter, so the printed setViewModel call is zero evidence that setVariable ran; prior REACHABLE rationale superseded by D4d.]") — that is a dated decision record, not a present-tense assertion that the row is OPEN, and the Phase 3 note is appended; no "stays OPEN" sentence is present. PASS.
- 59/8 ActivityLogBinding.getViewModel — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose (label, kind, confirmed_by correct per L3 D14: greps/L3/getters_appjava.txt 0 hits + greps/L3/getters_broad.txt 0 hits; LogActivity:94 calls setViewModel only). Stale prose: "stays OPEN under convention (v-field)".
- 59/13 ActivityLogBindingImpl.hasPendingBindings — REACHABLE INFERRED — FAIL-prose (label and confirmed_by correct per L3 D17, same print verification and version caveat as 58/32). Stale prose: "stays OPEN".
- 59/17 ActivityLogBindingImpl.setVariable — UNREACHABLE no_trigger_in_app INFERRED — PASS. Per L3 D15 (same basis as 59/5; printed setViewModel at LogActivity:94 is zero evidence setVariable ran under D4d). Work prose is the same dated D4d decision history as 59/5, with no "stays OPEN" sentence; Phase 3 note appended. PASS on the same basis as 59/5.
- 59/22 AddTorrentInfoBinding.getViewModel — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose (label, kind, confirmed_by correct per L3 D14: getters greps 0 hits; AddTorrentInfoBinding is the CHILD binding passed app:viewModel by its parent include; that pass-through calls child setVariable, not this getter). Stale prose: "stays OPEN under convention (v-field)".
- 59/27 AddTorrentInfoBindingImpl.hasPendingBindings — REACHABLE INFERRED — FAIL-prose (label and confirmed_by correct per L3 D17, same print verification and version caveat as 58/32). Stale prose: "stays OPEN".

## Sample rows (8)

- 59/1 ActivityFilemanagerDialogBindingImpl.executeBindings — REACHABLE INFERRED — PASS. R1: FileManagerDialog.java:142 setContentView(activity_filemanager_dialog) + :143 setViewModel; executeBindings is the generated lifecycle callback for the binding created there.
- 59/6 ActivityFilemanagerDialogBindingImpl.setViewModel — REACHABLE INFERRED — PASS. R1: FileManagerDialog.java:143 `binding.setViewModel(viewModel)` dispatches to this Impl method (generated dispatch, hence INFERRED).
- 59/11 ActivityLogBindingImpl.\<init\>(DataBindingComponent,View,Object[]) — REACHABLE INFERRED — PASS. R2: generated 2-arg ctor delegates to this 3-arg ctor (generated code, unprinted).
- 59/16 ActivityLogBindingImpl.onFieldChange — REACHABLE INFERRED — PASS. R2: setViewModel printed (:94) binds observables (mutableParams.logging two-way binding, activity_log.xml); onFieldChange is the generated callback; INFERRED (generated dispatch). Consistent with L3's D16 analysis: unlike the no-\<data\> layouts (e.g. 58/34, 60/11), this layout HAS a bound variable and observables.
- 59/21 AddTorrentInfoBinding.\<init\> — REACHABLE INFERRED — PASS. R3: super-call of AddTorrentInfoBindingImpl ctor, reached via AddTorrentInfoFragment.java:93 inflate + :105 binding.info access.
- 59/26 AddTorrentInfoBindingImpl.executeBindings — REACHABLE INFERRED — PASS. R3: generated lifecycle callback for the included binding created at :93.
- 59/31 AddTorrentInfoBindingImpl.onFieldChange — REACHABLE INFERRED — PASS. R3: setViewModel printed (:103) binds observables (info + mutableParams, add_torrent_info.xml); onFieldChange is the generated callback; INFERRED.
- 59/36 AddTorrentInfoBindingImpl$2.\<init\> — REACHABLE INFERRED — PASS. REACHABLE via two-way inverse listener; fresh this pass: add_torrent_info.xml declares exactly 5 two-way bindings (@={viewModel.mutableParams.name, sequentialDownload, startAfterAdd, ignoreFreeSpace, firstLastPiecePriority} on editable text and checkable views), and the plan contains exactly 5 $N rows of this family.

Totals: checked 15 (7 changed + 8 sample-only) — PASS 10, FAIL-prose 5, FAIL-label 0.
