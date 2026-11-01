# AnkiDroid — Muse's own decisions (for user / Yang review)

These are decisions made by Muse in this session, in Muse's own name, never in
Yang's name. They are recorded here for review. Nothing in this file changes a
label in the branch graph: no merge, no push, and no graph edit was made tonight
(the branch graph could not be reconstructed locally; see STEP_LOG.md).

## Decision A — EasySSLSocketFactory.equals / hashCode

Decision, in two parts, applied to both methods together (they stand or fall
together: a manager that compares schemes invokes equals; one that hashes them
invokes hashCode):

1. The standing labels STAND tonight: both remain UNREACHABLE,
   kind no_trigger_in_app, confirmed_by INFERRED. No flip is made on the
   factory's own comment, on the shape of the overrides, or on any tool run.
   Printed source tonight: EasySSLSocketFactory.java:102-105 (comment: "some
   connection managers" need the overrides), equals :108-110 (body :109,
   class-equality only), hashCode :114-116 (body :115, constant class hash),
   sole printed construction HttpSyncer.java:228, registry handed to
   ThreadSafeClientConnManager :229, request executed via DefaultHttpClient
   :235-236. No printed app line calls equals or hashCode on the factory.
   The comment proves only that some managers need the overrides, not that
   this manager compares or hashes a scheme.
2. Reading Apache HttpClient 4.x source outside the dataset IS authorised,
   as a verification step before any merge or tick — limited to the
   Scheme / ThreadSafeClientConnManager / DefaultHttpClient path used at
   HttpSyncer.java:226-236. The read by itself flips nothing. Only a printed
   line showing a compare or hash of the scheme on that path flips both
   methods to REACHABLE with a route through HttpSyncer.req under an ENV
   network gate. Until that printed line exists, the INFERRED UNREACHABLE
   labels stand and the item stays open in conflicts.md.

Reasoning: keeping INFERRED labels while refusing to settle them by
inference is the honest position, but leaving a plausible library dispatch
permanently unverified is worse than a scoped outside read whose result is
itself printed and cited. The brief's "only AOSP downloads" rule is therefore
overridden here, narrowly, by this explicit decision — for review, not as a
general waiver.

## Decision B — Device API 27 vs manifest target 23

Decision: "device API 27, whatever the manifest target" is CONFIRMED for
every app-code version check, and is NOT blanket-confirmed for framework
behaviour that keys on targetSdk.

- Confirmed part (SOURCE, printed tonight): CompatHelper.java:55-57,
  getSdkVersion() returns Build.VERSION.SDK_INT (the device level, never a
  manifest value); :35-36 selects CompatV21 at >= 21, so on an API 27 device
  CompatV21 is selected regardless of target_sdk 23. Every other version gate
  in the printed CompatHelper file is likewise SDK_INT-based (:61-63, :65-67,
  :69-71, :124-136). All closed_by_api_level labels that rest on the
  CompatV21 chain (for example CompatV10 base bodies shadowed by overrides,
  per label_072) are therefore unaffected by the target-23 question, and no
  user decision is needed for Compat dispatch itself.
- Not confirmed part: framework behaviour that keys on targetSdk is a
  separate question from app code, and no framework line was printed tonight.
  The concrete target-sensitive surface to check before any tick, with no
  method named today because none was printed, is: (i) permission
  enforcement behind CardContentProvider (target 23 already selects the
  runtime-permission model, so no divergence is expected, but the fw_src
  print is still owed); (ii) file-URI exposure to other apps, which is
  exempt below target 24 — assuming target 27 would wrongly close such
  routes, so a target-27 assumption must never be used; (iii) any other
  target-keyed framework shim, none identified in printed source tonight.
  A full-checkout grep for targetSdk-sensitive framework calls is a
  pre-tick check, not a label change tonight.

## Decision C — Card.toString (libanki) stays UNREACHABLE, contradiction stays open

Decision: do NOT flip Card.toString on the APE hit, and do NOT close the
contradiction. Printed source tonight: Card.java:634-648 defines toString
(the only toString occurrence in that file is its own definition);
AdvancedStatistics.java:399-411 defines a separate inner Card with its own
toString; ReviewOutcome.card is of the inner type (:1475) and its toString
at :1497-1501 concatenates the inner card; Review.writeLog at :1714-1720
logs prevCard/newCard, which are inner-Card fields (:1549, :1555); and
AdvancedStatistics imports com.ichi2.libanki.Collection, Decks, Stats only
— no libanki Card import. Those sites therefore do not call libanki
Card.toString. Tool coverage is never evidence, in either direction. The
label stays UNREACHABLE, no_trigger_in_app, and the APE hit stays recorded
as unexplained by app source until a full-checkout grep prints a libanki
Card passed to an Object parameter (log call, collection of Objects, or
similar) on a reachable path. If such a line is printed, relabel REACHABLE
with that citation; otherwise keep UNREACHABLE with the grep output cited.

## Decision D — Hooks.runFilter gate (proposed, NOT merged)

Decision: the Stats.calculateDue(Context,AxisType) ->
AdvancedStatistics.runFilter edge is a non_standard registry dispatch
(mechanism CORRECT tonight: Stats.java:308-311 calls Hooks.runFilter with
key "advancedStatistics" and argument order metaInfo, type, context, _limit(),
matching AdvancedStatistics.runFilter's casts at AdvancedStatistics.java:141-146;
install registers the key at :147-149; Hooks.runFilter dispatches through the
interface at Hooks.java:138-158, line 150). A direct explicit
Hooks.runFilter -> AdvancedStatistics.runFilter edge, if one exists in the
built graph, would be WRONG and must be suppressed or reclassified at merge
time — its presence could not be confirmed tonight because graph_def.py is
unfetchable. The edge's missing gate is decided as a STATE settings gate
(MG943 in the prior note): "preference advanced_statistics_enabled must be
true (default false, Hooks.java:61-62); otherwise the hook is not registered
and Stats.java:331 fallback runs instead". The gate text must match the
STATE_KINDS_OF table in graph_def.py at merge time; that table could not be
read tonight, so the attachment is PROPOSED, not applied. The full route
from the launcher is UNCLEAR tonight (launcher entry and
Statistics/ChartBuilder upstream steps were not printed in this session).

## Decision E — No exact rebuild, no fabricated log

Decision: do NOT assemble a substitute graph_def.py from parts and do NOT
write a verification.csv, readme_notes final, or LESSONS final that pretends
a build or sampler ran. Parts total 1,056,495 bytes against graph_def.py's
1,173,446; the sup blocks for most parts and several orchestrator addenda
exist only inside graph_def.py, and auto_calls.json (8,146 of 9,178 edges in
the branch build report) is likewise unfetchable. An assembled file could
not reproduce branch build 205 counts and would be a fabrication if
presented as the branch graph. The honest artefacts tonight are: this file,
STEP_LOG.md, AGENT_NOTES.md, the attempted-runs output, a DRAFT readme_notes
(five headings, marked draft, not run through gen_readme_v2), and a
source-judging note for the items above. The gate is therefore BLOCKED, not
passed, and the proposed status line is held for the coordinator's report
only — it is not written to any PROGRESS file by this leaf.
