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
