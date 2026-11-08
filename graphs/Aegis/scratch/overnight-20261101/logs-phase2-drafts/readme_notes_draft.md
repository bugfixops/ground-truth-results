# DRAFT readme_notes.md — Aegis (phase-2 leaf B, 2026-11-01)

DRAFT ONLY. This is NOT the branch `graphs/Aegis/readme_notes.md` and
must NOT be published as it: four sections are still drafts, and every
count or claim that depends on the final build, the final sample, or
the final checks is marked TO-VERIFY with its source. The final text
must use final-build numbers taken from files, per the
`gen_readme_v2.py` rule that no number is typed in. `gen_readme_v2.py`
appends this file's text under its own headings, so four "Pending"
sections would otherwise be published verbatim as "Pending".

Retired phrasing, noted for the finaliser: the branch file's Pending
text says each section "is written when the Aegis graph reaches
0 errors". That condition must not be reused: the stage-5 build already
showed 0 errors / 0 warnings, and round 7 then found 25 ERROR steps
over 12 routes (AGENT_NOTES.md line 669). "0 errors" is a build
condition, not a done condition.

`confirmed_by` in any future log is only SOURCE or INFERRED — never
DYN, FW-MEMORY, or UNVERIFIED. No count below is invented.

## What the re-audit changed (compared with the schema 1 graph)

- DRAFT, grounded: the method universe is `method_list.json`, 2,995
  methods, produced with `list_methods.py --jacoco` (the JaCoCo report
  filter, which drops generated code). Source: AGENT_NOTES.md line 98
  and line 159. The 117 extra methods from a fresh APK list
  (Dagger/Hilt injectors, BuildConfig, enum values, the JaCoCo
  receiver) are NOT graph nodes; they belong under Limits, one reason
  per group (AGENT_NOTES.md line 98).
- DRAFT, grounded, STAGE-5 ONLY (not final): at the stage-1 / stage-5
  builds the verdict split was REACHABLE 2,537 / UNREACHABLE 458
  (AGENT_NOTES.md lines 8, 9, 13, and the stage-5 build line: 2,995
  methods, 5,466 edges, 0 errors, 0 warnings). These are NOT final
  numbers.
- TO-VERIFY (source: final build output): the final method/edge counts,
  the final REACHABLE/UNREACHABLE split, and every schema-1 vs
  schema-2 difference. No schema-1 graph numbers were read in phase 1
  or phase 2, so no schema-1 comparison sentence is drafted as fact.
- TO-VERIFY (source: final graph + DECISIONS.md application record):
  which of the Stream-C decisions (D1–D7, R1–R8, recorded as Muse's own
  decisions for user/Yang review in stream-C `DECISIONS.md`) have been
  applied as graph edits, and what each changed. The decisions most
  likely to move this section are: the @SAVED variant model confirmed
  for the intro RESULT edge (D3); the tap-first @APP chain for app
  import (D5) with the Authy-default path left unmodelled; the root ENV
  gate on the app-import edge (D6); the @APP_GA variant pending the D7
  checked-row print; and the caller-context variant splits for the
  shared text-input relay, the shared error-dialog relay, the
  SwitchingProvider.get cases, and the shared saveAndFinish node
  (R2, R5, R6). Until the edits are applied and rebuilt, none of them
  may be described here as landed.

## How the checked paths were chosen

- DRAFT, grounded (history, NOT the final sample): the last fully
  documented sample is the round-7 sample:
  `graphs/Aegis/scratch/route_check_r7/sample_r7.txt`, seed 20261025,
  25 routes (AGENT_NOTES.md round-7 section). Round 7 checked those 25
  routes step by step against source, found 25 ERROR steps over 12
  routes and 13 routes with no ERROR (3 clean, 10 UNCLEAR-only), made
  no graph edit, and round 8 was not run — so round 8 would re-check
  the same graph and give the same verdicts (AGENT_NOTES.md line 669).
- DRAFT, grounded (steps 6–10 slice, re-derived, not a route clearance):
  in the steps 6–10 re-derivation, GlideRequests.asBitmap steps 6–10
  are CORRECT (steps 6, 7, 8, 10 SOURCE; step 9 SOURCE app part +
  INFERRED framework part — the launcher callback, androidx source not
  read), and Slot.<init> steps 6–10 are CORRECT as mechanics (steps 6,
  7 SOURCE; step 8 source mechanics SOURCE but its route-validity is
  the cold-start decision item; steps 9, 10 mechanics SOURCE/INFERRED
  inheriting step 8's item). The two checked routes are NOT cleared as
  a whole: GlideRequests has round-7 errors at steps 25, 28, 53, 65
  (AGENT_NOTES.md line 652) and Slot at steps 21, 27, 30 (line 655).
  The other 23 round-7 routes are NOT CHECKED — only 2 of the 25
  round-7 dumps are in the repo (`GlideRequests_asBitmap.txt`,
  `Slot_init.txt`, plus `sample_r7.txt`), confirmed by the steps 6–10
  leaf's fresh directory listing. A step not printed counts as not
  checked.
- DRAFT, grounded (earlier practice, for the method description only):
  the stage-1 sample was redrawn with `verify_sample.py` after the
  last graph change, and each route was then read step by step —
  current route first, then the source line, then a graph edit or a
  rejection with the line cited (AGENT_NOTES.md line 9).
- TO-VERIFY (source: fresh `verify_sample.py` run + fresh `show_route`
  dumps on the final build): the FINAL sample (size, seed, route list),
  the sampling rule it used, and the final error rate. The final
  section must describe the final sample, not round 7. Round 7 is
  history, not the final sample. The final error rate must be computed
  from the final sample's step verdicts, not carried from round 7
  (round-7 rate for reference only: 12 of 25 sampled routes with at
  least one ERROR step).
- TO-VERIFY (source: final route-check records): the classification
  rules applied in the final round — in particular rule D2 (a step whose
  only problem is a cross-run state is UNCLEAR, not ERROR), as
  confirmed for the final round in DECISIONS.md R1/R7/D2/D4, and the
  final treatment of the D7 GoogleAuthImporter route (ERROR until the
  checked-row print lands).

## What waits for a device (API 27)

DRAFT list, grounded only in code-read evidence already on the branch.
None of these items is claimed as reproduced on a device. `confirmed_by`
for any future log row about them is INFERRED unless a device run later
confirms it. Device checks are NOT STARTED; this section is the
handover for that later phase, not a claim that any device check passed.

- ENV-gated methods on the best route, not tested on a device (from the
  existing readme_notes.md Limits text, retained as evidence):
  MainActivity.handleIncomingIntent (ENV_VIEW, ENV_SEND);
  MainActivity.lambda$new$7 (ENV_PICK_IMAGE); ScannerActivity init and
  onCreate (ENV_CAMERA); WelcomeSlide lambdas (ENV_PICKER);
  ImportExportPreferencesFragment.lambda$new$0 and
  IconPacksManagerFragment.lambda$new$0 (ENV_PICKER);
  BackupsPreferencesFragment.lambda$new$0 (ENV_BACKUP_RESULT); export RESULT
  lambdas (ENV_EXPORT_RESULT); BiometricSlotInitializer
  .onAuthenticationSucceeded (ENV_BIOMETRIC).
- Baseline coverage gap (graphs/Aegis/review_notes.md, read in full in
  phase 1): the 1-hour runs got past first-run setup and showed the
  vault list, but the vault stayed empty — EntryAdapter.onBindViewHolder
  never ran — so nothing needing an entry (row binding, copy/edit/delete/
  group actions, action mode, TransferEntriesActivity) was exercised.
  Only 751 of the 2,995 methods ran. A device run with a populated vault
  is still needed to cover that region; it is device work and therefore
  out of this logs phase.
- Gates that only a device can discharge (review_notes.md): AuthActivity
  (password-protected, locked vault — the baseline vault opened without
  an unlock screen); Glide request classes (an entry with a custom icon
  or icon pack — baseline entries used the default letter icon); the
  other-authenticator importers (a backup file of that app; none among
  the baseline fixtures); quick-settings tile classes and biometric
  classes (emulators had no enrolled biometrics); the Android backup
  agent (entered from S_ENTRY through an env edge; the system Backup
  Manager creates it).
- Import-from-app path (review_notes.md + AGENT_NOTES.md round-7
  section): ImportEntriesActivity.lambda$startImportApp$5 to readFromApp
  / processImporterState needs a root shell and the other authenticator
  app installed (ImportEntriesActivity.java:149 shows a root error and
  finishes otherwise). Device confirmation needs root + that app
  installed. This is also the D6 root-gate item: the app-import edge
  carries an explicit root ENV gate in the decision model, so a
  standard-configuration route must not prefer it.
- TO-VERIFY (source: device plan, NOT this logs phase): the API 27 image
  / emulator choice, and whether any of the above was already covered by
  a later device run not recorded in the files read. Do not mark any of
  these as device-checked in a final log without a device-run record.
- DRAFT note for the finaliser (DECISIONS.md D5): add one Limits
  sentence (see Limits addendum below) recording that the app-import
  dialog's default-checked Authy path (DatabaseImporter.java:37) is not
  modelled; only the GA row-tap path is.

## Hazard candidates (from reading the code, not reproduced)

DRAFT list. Each item is a code-reading candidate only, explicitly NOT
reproduced. Keep this heading's disclaimer in the final text.

- SwitchPreference.setChecked(boolean) ignores its argument and always
  sets the switch on; the stored value is set through the androidx
  initial-value path (INFERRED, androidx source not read). Hazard
  candidate for the security page. Source: existing readme_notes.md
  Limits text.
- With android:fullBackupOnly="true" (AndroidManifest.xml:24), onBackup,
  onRestore and onQuotaExceeded are UNREACHABLE (INFERRED: the BackupAgent
  source is not in fw_src). A full-backup run on API 27 should show only
  onFullBackup and onRestoreFile running. Source: existing
  readme_notes.md Limits text.
- DropdownCheckBoxes filter: the framework runs the group filter
  (getFilter, performFiltering, publishResults, predicate lambda) even
  though typing is closed by app:allow_filtering="false"
  (dialog_export.xml:98, input type 0). The app source gives no trigger
  for that framework run and the AutoCompleteTextView source is not
  held. Open device item: open the export dialog's groups field and see
  whether the popup filters rows as the tap or the dialog opening
  triggers it. Source: existing readme_notes.md Limits text.
- Pin-switch visibility vs plain vault:
  SecurityPreferencesFragment.java:259–265 sets the pin switch visible
  only when the vault is encrypted, so routes that show the pin switch
  on a plain-text vault are suspect (AGENT_NOTES.md round-7 section:
  Slot step 21; detailed-multi step 21). Candidate, not a device finding.
- Default search mask: SEARCH_IN_ISSUER | SEARCH_IN_NAME
  (Preferences.java:198); GROUPS is set only by
  BehaviorPreferencesFragment.java:57. A same-run GROUPS search applies
  only after a relaunch, so it is a two-process route. Source:
  DECISIONS.md D4 (the two-process route decision: keep edge
  E399cebc2 with a prior-run needs_state; route verdict UNCLEAR under
  D2, not ERROR, not correct-as-printed). The final hazard text must
  follow the applied decision and the final route print, not pre-empt it.
- TO-VERIFY (source: final graph + applied decisions): whether each
  candidate above is still a live candidate on the final graph, and
  whether any new hazard candidate surfaced in round 7 / the final
  round. No new hazard candidate is asserted here.

## Limits

The existing Limits text below (batch-36-era) is the only finished
section of the branch file and is preserved VERBATIM, not replaced by
this draft. It was fetched in full from branch work-2026-10-31 this
session (SHA 24dd171e34df2d037731985a500cd2c5cab713f8). The dated
addendum after it is DRAFT and must be finalised in phase 2.

- Warnings after the batch-36 build (96 errors, 68 warnings; batches 33 to 36 added none): 67 are UNREACHABLE consistency flags (the 62 listed below from batch 22, plus the two TextDrawable$Builder flags, the two Dialogs flags and the batch-30 flag at the end of this list), and one is the REVIEW line. Each flagged method is UNREACHABLE, and every incoming edge comes from a caller that is also UNREACHABLE. None has a REACHABLE or UNRESOLVED caller, so no edge contradicts a verdict. The reasons:
  - GlideOptions (26 methods): generated Glide option class. The app source has no reference to GlideApp, GlideRequest or GlideOptions (grep of src/main/java, 0 hits). The instance methods are reached only from the static xxxOf and xxxTransform factories, which are UNREACHABLE. The GlideRequest and GlideRequests clusters are labelled in batch 22 (see the bullets below).
  - GlideRequest.apply and GlideRequest.<init>(Class,RequestBuilder) (2): UNREACHABLE in batch 22. Their only in-universe caller is GlideRequest.getDownloadOnlyRequest (auto_calls.json rows), which is also UNREACHABLE: the download paths (download, downloadOnly) are never called by the app (grep of the Glide-importing app files). Same consistency flag as the rest of this list.
  - Glide library path (batch 22, INFERRED; the Glide library source is not read): into(ImageView) at ui/glide/GlideHelper.java:41 and :54 reaches GlideRequest.clone, autoClone, optionalCenterCrop, optionalCenterInside and optionalFitCenter only when the ImageView scale type maps to them. These five are ENV-dependent on the view's scale type and were not tested on a device. GlideRequest.lock and GlideRequests.clearOnStop are UNREACHABLE INFERRED because the library may call them internally.
  - GoogleAuthProtos MigrationPayload (13) and OtpParameters (17): generated protobuf accessors. The app reads the payload through getOtpParametersList, getBatchId, getBatchIndex and getBatchSize (GoogleAuthInfo.java:204-271), none of which is flagged. The flagged methods (singular getOtpParameters, hasBatchIndex, clear*, set*Value, *Bytes, addOtpParameters(int,...), setOtpParameters, removeOtpParameters) have no caller outside the generated file. The protobuf cluster is not finished (its other methods are still errors).
  - ApkSignaturePin (2: getFingerprint, getSHA256Fingerprint): vendored library (info.guardianproject.trustedintents). The callers are getMD5Fingerprint, getSHA1Fingerprint, getSHA256Fingerprint and doFingerprintsMatchCertificates, all UNREACHABLE; the app source does not call any of them.
  - TrustedIntents.isIntentSane (1): private method of the same library. Its callers isReceiverTrusted(Intent) and startActivity are UNREACHABLE; the app source does not call isReceiverTrusted.
  - EntryAdapter.onItemDismiss (1): the only caller is SimpleItemTouchHelperCallback.onSwiped (SimpleItemTouchHelperCallback.java:98), which is UNREACHABLE because the touch helper enables only UP and DOWN drag, so no swipe starts (batch 18).
- One REVIEW line (not a method warning): the NONSTD_HINT regex at tools/build_graph.py:61 flags 7 edges (Ed430de74, Ed3b2fc19, E1c3ead1c, E9eaaba0b, E9e40d82d, E3c923e18, Ebdc15ea3) whose evidence contains the words dagger, library or reflect. Their edges are plain FRAMEWORK edges, so they are false positives. Not fixed; tools/ is not edited.
- TextDrawable$Builder.rect and TextDrawable$Builder.roundRect (batch 28, 2 flags): each has one incoming CALL edge, from buildRect and buildRoundRect. Both callers are UNREACHABLE (no app code calls them; grep of the app tree). No REACHABLE or UNRESOLVED caller exists, so no edge contradicts a verdict.
- Dialogs (batch 29, 2 flags): Dialogs.showErrorDialog(Context,String,Exception,OnClickListener) has one incoming CALL edge from the UNREACHABLE 3-argument String overload (Dialogs.java:360), and Dialogs.showTextInputDialog(Context,int,int,TextInputListener,boolean) has one incoming CALL edge from the UNREACHABLE 2-argument showPasswordInputDialog (Dialogs.java:255). Both callers have no app call sites (bytecode call rows), so the flags are the same kind as the batch-22 list.
- NotificationService.serviceMethod (batch 30, 1 flag): its one incoming CALL edge is from onStartCommand, which is UNREACHABLE because nothing starts the service. The start call in VaultManager.startNotificationService is inside a comment (VaultManager.java:280-283, issue #1047), and the manifest entry is not exported (AndroidManifest.xml:105). Same kind as the flags above.
- Batch 30 open items for a device check (not tested): (a) SwitchPreference.setChecked(boolean) ignores its argument and always sets the switch on; the stored value is set through the androidx initial-value path (INFERRED, androidx source not read). Hazard candidate for the security page. (b) With android:fullBackupOnly="true" (AndroidManifest.xml:24), onBackup, onRestore and onQuotaExceeded are UNREACHABLE (INFERRED: the BackupAgent source is not in fw_src). A full-backup run on API 27 should show only onFullBackup and onRestoreFile running.
- DropdownCheckBoxes filter (batch 28, INFERRED): the framework runs the group filter (getFilter, performFiltering, publishResults, and the predicate lambda) even though typing is closed by app:allow_filtering="false" (dialog_export.xml:98, input type 0). The app source gives no trigger for that framework run, and the AutoCompleteTextView source is not held. A tool run recorded the filter running, so these four routes are REACHABLE. Open item for a device check: open the export dialog's groups field and see whether the popup filters the rows as the tap or the dialog opening triggers it.
- ENV-gated methods (on the best route, not tested on a device): MainActivity.handleIncomingIntent (ENV_VIEW, ENV_SEND); MainActivity.lambda$new$7 (ENV_PICK_IMAGE); ScannerActivity.<init> and onCreate (ENV_CAMERA); WelcomeSlide lambdas (ENV_PICKER); ImportExportPreferencesFragment.lambda$new$0 and IconPacksManagerFragment.lambda$new$0 (ENV_PICKER); BackupsPreferencesFragment.lambda$new$0 (ENV_BACKUP_RESULT); export RESULT lambdas (ENV_EXPORT_RESULT); BiometricSlotInitializer.onAuthenticationSucceeded (ENV_BIOMETRIC).

### DRAFT addendum to Limits (to be finalised in phase 2 — do not publish as fact yet)

- The Limits text above opens with "Warnings after the batch-36 build
  (96 errors, 68 warnings...)". Those counts are batch-36-era and are
  superseded as build history by the stage-5 build (2,995 methods,
  5,466 edges, 0 errors, 0 warnings, AGENT_NOTES.md line 575) and then
  by the round-6/round-7 edits. Do not carry the "96 errors" figure
  forward as a current figure. The final Limits section needs a dated
  addendum stating which build the flag list was checked against.
- TO-VERIFY (source: final graph_def.py + final build output): the
  re-confirmation grep result — that every flagged method still has no
  REACHABLE or UNRESOLVED caller on the final graph. Do not finalise
  this addendum until that grep has run on the final graph.
- DRAFT sentence for the finaliser (DECISIONS.md D5, to be included
  once the @APP chain is verified on the final graph): "The app-import
  dialog's default-checked Authy path (DatabaseImporter.java:37) is not
  modelled; only the GA row-tap path is."
- DRAFT sentence for the finaliser (DECISIONS.md R3, library rule):
  Glide edges E265bbd0b, Ec449db03, E9d286870 are kept as INFERRED
  (Glide library source not read); E4db374dd is INFERRED-pending-print
  — its edge text must be printed and its evidence corrected to
  INFERRED wording before it counts, if it currently claims FW-SRC lines.
