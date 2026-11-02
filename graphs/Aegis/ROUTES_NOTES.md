# Aegis ROUTES_NOTES — per-route companion to the final route table

Purpose: the per-route companion to the final route table — one
entry per final-sample route, recording the judged verdict and, in this push, the staged device script and the still-empty device result for that route.
It does not replace the route table, the fix log, or
`device/routes/Aegis/ROUTES.csv`. Built from the NEW table only
(`turn/table/ROUTE_TABLE_NEW.md`, audit-PASS); the old outline's
sole-WRONG RawSlot row and its old count of 10 UNCLEAR routes are
NOT carried over. Device scripts are staged in this push (see the per-route entries); no device result is claimed: every device result below is TO-FILL after the first real run, and no real emulator run was started.

Header: app Aegis; final build (V3-corrected) 2995 methods, 2537
REACHABLE / 458 UNREACHABLE, 6430 edges, errors 0, warnings 0;
sample seed 20261025, 25 routes, 1093 steps, 446 distinct edges;
table tally CORRECT 13 / WRONG 1 / UNCLEAR 11, fixed 2 (AndOtp,
Stratum), distinct rate 3/14 = 0.2143, table rate 3/16 = 0.1875;
sample file: redraw sampler output (seed 20261025); table file:
`turn/table/ROUTE_TABLE_NEW.md`. Rule: a route's entry is updated
only from its own judged dump / device result, never by copying
another route's entry. Order below is sampler order (the new
table's order), NOT the old table's order: RawSlot first within
INFERRED; within ENV, Scanner first and AegisImporter third.

Per-route entry template (applied to all 25 entries below):
route number; method; steps; verdict (from the new table);
decisive steps with reasons (named steps for WRONG and UNCLEAR
routes, as in the table); device script path and status (staged in this push: firm, draft/TO-ASSESS, or unscriptable with reason); device result (TO-FILL after the first real run); notes / follow-ups.

## Entries

### 1. AndOtpImporter$EncryptedState.decryptNewFormat(SecretKey) — 67 steps — CORRECT (fixed)
Decisive: none adverse. Step 26 vault-load satisfied in-run by
step 21 initNew (VaultManager.java:59-72). Carried from old table
row 1, edge-identical. Device script: staged at device/routes/Aegis/route_01.py (draft, TO-ASSESS: system picker plus password dialog; run-time generated AndOTP backup; picker navigation and named-importer row tap open). Device
result: TO-FILL after the first real run. Notes: fixed route
(first-draw WRONG -> final CORRECT).

### 2. FreeOtpImporter$DecryptedStateV2.<init> — 64 steps — UNCLEAR
Decisive: step 48 root shell needs rooted device + su grant (not
in declared config, no in-run producer); step 50 non-root shell
-> toast + finish (ImportEntriesActivity.java:143-174); step 52
installed FreeOTP V2 tokens.xml data, no in-run producer. Not
WRONG: nothing listed contradicts root/FreeOTP presence. Steps
53-64 individually CORRECT but conditional on step 52. Carried
from old table row 2, edge-identical. Device script: NONE (unscriptable: rooted device plus su grant plus installed FreeOTP V2 tokens.xml data; no in-run producer, table steps 48, 50, 52; adb root does not provide the app's libsu su call). Device result: TO-FILL after the first real run.

### 3. StratumImporter$EncryptedState.decrypt(SecretKey) — 65 steps — CORRECT (fixed)
Decisive: none adverse. Step 26 as row 1; picked Stratum file +
password via in-run picker/password actions. Carried from old
table row 3, edge-identical. Device script: staged at device/routes/Aegis/route_03.py (draft, TO-ASSESS: system picker plus password dialog; run-time generated Stratum backup; picker navigation and named-row tap open; corrected @FILE prefix, not the removed @STRATUM edge).
Device result: TO-FILL after the first real run. Notes: fixed
route (first-draw WRONG -> final CORRECT); Stratum file-path
fallback edge correction (removed, 0 label flips) is on record
in AGENT_NOTES and is not re-argued here.

### 4. TwoFASImporter$EncryptedState.deriveKey — 63 steps — CORRECT
Decisive: none adverse. Step 26 producer step 21 initNew; step 55
TwoFAS EncryptedState from a TwoFAS file; steps 61-63 password
lambda -> decrypt(char[]) -> deriveKey, all inside TwoFAS. No
cross-importer step. Carried from old table row 4,
edge-identical. Device script: staged at device/routes/Aegis/route_04.py (draft, TO-ASSESS: system picker plus password dialog; run-time generated TwoFAS backup; picker navigation and named-row tap open). Device
result: TO-FILL after the first real run.

### 5. RawSlot.getType — 42 steps — UNCLEAR
Decisive: CHANGED from old table row 8 (WRONG, 49 steps) ->
UNCLEAR (42 steps, new @IMP route). Every step TRUE on action and
operative condition (REJUDGE.md step tables 1-42); no step false.
Load-bearing premise U2 producer-less: `new RawSlot` occurs
exactly once in main app source, at Slot.java:133 inside fromJson
(the parser); no app code writes a type-0 slot, no migration
produces one, no producer in evidence — so CORRECT is not
established, while WRONG would require a false step (none found)
and NOT-ROUTABLE would require a rejection/strip/unreachable
dispatch (parser explicitly accepts type 0, step-41 dispatch is a
real iterated call). INFERRED legs steps 2-3, 22 accepted as
caveats; stale Auth-leg guard/provenance text on steps 34-39 and
41 recorded as DEBT (see table notes). New @IMP prefix edges
I1-I8, L1-L3; tail edges as listed in new table row 5. Fresh dump
header path=WRONG is carried post-vault label metadata, NOT this
verdict. Revised-fix pointer: see AGENT_NOTES RawSlot revised fix
section (this C4 package, AGENT_NOTES_DELTAS.md Delta 1) — the
revised fix section, NOT a device result, is this route's
follow-up pointer. Device script: staged at device/routes/Aegis/route_05.py (draft, TO-ASSESS: Welcome import picker plus imported vault containing a type-0 slot, then assign-groups dialog OK, then save chain; open whether Welcome import unlocks the type-0 file with no password step, as the drawn chain requires). Device
result: TO-FILL after the first real run.

### 6. TotpAuthenticatorImporter$EncryptedState.lambda$decrypt$0 — 62 steps — CORRECT
Decisive: none adverse. Step 55 file/external branch (internal
branch would yield DecryptedState, never reach decrypt); steps
56/62 Yes-path lambda numbering corroborated by javac
inner-before-outer pattern. Carried from old table row 5,
edge-identical. Device script: staged at device/routes/Aegis/route_06.py (draft, TO-ASSESS: system picker plus password dialog; run-time generated TOTP Authenticator backup; picker navigation and named-row tap open). Device
result: TO-FILL after the first real run.

### 7. AuthenticatorPlusImporter$EncryptedState.decrypt(char[]) — 62 steps — CORRECT
Decisive: none adverse. Step 55 read always returns EncryptedState;
steps 61-62 password lambda -> decrypt(char[]), both inside
AuthenticatorPlus. Carried from old table row 6, edge-identical.
Device script: staged at device/routes/Aegis/route_07.py (draft, TO-ASSESS: system picker plus password dialog; run-time generated Authenticator Plus backup; picker navigation and named-row tap open). Device result: TO-FILL after
the first real run.

### 8. AuthyImporter$EncryptedState.decrypt(char[]) — 62 steps — CORRECT
Decisive: none adverse. Dispatch stays Authy at every step
(Dialogs.java:515-531; DatabaseImporter.java:37;
AuthyImporter.java:101-135,157-162,165-203,207-214). Step 26
producer step 21 initNew. Carried from old table row 7,
edge-identical. Device script: staged at device/routes/Aegis/route_08.py (draft, TO-ASSESS: system picker plus password dialog; run-time generated Authy backup; picker navigation and named-row tap open). Device
result: TO-FILL after the first real run.

### 9. IconAdapter$CategoryHeader.getPosition — 58 steps — UNCLEAR
Decisive: step 46 dump jumps from ImportEntriesActivity.onCreate
to the save-button tap, omitting the GA app-import sub-flow
(startImportApp/RootShellTask, ImportEntriesActivity.java:143-172;
GA package read, GoogleAuthImporter.java:60-68) — root +
installed GA app + import result never produced on route; step 48
assign-icons dialog requires an installed icon pack
(ImportEntriesActivity.java:320-322; IconPackManager.java:45-47),
no step installs one on a fresh-install route. Neither
contradicted. Tail 49-58 printed and correct. Carried from old
table row 9, edge-identical. Device script: NONE (unscriptable: drawn route omits the Google Authenticator app-import sub-flow needing root plus an installed Google Authenticator app plus its import result, table step 46, and the assign-icons dialog requires an installed icon pack, step 48; creating entries in-run cures neither precondition).
Device result: TO-FILL after the first real run.

### 10. EntryAdapter.setTempHighlightEntry — 44 steps — CORRECT
Decisive: none adverse. Step 26 producer steps 21-22 initNew;
suffix creates its own entry in-run (FAB -> manual entry -> save
-> result -> highlight); step 44 reached regardless of scroll
branch at step 43. Carried from old table row 10, edge-identical.
Device script: staged at device/routes/Aegis/route_10.py (firm: pure in-app flow, entry created in-run; dry-loads in staging, not device-proven). Device result: TO-FILL after
the first real run.

### 11. GroupAdapter.getGroupByUUID — 52 steps — UNCLEAR
Decisive: step 41 addGroup loop body runs only if the vault
already has a group (GroupManagerActivity.java:90-95); fresh vault
has none (Vault.java:16-17, initNew bare Vault); no group producer
in steps 1-40; no add-group UI. Satisfiable only by unlisted
in-run action. Steps 42-52 inherit, otherwise mechanically sound.
Carried from old table row 11, edge-identical. Device script: staged at device/routes/Aegis/route_11.py (firm: group created in-run first through the group-manager UI, supplying the group the drawn loop requires; dry-loads in staging, not device-proven). Device result: TO-FILL after the first real
run.

### 12. ScannerActivity.lambda$onQrCodeDetected$1 — 43 steps — CORRECT
Decisive: none adverse. Step 26 producer initNew
(VaultManager.java:66-68, _repo set, getVault() does not throw);
step 43 target via printed dialog OK listener
(ScannerActivity.java:194-196). Carried from old table row 13
(ENV order changed: first in ENV in the new draw, was second),
edge-identical. Device script: staged at device/routes/Aegis/route_12.py (draft, TO-ASSESS: live-camera QR scan to the scanner error-dialog OK target; emulator camera feeding open, no frame-injection primitive exists). Device
result: TO-FILL after the first real run.

### 13. ImportExportPreferencesFragment$ExportResultListener.onTaskFinished — 49 steps — CORRECT
Decisive: none adverse. Plain-export path end to end: step 43
exportPlainResultLauncher for Aegis format without encryption
(ImportExportPreferencesFragment.java:403-405); step 46
export(stream, null) (483-490). No dumped step demands an
encrypted vault. Carried from old table row 14, edge-identical.
Device script: staged at device/routes/Aegis/route_13.py (draft, TO-ASSESS: plain export via system document creator; document-creator picker navigation and export destination open). Device result: TO-FILL after
the first real run.

### 14. AegisImporter$DecryptedState.getCredentials — 30 steps — CORRECT
Decisive: none adverse. Step 19 encrypted branch
(WelcomeSlide.java:60-69, AegisImporter.read:45-53); step 28
non-null decrypt result from listed password steps 22-24; step 30
cast safe (decrypt(creds) returns DecryptedState,
AegisImporter.java:70-78). Carried from old table row 12 (ENV
order changed: third in ENV in the new draw, was first),
edge-identical. Device script: staged at device/routes/Aegis/route_14.py (draft, TO-ASSESS: Welcome-slide import of an encrypted Aegis vault file plus password; generated vault acceptance plus Welcome-picker navigation open). Device
result: TO-FILL after the first real run.

### 15. IconPackExistsException.getIconPack — 47 steps — UNCLEAR
Decisive: step 46 Exists dialog requires a pre-existing installed
pack (IconPackManager.java:84-89); no step 1-45 installs one;
step-43 import cannot be its own producer (throws before
installing). Satisfiable by unlisted in-run action (import same
pack once earlier, then re-import). Carried from old table row 15,
edge-identical. Device script: staged at device/routes/Aegis/route_15.py (draft, TO-ASSESS: icon-pack import via system picker, then Exists dialog; the table's cure, importing the same pack once earlier then re-importing, is scripted in-run; generated pack acceptance plus picker navigation open). Device
result: TO-FILL after the first real run.

### 16. GoogleAuthProtos$MigrationPayload.parser — 41 steps — UNCLEAR
Decisive: step 41 parser() accessor rests on the generated
protobuf class, absent from the tree (verified by search).
ParseFrom call site (GoogleAuthInfo.java:198) and proto definition
(google_auth.proto, MigrationPayload) verified. Step 26 producer
steps 21-22 initNew. Carried from old table row 16,
edge-identical. Device script: staged at device/routes/Aegis/route_16.py (draft, TO-ASSESS: scan-image flow, picker returns an image, decode, parseExportUri to parser; generated QR-image acceptance, picker navigation, and decode path open). Device
result: TO-FILL after the first real run.

### 17. AuthActivity.lambda$onCreate$3 — 36 steps — WRONG (sole WRONG route)
Decisive: NEW row (not in the old table; entered on the 9–9 ENV
coverage tie, see Migration). Two independent false steps, each
shown false on printed app source. Step 28 (lock-icon tap ->
VaultManager.lock): FALSE — updateLockIcon sets the lock item
visible only when the vault is encrypted
(MainActivity.java:1155-1160), applied from onCreateOptionsMenu
(:1015) and the onStart path (:1004) before any tap at S_LIST;
this route's vault is unencrypted (steps 21-22 initNew(null) ->
_creds null -> isEncryptionEnabled false,
VaultRepository.java:352-354), so the item is hidden and cannot
be tapped; the action_lock branch (:1093-1094) is the only
onOptionsItemSelected path to lock, and non-menu lock callers
call lock(false), which cannot produce drawn steps 30-36 since
onLocked only starts AuthActivity when userInitiated is true.
Step 35 (biometric-button tap): FALSE — button visible only with
a BiometricSlot + keystore key (AuthActivity.java:132-150,
Header(null,null) at VaultFile.java:102-105, step-8/21–22
contradiction: step 8 requires no vault file at launch, steps
21-22 save a new NONE vault overwriting any earlier biometric
vault). Steps 1–27 + 36 true, steps 29–34 true-if-reached but
unreached (with the audit N3 qualification for steps 33–34, see
table notes). FIXED-INELIGIBLE: not in the first-draw sample, so
it cannot count as fixed under the strict definition whatever its
verdict. Revised-fix pointer: NO revised fix is drafted here;
any fix is future merger work with fresh judging, not a device
result. Device script: NONE (unscriptable as drawn: step 28 lock-icon tap impossible on the unencrypted vault and step 35 biometric-button tap impossible; changing the vault type would be a different route, not this one; no harness extension cures as-drawn false steps). Device result:
TO-FILL after the first real run (a device result cannot
overwrite this WRONG verdict; it can only record the device
observation separately).

### 18. AuditLogDao_Impl.__EventType_enumToString — 22 steps — UNCLEAR
Decisive: step 8 checkIconOptimization demands a loaded vault
(VaultManager.java:231-233) but steps 1-7 contain no producer (no
intro/initNew/unlock; onStart plaintext-load branch itself needs
a pre-existing vault file = cross-run state); step 13
scheduleBackup requires encrypted vault + pref_backups (defaults
false, Preferences.java:400-401, no in-run producer); steps 19-22
generated AuditLogDao_Impl absent (only @Dao interface + Room
wiring printed). Carried from old table row 18, edge-identical.
Device script: staged at device/routes/Aegis/route_18.py (draft, TO-ASSESS, two-phase: old-format vault import plus backups enablement, then kill and relaunch plus Room tail; old-format acceptance, backups-location picker, fresh-instance trigger, and Room tail mapping open; NOT in the cap-acceptance set, it stays TO-ASSESS). Device result: TO-FILL after
the first real run.

### 19. SlotIntegrityException.<init>(Throwable) — 50 steps — UNCLEAR
Decisive: step 38 pin-keyboard preference visible only when vault
encrypted (SecurityPreferencesFragment.java:259-265;
preferences_security.xml:86); in-run vault is NONE intro vault,
hence unencrypted (IntroActivity.java:92-93;
VaultRepository.java:352-353). Unlisted enable-encryption visit
would satisfy it, contradicted by no listed step. Throw site
Slot.java:57. Step 26 producer steps 21-22 initNew. Carried from
old table row 19, edge-identical. Device script: staged at device/routes/Aegis/route_19.py (firm: encryption enabled in settings first in-run, then wrong-PIN trigger; dry-loads in staging, not device-proven). Device result: TO-FILL after the first real run.

### 20. IconPack$Icon.<init> — 19 steps — UNCLEAR
Decisive: steps 8-13 Hilt/Dagger injection chain rests on
generated code absent from the tree (zero Hilt_*.java /
Dagger*.java found); printed anchors do not verify the generated
edges. Step 16 independently UNCLEAR under STRICT step-8 (icon
pack is cross-run state, no in-run producer; rescan only reads
the existing icons folder, IconPackManager.java:132-165).
Carried from old table row 20, edge-identical. Device script: staged at device/routes/Aegis/route_20.py (draft, TO-ASSESS, two-phase: run-time generated pack install, then kill and relaunch so the rescan finds it; pack install acceptance, picker navigation, and kill/relaunch rescan open). Device result: TO-FILL after the first real
run.

### 21. Salsa20Engine.salsaCore — 25 steps — CORRECT
Decisive: none adverse. Setup-slide not-finished state is the
normal pre-derivation state (fresh empty credentials,
SecuritySetupSlide.java:97); tail printed direct calls through
SCrypt.java:90/122/188/210 to salsaCore (Salsa20Engine.java:32).
Carried from old table row 21, edge-identical. Device script: staged at device/routes/Aegis/route_21.py (firm: intro setup-slide password typed in-run, SCrypt to salsaCore; dry-loads in staging, not device-proven). Device result: TO-FILL after the first real
run.

### 22. EditEntryActivity.deleteAndFinish — 38 steps — UNCLEAR
Decisive: step 27 long-press: in-run vault created empty by
initNew (non-import intro branch), so no row exists to press;
unlisted add-entry visit (FAB -> startEditEntryActivity) can
supply one. Step 26 CORRECT (initNew step 21 is the STRICT step-8
producer). Steps 28-38 printed-correct conditional on step 27's
row. Carried from old table row 22, edge-identical. Device script: staged at device/routes/Aegis/route_22.py (firm: entry added via FAB first in-run, then long-press, action mode, edit, delete; dry-loads in staging, not device-proven). Device result: TO-FILL after the
first real run.

### 23. GoogleAuthProtos$MigrationPayload$DigitCount$DigitCountVerifier.<init> — 49 steps — UNCLEAR
Decisive: step 40 needs at least 1 qualifying TOTP/HOTP SHA-1
6-digit entry (in-run vault holds 0); step 42 Next visible only
if batch list size is not 1, i.e. at least 2 batches of 10 = at
least 11 entries (in-run count 0); steps 45-49 generated-protobuf
tail UNCLEAR (no GoogleAuthProtos source file in tree, only
references in GoogleAuthInfo.java:7,400,459). Carried from old
table row 23, edge-identical. Device script: staged at device/routes/Aegis/route_23.py (firm: 11 qualifying manual entries created first in-run; dry-loads in staging, not device-proven). Device result: TO-FILL after the first real run.

### 24. Hilt_AegisApplication.<init> — 2 steps — CORRECT
Decisive: manifest android:name leg + @HiltAndroidApp leg under
fixed-(c). Header-token note: fresh dump header path=SOURCE_OK
vs old dump path=UNCHECKED — pre-existing label metadata only;
step lines and edge ids identical, verdict unchanged. Carried
from old table row 24, edge-identical. Device script: staged at device/routes/Aegis/route_24.py (firm: app launch only; dry-loads in staging, not device-proven). Device result: TO-FILL after the first real run.

### 25. AegisApplication.<init> — 1 step — CORRECT
Decisive: manifest leg alone. Header-token note: same as row 24
(path UNCHECKED -> SOURCE_OK, pre-existing label metadata only);
step line and edge id identical, verdict unchanged. Carried from
old table row 25, edge-identical. Device script: staged at device/routes/Aegis/route_25.py (firm: app launch only; dry-loads in staging, not device-proven). Device result: TO-FILL after the first real run.

## Closing section: routes with no device result yet

All 25 routes have no device result yet. Device scripts are staged in this push (22 scripted, 3 unscriptable); ROUTES_NOTES is updated again after the first real device run (results per route). It is not a device-completion claim, and no entry above claims a device outcome.
UNCLEAR count in this file is 11 (rows 2, 5, 9, 11, 15, 16, 18,
19, 20, 22, 23) — NOT the old outline's 10. The sole WRONG route
is Auth (row 17) — NOT RawSlot. Any future edit that changes a
verdict must re-judge the route and update this file from the new
table, never by editing a verdict in place here.
