# Currency — agent notes (local mirror, 2026-11-01; NO PUSH, branch files untouched)

- Setup: reconstructed via GitHub connector, one file at a time with ~30 s
  pauses: graphs/Currency/graph_def.py (615 lines), method_list.json
  (145 methods — handover count 145 confirmed, not trusted blindly),
  auto_calls.json, tools/build_graph.py, verify_sample.py,
  check_citations.py, check_routes.py, check_bytecode_lines.py,
  scan_unreachable.py, gen_readme_v2.py, show_route.py, branch
  verification.csv (98 rows), readme_notes.md, DATASET.txt, all 17 app
  Java files, AndroidManifest.xml, res/xml/preferences.xml and widget.xml,
  and 20 cited AOSP files under fw_src/android-8.1.0_r1/.
- Build: `python3 -I tools/build_graph.py graphs/Currency Currency` —
  145 methods, 140 REACHABLE / 5 UNREACHABLE, 393 edges, 0 errors,
  0 warnings, STALE 0, STRICT=True. Re-run identical.
- Sample: `python3 -I tools/verify_sample.py Currency 30 20261025` —
  27 methods, 107 edges (pools exhaust below 30). All 27 routes printed
  step by step (scratch/routes_full.txt, 2,400 lines) and judged
  (scratch/route_judgements.md): 23 correct, 0 fixed, 0 wrong, 4 unclear;
  error rate 0.0. No graph fix; redraw identical (diff clean).
- Eight checks: build PASS; citations PARTIAL (2 problems, both the
  oversize ActivityManagerService.java); routes PASS (0 flagged);
  bytecode PASS vacuous (0 edges); greps PASS (0/0/0); scan PASS with
  explanations. Full report: scratch/eight_checks.md.
- Logs: verification.csv unchanged branch copy (make_verification.py
  missing on branch — blocker, see DECISIONS.md D1); readme_notes.md
  updated locally + README generated via gen_readme_v2.py (exit 0);
  LESSONS.md (6 bullets) and DECISIONS.md (D1–D6, Muse's own) written.
- Blockers for the gate (tooling only, not label/route failures):
  (1) fw_src ActivityManagerService.java (1,086,106 B) exceeds connector
  display; (2) tools/make_verification.py absent from the branch.
- Proposed status line (NOT written to PROGRESS_V2):
  "[K] Currency (labels, route checks and logs DONE 2026-11-01; device
  checks not started; awaiting user tick)" — to be used only once the
  two tooling blockers are resolved or waived by the user.
