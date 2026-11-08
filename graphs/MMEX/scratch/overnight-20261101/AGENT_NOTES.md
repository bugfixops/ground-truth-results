# MMEX — Stream B overnight mirror AGENT_NOTES (LOCAL ONLY, never branch files)

## Current step
- 2026-11-01 ~02:30 EST: awaiting branch fetch loop (tools + 47 parts + small files).
  Next command after loop: assemble parts, check method_list/auto_calls fetch results,
  then attempt build (full if inputs complete, else PARTIAL with header reconstructed
  and clearly labelled, or stop that step with the blocker named).
- Branch (input only, NOT re-verified): graphs/MMEX/graph_def.py 1348082 bytes,
  method_list.json 913821, auto_calls.json 2559591, parts 147 label_*.py (1336741 bytes
  total), out/methods.csv 3279801, out/mmex_trigger_graph.json 6471377.
- Handover counts (input only, NOT re-verified): 4270 methods, 3430 REACHABLE /
  840 UNREACHABLE. Do not copy as verified.

## Rules applied this session
- GitHub connector only for branch reads; no token anywhere; one file at a time,
  ~30 s pauses; on a fresh 429 stop that fetch attempt (no retry loop).
- Parts accepted only if connector-fetched this session or git-blob-SHA-verified
  against the connector parts listing (100 parts verified that way so far).
- confirmed_by only SOURCE or INFERRED. Never DYN, FW-MEMORY, UNVERIFIED as a
  confirmed_by. No tool coverage, old generated graphs, or build counts as evidence.
- No pushes. No device checks tonight. Standard configuration: debug build, fresh
  install, API 27, runtime permissions only where a route needs them.

## Blocked (so far)
- graphs/MMEX/graph_def.py: connector refuses display above ~1 MB (1348082 bytes).
  Workaround in progress: assemble from parts/ (see DECISIONS.md D-MMEX-6).
- graph_def header (~11341 bytes by size difference: TITLE/STRICT/USE_AUTO/SUPPRESS/
  CLASSIFY/EDIT/helpers) is in NO part file found so far. Not invented.
- auto_calls.json (2559591 bytes): connector display expected to refuse; USE_AUTO is
  confirmed by part comments, so a faithful build needs it. Fetch test pending in loop.

## Partial build plan (mirror only)
- Header reconstructed in scratch/partial_header.py (helpers only; CLASSIFY
  HAND_CLASS table missing — deviation bounded after assembly; EDIT assumed None;
  PREFER_SETUP_OVER_ENV assumed default False; USE_AUTO=False forced by missing
  auto_calls.json). Partial build runs in a separate scratch dir, never in
  graphs/MMEX/out/ (which holds the branch build_report.txt reference).

## Current step (2026-11-01 ~03:25 EST): GATE BLOCKED, work saved locally only
- Next (morning, needs authorized route for large files): fetch auto_calls.json
  (2559591 B) + graph_def.py header (~6.7 KB: S_ENTRY screen, 5 ENTRY edges,
  helpers, CLASSIFY rule, EDIT rule) via Mac clone or chunked fetch; rebuild
  (expect 0/0/0 per branch build_report); draw sample 30 seed 20261025; print +
  judge 30 routes; apply proposed fixes A-D (helper2 texts), ScreenTree scope
  (4 dispatch edges), p085 part re-sync, label_144 rewording; re-draw sample;
  run all 8 checks; generate verification.csv via make_verification.py; run
  gen_readme_v2.py; then — and only then — the [K] line becomes claimable.
- Do NOT quote partial-build numbers (193 reachable, 3308 errors) as branch
  results, and do NOT quote the 36-item input-only tally (34 correct / 1 wrong
  edge / 1 unclear) as a sample error rate. Sample error rate: NOT COMPUTED.
