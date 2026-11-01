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
