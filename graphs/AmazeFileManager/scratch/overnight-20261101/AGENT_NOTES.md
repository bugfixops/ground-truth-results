# AmazeFileManager — AGENT_NOTES (local mirror, stream B overnight)

Current step: BLOCKED at reconstruction — gate NOT reached (see Blocked).
No push made, no branch file touched. Next command (on a full checkout
arranged by the parent): print current graph_def.py lines for every item
in scratch/proposals_streamB_UNVERIFIED.py, apply after confirmation,
rebuild, re-print routes, draw the sample, run all eight checks, author
make_verification.py, then generate verification.csv and out/README.md.

## What was verified tonight (2026-11-01, connector, branch work-2026-10-31)
- tools/ listing: build_graph.py 38050 bytes (local copy hash-matches
  branch blob SHA), verify_sample.py 2373, show_route.py 5314 (sizes
  match; hashes not verified), check_citations.py 4680,
  check_routes.py 2747, check_bytecode_lines.py 5020,
  scan_unreachable.py 5716, gen_readme_v2.py 9223 (not fetched).
- graphs/AmazeFileManager/ listing: graph_def.py 1058622,
  auto_calls.json 1839161, method_list.json 673134; out/ contains
  build_report.txt 3881, methods.csv 1179770, sanity_check.csv 143900.
- out/build_report.txt fetched: 2981 methods, 2509 REACHABLE / 472
  UNREACHABLE (9 closed_by_api_level, 39 framework_never_calls, 424
  no_trigger_in_app), edges 7768, errors 0, warnings 0, UNCHECKED 2509,
  21 contradictions, 1 ENV-gated-but-ran. Diff-identical to local prior.
- scratch/build_finish_30.txt fetched: same blob SHA and counts as
  out/build_report.txt.
- method_list.json fetched: 673134 bytes, md5-identical to local copy,
  2981 entries.
- scratch/conflicts.md fetched: identical to local copy (Glide restore
  section + obsolete deletion section; reasoning there lacks printed
  source lines and does not satisfy KIRO section 3's grep requirement —
  not relied on for any verdict tonight).
- Branch root listing: NO verification.csv, NO readme_notes.md,
  NO LESSONS.md, NO make_verification.py for this app.

## Route work tonight (proposals only, see scratch/route_checks_consolidated.md)
- Re-derived from locally printed source: E89 WRONG (fix: lambda$null$5
  edge, :178/:199, guard :175); Ee1 WRONG/MISSING (fix: add
  onActionItemClicked -> decompress(String,String[]), :329);
  GlideRequest.listener wrong label -> REACHABLE proposed (:899/:945);
  GlideRequest.clone REACHABLE proposed (:45, corrected from :44);
  IconDataParcelable.setImageBroken REACHABLE proposed (:596/:599/:609/
  :724/:733 refs, :864/:883/:895 invocations);
  GlideRequests.as REACHABLE proposed with INFERRED delegation step.
- OPEN, not flipped: 13 Glide methods, SimpleTextWatcher.afterTextChanged,
  TextEditorActivity.<init> ENV gate, Sftp $2 vs $6 assignment.
- Prior section-B proposals carried as input only (not re-read tonight):
  LayoutElementParcelable.writeToParcel, RoundedImageView.setBackgroundColor,
  SimpleTextWatcher.beforeTextChanged / onTextChanged.

## Blocked
- graph_def.py fetch: "too large to display (1058622 bytes)".
- auto_calls.json (1839161) and out/methods.csv (1179770): same limit
  class; get_file_contents has no range parameter (schema verified).
- Parts assembly: merge_parts.py only appends 4 parts' UNREACHABLE
  entries; parts lack the base graph. Older under-1MB scratch copies
  rejected as non-current (decision D2).
- Token download URL: not used, not recorded (decision D1).
- Consequently NOT RUN: build, sampler, show_route on sampled routes,
  all eight checks, make_verification.py, verification.csv,
  gen_readme_v2.py, out/README.md. No check is marked passed.
- Source tree gap: only 10 Amaze java files locally; full tree needs a
  checkout or per-file connector fetches.

## Files in this local mirror (nothing pushed)
- graphs/AmazeFileManager/method_list.json (branch-verified),
  graphs/AmazeFileManager/out/build_report_branch_verified.txt,
  graphs/AmazeFileManager/readme_notes_DRAFT.md,
  graphs/AmazeFileManager/LESSONS_DRAFT.md,
  tools/build_graph.py, tools/verify_sample.py, tools/show_route.py,
  scratch/build_report_branch.txt, scratch/build_finish_30_branch.txt,
  scratch/conflicts_branch.md, scratch/merge_parts_branch.py,
  scratch/route_checks_consolidated.md,
  scratch/proposals_streamB_UNVERIFIED.py (AST-parse OK),
  STEP_LOG.md, DECISIONS.md, AGENT_NOTES.md (this file).
