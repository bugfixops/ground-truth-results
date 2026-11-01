# Stream C leaf C — Aegis route steps 6–10 re-derivation (connector-only, NOT pushed, NOT verified for merge)

Status: RE-DERIVED from freshly printed source this session. No file in
bugfixops/ground-truth-results was edited, merged, or pushed. No device work
(no emulator, adb, APKs, new repos). No decision item was decided here.
This report is a proposal/check only; nothing in it counts as a merge verdict
for graph_def.py.

## Method and fetch record

- Input read first in full: `~/workspace/aegis-wp3-steps6-10-report.md`
  (the prior WP3 steps 6–10 helper report).
- Every branch read used the GitHub connector, one file at a time, with
  ~30 s pauses between fetches, on branch `work-2026-10-31`, repo
  `bugfixops/ground-truth-results`. No token was used, waited for, or put in
  any URL, file, commit, log, or message. No 429 was encountered this session;
  no fetch was retried.
- `confirmed_by` below is only SOURCE (lines printed this session) or
  INFERRED (library/generated code, or code not read). No DYN, FW-MEMORY, or
  UNVERIFIED is used as evidence. Tool coverage is not used as evidence.
  No `search_code` result is used as evidence; the one search attempt this
  session failed on argument shape and was abandoned in favour of directory
  listings followed by direct file fetches.
- Files fetched fresh this session (branch `work-2026-10-31`):
  - `graphs/Aegis/scratch/route_check_r7/` (directory listing)
  - `graphs/Aegis/scratch/route_check_r7/GlideRequests_asBitmap.txt`
    (SHA 4a6e3a7deaae793fdd6c61cb3699c63626a54165)
  - `graphs/Aegis/scratch/route_check_r7/Slot_init.txt`
    (SHA 938eff5bb9f3bd46a9c0f7ddb70f456b6aee2d93)
  - `graphs/Aegis/scratch/route_check_r7/sample_r7.txt`
    (SHA 90ab7382d98eb2ca7a74cada67738beed2b3fa8d)
  - `final_java_only/Aegis/app/Aegis-#v3.4.2/app/src/main/java/com/beemdevelopment/aegis/ui/MainActivity.java`
    (1,541 lines; SHA 7ff23b25979b6e022ab3ed719c3ebd4163563eb2)
  - `.../aegis/ui/IntroActivity.java`
    (131 lines; SHA e7aecc1839c082b025835f96dd33398d619014ce)
  - `.../aegis/vault/VaultManager.java`
    (309 lines; SHA 9f981e0323e15e8250e63afeee37517c7dae6235)
  - `fw_src/android-8.1.0_r1/core/java/android/app/ActivityThread.java`
    (6,502 lines; SHA 45f7eba2af02f567bae391f24c3b61bae1c314d3)
  - `graphs/Aegis/graph_def.py` (4,982 lines by splitlines count this session;
    the prior report said 4,983 — the difference is consistent with a
    trailing-newline count and is NOT treated as a graph change)
  - `graphs/Aegis/AGENT_NOTES.md` (669 lines; SHA ff62d457ca067aa0153295821a2e985eb471a3e4)
- Directory listing of `graphs/Aegis/scratch/route_check_r7/` confirms the
  prior report exactly: only three files exist there — the two dumps above
  plus `sample_r7.txt`. The other 23 round-7 dumps are not in the repo.
  A step not printed counts as not checked.

## Route 1: GlideRequests.asBitmap (70 steps) — steps 6–10: CORRECT

Prior verdict (steps 6–10 CORRECT; route as a whole NOT clear) is CONFIRMED
by fresh prints. Round-7 errors on this route are at steps 25, 28, 53, 65
(AGENT_NOTES.md line 652, freshly printed this session) — none in 6–10.
Step 50 is a decision item (below), so the route as a whole is still NOT
clear regardless of steps 6–10.

### Step 6 — CORRECT (SOURCE)
- Dump: `Eb76444fd LIFECYCLE/standard*`, MainActivity.\<init\> ->
  MainActivity.onCreate, "Activity.onCreate after the constructor",
  evidence FW-SRC ActivityThread.java:2729-2731,2741 + SRC
  ui/MainActivity.java:192-194.
- Graph edge: `graphs/Aegis/graph_def.py:310-311` — identical endpoints,
  kind, text, and evidence (`FW_CREATE + '; SRC ui/MainActivity.java:192-194'`).
- Fresh print: MainActivity.java:192-194 is `@Override protected void
  onCreate(Bundle savedInstanceState) { super.onCreate(savedInstanceState);`
  (onCreate continues at :195 with setContentView). ActivityThread.java
  :2729-2731 is `mInstrumentation.callActivityOnCreate(...)` (persistable
  and non-persistable branches) and :2741 is `activity.performStart()`.
- Precision note (not an error): :2741 sits inside `if (!r.activity.mFinished)`
  at :2740, so "then performStart" holds for a non-finished activity, i.e.
  the normal launch case. The dump step does not state that guard.

### Step 7 — CORRECT (SOURCE)
- Dump: `E3a06baed LIFECYCLE/standard*`, MainActivity.onCreate ->
  MainActivity.onStart, "Activity.onStart after onCreate", evidence FW-SRC
  ActivityThread.java:2729-2731,2741 + SRC ui/MainActivity.java:938-940.
- Graph edge: `graph_def.py:314-315` — identical endpoints, kind, text, and
  evidence.
- Fresh print: MainActivity.java:938-940 is `@Override protected void
  onStart() { super.onStart();`. The onStart ordering is the FW performStart
  at ActivityThread.java:2741 (same guard note as step 6).

### Step 8 — CORRECT (SOURCE)
- Dump: `E0602e719 CALL/explicit*`, MainActivity.onStart ->
  MainActivity.startIntroActivity, "no vault file exists (fresh install):
  the intro starts and onStart returns", guard "vault init needed: no vault
  file exists", evidence SRC ui/MainActivity.java:942-948.
- Graph edge: `graph_def.py:400-401` — identical endpoints, kind, text,
  guard, and evidence.
- Fresh print: MainActivity.java:942-948 is exactly `if
  (_vaultManager.isVaultInitNeeded()) { if (_prefs.isIntroDone()) { Toast...
  } startIntroActivity(); return; }`. Supporting semantics, freshly printed:
  VaultManager.java:226-228, `isVaultInitNeeded()` returns
  `!isVaultLoaded() && !VaultRepository.fileExists(_context)` — so the
  "no vault file exists" shorthand is the file-existence half of that test;
  at a fresh-install onStart the not-loaded half is the normal case. This
  is the fresh-install standard-config branch, not the cross-run relaunch
  edge (see Slot step 8). It is distinct from the cold-start decision item.

### Step 9 — CORRECT (SOURCE app part + INFERRED framework part)
- Dump: `E4ce5043a INTENT/standard*`, MainActivity.startIntroActivity ->
  IntroActivity.\<init\>, "startActivityForResult(IntroActivity) through
  introResultLauncher", guard "intro not already running (_isDoingIntro
  false, MainActivity.java:604)", evidence SRC ui/MainActivity.java:603-612
  + INFERRED androidx.activity.result (launcher callback).
- Graph edge: `graph_def.py:482-484` — identical endpoints, kind, text,
  guard, and evidence (`SRC ui/MainActivity.java:603-612; ` + FW_LAUNCHER).
- Fresh print: MainActivity.java:603-609 is exactly `private void
  startIntroActivity() { if (!_isDoingIntro) { Intent intro = new Intent
  (this, IntroActivity.class); introResultLauncher.launch(intro);
  _isDoingIntro = true; } }`. The launcher-callback half is INFERRED, not
  SOURCE: `graph_def.py:138` defines FW_LAUNCHER as "INFERRED
  androidx.activity.result: the launcher callback runs with the result
  (androidx source not cached)". The dump says this itself, so it is not
  presented as SOURCE here.

### Step 10 — CORRECT (SOURCE)
- Dump: `E5e63fbe7 LIFECYCLE/standard*`, IntroActivity.\<init\> ->
  IntroActivity.onCreate, "Activity.onCreate of the intro", evidence FW-SRC
  ActivityThread.java:2729-2731,2741 + SRC ui/IntroActivity.java:35-41.
- Graph edge: `graph_def.py:485` — identical endpoints, kind, text, and
  evidence (`FW_CREATE + '; SRC ui/IntroActivity.java:35-41'`).
- Fresh print: IntroActivity.java:35-41 is exactly `@Override protected
  void onCreate(Bundle savedInstanceState) { super.onCreate(savedInstanceState);
  addSlide(WelcomeSlide.class); addSlide(SecurityPickerSlide.class);
  addSlide(SecuritySetupSlide.class); addSlide(DoneSlide.class); }`.
  The FW half is the same ActivityThread.java:2729-2731,2741 print as
  step 6 (same guard note).
- Note: the dump's parenthetical "(ActivityThread.java not found in the
  source tree)" is stale for the repo copy: the fw_src copy in the repo
  was printed this session and does contain lines 2729-2741. The FW claim
  is SOURCE here, not FW-MEMORY. This matches the prior report's caveat.

### GlideRequests decision item (NOT decided here)
- Step 50 (app import, file null, needs root): decision item, see DECISIONS.md.
  Freshly printed cross-reference: AGENT_NOTES.md line 636 — "GlideRequests
  step 50 (app import, file null, needs root): confirmed
  (ImportEntriesActivity.java:109-111 calls startImportApp; :143-153
  finishes the page when the shell is not root). Not fixed: the app-import
  edge is the router's cheaper choice. Decision for Yang (see HANDOFF_V2.md
  R10-2)." ImportEntriesActivity.java itself was NOT fetched this session,
  so step 50 is not re-judged here; only the decision-item status is
  carried forward.

## Route 2: Slot.\<init\>(UUID,byte[],CryptParameters) (37 steps) — steps 6–10 re-derived

Steps 6–7 are the identical lifecycle edges as GlideRequests steps 6–7 and
are CORRECT on the same fresh prints. Step 8 is the cold-start decision
item: its source mechanics are CORRECT as printed, but its route-validity
is NOT settled here. Steps 9–10 are judged only as far as printed source
settles them; both inherit step 8's decision item, so neither clears the
route. This is a deliberate extension of the prior report, which STOPPED at
step 8 and left steps 9–10 unjudged: the mechanics below are now printed
and judged, but the route-level consequence is explicitly NOT decided.

### Step 6 — CORRECT (SOURCE)
- Dump: `Eb76444fd LIFECYCLE/standard*`, MainActivity.\<init\> ->
  MainActivity.onCreate. Same edge, evidence, and fresh prints as
  GlideRequests step 6 (`graph_def.py:310-311`; MainActivity.java:192-194;
  ActivityThread.java:2729-2731,2741 with the :2740 guard note).

### Step 7 — CORRECT (SOURCE)
- Dump: `E3a06baed LIFECYCLE/standard*`, MainActivity.onCreate ->
  MainActivity.onStart. Same edge, evidence, and fresh prints as
  GlideRequests step 7 (`graph_def.py:314-315`; MainActivity.java:938-940;
  ActivityThread.java:2741 with the :2740 guard note).

### Step 8 — SOURCE MECHANICS CORRECT; ROUTE-VALIDITY IS A DECISION ITEM, see DECISIONS.md (NOT decided here)
- Dump: `E20e76e09 CALL/explicit* [STATE: A plain-text vault file exists
  in the app data, saved by an earlier intro run that chose no security
  (cross-run state, no producer in this run; MainActivity.onStart reads it,
  MainActivity.java:951-973)]`, MainActivity.onStart ->
  MainActivity.loadEntries, "plain-text vault (intro chose no security):
  loaded in onStart", guard "the plain-text vault file is loaded earlier in
  this same onStart call (VaultManager.loadFrom, MainActivity.java:963-965)
  with no early return at 947, 960 or 971, isVaultLoaded() is true
  (MainActivity.java:976-977 not taken), and this instance has not loaded
  the list (else branch at 991-992; _loaded false at 978)", evidence SRC
  ui/MainActivity.java:950-974,991-992.
- Graph edge: `graph_def.py:428-431` — identical endpoints, kind, text,
  guard, `needs_state=ST_PLAIN_VAULT_FILE`, and evidence.
- Fresh print confirms every cited line: MainActivity.java:942-948 is the
  fresh-install branch returning at :947 (not taken on this route, since
  `isVaultInitNeeded()` is false when a vault file exists — VaultManager
  :226-228); :950-974 is the plain-text load block (`readVaultFile` at
  :954, `isEncrypted()` check at :963, `loadFrom` at :965, error returns
  at :960 and :971); :976-977 is `if (!_vaultManager.isVaultLoaded()) {
  startAuthActivity(false); }` (not taken when the load succeeded); :978
  is `} else if (_loaded) {` (not taken when the list is not yet loaded);
  :991-992 is `} else { loadEntries();`.
- Wording precision note (not an error): the dump's "_loaded false at 978"
  is shorthand — :978 is the `else if (_loaded)` test itself, and _loaded
  being false is what falls through to the :991 else branch. The logic is
  correct as printed.
- Why this is still a decision item: the vault file the step reads was
  saved by an earlier intro run; there is no in-run producer of that file
  on this route. Freshly printed cross-references: AGENT_NOTES.md line 538
  ("R2 s8 | E20e76e09 ... OPEN | Fresh install returns at 947, so this
  plain-text edge is wrong for the fresh route, but it is the relaunch
  path. Yang: see the cold-start OPEN item. The standard edge E0602e719
  already exists."); line 558 (OPEN list: "Cold start, fresh install:
  E20e76e09, E57db524e and Ec7af65b2 stay as they are... Yang chooses:
  keep the relaunch edges and mark the routes non-standard, or split
  onStart into relaunch and fresh variants."); line 655 ("Slot... Step 8
  reclassified to UNCLEAR (D2)"). No decision is made here; the step is
  neither cleared nor rejected at route level.

### Step 9 — CORRECT (mechanics, SOURCE); ROUTE-VALIDITY INHERITS STEP 8's DECISION ITEM
- Dump: `Ea76ae1a0 ENTERS/page*`, MainActivity.loadEntries -> S_LIST,
  "the list is shown (vault loaded, list loaded in this instance)", guard
  "list not yet loaded in this instance (_loaded false,
  MainActivity.java:1134) and the vault is loaded (getVault() throws when
  none is loaded, VaultManager.java:231-233): a producer of the loaded
  vault must come earlier on the route (the intro result, or an unlock)",
  evidence SRC ui/MainActivity.java:1133-1144 + SRC
  vault/VaultManager.java:231-233.
- Graph edge: `graph_def.py:711-713` — identical endpoints, kind, text,
  guard, and evidence.
- Fresh print: MainActivity.java:1133-1144 is exactly `private void
  loadEntries() { if (!_loaded) { setGroups(...getUsedGroups());
  ...setEntries(...getEntries()); ... _loaded = true; } }`, and
  VaultManager.java:231-233 is exactly `public VaultRepository getVault()
  { if (!isVaultLoaded()) { throw new IllegalStateException("Vault manager
  is not initialized");`.
- Caveat that limits this verdict: on THIS route the earlier producer is
  step 8's `loadFrom` from the cross-run plain-text file, which the guard
  text does not name (it names "the intro result, or an unlock"). The
  mechanics are SOURCE-correct, but step 9 does not independently settle
  the producer question — it inherits step 8's decision item, see
  DECISIONS.md. Steps 9–10 are therefore NOT a clearance of the Slot route.

### Step 10 — CORRECT (SOURCE app part + INFERRED framework part); ROUTE-VALIDITY INHERITS STEP 8's DECISION ITEM
- Dump: `E887b87bf GUI/standard*`, S_LIST ->
  MainActivity.onOptionsItemSelected, "Tap an item in the list toolbar or
  overflow menu: the lock icon, Settings, About or a sort option",
  evidence INFERRED androidx.appcompat (tap calls onOptionsItemSelected,
  source not read) + SRC ui/MainActivity.java:1086-1118.
- Graph edge: `graph_def.py:834-835` — `gui('S_LIST',
  'MainActivity.onOptionsItemSelected', 'Tap an item in the list toolbar
  or overflow menu: the lock icon, Settings, About or a sort option',
  evidence=FW_MENU + '; SRC ui/MainActivity.java:1086-1118')`.
- Fresh print: MainActivity.java:1086-1118 is exactly the
  `onOptionsItemSelected` dispatch (settings at :1088-1089, about at
  :1090-1092, lock at :1093-1094, sort-category branches at :1096-1118).
  The tap-to-callback dispatch is INFERRED, not SOURCE: `graph_def.py:154`
  defines FW_MENU as "INFERRED androidx.appcompat: a tap on a toolbar menu
  item calls onOptionsItemSelected (source not read)". The dump says this
  itself.
- Route-level caveat: as with step 9, this step's correctness as a
  mechanism does not clear the route, because reaching S_LIST on this
  route depends on step 8's decision item, see DECISIONS.md.
- Round-7 errors on this route at steps 21, 27, 30 (AGENT_NOTES.md line
  655, freshly printed) are outside this slice and remain open; they are
  not re-judged here.

## Tensions recorded explicitly (NOT resolved by assumption)

### Tension 1: MainActivity.onIntroResult step 21 — ERROR + decision (round 6) vs clean (round 7) vs still open in handover
- Side A (freshly printed): AGENT_NOTES.md line 599 — "Route 1,
  MainActivity.onIntroResult, step 21 = E1dcf1457 (RESULT,
  IntroActivity.onDonePressed -> MainActivity.lambda$new$1). ERROR
  confirmed: its guard needs the vault created by initNew
  (IntroActivity.java:100), but the route has no edge that reaches initNew,
  and the RESULT edge has no needs_state, so the router skips the producer
  (the NONE path with creds null passes the check at :92-96). Not fixed in
  this batch: a fix needs a continuation node after initNew (no RETURN kind
  exists in build_graph.py KINDS), so this is a modelling decision for
  Yang."
- Side B (freshly printed): AGENT_NOTES.md line 666 — round-7 "Clean (no
  UNCLEAR): MainActivity.onIntroResult (24), Hilt_AegisApplication.\<init\>
  (2), AegisApplication.\<init\> (1)." And line 669 — "No graph edit made
  this round, so round 8 would re-check the same graph and give the same
  verdicts."
- Side C (from the prior report, NOT re-printed this session): the prior
  report states AGENT_NOTES round-6 line 611 says the step-21 edge was
  fixed via the @SAVED variant, and the handover still lists route 1 step
  21 as open. The @SAVED-variant claim was NOT verified by a fresh print
  this session (the lines printed around 599–610 this session do not
  contain it), so it is carried here only as a prior-report claim, not as
  a fresh finding.
- Why this is unresolved: the round-6 route (step 21 of an older sample)
  and the round-7 route (24 steps, sample_r7.txt, freshly printed this
  session) are different samples, so "clean" in round 7 does not by itself
  prove the round-6 step-21 error was fixed, and the handover's
  still-open listing points the other way. Do NOT treat onIntroResult
  step 21 as closed until Yang decides and a fresh show_route is printed.
  The onIntroResult dump itself is NOT in the repo (see NOT-CHECKED list),
  so no step verdict for that route is claimed here.

### Tension 2: Slot step 8 — fresh-install route vs relaunch route
- The same edge E20e76e09 is simultaneously the correct relaunch path
  (AGENT_NOTES.md line 538: "it is the relaunch path") and wrong for the
  fresh-install route (same line: "Fresh install returns at 947, so this
  plain-text edge is wrong for the fresh route"), with the standard fresh
  edge E0602e719 already existing (GlideRequests step 8, CORRECT above).
  AGENT_NOTES.md line 558 leaves the choice to Yang (keep relaunch edges
  and mark routes non-standard, or split onStart). Recorded, not resolved.

### Tension 3 (carried, not re-checked): prior-report decision items for other routes
- The prior report's other decision items (route 4 step 9 icon-pack
  leftover, EntryAdapter search step 14 two-process route, G3_5 step 34
  Authy row-tap, GoogleAuthImporter step 24 row-tap edge) concern routes
  whose dumps are NOT in the repo. They are NOT re-verified here and are
  listed only so they are not silently dropped: each is a decision item,
  see DECISIONS.md, and each awaits its own printed dump (see print
  requirements below).

## All other round-7 routes — NOT CHECKED (not printed)

Source of the list: `graphs/Aegis/scratch/route_check_r7/sample_r7.txt`
(seed 20261025), freshly printed this session: 25 routes total. Two are
checked above (GlideRequests.asBitmap, 70 steps; Slot.\<init\>, 37 steps).
The remaining 23 have no dump in `graphs/Aegis/scratch/route_check_r7/`
(directory listing freshly printed this session). NO step verdict — for
steps 6–10 or any other step — is claimed for them. Guessing a verdict
from AGENT_NOTES round-7 error summaries alone would violate the
not-printed rule, so none is given, including for the routes that carry
decision items.

| # | Route (sample_r7.txt, verbatim) | Steps in sample | What is needed to check steps 6–10 |
|---|---|---|---|
| 1 | VaultBackupManager$FileInfo.throwBadFormat | 31 | show_route re-run on a reconstructed checkout; save dump to graphs/Aegis/scratch/route_check_r7/VaultBackupManager_throwBadFormat.txt (name to match the route); then match dump steps 6–10 to graph_def.py edges and print every cited app + fw_src line fresh |
| 2 | EntryAdapter.setTempHighlightEntry | 27 | Same show_route re-run + dump save + edge match + fresh line prints |
| 3 | MOTP.\<init\> | 22 | Same show_route re-run + dump save + edge match + fresh line prints |
| 4 | MainActivity.importScannedEntries | 21 | Same show_route re-run + dump save + edge match + fresh line prints |
| 5 | IconPack$Icon.\<init\> | 19 | Same show_route re-run + dump save + edge match + fresh line prints |
| 6 | ImportExportPreferencesFragment$ExportResultListener.onTaskFinished | 56 | Same show_route re-run + dump save + edge match + fresh line prints |
| 7 | GoogleAuthProtos$MigrationPayload$DigitCount$DigitCountVerifier.\<init\> | 32 | Same show_route re-run + dump save + edge match + fresh line prints |
| 8 | IconPackExistsException.getIconPack | 30 | Same show_route re-run + dump save + edge match + fresh line prints |
| 9 | MainActivity.onIntroResult | 24 | Same show_route re-run + dump save + edge match + fresh line prints; this is also the print needed to settle Tension 1 above (step 21 in the old sample vs the 24-step round-7 route) |
| 10 | Dialogs.lambda$showPartialGoogleAuthImportWarningDialog$30 | 24 | Same show_route re-run + dump save + edge match + fresh line prints |
| 11 | ImportExportPreferencesFragment.lambda$onImportSelectResult$11 | 30 | Same show_route re-run + dump save + edge match + fresh line prints |
| 12 | AuthActivity.lambda$onCreate$3 | 14 | Same show_route re-run + dump save + edge match + fresh line prints |
| 13 | GoogleAuthImporter.readFromApp | 35 | Same show_route re-run + dump save + edge match + fresh line prints; step 24 on this route is a decision item, see DECISIONS.md (AGENT_NOTES.md line 659, freshly printed) |
| 14 | ApkSignaturePin.getSignatures | 11 | Same show_route re-run + dump save + edge match + fresh line prints |
| 15 | ScannerActivity.onOptionsItemSelected | 19 | Same show_route re-run + dump save + edge match + fresh line prints |
| 16 | Dialogs.lambda$showDetailedMultiErrorDialog$22 | 36 | Same show_route re-run + dump save + edge match + fresh line prints |
| 17 | VaultGroup.equals | 28 | Same show_route re-run + dump save + edge match + fresh line prints |
| 18 | OtpInfo.isAlgorithmValid | 17 | Same show_route re-run + dump save + edge match + fresh line prints |
| 19 | GlideOptions.clone | 15 | Same show_route re-run + dump save + edge match + fresh line prints |
| 20 | EntryAdapter.lambda$doesAnyGroupMatchSearchFilter$1 | 15 | Same show_route re-run + dump save + edge match + fresh line prints; step 14 on this route is a decision item, see DECISIONS.md (prior-report item 4; not re-printed this session) |
| 21 | Salsa20Engine.salsaCore | 25 | Same show_route re-run + dump save + edge match + fresh line prints |
| 22 | Hilt_AegisApplication.\<init\> | 2 | No steps 6–10 exist in a 2-step route: show_route re-run to confirm the step count only; there is nothing to judge for steps 6–10 |
| 23 | AegisApplication.\<init\> | 1 | No steps 6–10 exist in a 1-step route: show_route re-run to confirm the step count only; there is nothing to judge for steps 6–10 |

General print requirement for rows 1–21: a reconstructed checkout (full
local clone or connector reconstruction with the tools available) running
the route tool that produced the round-7 dumps, with the dump saved under
`graphs/Aegis/scratch/route_check_r7/`. Until that dump exists, the route
stays NOT CHECKED. The prior report's note that AGENT_NOTES says dumps
were in "scratchpad r7/" outside the repo copy is consistent with the
fresh directory listing (only 2 dumps + sample in the repo), but the
outside-repo location was not verified this session and no file was
retrieved from it.

## What was NOT done (explicit)
- No push, no branch edit, no graph_def.py edit, no other app touched.
- No build, sampler, grep, or C1 check run (no local checkout in this
  session); no such count is claimed.
- No Yang/decision item decided: GlideRequests step 50, Slot step 8
  (cold-start E20e76e09), onIntroResult step 21, and the other
  decision items above are all carried as decision items, see DECISIONS.md.
  Note: DECISIONS.md itself was not fetched or verified this session; the
  cross-reference label is used per the task instruction, and every item
  text above is grounded in the AGENT_NOTES.md lines cited (freshly
  printed this session unless marked as prior-report-only).
- Brief steps 6–10 (Paths / Log / Notes / Final checks / Lessons) are
  outside this leaf's re-derivation task and are not re-reported here;
  the prior report's PENDING status for them is unchanged by this session.
