# Aegis — FINAL route table (sample-30 redraw, post-vault fix round)

Sample: `python3 -I tools/verify_sample.py Aegis 30 20261025` on the
post-vault graph (row 23 @RAW chain + vault 3-edge deletion; 6387 edges,
pushed 351a99ad). 25 routes (PLAIN pool 2 vs quota 7, as in earlier draws),
1107 steps, 444 distinct edges. C3 sample (25 routes, 696 steps) kept
untouched at `merger/scratch/sample_30_final.txt`; this redraw saved at
`merger/scratch/sample_30_postvault.txt`, dumps at
`merger/scratch/routes_postvault.txt`. Judged fresh, every step,
against printed source by 8 helpers (h1–h8, max 4 routes each), with a
merger completeness check per report (step counts match the sample;
verdicts consistent with step grades; the single WRONG verdict's decisive
claims re-verified against printed source by the merger — see
`merger/scratch/redraw_completeness.md`). No prior verdict was carried
over: re-drawn routes were judged on their new dumps.

## Conventions applied (binding)

- Declared configuration: debug build, fresh install, API 27,
  runtime permissions granted only where a route needs them.
- `Aegis-C3-Step8` (binding, Muse's own, for user/Yang review): the STRICT
  D-C3-10 reading STANDS. A loadEntries/vault-load step whose guard demands
  a producer of the loaded vault earlier on the route, with no such producer
  in steps before it, grades UNCLEAR (not CORRECT). The same applies to any
  cross-run state (vault file, installed pack, installed app data from an
  earlier run) with no in-run producer. A step depending on an UNCLEAR
  producer is itself UNCLEAR.
- GenCode fixed-(c) with wrapper-bracketing (adopted on record, tree
  AGENT_NOTES.md line 792, forwarded in the selectIcon push): a Hilt
  superclass leg counts as a single wrapper anchored by the printed
  `@HiltAndroidApp` leg plus manifest and the printed destination body.
  Hilt steps 2–3 grade CORRECT under this rule wherever it applies.
- Grading discipline: a guard satisfiable by an unlisted in-run action
  grades UNCLEAR, not WRONG; a guard contradicted by a listed step grades
  WRONG. Steps downstream of a WRONG step do not change a verdict that
  already stands on an independent WRONG step (RawSlot, row 8 below).
- `fixed` in the error rate means first-draw WRONG → redrawn CORRECT,
  strictly. A first-draw WRONG route that grades UNCLEAR after its fix
  leaves the denominator (it is neither fixed nor wrong in the rate); a
  route not in the first-draw sample cannot be fixed. The migration table
  below shows those moves explicitly.
- Framework-file note: several dumps claim framework files "not found";
  helpers personally printed ActivityThread, View, AsyncTask, AbsListView
  lines in this tree (under `fw_src/android-8.1.0_r1/core/java/android/`,
  not the dumps' `frameworks/base/` prefix — a citation-path correction,
  not a grading change). The generated Hilt/Dagger classes and generated
  protobuf classes genuinely are absent, and steps resting on them are
  graded accordingly (see rows 18, 20, 23).

## Per-route verdicts (sample order)

| # | Stratum | Method | Steps | Verdict | Decisive steps | C3 table | Helper |
| 1 | NONSTD | AndOtpImporter$EncryptedState.decryptNewFormat(SecretKey) | 67 | CORRECT | None adverse. Step 26 vault-load satisfied in-run by step 21 initNew (VaultManager.java:59-72). | UNCLEAR (first draw WRONG) | h1 |
| 2 | NONSTD | FreeOtpImporter$DecryptedStateV2.<init> | 64 | UNCLEAR | 48 root shell needs rooted device + su grant (not in declared config, no in-run producer); 50 non-root shell → toast + finish (ImportEntriesActivity.java:143-174); 52 installed FreeOTP V2 tokens.xml data, no in-run producer. Not WRONG: nothing listed contradicts root/FreeOTP presence. Steps 53-64 individually CORRECT but conditional on 52. | WRONG (first draw UNCLEAR) | h1 |
| 3 | NONSTD | StratumImporter$EncryptedState.decrypt(SecretKey) | 65 | CORRECT | None adverse. Step 26 as row 1; picked Stratum file + password via in-run picker/password actions. | UNCLEAR (first draw WRONG) | h1 |
| 4 | NONSTD | TwoFASImporter$EncryptedState.deriveKey | 63 | CORRECT | None adverse. Step 26 producer step 21 initNew; step 55 TwoFAS EncryptedState from a TwoFAS file; steps 61-63 password lambda → decrypt(char[]) → deriveKey, all inside TwoFAS. No cross-importer step. | not in C3 sample | h2 |
| 5 | INFERRED | TotpAuthenticatorImporter$EncryptedState.lambda$decrypt$0 | 62 | CORRECT | None adverse. Step 55 file/external branch (internal branch would yield DecryptedState, never reach decrypt); steps 56/62 Yes-path lambda numbering corroborated by javac inner-before-outer pattern. | not in C3 sample | h2 |
| 6 | INFERRED | AuthenticatorPlusImporter$EncryptedState.decrypt(char[]) | 62 | CORRECT | None adverse. Step 55 read always returns EncryptedState; steps 61-62 password lambda → decrypt(char[]), both inside AuthenticatorPlus. | not in C3 sample | h2 |
| 7 | INFERRED | AuthyImporter$EncryptedState.decrypt(char[]) | 62 | CORRECT | None adverse. Dispatch stays Authy at every step (Dialogs.java:515-531; DatabaseImporter.java:37; AuthyImporter.java:101-135,157-162,165-203,207-214). Step 26 producer step 21 initNew. | not in C3 sample | h3 |
| 8 | INFERRED | RawSlot.getType | 49 | WRONG | 28 lock tap impossible: NONE intro (steps 14-21) leaves creds null, so updateLockIcon (MainActivity.java:1155-1161) hides the lock item; 33 AuthActivity.onCreate NPE at AuthActivity.java:131-132 (NONE header Header(null,null) → _slots null, onResume never runs); 35 "password security" STATE contradicted by NONE prefix; 39 empty-slot decrypt returns null (PasswordSlotDecryptTask loop-then-null), onTaskFinished takes invalid-password branch, never finish; 44,47-48 save takes plain branch (VaultRepository.java:119-121), header slots NULL, SlotList.toJson never runs, no RawSlot iterated. The @RAW chain belongs to a password vault; the router's cheapest prefix for this route is the NONE intro. Merger re-verified all five claims against printed source (see redraw_completeness.md). No fix in this round: a password-prefix variant route would need a new fix round + fresh redraw. | WRONG (not in first draw) | h3 |
| 9 | STATE | IconAdapter$CategoryHeader.getPosition | 58 | UNCLEAR | 46 dump jumps from ImportEntriesActivity.onCreate to the save-button tap, omitting the GA app-import sub-flow (startImportApp/RootShellTask, ImportEntriesActivity.java:143-172; GA package read, GoogleAuthImporter.java:60-68) — root + installed GA app + import result never produced on route; 48 assign-icons dialog requires an installed icon pack (ImportEntriesActivity.java:320-322; IconPackManager.java:45-47), no step installs one on a fresh-install route. Neither contradicted. Tail 49-58 printed and correct. | not in C3 sample | h3 |
| 10 | STATE | EntryAdapter.setTempHighlightEntry | 44 | CORRECT | None adverse. Step 26 producer steps 21-22 initNew; suffix creates its own entry in-run (FAB → manual entry → save → result → highlight); step 44 reached regardless of scroll branch at step 43. | UNCLEAR (first draw UNCLEAR) | h4 |
| 11 | STATE | GroupAdapter.getGroupByUUID | 52 | UNCLEAR | 41 addGroup loop body runs only if the vault already has a group (GroupManagerActivity.java:90-95); fresh vault has none (Vault.java:16-17, initNew bare Vault); no group producer in steps 1-40; no add-group UI. Satisfiable only by unlisted in-run action. Steps 42-52 inherit, otherwise mechanically sound. | UNCLEAR (first draw UNCLEAR) | h4 |
| 12 | ENV | AegisImporter$DecryptedState.getCredentials | 30 | CORRECT | None adverse. Step 19 encrypted branch (WelcomeSlide.java:60-69, AegisImporter.read:45-53); step 28 non-null decrypt result from listed password steps 22-24; step 30 cast safe (decrypt(creds) returns DecryptedState, AegisImporter.java:70-78). | CORRECT (first draw CORRECT) | h4 |
| 13 | ENV | ScannerActivity.lambda$onQrCodeDetected$1 | 43 | CORRECT | None adverse. Step 26 producer initNew (VaultManager.java:66-68, _repo set, getVault() does not throw); step 43 target via printed dialog OK listener (ScannerActivity.java:194-196). | UNCLEAR (first draw UNCLEAR) | h5 |
| 14 | ENV | ImportExportPreferencesFragment$ExportResultListener.onTaskFinished | 49 | CORRECT | None adverse. Plain-export path end to end: step 43 exportPlainResultLauncher for Aegis format without encryption (ImportExportPreferencesFragment.java:403-405); step 46 export(stream, null) (483-490). No dumped step demands an encrypted vault. | UNCLEAR (first draw UNCLEAR) | h5 |
| 15 | ENV | IconPackExistsException.getIconPack | 47 | UNCLEAR | 46 Exists dialog requires a pre-existing installed pack (IconPackManager.java:84-89); no step 1-45 installs one; step-43 import cannot be its own producer (throws before installing). Satisfiable by unlisted in-run action (import same pack once earlier, then re-import). | UNCLEAR (first draw UNCLEAR) | h5 |
| 16 | ENV | GoogleAuthProtos$MigrationPayload.parser | 41 | UNCLEAR | 41 parser() accessor rests on the generated protobuf class, absent from the tree (verified by search). ParseFrom call site (GoogleAuthInfo.java:198) and proto definition (google_auth.proto, MigrationPayload) verified. Step 26 producer steps 21-22 initNew. | UNCLEAR (first draw UNCLEAR) | h6 |
| 17 | ENV | EditEntryActivity$CustomSvgIcon.<init> | 43 | CORRECT | None adverse. Icon tap (EditEntryActivity.java:364-366) → startIconSelection → empty-packs branch 585-592 → SVG branch 141-158 → in-tree CustomSvgIcon constructor 1006-1012. 0 AssignIcons-prefix steps. | UNCLEAR (first draw WRONG) | h6 |
| 18 | LONG | AuditLogDao_Impl.__EventType_enumToString | 22 | UNCLEAR | 8 checkIconOptimization demands a loaded vault (VaultManager.java:231-233) but steps 1-7 contain no producer (no intro/initNew/unlock; onStart plaintext-load branch itself needs a pre-existing vault file = cross-run state); 13 scheduleBackup requires encrypted vault + pref_backups (defaults false, Preferences.java:400-401, no in-run producer); 19-22 generated AuditLogDao_Impl absent (only @Dao interface + Room wiring printed). | not in C3 sample | h6 |
| 19 | LONG | SlotIntegrityException.<init>(Throwable) | 50 | UNCLEAR | 38 pin-keyboard preference visible only when vault encrypted (SecurityPreferencesFragment.java:259-265; preferences_security.xml:86); in-run vault is NONE intro vault, hence unencrypted (IntroActivity.java:92-93; VaultRepository.java:352-353). Unlisted enable-encryption visit would satisfy it, contradicted by no listed step. Throw site Slot.java:57. Step 26 producer steps 21-22 initNew. | UNCLEAR (first draw UNCLEAR) | h7 |
| 20 | LONG | IconPack$Icon.<init> | 19 | UNCLEAR | 8-13 Hilt/Dagger injection chain rests on generated code absent from the tree (zero Hilt_*.java / Dagger*.java found); printed anchors do not verify the generated edges. 16 independently UNCLEAR under STRICT step-8 (icon pack is cross-run state, no in-run producer; rescan only reads the existing icons folder, IconPackManager.java:132-165). | UNCLEAR (first draw UNCLEAR) | h7 |
| 21 | LONG | Salsa20Engine.salsaCore | 25 | CORRECT | None adverse. Setup-slide not-finished state is the normal pre-derivation state (fresh empty credentials, SecuritySetupSlide.java:97); tail printed direct calls through SCrypt.java:90/122/188/210 to salsaCore (Salsa20Engine.java:32). | CORRECT (first draw CORRECT) | h7 |
| 22 | LONG | EditEntryActivity.deleteAndFinish | 38 | UNCLEAR | 27 long-press: in-run vault created empty by initNew (non-import intro branch), so no row exists to press; unlisted add-entry visit (FAB → startEditEntryActivity) can supply one. Step 26 CORRECT (initNew step 21 is the STRICT step-8 producer). Steps 28-38 printed-correct conditional on step 27's row. | UNCLEAR (first draw UNCLEAR) | h8 |
| 23 | LONG | GoogleAuthProtos$MigrationPayload$DigitCount$DigitCountVerifier.<init> | 49 | UNCLEAR | 40 needs ≥1 qualifying TOTP/HOTP SHA-1 6-digit entry (in-run vault holds 0); 42 Next visible only if batch list size ≠ 1, i.e. ≥2 batches of 10 = ≥11 entries (in-run count 0); 45-49 generated-protobuf tail UNCLEAR (no GoogleAuthProtos source file in tree, only references in GoogleAuthInfo.java:7,400,459). | UNCLEAR (first draw UNCLEAR) | h8 |
| 24 | PLAIN | Hilt_AegisApplication.<init> | 2 | CORRECT | Manifest android:name leg + @HiltAndroidApp leg under fixed-(c). | CORRECT (first draw CORRECT) | h8 |
| 25 | PLAIN | AegisApplication.<init> | 1 | CORRECT | Manifest leg alone. | CORRECT (first draw CORRECT) | h8 |

## Tally

- Final sample: CORRECT 14, WRONG 1, UNCLEAR 10 (25 routes, 1107 steps).
- Fixed (strict: first-draw WRONG → final CORRECT) = 3: AndOtp (row 1), Stratum (row 3),
  CustomSvgIcon (row 17). FreeOtp V2 went first-draw UNCLEAR → C3 WRONG → final UNCLEAR
  (not fixed); RawSlot went C3 WRONG → final WRONG (not fixed).
- Error rate = (fixed + wrong) / (correct + fixed + wrong) = (3 + 1) / (14 + 3 + 1)
  = 4/18 = 0.2222.
- C3 table rate was 5/9 = 0.5556 (4/5/16, 696 steps). The rate is NOT comparable
  across tables as a trend: the sample itself changed (see migration below), and the
  denominator counts only CORRECT + fixed + WRONG routes in each table's own draw.

## Migration (C3 table → final table)

- 19 methods common to both draws. Of those: 6 moved to CORRECT (AndOtp, Stratum,
  CustomSvgIcon, EntryAdapter, Scanner, ExportResult — all from UNCLEAR),
  1 moved to UNCLEAR (FreeOtp V2, from WRONG — the F2/v2 fix removed the GA
  dispatch defect, leaving only root + installed-data grounds), 1 holds WRONG
  (RawSlot — its new dump is wrong for a new reason, the NONE-intro prefix, not
  the old disable-path reason), and 11 hold their C3 verdicts (GroupAdapter,
  AegisImporter, IconPackExists, MigrationPayload, SlotIntegrity, IconPack Icon,
  Salsa, deleteAndFinish, DigitCount, Hilt, AegisApplication).
- Dropped from the sample (6): EditEntryActivity.selectIcon (C3 WRONG — fix-1 residual
  was fixed by the selectIcon split, but the method left the greedy sample),
  AuditLogRepository.addVaultUnlockedEvent (C3 UNCLEAR), ApkSignaturePin.getSignatures
  (C3 WRONG by design — trust guard unsatisfiable, plain TRIGGER entry, no
  startActivityForResult, no calling package, TEST=false; preserved in the fix log,
  not in this draw), DaggerAegisApplication_HiltComponents_SingletonC$SingletonCImpl.injectVaultLockReceiver2
  (C3 UNCLEAR), VaultBackupManager$FileInfo.throwBadFormat (C3 UNCLEAR),
  StratumImporter$LegacyEncryptedState.decrypt(SecretKey) (C3 WRONG — v2 variant
  dispatch fix; left the sample).
- Added to the sample (6, all judged fresh): TwoFASImporter$EncryptedState.deriveKey
  (CORRECT), TotpAuthenticatorImporter$EncryptedState.lambda$decrypt$0 (CORRECT),
  AuthenticatorPlusImporter$EncryptedState.decrypt(char[]) (CORRECT),
  AuthyImporter$EncryptedState.decrypt(char[]) (CORRECT),
  IconAdapter$CategoryHeader.getPosition (UNCLEAR),
  AuditLogDao_Impl.__EventType_enumToString (UNCLEAR).
- The final table covers ONLY the final draw, per the brief's redraw rule. Dropped
  rows' verdicts are superseded, not carried over; their reasons stay on record in
  the fix log and the C3 table (kept untouched).
