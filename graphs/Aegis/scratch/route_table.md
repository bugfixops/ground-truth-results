# Aegis — FINAL route table (sample-30 redraw, C3 sample-fix step)

Sample: `python3 -I tools/verify_sample.py Aegis 30 20261025` on the
post-fix graph (fixes 1–4 applied). 25 routes (PLAIN pool 2 vs quota
7, as in the first draw), 694 steps, 353 distinct edges. First-draw
sample (25 routes, 686 steps) kept untouched at
`merger/scratch/sample_30.txt`; this redraw saved at
`merger/scratch/sample_30_final.txt`. Judged fresh, every step,
against printed source by 9 helpers (h1–h9, max 3 routes each, two
staggered waves), with a merger completeness check per report
(step counts match the sample; per-helper arithmetic verified;
every report holds a per-step table with personally printed
file:lines). No prior verdict was carried over: re-drawn routes
were judged on their new dumps.

## Conventions applied (binding)

- Declared configuration: debug build, fresh install, API 27,
  runtime permissions granted only where a route needs them.
- `Aegis-C3-Step8` (coordinator decision, binding, Muse's own,
  for user/Yang review): the STRICT D-C3-10 reading STANDS. A
  loadEntries/vault-load step whose guard demands a producer of
  the loaded vault earlier on the route, with no such producer
  in steps before it, grades UNCLEAR (not CORRECT). The same
  applies to any cross-run state (vault file, installed pack,
  installed app data from an earlier run) with no in-run
  producer. A step depending on an UNCLEAR producer is itself
  UNCLEAR. UNCLEAR routes are excluded from the error-rate
  denominator under either reading, so this choice hides no
  WRONG route — but the final CORRECT count (4) must not be
  inflated by convention.
- `Aegis-C3-Exit` (merger decision, Muse's own): ExitActivity
  .onCreate is WRONG by design, route-14 class. It was NOT
  redrawn, so it does not appear below; see FIX_REPORT.md.
- `fixed` in the error rate means first-draw WRONG → redrawn
  CORRECT, strictly. A first-draw WRONG route that grades
  UNCLEAR after its fix leaves the denominator (it is neither
  fixed nor wrong in the rate); the migration table below
  shows those moves explicitly.
- Helper-counting differences (route verdicts unaffected, step
  tallies reported as delivered): (a) Hilt steps 2–3 — h3 grades
  UNCLEAR (generated file absent) while h1/h2/h4/h5/h6/h7/h8
  grade CORRECT on the printed `@HiltAndroidApp` leg; the
  table follows the majority + first-draw convention, and no
  h3 route verdict depends on it (all h3 routes UNCLEAR on
  step 9 regardless). (b) Steps downstream of a WRONG step —
  h1 counts them WRONG, h2 counts them correct-as-code.
  (c) Propagation of the step-8 UNCLEAR downstream — h5
  propagates one step, h7 propagates through most dependents.
  None of (a)–(c) changes any route verdict.
- Framework-file note: several dumps claim framework files
  "not found"; helpers personally printed ActivityThread,
  View, AsyncTask, AbsListView lines in this tree. The
  generated Hilt/Dagger classes and generated protobuf classes
  genuinely are absent, and steps resting on them are graded
  accordingly (see rows 17, 18, 21).

## Per-route verdicts (sample order)

| # | Stratum | Method | Steps | Verdict | Decisive steps | First draw | Helper |
|---|---------|--------|-------|---------|----------------|------------|--------|
| 1 | NONSTD | AndOtpImporter$EncryptedState.decryptNewFormat(SecretKey) | 49 | UNCLEAR | 8–9 vault (convention); 37 pick gap: @FILE dialog pick does not name the andOTP row (default is Aegis, Dialogs.java:519–528) — satisfiable by an unlisted tap, not established | WRONG → UNCLEAR (fix 2; splice gone) | h1: 46/0/3 |
| 2 | NONSTD | FreeOtpImporter$DecryptedStateV2.<init> | 47 | WRONG | 35: @APP GA prefix into FreeOTP decrypt — GA State super(false), so processImporterState never calls any decrypt; 36–47 downstream (h1 counting). Also 8–9 unclear, 30 GA-version, 34 root caveats | UNCLEAR → WRONG (same defect class, not one of the 4 fixes) | h1: 30/13/4 |
| 3 | NONSTD | StratumImporter$EncryptedState.decrypt(SecretKey) | 45 | WRONG | 35: @APP GA prefix into Stratum decrypt — GA State super(false); and even a genuine Stratum app import yields SqlState super(false) (readFromApp passes isInternal=true), so decrypt never fires. 8–9 unclear. Fix 4's @STRATUM→decrypt edge is itself refuted — see flag below | WRONG → WRONG (fix 4 partially refuted) | h2: 42/1/2 |
| 4 | NONSTD | AegisImporter$DecryptedState.getCredentials | 30 | CORRECT | All 30 verified: intro → Welcome import of an encrypted Aegis vault file (in-run producer) → password-slot decrypt → DecryptedState creds | CORRECT → CORRECT | h1: 30/0/0 |
| 5 | INFERRED | EntryAdapter.setTempHighlightEntry | 27 | UNCLEAR | 8–9 vault (convention); rest verified | UNCLEAR → UNCLEAR | h2: 25/0/2 |
| 6 | INFERRED | GroupAdapter.getGroupByUUID | 35 | UNCLEAR | 8–9 vault (convention); rest verified incl. replaceGroup → getGroupByUUID | UNCLEAR → UNCLEAR | h2: 33/0/2 |
| 7 | INFERRED | SlotIntegrityException.<init>(Throwable) | 33 | UNCLEAR | 2–3 Hilt-absent; 9 vault (convention); rest verified end to end incl. Slot.java:53–57 throw site | UNCLEAR → UNCLEAR | h3: 30/0/3 |
| 8 | INFERRED | EditEntryActivity.selectIcon | 42 | WRONG | 41–42: @ASSIGN prefix dispatches to EditEntryActivity$1.onIconSelected (fix-1 onIconSelected residual) instead of AssignIcons$1 (→ setNewIcon); selectIcon never runs from this picker. Also 2, 3, 9 unclear; 28–34 root caveat | not drawn → WRONG (new; fix-1 residual) | h3: 37/2/3 |
| 9 | STATE | Salsa20Engine.salsaCore | 25 | CORRECT | All 25 verified: setup-slide not-finished with matching passwords → SCrypt → salsaCore(8, …) | CORRECT → CORRECT | h4: 25/0/0 |
| 10 | STATE | ScannerActivity.lambda$onQrCodeDetected$1 | 26 | UNCLEAR | 8–9 vault (convention); rest verified conditional on S_LIST | UNCLEAR → UNCLEAR | h4: 24/0/2 |
| 11 | STATE | AuditLogRepository.addVaultUnlockedEvent | 20 | UNCLEAR | 8 cross-run ENCRYPTED vault file, no in-run producer; rest verified incl. MainActivity.java:798 | UNCLEAR → UNCLEAR | h4: 19/0/1 |
| 12 | ENV | ImportExportPreferencesFragment$ExportResultListener.onTaskFinished | 32 | UNCLEAR | 8–9 vault (convention); rest verified incl. plain-export path | UNCLEAR → UNCLEAR | h5: 30/0/2 |
| 13 | ENV | IconPackExistsException.getIconPack | 30 | UNCLEAR | 8–9 vault; 29 cross-run installed pack, no in-run producer; getIconPack call itself verified | UNCLEAR → UNCLEAR | h5: 27/0/3 |
| 14 | ENV | GoogleAuthProtos$MigrationPayload.parser | 24 | UNCLEAR | 8–9 vault; rest verified through scan/QR/SCHEME_EXPORT/parseFrom; generated proto absent (caveat, step 24) | UNCLEAR → UNCLEAR | h5: 22/0/2 |
| 15 | ENV | EditEntryActivity$CustomSvgIcon.<init> | 26 | UNCLEAR | 2–3 Hilt-absent; 9 vault (convention). New shortest route via the genuine empty-packs branch (startIconSelection → startImageSelectionActivity, :590); @EDIT picker path intact; 0 AssignIcons mentions | WRONG → UNCLEAR (fix 1; splice gone) | h3: 23/0/3 |
| 16 | ENV | ApkSignaturePin.getSignatures | 11 | WRONG (by design) | 8: trust guard unsatisfiable — plain TRIGGER entry, no startActivityForResult, no calling package; singleInstance corroborates; TEST=false verified. 9–11 unreachable/unverifiable after step 8. No fix (route-14 class) | WRONG → WRONG (by design) | h6: 5/1/5 |
| 17 | ENV | DaggerAegisApplication_HiltComponents_SingletonC$SingletonCImpl.injectVaultLockReceiver2 | 9 | UNCLEAR | 5–9 Hilt/Dagger injection chain absent; step 8 injected-flag guard expressly unverified. No step shown false | CORRECT → UNCLEAR (stricter generated-code grading, not a graph change) | h6: 2/0/7 |
| 18 | LONG | IconPack$Icon.<init> | 19 | UNCLEAR | 8–13 injection chain absent (step 12 SwitchingProvider unresolved); 16 cross-run installed pack, 17–19 by dependence. No step shown false | UNCLEAR → UNCLEAR | h6: 7/0/12 |
| 19 | LONG | VaultBackupManager$FileInfo.throwBadFormat | 32 | UNCLEAR | 8–9 vault; downstream propagation + unestablished preconditions (24/28/29/32: backups on, tree-uri folder, persisted permission, malformed file present). No step false | UNCLEAR → UNCLEAR | h7: 7/0/25 |
| 20 | LONG | EditEntryActivity.deleteAndFinish | 21 | UNCLEAR | 8–9 vault; delete chain code-verified conditional on a loaded vault | UNCLEAR → UNCLEAR | h7: 7/0/14 |
| 21 | LONG | GoogleAuthProtos$MigrationPayload$DigitCount$DigitCountVerifier.<init> | 32 | UNCLEAR | 8–9 vault; 25 needs ≥2 export batches vs 23 establishing ≥1; 28–32 generated classes absent. No step false | UNCLEAR → UNCLEAR | h7: 7/0/25 |
| 22 | LONG | StratumImporter$LegacyEncryptedState.decrypt(SecretKey) | 45 | WRONG | 35: GA row picked (not Stratum); GA State super(false) → decrypt never fires. Second layer: even genuine Stratum app import yields SqlState; LegacyEncryptedState arises only on the file path (legacy header). 8–9 unclear, 33–34 root unclear, 36–45 prefix-blocked | not drawn → WRONG (new; same defect class) | h8: 30/11/4 |
| 23 | LONG | RawSlot.getType | 31 | WRONG (by design of the disable path) | 29: disabling encryption nulls credentials → plain branch → Header(null, null) → JSONObject.NULL slots, never SlotList.toJson; 30–31 prefix-blocked. Fix is an encrypted-save prefix, not a disable variant. 8–9 unclear | not drawn → WRONG (new) | h8: 26/3/2 |
| 24 | PLAIN | Hilt_AegisApplication.<init> | 2 | CORRECT | Manifest + @HiltAndroidApp leg (generated file absent, caveat noted) | CORRECT → CORRECT | h8: 2/0/0 |
| 25 | PLAIN | AegisApplication.<init> | 1 | CORRECT | Manifest android:name + implicit constructor; no vault-load step, convention N/A | CORRECT → CORRECT | h9: 1/0/0 |

> Correction note (2026-11-01, post-judging): the fix-4 edge processImporterState@STRATUM → StratumImporter$EncryptedState.decrypt(Context,DecryptListener) judged refuted in this row has been REMOVED from the graph (Stratum correction, independently audited). This row's WRONG verdict stands as a verdict on the pre-correction 45-step draw: its decisive reasoning — decrypt never fires on any app-import prefix — is confirmed, not overturned, by the removal. The corrected graph's Stratum decrypt route is a 47-step @FILE route (showImportersDialog@FILE → lambda$27@FILE → startImportFile → processImporterState@FILE → Stratum decrypt → @STRATUM password-dialog chain → decrypt(SecretKey)); that route has NOT been step-judged, so no verdict on it is claimed here. Error rate unchanged (6/10 = 0.6000).

Per-helper tallies (steps correct/wrong/unclear): h1 106/13/7 (126);
h2 100/1/6 (107); h3 90/2/9 (101); h4 68/0/3 (71); h5 79/0/7 (86);
h6 14/1/24 (39); h7 21/0/64 (85); h8 58/14/6 (78); h9 1/0/0 (1).

## Tally and final error rate

- Final sample: CORRECT 4, WRONG 6, UNCLEAR 15 (25 routes).
- Steps: 537 correct / 31 wrong / 126 unclear (694 total).
- fixed (first-draw WRONG → redrawn CORRECT, strict) = 0.
- Final error rate = (fixed + wrong) / (correct + fixed + wrong)
  = (0 + 6) / (4 + 0 + 6) = 6/10 = 0.6000.
- First-draw rate was 6/11 = 0.5455. The rate ROSE although two
  fixable WRONGs left the WRONG set, because the redrawn sample
  contains 4 NEW WRONGs outside the 4-fix scope (rows 2, 8, 22,
  23) and lost 1 CORRECT to stricter generated-code grading
  (row 17). The rate is computed on decidable routes only;
  UNCLEAR routes (15) are excluded from numerator and
  denominator under either convention reading.

## Migration (first draw → redrawn sample)

- WRONG → UNCLEAR (fix applied, splice gone, step-8 cap only):
  CustomSvgIcon (fix 1), AndOtp decryptNewFormat (fix 2).
- WRONG → WRONG: Stratum decrypt (fix 4 refuted, see flag),
  getSignatures (by design, no fix).
- WRONG → not drawn: getKey (fix 3 verified by redump: genuine
  17-step auth path; not in the redrawn sample), ExitActivity
  (by design; not redrawn).
- CORRECT → CORRECT: getCredentials, salsaCore, Hilt_
  AegisApplication, AegisApplication.
- CORRECT → UNCLEAR: injectVaultLockReceiver2 (generated-code
  grading, not a graph change).
- UNCLEAR → WRONG: FreeOtp DecryptedStateV2 (fresh strict
  prefix judgement of the same defect class).
- UNCLEAR → UNCLEAR: 12 routes (rows 5, 6, 7, 10, 11, 12, 13, 14,
  18, 19, 20, 21).
- UNCLEAR → not drawn: startImportFile.
- Not drawn → WRONG: selectIcon, Legacy decrypt, RawSlot
  .getType.
- Not drawn → drawn, no verdict change class: (none besides
  the above).

## FLAG — fix 4 partially refuted (must be corrected before push)

Fresh judging (h2, h8, merger-verified) proves the fix-4 edge
`processImporterState@STRATUM → Stratum decrypt` is FALSE:
`DatabaseImporter.readFromApp` passes isInternal=true, so
Stratum's app-import state is always SqlState(super(false))
and processImporterState takes the decrypted branch — on ANY
app-import prefix, not just GA's. The @STRATUM chain up to
processImporterState is genuine and stays; only the decrypt
edge must be removed, after which the dumped Stratum decrypt
route falls back to the genuine @FILE path (as AndOtp does).
This correction is NOT applied in this step: applying it now
would desync this judged table from the graph. It needs its
own rebuild + redump + audit before the C3 push, and the push
must not include the @STRATUM→decrypt edge as-is. The same
caution applies to any app-import decrypt dispatch: verify
readInternal's state per importer.

> FLAG RESOLVED 2026-11-01 (Stratum correction, independently audited): the @STRATUM→decrypt edge has been removed; the corrected graph's Stratum decrypt route falls back to the genuine @FILE path as predicted here. The row-3 WRONG verdict stands as a historical verdict on the pre-correction draw (see correction note on row 3).

## Follow-ups (not this step; each needs its own design + audit)

1. Stratum @STRATUM→decrypt edge removal (flag above) +
   re-verify; check other importers' @APP decrypt edges
   against readInternal states.
2. FreeOtp decrypt GA-splice fix (FreeOTP-row / @FILE
   re-route, fixes 2–4 pattern).
3. selectIcon onIconSelected split (direct + forwarder,
   fix-1 pattern for onIconSelected).
4. Per-importer @FILE pick variants ($26@ANDOTP etc.) so
   @FILE importer routes establish the picked row (AndOtp
   step-37 gap class).
5. injectVaultLockReceiver2 / IconPack$Icon generated-code
   evidence: Hilt/Dagger chain files absent from the tree;
   whether CORRECT-on-leg or UNCLEAR is the standing rule
   for generated-code steps needs a coordinator decision
   (this table follows the majority + first-draw leg rule).
6. getKey + ExitActivity were not redrawn: getKey's fix-3
   verification (genuine auth path) and ExitActivity's
   by-design WRONG stand from redumps, not from this table.
