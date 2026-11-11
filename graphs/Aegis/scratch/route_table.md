# Aegis — NEW final route table (post-fix redraw, V3-corrected)

Sample: `python3 -I tools/verify_sample.py Aegis 30 20261025` on the
6430-edge V3-corrected build (apply-v3 after-staging, copied to
`turn/redraw/work/`). 25 routes, 1093 steps, 446 distinct edges, seed
20261025. Fresh dumps at
`turn/redraw/work/dumps/routes_sample_new.txt` (13,701 lines, 25 blocks);
fresh methods at `turn/redraw/work/graphs/Aegis/out/methods.csv`.
Sampler order below is the redraw sampler output order, NOT the old
table's order: RawSlot moves first within INFERRED, and within ENV
Scanner moves first and AegisImporter moves third.

## Conventions applied (binding, carried from the old table unless noted)

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
  already stands on an independent WRONG step.
- `fixed` in the error rate means first-draw WRONG → final CORRECT,
  strictly. A first-draw WRONG route that grades UNCLEAR after its fix
  leaves the denominator (it is neither fixed nor wrong in the rate); a
  route not in the first-draw sample cannot be fixed. See the fixed
  verification in the Tally and in RECOMPUTE.md.
- Operative-condition basis (merger-adopted, see Table notes): a step is
  judged on its action and operative condition, not stale provenance text.
  See the stale-guard disposition in the Table notes.
- Framework-file note: several dumps claim framework files "not found";
  helpers personally printed ActivityThread, View, AsyncTask, AbsListView
  lines in this tree (under `fw_src/android-8.1.0_r1/core/java/android/`,
  not the dumps' `frameworks/base/` prefix — a citation-path correction,
  not a grading change). The generated Hilt/Dagger classes and generated
  protobuf classes genuinely are absent, and steps resting on them are
  graded accordingly (see rows 20 and 23, as in the old table's rows 20
  and 23).
- The final table covers ONLY the final draw, per the brief's redraw rule
  and the path-(A) ruling. Dropped rows' verdicts are superseded, not
  carried over; their reasons stay on record in the old table.

## Per-route verdicts (sampler order)

ENV/STATE kinds are the fresh methods.csv `env_kinds` / `state_kinds`
fields, verified against the fresh dump headers (`-` = empty in both).
Edge-id lists are the fresh methods.csv `route_edge_ids`, verified
identical (same ids, same order) to the fresh dump block for every row.
"Carried" rows are edge-identical to the old table's route (see
Verification below); their verdicts and decisive summaries are carried
unchanged from `merger/scratch/route_table_postvault.md`.

| # | Stratum | Method | Steps | ENV | STATE | Verdict | Decisive steps / trace | Edge ids (fresh dump / methods.csv, in order) |
| 1 | NONSTD | AndOtpImporter$EncryptedState.decryptNewFormat(SecretKey) | 62 | other_app | - | CORRECT (fixed) | W8 re-verified 2026-11-07 (first verification: CORRECT (fixed); re-check: CORRECT). New steps 8-20: the baseline vault is password-protected (Q3), so onStart opens the unlock screen (MainActivity.java:942-977, 1146-1153), the password is typed and Unlock tapped (AuthActivity.java:167-178), the slot decrypts (PasswordSlotDecryptTask.java:87-90) and finish loads the vault and returns RESULT_OK (AuthActivity.java:295-311, 343-356; MainActivity.java:132-140, 797-801); this replaces the intro run of the old route. New step 39 carries the picker env (ImportExportPreferencesFragment.java:146-148). The rest as before. Earlier: Carried from old table row 1. None adverse. Step 26 vault-load satisfied in-run by step 21 initNew (VaultManager.java:59-72). Trace: route_table_postvault.md row 1; edge-identical (see Verification). | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed Eef600725 E06202b0e E0158aff6 E911809ef E87843ac5 E4520b83d Ec2a7b2f4 E9ea40df8 Ec024ef68 Ef7f4f7c4 E8a12fac2 Ec3137a3c E49a61ace Ea76ae1a0 E887b87bf Ef4e32054 Ef64f95ee E640fb9eb E94201299 E50e3cfda E382bc001 Eccc3a740 E3452b602 E63d9f2a4 E245f8b40 E91eeed07 Eb87e30cd E01a58312 E70725476 Ec9f89766 E36789acd E1a802824 E31663255 E9554bc19 Ee1545fce Ee0c18eba E6882a2c1 E2d576d7a E3c10497d Eda718e99 E826c9bd8 Ee380b6cb E0fac12e7 E597a7949 E01aaffdd E14fc61f8 E5107926b E231abefd E9be28c08 Ee204f827 E6fff18d2 Ef19126e7 Ee4728d7f E766b165c Ef9abfeec |
| 2 | NONSTD | FreeOtpImporter$DecryptedStateV2.<init> | 62 | other_app | - | CORRECT (fixed) | W8 re-verified 2026-11-07 (first verification: UNCLEAR; re-check: CORRECT; written as fixed: the gap the first check named is closed by a gate or avoided by the new route, review 5 fix 2). Re-check 2026-11-08 (W7 r6-p12): step 62 is the same call under a new edge id (E2d14031f to E14e5b783), which now carries the FreeOTP export env; the same 62 steps. Unlock prefix as row 1 (steps 8-20). The route now uses the file import (steps 33-50: Import row, FreeOTP in the importer list, system picker env, ImportFileTask, ImportEntriesActivity, processImporterState with a V2 file, FreeOtpImporter.java:69-115) instead of the root shell import, so the earlier UNCLEAR reason (root shell, installed FreeOTP data) no longer applies; the password dialog and PBKDF steps carry the encrypted-export env (FreeOtpImporter.java:180-193). Earlier: Carried from old table row 2. 48 root shell needs rooted device + su grant (not in declared config, no in-run producer); 50 non-root shell → toast + finish (ImportEntriesActivity.java:143-174); 52 installed FreeOTP V2 tokens.xml data, no in-run producer. Not WRONG: nothing listed contradicts root/FreeOTP presence. Steps 53-64 individually CORRECT but conditional on 52. Trace: route_table_postvault.md row 2; edge-identical. | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed Eef600725 E06202b0e E0158aff6 E911809ef E87843ac5 E4520b83d Ec2a7b2f4 E9ea40df8 Ec024ef68 Ef7f4f7c4 E8a12fac2 Ec3137a3c E49a61ace Ea76ae1a0 E887b87bf Ef4e32054 Ef64f95ee E640fb9eb E94201299 E50e3cfda E382bc001 Eccc3a740 E3452b602 E63d9f2a4 E245f8b40 E91eeed07 Eb87e30cd E27bbc836 E65e381fe E04fd60ef E89db3598 Ec974fdfd E489afca5 Edeedc4b7 E3e3cbef9 E65367273 E494ec178 Ea2466061 E2b7d7bc0 Ecbde6bd8 E53b00639 E68ce20aa E3445b99d Ec023c060 E6112940b E4766fd42 E8f6d7786 Eeb0c99d6 E20d818fb Ea697c567 E00f9feab Efe22519b E5ebe8322 Eef7de511 E14e5b783 |
| 3 | NONSTD | StratumImporter$EncryptedState.decrypt(SecretKey) | 60 | other_app | - | CORRECT (fixed) | W8 re-verified 2026-11-07 (first verification: CORRECT (fixed); re-check: CORRECT). Unlock prefix as row 1 (steps 8-20); new step 39 carries the picker env. The rest as before. Earlier: Carried from old table row 3. None adverse. Step 26 as row 1; picked Stratum file + password via in-run picker/password actions. Trace: route_table_postvault.md row 3; edge-identical. | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed Eef600725 E06202b0e E0158aff6 E911809ef E87843ac5 E4520b83d Ec2a7b2f4 E9ea40df8 Ec024ef68 Ef7f4f7c4 E8a12fac2 Ec3137a3c E49a61ace Ea76ae1a0 E887b87bf Ef4e32054 Ef64f95ee E640fb9eb E94201299 E50e3cfda E382bc001 Eccc3a740 E3452b602 E63d9f2a4 E245f8b40 E91eeed07 Eb87e30cd E9edc8c99 E704f59ea E2b769c0f E16b26e12 E79701a94 E6715f6d3 Eaf9670a3 Eaf584e08 Edc9e31c0 Efa07b0fb E4a84d5bd E743f9261 E062270d3 E06aeb459 E7067346f E631e6e57 E61c37f46 E88667145 E8aca2696 E9640aa8f E9f1f92f4 Efedc0a7e Eff73a574 Ee2ded0b9 Ebf7b06fe E18666fda |
| 4 | NONSTD | TwoFASImporter$EncryptedState.deriveKey | 58 | other_app | - | CORRECT | W8 re-verified 2026-11-07 (first verification: CORRECT; re-check: CORRECT). Unlock prefix as row 1 (steps 8-20); new step 39 carries the picker env. The rest as before. Earlier: Carried from old table row 4. None adverse. Step 26 producer step 21 initNew; step 55 TwoFAS EncryptedState from a TwoFAS file; steps 61-63 password lambda → decrypt(char[]) → deriveKey, all inside TwoFAS. No cross-importer step. Trace: route_table_postvault.md row 4; edge-identical. | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed Eef600725 E06202b0e E0158aff6 E911809ef E87843ac5 E4520b83d Ec2a7b2f4 E9ea40df8 Ec024ef68 Ef7f4f7c4 E8a12fac2 Ec3137a3c E49a61ace Ea76ae1a0 E887b87bf Ef4e32054 Ef64f95ee E640fb9eb E94201299 E50e3cfda E382bc001 Eccc3a740 E3452b602 E63d9f2a4 E245f8b40 E91eeed07 Eb87e30cd E62bc968a E06905a9d Eba811db5 E0fa92879 Ef54402ba Ed9f5dec4 E21108af4 E4a90b734 Ed4cd70c2 E9d7a28fb E8c908639 E09f926d2 Ef4e136f0 E62f67d24 Ef10125b7 Ea0308cd4 E543211ae E99919f5a E207eb47d E7f4b45c0 E574dd4c7 E15c7f356 E1dff62a9 E11001955 |
| 5 | INFERRED | RawSlot.getType | 42 | other;other_app | session | UNCLEAR | W8 re-verified 2026-11-07 (first verification: UNCLEAR; re-check: UNCLEAR). Round 3b (rule T, 2026-11-10): the same 42 steps; steps 23 and 26 (the intro's imported-vault branch) now carry ENV other_app instead of STATE: the imported vault file comes back from the system document picker (ACTION_GET_CONTENT, WelcomeSlide); new edge ids only, no step changed. Earlier: CHANGED from old table row 8 (WRONG, 49 steps) → UNCLEAR (42 steps, new @IMP route). Every step TRUE on action and operative condition (REJUDGE.md step tables 1-42); no step false. Load-bearing premise U2 producer-less: `new RawSlot` occurs exactly once in main app source, at Slot.java:133 inside fromJson (the parser); no app code writes a type-0 slot, no migration produces one, no producer in evidence — so CORRECT is not established, while WRONG would require a false step (none found) and NOT-ROUTABLE would require a rejection/strip/unreachable dispatch (parser explicitly accepts type 0, step-41 dispatch is a real iterated call). INFERRED legs steps 2-3, 22 accepted as caveats; stale Auth-leg guard/provenance text on steps 34-39 and 41 recorded as DEBT (see Table notes). New @IMP prefix edges I1-I8, L1-L3: I1 E0237a72b, I2 Edb4753c5, I3 Ec3048aa3, I4 Ed92e13fe, I5 E3cd165ef, I6 Eef8a8cb9, I7 Ecc2a9f7f, I8 E53167466, L1 E2a08d921, L2 E834df9cf, L3 Ebb585c74; tail Eeb5ad336, E6892571a, E6bfcd5a0, Ee2eb999f, E58750a27, E4a8bb39a, E9b24e5b2, Ea9adb818, E7a69f8a5. Fresh dump header path=WRONG is carried post-vault label metadata, NOT this verdict. Trace: turn/redraw/REJUDGE.md (gate 6) + turn/audit/redraw-reaudit/AUDIT.md gate 6 PASS, UNCLEAR confirmed. | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed E469ff740 E4ce5043a E5e63fbe7 E93598a00 E1440feb8 Ee1d29ff8 E3870f4a6 Ee4518b2e E4c857825 E3810e168 E87742878 E1462f671 Ea346ad34 E2cc12f00 E1555590e Eca3b318d Edb4753c5 Ec3048aa3 E395b9599 E3cd165ef Eef8a8cb9 Ecc2a9f7f E53167466 E2a08d921 E834df9cf Ebb585c74 Eeb5ad336 E6892571a E6bfcd5a0 Ee2eb999f E58750a27 E4a8bb39a E9b24e5b2 Ea9adb818 E7a69f8a5 |
| 6 | INFERRED | TotpAuthenticatorImporter$EncryptedState.lambda$decrypt$0 | 57 | other_app | - | CORRECT | W8 re-verified 2026-11-07 (first verification: CORRECT; re-check: CORRECT). Unlock prefix as row 1 (steps 8-20); new step 39 carries the picker env. The rest as before. Earlier: Carried from old table row 5. None adverse. Step 55 file/external branch (internal branch would yield DecryptedState, never reach decrypt); steps 56/62 Yes-path lambda numbering corroborated by javac inner-before-outer pattern. Trace: route_table_postvault.md row 5; edge-identical. | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed Eef600725 E06202b0e E0158aff6 E911809ef E87843ac5 E4520b83d Ec2a7b2f4 E9ea40df8 Ec024ef68 Ef7f4f7c4 E8a12fac2 Ec3137a3c E49a61ace Ea76ae1a0 E887b87bf Ef4e32054 Ef64f95ee E640fb9eb E94201299 E50e3cfda E382bc001 Eccc3a740 E3452b602 E63d9f2a4 E245f8b40 E91eeed07 Eb87e30cd Eb51c0932 E5eb44505 E3a5ccc62 E7c4a2b7c E0b4a32e9 E4d29f6bd E4b289f60 Ec7144448 Ea0b76b96 Eeb0293da E59b644b8 E030d215b Ee3bc9dfc Ef64041ea E559996bd E94c0e46e E709bf655 E9f3a18cb Ef8e931ed Eff775ca3 Ecade69e6 E10ae2e57 Efdb318dc |
| 7 | INFERRED | AuthenticatorPlusImporter$EncryptedState.decrypt(char[]) | 57 | other_app | - | CORRECT | W8 re-verified 2026-11-07 (first verification: CORRECT; re-check: CORRECT). Unlock prefix as row 1 (steps 8-20); new step 39 carries the picker env. The rest as before. Earlier: Carried from old table row 6. None adverse. Step 55 read always returns EncryptedState; steps 61-62 password lambda → decrypt(char[]), both inside AuthenticatorPlus. Trace: route_table_postvault.md row 6; edge-identical. | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed Eef600725 E06202b0e E0158aff6 E911809ef E87843ac5 E4520b83d Ec2a7b2f4 E9ea40df8 Ec024ef68 Ef7f4f7c4 E8a12fac2 Ec3137a3c E49a61ace Ea76ae1a0 E887b87bf Ef4e32054 Ef64f95ee E640fb9eb E94201299 E50e3cfda E382bc001 Eccc3a740 E3452b602 E63d9f2a4 E245f8b40 E91eeed07 Eb87e30cd E48388188 Ed962b9e4 E8b3d77a8 E52e9d592 Ecc7cbc8a E943fe5fb E5272f1f2 Eccbc4a6a E24719e25 Ea14766f6 E522daf42 Ea8c7408a E17286b97 E448772cf E8374933f Ebab0cfbb Ec97b03a4 E4535ce5b E57cedc3c E50422a95 Ec55e2dcf E2157cdc8 E7cc263b2 |
| 8 | INFERRED | AuthyImporter$EncryptedState.decrypt(char[]) | 57 | other_app | - | CORRECT | W8 re-verified 2026-11-07 (first verification: CORRECT; re-check: CORRECT). Unlock prefix as row 1 (steps 8-20); new step 39 carries the picker env. The rest as before. Earlier: Carried from old table row 7. None adverse. Dispatch stays Authy at every step (Dialogs.java:515-531; DatabaseImporter.java:37; AuthyImporter.java:101-135,157-162,165-203,207-214). Step 26 producer step 21 initNew. Trace: route_table_postvault.md row 7; edge-identical. | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed Eef600725 E06202b0e E0158aff6 E911809ef E87843ac5 E4520b83d Ec2a7b2f4 E9ea40df8 Ec024ef68 Ef7f4f7c4 E8a12fac2 Ec3137a3c E49a61ace Ea76ae1a0 E887b87bf Ef4e32054 Ef64f95ee E640fb9eb E94201299 E50e3cfda E382bc001 Eccc3a740 E3452b602 E63d9f2a4 E245f8b40 E91eeed07 Eb87e30cd Ee6001a0a Ef13d384d Ed997244d E47e55c77 Ea9a8eeb5 Ec7216cb2 Eb5c5b328 Ed2d31eff Ec2797cd6 E7760c455 Eead43db3 E5f2cb5b6 E40750ce6 Ed335999d E8e5f7f12 Ef3b2ba2f E360ebfb8 E5c56ded1 Ed6cf939b Ecba3a293 E91496925 Ed03a511a E838f4feb |
| 9 | STATE | IconAdapter$CategoryHeader.getPosition | 36 | other_app | - | CORRECT | W8 re-verified 2026-11-07 (first verification: UNCLEAR; re-check: CORRECT). Round 2 (2026-11-10): the floating action menu is no longer a state gate (cause D), so the route now opens Enter manually from the FAB menu (FabMenuHelper.java:55,60-63,68-74; MainActivity.java:256,475-476,494-514), then the icon of the new entry (EditEntryActivity.java:365,594, env: an icon pack from the system picker), the icon list and its category header (IconPickerDialog.java:127; IconAdapter.java:189); the old route went through Settings > Icon packs. New steps 22-36 read from the source. Earlier: Carried from old table row 9. 46 dump jumps from ImportEntriesActivity.onCreate to the save-button tap, omitting the GA app-import sub-flow (startImportApp/RootShellTask, ImportEntriesActivity.java:143-172; GA package read, GoogleAuthImporter.java:60-68) — root + installed GA app + import result never produced on route; 48 assign-icons dialog requires an installed icon pack (ImportEntriesActivity.java:320-322; IconPackManager.java:45-47), no step installs one on a fresh-install route. Neither contradicted. Tail 49-58 printed and correct. Trace: route_table_postvault.md row 9; edge-identical. | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed Eef600725 E06202b0e E0158aff6 E911809ef E87843ac5 E4520b83d Ec2a7b2f4 E9ea40df8 Ec024ef68 Ef7f4f7c4 E8a12fac2 Ec3137a3c E49a61ace Ea76ae1a0 E2e3490fc Eebad02db E554aee35 Ecd19b44c E0979a03c Ec66f5e2c E6597c1f8 Ee228ce53 E56c5c8c1 Eec8d017d E7ccd8d84 E323689ca E14340591 E7e558a17 Ef3e88d4c |
| 10 | STATE | EntryAdapter.setTempHighlightEntry | 39 | - | - | CORRECT | W8 re-verified 2026-11-07 (first verification: CORRECT; re-check: CORRECT). Round 2 (2026-11-10): the floating action menu is no longer a state gate (cause D), so the route adds an entry by hand: FAB menu > Enter manually (FabMenuHelper.java:55,60-63; MainActivity.java:494-514), Save (EditEntryActivity.java:535-544,656-660,668-682,845-867), the result returns to the list (MainActivity.java:179-182,618-623) and, with the two baseline entries the list does not scroll, so the new entry is highlighted (EntryListView.java:442-497); the old route used the selection action mode (session state). New steps 22-39 read from the source. Earlier: Carried from old table row 10. None adverse. Step 26 producer steps 21-22 initNew; suffix creates its own entry in-run (FAB → manual entry → save → result → highlight); step 44 reached regardless of scroll branch at step 43. Trace: route_table_postvault.md row 10; edge-identical. | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed Eef600725 E06202b0e E0158aff6 E911809ef E87843ac5 E4520b83d Ec2a7b2f4 E9ea40df8 Ec024ef68 Ef7f4f7c4 E8a12fac2 Ec3137a3c E49a61ace Ea76ae1a0 E2e3490fc Eebad02db E554aee35 Ecd19b44c E0979a03c Ec66f5e2c E6597c1f8 Ee228ce53 Ef6ab7dd8 E69bb265a E1436e4f3 E7c838ae7 E563cb84a Ea80bb15d E16eb2dbc E3d6ab8a1 E59ee7c4c Eb404a7df |
| 11 | STATE | GroupAdapter.getGroupByUUID | 47 | - | data | CORRECT (fixed) | W8 re-verified 2026-11-07 (first verification: UNCLEAR; re-check: CORRECT; written as fixed: the gap the first check named is closed by a gate or avoided by the new route, review 5 fix 2). W7 r6-p07 re-check: the same 47 steps; step 46 (lambda$onEditGroup$0 -> GroupAdapter.replaceGroup) is the same call under a new edge id (E77b81f18 to Ef5c9cf98) and now carries the state that a group exists and is renamed (GroupManagerActivity.java:117-120), which the route's earlier steps already make. Earlier: Carried from old table row 11. 41 addGroup loop body runs only if the vault already has a group (GroupManagerActivity.java:90-95); fresh vault has none (Vault.java:16-17, initNew bare Vault); no group producer in steps 1-40; no add-group UI. Satisfiable only by unlisted in-run action. Steps 42-52 inherit, otherwise mechanically sound. Trace: route_table_postvault.md row 11; edge-identical. | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed Eef600725 E06202b0e E0158aff6 E911809ef E87843ac5 E4520b83d Ec2a7b2f4 E9ea40df8 Ec024ef68 Ef7f4f7c4 E8a12fac2 Ec3137a3c E49a61ace Ea76ae1a0 E887b87bf Ef4e32054 Ef64f95ee E640fb9eb E94201299 E50e3cfda E382bc001 Eccc3a740 E3452b602 Eba86fd82 Ef17c8ca0 E37edc2e5 Ee5fe910f Ef4742d96 Eb71df3aa Ed82877e6 E5e433c4f E1fe7fa89 E05744b28 Ea558e9b6 E7d8dd4ed Ee0d2237f E862dcf74 E02b181bd Ef5c9cf98 E2d25c3ba |
| 12 | ENV | ScannerActivity.lambda$onQrCodeDetected$1 | 38 | hardware | - | CORRECT | W8 re-verified 2026-11-07 (first verification: CORRECT; re-check: CORRECT). Round 3 (2026-11-10): the same 38 steps; step 34 (the catch of GoogleAuthInfoException -> the error dialog) now carries the env gate of an invalid or unsupported QR code in the camera frame (ScannerActivity.java:178-197; a valid code finishes the scanner), and step 38 lost the session tag "camera provider ready", a device fact; new edge ids only. Earlier: Carried from old table row 13 (ENV order changed: first in ENV in the new draw, was second). None adverse. Step 26 producer initNew (VaultManager.java:66-68, _repo set, getVault() does not throw); step 43 target via printed dialog OK listener (ScannerActivity.java:194-196). Trace: route_table_postvault.md row 13; edge-identical. | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed Eef600725 E06202b0e E0158aff6 E911809ef E87843ac5 E4520b83d Ec2a7b2f4 E9ea40df8 Ec024ef68 Ef7f4f7c4 E8a12fac2 Ec3137a3c E49a61ace Ea76ae1a0 E2e3490fc Eebad02db E554aee35 Ecd19b44c Ed606a578 E519c06f3 Edd5d8048 Eaeecfde8 E22a9500d E875bd18a Ece1825c9 Ede72ed30 E35b9d1b6 E9126cde9 Eb421b292 Ed9b44100 Ee3a8d8e5 |
| 13 | ENV | ImportExportPreferencesFragment$ExportResultListener.onTaskFinished | 44 | other_app | - | CORRECT | W8 re-verified 2026-11-07 (first verification: CORRECT; re-check: CORRECT). Unlock prefix as row 1. New steps 38-42: the system document creator env returns to Aegis (ImportExportPreferencesFragment.java:82, 403-411), onExportResult (:505-514), startExportVault with the encrypted format (the baseline vault is encrypted, :442-499), the export task (:521-535). Earlier: Carried from old table row 14. None adverse. Plain-export path end to end: step 43 exportPlainResultLauncher for Aegis format without encryption (ImportExportPreferencesFragment.java:403-405); step 46 export(stream, null) (483-490). No dumped step demands an encrypted vault. Trace: route_table_postvault.md row 14; edge-identical. | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed Eef600725 E06202b0e E0158aff6 E911809ef E87843ac5 E4520b83d Ec2a7b2f4 E9ea40df8 Ec024ef68 Ef7f4f7c4 E8a12fac2 Ec3137a3c E49a61ace Ea76ae1a0 E887b87bf Ef4e32054 Ef64f95ee E640fb9eb E94201299 E50e3cfda E382bc001 Eccc3a740 E3452b602 E63d9f2a4 E245f8b40 E629987fd Ed8c9ae46 E76172dad E847a2f41 Eae638791 Eedce6158 Eb3e204cf Eafd916ef E351446e6 Efe3544fe Ec9295cb2 E546cc6f9 |
| 14 | ENV | AegisImporter$DecryptedState.getCredentials | 30 | other;other_app | - | CORRECT | W8 re-verified 2026-11-07 (first verification: CORRECT; re-check: CORRECT). W7 r6-p04 re-check: the same 30 steps; step 8 (onStart -> startIntroActivity) is the same call under a new edge id (E0602e719 to E469ff740) and now carries the env gate other: the intro opens only when no vault file exists, a fresh install or cleared app data (MainActivity.java:942-948). The rest as before. Earlier: Carried from old table row 12 (ENV order changed: third in ENV in the new draw, was first). None adverse. Step 19 encrypted branch (WelcomeSlide.java:60-69, AegisImporter.read:45-53); step 28 non-null decrypt result from listed password steps 22-24; step 30 cast safe (decrypt(creds) returns DecryptedState, AegisImporter.java:70-78). Trace: route_table_postvault.md row 12; edge-identical. | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed E469ff740 E4ce5043a E5e63fbe7 E93598a00 E1440feb8 Ee1d29ff8 E3870f4a6 Ee4518b2e E4c857825 E3810e168 E87742878 Edc48b00a E0350fbf8 Ebdf96377 E47430d38 Ec256263d E192d0dbc E97a42336 Ee2e7fca6 E418cf046 E4eeeeab8 E616ffa9b Efd47250b |
| 15 | ENV | IconPackExistsException.getIconPack | 42 | other_app | - | CORRECT (fixed) | W8 re-verified 2026-11-07 (first verification: UNCLEAR; re-check: CORRECT; written as fixed: the gap the first check named is closed by a gate or avoided by the new route, review 5 fix 2). Unlock prefix as row 1. Step 41 now carries the env the earlier UNCLEAR named: an icon pack is already installed (Aegis cannot create one, IconPacksManagerFragment.java:136-147). Earlier: Carried from old table row 15. 46 Exists dialog requires a pre-existing installed pack (IconPackManager.java:84-89); no step 1-45 installs one; step-43 import cannot be its own producer (throws before installing). Satisfiable by unlisted in-run action (import same pack once earlier, then re-import). Trace: route_table_postvault.md row 15; edge-identical. | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed Eef600725 E06202b0e E0158aff6 E911809ef E87843ac5 E4520b83d Ec2a7b2f4 E9ea40df8 Ec024ef68 Ef7f4f7c4 E8a12fac2 Ec3137a3c E49a61ace Ea76ae1a0 E887b87bf Ef4e32054 Ef64f95ee E640fb9eb E94201299 E50e3cfda E382bc001 Eccc3a740 E3452b602 Ea95d014f E5ddb974e Eb2fa28dd E66001fba E19ae8555 E6e1bc9d5 E6f1190ae E9e4e4013 E466a8c1f E3f4ee988 Ea98c30af E9bdbc29f |
| 16 | ENV | GoogleAuthProtos$MigrationPayload.parser | 0 | - | - | WRONG | W8 re-verified 2026-11-07 (first verification: CORRECT; re-check: WRONG). Round 3 (2026-11-10): the method is dead. No app code calls the static parser() accessor (grep of the app tree; otp/GoogleAuthInfo.java:195-460 uses parseFrom, newBuilder and the getters), and the protobuf-lite runtime parses through dynamicMethod of the default instance; the drawn route's last step (parseFrom(byte[]) -> parser, an INFERRED edge without a basis) is removed, so the route as drawn never runs. Earlier: Carried from old table row 16. 41 parser() accessor rests on the generated protobuf class, absent from the tree (verified by search). ParseFrom call site (GoogleAuthInfo.java:198) and proto definition (google_auth.proto, MigrationPayload) verified. Step 26 producer steps 21-22 initNew. Trace: route_table_postvault.md row 16; edge-identical. |  |
| 17 | ENV | AuthActivity.lambda$onCreate$3 | 14 | hardware;time | - | WRONG | W8 re-verified 2026-11-07 (first verification: WRONG; re-check: WRONG). Round 2 (2026-11-10): the same 14 steps; step 13 has a new edge id because biometric gates are env hardware throughout (cause B); the first verdict (wrong as drawn) is kept. Earlier: NEW row (not in the old table; entered on the 9–9 ENV coverage tie, see Migration). Two independent false steps, each shown false on printed app source. Step 28 (lock-icon tap → VaultManager.lock): FALSE — updateLockIcon sets the lock item visible only when the vault is encrypted (MainActivity.java:1155-1160), applied from onCreateOptionsMenu (:1015) and the onStart path (:1004) before any tap at S_LIST; this route's vault is unencrypted (steps 21-22 initNew(null) → _creds null → isEncryptionEnabled false, VaultRepository.java:352-354), so the item is hidden and cannot be tapped; the action_lock branch (:1093-1094) is the only onOptionsItemSelected path to lock, and non-menu lock callers call lock(false), which cannot produce drawn steps 30-36 since onLocked only starts AuthActivity when userInitiated is true. Step 35 (biometric-button tap): FALSE — button visible only with a BiometricSlot + keystore key (AuthActivity.java:132-150, Header(null,null) at VaultFile.java:102-105, step-8/21–22 contradiction: step 8 requires no vault file at launch, steps 21-22 save a new NONE vault overwriting any earlier biometric vault). Steps 1–27 + 36 true, steps 29–34 true-if-reached but unreached (with the audit N3 qualification for steps 33–34, see Table notes). ENV kinds hardware;time verified against methods.csv (not copied blindly): step 35 carries hardware, step 36 carries time; no step carries other_app (correct: no import on this route). FIXED-INELIGIBLE: not in the first-draw sample (grep zero in sample_30.txt; CustomSvgIcon control at line 2), so it cannot count as fixed under the strict definition whatever its verdict. Trace: turn/judge-auth/JUDGE_AUTH.md + turn/audit/judge-auth/AUDIT.md VERDICT PASS, blocking defects NONE. | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed Eef600725 E06202b0e E0158aff6 E911809ef E87843ac5 Ec43a93ad Ec640bc11 |
| 18 | LONG | AuditLogDao_Impl.__EventType_enumToString | 23 | - | - | UNCLEAR | W8 re-verified 2026-11-07 (first verification: UNCLEAR; re-check: UNCLEAR). Unlock prefix as row 1; new steps 17-18: a wrong password writes the unlock-failed audit event (AuthActivity.java:358-360; AuditLogRepository.java:51). Still UNCLEAR for the earlier reason: AuditLogDao_Impl is generated Room code, not in the source tree. Earlier: Carried from old table row 18. 8 checkIconOptimization demands a loaded vault (VaultManager.java:231-233) but steps 1-7 contain no producer (no intro/initNew/unlock; onStart plaintext-load branch itself needs a pre-existing vault file = cross-run state); 13 scheduleBackup requires encrypted vault + pref_backups (defaults false, Preferences.java:400-401, no in-run producer); 19-22 generated AuditLogDao_Impl absent (only @Dao interface + Room wiring printed). Trace: route_table_postvault.md row 18; edge-identical. | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed Eef600725 E06202b0e E0158aff6 E911809ef E87843ac5 E4520b83d Ec2a7b2f4 E9ea40df8 Ec024ef68 Ef1fa67ea E477e6d83 E70cfbd13 E41c81365 E75d86940 Ea076a7d4 Eb7b2b852 |
| 19 | LONG | SlotIntegrityException.<init>(Throwable) | 19 | other | - | CORRECT (fixed) | W8 re-verified 2026-11-07 (first verification: UNCLEAR; re-check: CORRECT; written as fixed: the gap the first check named is closed by a gate or avoided by the new route, review 5 fix 2). New 19-step route: unlock prefix steps 8-16, then PasswordSlotDecryptTask.decrypt -> decryptPasswordSlot(char[]) -> decryptPasswordSlot(SecretKey) with the env for a slot an older version wrote (PasswordSlotDecryptTask.java:31-77). The earlier UNCLEAR reason (pin keyboard preference on an unencrypted intro vault) is no longer on the route. Earlier: Carried from old table row 19. 38 pin-keyboard preference visible only when vault encrypted (SecurityPreferencesFragment.java:259-265; preferences_security.xml:86); in-run vault is NONE intro vault, hence unencrypted (IntroActivity.java:92-93; VaultRepository.java:352-353). Unlisted enable-encryption visit would satisfy it, contradicted by no listed step. Throw site Slot.java:57. Step 26 producer steps 21-22 initNew. Trace: route_table_postvault.md row 19; edge-identical. | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed Eef600725 E06202b0e E0158aff6 E911809ef E87843ac5 E4520b83d Ec2a7b2f4 E45df5be5 E8ef49332 Ebe974f3a E808d453d E6766e40e |
| 20 | LONG | IconPack$Icon.<init> | 19 | other_app | - | CORRECT | W8 re-verified 2026-11-07 (first verification: UNCLEAR; re-check: CORRECT). Re-check 2026-11-08 (W7 r6-p22, after the icon-pack steps of the edit picker got their other_app gates): new 19 steps, the app starts with an icon pack already in the icons folder (imported in an earlier run from a file another app supplies), so MainActivity's Hilt injection builds IconPackManager, whose constructor rescans the folder (IconPackManager.java:136-158) and parses each icon of pack.json (IconPack.java:117-121) through IconPack$Icon.fromJson into the constructor. Every step is a real call on a cold start; class other_app holds. Re-check 2026-11-07 (W7 r6-p11): the loadIcons -> DummyIcon bytecode edge was copied onto the @ASSIGN and @NOCUSTOM grids, which never add the custom row (showAddCustom false, IconAdapter.java:63-64); it is now one hand edge from loadIcons@EDIT. New 17 steps: another app opens an otpauth link (other_app, AndroidManifest.xml:52-59), the new entry editor opens (MainActivity.handleIncomingIntent), a tap on the icon opens the icon picker because an icon pack is imported (other_app, EditEntryActivity.java:586-594), the picker adds the custom row (IconAdapter.java:63-64) whose DummyIcon calls the Icon constructor. The vault must be unlocked first (a GUI step that handleIncomingIntent waits for, MainActivity.java:854-856). Class other_app holds. Earlier: Carried from old table row 20. 8-13 Hilt/Dagger injection chain rests on generated code absent from the tree (zero Hilt_*.java / Dagger*.java found); printed anchors do not verify the generated edges. 16 independently UNCLEAR under STRICT step-8 (icon pack is cross-run state, no in-run producer; rescan only reads the existing icons folder, IconPackManager.java:132-165). Trace: route_table_postvault.md row 20; edge-identical. | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd Efe5ce260 E1e4b62ae E7d4e454a E262cce3d Eada96a15 E67272644 E9f3e06cc E375694d7 E75a5e491 E6a3521b8 Eecb7add2 E6a270ba3 Ecc690490 |
| 21 | LONG | Salsa20Engine.salsaCore | 24 | - | - | CORRECT | W8 re-verified 2026-11-07 (first verification: CORRECT; re-check: CORRECT). New steps 8-18: the unlock prefix, then PasswordSlotDecryptTask.decrypt -> decryptPasswordSlot -> PasswordSlot.deriveKey -> CryptoUtils.deriveKey (scrypt, PasswordSlot.java:57; PasswordSlotDecryptTask.java:37-51). The rest as before. Earlier: Carried from old table row 21. None adverse. Setup-slide not-finished state is the normal pre-derivation state (fresh empty credentials, SecuritySetupSlide.java:97); tail printed direct calls through SCrypt.java:90/122/188/210 to salsaCore (Salsa20Engine.java:32). Trace: route_table_postvault.md row 21; edge-identical. | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed Eef600725 E06202b0e E0158aff6 E911809ef E87843ac5 E4520b83d Ec2a7b2f4 E45df5be5 E8ef49332 E7545a097 E996ea32b E0205a921 E95462315 Ecc90cdf7 E19236baa Effe83609 E89dde570 |
| 22 | LONG | EditEntryActivity.deleteAndFinish | 33 | - | session | CORRECT (fixed) | W8 re-verified 2026-11-07 (first verification: UNCLEAR; re-check: CORRECT; written as fixed: the gap the first check named is closed by a gate or avoided by the new route, review 5 fix 2). Unlock prefix as row 1; step 22 long press on a baseline entry (the baseline vault holds two entries, Q6), so the earlier UNCLEAR reason (no row to press on an empty intro vault) no longer applies. Earlier: Carried from old table row 22. 27 long-press: in-run vault created empty by initNew (non-import intro branch), so no row exists to press; unlisted add-entry visit (FAB → startEditEntryActivity) can supply one. Step 26 CORRECT (initNew step 21 is the STRICT step-8 producer). Steps 28-38 printed-correct conditional on step 27's row. Trace: route_table_postvault.md row 22; edge-identical. | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed Eef600725 E06202b0e E0158aff6 E911809ef E87843ac5 E4520b83d Ec2a7b2f4 E9ea40df8 Ec024ef68 Ef7f4f7c4 E8a12fac2 Ec3137a3c E49a61ace Ea76ae1a0 E7b3c936f E614708b9 Eec2cee41 Eecd32631 E61a741b2 Ee1fbd7db Edcca50e0 Ed53a4891 Ed78bc83b E117654d4 Ed46b4aa9 E94c17e0d |
| 23 | LONG | GoogleAuthProtos$MigrationPayload$DigitCount$DigitCountVerifier.<init> | 44 | other_app | - | UNCLEAR | W8 re-verified 2026-11-07 (first verification: UNCLEAR; re-check: UNCLEAR). Unlock prefix as row 1; new step 35 opens the Google Authenticator export (ImportExportPreferencesFragment.java:384-390; baseline TOTP SHA-1 6-digit entries) and step 41 is the generated protobuf dispatch. Still UNCLEAR: the Next button needs two or more QR batches (11 or more entries; the baseline has two) and the protobuf tail is generated code. Earlier: Carried from old table row 23. 40 needs ≥1 qualifying TOTP/HOTP SHA-1 6-digit entry (in-run vault holds 0); 42 Next visible only if batch list size ≠ 1, i.e. ≥2 batches of 10 = ≥11 entries (in-run count 0); 45-49 generated-protobuf tail UNCLEAR (no GoogleAuthProtos source file in tree, only references in GoogleAuthInfo.java:7,400,459). Trace: route_table_postvault.md row 23; edge-identical. | Eb9515d18 E5b266140 E1ef992ce E88ed9829 E28ffc58c Eb76444fd E3a06baed Eef600725 E06202b0e E0158aff6 E911809ef E87843ac5 E4520b83d Ec2a7b2f4 E9ea40df8 Ec024ef68 Ef7f4f7c4 E8a12fac2 Ec3137a3c E49a61ace Ea76ae1a0 E887b87bf Ef4e32054 Ef64f95ee E640fb9eb E94201299 E50e3cfda E382bc001 Eccc3a740 E3452b602 E63d9f2a4 E245f8b40 E8e4d066b E1f7435e7 Eff96a909 E72e1a8df Ec5f95bb3 E6817ac19 Ee0ce6c02 Ea8a623d5 E0cc0718a E00b93575 E6c7b88cc Ec45d78f1 |
| 24 | PLAIN | Hilt_AegisApplication.<init> | 2 | - | - | CORRECT | Carried from old table row 24. Manifest android:name leg + @HiltAndroidApp leg under fixed-(c). Header-token note: fresh dump header path=SOURCE_OK vs old dump path=UNCHECKED — pre-existing label metadata only (the apply-v3 BEFORE build and the merger-tree baseline already carry SOURCE_OK for this method); step lines and edge ids identical, verdict unchanged. Trace: route_table_postvault.md row 24; edge-identical. | Eb9515d18 Ecaf88dff |
| 25 | PLAIN | AegisApplication.<init> | 1 | - | - | CORRECT | Carried from old table row 25. Manifest leg alone. Header-token note: same as row 24 (path UNCHECKED → SOURCE_OK, pre-existing label metadata only); step line and edge id identical, verdict unchanged. Trace: route_table_postvault.md row 25; edge-identical. | Eb9515d18 |

Row count check: rows 1–25 above = 25 rows. No 26th row exists in this
table. The dropped row is recorded in the Migration and Table notes
only, never as a table row.

## Tally

- New final sample: CORRECT 13, WRONG 1, UNCLEAR 11 (25 routes, 1093 steps,
  446 distinct edges).
- Fixed (strict: first-draw WRONG → final CORRECT) = 2: AndOtp (row 1),
  Stratum (row 3). Verified by the helper from the old table's fixed
  tally (3: AndOtp, Stratum, CustomSvgIcon — each annotated first-draw
  WRONG in the old table) plus the first-draw sample
  (`merger/scratch/sample_30.txt`: CustomSvgIcon at line 2, AndOtp and
  Stratum present, AuthActivity absent in any form) plus the row swap
  (CustomSvgIcon dropped, Auth entered and fixed-ineligible): 3 − 1 = 2.
  No other new CORRECT row qualifies: the old table's fixed tally already
  exhausts the fixed set at 3, and no other CORRECT row in this table is
  annotated first-draw WRONG there (EntryAdapter, Scanner, ExportResult
  are first-draw UNCLEAR → CORRECT; AegisImporter, Salsa, Hilt,
  AegisApplication are first-draw CORRECT → CORRECT; TwoFAS, Totp,
  AuthenticatorPlus, Authy are not first-draw rows at all).
- Correct-only = CORRECT − fixed = 13 − 2 = 11. Verified independently:
  the 11 correct-only rows are TwoFAS, Totp, AuthenticatorPlus, Authy,
  EntryAdapter, Scanner, ExportResult, AegisImporter, Salsa, Hilt,
  AegisApplication (13 CORRECT minus AndOtp and Stratum).
- Error rate, distinct rate = (fixed + wrong) / (correct-only + fixed + wrong)
  = (2 + 1) / (11 + 2 + 1) = 3/14 ≈ 0.2143.
- Error rate, table formula = (fixed + wrong) / (CORRECT + fixed + wrong)
  = (2 + 1) / (13 + 2 + 1) = 3/16 = 0.1875.
- Old rates for comparison (old table: CORRECT 14 / WRONG 1 / UNCLEAR 10,
  fixed 3, correct-only 11): distinct = (3 + 1) / (11 + 3 + 1) = 4/15
  = 0.2667; table formula = (3 + 1) / (14 + 3 + 1) = 4/18 = 0.2222.
- Movement explained: fixed 3 → 2 (CustomSvgIcon dropped, see Migration);
  wrong count stays at 1 by a swap, not by stability — the old WRONG
  (RawSlot) leaves the WRONG column to UNCLEAR, and the new WRONG (Auth)
  enters it; correct-only is unchanged at 11 (the CORRECT column falls
  14 → 13 only because the fixed CORRECT row CustomSvgIcon leaves, while
  the two fixed rows AndOtp and Stratum stay CORRECT). Both rates fall
  because the numerator falls 4 → 3 while the distinct denominator falls
  15 → 14 and the table denominator falls 18 → 16.
- Step/edge movement: steps 1107 → 1093, delta −14 = RawSlot 49 → 42 (−7)
  plus the CustomSvgIcon (43) → AuthActivity-lambda (36) swap (−7).
  Distinct edges 444 → 446, delta +2 despite the shorter RawSlot route,
  because the new @IMP prefix edges and the swapped row's edges change
  the union. PLAIN still contributes only 2 vs quota 7, as in the old draw.

## Migration (old final table → new final table)

- 24 methods common to both draws (all old members except CustomSvgIcon;
  all new members except AuthActivity.lambda$onCreate$3). Of the 23 common
  methods other than RawSlot, edge-id lists are byte-identical (same ids,
  same order, full numbered step sequences compared old dump vs fresh
  dump), so their old verdicts are carried unchanged; the 2 header
  path-token differences (rows 24–25, UNCHECKED → SOURCE_OK) are
  pre-existing label metadata, NOT verdict changes (see rows 24–25).
- RawSlot.getType: old WRONG (49 steps, NONE-intro prefix) → new UNCLEAR
  (42 steps, @IMP prefix), first edge difference at step 13
  (E6830b6dc → Ee1d29ff8). RawSlot is not in the first-draw sample, so
  WRONG → UNCLEAR is not a fix under the strict definition.
- Dropped from the sample (1, recorded here and in the Table notes only,
  NEVER as a 26th row): EditEntryActivity$CustomSvgIcon.<init> (ENV, 43
  steps, CORRECT + fixed in the old table) left the sample on the 9–9 ENV
  coverage tie at ENV pick 6 (AuthActivity.lambda$onCreate$3 9 new edges,
  CustomSvgIcon 9 new edges at every ENV stage of the new draw, stable-sort
  tie-break selecting Auth; in the old draw Auth sat at only 2 new edges
  at every ENV stage while CustomSvgIcon sat at 9). Its route is unchanged
  (old-dump edge list byte-identical to its fresh methods.csv list, 43
  steps, REACHABLE, env other_app, state data;session); it left purely on
  the coverage tie. Its CORRECT verdict leaves the table with the row:
  neither carried nor counted in the new table.
- Added to the sample (1, judged fresh, independently audited):
  AuthActivity.lambda$onCreate$3 (ENV, 36 steps, 9 new edges), verdict
  WRONG on two independent false steps (steps 28 and 35, see row 17).
- Order changes within the common set: RawSlot.getType first within
  INFERRED (was last); within ENV, Scanner first and AegisImporter third
  (was first). NONSTD, STATE, LONG, and PLAIN orders are unchanged.
- The final table covers ONLY the final draw. Dropped rows' verdicts are
  superseded, not carried over; their reasons stay on record in the old
  table. The C3 table (25 routes, 696 steps, rate 5/9 = 0.5556) is kept
  untouched and is NOT comparable as a trend: the sample itself changed,
  and each table's denominator counts only its own draw's CORRECT + fixed
  + WRONG routes.

## Table notes (path-(A) exception conditions, table side)

### Gate-5 status

Gate 5 stays FAIL as written under exception (not PASS-on-ruling). The
exception waives ONLY the identical-list requirement. The gate as written
demands an identical method list, and that condition was not met (gate
5(a) FAIL literal: CustomSvgIcon out, AuthActivity.lambda$onCreate$3 in,
plus order changes); a ruling cannot retroactively make a failed literal
condition true. Gate 5(b) is PASS on route content (edge lists 23/23
identical, all step lines identical) and FAIL on literal full-block
byte-identity (the 2 pre-existing header tokens, rows 24–25); the literal
failure blocks nothing, since path rows for F1 are edge-id lists and
those are identical. Gate 5(c) PASS (RawSlot is exactly the 42-step @IMP
route); gate 5(d) PASS (25/1093/446 recomputed). If any exception
condition fails, the exception lapses and gate 5 blocks the chain. The
writer/check steps remain separate and are NOT claimed here.

### §11 item 5 correction

V3-corrected §11 item 5's prediction "the sample method list itself does
not change" is corrected as follows (correction note, not a silent edit
to the design's gate text in place — the original prediction and its
failure stay on record):

"the sample method list MAY change via the greedy coverage sampler when
a fix changes a route's edge set; if it does, judge every new row fresh,
drop removed rows with their verdicts (final table covers only the final
draw), and recompute on the new set"

This corrects V3-corrected §11 item 5's "the sample method list itself
does not change". The reason is structural, not a one-off slip: a greedy
coverage sampler's selection is a function of the routes, so any route
change can change later picks, even when the method set, verdicts, and
strata are unchanged.

### Stale-guard disposition (merger-adopted)

Operative-condition basis adopted: a step is judged on its action and
operative condition, not stale provenance text. RawSlot tail steps 34–39
and 41 keep current guard/provenance text for now, recorded as DEBT,
because rewording would re-id the tail edges (guard text is hashed into
edge ids) and break the apply gate's byte-identical tail claim; on any
future tail-edge rewrite, reword the guards to the assign leg at the same
time and re-prove the tail ids. The tail calls themselves are
unconditional direct calls and the operative conditions were verified on
the assign leg (step 37 encrypted branch via installed creds, step 40
_slots non-null via setContent(obj, _creds), step 41 iteration over the
imported header slots). Guard text must NOT be silently edited. A future
rewording, if ever wanted, is a new graph change with new ids and a fresh
re-judge, not a text fix. INFERRED legs (RawSlot steps 2–3, 22; Auth
INFERRED legs as in JUDGE_AUTH.md: steps 2–3 Hilt generated code, 6, 10,
15, 20, 23, 27, 31, 32, 33 framework lifecycle/click/launcher dispatch,
14 RadioGroup behaviour) are accepted as caveats as in prior rows, not
step failures, where the steps are not shown false. The Auth verdict does
not rest on any INFERRED leg: both falsifying chains use printed app
source only.

### Sharing-numbers record correction

Published totals are Auth old/new 34 vs 12 and Custom old/new 26 vs 12.
The helper's 25 vs 3 / 17 vs 3 match only intersections after excluding
RawSlot steps 1–9 (never defined in that report) and must NOT be published
as totals. Auth new-route sharing (unexcluded) = 12 (Auth steps 1–12 =
RawSlot steps 1–12, zero beyond step 12, divergence step 13: Auth
E6830b6dc vs RawSlot Ee1d29ff8). The 12 shared edges are the app-start
through intro-slide chain common to any fresh-install intro route; they
carry no information about the Auth route's later steps, which are
entirely disjoint from the RawSlot route. Direction and magnitude are
unchanged (the old route shares far more, the new route shares only the
opening chain); the swap mechanism itself stands on the independent
stage-by-stage tie reproduction, not on the sharing numbers.

### Auth audit non-blocking notes carried

- N1 (onStart-path label correction for MainActivity.java:1004): the
  judge called the MainActivity.java:1004 block "the onResume path"; the
  method containing :1004 is onStart (onStart at MainActivity.java:939;
  the next lifecycle method boundary is onCreateOptionsMenu at about
  :1010; updateLockIcon appears only at :1004, :1015, and its definition
  at :1155). The correct label is "the onStart path". Timing conclusion
  unaffected: onStart and onCreateOptionsMenu both run before any menu
  tap at S_LIST. The corrected label is carried in row 17 above.
- N2 (menu_main.xml clause UNVERIFIED but unnecessary): menu_main.xml is
  absent from the final_java_only tree (no res/ directory there) and was
  not found elsewhere under finish/work/Aegis, so the judge's clause
  about menu_main.xml giving action_lock no surviving default-visible
  override is UNVERIFIED from the materials available. It carries no
  load: setVisible(false) applied after inflation hides the item
  regardless of XML defaults, and step-28 falsity rests on updateLockIcon
  plus the unencrypted vault, not on the XML.
- N3 (steps 33–34 true only as code-existence, not executable on a
  null-slots vault — reinforces WRONG): with header slots null,
  _slots itself is null (Header(null, null) via VaultFile.java:102-105
  and fromJson at :146-149), so AuthActivity.java:132 throws a
  NullPointerException on `_slots.has(...)` (no null check precedes it)
  rather than returning false. The button therefore never becomes
  visible, and AuthActivity onCreate would not complete on this vault in
  any counterfactual where it launches, so steps 33 (onResume) and 34
  (S_AUTH) are true only as code-existence, not as executable on this
  vault. This reinforces WRONG; it is not a third independent false step
  and changes no verdict, count, or rate (steps 28 and 35 already falsify
  the route, and the NPE shares step 35's root cause, null header slots).
- Auth audit N4 (INFERRED legs accepted as in REJUDGE.md) and N5
  (sampling statement: every load-bearing step re-verified directly,
  remainder spot-checked) are carried by the trace citations in row 17
  and by the Verification section below.

### Sample provenance

Seed 20261025, sampler `python3 -I tools/verify_sample.py Aegis 30 20261025`
on the 6430-edge V3-corrected build. F1 "path rows = final sample" = THIS
new 25-row set (24 common methods plus AuthActivity.lambda$onCreate$3,
minus CustomSvgIcon), NOT the post-vault 25-row set. Pre-fix totals for
comparison: 25 routes / 1107 steps / 444 distinct edges, CORRECT 14 /
WRONG 1 / UNCLEAR 10, fixed 3, distinct 4/15 = 0.2667, table 4/18 = 0.2222.
Post-fix totals: 25 / 1093 / 446, CORRECT 13 / WRONG 1 / UNCLEAR 11,
fixed 2, distinct 3/14 ≈ 0.2143, table 3/16 = 0.1875. Stratum quotas for
n=30 are NONSTD 4, INFERRED 4, STATE 3, ENV 6, LONG 6, PLAIN 7; PLAIN
contributes only 2 (pool exhausted), giving 25 rows, as in the old draw.
Method set unchanged: 2537 REACHABLE / 458 UNREACHABLE out of 2995
methods in both builds; only the greedy selection changed.

## Verification performed by this helper (staging checks, not a merger audit)

- Edge-identity, old dump vs fresh dump: 24 common methods; RawSlot
  differs as designed (49 → 42, first difference step 13); the other 23
  are byte-identical edge-id lists (same ids, same order, full numbered
  step sequences). Full block text: 21 of 23 byte-identical; the 2
  exceptions differ in exactly one header token each (rows 24–25,
  path UNCHECKED → SOURCE_OK), with every step line identical.
- Fresh dump vs fresh methods.csv: 0 mismatches across all 25 rows
  (route_edge_ids identical to the dump block step edge ids, same order;
  step counts match steps_from_launch; ENV/STATE kinds match dump headers).
- Totals recomputed from the fresh methods.csv for the 25 picked methods
  (sum of steps_from_launch; union of route_edge_ids): 25 / 1093 / 446,
  agreeing with the sampler header. Old totals recomputed the same way:
  25 / 1107 / 444.
- RawSlot @IMP/tail ids checked against the task's list and §1.3: I1–I8
  and L1–L3 and the 9 tail ids all match exactly (see row 5).
- Auth ENV kinds checked against methods.csv: hardware;time (judge's
  header env=hardware;time confirmed, not copied blindly); Auth–RawSlot
  unexcluded sharing recomputed at 12 (see Sharing-numbers note).
- Fixed membership checked as in the Tally (old tally 3, minus dropped
  CustomSvgIcon, Auth fixed-ineligible): 2, AndOtp + Stratum.
- Correct-only checked by enumeration (11 rows listed in the Tally):
  13 − 2 = 11, agreeing with the distinct-rate denominator
  (11 + 2 + 1 = 14) and the derivation in RECOMPUTE.md. If that
  enumeration had disagreed, this helper was instructed to STOP and
  report the disagreement; it did not disagree.
- Dropped-row control: CustomSvgIcon's old-dump edge list is
  byte-identical to its fresh methods.csv list (43 steps), confirming its
  route never changed and it left purely on the coverage tie.

## NOT done in this step (explicitly out of scope here)

No eight-check suite, no drycheck, no writer regeneration, no
verification-row rewrite, no decision record, no push, and no push
readiness is claimed or implied. No merger-tree, branch, tools/,
.github/, or other-app file was modified. No emulator/adb/device run
was started and no CI request was sent. The merger's remaining
path-(A) items (writer/check steps) are separate work.
