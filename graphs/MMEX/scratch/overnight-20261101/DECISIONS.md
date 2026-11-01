# MMEX — Muse's own decisions (for user/Yang review, never in Yang's name)

Local mirror only. No decision below has been pushed or written to the branch.
Status of each decision: PROPOSED unless marked ADOPTED-FOR-MIRROR (applied only to
local mirror drafts, not to branch files). Nothing here changes a branch label.

## D-MMEX-1 — TutorialPagerAdapter.getPageTitle: KEEP UNREACHABLE / framework_never_calls / INFERRED
- Reasoning: app-side evidence re-printed by two prior helpers stands — the tutorial
  layout (activity_tutorial.xml) has only ViewPager + CircleIndicator + TextView, no
  title widget; TutorialActivity wires only CircleIndicator via setViewPager; the only
  other getPageTitle definition (AboutTabAdapter) is paired with a TabLayout via
  setupWithViewPager, the title-consuming pattern the tutorial lacks. Library source
  (CircleIndicator 2.1.6, androidx ViewPager) is not in the repo (declared as Gradle
  coordinates, no vendored copy found in checked locations), so the library step stays
  INFERRED exactly as the label already states. No relabel, no SOURCE upgrade.
- Route-check consequence: the item stays UNCLEAR as a route-check verdict (the library
  step is unprinted code), but the LABEL is kept as correct-with-INFERRED-caveat. The
  two are different judgments and must not be conflated in counts.
- Status: PROPOSED (label kept in mirror drafts; no branch change).

## D-MMEX-2 — ScreenTree dispatch edges under the debug standard configuration: DO NOT silently keep; DO NOT delete without a build
- Reasoning: printed source (MmexApplication.java:134-139) plants DebugTree in the
  debug branch and ScreenTree only in the release branch. The label_146
  ScreenTree.log -> PasscodeActivity.onEvent edge is therefore wrong as a debug-build
  route (part-1 R9), and helper2 verified the exact deletion proposal for that edge.
  The same pattern recurs: label_032 ScreenTree -> MmxBaseFragmentActivity.onEvent and
  label_092 ScreenTree -> WatchlistFragment.onEvent, both with "a release build"
  descriptions, plus label_096 CALL edges into ScreenTree.log guarded "release build
  only". A one-edge deletion would leave the systematic issue half-fixed.
- Decision: the correct end state is that no release-only edge may serve as the sole
  route for a REACHABLE label in the debug-config graph. The mechanism (delete the
  dispatch edges vs. a build-honoured release-only exclusion) must be confirmed against
  printed tools/build_graph.py behaviour first — annotation alone is NOT verified to
  exclude an edge (helper2 caveat; build code read this session shows no release/debug
  filter on edges). Until a build can be run to show label effects, NO ScreenTree edge
  is deleted in the mirror and NO label is flipped on this issue. PasscodeActivity.onEvent,
  MmxBaseFragmentActivity.onEvent and WatchlistFragment.onEvent stay REACHABLE via
  their parallel DebugTree edges (to be confirmed per method before any deletion).
- Status: PROPOSED, blocked on build (see STEP_LOG blockers).

## D-MMEX-3 — DebugTree env wording: widen when the graph is next edited
- Reasoning: DebugTree.java:36-38 (minLevel INFO, guard priority >= minLevel) and
  40-46 (post for any log at INFO+, "Error: " prefix only with a throwable) prove the
  current "an error is logged" wording is too narrow, and the shared env text naming
  ScreenTree is wrong for a debug route. Helper2 verified the exact replacement texts
  (Fix B). Wording-only: no label change.
- Status: PROPOSED edit text recorded in mirror (not applied to branch parts).

## D-MMEX-4 — ACTION_PICK wording on setResultAndFinish@ edges: description completeness only
- Reasoning: helper2's nuance corrects part-1 Fix 4: the home-arrow (BaseExpandableListFragment
  :164, BaseListFragment :157) and Back-key (AccountListActivity :64) calls to
  setResultAndFinish are NOT ACTION_PICK-gated; ACTION_PICK gates only (i) the row-tap
  handlers (CategoryListFragment :661 block) and (ii) what setResult() returns
  (RESULT_OK vs RESULT_CANCELED / no result). Any fix must state the gate in that
  scoped form and must NOT claim the @ methods cannot run without ACTION_PICK.
- Status: PROPOSED edit text recorded in mirror (not applied to branch parts).

## D-MMEX-5 — Prior judged items adopted as INPUT ONLY, not as verified route checks
- Reasoning: part-1 (20 items: 18 correct / 1 wrong / 1 unclear) and helper4 (16 items:
  16 correct) were judged on printed source, but neither ran the sampler, the build, or
  C1 checks, and neither drew the seed-20261025 sample. Their verdicts are therefore
  carried into this session as re-derivation targets, not as the WP2 sample table.
  Consolidated input-only tally: 36 judged, 34 correct, 1 wrong (edge only, R9),
  1 unclear (R1). This tally is NOT the sample error rate.
- Status: ADOPTED-FOR-MIRROR (counting rule for this session's report).

## D-MMEX-6 — Reconstruction fidelity rule for the mirror
- Reasoning: connector display refuses files above ~1 MB, and the task forbids token
  download URLs. Mirror parts are therefore accepted ONLY when (a) fetched via the
  connector in this session, or (b) byte-verified against branch blob SHAs from a
  connector directory listing (git blob SHA + size match). No part is accepted from
  memory, from an old generated graph, or from tool coverage. The graph_def header
  (TITLE/STRICT/USE_AUTO/SUPPRESS/CLASSIFY/EDIT, ~11 KB by size difference) is NOT in
  any part file and must NOT be invented: any local build using a reconstructed header
  is labelled PARTIAL and its counts are never reported as branch verification.
- Status: ADOPTED-FOR-MIRROR.

## D-MMEX-7 — Partial build is diagnostics only, never gate evidence
- Reasoning: the partial build (USE_AUTO=False, reconstructed helpers, no
  CLASSIFY/EDIT) proves the 147 parts assemble, compile, and agree with the
  branch report on every hand-checkable count (UNREACHABLE 840 + kinds exact,
  all non-CALL edge kinds exact except the 5 header ENTRY edges, 0
  UNREACHABLE-with-incoming-hand-edge warnings, C1-subset 0 problems). It does
  NOT prove the branch build: 3237 no-path errors are the missing auto edges,
  and routes/classes/confirmed_by from partial data are wrong by construction.
- Status: ADOPTED-FOR-MIRROR (partial numbers quarantined from gate claims).

## D-MMEX-8 — Parts/graph_def divergence (p085, 10 edges): merged graph_def wins
- Reasoning: branch AGENT_NOTES (p085 fix entry) records the 10 bare-evidence
  edges as fixed in graph_def.py, while current branch parts still carry the
  bare evidence (proven by the partial build). The parts are therefore NOT
  byte-identical to the merged graph for those 10 edges, and any future merge
  from parts would regress the fix and flip edge_sourced/confirmed_by for
  routes through SelectDatabaseActivity / MyActionBarDrawerToggle.
- Decision: before any future part-based merge, re-sync those 10 part edges to
  the merged text (first evidence segment SRC; LIFECYCLE edge: app line SRC +
  framework INFERRED). NOT applied this session (no branch edits, no push).
- Status: PROPOSED for morning.

## D-MMEX-9 — ScreenTree dispatch scope is 4 edges, each with a DebugTree parallel
- Reasoning: full 147-part sweep finds ScreenTree.log dispatch edges only in
  label_032, label_092, label_113 and label_146, and each target has a parallel
  DebugTree.log edge (032:14, 092:143, 113:38, 146:8). Deleting the 4 dispatch
  edges therefore would not orphan those targets. ScreenTree.log itself (its
  debug-config reachability rests on release-guarded CALL edges + INFERRED
  Timber dispatch) and the label_096 CALL edges into it are separate open
  items, not decided here.
- Status: PROPOSED for morning (deletion still needs a faithful build to
  confirm no other route depends on the 4 edges).

## D-MMEX-10 — No sample from partial data
- Reasoning: verify_sample.py on partial methods.csv would draw from 193
  hand-reachable methods with hand-only routes, not the branch's 3430
  reachable methods with true best routes. Any such "sample" would be invalid
  and could leak into reports as if it were the seed-20261025 sample.
- Decision: sampler runs only on a faithful build's methods.csv. This session's
  sampler attempt (FileNotFoundError, exit 1) is the recorded outcome.
- Status: ADOPTED-FOR-MIRROR.

## D-MMEX-11 — Literal DEAD-word grep on parts is 2 (prose, not verdicts)
- Reasoning: label_144.py line 8 (comment "is DEAD") and line 133
  (UNREACHABLE reason starting "DEAD PATH") are the only DEAD|FRAMEWORK_ONLY
  substring hits in the parts. They are prose, not legacy DEAD/FRAMEWORK_ONLY
  verdict dicts, but KIRO check (5) as literally specified (grep -c = 0)
  counts substrings, so the parts as written fail that literal check. The
  merged graph_def count is unknown (it may differ, as in D-MMEX-8).
- Decision (proposed for morning): reword the two prose occurrences
  (comment -> "unreachable"; reason -> drop the "DEAD PATH" prefix) and
  confirm the merged graph_def grep count is 0. NOT applied this session.
- Status: PROPOSED for morning.
