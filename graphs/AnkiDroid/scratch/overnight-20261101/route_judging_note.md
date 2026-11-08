# AnkiDroid — source judging note (NOT the WP2 sample table)

No sampler draw exists tonight (verify_sample fails: out/methods.csv is
missing locally). This note judges only the open items, from printed lines
in the local source copies under scratch/src_*.java. Verdicts use SOURCE
only for lines printed here; everything else is INFERRED or open.

## 1. Card.toString (libanki) — label UNCHANGED, contradiction OPEN

- Card.java:634-648 defines toString (reflection over declared fields,
  skipping SKIP_PRINT at :630-632). The only toString occurrence in
  Card.java is its own definition. No internal caller in that file.
- AdvancedStatistics.java:399-411: a separate private inner class Card
  with its own toString ("Card [ivl=...").
- AdvancedStatistics.java:1475 (ReviewOutcome.card, inner type), :1497-1501
  (ReviewOutcome.toString concatenates "card=" + card — inner card),
  :1549/:1555 (Review.prevCard/newCard, inner Card fields), :1714-1720
  (Review.writeLog logs tabs + prevCard and tabs + newCard — inner cards).
- AdvancedStatistics imports com.ichi2.libanki.Collection, Decks, Stats
  only; no libanki Card import.
- Verdict: the printed stringification sites do NOT call libanki
  Card.toString. The APE hit in the branch build report's sanity section
  is tool coverage and is never evidence, so it does not flip the label.
  What would settle it: a full-checkout grep printing a libanki Card
  passed to an Object parameter on a reachable path. Until then the label
  stays UNREACHABLE, no_trigger_in_app, and the contradiction stays open.

## 2. EasySSLSocketFactory.equals / hashCode — labels STAND (INFERRED)

- EasySSLSocketFactory.java:102-105: comment that "some connection
  managers" need the overrides. Equals :108-110 (body :109, class
  equality only). HashCode :114-116 (body :115, constant class hash).
- HttpSyncer.java:226-229: SchemeRegistry, https scheme registered with
  new EasySSLSocketFactory() at :228, registry handed to
  ThreadSafeClientConnManager at :229; DefaultHttpClient at :235, execute
  at :236.
- No printed app line calls equals or hashCode on the factory.
- Verdict: both stay UNREACHABLE, no_trigger_in_app, INFERRED (decision A).
  The comment proves a possibility for some managers, not a call by this
  manager. Flipping requires a printed HttpClient compare/hash line.

## 3. Hooks.runFilter -> AdvancedStatistics.runFilter — edge mechanism CORRECT, full route UNCLEAR

- Stats.java:308-311: calculateDue(Context,AxisType) calls
  Hooks.getInstance(context).runFilter("advancedStatistics", metaInfo,
  type, context, _limit()); :312 checks isStatsCalculated(); :331 falls
  back to calculateDue(type).
- AdvancedStatistics.java:141-146: runFilter casts args[1] to Context,
  args[0] to AxisType, args[2] to String — exactly the Stats call's
  argument order. Install at :147-149 registers key "advancedStatistics".
- Hooks.java:60-62 (constructor): AdvancedStatistics installed only if
  preference advanced_statistics_enabled is true (default false).
  Hooks.java:138-158: runFilter returns arg unchanged if hooks is null
  (:139-143), otherwise loops over the registered list and calls the
  interface method func.runFilter at :150.
- Verdict: the hand edge as a non_standard registry dispatch is CORRECT
  as a mechanism; a direct explicit Hooks.runFilter edge would be WRONG
  (presence in the built graph unconfirmed — graph_def.py unfetchable).
  Gate MG943 (STATE settings, preference must be true) is PROPOSED, not
  merged. Full launcher route UNCLEAR: upstream
  Statistics/ChartBuilder/launcher steps were not printed tonight.

## 4. Compat dispatch under API 27 — CONFIRMED for app code

- CompatHelper.java:55-57: getSdkVersion() returns Build.VERSION.SDK_INT.
  :35-36: >= 21 selects CompatV21. All other gates in the file are
  SDK_INT-based (:61-63, :65-67, :69-71, :124-136). No targetSdk reference
  in the printed file.
- Verdict: on an API 27 device, CompatV21 is selected regardless of
  target_sdk 23. Closed_by_api_level labels resting on this chain are
  unaffected by the target question. Framework targetSdk behaviour is a
  separate, still-open pre-tick check (decision B).

## Sample table

- Sample drawn: 0 (sampler not run — missing out/methods.csv).
- Correct / fixed / wrong / unclear for the WP2 sample: NOT COMPUTED.
- Error rate: NOT COMPUTED. No rate from the items above may be quoted
  as the WP2 rate.
