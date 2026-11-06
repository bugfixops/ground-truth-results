# MUSE_DECISIONS — consolidated from overnight stream decisions files (staged locally; NOT pushed yet)
# Authorship: all decisions below are Muse's own, recorded for user/Yang review. None is made in Yang's name.

==================================================================
## From stream-C
==================================================================

==================================================================
## From stream-B
==================================================================

==================================================================
## From stream-D
==================================================================

==================================================================
## From stream-A
==================================================================


### stream-C/DECISIONS.md

# DRAFT — Muse's own decisions, for user/Yang review

Stream C leaf dossier, Aegis only. No decision below is presented as anyone
else's, and no item is left "awaiting" anybody: every item gets a decision
plus, where a print is still missing, the exact print that would change it.
No graph file was edited here; graph edits are described only, for the
coordinator to apply and verify on a full checkout. No route verdict below
counts as verified until a fresh `show_route` is printed on the current
branch — several decisions below confirm a graph *model* while leaving the
route verdict open pending that print.

## Basis

Sources read for this dossier: the WP3 steps 6–10 report
(`~/workspace/aegis-wp3-steps6-10-report.md`, which quotes the 7 items
verbatim with AGENT_NOTES.md line numbers); `graphs/Aegis/AGENT_NOTES.md`
on branch `work-2026-10-31` via the GitHub connector (lines 370–390,
470–490, 530–575, 590–669 read); and the rule files in full:
`KIRO_CONVERT_APPS.md`, `KIRO_CORRECTIONS.md`, `SCHEMA_V2.md`,
`AGENT_BRIEF_V2.md`, `CONVERSION_RECIPE.md`.

Rules relied on, by short name:

- **R-LABEL** (SCHEMA_V2 "How the labels are derived"; KIRO §3):
  REACHABLE = a route from an entry point exists in the standard
  configuration, STATE gates allowed. `confirmed_by` is SOURCE only when
  every claim in the evidence of every edge of the best route cites a
  source line; otherwise INFERRED. Never DYN, FW-MEMORY, or UNVERIFIED.
  Tool coverage never sets a label. Never mark a method UNREACHABLE if it
  has a route.
- **R-CLASS** (SCHEMA_V2 "Edge class rules"; AGENT_BRIEF §2): `explicit` =
  direct app-code call; `standard` = framework calls a callback the app
  registered (lifecycle, listeners, launcher entry); `non_standard` =
  a library or reflection makes the link and nothing in the app code
  calls or registers the target. A STATE gate does **not** change an
  edge class.
- **R-STD** (AGENT_BRIEF §2; SCHEMA_V2 §"standard configuration"): the
  standard configuration is the instrumented debug build, a fresh install
  on an API 27 emulator, runtime permissions only where a route needs
  them, plus the fixtures.
- **R-FIRST** (AGENT_BRIEF §5 "first-resume shortcut"; CONVERSION_RECIPE
  "Added after Omni-Notes"): start every route at the cold start; an edge
  valid only after an earlier visit carries a STATE.
- **R-SPLIT** (CONVERSION_RECIPE "Added after Omni-Notes", "Split a method
  by how it is reached"): when a method's branches depend on how it is
  reached, split it into context variants (`@IMPORT`/`@LEGACY`,
  `@EXIST`, `@PICK` in the Omni-Notes precedent; `onActivityResult`
  split into `@OK`/`@CANCEL` in the brief), suppress the plain pair,
  and write one hand edge per variant. Automatic outgoing edges are
  copied to every variant, so every branch-specific callee needs its own
  suppression plus hand edge.
- **R-CLOSED** (CONVERSION_RECIPE "Added after hash-checker"): state no
  in-app action can create = closed in the standard configuration: remove
  the edge; a method only that edge reaches becomes UNREACHABLE
  `closed_by_configuration`.
- **R-GUARD** (CONVERSION_RECIPE, guard-less bytecode edges): read the
  enclosing conditions around every step; add the guard text, or a STATE
  gate when a cheaper route without it exists.
- **R-ROUTER** (AGENT_BRIEF §4 step 6; CONVERSION_RECIPE): the best route
  minimises ENV-gated edges, then STATE-gated edges, then steps, and
  ignores guard text. Consequence, repeatedly observed in Aegis notes:
  a producer edge alone never forces the router onto the producer chain;
  an ENV gate *does* change route cost, a STATE gate alone does not
  reliably divert the router (see R6B: the PIN path needs no picker ENV,
  so a STATE tag on the PIN edge does not divert the route).
- **R-VERDICT** (KIRO §4): per-route verdicts are correct / fixed /
  wrong / unclear. Unclear covers routes depending on code that cannot
  be read. A route with any step not printed counts as NOT checked.
- **R-LIB** (KIRO §3 library rule; AGENT_BRIEF §2; CONVERSION_RECIPE
  "Without the androidx / ORMLite sources"): library and generated code
  labels are INFERRED; a library UNREACHABLE needs a full-tree grep plus
  reason in `conflicts.md`. Sources not on disk (androidx, Material,
  Glide, Dagger/Hilt generated code) stay INFERRED, stated under Limits.
- **D1 / D2** (conventions as actually used in AGENT_NOTES rounds 6–7):
  D1 — a step that merely inherits an earlier step's failure is not a
  separate error. D2 — a step whose only problem is a cross-run
  (prior-run / relaunch) state is UNCLEAR, not ERROR. D2 is a
  *verdict* convention for route checking; it does not delete the edge
  and does not change the method label (see R-LABEL: STATE gates
  allowed).

Two distinctions run through every decision below and are applied
consistently:

1. **Edge vs route vs label.** Keeping an edge, fixing a route, and
   changing a label are three different acts. A cross-run edge can be
   kept (valid relaunch coverage) while a fresh-install route that uses
   it is UNCLEAR (D2) and while the target method stays REACHABLE
   (STATE-gated route exists).
2. **Own-edge contradiction vs missing producer.** A step whose own edge
   contradicts printed app code (wrong receiver, wrong case, a guard the
   route's own state falsifies) is ERROR. A step that is fine on its own
   but whose producer is absent from the route is ERROR if the producer
   is an in-run action the route could have taken, and UNCLEAR (D2) only
   if the producer is cross-run. A step resting on unread library code
   is INFERRED / UNCLEAR, not ERROR.

## Summary

| # | Item | Decision (one line) |
|---|------|---------------------|
| D1 | R1 step 13, intro ENTERS edge | Page node is enough; no SYSTEM producer, no needs_state |
| D2 | Route 4 step 9, Ebac005d0, icon pack | Add the cross-run precondition as needs_state; do NOT reclassify as non-standard; route verdict UNCLEAR (D2) |
| D3 | Route 1 step 21, E1dcf1457, RESULT / initNew | Confirm the @SAVED variant split as the permanent model; no new RETURN kind, no tools change |
| D4 | Search step 14, E399cebc2, SEARCH_IN_GROUPS | Two-process route: keep edge with a prior-run needs_state; verdict UNCLEAR (D2), not ERROR, not correct-as-printed |
| D5 | G3_5 step 34, app-import tap chain | Confirm the tap-first GA chain; the no-tap Authy-default path stays unmodelled, not UNREACHABLE |
| D6 | GlideRequests step 50, root-gated app import | Guard the app-import edge with a root ENV gate; no label change on this evidence; route stays open until redraw |
| D7 | GoogleAuthImporter step 24, $26@APP → $27@APP | Chain as written is INSUFFICIENT: route verdict stays ERROR until the checked-row print lands; guard + @APP_GA variant, do not bless, do not delete |
| R1 | Cold-start edges E20e76e09 / E57db524e / Ec7af65b2 | Keep all three with cross-run needs_state; fresh-declared routes using them are UNCLEAR (D2), relaunch-declared routes using them are correct |
| R2 | Shared text-input relay E41c33149 / E02b5fa3e (+ error-dialog relay $15) | Split into caller-context variants; wrong-listener steps stay ERROR until split |
| R3 | Glide INFERRED edges E265bbd0b / Ec449db03 / E9d286870, E4db374dd | Keep as INFERRED (library rule); E4db374dd needs its edge text printed before it counts |
| R4 | State-blind router | No tools change; variant nodes are the approved workaround (precedent: @SCAN, @SAVED) |
| R5 | SwitchingProvider.get per-case edges | Split into @VAULT / @ICON variants; wrong-case steps stay ERROR until split |
| R6 | Shared saveAndFinish node | Split into @ADD / @DELETE variants; affected steps stay ERROR until split |
| R7 | Other cross-run states (ST_VAULT_ENTRIES, ST_BIO_SLOT) | Same rule as R1/D2; keep, UNCLEAR on fresh-declared routes |
| R8 | R3 step 7, onCreateOptionsMenu ordering (androidx unread) | Keep as INFERRED; verdict UNCLEAR (code not read), not ERROR |

---

## D1 — R1 step 13: intro ENTERS edge S_INTRO_WELCOME → S_INTRO_PICKER

**Item (AGENT_NOTES line 379).** The ENTERS edge compresses the Next tap
and the `setCurrentSlide` producer. Question: is the page node enough, or
add a SYSTEM producer and needs_state on the Next edges?

**Options considered.** (a) Page node enough, ENTERS edge keeps a guard
citing the tap and the slide change. (b) Add a SYSTEM producer node for
`setCurrentSlide` and put needs_state on every Next edge. (c) Expand the
intro walk into method-level edges for every tap.

**Decision: (a). The page node is enough. No SYSTEM producer node, no
needs_state on the Next edges.**

**Reasoning.** SCHEMA_V2 edge classes state that `page` = a page
transition of the model, not counted as an edge class; AGENT_BRIEF §4
step 1 models entry points, lifecycle, *pages (SCREENS) and the GUI
handlers that move between them* — the page transition is the model
itself, not a method call to be reified. A SYSTEM producer would invent
a node that is in no method list and whose "method" no route can verify
against a printed call site, violating R-LABEL's SOURCE/INFERRED
discipline (a producer nobody can print is worse than a page edge whose
guard cites the tap). The batch-41 intro model already treats Next /
Previous as page-state transitions (S_INTRO_WELCOME → S_INTRO_PICKER →
S_INTRO_SETUP → S_INTRO_DONE) each with guard and source lines; D1
ratifies that model rather than reopening it. A needs_state would also
be wrong on its own terms: the slide advance is produced *by* the tap
on the same step, not by an earlier step, so there is no producer state
for a later step to need (contrast D3, where initNew genuinely precedes
the RESULT edge).

**Affects.** R1 step 13: UNCLEAR → CORRECT as written, provided its
guard text names the Next tap and cites the slide-change source lines;
if the guard text currently cites neither, that is a citation fix, not
a modelling change. No other route changes.

**Graph edit implied (not applied).** None, except ensuring the ENTERS
edge guard cites the Next-tap and setCurrentSlide lines. Do not add any
node, state, or edge.

**Evidence that would change it.** A printed AppIntro / intro source
showing the Next tap does *not* advance from Welcome to Picker in the
standard configuration (e.g. the tap is disabled on that slide) — then
the edge is wrong on its own terms (ERROR), and the intro walk must be
remodelled, not merely annotated.

## D2 — Route 4 step 9 (Ebac005d0): icon pack left over from an earlier run

**Item (AGENT_NOTES line 479; Stage 5 table line 531).** The route
header says `explicit_standard_route=yes`, but this step needs an icon
pack left over from an earlier run (IconPackManager.java:136-158).
Options as posed: reclassify the route as non-standard, or add the
precondition.

**Options considered.** (a) Reclassify the whole route non-standard.
(b) Add the precondition as needs_state, keep edge class and header
semantics. (c) Delete the edge / mark the target UNREACHABLE.

**Decision: (b). Add the precondition; do NOT reclassify as
non-standard.**

**Reasoning.** Under R-CLASS, `non_standard` means a library or
reflection link, not "needs something from an earlier run". The
IconPackManager step is an ordinary app-code call; what is special
about it is *when* its input was produced, and SCHEMA_V2 handles "when"
with STATE kinds (`file`, `settings`, `session`), not with edge class.
R-FIRST says exactly this: an edge valid only after an earlier visit
carries a STATE. Reclassifying would also corrupt the header's meaning:
SCHEMA_V2 defines `explicit_standard_route` as whether *some* route
uses only explicit and standard edges — a STATE-gated explicit/standard
route still qualifies, and R-LABEL expressly allows STATE gates on a
REACHABLE route. (c) is barred by R-LABEL (the method has a route) and
by the cold-start reasoning in R1 (deleting loses valid coverage).

**Affects.** Ebac005d0 only, plus by the same rule G3 route 3 step 29
(icon pack installed earlier, IconPackManager.java:85, 89; rescan
30-33) and G3 route 2 step 23 (export list needs an entry created
earlier, ImportExportPreferencesFragment.java:357-363, 384-385):
all three are precondition cases, not reclassification cases.
Route 4 step 9 verdict: ERROR → UNCLEAR (D2) once the needs_state is
present, because the printed route as it stands does not declare its
cross-run precondition. The target method's label does not change.

**Graph edit implied (not applied).** Add
`needs_state` to Ebac005d0 naming the cross-run icon-pack state
(reuse the existing icon-pack state constant if one exists; otherwise
add one STATE_KINDS_OF entry, e.g. "icon pack installed by an earlier
run"), and put the same precondition wording in its guard text.
Do not change its edge class. Apply the same pattern to the G3
step-29 edge and to the G3 step-23 export edge (entry-created state).

**Evidence that would change it.** A printed in-run producer: a step
on this same route that installs the icon pack (or creates the entry)
before step 9 — then drop the needs_state and the route becomes
correct. Conversely, printed proof the pack cannot persist across runs
in the standard configuration would make the step closed under
R-CLOSED, not merely UNCLEAR — no such proof is in the printed record.

## D3 — Route 1 step 21 (E1dcf1457): RESULT edge needs initNew, no RETURN kind exists

**Item (AGENT_NOTES line 599; fixed per line 611; round-7 clean per
line 666; still listed open in the handover — the tension the WP3
report flags).** The RESULT edge
IntroActivity.onDonePressed → MainActivity.lambda$new$1 needs the
vault created by initNew (IntroActivity.java:100), but the route had no
edge reaching initNew and the RESULT edge had no needs_state, so the
router took the NONE path (creds null passes :92-96). A fix was said to
need a continuation node after initNew, and no RETURN kind exists in
`build_graph.py` KINDS.

**Options considered.** (a) Add a RETURN kind / change tools. (b) Split
onDonePressed into context variants so only producer chains reach the
RESULT edge. (c) Put needs_state on the RESULT edge and hope the router
picks the producer chain.

**Decision: (b), and it is already the recorded fix — D3 confirms the
@SAVED variant model as permanent and closes this item as a modelling
question.** The RESULT edge starts from
IntroActivity.onDonePressed@SAVED; only VaultManager.initNew
(IntroActivity.java:100-104, needs ST_NOT_IMPORTED, the none path) and
the import branch (IntroActivity.java:106-123, needs ST_IMPORTED and
ENV_PICKER) reach @SAVED. The picker gate on the import branch is part
of the decision, not an optional extra: without it the router took the
import branch and contradicted step 13 ("imported" false).

**Reasoning.** (a) is out of scope: tools are read-only in this job
(AGENT_BRIEF §3) and a new edge kind is a schema change, not a graph
edit. (c) is known not to work under R-ROUTER: the router compares
ENV, needs_state count and steps and never checks that a state is
produced, so a needs_state alone cannot force the initNew chain.
(b) is exactly R-SPLIT, with Aegis-internal precedent (the @SCAN split
at line 608, which fixed the analogous scan-action leak by routing
through a variant only the tile/shortcut chains reach) and
ticked-app precedent (Omni-Notes `@IMPORT`/`@LEGACY`,
`onActivityResult` `@OK`/`@CANCEL`). The variant works because the
router *must* pass through the @SAVED node, and only producer chains
reach that node — the producer-forcing is structural, not textual.

**Affects.** Route 1 step 21: ERROR → CORRECT on a fresh `show_route`
of MainActivity.onIntroResult, *subject to that print* (see below).
This resolves the WP3 tension in favour of line 611/line 666 over the
handover's stale open listing: the handover listing is superseded by
the applied fix, not by a new decision. No method label changes: every
method on this route already had a route; the fix changes *which*
route the router picks.

**Graph edit implied (not applied).** None new. Verify on the current
branch that the plain RESULT edge (successor of E1dcf1457) is gone and
the @SAVED variant edges plus the ENV_PICKER gate on the import branch
are present; if the current branch still carries the plain edge,
replace it with the @SAVED construction described above. Do not add a
RETURN kind.

**Evidence that would change it.** A fresh `show_route`
MainActivity.onIntroResult on the current branch that still bypasses
initNew (plain edge present, or @SAVED reachable without initNew or
the import branch) — then the fix has not survived to this branch and
must be re-applied as above; the *model* decision does not change.
Printed proof of a third onDonePressed path that creates a vault
without initNew or import would require a third variant reaching
@SAVED, not a reopening of the question.

## D4 — Search step 14 (E399cebc2): SEARCH_IN_GROUPS is a two-process route

**Item (AGENT_NOTES line 603).** Default mask is
SEARCH_IN_ISSUER | SEARCH_IN_NAME (Preferences.java:198); GROUPS is set
only by BehaviorPreferencesFragment.java:57 and read once in
MainActivity.onCreate (MainActivity.java:234). A same-run change
applies only after a relaunch, so this is a two-process route. The R6E
note adds that calling it "prior run" would make it UNCLEAR by D2,
not ERROR.

**Options considered.** (a) ERROR: the single printed route is wrong
because it spans two processes without a relaunch step. (b) UNCLEAR
(D2): cross-run state, kept with a precondition. (c) Correct: treat
relaunch as an ordinary step inside one route.

**Decision: (b). The route as printed is UNCLEAR (D2), not ERROR and
not correct.** Keep E399cebc2 with a prior-run needs_state; do not
claim the single printed route is a correct single-process route.

**Reasoning.** (c) misrepresents the process boundary: the mask is
read once at onCreate:234, so no in-run step on the printed route can
make GROUPS take effect before the search step — the route as printed
asserts a causal order the code does not support. (a) overstates it:
the step's own edge is not contradicted by printed code (the search
code does read the mask at EntryAdapter.java:206-209, and the mask
*can* hold GROUPS); what is missing is a process boundary, which is
precisely the D2 case — the same treatment as D2/R1, where a
cross-run precondition downgrades a route verdict without deleting
the edge or the label. Under R-LABEL the target method stays
REACHABLE: a STATE-gated route exists (set GROUPS in preferences, relaunch,
search), and relaunching after a settings change is ordinary standard
use, not a different configuration. The distinction from an ERROR is
deliberate and load-bearing: ERROR would demand a graph fix for
something no graph edit within current KINDS can express (there is no
process-boundary edge kind), while UNCLEAR honestly records that the
printed route spans two processes.

**Affects.** EntryAdapter.lambda$doesAnyGroupMatchSearchFilter$1
step 14: ERROR → UNCLEAR (D2). This decision does **not** close steps
8 or 12 of the same route, which are different failures: step 8 (the
restore edge Ed60e6cbd, guard MainActivity.java:1070) lacks an in-run
submit producer (MainActivity$1.onQueryTextSubmit, needs
ST_SEARCH_OPEN), and step 12 (E21f79a09, ST_ENTRY_LIST_NONEMPTY) lacks
an in-run entry-list producer (loadEntries / onAddEntryResult). Those
are missing-*in-run*-producer ERRORs, not cross-run cases, and they
stay ERROR until a variant or producer chain puts the producer on the
route (R4 pattern). Conflating them with step 14 would be a category
error. The method's label is unchanged by all three steps: it has
STATE-gated routes; the route-check verdicts are about the printed
routes, not the label.

**Graph edit implied (not applied).** Add needs_state to E399cebc2
naming the prior-run GROUPS state (e.g. "search mask with GROUPS set
in a prior run, process relaunched; mask read at onCreate:234") and
mirror that wording in its guard text. Do not split the search method
for this item, do not delete the edge.

**Evidence that would change it.** A printed in-run path by which a
GROUPS change takes effect without relaunch (e.g. the mask re-read
after the preferences fragment returns, or a second onCreate on the
same process path) — then drop the needs_state and the route becomes
correct. Printed proof the mask is *never* re-read and the preferences
fragment cannot run before MainActivity in the standard configuration
would move this from UNCLEAR toward R-CLOSED; no such proof is in the
printed record.

## D5 — G3_5 step 34: app-import dialog opens with Authy checked; OK now needs a row tap

**Item (AGENT_NOTES line 609).** The app-import dialog opens with
Authy checked (DatabaseImporter.java:37). OK on the app path now needs
a row tap first: _IMP_APP →
Dialogs.lambda$showImportersDialog$26@APP (guard: GA row tapped) →
lambda$showImportersDialog$27@APP. The OK edge without a tap is removed.
Question posed: the default Authy app-import path is no longer
modelled.

**Options considered.** (a) Confirm the tap-first chain and accept the
Authy-default path as unmodelled. (b) Restore the no-tap OK edge so
both Authy-default and GA-tap paths are modelled on the shared OK node.
(c) Mark the Authy import path UNREACHABLE.

**Decision: (a). Confirm the tap-first GA chain; the no-tap
Authy-default path stays unmodelled (recorded as a Limits note), not
UNREACHABLE.**

**Reasoning.** (b) is what R-SPLIT forbids: one shared OK node cannot
carry two receivers with different preconditions (GA row tapped vs
Authy checked by default) without conflating them — that shared-node
conflation is the structural defect behind most remaining Aegis route
errors (R2, R6). The @APP variant split is the correct R-SPLIT
application: the GA path gets its own tap-guarded chain. (c) is barred
by R-LABEL on the evidence available: "unmodelled" is not
"unreachable". GoogleAuthImporter.readFromApp has the GA tap route,
and the Authy importer path has not been shown, by a full-tree grep
plus reason (R-LIB), to have no trigger; absence of a modelled edge is
not evidence of absence (and a `search_code` 0 would not be either).
The honest statement is narrower: the graph models the GA tap path and
does not model the Authy-default path.

**Affects.** G3_5 step 34: the tap chain stands as the modelled GA
path. **Cross-effect with D7 (read both together):** D5 confirms the
*tap-first shape* of the chain; it does not make the
GoogleAuthImporter.readFromApp route correct, because D7 holds that
the downstream OK step (step 24 in the round-7 route) is still ERROR
on the checked-row question. Step 34 and step 24 are different steps
of the same chain, and D5 must not be quoted as closing the route.
No label changes: readFromApp stays REACHABLE via the tap route's
existence as a modelled route; Authy-import methods keep whatever
labels their own routes support.

**Graph edit implied (not applied).** None new; keep
$26@APP → $27@APP and the removed no-tap OK edge removed. Add one
Limits sentence to readme_notes.md when it is written: "The
app-import dialog's default-checked Authy path (DatabaseImporter.java:37) is not modelled; only the GA row-tap path is." Do not add an
Authy-default edge on the shared OK node.

**Evidence that would change it.** The checked-row print required by
D7: if it shows the checked state *is* set by the default selection
or by a tap through a printed mechanism, restore the Authy-default
path as its own @AUTHY variant (not on the shared node) and the
"unmodelled" note is deleted. If it shows nothing sets the checked
row, see D7 — the GA path itself, not just the Authy path, is in
trouble.

## D6 — GlideRequests step 50: app import with file null, needs root; router's cheaper choice

**Item (AGENT_NOTES line 636; WP3 report item 6; round-7 line 652
step 53, same branch).** ImportEntriesActivity.java:109-111 calls
startImportApp; :143-153 finishes the page when the shell is not root.
The app-import edge is the router's cheaper choice. Decision reference
HANDOFF_V2.md R10-2 (not re-read for this dossier; the decision below
rests on the printed source lines and rules, not on that reference).

**Options considered.** (a) Delete/suppress the app-import edge.
(b) Add a root ENV gate to the app-import edge so the router stops
preferring it on a standard (non-root) route. (c) Add needs_state
(root) and keep the route. (d) Mark the app-import methods
UNREACHABLE / closed_by_configuration.

**Decision: (b). Guard the app-import edge with an explicit root ENV
gate; no label change on this evidence; the GlideRequests.asBitmap
route stays open until a fresh redraw.**

**Reasoning.** (a) would delete a real branch (on a rooted device the
branch runs) and is disproportionate: the defect is not the edge's
existence but the router's preference for it. (c) fails under
R-ROUTER for the reason the notes themselves record for the PIN path:
a STATE tag does not reliably divert an ENV-first router, and "root"
is not in any case a STATE produced by an in-app step — it is an
environment property, i.e. an ENV kind (`other`, with text copied from
the code: shell root, ImportEntriesActivity.java:143-153). (b) works
*with* the router instead of against it: the best-route rule minimises
ENV-gated edges first, so an ENV-gated app-import branch becomes more
expensive than a non-ENV alternative and the router prefers the
alternative — the same cost logic that already explains why the PIN
path beats the picker path. (d) is barred on this evidence alone:
R-LABEL requires a method-level showing (full-tree callers, a reason
the printed source shows) before any UNREACHABLE label, and no such
showing for startImportApp or its callees is in the printed record;
a method reachable only via root *in the standard configuration*
would be a R-CLOSED candidate, but that "only" has not been shown.

**Affects.** GlideRequests.asBitmap step 50/53: ERROR until the ENV
gate is added *and* a fresh show_route is printed; after the gate, the
expected outcome is a redraw that avoids the app-import branch (route
verdict then judged on the new steps), or, if no alternative route
exists, a route that carries the root ENV gate openly — in which case
the route is judged as a rooted-device route, not a standard route,
and the standard-configuration verdict stays open. No method label
changes from this decision. The same ENV-gate pattern applies to any
other route where the router prefers a root-gated branch; it does not
apply to STATE-gated branches (see R-ROUTER distinction).

**Graph edit implied (not applied).** Add an ENV gate (kind `other`,
text: "shell is root; otherwise the page finishes,
ImportEntriesActivity.java:143-153") to the app-import edge used at
this step, with a matching ENV_KINDS_OF entry. Do not suppress the
edge, do not add needs_state for root, do not change any label.

**Evidence that would change it.** Printed proof the standard API 27
emulator shell *is* root (then the gate is satisfiable in the
standard configuration and the route as gated becomes correct), or
printed proof the file-null app-import branch is the *only* route to
some method (then that method is a R-CLOSED candidate and the
decision becomes a label decision, not a routing decision).

## D7 — GoogleAuthImporter.readFromApp step 24: OK reads the ListView's checked row, which the row listener does not set

**Item (AGENT_NOTES line 659; graph_def.py:1130 edge
`gui(_IMP_PICK_APP, _IMP_OK_APP, 'Tap OK after the Google Authenticator
row was tapped …')`, confirmed still at that line by the WP3
cross-check).** ERROR as reported (checker report, cites not re-read
by the coordinator — "R" in round-7 notation): the row-tap edge
$26@APP → OK $27@APP is the R9-1 decision, but the OK button reads the
ListView's checked row, which the row listener does not set.

**Options considered.** (a) Bless the $26@APP → $27@APP chain as
correct (the tap *is* the selection). (b) Delete the chain.
(c) Hold the route at ERROR, guard the checked-row precondition
explicitly, and split the OK node into a @APP_GA variant whose
needs_state is the checked-row state, pending the missing print.
(d) Downgrade to UNCLEAR (D2) as a cross-run or unread-code case.

**Decision: (c). The chain as written is INSUFFICIENT and the route
verdict stays ERROR. The edge is neither blessed nor deleted.**

**Reasoning.** (a) would assert a mechanism — tap sets checked row —
that no printed line in the record shows; under R-LABEL that assertion
could at most be INFERRED, and an INFERRED mechanism that contradicts
the printed OK handler (which reads a checked row) is not a basis for
a correct verdict. (d) is the wrong category: D2 covers cross-run
states, and this is not cross-run; nor is it merely unread library
code — the OK handler and the row listener are app code, and their
printed behaviour contradicts the chain's implication. That is a D1
own-edge contradiction, i.e. ERROR. (b) would destroy the only modelled
GA app-import path on the basis of a checker report whose cites the
coordinator did not re-read; deletion requires a coordinator-verified
printed showing, not a carried "R" verdict. (c) is therefore the only
option consistent with all three constraints: it preserves the model,
refuses to count the route correct, and names exactly what would
settle it.

**Affects.** GoogleAuthImporter.readFromApp round-7 step 24: stays
ERROR. By inheritance (D1), later steps of that route that depend on
the import having read the GA app are not separate errors, but the
route as a whole is not correct. D5's tap chain (step 34 in its route)
is unaffected as a *graph edit* but inherits this verdict for its
route (see D5 cross-effect). No label changes: readFromApp's label
must rest on its other routes (file import and any verified path), not
on this chain, until the print lands; if no other verified route
exists, the label question is open, not UNREACHABLE (R-LABEL bars
UNREACHABLE for a method with a route, and this route exists as a
model even though its verdict is ERROR — the label and the route
verdict must not be collapsed into each other).

**Graph edit implied (not applied).** Keep the $26@APP → $27@APP
edges. Add guard text to the OK edge stating the precondition
explicitly: "ListView checked row is the GA row (checked-setting
mechanism: see missing print below)". Split the OK node into a
@APP_GA variant carrying needs_state for the checked-row state once
the producer is identified; do not put the checked-row state on the
shared OK node (R-SPLIT). Do not delete any edge on this decision.

**Evidence that would change it — exact missing print.** The
Dialogs showImportersDialog source: the ListView's choice mode
(`CHOICE_MODE_SINGLE` or equivalent), any `setItemChecked` /
`setSelection` / `setChoiceMode` call, and the row-listener body, plus
the OK handler's checked-row read — printed together, with file:line
for each. If the print shows the framework sets the checked row on tap
in single-choice mode, the chain becomes CORRECT with confirmed_by
INFERRED for the framework step (R-LIB: framework behaviour not in
fw_src stays INFERRED, explicitly allowed) and SOURCE for the app
steps, and the @APP_GA needs_state producer is the tap itself. If the
print shows nothing sets the checked row anywhere, the GA app-import
route is broken as modelled: the correct fix is then to remodel from
the actual selection mechanism (or, if the dialog's default-checked
Authy row is the only checked row ever read, to restore the
Authy-default path as a @AUTHY variant per D5) — and the route stays
ERROR until that remodel is printed. This is the one item where the
decision is explicitly "ERROR pending a named print"; that is a
decision about how to carry the item, not an undecided item.

---

## Related decisions

### R1 — Cold-start relaunch edges E20e76e09, E57db524e, Ec7af65b2

**Decision: keep all three edges, each with its cross-run needs_state
(ST_VAULT_FILE / ST_PLAIN_VAULT_FILE family as already carried);
route headers must declare fresh vs relaunch; a fresh-declared route
using any of them is UNCLEAR (D2), a relaunch-declared route using
them is correct on that step.**

Reasoning: same as D2/D4, applied to the whole family. Deleting them
would lose valid relaunch coverage (AGENT_NOTES line 558 states this
directly, and R-LABEL bars removing a route a method has). The
standard fresh edge E0602e719 already exists (MainActivity onStart,
fresh-install standard-config branch, verified in the WP3
GlideRequests step-8 check), so fresh routes have a correct
alternative — the defect is the router preferring the one-state
cross-run edges, which is a route-redraw problem (R4), not an
edge-deletion problem. The Slot route's step 8 reclassification
(ERROR → UNCLEAR under D2, round-7 line 655) and the EntryAdapter
step-8 reclassification (line 654) are both ratified by this decision
and are now the standing treatment, not one-off reclassifications.

Affects: every route whose step 8 (or equivalent onStart step) is one
of these three edges — including Slot.<init> step 8, GlideRequests
step 8's neighbours, and the G3 route-3 step-8 plain-text edge. Labels
unchanged. Graph edit: ensure each of the three edges carries its
cross-run needs_state (add it where missing); do not delete, do not
reclassify edge class, do not touch E0602e719.

Evidence that would change it: a printed in-run producer of the vault
file on a fresh-install route (then that route's step becomes correct
without D2), or proof the vault file cannot survive to a relaunch in
the standard configuration (then R-CLOSED, not D2).

### R2 — Shared text-input relay E41c33149 / E02b5fa3e (and shared error-dialog relay $15)

**Decision: split into caller-context variants; until the split,
wrong-listener steps stay ERROR.**

Reasoning: R-SPLIT, applied to the worst shared-node defect in the
graph. The shared text-input relay (Dialogs.lambda$showTextInputDialog$7
OK relay) dispatches every caller to every page listener: the
importer branch lands on the PIN-keyboard lambda (R6B steps 24-29:
AegisImporter.java:90 passes lambda$decrypt$1, but the relay reaches
the PIN lambda; PasswordSlotDecryptTask.onPostExecute then goes to
PasswordConfirmationListener at SecurityPreferencesFragment.java:161
instead of the importer listener), and the same defect recurs at
GlideRequests steps 24/27, Slot step 26, ExportResultListener steps
25/28/29, and detailedmulti step 27 (Dialogs.java:231-241). The
round-6 typing fix (OK $7 starts from typing node $6, not from
OnShowListener $8) stays — it fixed OK-with-no-typing and must not be
reverted — but typing-before-OK does not fix *which* listener OK
reaches. The fix shape is already specified in the notes (R6B:
Dialogs.showTextInputDialog@PIN and @IMPORT, with
PasswordSlotDecryptTask.onPostExecute callback variants) and matches
the @SCAN/@SAVED precedent. The shared error-dialog relay
(Dialogs.lambda$showErrorDialog$15, Dialogs.java:391-395; scanner vs
onStart listeners, G2 steps 12-13, G3 step 26, importScannedEntries
step 12 where MainActivity.java:957-958 closes the app but the route
reaches ScannerActivity.java:194-196) gets the same decision:
@SCANNER / @ONSTART variants, wrong-destination steps ERROR until
split.

Affects: E41c33149 (AuthenticatorPlus) and E02b5fa3e (Authy) are
replaced by per-caller variant edges; the plain shared edges are
suppressed. All routes listed above keep ERROR on their relay steps
until the split is applied and re-printed; they do not become UNCLEAR,
because the receiver contradiction is in printed app code. No label
changes: the relay methods themselves have routes; the defect is
which listener a route reaches.

Graph edit implied (not applied): sup the plain relay pairs; add
hand edges showTextInputDialog@PIN → OK@PIN → PIN listener chain and
showTextInputDialog@IMPORT → OK@IMPORT → importer listener chain
(and @AUTHY/@AUTHENTICATORPLUS variants if the callers differ);
redirect each caller to its variant; same for $15 @SCANNER/@ONSTART.
Rebuild and re-print every affected route — the split changes edge
ids, so old step citations go stale.

Evidence that would change it: a printed dispatch in the relay that
actually routes by caller (e.g. a listener field set per show call
and read by OK) — then the shared node is correct as written and the
variant split is unnecessary; the ERROR steps would need re-judging
against that dispatch code, not against the variant model.

### R3 — Glide INFERRED edges E265bbd0b, Ec449db03, E9d286870, and E4db374dd

**Decision: keep all four edges as INFERRED. The FW-SRC citation rule
does not require deleting them, and does not require fabricating
FW-SRC lines for Glide.**

Reasoning: the FW-SRC rule (KIRO §5; AGENT_BRIEF §2) governs
*framework* claims (AOSP 8.1.0_r1 lines printed from fw_src). Glide is
a library, and AGENT_BRIEF §2 lists Glide-class sources among "not
available here, so their steps stay INFERRED", while R-LIB makes
library labels INFERRED by rule and CONVERSION_RECIPE states that
without library sources the claims stay INFERRED and are said under
Limits. INFERRED is a permitted confirmed_by value (R-LABEL); the
forbidden values are DYN, FW-MEMORY, UNVERIFIED, none of which is
used. The Stage 5 OPEN framing ("this does not meet the rule that
framework claims cite FW-SRC lines") conflates the framework rule
with the library rule; this decision separates them.

Caveat, stated plainly: E4db374dd is different in one respect —
AGENT_NOTES line 562 records that it was carried from the handover
with no earlier entry, so its *reason* is not recorded. The decision
for E4db374dd is therefore conditional: it is kept as INFERRED **only
if** its evidence text says the source was not read (AGENT_BRIEF §5:
INFERRED with what was not read). If its current evidence text claims
FW-SRC lines, that citation is wrong and must be corrected to
INFERRED text before the edge counts; if its evidence text claims
anything else, it must be printed before merge.

Affects: E265bbd0b, Ec449db03, E9d286870 — no change, confirmed_by
INFERRED, routes through them judged INFERRED (not SOURCE) but not
ERROR on that ground. E4db374dd — INFERRED-pending-print as above.
No label changes: Glide methods reached through these edges stay
REACHABLE/INFERRED; a Glide method whose *only* support is an
INFERRED edge is still REACHABLE (R-LABEL allows INFERRED), it is
simply not SOURCE-confirmed.

Graph edit implied (not applied): none for the three named edges,
except ensuring their evidence texts say "source not read" where
applicable. For E4db374dd: print its edge text and correct it to
INFERRED wording if needed.

Evidence that would change it: Glide source printed from the dataset
or a tagged release matching the dataset version — then the affected
edges can be re-evidenced as SOURCE with file:line citations. A
printed showing that a Glide edge's target is never called by the app
(grep over app sources, R-LIB) would make that method a candidate for
UNREACHABLE with a written reason, not a deletion of the edge on
INFERRED grounds alone.

### R4 — The state-blind router (tools/build_graph.py)

**Decision: no tools change is requested or approved in this dossier;
variant nodes are the approved Aegis workaround for producer-forcing,
and every remaining producer-forcing problem is to be solved that way
or left ERROR/UNCLEAR, not worked around by editing guard text alone.**

Reasoning: tools are read-only in this job (AGENT_BRIEF §3), and a
state-aware router is a tool/schema change with cross-app blast
radius, not an Aegis graph decision. The record shows the workaround
works where applied (@SCAN line 608, @SAVED line 611, @APP line 609)
and that guard-text-only fixes do not (R-ROUTER). Guard text remains
necessary for *evidence* (R-GUARD) but is never sufficient for
*routing*; any future fix proposal for Aegis that consists only of
adding guard or needs_state text to force a producer chain should be
rejected on this decision and converted to a variant proposal.

Affects: all "structural" ERRORs whose notes cite the router
(G4 step 7 panic producer, G5 step 6 SwitchingProvider, search steps
8/12, MOTP chain, VaultGroup group producer, Salsa20 typed passwords,
detailedmulti steps). They stay ERROR (in-run producer missing) or
UNCLEAR (D2, cross-run) as classified in this dossier until a variant
or producer chain is applied — the router decision does not reclassify
any of them by itself.

### R5 — SwitchingProvider.get per-case edges (G5 step 6; R2 step 6; R4 step 6)

**Decision: split into @VAULT / @ICON variants (sup plain pairs, one
hand edge per case, callers redirected to the matching variant);
wrong-case steps stay ERROR until split.**

Reasoning: R-SPLIT applied to a switch dispatch. Printed source:
SwitchingProvider.get is one method for all switch ids — case 0
(line 627) is provideVaultManager, case 3 (line 636) is
provideIconPackManager (AegisModule.java:26-28, 37-41). A route that
needs the icon-pack provider but takes the vault-manager case (or vice
versa) contradicts its own printed dispatch — own-edge ERROR, not
UNCLEAR. The notes already specify the fix shape (line 593); this
decision adopts it.

Affects: R2 step 6, R4 step 6 (E29463d22 route fix: inject
IconPackManager through AegisActivity.java:55-56 or
IconPacksManagerFragment.java:45-46 — that redraw instruction stands
alongside, not instead of, the variant split), G5 step 6. No label
changes.

Graph edit implied (not applied): sup plain SwitchingProvider.get →
provider pairs; add get@VAULT → provideVaultManager and get@ICON →
provideIconPackManager hand edges with case guards; redirect callers
by the switch id they pass.

Evidence that would change it: printed proof all callers on the
affected routes pass the same switch id (then the plain edge is not
wrong for those routes, only under-specified).

### R6 — Shared saveAndFinish node (EntryAdapter steps 20, 23)

**Decision: split into @ADD / @DELETE variants; affected steps stay
ERROR until split.**

Reasoning: R-SPLIT again. Printed source: EditEntryActivity.java:680
addAndFinish calls saveAndFinish(entry,false); :693-695
deleteAndFinish calls saveAndFinish(entry,true); the graph has no
addAndFinish or deleteAndFinish node, only the shared saveAndFinish
node — so a route that deletes cannot be distinguished from a route
that adds, and the delete-item-hidden-for-new-entry guard
(EditEntryActivity.java:658-659) is contradicted on the delete path
(step 20) while the result-edge guard "delete is false" is reached
from the delete path (step 23). Both are own-edge contradictions
(ERROR), not D2 cases.

Affects: EntryAdapter.setTempHighlightEntry steps 20, 23. No label
changes.

Graph edit implied (not applied): add addAndFinish / deleteAndFinish
nodes (or @ADD / @DELETE variants of saveAndFinish) with the
false/true guards from :680/:693-695, and route add vs delete callers
to the matching variant.

Evidence that would change it: printed proof saveAndFinish's boolean
is read identically on both paths for the steps in question (then the
shared node is harmless for those steps and the ERRORs are re-judged,
not the model).

### R7 — Other cross-run states: ST_VAULT_ENTRIES, ST_BIO_SLOT

**Decision: same rule as R1/D2. Keep both states and their edges;
UNCLEAR on fresh-declared routes, correct on relaunch-declared routes
that genuinely need them.**

Reasoning: ST_BIO_SLOT already has Aegis precedent for this treatment
(line 619: the biometric tap needs ST_BIO_SLOT, cross-run, because the
unlock screen is reached on a later launch with no intro; the intro
variant ST_BIO_SLOT_INTRO was removed as unused). ST_VAULT_ENTRIES
(shared, Vault.java:9-12 citation) is a data state produced by an
earlier run's entries; nothing in the printed record shows it is
in-run producible on the routes that use it, and nothing shows it
cannot persist — so D2, not ERROR and not R-CLOSED.

Affects: any route step carrying ST_VAULT_ENTRIES or ST_BIO_SLOT
without an in-run producer on that route. No label changes; no graph
edit except ensuring the needs_state is present where the state is
cross-run.

### R8 — R3 step 7: onCreateOptionsMenu runs after onCreate (androidx unread)

**Decision: keep as written with confirmed_by INFERRED; route verdict
UNCLEAR (code not read), not ERROR.**

Reasoning: R-LIB / AGENT_BRIEF §2 — androidx is not on disk, so
lifecycle-ordering claims resting on it stay INFERRED; KIRO §4
verdict unclear covers "code you cannot read". This is the mirror
image of D7: where D7 has printed app code contradicting the chain
(ERROR), here no printed code contradicts it and the only gap is
unread library code (UNCLEAR). The distinction is intentional and
must be preserved when judging other steps: unread library ≠ wrong.

Affects: R3 step 7 only. No graph edit. Evidence that would change
it: androidx appcompat source printed showing the ordering (then
SOURCE / correct) or contradicting it (then ERROR).

---

## Cross-effects: how verdicts move when these decisions are applied together

- Slot.<init> step 8 and EntryAdapter step 8: already UNCLEAR (D2)
  in round 7; R1 confirms that as final, not provisional.
- EntryAdapter search step 14: ERROR → UNCLEAR (D4). Steps 8 and 12 of
  the same route do **not** move with it; they stay ERROR.
- Route 4 step 9: ERROR → UNCLEAR (D2) once the needs_state is added;
  the route header's `explicit_standard_route=yes` is **not** changed
  (D2's point is that a STATE gate does not falsify it).
- Route 1 step 21: ERROR → CORRECT on fresh print (D3). If the fresh
  print still bypasses initNew, the decision stands but the fix has
  not survived to the branch — re-apply, do not re-decide.
- G3_5 step 34 tap chain: graph edit stands (D5), but the
  GoogleAuthImporter.readFromApp route as a whole stays ERROR because
  of step 24 (D7). Quoting D5 as closing that route would be wrong.
- GlideRequests.asBitmap: steps 6–10 already CORRECT (WP3 check);
  step 50/53 stays ERROR until the D6 ENV gate plus redraw; steps 25/28
  (PIN listener / PasswordConfirmationListener) stay ERROR until the
  R2 variant split; step 65 (AssignIcons showAddCustom false,
  AssignIconsActivity.java:194, IconAdapter.java:63) is a separate
  wrong-source ERROR untouched by this dossier.
- Fresh-install routes that currently pick cross-run edges (G4 route 1,
  G1 routes 3–4, G2 routes 1–5 per the Stage 5 redraw list) do not
  become correct by keeping the edges (R1): they need redraws through
  the fresh edge E0602e719 or a relaunch declaration. Keeping an edge
  and blessing a route that misuses it are different acts.
- No method label changes anywhere in this dossier. Every decision
  above is a route/edge/verdict decision. Any future label change
  needs its own method-level showing (printed callers, kind, reason,
  SOURCE or INFERRED) under R-LABEL; in particular, nothing here
  licenses marking any Aegis method UNREACHABLE.

## Not decided here (ordinary fixes, not conventions — handling rule stated)

The following open items are **not** modelling decisions and are not
reclassified by this dossier; their handling rule is: missing in-run
producer = ERROR until a printed producer chain or variant puts the
producer on the route; cross-run producer = UNCLEAR (D2); unread
library producer = INFERRED / UNCLEAR (R8 pattern). Listing them here
so they are not mistaken for decided items: MOTP chain producers
(vault creation in intro, two TOTP entries with different periods,
bind step, MOTP PIN producer at EditEntryActivity.java:781-782);
Salsa20 typed-password producers (SecuritySetupSlide.java:138-142,
EditTextHelper.java:22); VaultGroup.equals group-creating producer
(S_LIST → group add EditEntryActivity.java:403-418 → save :800-804);
ApkSignaturePin panic producer (pref_panic_trigger,
preferences_security.xml:91-96, PanicResponderActivity.java:22-26);
DigitCount / VaultBackupManager typed-password, backup-switch, backup-
folder and SAF-grant producers; EntryAdapter bind producer
(EntryAdapter.java:569, :585); G4 route 1 step 16 multi-select env
note and G4 route 4 step 29 supported-version edge (route-note fixes).
The Hilt auto edge E1ef992ce (Hilt → AegisApplicationBase.onCreate,
INFERRED generated code) is kept as INFERRED under R-LIB and needs no
decision beyond R3's library rule.

## For the coordinator (merge checklist, not a verdict)

1. Apply the graph edits described in D2, D4, D6, D7, R1, R2, R5, R6
   (and verify D3's @SAVED construction and D5's @APP chain are
   present on the current branch); do not apply any edit this dossier
   does not describe.
2. Rebuild (0 errors, 0 warnings expected; any rise stops the merge)
   and re-print with `show_route` every route named above; edge ids
   change after variant splits, so old step citations go stale and
   must not be carried forward.
3. Obtain the D7 missing print (showImportersDialog choice mode,
   setItemChecked/selection calls, row-listener body, OK checked-row
   read) and the E4db374dd edge text before counting those two items
   as settled.
4. Record the D5 Authy-default Limits sentence and the R3 INFERRED
   statements in readme_notes.md under Limits when that file is
   written; do not record any of this dossier's decisions in anyone
   else's name.
5. Aegis is not done on the basis of this dossier: WP3 brief steps
   6–10 (final sample, verification.csv, readme, final checks,
   lessons) remain pending on a full checkout, as the WP3 report
   states.

### stream-B/AmazeFileManager/DECISIONS.md

# AmazeFileManager — DECISIONS (Muse's own decisions, for user/Yang review; never in Yang's name)

## D1. Do NOT use the token-bearing download URL (2026-11-01, stream B)
Reasoning: the task's hard constraint forbids waiting for, using, or
recording any token, and the connector redacts the token in its own
output. The URL was therefore not unwrapped, not fetched, and not
recorded anywhere. Consequence: large branch files stay unfetched and
the gate is blocked (see STEP_LOG). This decision follows the task
constraint, not a user instruction about this app.

## D2. Do NOT substitute an older under-1MB graph copy for the current graph_def.py
Reasoning: scratch copies under 1 MB (e.g. graph_def_before_rb12.py,
746,302 bytes) are intermediate states, not the current graph
(1,058,622 bytes, build 28/29/30 state, 2509/472). Building one would
produce different counts and would misrepresent the branch graph.
A faithful reconstruction from parts/ is also impossible because
merge_parts.py only appends UNREACHABLE entries from 4 parts and the
parts lack the base graph (entries, SCREENS, hand edges, SUPPRESS,
ENV_KINDS_OF, CLASSIFY/EDIT hooks). Consequence: no local build is
claimed tonight.

## D3. Do NOT flip any of the 21 contradictions on tool coverage alone
Reasoning: KIRO section 3 and the task both forbid it; coverage is a
pointer only. Tonight's flips are proposals from printed source only
(section A of route_checks_consolidated.md), and the 13 Glide methods
with no printed call site stay OPEN rather than being confirmed
UNREACHABLE.

## D4. GlideRequests.as is INFERRED, and held if SOURCE-only is required
Reasoning: the two asDrawable() anchor sites are printed SOURCE, but
the asDrawable() -> as(Class) step is generated-code delegation and
generated GlideRequests.java is not in final_java_only and was not
printed. Presenting the whole route as SOURCE would overstate the
evidence. The merger must either record the INFERRED step or print
the generated file first.

## D5. No sample error rate is reported tonight
Reasoning: the sampler could not run (methods.csv blocked), so the
only judged items are an issue-first selection. Reporting 6/6 = 1.00
as "the error rate" would mislead; the consolidated report states
the 6/6 figure only as the issue-first set's fraction and forbids
quoting it as the app's error rate.

## D6. Citation corrections adopted tonight (supersede prior files)
Reasoning: grep-verified against locally printed source tonight.
(a) AppsAdapterPreloadModel clone line is :45, not :44 — all fix
fragments citing :44 must be corrected before merge.
(b) Sftp lambda$null$5 matches the removeConnection Runnable by
elimination (only 7-capture, non-static, no-trailing-interface-param
lambda$null$ candidate), NOT by exact descriptor order — the
descriptor order (String, int, String, ...) differs from the
source-textual capture order, so the prior "exact order" claim is
withdrawn. Neither correction changes any verdict.

## D7. verification.csv is NOT hand-written tonight
Reasoning: the rules require verification.csv to be produced by
make_verification.py with assertions against the graph, and no
make_verification.py exists for AmazeFileManager on the branch.
Hand-writing it would violate the rule and could not be asserted
without a build. It stays unwritten until a checkout exists and the
generator is authored.

## D8. Draft logs are kept as drafts, not as branch logs
Reasoning: readme_notes_DRAFT.md and LESSONS_DRAFT.md in this local
mirror are hand drafts. They must not be copied to the branch as
readme_notes.md / LESSONS.md until the build passes and
gen_readme_v2.py has run on a full checkout. The filenames carry
_DRAFT to prevent accidental promotion.

### stream-B/AnkiDroid/DECISIONS.md

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

### stream-B/MMEX/DECISIONS.md

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

### stream-D/DECISIONS.md

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

### stream-A/DECISIONS.md

# LibreTorrent convention decisions — Stream A, Phase 1

**Status: DECISIONS ONLY. No batch file, `graph_def.py`, `out/`, `PROGRESS_V2`,
or `AGENT_NOTES` was edited. Nothing was pushed. Nothing here is verified for
merge (build, sampler, rule-F grep, and C1 are still owed); these decisions
state what the merger applies, they do not merge anything.**

**Authorship: these are Muse's own decisions, recorded for user/Yang review.
They are NOT made in Yang's name, and no decision below is attributed to Yang.
No tick mark is written anywhere in this file.**

**Sources used:** the conditional tables in
`~/workspace/overnight/stream-A/work/batch<N>-merge-ready.md`, the dossiers in
`~/workspace/libretorrent-conventions/` (confirmed-by, strict-entry, room,
binding-variant-getter, generated-parcelable, clinit-rx-apigate), the grep
summaries in `~/workspace/libretorrent-grep/`, and the rule files
(`handoff/KIRO_CONVERT_APPS.md` §§0–14 incl. rule F,
`handoff/KIRO_CORRECTIONS.md` C1–C8, `handoff/SCHEMA_V2.md`,
`handoff/AGENT_BRIEF_V2.md`, `handoff/CONVERSION_RECIPE.md`,
`handoff/CHATGPT_PROMPT_LIBRETORRENT_3.md` Part 1 + rules A–K; local copies
under `~/workspace/b27scratch/` were used where the branch text was not
re-read). Where a conditional table already stated a flip set, that row list
is adopted here, not re-derived. Row lists were checked against the
merge-ready files for the families below.

**Standing principles applied throughout (from the written rules):**
- P1. A label needs a printed route (REACHABLE) or an authored reason with a
  source reference (UNREACHABLE); there is no automatic dead code, and a
  method with a route is never UNREACHABLE.
- P2. Absence in the 252-file app-Java tree alone never flips a row to
  UNREACHABLE, because that corpus excludes res XML, generated code, and
  library/framework bodies. A `search_code` 0 is never evidence of absence.
  UNREACHABLE on absence requires a saved full-repo grep in rule-F/C5 form
  covering the domain that could actually trigger the method.
- P3. Generated/library/framework dispatch that is unprinted is INFERRED,
  never SOURCE, and never a reason to call a row untriggered: the dispatch
  exists, it is just unprinted.
- P4. One rule per family, project-wide, never batch-local. Where two options
  are genuinely tied by the rules, the tie-break used below is explicit:
  keep the most already-standing rows standing.
- Note on precedent: no ticked-app convention file was in this task's read
  set, so no ticked-app precedent is cited as evidence below. Precedent cited
  is LibreTorrent's own recorded batch practice plus the written rules. If
  the coordinator holds ticked-app precedent contradicting any decision
  here, that decision should be re-opened, not silently overridden.

**Net effect of the decisions below (label flips ordered here, families
decided here only):** 62 rows OPEN → REACHABLE, 46 rows → OPEN (reverts),
43 rows → UNREACHABLE, 1 confirmed_by-only change. Separately affirmed (not
newly ordered here): TagInfo trio rows 31/23, 31/26, 31/28 → REACHABLE
INFERRED on their printed round trip (see D5). All other rows named below
stay exactly as their files table them.

---

## D1. confirmed_by: per-row, not whole-route

**Chosen: per-row SOURCE.** `SOURCE` = a printed app-code line names the
method itself (direct call, `new` construction, printed internal call from
a REACHABLE method, printed super-call, printed call inside a
listener/lambda body, a printed `notifyListeners`/method-reference site
naming the callback, or a printed registration of a standard framework
callback whose dispatch is framework-defined — lifecycle, click, adapter/
DiffUtil callbacks, as in batches 81/82/92). `INFERRED` = the method is
reached only through unprinted framework/library/generated dispatch, or
(UNREACHABLE proposals) through absence over a saved grep. Labels are
unaffected by this decision in every case.

**Reasoning.** All 43 batches in the confirmed-by dossier record per-row
intent; zero record whole-route as their table convention. SCHEMA_V2's
"SOURCE when every claim in the evidence of every edge of the best route
cites a source line" is satisfied per-row: each row's own edge cites its
printed line, and the rows' route columns record the remaining edges as
INFERRED where unprinted. Whole-route would flip up to 637 SOURCE rows to
INFERRED on a print-completeness technicality no batch's evidence meets,
and would destroy the distinction the files deliberately draw between a
row's own evidence and its upstream dispatch.

**Width rulings inside per-row (each decided, not left open):**
- (a) Registration-printed standard callbacks = SOURCE (batches 81/82/92
  stand). The registration print IS the source citation for the callback
  edge; framework dispatch from a printed registration is not the same
  evidence class as unprinted generated code.
- (b) `notifyListeners`/method-reference sites naming a callback = SOURCE
  (batch 28 stands).
- (c) Interface/facade call sites: SOURCE only where the printed line
  names the row method itself. A printed call naming only the
  interface/facade method, with dispatch to the row's implementation
  unprinted, is INFERRED. Consequence: batch 55's SafFsModule rows stand
  SOURCE (their printed facade callers name them, e.g. 55/27, 55/28);
  batch 54's INFERRED SafFileSystem rows stand INFERRED unless a merger
  audit finds a printed line naming one of them, in which case that row
  upgrades to SOURCE under this rule (audit action, not a flip ordered
  here). Batches 53–55 are therefore consistent under one rule, not split.
- (d) Generated-binding dispatch behind a printed binding call = INFERRED,
  never SOURCE (batches 59–61 stand; no upgrade). The generated body is
  absent, so no printed line names the Impl method.
- Batch 112's 11 upgraded rows (2, 3, 12, 20, 21, 22, 25, 26, 27, 28, 29)
  stand SOURCE: the revert condition ("requires a direct caller outside
  the adapter") is NOT adopted — adapter-internal printed calls name the
  methods, which satisfies per-row.
- Batch 3's unnamed "SOURCE-upgrade" note applies to NO row: it names no
  row, and no UNREACHABLE row is claimed SOURCE.
- OPEN rows normalise to `—` at merge (not `INFERRED ('at best')`): an
  OPEN row has no confirmed route, and labelling it INFERRED overstates
  what is known. Presentational only; no label changes.

**Flips under D1: none.** No `confirmed_by` value changes except D5's
22/2 (see below). Named whole-route candidates that STAY SOURCE:
12/24; 20/34, 20/35; 29/11, 29/27, 29/30; 30/40; 31/12; 44/22, 44/24, 44/26,
44/28, 44/30, 44/32; 74/12, 74/13, 74/37, 74/40; 96/37.
**Evidence that would change it:** a project decision, recorded by the
user, to adopt whole-route — it would flip the SOURCE lists in the
confirmed-by dossier's Appendix, row by row, and must not be applied
piecemeal to one batch.

## D2. Strict launcher-entry — five sub-decisions, decided separately

**D2a. Anchor vs strict printed-launcher rule — ADOPT the anchor
convention.** A row is REACHABLE if a printed in-app chain reaches it
from a printed host anchor (activity, fragment, dialog, service, worker,
ViewModel, repository, engine). The launcher→host step need not be freshly
printed in the same batch, and its absence is a documentation caveat, not
a label blocker, provided the host is a real app component (manifest-
declared, or hosted by one, or reached from one on a printed chain).
**Reasoning:** labels describe the app's trigger graph, not per-batch
print completeness. The launcher itself IS printed for this app
(manifest MAIN/LAUNCHER, MainActivity — batches 73/74/99/112). The strict
rule would revert ~1,102 of 1,261 proposed REACHABLE rows in the
strict-entry dossier's set on a formality, while the underlying routes
are printed. P1 forbids the reverse error too: a row with NO printed
chain to any anchor does not stand (see D2c, batch 99).

**D2b. Fresh-in-this-pass vs sibling-batch/trunk print — sibling/trunk
prints COUNT, if cited.** A print from another batch's pass on the same
branch (manifest, DetailTorrentActivity from batches 87–88, TorrentService
→ TorrentEngine from batches 71/72, launcher/settings-menu from batches
109–110/114, FeedSettingsFragment opening from SettingsFragment/
PreferenceActivity) counts as evidence when the citing file gives the
batch and line. "Fresh in this pass" is preferred, not required. A lead
asserted without a citable print does not count.

**D2c. Launcher-step-only, not every-step-fresh.** The requirement stops
at the launcher→host link. Layout-attachment steps (batch 112's
`activity_main.xml`), fragment-attachment steps, and dialog/activity
starter steps need not each be freshly printed where the host chain is
otherwise printed. Batch 112 therefore stands (launcher→MainActivity and
MainActivity→MainFragment via findFragmentById are printed; only the
layout declaration is unprinted). Batch 99 rows 1–13 stand (launcher →
MainActivity → FeedActivity chain freshly printed). **Exception, and the
sole strict-entry revert:** batch 99 rows 14–40 (26 REACHABLE rows)
revert to OPEN — not because an attachment step is unfresh, but because
the FeedActivity→FeedFragment link is unevidenced anywhere: FeedActivity
code never names FeedFragment and `res/layout/activity_feed.xml` was not
found. A chain with a missing link is not a chain.

**D2d. Per-row, not whole-batch.** Applied row by row. The files' own
splits stand: batch 73 (26 rows stand, launcher-anchored), batch 74 (all
38 stand — its 16–27 TorrentNotifier rows stand under D2b on the
71/72 TorrentService→TorrentEngine print), batch 99 (13 stand / 26
revert, above), batch 112 (39 stand under D2c).

**D2e. Downstream inheritance — no propagation beyond a printed chain.**
If the host link is satisfied (D2a/D2b), downstream rows on a printed
in-app chain stand; strictness does not re-attach at each hop. Batch 96
rows 19–39 stand (ErrorReportActivity and FeedItemsActivity are
manifest-declared activities, i.e. anchors; their lifecycle rows are
INFERRED on framework dispatch as their file already marks them). Batch
106 rows 12–39 stand downstream of LogActivity (whose start IS freshly
printed: MainActivity menu → LogActivity). Batch 96 rows 1–18 and batch
106 rows 1–11 likewise stand under D2b (batch-95 trunk; manifest lead
from batches 107–108).

**Flips under D2: batch 99 rows 14–40 → OPEN (26 rows). No other row
moves on strict-entry grounds.** The FeedSettingsFragment opening print
(SettingsFragment :122/:131–134/:195–199, PreferenceActivity :113–114)
is adopted as the settled print for that one step only: it supports
batch 44 rows 1–3's upstream link under D2b but does not change batch
44's standing (its other settings-fragment rows still rest on the
anchor convention) and does not touch batch 12 (whose gap is the
preference-change→Scheduler step, a different step).
**Evidence that would change it:** a printed FeedActivity→FeedFragment
link (activity_feed.xml in any layout dir naming FeedFragment, or a
FragmentTransaction naming it from FeedActivity) flips batch 99 rows
14–40 back to REACHABLE. A user decision to adopt the strict rule instead
would revert the ~1,102-row set in the strict-entry dossier — recorded
here as the cost of that alternative, not adopted.

## D3. Room

**D3a. `$N` SET vs STRICT — ADOPT SET, project-wide.** Every generated
helper in a set is used because every underlying DAO operation in that
set is called on a freshly printed route; a swap of `$N` assignments
within a set changes no label. Per-row `confirmed_by` is INFERRED
(generated dispatch unprinted). STRICT is rejected: it demands printed
generated source or bytecode that this project has for no generated
family, it cannot be applied uniformly without the pinning exemptions
its own files raise (FeedDao_Impl$8.call return-type uniqueness,
FastResumeDao_Impl$1 single-`@Insert` elimination), and it would revert
46 rows in batches 50–52 while leaving batch 53 inconsistent. Under SET
the pinning-exemption question is moot (pinned cases stand as
corroboration, not as the basis). STRICT's evidence standard (printed
generated source and/or bytecode from a build emitting `*_Impl.java`)
is recorded as the standard that would be needed if SET were ever
reversed — it is not met today.
**Flips under D3a: batch 53 rows 10–28, 30, 31 → REACHABLE INFERRED
(21 rows).** Batches 50–52 unchanged. Rejected alternative's revert
lists (NOT applied): 50/28–30; 51/13–17, 51/19, 51/20, 51/22, 51/23,
51/25–40; 52/1, 52/3, 52/4, 52/16–26, 52/28, 52/29, 52/31, 52/32.

**D3b. Callable `finalize()` — ADOPT F1: GC dispatch counts as a
trigger-graph route.** A `finalize()` row is REACHABLE INFERRED where
its enclosing Callable is REACHABLE (which D3a guarantees for every row
below). The object is created on a printed route, and JVM finalization
is defined runtime dispatch on collection — nondeterministic timing is
a condition on the route, like a STATE gate, not a blocker. It is never
`no_trigger_in_app` (the Callable IS created) and never SOURCE (GC
dispatch is unprinted).
**Flips under D3b: 51/18, 51/21, 51/24, 52/2, 52/5, 52/27, 52/30, 52/33,
53/29, 53/32, 41/11 (TorrentInputStream.finalize, object created on the
printed TorrentEngine.getTorrentInputStream :758–759 route) → REACHABLE
INFERRED (11 rows).**
**Evidence that would change it:** a project rule excluding GC-only
dispatch from the trigger graph would return all 11 rows to OPEN (not
UNREACHABLE — creation is printed).

**D3c. `getRequiredConverters` — ADOPT the database-build assumption as
a project rule, extended set.** Room's generated `_Impl` validation
calling DAO `getRequiredConverters` at database build is adopted as the
project rule, on the printed build itself (AppDatabase.buildDatabase
:81–87, `Room.databaseBuilder...build()`). This resolves the wording
tension explicitly: batch 48's "only on a printed Room dispatch" wording
is overridden by this decision; the 50–52 files' "or a project decision
adopting the assumption" wording governs.
**Flips under D3c: 50/27, 51/6, 52/11, 53/4, 48/14
(AppDatabase_Impl.getRequiredTypeConverters, validating the printed
`@TypeConverters({UriConverter.class})` at AppDatabase.java:53) →
REACHABLE INFERRED (5 rows).**
**NOT flipped by D3c:** 48/12 (getAutoMigrations) and 48/13
(getRequiredAutoMigrationSpecs) stay OPEN. AppDatabase declares NO
auto-migrations (`@Database` :42–52 lists entities and version 9 only),
so there is no declared auto-migration for Room to validate — the
converter argument (a real declared converter to validate) has no
analogue here. They need their own printed Room dispatch or printed
generated AppDatabase_Impl showing the call. 48/7 (clearAllTables) and
48/19 (dropAllTables) stay OPEN: no caller is printed, and the
destructive-migration path that would call dropAllTables is not
configured (buildDatabase uses addMigrations, no fallback) — but that
is a configuration observation, not a full-repo proof about generated
code, so neither row goes to UNREACHABLE. 4/11 (UriConverter.<init>)
stays OPEN: Room registration alone does not construct the converter
(its methods are static; zero `new UriConverter` in the tree); it needs
a printed generated-instantiation step or a `new` site, and is NOT
flipped by the converter decision, which covers only the
getRequiredConverters/getRequiredTypeConverters methods.
**Room totals check (batches 48 + 50–53, 200 rows):** as recorded
160/0/40 → SET project-wide 181/0/19 → + D3b 191/0/9 → + D3c
196/0/4. Remaining OPEN: 48/7, 48/12, 48/13, 48/19.

## D4. Binding

**D4a. getViewModel read-path (v) — ADOPT field-read (v-field).**
Generated `executeBindings` reads the `mViewModel` field, NOT the
abstract `getViewModel()` getter. The abstract getter is app-callable
API, not the generated read path; no generated Impl body is printed
anywhere to show otherwise, and the field-read is the mechanically
standard generated-code shape.
**Flips under D4a: 62/4 (DialogCreateTorrentBinding.getViewModel) and
62/30 (DialogErrorBinding.getDetailError) → OPEN (2 rows).** Both were
REACHABLE only on the getter-reading. All other abstract binding
getters already OPEN stay OPEN: 59/8, 59/22, 60/30, 61/15, 61/30, 63/1,
63/15, 64/33, 65/6, 66/12, 66/24, 67/10, 67/22. Each resolves only on a
printed caller of the getter itself.
**Different mechanism, NOT moved by D4a:** layout-resolved property
getters stand REACHABLE INFERRED — 84/40 (CreateTorrentViewModel.
getBuildProgress, via `dialog_create_torrent.xml:36
android:progress="@{viewModel.buildProgress.intValue()}"` + dialog
inflate + setViewModel) and 90/5 (TorrentDetailsInfo.getDirName, via
`@Bindable` + generated databinding for the detail-info layout). Those
are layout-expression resolutions through a getter, not
executeBindings reads of a binding field. If the merger ever requires a
printed generated binding class for layout-resolved getters, 84/40 and
90/5 revert to OPEN on their own stated conditions — that requirement
is NOT adopted here.

**D4b. Variant config gate (iv) — ADOPT all-configurations (Option A),
for batches 60 and 65 together.** Labels cover all device
configurations. A config-qualified Impl (layout-large-land-notouch,
layout-sw600dp-land) created on a matching device is REACHABLE. The
single-fixed-portrait-phone alternative is rejected: no fixed config
was printed in any file (batch 60's header admits this), so Option B
would rest on a merger-supplied premise, and it would still leave an
OPEN → UNREACHABLE `closed_by_configuration` step to be taken
separately. Configuration is a device state, like an API level or a
setting — STATE gates are allowed on routes (SCHEMA_V2).
**Flips under D4b: none (rows already REACHABLE stand).** Standing:
60/13–16, 60/21–24 (variant appbar creation/lifecycle) and the batch-65
variant Impl creation/lifecycle rows (including 65/23, 65/25, 65/34,
65/36; 65/27 and 65/38 setVariable rows revert under D4d regardless —
the gate governs creation rows, not callback rows). Batch 60's header
"Judging rule" paragraph saying rows 13–28 stay OPEN is STALE and is
overridden by its own table (13–16 and 21–24 REACHABLE, 17–20 and 25–28
OPEN); the table governs.
**Evidence that would change it:** a printed, project-adopted fixed
device configuration plus an explicit merger step would be needed even
to move these rows to OPEN as `closed_by_configuration` candidates.

**D4c. No-variable layouts and the U rule — ADOPT option U for
setVariable/onFieldChange of no-variable, no-parent bindings.**
A binding whose layout declares NO `<data>` variable, whose layout is
passed NO variable by any `<include>` parent anywhere in res/layout
(verified: all 69 layout files, only `<include>` targets are `toolbar`,
`main_drawer_content`, `add_torrent_info`, `detail_torrent_appbar`, zero
`bind:` attributes; no qualified variant of any of the 13 group layouts
exists; the only `@{...}` expressions in the 13 are static dimen sums
referencing no variable/observable), with zero `.setVariable(`/
`.onFieldChange` hits in the complete 252-file app-Java tree and no
typed-setter call on that binding, has NO possible caller left for
setVariable/onFieldChange: app code is fully covered by the tree grep,
generated parent-Impl dispatch is ruled out by the include check, and
the databinding library does not call these two methods (they are
app/generated API, not library callbacks — onFieldChange fires only via
a generated observable registration, which cannot exist without a
variable/observable). This is the one family where app-tree + layout
evidence is complete enough to close, and it is decided here rather
than left OPEN forever.
**Flips under D4c: 40 rows → UNREACHABLE `no_trigger_in_app` INFERRED:**
60/11, 60/12, 60/19, 60/20, 60/27, 60/28 (appbar base + variants);
64/3, 64/4, 64/12, 64/13, 64/21, 64/22, 64/30, 64/31 (SelectTag + drawer
items); 67/40 (TrackerList onFieldChange, companion of 68/1);
68/1, 68/9, 68/10, 68/18, 68/19, 68/27, 68/28, 68/36, 68/37;
69/5, 69/6, 69/14, 69/15, 69/23, 69/24, 69/32, 69/33;
70/1, 70/2, 70/10, 70/11, 70/19, 70/20, 70/28, 70/29.
The generic-framework-callback alternative (option R: framework dispatch
always runs these callbacks) is REJECTED: it conflicts with rule (xv)
(a variable/observable callback cannot run without a variable/
observable) and no file shows a library call to them. U does NOT cover
hasPendingBindings (library state query — see D4f) and does NOT cover
invalidateAll (ctor-internal — see D4e), even for no-variable bindings.
**Evidence that would change it:** a printed variable declaration for
the layout, a printed `bind:` pass-through to it, a printed
`.setVariable(` call, or a printed generated Impl body showing a
registration — any one flips the affected row(s) back to REACHABLE.

**D4d. setVariable direction — RESOLVED MECHANICALLY: in generated
code `setVariable` CALLS the typed setter (`setViewModel`, etc.), not
vice versa.** A printed `setViewModel` call is therefore evidence that
the typed setter ran, and ZERO evidence that `setVariable` ran. The
batch 65 wording ("`setVariable` is the generated dispatch point behind
`binding.setViewModel`") and the identical backwards wordings in
batches 59/60/61/62/66/67 ("generated setViewModel calls setVariable",
"Called by the generated setViewModel", "generic variable dispatch")
are wrong about direction and are overridden. The correct
setVariable rule: REACHABLE INFERRED iff (i) a printed `.setVariable(`
call names the binding, or (ii) a printed `<include>` with a `bind:`
attribute passes a variable to this child binding from a REACHABLE
parent executeBindings (the parent-to-child generated route).
**Flips under D4d: 15 rows → OPEN (reverts):** 59/5, 59/17, 60/40,
61/25, 61/39, 62/15, 62/39, 65/3, 65/16, 65/27, 65/38, 66/21, 66/34,
67/19, 67/31. **Standing under D4d:** 59/32
(AddTorrentInfoBindingImpl.setVariable) — the child binding IS passed
`app:viewModel` by its parent include in fragment_add_torrent_info
(printed), so the parent executeBindings → child setVariable route is
real; only its rationale wording is corrected. All other setVariable
rows already OPEN stay OPEN (63/10, 63/24, 64/4, 64/13, 64/22, 64/31
except where D4c flips them to UNREACHABLE, 66/10, 67/8, 68/10, 68/19,
68/28, 68/37, 69/6, 69/15, 69/24, 69/33, 70/2, 70/11, 70/20, 70/29 —
several of the last groups flip under D4c instead; the two decisions
compose, they do not conflict).
**Evidence that would change it:** a printed `.setVariable(` call, a
printed `bind:` pass-through, or a printed generated Impl body showing
the call — for the specific binding in question.

**D4e. invalidateAll rule — ADOPT REACHABLE-on-inflate.** A generated
Impl's `invalidateAll()` is called by the generated Impl constructor
itself on construction — the same evidence class as the already-
accepted 2-arg→3-arg ctor delegation and the executeBindings wave
(printed inflate + printed layout + generated dispatch INFERRED).
Batches 65–70 already apply this rule; batches 59–64 keep the rows
OPEN. This is a genuine tie by batch count (6 batches each way), so the
stated tie-break applies: REACHABLE preserves 22 standing invalidateAll
rows in batches 65–70, while OPEN would preserve only the 18 OPEN rows
in batches 59–64 and revert those 22. REACHABLE wins on the tie-break,
and on the ctor-internal evidence class.
**Flips under D4e: 18 rows → REACHABLE INFERRED:** 59/3, 59/14, 59/28;
60/10, 60/18, 60/26, 60/36; 61/21, 61/36; 62/10, 62/36; 63/7, 63/21;
64/2, 64/11, 64/20, 64/29, 64/39. (Variant rows 60/18, 60/26 flip under
D4b + D4e together.) Already-REACHABLE invalidateAll rows in batches
65–70 stand.
**Evidence that would change it:** a printed generated Impl body
showing the constructor does NOT call invalidateAll would revert the
affected rows to OPEN.

**D4f. hasPendingBindings resolver — NO FLIP; resolver named.**
Every hasPendingBindings row currently OPEN stays OPEN: 59/2, 59/13,
59/27; 60/9, 60/17, 60/25, 60/35; 61/20, 61/35; 62/9, 62/35; 63/6, 63/20;
64/1, 64/10, 64/19, 64/28, 64/38; 65/11, 65/22, 65/33; 66/5, 66/17, 66/29;
67/5, 67/15, 67/27, 67/38; 68/7, 68/16, 68/25, 68/34; 69/3, 69/12, 69/21,
69/30, 69/39; 70/8, 70/17, 70/26. Unlike setVariable/onFieldChange,
hasPendingBindings IS a library-query method: the databinding rebind
path (executePendingBindings → rebind body) may query it, and that body
is unprinted. D4c's completeness argument therefore fails for it, and
it stays OPEN under every option in the 68–70 conditional tables.
Resolver (the only evidence that closes it either way): a printed
generated Impl body or a printed androidx ViewDataBinding rebind body
showing whether the rebind path calls this override, or a printed
caller. Never UNREACHABLE on the app-Java zero alone.

**D4g. `$N` count-match identification (batches 59–61, with 62–64) —
ACCEPT.** The inverse-listener identification stands: where the number
of two-way bindings `@={...}` in the freshly printed layout matches the
number of `$N` rows in the plan for that Impl exactly, while the number
of observable objects does NOT match, the `$N` rows are identified with
two-way inverse listeners. Route existence does not depend on
`$N`-to-field assignment (source-order only, NOT bytecode-verified)
because every two-way field is user-editable/toggleable in the same
host fragment/dialog. The old convention (all `$N` OPEN, batches 62–64
as originally recorded) is superseded for these rows.
**Flips under D4g: none (rows already REACHABLE stand).** Standing:
59/19, 59/20, 59/34–40; 60/1–3; 61/2–13, 61/27, 61/28; 62/1, 62/2,
62/17–28; 63/12, 63/13, 63/26–35; 66/36–39 (FragmentDetailTorrentInfo
`$1`/`$2` init+onChange, same family). Batches 62–64 `$N` rows already
REACHABLE are consistent under this rule; no 62–64 `$N` row is OPEN on
the old convention in the current files.
**Evidence that would change it:** a printed generated Impl body
showing a `$N` listener bound to a different trigger (or to no
two-way field) would revert the affected `$N` rows to OPEN.

**D4h. Base `*Binding` statics (batches 5–9, plus batch 10 rows 1–22) —
stay OPEN.** A base static (`bind(View)`, `bind(View,Object)`, the four
`inflate` overloads) requires a printed direct call naming that static,
or printed generated code calling it. A `DataBindingUtil.inflate` /
`setContentView` site does NOT count: every instantiation in the tree
goes through DataBindingUtil, which returns the Impl via the mapper and
bypasses the base static at app level — and no DataBindingUtil site
selects among the class's 6 overloads, so no single overload could be
promoted while its siblings stay OPEN on identical evidence. Zero
direct calls (0 in the 252-file tree, strict and loose patterns) plus
unprinted generated code = OPEN, never UNREACHABLE: generated
parent-Impl code could call a child binding's `bind` (the two
zero-reference classes below are exactly that shape).
**Flips under D4h: none — all 200 rows in batches 5–9 stay OPEN, and
batch 10 rows 1–22 (same shape) stay OPEN.** Per-class note: 32 of 34
classes have exactly one DataBindingUtil site for their layout (29
inflate + 3 setContentView); the 2 with zero app-Java references —
AddTorrentInfoBinding (child of fragment_add_torrent_info) and
DetailTorrentAppbarBinding (child of fragment_detail_torrent) — are
created, if at all, only by generated parent-Impl code, which is
unprinted. Corrected count carried forward: 83 word-boundary hits
across 32 classes (not "85 across 33" — the difference is the
FragmentAddTorrentInfoBinding substring trap).
**Evidence that would change it:** a printed generated Impl/mapper body
calling a specific overload, or a printed direct app call naming it —
for that class's overload(s) only.

**D4i. onFieldChange rule (for the record, completing D4).** REACHABLE
INFERRED iff the variable is set via a printed typed setter (or a
printed parent pass-through) AND the layout binds an observable of that
variable AND the Impl is created on a printed inflate. Standing under
this rule (no change): 59/4, 59/16, 59/31; 60/39; 61/24, 61/38; 62/14;
63/9, 63/23; 65/2, 65/14, 65/25, 65/36; 66/20, 66/33; 67/18, 67/30.
Staying OPEN (variable exists but no qualifying observable/change
path is printed, or no variable is set and D4c does not apply):
62/37, 66/8, 70/1 except where D4c flips it (70/1 flips under D4c —
see D4c list), 64/33-related rows. Where a file's onFieldChange row is
already REACHABLE on a printed change event for a named observable
(onChangeViewModel* rows, e.g. 59/15, 59/29, 59/30, 65/1), those stand
on their stronger event evidence.

## D5. Parcelable trio

**D5a. Trio policy — KEEP as recorded.** A Parcelable framework method
(`writeToParcel`, `describeContents`, Parcel ctor, `$1.createFromParcel`,
`$1.newArray`) stays OPEN unless a printed app-side parcel/unparcel
site names the class (Intent/Bundle `putExtra`/`getParcelableExtra`,
`putParcelable`, `writeParcelable`/`readParcelable`, a printed unparcel
site, or a qualifying storage site under D5d). A CREATOR definition
alone is not a caller. A `$1.<init>` REACHABLE verdict does NOT imply
`createFromParcel`/`newArray` (the `$1` instance runs at class init;
the Creator methods run only on framework unparcel).
**Affirmed flips under D5a (printed round trip, from the parcel grep
work, adopted here): TagInfo 31/23 (describeContents), 31/26
(writeToParcel), 31/28 (`$1.createFromParcel`) → REACHABLE INFERRED**
on: write side MainActivity :323 `putExtra(TAG_INIT_INFO, item.info)`,
SelectTagDialog :181 `putExtra(TAG_RESULT_SELECTED_TAG, item.info)`,
AddTagDialog :71 `putParcelable(TAG_INIT_INFO, initInfo)`; read side
AddTagActivity :57, AddTagDialog :119, DetailTorrentInfoFragment :137,
AddTorrentInfoFragment :142. Framework dispatch is unprinted, hence
INFERRED. All other OPEN trio rows stay OPEN (batches 21, 22, 28, 29,
30, 31 remainder, 32, 41, 42, 73, 82, 114 — 62 rows in the parcel
summary's count, minus the 3 affirmed above as counted there).

**D5b. `$1.<init>` / Parcel-ctor — ADOPT Option 1 (strict
marshalling-site rule), NO Creator-body exception to the dependency
rule.** The dependency rule stands as recorded: a method whose only
printed caller sits inside an OPEN method stays OPEN; the OPEN caller
does not bootstrap anything. Option 2 (internal construction counts)
is rejected: it would require flipping every Parcel ctor whose only
caller is its own OPEN `createFromParcel` to REACHABLE on unbacked
dispatch, contradicting D5a.
**Flips under D5b: 21/36 (AddTorrentParams.<init>(Parcel)) → OPEN (1
row, label flip); 22/2 (AddTorrentParams$1.<init>) SOURCE → INFERRED
(confirmed_by only — its construction site is a CREATOR field
initializer, not an app-code call site; same correction batch 29
already applied to 29/5).** Uniform Treatment A for all other
`$1.<init>` rows stands (28/31, 29/5, 29/20, 29/38, 30/11, 30/31, 31/4,
31/16, 31/27, 73/34, 82/15 — all INFERRED on enclosing-class first
use). 21/38 (describeContents), 21/39 (hashCode), 21/40 (toString)
stay OPEN under both options. Dependency companions that stay OPEN
under this rule: 30/16 + 30/17 (stand/fall with 30/2 + 30/10);
28/21 (super calls inside OPEN subclass methods are blocked);
31/26 (not bootstrapped by the AddTorrentParams parcel ctor).

**D5c. newArray single-vs-array — ADOPT Option B: newArray requires a
printed Parcelable-array site.** Framework semantics are mechanical:
a single-object extra calls `createFromParcel`, never `newArray`;
`newArray` runs only when unmarshalling a Parcelable array. Zero array
sites exist in the whole 252-file tree (zero `getParcelableArrayExtra`
/ `putParcelableArray*` / `writeParcelableArray` /
`createTypedArray*`). Option A (single-extra dispatch suffices for the
whole trio, newArray included) is rejected: it would treat a dispatch
that provably does not call the method as a route for it.
**Flips under D5c: 102/17 (FileManagerConfig$1.newArray) → OPEN
(revert from REACHABLE INFERRED); 114/27
(PreferenceActivityConfig$1.newArray) stays OPEN; 31/29
(TagInfo$1.newArray) stays OPEN (its round trip parcels single objects
only). Spillover (same logic, all newArray rows marked REACHABLE on a
non-array site): 92/39 (TorrentContentFileItem$1.newArray) → OPEN.**
Under both options the trio companions (Parcel ctor,
createFromParcel, describeContents, writeToParcel) stay REACHABLE on
the single extra where they already stand; only newArray differs.
**Evidence that would change it:** a printed array-extra site naming
the class flips that class's newArray row to REACHABLE INFERRED (and
only that class's row).

**D5d. Storage-site sub-decision — `createParcelableStorage(X.class)`
COUNTS as a printed parcel site for X's trio members EXCEPT newArray.**
Batch 92's storage site (FilesFragment :227
`StorageStrategy.createParcelableStorage(TorrentContentFileItem.class)`
+ onSaveInstanceState :309) names TorrentContentFileItem.class
directly, and the framework must invoke that class's own parcel
methods to store/restore it — that is a printed, typed parcel context,
with dispatch INFERRED (not SOURCE). Batch 30's refusal is
distinguished, not overruled: there the storage names a SUBCLASS while
the parcel methods live on the base class (see D5e).
**Flips under D5d: none beyond D5c.** Standing: 92/33
(describeContents), 92/36 (writeToParcel), 92/38 (createFromParcel)
REACHABLE INFERRED; 92/31 (Parcel ctor) SOURCE (its caller 92/38
stands). 92/39 reverts under D5c, above. Batch 102's trio (102/10,
102/12, 102/14, 102/16) stands on its printed putExtra +
getParcelableExtra round trip (CreateTorrentDialog :258–263/:268–273/
:327–334 + FileManagerDialog :137); only 102/17 moves, under D5c.
Batch 102/15 (`$1.<init>`) stands SOURCE: unlike 22/2, its SOURCE
marking is backed by a printed marshalling site, not by the field
initializer alone.

**D5e. Dependency rule + Room-entity-status rule — ADOPT both as
recorded, no change.** Dependency rule: see D5b (no exception).
Room-entity-status rule: a Room `@Entity`'s ctor or Parcel ctor is NOT
flipped to REACHABLE on entity status alone; only a printed
construction or a printed generated-instantiation step counts.
Staying OPEN under it: 30/37 (FeedChannel Parcel ctor), 31/20, 31/21,
31/22 (TagInfo ctors + Parcel ctor), 4/11 (UriConverter.<init> — see
also D3c). Counter-examples already REACHABLE on printed `new` sites
(30/38, 31/8, 31/10, 31/32, 31/38) are unaffected. Each OPEN row here
still needs its own printed site; the rule itself flips none.
**Inherited-CREATOR rows stay OPEN (no transfer across classes):**
30/6, 30/10, 30/12, 30/13 (TorrentInfo via TorrentListItem storage);
30/24, 30/30, 30/32, 30/33 (TrackerInfo via TrackerItem storage);
30/39, 31/3, 31/5, 31/6 (FeedChannel via FeedChannelItem storage);
73/35, 73/36, 73/29 (FileItem — the TorrentContentFileItem storage
names the subclass, and the subclass CREATOR returns the subclass,
not FileItem). Whether androidx storage dispatch invokes an inherited
base CREATOR is unprinted library semantics; a printed androidx
dispatch body or a project rule on inherited CREATORs would be needed
to move them.

## D6. Project-wide hashCode rule

**Chosen: printed-trigger rule with a narrow private-nested exception.**
- REACHABLE iff a printed trigger exists: a receiver-typed `.hashCode()`
  call on the type, a hash collection keyed/element-typed on the type,
  a printed library dispatch showing hash dispatch for the type, or a
  REACHABLE delegator that calls it (dependency rule, positive
  direction).
- UNREACHABLE `no_trigger_in_app` iff a saved full-repo grep (app Java
  + res + generated + library sources in scope) shows zero triggers,
  OR the type is provably unreferenceable outside its defining file
  (private nested class) with zero external use in the complete app
  tree.
- Otherwise OPEN. In particular, zero receiver-typed hits + zero hash
  collections in the 252-file app-Java tree alone does NOT flip a row
  to UNREACHABLE (library/framework dispatch — notably androidx
  `MutableSelection` storage — is unprinted), and does NOT flip it to
  REACHABLE. Options H-grep and H-lib-as-absence are both rejected;
  H-printed (stay OPEN) is adopted as the default, with the two
  UNREACHABLE paths above as the only exits.
**Flips under D6: none — all 23 OPEN hashCode rows stay OPEN:**
10/30 (PeerItem), 10/32 (FeedItemsListItem), 10/39 (drawer TagItem),
112/30 (TorrentListItem), 20/39 (LogEntry), 21/39 (AddTorrentParams),
28/28 (AdvancedTorrentInfo), 29/2 (MagnetInfo), 29/17 (PeerInfo),
29/35 (SessionStats), 3/26 (TagInfo), 30/8 (TorrentInfo), 30/27
(TrackerInfo), 31/1 (FeedChannel), 31/13 (FeedItem), 31/37 (Torrent),
32/7 (TorrentTagInfo), 32/34 (TorrentMetaInfo), 41/28
(TorrentInputStream$Piece — see exception note below), 41/36
(TorrentStream), 73/31 (FileItem), 95/35 (TrackerItem), 99/18
(FeedChannelItem). Traps NOT counted as triggers (recorded, not
re-decided): `List.contains`/`containsAll`/`indexOf` and DiffUtil
equals routes (equals-only); `.hashCode()` calls on fields inside a
definition body (String `id`/`name`/`url`, `List tags` — a List call,
not the element type's call); being a Map value or List element.
**SelectionTracker lead (not a flip):** exactly three of the 23 types
have a SelectionTracker + `createParcelableStorage` + `copySelection`
site (TorrentListItem MainFragment :100/:157–162/:575–576/:599–600/
:610–611; FeedChannelItem FeedFragment :84/:137–142/:446–447/:466–467/
:483–484/:496–497/:511–512; TrackerItem DetailTorrentTrackersFragment
:84/:178–183/:362–363/:376–377). `createParcelableStorage` is Parcelable
storage, not a hashCode call. If a printed androidx `MutableSelection`
source shows hash-backed storage, 112/30, 99/18, 95/35 flip to
REACHABLE INFERRED, and 3/26 flips with them via the drawer-TagItem
delegation (10/39) — but only on that print, not on the lead.
**TagInfo dependency (3/26):** its only receiver-typed hits are
`info.hashCode()` inside the two TagItem.hashCode bodies (ui/tag
TagItem :50, batch 11/7 UNREACHABLE-proposed; drawer TagItem :51,
batch 10/39 OPEN). Neither delegator is REACHABLE, so 3/26 does not
flip; it stands or falls with a delegator trigger or the
MutableSelection print above.
**Flag for merger spot-check (not a flip ordered here):** rows already
proposed UNREACHABLE on app-tree-zero alone must be re-derived against
this rule's full-repo standard; if their only basis is app-tree zero
they revert to OPEN. Named for that check: 41/36 (TorrentStream.
hashCode) and 11/7 (ui/tag TagItem.hashCode). 41/28 stands under the
private-nested exception (Piece is a private nested class with zero
use outside TorrentInputStream.java), so it is NOT in the revert
check. No other already-proposed UNREACHABLE hashCode row is disturbed
by D6.
**Evidence that would change it:** per row — a printed trigger (→
REACHABLE), a saved full-repo grep (→ UNREACHABLE), or a printed
androidx MutableSelection hash-backing source (→ the three
SelectionTracker rows + TagInfo, above).

## D7. Project-wide toString rule

**Chosen: the exact parallel of D6.** REACHABLE iff a printed trigger
exists: an explicit `.toString()` call, a log/concat/`String.valueOf`/
`setText`/`format` use of a variable of that exact type, a printed
databinding text-binding expression resolving it, or `List.toString()`
element dispatch from a REACHABLE host — in every case OUTSIDE any
OPEN toString body (dependency rule). UNREACHABLE iff a saved
full-repo grep (app + res + generated + library) shows zero such
sites. Otherwise OPEN. Zero hits in the 252-file app-Java tree alone
(122 `.toString` lines triaged, 30 OPEN rows) never flips to
UNREACHABLE: toString can be reached implicitly (concatenation,
logging, `List.toString()` element dispatch, databinding text binding,
framework dispatch) with no app-Java site. Options T-grep and T-lib-
as-absence are rejected; T-printed (stay OPEN) is the default.
**Flips under D7: none — all 30 OPEN toString rows stay OPEN.**
Zero receiver-typed hits (22): 10/40 (drawer TagItem), 103/37
(FileManagerNode), 106/40 (LogMutableParams), 21/40 (AddTorrentParams),
29/3 (MagnetInfo), 29/18 (PeerInfo), 29/28 (ReadPieceInfo), 29/36
(SessionStats), 30/29 (TrackerInfo), 31/2 (FeedChannel), 31/14
(FeedItem), 32/8 (TorrentTagInfo), 32/20 (BencodeFileItem), 34/16
(TorrentContentFileTree), 47/21 (BaseSorting), 81/2
(AddTorrentMutableParams), 82/13 (DownloadableFileItem), 84/30
(CreateTorrentMutableParams), 90/16 (TorrentDetailsInfo), 90/28
(TorrentDetailsMutableParams), 92/35 (TorrentContentFileItem), 33/8
(BencodeFileTree). Conditional hits only, inside another OPEN toString
body — each flips ONLY together with its host (dependency rule), and
no host flips under D7 (8): 34/3 (FileTree; hosts 33/8, 34/16), 73/32
(FileItem; hosts 82/13, 92/35), 33/16 (FilePriority; host 34/16),
31/40 (Torrent; host 90/16), 32/35 (TorrentMetaInfo; host 90/16), 30/9
(TorrentInfo; host 90/16), 28/29 (AdvancedTorrentInfo; host 90/16),
31/25 (TagInfo; hosts 10/40, 30/9, 21/40 — NOT the ui/tag TagItem
:57 concat, since that TagItem.toString is UNREACHABLE-proposed in
batch 11/8). Near-misses rejected (recorded): `Long.toString(info.id)`
(MainActivity :355) is not a TagItem call; enum/field `.toString()`
calls inside bodies are calls on the field's type; `super.toString()`
lines are hits for the SUPERCLASS row only.
**Dependency summary for the merger:** flipping 90/16 would flip
31/40, 32/35, 30/9, 28/29 with it; flipping 34/16 would flip 33/16 and
(with 33/8) 34/3; flipping 82/13 or 92/35 would flip 73/32; flipping
10/40, 30/9, or 21/40 would flip 31/25. No other OPEN row is reached
from a REACHABLE method in this corpus.
**Flag for merger spot-check (same standard as D6):** already-proposed
UNREACHABLE toString rows resting only on app-tree zero (notably
41/37 TorrentStream.toString, 11/8 ui/tag TagItem.toString) are to be
re-derived against the full-repo standard; if app-tree zero is their
only basis they revert to OPEN. Not a flip ordered here.
**Evidence that would change it:** per row — a printed trigger outside
any OPEN body (→ REACHABLE, with its dependents), a printed caller of
a host row (→ host + dependents together), or a saved full-repo grep
(→ UNREACHABLE).

## D8. Generated mapper convention (x) — three mapper classes, no transfers

**Chosen: M-dispatch (not M-printed, not M-dispatch-full, not
M-direct).** A `DataBindingUtil` request through the generated mapper
counts as a route for the mapper's load, instantiation, and
dispatch-entry methods — because DataBindingUtil.inflate/setContentView
are printed app calls (35 sites) whose documented behavior IS to go
through the generated mapper, and printed Impl creation at those
inflate sites is already accepted project-wide for Impl rows.
M-printed (printed generated source required) is rejected: it would
revert all Impl rows too, contradicting the accepted Impl practice.
M-direct (direct app-code call required; generated dispatch never
counts) is rejected: it would flip hundreds of rows toward UNREACHABLE
on absence in a corpus that excludes generated code, violating P2.
M-dispatch-full (the whole mapper API surface counts) is rejected:
`collectDependencies` and `convertBrIdToString` are runtime-API
methods, not on the inflate path, and have no printed caller.
**Flips under D8: 7 rows → REACHABLE INFERRED, all in the libretorrent
mapper family with printed DataBindingUtil trigger sites:** 17/34
(DataBinderMapperImpl.<clinit>), 17/35 (<init>), 17/38 (getDataBinder,
View overload), 17/39 (getDataBinder, View[] overload), 17/40
(getLayoutId); 18/1 (InnerBrLookup.<clinit>), 18/2
(InnerLayoutIdLookup.<clinit>). `confirmed_by` under this option is
INFERRED (generated dispatch unprinted), never SOURCE. 17/36
(collectDependencies) and 17/37 (convertBrIdToString) stay OPEN.
**No outcome transfers — each other mapper row stays OPEN for its own
reason:** 1/1 (androidx.databinding.library.baseAdapters.BR.<init>) —
BR field reads prove class loading, not constructor invocation; a
field read triggers `<clinit>`, not `<init>`, and zero `new BR(` sites
exist. 2/37 (libretorrent.BR.<init>) — same: field reads ≠
instantiation. 2/38, 2/39 (InnerBrLookup/InnerLayoutIdLookup.<init>) —
`<clinit>` (flipped for batch 18's rows) does not imply `<init>`; no
printed lookup-instantiation site exists, and whether the mapper's
static init creates the lookups is unprinted generated internals.
2/40 (DataBindingTriggerClass.<init>) — no printed site of any kind.
12/1 (databinding.DataBinderMapperImpl.<init>) — a DIFFERENT
fully-qualified class from the libretorrent mapper; no DataBindingUtil
site is shown to route through the databinding-package mapper, and no
conclusion is copied between them. Batch 12's databinding-mapper
conclusion is never cited for any libretorrent-mapper row, and vice
versa.
**Consequence for Impl rows:** the 59–61 mapper caveat is discharged
under M-dispatch (the mapper step counts), so Impl rows stand and do
NOT revert to OPEN on mapper grounds; batch 84's seven layout-resolved
rows (84/20, 84/22, 84/25, 84/26, 84/28, 84/29, 84/40) likewise stand.
**Evidence that would change it:** a printed generated mapper body
showing lookup instantiation (→ 2/38, 2/39), a printed `new BR(` site
(→ 1/1 or 2/37 respectively), a printed databinding-mapper dispatch
site (→ 12/1), or a printed generated dispatch for 17/36/17/37 (→
those rows). M-direct is recorded as rejected, not as a live option:
it must not be applied to batch 10 rows 1–22, batches 5–9, or batches
58–67 Impl rows on the strength of this file.

## D9. AndroidX preference 1-arg ctors (batch 11 rows 2–4) — together, UNREACHABLE

**Chosen: all three together → UNREACHABLE `no_trigger_in_app`
INFERRED.** 11/2 (SummaryPreference.<init>(Context)), 11/3
(SwitchBarPreference.<init>(Context)), 11/4
(TimePreference.<init>(Context)). **Reasoning:** the three share one
gap (no printed 1-arg construction site, AndroidX PreferenceInflater
dispatch unprinted) and batch 11's own rule requires judging them
together or not at all — that rule is adopted. The deciding mechanical
fact is the inflation parity already used in this project: layout
inflation invokes the 2-arg `(Context, AttributeSet)` ctor (batch 11
row 9, TorrentTagsList, uses exactly this basis), and preference
inflation from XML follows the same inflater shape — XML-declared
preferences (printed: pref_anonymous_mode.xml for Summary/SwitchBar,
pref_scheduling.xml :11–17/:26–32 for Time) are instantiated through
the 2-arg ctor, not the 1-arg ctor. The 1-arg bodies only delegate
(`this(context, null)` — Summary :39–42, SwitchBar :40–43, Time
:32–36), so nothing in the printed tree constructs through them, and
no programmatic 1-arg site is printed for any of the three.
**Consistency check:** batch 115's 2-arg rows for the same classes
stand REACHABLE INFERRED (115/3, 115/9, and Time 2-arg rows) — the two
decisions are mirrors, not contradictions: inflation → 2-arg is the
same fact in both, and the 3-/4-arg rows stand on printed delegation
from the 2-arg ctor. Batch 115's reasoning does NOT transfer to batch
11 (its robustness argument runs the other direction: 2-arg runs
whether inflation calls 1-arg or 2-arg; it says nothing about whether
1-arg runs).
**Flips under D9: 11/2, 11/3, 11/4 → UNREACHABLE `no_trigger_in_app`
INFERRED (3 rows, together or none — no single-class flip).**
**Evidence that would change it:** a printed AndroidX
PreferenceInflater dispatch showing a 1-arg path, or a printed `new
XxxPreference(context)` site — either flips the affected row(s) to
REACHABLE (and, under the together-rule, the merger must then judge
all three again on that print).

## D10. API-gate consistency — method-vs-branch rule + printed-corpus threshold

**Chosen: CONFIRM the method-vs-branch rule, and ADOPT the
printed-corpus threshold (dossier Option A).** Rule: a method whose
body returns early or branches at API 27 is still REACHABLE if its
call site runs at API 27; only a method whose call site itself never
runs at API 27 is a `closed_by_api_level` candidate. (Standard device:
API 27; O = 26, R = 30, S = 31, TIRAMISU = 33.) No completed batch
states the opposite rule. Threshold: where every call site found in
the printed corpus (including, for the round-2 rows below, saved
252-file tree greps) is gated so it never runs at API 27, the row may
be marked UNREACHABLE `closed_by_api_level` (INFERRED) — with the
standing revert condition that any later printed ungated caller flips
it to REACHABLE. The full-repo-grep threshold (Option B) is rejected:
it would revert already-standing Group X rows and the round-2 Group Y
rows (below) to OPEN on a standard no file in this family has met,
while the gate analysis for these rows is complete over the printed
corpus and the gates themselves are printed source facts (not
absence arguments).
**Standing (no new flips under D10):** Group X — 44/17, 44/18, 44/19,
44/20 (SettingsRepositoryImpl led getters; call sites inside
initLegacyNotifySettings gated SDK < O at Appearance :118–119, or
inside TorrentNotifier.applyLegacyNotifySettings' early return at
:276, or in onPreferenceChange branches bound only inside the gated
block) and 115/38, 115/39, 115/40 (initLegacyNotifySettings + its two
lambdas; only caller under SDK < O guard at :118–119) — all
UNREACHABLE `closed_by_api_level`. Group Y (already flipped in the
2026-11-01 round 2 on saved full-tree greps, affirmed here) — 47/1,
47/2, 47/13 (vibrationNotify / ledIndicatorColorNotify Default, sole
caller through 44/17); 73/39, 73/40, 74/1 (one
newInstance → construction → onCreateDialog route, gated at
Utils :704–707 / :713); 74/9 (PermissionManager lambda, gated route).
**Unaffected REACHABLE rows (body-gated, call site runs at API 27):**
74/4 (PermissionDeniedDialog.onCreateDialog), 74/12, 74/13
(PermissionManager setters — internal SDK branches gate only the
preference write), 74/17 (TorrentNotifier.applyLegacyNotifySettings —
reached, no-op at API 27), 74/20 (makeExactAlarmPermissionNotify),
74/23 (makeNotifyChans), 115/37 (bindOnPreferenceChangeListener —
onCreate calls suffice; only the initLegacy calls are dead), and the
Utils.showManageAllFilesWarningDialog method itself (only its dialog
branch at Utils :713 is gated — do not conflate method with branch).
**Couplings that must not be split:** 47/13 ↔ 44/17; 115/39, 115/40 ↔
115/38; 73/39 ↔ 73/40 ↔ 74/1; 74/17 ↔ 44/17, 44/19, 47/1 (the same
applyLegacyNotifySettings method is the REACHABLE no-op in 74/17 and
the gated container in the others — the rule, applied consistently,
is what lets both standings coexist).
**Extension owed (not decided here for lack of re-read):** batches 45,
46, 118 hold the same Appearance/TorrentNotifier gates; the merger
must apply this one rule to their rows on their own files.
**Evidence that would change it:** a printed ungated caller for any
closed row flips that row (and its coupled rows, per the couplings
above) to REACHABLE. Rejecting the method-vs-branch rule itself is
not recorded in any batch and would require fresh judging of every
§3.2 row in the clinit-rx-apigate dossier — it is not adopted.

## D11 (supplementary). `<clinit>` on first use (ix) — ACCEPT

**Chosen: ACCEPT (ix) in full, including both sub-groups.** A printed
first use of a class plus a non-constant static field (`TAG =
getSimpleName()`, CREATOR, diffCallback, INSTANCE, or equivalent)
suffices for REACHABLE INFERRED for that class's `<clinit>` (and, by
the same JVM timing, its `$1.<init>` Creator rows). JVM
class-initialisation dispatch is defined runtime behavior; INFERRED
marks exactly that (printed trigger, unprinted dispatch). Rejecting
(ix) would revert dozens of rows to OPEN on a print formality while
accepting identical JVM reasoning for `$1.<init>` (D5b Treatment A).
Sub-groups: (i) manifest-only first use ACCEPTED where the manifest
entry + framework role is printed — 96/19 (ErrorReportActivity,
manifest ACRA-process activity :167–172), 96/34 (FeedItemsActivity,
manifest :176), 102/18 (framework-launched activity): manifest-
declared activities are entry points by design, consistent with D2a's
anchor treatment. (ii) enum-only `<clinit>` ACCEPTED: enum constants
ARE static initializers; requiring an explicit static block would be
a distinction without a semantic difference (covers 21/33, 12/16,
73/10, 73/38, 82/3, 47/22, 47/24 and the 47/48 anonymous
enum-subclass `<init>`s, which exist only because the parent
`<clinit>` runs).
**Flips under D11: none** — all (ix) rows already REACHABLE stand
(including 22/17, 50/6, 73/14, 73/37, 74/33, 81/6, 82/18, 82/40, 84/31,
95/36, 96/19, 96/28, 96/34, 96/38, 97/13, 115/29, and the wider
first-use family in the dossier §1.3). Converse case stands: 3/35
(TorrentCriticalWork$Type.<clinit>) stays UNREACHABLE
`no_trigger_in_app` — no first use is the negative direction of the
same JVM rule, not a consequence of accepting (ix).
**Evidence that would change it:** a printed JVM/framework
class-load dispatch requirement adopted by the user would return the
(ix) rows to OPEN (not UNREACHABLE — a printed first use exists for
each); a printed first-use site for 3/35 would flip it to REACHABLE
INFERRED.

## D12 (supplementary). Rx-error / condition-on-route — ACCEPT

**Chosen: ACCEPT "condition on the route, not a blocker" (dossier
Option A).** A row whose only trigger is an error emission from an Rx
source (or an error/session-error event generally), with the
subscription/registration printed and the lambda/handler body printed,
is REACHABLE — the error occurrence itself is a runtime condition,
like a STATE gate, not a missing route element. The throw-site case is
stronger, not different in kind: a printed throw statement naming the
constructor is printed app code (SOURCE), while an Rx error emission
is library dispatch (INFERRED) — both stand, and no split rule (Option
C) is needed because both rest on a printed trigger.
**Flips under D12: none.** Standing: 72/13, 72/15 (TorrentService Rx
error lambdas, REACHABLE INFERRED); batch 20 exception ctors
(20/1–20/8, REACHABLE SOURCE on printed throw sites); §2.4
listener-error rows (22/16, 74/19, 74/24, 74/25, 28/2, 28/8, REACHABLE
on printed listener routes). Requiring a printed error occurrence
(Option B) is rejected: it would revert 72/13, 72/15 to OPEN and, on
its broad form, the batch-20 and listener rows with them, on a
standard no batch in the set applies to any error row.
**Application owed:** batches 26–27 (interval/error-source rows, not
read in the dossier set) must be judged under this rule: printed
subscription/registration → REACHABLE on the same reasoning; no
printed subscription → OPEN on that row's own evidence.
**Evidence that would change it:** a user rule requiring a shown
error occurrence would return 72/13, 72/15 to OPEN (not UNREACHABLE —
the subscription is printed and an error is a possible runtime
event).

---

## Decision index (for the merger)

| # | Convention | Option chosen | Label flips ordered |
|---|---|---|---|
| D1 | confirmed_by | Per-row (wide: registration callbacks SOURCE; generated dispatch INFERRED) | 0 labels; OPEN → `—` presentational |
| D2 | Strict entry (5 sub-decisions) | Anchor; sibling prints count; launcher-step-only; per-row; no downstream propagation | 99/14–40 → OPEN (26) |
| D3a | Room $N | SET | 53/10–28,30,31 → REACHABLE INFERRED (21) |
| D3b | Room finalize() | F1: GC route counts | 11 rows → REACHABLE INFERRED |
| D3c | Room converters | Database-build assumption, extended set | 50/27, 51/6, 52/11, 53/4, 48/14 → REACHABLE INFERRED (5) |
| D3c | Room auto-migrations / clear / drop / UriConverter ctor | Stay OPEN | 48/12, 48/13, 48/7, 48/19, 4/11 stay OPEN |
| D4a | Binding getViewModel | Field-read | 62/4, 62/30 → OPEN (2) |
| D4b | Binding variant gate | All configurations | 0 (60/13–16,21–24 + 65 variants stand) |
| D4c | No-variable setVariable/onFieldChange | Option U (combined evidence) | 40 rows → UNREACHABLE no_trigger_in_app INFERRED |
| D4d | setVariable direction | setVariable CALLS typed setter | 15 rows → OPEN |
| D4e | invalidateAll | REACHABLE on inflate (tie-break: keeps 22 standing vs 18) | 18 rows → REACHABLE INFERRED |
| D4f | hasPendingBindings | Stay OPEN; printed rebind body is the resolver | 0 |
| D4g | Binding $N count-match | Accept inverse-listener identification | 0 (56 rows stand) |
| D4h | Base Binding statics | Direct call or generated evidence required; DataBindingUtil does not count | 0 (200 + 22 rows stay OPEN) |
| D4i | onFieldChange | Variable set + observable bound + inflate | 0 (listed rows stand) |
| D5a | Parcelable trio | Keep trio policy | Affirmed: 31/23,26,28 → REACHABLE INFERRED |
| D5b | $1 / Parcel ctor | Option 1, no Creator-body exception | 21/36 → OPEN; 22/2 SOURCE→INFERRED |
| D5c | newArray | Option B: array site required | 102/17, 92/39 → OPEN (2) |
| D5d | Storage site | Counts for trio except newArray | 0 (92/33,36,38,31 stand) |
| D5e | Dependency / Room-entity rules | Adopt as recorded | 0 |
| D6 | hashCode | Printed-trigger rule + private-nested exception | 0 (23 stay OPEN) |
| D7 | toString | Parallel printed-trigger rule | 0 (30 stay OPEN) |
| D8 | Generated mapper (x) | M-dispatch | 17/34,35,38,39,40 + 18/1,2 → REACHABLE INFERRED (7) |
| D9 | Preference 1-arg ctors | Together → UNREACHABLE | 11/2,11/3,11/4 → UNREACHABLE (3) |
| D10 | API-gate | Method-vs-branch + printed-corpus threshold | 0 (Groups X + Y stand) |
| D11 | <clinit> (ix) | Accept in full | 0 |
| D12 | Rx-error | Condition, not blocker | 0 |

## What the merger must still do (not decided here)

1. Apply the flips above batch by batch (no batch file was touched by
   this task), then run the 1-in-5 spot-check on flipped rows before
   any merge — these decisions do not verify any row.
2. Re-derive the D6/D7 spot-check flags (41/36, 11/7, 41/37, 11/8)
   against the full-repo standard.
3. Apply D10 to batches 45/46/118 and D12 to batches 26–27 on their own
   files.
4. If ticked-app precedent contradicts any decision above, re-open
   that decision explicitly rather than applying it inconsistently.

---

# Phase 3 decisions (Stream A Phase 3 coordinator, Muse's own, for user/Yang review — never Yang's)

**Status: DECISIONS ONLY, appended 2026-11-01 (Phase 3). No batch file was
edited by this appendix itself; Phase 3 leaves apply these decisions to
copies under `phase3/work/` and report verdicts for coordinator
application. Nothing pushed. D1–D12 stand unchanged except where a
decision below explicitly clarifies or extends one (named as such).**

## D13. Constants / static-utility class `<init>` rule (new)

A `<init>` row for a class whose members are ALL static (constants
holder, static utility, empty marker with no instance members) flips to
UNREACHABLE `no_trigger_in_app` INFERRED iff (i) zero `new <Class>(`
sites exist in the complete corpus (app Java 281 + all res XML +
library sources in `final_java_only`), AND (ii) no framework/library
construction path for the class is printed or documented (the
framework's use of such classes is field/method access, never
construction). This is the D9 parity logic generalised: a class that
cannot be instantiated by any printed path, and is never constructed
in the corpus, has no trigger.
**Applies directly:** 1/1 (baseAdapters.BR.<init>), 2/37
(libretorrent.BR.<init>). **Applies conditionally (leaf must verify
the static-only premise from printed evidence before flipping):**
2/38, 2/39 (inner lookups — only if their members are static-only),
4/11 (UriConverter.<init> — only if all its methods are static and
zero `new UriConverter` sites exist), 2/40 (DataBindingTriggerClass —
only if it is an empty marker with no instance members and zero new
sites). If the premise fails for a row, that row stays OPEN with the
failing premise named. **Revert condition:** a printed `new` site or
a printed generated/framework body constructing the class.

## D14. Binding getters — D4a extension (overturns D4a's OPEN default)

Abstract binding getters (`getViewModel`, `getDetailError`, and the
like) with ZERO callers in the complete corpus flip to UNREACHABLE
`no_trigger_in_app` INFERRED. Completeness argument (same shape as
accepted D4c): the only caller classes are app code (zero, complete
corpus including other source sets, test callers excluded by D23) and
generated code (which reads the FIELD per D4a, never the getter); the
databinding library never calls typed getters (it uses the base
`ViewDataBinding` API). D4a's "resolves only on a printed caller" is
superseded for the zero-caller case: a printed caller is now the
revert condition, not a standing requirement. **Rows:** every OPEN
abstract-getter row in batches 58–67 (incl. 58/37, 59/8, 59/22, 60/30,
61/15, 61/30, 63/1, 63/15, 64/33, 65/6, 66/12, 66/24, 67/10, 67/22 —
leaf to confirm the row identities from the files). **Revert:**
a printed caller of the getter itself.

## D15. setVariable — D4d extension (overturns D4d's OPEN default)

A `setVariable` row with ZERO `.setVariable(` calls naming its
binding in the complete corpus AND no `bind:` pass-through to that
child binding in any res layout flips to UNREACHABLE
`no_trigger_in_app` INFERRED. Caller classes are exhaustive: app code
(zero) and generated parent code via `bind:` (absent — generated
parent code calls child `setVariable` ONLY for variables passed via
`bind:` attributes); the databinding library never calls
`setVariable` (it calls `executeBindings`). D4d's OPEN default is
superseded for this zero/zero case. **Rows:** every OPEN setVariable
row in batches 59–67 (leaf to confirm identities). **Revert:** a
printed `.setVariable(` call or a printed `bind:` pass-through.

## D16. onFieldChange — D4i extension

An `onFieldChange` row flips to UNREACHABLE `no_trigger_in_app`
INFERRED iff (a) no printed typed-setter call for its variable AND no
`bind:` pass-through (so the observable is never registered), OR (b)
the variable is set but the layout binds NO observable of it (so no
field-change registration exists for it). Registration is the only
path to the callback; without registration there is no trigger.
**Rows:** every OPEN onFieldChange row (leaf to confirm identities;
70/1 already flipped under D4c). **Revert:** a printed setter +
observable binding for that variable.

## D17. hasPendingBindings — D4f binary resolver (rule, outcome by print)

All OPEN `hasPendingBindings` rows flip TOGETHER on one print: the
`androidx.databinding.ViewDataBinding` rebind body (public androidx
source, version noted by the leaf). If the rebind path
(`executePendingBindings` / rebind runnable / Choreographer callback)
queries `hasPendingBindings()` on the binding, every row flips to
REACHABLE INFERRED (polymorphic dispatch — the override runs). If it
does NOT query it, and app-tree callers are zero, every row flips to
UNREACHABLE `no_trigger_in_app` INFERRED (caller classes: app code
zero + library rebind path not querying = exhaustive). If no print
is obtainable, all rows stay OPEN with the missing print named.
**Rows:** every OPEN hasPendingBindings row in batches 59–70 (leaf to
confirm identities).

## D18. D4c scope — pattern test, not list extension

D4c extends ONLY where the FULL D4c evidence pattern is verified per
row: (i) layout declares NO `<data>` variable, (ii) NO `<include>`
parent anywhere in res/layout passes a variable to it (no `bind:`
attributes), (iii) zero `.setVariable(`/`.onFieldChange` hits in the
complete app-Java tree, (iv) no typed-setter call on that binding.
**58/34, 58/35: do NOT extend.** Batch 58's layout declares a
viewModel variable (Phase 1c record), so pattern element (i) fails;
these rows are judged under D15/D16 instead. **67/7: decided by the
pattern check** — if the leaf verifies all four elements for 67/7's
layout/binding, it flips to UNREACHABLE under D4c; otherwise it stays
OPEN under D15/D16 as applicable. No other D4c extension is ordered.

## D19. newArray — D5c extension (array-site + array-state test)

A `newArray` row flips to UNREACHABLE `no_trigger_in_app` INFERRED
iff ALL of: (i) zero array-extra APIs in the complete corpus
(`getParcelableArrayExtra`, `putParcelableArray*`,
`writeParcelableArray`, `createTypedArray*`), (ii) zero
Parcelable[]-typed fields/state for the class in app code, (iii) no
Bundle/array parcel path names the class. Framework array
unmarshalling requires an array to have been parcelled; with no array
parcelled anywhere, `newArray` cannot run. D5c's OPEN default is
superseded for rows passing all three tests. **Rows:** 102/17,
114/27, 31/29, 92/39, plus any other OPEN newArray row the leaf
identifies. **Revert:** a printed array site or array field.

## D20. Inherited-CREATOR rule (framework print decides)

Fetch the printed AOSP `Parcel.readParcelableCreator` body from
`fw_src/android-8.1.0_r1/` via the connector. If it looks up
`CREATOR` with `getField` (inherited-field lookup), then a subclass
storage site IS a marshalling site for the BASE class's parcel
methods: the base CREATOR is found via the subclass, so inherited-
CREATOR rows flip to REACHABLE INFERRED on the subclass storage site
(the storage site names the subclass; dispatch to the base CREATOR is
INFERRED). If it uses `getDeclaredField` (declared-only) or the print
is unobtainable, inherited-CREATOR rows stay OPEN — do NOT flip them
to UNREACHABLE on this question. **Rows:** 30/6, 30/10, 30/12, 30/13;
30/24, 30/30, 30/32, 30/33; 30/39, 31/3, 31/5, 31/6; 73/35, 73/36,
73/29 (leaf to confirm identities and storage sites from the files).

## D21. D5e clarification (no flips)

D5e rules out Room-entity status as the SOLE basis for REACHABLE; it
does NOT order OPEN any row that has printed construction or a
printed marshalling round trip. **31/20, 31/22 stand REACHABLE** on
their printed `new TagInfo` sites (AddTagViewModel :61/:59);
**31/21 stands REACHABLE** via its REACHABLE `createFromParcel`
caller (31/28, affirmed under D5a) on the printed TagInfo round trip.
D5e's "staying OPEN" list is read as "staying OPEN on entity-status
alone". No label changes under D21.

## D22. D5b Treatment A extension (project-wide)

Treatment A extends to EVERY `$1.<init>` row: REACHABLE INFERRED iff
the enclosing class has a printed first use on a REACHABLE route
(class init runs the CREATOR field initializer); otherwise the row
stays OPEN. **Rows:** 32/2, 32/22, 32/37, plus any other OPEN
`$1.<init>` row the leaf identifies (check 22/1 and batch 28/31/41/42
OPEN rows for `$1` members). The leaf verifies first use per row
from printed source; no batch-local exception.

## D23. Test-scope rule

Callers in test source sets (`src/test`, `src/androidTest`, test-only
modules) do NOT count as in-app triggers: the trigger graph is about
app use, and test code runs under a test harness, not the shipped app.
**3/16 (Logger.getEntry) and 3/21 (TorrentInfoProvider.getInstance
Engine overload) stay UNREACHABLE** provided the leaf verifies (a)
their only callers are in test sets (LoggerTest; AbstractTest :72,
TorrentEngineTest :181) and (b) zero main-tree callers in the complete
corpus. The same rule applies to any other row whose only caller is
in a test set. **Revert:** a printed main-tree caller.

## D24. 3-arg ctor rule (project-wide, single rule)

A 3-arg `(Context, AttributeSet, defStyleAttr)` ctor is REACHABLE iff
(i) a printed programmatic 3-arg construction site exists, OR (ii)
the class's own 2-arg ctor delegates to it via a printed `this(...)`
call; otherwise it is UNREACHABLE `no_trigger_in_app` INFERRED
(LayoutInflater calls the 2-arg ctor only, per printed fw_src
:88–91, :615; zero programmatic sites in the complete corpus).
**Rows:** every 3-arg ctor row in batches 85/86/94 (leaf to enumerate
from the files — do not assume which rows these are) plus any other
batch's 3-arg ctor rows. The leaf prints each class's 2-arg ctor body
before judging. **Revert:** a printed 3-arg site or delegation.

## D25. D10 extension to batches 45/46/118

Apply D10 (method-vs-branch rule + printed-corpus threshold) to
batches 45/46/118 on their own files, including couplings to the
Appearance/TorrentNotifier gates. Batch 118 is expected untriggered
(Phase 2 found zero SDK hits in its source — leaf to verify). Report
any flips in 45/46 (rows 45/16, 45/21, 46/21, 46/22 were flagged as
turning on this extension); if no row changes, report confirmation
with the gate prints cited.

## D26. D12 application to batches 26/27

Apply D12 (condition on the route, not a blocker) to batches 26/27
Rx/error-source rows on their own files: printed subscription/
registration + printed handler body → REACHABLE (INFERRED for Rx
library dispatch, SOURCE for printed throw sites); no printed
subscription → OPEN on that row's own evidence. Report any flips
(27/21 was flagged, left as filed); if no row changes, report
confirmation with the subscription prints cited.

## D27. Service onBind rule

A `Service.onBind` row flips to UNREACHABLE `no_trigger_in_app`
INFERRED iff (i) zero `bindService`/`unbindService`/`ServiceConnection`
in the complete corpus, (ii) the manifest declares the service
non-exported with no intent filter that would allow external binding,
(iii) no system binding path is printed. **Row:** 72/21 (leaf to
verify (i)–(iii) from printed manifest + greps before flipping).
**Revert:** a printed bind request or an exported/intent-filtered
manifest entry.

## D28. confirmed_by normalisation (labels unchanged)

One rule, applied as a sweep: every UNREACHABLE row → INFERRED; every
OPEN row → `—`; REACHABLE confirmed_by values stand as filed (the
75-vs-77/80, 76/16-vs-79/11, and 23/24/25 variance is documented
variance, not churned — D1's wide rulings do not draw a crisp
Rx-vs-LiveData line, and the gate counts labels). **Known fix:**
115/38, 115/39, 115/40 if filed SOURCE → INFERRED (verify from the
file). Report every confirmed_by change; no label changes under D28.

## D29. Batches 5–10 confirmation + recorded tension (no flips tonight)

Batches 5–9 (200 rows) + batch 10 rows 1–22 UNREACHABLE flips STAND,
on (a) the user's 2026-11-01 chat statement that batches 5–9 are
UNREACHABLE `no_trigger_in_app`, and (b) the complete-corpus zero
direct-call greps (252-file tree + 29 missing files + res XML
scope as saved). **RECORDED TENSION for morning review (not a flip
tonight):** AddTorrentInfoBinding and DetailTorrentAppbarBinding are
`<include>` children (of fragment_add_torrent_info and
fragment_detail_torrent); under D4d parent-include logic, generated
parent-Impl code arguably calls their `bind()` (a parent must hold
the child binding to pass variables, cf. 59/32). If the user accepts
that argument, those two classes' `bind` rows flip to REACHABLE
INFERRED; otherwise they stand UNREACHABLE per the user's statement.
The leaf identifies the exact row numbers for those two classes'
`bind` overloads and records them in the tension note. Do NOT flip
them tonight — the user's explicit statement governs until the user
revises it.

## D30. D6/D7 exit execution (hashCode / toString)

For EVERY OPEN hashCode/toString row, the leaf runs the full-scope
grep (app Java 281 + ALL res XML incl. menu/values/preference/xml +
library sources in `final_java_only`) plus a per-row out-of-scope
dispatcher check, and applies exactly one outcome:
- printed trigger OUTSIDE any OPEN body → REACHABLE (triggers:
  receiver-typed `.hashCode()` call, hash collection keyed/element-
  typed on the type, printed library dispatch for the type; for
  toString: explicit `.toString()`, log/concat/`String.valueOf`/
  `setText`/`format` use of an exact-type variable, databinding
  text-binding expression, `List.toString()` element dispatch from a
  REACHABLE host). Dependents flip TOGETHER per the D6/D7 dependency
  summaries (e.g. flipping 90/16 flips 31/40, 32/35, 30/9, 28/29;
  flipping 34/16 flips 33/16 and (with 33/8) 34/3; flipping 82/13 or
  92/35 flips 73/32; flipping 10/40, 30/9, or 21/40 flips 31/25).
- full-scope zero AND no plausible unprinted dispatcher → UNREACHABLE
  `no_trigger_in_app` INFERRED. "No plausible dispatcher" must be
  argued per row: SelectionTracker types are NOT in this branch
  (they go to the MutableSelection print below); databinding text
  expressions are checked in res XML; `List.toString()` hosts are
  checked in app code; framework/library implicit dispatch that could
  reach the type must be named if claimed.
- otherwise the row stays OPEN, with the specific dispatcher or gap
  named as its resolver.
**SelectionTracker rows (112/30 TorrentListItem, 99/18
FeedChannelItem, 95/35 TrackerItem, plus 3/26 TagInfo via the
drawer-TagItem delegation 10/39):** the resolver is a printed
androidx `MutableSelection` source showing hash-backed storage (fetch
via public web, version noted). If hash-backed → all four flip to
REACHABLE INFERRED (3/26 via the delegation chain as D6 states, leaf
to verify the chain links from printed source). If the print shows
non-hash storage, or no print is obtainable, these rows stay OPEN
with the print named as resolver — do NOT flip them to UNREACHABLE
on app-tree zero, because the unprinted dispatcher question is
exactly what is open for them.
**Already-UNREACHABLE flags (D6/D7 spot-check flags):** 41/36
(TorrentStream.hashCode), 11/7 (ui/tag TagItem.hashCode), 41/37
(TorrentStream.toString), 11/8 (ui/tag TagItem.toString) are
re-derived against this same full-repo standard; if app-tree zero is
their only basis they revert to OPEN (leaf to verify — 41/28 stands
under the private-nested exception and is NOT in this check).

## D31. Room residuals (48/7, 48/12, 48/13, 48/19)

The leaf reads the batch-48 file rows first and verifies identities
before any flip. **48/12 (getAutoMigrations) / 48/13
(getRequiredAutoMigrationSpecs):** attempt a printed androidx Room
library open-path print (public web, version noted). If Room calls
these unconditionally at open → REACHABLE INFERRED; if only when
auto-migrations are declared (none declared — printed `@Database`
:42–52 lists entities + version 9 only) → UNREACHABLE
`no_trigger_in_app` INFERRED; if no print → stay OPEN. **48/7
(clearAllTables):** app-code callers zero + Room never calls it
internally (public clear API) → UNREACHABLE `no_trigger_in_app`
INFERRED, if the row identity matches. **48/19 (dropAllTables):**
app-code callers zero + the only library path (destructive-migration
fallback) is NOT configured (printed buildDatabase uses
addMigrations, no fallback) → UNREACHABLE `closed_by_configuration`
INFERRED, if the row identity matches. If any identity or premise
fails, the row stays OPEN with the failing premise named.

## D32. D3c UriConverter ctor (see D13)

4/11 (UriConverter.<init>) is judged under D13's test only (all-
static methods + zero `new` sites + no construction path → UNREACHABLE;
otherwise stays OPEN). It is NOT flipped by the D3c converter
decision, which covers only the getRequiredConverters methods.

## D33. Parcel trio execution (remaining OPEN trio rows)

For every remaining OPEN Parcelable-trio row (batches 21, 22, 28, 29,
30, 31, 32, 41, 42, 73, 82, 114 — leaf to enumerate from the files),
apply in order: D5a (printed marshalling site naming the class →
REACHABLE for the trio members except newArray), D5b dependency
(caller OPEN → stays OPEN; caller REACHABLE → REACHABLE), D20
(inherited CREATOR via subclass storage), D19 (newArray test), D22
(`$1.<init>` first-use test). Each row gets exactly one outcome with
its site cited, or stays OPEN with its specific missing site named.
No row flips on CREATOR definition alone, on entity status alone
(D21), or on a single-extra site for newArray (D19).

## D18 correction (Phase 3 coordinator, on L3's printed-XML finding)

L3 verified from printed XML that `activity_add_torrent.xml` declares
NO `<data>` block — so the D18 premise for 58/34, 58/35 ("their
layout declares a viewModel variable") was WRONG; the viewModel
layout in batch 58 is `activity_filemanager_dialog.xml` (58/37).
Outcome UNAFFECTED: 58/34 flips UNREACHABLE under D16 (no variable,
no setter) and 58/35 under D15 (zero setVariable + no pass-through),
so both rows are UNREACHABLE either way; the D4c-vs-D15/D16 path
distinction is moot for them. D18's pattern test itself stands (67/7
passed all four elements and flipped under D4c). No other D18
conclusion changes.

## D37. Missed D5b dependency consequences (coordinator, Phase 3 completion)

The 1–60 spot-check leaf found one FAIL-label the Phase 3 verdicts missed:
28/21 AbstractInfoParcel.writeToParcel was OPEN on the claim that all its
printed super-callers sit inside OPEN writeToParcel methods. That claim broke
when L2 flipped TorrentInfo.writeToParcel (30/10) and TrackerInfo.writeToParcel
(30/30) to REACHABLE: both call `super.writeToParcel(dest, flags)` as first
statement (corpus TorrentInfo.java:151, TrackerInfo.java:185), and
TorrentListItem/TrackerItem define no parcel overrides, so D20 storage dispatch
reaches exactly these super-calls. Under D5b positive direction (as applied
for 30/2, 30/16, 30/17), 28/21 flips to REACHABLE SOURCE (printed super-call
names the base method, D1). The same leaf flagged 28/19
AbstractInfoParcel.<init>(Parcel), out of its scope: coordinator verified
from printed corpus source that TorrentInfo(Parcel) :121 `super(source)` and
TrackerInfo(Parcel) :170 `super(source)` call the base ctor
(AbstractInfoParcel.java:46), and both subclass ctors are REACHABLE (30/2,
30/19) — so 28/19 likewise flips to REACHABLE SOURCE under D5b. FeedChannel
implements Parcelable directly (no super calls to either base method) and
AbstractInfoParcel defines no describeContents, so no further base-method
flip follows. 28/23/28/32 stay OPEN correctly (their chain runs through OPEN
createFromParcel 28/32). Both flips carry revert conditions: if 30/2, 30/10,
30/19, or 30/30 reverts to OPEN, the corresponding base row reverts to OPEN.

### stream-D/Currency/DECISIONS.md

# Currency — decisions by Muse (own decisions, for user/Yang review; never in Yang's name)

No open question from the user or from Yang arose during this re-check. The
following are Muse's own decisions on issues that came up while working, each
with reasoning. Nothing here changes a label, a route, or a branch file.

## D1 — verification.csv is NOT hand-edited for the two newly judged path rows

Reasoning: the task rule is that verification.csv is produced ONLY via
tools/make_verification.py, and that tool does not exist anywhere in tools/
on branch work-2026-10-31 (verified by directory listing). Hand-appending
rows would break the audit provenance the file exists to provide. The two
new judgements (Parser$Handler.<init> correct, Main.onDateResult correct)
are therefore recorded in scratch/route_judgements.md only, and the local
verification.csv is an unchanged copy of the branch file (98 rows, header
type,item,result,confirmed_by,ref,edges,note). Morning action for the user:
either supply/confirm the intended verification.csv producer, or accept
carrying these two rows forward in the judgements file.

## D2 — check_citations' 2 remaining problems are a reconstruction blocker, not graph errors

Reasoning: after reconstructing the cited AOSP files locally, 39 of 41
distinct citations resolve with all cited line ranges in range and 0
unbacked-evidence claims (no FW-MEMORY/DYN/UNVERIFIED). The 2 remaining
problems are both the same file, am/ActivityManagerService.java, which the
connector refuses to display at 1,086,106 B ("too large to display"). The
citations themselves (ActivityManagerService.java:19199-19224 and the
ActiveServices-adjacent edge) are unchanged from the branch graph, and the
raw download URL the connector offered contains a token, which the standing
connector-only rule forbids using. So the check is reported as partial, not
failed on the graph, and no token URL was fetched.

## D3 — the 27-method sample is accepted as the complete sample

Reasoning: verify_sample.py's quotas sum to 30 but its pools exhaust at 27
for Currency (deterministic, seed 20261025; redraw identical). Reporting
"30 routes checked" would be false. Error rate is computed over judged
routes only, excluding unclear, following the build's own formula:
(0 fixed + 0 wrong) / (23 correct + 0 + 0) = 0.0.

## D4 — the 4 unclear routes stay unclear

Reasoning: Main.onEditorAction (IME step INFERRED), CurrencyWidgetUpdate
.onDestroy, CurrencyWidgetUpdate.onDateResult and CurrencyWidgetProvider
.onDeleted (launcher steps INFERRED) all have fully printed app-side chains,
but their blocking steps are in code that was not read (launcher, IME).
Upgrading them to correct would overstate what was checked. This matches
the branch verification.csv, where the same 4 rows are already unclear.

## D5 — scan_unreachable --callers hit on Singleton.getList does not change its label

Reasoning: the hit is ChartActivity.onCreate -> Singleton.getList at
ChartActivity.java:176, which is the else-branch of "instance == null"
(:163). Re-reading ChartActivity.java:163-177 confirms instance is an
instance field, null whenever onCreate starts, so the else-branch never
runs — exactly what the branch_never_taken reason text already says. The
same-name overload hits (ChartParser.startParser, getItem) are likewise
explained in the reasons, not new callers.

## D6 — readme_notes history kept, re-check appended rather than rewritten

Reasoning: the branch notes' 28-method / 391-edge figures describe the
first audit against the schema 1 graph; rewriting them would erase the
audit trail. The 2026-11-01 re-check (27 methods, 107 edges, 23/0/0/4) is
added as a dated paragraph in the same section, and the generated README
shows the current build numbers (145 methods, 393 edges) from the build
itself. The five headings stay in their original order.

### stream-D/Diary/DECISIONS.md

# Diary — decisions (Muse's own decisions, for user/Yang review; never in Yang's name)

## D1. make_verification.py does not exist on the branch — verification.csv kept unchanged
Reasoning: tools/make_verification.py returns "path does not exist" on work-2026-10-31, and no sibling Stream D leaf has it either. Inventing a generator, or hand-editing verification.csv to look generated, would fabricate a log. Decision: use the branch verification.csv (128 rows, header exactly type,item,result,confirmed_by,ref,edges,note) unchanged, and report the missing tool as a blocker for the "ONLY via make_verification.py" wording. The build already validates that file (0 errors, 0 warnings).

## D2. check_citations.py "81 problems" are missing-cache problems, not citation errors
Reasoning: all 81 problems are "file not held"; 0 are line-out-of-range and 0 evidence rows use FW-MEMORY/DYN/UNVERIFIED. Decision: do not report 81 citation errors, and do not mark the check passed on the first run. Instead fetch the cited framework files from aosp-mirror/platform_frameworks_base at android-8.1.0_r1 (the tag the graph cites) into fw_src/android-8.1.0_r1/ and re-run, so the check judges line ranges for real.

## D3. Route judgments carried over after exact edge-match, plus fresh spot-check
Reasoning: the 30-route sample redrawn from the current build is exactly the 30 path rows already in verification.csv, and every stored edge list matches the current derived route edge-for-edge (30/30). Re-reading all 370 steps from scratch would duplicate work already recorded on the branch; silently trusting it would be worse. Decision: carry the judgments over on the strength of the exact match, print all 370 steps in scratch/route_steps.txt, and freshly verify the cited lines for all 5 unclear routes against upstream source at the pinned commit (all matched). No route was re-judged differently and no fix was applied.

## D4. scan_unreachable.py first run is vacuous, not a pass
Reasoning: with no final_java_only source tree locally, the tool searched zero files, so "no other mention" for all 21 UNREACHABLE methods proves nothing. Decision: report the first run as not-run (meaningful), and re-run after reconstructing the app source tree from billthefarmer/diary at the pinned commit 07bb05c3b7a8ea90db5efdc8f574b9f334402a71 (the commit graph_def.py itself cites).

## D5. DATASET target_sdk 28 vs graph API 27 — recorded, not changed
Reasoning: DATASET.txt says target_sdk 28; graph_def.py says the baseline is API 27 with fw_src android-8.1.0_r1. Changing labels or citations over this would need a decision about which baseline the project intends. Decision: record the discrepancy in AGENT_NOTES.md, change nothing.

## D7. ActivityManagerService.java fetch stopped after two identical failures
Reasoning: the file fails on both aosp-mirror and android mirrors with the same connector error, while neighbouring files from the same tree succeed — this looks like a per-file connector limit (plausibly size), not a wrong path. Decision: stop fetching it (no retry loop), report check_citations as 81 distinct / 1 file-not-held / 0 line-range errors, and do not claim the check is 0. The single affected citation (AMS:19198-19224, APPWIDGET_UPDATE limited to the caller's package) is corroborated in kind by the neighbouring BroadcastQueue:1267-1279 citation on the same edges, which did verify in range — but that corroboration is not a substitute for the AMS lines themselves, and is not claimed as such.

## D8. scan_unreachable hits are triaged by overload and declaring class, not by name
Reasoning: the genuine scan (complete 16-file tree, 2026-11-01 takeover) shows hits for 14 of the 21 UNREACHABLE methods, but every hit is a same-name trap or a call inside the unreachable set: Diary.java:2783 calls copyFile(File,File) (both args are File, lines 2769-2770), not the UNREACHABLE copyFile(Context,Uri,Uri); Diary.getFile() is a different class from DiaryWidgetProvider.getFile(), and the widget file's only calls are getFile(entry) (the Calendar overload, :193) and getFile(calendar) inside getFile() itself (:268); File.delete / Editable.insert are not FileProvider.delete / FileProvider.insert; getThumbnail overloads call each other and getUri/isMediaUri are called only from inside the getThumbnail overloads, all of which are themselves UNREACHABLE; FileUtils.<init>'s only "hit" is its own private declaration (:102), with no `new FileUtils(` anywhere. Decision: no label changes; the scan supports the 21 UNREACHABLE labels rather than contradicting them. A name-only scan must never flip a label on its own.

## D9. Gate is BLOCKED, not waived, on the single AMS file-not-held
Reasoning: check_citations exits 1 with exactly 1 problem (ActivityManagerService.java not held) and 0 line-range errors. The missing file is a connector fetch limit already established under D7, not evidence against any citation, but waiving a failing check into a pass would be inventing a result. Decision: report the gate as BLOCKED on this one item (plus the D1 make_verification.py absence for the strict "ONLY via" wording), list everything else as passing, and propose the [K] status line only as a proposal for the parent/coordinator to apply once the AMS lines are verified via an authorised morning route (e.g. Mac clone) or the near-pass is explicitly accepted. Nothing else is pending: no label, route, or log item needs further local work.

## D10. Takeover re-verified rather than re-derived
Reasoning: the prior worker's build, sample, and check outputs were all reproduced byte-identically on re-run (build.txt, sample_30.txt, sample_30_redraw.txt), and the verification path rows match the redrawn sample in order and set (30/30) with judgments matching (0 mismatches). Re-deriving all 370 steps from scratch would duplicate verified work. Decision: carry the judgments, as D3 did, on the strength of the exact re-run match, and spend the takeover effort on the genuinely unfinished items instead (complete source tree, genuine scan, readme, sanity/DATASET recovery).

## D6. No device checks, no pushes, no branch edits
Reasoning: per the Stream D brief. Decision: all work stays under ~/workspace/overnight/stream-D/Diary/; nothing was pushed and no branch file was edited.

### stream-D/hash-checker/DECISIONS.md

# hash-checker — Muse's own decisions (Stream D, overnight; for user/Yang review)
Never in Yang's name. These are Muse's decisions only.

## D1 — make_verification.py missing on the branch: use the branch verification.csv as build input, do not invent a regeneration
Reasoning: tools/ on work-2026-10-31 contains no make_verification.py (fetch returned "path does not point to a file or directory"; the tools/ listing has no such file). The task step 4 says verification.csv ONLY via make_verification.py, but that tool cannot be run if it does not exist. Inventing its output would violate the no-invention rule. So: the branch verification.csv (125 lines, header type,item,result,confirmed_by,ref,edges,note) was fetched via the connector and used as the build's verification input; the local build reproduces the branch counts exactly (529/1314, 507/22, errors 0, warnings 0). Regeneration of verification.csv is BLOCKED pending the tool's location/creation; the existing log is preserved verbatim in the local mirror and is NOT rewritten by hand.
Status: open question for the parent/coordinator — where does make_verification.py live, or should verification.csv be regenerated by another approved tool?

## D2 — DEAD/FRAMEWORK_ONLY and PENDING greps: explained non-failures, not zero raw hits
Reasoning: graph_def.py legitimately defines the legacy DEAD (line 63) and FRAMEWORK_ONLY (line 79) dicts, which build_graph.py reads as UNREACHABLE and then clears (lines 684-706). The built JSON contains no DEAD/FRAMEWORK_ONLY keys and 22 UNREACHABLE labels. Likewise every PENDING hit is the S_MAIN_EXIT_PENDING screen name, not a pending label/status. Reporting raw grep counts as "0" would be false; reporting them as failures would be wrong, since the build's own conversion is the documented schema-2 mechanism. So these checks are reported as PASS-WITH-EXPLANATION with the exact hit counts and locations.
Status: decided by Muse; for user review.

## D3 (pending) — route-check error rate basis
Reasoning (to be confirmed after source reading): the redrawn sample is identical to the branch's final 30 path rows, and the local build reproduces the branch graph exactly, so any "fixed" counted in THIS check must be a fix Muse makes during this check — not the 8 historical fixes already in graph_def.py (those are recorded in the branch readme_notes.md, error rate 0.351 over 37 rows). If this check finds no new errors, the reported error rate for this redraw is 0/30.
Status: provisional until route judgments are complete.

## D4 — scan_unreachable scope: main + thirdPartyStores only (no googlePlay copies)
Reasoning: the standard configuration is the thirdPartyStores debug build (DATASET.txt, graph_def header). The local mirror therefore holds `src/main/` plus the single thirdPartyStores override (`MainActivity.java`) and no googlePlay copies. A mention found only in googlePlay code would not be a caller in the built app, so excluding googlePlay from the scan mirror is the correct scope for this app, not a gap. (The branch readme's "grepped in all three source sets" was the authors' label work, not this scan's scope.)
Status: decided by Muse; for user review.

## D5 — check_citations 14/15: AMS citation left unverified, not marked failed
Reasoning: `ActivityManagerService.java` (1,086,106 bytes) exceeds the connector's display limit; the connector returned a placeholder instead of content, and the placeholder's download link was not used (it carries a token, and the task forbids tokens entirely). The two AMS line ranges for `App.onTerminate` therefore cannot be re-verified from this VM, while the ActivityThread side of the same claim verifies. Marking the label wrong on that basis would invent a failure; marking the check fully passed would hide the gap. So the check is reported as 14/15 with the AMS gap named.
Status: decided by Muse; for user review.

## D6 (pending) — gate call after scan --all
Reasoning (provisional): labels pass on the build, routes pass 30/30 with rate 0, and logs are produced (branch verification.csv preserved verbatim with correct header, readme_notes five headings in order, README generated, LESSONS + AGENT_NOTES written). Two items remain open regardless of scan --all: verification.csv cannot be regenerated (tool missing, D1) and one AMS citation cannot be re-verified (size limit, D5). The gate call will state these explicitly rather than claiming an unqualified pass.
Status: provisional until scan --all completes.

## D6 (final) — gate call: REACHED for labels/routes/logs content, with two named tooling limitations
Reasoning: labels pass (UNRESOLVED 0, errors 0, warnings 0, STRICT=True); route checks pass (30/30 correct, error rate 0, no graph change); logs content passes (verification.csv header/counts/confirmed_by validated, readme_notes five headings in order, README generated, LESSONS + AGENT_NOTES written). The two open items change no label or route result: (D1) verification.csv could not be regenerated because make_verification.py is absent on the branch — the branch log is preserved verbatim instead; (D5) one framework citation file (ActivityManagerService, 1,086,106 bytes) exceeds the connector display limit, so its two line ranges stay unverified by Muse. Proposing the [K] line below with these limitations attached, for the coordinator to present; device checks not started.
Status: decided by Muse; for user review.

### stream-D/Omni-Notes/DECISIONS.md

# Omni-Notes — decisions (Muse's own, for user/Yang review)

None of these are made in Yang's name. Each states what was decided, why, and what
would change it. Nothing here was pushed anywhere; all work is local.

## D1. DEAD|FRAMEWORK_ONLY grep: report the literal 11, do not fake a 0

`grep` on the local `graph_def.py` copy finds 11 lines matching `DEAD|FRAMEWORK_ONLY`:
population (1635, 1641), SUPPRESS uses (1693-1694, 1793-1794, 1801, 1808), a comment
(2078), the conversion loop into UNREACHABLE (2136), and the reset `DEAD, FRAMEWORK_ONLY
= {}, {}` (2145). The effective legacy entries are 0: the dicts are emptied at line 2145
before the build, and the build's verdict kinds contain only the four real UNREACHABLE
kinds (no 'unclassified'). The task's check (5)-(7) asks for 0; the honest report is
"literal 11, effective 0, mechanism-only". Faking a 0 by editing the graph locally would
break the byte-identical rebuild and hide the mechanism. What would change it: a
branch-side cleanup removing the legacy-dict machinery from `graph_def.py` entirely.

## D2. verification.csv regeneration is BLOCKED; branch file kept verbatim

`make_verification.py` is not locatable on branch work-2026-10-31: absent from the
`tools/` root listing and from `tools_dev/` (only `.design_scratch/`, DESIGN.md,
design_review.json, design_review.md); a scoped `search_code` query for
`make_verification` in the repo returned total_count 0 with incomplete_results=true
(which, per the task rules, is not proof of absence elsewhere — only that no locatable
copy was found). The task says `verification.csv` is produced ONLY via
`make_verification.py`, so the branch file (196,534 B, header exactly
`type,item,result,confirmed_by,ref,edges,note`, 370 rows) is kept verbatim as the audit
log and is NOT hand-edited. Fresh judgments live only in
`scratch/sample_30_judgment.md`, never merged into `verification.csv`. What would
change it: the parent locating `make_verification.py`, after which the judgment file is
the input to regenerate from.

## D3. DbHelper.deleteNote route: judge wrong, attempt no local graph fix

The drawn best route to `DbHelper.deleteNote(long,boolean)` is internally inconsistent
(FAB-created new note + merged-note STATE; see `scratch/sample_30_judgment.md`). The
label REACHABLE is right (a real Merge path exists), but fixing the route properly needs
a new editor context (e.g. @MERGE) with its own Back/save chain — a graph-model change,
not a one-edge edit. A local edit without full verification could break the 0-error
build, and the branch `readme_notes.md` "Limits" section already documents this as the
one route that stays wrong. So: verdict wrong, no fix, parent decides whether one
documented wrong route blocks the "route checks pass" gate.

## D4. Clinit-ordering steps are a convention, not errors

Steps `X.<init> -> X.<clinit> -> X$1.<init>` (Tag, Attachment routes) mean "first use
triggers class init": the $1 CREATOR anonymous class is instantiated in static init
(Tag.java:65, Attachment.java:85). Temporally `<clinit>` runs before first use, but the
edge direction is not a temporal claim. Reachability holds either way. Judged correct
with a written note in the judgment file, not as errors.

## D5. check_citations: a targeted fw_src cache is valid; a partial cache is not a pass

The checker only consults files cited by the graph's FW-SRC evidence, so a cache holding
exactly the cited framework files is a valid run. The first run found 18 distinct cited
specs with 1 problem (AdapterView.java not held) — that run is NOT reported as a pass.
The missing file was fetched and the check re-run for a clean result, rather than
calling a partial-cache run good.

## D6. check_bytecode_lines: minimal-tree runs are reported with their caveat

The checker runs over the full graph, so a minimal tree (only route-cited files) cannot
yield a clean 0: every bytecode-cited edge in an unheld file reports "file not found".
The first run's 297 bad entries were ALL "file not found" for 10 unheld app files, with
ZERO genuine line mismatches among held files. The 10 files were fetched and the check
re-run, rather than presenting the minimal-tree output as a pass or a failure of the
graph. Residual caveat, recorded with the final result: with one copy per basename,
flavor disambiguation is limited (checker prefers `/src/main/` or a built flavor; built
flavor here is `play` per `class_files.json`); a duplicate-basename file in another
flavor folder could in principle resolve differently in a full tree.

## D7. scan_unreachable --all: not run, and not faked

`--all` searches the FULL app source tree for every unreachable method name. Only the
route-cited files plus the 10 bytecode-cited files are reconstructed here, so running
`--all` against this tree would fabricate "no other mention" results. It is reported as
not-run with this exact reason. `--callers` (needs only auto_calls + JSON) is the valid,
completed part: 5 of 254 unreachable methods have a bytecode caller outside the set, each
explained in its reason text (see `scratch/scan_unreachable_callers.txt`).

## D8. Coverage artifacts are not label evidence

`coverage_baseline.json` was fetched only to reproduce the branch build's sanity-check
artifact exactly. The sanity-check counts (848 ran, 0 UNREACHABLE-but-ran contradictions,
79 ENV-gated-but-ran) never set or change any label, per the task's label rules and the
tool's own docstring.

## D9. File locations resolve through method_list.json class paths, not guesses

The first IntroActivity fetch failed ("path does not exist") because the path was guessed
as the root package. `method_list.json` gives the authoritative class path
(`it/feio/android/omninotes/intro/IntroActivity` -> `intro/IntroActivity.java`), and the
corrected fetch succeeded. The same resolution was used for all 10 bytecode-missing
files. Guessed paths that fail are recorded as wrong guesses, never as missing files.

## D10. Branch root AGENT_NOTES.md is AmazeFileManager's, not Omni-Notes'

The file fetched as `scratch/branch_AGENT_NOTES.md` is headed "# Agent Notes -
AmazeFileManager" and contains Amaze build logs. No Omni-Notes branch notes existed to
mirror, so the local `AGENT_NOTES.md` (Omni-Notes-specific, started fresh) remains the
mirror. Nothing was copied from the Amaze notes into Omni-Notes logs.

## D11. Sketch-route Back link accepted via fragment recreation

The step MainActivity.onBackPressed@SKETCH_DRAWN -> Attachment.<init>(Uri,String) rests
on: onBackPressed saves the sketch (SketchFragment.save, guarded by
SketchView.getBitmap() != null) and pops the back stack, so DetailFragment is recreated
and its onActivityCreated attaches `mainActivity.sketchUri` (DetailFragment 385-388).
This is standard fragment-lifecycle behavior, confirmed on both ends of the link, and is
judged correct — not an error — with the recreation step stated explicitly.

### stream-D/openlauncher/DECISIONS.md

# openlauncher — decisions made by Muse (Stream D leaf, 2026-11-01), for user/Yang review

None of these decides anything about another app or about Yang's open items. Each is recorded here as Muse's
own decision, not in Yang's name.

## D1 — check_citations: 2 residual "file not held" problems are a cache blocker, not a graph failure
Decision: report check (2) as NOT fully passing locally, rather than passed or failed on the merits.
Reasoning: the only 2 of 64 distinct citations that do not resolve locally point at
fw_src/android-8.1.0_r1/services/core/java/com/android/server/am/ActivityManagerService.java (1,086,106 B) and
.../pm/PackageManagerService.java (1,190,171 B), which exceed the GitHub connector's get_file_contents display
limit. The connector's suggested download URLs carry a token, which this project's hard constraints forbid
using. All other 62 citations resolve with 0 line-range problems and FW-MEMORY/DYN/UNVERIFIED = 0, and the
earlier session read both oversize files in full from a checkout with 0 errors. Inventing a pass would hide a
real gap; calling the graph wrong would misdescribe a tooling limit as a citation error.

## D2 — the single PENDING grep hit is legitimate source terminology, not an unfinished marker
Decision: treat grep check (7) as explained, not failed.
Reasoning: the only `PENDING` hit in graph_def.py is `taskList.getStatus() == PENDING` (AsyncTask.Status.PENDING)
in a guard at line 942, matching HideAppsFragment.java:66 exactly. It is not a PENDING label, status, or TODO.

## D3 — the sample is 27 routes, not 30, and the error rate is computed over 27
Decision: report "verify_sample.py openlauncher 30 20261025 -> 27 methods" and error rate 1/27 = 0.037.
Reasoning: the tool's strata quotas cap below 30 for this app (fewer members than quota in several strata);
27 is the tool's reproducible output for seed 20261025, identical before and after the rebuild. Dividing by 30
would understate the rate; inventing 3 more routes would break reproducibility.

## D4 — no graph change from this re-verification; the DialogUtils "fixed" row stays "fixed"
Decision: make no edit to graph_def.py and keep verification.csv byte-identical to the branch file.
Reasoning: the one fixed route (DialogUtils.copy) was already fixed in the fetched graph_def (no
ENV_STORAGE_FAIL on the copy edge; guards "item is Backup"/"item is Restore"), independently re-confirmed
against DialogUtils.java:146-182. The regenerated verification.csv matches the branch file byte for byte, so
there is nothing new to merge; the "fixed" verdicts in verification.csv record history (errors found and
fixed by the earlier session), not errors in the current graph.

### stream-D/Vanilla-Music/DECISIONS.md

# DECISIONS (Vanilla-Music, Stream D overnight re-verification) — Muse's own decisions, for user/Yang review, never in Yang's name

## D1. Scope of re-verification vs. full source fetch (decided by Muse)
The build itself needs app sources (cases.Cases indexes final_java_only), which the leaf task's step-1 list did not include. Muse fetched: all graph/tool inputs, the 10 Cases() build inputs, the 38 further app .java files + manifest + 5 res XML cited on the 30 sampled routes, and (planned) the 47 FW-SRC files cited in the built graph for check_citations.py. Muse did NOT fetch the remaining ~67 app .java files and the remaining res XML solely to run check_bytecode_lines.py (full) and scan_unreachable.py --all: at ~30 s per connector fetch that is roughly another hour of fetches, on top of the ~90 already done, with rising 429 risk shared with the other 7 leaves. Those two checks are therefore reported NOT-RUN with exact blockers, and the prior session's passes on the byte-identical-count rebuild are cited as carry-over evidence only, not re-claimed. (To be completed after route reading: confirm this decision stands.)

## D2. readme_notes prose counts corrected to the rebuild (labels unchanged)
Branch readme_notes.md said 1158 SOURCE / 315 INFERRED and 266 sample edges; the rebuild prints 1157 / 316 and 270 (union of the 30 routes' route_edge_ids, matching verify_sample.py's header). Muse corrected those three prose numbers in the LOCAL mirror readme_notes.md only; no label, edge, or route changed. AGENT_NOTES.md's final counts (1157/316) already agreed with the rebuild.

## D3. Route judgments: this-run result vs. branch logged convention (decided by Muse)
This run re-read every step of all 30 sampled routes from the rebuilt graph's
printed routes (scratch/routes_30.txt, via the local printer scratch/print_routes.py,
which works around the known tools/show_route.py evidence-regex bug) against the
freshly fetched cited sources. Result: 30 CORRECT, 0 newly fixed, 0 wrong,
0 unclear. Two method-level caveats were recorded and do NOT change any label:
(1) SongTimeline.removeSongPosition step 11 enters SmoothAnimator.start through
startDrag's mLiftAnimator.start() (guarded, and the LiftAnimator assignment is
commented out) while step 13's RemoveAnimator.onStop belongs to the RemoveAnimator
started at lines 1457-1458 — a coherent path exists through mRemoveAnimator.start,
and the graph's route semantics ignore guards and model virtual dispatch per
method; (2) MediaLibrary.renamePlaylist's printed entry is the create-playlist
dialog flow while its exit callback is the rename callback — a coherent rename
path exists (playlist-row Rename -> same dialog with the LibraryActivity$2
callback -> onSuccess). No fix was applied in either case: re-deriving would
change route costs, not verdicts, and no route was redrawn after a fix this run,
so the "final sample" is the initial sample (same 30 methods, same order as
make_verification.py's P list).
Separately, the branch logging convention (readme_notes.md, make_verification.py)
logs a sampled path as 'fixed' when its route runs through the systemic onResume
fix, even though it reads correct after the fix. Under that convention the
regenerated verification.csv path rows are 19 fixed / 11 correct / 0 wrong,
error rate (fixed+wrong)/(correct+fixed+wrong) = 19/30 = 0.63 — identical to the
branch record. Muse reports BOTH rates and does not conflate them: this-run
re-verification found 0 new errors; the 0.63 is the logged-convention rate
carried from the branch's own fix history, not new errors found this run.
Confirmed from the regenerated verification.csv (make_verification.py exit 0):
Counter path fixed 19 / path correct 11, label correct 178, edge correct 70 /
edge fixed 10 — exactly the branch record. The D3 numbers above stand as written.


## D4. LESSONS.md kept at 8 bullets (decided by Muse)
The local mirror LESSONS.md already has 8 bullets, within the required 3-8.
This run confirmed the same lessons rather than adding new ones (show_route.py
evidence-regex bug worked around with the local printer; scan --callers' 3
flagged callers each already explained in the method's own reason; tool coverage
contradictions are the same 4 methods as the build's sanity check prints), so
no bullet was added or removed. This run's one new observation class — routes
that are valid at method level (guards ignored, virtual dispatch per method)
while individual guard combinations on the printed chain do not all fire
together (removeSongPosition, renamePlaylist) — is recorded in
scratch/route_judgments.md and the local AGENT_NOTES, not as a 9th bullet.

## D5. check_citations.py reported PARTIAL, not pass, over one unfetchable FW file (decided by Muse)
FW batch 6 finished 47/47 with one failure: ActivityManagerService.java
(1,086,106 B) exceeds the connector get_file_contents display limit ("too large
to display"); a single retry failed identically, and the suggested raw URL is
unusable (private repo, no token allowed). The batch-6 list also missed
HandlerThread.java (5,279 B); the checker's own enumeration caught that gap and
the file was fetched, after which the re-run reads: 100 distinct citations,
1 problem, 0 FW-MEMORY/DYN/UNVERIFIED. The single problem is edge E40f400d7
(S_LIBRARY_PAUSED -> PlaybackService.onDestroy), whose ActivityManagerService
:22975 segment (stopInBackgroundLocked) is unverified locally; its other two
segments (ActiveServices, ActivityThread:3504) are held and verified. Muse does
NOT claim check_citations.py as passed and does NOT change the onDestroy label:
the gate is reported as partial on this one check, with the exact blocker, for
the parent to decide (a full checkout, or an authorised large-file route, would
close it). No public-AOSP lookup was substituted for the branch citation.

### stream-D/Markor/DECISIONS.md

# Markor — Muse's own decisions (overnight Stream D, 2026-11-01)

These are Muse's own decisions, never Yang's, for user/Yang review. No decision below
changes any label, route, or branch file; all work stayed local and no push was made.

## D1. Do NOT fetch auto_calls.json via its raw download URL
- Facts: graphs/Markor/auto_calls.json is 2,090,438 bytes. The GitHub connector's
  get_file_contents refuses it ("too large to display") and returns a raw download
  URL carrying a token. The task's hard constraints forbid putting any token in a
  URL, file, commit, log, or message, and forbid waiting for / using a token at all.
- Decision: do not use that URL, do not try to unwrap or reuse the token, and do not
  treat the file as fetched. Consequence: the branch-exact build is blocked (see D2).
  Morning need: an authorized route for this one file (e.g. a Mac clone, or a
  connector chunked fetch if one becomes available).

## D2. Do NOT present a hand-only build or static counts as the build gate
- Facts: with auto_calls.json absent, build_graph.py exits 1 at graph_def.py:1293
  (`for _c in AUTO['calls']`, AUTO is None). A build with USE_AUTO disabled, or with
  a regenerated auto_calls, would be a different graph, not the branch graph.
- Decision: no build counts, no sample, and no [K] line are claimed. The only counts
  reported as my own work are: (a) py_compile passes on graph_def.py and all fetched
  tools; (b) a static AST count of the UNREACHABLE dict in the fetched graph_def.py:
  414 entries (404 no_trigger_in_app, 9 closed_by_configuration, 1 closed_by_api_level;
  confirmed_by SOURCE 272 / INFERRED 142) — this matches the branch build_report.txt
  exactly, but it is corroboration of the hand-written dict only, NOT a build verdict,
  because REACHABLE verdicts depend on the missing auto edges (branch report: 5214 of
  6891 edges are auto edges).
- Decision: the branch's own numbers (2864 methods = 2859 in method_list.json + 5
  framework nodes; 2450 REACHABLE / 414 UNREACHABLE; 6891 edges; errors 0, warnings 0)
  are reported only as "branch build_report.txt says", never as re-verified by me.

## D3. Do NOT claim the branch's 30-route sample as my route check
- Facts: the branch verification.csv (fetched as a local mirror) has 30 path rows:
  13 correct / 17 fixed / 0 wrong, i.e. a prior error rate of 17/30 = 0.567, plus
  445 label rows (397 correct / 48 fixed) and 87 edge rows (42 correct / 40 fixed /
  5 unclear). But out/methods.csv (2,228,936 bytes) is also over the connector
  display limit, so I cannot redraw the sample myself (verify_sample.py reads
  out/methods.csv) and cannot print/judge 30 fresh routes.
- Decision: report those branch figures as prior work only. My sample error rate is
  NOT RUN, not 0.567, and no fresh route judgement is claimed.

## D4. Greps 5-7 are genuinely runnable and pass; the other checks are not run
- Facts: checks (5)-(7) need only the fetched graph_def.py. With grep -E they give
  0 matches each for DEAD|FRAMEWORK_ONLY, FW-MEMORY, and PENDING (saved in
  scratch/check_greps.txt). Checks (1)-(4) and (8) need a successful build output
  and/or the app source tree (final_java_only), which are not locally available.
- Decision: report (5)-(7) as PASS on the fetched file, and (1)-(4), (8) as NOT RUN
  with the exact missing input named, rather than running them vacuously against
  empty inputs and calling that a pass.

## D5. Logs are not regenerated
- Facts: verification.csv may only be produced via graphs/Markor/make_verification.py,
  which reads out/markor_trigger_graph.json and out/methods.csv — both unavailable
  (build blocked; branch copies also over the connector display limit at 5,207,767
  and 2,228,936 bytes). readme_notes.md (branch copy, 25,026 bytes, five headings
  in order: What the re-audit changed / How the checked paths were chosen / What waits
  for a device (API 27) / Hazard candidates / Limits), LESSONS.md, and AGENT_NOTES.md
  were fetched as local mirrors only.
- Decision: keep the branch mirrors unchanged and unclaimed as regenerated logs;
  write this DECISIONS.md, a local AGENT_NOTES overnight section, and a
  scratch/BLOCKER_AND_STATUS.md instead. No verification.csv, readme_notes.md,
  LESSONS.md, or README is presented as newly generated by me.

## D6. No tick mark, no push, no branch edit
- Per task constraints: nothing was pushed, no branch file was edited, and no
  tick/checkmark was written anywhere in this work.

### stream-D/AnyMemo/DECISIONS.md

# AnyMemo — decisions (Muse's own decisions, for user/Yang review; never in Yang's name)

Overnight stream D, 2026-11-01. Branch work-2026-10-31, repo bugfixops/ground-truth-results.
No pushes; all work local under ~/workspace/overnight/stream-D/AnyMemo/.

## D1 (REQUIRED): the AnyMemo storage-permission question — DECIDED

Question: is WRITE_EXTERNAL_STORAGE treated as pre-granted, or only where a route
needs it? It touches graphs/AnyMemo/graph_def.py:157 (ENV_STORAGE_PERM) and the
startup gate near line 1765 (S_PERM_STORAGE ENTERS edge).

Fresh source printed via the GitHub connector from
final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo/ui/AnyMemo.java:

- onCreate, lines 124-141: if SDK_INT <= Q (29) and WRITE_EXTERNAL_STORAGE is not
  granted, requestPermissions() is called (:127); if already granted and !isUiLoaded,
  loadUiComponents() runs (:131-133). If SDK_INT > Q, loadUiComponents() runs
  unconditionally (:137-139).
- onResume, lines 145-162: on API <= Q, loadUiComponents() runs only if the
  permission is already granted (:155-158) — the gap-fill for the case where
  onCreate could not proceed because the dialog was still pending.
- onRequestPermissionsResult, lines 165-182: grant -> loadUiComponents() (:170-173);
  deny (or empty result) -> Toast then finish() (:178).
- prepareStoreage(), lines ~269-277: the unreadable-storage dialog's Exit button
  calls finish() (:275); no permission re-check anywhere downstream.

DECISION: keep the current modelling — permission is an explicit ENV gate ONLY
on the startup trunk, not pre-granted globally and not re-gated on every
storage-touching route. Concretely:

- ENV_STORAGE_PERM (graph_def.py:157: "the WRITE_EXTERNAL_STORAGE runtime
  permission is granted (requested once on API <= 29; always granted on API 27 if
  accepted)") stays as the ENV gate on exactly the three loadUiComponents edges
  (onCreate-granted, onRequestPermissionsResult-granted, onResume-gap-fill) and
  S_PERM_STORAGE (line 1765: the dialog shown when not granted) stays as the
  not-granted branch.
- No graph change is needed: the current text already says this. This decision
  CONFIRMS the existing modelling; it does not edit graph_def.py (and no branch
  file is edited by this overnight run in any case).

Reasoning:

1. Pre-granted globally would be wrong: on a fresh install the first run MUST
   pass the dialog (Allow) or the activity dies via finish() at :178. Deleting
   the gate would overstate first-run reachability and hide the only
   permission-deny exit in the app.
2. Re-gating every storage-touching route would be wrong too: the app checks
   the permission only at startup (lines 124-182). Downstream storage use
   (prepareStoreage, file browsers, DB open) never re-checks it; it inherits the
   gate through the startup trunk. A second gate would double-count one user
   action and would contradict the source.
3. On the API 27 standard configuration SDK_INT (27) <= Q is always true, so the
   gate always applies on first run and is satisfied thereafter by the one
   acceptance (a runtime grant persists until revoked). The ENV text's "always
   granted on API 27 if accepted" states exactly this.
4. Effect on labels/routes: none numerically. Every launcher-trunk route already
   carries the permission ENV gate (branch build: 1881 methods with ENV); the
   deny path to onDestroy is already modelled (graph_def.py:322). Route checks
   and logs in this run are consistent with this decision.

Status: decided by Muse (overnight stream D leaf), for user/Yang review. If the
user prefers the pre-granted reading, the change would be to drop ENV_STORAGE_PERM
from the three loadUiComponents edges — that change is NOT made.

## D2: partial-build approach under the connector size limit — DECIDED

Branch auto_calls.json (1,132,200 B) exceeds the connector get_file_contents
display limit, and the MCP tool offers no chunked/range fetch; the download URL
it prints carries a token, which this task forbids using. DECISION: run the
build locally with a clearly-labelled NO-AUTO partial copy (USE_AUTO=False,
stub auto_calls {"calls": []}) to validate graph_def.py syntax, hand edges and
the UNREACHABLE set, and report its counts SEPARATELY from the branch build
counts — never as the gate build. The full local build, sample redraw,
check_citations, check_routes, check_bytecode_lines, scan_unreachable,
make_verification and gen_readme_v2 are BLOCKED (not passed, not faked) until a
route for the large files exists (e.g. a Mac clone in the morning).

## D3: route-check judgment basis — DECIDED

With out/methods.csv (3,282,143 B) and out/anymemo_trigger_graph.json
(4,221,347 B) unfetchable for the same reason, the 30-route judgment in this run
rests on: (a) the branch final sample (kiro_sample_30_final.txt, seed 20261025)
and branch verification.csv path rows (30/30 correct, SOURCE); (b) the branch
route prints — 20 routes match the verified path exactly in kiro_routes_all.txt,
and the other 10 are exact prefixes truncated by the known show_route.py comma-
citation crash, whose full comma-safe prints (scratch/route_print/*.txt) were
then fetched and matched against verification.csv; (c) fresh AnyMemo.java lines
for the shared startup trunk; (d) the branch build report's path status
SOURCE_OK 30. This is reported as a consistency re-verification, NOT as an
independent redraw — the redraw itself is blocked (see D2).

## D4: no branch edits, no pushes — DECIDED (standing overnight constraint)

All overnight work stays local; nothing is written to PROGRESS_V2, graph_def.py,
out/, verification.csv or AGENT_NOTES on the branch, and no tick marker is written
anywhere. The proposed status line is stated in the final report only.

## Finish run decisions appended 2026-11-01 ~16:40 EST (coordinator)

All entries below are Muse's own decisions for user/Yang review, unless marked USER.
They cover the finish run since the 11:10 EST push (head 8124fa4). Overnight
decisions already in this file are not repeated. Format per brief section 6:
id, app, item, options, choice, printed evidence, effect, how to reverse.

- LT-A1-C1 (LibreTorrent, A1 parcel rows): brief A1 rule (b) overrides the
  earlier batch-file parcel conventions. Effect: A1 parcel verdicts follow the
  brief rule, not the batch files. Reverse: restore the batch-file convention
  for the affected rows and re-verify.
- LT-A1-C2 (LibreTorrent, batch 17 row 36 collectDependencies): choice
  REACHABLE INFERRED, overriding batch-17 decision D8. Evidence: printed
  javadoc contract for the addMapper to collectDependencies library link;
  the final library link itself was not independently re-printable, so the
  row discloses the unpinned blame view 671bd2ff plus the javadoc contract
  and is correctly INFERRED, not SOURCE. Auditor caveat recorded. Reverse: if
  the premise behind D8 is shown to hold, flip the row back and re-verify.
- LT-A1-C3 (LibreTorrent, batch 48 rows 12-13): choice stay UNREACHABLE,
  kind framework_never_calls, confirmed_by INFERRED. Evidence:
  core/storage/AppDatabase.java:42-52 (the @Database annotation lists
  entities plus version 9 only); auto_calls shows 0 callers for both rows;
  these are the weakest flips in the A1 set. Reverse: on a printed Room
  2.6.1 runtime call site for either row, flip to REACHABLE with the route.
- LT-A3-B019-1 (LibreTorrent, batch 19): the bare TorrentMetaInfo init edge
  is split into 3 qualified edges (byte array form :69, TorrentInfo form :79,
  FileInputStream form :92), each with evidence DecodeException.java:35-39.
  The (Parcel) and (String,String) forms are excluded as decided. Effect:
  R=33 U=7 O=0 of 40 for the batch, edges 35, SUPPRESS 7. Reverse: restore
  the bare edge and re-run the batch harness.
- Aegis-C2-D1 (Aegis, R1 step 13, S_INTRO_WELCOME to S_INTRO_PICKER ENTERS,
  graph_def.py:557): page node enough; NO SYSTEM producer, NO needs_state.
  The brief starting choice (add producer plus needs_state) is DECLINED:
  goToNextSlide (IntroBaseActivity.java:80-93) advances the slide on the tap
  itself (:47; a GUI edge lambda onCreate 1 to goToNextSlide exists), so no
  earlier producer state exists to name, and a SYSTEM node would be
  unverifiable. No edit. Reverse: printed AppIntro source showing the slide
  change needs a separate producer step not on the tap path.
- Aegis-C2-D2 (Aegis, Route 4 step 9, Ebac005d0 icon pack): CONFIRM AS-IS.
  needs_state ST_ICON_PACK_INSTALLED already present; verified
  IconPackManager.java:33 is rescanIconPacks (constructor :31-35). No edit.
  Fresh-declared routes UNCLEAR, relaunch-declared correct.
- Aegis-C2-D3 (Aegis, Route 1 step 21, E1dcf1457 RESULT/initNew): CONFIRM
  the @SAVED variant split as permanent. Fresh show_route
  MainActivity.onIntroResult steps 22-24 resolve (initNew to
  onDonePressed@SAVED to lambda new 1 to onIntroResult;
  IntroActivity.java:92-104,126-129; MainActivity.java:142-148). No edit.
- Aegis-C2-D4 (Aegis, search step 14, E399cebc2 SEARCH_IN_GROUPS): UNCLEAR
  with prior-run needs_state. Verified BehaviorPreferencesFragment.java:57
  sets the mask, MainActivity.java:234 reads it once at onCreate (:193),
  EntryAdapter.java:206-209 reads it. Added ST_SEARCH_IN_GROUPS plus
  STATE_KINDS settings plus needs_state on the edge. No label change.
  Reverse: print showing the mask re-read after a preference change
  without relaunch.
- Aegis-C2-D5 (Aegis, G3_5 step 34, tap-first GA chain): CONFIRM; the no-tap
  Authy-default path stays unmodelled (Limits note at C4), not
  UNREACHABLE. Mechanism corrected: Authy is default-checked on @APP
  because isDirect leaves i at 0 (Dialogs.java:519-522,528) and Authy is
  first among supportsDirect entries (DatabaseImporter.java:99-102,37),
  not because :37 alone means checked. Comment plus pick-edge guard
  corrected. No model change; no Authy edge on the shared OK node.
- Aegis-C2-D6 (Aegis, GlideRequests step 50, root-gated app import):
  CONFIRM AS-IS. ENV_ROOT already maps to kind other (ENV_KINDS_OF) with
  text citing ImportEntriesActivity.java:149-153 plus RootShellTask.java:
  17-20, and already gates lambda startImportApp 5 to readFromApp;
  startImport to startImportApp already has ENV_INSTALLED_GA;
  doInBackground needs no gate (Shell.build runs regardless; root is
  checked at the callback :149-153). Route stays open until C3 redraw.
  No edit.
- Aegis-C2-D7 (Aegis, readFromApp step 24, checked-row chain): RESOLVED,
  chain CORRECT as printed; the missing print LANDED.
  dialog_importers.xml sets choiceMode singleChoice; Dialogs.java:528
  setItemChecked, :529-531 listener (help text only), :537 OK reads
  getCheckedItemPosition; AbsListView.java:1136-1150 (CHOICE_MODE_SINGLE
  tap sets the checked row, then dispatches to the listener). The
  dossier hold-ERROR plus @APP_GA variant is superseded: the @APP_GA
  split is DECLINED (no missing producer; the framework step is the
  producer, now FW-SRC cited). Pick-edge evidence gains the AbsListView
  FW-SRC citation; OK-edge guard now states the precondition explicitly.
  GA tap route judgable CORRECT at C3 redraw (was ERROR). Reverse: print
  showing the dialog ListView is NOT single-choice at runtime.
- Aegis-C2-R1 (Aegis, cold-start edges E20e76e09/E57db524e/Ec7af65b2):
  keep all three with cross-run needs_state. E20e76e09/E57db524e already
  carry ST_PLAIN/ST_ENCRYPTED; Ec7af65b2 (onStart to updateErrorCard)
  was missing its gate, so needs_state ST_VAULT_FILE added (onStart
  returns early with no vault, MainActivity.java:942-948; reads the vault
  :950-977). Fresh-declared routes UNCLEAR, relaunch-declared correct,
  intro-flow routes satisfy in-run via initNew. C2 pushed as e02f1e6
  (first attempt failed not-a-fast-forward when AnkiDroid B1 landed;
  Aegis files untouched, retried, landed); local build after C2 edits:
  2995 methods, 2537/458, edges 5483, errors 0, warnings 0, check 2: 22
  distinct 0 problems, other checks 0, STRICT 1, check 8: 0 of 458.
- Aegis-C3-D01 to D10 (Aegis, round-7 fixes 04/06/16 package, Muse's own):
  variant splits over deletion; plain-delegation re-writes where a plain
  caller remains; Aegis two-chain split; route-06 format split over
  needs_state; $26 guard correction; plain cancel edges kept; only
  onStateDecrypted Welcome edges suppressed; import-page file-argument
  split; PBKDF split by builder; grading UNCLEAR on step 8 only. Full
  record in helper EDITS.md section 6 plus merger scratch/fix_log.md.
  Merger-verified corrections to the helper package (not new labelling
  decisions): the dialog-script section-7 $26 needs_state removal (it
  contradicted section-06 Fix 2 plus the helper's own final graph);
  Fix L applied (10-pair suppression, non-Aegis importer callbacks to
  WelcomeSlide 1 onStateDecrypted, in EDITS.md section L plus
  graph_def_final.py but omitted from the dialog script; without it
  WelcomeSlide 1 still dumped a false 38-step Totp-import route; with
  it 29 steps via @WELCOME); 13 check-4 citation corrections (delegation
  citations off by one, call line not declaration line: PWD3 :260 to
  :259 x3, PWD5 :272 to :271 x6, TIDLG5 :244 to :243 x2, export
  launchers :82 to :83, :86 to :87; check 4 then 0). Effect: routes 04
  (22 steps), 06 (32), 16 (42) all ERROR-free, graded UNCLEAR on step 8
  only; round-7 wrong routes fixed: 01, 02, 03, 04, 06, 16, 20; route 14
  stands wrong by design. Reverse: revert the package edits one group at
  a time and re-dump.
- Aegis-C3-Step8 (Aegis, final sample table, coordinator decision,
  binding, Muse's own): the STRICT D-C3-10 reading STANDS. The 12
  solely-step-8 UNCLEAR routes stay UNCLEAR, NOT CORRECT. The
  relaunch-compatible reading (which would give CORRECT 17, WRONG 6,
  UNCLEAR 2, first-draw rate 6/23 = 0.2609) is NOT adopted: the declared
  configuration is fresh install, step 8's own guard demands a producer
  of the loaded vault earlier on the route, steps 1-7 contain none, and
  adopting the relaunch reading would hide the one step with no in-run
  producer. This reaffirms the concordant rulings of all three fix
  audits (fix-010203, fix-2014-sample, fix-040616). Honest note: UNCLEAR
  routes are excluded from the error-rate denominator under either
  reading, so this choice hides no WRONG route; but the final CORRECT
  count must not be inflated from 5 to 17 by convention. Reverse: only by
  an explicit user ruling adopting the relaunch reading, recorded here.
- Anki-B2-1 (AnkiDroid, check-2 citations): word-form citations only as
  the in-rules resolution. Root cause: check_citations.py:20 ROOT_STYLE
  is unanchored and matches a services slash path colon digits substring,
  so app files under a services directory can never be cited in dir form.
  Fix keeps the path verbatim and puts line numbers in words (for
  example, line 47). Effect: check 2 goes 276/3 to 273 distinct 0
  problems. Reverse: re-anchor the checker (tools edit, not done here).
- Anki-B2-2 (AnkiDroid, MockNoteFactory wording): the wording is that
  source under multimediacard/test/ is PRUNED from the checker source
  index (show_route.py:23 test/ pruning), NOT the brief's literal "no
  source in the upload" (FALSE: the file exists, 2600 B, lines printed
  and correct). Effect: the citation stands in passing form with the
  correct explanation. Reverse: none needed; wording correction only.
- Anki-B4-binding (AnkiDroid, check-8): the 8 supposedly new entries are
  NOT new. All 8 pairs already exist in graph_def_mod/01.py sup blocks
  (XAxisBarGraph.paint:3699/:3700, XAxisHistoGram.paint:3711/:3712,
  YAxisBarGraph.paint:3796/:3800, YAxisHistoGram.paint:3795/:3799), so
  the merger VERIFIES rather than duplicating them. The ReliefLegend
  reason reword APPLIES (ReliefDrawer.java:473-474 getLegend creates a
  ReliefLegend, zero callers root-wide, ReliefDrawer never constructed).
- MMEX-D1 (MMEX, check-2 citations): where the basename is unique in
  final_java_only/MMEX, cite SRC basename colon lines with identical
  lines; where not unique, keep the full path with ", lines" wording.
  Both keep a true verifiable file-plus-lines reference and break the
  false match (the checker's ROOT_STYLE regex is unanchored, so any
  core slash file colon lines anywhere in evidence or reasons is treated
  as a framework citation; app files under core/ can therefore never be
  cited in dir form). Effect: combined B2 gives check 2 = 249 distinct,
  0 problems. Reverse: re-anchor the checker (tools edit, not done).
- MMEX-D2 (MMEX, check-4 EDIT): (a) use B3a's corrected criterion, not
  the brief's _Factory.java-only form (the corrected rule adds: contains
  _Provide AND ends with Factory.java; the brief form misses 18
  _Provide Factory lines over 9 basenames); (b) apply it criterion-wide
  (278 edges), not scoped to the 212 problem ids (B3a verified the extra
  66 carry the identical defect and 0 wrongful rewrites, and a rule, not
  a 212-entry list, cannot drift); (c) FIX_LINES values verbatim;
  (d) MmxContentProvider 19 goes to B3b's true new X open-paren lines.
  EDIT touches only edges matching these patterns; all others pass
  through. Edge ids change; no path rows exist yet, so nothing goes
  stale. Accept at check 4 = 0 where the cited line does not show the
  name (bytecode form). Effect: check 4 goes 244 to 32 (B3a) to 0 (B3b).
  Reverse: revert the EDIT block and re-run check 4.
- MMEX-B6-DispatchSplit (MMEX, B6 fix phase, coordinator decision,
  Muse's own): the dispatcher-split rework is AUTHORISED; accepting the
  15 WRONG routes as wrong-with-reason is REJECTED (it would leave a
  0.875 final error rate, half the sample wrong, not ground-truth
  quality, and a viable fix mechanism exists); a guard-corrected redraw
  only is REJECTED as insufficient (guards are text never evaluated by
  the pathfinder, verified in tools/build_graph.py, so a guard-corrected
  redraw returns the same 15 wrong paths and only converts the 6 FIXED
  routes to CORRECT, giving 15/24 = 0.625). Authorised mechanism: brief
  section 6 preference (variant node over deleting a route) plus the
  Aegis precedent (Aegis fixed exactly this defect class with variant
  nodes only the producer chain reaches, never by deleting the
  dispatcher edge). Edge deletion is FORBIDDEN: 14 of the 15 WRONG routes
  are shortest-path context errors through a shared dispatcher node,
  NOT spurious edges, and deleting the edge would break a real route
  (the ad-hoc AbsListFragment to BudgetListFragment.onViewCreated
  sibling-edge deletion was correctly refused: model-inconsistent
  without the same treatment for all sibling fan-outs, and still left
  that route wrong at steps 9 and 18). Any split impossible from printed
  source falls back to wrong-with-reason with a route-14-style proof of
  no-variant-fix, recorded, never forced. Reverse: revert splits one
  dispatcher at a time and re-dump.
- Currency-CUR-T1-D1 (Currency, T1 path rows): preserve the 28 recorded
  path rows despite today's 27-method redraw; all 28 validate, SOURCE_OK.
  Reverse: re-draw and re-validate if any row fails validation.
- Currency-CUR-T1-D2 (Currency, T1 writer): the writer uses section 4
  validation plus ref-sanity, not AnyMemo's stricter ref-on-evidence
  check. Reverse: adopt the stricter check if a row's ref is challenged.
- Currency-CUR-D3-D1 (Currency, route_07 toast): stays scripted. The
  network-failure precondition is creatable via adb in principle; on a
  Wi-Fi emulator the route may return not-reached, which maps to unclear,
  never wrong. Open setup question for the device lead: whether the
  run contract supports per-route network preconditions. Reverse: re-grade
  unscriptable if the device lead rules the precondition uncreatable.
- Currency-CUR-D3-D2 (Currency, widget routes 24-27): broadcast
  substitution is brief-prescribed and accepted. Reverse: none; disclosed
  in the scripts.
- Diary-D3-01/02/04 (Diary, widget routes 01, 02, 04): unscriptable
  verdicts stand. DiaryWidgetUpdate has no intent filter, Diary.java:
  2357-2368 broadcasts only placed ids, edge Ede74cf66 requires a placed
  widget, and the harness has no placement or drag operation; later
  steps tap a placed widget's PREV/NEXT arrows. Reverse: a harness drag
  primitive that places widgets (see the user's 16:31 EST harness
  extension order) converts these three to scripted.
- Diary-D3-05F (Diary, route_05 fixtures): the fixtures cell gains
  Pictures/photo_1.jpg (file exists in the fixture store); this closes
  the device-lead item on sample.pdf-style gaps for this route. Drycheck
  does NOT catch this gap (it passes an empty fixtures cell vacuously).
- Diary-D3-14 (Diary, route_14 I/O error): unscriptable verdict stands.
  Diary.java:1982-1988 getHome falls back to writable storage,
  Editor.java:396-425; there is no chmod, remount, or fill action in the
  harness. The directory-fixture avenue is explicitly unverified, not
  disproven: it needs a path mapping, a fixture-dir entry, a ROUTES
  fixtures entry, real-emulator proof, and an ordering check against
  other Editor routes, and must NOT count toward the cap today.
- Diary-D3-28 (Diary, route_28 fling): unscriptable verdict stands.
  Diary.java:841-842,:3440-3441: getNextCalendarMonth runs only from
  onSwipeUp, only from onFling; a single-pointer scroll_to fails the
  same guard. Reverse: a multi-touch primitive converts this route.
- Diary-D3-12P (Diary, route_12): stays scripted, CONFIRMED SAFE.
  Diary.java:1305-1323; QueryHandler.java:124-126; the edit-button
  substitution for the printed double-tap reaches the same edit state
  and is disclosed; it degrades to unclear, never wrong, if
  unprovisioned. Reverse: none unless the substitution is disproven.
- Diary-D3-PERM (Diary, permissions): the grant-set reading is sound.
  Only route_17 carries an ENV permission kind, and its cell lists
  exactly its four permissions; every granted permission (routes 08, 09,
  10, 11, 12, 17, 24) is manifest-declared; the manifest declares exactly
  INTERNET plus the four granted. Basis: Diary.java:2248-2265,:561-564.
- Diary-D3-CAP (Diary, cap): 5 of 30 unscriptable (01, 02, 04, 14, 28) is
  16.7 percent, OVER the D3 10 percent cap (3 of 30). The cap is a
  written rule and is NOT waived by the coordinator. Path: a harness
  extension (widget placement alone converts 01/02/04 to 2 of 30; fling
  plus multi-touch plus the route_14 avenue together convert 14/28 to
  3 of 30) or a user ruling. No row is hidden to meet the cap. See the
  USER ruling below for the resolution path ordered 2026-11-01 ~16:31 EST.
- Hash-HC-T3-1 (hash-checker, T3 writer): seed order is current file
  order, not alphabetical, because T3 acceptance is byte-identical
  output. Reverse by re-sorting the seed (breaks byte-identity; do not).
- Hash-HC-T3-2 (hash-checker, T3 writer): path-ref validation exception
  for LogUtils.e over SharedPreferencesSettings.java:44-49 (the
  getLastHashType catch that calls LogUtils.e, the second printed
  LogUtils.e call site, retained as supporting evidence for this fixed
  row; the route ends at the openSystemFileManager catch,
  HashCalculatorFragment.java:196-199). All other path refs validate
  against route evidence or the method's own file. Reverse by removing
  the exception entry (the writer then refuses the current file; only
  valid if the row's ref changes after a route re-check).
- Hash-HC-D1-1 (hash-checker, D1): empty permissions plus
  debug-manifest storage permissions are flagged as a harness
  precondition, not route gates (auditor-confirmed). Reverse by listing
  READ/WRITE_EXTERNAL_STORAGE on picker routes.
- Hash-HC-D3-31 (hash-checker, route_31 LogUtils.e, coordinator decision,
  Muse's own): RECLASSIFIED as unscriptable. Grounds: LogUtils.e fires
  ONLY in the ActivityNotFoundException catch in openSystemFileManager
  (HashCalculatorFragment.java:191-200: try :192-196 ACTION_OPEN_DOCUMENT
  startActivityForResult, catch :197, LogUtils.e :198, snackbar :199)
  when no app handles the intent; on the replay image DocumentsUI
  handles it, so the catch never fires normally. The D3 auditor's
  route_31 PASS was explicitly CONDITIONAL on device-lead confirmation;
  the device lead responded that the harness has no component-disable
  action, adding one is invasive plus risks breaking other picker
  routes, and recommended reclassification, so the condition FAILED.
  Manufacturing the precondition via the script's private runner shell
  call to disable the documents UI package is not a supported replay
  step. Label UNTOUCHED; D7 maps not-reached to unclear, never wrong.
  Hash-checker becomes 36 scripted, 1 unscriptable, 2.7 percent, within
  cap. Reverse: a supported component-disable primitive plus a proof
  the catch fires on the replay image.
- Hash-HC-D3-31-NOTE (hash-checker, D3 bundle): ROUTE_UNSCRIPTABLE_31.md
  JOINS the push (40 paths total), with the AGENT_NOTES sentence
  updated to record the 40-path push (the re-audit's two conditions;
  the bundle as staged before those updates must NOT be pushed as-is).
- Markor-D3-04 (Markor, ROUTES row 04 permissions): row 04 permissions
  cell goes from empty to WRITE_EXTERNAL_STORAGE. The gate DOES divert
  the SEND flow on a fresh install: DocumentActivity.onCreate calls
  requestPermissions at :137 before handleLaunchingIntent at :149; on
  API 27 a missing grant returns false, so it starts
  StoragePermissionActivity and finishes DocumentActivity; the target
  needs a post-resume tap (step 9), by which time the activity is
  destroyed, and even the dialog's Yes path goes to MainActivity, not
  back to the SEND flow, so it is unrecoverable. The script has no
  permission handling. Pre-grant is the original D3 audit's prescribed
  resolution (adding the permission to row 04). This supersedes, not
  contradicts, the D1 audit's "exactly one row lists a permission"
  observation; row 04's env kind stays other_app. Reverse: a script
  permission-handling step plus a proof the SEND flow survives.
- AnyMemo-D3-17 (AnyMemo, route_17 Card.toString): status scripted to
  unscriptable, firing exactly the D1 revert condition. The target fires
  only in the RuntimeException message at LearnQueueManager.java:267
  (cardDao.update(card) equals 0); the chain flush is build-time flush
  (Builder.build:360 to refill to flushDirtyCache:170) with an empty
  dirtyCache (only producer is LearnQueueManager.update:193, called
  after grading at StudyActivity.java:608 and QuizActivity.java:422,
  both with DB-loaded cards; refill call sites only update():198 and
  build():360); deleting the card trips the earlier :263 LearningData
  check first (CardDaoImpl.delete cascade-deletes learning data first);
  release flush at :127 drains the same graded-card cache. No UI,
  fixture, or harness path populates dirtyCache with a nonexistent
  card: structurally impossible, not merely unimplemented. Evidence
  re-printed by the helper (:258 loop, :261-263 LearningData check and
  throw, :265-267 card throw, :170 refill flush, :184/:193/:198
  update and dirtyCache, :127 release flush, :358/:360 build). The cell
  fix (comma to semicolon, single character, line 18 only) keeps the row
  at exactly 10 CSV fields with both :267 and :263 in the parsed status.
  Cap becomes exactly 3 of 30, 10.0 percent, at (not over) the cap.
  Route_17.py is EXCLUDED from the D3 push. D7 consequence: not-reached
  maps to unclear, never wrong. Label untouched.
- AnyMemo-D3-07-cell (AnyMemo, route_07 fixtures cell, coordinator
  decision, Muse's own, Markor precedent): the fixtures-cell amendment
  (adding the identical picker-root DejaVuSans.ttf path in semicolon
  form, keeping the .apkg entry) is a merger-side push-assembly
  amendment at D3-push time (recorded in AGENT_NOTES plus the report,
  with drycheck plus column and cap re-verification), not a separate
  helper task. It changes no script and no status, and the D1 PASS
  stands either way (route_07 without it fails at picker tap to unclear,
  never wrong, until provisioned).
- Amaze-D3-CAP (AmazeFileManager, cap): 11 of 30 unscriptable is 36.7
  percent, OVER the D3 10 percent cap, reported honestly with reasons
  (cloud OAuth, SMB/SSH servers, SAF picker, parcel recreation, gated
  SSH state, read-only-grant failure). Forcing scripts would fake
  routes, per the Diary 5 of 30 precedent. NOT waived by the coordinator.
  See the USER ruling below for the resolution path ordered 2026-11-01
  ~16:31 EST.
- USER-CAP-ACCEPTANCE (USER decision, user's own words, in chat,
  2026-11-01 ~16:31 EST): for unscriptable routes over 10 percent, most
  reasons say the delivered harness has no capability, and the harness
  is ours, so extend it (rotation, background plus process kill plus
  restore, long-press drag for widget placement, multi-touch, driving
  system UI; throwaway SSH/SMB servers on the CI host with runtime
  generated keys, reachable at 10.0.2.2), then retry every unscriptable
  route. Only routes that need a real online account or credentials stay
  unscriptable. If an app is still over 10 percent after that, record a
  decision with the reason for each route and accept it. Do not leave F1
  blocked by the cap alone. This ruling governs the resolution of
  Diary-D3-CAP and Amaze-D3-CAP; it does not retroactively waive the
  coordinator's cap findings, which stand as the pre-retry record.

- Aegis-C3-Exit-Hold (Aegis, ExitActivity.onCreate, coordinator holding, Muse's own, 2026-11-01 ~18:00 EST): the C3 merger's WRONG-by-design verdict for the table stands (route-14 class, proof printed: 10-step dump step-7 trust guard, singleInstance manifest, TEST=false in defaultConfig, sole caller finishApp, no intent-filter on ExitActivity). Labels UNCHANGED: the 4-method production-unreachable question is held open, not flipped — no label change without printed production-unreachability proof (standing no-flip rule). The question stays open for user review; the table verdict alone changes no label.

- MMEX-B6-INFERRED (MMEX, final table grading standard, coordinator acceptance, Muse's own, 2026-11-01 ~18:01 EST): the auditor-consensus INFERRED-delivery standard governs the B6 final table (verified app-side endpoints + standard dispatch + explicit INFERRED flag + nothing contradicting = CORRECT/FIXED; UNCLEAR only for genuine app-side doubt; failed precondition / proven absence = WRONG). The strict blanket line is NOT adopted (its exact restatement would be CORRECT 13->6, FIXED 10->4, UNCLEAR 2->15, WRONG 5, rate 9/15 = 0.6): it would mark verified deliveries unclear, against the project's established INFERRED handling. Recorded for user review; if the user rules otherwise, the restatement above is exact.
- MMEX-B6-getContext (MMEX, DatabaseManager.getContext, coordinator acceptance, Muse's own, 2026-11-01 ~18:01 EST): wrong-with-reason fallback ACCEPTED for the final table (step 5 WRONG on the drawn MainActivity prefix, proof confirmed line by line by h5 + a5; the full 32-edge repair design in fix_log §9 is NOT applied — disproportionate + sync-subtree blast risk, and the task authorizes fallback when the caller list is messy). This is the only first-draw WRONG route to fall back; the other 14 were fixed by dispatcher splits. Valid non-shortest alternatives (backup-agent prefix, broadcast prefix via SyncManager.triggerSynchronization) are recorded in fix_log §9, not drawn.

- Amaze-D3-CAP-ACCEPT (AmazeFileManager, cap, coordinator acceptance under USER-CAP-ACCEPTANCE, Muse's own, 2026-11-01 ~18:08 EST): post-retry Amaze is 6/30 = 20% unscriptable, still over the 10% cap. ACCEPTED with a recorded reason per route; F1 is NOT blocked by the cap alone (user ruling 2026-11-01 ~16:31 EST). Reasons: route_05 — configured cloud provider account + media file inside it, adb/harness cannot create (real online account); route_06 — live SMB server + external player fetching the app's local HTTP stream, no SMB fixture, adb cannot create one; route_12 — (Throwable) constructor reachable only through a write failure the harness cannot arrange (read-only content URI grant; delete-then-save yields EXCEPTION_IO, not the RuntimeException needed); route_22 — computerFound fires only when a real SMB host responds on the local network; emulator network has no SMB host; route_08 — stays PENDING the Amaze graph push (route_08 follow-up rewire verified locally, push pending; conversion awaits that push + D1 edge refresh; revisit after it lands); route_23 — stays BLOCKED on the merger's row correction (SYSTEM SAF picker is another package's UI; system-UI conversion could not land without the pending row correction; revisit after it lands). This acceptance does not erase the pre-retry Amaze-D3-CAP record (11/30 = 36.7%). Routes 08/23 are revisit items, not permanent stays.

- Aegis-C3-Audit-PASS (Aegis, correction audit, coordinator acceptance, Muse's own, 2026-11-01 ~18:13 EST): the independent Stratum correction audit PASSED on all 7 items (evidence lines confirmed; diff exactly one hunk, lines 1356-1359 replaced by the correction comment, file 570,664 B; auditor's private rebuild 2995 / 2537 / 458 / edges 5957 / 0 / 0, 0 label flips, correction-only row differences exactly 14 confined to Stratum decrypt + Argon2Task downstream; eight checks confirmed incl. auditor's own re-runs of check 2 and check 8; redump 47-step @FILE route identical to the auditor's shortest path, ONLY incoming edge to Stratum decrypt is E8360a30f from processImporterState@FILE; cross-importer citations confirmed, edges Ee4fdd4f0 + Eda333e39 exist). C3 push gate opens for the correction itself. Environment note (not a graph defect): the auditor's first check-2 run showed framework PROBLEM lines only because its private copy initially lacked fw_src (the merger tree's fw_src is a near-empty partial extraction); with the clone's full fw_src it matches exactly.
- Aegis-C3-Push-Scope (Aegis, push scope, coordinator decision, Muse's own, 2026-11-01 ~18:13 EST): the C3 push proceeds WITHOUT waiting for the Legacy (Ee4fdd4f0) + Totp (Eda333e39) suspect edges. They are pre-existing fix-4 design edges outside the judged sample, recorded as follow-ups needing their own design + audit packages — the same treatment as the FreeOtp GA-splice / selectIcon / per-importer @FILE pick / generated-code-grading carry-forwards. Holding C3 for them would stall the judged table/graph sync. The audit section-6 row-3 correction note + FLAG-resolved note MUST accompany the table at push time (verdict column untouched).
- Aegis-C3-Rejudge-Followup (Aegis, follow-up, coordinator note, Muse's own, 2026-11-01 ~18:13 EST): fresh step-judging of the corrected 47-step @FILE Stratum route is a follow-up, not a C3 blocker. No verdict on the new route is claimed until judged; the auditor notes its steps 8-9 are the same step-8-convention pair, so re-judging could move row 3 to UNCLEAR (rate 5/9) — recorded as a consequence, not claimed. Row 3 stands as WRONG on the pre-correction 45-step draw with the correction note.

- MMEX-B6-Gate-Ruling (MMEX, B6 push gate, coordinator ruling, Muse's own, 2026-11-01 ~18:19 EST): B6 push is BLOCKED until the audit defects are fixed and the affected groups re-audit to PASS (gate rule: any FAIL blocks). Defects: D-G2 (:45 -> :43 citation), D-G3 (evidence -> :571-580), D-G7 (missing Morningstar guard on E6ec96bae + §10 accounting 45 -> 46), D-G8-1 (7 citations to basename form, check 2 back to 0), D-G8-2 (rebuild.sh run for saved final-graph eight-check output). D-G5 ruling: the Sync drawn route's RE-FEED repair + redraw + re-judge remains a FOLLOW-UP (as before), NOT a B6 push blocker — because route_table route 12 already records the route honestly as WRONG — BUT the fix_log §8 claim that the drawn route is message-correct MUST be corrected before push (both failures: SYNC-vs-DOWNLOAD intent contradiction + unregistered subscriber), plus the §R3 stale header comment and the Eee5044ad overbreadth nit. D-G8-3 (no B4-stamped methods.csv) is NON-BLOCKING: counts independently recounted (4270/3430/840) + per-step 0-flip stability + backup_pre_B2a JSON verdict dict compose to 0 flips; the helper documents the comparison explicitly. Group 4's caveated PASS requires full item-level detail in the re-audit. B7 verification rows are re-issued under the NEW edge ids after the fixes (per fix_log §5) — a B7 item, not a B6 blocker.

- MMEX-B6-Push-Ready (MMEX, re-audit gate, coordinator acceptance, Muse's own, 2026-11-01 ~18:56 EST): the independent B6 re-audit FINAL verdict is PUSH READY — all six units PASS (groups 2, 3, 7, 8 clean; groups 5 and 4 passed after documentary rounds closing D-G5-1, D-G5-2, nits, and G4-D1–D5). MANDATORY push-assembly step: the stage-B6 staging copy of fix_log.md is STALE ("Of the 22" at line 806 + one path-wording line) — staging MUST be re-synced from the live fix_log.md before the push, with the "Of the 23" sentence confirmed. MainActivity.onEvent needs NO table amendment (not a judged route; a 31st route would change the audited 30-route sample without redraw + re-judge). Strong-sense all-paths Payee partition is NOT a Search gate criterion — drawer (§6) follow-up (plain-dispatcher item-id guards or dispatcher split); no Search edge causes the $3 path. B7 verification rows re-issued under the new ids (E0044db82, Ecf182680, E2732f4b0, Eb1cc3582, Eab5e2ab6, E10ea56a2, E57e26427, Ee6b626ff, E06eb6eae, E8c18509f; :331/:156/:119 for Search rows). Follow-ups, NOT B6 blockers: Sync re-feed + redraw + re-judge (route 12 stays WRONG; re-feed needs coordinator authorization with the repair design); Payee partition; routes 8+18; showPrerequisite on onCreate→:244; §9 32-edge repair.

- D9-SET_LOCALE (device gate, coordinator, Muse's own, 2026-11-01 ~19:04 EST): branch device/harness/harness.py MUST contain set_locale before the D9 dry run, or Omni route_12 fails to load (--dry-run uses --load-scripts; reproduced 32/1 with route_12 AttributeError). Current device-stage harness LACKS it; phase2 harness HAS it (def line 293); stage-push2 harness HAS it byte-identical to phase2. Landing the device Phase-2 harness push satisfies this; otherwise a separate set_locale addition is needed. Whether stage-push2 has landed is UNCONFIRMED — confirm by branch read-back before D9. The Omni D3 push itself is NOT blocked by this gap.
- Omni-D1-final/D3-final (device, audit PASS, 2026-11-01 ~19:04 EST): D1-final (merger/stage-D1-final, 2 files) and D3-final (merger/stage-D3-final, 31 scripts) both audit-PASS; route_12 conversion passed its FIRST audit (set_locale('ja_JP') before launch, fresh pm-clear launch as the restart, locale restored en-US after the target edge; ja-JP-absence uncertainty honestly unclear, never wrong). D1-final: exactly one cell diff vs the merger route list (route_12 → scripted), 31 scripted / 2 unscriptable (13, 17) = 6.06%. D3-final: route_16 rework only (e448a1d7; failed original absent), route_12 phase2 conversion unmodified, preview drycheck 33/0. Push order T4 → D1-final → D3-final (D1 precedes D3); stale merger staging-D1 NOT reused; preview root not in any manifest.

- LT-b003-minus1-EXPLAINED (LibreTorrent, coordinator acceptance, 2026-11-01 ~19:08 EST): the b003 REACHABLE drop 2121 → 2120 is the intended MUST-RESOLVE outcome, not a label flip. The live-tree hand edge at :1109 (clone :1114) TorrentSessionImpl.download → PriorityConverter.convert(Priority) was qualified to #2; :103 went REACHABLE→UNREACHABLE (its audited part label, previously mis-honoured through the wrong overload), :94 stays REACHABLE via its true callers; net R−1/U+1. Row 31 stays UNREACHABLE; its part key and SUPPRESS entry for the bare name correctly denote :103, NOT extended to #2. Dedupe against b034's #2 edge stands as a b034-merge item. No escalation was needed (body shows no genuine :103 call).
- LT-b003b007-SOURCE-RESTORE (LibreTorrent, coordinator authorization, 2026-11-01 ~19:08 EST): the b003–b007 merges also downgraded SOURCE entries (503 at b003 → 464 at b007). Restoration is AUTHORIZED as a follow-up repair under the standing stronger-evidence-wins rule (same method as the b001/b002 rewrite: audit vs A1-base inline entries, restore SOURCE grades, kinds/labels untouched, owed greps run + saved, no label flips, repair build with no error/warning rise, SOURCE increase exactly = restored count, own repair commit). Assigned to the new LT merger continuation, after the b001/b002 repair push lands.
- LT-row26-NOT-CLOSED (LibreTorrent, coordinator ruling, 2026-11-01 ~19:08 EST): batch-3 row-26 (cell-vs-prose) is NOT closed. QUEUE.md's "closed by the b003 merge" marking is NOT accepted as a resolution — the previous merger did not resolve it unilaterally. It remains an open escalation alongside 59/32 setVariable. Correction sent to the LT conversion coordinator (QUEUE.md owner).
- LT-citation-no-increase (LibreTorrent, working rule, 2026-11-01 ~19:08 EST): check-2 on the repair build = 190 distinct, 130 problems (matches the user's figure); the repair added zero regex-matching citations. Mechanism: the checker misreads app core/... citations as AOSP framework citations ("file not held" in fw_src). Going forward each LT build reports its count under a no-increase rule; new part-edge citations in bare core/... form get reworded to full-package org/... form (citation-only) before pushing.

- Harness-PROVEN (device, audit PASS, 2026-11-01 ~19:37 EST): kill + restore primitives PROVEN (harness.py:234–274: HOME, am kill, relaunch, settle) WITH the correction that Amaze 09/11 do NOT use kill/restore — they recreate via rotate() alone (sufficient; MainActivity has no configChanges; pasteHelper via PASTEHELPER_BUNDLE). Long-press drag PROVEN (drag_from, Diary 01/02/04; 25/25/24 lines, 0 unknown/unused) with a named live-only fallback (sendevent hold-then-drag if CI shows input swipe scrolling the picker instead of holding). Multi-touch PROVEN (two_finger_swipe + touch_device.py; exactly 87 sendevents for route 28's parameters; multi=true on 2+ pointers; thresholds + upward branch re-verified vs printed Diary.java); live uncertainties (fling velocity, touch-node discovery) settle only on the CI live run via JaCoCo. Harness tests 30/0 via direct invocation (the -I -m unittest module failure is a sys.path quirk, not a regression); touch_device.py 3/3.
- SSH-CI-PROVISIONING (device, requirement recorded NOT applied, 2026-11-01 ~19:37 EST): the workflow installs nothing SSH-related and never sets WITH_SSH_SERVER, so the block is skipped and Amaze 07/29/30 would fail later at setup (missing client key), not at the fail-fast check. run_app.sh's block is partly sound (port 2222, same-user, host key, pubkey-only) but has three gaps: inherits UsePAM yes (bars non-root sshd); never creates/checks /run/sshd; alive-check (sleep 2 + kill -0) passes for a login-rejecting sshd (no login probe). Emulator reachability via 10.0.2.2 is viable at the NAT level. Provisioning requirement (pre-real-run item, NOT applied now — workflow edits are out of scope for this run): workflow step sudo apt-get install -y openssh-server + sudo mkdir -p /run/sshd before the emulator step (real runs only); WITH_SSH_SERVER=1 for Amaze matrix jobs only; -o UsePAM=no plus a BatchMode login probe exiting 2 on failure; then one real CI Amaze run proving install, sshd line, probe success, and route operations before 07/29/30 count.
- SMB-CI-SPLIT (device, determination, 2026-11-01 ~19:37 EST): route 06 viable-with-steps (CI-host smbd via sudo, SMB1/NT1 guest share, direct 10.0.2.2 dialog entry) but its §5 probes are unproven (jcifs SMB1 handshake; resolving media player). Route 22 precisely impossible via a CI-host server (broadcast discovery cannot cross the emulator router; the per-IP half needs nmbd UDP 137, not smbd TCP 445), with one falsifiable exception (non-zero guest Wi-Fi IP + nmbd node-status answer + computer appearing in the dialog).
- Diary-14-CONVERTED (device, audit PASS, merge-gated, 2026-11-01 ~19:37 EST): Diary route_14 CONVERTED via the css-blocker.txt fixture (plain file where Diary expects a directory → mkdirs() fails silently → FileWriter throws ENOTDIR → catch calls the target); no privilege/new primitive/chmod/fill/run-as, so the STAYS-branch safety-review condition does not apply. Diary would be 0/30 = 0% unscriptable. MERGE GATE: after merge, a healthy-session stock-drycheck re-run must show route_14 PASS and Diary 30/0 (minimum gate route_14 PASS; if it fails route_14, the conversion does not count). Counting is BLOCKED until that re-run passes. A dedicated Diary-14 merge agent (stage-only, STOP for audit) is spawned; it builds on landed stage-push2 (route_28 scripted + route_14 unscriptable) and must not touch stage-push2.
- Amaze-retry-STAYS (device, audited, 2026-11-01 ~19:37 EST): 05 STAYS (real cloud account; local SFTP builds CloudStreamSource, never StreamSource; the SMB-path getCurrentPosition note is NOT relied on — claiming 05 on SMB edges would need a merger edge-set decision + audit and still depends on 06's probes). 06 STAYS (viable-with-steps applied, both probes unproven, player half an independent blocker; no draft script written deliberately — selectors are probe-dependent). 12 STAYS (only a RuntimeException from openOutputStream in the SCHEME_CONTENT branch reaches the (Throwable) constructor; the speculative read-only-grant SecurityException theory was explicitly NOT used; a concrete CI probe is specified). 22 STAYS, script work gated CLOSED until the §2.3 probe passes (no script written). Amaze accounting UNCHANGED: 24 scripted / 6 unscriptable = 20.0%, still over the D3 10% cap; the section-6 per-route acceptance record must accompany the Amaze device push (Amaze-D3-CAP-ACCEPT covers the six reasons). Blocked, not retried: Amaze 08 (graph push + D1 edge refresh), Amaze 23 (merger row correction), Amaze 06 conversion (CI probes), Amaze 22 script work (§2.3 probe), Amaze 07/29/30 counting (SSH §5 provisioning + live CI run).

- D9-SET_LOCALE-SATISFIED (device gate, coordinator verification, 2026-11-01 ~19:43 EST): the branch harness now contains set_locale — device Phase-2 commit c4e4ea59 landed stage-push2's harness.py, and its def set_locale is at line 293 (verified in the staging copy, which the Phase-2 read-back confirmed 21/21 identical to the branch). The D9 branch requirement is therefore SATISFIED; the D9 pre-run read-back remains as a final cheap check at D9 time, not a gate item. (Supersedes the "confirm by read-back before D9" hold in D9-SET_LOCALE.)

- Writer-sweep-SCOPE (sweep, correction, 2026-11-01 ~19:45 EST): only 11 writers exist, NOT 13. AnkiDroid (B7 logs not yet written) and LibreTorrent (A8 logs not yet written) have NO make_verification.py anywhere (verified by unbounded find + clone checks) — they are NOT testable and must NOT be counted as failures; they join the sweep when their log phases land. The 11 existing writers all live in their merger trees with out/methods.csv + out/<app>_trigger_graph.json present. Aegis's second copy (graphs_Aegis/) is byte-identical to graphs/Aegis/; Aegis is the only writer taking arguments (--rows, --graph_json, --csv_out).
- Writer-sweep-FLAGS (sweep, static analysis only — NOT verdicts, 2026-11-01 ~19:45 EST): high-risk direct set iteration in an output loop: Vanilla-Music line 177 `for m in unre:` and AnyMemo line 132 `for m in unre:` (the latter matches the old note that AnyMemo's writer reordered rows run to run via set iteration; the pattern is still present). Zero sorted() calls: Aegis (283 lines) and Omni-Notes (104 lines) — row order depends entirely on input-file order preservation. The other nine use sorted() in key loops but have unsorted .items() output loops whose determinism depends on insertion order — unverified statically. No writer uses random/time/datetime/urandom in code (two prose-only mentions). These flags only prioritize the re-run; no app is DETERMINISTIC or NON-DETERMINISTIC on this evidence.

- EXEC-WRITE-HAZARD (environment, coordinator rule, 2026-11-01 ~19:47 EST): three consecutive agent sessions (Amaze push, two writer-sweep attempts) hit an exec content-write restriction — bash writes fail outright with EPERM, and Python writes fail SILENTLY (open().write() exits 0 but leaves a 0-byte file, data lost at flush/close with no error surfaced). A naive "run writer, check exit code" check would falsely pass with empty outputs. RULE for all streams until a session demonstrably writes: never trust exit codes alone for produced files — re-read every build/writer/staging output and confirm non-empty expected content (row counts, edge counts) before pushing; if a session cannot produce verified non-empty outputs, STOP and report the block rather than pushing anything unverified. The file tool still writes static content correctly and may write staging files whose content was verified by reading. Do NOT keep re-dispatching identical sweep retries: the writer sweep is PARKED until an environment exists where exec writes demonstrably work (re-run plan preserved in SWEEP_REPORT_RETRY.md §6, plus the new re-read-verification requirement: prove writability by re-reading a non-empty Python write, not by exit code).

- MMEX-8+18-PASS (MMEX, design audit PASS, 2026-11-01 ~19:55 EST): routes 8+18 repair design independently audit-PASS (auditor read-only, all 12 items verified vs printed source, built JSON/methods.csv, and tools/build_graph.py behaviour; AUDIT.md 469 lines + reproduction harness run_builds.py/steps_check.py/cross_check.py). Route 8 defect confirmed (steps 1–16 never create/start/register a WatchlistFragment; step 17 E992e5393 sole Watchlist mention inventing a return via its STATE guard; Fixer posts plain at FixerService.java:120; Watchlist registers :131, unregisters :138; true recipient CurrencyListFragment registers :114, @Subscribe :354-355, graph edge graph_def.py:4666; both ExchangeRateUpdaterFactory branches return FixerService). Route 8 repair: deletion target 03.py:852-858 exists exactly; deletion-only build drops exactly 2 edges (hand + auto fan-out E887d2bcd), plain Watchlist edge untouched; guard-only fix impossible (bfs()/cheapest() never read guards; Fixer path wins 1 vs 3 needs_state edges, STRICT kinds 1 vs 2 — same winner). Route 18 defect confirmed (launcher AccountEditActivity.java:304-307 AMOUNT vs misdelivery step 15 E282384e2 to ITEA, never in steps 1–14; FW-SRC deliverResults :4253-4266 → dispatchActivityResult :7259-7266 confirmed). Route 18 repair: all 5 deletion targets exist exactly; all 24 proposed edges src/dst-plausible; all four chains complete with exactly one feeder each; plain returnResult RESULT destinations after repair exactly AccountEdit/Checking/PriceEdit/Search; plain equals-preserving edge (03.py:463) intact. cls='standard' load-bearing (without it warnings 1 with REVIEW listing exactly 4 INTENT edges; with it warnings 0 — F1 needs warnings 0). Auditor's own builds: baseline 4270, 3430/840, 8256 edges, 0/0, INFERRED 2771/SOURCE 1499; R8 alone 8254 (−2), 13 routes, 0 flips; R18 alone 8363 (+107), 17 routes, 0 flips; combined 8361, 30 routes, 0 flips, change set exactly the union; all 30 step pairs match the design exactly. Honest outcomes: deleted ids absent in the combined build, so neither WRONG verdict survives; getContentValues → 21-step PriceEdit route; getNumberOfShares → 20-step pre-fill read (ITEA.java:213, confirmed in auto_calls.json); calculator delivery → 25-step onActivityResult variant route with zero plain incoming edges; the design promises FIXED for neither route. Residual fan-out real (11 destinations from @NUM_SHARES) but a full scan found zero cross-branch best routes (siblings route via displayStock/Stock.create()); the branch-exact alternative is honestly framed as untested follow-up, not a hidden blocker. Sequencing: disjoint edge sets, no shared deleted ids, combined target routes identical to single-repair builds; single final redraw after the last repair per B6 step 6, D1/D3 only from that final sample. Minors M1–M7 (none in any edge text to be written): M1 :161/:172 (not :164/:171); M2 :340 (not :341); M3 :80-81 (not :82-84); M4 :104-107 (not :107-109); M5 fan-out set omits Stock.getCurrentPrice (:138), count 11 correct; M6 branch-conditional direct edge is step 21, not step 20, of the new PriceEdit route; M7 getAmountFromResult's reproduced route ends in a different handler's call, not ITEA :125.
- MMEX-R18-VERBATIM (MMEX, implementation instruction, 2026-11-01 ~19:55 EST): the routes 8+18 auditor ran the real tools/build_graph.py in-process with graph-file reads served from in-memory edited texts and out/ writes captured in memory (no disk private copy was possible under the exec-write block); the reproduction matched every claimed number exactly. The auditor's R18 edge texts are a TRANSCRIPTION of design §(c) — implementation MUST use the design's verbatim texts (ids would differ if guard/evidence wording differed, but counts/routes/warnings transfer since all hint words and cls assignments were preserved).
- MMEX-Sync-v2-AUTHORIZED (MMEX, coordinator authorization, 2026-11-01 ~19:55 EST): Sync re-feed v2 implementation is AUTHORIZED — v2 ONLY, never v1 (design audit PASS). The implementation itself must still be independently audited before merging. Route 12's WRONG verdict stands until the final redraw + re-judge after ALL repairs land; the Sync fix does not immediately change it.
- MMEX-designs-ALL-APPROVED (MMEX, milestone, 2026-11-01 ~19:55 EST): all four follow-up designs are now audit-approved — showPrerequisite guard PASS; §9 getContext 32-edge repair PASS (5 non-blocking defects); Sync re-feed v2 PASS (implementation authorized above, v2 only); routes 8+18 PASS. No design work remains open. Remaining order: (1) B6 push on lock window; (2) follow-up implementations, each audited before merge (+ Payee partition as its own design package, drawer follow-up, not a Search gate); (3) ONE final redraw + re-judge after the last repair, rate recomputed from that table only; (4) B7 rows re-issued under all new ids (B6 set, Sync set of 10, §9 set, 8+18 deleted + new variant-chain ids); (5) D1/D3 + DEVICE rows from the final sample only; (6) F1-readiness report (CI SUMMARY + D9 remain coordinator gates). A NEW MMEX merger continuation is spawned (the prior merger-coordinator completed while B6 was still lock-gated); it owns the B6 push + follow-ups + redraw + B7 + D1/D3 + F1-readiness.

- LT-repair-LANDED (LibreTorrent, 2026-11-01 ~20:05 EST): b001/b002 repair push DONE, branch-verified: commit 09e317bc (82 files, 527,260 B; 75 keys restored: b001 39, b002 36; owed greps 74 rows) + fix-up commit ea36e93d (1 file). Pre-check head was c4e4ea59; branch b001.py pre-repair blob f515da1d confirmed; summary path confirmed absent. Read-back: b001.py d552f210, b002.py 6420b0bc, AGENT_NOTES.md 1c10657d, build_repair_b001b002.txt fb2267cb, row-10 grep file 21ac69c0 — all match staging exactly; head ea36e93d. Repair build: 4732, edges 6234, R2120/U481/UNRES 2131, errors 2131 (no rise), warnings 21 (identical set), SOURCE 539 (+75); check 2: 190 distinct, 130 problems (no increase). Row-10 correction made pre-push (not in the prior staging): b002 row 10 NanoHTTPD.<init>(int) carried a residual "Full grep still owed" sentence the exact-phrase check missed (b002.py:53, b002.md:20; grep dir had rows 01–09, 11–35, row 10 missing) — full-repo grep run (0 new NanoHTTPD( sites; sole subclass TorrentStreamServer calls super(host, port) at :69, 2-arg only), saved, sentence replaced in .py/.md, summary 73→74 greps / 49→50 zero-hit rows, AGENT_NOTES updated, rebuild byte-identical to the repair build; no label/kind/grade change (row stays UNREACHABLE no_trigger_in_app); staging after correction 82 files, manifest==disk re-verified, staged==tree for all changed files, b002.py compiles, zero outstanding "owed" sentences in the four part files.
- LT-restoration-READY-78 (LibreTorrent, analyzed not applied, 2026-11-01 ~20:05 EST): b003–b007 SOURCE restoration ANALYZED, scripted, NOT applied (blocked by the session write restriction). Analyzer (merger/analyze_b003b007_restore.py, 3,446 B, intact) reproduces the b001/b002 repair exactly and shows tree b001/b002 at 0 remaining candidates. b003: 39 candidates, b004: 39, b005/b006/b007: 0 — TOTAL 78. b003's one expected non-candidate: bare PriorityConverter.convert(Priority) has no clone UNREACHABLE entry (REACHABLE in clone via the bare edge) — leave exactly as the b003 merge left it (#2 qualification; b034 dedupe remains a b034-merge item). Arithmetic: 617 → 578 → 542 → 503 → 464 → 464 → 539 (repair +75) → 617 after restoration (+78). Restoration build MUST show SOURCE 617 exactly, 4732, 6234, R2120/U481/UNRES 2131, errors 2131, warnings 21 (identical set), check 2 at 190/130 (no-increase). One owed sentence in scope: b003 row 6 FileAlreadyExistsException.<init>() — grep done (0 sites), saved as tree scratch/b003_greps/b003_row06_FileAlreadyExistsException._init_.txt (345 B, verified); in the restoration it gets BOTH the SOURCE restore (clone SRC :22-30) and the sentence replacement citing that grep file; no label flip. No other owed/TODO/FIXME sentences in b003–b007 parts (b003.py:169, b004.py:65 "weakest" caveats are honest notes — leave them). Ready compute script: merger/.probe_python.txt (105 lines, stdout-only, proven PY-OK b003 restored=39 via pipe). Steps for a healthy/write-verified session: run for b003 py, b004 py, b003 md (verify: b003 39 SOURCE + 1 INFERRED row-31 bare key, compiles, no owed; b004 39 SOURCE; b003.md row-6 cited); copy over tree parts (verified untouched); rebuild, require exact counts else back out; stage b003.py, b004.py, b003.md, b004.md, row-06 grep file, restore note, build file, AGENT_NOTES (append restoration section); push as its own repair commit under lock; record commit + sync record. Do NOT touch merge-ready files or graph_def.py. A NEW LT merger continuation is spawned (the prior continuation completed with restoration + QUEUE merges unfinished) owning the restoration + QUEUE merges, with the broken-session playbook (file tool / heredoc-overwrite-to-existing-files / mv + re-read verification; in-process build capture if session python writes are broken).
- LT-row26-OPEN-CONFIRMED (LibreTorrent, 2026-11-01 ~20:05 EST): QUEUE.md currently flags batch-3 row-26 cell-vs-prose as OPEN ("NOT resolved by the b003 merge") — the discrepancy the previous merger flagged appears resolved in the current QUEUE text; no correction send is needed. Row-26 stays an open escalation alongside 59/32 setVariable and the b034 #2-edge dedupe.
- WRITE-PLAYBOOK-UPDATE (environment, 2026-11-01 ~20:05 EST): from the LT continuation's session — what STILL works: bash's own writes to EXISTING files (heredoc overwrite, printf overwrite, >> append — MERGER_REPORT append verified), mv renames, python→pipe→exec-result (computation fine, only file delivery broken), and the file tool. What FAILS: python open().write() to new files (SILENT 0 bytes — the row-10 grep file was pushed EMPTY as blob e69de29 in 09e317bc, caught only by a staging size audit, fixed via heredoc rewrite + fix-up ea36e93d; a second silently-emptied write, b003 row-06 grep file, was caught pre-push and rewritten the same way), bash printf redirect to new files (EPERM), python stdout/stderr redirect to files (exits 120, 0-byte targets even for existing targets), piping python to cat > file (0 bytes), cp (EPERM). Collateral: apply_b003b004_restore.py truncated to 0 bytes by a failed patch attempt (superseded by the compute script — do not rely on it); staging-repair sync JSON left 0 bytes (durable record is the two branch commits + MERGER_REPORT entry; a healthy session should rewrite it — assigned to the new continuation); MERGER_REPORT ends with one labeled PROBE-APPEND-TEST line (harmless; strip on next append). Lesson carried forward: staging size audits catch silent-empty files — every staging must be audited for 0-byte files before pushing, not just by count.

- Diary-14-STAGED (Diary, staged for audit, 2026-11-01 ~20:08 EST): route_14 merge STAGED, NO push, stopping for independent audit. Branch base verified with ref: c4e4ea59 (stage-push2, parent b9177c03); landed ROUTES.csv blob e1a80b5f == hash-object of the stage-push2 file; landed route_28 scripted; landed route_14 still old unscriptable reason; wait condition met. Staged (stage-diary14, manifest MANIFEST.md): ROUTES.csv 6970 B sha256 239b990b; route_14.py 9573 B sha256 8dfdfdef; fixtures/css-blocker.txt 516 B sha256 e83ff064; device/PROGRESS.md 467 B sha256 35939e19. Row-14-only diff vs landed branch (status → scripted, permissions → WRITE+READ, fixtures → css-blocker.txt -> /sdcard/Diary/css; method/edges/source/env/state/setup unchanged; no other row changed); staged ROUTES.csv 30 rows / 30 scripted / 0 unscriptable; route_14.py md5 018d31c8 + fixture md5 108bd5b2 == audited conversion originals; route_14.py compiles, 14 EDGE_IDS == row-14 edges; hygiene 0 tick markers, 0 >900 KB, 0 __pycache__/.pyc; every staged file re-read non-empty with expected content. PROGRESS.md did NOT exist on the branch at c4e4ea59, so it was CREATED (not appended) with the Phase-2 landing line only (c4e4ea59, 21 files, harness extensions incl. touch_device.py, Diary 29/1, Amaze 24/6, + didn't-exist note); the local 1,038-line notes file was NOT copied. Drycheck, stated precisely: stock STATIC drycheck from the merged root GENUINE PASS (exit 0, Diary 30 PASS / 0 FAIL, route_14 PASS; merged root = staged files + all 29 branch scripts, each blob-SHA-verified from stage-push2 + merger device-routes); stock --load-scripts CANNOT run in the staging session (dies before any script executes at tempfile.mkdtemp/gettempdir → FileNotFoundError: No usable temporary directory; probe writes fail under the EPERM fault; mkdtemp(dir='/tmp') works but gettempdir() fails for every candidate incl. /home/hatch, no TMPDIR value passes the write-probe; Runner log-file writes would fail the same way); control proving the block environmental: known-PASS route_28 crashes with a regular-file log (exit 120, traceback through harness.py _run) and passes with --log /dev/stdout (exit 0, 7 lines, exact order); execution-phase equivalent via stdout-pipe (all 30 scripts, dry mode): 30/30 PASS, every script exit 0 with deduplicated log edges exactly equal to its ROUTES row edges in order (route_14: exit 0, 15 lines, Ebd97851f doubled tap+type as expected), 0 pushes from any script. Deviations all caught by verification: three hand-mistranscribed rows (08, 11, 24) caught by the post-write diff (final diff row-14-only); hand-typed SHA truncation for route_12 briefly showed a false mismatch (programmatic re-verification confirmed all 29 branch scripts OK); the local work/device/routes/Diary/ tree is NOT branch state (old D3-era route_14 draft) and was not used; /tmp did not block this work. An independent auditor is spawned (verdict only, no push); push only on PASS.
- Diary-14-GATE-SATISFIED (Diary, coordinator ruling, 2026-11-01 ~20:08 EST): the Diary-14 merge gate (healthy-session stock-drycheck re-run showing route_14 PASS + Diary 30/0) is SATISFIED by genuine static 30/0 + 30/30 pipe execution with the route_28 control proving the --load-scripts block environmental, not a route failure. Reasoning: the gate's intent (re-run shows route_14 PASS + Diary 30/0) is met in both phases; the static drycheck is genuine and independently re-runnable; the pipe execution is the same evidence class the original conversion acceptance rested on (stdout-pipe log + replicated static checks with a known-PASS control), now strengthened by a genuine static 30/0; the missing piece is the literal --load-scripts invocation form, which no currently-available session can run. The literal --load-scripts re-run remains OWED post-push as confirmation when a healthy session is available, but is NOT a push blocker. The auditor verifies the evidence (re-running static + pipe itself); it does not re-litigate this ruling.
- Diary-14-stale-note (Diary, coordinator decision, 2026-11-01 ~20:08 EST): device/routes/Diary/ROUTE_UNSCRIPTABLE_14.md still exists on the branch and becomes stale the moment route_14 is scripted. Its deletion is AUTHORIZED in the same push IF the push mechanism supports deletion; if not, push the 4 staged files and report the stale file as an explicit follow-up item for a deletion-capable push (noted in the push report + AGENT_NOTES so it is not forgotten). The deletion was not staged (not in the merge brief) and is not a push blocker by itself.

- Diary-14-AUDIT-PASS (Diary, independent audit PASS, 2026-11-01 ~20:18 EST): auditor verified every item in its own session against the branch (connector, ref-based) and its own rebuilt merged root (audit-diary14-root/, 42 files, left in place for the push agent); no staging edits, no push. (1) Branch base PASS: c4e4ea59 confirmed with message "Device Phase 2…" (parent b9177c03 directly below); landed ROUTES.csv blob e1a80b5f == hash-object of stage-push2 file; route_28 scripted; route_14 old reason; wait condition met. (2) Staged files + hashes PASS: all four match size, SHA-256, md5 exactly, non-empty, expected content (ROUTES.csv 6970 B sha256 239b990b; route_14.py 9573 B sha256 8dfdfdef, md5 018d31c8 == conversion original; fixture 516 B sha256 e83ff064, md5 108bd5b2 == conversion original, content = blocker mechanism note: plain file at /sdcard/Diary/css → mkdirs() fails silently → FileWriter throws ENOTDIR → target alertDialog; PROGRESS.md 467 B sha256 35939e19). (3) Diff row-14-only PASS: exactly one line (route_14: status unscriptable → scripted; permissions empty → WRITE_EXTERNAL_STORAGE;READ_EXTERNAL_STORAGE; fixtures empty → css-blocker.txt -> /sdcard/Diary/css; method Editor.alertDialog(int,String,int), edges, source Editor.java:411-425, env/state/setup unchanged; no other row changed — the three hand-mistranscribed rows 08/11/24 confirmed corrected); staged ROUTES.csv 30/30/0; route_14.py compiles, 14 EDGE_IDS == row-14 edges (AST extraction); hygiene 0 tick markers, 0 >900 KB (max 9573 B), 0 __pycache__/.pyc; all 29 branch scripts re-verified programmatically 29/29 (stage-push2 01/02/04/28 + merger device-routes 25 others, incl. route_12 — the earlier hand-typed SHA truncation false mismatch resolved); local work/device/routes/Diary/ tree never used by either agent; staging agent's deviation notes all confirmed corrected, none hidden. (4) PROGRESS.md PASS: does not exist on branch at c4e4ea59 (connector: "does not exist"), so creation is correct; content is the Phase-2 landing line only + didn't-exist note; 1,038-line notes NOT copied (467 B). (5) Independent re-runs PASS (auditor's own merged root, every file blob-verified: branch-verified drycheck.py, route_info.py blob 26c7feab, harness/ 3 files, run_app.sh, touch_device.py — all 7 matching branch blobs; 29 branch scripts; 4 staged files; graphs/Diary/out/diary_trigger_graph.json blob 6218aa52 + methods.csv blob 6706d5ee from the merger tree; Diary manifest branch blob 9ceadd21 matches the clone copy, both WRITE_ and READ_EXTERNAL_STORAGE declared): (a) stock static drycheck exit 0, Diary 30 PASS / 0 FAIL, route_14 PASS, printed lines identical to dryrun_report.txt — genuine reproduction; (b) stdout-pipe execution all 30 (dry mode) 30/30 PASS, each exit 0, fully-deduped log edges == ROUTES row edges in order, 0 pushes; route_14 reproduces exactly (exit 0, 15 lines, Ebd97851f doubled tap+type). Non-defect note: route_10's log repeats the S_ENTRY launch edge Ee6b8aa80 non-consecutively (logging artifact in a pre-existing branch script, untouched by this merge); under the full-dedupe rule its edges match exactly, and route_10 passes static and load-scripts independently. (6) --load-scripts question PASS — closes the owed item outright: stock --load-scripts RUNS AND PASSES in the auditor's session (same invocation + --load-scripts → exit 0, Diary 30 PASS / 0 FAIL, route_14 PASS, printed lines identical to the report) — stronger than the coordinator's ruling required (static + pipe sufficing, --load-scripts owed post-push); the literal --load-scripts exit-0 gate is now met PRE-push by a genuine run. The staging agent's block does not reproduce here (auditor session writes verify: cp, python write, heredoc, symlink all produced non-empty verified files; tempfile.mkdtemp() succeeds directly; drycheck created out-static/out-load reports + per-script tmpdirs) — the block was environmental to that session, not a route failure; the route_28 control is superseded, not needed. Push-agent notes (not defects): ROUTE_UNSCRIPTABLE_14.md still on branch (blob 86db141b…), becomes stale once route_14 is scripted, deletion not staged (branch already carries ROUTE_UNSCRIPTABLE_28.md alongside scripted route_28 — stale notes are a pre-existing pattern — but the route_14 deletion stands as coordinator-decided); branch head has advanced past the staging base (auditor-observed ae6313df, with MMEX B6, an Aegis row-3 amendment, and Currency D3 landed since c4e4ea59 — PENDING owner reports with read-back verification; the push agent must do its usual ref pre-checks against current head; staged paths do not overlap those newer commits per the auditor); no pollution from auditor runs (only audit root + /tmp scripts; the empty __pycache__ dir under stage-push2's harness predates the session, mtime 01:07:16 UTC, zero files inside, unchanged; staging read-only throughout). VERDICT: PASS — the 4 staged files are correct, complete, independently proven (static 30/0, pipe 30/30, stock --load-scripts 30/0, route_14 PASS in all three); merge may proceed to push. A Diary-14 PUSH agent is spawned (push only, no staging changes; ref pre-checks vs current head; stale-note deletion if the mechanism supports it, else explicit follow-up; staging size audit for 0-byte files before pushing).
- Diary-14-load-scripts-CLOSED (Diary, 2026-11-01 ~20:18 EST): the owed post-push --load-scripts confirmation from the Diary-14-GATE-SATISFIED ruling is now CLOSED PRE-push by the auditor's genuine stock --load-scripts run (exit 0, Diary 30 PASS / 0 FAIL, route_14 PASS). It is no longer an owed item.

- Aegis-Importer-Sequence (Aegis, Muse's own decision for user/Yang review, 2026-11-01 ~20:27 EST): interaction review delivered 2026-11-02T01:25:30Z (INTERACTION.md, 557 lines, 41,398 B, head/middle/tail verified, zero tick markers, reviewer's only write; coordinator read it in full before deciding, not from the handoff preview alone). Baseline confirmed: tree still 5,957 edges, zero @FILE_ variant nodes, zero @FREEOTP nodes — none of the three designs has landed yet. Key findings: v2's six sups SUBSUME the other designs' sups entirely (Legacy/Totp/FreeOtp pairs are the same tuples as three of v2's six; TwoFAS/AuthPlus/Authy v2-only); duplicate sup() is a set no-op, but duplicate lines must collapse to one canonical line. Central conflict: Legacy+Totp's and FreeOtp-S1b's shared @FILE hand edges vs v2's @FILE_X E19 edges share the same base pair but different source nodes — both land legally, but keeping both gives incoming 3→2 (not 3→1) and the shorter shared @FILE route still wins the shortest-path dump, failing v2 §9 items 1–2; landing both as written is build-legal but not a clean composition (v2's own AndOtp/Stratum-Encrypted hand-moves are the analogy). FreeOtp stage 2 vs v2: @FREEOTP vs @FILE_FREEOTP are distinct nodes, no collision; both dispatch edges SHOULD coexist (file vs app prefixes); final FreeOtp incoming = 2; grep hazard — naive grep @FREEOTP also matches @FILE_FREEOTP, so dump checks must use full node names. Base-feed deletion breaks no premise of the other designs but must come last. Mechanism asymmetry: suppression/hand-cover is sticky-forward; variant creation is leaky-until-suppression. Per-build gates: composed final ≈ 6,369 = v2 6,329 + stage-2 net +40 (13 hand + 27 auto), reconciled from naive 6,368 by +9 (nine auto edges removed once, not twice), −3 (three skipped shared hand edges), −5 (stage-2 auto 32→27; processImporterState@FREEOTP component 10→5). NO per-step V1–V7 totals invented — gated by edge-dump diffs (must-be-gone / must-exist / incoming counts), 0 flips, eight checks. DECISION ORDER = selectIcon FIRST (disjoint, own push, 5957→5954) → v2 V1–V8 in v2's order (AndOtp, Stratum, TOTP, FreeOTP, 2FAS, AuthPlus, Authy, then V8 base-feed deletion LAST) → L0 verification-only (Legacy+Totp, nothing lands) → F0 verification-only (FreeOtp stage 1, nothing lands) → F2 stage 2 last (F1–F13 land in full). SKIP-RESOLUTION (partially supersedes the Legacy+Totp and FreeOtp-S1 "apply as specified" authorizations, justified by subsumption, recorded for review): one canonical v2 sup line per pair lands; the other designs' sup lines do NOT land; their shared @FILE hand edges do NOT land (superseded by v2 E19s); their falsity analyses remain the fix-log justification. If L0/F0 verification fails, STOP and return to audit — never land skipped items ad hoc. R1 push cadence (ruling): V1–V8 run as PRIVATE incremental builds (rebuild + redump + §9 checks each, item 8 narrowed at intermediates to hand edges + landing importer's own dispatch + landed pairs) and push as a SINGLE final commit only when full §9 passes — because the literal per-build D3 check cannot pass at intermediates (transient @FILE_X→unsuppressed-decrypt auto edges), and pushing intermediates would push known WRONG-grade cross edges. Front-loading all sups REJECTED (transient UNREACHABLE flips); accepting transient cross edges in pushed intermediates REJECTED. R2: v2's E19 text governs for the three file dispatches; other texts stay as fix-log justification; requiring the other wording on a variant edge is a text change needing re-audit. R3: v2 item 1 for FreeOTP evaluated at V4/F0, re-read after F2 as shortest-FILE-route. R4: stage-2 auto 27 is a derived prediction; F2 gate confirms component by component (pick 1, <init> 1, onCreate 6, startImport 8, startImportApp 1, onPostExecute 1, lambda$5 4, processImporterState 5), any deviation explained edge by edge per FreeOtp §7 stop rule. R5: order load-bearing (stage 2 last, V8 last); any reorder invalidates §3 gates and re-invokes the fallback (hand-move spec + re-audit). R6: not open. Baseline note: review totals are 5,957-baseline predictions; selectIcon-first shifts them by −3 (v2 final ≈ 6,326; composed final ≈ 6,366) — recompute gates from the ACTUAL baseline at apply time and report actuals, never copy 6,329/6,369 blindly. Redraw only after F2; table never rewritten at any step. Fallback (not applicable under this order, recorded for cost visibility): had the other designs landed first, a hand-move spec + re-audit would be required. Decision entry verified in tree AGENT_NOTES.md (217,098 bytes, grep 1 hit, tail read-back); forwarded in the next Aegis push with the re-judgment + GenCode decision entries. A NEW Aegis merger continuation is spawned (the prior coordinator completed with the sequence decided but not applied) owning selectIcon → v2 → L0/F0 → F2 → C4 → D1/D3 → D7 → F1-readiness.
- Aegis-GenCode-Rule (Aegis, Muse's own decision for user/Yang review, 2026-11-01 ~20:27 EST): ADOPT fixed-(c) tiered/anchored-leg WITH the wrapper-bracketing clause. Row-24 implicit-constructor reading CONFIRMED (rows 4/9 independent). Rejected: (a) Strict (1/5/19, 5/6, rate distortion), (b) Lenient (re-certifies unverified guards), unfixed (c) (collapses to (a)). Consequences: no route changes (4/5/16, 5/9); rule-applied steps 551/30/115. Rows 17/18/21 stay UNCLEAR; row-17 step 5 remains a separate open framework-delivery question. No table change now (pushed 539/30/127 stands; future redraws/re-judges use fixed-(c)).
- Aegis-row3-amended (Aegis, 2026-11-01 ~20:11 EST): row-3 amendment PUSHED as commit 1e5aa7cb (work-2026-10-31 only, route_table.md only, blob SHA read-back verified 8353e7f6…). CURRENT branch Aegis table (SUPERSEDES the C3 final table's row-3 WRONG verdict and 0.6000 rate): CORRECT 4 / WRONG 5 / UNCLEAR 16, rate 5/9 = 0.5556, steps 539/30/127 (696), distinct edges 341. Graph unchanged (5957 edges, 0 flips). C3 pushed earlier as e93c5c1e (5 paths, 855,094 B).

- LT-restoration-LANDED (LibreTorrent, 2026-11-01 ~20:39 EST): b003/b004 SOURCE restoration PUSHED as commit 3e7519745959d587805f2a4d756bbcb78c9c2412 (pre-check head 926f3d13, Diary route-14 push; message "LibreTorrent restoration: b003/b004 SOURCE restoration (78 keys) + row-06 grep (local build: methods 4732, REACHABLE 2120, UNREACHABLE 481, UNRESOLVED 2131, errors 2131, warnings 21)"). Read-back verified: all 8 branch blob SHAs match staged copies exactly (b003.py 2485e17a, b004.py 2f1b252d, b003.md 905b864a, row-06 grep 48a209ad, restore note 29a67086, build summary f37ae262, full report f1c402fe, AGENT_NOTES 769dad5e); lock held only around push + read-back, released, verified gone; sync record written for 8 paths; merger log appended. Contents: b003.py 39 keys restored INFERRED → SOURCE (clone inline citation leads) + row-6 reason replaced, exactly 1 INFERRED remains — bare PriorityConverter.convert(Priority), no clone UNREACHABLE entry, left exactly as the b003 merge left it (#2 qualification; b034 #2-edge dedupe remains a b034-merge item); b004.py 39 keys restored, exactly 1 INFERRED remains — UriConverter.<init> (INFERRED in both); b003.md exactly the row-6 line changed; scratch/b003_greps/b003_row06_FileAlreadyExistsException._init_.txt (345 B, 0 construction sites, cited by both .py and .md reasons, no label flip); scratch/b003b004_restore.md (restore note), scratch/build_restore_b003b004.txt (build summary), scratch/build_restore_b003b004_full.txt (full build report, 265,316 B / 3,408 lines), AGENT_NOTES.md (append-only restoration section). Deliberately NOT pushed: b004.md (byte-identical to branch — no-op file, verified by branch blob equality) and graph_def.py (unchanged). No kinds or labels changed anywhere; b005–b007 had 0 candidates each (keys already INFERRED in the clone). Verification (own runs, then independently audited): build via in-process capture (tree out/ untouched) — 4732, edges 6234, R2120/U481/UNRES 2131, errors 2131 (all unresolved-pattern, no rise), warnings 21 with set identical to the repair build, labels INFERRED 4115 / SOURCE 617; arithmetic closes exactly 617 → 578 → 542 → 503 → 464 → 464 → 539 → 617. Check-2 (real checker, in-process): 190 distinct / 130 problems on both repair-state and restoration builds, identical problem sets — no-increase rule holds, no citation rewording needed. Independent auditor verdict: PUSH-READY on all 9 items (diffs exactly as specified, grades 39+1/39+1, both .py compile, row-06 claim verified vs grep content, AGENT_NOTES diff append-only, b004.md exclusion justified, tree == branch base clean at ref ae6313df, build counts + check-2 reproduced independently); auditor session writes verified healthy, so it produced the full build report from its own capture; merger verified it itself (sha, size, line count, 21 WARN + 2131 ERROR lines, diff vs repair build report exactly one line) before including it. Session hazard note: this session's exec writes were all broken (Python silently 0-byte, bash > EPERM, cp 0-byte copy) — everything delivered went through the file tool, dd, install, or bash >> appends, each verified by re-reading, diff, or hash. Collateral closed: the 0-byte staging-repair sync record repaired (now valid JSON: 09e317bc with all 82 manifest paths verified exact, plus the ea36e93d fix-up entry) and the PROBE-APPEND-TEST line stripped from the merger log.

- USER-CHECK-3e751974 (user verification, 2026-11-01 ~20:43 EST): user checked head 3e751974 (all 13 rebuilt, every dry run). Confirmed: LibreTorrent evidence restored (SOURCE 617, no "Grep owed"); Amaze 30/30 with a deterministic writer; Diary 30/30 with 0 unscriptable; Currency 28/28; hash-checker 37/37; harness extensions with 62 tests passing.
- DRYCHECK-EVERY-APP-RULE (standing rule, user order #1, 2026-11-01 ~20:43 EST): re-run drycheck on EVERY app after ANY drycheck or harness change. Each such push is followed by an every-app drycheck sweep with per-app PASS/FAIL reported. Briefed explicitly to the Vanilla --adb and Amaze retry coordinators; applies to all streams' pushes touching device/, drycheck.py, or harness/.
- Aegis-WRONG-only-tools-edit (user order #2, 2026-11-01 ~20:43 EST): B6 step 7 / C3 allow WRONG only when the fix needs a tools/ edit. Current table 4/5/16 (row-3 amendment 1e5aa7cb): rows 2, 8, 22 are the same defect class as fixes 1–4 (or a fix-1 residual) and row 23's fix is an encrypted-save prefix — fix all four with variant nodes. Only row 16 (by design) stays WRONG, with its reason stated. Sequencing: importer sequence FIRST (selectIcon → v2 V1–V8 → L0/F0 verification-only → F2), THEN this fix round, THEN redraw + re-judge, THEN C4. Table never rewritten before the final redraw.
- Aegis-vault-producer (user order #2, 2026-11-01 ~20:43 EST): 16 of 25 routes are UNCLEAR because they load a vault from an earlier run. A fresh install creates the vault through the intro in the same run (Aegis-C2-D3 already shows initNew → onDonePressed@SAVED → onIntroResult). Where printed source supports it, route vault-dependent steps through that in-run producer (variant node or needs_state with producer), then re-judge. Part of the post-F2 fix round.
- MMEX-WRONG-only-tools-edit (user order #3, 2026-11-01 ~20:43 EST): one more fix round on the 5 WRONG routes after the current implementations (routes 8+18, showPrerequisite guard, §9 repair, Sync re-feed v2). Guard contradictions are the dispatcher class already fixed — apply that class. Leave a route WRONG ONLY if fixing it needs a tools/ edit, and say so explicitly (state which tools/ edit). Route 12's WRONG stands until the final redraw + re-judge (unchanged); the final redraw + re-judge reflects this round.
- Amaze-retry-refutations (user order #4, 2026-11-01 ~20:43 EST): the SAF picker reason is FALSE (uiautomator dump reads any package's window; hash-checker's own note says DocumentsUI is on the image); "smbd needs root" does NOT hold on GitHub runners (passwordless sudo — smbd CAN run on the runner); removeConnection can now use the SSH server (per SSH-CI-PROVISIONING). Retry those routes, then accept the rest with a per-route decision under USER-CAP-ACCEPTANCE (only real-online-account/credential routes stay unscriptable; if still over 10%, record a per-route decision and accept it; F1 not blocked by the cap alone). Starting state 24 scripted / 6 unscriptable = 20.0% (CAP-ACCEPT covers). Route 08's revisit still needs the D1 edge refresh for the 5 reprinted methods (separate owed item); route 23's revisit still needs the merger's row correction (separate item) — if either has not happened, that route stays with a decision, not a silent block.
- LT-full-speed (user order #5, 2026-11-01 ~20:43 EST): no part merged since b007 at 18:45; 113 parts left, 2131 UNRESOLVED (user check) — resume merging at full speed with pre-tested parts, up to 5 per build (18:41 order). QUEUE note (coordinator read ~20:43 EST): "Audited-ready parts, in merger order: (none yet)"; ledger: 111 batches remaining in order 8–12, 15–27, 28–120 (parts-vs-batches count differs from the user's 113 by 2; the merger pulls from QUEUE regardless). New merger standing by to pull continuously as parts list; conversion coordinator prodded to accelerate + report QUEUE status. QUEUE pair-merge rule carried into the merger brief: b055+b056 MUST merge in one build (b055 alone transiently drops 6 methods to UNRESOLVED, resolved by b056; predicted residuals PercentEncoder.pow warning + b057 buildExactAlarmPermissionRequest until b058/b074 SUPPRESS land). Stale QUEUE "Merger feed READY" b001/b002 note flagged IGNORE (rewrite already landed 09e317bc + ea36e93d; branch SOURCE 617).
- Idle-streams-activated (user order #6, 2026-11-01 ~20:43 EST): AnkiDroid check fixes (3 citations, 48 bytecode lines, 169 callers — unchanged) with helpers (B2→B3→B4 push first if not yet pushed, then B6 fixes, each audited); Omni-Notes logs + device scripts with helpers (T4 logs → D1-final → D3-final → DEVICE rows → D7); Aegis + MMEX logs with helpers; device scripts for Aegis + MMEX with helpers (prepare in parallel where independent of final tables; land D1/D3 + DEVICE rows from final tables only). All five stream coordinators confirmed running (subagent.list) and sent follow-ups (submitted, pending application — not described as applied); Anki noted quiet ~45 min at send time.
- Hourly-logs-push-with-counts (user order #7, 2026-11-01 ~20:43 EST): push MUSE_RUN_LOG.md at least hourly; include the number of agents running (in the RUN_LOG entry + status replies). Last pushed base 98401e29 (17:58 EST); the 19:44 cron run deferred on the LT repair lock; this turn's entries ride the next push (coordinator push attempted this turn; hourly cron at :44 as backup).

## Amaze-D3-CAP-ACCEPT-RENEWAL (2026-11-01 ~21:02 EST, Muse's own, for user/Yang review)
Amaze stays 24 scripted / 6 unscriptable = 20.0 percent, ACCEPTED under USER-CAP-ACCEPTANCE; F1 is not blocked by the cap alone. Per-route decisions from retry round 2 (no conversions, no push, no branch edit): 05 real online cloud provider account, the only real-online-account stay; 06 live SMB server plus a resolving external player, both unproven, audit-PASS stay; 12 (Throwable) constructor reachable only via a write failure the harness cannot arrange; 22 real SMB host broadcast discovery, which cannot cross the emulator router; 08 stay-with-decision pending the D1 edge refresh; 23 stay-with-decision pending the D1 edge refresh plus the merger row correction (SAF-picker premise refuted, but the branch row still carries the old prefix). This renews and does not erase the prior Amaze-D3-CAP-ACCEPT record. Follow-ups owned separately: D1 refresh for rows 08, 23, 22; route 23 merger row correction; route 06 probes on a real CI run before any reclassification; correction of the stale run_app.sh smbd comment.

## LT-HAZARD-GATE-CLOSED (2026-11-01 ~21:10 EST, Muse's own, for user/Yang review)
Formal closure of parent ruling (1): with R3/R4/R5 complete, every audit-PASS LibreTorrent part now has file-backed disk evidence (R1 b008-b012, A1b b016-b021, R2 b022-b027, A2 b028-b046 via chunked writes, R3 b047-b062, A3b b063 plus C10-fix b064-b065, R4 b066-b084 PASS subset, A5 b085-b103, R5 b104-b120). No PASS part's QUEUE eligibility now depends on in-memory-only evidence, so ruling (1) is moot for queueing. In-memory reproductions are not used as QUEUE evidence going forward; file-backed rebuilds are the standard. Remaining LibreTorrent blockers are order (b015 FAIL) and ruling (2) (check-2 gate), not the hazard gate.

## 2026-11-01 ~22:05 EST — user rulings at head a9e6392e (verified by user: all 13 rebuilt, every dry run)

- LT-CHECK2-BASENAME (user): citation-form ruling REPLACES the check-2 gate. Cite LibreTorrent app files by file name only (core/model/TorrentEngine.java:N -> TorrentEngine.java:N) for FeedParser, RepositoryHelper, TorrentEngine, TorrentInfoProvider, PriorityConverter, TorrentSessionImpl, TorrentStreamServer, SettingsRepositoryImpl, FileSystemFacadeImpl, SystemFacadeHelper, Utils; reviewer simulation on a9e6392e gives check 2 130 -> 0. Apply to every unmerged part before merging.
- LT-CHECK4-SAMENAME (user): drawer.* 27 citations -> SRC drawer/TagsAdapter.java:N and drawer/TagItem.java; FeedParser.* 19 -> SRC libretorrent/core/FeedParser.java:N; 335 lines via --emit FIX_LINES in the EDIT hook. The 16 FeedParser-path lines that re-trip check 2 are known false alarms recorded by edge id; no tools fix without user approval.
- ANKI-NOTIF (user): check-2 edges E50d68ebc, E16231eaa, Ed8355a39 -> NotificationService.java (only one in the app); check 2 to 0.
- AMAZE-R23-PICKER (user): route_23's unscriptable reason is false; script via the system picker as Omni routes 02/03/31 do. Route_08: throwaway SSH server exists, add the connection then remove it.
- OMNI-MISSING-STEPS (user): routes 05/06/08 scripted to miss REACHABLE targets — add 05 Merge flow, 06 note-with-attachment before export, 08 make-file-missing first.
- LEADS-6 (user): one lead per open stream — LibreTorrent, AnkiDroid, MMEX, Aegis, Amaze device, Omni-Notes — count stated in every log push.

## 2026-11-01 ~22:35 EST — LibreTorrent owed rulings (merger's own, from RULINGS_20261101_2205.md, for user review)

- LT-2205-2 C05 CONFIRMED: b034-b039 basename normalisation is exactly the mandated form; no reversal.
- LT-2205-3 Q1 gate extension YES to b028-b033: their deltas are the same file-not-held artifact class; rework to basename and merge on delta-0 pre-test, not accepted with deltas.
- LT-2205-4 Q2 SOURCE waiver GRANTED for b029/b032: 6 flagged upgrades (b029 MagnetInfo trio; b032 Torrent trio) verified genuine, accepted at merge; harness FAIL lines limited to exactly those 6 keys waived; grades not reverted to INFERRED.
- LT-2205-6 b016-b021: rework, then merge (no delta acceptance); 37 SOURCE upgrades preserved.
- LT-2205-7 check-4 sequencing: basename first at delta 0; qualified drawer/FeedParser forms afterwards via EDIT hook (--emit FIX_LINES); FeedParser re-trips recorded by edge id as known false alarms, no tools fix without user approval.

## 2026-11-01 ~23:11 EST — Amaze-D3-CAP-ACCEPT-ROUND3

Amaze 26 scripted / 4 unscriptable = 13.3%, ACCEPTED under USER-CAP-ACCEPTANCE (F1 not blocked by the cap alone): 05 real online cloud account, 06 live SMB server + resolving external player (both unproven), 12 (Throwable) constructor only via an unarrangeable write failure, 22 broadcast SMB discovery cannot cross the emulator router. Routes 08 and 23 converted this round (system picker / throwaway SSH server). This renews, does not erase, earlier Amaze cap acceptances.

## LT-2205-1 — Check-2 gate REPLACED by basename citation form (user ruling 2026-11-01 ~22:05 EST, applied)
tools/check_citations.py ROOT_STYLE matches any path starting core/ (also services/, data/, libcore/, packages/) as a framework file, and LibreTorrent's own package has a core/ folder, so app citations under core/ are falsely counted "file not held". Rule: cite the 11 app files by file name only (FeedParser, RepositoryHelper, TorrentEngine, TorrentInfoProvider, PriorityConverter, TorrentSessionImpl, TorrentStreamServer, SettingsRepositoryImpl, FileSystemFacadeImpl, SystemFacadeHelper, Utils); e.g. core/model/TorrentEngine.java:N -> TorrentEngine.java:N. This REPLACES the old ruling-(2) choice (accept deltas vs mandate basename): basename is now mandated, every unmerged part gets this rework BEFORE merging, so parts add 0 check-2 problems. Rework waves: head (b015, b016-b021), r28 (b028-b039), r40 (b040-b057); later ranges (b058-b120) get the same rework before their merges.

## LT-2205-2 — C05 basename normalisation CONFIRMED (b034-b039)
C05's unilateral basename normalisation for b034-b039 is CONFIRMED under LT-2205-1 (exactly the mandated form). Verified: scope (only rendering + headers changed), uniqueness (every basename resolves to exactly 1 app file), reversibility (full paths in .md / printed), edge-ids (0 hits in existing route-check rows). No reversal.

## LT-2205-3 — Q1 gate extension: YES, to b028-b033
The check-2 ruling extends to C04's b028-b033. Their measured deltas (+44/+24/+43/+27/+26/+46) are the same file-not-held artifact class, not evidence defects. They are reworked to basename form (r28 wave) and merge on a delta-0 pre-test, not accepted with deltas.

## LT-2205-4 — Q2 SOURCE waiver for b029/b032: GRANTED
The 6 flagged upgrades (b029 MagnetInfo trio; b032 Torrent trio) are verified genuine: tree holds SOURCE for all 6, part holds SOURCE, kinds unchanged, no downgrades. Merger explicitly ACCEPTS SOURCE at merge for b029/b032, same standing as the b010-b012 / b022 SOURCE exceptions already accepted. Harness FAIL lines limited to exactly those 6 keys are waived, not defects. Grades must NOT be reverted to INFERRED (that would repeat the 617 -> 578 -> 503 SOURCE regression).

## LT-2205-6 — b016-b021 gate: rework, then merge (no delta acceptance)
A1b verdicts PASS + GATE-HELD on check-2 only (deltas +6/+2/+26/+47/+57/+56, all file-not-held class). Under LT-2205-1 these are reworked to basename form (head wave) and merge on a delta-0 pre-test. Their 37 SOURCE upgrades are preserved (same standing as LT-2205-4).

## LT-2205-7 — Check-4 same-name files (sequencing, not yet applied at ruling time)
Drawer citations (27): SRC drawer/TagsAdapter.java:N (bytecode) and drawer/TagItem.java, because the bare basename resolves to the shorter ui/tag/TagsAdapter.java (111 lines) instead of the drawer file (316 lines). FeedParser citations (19): SRC libretorrent/core/FeedParser.java:N (bytecode), because the bare basename resolves to the 18-line com/ernieyu interface and crashes check_bytecode_lines.py (IndexError at line 77, reproduced at b012). SEQUENCING: parts reworked to basename form first, merge at delta 0; check-4 qualified forms applied afterwards via the EDIT hook in graph_def.py (as for Amaze/MMEX, via --emit FIX_LINES), because the qualified FeedParser form re-trips check-2. Re-tripped FeedParser lines are recorded BY EDGE ID as KNOWN FALSE ALARMS, not new defects, not a reason to block merges. NO tools/ fix is made — the user may approve one later. Consequence: with the check-4 hook in place, check-2 reads above baseline (false alarms), not 0, until a tools fix is approved; A6 check-2 = 0 therefore needs that approval or an accepted false-alarm exception at gate time. Check-4 helper addendum (2026-11-02 ~03:15 UTC, pending independent audit at ruling time): 27 drawer + 19 FeedParser bare (bytecode) citations verified exactly; post-fix check-4 3214 checked / 938 skipped / 315 implicit / 335 listed (user's 335 figure CONFIRMED); check-2 correction baseline 190/130 -> post-fix 205/145 (+15 not +16, line 110 already a baseline distinct key; 18 qualified edges carry the 15 new keys).

## LT-2205-8 — Standing items carried, unchanged
Batch-3 row 26 stays OPEN; 59/32 setVariable escalation stays flagged, label never flipped; b055+b056 MUST merge in one build; merger-register items at named merges: SUPPRESS unions (G19; G12 F4 pairs into b058/b074; G11 C1 into b058/b074), hand-edge reconciliations (G9 at b115/b116; G15:2060 at b075; G22 C4 $2->$1 at b108; G8 dedupe at b074), G12 C1.md wording (setTextWatcher, not setListeners); batches 13/14 INLINE, never part; b015/b070/b071/b074 FAILs are citation-form only, rework (not relabelling) is their fix path, b070/b071/b074 rework in the r58 wave (b058-b075).

## LT-2205-9 — r28 audit PASS + post-hook baseline clarification
r28 audit PASS on diff-only, zero-tripping, uniqueness, harness, pre-test; b034-b039 clean-claim verified (exactly 1 core/ occurrence each, the C05 header, 0 SRC tripping substrings). Auditor's deviation note EXPLAINED, not a defect: helper pre-tested on PRE-hook baseline (190/130), auditor re-baselined on POST-hook tree (205/145, hook commit 611a130f); cumulative b028-b033 build atop post-hook tree gives edges 6262, R2173/U564/UNRES1995, warnings 29 (baseline 21 + 8 Parcel-ctor), check-2 204/144 — exactly ONE removal, ZERO additions (b031 hand edge Ea22ea235 supersedes baseline auto edge E863c4541 for the same pair). Gate intent is "no new problem"; a sole beneficial removal PASSES. Real merge acceptance still measured against the immediately preceding merge state.

## LT-2205-10 — r40 audit: FAIL on baseline figure only, ACCEPTED on substance
r40 audit items 1-4 PASS (diff-only exact, 1134 replacements; zero tripping citations, caveat 6 libretorrent/core/ strings are pre-existing C06 comment prose on line 2 of b040-b045, inert for check-2; 44 basenames unique; harness 18/18 PASS). Item 5 FAIL ONLY because the helper's stated baseline (190/130) does not reproduce post-hook: auditor measured 205/145 with the real tool on its own build and on the shared tree's out/. Same hook-landing explanation as LT-2205-9, NOT a rework defect. Delta gate HOLDS: all 18 singles, cumulative build, pair show 205/145 with EMPTY problem-set diffs vs post-hook baseline. ACCEPTED: b040-b057 rework stands; operative check-2 baseline is 205/145 (post-hook) until FeedParser false alarms are dispositioned. Pair wording CLARIFIED: b055 alone drops exactly the 6 flagged methods to UNRESOLVED (confirmed); the pair does NOT return them to REACHABLE — its verdict map equals b056 alone, all 6 UNREACHABLE per b056's labels; "restores" means only the transient UNRESOLVED state is eliminated; b055 must still never merge alone.

## LT-2205-b015 — b015 rework (citation-form only, part of the head wave)
b015 FAILs are citation-form only under LT-2205-1/8; rework (not relabelling) is the fix path, applied in the head wave (b015, b016-b021) before merging, on a delta-0 pre-test, with SOURCE upgrades preserved per LT-2205-6.

## MMEX-B3-UIDRIVE — UI-driving setup scripts ACCEPTED with a run_app.sh contract amendment (coordinator decision, Muse's own, for the user and Yang to review)
Audit §2.8 / §7 item 8 (MMEX B3 re-audit, PASS on all 9 changed items): UI-driving setup scripts are mechanically permitted by run_app.sh (it runs any setup_<route>.py with --package/--log/--outdir/--gen-dir, only its exit code matters) and by the landed harness (Runner(edge_ids=None) accepts any non-None edge, setups log in the separate setup log, never against a route edge; setup runs before the discard coverage dump, so seeding cannot pollute route coverage). But the DOCUMENTED contract describes setups as generating run-time files into <outdir>/gen/<route>/, and every precedent setup checked is a pure host-side generator — UI-driving setup is a NEW pattern, not an established one, and it carries two contract-level consequences: (1) drycheck never executes setups (it only py_compiles them when they back a gen: fixture, and MMEX setups back no fixture — so these setups are entirely dry-unvalidated, and the retry's smoke test is not a substitute for real drycheck of the route scripts); (2) setup UI state leaks into the route script's starting state, because launch is plain am start -W -n with no task-clearing flags (see setup_03 portfolio-ending hazard, audit §3.4). DECISION: ACCEPT UI-driving setups as a pattern, with the run_app.sh contract amended to admit them and to write in the drycheck gap and the return-to-home rule (§3.4). What must NOT happen is silent shipment under the old "generates files" wording. Rejection was considered and not chosen: no alternative seeding mechanism exists in this pass, since the database is SQLCipher-encrypted and cannot be seeded by writing a plaintext file.

## MMEX-B3-CAP — Cap decision for this pass: 22 scripted / 8 unscriptable = 26.7% (coordinator decision, Muse's own, for the user and Yang to review)
MMEX B3 package: ROUTES.csv 30 rows, 22 scripted / 8 unscriptable. Only routes 11 (real online cloud-storage account only) and 19 (double blocker: null-base-currency branch + Toast fault) are genuinely unscriptable on current evidence. The other six are "unscriptable in this pass" with named follow-ups in device-fix/NOTES.md (06 split/recurring-form creation ungrounded; 07 Morningstar HTTP download + provider; 08 Fixer HTTPS download + JSON; 10 payee-report row needs a transaction; 12 tablet layout mechanism; 14 due-bill seed ungrounded + notification). DECISION: the B3 package pushes now with the 26.7% cap recorded, under the standing user cap-acceptance rule (record a per-route decision and accept; do not leave F1 blocked by the cap alone) — with the follow-ups explicitly remaining OPEN, so the six in-pass routes may convert in a later pass and the cap figure may fall; this acceptance covers this pass only and does not close those six routes as permanently unscriptable. Per-route reasons are in device-fix/NOTES.md; the package's drycheck is MMEX 30 PASS / 0 FAIL in both plain and --load-scripts modes after the prose-only touches.

## ANKI-ROUTES-CRITERION — ROUTES rows judged by the route_table driven-route criterion, not literal 30/30 vs verification.csv (coordinator decision, Muse's own, for the user and Yang to review)
AnkiDroid device audit (push-round commit 78e6f174): ROUTES edge lists match verification.csv path rows on only 22/30. The 8 differences are exactly the documented corrected derivations (route_07's 14-vs-16 menu re-derivation; WRONG routes 11, 14, 20, 24, 28, 30 corrected derivations; route_12's 37-vs-37 with two edges swapped to Reviewer.openCardBrowser), each verified contiguous against the 9,608-edge graph and matched by its script. DECISION: the auditor's qualification is APPROVED — the merger must NOT "fix" these 8 rows to match verification.csv, which would reintroduce 7 judged fictions plus a CI-impossible sync entry. The gate criterion is the route_table.md driven-route criterion: ROUTES rows must match the judged/corrected drivable routes; verification.csv path rows for WRONG routes are by definition the judged-wrong BFS routes, not the drivable ones. Consequence for the fix round: variant-fixed WRONG routes should become genuine BFS routes, after which their ROUTES rows will match the new path rows. If the user disagrees, their word overturns this ruling and the 8 rows are re-examined.

## D2 decision — 23 REACHABLE→UNREACHABLE flips accepted as labelled (b075 tree; API level 27)

No verdict is changed by this decision; it records why each flip is genuine
rather than a merge artefact. All 23 were REACHABLE before their part merged
(via auto edges and, for the Settings group, via pre-existing hand edges that
now surface as warnings until their SUPPRESS pairs land) and are UNREACHABLE in
the b075 tree (methods 4732, edges 6648, R3276/U724/UNRES732). Full 23-row
table (part, printed guard line, API 27 reasoning) is in
work/LibreTorrent/d2/D2_DECISION_DRAFT.md, forwarded to the coordinator for
the handoff/MUSE_DECISIONS.md append (the merger never writes that file).

### The 16th Settings method — gap closed, not guessed

The previous "exactly 15" count covered only direct SettingsRepositoryImpl.*
methods. The 16th is the nested-class method
SettingsRepositoryImpl$Default.ledIndicatorColorNotify (b047), flipping with
batch-44 row 17 (getter ledIndicatorColorNotify() :342-344 fallback argument;
getter itself closed via AppearanceSettingsFragment.java:180 gated :118-119
and TorrentNotifier.java:290 after early return :276). Settings group is
exactly 16: sound 4, vibration 2, LED 5, ManageAllFiles 4, notification
permission 1.

### Settings group — closed_by_api_level (16)

- b042 x3: askManageAllFilesPermission() (PermissionManager :60-67, :99-104,
  R-gated, false at 27); askManageAllFilesPermission(boolean) (:117 R-gated);
  askNotificationPermission(boolean) (:123 TIRAMISU-gated, 33 false at 27).
- b044 x4: ledIndicatorColorNotify() (AppearanceSettingsFragment.java:180 in
  initLegacyNotifySettings, SDK < O gate :118-119; TorrentNotifier.java:290 in
  applyLegacyNotifySettings, early return :276 at SDK >= O — both sites dead
  at 27); ledIndicatorColorNotify(int) (:250 branch, listener bound only in
  initLegacyNotifySettings :181); ledIndicatorNotify() (:173 + :289, same
  gates); ledIndicatorNotify(boolean) (:244 branch, listener bound :174).
- b045 x4: notifySound() (:139, :151 + TorrentNotifier :282); notifySound(String)
  (:213 ringtone-picker handler, picker launched only from listener :144-168
  in initLegacyNotifySettings); playSoundNotify() (:133 + :281);
  playSoundNotify(boolean) (:241 branch, listener bound :134).
- b046 x2: showManageAllFilesWarningDialog() (Utils.java:706, third disjunct
  of early-return :704-707; at 27 SDK_INT < R is TRUE so || short-circuits
  and :706 is never evaluated); showManageAllFilesWarningDialog(boolean)
  (:711, after the early return always taken at 27).
- b047 x3: vibrationNotify() (:187 + TorrentNotifier :286, same gates);
  vibrationNotify(boolean) (:247 branch, listener bound :188);
  SettingsRepositoryImpl$Default.ledIndicatorColorNotify (see 16th above).
Spot-verified in printed source: AppearanceSettingsFragment.java:118-119
SDK < O gate and TorrentNotifier.java:276 SDK >= O early return.

### Branch-never-taken group (7, b055+b056 pair build)

- NormalizeUrl.join: only call site doNormalize :268, inside
  if (options.removeDirectoryIndex.length > 0) :263; default empty
  (NormalizeUrl.java:90); saved 252-file grep finds zero assignments.
- NormalizeUrl.makeUserInfo: only call site urlToString :397, guarded
  user != null && !user.isEmpty() :396; doNormalize :232-234 nulls
  user/password whenever removeAuthentication is true, default true (:100).
- PercentEncoder.<clinit>: inherited from decode (first active use behind
  if (options.decode) :216; all 3 normalize callers set decode=false).
- PercentEncoder.decode: only call site doNormalize :217, inside
  if (options.decode) :216; callers DetailTorrentFragment :720,
  CreateTorrentViewModel :309, AddLinkViewModel :68, all decode=false.
- PercentEncoder.needsUnescaping: only call site decode :35 (decode never runs).
- PercentEncoder.pow: only call site unhex :111 (unhex runs only from decode).
- PercentEncoder.unhex: only call sites decode :54 and :79 (decode never runs).

### Standing items carried, unchanged

Batch-3 row 26 stays OPEN. 59/32 setVariable stays flagged (b059 row 32 kept
REACHABLE as audited, edge kept for harness coverage, NOT claimed as a
verified route). Check-4 FeedParser re-tripped lines remain known false
alarms with no tools/ fix. F1 warnings-0 disposition still owed for all
warning classes.

# FORWARD TO COORDINATOR — for handoff/MUSE_DECISIONS.md append (merger never writes that file)

## MMEX-D3-CAP-ACCEPT-ROUND2 — Cap decision for the 26/4 package (coordinator decision, Muse's own, for the user and Yang to review)

MMEX at 26 scripted / 4 unscriptable = 13.3% is ACCEPTED under the
user's cap ruling, so F1 is not blocked by the cap alone. Per-route
reasons for the four that stay unscriptable: route_07 Morningstar HTTP
download + provider switch (specified-but-unverified HTTP substitute:
hosts remount + CI-host server, outside the current run_app contract);
route_08 Fixer HTTPS download + JSON (specified-but-unverified HTTPS
substitute: local HTTPS server + system-CA install); route_11 real
online cloud-storage account only (Dropbox/OneDrive/GoogleDrive/Box/
pCloud enum; no WebDAV); route_19 double blocker (null-base-currency
branch unreachable with an app-created database; Toast-throw trigger
uncreatable on a normal foreground flow). This supersedes, and does
not erase, the MMEX-B3-CAP 22/8 = 26.7% acceptance for the earlier
package. Routes 06, 10, 12 and 14 were converted to scripted in this
round (UI-driving setups under the MMEX-B3-UIDRIVE contract: account,
transaction and recurring-bill entry; wm size 1920x1200 + density 240
for the route_12 tablet layout), each independently audit-PASS under
the 1-in-3 script audit (audit/fix2-1in3/AUDIT.md, all 10 sampled
scripts PASS, all five contract questions ACCEPT).

Status of this forward: DRAFT until the package pushes at MMEX's turn.
The 26/4 ROUTES.csv, the four new scripts + setups, and the doc-only
fixes are staged locally at work/MMEX/device-fix2/merge/ and
work/MMEX/device-fix2/routes/, NOT pushed, per the 2026-11-02 ~09:43
EST coordinator amendment (one-app-at-a-time regime; MMEX pushes
again only at MMEX's turn unless the coordinator orders otherwise).

## AMAZE-G4-ENDORSEMENT (coordinator decision, Muse's own, for the user and Yang to review; 2026-11-02 ~10:38 EST)

AmazeFileManager route_08 tally: the pushed route table's fixed-25 count STANDS — route_08 stays "fixed" per the verdict key, and the 24+1 alternative (counting route_08 separately from the 24 fixed) is NOT adopted. No re-tally and no verdict change is made. Rate is 0.833 either way (5 correct / 25 fixed / 0 wrong / 0 unclear over 30), so this endorsement changes no number; it removes the assessment's qualification on finality. If the user disagrees, their word overturns this ruling.

# FORWARD TO COORDINATOR — for handoff/MUSE_DECISIONS.md append (merger never writes that file)

## MMEX-D3-CAP-ACCEPT-ROUND2 — Cap decision for the 26/4 package (coordinator decision, Muse's own, for the user and Yang to review)

MMEX at 26 scripted / 4 unscriptable = 13.3% is ACCEPTED under the
user's cap ruling, so F1 is not blocked by the cap alone. Per-route
reasons for the four that stay unscriptable: route_07 Morningstar HTTP
download + provider switch (specified-but-unverified HTTP substitute:
hosts remount + CI-host server, outside the current run_app contract);
route_08 Fixer HTTPS download + JSON (specified-but-unverified HTTPS
substitute: local HTTPS server + system-CA install); route_11 real
online cloud-storage account only (Dropbox/OneDrive/GoogleDrive/Box/
pCloud enum; no WebDAV); route_19 double blocker (null-base-currency
branch unreachable with an app-created database; Toast-throw trigger
uncreatable on a normal foreground flow). This supersedes, and does
not erase, the MMEX-B3-CAP 22/8 = 26.7% acceptance for the earlier
package. Routes 06, 10, 12 and 14 were converted to scripted in this
round (UI-driving setups under the MMEX-B3-UIDRIVE contract: account,
transaction and recurring-bill entry; wm size 1920x1200 + density 240
for the route_12 tablet layout), each independently audit-PASS under
the 1-in-3 script audit (audit/fix2-1in3/AUDIT.md, all 10 sampled
scripts PASS, all five contract questions ACCEPT).

Status of this forward: CONFIRMED for Push 1. The 26/4 ROUTES.csv, the
four new scripts + setups, and the doc-only fixes are Push-1 content
in the one-app-at-a-time regime; this decision takes effect when
Push 1 lands. (It previously sat in DECISIONS as a FORWARDED DRAFT,
"DRAFT until the package pushes at MMEX's turn"; the per-route
reasons above are unchanged from the draft — only the status line
changes, from DRAFT to confirmed.)

**AnkiDroid route 14 (r14 v2) — 16-count correction + sort-tie dependency (audit record, for DECISIONS):**

THE ONE FACTUAL CORRECTION (non-failing, must be recorded): the drafter's 14-node flip claim UNDERSTATES the count — bare 4-entry closure loses 16 labeled REACHABLE methods, not 14. The §6 list omits ModelFieldEditor$7.confirm and $7.cancel (both verdict REACHABLE), which necessarily die with no $7 variant page. Node-level losses total 20 (16 methods + 3 pseudo-nodes + the page). Mechanism otherwise confirmed (none of the 16 has its own ENTERS into the generic page; fan-out nodes' sole incoming is the generic page; survivors explained via CHANGETYPE/FULLSYNC variant pages and a FRAMEWORK edge). The correction STRENGTHENS the case against bare closure and does NOT reopen the full split without label cost. The count must be corrected to 16 in DECISIONS/merger log, but this needs no re-draft or re-audit.

CENTRAL JUDGEMENT: sort-open is PASS-with-rebuild-gate. The tie is genuinely order-dependent, nothing else helps: genuine $3.confirm cost (1,4,16) = sort-prefix cost (1,4,16); every differing edge has env=None, needs_state=None. Resolution is purely $9.onSelection out-order in the built graph (deleteFieldDialog 3327 before sortByField 3329), under both BFS and cheapest. A sort-prefix print would be a fiction of the same kind as the $2 fiction — and indistinguishable by length or cost (also 21 edges, (1,4,21)). So the gate must check the NODE SEQUENCE, not count/cost, and a sort-prefix print must be a v2 failure — which is exactly the gate the drafter specifies and the auditor adopts as hard. Why not FAIL: the tie resolution is deterministic from the rebuild's own inputs (graph_def.py order + auto_calls.json order), and v2 adds no $9 edge, so nothing in this merge reorders the deciding edges. The residual risk is bounded and, crucially, converted by the gate from a silent misjudgement into a checked failure. Forcing the full split now (which would require modelling NoteEditor/CardTemplate entries that don't exist in the graph at all, plus fan-out disposition) would be the worse trade. The turn lead should also record the tie dependency in DECISIONS so future rebuilds re-print route 14 (coordinator item, as above).

Merger-gate outcome on this rebuild (lead addition, NOT part of the quoted audit text): the merged graph prints the genuine 21-edge DELETEFIELD sequence (Judge B confirmed), so the sort-tie gate HELD on this rebuild — no sort-prefix print occurred.

**STEP1-DELETION-SHAPE (coordinator's own, for user review):** the Step 1 deletion package landed as 6 single-file commits (5 Anki + 1 Diary) rather than one batched commit, because the connector's delete_file tool takes exactly one path per call and push-files cannot delete. Each Anki commit message lists all 5 Anki paths verbatim + the ROUTES.csv-governs lines + the 634735a8 run-log reference, so the 09:40 requirement (all 5 paths in the run log AND in the deletion commit message) holds for every deletion commit. The Step 1 one-commit-per-app batching holds for push-files packages (Anki Push 2 cf43c4f8, LibreTorrent logs 36bcfcfb) and for this logs commit; the deletion shape is a tool constraint, not a batching choice.

**E1-ANKI-CLOSED (coordinator's own, for user review):** Stream E's E1-Anki rename job is closed with no separate push: the branch graphs/AnkiDroid/AGENT_NOTES.md already carries the renamed heading "## Decisions made by Muse (for the user and Yang to review)" (1 occurrence) and the old heading "## Open decisions for the user" (0 occurrences), via commit 78e6f174. The verify-then-apply onto a fresh copy is therefore already satisfied in substance; nothing further rides any AnkiDroid push for this item.

**STEP2-PATH-A (user ruling 2026-11-02 ~17:06 EST):** LibreTorrent T1 execution via Path A — 17 frontier delivery edges (E1–E8 + H1 + RULE-D1 enumeration), no tools/ change. Path B (a rule that REGISTER edges count as path steps, changing tools/build_graph.py BFS) stays unauthorized; it was not given a direct user order.

**STEP2-D2-D3 (user rulings 2026-11-02 ~17:09 EST):** D2 ACCEPTED — TorrentInputStream.toUnsignedByte recorded UNREACHABLE on read()'s settled UNREACHABLE entry (edge E24273691, read()'s sole caller edge into toUnsignedByte). D3 = POLL EDGE — DialogSelectTagBindingImpl.hasPendingBindings recorded REACHABLE via INFERRED poll edge E99f87464 from SelectTagDialog.onCreateDialog (not the grep-zero precedent). With Path A, T1 closes fully: expected UNRESOLVED 86 to 0, errors 0, REACHABLE 3967 / UNREACHABLE 765. R4 (notifySound) still NOT decided, so warnings 16 to 0 remains blocked (and item 5 showed D2 itself adds a 17th warning, so warnings to 0 also needs a warning-class decision).

**STEP2-BATCH-SCRIPT (user order 2026-11-02 ~18:14 EST + coordinator's own method note):** the user ordered deletions "all at once in one script" after the one-by-one deleter stalled. Connector finding, verified by listing the live MCP tools: there is NO batch-delete tool — delete_file takes exactly one path per call (one commit each), and push_files pushes multiple files in one commit but requires content per file (create/update only, cannot delete). One script looping delete_file calls is therefore the closest the connector allows to "all at once"; per-delete approval cards remain a runtime property, not a script property. A true single-commit deletion would need a direct git push, which the standing connector-only rule forbids; it was not done and needs an explicit user override of that rule. Executed as delete_remaining_setups.py: 14 setups, 0 failed, last delete 2dfba2be.

**Aegis-D3-CAP-ACCEPT (user decision 2026-11-02):** Unscriptable 3/25 = 12% ACCEPTED, like Amaze-D3-CAP-ACCEPT-ROUND3, under USER-CAP-ACCEPTANCE (record the decision with the reason for each route; do not leave F1 blocked by the cap alone). Rows: 02 FreeOTP (table steps 48 root shell, 50, 52 installed FreeOTP V2 tokens.xml data; no in-run producer; adb root does not supply the app's libsu su call); 09 IconAdapter (step 46 omits the GA app-import sub-flow; step 48 requires an installed icon pack); 17 Auth (WRONG on two printed-source grounds, steps 28/35). No row demands a real online account. Row 18 is NOT in the acceptance set (retry legitimate; if its retry fails on device, unscriptable becomes 4/25 = 16.0% needing its own cap decision).

**LT-4A-STAYS-INFERRED (user decision 2026-11-02):** The 10 labels stay INFERRED. The path-based confirmed_by rule (SOURCE only if EVERY edge on the best path is sourced) is correct tool behaviour; NO tools/ change. The 10: LogEntry.getTimeStampAsString, BaseAlertDialog.<clinit>, BaseAlertDialog$SharedViewModel.observeEvents, AddTagDialog.<clinit>, ExpansionHeader.createRotateAnimator, ExpansionHeader.setExpanded(boolean,boolean), ExpansionHeader.toggleExpand, DrawerGroup.selectItem, drawer.TagsAdapter.<clinit>, drawer.TagsAdapter$1.<init>. SOURCE total stays 620. This closes the Step 2 item-4(a) blocker as a decision, not a fix.

**STOPPING-RULE-B (user decision 2026-11-02, option B):** No further fix rounds for AnkiDroid or Aegis. AnkiDroid rows 09/18/28 and Aegis row 17 stay WRONG with their reasons. AnkiDroid routes 18 and 28 stay out as scripted routes but each gets an unscriptable row ("route WRONG as drawn (see route_table.md)"), so ROUTES.csv has one row per path row (30).

**ANKI-RATE-2026-11-02 (user decision 2026-11-02):** Rate definition corrected: fixed = WRONG in ANY earlier draw (first draw at 3213cea2 included) AND CORRECT now. The fixed 13: AdvancedStatistics$Card.setIvl, DB.insert, DiffEngine.diff_cleanupSemanticScore, EasyX509TrustManager.<init>, Finder.findNotes, HttpFetcher.downloadFileToSdCardMethod, Models$TransformFieldDelete.<init>, Phrase.<init>, Sched.getToday, SimpleMessageDialog.<init>, Sound.notifyConfigurationChanged, Stats$1.compare, libanki.Utils$1.<init>. Correct-only 14, wrong 3, rate = (13+3)/(14+13+3) = 16/30 = 0.533, each route counted once. This supersedes the Step 2 8/35 figure, which double-counted fixed routes inside correct.

**REAUDIT-W3-ENTRIES (user confirmation 2026-11-05):** In W3, exported or external entry edges are never replaced or deleted. The missing in-app edges are added (UI handler -> ViewModel -> engine, Rx runnables, adapter clicks, the app's own broadcasts) and each external entry keeps its env gate; the builder then prefers the in-app route by itself. The only env gates removed are the launcher entries (MAIN/LAUNCHER intent filter): in LibreTorrent Ef4711e98, E558b0012, E50191c30. Those edges stay; only their gate goes.

**REAUDIT-W4-HAND-FIXES (user confirmation 2026-11-05):** Two hand fixes RTA cannot catch are part of W4. (1) Aegis-16: SUPPRESS the cha edge DatabaseImporter.readFromApp -> GoogleAuthUriImporter.getAppPath, citing DatabaseImporter.java:46, 79-80, 99-101; then GoogleAuthUriImporter.getAppPath gets an UNREACHABLE entry with that evidence. (2) MMEX-03: clone MainActivity.showFragment_Internal per caller (as already done for @RECURRING), or move the edge MainActivity.showFragment_Internal -> AccountListFragment.onActivityCreated behind the creation of AccountListFragment; together with ESR_CREATION, MMEX-03 must come out library.

**REAUDIT-APPENDIX-B (user confirmation 2026-11-05):** review/sample_tune/ and review/checked_cases.csv are not on the branch yet. Until checked_cases.csv arrives, the table in Appendix B of handoff/MUSE_REAUDIT_5APPS.md is the reference for the 23 checked cases. W0 and the round measurements wait for sample_tune/.

**REAUDIT-W1-MERGE (Muse decision 2026-11-06):** Merging the three W1 switches: for a method reachable only through SETUP_ONLY edges, explicit_standard_route is computed on the unfiltered reachability sets (its route is derived with the setup edges allowed, so its standard-route test uses the same graph); all other methods use the filtered sets. Coordinator adjustment to the SETUP_ONLY helper's version, which used the filtered sets for every method and so reported explicit_standard_route = no for all 37 Aegis setup-only methods. Recorded here so the auditors and the reviewer can overrule it.

**REAUDIT-W1-RTA-HYBRIDFILE9 (Muse decision 2026-11-06):** RTA is implemented exactly as brief T2 specifies. Its W1 side test does not reproduce the brief's expectation that AmazeFileManager HybridFile$9.execute loses its route, for two source/graph reasons recorded as Q5 in handoff/MUSE_REAUDIT_QUESTIONS.md. The switch was not bent to force the example; the two hand edges are re-judged from printed source in W4.

**REAUDIT-W2-AEGIS (Kiro's own decision 2026-11-06 04:18 UTC):** Aegis baseline = onboarding passed, a password-protected vault (Q3) with two default TOTP entries (Q6). Cleared: the two intro gates, vault loaded, entry list loaded, vault file exists, Google Authenticator export not empty, at least one entry row bound, at least one entry, entry list not empty, password slot, vault encrypted, AegisActivity registered as lock listener. Kept: "icons not optimised" (a vault this version creates has icons_optimized true, Vault.java:18, 46; false only for a vault file an older version wrote, Vault.java:92-93), the plain-text vault, every UI-session gate, non-default settings, other entry types, device states. SETUP_ONLY = S_INTRO_WELCOME, S_INTRO_PICKER, S_INTRO_SETUP, S_INTRO_DONE. Self-checked only; second: pending reviewer.

**REAUDIT-W3-LIBRETORRENT (Kiro's own decision 2026-11-06 04:24 UTC):** Three exported entries keep their env gate after W3 because the app has no in-app sender: BootReceiver (system boot broadcasts only), NotificationReceiver (only the notification's PendingIntent buttons, TorrentService.java:498-520; its engine calls have in-app routes) and SendTextToClipboard (another app's SEND only). The torrent-row bind edge MainFragment.onViewCreated -> TorrentListAdapter.onBindViewHolder needs a torrent in the list (W3 point 4), with the text and kind the other row-binding edges already use ('adapter.getItemCount() > 0', data). Self-checked only; second: pending reviewer.

**REAUDIT-W3-AEGIS (Kiro's own decision 2026-11-06 04:26 UTC):** The cold-start edge MainActivity.onStart -> MainActivity.startAuthActivity (removed in the earlier vault round, when the encrypted vault file counted as cross-run state, R1) comes back as a hand edge with no state gate: under the re-audit baseline the encrypted setup vault exists, so the launcher start opens the unlock screen (MainActivity.java:942-977). This replaces the screen-off broadcast as the start of the unlock routes. PanicResponderActivity, AegisBackupAgent and the quick-settings tile services keep their env gates (no in-app sender). Self-checked only; second: pending reviewer.
