## What the re-audit changed (compared with the schema 1 graph)

- STRICT mode on (B1, graph_def.py line 10: STRICT = True).
- Check 2 (B2): the 3 NotificationService citation problems were a
  checker-regex artefact (tools/check_citations.py ROOT_STYLE matches the
  services/NotificationService.java:<digits> substring inside the full-path
  citation). Fixed on the citation side only, keeping the full path and
  writing line numbers in words (:47 -> (line 47), :46-54 -> (lines 46-54),
  :37 -> (line 37)). Check 2 is now 0 problems (273 distinct).
- Check 4 (B3): one combined EDIT (single EDIT definition) fixes all 48
  bytecode lines from the checker's own keys: 23 TaskData/ChartBuilder/
  DisplayPair line moves + 18 libanki Utils path pins (bare Utils.java ->
  com/ichi2/libanki/Utils.java) + 7 MockNoteFactory INFERRED rewrites
  (source under multimediacard/test/ is pruned from the checker source
  index; it is NOT absent from the upload). Check 4 is now 0 not-show
  (6904 checked, with the disclosed caveat that the 23 B3-a edges drop
  out of the checker's checked set because their "(bytecode line was N)"
  form does not match its pattern; verification rests on printed lines
  and auditor re-prints).
- Check 8 (B4): all 169 scan lines explained in
  scratch/check8_explained.md (106 sibling-only + 52 remainder-only +
  11 mixed). The paint-sync helper's "8 NEW entries" already existed in
  graph_def_mod/01.py sup() blocks (VERIFY-ONLY, never duplicated); one
  ReliefLegend reason reworded (getLegend has no caller and ReliefDrawer
  itself is never constructed).
- Route checks (B6): no label changes (REACHABLE 3275, UNREACHABLE 911
  throughout). Fixes are guard/evidence additions, two variant-page
  splits (SyncErrorDialog NOT_LOGGED_IN/MEDIA; ConfirmationDialog
  FULLSYNC/RENAME/NOTEEDITOR_CHANGETYPE), and audited corrected
  derivations for the 18 WRONG routes. Final graph: methods 4186,
  pages 48, edges 9183, errors 0, warnings 0.

## How the checked paths were chosen

- `python3 -I tools/verify_sample.py AnkiDroid 30 20261025` on the
  pre-fix graph: 30 of 3275 REACHABLE methods, stratified
  (NONSTD 4, INFERRED 4, STATE 3, ENV 6, LONG 6, PLAIN 7), spreading over
  route edges (299 distinct edges). Every route was printed with
  scratch/route_print.py and judged step by step against printed source
  (including if/catch/for conditions), then fixed one route at a time
  with a rebuild after each fix group (F1-F5), each fix group
  independently audit-PASS before merging.
- The route table (scratch/route_table.md) covers the FIRST-draw 30
  routes: WRONG 18, FIXED 9, UNCLEAR 2, CORRECT 1; first-draw error rate
  27/28 = 0.9643. For FIXED/CORRECT routes the table route is the final
  BFS route (the fix is in the graph). For WRONG routes the table route
  is the audited corrected derivation (never the BFS route where the
  audit says BFS is misleading: routes 12, 13, 18, 20, 21, 26, 30, and
  routes 01-06 from C01-C06). verification.csv path rows use the built
  (BFS) route's edge ids with the audited verdict, and their notes
  point at the corrected derivation for WRONG routes.

## What waits for a device (API 27)

- Device preparation (D1/D3) is separate from this log work: the final
  sample's 30 routes need device/routes/AnkiDroid/ROUTES.csv and one
  script per scripted route, plus DEVICE rows in make_verification.py,
  before the CI device dry run (D9). No device run has been made in
  this run (no emulator/adb use); the user runs
  .github/workflows/device-replay.yml later.
- Routes whose table route is a corrected derivation (the 18 WRONG
  routes) must be scripted from the CORRECTED route, not from the BFS
  route: in particular route 21 from the hkey-empty NOT_LOGGED_IN
  prefix, route 30 from the SAVE_MODEL prefix, route 20 from the
  UPDATE_FACT + mUpdateCardHandler prefix, and route 26 from route A
  (open) or B (rename-flow), never from the generic-page dispatch
  route. Route 12 must be scripted from the reviewer flow (answerCard
  with mAnswerCardHandler), never from the LOAD_DECK_COUNTS prefix.
- The redraw sample differs from the first-draw sample (see Limits):
  if the coordinator rules the final table must cover the redraw
  sample, the 5 redraw-only methods need judging + device scripts too.

## Hazard candidates (from reading the code, not reproduced)

- Card.toString is UNREACHABLE (no_trigger_in_app) but ran in a tool
  run (coverage_baseline.json; the build's sanity check still reports
  this contradiction). The label is unchanged: the contradiction is a
  candidate for a future caller hunt, not a flip on coverage alone
  (labels come only from printed source).
- The graph's best-route finder does not evaluate guard text against
  actual arguments: for routes 13, 21 and 30 the BFS best route still
  shows a guard-inconsistent prefix even after the fix (dispatch chain
  wins on cost for route 13; the old DeckPicker prefix for route 30).
  A guard-checking redraw must reject those prefixes in favour of the
  corrected routes in route_table.md; this is a cost-model limitation,
  not a reason to split or suppress edges without a separate audited
  proposal.
- The builder does not deduplicate hand edges with the same
  (src, dst, kind) but different guards: the combined graph contains
  both the F4 and F5 hand edges for DeckPicker.onCreate ->
  CollectionHelper.exceededCursorSizeLimit and for
  CollectionHelper.getCol -> Storage.Collection (both guards true for
  the same call sites). No label or route effect; recorded in
  route_table.md.

## Limits

- Check 5 counts the schema-1 DEAD/FRAMEWORK_ONLY container lines and
  SUPPRESS lines in graph_def.py / graph_def_mod/01.py; they are
  temporary containers converted to UNREACHABLE entries, not placeholder
  labels. Greps for DEAD|FRAMEWORK_ONLY, FW-MEMORY and PENDING are
  reported in the CI SUMMARY; the PENDING count is 0 in the final graph
  files (see the B6 build record).
- The redraw sample differs from the first-draw sample (5 methods swap
  in/out; 297 vs 299 distinct edges) because the sampler spreads over
  route_edge_ids, which change when fix edits change edge ids, and
  because B6 added ENV/STATE kinds to more methods. This table covers
  the first-draw sample per the merger's assigned task; the 5
  redraw-only methods (CardTemplateEditor$CardTemplateFragment$4.<init>,
  Info.copyDebugInfo, AbstractFlashcardViewer.typeAnswer,
  BackupManager.deleteDeckBackups, CustomTabsHelper.hasSpecializedHandlerIntents)
  are unjudged here.
- Route 06 stays UNCLEAR (final step INFERRED: support-v4 lifecycle
  source not in the tree) and route 08 stays UNCLEAR (step 11 INFERRED;
  $15 -> $16 rename held on bytecode proof). Only route 16 (Sched.
  haveBuried) is CORRECT, and only the 18 WRONG routes' corrected
  derivations establish their targets; the targets themselves all
  remain REACHABLE (no label was changed by any route verdict).
- tools/show_route.py crashes on multi-citation lifecycle edges; this
  is pre-existing (identical on the unmodified baseline) and tools/
  was not edited. The merger used its own dump methods for those
  routes.
