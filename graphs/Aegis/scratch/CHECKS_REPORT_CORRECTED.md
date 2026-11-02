# Aegis eight-check + drycheck report — STAGING ONLY (§11 gates 7–8)

CORRECTION NOTE (B1 only): This copy corrects exactly one defect
from the independent audit of the original report: the Check 8
supporting-listing description of 8a_scan_all.txt. The original
report is retained as history, unchanged. No check was re-run for
this correction, no gate verdict changes, and no count, route,
label, or graph value other than the 8a listing description
changes. The operative Check 8 gate (8b, 0 of 458) is unaffected.

Role: EIGHT-CHECK + DRYCHECK HELPER. Not the merger, not an auditor,
not a pusher. Nothing was pushed, no branch file was edited, no
merger/tree file was edited in place, no tools/ file in the real tree
was edited, no .github/ file was touched, no out/ file in the real
tree was written, no handoff decision record was written, no
emulator/adb/device run was started, and no CI request was sent.
Scope held: Aegis only. MMEX, AnkiDroid, and LibreTorrent were never
touched. The merger alone decides whether these results enter the
push package, after an independent audit. No push readiness is claimed
here — checks/drycheck results alone do not make a push package (C4
packaging + promotion re-point + re-verification still follow).

## Verdict summary (all eight checks PASS their gates; drycheck NOT YET APPLICABLE)

| Check | Name | Printed result | Gate verdict |
| 1 | Build | 6430 edges, 2995 methods, 2537/458, errors 0, warnings 0 | PASS |
| 2 | Citations | 22 distinct, 0 problems; unbacked 0 | PASS |
| 3 | Guard contradictions | 0 routes flagged | PASS |
| 4 | Bytecode lines | 4273 checked, 345 skipped, 168 implicit, 0 mismatches | PASS |
| 5 | DEAD / FRAMEWORK_ONLY grep | 0 lines | PASS |
| 6 | FW-MEMORY grep | 0 lines | PASS |
| 7 | PENDING grep | 0 lines | PASS |
| 8 | UNREACHABLE with bytecode caller | 0 of 458 | PASS |
| Drycheck | Device dry run (D9) | NOT YET APPLICABLE (see Drycheck section) | N/A, not a pass |

STOP conditions hit: NONE. No check failed its gate, so no apply-stop
arises from this suite.

## Staging paths

- This step's root: `~/workspace/finish/work/Aegis/turn/checks/`
- This report: `~/workspace/finish/work/Aegis/turn/checks/CHECKS_REPORT.md`
- Staging work root (all commands run from here):
  `~/workspace/finish/work/Aegis/turn/checks/work/`
- Staging tools (copies, verified by cmp — see below):
  `work/tools/` (build_graph.py, check_citations.py,
  check_bytecode_lines.py, check_routes.py, scan_unreachable.py,
  show_route.py, plus tests/check_v2.py for the supplementary run)
- Staging graph inputs (copies, verified by cmp):
  `work/graphs/Aegis/` (graph_def.py, method_list.json,
  auto_calls.json, coverage_baseline.json, verification.csv) and
  `work/graphs/Aegis/out/` (aegis_trigger_graph.json, methods.csv,
  build_report.txt, sanity_check.csv — the apply-v3 after-build
  outputs, before the check-1 rebuild overwrote out/)
- Staging source corpora (read-only symlinks mirroring the tree
  layout, not copies): `work/final_java_only` and `work/fw_src`,
  pointing at the merger tree's symlinked corpora
- Raw check outputs: `work/raw/` (1_build.txt, 2_citations.txt,
  3_routes.txt, 4_bytecode.txt, 5_7_greps.txt, 8a_scan_all.txt,
  8b_scan_callers.txt, check2_ranges.txt, check4_breakdown.txt,
  checkv2_supplementary.txt, plus pre-rebuild out/ copies
  aegis_trigger_graph.json, methods.csv, build_report.txt)
- Fresh graph inputs (read-only sources):
  `~/workspace/finish/work/Aegis/turn/apply-v3/work/after/` (6430-edge
  build) and `~/workspace/finish/work/Aegis/turn/redraw/work/`
  (sampler 25/1093/446; its out/ files are md5-identical to the
  apply-v3 after out/ files)
- Regenerated verification.csv (read-only for this step, copied
  into staging, NOT edited):
  `~/workspace/finish/work/Aegis/turn/writer/work/graphs/Aegis/verification.csv`
  (263,972 bytes, 535 lines; SHA-256
  83c527cad5a03ec8c5e002e2b5177ceee79572e0ec8885133635139cb4074321,
  matching the writer audit; re-verified unchanged after this run)

## Copy integrity (verified before running anything)

Every staged copy was verified with cmp against its source before
any check ran; no copy truncated:

- Tools: build_graph.py, check_citations.py, check_bytecode_lines.py,
  check_routes.py, scan_unreachable.py, show_route.py, tests/check_v2.py
  — all cmp-clean against the merger tree tools.
- Graph inputs: graph_def.py (641,477 bytes — the modified file with
  the appended V2 + V3 blocks, not the 637,506-byte baseline file),
  method_list.json, auto_calls.json, coverage_baseline.json — all
  cmp-clean against the apply-v3 after staging copy.
- Build outputs (pre-rebuild): aegis_trigger_graph.json (5,701,550
  bytes), methods.csv (5,468,224 bytes), build_report.txt (3,338 bytes),
  sanity_check.csv (161,090 bytes) — all cmp-clean.
- verification.csv: 263,972 bytes, cmp-clean against the writer output.
- Every check output file was re-read after its run and confirmed
  non-empty with its expected content; no result below rests on an
  exit code alone.

## Eight-check inventory (name / command / inputs / gate)

Commands are as run from the staging root
(`turn/checks/work/`), mirroring `handoff/ci/rebuild.sh` (which
writes `1_build.txt` through `8b_scan_callers.txt` and SUMMARY.txt).
That script is the suite definition used here; the previous Aegis
check logs (`merger/scratch/check2_*.txt`, `check3_*.txt`,
`check4_*.txt`, `check8_*.txt`) confirm the check 2/3/4/8 commands
and naming. Gates are the project F1 gates from
`handoff/MUSE_FINISH_ALL.md` (checks 2/4 = 0, check 3 explained,
checks 5–7 = 0, check 8 all explained) plus each tool's own
definition for check 1.

| # | Name | Command (from staging root) | Inputs (staging) | Gate |
| 1 | Build | `python3 -I tools/build_graph.py graphs/Aegis aegis` | graphs/Aegis/graph_def.py, method_list.json, auto_calls.json, coverage_baseline.json, verification.csv (audit-log input) | errors 0, warnings 0 (tool's own report lines); counts reported |
| 2 | Citations | `python3 -I tools/check_citations.py Aegis` | graphs/Aegis/out/aegis_trigger_graph.json; fw_src caches | 0 problems; FW-MEMORY / DYN / UNVERIFIED count 0 |
| 3 | Guard contradictions | `python3 -I tools/check_routes.py Aegis` | trigger graph + graphs/Aegis/out/methods.csv | 0 flagged, or each flagged route explained |
| 4 | Bytecode lines | `python3 -I tools/check_bytecode_lines.py Aegis` | trigger graph + final_java_only sources (flavor-aware, via show_route.py) | 0 where the cited line does not show the callee |
| 5 | DEAD / FRAMEWORK_ONLY grep | `grep -c 'DEAD\|FRAMEWORK_ONLY' graphs/Aegis/graph_def.py` | graphs/Aegis/graph_def.py | 0 (or hits explained in Limits for ticked apps; none needed — count is 0) |
| 6 | FW-MEMORY grep | `grep -c 'FW-MEMORY' graphs/Aegis/graph_def.py` | graphs/Aegis/graph_def.py | 0 |
| 7 | PENDING grep | `grep -c 'PENDING' graphs/Aegis/graph_def.py` | graphs/Aegis/graph_def.py | 0 |
| 8 | UNREACHABLE with bytecode caller | `python3 -I tools/scan_unreachable.py Aegis --callers` (plus `--all` as supporting listing) | trigger graph + graphs/Aegis/auto_calls.json (+ final_java_only for the --all listing) | every flagged method's caller explained; here 0 flagged, so nothing to explain |

Supplementary, NOT one of the eight: `python3 -I
tools/tests/check_v2.py Aegis` (schema-2 equivalence test). One
AGENT_NOTES entry labels it "checks 5–7", but rebuild.sh and
MUSE_FINISH_ALL define checks 5–7 as the three greps above, so the
greps are reported as checks 5–7 and check_v2 is reported separately
below to close the ambiguity rather than silently picking a reading.

STRICT line (SUMMARY line, not a numbered check):
`grep -c '^STRICT = True' graphs/Aegis/graph_def.py` = 1.

## Results by check

### Check 1 — Build: PASS

Raw output: `work/raw/1_build.txt` (3,338 bytes, re-read in full).
Exit 0. methods 2995, pages 12, edges 6430. Verdicts REACHABLE 2537 /
UNREACHABLE 458. Unreachable by kind: branch_never_taken 1,
framework_never_calls 31, no_trigger_in_app 426. Edge kinds: CALL
5344 (predicted 5344), ENTERS 23, GUI 55, RESULT 26, others as
printed. Auto edges 4935 of 6430 (predicted 4935). Evidence: FW-SRC
261, INFERRED 832, SRC 5337. Edges with a claim that cites no source
line: 897 of 6430 (carried V2-after count, see the I5 note below).
needs_state edges 113; env edges 55; methods with ENV 198, with
STATE 2114. Labels confirmed by: INFERRED 2719, SOURCE 276. Path
status: SOURCE_OK 2, UNCHECKED 2534, WRONG 1. Build-report
verification section (audit-log counts against the regenerated
verification.csv; "checked" = correct + fixed + wrong, unclear
excluded by the tool's own definition): label checked 472, errors
found 1, unclear 11; edge checked 26, errors 0, unclear 0; path
checked 14, errors found 1, unclear 11. Sanity check: 751 methods
ran, 0 UNREACHABLE but ran (contradictions), 18 ENV-gated but ran
(listed in the raw file; tool coverage only, never used to set a
label). errors: 0. warnings: 0. Gate verdict: PASS.

Reproduction note (stated, not smoothed over): the staging rebuild
does NOT reproduce the apply-v3 out/ files byte-identically, for a
single explained reason — the staging build's verification.csv input
is the REGENERATED file (263,972 bytes), while the apply-v3 build's
input was the pre-fix file (258,143 bytes), and build_graph.py folds
verification.csv into label metadata and the build-report verification
section. Proven by direct comparison (rebuilt out/ vs the preserved
pre-rebuild copies in `work/raw/`): edge id sets equal (6430/6430)
with ZERO differing edge records; route_edge_ids, verdicts, steps,
ENV kinds, and STATE kinds differ for ZERO methods; unreachable sets
equal (458/458) with identical kind/reason texts. The ONLY
differences are three verification-metadata fields, each explained by
the regenerated file: RawSlot.getType path_status WRONG → UNCHECKED
(its path row is now UNCLEAR, and unclear rows map to UNCHECKED);
AuthActivity.lambda$onCreate$3 path_status UNCHECKED → WRONG (its new
path row is WRONG); EditEntryActivity$CustomSvgIcon.<init> source_ref
manifest text → ui/EditEntryActivity.java:151-152 (it has no label
row in the new file, so source_ref falls back to its last route
edge's evidence ref). No graph, route, verdict, or label difference
hides behind the byte difference. Checks 2/3/4/8 read edges, routes,
guards, and unreachable sets — none of which differs — so they are
unaffected by the metadata delta.

### Check 2 — Citations: PASS (tool 0 problems + operative SRC re-print)

Raw output: `work/raw/2_citations.txt` (118 bytes, re-read):
`citations: 22 distinct, 0 problems; library citations (not
checked): 0; evidence with FW-MEMORY / DYN / UNVERIFIED: 0`.
Tool exit 0. Gate verdict: PASS on the tool's own terms.

Operative SRC check (the tool validates FW-SRC citations, not SRC
app citations, so the print-every-cited-range step is the operative
check for the new SRC edges, per the design §10): every cited range
for I1–I8, L1–L3, P1, and P2 was re-printed from source in this run
and saved in full to `work/raw/check2_ranges.txt` (5,704 bytes,
re-read). All ranges printed as claimed; key lines:

- I1 (E0237a72b) `SRC ui/IntroActivity.java:57-62`: the imported
  branch — `getBoolean("imported")` → `skipToSlide(DoneSlide.class)`.
- I2 (Edb4753c5) `SRC ui/intro/IntroBaseActivity.java:104` (the
  skipToSlide definition) + `SRC ui/IntroActivity.java:57-62`.
- I3 (Ec3048aa3) `FW-SRC core/java/android/view/View.java:6289-6296`
  (performClick → OnClickListener.onClick) + `SRC
  ui/intro/IntroBaseActivity.java:47` (Next → goToNextSlide) and
  `80-93` (last slide → onDonePressed).
- I4 (Ed92e13fe) `SRC ui/IntroActivity.java:106-123`: readVaultFile
  + loadFrom(vaultFile, creds) with error-dialog returns.
- I5 (E3cd165ef) `SRC ui/IntroActivity.java:125-129` (setIntroDone,
  setResult(RESULT_OK), finish) + `FW-SRC
  core/java/android/app/ActivityThread.java:4253-4265`
  (deliverResults → dispatchActivityResult) + `FW-SRC
  core/java/android/app/Activity.java:5526-5527` (finish) + the
  INFERRED androidx.activity.result segment (no source line — see
  the I5 note below).
- I6 (Eef8a8cb9) `SRC ui/MainActivity.java:142-148`: RESULT_OK →
  onIntroResult().
- I7 (Ecc2a9f7f) `SRC ui/MainActivity.java:752-754`: onIntroResult
  → loadEntries().
- I8 (E53167466) `SRC ui/MainActivity.java:1133-1144` (loadEntries,
  `_loaded` false branch) + `SRC vault/VaultManager.java:231-233`
  (getVault throws when none is loaded).
- L1 (E2a08d921) `FW-SRC core/java/android/view/View.java:6289-6296`
  + `SRC ui/MainActivity.java:570-597` (OK handler: group-required
  errors and returns, entry group assignment, save at :594). The
  FW-SRC segment is byte-identical to the plain edge E5cd3d480's
  FW-SRC segment (verified from the trigger graph: both edges carry
  the identical `View.java:6289-6296 (performClick calls the
  OnClickListener.onClick)` text and the identical SRC 570-597
  segment) — the mirroring claimed in the task holds exactly.
- L2 (E834df9cf) `SRC ui/MainActivity.java:594`: `saveAndBackupVault();`.
- L3 (Ebb585c74) `SRC ui/MainActivity.java:1370-1371` (override
  calls super) + `SRC ui/AegisActivity.java:139-141` (superclass
  save calls VaultManager.saveAndBackup).
- P1 (Ed3fd969c) `SRC MainActivity.java:594 (bytecode)`: short file
  form, resolving by basename to ui/MainActivity.java:594, which
  prints `saveAndBackupVault();` — the exact line claimed.
- P2 (E30bbb737) `SRC MainActivity.java:1371 (bytecode)`: short file
  form, resolving to ui/MainActivity.java:1371, which prints
  `boolean res = super.saveAndBackupVault();` — the exact line
  claimed. The short form is NOT a typo to fix into the ui/ form:
  fixing it would break id preservation (design §1.2).

No cited range failed to print as claimed. No range was substituted.
Check-2 verdict including the operative re-print: PASS.

### Check 3 — Guard contradictions: PASS, none found

Raw output: `work/raw/3_routes.txt` (26 bytes, re-read):
`# Aegis: 0 routes flagged`. Tool exit 0. Gate verdict: PASS — no
flagged route exists, so no explanation is owed.

New-edge guard audit (extra evidence, not a substitute for the
tool): the trigger/guard/env/evidence text of all 13 new edges
(I1–I8, L1–L3, P1, P2) was grepped for the forbidden gratuitous
texts RESULT_CANCELED, "Cancel tapped", "histMap == null", and
"network off" — zero hits on every edge. The @IMP route contains
exactly one RESULT_OK leg (I5) with no earlier RESULT_CANCELED leg
on the route (the tool's 0-flagged result across all 2537 REACHABLE
routes is consistent with this). P1/P2 carry no guard at all, so
they add no check-3 surface.

### Check 4 — Bytecode lines: PASS, 0 mismatches (P1/P2/auto-copy breakdown below)

Raw output: `work/raw/4_bytecode.txt` (171 bytes, re-read):
`Aegis: 4273 bytecode-cited edges checked, 345 skipped (lambda /
clinit / anonymous), 168 implicit (super / enum / Dagger), 0 where
the cited line does not show the callee`. Tool exit 0. Gate
verdict: PASS.

Breakdown (derived with the tool's own callee_token + line-search
logic from show_route/check_bytecode_lines, saved in full to
`work/raw/check4_breakdown.txt`, 4,576 bytes, re-read; the headline
0-mismatch result above is the tool's own, this breakdown only
splits it):

- P1 (Ed3fd969c, hand, no auto flag):
  MainActivity.lambda$startAssignGroupsDialog$15 →
  MainActivity.saveAndBackupVault, cited `SRC MainActivity.java:594
  (bytecode)` — CHECKED and PASS: line 594 contains
  `saveAndBackupVault();` (callee token saveAndBackupVault, no @
  to strip). P1 newly enters check 4 by its (bytecode) token, as
  predicted, and passes.
- P2 (E30bbb737, hand, no auto flag):
  MainActivity.saveAndBackupVault →
  AegisActivity.saveAndBackupVault, cited `SRC MainActivity.java:1371
  (bytecode)` — CHECKED and PASS: line 1371 contains
  `super.saveAndBackupVault();`. P2 newly enters check 4 and passes.
- Auto copies (33, computed as the added auto edges versus the
  apply-v3 before build — exactly the design §5.5 inventory):
  ALL 33 CHECKED and PASS on the cited line itself (no near-line
  fallback needed). By source: loadEntries@IMP 10, onDonePressed@IMP
  + onDonePressed@SAVED@IMP 12, assign-lambda@IMP 9,
  skipToSlide@IMP 1, saveAndBackupVault@IMP 1. The full 33-edge list
  with cited file/line and outcome is in
  `work/raw/check4_breakdown.txt`; the save@IMP copy is Eceae5176
  (→ updateErrorCard, MainActivity.java:1372). The
  callee_token-strips-@ explanation was NOT relied on: the outcome
  above is the actual per-edge result, and it is pass for all 33.
- No check-4 failure names any edge, because there is no failure.
  In particular no failure names P1, P2, or any auto copy.

Note on the count movement: 4273 checked here versus 4241 in the
post-vault DOCS_PLAN figure and 4193/3946 in earlier AGENT_NOTES
entries — the count moves with the graph (P1/P2 + the 33 auto copies
add bytecode-cited edges); the gate is the mismatch count (0), not
the checked count.

### Check 5 — DEAD / FRAMEWORK_ONLY grep: PASS

Raw output: `work/raw/5_7_greps.txt` (re-read):
`DEAD|FRAMEWORK_ONLY lines: 0`. Gate verdict: PASS. (For a schema-2
converted graph this is expected: DEAD/FRAMEWORK_ONLY containers
were converted to UNREACHABLE entries.)

### Check 6 — FW-MEMORY grep: PASS

Raw output, same file: `FW-MEMORY lines: 0`. Gate verdict: PASS.

### Check 7 — PENDING grep: PASS

Raw output, same file: `PENDING lines: 0`. Gate verdict: PASS.

STRICT line (not a numbered check, reported for the SUMMARY):
`STRICT = True line in graph_def.py: 1`.

### Check 8 — UNREACHABLE with bytecode caller: PASS, none flagged

Raw outputs: `work/raw/8b_scan_callers.txt` (68 bytes, re-read):
`0 of 458 unreachable methods have a bytecode caller outside the
set`. Tool exit 0. Supporting listing `work/raw/8a_scan_all.txt`
(86,534 bytes, first-level entries counted in full for this
correction): 8a (--all) shows all 458 unreachable methods: 191
with other (non-caller) name mentions, 267 with no other mention
at all. Note: the tool's summary line reads "458 methods with
other mentions shown; 0 with no other mention", but that 0 is a
flag artefact, not a count — in scan_unreachable.py the quiet list
is only appended when '--all' is NOT passed, so with '--all' every
method is forced into "shown" and the summary's 0 is 0 by
construction. Gate verdict: PASS —
zero flagged items, so the item list is empty and no caller
explanation is owed.

Supporting facts (verified, not assumed): no UNREACHABLE method was
touched — the unreachable sets are identical between the before and
after builds (458/458) with identical kind/reason texts; no method
was added or removed (2995 methods, same set); every @IMP node's
base maps to an existing REACHABLE method or page (the build's 0
label flips + the unchanged verdict columns); the deleted edge's
destination (saveAndBackupVault@RAW) is a variant node, not a method;
the four methods it fed stay REACHABLE with the new prefix (apply
gates 1–4, confirmed by the check-1 rebuild's identical verdicts).

### Supplementary — check_v2 (schema-2 equivalence, NOT one of the eight)

Raw output: `work/raw/checkv2_supplementary.txt` (re-read):
`Aegis converted to schema 2 (graph_def.py has UNREACHABLE): the old
tool cannot build it, skipped` / `apps with problems: 0`. This
matches the previous `checkv2_v3.txt` exactly. It is reported here
only to close the AGENT_NOTES "checks 5–7 (check_v2)" wording
ambiguity: under either reading — greps 0/0/0, or check_v2 skip with
0 problems — the checks 5–7 outcome is clean.

### The I5 no-source-line edge (E3cd165ef) — flagged by NO check

The build statistic "edges with a claim that cites no source line"
is 897 in this staging build (carried from V2-after: 896 → 897 via
exactly the I5 RESULT edge, whose evidence inherits the FW_LAUNCHER
constant's INFERRED segment, mirroring the plain RESULT edge
E743b6812 verbatim — both edges carry the identical FW-SRC segments
plus the identical INFERRED androidx.activity.result segment, verified
from the trigger graph). Judgment by check:

- Check 2 does NOT flag it: the tool's unbacked regex matches
  FW-MEMORY / DYN / UNVERIFIED only, and I5's segment is INFERRED, so
  the unbacked count stays 0. The 897 figure is a build-report
  statistic, not a check-2 problem.
- Check 4 does NOT flag it: I5's evidence carries no (bytecode)
  token, so the tool does not examine it.
- Check 3 does NOT flag it: 0 routes flagged overall, and I5's route
  has no RESULT_CANCELED leg before it.
- Checks 5–7 do NOT flag it: I5 is a built edge, not a graph_def.py
  text hit (0/0/0).
- Check 8 does NOT flag it: I5's destination is a variant node, not
  an UNREACHABLE method.

So the I5 edge stands as the design states it: carried at 897, judged
by no check as a failure, neither excused nor claimed as passing a
check that does not examine it. If a later gate judges the I5
evidence a failure, that judgment would come from outside this suite
as run here, and per §11 gate 8 it would stop the apply — nothing in
this report pre-decides that question.

### Writer-audit path-note traces — NOT check failures

The writer audit's non-blocking note N2 records two path notes
containing `turn/` evidence traces, but only inside verbatim table
Decisive text (RawSlot: turn/redraw/REJUDGE.md and
turn/audit/redraw-reaudit/AUDIT.md; Auth:
turn/judge-auth/JUDGE_AUTH.md and turn/audit/judge-auth/AUDIT.md).
No check tool flagged them in this run (check 2: 0 problems; no
other check examines note text), so per the task they are NOT
treated as check failures. This is a C4 docs decision, not a check
result, and it is recorded here as such, not resolved.

## Drycheck — definition and result: NOT YET APPLICABLE

Definition (from the shared device harness, D7_PLAN §2.2–§2.3, and
the finish brief's dry-run mode — NOT from any graph-stage tool):
the device drycheck is the D9 dry run, `bash device/run_app.sh
<App> <glob> <outdir> --dry-run`, which runs `drycheck.py
--load-scripts` with NO adb at all. For every ROUTES.csv row it
checks: every edge id exists in the CURRENT trigger graph; the
edges form a contiguous chain from S_ENTRY to the method node; the
method exists in methods.csv; permissions are declared in the
manifest; committed fixtures exist and generated fixtures are
declared via the current `gen:` mechanism; and every scripted
script loads in dry mode under the harness. Unscriptable rows need
only a non-empty reason. A dry run passes ONLY when EVERY scripted
route shows PASS in dryrun_report.txt. It is a device-layer check,
not a graph check: dry mode skips node resolution, so it does not
cover launch-component correctness, and it is not a real emulator
run.

There is NO graph-stage drycheck tool: a search of the tree tools
for a drycheck/dry-run facility finds only an unrelated "dry run:
not pushed" message in publish_graphs.py (a publish guard, not a
check). No graph-stage drycheck is claimed, run, or implied here,
and no emulator/adb/device step was run under the name drycheck.

Result: NOT YET APPLICABLE, for this reason: the device drycheck
requires a final ROUTES.csv plus one route script per scripted route
(D1/D3/D7), built from the FINAL sample only, after C4. Those
artifacts do not exist for the new sample yet:

- `turn/device/` holds only a DRAFT: ROUTES_DRAFT.csv (pre-fix,
  explicitly "must never be renamed into place as ROUTES.csv"
  because its edge lists are deliberately absent and its pre-fix
  rows are stale by design), D1_NOTES.md (draft scriptability
  assessment on the pre-fix sample), and D7_PLAN.md (draft plan).
  No route_NN.py script exists there, and no final ROUTES.csv
  exists for Aegis anywhere in staging or in the merger tree's
  graphs/Aegis/ directory (which holds no device/ directory).
- The final sample itself only settled in this turn (25/1093/446,
  Auth in, CustomSvgIcon out, RawSlot on the 42-step @IMP route),
  and D1/D3/D7 are defined to come from that final sample after C4
  (writer promotion conditions P1–P6 put checks/drycheck as separate
  steps, and the device lead owns D1/D3/D7 implementation).

What would make drycheck applicable: a final ROUTES.csv with the 25
new-sample rows (edge lists from the regenerated verification.csv
path rows), one route_NN.py per scripted route, per-route setup
scripts/fixtures as applicable, and unscriptable reasons for the
rest — then `run_app.sh Aegis --dry-run` via the coordinator, which
is the only route by which a dry run is requested. Until then, any
claim of a drycheck pass for Aegis would be false, and none is made.

## STOP conditions hit

NONE. No check failed its gate; no staging copy truncated (all
cmp-verified); no cited range failed to print; neither P1 nor P2 id
differed from its required id; the check-1 rebuild reproduced the
graph exactly (edge records 0 differences, routes 0 differences —
the 3 metadata-field differences are explained above and are not a
STOP); the drycheck non-applicability is a pending-input state, not
a failure. No fifth route changed, no label flipped, no tool crashed.

## NOT done (explicitly out of scope here)

No merger, no independent audit of this output, no C4 packaging, no
promotion re-point, no re-verification in branch layout, no device
scripts, no ROUTES.csv, no dry-run request, no push, and no push
readiness is claimed or implied. The merger must still obtain an
independent audit of these check results before any merge, and the
C4 packaging step must still re-point TABLE_FILE, re-run the writer
in branch layout, and re-verify byte-identity (writer audit
conditions P1–P6) before any push package exists.
