# Stream D decisions (Muse's own decisions, for user/Yang review; never in Yang's name)

## AnyMemo D1 (2026-11-01): storage permission — startup-trunk ENV gate only
WRITE_EXTERNAL_STORAGE stays an explicit ENV gate ONLY on the startup trunk
(ENV_STORAGE_PERM, graph_def.py:157, on the three loadUiComponents edges;
S_PERM_STORAGE, line 1765, for the not-granted branch). NOT pre-granted
globally (fresh-install first run must pass the dialog or the activity dies
via finish(), AnyMemo.java:178, freshly printed) and NOT re-gated on every
storage route (the app checks the permission only at startup, AnyMemo.java
lines 124-182; downstream use inherits the gate through the trunk). No graph
change needed: current modelling already says this. Full reasoning in
~/workspace/overnight/stream-D/AnyMemo/DECISIONS.md.

## AnyMemo D2 (2026-11-01): partial build labelled, never gated
Connector display limit blocks auto_calls.json (1,132,200 B), methods.csv
(3,282,143 B) and trigger_graph.json (4,221,347 B). A NO-AUTO partial build is
reported separately, never as the gate build; full build/sample/checks/logs
that need those files are BLOCKED, not faked.

## AnyMemo D3 (2026-11-01): route judgment basis
30-route judgment rests on branch sample + verification.csv (30/30 correct) +
route prints cross-matched locally (20 exact in kiro_routes_all.txt; 10
prefix-truncated by the show_route comma bug, full route_print files matched
exactly) + fresh AnyMemo.java startup-trunk lines + branch build SOURCE_OK 30.
Reported as consistency re-verification, NOT an independent redraw.

## AnyMemo D4 (2026-11-01): no branch edits, no pushes, no tick marks
All overnight work local only; proposed status line stated in the final
report, not written to PROGRESS_V2.
