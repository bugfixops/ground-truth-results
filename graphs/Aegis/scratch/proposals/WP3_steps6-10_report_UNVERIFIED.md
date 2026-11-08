# UNVERIFIED PROPOSAL — DO NOT RELY ON, MERGE, OR USE AS EVIDENCE YET

**Status: UNVERIFIED.** This is a coordinator first part from 2026-10-31, saved here so it is not lost. It has NOT passed a build, sampler, full-repo grep, or C1 checks on a full local checkout, and must be re-checked from printed source before any label, route, or graph change is relied on or merged.

**Branch rule:** work in progress is on work-2026-10-31 only, never main, and the 'result' branch is not used for work in progress unless the user says so.

---

# WP3 Aegis — steps 6–10 helper report (connector-only, NOT pushed, NOT verified for merge)

Status: PENDING, not pushable. No file in bugfixops/ground-truth-results was edited, merged
or pushed by this helper. No Yang decision was made. This is a proposed, separable check
report only.

## Scope clarification
"Steps 6–10" are the brief steps in handoff/AGENT_BRIEF_V2.md §4:
6 Paths, 7 Log (verification.csv), 8 Notes (readme_notes.md), 9 Final checks, 10 Lessons.
Within-route steps 6–10 were also checked where a route dump is actually in the repo
(see below). Both readings are reported so neither is silently assumed.

## Re-check of handover numbers (not re-verified by a build)
- Handover (handoff/MUSE_HANDOVER.md, work-2026-10-31) and AGENT_NOTES.md RESUME POINT
  (2026-10-28 02:42) agree: 2995 methods, 5466 edges, 0 errors, 0 warnings,
  graph_def.py md5 ad6d1fe684f0f1611557692115cd9e5b.
- This session did NOT run a build: this VM has no local clone and I cannot run
  tools/build_graph.py locally. The graph_def.py fetched from work-2026-10-31 this
  session has md5 5a7591221f153facc574eaad368aabc3 (4983 lines), which differs from the
  resume-point md5 — consistent with the round-6 edits recorded in AGENT_NOTES.md, but
  the diff was not verified and no current build count is claimed. Never use tool
  coverage, old generated graphs, or build REACHABLE counts as evidence; none is used here.
- Sample: graphs/Aegis/scratch/route_check_r7/sample_r7.txt (seed 20261025) lists 25 routes.

## The 7 "Decision for Yang" items — verbatim, from graphs/Aegis/AGENT_NOTES.md (work-2026-10-31)
Line numbers verified against the file actually read (they match the handover's
"about" numbers exactly):

1. Line 379: `- R1 step 13 (UNCLEAR): the ENTERS edge S_INTRO_WELCOME -> S_INTRO_PICKER compresses the Next tap and the setCurrentSlide producer. A SYSTEM producer and needs_state on the Next edges are a modelling decision for Yang (page node enough, or add the producer).`
2. Line 479: `- Route 4 step 9 (Ebac005d0): OPEN. The route header says explicit_standard_route=yes, but this step needs an icon pack left over from an earlier run (IconPackManager.java:136-158). Decision for Yang: reclassify the route as non-standard, or add the precondition.`
3. Line 599: `- Route 1, MainActivity.onIntroResult, step 21 = E1dcf1457 (RESULT, IntroActivity.onDonePressed -> MainActivity.lambda$new$1). ERROR confirmed: its guard needs the vault created by initNew (IntroActivity.java:100), but the route has no edge that reaches initNew, and the RESULT edge has no needs_state, so the router skips the producer (the NONE path with creds null passes the check at :92-96). Not fixed in this batch: a fix needs a continuation node after initNew (no RETURN kind exists in build_graph.py KINDS), so this is a modelling decision for Yang.`
4. Line 603: `  - step 14 (E399cebc2, SEARCH_IN_GROUPS): ERROR confirmed by source. Default mask is SEARCH_IN_ISSUER | SEARCH_IN_NAME (Preferences.java:198); GROUPS is set only by BehaviorPreferencesFragment.java:57 and read once in MainActivity.onCreate (MainActivity.java:234). A same-run change applies only after a relaunch, so this is a two-process route; decision for Yang (the R6E text "prior run" would make it UNCLEAR by rule D2, not ERROR).`
5. Line 609: `- G3_5 step 34 (lambda$startImportApp$5 -> GoogleAuthImporter.readFromApp): the app-import dialog opens with Authy checked (DatabaseImporter.java:37). OK on the app path now needs a row tap first: _IMP_APP -> Dialogs.lambda$showImportersDialog$26@APP (guard: GA row tapped) -> lambda$showImportersDialog$27@APP. The OK edge without a tap is removed. show_route GoogleAuthImporter.readFromApp now shows the tap. Decision for Yang: the default Authy app-import path is no longer modelled (see HANDOFF_V2.md run-9 entries).`
6. Line 636: `- GlideRequests step 50 (app import, file null, needs root): confirmed (ImportEntriesActivity.java:109-111 calls startImportApp; :143-153 finishes the page when the shell is not root). Not fixed: the app-import edge is the router's cheaper choice. Decision for Yang (see HANDOFF_V2.md R10-2).`
7. Line 659: `- GoogleAuthImporter.readFromApp (35): ERROR 24 (R, the row-tap edge $26@APP to OK $27@APP at graph_def.py:1130 is the R9-1 decision; the OK button reads the ListView's checked row, which the row listener does not set). Decision for Yang, not edited.`
   - Cross-check this session: work-branch graph_def.py:1130 is indeed
     `gui(_IMP_PICK_APP, _IMP_OK_APP, 'Tap OK after the Google Authenticator row was tapped …')`
     (lines 1130–1132), so the citation still points at the same edge. This does not
     decide the item.

Related, not counted among the 7: AGENT_NOTES.md lines 557–567 (Stage 5 OPEN list) also
leave cold-start relaunch edges E20e76e09/E57db524e/Ec7af65b2, the shared text-input
relay E41c33149/E02b5fa3e, Glide INFERRED edges E265bbd0b/Ec449db03/E9d286870 and
E4db374dd open for Yang. The cold-start item is what stops the Slot route below.

## Within-route steps 6–10 actually printed and checked
Only 2 of the 25 round-7 route dumps are in the repo under
graphs/Aegis/scratch/route_check_r7/: GlideRequests_asBitmap.txt and Slot_init.txt.
The other 23 dumps were not found in the repo (candidate filenames missed; AGENT_NOTES
says dumps were in "scratchpad r7/", outside the repo copy). A step not printed counts
as not checked, so the other 23 routes' steps 6–10 are NOT checked here — no verdict
is claimed for them.

Method: each dump step was matched to its graph_def.py edge line, and the cited app
source lines were printed this session from final_java_only/Aegis (work-2026-10-31)
and fw_src/android-8.1.0_r1. confirmed_by is only SOURCE or INFERRED below; no DYN,
FW-MEMORY or UNVERIFIED is used.

### GlideRequests.asBitmap (70 steps) — steps 6–10: CORRECT (steps only; route as a whole is NOT clear)
Round-7 errors on this route are at steps 25, 28, 53, 65 (AGENT_NOTES line 652), none in
6–10. Its step 50 is Yang item 6 above, so the route as a whole stays open regardless.
- Step 6, MainActivity.<init> -> MainActivity.onCreate, LIFECYCLE/standard:
  graph_def.py:310–311; FW_CREATE = FW-SRC ActivityThread.java:2729–2731,2741
  (graph_def.py:127–128, printed from fw_src this session: 2729–2731 callActivityOnCreate,
  2741 performStart); SRC MainActivity.java:192–194 printed (onCreate, super call). CORRECT.
- Step 7, MainActivity.onCreate -> MainActivity.onStart, LIFECYCLE/standard:
  graph_def.py:314–315; same FW_CREATE lines; SRC MainActivity.java:938–940 printed. CORRECT.
- Step 8, MainActivity.onStart -> MainActivity.startIntroActivity, CALL/explicit:
  graph_def.py:400–401, guard "vault init needed: no vault file exists";
  SRC MainActivity.java:942–948 printed (isVaultInitNeeded -> startIntroActivity, return).
  This is the fresh-install standard-config branch and the standard edge E0602e719 noted
  in AGENT_NOTES stage 5; it is not the cross-run relaunch edge. CORRECT.
- Step 9, MainActivity.startIntroActivity -> IntroActivity.<init>, INTENT/standard:
  graph_def.py:482–484, guard "_isDoingIntro false, MainActivity.java:604";
  SRC MainActivity.java:603–612 printed (guard at 604, Intent at 605, launcher launch at
  606). The launcher-callback part is INFERRED androidx (graph_def.py:138), which is
  allowed; it is not presented as SOURCE. CORRECT.
- Step 10, IntroActivity.<init> -> IntroActivity.onCreate, LIFECYCLE/standard:
  graph_def.py:485, FW_CREATE + SRC IntroActivity.java:35–41; SRC IntroActivity.java:35–41
  printed (super.onCreate, four addSlide calls). CORRECT.
- Caveat: the dump itself notes "(ActivityThread.java not found in the source tree)" for
  the FW lines; the fw_src copy in the repo was printed this session and does contain
  lines 2729–2741, so the FW claim is SOURCE here, not FW-MEMORY. Steps 1–5 and 11–70
  were not re-checked in this slice.

### Slot.<init>(UUID,byte[],CryptParameters) (37 steps) — STOPPED at step 8
- Steps 6–7: identical lifecycle edges to GlideRequests steps 6–7 above
  (graph_def.py:310–311, 314–315; FW_CREATE; MainActivity.java:192–194, 938–940). CORRECT.
- Step 8, MainActivity.onStart -> MainActivity.loadEntries, CALL/explicit, E20e76e09,
  needs_state=ST_PLAIN_VAULT_FILE: graph_def.py:428–431; SRC MainActivity.java:950–974,
  991–992 printed. This is the cold-start cross-run plain-text vault edge: the vault file
  was saved by an earlier intro run, with no in-run producer (AGENT_NOTES lines 538, 558;
  round-7 line 655 reclassifies this step ERROR -> UNCLEAR under D2). STOP on this route:
  no decision is made, steps 9–10 are NOT judged, and no fix is proposed for this route.
  (Graph_def lines for steps 9–10 exist — loadEntries -> S_LIST at 711–713 and
  S_LIST -> onOptionsItemSelected at 834–835 — but they are not verdicts.)
- Round-7 errors on this route at steps 21, 27, 30 (AGENT_NOTES line 655) are outside
  this slice and remain open.

### All other round-7 routes — NOT CHECKED (pending)
VaultBackupManager throwBadFormat, EntryAdapter.setTempHighlightEntry, MOTP.<init>,
MainActivity.importScannedEntries, IconPack$Icon.<init>, ImportExportPreferencesFragment
ExportResultListener.onTaskFinished, DigitCountVerifier.<init>, IconPackExistsException.getIconPack,
MainActivity.onIntroResult, Dialogs showPartialGoogleAuthImportWarningDialog$30,
ImportExportPreferencesFragment onImportSelectResult$11, AuthActivity onCreate$3,
GoogleAuthImporter.readFromApp, ApkSignaturePin.getSignatures, ScannerActivity.onOptionsItemSelected,
Dialogs showDetailedMultiErrorDialog$22, VaultGroup.equals, OtpInfo.isAlgorithmValid,
GlideOptions.clone, EntryAdapter doesAnyGroupMatchSearchFilter$1, Salsa20Engine.salsaCore,
Hilt_AegisApplication.<init>, AegisApplication.<init>.
For these, only the sample list and AGENT_NOTES round-7 error summaries were read; their
step texts were not printed, so no step verdict is claimed. In particular:
- Route 4 step 9 (Yang item 2) and Route 1 step 21 (Yang item 3) are NOT re-verified here.
  Note a tension to resolve, not a decision: AGENT_NOTES round-6 line 611 says the
  onIntroResult step-21 edge was fixed via the @SAVED variant, and round-7 line 666 lists
  MainActivity.onIntroResult (24 steps) as clean, yet the handover still lists route 1
  step 21 as open and item 3 still calls it a modelling decision for Yang. Do not treat
  it as closed until Yang decides and a fresh show_route is printed.
- The EntryAdapter search route's step 14 (Yang item 4) and step 8, and
  GoogleAuthImporter.readFromApp step 24 (Yang item 7), are likewise not re-checked.

## Brief steps 6–10 — status (all PENDING, none pushable)
- Step 6 Paths: NOT DONE. Round 7 checked 25 routes with 25 ERROR steps over 12 routes
  (AGENT_NOTES line 669), made no graph edit, and round 8 was not run, so there is no
  final-build sample, no redraw after a fix, and no final error rate. A fresh
  verify_sample + show_route run on a full checkout is still required.
- Step 7 Log: NOT DONE. graphs/Aegis/verification.csv does not exist in the repo and
  graphs/Aegis/make_verification.py does not exist (both fetch attempts failed).
- Step 8 Notes: NOT DONE. graphs/Aegis/readme_notes.md exists but its first four headings
  are all "Pending: this section is written when the Aegis graph reaches 0 errors";
  only Limits is written (batch-36-era text). gen_readme_v2 has not produced a finished
  v2 readme from it.
- Step 9 Final checks: NOT DONE and NOT RUN this session (no local checkout/tools).
  The stage-5 final checks (AGENT_NOTES lines 574–579: build 0/0, citations 0 problems,
  bytecode 0 mismatches) are for the stage-5 build, not the current graph.
- Step 10 Lessons: NOT DONE. graphs/Aegis/LESSONS.md does not exist in the repo.

## Proposed fixes (not merged) — non-decision routes only
- None. GlideRequests steps 6–10 need no fix; Slot is stopped at its decision step;
  the other 23 routes were not printed, so proposing fixes for them would be guessing.
  No graph_def.py, out/, progress/notes, tools/ or other helper file was edited.

## Blockers
1. Yang's 7 decisions above (handover D1) — Aegis cannot be reported done until they are made.
2. No local clone / cannot run tools/build_graph.py, verify_sample.py, show_route.py,
   check_citations.py, check_routes.py, check_bytecode_lines.py, scan_unreachable.py,
   make_verification.py or gen_readme_v2.py from the connector-only copy. All step 6–10
   verification that needs those tools is pending on a full checkout.
3. Only 2 of 25 round-7 route dumps are in the repo; the rest must be re-printed from a
   full checkout before their steps 6–10 can be judged.
4. Aegis is NOT done and must not be ticked. Do not claim Aegis is done.
