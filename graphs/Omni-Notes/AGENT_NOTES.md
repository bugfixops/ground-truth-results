# Agent Notes — Omni-Notes (finish run, branch work-2026-10-31)

Ticked app: log work only (T4) plus device preparation (D1, D3, D7). No label,
edge, route, or graph_def.py change is made here; the PROGRESS line stays as it is.

## Current step

T4 done locally; its push is pending a sequenced retry under the push-lock
protocol (see below). D1 ROUTES.csv + ROUTES_NOTES written and drycheck-valid
except missing scripts. D3 scripts: route_01 template dry-runs clean; helpers
for routes 02-33 fanned out (7 helpers, all routes covered). CI request for
Omni-Notes is with the coordinator (coordinator-only send).

## Steps

- 2026-11-01: private tree built from the clone (HEAD 6805252): graphs/Omni-Notes
  copied; tools/, handoff/, fw_src/, final_java_only/, work-emulator symlinked
  read-only. Lock: finish/locks/Omni-Notes.lock.
- 2026-11-01: local rebuild in the private tree (`bash handoff/ci/rebuild.sh
  Omni-Notes`): methods 1456, REACHABLE 1202, UNREACHABLE 254 (no_trigger_in_app
  194, framework_never_calls 34, closed_by_configuration 21, branch_never_taken 5),
  errors 0, warnings 0; check 2: 0 problems; check 3: 0 flagged; check 4: 0
  where the cited line does not show the callee; checks 5-7: DEAD|FRAMEWORK_ONLY
  11, FW-MEMORY 0, PENDING 0, STRICT 1; check 8: 5 of 254; verification.csv rows:
  path 33, DEVICE 0. Matches the branch CI SUMMARY (commit 60c27937) except the
  header commit/timestamp and the absent sanity block (no coverage_baseline.json
  locally is expected; sanity lines only).
- 2026-11-01 (T4 writer): current verification.csv counted: header exactly
  `type,item,result,confirmed_by,ref,edges,note`; 370 rows (path 33, label 288,
  edge 49); path verdicts 3 correct, 29 fixed, 1 wrong (DbHelper.deleteNote).
  Seeded to graphs/Omni-Notes/scratch/verification_rows.json (370 rows, current
  order). Wrote portable graphs/Omni-Notes/make_verification.py (repo-relative,
  validates every row against out/methods.csv and the trigger graph; see the
  writer's docstring for the kept UNREACHABLE path-row exception).
- 2026-11-01 (T4 writer acceptance): two runs in the private tree, both exit 0,
  both byte-identical to the current verification.csv (`cmp` prints nothing;
  md5 0ffb1225dcfa19984f4cf43d20af8510 before and after). No row failed
  validation, so no scratch/fix_log.md entry and no verification.csv change.
  One writer bug found and fixed during the run: the first draft asserted every
  UNREACHABLE label note names its kind, but most UNREACHABLE label rows carry a
  generic "call sites searched" note; only the seven changed labels carry an
  "ERROR FOUND ... UNREACHABLE (kind)" note. The assertion was dropped (label
  notes are validated for existence, result, confirmed_by, and non-empty only).
- 2026-11-01 (D7 test): synthetic device/results.csv (4 rows: reached, not
  reached, script failed, unscriptable) in a private test copy: writer exit 0,
  exactly 4 DEVICE rows appended after the seeded rows with the brief's format
  (correct/unclear, DEVICE ref, script status + reason); no label changes. The
  no-results case is the byte-identical run above. No real
  graphs/Omni-Notes/device/results.csv exists or was written.
- 2026-11-01 (T4 checks): check-5 lines printed from graph_def.py (1635, 1641
  population; 1693, 1694, 1793, 1794, 1801, 1808 SUPPRESS uses; 2078 comment;
  2136 conversion loop; 2145 reset) — containers + SUPPRESS lines, not
  placeholders. Check 8 re-run fresh (`scan_unreachable.py Omni-Notes
  --callers`): the same 5 methods; each reason names and explains its caller,
  confirmed against printed caller lines (GeocodeHelper.java:168,
  DetailFragment.java:1102 and :1032, menu_detail.xml:73-78,
  DetailFragment.java:1956-1962, SettingsActivity.java:50,78-83,
  GeocodeHelper.java:173-175,228). No graph change needed.
- 2026-11-01 (T4 readme): added two bullets to readme_notes.md `## Limits`
  (check-5 11-line note; check-8 five-caller confirmation). Five headings still
  in order. `gen_readme_v2.py Omni-Notes` exit 0; regenerated out/README.md
  differs from the branch out/README.md by exactly those two bullets.
- 2026-11-01 (T4 LESSONS): wrote graphs/Omni-Notes/LESSONS.md (7 bullets, from
  readme_notes.md and the overnight AGENT_NOTES/DECISIONS/LESSONS inputs).
- 2026-11-01 (T4 push, pre-lock protocol): staging verified (5 files, all under
  900 KB, 0 token hits, py_compile OK; branch readme matched the 14,208 B base
  and all four new files were absent). Attempt 1 failed "not a fast forward"
  (head moved 024e7102 to 2722b9a0 during the window); paths re-verified
  untouched and attempt 2 made once, which also failed "not a fast forward"
  (head moved to 21db8c53). No partial push landed either time. No further
  retries (no-loop rule); staging held for a sequenced retry.
- 2026-11-01 (push-lock protocol, coordinator mandate, ORG_RULES.md): adopted
  immediately. Before any push-files call: atomic `mkdir
  finish/locks/PUSH.lock`; if it exists, do other work and retry later (never
  spin/sleep-loop); owner + UTC time inside; re-check head + staged paths
  immediately before the call; hold through the call; remove immediately
  after, success or fail; locks older than 30 minutes may be broken (record
  owner/time). First check under the mandate found PUSH.lock held by the Diary
  merger (taken 2026-11-01T18:51:35Z, fresh, not stale), so no push was
  attempted; other work (D3 helpers for routes 27-33) was done instead.
- 2026-11-01 (D1): ROUTES.csv written (33 rows in path-row order, 30 scripted,
  3 unscriptable = 9.09%) plus ROUTES_NOTES.md (permission mapping, fixtures,
  setup, special rows). Drycheck on ROUTES.csv with no scripts: 3 unscriptable
  PASS, 30 scripted fail only on "missing script" (chains, permissions,
  fixtures all valid). Route_01 template script dry-runs clean (exit 0, 26 log
  lines) and drycheck route_01 PASS with --load-scripts.
- 2026-11-01 (D3 helpers): 7 helpers fanned out (routes 02-06, 07-11, 12-16,
  17-21, 22-26, 27-31, 32-33; route_01 is the merger's own template). Their
  scripts merge into staging only after coordinator-assigned auditor PASS.

## Decisions made by Muse (for the user and Yang to review)

None of these is made in Yang's name. Each states what was decided, why, and what
would change it. (Full section-6 records go to handoff/MUSE_DECISIONS.md via the
coordinator; these are the Omni-Notes entries.)

- T4-W1 (writer seeded from the current csv, not rewritten from the sample):
  the old writer is unlocatable and the sample files live in overnight scratch,
  so seeding the 370 current rows into scratch/verification_rows.json and
  validating them against the fresh build is the only route to a byte-identical,
  deterministic writer. Revert: a branch-side writer that reproduces the same
  370 rows from first principles replaces the seed.
- T4-C8 (check-8 five confirmed, no Limits fix): all five reasons name and
  explain their outside callers (printed lines above), so T1 step 4's fallback
  (explain in Limits) is not triggered; Limits gains a confirmation bullet
  instead. Revert: a reason found not to cover its caller moves that method's
  explanation into Limits with printed lines.
- T4-C5 (Limits gains the 11-line note): the brief requires the note; the lines
  were printed and match the containers + SUPPRESS description. Revert: a
  branch-side cleanup removing the legacy-dict machinery from graph_def.py
  (a graph change, not for this ticked app) would make the note obsolete.
- T4-D7 (DEVICE rows appended after seeded rows): the brief fixes the row
  format but not the position; appending keeps the seeded order byte-identical
  when no results file exists. Revert: none needed; position changes only if
  the device lead's compare.py output ordering requires it.
