# Aegis C3 fix log (finish run, continuation merger)

## Route 20 — EntryAdapter.lambda$doesAnyGroupMatchSearchFilter$1: WRONG -> UNCLEAR (fixed, 2026-11-01)

- Pre-fix verdict (merger direct, round-7): WRONG, 15 steps. Step 8
  ERROR: restore edge Ed60e6cbd (`onCreateOptionsMenu ->
  EntryListView.setSearchFilter`) had no producer for
  `_submittedSearchQuery` on the route and carried no needs_state.
  Step 12 ERROR: route skipped `onStart`/`loadEntries`, so the
  entry list was never filled. Step 14 UNCLEAR per C2-D4
  (SEARCH_IN_GROUPS mask + relaunch).
- Fix design: helper fix-14-20-carry EDITS.md §2 (tested in the
  helper's private copy first; applied here by the merger, one route
  package at a time, with build + re-dump after). R4 variant fix,
  parts 1 + 2 together (part 1 alone is insufficient — the router
  then picks an initial-load shortcut that is wrong at the stream
  step, because `_searchFilter` is null on initial load):
  - R4-1: new state constant ST_SUBMITTED_QUERY_SAVED (query
    submitted in this MainActivity instance and saved to the
    instance bundle: MainActivity.java:1040 sets it, :419-420
    saves it, :204-205 restores it).
  - R4-2: ST_SUBMITTED_QUERY_SAVED registered as kind `session`
    in STATE_KINDS_OF.
  - R4-3: restore edge relocated to
    `onCreateOptionsMenu@RESTORED -> EntryListView.setSearchFilter`
    with needs_state=ST_SUBMITTED_QUERY_SAVED; the base
    onCreateOptionsMenu no longer feeds setSearchFilter directly.
  - R4-4: producer chain `onSaveInstanceState ->
    onCreateOptionsMenu@RESTORED` (SYSTEM, FW_RECREATE INFERRED +
    SRC MainActivity.java:419-420,204-205,1066-1073).
  - R4-5: filter-set refresh chain on @FILTERED variants
    (setSearchFilter -> refreshEntryList@FILTERED ->
    calculateShownEntries@FILTERED -> isEntryFiltered@FILTERED).
  - R4-6: stream lambda reachable only from isEntryFiltered@FILTERED
    (base isEntryFiltered has no lambda edge now, matching the
    null-filter semantics at EntryAdapter.java:200).
  - R4b follow-up (merger-found, not in the helper design): the
    variant-duplicated auto edge refreshEntryList@FILTERED ->
    EntryList.<init> cited only :281, which does not show the
    callee (check 4 = 1 after the R4 edits). Fixed with hand edges
    citing the full call span :278-281 for BOTH the variant pair
    and the base pair — the base hand edge is required because
    add_auto_edges suppresses an auto call when its base pair has
    a hand edge, so without it the true base call would be
    unmodelled. After this, check 4 = 0 again.
- Build after fix: methods 2995, REACHABLE 2537, UNREACHABLE 458,
  edges 5498, errors 0, warnings 0. Check 2: 22 distinct,
  0 problems. Check 3: 0 flagged. Checks 5-7: 0/0/0. Check 8:
  0 of 458. Label flips vs the helper's private final build: none.
  Edge diff vs the helper's private final build: exactly the 2
  intended hand-edge replacements (2 auto edges out, 2 hand edges
  in). Spot re-dumps still REACHABLE: setSearchFilter,
  isEntryFiltered, lambda$isEntryFiltered$0, onCreateOptionsMenu.
- Re-dumped route (18 steps, step-edge sequence byte-identical to
  the helper's private final dump route20_after2.txt): onCreate ->
  onStart -> loadEntries (plain-text vault STATE; entries + groups
  filled) -> S_LIST -> typing (onQueryTextChange) ->
  setSearchFilter -> filtered refresh chain -> group-name test.
  NO ERROR step remains. Post-fix grade UNCLEAR (not CORRECT):
  step 8 (plain-text vault file from an earlier run) and step 17
  (SEARCH_IN_GROUPS + relaunch, C2-D4) remain cross-run
  preconditions carried on their edges. The router picks the
  typing chain, not submit (exact cost tie, typing gui edge defined
  first); both are in-run, and the final table cites the picked
  route with submit noted as the equally valid alternative.
- Grading decision (C3-D-R20, Muse's own): forward convention for
  restore-state edges is UNCLEAR (the edge now carries its
  precondition, per H1's stated rule and D2); the pre-fix route-20
  step 8 stays ERROR in the historical record. Neither grading
  changes any route verdict (route 03 is wrong either way at
  step 13). Reversal: a printed source line showing the restore
  edge needs no precondition would restore the ERROR grading.
- Residual caveat (no action now): the back-press clear path
  (setSearchFilter(null), MainActivity.java:1408) still reaches
  the @FILTERED chain but is outbid for this target; if a later
  redraw picks it, the next fix is a caller-context split of view
  setSearchFilter (non-null vs null), not suppression of the true
  back-press edge.

## Route 14 — ApkSignaturePin.getSignatures: WRONG, NO FIX (confirmed, 2026-11-01)

- Verdict (H4, audited PASS): WRONG, first failing step 8.
  getIntentFromTrustedSender returns null on an empty calling
  package (TrustedIntents.java:107-109, :133-135); the entry is a
  plain TRIGGER intent into a singleInstance activity
  (AndroidManifest.xml:94,98), not a startActivityForResult launch
  (FW Activity.java:5384-5399), so the trust check is never
  reached. Steps 9-11 correct in isolation, never reached.
- No-fix confirmation: helper fix-14-20-carry re-ran the
  whole-tree greps this session — PanicResponderActivity (:30-34)
  is the only app caller of any TrustedIntents method; no app code
  calls isReceiverTrusted, TrustedIntents.startActivity, or
  checkTrustedSigner(PackageInfo). No variant node can reach
  getSignatures without passing step 8. Draft table entry filed in
  helper EDITS.md §1.2. No graph edit made for this route.

## Routes 01, 02, 03 — fixes APPLIED (helper fix-01-02-03 design, merger-verified, 2026-11-01)

- Design: helper fix-01-02-03 EDITS.md (tested by the helper in a
  private copy on the R4 tree, then re-applied by the merger to the
  current tree — R4 + R4b follow-up — with a backup kept in
  merger/backup-pre-010203/). Every old-text block was verified
  verbatim in the current tree before applying; the dropped R3
  restore edit was NOT applied (R4 supersedes it: the restore edge
  is already the @RESTORED variant with a producer chain).
- Build after fix: methods 2995, REACHABLE 2537, UNREACHABLE 458,
  edges 5564, needs_state edges 112, env edges 55, errors 0,
  warnings 0. All eight checks: check 2: 22 distinct, 0 problems;
  check 3: 0 flagged; check 4: 0 not-show; checks 5-7: 0/0/0;
  check 8: 0 of 458. Label flips vs a temp baseline build from
  the pre-fix graph_def.py: NONE (2995/2995). Routes changed:
  exactly 1706, matching the helper's measurement (1612 from the
  loadEntries swap alone, 94 from all other edits).
- Route 01 throwBadFormat: WRONG -> CORRECT (32 steps, step-edge
  sequence byte-identical to the helper's final01.txt). Edits:
  @SETPWD variant chain (KeyDerivationTask callback fixed at
  construction: Dialogs.java:166 vs SecuritySetupSlide.java:112);
  backups-trigger gate needs_state=ST_VAULT_ENCRYPTED (row visible
  only when backupEnabled, BackupsPreferencesFragment.java:197-199,
  :209); loadEntries tie-break swap (see decision C3-D-01c);
  biometrics-row device state ST_BIOMETRICS_AVAILABLE (row enabled
  only then, SecurityPreferencesFragment.java:277). Residual: the
  Dialogs.lambda$2 listener dispatch picks the earliest row
  (SetPassword row) — harmless here since both listeners call
  saveAndBackupVault().
- Route 02 setTempHighlightEntry: WRONG -> CORRECT (27 steps,
  byte-identical to final02.txt). Edits: save-branch guard edges
  (save item tapped; parse succeeds, no duplicate) + @ADD variant
  (addAndFinish -> saveAndFinish@ADD -> lambda$new$6 add launcher;
  plain saveAndFinish keeps only the edit launcher, so a delete
  result reaches only onEditEntryResult); @EDIT variant chain for
  the delete tap (reachable only from the entryUUID-carrying
  launch, MainActivity.java:516-520). Neighbour check by the
  helper: deleteAndFinish now dumps a real existing-entry prefix.
- Route 03 MOTP.<init>: WRONG -> UNCLEAR (17 steps, byte-identical
  to final03.txt; NOT correct — see decision C3-D-03c). Edits:
  uniformity edge now requires ST_HOLDERS_BOUND (row bound, so
  _holders is not empty) + setData -> setShowProgress hand edge
  with the full >=2-TOTP-periods guard. The old wrong route
  (restore -> filter change -> empty-holders uniformity) no longer
  dumps; the intended bind route exists and is step-correct
  (helper's final_bind_setShowProgress.txt). The dumped 17-step
  tap route is UNCLEAR because step 11 (focusEntry) needs a
  settings precondition (tap-to-reveal or highlight ON) that
  defaults OFF (Preferences.java:85-94) and no step supplies it.
  FOLLOW-UP (not applied — needs type-aware handling): gate the
  tap chain ($1.onClick -> focusEntry, focusEntry -> hideCode,
  focusEntry -> revealCode) AND the $4 refresh-button path as a
  set; gating the tap chain alone would let BFS fall through to
  the $4 path, which is WRONG for MOTP (refresh button is HOTP-only,
  EntryHolder.java:152-153; HotpInfo is not TotpInfo, so getOtp(int)
  never dispatches to MotpInfo.getOtp). The $4 fix needs a
  holder-type variant split, beyond this design.
- Decision C3-D-01c (Muse's own): ACCEPT the loadEntries swap
  (UNLOCKED before PLAIN). Reasons: the UNLOCKED condition (vault
  loaded, else branch MainActivity.java:991-996) is weaker and true
  whenever PLAIN holds (after loadFrom at :963-965 the vault is
  loaded and the else branch runs), while PLAIN is false for
  encrypted vaults — so no route becomes false, only less specific
  at the loadEntries step; routes whose tail genuinely needs
  plain-text still dump PLAIN via kind accounting (PLAIN adds no
  new kind when the tail already needs `file`); measured 0 label
  changes; the alternative (full @ENC preferences chain) is much
  larger. Reversal: swap the two edge definitions back (route 01
  reverts to WRONG at the vault-type step).
- Decisions D-01a (@SETPWD variant), D-01b (backups-trigger gate),
  D-01d (biometrics device state), D-02a (@ADD + save guards +
  @EDIT), D-03a (uniformity gate + setData guard), D-03b (step-8
  grading: adopt the merger/R4 resolution, ST_SEARCH_RESTORED
  proposal dropped), D-03c (tap-route verdict UNCLEAR, not
  CORRECT): adopted as recorded in helper EDITS.md (all Muse's
  own, never Yang's name). Full records in EDITS.md; the
  coordinator appends them to handoff/MUSE_DECISIONS.md.

## Route 20 amendment — loadEntries swap changed its step 8 (2026-11-01)

- After the 01/02/03 edits, route 20's re-dump differs from the
  verified R4 dump in exactly one step: step 8 is now the UNLOCKED
  edge Edae1b52a ("vault is loaded in this process and has not
  been locked since") instead of the PLAIN edge E20e76e09
  ("plain-text vault file exists"). All other 17 steps identical.
  This is the intended effect of decision C3-D-01c: the route no
  longer asserts plain-text, only that a vault file pre-exists and
  is loaded (fresh install still returns early at MainActivity
  :947, so the pre-existing-file precondition stands, now implicit
  in the unlocked-load step). Verdict UNCHANGED: still UNCLEAR
  (step 17 SEARCH_IN_GROUPS + relaunch, C2-D4, remains cross-run).
  The fix_log's route-20 entry above stands with this amendment.

## Routes 04, 06, 16 fixes — APPLIED (2026-11-01, helper fix-04-06-16 design)

- Source: helper deliverables in
  work/Aegis/helper/fix-04-06-16/ (EDITS.md, REPORT.md,
  apply_dialog_splits.py, apply_route06_split.py). Applied by the
  merger in this order, each step verified, NOT copied from any
  private graph_def.py: (1) merger step-1 script
  (/tmp/apply_step1_040616.py): section 04 scanner-error variant
  chain, section 16 T-1 @SECURITY chain, T-2 @AUTHY chain, section
  06 K task split by builder with the single-@AEGIS intermediate
  the dialog script expects, section 16 S import-page @FILE/@APP
  split (text verbatim from the helper's tested
  graph_def_final.py where EDITS.md abbreviates); build after
  step 1: 2995 methods, 2537/458, edges 5646, errors 0,
  warnings 0. (2) dialog script with ONE deviation: its section 7
  ($26 needs_state) REMOVED before running — it contradicts the
  section 06 Fix 2 design and the helper's own final graph, where
  the shared $26 edge carries the corrected format-agnostic guard
  and NO needs_state; running both scripts as written would make
  the route-06 script's asserted old text fail. Build after the
  dialog script: 2995, 2537/458, edges 5763, 0/0. (3) route-06
  format-split script as written. Build: 2995, 2537/458, edges
  5791, 0/0. (4) Fix L, which the dialog script OMITS although
  EDITS.md section L and graph_def_final.py both contain it: the
  10-pair sup block suppressing non-Aegis importer callbacks ->
  WelcomeSlide$1.onStateDecrypted, inserted after the Welcome sup
  block. Without it, WelcomeSlide$1.onStateDecrypted still dumped
  a false 38-step Totp-import route; with it, 29 steps via
  @WELCOME as designed. Build after Fix L: 2995, 2537/458, edges
  5782, 0/0. (5) Check-4 fix found by the merger, not the helper:
  the dialog script's delegation citations were off by one (the
  call line, not the declaration line): PWD3 :260 -> :259 (3
  edges), PWD5 :272 -> :271 (6 edges), TIDLG5 :244 -> :243 (2
  edges), export launchers :82 -> :83 and :86 -> :87 (2 edges);
  all 13 corrected after printing Dialogs.java:243,259,267,271
  and ImportExportPreferencesFragment.java:82-83,86-87. Check 4
  then 0 not-show (3855 checked, 311 skipped, 159 implicit).
- Backup of the pre-fix graph_def.py kept in
  merger/backup-pre-040616/. Label-flip check vs a temp baseline
  build from that backup: 2995/2995 methods, 0 flips.
- Re-dumps (merger/scratch/route04_after.txt, route06_after.txt,
  route16_after.txt): 04 = 22 steps, scan-image route (FAB ->
  startScanImageActivity :812-824 -> picker result ->
  onScanImageResult -> QrDecodeTask -> $18 ->
  importScannedEntries :723), ERROR-free; 06 = 32 steps, plain-
  format branch ($2 -> onExportResult@PLAIN ->
  startExportVault@PLAIN_RESULT -> $26@PLAIN -> ExportTask ->
  target), no encryption claim, ERROR-free; 16 = 42 steps, GA
  app-import route (@APP chain -> root shell -> $5 ->
  processImporterState -> processDecryptedImporterState ->
  processImporterResult -> multi-exception -> multi-error ->
  Details $20 -> detailed dialog -> Copy $23 -> $22 target),
  ERROR-free. Grading for all three: UNCLEAR on step 8 only, NOT
  CORRECT in the strict sense (decision D-C3-10, below). Note on
  step 8: on the current tree (after C3-D-01c) step 8 is the
  UNLOCKED edge Edae1b52a, not the helper baseline's
  ST_PLAIN_VAULT_FILE; the grading is unchanged because the
  unlocked-load step still presupposes a pre-existing vault file
  (fresh install returns early at MainActivity:947), i.e. a
  cross-run precondition with no in-run producer. Relaunch-
  declared reading grades them CORRECT.
- Neighbour spot-checks (helper's 18, re-dumped on the current
  tree): 18/18 match step counts and producer chains —
  Scanner $1 26 @SCANNER_ERROR, Security $7 27 @SECURITY, Auth
  listener 16 @AUTH, Security listener 30 @SECURITY, Aegis $0 44
  @IMPORT, Authy $0 41 @AUTHY, ImportEntries $2 38, process-
  ImporterState 34 @APP, GroupManager $0 33 @GROUP, AndOtp $1 42
  @ANDOTP, FreeOtp $1 42 @FREEOTP, Stratum $1 41 @STRATUM, Legacy
  $1 41 @LEGACY, Totp $0 42 @TOTP, AuthPlus $0 41 @AUTHPLUS,
  TwoFAS $0 41 @TWOFAS, Aegis $1 41 @IMPORT, WelcomeSlide $1 29
  @WELCOME (only after Fix L; see above).
- Eight checks after the full package: build 2995, 2537/458,
  edges 5782, errors 0, warnings 0; check 2: 22 distinct, 0
  problems; check 3: 0 flagged; check 4: 0 not-show; checks 5-7:
  0/0/0; check 8 --all: 0 with no other mention (458); --callers:
  0 of 458; STRICT line 10 = True.
- Decisions D-C3-01 to D-C3-10 (Muse's own, never Yang's name):
  adopted as recorded in helper EDITS.md section 6 (variant
  splits over deletion; plain-delegation re-writes where a plain
  caller remains; Aegis two-chain split; route-06 format split
  over needs_state; $26 guard correction; plain cancel edges
  kept; only onStateDecrypted Welcome edges suppressed; import-
  page file-argument split; PBKDF split by builder; grading
  UNCLEAR on step 8 only). Merger additions recorded here: the
  dialog-script section-7 removal, the Fix L application, and
  the 13 check-4 citation corrections are merger-verified
  corrections to the helper package, not new labelling
  decisions; the coordinator appends D-C3-01..10 to
  handoff/MUSE_DECISIONS.md. No route is left WRONG among 04,
  06, 16; no step required editing tools/.
- Round-7 wrong routes now fixed: 01, 02, 03, 04, 06, 16, 20
  (14 stands wrong with no fix, by design). Remaining open
  carry-forwards: GlideRequests.asBitmap (steps 6-10 correct;
  route still WRONG on ERRORs 25/28/53/65 + UNCLEAR 55) and
  Slot.<init> (steps 6-7 correct, step 8 C2-R1 kept; route still
  WRONG on ERRORs 21/27/30 + UNCLEAR 8/29/33-36) — neither was in
  this session's fix helpers; they need their own fix designs
  before the final sample, or they stand as wrong in the
  round-7 table (they are NOT in the sample-30 draw unless
  drawn; the sample-30 routes are judged separately).

## Sample-30 fix step — decisions recorded before applying fixes (2026-11-01, continuation merger)

- Decision Aegis-C3-Step8 (coordinator decision, binding, Muse's
  own, for user/Yang review): the STRICT D-C3-10 reading STANDS
  for the final table. The 12 solely-step-8 UNCLEAR routes stay
  UNCLEAR, NOT CORRECT. The relaunch-compatible reading (CORRECT
  17, rate 6/23 = 0.2609) is NOT adopted: the declared
  configuration is fresh install, step 8's own guard demands a
  producer of the loaded vault earlier on the route, steps 1-7
  contain none, and adopting the relaunch reading would hide the
  one step with no in-run producer. This reaffirms the concordant
  rulings of all three fix audits (fix-010203, fix-2014-sample,
  fix-040616). UNCLEAR routes are excluded from the error-rate
  denominator under either reading, so this choice hides no WRONG
  route — but the final CORRECT count (5 first-draw) must not be
  inflated to 17 by convention.
- Decision Aegis-C3-Exit (merger decision, Muse's own, for
  user/Yang review): ExitActivity.onCreate is WRONG by design,
  route-14 class (option (a)), with proof printed by the merger
  this session — NOT fixable, NOT plain WRONG, never CORRECT or
  UNCLEAR. Evidence printed personally: dumped route
  (merger/scratch/route_ExitActivity_before.txt, 10 steps) step 7
  E9dbeda39 PanicResponderActivity.onCreate -> finishApp, guard
  "pref_panic_trigger is on and the sender is trusted and the
  action is the TRIGGER"; PanicResponderActivity.java:29
  (!BuildConfig.TEST.get() -> trusted path :31-34, else
  getIntent() :35-36), :38-42 (TRIGGER -> finishApp, else
  finish), :49-52 (finishApp calls exitAppAndRemoveFromRecents);
  AndroidManifest.xml:91-101 (PanicResponderActivity exported,
  launchMode singleInstance, TRIGGER intent-filter) and the bare
  ExitActivity declaration (no intent-filter, so only explicit
  intents reach it); app/build.gradle:37 (TEST =
  AtomicBoolean(false) in defaultConfig, so the TEST re-scope is
  invalid under the declared standard configuration); whole-app
  grep: exitAppAndRemoveFromRecents is called only from
  PanicResponderActivity.finishApp (:50). The "sender is
  trusted" clause is unsatisfiable in standard config: entry is
  a plain TRIGGER intent (not startActivityForResult) into a
  singleInstance activity, so no calling package exists for
  TrustedIntents.getIntentFromTrustedSender, which returns null
  and onCreate falls to finish() (:46) — steps 8-10 correct in
  isolation, never reached. Caveat recorded honestly:
  TrustedIntents.java and FW Activity.java are ABSENT from the
  merger tree's fw_src (partial extraction), so the library
  lines (TrustedIntents.java:104-110,120-124,131-142; FW-SRC
  Activity.java:5384-5399) rest on graph_def.py's guard text at
  the TrustedIntents edge block plus the route-14 audit's
  printed verification — both in-tree legs (singleInstance
  manifest, TEST=false) were re-printed by the merger. No graph
  fix exists within standard config: dropping the trust guard
  would invent a variant contradicting code, and the TEST
  re-scope contradicts the declared configuration. Labels
  UNCHANGED (route-14 precedent: ApkSignaturePin.getSignatures
  stays REACHABLE while its route stands WRONG by design).
  OPEN ITEM for coordinator/user review: on this evidence the
  whole ExitActivity chain (finishApp, exitAppAndRemoveFrom-
  Recents, ExitActivity.<init>, ExitActivity.onCreate) is
  production-unreachable; if the coordinator/user rule so, those
  4 methods flip to UNREACHABLE and the sample composition
  changes — that is a label decision, NOT made silently here.
  Final-table effect: none on the rate (WRONG counts as wrong
  under all three options).
- Baseline re-confirmed before fixes (private tree build):
  methods 2995, REACHABLE 2537, UNREACHABLE 458, edges 5782,
  errors 0, warnings 0; backup of pre-fix graph_def.py at
  merger/backup-pre-samplefix/graph_def.py.

## Sample-30 fix 1 — CustomSvgIcon installer split: APPLIED (2026-11-01)

- Design (J1, merger-verified against printed source, EXTENDED):
  the judging design split create/loadIcons/lambda$2 by installer,
  but printed source shows two more paths the design missed: the
  IconPickerDialog$1 forwarder (adapter listener is always the $1
  instance created in create(), IconPickerDialog.java:53-66, which
  forwards to the installing activity's listener :62-64) and the
  search-clear path (setQuery(null) reloads with showAddCustom
  false, IconAdapter.java:92-96). Both are split here too, or the
  @ASSIGN prefix would still reach EditEntryActivity$1 through
  the shared forwarder / shared search reload.
- Edits (graph_def.py, after the :4444 dispatch edge): create
  @EDIT (from startIconSelection, showAddCustom true, :594) /
  @ASSIGN (from onAssignIconEntryClick, showAddCustom false,
  :194); loadIcons @EDIT/@ASSIGN; popup lambdas $2/$1 @EDIT/
  @ASSIGN (pack switch keeps the flag, :138); shared create
  machinery replicated onto both variants (focus $0, watcher $2
  x3, preloader getPreloadItems/getPreloadRequestBuilder, span
  $3, IconRecyclerView <init>/onMeasure; auto constructor edges
  replicate on their own); loadIcons framework edges replicated
  (onCreateViewHolder, getItemCount, getItemViewType, sort
  lambda) with onBindViewHolder split; category-header tap $3
  replicated shared from both variants (installer-independent);
  dispatch split direct (lambda$2@EDIT -> EditEntry$1, @ASSIGN ->
  AssignIcons$1 empty dead-end) AND forwarder ($1@EDIT ->
  EditEntry$1, $1@ASSIGN -> AssignIcons$1); search-clear sup'd
  and re-routed to loadIcons@NOCUSTOM -> onBindViewHolder
  @NOCUSTOM with NO onCustomSelected dispatch (no DummyIcon row
  after a false reload). Base chain left unfed (both callers use
  variants); its edges stay as documentation, per the @APP/@FILE
  precedent. Residual (recorded, out of scope): onIconSelected
  dispatch stays shared (cannot reach CustomSvgIcon).
- First build after the edit: 2 errors / 2 flips (lambda$3 +
  setIsCollapsed UNRESOLVED — the category tap had not been
  replicated); fixed by replicating the $3 gui edges, rebuilt.
- Build after fix 1: methods 2995, REACHABLE 2537, UNREACHABLE
  458, edges 5900 (+118), errors 0, warnings 0; label flips 0.
  Eight checks: check 2: 22 distinct, 0 problems; check 3: 0
  flagged; check 4: 3915 checked, 317 skipped, 159 implicit, 0
  not-show; checks 5-7: check_v2 skips schema-2 Aegis, 0
  problems; check 8 --all: 0 with no other mention; --callers:
  0 of 458; STRICT line 10 = True.
- Redump CustomSvgIcon.<init> (26 steps, scratch/
  route_CustomSvgIcon_after_fix1.txt): edit page -> icon click
  -> startIconSelection -> startImageSelectionActivity (empty
  icon-packs branch, :590) -> chooser -> SVG -> ImportFileTask
  @SVG_PICK -> lambda$new$0 -> CustomSvgIcon.<init>; 0
  AssignIcons mentions. Graph reachability check: AssignIcons
  prefix reaches CustomSvgIcon = False, reaches EditEntry$1
  .onCustomSelected = False, reaches AssignIcons$1 = True (dead
  end); EditEntry prefix reaches CustomSvgIcon and EditEntry$1
  = True. Note: the new shortest route skips the picker via the
  genuine empty-packs branch; the @EDIT picker path remains as
  the longer genuine route. Step 8 on this route is the
  UNLOCKED edge, so under STRICT D-C3-10 it grades UNCLEAR at
  best if redrawn — the fix removes WRONG, it does not remove
  the step-8 caveat.

## Sample-30 fix 2 — AndOtp processImporterState @FILE split: APPLIED (2026-11-01)

- Design (J4, merger-verified): the @APP-variant edge wording in
  the helper report does not exist as such — the dumped step 35
  was the SHARED auto CHA edge (processImporterState ->
  AndOtp decrypt, :179), so a bare sup would have killed the
  genuine @FILE path too. The fix splits instead: startImportFile
  feeds processImporterState@FILE (new) and the base node (hand
  replacement of the auto :134 edge, for all other importers);
  the auto CHA edge to AndOtp decrypt is sup'd; only the @FILE
  variant reaches AndOtp decrypt, guarded by supportsDirect
  false (DatabaseImporter.java:35), getAppPath throws
  (AndOtpImporter.java:59-62), and read -> EncryptedState on
  non-JSON (AndOtpImporter.java:76-80).
- Build after fix 2: methods 2995, REACHABLE 2537, UNREACHABLE
  458, edges 5913 (+13), errors 0, warnings 0; label flips 0.
  Eight checks: check 2: 22/0; check 3: 0; check 4: 3926
  checked, 318 skipped, 159 implicit, 0 not-show; checks 5-7:
  check_v2 schema-2 skip, 0 problems; check 8 --all: 0;
  --callers: 0 of 458; STRICT True.
- Redump decryptNewFormat (scratch/
  route_AndOtp_after_fix2.txt): pref_import -> @FILE dialog ->
  file picker -> ImportFileTask -> SIE@FILE -> onCreate@FILE ->
  startImport@FILE -> startImportFile -> processImporterState
  @FILE -> AndOtp decrypt -> @ANDOTP dialog chain ->
  decryptNewFormat; 0 @APP/GA mentions. Caveat: the @FILE
  dialog pick step does not name the andOTP row (the graph's
  existing @FILE abstraction level, shared by all @FILE importer
  routes); the route is genuine (pick andOTP row, pick an
  andOTP file) and no longer contradicts its prefix.

## Sample-30 fix 3 — Aegis decrypt@IMPORT onto @FILE variant: APPLIED (2026-11-01)

- Design (J8, merger-verified): the :1291 hand edge moved from
  base processImporterState to processImporterState@FILE (fed by
  startImportFile since fix 2); guard/evidence updated to the
  @FILE Aegis facts (supportsDirect false, DatabaseImporter
  .java:34; getAppPath throws, AegisImporter.java:39-42; read
  returns EncryptedState for an encrypted vault file,
  AegisImporter.java:44-52). The auto CHA edge to Aegis decrypt
  stays suppressed by this hand edge's base pair, as before.
  The @APP prefix must NOT be "fixed" for this target (Aegis is
  excluded from the direct dialog).
- Build after fix 3: methods 2995, REACHABLE 2537, UNREACHABLE
  458, edges 5913 (unchanged — the edge moved, not added),
  errors 0, warnings 0; label flips 0. Eight checks: check 2:
  22/0; check 3: 0; check 4: 3926 checked, 318 skipped, 159
  implicit, 0 not-show; checks 5-7: check_v2 schema-2 skip, 0
  problems; check 8 --all: 0; --callers: 0 of 458; STRICT True.
- Redump getKey (scratch/route_getKey_after_fix3.txt): the
  dumped route is now the 17-step AUTH path (MainActivity
  .onStart -> startAuthActivity (ENCRYPTED edge) -> AuthActivity
  -> password-slot decrypt task -> getKey), NOT the importer
  path — the router prefers it once the @APP splice is gone.
  That path is genuine (getKey runs on every password unlock,
  AuthActivity.java:356); its only caveat is the cross-run
  ENCRYPTED step-8 state, so it grades UNCLEAR at best under
  the strict convention, never WRONG. The @FILE importer path
  to getKey still exists (verified: startImportFile reaches
  getKey) and is genuine.
- Reachability audit note (for auditors): a BFS still finds
  base processImporterState -> decrypt@IMPORT, but ONLY the long
  way around (base -> processDecryptedImporterState -> icon
  optimisation -> MainActivity -> Settings -> file import ->
  @FILE chain -> @FILE variant -> decrypt@IMPORT). That is a
  genuine two-import execution, not a surviving splice: every
  path to decrypt@IMPORT now passes through a @FILE segment
  that establishes the file-import context. The same holds for
  AndOtp after fix 2. No direct @APP-prefix path to either
  decrypt remains.

## Sample-30 fix 4 — Stratum dispatch split: APPLIED (2026-11-01)

- Design (J8, merger-verified, CORRECTED in application):
  Stratum is genuinely reachable both ways (supportsDirect true,
  DatabaseImporter.java:49; real getAppPath, StratumImporter
  .java:65-66), so unlike AndOtp/Aegis it needs its own @APP
  chain, not just @FILE. Threaded: $26@STRATUM (Stratum row tap
  in the direct dialog) -> $27@STRATUM (OK reads Stratum) ->
  lambda$7@STRATUM -> SIE@STRATUM -> <init>@STRATUM ->
  onCreate@STRATUM -> startImport@STRATUM -> startImportApp
  @STRATUM -> async -> lambda$5@STRATUM -> processImporterState
  @STRATUM -> Stratum decrypt; plus @FILE variant -> Stratum
  decrypt; shared auto CHA edge sup'd; base lambda$5 ->
  processImporterState re-written by hand (its auto edge is
  suppressed by the @STRATUM variant hand edge's base pair).
  Warning lambdas NOT threaded for @STRATUM (direct path only;
  supported-version case suffices for REACHABLE).
- FIRST ATTEMPT FAILED REDUMP (caught by the per-fix redump,
  not by the checks): the first build passed everything
  (2995, 2537/458, edges 5956, 0/0, flips 0) but the redump
  still showed the GA pick (steps 23-27 @APP) followed by
  lambda$5@STRATUM dispatch — because lambda$5@STRATUM had been
  fed from the SHARED onPostExecute node, which the base
  startImportApp chain also reaches. Fix: the root-shell async
  chain is variant-split too (doInBackground@STRATUM,
  onPostExecute@STRATUM, same pattern as ImportFileTask
  @SVG_PICK/@SETTINGS_IMPORT); the shared-node feed was
  removed. Lesson recorded: variant dispatch must be split
  end-to-end through shared async machinery, or the shared
  nodes re-merge the prefixes.
- Build after fix 4 (corrected): methods 2995, REACHABLE 2537,
  UNREACHABLE 458, edges 5958 (+2 vs first attempt), errors 0,
  warnings 0; label flips 0 (vs pre-fix4). Eight checks: check
  2: 22/0; check 3: 0; check 4: 3955 checked, 321 skipped, 160
  implicit, 0 not-show; checks 5-7: check_v2 schema-2 skip, 0
  problems; check 8 --all: 0; --callers: 0 of 458; STRICT True.
- Redump decrypt(SecretKey) (scratch/
  route_Stratum_after_fix4b.txt): Stratum row tap -> OK ->
  @STRATUM page chain -> @STRATUM async -> @STRATUM dispatch
  -> Stratum decrypt -> @STRATUM dialog chain -> decrypt
  (SecretKey); 0 GA mentions. Reachability audit note: a BFS
  still finds base processImporterState -> Stratum decrypt,
  but ONLY the long way around through the @FILE chain (same
  genuine two-import execution as fix 3's note); no direct
  @APP-prefix path remains.
- ALL FOUR SAMPLE FIXES NOW APPLIED. Cumulative: methods
  2995, 2537/458, edges 5782 -> 5958 (+176), errors 0,
  warnings 0, label flips 0 across all four fixes.

## Sample redraw + final judging wave 1 (2026-11-01)

- Redraw (same seed 20261025, verify_sample.py Aegis 30):
  25 routes again (PLAIN pool 2 vs quota 7, as expected),
  353 distinct edges (first draw: 330), saved to merger/scratch/
  sample_30_final.txt; first-draw sample_30.txt untouched.
  Composition changed vs first draw (strata follow routes):
  IN: EditEntryActivity.selectIcon, StratumImporter
  $LegacyEncryptedState.decrypt(SecretKey), RawSlot.getType;
  OUT: ImportEntriesActivity.startImportFile, PasswordSlot
  DecryptTask$Result.getKey (its new 17-step auth route left
  its old stratum), ExitActivity.onCreate. The 3 other fixed
  targets ARE redrawn (AndOtp 49 steps via @FILE, Stratum 45
  steps via @STRATUM, CustomSvgIcon 26 steps via the empty-
  packs branch). getSignatures redrawn (11 steps).
- Final judging: 9 helpers, max 3 routes each, staggered waves
  (wave 1: h1-h5 spawned; wave 2: h6-h9 follow on wave-1
  delivery). Helpers judge fresh from per-helper dumps in
  judging-final/h1-h9/routes.txt under the STRICT D-C3-10
  step-8 convention; prior verdicts deliberately withheld.
  Merger completeness check per report follows delivery.

## Final-judging wave 1 — merger verification of WRONG verdicts (2026-11-01)

- h2 Stratum decrypt WRONG — CONFIRMED by the merger on
  printed source, and it REFUTES part of fix 4. DatabaseImporter
  .readFromApp passes isInternal=true (DatabaseImporter.java
  :79-87); StratumImporter.read(stream, true) takes readInternal
  (StratumImporter.java:70-72), which returns SqlState with
  super(false) (:324-328). No Stratum readFromApp override
  exists. So on ANY app-import prefix (@APP or @STRATUM) the
  state is SqlState, processImporterState takes the decrypted
  branch, and EncryptedState.decrypt is NEVER called. The fix-4
  edge processImporterState@STRATUM -> Stratum decrypt is
  therefore FALSE, even though the @STRATUM chain up to
  processImporterState is genuine. The genuine Stratum decrypt
  path is @FILE only (readExternal -> readEncrypted ->
  EncryptedState). CORRECTION REQUIRED BEFORE PUSH (flagged for
  the fix audits, NOT applied silently here — applying it now
  would desync the judged sample from the graph): remove the
  @STRATUM -> Stratum decrypt edge; keep the @STRATUM chain
  for the decrypted branch; the dumped route then falls back
  to the genuine @FILE path. The final table judges the graph
  as it stood at judging time, so Stratum stays WRONG there.
  General caution recorded: app-import decrypt dispatch needs
  per-importer verification of readInternal's state — Stratum
  proves @APP decrypt can be false even for supportsDirect
  importers.
- h1 FreeOtp V2 WRONG — CONFIRMED (new WRONG of the same
  defect class, NOT one of the 4 fixes; reported in the final
  table, follow-up fix needed, not applied in this step). The
  dumped route runs the @APP GA prefix (GA row tapped, steps
  22-34) into FreeOTP decrypt; GA State is super(false), so
  processImporterState takes the decrypted branch and never
  calls any decrypt. Fix direction (for follow-up): re-route
  by tapping the FreeOTP row / @FILE path, same pattern as
  fixes 2-4.
- h3 selectIcon WRONG — CONFIRMED (known residual from fix 1,
  now sampled; reported in the final table, follow-up fix
  needed). The dumped route correctly follows the @ASSIGN
  variants through step 40 (create@ASSIGN -> loadIcons@ASSIGN
  -> onBindViewHolder@ASSIGN -> lambda$2@ASSIGN), but step 41
  dispatches to EditEntryActivity$1.onIconSelected — the
  SHARED onIconSelected dispatch fix 1 deliberately left
  unsplit. On the Assign prefix the listener is AssignIcons$1
  (onIconSelected -> entry.setNewIcon), so selectIcon never
  runs from this picker. Fix direction (for follow-up): split
  onIconSelected direct + forwarder the same way as
  onCustomSelected.
- h1 AndOtp UNCLEAR — verdict stands regardless: steps 8-9
  UNCLEAR (step-8 convention) plus step 37 UNCLEAR (the @FILE
  dialog pick step does not name the andOTP row; the default
  checked row is Aegis, Dialogs.java:519-528). The @FILE route
  is satisfiable (tap andOTP row) but not established as
  dumped. Follow-up: per-importer @FILE pick variants
  ($26@ANDOTP etc.) would make @FILE importer routes
  establishable. No conflict with fix 2's correctness (the
  splice is gone; the remaining gap is pick-step precision).
- Helper-convention notes (no route verdict depends on them):
  (a) Hilt steps 2-3: h3 grades UNCLEAR (generated file
  absent) while h1/h2/h4/h5 grade CORRECT on the printed
  @HiltAndroidApp leg. The final table follows the majority
  + first-draw convention (CORRECT on the leg, caveat noted);
  all h3 routes are UNCLEAR on step 9 regardless, so no h3
  verdict changes. (b) Post-failure downstream steps: h1
  counts them WRONG, h2 counts them correct-as-code. Step
  tallies are reported as delivered per helper; route
  verdicts (which drive the error rate) are unaffected.

## Final table built + STOP (2026-11-01, continuation merger)

- Final judging complete: 9 helpers (h1-h9), 25 routes, 694
  steps. Final table: judging-final/route_table.md (NOT yet
  copied to scratch/ — that copy happens ONLY at C3 push
  time after fix audits PASS). Tally: CORRECT 4, WRONG 6,
  UNCLEAR 15; steps 537/31/126. Final error rate (fixed =
  first-draw WRONG -> redrawn CORRECT, strict) = (0+6)/
  (4+0+6) = 6/10 = 0.6000 (first draw 6/11 = 0.5455; the rise
  is 4 NEW WRONGs outside the 4-fix scope + 1 CORRECT lost
  to stricter generated-code grading, not fix failure).
- Merger completeness check per report: step counts match
  the redrawn sample for all 25 routes; per-helper
  arithmetic verified (h1 106/13/7 of 126; h2 100/1/6 of 107;
  h3 90/2/9 of 101; h4 68/0/3 of 71; h5 79/0/7 of 86; h6
  14/1/24 of 39; h7 21/0/64 of 85; h8 58/14/6 of 78; h9 1/0/0
  of 1); every report holds per-step tables with personally
  printed file:lines; graph untouched by helpers (graph_def
  .py mtime = fix-4 edit time).
- Merger-verified findings: Stratum fix-4 edge REFUTED
  (readFromApp isInternal=true -> SqlState super(false) ->
  decrypt never fires on ANY app-import prefix; correction
  = remove @STRATUM -> decrypt edge, route falls back to
  @FILE; flagged for audits, NOT applied here to avoid
  desyncing the judged table); FreeOtp WRONG confirmed (GA
  splice, same class, not a fix target); selectIcon WRONG
  confirmed (fix-1 onIconSelected residual); AndOtp UNCLEAR
  (steps 8-9 + step-37 pick gap); getSignatures WRONG by
  design confirmed independently (h6).
- Deliverables: appended fix_log.md + AGENT_NOTES.md entries;
  judging-final/route_table.md (FINAL); merger/FIX_REPORT.md
  (fixes with per-fix rebuild counts, ExitActivity decision
  with printed evidence, step-8 convention record, redrawn
  sample + tally + rate, exact C3 push manifest with the
  Stratum correction warning). NO PUSH made. Next: independent
  fix audits, then C3 push, then C4 logs, then D1/D3/D7, then
  F1-readiness. No F1 claim, no PROGRESS line.

## Stratum correction — fix-4 edge removed (2026-11-01, Stratum-correction step)

- REMOVED the single hand edge `ImportEntriesActivity.processImporterState@STRATUM
  -> StratumImporter$EncryptedState.decrypt(Context,DecryptListener)` (was
  graph_def.py:1356-1359; a correction comment now marks its place). Nothing
  else changed: the @STRATUM chain up to processImporterState stays
  (lambda$startImportApp$5@STRATUM -> processImporterState@STRATUM, and
  processImporterState@STRATUM -> processDecryptedImporterState for the
  decrypted branch); the @FILE hand edge to Stratum decrypt stays.
- Evidence re-verified on printed source before deletion:
  DatabaseImporter.readFromApp passes isInternal=true
  (DatabaseImporter.java:79-87); StratumImporter.read branches on it
  (StratumImporter.java:70-72) to readInternal (:74-77), which returns
  SqlState with super(false) (:324-328); processImporterState takes the
  decrypted branch when isEncrypted() is false
  (ImportEntriesActivity.java:176-182; State base :144-153). No Stratum
  readFromApp override exists. So EncryptedState.decrypt never fires on ANY
  app-import prefix. Genuine Stratum decrypt path is @FILE only
  (readExternal -> readEncrypted -> EncryptedState, :80-105).
- Rebuild after correction: methods 2995, REACHABLE 2537, UNREACHABLE 458,
  edges 5957 (-1, exactly the removed edge), errors 0, warnings 0.
  Label diff vs methods_before_fix4.csv: 0 flips, 0 added, 0 removed.
- Redump StratumImporter$EncryptedState.decrypt(SecretKey)
  (merger/scratch/route_Stratum_after_correction.txt): falls back to the
  genuine @FILE path — showImportersDialog@FILE -> lambda$27@FILE ->
  startImportFile -> processImporterState@FILE -> Stratum decrypt ->
  @STRATUM password-dialog chain -> decrypt(SecretKey); 0 @STRATUM dispatch
  steps before decrypt. Post-correction trigger graph confirms the ONLY
  incoming edge to Stratum decrypt(Context,DecryptListener) is
  processImporterState@FILE.
- Eight checks after correction (merger/scratch/*_after_correction.txt):
  check 2: 22 distinct, 0 problems; check 3: 0 flagged; check 4: 3955
  checked, 321 skipped, 160 implicit, 0 not-show; checks 5-7: 0/0/0,
  STRICT True (line 10); check 8 --all: 0 with no other mention;
  --callers: 0 of 458.
- Report-only cross-importer check (NO other edges changed): same
  readInternal-state error found in TWO further app-import decrypt
  dispatches — (1) processImporterState@STRATUM ->
  StratumImporter$LegacyEncryptedState.decrypt (Legacy arises only via
  readEncrypted on the file path, StratumImporter.java:94-105; readInternal
  yields SqlState only); (2) any app-import-prefix dispatch to
  TotpAuthenticatorImporter$EncryptedState.decrypt (Totp read() branches
  on isInternal: internal -> DecryptedState always, TotpAuthenticator
  Importer.java:70-95; decrypt fires only on the file path, despite
  supportsDirect=true and a real getAppPath). NOT the error:
  FreeOtp (readV2 -> EncryptedState regardless of isInternal, :106-115)
  and Authy (readFromApp override can yield EncryptedState, :71-100,128)
  are genuine on app import; AndOtp, Aegis, TwoFAS, AuthenticatorPlus
  have no app import at all (supportsDirect false and/or getAppPath
  throws: AndOtpImporter.java:59-62, AuthenticatorPlusImporter.java:26).
- Judged table NOT touched (judging-final/route_table.md still judges the
  graph as it stood at judging time; Stratum stays WRONG there). NO PUSH
  made. Ready for independent audit; C3 push only after audit PASSES.

## selectIcon split (C3 follow-up, pushed ed60374a) — EditEntryActivity.selectIcon route, WRONG -> fixed in graph (table redraw pending)
- Defect (judged row 8, 42 steps): steps 41–42 ran an @ASSIGN prefix then dispatched to EditEntryActivity$1.onIconSelected; the dispatch was 12 auto CHA edges (base lambda -> 3 listeners; lambda@EDIT -> 3; lambda@ASSIGN -> 3; base forwarder $1 -> self + 2), so the @ASSIGN picker path reached selectIcon (edit page) instead of setNewIcon (assign-icons page).
- Fix (design audit PASS): 6 hand edges + fix-1 comment update, placed after the onCustomSelected forwarder block. Layer A direct: lambda@EDIT -> Edit$1.onIconSelected (E7686fd9e), lambda@ASSIGN -> Assign$1.onIconSelected (E3970a521). Layer B forwarder: lambda@EDIT -> $1.onIconSelected@EDIT (E6ceb381c), lambda@ASSIGN -> $1.onIconSelected@ASSIGN (E8c8543fd), $1@EDIT -> Edit$1.onIconSelected (E04e63aba), $1@ASSIGN -> Assign$1.onIconSelected (E7a64eb0f). No sup (variant-source sup does not work; base-pair suppression redundant once all six hand edges exist), no base hand edge, no @NOCUSTOM edge (follow-up: watcher/setQuery split first). Base self-loop E1cb4fdc9 kept; downstream E8aa09ff0 (Edit$1 -> selectIcon) and Efb20eb51 (Assign$1 -> setNewIcon) unchanged.
- Build: 2995/2537/458/5954/0/0 (5957 − 11 auto removed + 8 added: 6 hand + 2 variant self-loops E6bdabf18/Ef6ab0015). 0 label flips. Prefix assertions both layers PASS; old 42-step @ASSIGN -> selectIcon gone via direct AND forwarder. Redumps: selectIcon 25 steps via @EDIT picker (0 @ASSIGN steps); setNewIcon shortest 34 steps onCreate path with @ASSIGN picker path verified by reachability. Eight checks clean. Only selectIcon of the 25 sampled routes changed (42 -> 25). Table verdict updates at the final redraw + re-judge, not here.

## file-pick v2 V1–V8 (pushed with the v2 commit) — per-importer @FILE pick variants, seven importers
- Design: helper/file-pick-design-v2/DESIGN.md (audit PASS). Template E1/E3–E16/E19 per importer (E2/E17/E18 deleted by audit D1/D2 — auto expansion); Stratum two E19s (AUTHENTICATORPRO header -> EncryptedState; AuthenticatorPro legacy header -> LegacyEncryptedState). Order V1 AndOtp, V2 Stratum, V3 TOTP, V4 FreeOTP, V5 2FAS, V6 AuthPlus, V7 Authy, V8 base-feed deletion last. Each importer: chain + suppression/hand-move in a single private sequence; no intermediate pushed (R1).
- Moves: AndOtp @FILE hand edge Efee7d0a4 -> variant E19 (fix-2 guard moved verbatim); Stratum-Encrypted @FILE hand edge E8360a30f -> variant E19 (fix-4 guard moved verbatim); Aegis @FILE hand edge E2b621d3f STAYS (default chain). Sups (base pairs): Legacy, TOTP, FreeOTP, 2FAS, AuthPlus, Authy. V8: startImportFile -> base processImporterState (E4f8ba81d) deleted; startImportFile -> @FILE (Eb1eb3667) retained; base reachable only from lambda$startImportApp$5.
- Measured suppression rule: a variant E19 hand edge alone suppresses all auto copies of its base pair (observed at V2 Legacy, V3 TOTP, V4 FreeOTP chain-first builds); the six sups are explicit, not load-bearing.
- Build: 5954 -> V1 6015 -> V2 6072 -> V3 6127 -> V4 6180 -> V5 6231 -> V6 6280 -> V7 6327 -> V8 6326; methods 2995, 2537/458, 0 flips, errors 0, warnings 0 throughout. All eight variant decrypt routes dump 38 steps via their variant chains; every variant target incoming exactly 1 (its variant E19). Full §9 passes on the V8 build (see AGENT_NOTES.md v2 entry for the item-by-item record).
- Side effects (recorded, not hidden): @APP GA-prefix routes to the six auto targets are removed. For 2FAS, Authenticator Plus, TOTP, Legacy those routes were false anyway; for Authy and FreeOTP they were genuine only with their own row tap, and a genuine @APP pick variant is out of scope (design §8). No label regression: all targets stay REACHABLE via @FILE variant chains.
- Table NOT rewritten here. L0/F0 verification-only, then F2, then fix round, then redraw + re-judge.

## L0 verification-only (Legacy+Totp, nothing landed) — post-v2 graph, 6326 edges
- Legacy decrypt incoming exactly 1 (variant E19 E53060425, @FILE_STRATUM dispatch); Totp decrypt incoming exactly 1 (variant E19 E94c0e46e, @FILE_TOTP dispatch). All six suspect auto ids absent (Legacy E9d8ead03 / E4d74d97b / Ee4fdd4f0; Totp E5a52eefb / Eb33de12d / Eda333e39). Re-picked routes Legacy 18 + Totp 10, all REACHABLE, 0 bad dispatch, +3 steps throughout; 26 of 28 through their own variant decrypt with byte-identical suffixes; the 2 exceptions (ContextHelper.getActivity/getLifecycle via the sibling Stratum Encrypted variant) are fully explained shared-downstream routing, not defects. VERDICT: L0 PASS — skipped Legacy+Totp items correctly subsumed by v2; nothing lands.

## F0 verification-only (FreeOtp stage 1, nothing landed) — post-v2 graph, 6326 edges
- FreeOtp decrypt incoming exactly 1 (variant E19 E3445b99d, @FILE_FREEOTP dispatch). All three S1a-target auto ids absent (E598edf30 base, E2f10eb15 @FILE-auto, E88e09203 @STRATUM-auto). No GA/Stratum/base/shared-@FILE prefix reaches FreeOtp decrypt. @FILE_FREEOTP file route 38 steps, REACHABLE (R3 item-1 at V4/F0 satisfied). F2 baseline: 0 upstream @FREEOTP nodes. VERDICT: F0 PASS — skipped stage-1 items correctly subsumed by v2; nothing lands.

## F2 stage 2 applied (FreeOtp @FREEOTP app-import chain F1-F13, LAST) — private build, independently audit-PASS, pushed in this commit
- F1-F13 verbatim from helper/freeotp-design/DESIGN.md section 4 stage 2 (see AGENT_NOTES.md F2 entry for the full per-edge record). No version-warning lambdas, no onCreate@FREEOTP side branches; GA edges/label/processDecrypted branch untouched.
- Build: 6326 -> 6366 edges, delta exactly +40 (13 hand + 27 auto), 0 removed; errors 0, warnings 0; methods 2995, 2537/458, 0 flips.
- R4 gates exact: pick 1, <init> 1, onCreate 6, startImport 8, startImportApp 1, onPostExecute 1, lambda$5 4, processImporterState 5 (= 27; processImporterState 10 -> 5 correction confirmed post-v2). FreeOtp decrypt incoming 1 -> 2 (variant file E19 E3445b99d + F13 Eb4ba083b); no other decrypt's incoming set changed.
- Redumps: FreeOtp decrypt 35 steps via @FREEOTP, producer steps exactly F1-F13 in order; DecryptedStateV2.<init> 47 steps via @FREEOTP, downstream password chain unchanged. R3 re-read: overall shortest now the @FREEOTP app route (35 steps); the @FILE_FREEOTP file route (38 steps) survives structurally (0 edges removed) but is no longer shortest.
- Checks: 2: 22/0; 3: 0 flagged; 4: 4218/345/168/0; 5-7: 0; 8: 0/458. Independent audit helper/audit/f2-application/AUDIT.md: PASS.
- Table NOT rewritten here. Next: fix round, then redraw + re-judge, then C4.
