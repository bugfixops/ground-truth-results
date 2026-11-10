# Aegis 3.4.2: method-level trigger graph (schema 2)

How every method of **Aegis** is triggered, in the standard configuration: the instrumented debug build (`beemdevelopment/Aegis@v3.4.2`, commit `619c1ab13cdd`, APK sha256 `0855ee49...`), an API 27 emulator, permissions and fixtures as in `final_java_only`. Labels follow `handoff/SCHEMA_V2.md`: REACHABLE or UNREACHABLE, ENV and STATE gates, edge classes (explicit, standard, non-standard), and how each label was confirmed.

## What is in this folder

| File | What it is |
|---|---|
| `aegis_trigger_graph.json` | pages, methods, `verdict`, `labels` (per-method fields), `edges` (with `edge_class`, `env_kinds`, `state_kinds`, stable ids), `paths` (verified paths only), `verification` (counts) |
| `methods.csv` | one row per method: verdict, UNREACHABLE reason, ENV and STATE kinds and texts, edge classes on the best route, whether an explicit/standard-only route exists, how the label was confirmed, path status, the derived best route (`shortest_path`, `route_edge_ids`), and the full JVM class and descriptor (`jvm_class`, `jvm_descriptor`; the `method` key adds a package prefix only where simple class names clash) |
| `../verification.csv` | the audit log: one row per label, edge or path that was checked, with result, how, and where (file:line) |
| `sanity_check.csv` | tool coverage (Monkey / APE, API 27) next to the labels; a one-way check only, it never sets a label |
| `aegis_trigger_graph.html`, `build_report.txt` | the viewer and the validation report |

## Numbers

- **2995 methods**, **12 pages** (including pseudo pages), **6362 edges**. Verdicts: **2521 REACHABLE**, **474 UNREACHABLE**.
- UNREACHABLE by reason: branch_never_taken 3, closed_by_api_level 1, closed_by_configuration 3, framework_never_calls 31, no_trigger_in_app 436.
- ENV gates (methods): hardware 78, other 243, other_app 544, system_event 18, time 7. STATE gates (methods): data 144, file 16, session 79, settings 96. Methods with no gate: 1457.
- Edge classes: explicit 5215, non_standard 98, page 22, standard 1027. Non-standard edges: 98 (Dagger / Hilt dependency injection: the library makes the link to the generated component; JDK library: HashSet.removeAll (AbstractSet.removeAll) reaches equals through its contains branch (JDK source not on disk); intent resolved by action name: the system matches the panic app action info.guardian).
- 275 reachable methods have a non-standard edge on their best route; 523 have no explicit-or-standard-only route at all.
- Labels confirmed by: INFERRED 2694, SOURCE 301 (SOURCE: every edge of the best route cites a source line, in the app or in the Android 8.1 / library source; INFERRED: some edge rests on inference or on another app).

## How much to trust it

Verification log (`verification.csv`), counts of what was checked and found:

| Checked | Rows | Correct | Errors found (fixed) | Unclear |
|---|---:|---:|---:|---:|
| labels | 558 | 542 | 13 | 3 |
| edges (framework and other claims read against source) | 26 | 26 | 0 | 0 |
| paths (stratified sample, read step by step) | 25 | 14 | 8 | 3 |

Device replay on the emulator (API 27): 0 of 24 routes reached their target method; 0 of these ran the whole script and are `DEVICE_OK`. The other routes are unclear (not reached, script stopped, or unscriptable), never wrong; see `../device/results.csv`.
1 further replayed route(s) reached their target in run 42560435293-1 but are not counted above: the graph's best route changed after that run, so the DEVICE row was dropped (device row rule, `tools_dev/device_rows.py`); the method keeps its static label. The run total stays in `../device/results.csv`.

Path status over all reachable methods: SOURCE_OK 2, UNCHECKED 2518, WRONG 1.
The rows are the items that were individually checked, not a random sample of all labels; see the notes below for how they were chosen and what the unclear rows wait for.

Edges whose evidence is not a source line (893 of 6362): E5b266140 (AegisApplication.<init> -> Hilt_AegisApplication.onCreate); Ed430de74 (Hilt_AegisApplication.generatedComponent -> Hilt_AegisApplication$1.get); E1e4b62ae (AegisActivity.onCreate -> Hilt_AegisActivity$1.onContextAvailable); Ed3b2fc19 (Hilt_AegisActivity.generatedComponent -> DaggerAegisApplication_HiltComponents_SingletonC$SingletonCImpl.retainedComponentBuilder); E1c3ead1c (Hilt_AegisActivity.generatedComponent -> DaggerAegisApplication_HiltComponents_SingletonC$ActivityRetainedCBuilder.build); E9eaaba0b (Hilt_AegisActivity.generatedComponent -> DaggerAegisApplication_HiltComponents_SingletonC$ActivityRetainedCImpl.activityComponentBuilder); E9e40d82d (Hilt_AegisActivity.generatedComponent -> DaggerAegisApplication_HiltComponents_SingletonC$ActivityCBuilder.activity); E3c923e18 (Hilt_AegisActivity.generatedComponent -> DaggerAegisApplication_HiltComponents_SingletonC$ActivityCBuilder.build); E983da919 (AegisApplicationBase.onCreate -> AegisApplicationBase$AppLifecycleObserver.onStateChanged); E313f4f87 (S_PROCESS -> VaultLockReceiver.onReceive); Ed3c98a2a (S_PROCESS -> QsTileRefreshReceiver.onReceive); E436827e4 (MainActivity.onStart -> AegisActivity.onResume) ...

Sanity check against tool coverage (never used to set a label): 751 methods ran in the 1-hour Monkey / APE runs on API 27; **0** of them are labelled UNREACHABLE.

Aegis final build (V3-corrected):
2995 methods, 2537 REACHABLE / 458 UNREACHABLE, 6430 edges,
errors 0, warnings 0. Final route table (post-fix redraw, seed
20261025): 25 routes, 1093 steps, 446 distinct edges; CORRECT 13
/ WRONG 1 / UNCLEAR 11; fixed 2 (AndOtp, Stratum); distinct error
rate 3/14 = 0.2143; table-formula rate 3/16 = 0.1875. CI SUMMARY
at the final commit is pending (coordinator gate); no CI count
is claimed here.

## What the re-audit changed (compared with the schema 1 graph)

Re-audit of November 2026 (rounds of W2 to W7, see handoff/MUSE_REAUDIT_SUMMARY.md):

- Baseline (W2): the onboarding is passed and a password-protected vault holds two default TOTP entries; 12 gate texts the baseline satisfies are cleared, and the four intro pages are setup-only.
- Launcher start (W3): MainActivity.onStart opens the unlock screen again (MainActivity.java:942-977), so unlock routes no longer start from the screen-off broadcast (env on best routes 1,613 to 218).
- Impossible calls (W4): DatabaseImporter.readFromApp never dispatches to the nine importers without direct import; their getAppPath methods are UNREACHABLE (Aegis-16).
- Library class (W5): ESR_CREATION is on; settings sub-pages opened by header rows count as standard navigation (Q7).
- Outside data (W6): the old single-group vault format and the document-picker backup targets are env (Aegis-46, Aegis-47); picker results of the import variants are env.

- The schema 1 graph was converted to schema 2 and then re-audited
  batch by batch (batches 14-42 in AGENT_NOTES, followed by the
  finish-run C1-C3 work and this turn's V3 correction). Labels and
  edges now rest on printed app source; bytecode
  (`auto_calls.json`, `javap`) is INFERRED evidence for generated
  and library code only, never a substitute for reading the app
  source around a guard.
- Check 2 was driven to zero, including the two edges that cited
  `services/LaunchScannerTileService.java` as "file not held": the
  file exists under the Aegis source tree and the citations were
  rewritten in the form passing Aegis citations use, with the lines
  printed (C1).
- The route checker reads every step against printed source,
  including if/catch/for conditions. Where the printed source
  showed a branch crossing (a step following an edge the guard
  forbids), the graph was fixed rather than the verdict bent: the
  toolbar lock-icon edge was separated from the Settings step
  (batch 40), and the intro Next/Previous transitions were rebuilt
  on page states (S_INTRO_WELCOME through S_INTRO_DONE) so the
  escape route walks Welcome, Picker, Setup, Done, then
  onDonePressed (batch 41).
- Structural ERROR steps that no single edge could express were
  fixed with variant nodes reached only by the producer chain (the
  `MainActivity.doShortcutActions@SCAN` technique), and the
  selectIcon path was split the same way so that distinct caller
  chains no longer share one node. Tools were never edited to make
  a route pass.
- The importer decrypt paths were wired from printed source:
  reflection CALL edges from `DatabaseImporter.create` to each
  importer constructor, the password-dialog listener chains through
  `Dialogs.lambda$showTextInputDialog$7`, the PBKDF/Argon2 task
  chains, and the per-importer decrypt overloads that genuinely
  have no trigger (labelled UNREACHABLE `no_trigger_in_app` from
  source, not from absence alone). A decrypt edge that re-printing
  proved false (the Stratum file-path fallback edge) was removed
  rather than defended; the correction changed no label.
- Generated code is labelled as generated code: the Glide
  option/request clusters (no app-source reference to GlideApp,
  GlideRequest or GlideOptions in the app tree grep), the protobuf
  accessors, and the Dagger/Hilt component families (one
  UNREACHABLE group per kind where no path exists, with the ten
  Hilt methods the tool run reached given explicit paths). STRICT
  mode is on.
- The finish-run importer sequence: the selectIcon split
  (5957 -> 5954 edges), the per-importer @FILE variant chains
  V1–V8 (6326 edges), FreeOTP stage 2 F1–F13 (6366 edges), the
  row-23 @RAW chain (6390 edges), and the vault round's three
  shared deletions (6387 edges). This turn's V3 correction then
  rebuilt the RawSlot chain on the @IMP prefix (I1–I8, L1–L3,
  plus P1/P2 hand edges), giving the V3-corrected final build:
  2995 methods, 2537 REACHABLE / 458 UNREACHABLE, 6430 edges,
  errors 0, warnings 0. Eight checks on the V3-corrected build (corrected copy + re-audit PASS): check 2:
  22 distinct / 0 problems; check 3: 0 flagged; check 4: 4273
  checked / 345 skipped / 168 implicit / 0 mismatches; checks 5–7:
  0; check 8: 0 of 458. CI SUMMARY at the final commit is pending
  (coordinator gate); no CI count is claimed here.

## How the checked paths were chosen

- Sampling command, as actually run: `python3 -I
  tools/verify_sample.py Aegis 30 20261025` on the V3-corrected
  graph (6430 edges), after the last fix and the redraw.
- Final sample size: 25 routes, not 30, because the PLAIN pool
  holds only 2 routes (Hilt_AegisApplication, 2 steps;
  AegisApplication, 1 step) against a quota of 7, as in earlier
  draws. The sample file is the redraw sampler output
  (25 routes, 1093 steps, 446 distinct edges, seed 20261025).
- The final table (new table, independently audit-PASS) covers
  ONLY the final draw: 25 routes judged fresh, every step, with
  no prior verdict carried over except the 23 edge-identical
  carried rows whose verdicts and decisive summaries are carried
  unchanged from the old table (see the new table's Verification
  section; RawSlot re-judged, Auth judged fresh). Tally: CORRECT
  13, WRONG 1, UNCLEAR 11. Fixed (strict: first-draw WRONG ->
  final CORRECT) = 2 (AndOtp, Stratum). Error rates, with the
  counting rule stated: distinct rate = (fixed + wrong) /
  (correct-only + fixed + wrong) = (2 + 1) / (11 + 2 + 1) =
  3/14 = 0.2143; table-formula rate = (fixed + wrong) /
  (CORRECT + fixed + wrong) = (2 + 1) / (13 + 2 + 1) = 3/16 =
  0.1875. UNCLEAR routes are excluded from both rates. Fixed
  routes are already among the CORRECT routes and must not be
  double-counted. The sole WRONG route is
  AuthActivity.lambda$onCreate$3 (36 steps, ENV
  hardware;time): two independent false steps on printed app
  source — step 28 (lock-icon tap impossible on the unencrypted
  vault) and step 35 (biometric-button tap impossible with null
  header slots). RawSlot.getType is UNCLEAR (42 steps, @IMP
  route), not WRONG: every step true on action and operative
  condition, no step false, producer-less type-0 premise. The
  dropped row EditEntryActivity$CustomSvgIcon.<init> (old CORRECT
  + fixed) left on the 9–9 ENV coverage tie and is NOT a 26th
  row. Gate 5 stays FAIL as written under the path-(A)
  exception (identical-list requirement waived only); the
  exception conditions (new-row judging, recompute, correction
  note, stale-guard disposition) are recorded in the new table
  notes. The C3 table rate (5/9) is not comparable as a trend:
  the sample itself changed.
- Dropped rows' verdicts are superseded, not carried over; their
  reasons stay on record in the fix log and the old table (kept
  untouched). The verification log (`verification.csv`, written
  only by `make_verification.py`) has, in its current regenerated
  staging form, one path row per final-sample route (25), 483
  label rows (458 UNREACHABLE + 25 sampled), and 26 edge rows
  (8 variant dispatch edges + 18 FW-SRC citation-representative
  edges) — 534 data rows, 535 lines total. See the counts note
  below for which file each total describes; do not quote the
  superseded 533/25 figures for this file.
- Sample-timing note (NOT dropped; fallback wording verified):
  the log step does not change the sampler's input for Aegis.
  Verification, read-only, in this turn: the sampler
  (`tools/verify_sample.py`, line 36) reads ONLY
  `graphs/<app>/out/methods.csv` for REACHABLE rows — it does not
  read verification.csv; the writer writes ONLY verification.csv
  and never touches out/. The MMEX mechanism (sample drawn
  before the log step, log-step label rows changing the sampler's
  picks) therefore does not transfer to Aegis. The judged routes
  remain current because the writer's path-edge check asserts
  every path edge list equals methods.csv route_edge_ids exactly
  for all 25 rows. (If the merger runs a post-writer sampler
  re-run, its result should be recorded here as evidence; until
  then this paragraph rests on the input/output verification
  above, not on a re-run.)

## What waits for a device (API 27)

- **Re-audit, last real run 42560435293-1 (2026-11-09, API 27).** The sampled routes were re-verified first (Step 3), and the dry run had 0 FAIL. 1 of 25 routes reached its target (6 scripts ran to the end, 16 stopped, 3 are unscriptable); the others are unclear, never wrong. The device route of Salsa20Engine.salsaCore is no longer the best route and could not be replayed again (the re-audit allows two real runs). What is listed below still waits for a device.

- **Device run 41593209101-1 (2026-11-03, Google APIs, API 27, x86).** 1 of 25 routes reached their target method; 1 of them ran the whole script and are now `DEVICE_OK`. The other routes are unclear (not reached, script stopped, or unscriptable), never wrong; the reason for each route is in `handoff/DEVICE_RUN_SUMMARY.md`. What is listed below still waits for a device.

- ENV-gated routes: camera scan (ENV_CAMERA), image-pick import
  (ENV_PICK_IMAGE / ENV_PICKER), QR-code presentation (ENV_QR_CODE),
  biometric success/failure (ENV_BIOMETRIC / ENV_BIOMETRIC_FAIL),
  autofill (ENV_AUTOFILL), backup/restore (ENV_BACKUP / ENV_RESTORE),
  boot and quick-settings tile listening (ENV_BOOT / ENV_QS),
  export result and backup result (ENV_EXPORT_RESULT /
  ENV_BACKUP_RESULT), incoming VIEW/SEND intents (ENV_VIEW /
  ENV_SEND). The device scripts (`device/routes/Aegis/`,
  ROUTES.csv) are the per-route record; this section is the
  summary, not the record. No device result is claimed here: the final-sample device scripts ship in this same push, staged at device/routes/Aegis/ with ROUTES.csv (25 rows: 22 scripted / 3 unscriptable); the cap proposal (3/25 = 12.0%) is pending a user decision, and the pre-fix ROUTES_DRAFT.csv must never be renamed into place as ROUTES.csv.
- Backup agent: with `android:fullBackupOnly="true"` in the
  manifest, a full-backup run on API 27 should show only
  onFullBackup and onRestoreFile running; onBackup, onRestore and
  onQuotaExceeded are UNREACHABLE (INFERRED: BackupAgent source is
  not in fw_src).
- The export dialog's groups filter: the framework filter chain
  (getFilter, performFiltering, publishResults, predicate lambda)
  is REACHABLE from a tool run even though typing is closed by
  `allow_filtering="false"`; the on-device trigger (tap vs dialog
  opening) is unidentified from app source.
- The Glide decode/fetch/cancel/key edges and the Hilt
  fragment/activity component paths are INFERRED (library source
  not read); the backup `createBackup` overloads carry no strategy
  guard, so which strategy runs is a device check.
- Icon-pack and export-entry producer chains, and any route whose
  gate is a STATE with no producer step on the route, need the
  device run to confirm the state is actually produced before the
  gated step.
- Device items still open at C4 time (recorded in AGENT_NOTES, not
  hidden): the CI-side verification-object injection for the
  generated README (see Limits), and any live-dump
  selector/fixture gaps the device scripts flag for the first real
  run. No real emulator run was started by this turn.

## Hazard candidates (from reading the code, not reproduced)

- `SwitchPreference.setChecked(boolean)` ignores its argument and
  always sets the switch on; the stored value is set through the
  androidx initial-value path (INFERRED, androidx source not read).
  Hazard candidate for the security page.
- Full-backup-only manifest flag (see device section above): a
  restore path that assumes onRestore runs would silently never
  execute.
- The export groups filter running despite filtering being disabled
  (see device section above): any export flow that assumes the
  group list is unfiltered is suspect.
- Biometric error/non-match callbacks and the autofill type query
  on the no-autofill fields: framework behaviour the app cannot
  trigger from its own UI, so a device run is the only confirmation
  (see device section above).
- Nothing in this section was reproduced on a device. Each item is
  a reading of the code, labelled as such, and none of them changes
  a label.

## Limits

- The route search is state-blind: it compares env, needs_state
  count and steps, but never checks that a state is produced before
  it is consumed. Producer-chain variant nodes (section 1 above)
  work around this per route; they do not fix the router, and tools
  are not edited in this project.
- Tool coverage, the old generated graphs, and the build's
  REACHABLE count are never evidence. Every label and edge rests
  on printed source, or is marked INFERRED with "source not read"
  where the source (Glide, Hilt, androidx, JDK, protobuf runtime)
  was not read.
- UNREACHABLE consistency flags (a UNREACHABLE method with an
  incoming edge from a caller that is also UNREACHABLE) are not
  contradictions: no flagged method in the list below has a
  REACHABLE or UNRESOLVED caller. The flag list below is carried
  from the batch-22/28/29/30 record; the V3-corrected build has
  warnings 0, so no new flag class arises at C4 time. The reasons
  are as in the current readme (GlideOptions/GlideRequest clusters,
  GoogleAuthProtos accessors, ApkSignaturePin, TrustedIntents,
  EntryAdapter.onItemDismiss, TextDrawable builders, Dialogs
  overloads, NotificationService.serviceMethod) — carried
  unchanged here; the merger updates this list only from a fresh
  post-C4 flag run, never by copying it blindly. Two follow-ups
  recorded in the Stratum correction work (Legacy/Totp suspect
  app-import decrypt edges) are follow-ups, not C3 blockers, and
  are not added to the flag list on this draft's authority.
- One REVIEW line (not a method warning): the NONSTD_HINT regex at
  tools/build_graph.py:61 flags 7 edges (Ed430de74, Ed3b2fc19,
  E1c3ead1c, E9eaaba0b, E4e40d82d, E3c923e18, Ebdc15ea3) whose
  evidence contains the words dagger, library or reflect. Their
  edges are plain FRAMEWORK edges, so they are false positives.
  Not fixed; tools/ is not edited.
- TextDrawable$Builder.rect and TextDrawable$Builder.roundRect
  (batch 28, 2 flags); Dialogs overloads (batch 29, 2 flags);
  NotificationService.serviceMethod (batch 30, 1 flag); batch-30
  open items for a device check (SwitchPreference, full-backup-only
  agent); DropdownCheckBoxes filter (batch 28, INFERRED); ENV-gated
  methods (best route, not tested on a device) — all as in the
  current readme, carried unchanged; see that file for the full
  wordings, which this draft does not re-argue.
- Writer/README gap (C4 decision 2, open, not hidden):
  `make_verification.py` writes only `verification.csv` and never
  touches `out/` (brief section 2.3), so it does not inject the
  `verification` object that `gen_readme_v2.py` reads. Until CI
  injects that object (or the generator is changed to read the
  CSV), a CI-generated README will print "No verification log
  yet" for Aegis even though the CSV exists and is validated.
  Check 5/7 tallies for Aegis are not stated here: they must be
  read from the final CI SUMMARY.txt at merge time, not copied
  from another app or from an intermediate build.
- Open follow-ups, not blockers for this log, as the merger states
  them at C4 time: the stale-guard DEBT on RawSlot tail steps
  34–39 and 41 (see the new table notes); the Legacy/Totp suspect
  edges above. Neither changes a verdict, count, or rate in this
  draft.

Counts note (which file each total describes — merger to confirm
at merge time): 534 data rows / 26 edge rows / 535 lines =
the current regenerated verification.csv in staging
(turn/writer/work/graphs/Aegis/verification.csv, 263,972 bytes,
SHA-256
83c527cad5a03ec8c5e002e2b5177ceee79572e0ec8885133635139cb4074321)
AND the C2 re-audited file (same row/edge counts, different
verdicts/routes/notes). 533 rows / 25 edge rows = the superseded
pre-redraw C4 writer output described in the line-841 C4 logs
entry (before the E9edc8c99 edge-row addition). 535 lines is the
line count including the header for both 534-row files, not a
third total. Do not quote 533/25 for the current file, and do not
quote 534/26 for the superseded file.

## JSON shape (short)

```
{ "schema": 2, "title", "screens": {page: description}, "methods": [...], "verdict": {method: REACHABLE|UNREACHABLE},
  "labels": {method: {unreachable: {kind, text}, env: [{kinds, text}], state: [{kinds, text}], route_edge_classes, explicit_standard_route,
                      confirmed_by, source_ref, path_status}},
  "edges": [ {id, src, dst, kind, edge_class, via, trigger, gui[], guard, reads[], writes[], note, needs_state, state_kinds, env, env_kinds, evidence, class_basis} ],
  "paths": [ {method, edges[], edge_classes, explicit_standard_only, env, state, verified_by, ref} ], "verification": {...} }
```

`src`/`dst` are methods (`Class.method`, overloads as `Class.method(Type,Type)`) or pages (`S_...`). A suffix `@CONTEXT` is the same method or page in a specific context. Edge ids are a hash of the edge content, so they stay stable when other edges change.
