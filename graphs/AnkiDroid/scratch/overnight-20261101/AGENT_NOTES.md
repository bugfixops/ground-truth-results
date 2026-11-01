# AnkiDroid — stream-B leaf notes (local mirror only, NO PUSHES)

Branch: work-2026-10-31, repo bugfixops/ground-truth-results, head
614a9540d5c72ab1406316cb6f05120493ffcfbe (from branch directory listings).
Standard configuration: debug build, fresh install, API 27, runtime
permissions granted only where a route needs them. No device checks tonight
(no emulator, adb, APKs, new repos, GitHub Actions runs). No other app touched.

## Current step

BLOCKED at reconstruction. Branch-verified inputs are in place; the branch
graph itself could not be reconstructed, so the build, sampler, eight checks,
and verification.csv could not run. See STEP_LOG.md for the timed record and
DECISIONS.md for the decisions made tonight.

## What was verified against the branch (connector, spaced single fetches)

- graphs/AnkiDroid/ contents: AGENT_NOTES.md (61,538), auto_calls.json
  (2,543,896), coverage_baseline.json (735,617),
  generated_draft_graph_def.py.txt (5,074), graph_def.py (1,173,446, SHA
  5c07052392aa03603867e1628611df4df471c0c5), method_list.json (779,471, SHA
  79a5122243cfe2a565557a969b0245cc8083ab1a), out/, parts/ (302 files),
  review_notes.md (2,933), scratch/ (474 entries). No verification.csv,
  no readme_notes.md, no LESSONS.md, no make_verification.py in
  graphs/AnkiDroid/ on the branch.
- tools/ on the branch: build_graph.py 38,050, verify_sample.py 2,373,
  check_citations.py 4,680, check_routes.py 2,747, scan_unreachable.py
  5,716, gen_readme_v2.py 9,223, check_bytecode_lines.py 5,020,
  show_route.py 5,314 — local tool copies match these sizes exactly.
- out/ on the branch: README.md (13,922), ankidroid_trigger_graph.html
  (5,863,289), ankidroid_trigger_graph.json (6,631,016), build_report.txt
  (10,812), methods.csv (2,805,329), sanity_check.csv (196,356).
- out/build_report.txt fetched in full: git blob SHA
  4d2ced440cbf57ba2beb9d90722b645c700af6d5, identical to both local copies.
  Its printed counts (branch build 205, NOT a run by this leaf): methods
  4186, pages 43, edges 9178, REACHABLE 3275, UNREACHABLE 911 (by kind:
  branch_never_taken 48, closed_by_api_level 44, closed_by_configuration 22,
  framework_never_calls 48, no_trigger_in_app 749), errors 0, warnings 0,
  path status UNCHECKED 3275, labels SOURCE 3945 / INFERRED 241, edge classes
  explicit 8164 / non_standard 26 / page 56 / standard 932, auto edges 8146
  of 9178, sanity: 1 UNREACHABLE but ran (Card.toString), 180 ENV-gated but
  ran (sanity output only, never label evidence).
- scratch/conflicts.md fetched in full: git blob SHA
  4079a138fe09941b10c76938371d990329e78af6, identical to the local copy.
  Open items current on the branch: Card.toString contradiction OPEN,
  EasySSLSocketFactory equals/hashCode OPEN; LoadPronounciationActivity
  kind settled (INTENT route, not FRAMEWORK).
- scratch/head.py.txt fetched (header only, 10,484 bytes): TITLE, USE_AUTO,
  STRICT = False in the header text, helper functions, SCREENS table start.
  scratch/orch_merge.py fetched (975 bytes): incremental append of one part
  plus build — not a full-assembly script.

## What could NOT be fetched (the blocker)

- graph_def.py: connector returns "too large to display (1173446 bytes)"
  with no content block, only a download link. The link was NOT used: it
  carries a token, and this task forbids tokens in URLs, files, or messages.
- auto_calls.json (2,543,896), out/methods.csv (2,805,329),
  out/ankidroid_trigger_graph.json (6,631,016): same size class, same
  failure mode (not re-attempted after the graph_def failure, by the same
  reasoning; methods.csv was already reported too large in prior WP2 work).
- Parts assembly assessed and rejected: parts/*.py total 1,056,495 bytes,
  but sup blocks for most parts and several orchestrator addenda exist only
  inside graph_def.py, and auto_calls.json supplies 8,146 of 9,178 edges.
  Fetching all 151 part files (spaced) would still not reproduce the branch
  graph or its build counts, so it was not attempted as an exact rebuild.

## Own runs (printed output in scratch/attempted_runs.txt)

- python3 -I tools/build_graph.py graphs/AnkiDroid ankidroid:
  FileNotFoundError graphs/AnkiDroid/graph_def.py, exit 1. NOT RUN.
- python3 -I tools/verify_sample.py AnkiDroid 30 20261025:
  FileNotFoundError graphs/AnkiDroid/out/methods.csv, exit 1. NOT RUN.
  No sample, no error rate. Error rate is NOT computed.
- python3 -I tools/check_citations.py AnkiDroid, check_routes.py,
  scan_unreachable.py --all: IndexError, no out/*_trigger_graph.json.
  NOT RUN.
- python3 -I tools/check_bytecode_lines.py AnkiDroid: ModuleNotFoundError
  show_route (sibling tool not in the local set); in any case the trigger
  graph JSON is missing. NOT RUN.
- python3 -I tools/gen_readme_v2.py AnkiDroid: IndexError, no trigger
  graph JSON. NOT RUN. readme_notes here is a DRAFT only.
- Greps for DEAD / FRAMEWORK_ONLY, FW-MEMORY, PENDING on graph_def.py:
  NOT RUN — the file is absent locally (see graphs/AnkiDroid/
  graph_def.MISSING.txt). No grep count is claimed.

## Source judging done tonight (from printed local source copies)

- Card.toString: label stays UNREACHABLE; contradiction stays open
  (DECISIONS.md decision C). Inner-Card sites re-checked and excluded.
- EasySSLSocketFactory.equals / hashCode: labels stand as INFERRED
  UNREACHABLE tonight; outside HttpClient read authorised as a
  pre-merge verification step (decision A).
- Hooks.runFilter -> AdvancedStatistics.runFilter: registry-dispatch edge
  mechanism correct; MG943 STATE settings gate proposed, not merged;
  full launcher route unclear (decision D).
- Compat / API 27: device-API rule confirmed for app code; framework
  targetSdk surface named as a pre-tick check, no method named (decision B).
- Prior WP2 material (route_check_part1, part 2 draft, parts routes for
  label_134-137, card hunt, easyssl/api27, hooks route reports) was treated
  as INPUT ONLY and re-derived where this note claims a verdict; nothing
  was copied as a verified result.

## Next command (for the agent with a full checkout)

1. Obtain a full checkout of work-2026-10-31 by a method that does not use
   a token in a URL (coordinator to agree the method; this leaf used the
   connector only).
2. Run python3 -I tools/build_graph.py graphs/AnkiDroid ankidroid and
   confirm the printed counts match branch build 205 (4186 / 3275 / 911 /
   errors 0 / warnings 0) before trusting the checkout.
3. Run python3 -I tools/verify_sample.py AnkiDroid 30 20261025, print every
   step of all 30 routes, judge each, fix wrong routes from printed source,
   redraw the final sample, then run the eight checks and write
   verification.csv only via make_verification.py (to be written for
   AnkiDroid; none exists on the branch).
4. Apply DECISIONS.md decisions A-D at merge time (gate attachment for
   MG943, HttpClient read for EasySSL, targetSdk pre-tick grep, Card
   Object-parameter grep) and record the printed lines in scratch/.
5. Only then finalise readme_notes.md via gen_readme_v2.py, LESSONS.md,
   and the proposed status line for the coordinator.

## Files in this local mirror (none pushed)

- graphs/AnkiDroid/method_list.json (branch-SHA-verified, 4186 entries)
- graphs/AnkiDroid/graph_def.MISSING.txt (blocker notice, not a graph)
- graphs/AnkiDroid/out/ (empty; branch out/ files not fetched)
- tools/ (build_graph, verify_sample, check_citations, check_routes,
  scan_unreachable, gen_readme_v2, check_bytecode_lines — sizes match branch)
- scratch/branch_build_report_205.txt (branch output, SHA-verified, not
  this leaf's run), scratch/attempted_runs.txt, scratch/src_*.java
  (printed-source copies used for judging), scratch/route_print_template.py
- DECISIONS.md, STEP_LOG.md, AGENT_NOTES.md (this file), LESSONS.md,
  readme_notes_DRAFT.md, route_judging_note.md
