# AnyMemo — decisions (Muse's own decisions, for user/Yang review; never in Yang's name)

Overnight stream D, 2026-11-01. Branch work-2026-10-31, repo bugfixops/ground-truth-results.
No pushes; all work local under ~/workspace/overnight/stream-D/AnyMemo/.

## D1 (REQUIRED): the AnyMemo storage-permission question — DECIDED

Question: is WRITE_EXTERNAL_STORAGE treated as pre-granted, or only where a route
needs it? It touches graphs/AnyMemo/graph_def.py:157 (ENV_STORAGE_PERM) and the
startup gate near line 1765 (S_PERM_STORAGE ENTERS edge).

Fresh source printed via the GitHub connector from
final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo/ui/AnyMemo.java:

- onCreate, lines 124-141: if SDK_INT <= Q (29) and WRITE_EXTERNAL_STORAGE is not
  granted, requestPermissions() is called (:127); if already granted and !isUiLoaded,
  loadUiComponents() runs (:131-133). If SDK_INT > Q, loadUiComponents() runs
  unconditionally (:137-139).
- onResume, lines 145-162: on API <= Q, loadUiComponents() runs only if the
  permission is already granted (:155-158) — the gap-fill for the case where
  onCreate could not proceed because the dialog was still pending.
- onRequestPermissionsResult, lines 165-182: grant -> loadUiComponents() (:170-173);
  deny (or empty result) -> Toast then finish() (:178).
- prepareStoreage(), lines ~269-277: the unreadable-storage dialog's Exit button
  calls finish() (:275); no permission re-check anywhere downstream.

DECISION: keep the current modelling — permission is an explicit ENV gate ONLY
on the startup trunk, not pre-granted globally and not re-gated on every
storage-touching route. Concretely:

- ENV_STORAGE_PERM (graph_def.py:157: "the WRITE_EXTERNAL_STORAGE runtime
  permission is granted (requested once on API <= 29; always granted on API 27 if
  accepted)") stays as the ENV gate on exactly the three loadUiComponents edges
  (onCreate-granted, onRequestPermissionsResult-granted, onResume-gap-fill) and
  S_PERM_STORAGE (line 1765: the dialog shown when not granted) stays as the
  not-granted branch.
- No graph change is needed: the current text already says this. This decision
  CONFIRMS the existing modelling; it does not edit graph_def.py (and no branch
  file is edited by this overnight run in any case).

Reasoning:

1. Pre-granted globally would be wrong: on a fresh install the first run MUST
   pass the dialog (Allow) or the activity dies via finish() at :178. Deleting
   the gate would overstate first-run reachability and hide the only
   permission-deny exit in the app.
2. Re-gating every storage-touching route would be wrong too: the app checks
   the permission only at startup (lines 124-182). Downstream storage use
   (prepareStoreage, file browsers, DB open) never re-checks it; it inherits the
   gate through the startup trunk. A second gate would double-count one user
   action and would contradict the source.
3. On the API 27 standard configuration SDK_INT (27) <= Q is always true, so the
   gate always applies on first run and is satisfied thereafter by the one
   acceptance (a runtime grant persists until revoked). The ENV text's "always
   granted on API 27 if accepted" states exactly this.
4. Effect on labels/routes: none numerically. Every launcher-trunk route already
   carries the permission ENV gate (branch build: 1881 methods with ENV); the
   deny path to onDestroy is already modelled (graph_def.py:322). Route checks
   and logs in this run are consistent with this decision.

Status: decided by Muse (overnight stream D leaf), for user/Yang review. If the
user prefers the pre-granted reading, the change would be to drop ENV_STORAGE_PERM
from the three loadUiComponents edges — that change is NOT made.

## D2: partial-build approach under the connector size limit — DECIDED

Branch auto_calls.json (1,132,200 B) exceeds the connector get_file_contents
display limit, and the MCP tool offers no chunked/range fetch; the download URL
it prints carries a token, which this task forbids using. DECISION: run the
build locally with a clearly-labelled NO-AUTO partial copy (USE_AUTO=False,
stub auto_calls {"calls": []}) to validate graph_def.py syntax, hand edges and
the UNREACHABLE set, and report its counts SEPARATELY from the branch build
counts — never as the gate build. The full local build, sample redraw,
check_citations, check_routes, check_bytecode_lines, scan_unreachable,
make_verification and gen_readme_v2 are BLOCKED (not passed, not faked) until a
route for the large files exists (e.g. a Mac clone in the morning).

## D3: route-check judgment basis — DECIDED

With out/methods.csv (3,282,143 B) and out/anymemo_trigger_graph.json
(4,221,347 B) unfetchable for the same reason, the 30-route judgment in this run
rests on: (a) the branch final sample (kiro_sample_30_final.txt, seed 20261025)
and branch verification.csv path rows (30/30 correct, SOURCE); (b) the branch
route prints — 20 routes match the verified path exactly in kiro_routes_all.txt,
and the other 10 are exact prefixes truncated by the known show_route.py comma-
citation crash, whose full comma-safe prints (scratch/route_print/*.txt) were
then fetched and matched against verification.csv; (c) fresh AnyMemo.java lines
for the shared startup trunk; (d) the branch build report's path status
SOURCE_OK 30. This is reported as a consistency re-verification, NOT as an
independent redraw — the redraw itself is blocked (see D2).

## D4: no branch edits, no pushes — DECIDED (standing overnight constraint)

All overnight work stays local; nothing is written to PROGRESS_V2, graph_def.py,
out/, verification.csv or AGENT_NOTES on the branch, and no tick marker is written
anywhere. The proposed status line is stated in the final report only.
