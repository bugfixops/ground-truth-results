# UNVERIFIED PROPOSAL — has NOT passed build, sampler, full-repo grep, or C1 checks; re-check from printed source before relying/merging.

# AnkiDroid WP2 route-check — part 2 (DRAFT, UNVERIFIED, NOT MERGED)

Repo: bugfixops/ground-truth-results, branch work-2026-10-31 only.
Status: NOT done. No [K] status claimed. No build, sampler, grep, or C1 count is
claimed in this draft unless a helper report below prints it.

## Baseline re-checked in this stage (printed, not copied)
- graphs/AnkiDroid/out/build_report.txt: methods 4186, edges 9178,
  REACHABLE 3275, UNREACHABLE 911, errors 0, warnings 0, path UNCHECKED 3275.
  Unreachable by kind: no_trigger_in_app 749, branch_never_taken 48,
  framework_never_calls 48, closed_by_api_level 44, closed_by_configuration 22.
  Labels: SOURCE 3945, INFERRED 241. Edge classes: explicit 8164,
  non_standard 26, page 56, standard 932.
- Sanity (tool coverage, NEVER evidence): 1 UNREACHABLE but ran:
  Card.toString (libanki). 180 ENV-gated but ran lines are sanity only.

## Sampler blocker (the reason WP2 cannot be marked [K] from the connector)
- tools/verify_sample.py reads graphs/AnkiDroid/out/methods.csv.
  That file is 2,805,329 bytes and the GitHub connector returns
  "too large to display" for it. graphs/AnkiDroid/graph_def.py is
  1,173,446 bytes and is likewise too large to display.
  graphs/AnkiDroid/out/<prefix>_trigger_graph.json is needed by the
  route-print template and was not fetched (same size class).
- Therefore: no sampler draw (30, seed 20261025) is claimed, no final
  sample table, no error rate, no verification.csv, no readme_notes.md
  / gen_readme_v2.py / LESSONS.md finalisation, and none of the eight
  checks in handover section 2 is claimed as passed in this stage.
- What WAS done instead: route judging from small parts files and
  printed source, plus resolution work on the four open items from
  the first set. Those are proposals, not verified routes.
- What unblocks [K]: a full local checkout of work-2026-10-31 on a
  machine that can run python3 -I tools/verify_sample.py AnkiDroid 30
  20261025, tools/build_graph.py, check_citations, check_routes,
  check_bytecode_lines, scan_unreachable --all/--callers, and
  make_verification (which does not yet exist for AnkiDroid), with
  printed output saved under graphs/AnkiDroid/scratch/.

## Open items from the first set (to be filled from helper reports)
1. Card.toString — helper report DELIVERED:
   ~/workspace/ankidroid-wp2/card_tostring_hunt.md
   Verdict still UNCLEAR, label NOT flipped, APE hit NOT used as
   evidence. New mechanism found in printed source: Card.flush()
   (Card.java:214) and Card.flushSched() (Card.java:243) both end in
   mCol.log(this); Collection.log(Object... args) (Collection.java:
   1498-1513, fetched spaced) passes args into TextUtils.join at
   :1510, which stringifies each arg (join->toString step INFERRED,
   pending fw_src TextUtils print). Gate blocks closure:
   Collection.log returns immediately unless mDebugLog is true
   (:1499-1501); 3-/4-arg constructors default false (:129-139),
   only the 5-arg constructor takes a log parameter, and no in-app
   new Collection(...) site was printed. Excluded: AdvancedStatistics
   inner Card sites, runFilter (arg is StatsMetaInfo), all local
   Timber/Log/format/concat and List<Card> candidates, and
   Hooks.runHook pass-through alone (hook bodies not printed).
   Decisive full-checkout greps (saved to scratch/ at merge time):
   new Collection( sites + log argument; flush/flushSched callers;
   runHook/runFilter Card sites + hook bodies; exhaustive Timber/Log/
   valueOf/format/concat + List<Card> sweep; fw_src TextUtils.join.
   Settle rule: REACHABLE only if gate-open on a standard path plus
   a reachable flush caller (or a printed hook/log stringification
   on a reachable path); otherwise keep UNREACHABLE with greps cited
   and the APE hit recorded as unexplained by app source.
2. Hooks.runFilter -> AdvancedStatistics.runFilter — helper report
   DELIVERED: ~/workspace/ankidroid-wp2/hooks_runfilter_route.md
   Per-step verdicts: Hooks constructor gate CORRECT (Hooks.java:61-62,
   preference read once at first singleton construction); install
   registration CORRECT (AdvancedStatistics.java:147-149); Stats ->
   Hooks.runFilter call + argument order CORRECT (Stats.java:308-311);
   line-150 interface dispatch CORRECT as a mechanism, a direct
   Hooks.runFilter -> AdvancedStatistics.runFilter edge would be WRONG
   (presence in built graph UNCLEAR, not claimed); runFilter override
   + setStatsCalculated(true) CORRECT (AdvancedStatistics.java:140-146,
   175); fallback calculateDue(AxisType) CORRECT (Stats.java:331,
   fresh-StatsMetaInfo premise INFERRED); upstream
   Statistics.ChartFragment -> TaskHandler -> ChartBuilder ->
   Stats.calculateDue CORRECT for every printed step (Statistics.java:
   483-487, TaskHandler:108-110, ChartBuilder:69-73/112-113; fragment
   and AsyncTask dispatches INFERRED); full route from the launcher
   UNCLEAR (launcher entry not printed — sole remaining blocker).
   Proposed gate (not merged, exact text in helper report): MG943
   STATE settings — SharedPreferences advanced_statistics_enabled
   must be true (default false), so AdvancedStatistics is registered
   under hook key advancedStatistics when Hooks.runFilter runs;
   otherwise runFilter returns input unchanged and calculateDue
   falls back to calculateDue(AxisType) at Stats.java:331.
   Proposed edge fix (not applied): keep label_100.py hand edge,
   replace its MG943 note with the attached gate; write no direct
   Hooks.runFilter edge, suppress/reclassify one if a full-checkout
   grep finds it. The exact needs_state text must match the
   STATE_KINDS_OF table in graph_def.py at merge time; that table
   could not be read here because graph_def.py exceeds the connector
   display limit.
3. EasySSLSocketFactory.equals/hashCode and API 27 vs target 23 —
   helper report DELIVERED: ~/workspace/ankidroid-wp2/easyssl_api27.md
   EasySSL: INFERRED UNREACHABLE STANDS, not flipped, not settled.
   Printed SOURCE: comment :102-105, equals :108-110 (body :109),
   hashCode :114-116 (body :115), sole printed construction
   HttpSyncer.java:228, ThreadSafeClientConnManager :229,
   DefaultHttpClient.execute :236; no printed app call on the
   factory in local files. Comment proves only that some managers
   need the overrides, not that this one compares/hashes a scheme.
   Apache HttpClient 4.x not in dataset, not read/downloaded.
   API 27: RESOLVED for Compat dispatch (CompatHelper.java:55-57
   returns SDK_INT, :35-36 selects CompatV21 at >=21, so API 27 ->
   CompatV21 regardless of target 23; closed_by_api_level labels on
   that chain unaffected); OPEN for the rest of the app (only
   CompatHelper.java was locally available, zero targetSdkVersion
   hits there, no CompatV* bodies/manifest/CardContentProvider, no
   fw_src lines printed, so no framework permission/shim claim).
4. Parts routes (label_134-137) — helper report DELIVERED:
   ~/workspace/ankidroid-wp2/parts_routes_part1.md
   Parts fetched spaced, complete: label_134 38 rows, label_135 40,
   label_136 40, label_137 40, all REACHABLE as labelled in parts.
   10 methods judged, all PROPOSED REACHABLE, 0 verified for merge,
   0 re-printed steps judged WRONG, 150 rows not judged:
   answerCard, clipboardGetText, delayedHide (134);
   GraphicsWrap.<init>, GraphicsWrap.setClip (135);
   TranslationActivity.translate,
   LoadPronounciationActivity.onLoadPronunciation (136);
   Reviewer.addNote, Whiteboard.touchStart, YAxis.drawMarkers (137).
   Every route has at least one NOT CHECKED upstream/entry step
   (S_REVIEWER / S_STATISTICS / S_TRANSLATION /
   S_LOAD_PRONONCIATION entry or framework dispatch, or a part .py
   e() edge not re-fetched). S_REVIEWER and S_STATISTICS ENTERS
   gaps in label_137 affect rows 3, 4, 5, 8, 9; label_137.py's
   claimed fix edges were not re-fetched and remain unverified.

## Route table (this stage, NOT the WP2 final sample table)
- Items judged in this stage: 10 parts routes (all proposed
  REACHABLE, 0 verified for merge) + 4 open items (Card UNCLEAR,
  Hooks edge fixed-on-gate / full route UNCLEAR, EasySSL stands,
  API 27 Compat resolved / rest OPEN).
- No step re-printed in this stage was judged WRONG. No route was
  judged correct end-to-end in this stage (Hooks full route and
  all 10 parts routes are UNCLEAR / conditional on an unprinted
  entry step).
- Correct / fixed / wrong / unclear counts for the WP2 sample:
  NOT COMPUTED. Error rate = (fixed + wrong) / (correct + fixed
  + wrong) — not computed until a final sampler draw exists.
  Do not quote a rate from the first set (5 items, 0 full routes
  correct) or from this stage as the WP2 rate.

## Proposed fixes (NOT merged)
- Hooks.runFilter gate attachment above (MG943).
- Any other fixes will be listed here only after helper reports
  print the current graph_def.py / parts lines they propose to change.
  Helpers never edit graph_def.py, out/, progress, tools, or
  another helper's files; merges happen only after C1 checks pass
  on a full checkout.

## Decisions needed (user/Yang — none decided here)
- EasySSL: accept INFERRED UNREACHABLE for equals/hashCode, or
  authorise reading Apache HttpClient 4.x source (outside the
  dataset; brief allows only AOSP downloads).
- API 27: confirm device-API-27 rule for all labels, or name
  targetSdk-sensitive methods to re-check.
- Card.toString: full-checkout grep for libanki Card passed to
  Object parameters must be printed before the label is settled.
- Working copy: how to obtain a full local checkout of
  work-2026-10-31 so the sampler, build, and C1 checks can run.
  No token is to be waited for (user instruction 2026-10-31);
  work via the connector until that method is agreed.

## Files in this stage (local only, not pushed)
- ~/workspace/ankidroid-wp2/MUSE_HANDOVER.md
- ~/workspace/ankidroid-wp2/AGENT_NOTES.md
- ~/workspace/ankidroid-wp2/conflicts.md
- ~/workspace/ankidroid-wp2/build_report.txt
- ~/workspace/ankidroid-wp2/method_list.json
- ~/workspace/ankidroid-wp2/tools_*.py (verify_sample, build_graph,
  check_citations, check_routes, scan_unreachable, gen_readme_v2)
- ~/workspace/ankidroid-wp2/route_print_template.py
- Helper reports listed above (when delivered).
