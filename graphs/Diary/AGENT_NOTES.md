# Diary — agent notes (finish run, branch work-2026-10-31)

Prior overnight work is in graphs/Diary/scratch/overnight-20261101/
(AGENT_NOTES.md, DECISIONS.md, LESSONS.md drafts, scratch-outputs).
This file records the finish-run steps only.

## Steps

- 2026-11-01 ~13:27 EST: merger start. Lock created
  (~/workspace/finish/locks/Diary.lock). Private tree built from the
  shared clone (HEAD 6805252649bca27392a4d70d83e45c2ef860ca8c):
  graphs/Diary copied; tools/, handoff/, fw_src/, final_java_only/,
  work-emulator symlinked read-only. No branch file edited in place.
- 2026-11-01 ~13:29 EST: local build, `bash handoff/ci/rebuild.sh Diary`
  in the private tree (output graphs/Diary/scratch/ci_latest/):
  methods 286, pages 34, edges 1435; REACHABLE 265, UNREACHABLE 21
  (framework_never_calls 4, no_trigger_in_app 17); errors 0, warnings 0;
  check 2: 81 distinct, 0 problems; check 3: 0 flagged; check 4: 0 where
  the cited line does not show the callee; checks 5-7: 5/0/0;
  STRICT = True line 1; check 8 N/A (no auto_calls.json);
  verification.csv rows: path 30, DEVICE 0.
- 2026-11-01 ~13:31 EST (T2): wrote graphs/Diary/make_verification.py
  (portable, repo-relative, deterministic). Seeded
  graphs/Diary/scratch/verification_rows.json (128 rows) once from the
  branch verification.csv. Ran the writer twice: both runs
  byte-identical to the branch verification.csv (cmp prints nothing).
  No row failed validation, so no row was corrected and no
  scratch/fix_log.md was needed; verification.csv is unchanged.
- 2026-11-01 ~13:31 EST (D7): synthetic test in a private copy:
  4 synthetic device results (reached, not reached, unscriptable,
  script failed) produced exactly the 4 expected DEVICE rows, the 128
  seed rows stayed byte-identical, and a bad-edges input errored with
  exit 1. No real graphs/Diary/device/results.csv exists in this run.
- 2026-11-01 ~13:32 EST (T2): wrote graphs/Diary/LESSONS.md (7 bullets).
  Added to readme_notes.md ## Limits: the check-5 line note (verified
  against graph_def.py lines 199, 228, 1608, 1624, 1629 — exactly the 5
  lines check 5 counts) and the check-8 N/A note. readme_notes.md keeps
  its five headings in order; gen_readme_v2.py re-run after the edit.
- 2026-11-01 ~13:33 EST (D1): verified the device lead's
  graphs-independent route list at
  ~/workspace/finish/work/device/routes/Diary/ROUTES.csv against
  verification.csv path rows and out/methods.csv: 30 rows, 0 mismatches
  (method, edges, source, env_kinds, state_kinds all exact), route ids
  unique, all status scripted, 0 unscriptable. Route_17 permissions
  (WRITE/READ_EXTERNAL_STORAGE, WRITE/READ_CALENDAR) are all declared in
  the manifest; setup and fixtures are empty, matching ci/apps.csv
  (Diary setup empty) and the absence of STATE file gates. Held for
  auditor PASS before push (helper output, not merger's own).
- D3 route scripts: fanned out to helpers (at most 5 routes each) after
  the T2 push; scripts are held for auditor PASS before push. The
  'scripted' status in ROUTES.csv is contingent on the scripts existing
  and passing the dry run (D9, coordinator-sent).
- 2026-11-01 ~13:35 EST (T2 push BLOCKED): two push attempts failed
  (attempt 1 "not a fast forward", attempt 2 "Reference cannot be
  updated") while other streams pushed. Before attempt 2, all 5 paths
  were verified untouched on the branch (readme_notes.md still the
  pre-edit version, 4 new files absent) — no content conflict, no
  partial push landed. Per the merger brief, no further retries were
  made; the push needs a coordinator-sequenced window. Staging held at
  ~/workspace/finish/work/Diary/merger/staging-T2/ (5 files, 62,970 B);
  it must be rebuilt from the private tree at retry time because this
  AGENT_NOTES.md gained entries after staging.
- 2026-11-01 ~13:40 EST (D3): 5 helpers spawned (d3-1 routes 01-05,
  d3-2 routes 06-10, d3-3 routes 11-15, d3-4 routes 16-20, d3-5 routes
  21-25), each at most 5 routes, one app. Routes 26-30 remain as the
  merger's own direct work. Helper outputs are held for auditor PASS
  before any push.

## Current step

D3 scripts complete for Diary (25 scripts + 5 unscriptable notes; drycheck 30 PASS, 0 FAIL). Held for coordinator-assigned auditor PASS before any push of device/routes/Diary/. D3 acceptance blocked on the 10% unscriptable cap (5/30 = 16.7%; see Diary-D3-CAP) pending coordinator/device-lead decision. T2 push still blocked after 3 failures (third under PUSH lock); no fourth attempt until the coordinator investigates head movement 18:51–18:56Z. CI acceptance for T2 and the D9 dry run are coordinator-sent; owed.

## Decisions made by Muse (for the user and Yang to review)

No label, edge, route, or graph_def.py change was made (ticked app;
logs + device prep only). No row failed validation. The check-5
## Limits text is the brief's prescribed wording, verified line by
line against graph_def.py before it was written. Device-prep
decisions (merger's own, for coordinator's MUSE_DECISIONS.md; full
text in MERGER_REPORT.md): Diary-D3-01/02/04 (routes 01, 02, 04
UNSCRIPTABLE, widget placement not drivable); Diary-D3-05F
(route_05 fixtures += Pictures/photo_1.jpg); Diary-D3-14
(route_14 UNSCRIPTABLE, I/O error not creatable by harness);
Diary-D3-28 (route_28 UNSCRIPTABLE, multi-pointer fling not
drivable); Diary-D3-12P (route_12 stays scripted with run-level
preconditions: 24h locale + calendar row); Diary-D3-PERM
(ROUTES.csv permissions = route grant set, all
manifest-declared); Diary-D3-CAP (GATE EXCEPTION: 5/30
unscriptable = 16.7% over the 10% D3 cap; acceptance-blocked
pending coordinator/device-lead decision, not waived here).
- 2026-11-01 ~13:51 EST (push lock adopted): coordinator-mandated PUSH
  lock protocol (ORG_RULES.md) adopted: mkdir
  ~/workspace/finish/locks/PUSH.lock before any push-files call, hold
  through the call, remove immediately after, re-check head + staged
  paths immediately before the call, break only locks older than 30
  minutes. No push without holding the lock.
- 2026-11-01 ~13:51-13:56 EST (T2 push attempt 3, UNDER LOCK): lock
  acquired 18:51:35Z (owner recorded), staging rebuilt from the private
  tree (5 files, 72 KB), pre-push branch check clean (readme_notes.md
  still pre-edit 8,816 chars; 4 new files absent). Push STILL failed:
  "failed to update reference: Reference cannot be updated"
  (approval granted). Lock removed immediately after. No partial push
  landed (branch readme_notes.md re-checked after: still pre-edit).
  NOTE FOR COORDINATOR: the lock did not prevent this failure, so the
  cause is not only concurrent local pushes — possibly a CI commit or
  an unlocked push landing inside the approval window, or a connector
  limitation. Needs coordinator investigation of head movement during
  18:51-18:56Z before a fourth attempt. No further retries made.
- 2026-11-01 ~13:57 EST (D3 d3-1 delivered, merger-verified): helper
  d3-1 (routes 01-05) delivered route_03.py + route_05.py (both
  py_compile OK; merger re-ran both dry runs in a fresh testroot:
  exit 0, EDGE_IDS exactly equal ROUTES.csv edges in order, log order
  exactly equal ROUTES order, 11/11 and 23/23) and 3
  unscriptable-candidate notes (routes 01/02/04). Merger spot-checked
  the widget claims against printed source: widget.xml prev/next are
  ImageViews with id + src only (tools:ignore ContentDescription, no
  text/desc); DiaryWidgetUpdate has no intent filter (manifest
  Theme.NoDisplay block only); Diary.java:2357-2368 broadcasts only
  placed ids; Ede74cf66 guard is "at least one Diary widget placed"
  (FW-SRC AppWidgetProvider:61-67 + Diary.java:2361-2367); the
  delivered harness has no widget-placement operation. Fabricated
  broadcast ids were rejected (they would fake the precondition).
  Note: the arrows DO carry resource-ids (R.id.prev/next), so they are
  tappable by res_id once a widget is placed — placement, not the tap,
  is the blocker.
- 2026-11-01 ~13:57 EST (decisions, merger's own, for coordinator's
  MUSE_DECISIONS.md): Diary-D3-01/02/04 — routes 01, 02, 04 are
  UNSCRIPTABLE (widget placement via launcher not drivable with the
  delivered harness; reasons as above; revisit if the device lead adds
  placement support). This disagrees with the D1 helper's
  ROUTES_NOTES.md judgment ("scriptable with UI automation"); the
  d3-1 printed evidence governs because placement has no harness
  operation. Effect: 3/30 routes unscriptable = exactly the 10% D3
  cap. Diary-D3-05F — route_05 fixtures gains Pictures/photo_1.jpg
  (file exists in $WEMU/fixtures/Pictures/, 6,303 B); the chooser
  caveat stands (if the chooser shows an app list first, an extra
  picker-app tap not in the printed route is needed at real-run time).
  Applied to the merger-side push candidate
  ~/workspace/finish/work/Diary/merger/device-routes/ROUTES.csv (4
  cells changed vs the device-lead original; diff recorded in
  MERGER_REPORT.md). The candidate is HELD for auditor PASS before
  push, as is every helper output.
- 2026-11-01 ~13:57 EST (drycheck, partial): device/drycheck.py Diary
  --load-scripts on the edited ROUTES.csv in a test root: 5 PASS
  (01/02/04 unscriptable with reason, 03/05 script dry runs incl. the
  new fixture check), 25 FAIL all "missing script route_NN.py" only —
  no edge, permission, or fixture failure on any row. The 25 resolve
  as d3-2…d3-5 outputs land and routes 26-30 are written.
- 2026-11-01 ~14:1x EST (D3 d3-2…d3-5 delivered, merger-verified):
  d3-2 (06–10) 5 scripts 65/65 edges; d3-3 (11–15) 4 scripts 39/39
  edges + ROUTE_UNSCRIPTABLE_14.md; d3-4 (16–20) 5 scripts 71/71
  edges; d3-5 (21–25) 5 scripts 53/53 edges. Merger re-verified all
  21 scripts (routes 03, 05–25 except 01/02/04/14): py_compile OK,
  fresh-testroot dry run exit 0, EDGE_IDS exactly equal ROUTES.csv
  edges in order, first-occurrence log order exactly equal ROUTES
  order. Caveats recorded in MERGER_REPORT.md (route_06 picker-app
  taps, route_07 60-DEL clear, route_17 grant-ordering constraint,
  route_23 toast no-assertion, route_12 locale/calendar
  preconditions, route_24 permission caveat).
- 2026-11-01 ~14:1x EST (merger edits, push candidate
  ~/workspace/finish/work/Diary/merger/device-routes/, helper
  originals pristine): (1) added optional --adb (default "adb") to
  the 14 scripts lacking it (all d3-2/d3-3/d3-5) — real-mode
  run_app.sh passes --adb adb (lines 190-191) and argparse would
  otherwise fail those real runs; (2) SETUP grants for routes
  08/09/10 (WRITE+READ_EXTERNAL_STORAGE before setup saves) and
  route_24 (WRITE_EXTERNAL_STORAGE pre-launch, help-copy gate
  Diary.java:561-564 runs during launch onResume), ROUTES.csv cells
  filled for 08/09/10/11/12/24 (11/12 already granted in-script);
  deliberately not granted: 21 (target is the cancel lambda itself),
  22 (Discard), 23 (toast in onPreExecute, Diary.java:3121), 07
  (alertDialog fires on any write failure, same edge); (3) route_14
  status -> unscriptable (Diary-D3-14), route_28 status ->
  unscriptable (Diary-D3-28); (4) routes 26–30 written as merger's
  own direct work: 26 scripted with flagged day-tap assumption
  (dialog class not in app slice; constructed with currEntry's
  date, Diary.java:1731-1736), 27 scripted (addEvents has no gate,
  Diary.java:1858-1876), 28 unscriptable (no script), 29 scripted
  (URI built before chooser; chooser untouched), 30 scripted
  launch-only (onResume getFile() check, Diary.java:554).
- 2026-11-01 ~14:1x EST (drycheck FULL): device/drycheck.py Diary
  --load-scripts on the push candidate: 30 PASS, 0 FAIL, exit 0
  (25 script dry runs + 5 unscriptable-with-reason). No edge,
  permission, or fixture failure on any row.
- 2026-11-01 ~14:1x EST (decisions, merger's own, for coordinator's
  MUSE_DECISIONS.md): Diary-D3-14 (route_14 unscriptable; I/O error
  not creatable by delivered harness; getHome fallback
  Diary.java:1982-1988; directory-fixture avenue unverified);
  Diary-D3-28 (route_28 unscriptable; multi-pointer fling not
  drivable; !multi early return Diary.java:3440-3441, multi set
  only on 2+ pointers Diary.java:841-842); Diary-D3-12P (route_12
  stays scripted with run-level preconditions: 24h locale + calendar
  row; degrades to unclear, never wrong, if unprovisioned);
  Diary-D3-PERM (ROUTES.csv permissions = route grant set: ENV gates
  + setup preconditions, all manifest-declared); Diary-D3-CAP (GATE
  EXCEPTION: 5/30 unscriptable = 16.7% over the 10% cap; D3
  scripts-complete + drycheck-clean but acceptance-blocked pending
  coordinator/device-lead decision: widget placement alone -> 2/30,
  or fling + route_14 avenue together -> 3/30).

## Continuation merger 2026-11-01 ~14:30 EST (all three audits PASS: D1, d3-01-15, d3-16-30)

- Adopted the previous merger's work dir + private tree (no rebuild).
  Scope: T2 + device-prep pushes ONLY; no label, edge, route, or
  graph_def.py change; no PROGRESS line (coordinator only).
- STEP 1 (in progress): T2 push retry under the PUSH lock with the
  corrected protocol (mkdir success = only authority for ownership;
  never write owner.txt after a failed mkdir). Staging rebuilt from
  this private tree (AGENT_NOTES.md had gained entries since the old
  staging; other 4 T2 files byte-identical to the old staging).
  verification.csv NOT pushed (unchanged, byte-identical to branch).
  Coordinator investigation of the three prior T2 failures is recorded
  in STATE.md (no commit inside 18:51-18:56Z; next head move 493450f
  at 18:56:34Z; no [ci] commit near the window; failures consistent
  with the known lock limitation, not a new defect).
- STEP 2 (planned, after T2 lands): D1/D3 push of the 31-file device
  candidate (ROUTES.csv + 25 scripts + 5 unscriptable notes; never
  __pycache__/.pyc), after three docstring-only touch-ups
  (--adb wiring normalized to forward to Runner; route_05 stale
  fixture sentence corrected; route_26 header cites the v1.06
  CustomCalendarDialog source) + full drycheck re-verification
  (Diary 30 PASS, 0 FAIL required).
- STEP 3 (report, not a claim): D7 DEVICE rows already implemented in
  the writer and proven on synthetic data; no real
  graphs/Diary/device/results.csv exists. F1 awaits coordinator CI
  REBUILD acceptance + D9 dry run + the Diary-D3-CAP decision.
  Diary-D3-CAP stays an OPEN F1 blocker: 5/30 unscriptable = 16.7%
  over the 10% D3 cap; harness extension (widget placement alone ->
  2/30; fling/multi-touch + route_14 avenue together -> 3/30) or a
  user ruling is still owed. No row hidden to meet the cap.
