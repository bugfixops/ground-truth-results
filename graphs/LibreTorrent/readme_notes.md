# LibreTorrent logs — readme notes (B6 logs step)

Prose/docs only. This file changes no verdict, no label, and no graph
file, and it claims no device result. Every fact below comes from the
B6 final route table, the final B6 judgments, the B6 audits, the D7
labels-gate report, or the D5/D6 report listed in DOCS_REPORT.md.

## What the re-audit changed (compared with the schema 1 graph)

The graph judged in B6 is the schema-2 rebuild from printed source:
120 parts merged, on branch base commit `a9e8b93d` with graph_def blob
`564da867` — 4732 methods, 7293 edges, R3882 / U764 / UNRES86. The D7
gate rebuild reproduces the audited D5 post-fix graph byte-identically,
so the judged graph is the stable, fully measured graph, not a fresh
variant.

D5 citation fixes took check-4 bad from 166 to 141. The remaining 141
are not zero and are not hidden: Class A 134 file-not-found lines
(generated code absent from the source tree: data-binding 108 + Room
26) plus Class B 7 name-not-within-2 lines (compiler-emitted
try-with-resources closes). Their disposition is ruling-owed (R2/R3),
not closed in this logs step — see Limits below.

No label changes were made in this step. Labels stay R3882 / U764 /
UNRES86 unless a separate audited T1 execution (NOT this task) changes
them.

## How the checked paths were chosen

The sample was drawn with seed 20261025
(`python3 -I tools/verify_sample.py LibreTorrent 30 20261025`) from
the 3882 REACHABLE methods, stratified by quota: NONSTD 4, INFERRED 4,
ENV 6, LONG 6, PLAIN 7, STATE 3. The STATE stratum pool is empty
(0 STATE-gated methods in all 4732 rows), so its quota of 3 went
unfilled and the sample is 27 routes, not 30 — do NOT pad it to 30.

The first draw IS the final draw: there was no redraw. A confirmatory
second sampler run was cmp-identical. The 27 routes total 407 steps
and 294 distinct edges.

Judging standard: every step needs BOTH action TRUE (the source
actually calls/reaches the destination as drawn, on printed lines) AND
operative condition TRUE (guards and STATE/ENV preconditions
satisfiable in ONE execution: fresh install, API 27, instrumented
debug build). A step failing either is FALSE.

Every route was judged by a helper and independently audited (A1–A5).
Two routes were overturned on audit and went to a fresh re-judge plus
re-audit: route 2 (havePiece, WRONG → CORRECT) and route 19 (safRoot,
CORRECT → WRONG). The superseded original judgments are NOT used here.
Final counts: CORRECT 19 / WRONG 8 / UNCLEAR 0 / BLOCKED 0, rate
8/27 ≈ 0.2963.

B6 did NOT fix WRONG routes in place (FIXED = 0): the 8 WRONG routes
stay WRONG with their decisive-step reasons; fix directions in the B6
report are NOT applied here.

## What waits for a device (API 27)

Device work comes AFTER logs. No device ROUTES rows, no device
scripts, and no DEVICE rows were built in this logs step, and no
device result is claimed anywhere in these docs.

What is pending, in coordinator-dispatched order: the logs-step push,
then device D1/D3/D7, then CI rebuild → SUMMARY gate → dry-run
request → D9. The judging precondition throughout B6 was a fresh
install on API 27 in an instrumented debug build; whether the judged
premises hold on a real device run is exactly what that later device
phase is for, and it has not happened yet.

## Hazard candidates (from reading the code, not reproduced)

Each item below is a READING HAZARD drawn only from the B6 judgments
— a place where a future route, script, or device step could go wrong
in the same way a judged route already did. None of these was
reproduced on a device in this step, and none is claimed as a device
failure.

- GC-finalize nondeterminism (route 3, FeedDao_Impl$11.finalize):
  a drawn step from a constructor to `finalize` rests on garbage
  collection, which is nondeterministic and not guaranteed in one
  execution. Reading hazard, not a reproduced failure.
- SAF content:// prefix no in-app action can supply (routes 17 and
  19, SafFileSystem.getParentDirUri and safRoot): on a fresh install
  the seed/save path is necessarily file://, the in-app picker returns
  Uri.fromFile results only, and no in-app action makes a path
  content:// — so any route or script that needs a content:// prefix
  must supply it from outside the app or not be drawn that way.
  Reading hazard, not a reproduced failure.
- ADD/EDIT dialog-mode conflation (routes 4 and 7, PathResolver.join
  and FeedDao_Impl$1.bind): prefixes launched in one dialog mode
  (FILE_CHOOSER_MODE, ADD mode) were mixed with middles/tails from
  another mode (SAVE_FILE_MODE, EDIT mode), so steps that are each
  sound in isolation do not form one real execution. Reading hazard,
  not a reproduced failure.
- Worker action-dispatch mismatch (route 8, BaseElement.getUri):
  fixing the work input to one action (ACTION_FETCH_ALL_CHANNELS)
  dispatches to the plural handler (fetchChannels), not the singular
  handler the route draws. Reading hazard, not a reproduced failure.
- Fragment-commit versus header-click path (route 10,
  SettingsRepositoryImpl.proxyLogin): the fragment committed by the
  drawn step is AppearanceSettingsFragment; the Network fragment
  arrives only via the unprinted network-header click path, and a
  satisfiable screen-size guard cannot change which fragment was
  committed. Reading hazard, not a reproduced failure.
- Cancel-button versus positive-button listener (route 6,
  AddTagViewModel$TagAlreadyExistsException): the drawn cancel-button
  listener calls finish(CANCEL) and never calls addTag; addTag is
  reachable only via the positive/add button listener, which the
  route does not draw. Reading hazard, not a reproduced failure.

## Limits

Honest, measured limits. None of these is closed here.

- Check-2 has 131 problems (ruling-owed R8): all "file not held",
  over 10 app paths, all app citations in `core/...` short form that
  the checker matches against framework sources only. Disposition
  owed: explained checker-scope artifact, citation-form rewrite, or
  checker exemption.
- Check-4 bad is 141, NOT zero (ruling-owed R2/R3): Class A 134
  file-not-found + Class B 7 name-not-within-2. The `checked` figure
  (1673) excludes file-not-found lines, so bad is NOT a subset of
  checked.
- Check-8 has 33 explained rows (33 of 764 unreachable methods have a
  bytecode caller outside the set); check-8 --all 0 is 0 by
  construction and is not the substantive figure (the default split
  is 606 with other mentions / 158 with none).
- Warnings total 16 (15 method warnings + 1 REVIEW line), including
  the notifySound warning (ruling-owed R4: keep-and-explain versus
  suppress).
- Errors total 86, exactly the 86 UNRESOLVED methods — technical
  blocker T1, blocking F1 until labeled (or until a ruling disposes
  of them; none granted). T1 plus user-owed rulings R1–R8 are all
  still owed: R1 D4 FeedParser lines/edges, R2 D5 Class A route,
  R3 D5 Class B handling, R4 notifySound option, R5 b034 hand-edge
  dedupe auditor ruling, R6 batch-3 row 26 OPEN flag,
  R7 59/32 setVariable label question, R8 check-2 131 disposition.
- The 59/32 edge Ea751b47d appears in ZERO sampled routes and is
  never claimed as a verified route. All 407 drawn steps have 0
  src/dst touches of unresolved_86.txt.
- Batch-3 row 26 (TagInfo.hashCode) stays flagged OPEN: its
  'closed by b003' marking is NOT accepted, and the provenance /
  documentation dispute (accept cells-govern or reopen) is owed as
  R6, not settled here. The label itself (UNREACHABLE / SOURCE) is
  present and audited; the OPEN flag is the dispute.
- The b034 hand-edge dedupe ruling is owed (R5): edge E147e95ca is
  present and is the sole edge from TorrentSessionImpl.download to
  convert(Priority)#2, but the dedupe itself is NOT treated as
  settled.
- Route-2 caveat-2 ruling (i) + rule-(ii) contingency, carried in
  full: TorrentDownloadImpl.havePiece is CORRECT under ruling (i) —
  the caveat attaches ONLY to drawn route steps, and its
  shutdown-first premise chain (SchedulerReceiver/TorrentService/
  Utils setup methods, all in unresolved_86.txt) was verified
  directly from source, not from the graph, so it is setup history,
  not a drawn step. Contingency, NOT adopted: if the gate adopts
  rule (ii) (caveat attaches to any method the verdict depends on),
  route 2 becomes BLOCKED with no verdict, counts become CORRECT 18
  / WRONG 8 / BLOCKED 1, rate 8/26 ≈ 0.3077.
- No label changes in this step: labels stay R3882/U764/UNRES86
  unless a separate audited T1 execution (NOT this task) changes
  them.
- B6 did NOT fix WRONG routes in place (FIXED = 0): the 8 WRONG
  routes stay WRONG with their decisive-step reasons; fix directions
  in the B6 report are NOT applied here.
- The STATE stratum pool is empty (0 STATE-gated methods in all
  4732 rows), which is why the sample is 27, not 30 — do NOT pad it
  to 30.
- Two drawn steps are UNVERIFIABLE (generated Room code absent from
  the upload), both explicitly non-decisive: FeedDao_Impl$1.bind
  step 14 and FeedDao_Impl$11.finalize step 19. No route was left
  unjudgeable on their account.
