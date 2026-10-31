# UNVERIFIED PROPOSAL — DO NOT RELY ON, MERGE, OR USE AS EVIDENCE YET

**Status: UNVERIFIED.** This is a coordinator first part from 2026-10-31, saved here so it is not lost. It has NOT passed a build, sampler, full-repo grep, or C1 checks on a full local checkout, and must be re-checked from printed source before any label, route, or graph change is relied on or merged.

**Branch rule:** work in progress is on work-2026-10-31 only, never main, and the 'result' branch is not used for work in progress unless the user says so.

---

# AnkiDroid WP2 route-check — first set (PROPOSED, NOT MERGED, NOT PUSHED)

Status: **PENDING — do not push.** This part is not verified under the C1 checks,
because verification genuinely requires running tools locally on a full checkout,
which this connector-only working copy cannot do. Delivered as a clearly separable
proposed set only, per the updated push rule. Nothing in the repo was edited, merged,
or pushed by this helper. No route was assigned to Card.toString.

Standard configuration used for judging: debug build, fresh install, API 27,
permissions only where a route needs them (handover §2).

## Sampler limitation (stated, not worked around)

- The WP2 target sample (30 methods, seed 20261025) was NOT drawn. This VM has no
  local clone and `tools/verify_sample.py` / `tools/build_graph.py` cannot be run on
  a full checkout via the connector alone. No `sample_30.txt` output is claimed.
- Therefore there is no final sample table, no error rate, and WP2 for AnkiDroid is
  NOT done. Error rate = (fixed + wrong) / (correct + fixed + wrong) cannot be
  computed on this first set, and none is invented.
- `graphs/AnkiDroid/verification.csv` is absent from the directory listing of
  `graphs/AnkiDroid/` on branch `work-2026-10-31` (files present: AGENT_NOTES.md,
  auto_calls.json, coverage_baseline.json, graph_def.py, method_list.json, out/,
  parts/, review_notes.md, scratch/). That is consistent with 0 route checks so far.

## Counts re-checked (not copied from the handover)

From `graphs/AnkiDroid/out/build_report.txt` on `work-2026-10-31`, printed in full
in this session:

- methods 4186, edges 9178
- verdicts: REACHABLE 3275, UNREACHABLE 911
- unreachable by kind: branch_never_taken 48, closed_by_api_level 44,
  closed_by_configuration 22, framework_never_calls 48, no_trigger_in_app 749
- errors: 0, warnings: 0
- path status: UNCHECKED 3275
- labels confirmed by: INFERRED 241, SOURCE 3945
- edge classes: explicit 8164, non_standard 26, page 56, standard 932
- sanity (tool coverage, never used to set a label): 1 UNREACHABLE but ran
  (Card.toString); 180 ENV-gated but ran. These lines are NOT evidence for any label.

These match the handover's 4186 / 3275 / 911 / 0 / 0, but the match was checked
against `out/build_report.txt` itself, not taken on trust.

## 1. Card.toString (libanki) — verdict: UNCLEAR (label NOT resolved)

Current label (per `graphs/AnkiDroid/scratch/conflicts.md` and
`graphs/AnkiDroid/out/build_report.txt`): UNREACHABLE, `no_trigger_in_app`.
The single tool-run hit (APE, `sanity_check.csv` row 2424 per conflicts.md) is
**NOT evidence for a label** and does not flip it to REACHABLE.

Printed source checked in this session:

- `final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/java/com/ichi2/libanki/Card.java:634-648`:
  `public String toString()` exists, reflection-based, `SKIP_PRINT` at 630-632.
  The only occurrence of `toString` in that file is its own definition (grep of the
  printed file: line 634 only). No internal caller in Card.java.
- `.../com/ichi2/libanki/hooks/AdvancedStatistics.java:399` — inner private class
  `Card` with its own `toString` at ~408-411 (`"Card [ivl=" + ...`).
  `AdvancedStatistics.java` imports no `com.ichi2.libanki.Card` (imports printed,
  lines 20-44: `com.ichi2.libanki.Collection`, `Decks`, `Stats` only).
- `AdvancedStatistics.java:1474-1501` — `ReviewOutcome.card` is of the inner type
  (field at 1475, constructor at 1478), and `ReviewOutcome.toString` at 1495-1501
  concatenates `"card=" + card`, i.e. the inner Card, not libanki Card.
- `AdvancedStatistics.java:1710-1716` — `Review.writeLog` does
  `Timber.d(tabs + prevCard)` / `Timber.d(tabs + newCard)` where prevCard/newCard
  are inner-Card fields (1549, 1555). Again not libanki Card.toString.

What was NOT checked (so the item stays open): the hypothesis recorded in
conflicts.md — a libanki Card passed to an Object-typed parameter (a log call or a
collection of Objects) on a path the earlier greps missed. An exhaustive grep over
the app source root for libanki Card variables was not possible via the connector
in this session (global code search is unscoped to this repo/branch and returned
0/incomplete results; it was not used as evidence). Until that grep is printed on
a full checkout, Card.toString must not be given a route and its label must not
be flipped on the tool hit alone.

Proposed fix: none to the label yet. Next step (for the merging agent, on a full
checkout): print a grep for libanki Card usages passed to Object parameters /
Timber / collections; if a printed line shows such a call from a reachable caller,
relabel REACHABLE with that citation; otherwise keep UNREACHABLE and record the
grep output in scratch/.

## 2. EasySSLSocketFactory.equals and hashCode — verdict: UNCLEAR (both)

Current labels (per `graphs/AnkiDroid/parts/label_126.md`): UNREACHABLE,
`no_trigger_in_app`, `confirmed_by` INFERRED, for both methods. That INFERRED
status is correct as far as it goes — but the labels are not settled.

Printed source checked in this session:

- `.../org/apache/commons/httpclient/contrib/ssl/EasySSLSocketFactory.java:102-105`
  (printed in full, 117 lines): the file's own comment says
  "Both Object.equals() and Object.hashCode() must be overridden for the correct
  operation of some connection managers".
- Same file: `equals` at 108-110
  (`return ((obj != null) && obj.getClass().equals(EasySSLSocketFactory.class));`),
  `hashCode` at 114-116 (`return EasySSLSocketFactory.class.hashCode();`).
  (conflicts.md cites body lines 109/115; label_126 cites ranges 107-110/113-116
  including `@Override`. No contradiction once the annotation lines are counted.)
- `.../com/ichi2/libanki/sync/HttpSyncer.java:226-236` (printed): line 228 is the
  sole construction in the app source,
  `registry.register(new Scheme("https", new EasySSLSocketFactory(), 443));`;
  line 229 hands that registry to `new ThreadSafeClientConnManager(params, registry)`;
  lines 235-236 run `new DefaultHttpClient(cm, params)` and `httpClient.execute(httpPost)`.

Step-by-step judgement: no app code calls equals/hashCode on the factory (that
half of label_126 is supported by the printed construction site and by the
label's own grep claim), BUT the factory is handed to a connection manager, and
the factory's own comment warns that some connection managers need these
overrides. Whether this app's HttpClient/connection-manager path compares or
hashes the scheme is a library question: Apache HttpClient 4.x source is not in
the dataset and was not read here. A step not printed counts as not checked.

Proposed fix: keep both labels INFERRED UNREACHABLE for now; do not mark them
correct. Decision needed from the reviewer/user (as conflicts.md already says):
either (a) accept the INFERRED labels as standing, or (b) authorise reading the
Apache HttpClient 4.x Scheme / ThreadSafeClientConnManager source from outside
the dataset (the brief's "only download allowed" is AOSP 8.1.0_r1, so this needs
an explicit decision) and, if it compares/hashes schemes, relabel both REACHABLE
with a route through HttpSyncer.req (ENV network gate).

## 3. Hooks.runFilter → AdvancedStatistics.runFilter pair — verdict: WRONG as a direct edge; hand edge CORRECT, full route UNCLEAR, gate MISSING

Printed source checked in this session:

- `.../com/ichi2/libanki/hooks/Hooks.java:60-62` (printed): the constructor
  installs AdvancedStatistics only `if (prefs.getBoolean("advanced_statistics_enabled", false))`.
- `Hooks.java:138-158` (printed): `runFilter` returns `arg` unchanged if
  `hooks == null` (139-143); otherwise it looks up `hooks.get(hook)` (144) and,
  only if non-null, loops `arg = func.runFilter(arg, args)` (150). The call at
  line 150 is to the interface `Hook.runFilter`, not a direct call to
  `AdvancedStatistics.runFilter`.
- `.../com/ichi2/libanki/hooks/AdvancedStatistics.java:99` (printed):
  `public class AdvancedStatistics extends Hook`; `runFilter` override at 141-146
  (uses `args[1]` as Context, `args[0]` as AxisType, `args[2]` as String);
  `install` at 147-149 registers `h.addHook("advancedStatistics", new AdvancedStatistics())`.
- `.../com/ichi2/libanki/Stats.java:308-311` (printed): `calculateDue(Context,AxisType)`
  calls `Hooks.getInstance(context).runFilter("advancedStatistics", metaInfo, type, context, _limit())`,
  and falls back to `calculateDue(type)` at 331 when `isStatsCalculated()` is false.
  The argument order matches AdvancedStatistics.runFilter's casts exactly.
- `graphs/AnkiDroid/parts/label_100.py:12-17` (printed): the hand edge is
  `e('Stats.calculateDue(Context,AxisType)', 'AdvancedStatistics.runFilter', 'CALL', ...,
  cls='non_standard', via=['hook registry dispatch (Hooks.runFilter loops over the Hook objects
  registered under the key advancedStatistics)'], evidence='SRC ...Stats.java:308-311;
  ...Hooks.java:61-62, 138-150; ...AdvancedStatistics.java:141-148')`.
  Its note (line 17) says `MISSING GATE MG943: the preference
  advanced_statistics_enabled (default false, Hooks.java:61) must be true`.

Judgement:

- The hand edge's class (non_standard, via hook registry) and its evidence are
  CORRECT against the printed lines. The dispatch is a registry dispatch, not an
  explicit call.
- Any direct explicit/auto CALL edge `Hooks.runFilter → AdvancedStatistics.runFilter`
  in `graph_def.py` would be WRONG as written: Hooks.java:150 calls the interface
  method, and the target is selected only by the registered key. AGENT_NOTES
  records this pair as "suspect automatic CALL, not suppressed". This session
  could NOT confirm whether such an auto edge is still present in the built graph,
  because `graph_def.py` (1,173,446 bytes) and `auto_calls.json` (2,543,896 bytes)
  are both too large for the connector's file display, and no line-range fetch
  exists in the connector's get_file_contents schema.
- The full route from the launcher is UNCLEAR in this session: the upstream steps
  (launcher → ChartBuilder.calcStats case FORECAST → Stats.calculateDue, cited in
  label_100.md but not printed here) were not printed, so the route cannot be
  marked correct under KIRO §4 ("a route with any step not printed counts as NOT checked").
- The gate is genuinely missing from the edge as written in label_100.py: it is
  only a note, not an attached STATE settings gate.

Proposed fixes (not merged):

1. Attach a STATE `settings` gate to the Stats.calculateDue → AdvancedStatistics.runFilter
   edge: "preference advanced_statistics_enabled must be true (Hooks.java:61-62,
   default false); otherwise Stats.java:331 fallback runs instead".
2. On a full checkout, grep `graph_def.py` / `auto_calls.json` for the pair
   `Hooks.runFilter → AdvancedStatistics.runFilter`; if a direct explicit CALL edge
   exists alongside the label_100 non_standard edge, suppress it (sup block, with
   Hooks.java:150 as justification) or reclassify it, keeping only the
   non_standard registry edge. If no such edge exists, record that the AGENT_NOTES
   "suspect" note is stale.
3. Print the upstream ChartBuilder/Statistics steps before marking the full route correct.

Note on the parallel runHook case (for contrast, not a new verdict): label_104.md
records the analogous `Hooks.runHook → Leech$LeechHook.runHook` as a non_standard
registry edge with gate MG982, and `Hook.runHook` as UNREACHABLE branch_never_taken
because the only dispatched key is `leech` and its only registrant overrides
runHook. The runFilter case follows the same pattern; the difference is only that
its gate was left as a note rather than attached.

## 4. API level 27 vs target 23 question — verdict: PARTIALLY RESOLVED for Compat dispatch; otherwise OPEN (decision needed)

Printed source checked in this session:

- DATASET facts (AGENT_NOTES setup): package `com.ichi2.anki`, min_sdk 10,
  target_sdk 23, source commit 58725f6db609b85c01c2a6e026f55c6c357447e1.
- `.../com/ichi2/compat/CompatHelper.java:33-36` (printed): selection is
  `getSdkVersion() >= 21 → new CompatV21()`, with the Nook special case at 33.
- `CompatHelper.java:55-57` (printed): `getSdkVersion()` returns
  `Build.VERSION.SDK_INT` — the device API level, not the target SDK.

Judgement: for every Compat dispatch in the graph, the API-27 outcome does NOT
depend on target_sdk 23: on an API 27 device the chain selects CompatV21
regardless of the manifest target. The `closed_by_api_level` labels that rest on
CompatHelper (e.g. CompatV10 base bodies shadowed by the CompatV21 chain, per
label_072.md) are therefore unaffected by the target-23 question.

What remains open: whether any other label in the graph depends on targetSdk
rather than SDK_INT (framework behaviour that changes with targetSdk, e.g.
permission-model or other compatibility shims). No such method was identified in
this session, and no framework claim is made here, because no `fw_src/android-8.1.0_r1/`
lines were printed in this session (framework claims cite only printed fw_src
lines; none are cited).

Decision needed (user/Yang): confirm that the standard configuration is "device
API 27, whatever the manifest target" for all labels, or name the target-sensitive
methods to re-check. Until then this question is not closed.

## Counts for routes actually judged (only these)

- Items judged: 5 (Card.toString; EasySSLSocketFactory.equals; EasySSLSocketFactory.hashCode;
  Hooks.runFilter/AdvancedStatistics.runFilter edge; API 27 vs target 23 question).
- Verdicts: correct (edge only, full route not fully printed): 0 full routes;
  correct (single edge, evidence + class): 1 (Stats.calculateDue → AdvancedStatistics.runFilter
  as a non_standard edge, gate aside);
  wrong (as a direct explicit edge, if present in graph_def — presence unconfirmed): 1 pair;
  unclear: 4 items (Card.toString; equals; hashCode; API question overall; plus the
  full runFilter route upstream).
- No route was marked correct end-to-end. No error rate is computed (no sample).
- `confirmed_by` used in this report: SOURCE only for lines printed in this session;
  INFERRED is quoted from existing labels where the underlying source was not read
  (library/platform). No DYN, FW-MEMORY, or UNVERIFIED is used or endorsed.
- Tool coverage (Monkey/APE, coverage_baseline.json, sanity_check.csv, JaCoCo) was
  NOT used as evidence for any label in this report; it is mentioned only to
  record that the Card.toString contradiction exists and remains unexplained.

## Blockers / decisions needed

1. No local clone / no local tool runs: sampler (30, seed 20261025), build_graph,
   check_citations, check_routes, check_bytecode_lines, scan_unreachable, and
   make_verification cannot be run from the connector alone. A full-checkout agent
   must do these before anything here is marked verified or pushable.
2. `graph_def.py` (1.17 MB) and `auto_calls.json` (2.54 MB) exceed the connector's
   file-display limit and get_file_contents has no line-range parameter, so the
   presence/absence of the suspect Hooks.runFilter auto edge, and the current
   gate attachment on the label_100 edge, could not be confirmed here.
3. Decisions needed: (a) EasySSL equals/hashCode — accept INFERRED or authorise
   reading Apache HttpClient 4.x source; (b) API 27 vs target 23 — confirm the
   device-API-27 rule for all labels or name target-sensitive methods;
   (c) Card.toString — the Object-parameter grep must be printed before the
   label is settled.
4. Rate-limit note: one transient HTTP 429 occurred when fetching AGENT_NOTES.md
   in a burst of parallel connector calls early in this session; the file was
   fetched successfully on a later spaced call. Further connector work should stay
   spaced, not bursty.
5. Push rule applied: this part is PENDING, not pushable. When verified on a full
   checkout, it should be merged and pushed as a separate commit to branch
   `result` in bugfixops/ground-truth-results only (naming AnkiDroid and the part),
   never to work-2026-10-31 or main — and not by this helper, to avoid conflicts
   with parallel helpers on shared files.

## Files produced by this helper (local workspace only, not in the repo)

- Route-check report (this file): ~/workspace/wp2-ankidroid/route_check_part1.md
- Printed-source extracts used for judging (local copies only): Card.java,
  EasySSLSocketFactory.java, HttpSyncer.java, Hooks.java, AdvancedStatistics.java,
  Stats.java, CompatHelper.java, label_100.md/.py, label_104.md, label_126.md,
  label_072.md, agent_notes.md, build_report.txt, handover.md, kiro.md, brief.md,
  schema.md — all under ~/workspace/wp2-ankidroid/.
