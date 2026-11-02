# MMEX B6 fix log (merger, 2026-11-01)

One entry per fix group, in application order. Each entry records the
spec, the exact edits, the rebuild counts, and the reprint verification.
No fix group is pushed until the final table passes independent fix
audits (task order step 5).

## 1. Drawer split (drawer spec, AUDIT PASS) — APPLIED + VERIFIED

Spec: `helper/b6-fix-drawer/SPEC.md` (~700 lines) + `blast_counts.txt`.
Coordinator decision applied: MMEX-B6-DispatchSplit (dispatcher-split
rework authorised; options (a) and (c) rejected).

Edits (all B6 fix ADDs in new `graphs/MMEX/graph_def_mod/03.py`, which
loads after 01.py/02.py in name order — placement deviation from the
drawer spec's "append to 02.py" recorded: 03.py IS the last-loaded
module, preserving the spec's intent, and keeps all B6 fix edges in one
auditable file as the result1 spec requires):
- Feeder: `MainActivity$3$1.run -> MainActivity.onDrawerMenuAndOptionMenuSelected@GROUP` (CALL).
- 5 @GROUP INTENT edges: Budgets, About, Settings, Search (companion),
  Password create-only.
- 3 hand replacements of auto edges: AboutTabAdapter.getItem ->
  AboutFragment.newInstance (guard position==0), AboutFragment.newInstance
  -> AboutFragment.<init> (guard mInstance==null),
  LookFeelPreferenceFragment.onCreate -> DefinedDateRanges.<init> (guard
  show-transactions preference non-null).
Deletions in home files (partition-replacements, tombstone comment left):
- `graph_def.py:199` plain dispatcher -> AboutActivity.<init> (E1760f123).
- `graph_def.py:1627` plain dispatcher -> BudgetsActivity.<init> (Ec72b7276).
- `graph_def_mod/01.py:4767` plain dispatcher -> SettingsActivity.<init> (Edcb3f4b6).
In-place guard edits in `graph_def_mod/01.py`:
- :4785 SettingsActivity.onCreate -> S_SETTINGS (no EXTRA_FRAGMENT =
  PerDatabaseFragment guard).
- :4879 S_SETTINGS -> SettingsFragment$2.onPreferenceClick
  (look-and-feel preference non-null guard).
- :573 group gui edge (optional spec D.4): "Payees" example corrected to
  "Recurring transactions or Budgets" + null-children/mDrawer guard.
NOT applied (deliberate): result1 §1.6 guard edit to plain Edcb3f4b6 —
the edge is deleted by this group; its guard lives on the @GROUP
Settings edge (ADD 4) instead.

Rebuild (tree, `python3 -I tools/build_graph.py graphs/MMEX mmex`):
4270 methods, 3430 REACHABLE / 840 UNREACHABLE (unchanged from B4
baseline), 8041 edges (baseline 8027: +9 hand in 03.py +12 auto fan-out
from @GROUP -1 suppressed $3 auto -3 suppressed About/DDR autos -3
deleted hand = +14), errors 0, warnings 0. No label flips.
Verification (built JSON + methods.csv):
- Feeder present; auto $3$1.run -> plain dispatcher GONE; child
  $4$1.run -> plain dispatcher kept; 3 plain INTENT edges GONE; 5
  @GROUP INTENT edges present; plain Search + Password edges kept.
- @GROUP auto outs (12): showFragment(Class), SyncManager.<clinit> /
  .<init> / triggerSynchronization, FileStorageHelper.<init> /
  showStorageFilePicker / showCreateFilePicker, DrawerMenuItem.getId /
  .getTag, MainActivity.getDatabases, RecentDatabasesProvider.get,
  TransactionTypes.<clinit>.
- Redraws (node-for-node as predicted, counts unchanged):
  DbModule_ProvideSqlBriteFactory.get 27 (group prefix), AboutFragment
  .getLogcat 17 (group prefix), DefinedDateRange$1.<init> 20 (group
  prefix).
- Blast: all 424 methods using the 3 deleted edges still REACHABLE, 0
  step-count changes vs clone baseline.
Known residual (NOT a regression, per drawer spec B.5): @GROUP inherits
auto showFragment(Class), so a group prefix can still reach
AccountListFragment.<init> (child item) — fully partitioning that
fan-out is separate follow-up, not smuggled into this change.

## 2. Activity-result Route 2: resetCategory (result1 spec §2) — APPLIED + VERIFIED

Spec: `helper/b6-fix-result1/SPEC.md` §2 (+ §0 mechanics, §2.5 mirrors).
Application order per spec §4: Route 2 FIRST (Route 3 reuses its
@CHECKING chain).

Edits (in `graphs/MMEX/graph_def_mod/03.py`, appended after drawer):
- 5 sup() pairs: (Checking.initializeInputControls, initSplitCategories),
  (Recurring.initializeControls, initSplitCategories), ($11.onClick,
  showSplitCategoriesForm), ($4.onClick, showSplitCategoriesForm),
  (Split.onOptionsItemSelected, Split.onActionDoneClick).
- CHECKING chain C1-C9 + RECURRING chain R1-R9 + K edge ($4.onClick ->
  showSplitCategoriesForm@RECURRING, category-field entry, Recurring
  page only — no Checking $4 gui edge exists, so no Checking variant).
- 24 mirrors (12 per host, verbatim from plain edges): onCreate@V x6,
  S_SPLIT@V x2, show@V x3, onActionDoneClick@V x1.
Deletions in home files (tombstone comments left):
- mod02:256 show -> Split.<init> (E23751ccf), :262 Split.<init> ->
  onCreate (Ef45d7864), :266 onCreate -> S_SPLIT (E987b13c0), :280
  S_SPLIT -> onOptions (E3e76d475), :168 Split.onActionDoneClick ->
  Checking.onActivityResult (E4efc272b).
- mod01:2798 (was :2797 before drawer shifts) Split.onActionDoneClick ->
  Recurring.onActivityResult (E354ebf06); :5671 initSplitCategories ->
  $11.onClick (Ee6d65779).
Kept deliberately as dead edges (spec §2.3): all other plain hand edges
out of partitioned Split nodes (incl. batch-071 parceler edges); their
srcs are unreachable, so they have no BFS effect.

Rebuild: 4270 methods, 3430 REACHABLE / 840 UNREACHABLE (unchanged),
8132 edges, errors 0, warnings 0. No label flips.
Verification:
- resetCategory redraws EXACTLY as spec §2.7 (17 edges, @CHECKING
  sequence node-for-node); Checking.onActivityResult 14 via @CHECKING;
  Recurring.onActivityResult 17 via the Payee RESULT path (as spec §2.8
  predicted; @RECURRING Split chain 28, not shortest).
- All 11 mirror methods REACHABLE (onCreateOptionsMenu 11,
  onSaveInstanceState 11, ViewBinding.<init> 11/12, ViewBinding$1.<init>
  13, ViewBinding$1.doClick 12, onFabClick 13, $1.onClick 12,
  ScrollAwareFABBehavior.<init> 11, onStartNestedScroll 12,
  onNestedScroll 13).
- Route step 12 (AppCompat dispatch to onOptionsItemSelected) stays
  UNCLEAR per spec §0.6 — no CORRECT claim on the platform citation
  alone; the redraw judging wave verdicts this step as UNCLEAR.

## 3. Activity-result Route 1: Passcode (result1 spec §1) — APPLIED + VERIFIED

Spec: `helper/b6-fix-result1/SPEC.md` §1 (+ §0 mechanics).
Application order per spec §4: Route 2 first (done §2), then Route 1,
then Route 3.

Edits (in `graphs/MMEX/graph_def_mod/03.py`, appended after Route 2):
- sup((SecuritySettingsFragment.onActivityResult, Passcode.setPasscode))
  — partitions the plain auto edge :118 (fires only on the REINSERT
  visit, requestCode==10).
- 7 chain edges: onActivityResult -> startActivityPasscode@REINSERT
  (CALL, INSERT-branch guard); startActivityPasscode@REINSERT ->
  PasscodeActivity.<init>@REINSERT (INTENT, gui); <init>@REINSERT ->
  onCreate@REINSERT (LIFECYCLE); onCreate@REINSERT -> S_PASSCODE@REINSERT
  (ENTERS); S_PASSCODE@REINSERT -> $1.onClick@REINSERT (GUI);
  $1.onClick@REINSERT -> onActivityResult@REINSERT (RESULT, 5th-field
  guard); onActivityResult@REINSERT -> setPasscode (CALL, REINSERT
  guard).
- Plain-preserving hand edge: onActivityResult -> startActivityPasscode
  (CALL, EDIT-branch guard) — REQUIRED because the @REINSERT hand
  edge's base pair suppresses the plain :132 auto edge.
Kept deliberately: plain RESULT E5c156fe7 (first visit) and plain INTENT
E9ac9395c (first launch). Guard edits (§1.6) deferred to the guard
phase (§5 below) per spec §4.

Rebuild: 4270 methods, 3430 REACHABLE / 840 UNREACHABLE (unchanged),
8154 edges, errors 0, warnings 0. No label flips.
Verification:
- savePasscode 29 edges, matching spec §1.4 node-for-node EXCEPT the
  drawer prefix is the group prefix ($3.onGroupClick -> $3$1.run ->
  @GROUP -> SettingsActivity) instead of the spec's child prefix — BY
  DESIGN, because the drawer group (§1 above) was applied first and
  Settings is a group item, not a child item.
- setPasscode 28 via @REINSERT; clearPasscode 22 via plain handler
  (:144); encrypt 29 via @REINSERT (as spec §1.5 predicted).
- Variant screen S_PASSCODE@REINSERT accepted by the build with no
  unknown-node error — this resolves result2's variant-screen question
  by precedent (see §6).

## 4. Activity-result Route 3: Split$1 (result1 spec §3) — APPLIED + VERIFIED, with one REVIEW warning resolved

Spec: `helper/b6-fix-result1/SPEC.md` §3 (+ §0 mechanics). Reuses
Route 2's @CHECKING chain (§2) — not duplicated. Adapter path branches
from onCreate@CHECKING via the initRecyclerView fan-out, NOT from the
S_SPLIT page.

Edits (in `graphs/MMEX/graph_def_mod/03.py`, appended after Route 1):
- 8 ADDs: onEvent -> CalculatorActivity.<init>@SPLIT (INTENT, guard
  requestId+1000); <init>@SPLIT -> onCreate@SPLIT (LIFECYCLE);
  onCreate@SPLIT -> S_CALCULATOR@SPLIT (ENTERS); S_CALCULATOR@SPLIT ->
  onEqualsClicked@SPLIT (GUI, cls non_standard, via ButterKnife);
  onEqualsClicked@SPLIT -> returnResult@SPLIT (CALL); plain-preserving
  onEqualsClicked -> returnResult (CALL — REQUIRED, restores the plain
  :249 auto edge suppressed by the @SPLIT hand edge's base pair);
  returnResult@SPLIT -> onActivityResult@AMOUNT (RESULT, guard >=1000
  + RESULT_OK + data); onActivityResult@AMOUNT -> onAmountEntered
  (CALL, guard RESULT_OK + data + >=1000).
- sup((SplitCategoriesActivity.onActivityResult,
  SplitCategoriesActivity.onAmountEntered)) — partitions the
  branch-agnostic auto :145 (handler itself variant-tagged @AMOUNT,
  because a Category-delivered route would otherwise be a candidate
  shortest path to $1).
Deletions in home files (tombstone comments left; both ids confirmed
from the merger's own build output BEFORE deleting):
- `graph_def.py:2232` (was :2238 before drawer shifts)
  Split.onEvent(AmountEntryRequestedEvent) -> CalculatorActivity.<init>
  (INTENT, built id E20490343 — MATCHES the spec's computed id exactly;
  its evidence uses '...' + EV_START concatenation, which is why the
  spec required build confirmation).
- `graph_def_mod/02.py:334` (was :348) CalculatorActivity.returnResult ->
  SplitCategoriesActivity.onActivityResult (RESULT, Edc2b1ed0).
Not built (deliberate): the @SPLIT save-menu path
(onOptionsItemSelected -> returnResult :149) — the equals-key path
suffices for $1; add it only if a future sampled route needs a
Split-launched save-menu Calculator. No Calculator mirrors needed
(plain Calculator chain stays live via the AccountEdit prefix).

Rebuild: 4270 methods, 3430 REACHABLE / 840 UNREACHABLE (unchanged),
8172 edges, errors 0, warnings 1 (the REVIEW warning below — the ONLY
open build issue at that point).
Verification:
- $1.<init> 24 steps, EXACTLY spec §3.7 sequence node-for-node;
  onAmountEntered 22 via @AMOUNT; showInvalidAmountDialog 23 via
  @AMOUNT; plain Split.onActivityResult 18 via the Category RESULT
  edge (as spec §3.8 predicted); CalculatorActivity.<init> 10 via
  AccountEdit (unchanged); CalculatorActivity.returnResult 14 via
  AccountEdit equals key (plain-preserving hand edge works).
- CalculatorActivity.returnResult -> AccountEditActivity.onActivityResult
  edge KEPT (E09fdbf18 RESULT; AccountEdit handler's own shortest path
  is 14 via the CurrencyListFragment setResult path, but the
  Calculator -> handler edge survives as a valid alternative — spec
  §3.8 requires the chain to survive, not to be shortest).
OPEN WARNING (then resolved, see §5): `WARN REVIEW 2 edges on the
default class mention a library/reflection hint: Ec97f118b E6f36f793`.
Identified in built JSON: Ec97f118b = CalculatorActivity.onCreate@SPLIT
-> S_CALCULATOR@SPLIT (ENTERS, class page) — flagged because its
EVIDENCE cites "ButterKnife.bind at 118" (part of onCreate's body
111-128); E6f36f793 = CalculatorActivity.onEqualsClicked ->
CalculatorActivity.returnResult (CALL, class explicit) — flagged because
its EVIDENCE cites "@OnClick at 247". Merger's assessment: both are
FALSE POSITIVES on evidence citations, not mechanism — the ENTERS edge
is framework setContentView (not ButterKnife-mediated; the bind is a
separate auto edge fanned out from onCreate@SPLIT) and the CALL edge is
a direct bytecode call at :249 (not via @OnClick binding; the binding
is the separate non_standard GUI edge).

## 5. Result1 guard phase (spec §4 step 4) + REVIEW warning resolution — APPLIED + VERIFIED

Applied after all three structural blocks (guard edits change edge ids
and would stale helpers' blast-radius greps if applied earlier).
- REVIEW fix (chosen over evidence rewording, which would have dropped
  accurate citations): hand-set cls on the two flagged edges to exactly
  their classifier defaults, marking them human-reviewed
  (class_basis 'authored', so the REVIEW heuristic — which targets
  unreviewed defaults — no longer flags them). cls is NOT in the edge-id
  hash, so ids and routes are unchanged. ENTERS edge: cls='page'
  (comment: reviewed, ButterKnife word is only in the evidence citation
  of a neighbouring onCreate line, not in the edge's mechanism).
  Plain-preserving CALL edge: cls='explicit' (comment: reviewed, direct
  bytecode CALL at :249; @OnClick word is only in the evidence
  citation of the handler's annotation; the binding edge is separately
  non_standard). REJECTED: cls non_standard (would misclassify
  framework/bytecode edges and change plain Calculator routes'
  explicit/standard-only status).
- §1.6: Passcode RESULT E5c156fe7 guard edit (mod01:4754; located by
  (src,dst) grep, NOT by the spec's mod01:4756 — drawer + Route 2 edits
  shifted mod01 lines): guard 'resultCode is RESULT_OK and data is
  non-null (SecuritySettingsFragment.java:97-98)'. Drawer -> Settings
  Edcb3f4b6 guard edit SKIPPED (edge deleted by §1; guard lives on the
  @GROUP Settings edge).
- §2.6 step 3 (MERGED edit — result1 §2.6 + result2 §1(c) both edit the
  widget edge E37b8fad5, so applied ONCE as their union, never twice):
  mod02:49 widget edge gains gui 'Tap the add-transaction widget button
  (R.id.buttonNewOperation)' (result1) + guard 'user taps the widget
  button (RemoteViews click)' (result2) + evidence extended to :32-45
  (covers result2's :32-42 and result1's :32-45; intent :38,
  ACTION_INSERT :39, PendingIntent :41, setOnClickPendingIntent :42,
  updateAppWidget :45). gui, NOT env — result1 §2.6 warns an env gate
  would change this route's cheapest cost to (1,0,17) and invalidate
  the §2.7 analysis.
- §3.6 hand replacement (in 03.py): onAmountEntered ->
  showInvalidAmountDialog (CALL, guard amount.toDouble() < 0,
  evidence :276-279) replaces auto Ed4b0a689 by base-pair suppression;
  same src/dst/kind/cost, so route-neutral by construction (id
  renumbers). Simulation-untested — verified by node-sequence check
  below. onAmountEntered's other auto dsts (getStorageAmount :287,
  setAmount :288) untouched (different pairs).

Rebuild: 4270 methods, 3430 REACHABLE / 840 UNREACHABLE (unchanged),
8172 edges, errors 0, warnings 0 (REVIEW warning RESOLVED). No label
flips.
Verification: all three result1 node sequences UNCHANGED from §§2-4
(resetCategory 17 via @CHECKING; savePasscode 29 via @GROUP +
@REINSERT; $1.<init> 24 via @CHECKING + @SPLIT + @AMOUNT) — only ids
changed (old ids appear as stale-edge warnings in verification rows,
expected, not an error; B7 re-issues rows under new ids).

## 6. Result2 group (result2 spec §§1-2) — APPLIED + VERIFIED

Spec: `helper/b6-fix-result2/SPEC.md` (851 lines) +
`blast_E99cd6390_E00164e96.txt` + sim.py/sim_fullchain.py/sim_shortcut.py.
Application order per spec §4: §2 PRIMARY first, then §1. Widget-edge
correction NOT re-applied (already covered by the merged edit in §5 —
do NOT apply it twice).

Edits (in `graphs/MMEX/graph_def_mod/03.py`, appended after §5):
- §2 PRIMARY (11 edges): F1 ($3$1.run -> dispatcher@RECURRING, CALL,
  guard item != null) + D2 (dispatcher@RECURRING -> showFragment(Class)
  @RECURRING, CALL, guard menu_recurring_transaction) + D3 (showFragment
  (Class)@RECURRING -> showFragment(Fragment)@RECURRING, CALL, guard
  fragmentClass != null AND resulting fragment != null) + D4
  (showFragment(Fragment)@RECURRING -> showFragment(Fragment,String)
  @RECURRING, CALL) + D5 (showFragment(Fragment,String)@RECURRING ->
  showFragment_Internal@RECURRING, CALL) + D6 (showFragment_Internal
  @RECURRING -> RecurringTransactionListFragment.onActivityCreated,
  FRAMEWORK, guard fragment not already added) + 5 MANDATORY plain
  re-asserts R2a-R2e (trigger 'Direct call', evidence 'SRC ...:957 /
  :652 / :751 / :759 / :770 (bytecode)' — bit-for-bit preservation of
  the suppressed auto pairs; without them the plain showFragment chain
  loses its only chain incoming and hand edge E02664d9b
  (showFragment_Internal -> AccountListFragment.onActivityCreated) is
  stranded).
- §1 (7 edges): V1 (showCreateTransactionActivity ->
  Checking.<init>@FRAG, INTENT, gui, guard repo.load != null) + V2
  (Checking.<init>@FRAG -> Checking.onCreate@FRAG, LIFECYCLE) + V3
  (Checking.onCreate@FRAG -> S_CHECKING_TRANSACTION_EDIT@FRAG, ENTERS;
  variant screen REQUIRED — routing through the PLAIN screen leaks:
  the widget path would still reach the variant RESULT edge, simulation
  reproduced it at 14 steps; build accepts variant screens, precedent
  §3) + V4 (S_CHECKING_TRANSACTION_EDIT@FRAG ->
  Checking.onOptionsItemSelected@FRAG, GUI, guard item id ==
  MenuHelper.save) + V5 (onOptionsItemSelected@FRAG ->
  onActionDoneClick@FRAG, CALL) + V6 (onActionDoneClick@FRAG ->
  RecurringTransactionListFragment.onActivityResult, RESULT, guard
  saveData()==true AND resultCode==RESULT_OK) + R1 (MANDATORY
  re-assert: plain onOptionsItemSelected -> onActionDoneClick, CALL;
  without it plain onActionDoneClick loses its ONLY incoming edge
  E49e398a6).
- Step-21 guard correction (in 03.py): RecurringTransactionEditActivity
  .saveSplitCategories -> SplitRecurringCategoriesRepository.insert
  (CALL, guard hasSplitCategories()==true AND (split item id == null OR
  split item id == Constants.NOT_SET), evidence :574-580) — hand
  replacement of auto Eba4c84fa by base-pair suppression (id renumbers).
Deletions in home files (tombstone comments left; ids confirmed from
the merger's own build output BEFORE deleting):
- mod01:2915 (was :2917) plain showFragment_Internal ->
  RecurringTransactionListFragment.onActivityCreated (FRAMEWORK,
  E00164e96).
- mod01:2982 (was :2984) plain Checking.onActionDoneClick ->
  RecurringTransactionListFragment.onActivityResult (RESULT, E99cd6390).
  Sibling RESULT edge E253e0762 (RecurringTransactionEditActivity ->
  onActivityResult, mod01:2980) UNTOUCHED (different launch).
In-place guard edit in mod01 (hand edge, not auto):
- :2952 RecurringTransactionListFragment.onActivityResult ->
  onCreateLoader (FRAMEWORK, E192886f6): guard 'resultCode ==
  RESULT_OK'.
Not applied (deliberate): result2 §1(c) widget-edge correction — the
merged edit in §5 already covers it (guard + gui + evidence :32-45,
a superset of result2's guard + evidence :32-42). Result2 §1(c)'s
":436" note: the RESULT edge being deleted cites :437 correctly; the
plain INTENT edge (mod02:69) was NOT touched, so no correction was made
to it — recorded as a citation-nit follow-up, not a B6 blocker (line
:436 exists, so check (2) is unaffected).
Result2 Route 3 (DatabaseManager.getContext) NOT in this group — still
open (see task order step 6; backup-agent caller-partition design under
investigation, decision pending).

Rebuild: 4270 methods, 3430 REACHABLE / 840 UNREACHABLE (unchanged),
8217 edges, errors 0, warnings 0. No label flips.
Verification (all STOP conditions PASS):
- SplitRecurringCategoriesRepository.insert 23 steps, EXACTLY the
  predicted §2(b) PRIMARY route via @RECURRING (not the 20-step
  shortcut fallback — PRIMARY is the plan).
- TransactionStatuses.<init> 15 steps, EXACTLY the predicted §1
  search/all-data route (SearchActivity -> AllDataListFragment.loadData
  -> onLoadFinished -> bindView -> getBackgroundColorFromStatus ->
  <clinit> -> <init>); the 27-step RESULT route remains valid but
  non-shortest (verified by tracing §1(b)(i) edges, not by expecting
  it printed). No loader/bindView edge was deleted to force it.
- RecurringTransactionListFragment.onActivityResult 21 steps via
  @RECURRING (RecurringEdit RESULT path; spec §1 blast predicted
  reachability, not a specific count — the +1 vs its predicted 20 is
  the extra @RECURRING hop, not a defect).
- CheckingTransactionEditActivity.onActionDoneClick 7 steps via the
  widget prefix (plain pair preserved by R1).
- All five plain re-assert pairs R2a-R2e present in built JSON; R1 pair
  present; AccountListFragment.onActivityCreated REACHABLE 10 steps
  via E02664d9b (not stranded).
- F1 + drawer feeder share the base pair ($3$1.run, dispatcher) and
  suppress the same auto edge — complementary, not conflicting
  (@GROUP covers the 5 INTENT cases, @RECURRING covers the
  showFragment CALL case). Auto-duplication residue noted (spec §2(e)):
  @RECURRING -> plain showFragment(Fragment) -> ... ->
  AccountListFragment.onActivityCreated is a longer non-shortest
  alternative — harmless.

## 7. Search/host + loader group (search spec) — APPLIED + VERIFIED

Spec: `helper/b6-fix-search/SPEC.md` (1,032 lines), audit-PASS.
Reconciliations applied (merger's own, recorded in the spec section
headers in 03.py):
- SKIP R1-C/R1-D/R1-Del2 as drawer duplicates (already applied in §1;
  drawer @GROUP Budgets edge carries the CORRECTED null citation
  :889-890, not the search spec's :887, which is Recurring's entry —
  citation error only, topology unaffected).
- SKIP R3-F/R3-G/R3-Del3 as superseded by the drawer design: applying
  R3-F would suppress auto $4$1.run -> plain dispatcher and, combined
  with the drawer feeder's suppression of $3$1.run -> plain, strand
  every plain case edge. Payee case stays on PLAIN, achieving the
  spec's goal on the drawn-route scope (the drawn Payee route is via
  $4, 8 steps, not $3) without a @CHILD node. Predicted 18-step route
  uses the plain dispatcher at steps 5-7, same count.
  Correction (g4-full D1, drawn-route scope only): a $3 path via the
  §6 hand re-assert E61edcf43 ($3$1.run -> plain dispatcher) exists
  in the full graph and predates §7, so the $3 half of the R3
  mechanism premise above was already stale at §7 time and the
  "plain IS the child variant" gloss is scoped to the drawn route
  only. Strong-sense all-paths Payee partition is a drawer
  follow-up (plain-dispatcher item-id guards or dispatcher split),
  not a Search claim; no Search rework follows from it.
- ADD plain re-assert for Ed8e6a9c0 alongside R2-A: the spec's "KEPT"
  claim is WRONG under the base-pair rule (R2-A's base pair equals the
  auto pair, so the auto is suppressed); the re-assert (trigger 'Direct
  call', evidence 'SRC AccountTransactionListFragment.java:331
  (bytecode)' exactly as the auto record) restores the pair bit-for-bit
  (id Ed8e6a9c0 preserved post-build, verified). Spec citation nit
  noted: R2-A's evidence parenthetical placed the call one line
  early, but the auto record puts the plain call at :331; the cited
  range :327-331 covers both. Corrected citation (g4-full D3): the
  call is at :331. Citation corrections (g4-full D3, all three):
  R2-A call :331; Budget onLoaderReset guard :156 (see the in-place
  guard edit below); R3-E 03.py comment onCreateLoader id check
  :119. B7 rows must quote :331/:156/:119.
- Accept R3-C's suppression of auto Edf4d25c9 (@Payee onActivityCreated
  -> plain startLoader) as BENIGN (spec's "kept as a side branch"
  superseded by the receiver-variant exact-src rule): it kills an
  unnamed Payee->Categories splice; Categories survives via the kept
  plain chain (verified: CategoriesReportFragment.onLoadFinished
  14 steps via the kept plain chain, exactly as spec §(d)
  predicted). Correction (g4-full D4): the drawn 14-step route uses
  the kept plain chain (E3756fffc+Eb0a3bd39) and does NOT traverse
  E057603ab (0 drawn routes use it; it is a live 16-step
  alternative).
  Note (g4-full D2, benign): R3-C's base pair also suppresses plain
  E1c319b33 (onActivityCreated -> startLoader). Benign: its src node
  has zero incoming edges, it appears in zero drawn routes even
  without Search, and plain startLoader keeps 6 other incoming
  edges. No graph change.
- Search spec's Budgets citations off by 3 lines vs drawer spec +
  merger's own sed (null :887, item :1087-1090; verified :889-890,
  :1090-1093) — moot for the graph (R1-D skipped; drawer ADD 2's guard
  used); every other search-spec citation verified against the tree
  before applying.

Edits (in `graphs/MMEX/graph_def_mod/03.py`, appended after §6):
- R1-A (BudgetListFragment.onCreate -> AbsListFragment.onCreateView
  @BudgetListFragment, LIFECYCLE — the missing link) + R1-B
  (AbsListFragment.onCreateView@BudgetListFragment ->
  BudgetListFragment.onViewCreated, LIFECYCLE — receiver-partitioned
  delivery).
- R2-A (loadTransactions -> loadData(Bundle)@AccountTransactionListFragment,
  CALL, guard mAllDataListFragment != null) + R2-B (loadData(Bundle)@host
  -> onLoadFinished@host, FRAMEWORK) + R2-C (onLoadFinished@host -> host
  onLoadFinished, CALL, guard parent != null) + plain re-assert
  (Ed8e6a9c0, see above) + 2 guard hand replacements of AUTO edges
  (host onLoadFinished -> populateRunningBalance, guard loader id ==
  ID_LOADER_ALL_DATA_DETAIL :370-375; host onEvent ->
  displayRunningBalances, guard mAllDataListFragment != null :837).
Deletions in home files (tombstone comments left; ids confirmed from
the merger's own build output BEFORE deleting):
- graph_def.py:1660 (was :1673 at §7 time; §7 cited :1667, drifted
  by later edits — current line per g4-full audit) plain
  AbsListFragment.onCreateView ->
  BudgetListFragment.onViewCreated (LIFECYCLE, Ef021d80a).
- graph_def.py:916 (was :919) plain AllDataListFragment.onLoadFinished ->
  AccountTransactionListFragment.onLoadFinished (CALL, E2179223e).
- mod/01.py:3344 (was :3355 at §7 time; §7 cited :3350, drifted by
  later edits — current line per g4-full audit) plain
  BaseReportFragment.onCreate ->
  PayeeReportFragment.onActivityCreated (LIFECYCLE, E6fab2c3b).
- mod/01.py:3350 (was :3363 at §7 time; §7 cited :3358, drifted by
  later edits — current line per g4-full audit) plain
  BaseReportFragment.onCreateLoader ->
  PayeeReportFragment.onLoadFinished (FRAMEWORK, E7f8589cf).
In-place guard edits in graph_def.py (hand edges; current lines per
g4-full audit, §7 lines drifted by later edits):
- :1668 displayBudgets -> onCreateLoader (Ec38921e3): guard loader id
  == LOADER_BUDGETS (:131, initLoader :235).
- :1677 onCreateLoader -> onLoadFinished (E6029248f): guard loader id
  == LOADER_BUDGETS (:143).
- :1682 onLoadFinished -> onLoaderReset (Ef6edef5d): guard loader id
  == LOADER_BUDGETS (:156).
Not edited (flagged follow-up only): parallel plain forwards
onCreateLoader (~:915) and onLoaderReset (:925-929) with the same
host-instance defect (do not affect this target).

Rebuild: 4270 methods, 3430 REACHABLE / 840 UNREACHABLE (unchanged),
8235 edges, errors 0, warnings 0. No label flips.
Verification (all predictions exact):
- BudgetListFragment.onLoaderReset 19 steps via @GROUP + variant
  onCreateView (spec §(d) 19 steps); BudgetListFragment.onViewCreated
  15 steps via R1-A/B.
- AllDataListFragment.displayRunningBalances 24 steps via host prefix +
  variant loadData/onLoadFinished — the spec's SIMULATION middle
  (onCreateView -> S_ACCOUNT_TRANSACTIONS -> onOptionsItemSelected ->
  isStatusSelectionHandled -> loadTransactions), which the spec says to
  accept (both middles instance-correct, same total).
- Core.resolveColorAttribute 18 steps via plain child dispatcher +
  variant onCreate/startLoader/onCreateLoader chain (spec §(b) 18 steps,
  plain dispatcher at steps 5-7 per the drawer reconciliation).
- TransactionStatuses.<init> 15 steps UNCHANGED (search route survives
  the search group — reconciliation 6 confirmed; it uses plain
  loadData(Bundle) -> plain onLoadFinished -> bindView, all kept).
- Negative checks (all PASS on drawn-route scope; see the D1
  correction above for the strong-sense Payee qualification): no
  route to BudgetsActivity.<init>
  contains $4; no DRAWN route to PayeesReportActivity.<init> contains
  $3 (a $3 path via E61edcf43 exists in the full graph — drawer
  follow-up, not a Search claim); no
  route to BudgetListFragment.onLoaderReset, AccountTransactionListFragment
  .onLoadFinished, or displayRunningBalances contains SearchActivity; no
  route to Core.resolveColorAttribute contains CategoriesReportActivity
  or CategoriesReportFragment.
- Blast radii (all REACHABLE, none lost): Ef021d80a 8 methods;
  E2179223e 23 methods; E7f8589cf 6 methods; E6fab2c3b 4 methods.
  No built route uses any deleted edge id (checked all 19 deleted ids
  across the fix phase: NONE). No Budgets-hosted method's route still
  contains child-click E25d552ed (spec §(e) check, scoped to
  Budgets-hosted methods; the 2 non-REACHABLE Budgets methods —
  BudgetAdapter.getAmountForSubCategory, BudgetService.copy — were
  already UNREACHABLE in the B4 baseline, not a regression).
- Ed8e6a9c0 preserved (id identical post-build); Edf4d25c9 suppressed
  as predicted; E057603ab Categories edge kept; plain dispatcher ->
  PayeesReportActivity edge E3e34477a kept (drawer design).

## 8. Event group (event spec) — APPLIED + VERIFIED, with two honest prediction deviations (shorter valid routes, not partition failures)

Spec: `helper/b6-fix-event/SPEC.md` (812 lines), audit-PASS. Applied
route by route (R1, then R2, then R3) + §(f) guard replacements, never
a DELETE without its replacing variant edges in the same rebuild.

Edits (in `graphs/MMEX/graph_def_mod/03.py`, appended after §7):
- R1: onCreate -> onCreate@RESTORED (FRAMEWORK, cls non_standard, via
  androidx FragmentManager save/restore INFERRED) + onCreate@RESTORED ->
  createFromParcel (FRAMEWORK, guard restored filter dateRange
  non-null) + guard hand replacement E2207076a (isFilterSelected ->
  showFilterDialog, guard item id == menuTransactionFilters).
- R2: FixerService.onContentDownloaded -> WatchlistFragment.onEvent
  (PriceDownloadedEvent)@RETURNED (ASYNC, session needs_state via
  registered state_text, cls non_standard, via EventBus) + 2 guard hand
  replacements (onPriceDownloaded -> completePriceUpdate, guard symbol
  non-empty AND counter == total; displayHeaderData -> getAccount,
  guard accountId != NOT_SET).
- R3: 2 sup() pairs (onHandleWork -> sendMessage E060e9c23;
  triggerSync -> sendMessage E87011444) + 8 variant edges (@DOWNLOAD/
  @OTHER chains: onHandleWork/triggerSync -> sendMessage@DOWNLOAD/@OTHER
  -> handleMessage@DOWNLOAD/@OTHER -> onEvent, DOWNLOAD-only posts;
  deliberately NO @OTHER -> onEvent edge) + 4 guard hand replacements
  (initializeSync -> triggerSynchronization; triggerSynchronization ->
  invokeSyncService; invokeSyncService -> enqueueWork; onHandleWork ->
  triggerSync SYNC-branch guard E4ee94586).
Deletions in home files (tombstone comments left; ids confirmed from
the merger's own build output BEFORE deleting):
- graph_def.py:1441 (was :1447) plain onCreate -> createFromParcel
  (FRAMEWORK, E87fb73c0).
- mod/01.py:1986 (was :1985) plain Fixer -> Watchlist onEvent
  (ASYNC, Ea9af2cd3).
- mod/01.py:5314 (was :5323) plain sendMessage -> handleMessage
  (FRAMEWORK, E9ec99f56); :5008 (was :5017) plain handleMessage ->
  SyncPref onEvent (ASYNC, E1982f6fc); :741 (was :740) plain
  handleMessage -> MainActivity onEvent (ASYNC, Ef4a05204).
Not removed (deliberate, inert): the HAND_CLASS entry at graph_def.py:42
for (handleMessage, SyncPreferenceFragment.onEvent) — it classifies an
edge that no longer exists as plain; the new @DOWNLOAD edge sets
cls='non_standard' explicitly, so the entry cannot affect it. Removing
it is out of the spec's scope; recorded here so a future re-add of the
plain pair does not silently inherit it.
Known harmless residue (spec §(c), accepted): handleMessage@OTHER ->
DbFileDownloadedEvent.<init> fan-out (constructor only, no delivery —
cannot be cut with sup() since the plain pair must stay for @DOWNLOAD).

Rebuild: 4270 methods, 3430 REACHABLE / 840 UNREACHABLE (unchanged),
8256 edges, errors 0, warnings 0. No label flips. No built route uses
any deleted/cut edge id (E87fb73c0, Ea9af2cd3, E9ec99f56, E1982f6fc,
Ef4a05204, E060e9c23, E87011444 — all NONE).
Verification:
- R1 EXACT: DateRange.<init>() 24 steps via onCreate@RESTORED (spec
  §(d) 24 edges); blast 5 methods at 21/22/23/23/24 (+1 each, as
  predicted). Fresh-path edges :1435 (getParcel) and :1442
  (writeToParcel) kept.
- R2 DEVIATION (shorter valid route, spec prediction superseded, NOT a
  partition failure): getAccount prints 14 steps via the watchlist's
  OWN context-menu path (S_WATCHLIST -> onContextItemSelected ->
  getAccount), NOT the spec's predicted 20-step onResume path. Why the
  spec missed it: before the partition, cross (0,0,25) beat onContext
  (0,1,14) on setup count, so onContext never printed; after the
  partition, cross is (0,1,25) and onContext (0,1,14) beats onResume
  (0,1,20) on steps. Verified REAL from printed source: auto CALL
  E90abc1ad onContextItemSelected -> getAccount at
  WatchlistItemsFragment.java:249 (bytecode), GUI edge Eee5044ad ('Tap
  an item of the context menu of a security row'), prefix
  showWatchlistFragment -> newInstance (Ed218404b). The 14-step route
  is the watchlist's own path and is CORRECT if every step checks out
  — the redraw judging wave verdicts it fresh (flag for the wave: which
  context-menu branch holds the :249 call — the GUI text lists three
  items). Nit resolution (post-audit): the :249 getAccount call sits
  ONLY in the EditPrice branch (WatchlistItemsFragment.java:240-264;
  DownloadPrice :234-238 posts PriceUpdateRequestEvent, DELETE
  :266-268 shows the delete dialog, neither calls getAccount). GUI
  edge Eee5044ad is NOT narrowed: it is shared by 46 shortest paths
  through all three branches (EditPrice -> getAccount /
  PriceEditActivity subtree / IntentFactory.getPriceEditIntent;
  DownloadPrice -> PriceUpdateRequestEvent subtree; DELETE ->
  showDeleteConfirmationDialog subtree), so narrowing its text to
  EditPrice would falsify the DownloadPrice and DELETE routes' steps,
  and an EditPrice-only guard on the shared edge would leave those
  paths standing with a false guard annotation; only a three-way
  variant split would change topology (a structural change, not
  done). The getAccount
  route's branch is disambiguated by its NEXT step (E90abc1ad, :249
  getAccount, which exists only in the EditPrice branch), not by the
  GUI text alone. Items tail all REACHABLE via the shorter prefix (reloadData
  14, onCreateLoader 15, onLoadFinished 16, displayHeaderData 17,
  onLoaderReset 17, prepareArgsForChildFragment 15). Price tail all
  REACHABLE via @RETURNED (onEvent 17 as predicted, onPriceDownloaded
  18, completePriceUpdate 19, $2 20, getStockRepository 19,
  getStockHistoryRepository 19, FormatUtilities 18, bindView/newView
  17, viewHolder 18). Partition (not outright deletion) per coordinator
  decision MMEX-B6-WatchlistPartition; the outright-deletion fallback
  does NOT apply (return-interleaving was not ruled out).
- R3 CORRECTION (post-audit D-G5; supersedes the DEVIATION paragraph's
  message-correctness claim — the partition itself is unaffected):
  SyncPreferenceFragment.onEvent prints 10 steps via the DIRECT
  onHandleWork DOWNLOAD branch (initializeSync ->
  triggerSynchronization -> invokeSyncService -> enqueueWork ->
  onHandleWork -> sendMessage@DOWNLOAD -> handleMessage@DOWNLOAD ->
  onEvent), NOT the spec's predicted 11-step triggerSync DOWNLOAD path
  — but the drawn 10-step route is NOT message-correct, and the final
  table records it WRONG (route 12), which stands. Failure 1: step 5
  (E64d793d3) invokes the sync service with the SYNC action
  (SyncManager.java:348 invokeSyncService(INTENT_ACTION_SYNC),
  preserved verbatim by IntentFactory.setAction :42, no different
  action set by invokeSyncService), while step 8 (Ed4e987ec) guards on
  action == INTENT_ACTION_DOWNLOAD (SyncService.java:126-128);
  onHandleWork extracts the action via intent.getAction()
  (SyncService.java:91-93) and the switch (action) statement is at
  :125, so the SYNC case (:134-135, triggerSync)
  fires, never the DOWNLOAD case — the same intent cannot carry SYNC
  at step 5 and DOWNLOAD at step 8. Failure 2: step 10's subscriber is
  never registered on the prefix (SyncPreferenceFragment registers
  only in onStart :103-108, register call :107, unregisters onStop;
  the drawn prefix has no Settings/fragment-open step; the step-10
  ENV text describes the different forceDownload prefix, click :236
  -> forceDownload :307-308 -> triggerDownload -> DOWNLOAD at
  SyncManager.java:356-357). The partition works exactly as designed
  (UPLOAD prefixes dead-end at @OTHER, no @OTHER -> onEvent edge).
  The valid non-drawn alternative is the 11-step triggerSync
  remote-only branch (SyncService.java:206-210, pullDatabase +
  DOWNLOAD_COMPLETE) WITH a subscriber-open prefix — neither in the
  drawn route. Repair (re-feed @DOWNLOAD from the triggerSync branch
  + subscriber-open prefix + re-redraw + re-judge) remains a
  follow-up needing coordinator authorization; it is NOT done here.
  Coordinator decision MMEX-B6-SyncDrawn's criterion (a
  message-correct DOWNLOAD path as drawn) is therefore NOT met by the
  drawn 10-step route; the decision stands as the naming of the
  11-step alternative, not as a claim about the drawn route (BFS
  cannot be forced to prefer a longer path, and no graph fix is made
  for this claim). MainActivity.onEvent(DbFileDownloadedEvent)
  likewise prints 10 steps via direct DOWNLOAD with the SAME step-8
  defect (identical steps 1-9, including E64d793d3 + Ed4e987ec); its
  step 10 differs only in that MainActivity IS registered between
  onStart :141 and onStop :146 (MmxBaseFragmentActivity), so the
  registration failure does
  not apply to it — but the message-incorrectness does, and no
  'message-correct' claim is made for it either (final edge env None,
  so env kinds 0, is unchanged).
  sendMessage/handleMessage stay REACHABLE via variants (8/9 steps);
  handler-body methods all REACHABLE (parse 10, closeDialog 10,
  getContext 10, DbFileDownloadedEvent.<init> 10, closeProgressDialog
  11, useDownloadedDatabase 11, getInstance 12).
- Guard-replacement step counts: old ids retire (E2207076a, E4d4c7f5a,
  E54bd84fb, E09bcb83d, E900fb1cd, E0e96bbf6, E4ee94586); stored
  verification rows naming those ids need re-issuing against the new
  ids (B7 concern, not a B6 block).

## 9. Backup-agent decision: DatabaseManager.getContext FALLS BACK TO WRONG-WITH-REASON (no partition applied; guards applied)

Result2 spec §3 + task order step 6 investigation (merger, from printed
source + built graph — NOT from the spec's summary alone).

Current route (unchanged by all fix groups): 8 steps via MainActivity
(S_ENTRY -> MainActivity.<init> -> onCreate -> showCurrentDatabasePath
-> getDatabasePath -> getDefaultDatabasePath ->
getDefaultDatabaseDirectory -> getPackageDirectory -> getContext).
Step 5 (E12cf38a6) is WRONG on this prefix by the J10 proof, re-verified:
onCreate `if (showPrerequisite()) { finish(); return; }` (:184-187)
means everything after :184 runs ONLY when a valid database exists
(showPrerequisite false ⟺ tutorial not needed AND stored path non-empty
AND file exists, :1338-1348 + :1478-1499); between :184 and the
showCurrentDatabasePath call (:223), onCreate runs only
migrateRecentDatabases (:190, recent-files map only), handleIntent
(:210, via changeDatabase sets a VALID file), restoreInstanceState
(:213-215, booleans only), handleDeviceRotation (:217, back-stack
only) — nothing deletes the file or clears the path. So at :223 the
file EXISTS, getDatabasePath early-returns (:44-49), and the step-5
fall-through (stored path empty OR file missing, call :54) is
IMPOSSIBLE on this prefix. The backup prefix EXISTS verbatim
(E3f865c2d ENTRY with system_event env, E58735491 LIFECYCLE, E5385d81d
auto CALL :46; BackupAgent onCreate at :38, not :41) but costs
(1 env, 0, 7) vs MainActivity (0, 0, 8) — env dominates steps, so BFS
will not return it while the MainActivity path exists (result2 §3(d),
confirmed by simulation).

Per-caller investigation (all 8 graph callers of getDatabasePath, all
auto CALLs; prefix costs are (env, setup, steps) to the caller, hence
+5 edges to getContext via the plain tail):
- showCurrentDatabasePath (:1426): CONTRADICTED (J10 proof above).
  Graph prefix (0,0,3) -> getContext (0,0,8). [Sketch dead-end candidate.]
- MmexApplication.createDbInstance (:243, calls getDatabasePath iff
  passed path empty): CONTRADICTED on the graph. Graph prefixes:
  useDatabase/changeDatabase (7 -> getContext 12; passed path is the
  valid changed file, non-empty -> :243 branch NOT taken) and
  DbModule.provideOpenHelper -> initDb(null) (9 -> getContext 14;
  null path means getDatabasePath IS called, but on the onCreate prefix
  the file exists -> early return, no fall-through). Uniformly
  contradicted on the graph (both prefixes pass onCreate :184).
- MainActivity.onOpenDatabaseClick (:1361, quick-switch recent
  databases): CONTRADICTED on the graph prefix (drawer ->
  PasswordActivity -> onActivityResult -> onOpenDatabaseClick, 14 ->
  getContext 19; MainActivity existed before PasswordActivity, so
  onCreate passed and the current file exists under the linear model).
- DatabaseMetadataFactory.createDefaultEntry (:73, transition from
  preferences to metadata records): CONTRADICTED on the graph prefix
  (onCreate -> migrateRecentDatabases -> RecentDatabasesProvider
  .getCurrent -> createDefaultEntry, 5 -> getContext 10; migrate is
  called ONLY from onCreate :190, after the :184 gate; getCurrent's
  other source callers (DatabaseSettingsFragment, SyncManager,
  SyncPreferenceFragment, EditTransactionCommonFunctions) call
  getCurrent() on the metadata list, not createDefaultEntry — the
  graph edge to createDefaultEntry is only via getCurrent's
  createDefaultEntry call at RecentDatabasesProvider.java:128, reached
  via migrate).
- HomeFragment.createWelcomeView (:607, "Show current database" text):
  CONTRADICTED on the graph prefix (onCreate -> initHomeFragment ->
  onCreateView -> createWelcomeView, 5 -> getContext 10; initHomeFragment
  is called ONLY from onCreate :238, after the :184 gate; HomeFragment
  is MainActivity's home fragment, never hosted with no database since
  MainActivity finishes on showPrerequisite).
- SyncManager.triggerSynchronization (:336): MIXED (the one mixed
  caller). MainActivity prefixes CONTRADICTED (initializeSync :242,
  4 -> getContext 9; drawer dispatcher incl. @GROUP/@RECURRING fan-outs
  from MainActivity:615 — all require onCreate passed). Broadcast
  prefix VALID: SyncBroadcastReceiver.onReceive (5 steps, env-free,
  1 setup: sync enabled + interval > 0) -> triggerSync -> getDatabasePath
  -> tail = getContext (0,1,11); canSync() (SyncManager.java:103-124)
  checks only isActive() (sync enabled, online, wifi, remote non-empty)
  + wifi — NO local database file check — so fall-through is genuinely
  possible when sync is configured but the local file is missing.
  Dead-ending triggerSync would DELETE this real broadcast
  fall-through from the graph (forbidden: never delete a real call
  outright).
- SyncManager.useDownloadedDatabase (:372, installs a downloaded
  database): CONTRADICTED on the graph prefix (MainActivity.onEvent
  (DbFileDownloadedEvent) -> useDownloadedDatabase, 11 -> getContext 16;
  MainActivity.onCreate passed; the download does not delete the
  current file under the linear model).
- MoneyManagerBackupAgentHelper.onCreate (:46): VALID (backup can run
  before any database is configured; fall-through genuine). Prefix
  (1 env, 0, 2) -> getContext (1,0,7).

Why the 3-edge sketch FAILS: dead-ending showCurrent + feeding backup
leaves 6 contradicted env-free callers on plain; BFS picks
triggerSync/initializeSync (0,0,9) — contradicted — still wrong.
Why the FULL fix is MESSY (fallback criterion met): it needs 6
dead-ends + triggerSync prefix-partition (4 MainActivity feeders ->
triggerSync@MAIN + mirrors of triggerSync's 10 non-getDatabasePath outs
+ 10 plain re-asserts, because hand mirrors suppress plain auto outs by
the base-pair rule) + backup feeding variant = ~32 edges, with blast
risk to the sync subtree (every downstream sync method's prefix).
Without mirrors, MainActivity sync routes reroute via broadcast
(distorting the primary sync path); without re-asserts, plain
triggerSync loses its outs (breaking broadcast sync routes). A 32-edge
rework with sync-hub mirrors for a single sample route is
disproportionate in the B6 fix phase, and the task authorizes fallback
when "the caller list is messy" — it is (6 uniformly contradicted + 1
mixed). The full design is RECORDED here for a future worker or a
coordinator decision to apply it (it is sound, just messy); it is NOT
applied now, and NO edge is deleted to force the backup route (the
spec's prohibitions stand: no MainActivity edge deletion, no backup
env stripping, no tail-split).

DECISION (merger's own, for user/Yang review): DatabaseManager
.getContext falls back to WRONG-WITH-REASON in the final table, with
the J10 guard-contradiction proof above. The backup (1,0,7) and
broadcast (0,1,11) prefixes remain VALID non-shortest alternatives,
documented in the table, not drawn. This is the ONLY route of the 15
WRONG routes to fall back (the other 14 are fixed by the dispatcher
splits above); the final table carries it as wrong-with-reason, not as
an unexamined wrong.

Guards applied regardless (result2 §3(f), task order step 6; all three
are AUTO edges -> hand replacements in 03.py, ids renumber, routes
unchanged — verified: getContext still 8 steps, same nodes):
- Step 3 (Ec1f7c9c2, onCreate -> showCurrentDatabasePath): guard
  '!showPrerequisite() (:184-187; definition :1478-1499)'.
- Step 5 (E12cf38a6, getDatabasePath -> getDefaultDatabasePath): guard
  'stored database path is empty OR its file does not exist (:44-49;
  fall-through :54)' — this guard CONTRADICTS the step-3 guard on the
  MainActivity prefix and is satisfiable on backup/broadcast.
- Step 7 (Ed1acc672, getDefaultDatabaseDirectory -> getPackageDirectory):
  guard 'getDbExternalStorageDirectory() == null AND
  getExternalFilesDirectory() == null (:90-94; call :97)'.
Steps 6 and 8 unconditional (:74-76, :161-163); no guard. The guard
corrections make the contradiction EXPLICIT in the edge text (they do
not change BFS cost — guards are text, not env/needs_state).

Rebuild after guards: 4270 methods, 3430 REACHABLE / 840 UNREACHABLE
(unchanged), 8256 edges, errors 0, warnings 0. No label flips.

## 10. Guard group: 46-recorded-corrections pass (LAST) — APPLIED + VERIFIED

Applied after all structural groups (guard edits change edge ids and
would stale helpers' blast-radius greps if applied earlier). Source:
exact guard texts from b6-j8 (route 24), b6-j9 (routes 25-27), b6-j10
(routes 28 + 30) JUDGMENTS.md — NOT reconstructed from memory.

SCOPE ACCOUNTING (the "46" first-draw fixed-step total vs what is
applied here — read carefully, this is the merger's reconciliation):
- APPLIED (23 edges): the 19 corrections for the 6 FIXED routes (J8
  route 24: 3; J9 routes 25/26/27: 3 each = 9; J10 route 28: 4, route 30:
  3) + 3 verified extras for still-existing unguarded edges
  (E346a1795 onOptionsItemSelected -> SearchActivity, guard item id ==
  menu_search; E87646b1f dispatcher -> CategoriesReportActivity, guard
  menu_report_categories; E303c403e onLoadFinished ->
  renderAccountsList, guard loader id == LOADER_ACCOUNT_BILLS).
  Of the 23: 4 are HAND edges -> in-place guard edits (mod/02.py:1172
  E0c39a837, :1297 E82052096; mod/01.py:3426 E346a1795, :3053
  E87646b1f); 19 are AUTO edges -> hand replacements in 03.py.
- NOT RE-APPLIED (already covered by structural specs — re-applying
  would overwrite those specs' guards): drawer D guards (About steps
  11/12, DDR steps 10/11/16, E39526a56 + E2aab9f64 retired under new ids
  by the drawer in-place guards at mod/01.py:4785/:4879), result1
  §§1.6/2.6/3.6, result2 §§1(f)/2(f)/3(f) (incl. Ec1f7c9c2 + Ed1acc672
  in §9), search §§(c)/(f) (E72c81aec, Ee33a1f51, Ec38921e3, E6029248f,
  Ef6edef5d), event §§(f) (E2207076a, E4d4c7f5a, E54bd84fb, E09bcb83d,
  E900fb1cd, E0e96bbf6, E4ee94586), merged widget edge E37b8fad5 (§5).
- MOOT (edge deleted by a structural partition — no guard to apply):
  E23751ccf, E20490343, Edc2b1ed0, E1760f123, Ec72b7276, Edcb3f4b6,
  E00164e96, E99cd6390, Ef021d80a, E2179223e, E6fab2c3b, E7f8589cf,
  E87fb73c0, Ea9af2cd3, E9ec99f56, E1982f6fc, Ef4a05204, E060e9c23,
  E87011444 (+ suppressed autos).
- NOT APPLIED (contested): Ec1f72a40 (S_HOME -> onOptionsItemSelected)
  — judgments disagree (one group: correct with guard None, "method
  entry fires for any menu item tap"; another: fixed with menu_search
  guard). The menu_search condition is applied on the NEXT edge
  (E346a1795, see above), which both judgments agree on. The redraw
  judging wave verdicts Ec1f72a40 fresh; do NOT silently pick a side
  here.
- The remaining first-draw fixed-step instances (46 total instances
  across routes, some edges counted in multiple routes) are either in
  the categories above or on routes whose steps changed structurally
  (their old fixed steps no longer exist on the redrawn routes). No
  guard text is invented: every applied guard is quoted from its
  judgment (with file:lines); every skipped guard names its reason
  above. If the redraw judging wave finds fixed steps on redrawn
  routes, those are recorded as FIXED verdicts in the final table
  (honest, not hidden) — the wave judges, it does not trigger another
  correction pass (that would be endless).

Special records:
- Route 28 joint condition (J10): step 3 guard keeps the judgment's
  exact text (uid == null OR uid.isEmpty()) AND step 4 guard (exists,
  getInfoValue != null); jointly satisfiable ONLY by a stored EMPTY
  (non-null) UID — recorded in the route table as "stored UID value is
  empty (non-null)", never as the null-UID case reaching step 4.
- Route 30 compatibility note (J10): the guards record the
  already-configured-database + intent-file case, NOT cold-start
  (cold-start fails showPrerequisite and never reaches handleIntent).

Rebuild: 4270 methods, 3430 REACHABLE / 840 UNREACHABLE (unchanged),
8256 edges (net 0: each hand replacement suppresses 1 auto and adds 1
hand; in-place guards change ids only), errors 0, warnings 0. No label
flips.
Verification: all 6 FIXED routes redraw with IDENTICAL node sequences
and step counts (NumericHelper 8, AccountRepository.first 7,
prepareQuery 10, logUpdate 9, getUploadImmediately 8,
MmxOpenHelper.<init> 8) — only ids changed, as required for
topology-safe guards. The redraw judging wave re-reads every changed
route per brief step 6 (that re-read IS the wave, not a separate step).

D-G7 correction (post-audit): the audit found a 46th first-draw
fixed-step instance unaccounted in the reconciliation above (APPLIED
22 + NOT RE-APPLIED 18 + MOOT 3 + contested 1 + structurally-
partitioned 1 = 45): b6-j2 route 3 (SqlRepositoryBase.first) step 14,
WatchlistFragment$4.onClick -> MorningstarPriceUpdater.downloadPrices
(auto E6ec96bae, guard None). APPLIED is now 23: this edge's hand
replacement (guard InvestmentSettings.getQuoteProvider() ==
QuoteProviders.Morningstar, SecurityPriceUpdaterFactory.java:38-42)
is appended at the end of the §10 block in 03.py; 23 + 18 + 3 + 1 + 1
= 46, so the accounting now closes. The route was not resampled, so
no redraw wave re-judged it (final methods.csv still draws it in 20
steps with the new hand edge at step 14). Yahoo sibling edges from
the same onClick stay unguarded (separate dispatch targets; this
guard applies to the Morningstar target only).

## 11. REDRAW (final sample) — 2026-11-01

Command (from tree root): `python3 -I tools/verify_sample.py MMEX 30 20261025`
> tree/graphs/MMEX/scratch/sample_30_final.txt. First-draw
sample_30.txt untouched for history.

RESULT: same seed, DIFFERENT 30 methods (expected: the sampler is a
greedy coverage pick over strata + a seeded shuffle of methods.csv row
order, and the fix phase changed routes, strata, edge ids, and row
order). Quotas still met exactly (NONSTD 4, INFERRED 4, STATE 3, ENV 6,
LONG 6, PLAIN 7 = 30). Header: "30 of 3430 reachable methods, 341
distinct edges on their routes (seed 20261025)" (first draw: 323).

Redrawn sample (30): DbModule_ProvideSqlBriteFactory.get (27),
SplitCategoriesActivity$1.<init> (24), AllDataListFragment.
displayRunningBalances (24), Stock.setSymbol (22), Passcode.savePasscode
(29), SplitRecurringCategoriesRepository.insert (23),
StockHistoryRepository$UpdateType.<init> (21), StockHistoryRepository.
getContentValues (20), CategoryListFragment$2.onClick (16), Core.
resolveColorAttribute (18), DateRange.<init>() (24),
SyncPreferenceFragment.onEvent (10), RecurringTransactionIntentService.
onHandleWork (7), IncomeVsExpensesListFragment$1.run (11),
RecurringTransactionListActivity.onActivityResult (9), TutorialActivity.
onOptionsItemSelected (8), SingleAccountWidgetConfigureActivity.
saveTitlePref (4), Stock.getNumberOfShares (17), ExceptionHandler.
getLogcat (16), AboutFragment.getLogcat (17), DefinedDateRange$1.<init>
(20), QueryAccountBills.setReconciled (12), Budget.setName (20),
NumericHelper.getNumberOfDecimals (8), AccountRepository.first (7),
MmxContentProvider.prepareQuery (10), MmxContentProvider.logUpdate (9),
SyncPreferences.getUploadImmediately (8), DatabaseManager.getContext
(8), MmxOpenHelper.<init> (8).

Composition vs first draw: 10 of the 15 fixed WRONG routes ARE in the
redraw (DbModule, $1, displayRunningBalances, Passcode, Split insert,
DateRange, Core, SyncPreferenceFragment, About, DefinedDateRange) + the
getContext fallback + all 6 FIXED + all 3 CORRECT + 4 UNCLEAR (Stock.
setSymbol, CategoryList$2, RecurringIntentService, IncomeVsExpenses$1)
+ 6 NEVER-JUDGED (StockHistory$UpdateType, StockHistory.
getContentValues, Stock.getNumberOfShares, ExceptionHandler.getLogcat,
QueryAccountBills.setReconciled, Budget.setName). NOT in the redraw (6):
WatchlistItemsFragment.getAccount, SqlRepositoryBase.first,
TransactionStatuses.<init>, HomeAccountsExpandableAdapter.getAccountData,
EditTransactionCommonFunctions.resetCategory, BudgetListFragment.
onLoaderReset. Their fixes stand on the fix-phase reprint verifications
(§§7-8: Watchlist 14, resetCategory 17, BudgetList 19, TransactionStatuses
15 — all verified node-for-node at apply time); they are NOT in the
final sample and are NOT re-judged as part of it. The final error rate
is computed on the redrawn 30, per the brief ("final sample redrawn
after last fix") — the tool's output on the fixed graph IS the final
sample, not a failure to reproduce the first draw.

DUMP TOOLING (important): tools/show_route.py CRASHES on 18/30 redrawn
routes (ValueError in snippet(), int('') on citations of the form
"File.java:26, 108-112" — its capture stops at the space, leaving a
trailing comma). Pre-existing bug (the crashing ENTRY edge is B4-era),
NOT caused by B6 edges; tools/ is out of the merger's scope, so it was
NOT edited. Workaround: merger script
dump_routes.py (merger work dir) (NOT in tools/)
replicates the print with a citation parser handling comma-space
multi-ranges. All 30 dumps regenerated into
tree/graphs/MMEX/scratch/route_print_final/ (first-draw route_print/
untouched): 0 crashes, all step counts verified against methods.csv
(6,339 lines total).

JUDGING WAVE 1 (spawned): helpers b6-redraw-h1..h5 (max 3 routes each):
h1 DbModule/$1/displayRunningBalances; h2 Passcode/Split insert/
DateRange; h3 Core/SyncPreferenceFragment/About; h4 DefinedDateRange/
Stock.setSymbol/CategoryList$2; h5 RecurringIntentService/
IncomeVsExpenses$1/getContext. Wave 2 (h6..h10: 3 CORRECT, 6 FIXED,
6 NEW) follows wave 1. Every helper output gets an independent audit
before acceptance; re-drawn routes judged on their new dumps only.

## 12. REDRAW JUDGING WAVE + INDEPENDENT AUDITS + FINAL TABLE — 2026-11-01

Judges: b6-redraw-h1..h10 (max 3 routes each, staggered waves), all
read-only, every step judged fresh on the NEW dumps in
tree/graphs/MMEX/scratch/route_print_final/ (merger dump script, NOT
tools/show_route.py — see §11 for the show_route crash + the two
dump-script fixes: comma-space citations, core/... app paths, bare-name
FW fallback; final dumps: 0 "not found", all step counts verified).
Auditors: b6-redraw-a1..a10 (one per helper), all read-only. NO helper
output was FAILed; no route required re-judging. All audits PASS or
PASS-WITH-CORRECTIONS; every correction is incorporated in
tree/graphs/MMEX/scratch/route_table.md (the FINAL table).

Unaudited wave totals -> audited final (the ONLY verdict change from
audits is h5, by its own auditor a5):
- Wave 1 unaudited: 6C/4F/3W/2U (280 steps) -> audited: 7C/4F/3W/1U.
- Wave 2 unaudited = audited: 6C/6F/2W/1U (177 steps).
- FULL unaudited: 12C/10F/5W/3U (457 steps), rate 15/27 = 0.5556.
- FULL AUDITED: 13C/10F/5W/2U (30 routes); steps 423c/24f/7w/3u (457);
  final error rate = (10+5)/(13+10+5) = 15/28 = 0.5357.
- The single audit verdict change: onHandleWork UNCLEAR -> CORRECT (a5
  overturned h5's strict line; steps 4 + 7 standard delivery verified).
  IncomeVsExpenses steps 5, 8, 9 UNCLEAR -> CORRECT, step 10 UNCLEAR ->
  FIXED ("YEARS loader"); route stays WRONG. All other audits confirmed
  their helpers (citation/wording corrections only).

INFERRED-delivery standard (auditor consensus, a1-a10 — governs the
table): verified app-side endpoints + standard dispatch semantics +
explicit INFERRED flag + nothing contradicting = CORRECT/FIXED (a1's
5-condition test). UNCLEAR only for genuine app-side doubt (ambiguous
logic, unverified guard, unknown branch, hidden identity routing —
androidx FragmentActivity). Failed precondition = WRONG (a3); proven
absence of subscriber/recipient = WRONG (a9). Strict blanket line
rejected (a5 infinite-regress argument). FW-SRC analogies are analogy
only (a1). Full per-auditor rulings in redraw_wave1_notes.md.

Audit corrections incorporated in the table (all citation/wording except
the h5 verdict changes above): Passcode step 23 :45 -> :43 (a2); $1 step
24 evidence :320 -> :318-321 (a1); display step 16 "Direct call" ->
guarded call + step 14 narrowing (a1); display step 22 delete stale
"(not found)" parenthetical (a1); Recurring step 3 citation :1478-1482 ->
:1478-1489 (a6); logUpdate step 9 note :37 -> :36 (a8); IncomeVsExpenses
step 5 + View.java citation, step 10 "YEARS loader" annotation (a5).
Also recorded: h5's own tally table miscounted route 2 (6c/3u) vs its
step table (5c/4u); a5's corrections applied to the STEP tables give the
consistent corrected counts used in the table (8c/2f/1w) — step tables
are authoritative.

WRONG routes, audited (5): SyncPreferenceFragment.onEvent (steps 8-10;
CONFIRMED event-fix defect — @DOWNLOAD fed by a SYNC-action prefix; repair
= re-feed from triggerSync remote-only-modified branch + subscriber-open
prefix, coordinator authorization required); IncomeVsExpenses$1.run
(step 11; REPORT-only post on a YEARS prefix); DatabaseManager.getContext
(step 5; guard contradiction — wrong-with-reason fallback, §9 + table
route 29); StockHistoryRepository.getContentValues (step 17; no
WatchlistFragment subscriber on the prefix); Stock.getNumberOfShares
(step 15; Calculator result to the wrong activity). The last two are NEW
routes, not fix-phase touched.
UNCLEAR routes, audited (2): Passcode.savePasscode (steps 21 + 27,
androidx identity routing); ExceptionHandler.getLogcat (step 16, no
printed Toast-throw trigger).
FIXED steps (24) inventoried in the table, incl. the systematic
showPrerequisite guard gap on the onCreate -> :244 edge (routes 15 + 26,
found independently by h6 + h7, confirmed by a6 + a7) — recorded, NOT
applied to the graph in this task.

STOP: no B6 push made. The manifest is in the table (graph files +
first-draw + redrawn samples + route_table + both route_print dirs,
~2.43 MB total, every file < 900 KB; out/ + __pycache__/ excluded;
ABSENT claims to be re-verified with `ref` under the push lock at push
time). B7 logs + D1/D3/D7 proceed ONLY from this final sample, after
independent fix audits PASS. Open coordinator follow-ups: (1) Sync
re-feed, (2) routes 8 + 18 recipient-identity repairs, (3)
showPrerequisite guard on :244, (4) §9 getContext 32-edge repair, (5)
B7 + D1/D3/D7 from the final sample. Each repair needs a fresh redraw +
re-judge; 0.5357 is the audited rate for the CURRENT graph.
