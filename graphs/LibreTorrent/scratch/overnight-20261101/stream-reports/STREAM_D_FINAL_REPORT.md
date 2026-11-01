# Stream D — FINAL REPORT (consolidation from files only)

Branch `work-2026-10-31`, repo `bugfixops/ground-truth-results`.
Scope: logs + route checks for the 8 ticked apps. No device checks.

## How this report was produced (read this first)

The Stream D coordinator ended without a final report (one leaf errored; the
Vanilla-Music final handoff never arrived). This report consolidates ONLY what
is already on disk under `~/workspace/overnight/stream-D/`: `RUN_LOG.md`,
the stream `DECISIONS.md`, each app's `DECISIONS.md`, and each app's scratch
outputs (build reports, check outputs, sample/judgment files, logs). Every
number below was either read from one of those files or re-verified by a
read-only command (`grep`/`wc`/`ls`) against them in this close-out.

NOT done in this close-out: no route was re-judged, no label was changed, no
build or check was re-run, no branch file was edited, nothing was pushed, no
device work was done. Where a claim is not in any file, this report says
NOT IN FILES rather than filling the gap.

Two close-out findings the parent must know before any morning push:

1. **Token-bearing URL redacted.** `Vanilla-Music/scratch/fetch_batch6.log`
   contained a connector-returned raw download URL carrying a token parameter
   (the connector's "too large to display" fallback for
   `ActivityManagerService.java`). The close-out replaced the token value with
   `REDACTED` in place (1 redaction, verified: 0 long token parameters remain
   in that file). A full audit of stream-D text files found no other long
   token parameter; the only other `token=` matches are 1-character fragments
   in Omni-Notes raw fetch JSON, which cannot be credentials. The token value
   itself is never reproduced anywhere in this report. Morning action: confirm
   no token-bearing content is pushed; the redacted log is local scratch only.
2. **Tick-marker hygiene.** Overnight-authored files contained only
   meta-mentions of the tick marker in constraint text ("never write the tick
   marker"); those were reworded so no overnight-authored file now contains
   the literal tick-marker string. EXCEPTION, flagged not fixed:
   `openlauncher/graphs/openlauncher/AGENT_NOTES.md` lines 27–55 contain a
   pre-existing branch checklist ("step 1 … step 10") with tick markers. That
   file is the branch mirror, not overnight-authored text, so the close-out
   did not edit it. Morning action: confirm at merge that those lines are
   branch content and decide whether they stay.

Process notes from `RUN_LOG.md`: a VM/runtime restart at ~07:52 UTC wiped
`/tmp` (raw fetch JSON lost; workspace survived) and Java was lost in the
restart (`java: command not found`); no remaining step strictly needed javac.
The Diary original worker errored on the restart drain; a takeover worker
completed Diary from the surviving files (re-verified byte-identically).
Vanilla-Music's status below is verified from its scratch files alone — no
handoff was invented for it.

## Per-app gate table

| App | Gate | One-line reason |
|---|---|---|
| Currency | BLOCKED (tooling only) | Check (2) partial on oversize ActivityManagerService; verification.csv not regenerated (no generator on branch) |
| Diary | BLOCKED (tooling only) | Check (2) exits 1 on the same oversize file; verification.csv not regenerated (no generator on branch) |
| hash-checker | REACHED FOR CONTENT ONLY (qualified) | Labels/routes/logs content pass; check (2) partial on the same file + verification.csv preserved, not regenerated |
| Omni-Notes | NOT FULLY REACHED | 1 documented wrong route + verification.csv regeneration blocked + scan --all not run |
| openlauncher | PASSED except check (2) cache caveat | Everything else passes; check (2) 62/64 on two oversize framework files |
| Vanilla-Music | NOT FULLY REACHED | Check (2) partial on the same file + check (4) not run + scan --all not run |
| Markor | BLOCKED | `auto_calls.json` (2,090,438 B) over the connector display limit; build exits 1 |
| AnyMemo | BLOCKED | `auto_calls.json` (1,132,200 B), `methods.csv` (3,282,143 B), trigger-graph JSON (4,221,347 B) all over the limit |

No app's status line was written to any PROGRESS file by this stream. The
`[K]` lines quoted below are proposals only.

## Currency (145 methods)

- **Build:** `python3 -I tools/build_graph.py graphs/Currency Currency`
  (from `Currency/scratch/build_final.txt`, re-verified): methods 145, pages
  22, edges 393; REACHABLE 140 / UNREACHABLE 5; errors 0, warnings 0;
  STALE 0; STRICT=True (`scratch/eight_checks.md`: "STRICT = True in
  graph_def.py (line 20)"). Handover count 145 confirmed by own build.
- **Sample:** `verify_sample.py Currency 30 20261025` drew 27 methods /
  107 edges (tool quotas exhaust at 27; `Currency/DECISIONS.md` D3).
  Judged (`scratch/route_judgements.md`, `scratch/sample_30_final.txt`):
  23 correct / 0 fixed / 0 wrong / 4 unclear; error rate 0.0 over judged
  routes (23). No fix, redraw identical.
- **Eight checks** (`scratch/check*.txt`, `scratch/eight_checks.md`):
  (1) build PASS; (2) check_citations PARTIAL — 41 distinct, 2 problems,
  both `am/ActivityManagerService.java` file-not-held (1,086,106 B, connector
  display limit; token URL not used), 0 FW-MEMORY/DYN/UNVERIFIED evidence;
  (3) check_routes PASS, 0 flagged; (4) check_bytecode_lines PASS, 0 bad
  (vacuous per RUN_LOG — 0 bytecode-cited edges); (5) DEAD|FRAMEWORK_ONLY 0
  PASS; (6) FW-MEMORY 0 PASS; (7) PENDING 0 PASS; (8) scan PASS with
  explanations (Singleton.getList hit = explained dead else-branch, D5).
- **Logs:** verification.csv = unchanged branch copy (98 rows, header exact);
  the 2 new path judgments (Parser$Handler init, Main.onDateResult) live only
  in `scratch/route_judgements.md` (D1 — not hand-appended). readme_notes.md
  updated (five headings in order, verified) + README generated via
  gen_readme_v2.py (exit 0; tool printed 51 lines, 93 lines on disk — minor
  discrepancy, see open items). LESSONS.md 6 bullets (verified by count).
  AGENT_NOTES.md updated (`scratch/AGENT_NOTES.md`, `scratch/eight_checks.md`).
- **Gate:** BLOCKED on tooling only (check (2) partial + missing generator).
- **Decisions** (`Currency/DECISIONS.md`, all Muse's own, never Yang's):
  D1 verification.csv not hand-edited for the 2 new judgments; D2 the 2
  citation problems are a reconstruction blocker, not graph errors; D3 the
  27-method sample is accepted as complete; D4 the 4 unclear routes stay
  unclear (launcher/IME steps not read); D5 scan hit on Singleton.getList
  does not change its label; D6 readme history kept, re-check appended.

## Diary (286 methods)

- **Build:** `python3 -I tools/build_graph.py graphs/Diary diary`
  (`Diary/scratch/build.txt`): methods 286, pages 34, edges 1435;
  REACHABLE 265 / UNREACHABLE 21; errors 0, warnings 0, STRICT=True.
- **Sample:** `verify_sample.py Diary 30 20261025`: 30 routes, 370 steps
  (`scratch/sample_30.txt`, redraw `scratch/sample_30_redraw.txt`
  identical): 18 correct / 7 fixed / 0 wrong / 5 unclear; error rate 0.28
  ((7+0)/(18+7+0)). Judgments carried after exact edge-match with the branch
  verification path rows (30/30) + fresh spot-check of the 5 unclear routes
  (D3, D10); takeover re-verified build/sample byte-identically.
- **Eight checks:** (1) build PASS; (2) check_citations exit 1 —
  81 distinct, 1 problem (`ActivityManagerService.java` file-not-held),
  0 line-range errors (`scratch/check_citations_takeover.txt`); (3)
  check_routes PASS, 0 flagged; (4) check_bytecode_lines 0 bad PASS
  (vacuous in the first run; genuine re-run in the takeover);
  (5) DEAD|FRAMEWORK_ONLY 0; (6) FW-MEMORY 0; (7) PENDING 0;
  (8) scan_unreachable --all genuine PASS (triaged by overload/declaring
  class, D8); --callers n/a (no auto_calls.json).
- **Logs:** verification.csv kept unchanged (128 rows, header exact) for want
  of the generator (D1). readme_notes.md five headings in order +
  gen_readme_v2.py README done (`graphs/Diary/out/README.md`, 90 lines on
  disk). LESSONS.md 8 bullets. AGENT_NOTES.md updated.
  Recovered: DATASET.txt (target_sdk 28) and sanity_check.csv (286 rows,
  187 ran, 0 UNREACHABLE-but-ran).
- **Gate:** BLOCKED on the AMS file-not-held + missing generator only.
  Proposed line (NOT written, from RUN_LOG): "[K] Diary (labels, route checks
  and logs DONE 2026-11-01; device checks not started; awaiting user tick)".
- **Decisions** (`Diary/DECISIONS.md`, Muse's own): D1 generator absent, file
  kept unchanged; D2 the "81 problems" were missing-cache, not citation
  errors; D3 judgments carried on exact edge-match + fresh spot-check;
  D4 first scan run vacuous, not a pass; D5 DATASET target_sdk 28 vs graph
  API 27 recorded, not changed; D7 AMS fetch stopped after two identical
  failures (connector limit, not wrong path); D8 scan hits triaged by
  overload/class, no label change; D9 gate BLOCKED, not waived, on the single
  AMS item (+ D1); D10 takeover re-verified rather than re-derived;
  D6 no device checks, no pushes, no branch edits.

## hash-checker (529 methods)

- **Build:** `python3 -I tools/build_graph.py graphs/hash-checker hash-checker`
  (`hash-checker/scratch/build_1.txt`): methods 529, pages 39, edges 1314;
  REACHABLE 507 / UNREACHABLE 22; errors 0, warnings 0, STRICT=True,
  UNRESOLVED 0, STALE 0. Handover count confirmed.
- **Sample:** redrawn 30 routes / 213 edges, all judged correct, 0 fixed,
  0 wrong, error rate 0.0, no graph change (`scratch/sample_30.txt`,
  `scratch/routes_30_steps.txt`).
- **Eight checks:** (1) build PASS; (2) check_citations 14/15, 1 problem =
  ActivityManagerService oversize file, FW-MEMORY/DYN/UNVERIFIED 0 (D5);
  (3) check_routes 0 flagged; (4) check_bytecode_lines 548 checked, 0 bad;
  (5) DEAD/FRAMEWORK_ONLY explained (legacy dicts converted by the build,
  built JSON clean, D2); (6) FW-MEMORY 0; (7) PENDING explained (screen name
  S_MAIN_EXIT_PENDING only, D2); (8) scan --all 22/22 triaged, no
  contradiction; --callers 4 explained.
- **Logs:** verification.csv preserved verbatim + validated (124 rows +
  header = 125 lines on disk), NOT regenerated — generator absent (D1).
  readme_notes.md five headings in order; README generated (tool printed
  51 lines, 85 lines on disk — minor discrepancy, see open items).
  LESSONS.md 7 bullets. AGENT_NOTES.md + DECISIONS.md written.
- **Gate:** REACHED FOR CONTENT ONLY (leaf D6-final wording, quoted exactly
  because it is qualified, not an unqualified pass): labels pass, routes
  pass, logs content passes; the two open items change no label or route
  (D1 generator absent; D5 AMS citation unverified). Proposed line (from
  RUN_LOG, NOT written): "[K] hash-checker (labels, route checks and logs
  DONE 2026-11-01; device checks not started; awaiting user tick)".
- **Decisions** (`hash-checker/DECISIONS.md`, Muse's own): D1 generator
  missing — branch file used as build input, not invented; D2 greps
  explained, not zero raw hits and not failures; D3 error-rate basis (this
  check's fixes only, not the 8 historical fixes); D4 scan scope main +
  thirdPartyStores only (no googlePlay copies — correct for the debug
  build); D5 AMS citation left unverified, not marked failed; D6 gate call
  as above.

## Omni-Notes (1456 methods)

- **Build:** `python3 -I tools/build_graph.py graphs/Omni-Notes omni-notes`
  (`Omni-Notes/scratch/build_omni-notes.txt`): methods 1456, pages 68,
  edges 3803; REACHABLE 1202 / UNREACHABLE 254 (194 no_trigger_in_app,
  34 framework_never_calls, 21 closed_by_configuration, 5
  branch_never_taken); errors 0, warnings 0, STRICT=True
  (graph_def.py:2422), UNRESOLVED 0. Local build report byte-identical to
  branch build report per RUN_LOG. Handover count confirmed.
- **Sample:** `verify_sample.py Omni-Notes 30 20261025`: 30 routes, 526
  steps (`scratch/sample_30_routes.txt`), judged fresh in
  `scratch/sample_30_judgment.md`: 29 correct / 0 fixed / 1 wrong /
  0 unclear; error rate 1/30 = 0.0333. Redraw byte-identical (no fixes
  applied). The 1 wrong route: DbHelper.deleteNote — FAB-created new note +
  merged-note STATE are mutually exclusive (DetailFragment.java:508 set
  only from the "merged_notes" extra, put by ListFragment.java:1755 in the
  Merge flow); label REACHABLE is right, a real Merge path exists (D3).
- **Eight checks:** (1) build PASS; (2) check_citations PASS, 18 distinct,
  0 problems (after AdapterView fetch); (3) check_routes PASS, 0 flagged;
  (4) check_bytecode_lines PASS, 1381 checked, 114 skipped, 32 implicit,
  0 bad (final re-run after 45-file fetch); (5) DEAD|FRAMEWORK_ONLY literal
  11 / effective 0, mechanism-only (dicts emptied at graph_def.py:2145
  before the build; D1); (6) FW-MEMORY 0 PASS; (7) PENDING 0 PASS (DYN 0
  also); (8) --callers PASS, 5/254 explained; --all NOT RUN (no full tree,
  D7).
- **Logs:** verification.csv branch-verbatim (370 rows + header = 371 lines
  on disk), regeneration BLOCKED — make_verification.py not locatable on
  the branch (absent from tools/ root and tools_dev/; scoped search_code
  returned 0 with incomplete_results=true, which is not proof of absence
  elsewhere, D2). Fresh judgments live only in
  `scratch/sample_30_judgment.md`. readme_notes.md five headings in order
  verified; gen_readme run, local README byte-identical to branch per
  RUN_LOG (19,475 B; 99 lines on disk). LESSONS.md 7 bullets. AGENT_NOTES.md
  local mirror updated after every step.
- **Gate:** NOT FULLY REACHED. Labels PASS; route checks 29/30 with 1
  documented wrong route; logs complete except verification.csv regeneration
  blocked; scan --all not run.
- **Decisions** (`Omni-Notes/DECISIONS.md`, Muse's own): D1 literal-11 grep
  reported honestly, not faked to 0; D2 verification.csv regeneration
  blocked, branch file kept verbatim; D3 deleteNote judged wrong, no local
  graph fix attempted (needs a new @MERGE editor context, not a one-edge
  edit); D4 clinit-ordering steps are a convention, not errors; D5 targeted
  fw_src cache valid, partial cache not a pass; D6 minimal-tree bytecode
  runs reported with their caveat (flavor disambiguation limited — built
  flavor `play`); D7 scan --all not run, not faked; D8 coverage artifacts
  not label evidence; D9 file locations resolved via method_list.json class
  paths, not guesses; D10 branch root AGENT_NOTES.md is AmazeFileManager's,
  not Omni-Notes' (nothing copied across); D11 sketch-route Back link
  accepted via fragment recreation.

## openlauncher (900 methods)

- **Build:** `python3 -I tools/build_graph.py graphs/openlauncher openlauncher`
  (`openlauncher/scratch/build_2.txt`): methods 900, pages 43, edges 1515;
  REACHABLE 728 / UNREACHABLE 172 (143 no_trigger_in_app, 19
  closed_by_configuration, 10 framework_never_calls); errors 0, warnings 0,
  STRICT=True (graph_def.py:1314). Handover count confirmed.
- **Sample:** `verify_sample.py openlauncher 30 20261025` drew 27 methods /
  194 edges (strata quotas cap below 30, D3). Judged step by step
  (`scratch/routes_27_full.txt`, 2441 lines): 26 correct / 1 fixed /
  0 wrong / 0 unclear; error rate 1/27 = 0.037. The 1 fixed route
  (DialogUtils.copy) was already fixed in the fetched graph_def and was
  independently re-checked against DialogUtils.java:146-182 (D4). Route edge
  ids identical to branch verification.csv path rows (0 mismatches). Final
  redraw identical.
- **Eight checks:** (1) build PASS; (2) check_citations PARTIAL — 64
  distinct, 2 problems, both file-not-held oversize framework files
  (ActivityManagerService 1,086,106 B, PackageManagerService 1,190,171 B),
  0 line-range problems (D1); (3) check_routes PASS, 0 flagged;
  (4) check_bytecode_lines PASS, 569 checked / 60 skipped / 16 implicit /
  0 bad; (5) DEAD|FRAMEWORK_ONLY 0 PASS; (6) FW-MEMORY 0 PASS;
  (7) PENDING 1 explained (AsyncTask.Status.PENDING guard text,
  HideAppsFragment.java:942, not a marker, D2); (8) scan --all + --callers
  PASS, 2/172 with outside callers, both explained
  (Home$CallLogObserver, closed_by_configuration).
- **Logs:** verification.csv REGENERATED via
  `graphs/openlauncher/make_verification.py` (found in the app dir, not in
  tools/): 263 rows + header = 264 lines on disk, BYTE-IDENTICAL to branch
  per RUN_LOG. Rebuild with it: errors 0, warnings 0, path SOURCE_OK 27 /
  UNCHECKED 701. readme_notes.md five headings in order; README generated
  (tool printed 51 lines, 81 lines on disk — minor discrepancy, see open
  items). LESSONS.md 6 bullets (per the branch-mirror AGENT_NOTES step 10).
  AGENT_NOTES mirror (branch content; see the tick-marker note above).
- **Gate:** PASSED except the check (2) cache caveat. No other item open.
- **Decisions** (`openlauncher/DECISIONS.md`, Muse's own): D1 the 2 residual
  citation problems are a cache blocker, not a graph failure; D2 the single
  PENDING hit is legitimate source terminology; D3 the sample is 27 routes
  and the rate is computed over 27; D4 no graph change from this
  re-verification; the DialogUtils "fixed" row stays "fixed" (history, not a
  current-graph error).

## Vanilla-Music (1473 methods) — verified from scratch files alone

No final leaf handoff arrived for this app. Everything below comes from
`Vanilla-Music/scratch/` files and `Vanilla-Music/DECISIONS.md` on disk,
re-verified by read-only commands in this close-out. Nothing is synthesized
from the missing handoff.

- **Build:** `python3 -I tools/build_graph.py graphs/Vanilla-Music vanilla`
  (`scratch/build_2.txt`): methods 1473, pages 44, edges 3429;
  REACHABLE 1325 / UNREACHABLE 148 (144 no_trigger_in_app, 4
  branch_never_taken); SOURCE 1157 / INFERRED 316; errors 0, warnings 0,
  STRICT=True, UNRESOLVED 0, STALE 0. Matches branch AGENT_NOTES counts
  exactly per RUN_LOG.
- **Sample:** `verify_sample.py Vanilla-Music 30 20261025`: 30 methods /
  270 edges (`scratch/sample_30.txt`, `scratch/routes_30.txt`). This-run
  re-verification (`scratch/route_judgments.md`, 207 lines): 30 correct /
  0 newly fixed / 0 wrong / 0 unclear — 0 new errors. Two method-level
  caveats recorded, neither changing a label: SongTimeline.removeSongPosition
  (LiftAnimator/RemoveAnimator dispatch) and MediaLibrary.renamePlaylist
  (create-dialog entry vs rename callback) — coherent paths exist in both
  cases (D3). No fix applied this run, so the final sample is the initial
  sample (same 30 methods/order as make_verification.py's list).
  SEPARATELY, the branch logging convention logs a sampled path as "fixed"
  when its route runs through the systemic onResume fix, even though it
  reads correct after the fix. Under that convention the regenerated
  verification.csv path rows are 19 fixed / 11 correct / 0 wrong, error
  rate 19/30 = 0.633 — identical to the branch record (D3). Both rates are
  reported here and must not be conflated: 0.0 new errors this run;
  0.633 logged-convention rate carried from the branch's fix history.
- **Eight checks:** (1) build PASS; (2) check_citations PARTIAL — 100
  distinct, 1 problem: edge E40f400d7 (S_LIBRARY_PAUSED ->
  PlaybackService.onDestroy), ActivityManagerService:22975 segment
  unverified (file over the connector limit; single retry failed
  identically); other two segments held and verified; 0 FW-MEMORY/DYN/
  UNVERIFIED (D5; `scratch/check_citations.txt`). HandlerThread.java was
  missing from the batch list and was caught by the checker's own
  enumeration and fetched (5,279 B). (3) check_routes PASS, 0 flagged
  (also 0 flagged on build 2). (4) check_bytecode_lines NOT RUN — the
  remaining ~67 app files were deliberately not fetched (D1: ~1 more hour
  of fetches at ~30 s each, rising 429 risk shared with 7 other leaves);
  the prior session's pass on the byte-identical-count rebuild is cited as
  carry-over evidence only, not re-claimed (`scratch/check_bytecode_lines_NOT_RUN.md`).
  (5) DEAD|FRAMEWORK_ONLY 0 PASS; (6) FW-MEMORY 0 PASS; (7) PENDING 0 PASS
  (`scratch/check_routes.txt`, greps per RUN_LOG). (8) --callers PASS,
  3/148 with outside callers, exactly the branch-explained three
  (LiftAnimator.onStart/onUpdate via never-constructed LiftAnimator;
  removeItem(int) via never-configured CLICK_REMOVE mode,
  `scratch/scan_callers.txt`); --all NOT RUN
  (`scratch/scan_all_NOT_RUN.md`, same D1 reason).
- **Logs:** verification.csv REGENERATED only via make_verification.py
  (exit 0, header exact): Counter label correct 178, edge correct 70 /
  edge fixed 10, path fixed 19 / path correct 11; 288 rows + header =
  289 lines on disk (`scratch/make_verification.txt`). Build 2 with it:
  exit 0, errors 0, warnings 0, path SOURCE_OK 30; check_routes on build 2:
  0 flagged. readme_notes.md five headings in order; Limits prose corrected
  315 -> 316 (missed instance) in the local mirror only, README regenerated
  (tool printed 53 lines, 91 lines on disk — minor discrepancy, see open
  items). LESSONS.md 8 bullets (verified by count, in
  `graphs/Vanilla-Music/LESSONS.md`). AGENT_NOTES local mirror consolidated
  (`scratch/AGENT_NOTES_local.md`, `scratch/agent_notes_appendix_final.md`;
  `graphs/Vanilla-Music/AGENT_NOTES.md`, 75 lines on disk).
- **Gate:** NOT FULLY REACHED. Open: check (2) partial on the AMS segment;
  check (4) not run; scan --all not run. Routes and logs are otherwise done.
  No proposed status line for Vanilla-Music appears in any file on disk
  (NOT IN FILES — none is invented here).
- **Decisions** (`Vanilla-Music/DECISIONS.md`, Muse's own): D1 scope of
  re-verification vs full source fetch (the two not-run checks, with exact
  blockers); D2 readme prose counts corrected to the rebuild in the local
  mirror only (1157/316, 270 sample edges; labels unchanged); D3 dual-rate
  reporting as above; D4 LESSONS kept at 8 bullets; D5 check_citations
  reported PARTIAL, not pass, over the one unfetchable framework file, and
  the onDestroy label NOT changed on that basis.

## Markor (2864 methods) — GATE BLOCKED

- **Build:** `python3 -I tools/build_graph.py graphs/Markor markor`, exit 1
  (`Markor/scratch/build_attempt2.txt`): `graph_def.py:1293`, AUTO is None
  because `graphs/Markor/auto_calls.json` (2,090,438 B) exceeds the connector
  get_file_contents display limit (blob-SHA retry also failed; raw URL with
  a token NOT used, D1). No build counts exist from this run — none are
  claimed. Branch figures, NOT re-verified (D2): 2864 methods (2859 in
  method_list.json + 5 framework nodes), 2450 REACHABLE / 414 UNREACHABLE,
  6891 edges, errors 0, warnings 0; branch verification.csv paths 13 correct
  / 17 fixed (prior error rate 17/30 = 0.567 is prior work only, D3).
- **Own work that did run:** py_compile passes on graph_def.py + tools;
  static AST UNREACHABLE count 414 (404 no_trigger_in_app, 9
  closed_by_configuration, 1 closed_by_api_level; SOURCE 272 / INFERRED
  142) — matches the branch build report exactly, but is corroboration of
  the hand-written dict only, NOT a build verdict (5214 of 6891 edges are
  auto edges, D2).
- **Sample:** NOT RUN (needs out/methods.csv, 2,228,936 B, also over the
  limit). No sample error rate exists; the branch 0.567 is NOT this run's
  rate (D3).
- **Eight checks:** (1)–(4) NOT RUN; (5) DEAD|FRAMEWORK_ONLY 0 PASS;
  (6) FW-MEMORY 0 PASS; (7) PENDING 0 PASS (`scratch/check_greps.txt`,
  re-verified); (8) NOT RUN (needs build output / source tree).
- **Logs:** NOT regenerated. Branch mirrors only: verification.csv 562 rows
  + header = 563 lines on disk; readme_notes.md five headings in order
  (90 lines); LESSONS.md 8 bullets. Local DECISIONS.md, AGENT_NOTES.md, and
  `scratch/BLOCKER_AND_STATUS.md` written instead (D5).
- **Gate:** BLOCKED. Morning need: an authorized route for auto_calls.json
  only (e.g. Mac clone) — or acceptance of build-blocked status.
- **Decisions** (`Markor/DECISIONS.md`, Muse's own): D1 no token-URL fetch;
  D2 no hand-only build or static counts presented as the gate; D3 branch
  sample not claimed as this run's route check; D4 greps 5–7 genuinely
  runnable and passing, the rest not run rather than run vacuously; D5 logs
  not regenerated; D6 no tick marker, no push, no branch edit.

## AnyMemo (2207 methods) — GATE BLOCKED

- **Build:** NO full local build exists. Partial NO-AUTO build only
  (`AnyMemo/scratch/build_partial_noauto.txt`, D2 — USE_AUTO=False, stub
  auto_calls): methods 2207, edges 1474, REACHABLE 663, UNREACHABLE 241
  (= branch), UNRESOLVED 1303, errors 1304, warnings 0. This is diagnostics
  only, NEVER the gate build. Branch build report (reference only):
  REACHABLE 1966, UNREACHABLE 241, errors 0, warnings 0, SOURCE_OK 30.
  method_list.json confirms 2207 methods (handover count).
- **Sample:** independent redraw BLOCKED (methods.csv 3,282,143 B
  unfetchable). Consistency re-verification only (`AnyMemo/scratch/
  route_check_final.md`, D3): 30/30 correct, error rate 0.0 on that basis —
  branch final sample (seed 20261025) + verification.csv path rows +
  route prints cross-matched locally (20 exact in kiro_routes_all.txt;
  10 prefix-truncated by the known show_route comma bug, full comma-safe
  prints in scratch/route_print/ matched exactly) + fresh AnyMemo.java
  startup-trunk lines + branch build SOURCE_OK 30. This is NOT an
  independent redraw and must not be quoted as one.
- **Eight checks:** (1) partial only (above); (2) check_citations NOT RUN;
  (3) check_routes NOT RUN; (4) check_bytecode_lines NOT RUN;
  (5) DEAD|FRAMEWORK_ONLY 0 PASS; (6) FW-MEMORY 0 PASS; (7) PENDING 0 PASS
  (all three on the fetched graph_def.py); (8) scan NOT RUN (needs out
  JSON + sources).
- **Logs:** verification.csv NOT regenerated (make_verification.py needs
  out/); branch copy preserved as reference
  (`scratch/verification_branch.csv`, 346 rows + header = 347 lines on
  disk). readme_notes.md mirror: five headings in order + overnight
  addendum (93 lines). LESSONS.md 8 bullets (32 lines). AGENT_NOTES.md
  mirror updated (203 lines). DECISIONS.md D1–D4.
- **Gate:** BLOCKED. Blocker (single class, D2): connector display limit on
  auto_calls.json (1,132,200 B), methods.csv (3,282,143 B), and
  trigger_graph.json (4,221,347 B); token-bearing download URL not used.
  Morning need: authorized route for the large files (e.g. Mac clone) or
  acceptance of build-blocked status.
- **Decisions** (`AnyMemo/DECISIONS.md`, Muse's own): D1 the AnyMemo
  storage-permission question — DECIDED: WRITE_EXTERNAL_STORAGE stays an
  explicit ENV gate ONLY on the startup trunk (ENV_STORAGE_PERM,
  graph_def.py:157, on the three loadUiComponents edges; S_PERM_STORAGE,
  line 1765, for the not-granted branch). NOT pre-granted globally (fresh
  install must pass the dialog or the activity dies via finish(),
  AnyMemo.java:178, freshly printed) and NOT re-gated on every storage
  route (the app checks the permission only at startup, AnyMemo.java
  lines 124–182; downstream use inherits the gate through the trunk). No
  graph change needed — current modelling already says this. If the user
  prefers the pre-granted reading, the change would be to drop
  ENV_STORAGE_PERM from the three loadUiComponents edges; that change is
  NOT made. D2 partial-build approach labelled, never gated; D3 route
  judgment basis as above; D4 no branch edits, no pushes.

## Cross-app patterns (for the parent's morning decisions)

1. **One systemic blocker, five apps.** ActivityManagerService.java
   (1,086,106 B) exceeds the connector display limit and blocks a full
   check (2) pass for Currency, Diary, hash-checker, openlauncher (which
   additionally loses PackageManagerService.java, 1,190,171 B), and
   Vanilla-Music. Every affected leaf refused the token-bearing download
   URL. This is a tooling limit, not evidence against any citation: in all
   five apps every other distinct citation resolved with 0 line-range
   problems and 0 FW-MEMORY/DYN/UNVERIFIED evidence.
2. **A second systemic blocker, two apps.** Markor and AnyMemo cannot build
   at all on this VM because their auto_calls.json (and, for AnyMemo, the
   out/ files) exceed the same limit. Same limit family as Stream C (Aegis)
   and Stream B (Amaze/Anki/MMEX) — the morning's single biggest unblock is
   an authorized route for large files (e.g. the user's Mac clone).
3. **Generator location is a cross-app question.** make_verification.py was
   found in the app dir for openlauncher and Vanilla-Music, but NOT on the
   branch for Currency, Diary, hash-checker, or Omni-Notes (tools/ root
   listing + tools_dev/ checked for Omni-Notes). Those four apps'
   verification.csv files are preserved verbatim, not regenerated. The
   parent should locate the generator (or approve an alternative) before
   any of those four can claim fully regenerated logs.
4. **No label was changed by any Stream D leaf** (all DECISIONS.md files
   state this; the only local-mirror text corrections are Vanilla-Music
   readme prose counts, 1158/315 -> 1157/316 and 266 -> 270 sample edges,
   and AnyMemo's none). No tool-coverage contradiction flipped a label
   anywhere in this stream.

## Decisions still owed to the parent (complete list)

1. **AMS/PMS caveat:** accept the partial check (2) results for Currency,
   Diary, hash-checker, openlauncher, and Vanilla-Music as sufficient for
   their status lines, or require an authorized large-file route (e.g. Mac
   clone) to verify the ActivityManagerService (and, for openlauncher,
   PackageManagerService) citation lines first?
2. **Generator location:** where does make_verification.py live for
   Currency, Diary, hash-checker, and Omni-Notes — or is another approved
   tool to regenerate their verification.csv files? Until answered, those
   four files stay preserved verbatim and their status lines stay proposals.
3. **Omni-Notes wrong route:** does the 1 documented wrong route
   (DbHelper.deleteNote, D3) block the "route checks pass" gate, or is it
   accepted as documented in Limits? If a fix is wanted, it needs a new
   editor context (e.g. @MERGE) with its own Back/save chain, not a
   one-edge edit.
4. **Vanilla-Music dual rates + not-run checks:** confirm the D3 reporting
   (0.0 new errors this run; 0.633 logged-convention rate from branch fix
   history) and decide whether check (4) not run + scan --all not run block
   its gate, or whether the carry-over evidence + this run's other passes
   suffice pending a full-tree run.
5. **Markor + AnyMemo:** authorize a route for the large files (Mac clone or
   a connector chunked fetch, if one becomes available) — or accept
   build-blocked status for both apps tonight.
6. **hash-checker / openlauncher status lines:** hash-checker's gate is
   "reached for content" with two named limitations and openlauncher's gate
   is passed except the check (2) cache caveat — does the parent apply
   their proposed status lines now, or hold them with items 1–2?
7. **Minor, merge-time only:** gen_readme_v2.py printed 51/53 lines for
   Currency / Vanilla-Music / openlauncher / hash-checker READMEs, but the
   files on disk measure 93 / 91 / 81 / 85 lines. Re-run gen_readme_v2.py at
   merge and compare; the generation itself exited 0 in each case, so this
   is a counting discrepancy, not a failed log step. (Omni-Notes' README is
   separately reported byte-identical to branch per RUN_LOG.)
8. **Morning-push hygiene:** confirm the redaction in
   `Vanilla-Music/scratch/fetch_batch6.log` (token value replaced with
   REDACTED) and that the pre-existing branch checklist lines in the
   openlauncher AGENT_NOTES mirror stay untouched as branch content.

## Files

- This report:
  [STREAM_D_FINAL_REPORT.md](sandbox://workspace/overnight/stream-D/STREAM_D_FINAL_REPORT.md)
- Run log (with close-out appendix):
  [RUN_LOG.md](sandbox://workspace/overnight/stream-D/RUN_LOG.md)
- Stream decisions:
  [DECISIONS.md](sandbox://workspace/overnight/stream-D/DECISIONS.md)
- Per-app decisions and scratch outputs under
  `~/workspace/overnight/stream-D/<App>/` (Currency, Diary, hash-checker,
  Omni-Notes, openlauncher, Vanilla-Music, Markor, AnyMemo).

No pushes were made. No branch file was edited. No device work was done.
