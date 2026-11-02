# MMEX 2024.06.14: method-level trigger graph (schema 2)

How every method of **MMEX** is triggered, in the standard configuration: the instrumented debug build (`moneymanagerex/android-money-manager-ex@2024.06.14.1033`, commit `f6e8d005340b`, APK sha256 `5bedb170...`), an API 27 emulator, permissions and fixtures as in `final_java_only`. Labels follow `handoff/SCHEMA_V2.md`: REACHABLE or UNREACHABLE, ENV and STATE gates, edge classes (explicit, standard, non-standard), and how each label was confirmed.

## What is in this folder

| File | What it is |
|---|---|
| `mmex_trigger_graph.json` | pages, methods, `verdict`, `labels` (per-method fields), `edges` (with `edge_class`, `env_kinds`, `state_kinds`, stable ids), `paths` (verified paths only), `verification` (counts) |
| `methods.csv` | one row per method: verdict, UNREACHABLE reason, ENV and STATE kinds and texts, edge classes on the best route, whether an explicit/standard-only route exists, how the label was confirmed, path status, and the derived best route (`shortest_path`, `route_edge_ids`) |
| `../verification.csv` | the audit log: one row per label, edge or path that was checked, with result, how, and where (file:line) |
| `sanity_check.csv` | tool coverage (Monkey / APE, API 27) next to the labels; a one-way check only, it never sets a label |
| `mmex_trigger_graph.html`, `build_report.txt` | the viewer and the validation report |

## Numbers

- **4270 methods**, **43 pages** (including pseudo pages), **8441 edges**. Verdicts: **3430 REACHABLE**, **840 UNREACHABLE**.
- UNREACHABLE by reason: branch_never_taken 13, closed_by_api_level 9, framework_never_calls 77, no_trigger_in_app 741.
- ENV gates (methods): hardware 9, network 4, other 11, other_app 44, system_event 28, time 6. STATE gates (methods): account 386, data 42, session 9, settings 481. Methods with no gate: 2860.
- Edge classes: explicit 6965, non_standard 497, page 53, standard 926. Non-standard edges: 497 (AbstractAccountAuthenticator binder stub: onBind returns the IBinder from getIBinder, and the stub dispatches addAccount (the library and AccountManagerService are not in fw_src; INFERRED); Activity.runOnUiThread (fw_src core/java/android/app/Activity.java:6170-6176); AmplitudeKt.Amplitude (com.ampl).
- 1396 reachable methods have a non-standard edge on their best route; 931 have no explicit-or-standard-only route at all.
- Labels confirmed by: INFERRED 2756, SOURCE 1514 (SOURCE: every edge of the best route cites a source line, in the app or in the Android 8.1 / library source; INFERRED: some edge rests on inference or on another app).

## How much to trust it

Verification log (`verification.csv`), counts of what was checked and found:

| Checked | Rows | Correct | Errors found (fixed) | Unclear |
|---|---:|---:|---:|---:|
| labels | 870 | 860 | 8 | 2 |
| edges (framework and other claims read against source) | 0 | 0 | 0 | 0 |
| paths (stratified sample, read step by step) | 30 | 20 | 8 | 2 |

Path status over all reachable methods: SOURCE_OK 28, UNCHECKED 3402.
The rows are the items that were individually checked, not a random sample of all labels; see the notes below for how they were chosen and what the unclear rows wait for.

Edges whose evidence is not a source line (859 of 8441): E19395ce1 (S_ENTRY -> PayeeActivity.<clinit>); E76a7aa66 (SearchParametersFragment$1.onClick -> PayeeActivity.<clinit>); E6f579f87 (EditTransactionCommonFunctions$9.onClick -> PayeeActivity.<clinit>); E87a1872f (AboutActivity.onCreate -> AboutTabAdapter.getCount); Ee835bc9a (AboutActivity.onCreate -> AboutTabAdapter.getItem); Eb0b17b72 (S_ABOUT_ACTIVITY -> AboutTabAdapter.getItem); E388582e3 (AboutActivity.onCreate -> AboutTabAdapter.getPageTitle); E503e054a (AboutActivity.onCreate -> AboutActivity.onRestoreInstanceState); Ea0013de2 (AboutCreditsFragment.<init> -> AboutCreditsFragment.onCreateView); Eeff0a2bf (AboutCreditsFragment.onCreateView -> AboutCreditsFragment.onActivityCreated); Ecef22362 (AboutFragment.<init> -> AboutFragment.onCreateView); E9a349a2e (S_ABOUT_TAB -> AboutFragment$1.onClick) ...

Sanity check against tool coverage (never used to set a label): 271 methods ran in the 1-hour Monkey / APE runs on API 27; **0** of them are labelled UNREACHABLE.

# MMEX readme notes — B7 draft (from the final route table and the B7 run log)

Final build (private rebuild of the current tree sources):
4270 methods, 3430 REACHABLE / 840 UNREACHABLE, 8441 edges,
errors 0, warnings 0; checks 2, 3, 4 at 0; check 8 at 19/840.
Final route table: CORRECT 20 / FIXED 8 / WRONG 0 / UNCLEAR 2
= 30 routes; error rate (fixed + wrong) / (correct + fixed
+ wrong) = 8/28 = 0.2857 (UNCLEAR excluded). Verification
rows: 30 path + 870 label + 0 edge = 900, written only by
`graphs/MMEX/make_verification.py` from the final sample and
the final table. Sampled reachable methods get a label row
carrying the path verdict (see `B7_RUN_LOG.md` section 8 for
the reading rule).

## What the re-audit changed (compared with the schema 1 graph)

- Strict mode on, and the check backlogs cleared: citation
  problems (43 at B2 start) to 0, bytecode-line problems (244
  at B3 start) to 0, with the DEAD wording reworded (B5) and
  every check-8 method's caller named and explained (19).
- Visit-agnostic edges were partitioned where the route
  checks proved them wrong: the drawer dispatcher split into
  @GROUP variants; the activity-result chains into @CHECKING
  and @RECURRING variants; the calculator result delivery
  into four per-launcher variant chains (@NUM_SHARES,
  @PURCHASE_PRICE, @COMMISSION, @CURRENT_PRICE), replacing
  the single plain RESULT edge; the sync delivery into
  @SYNC/@DOWNLOAD/@UPLOAD variants with the @MAIN partition
  of `triggerSynchronization`; the loader-id chain into
  @YEARS/@REPORT variants; and the scheduled-transactions
  feeder guarded by `!showPrerequisite()`.
- Edge ids changed wherever an edge's text changed (see
  `B7_ID_MAP.md`: the B6 set of 10, plus 33 stage-to-final
  retirements and the intermediate §9 mirror id retired by
  Sync). No label flipped in the whole re-audit: REACHABLE
  3430 / UNREACHABLE 840 at both the stage-B6 baseline and
  the final build.
- The final table was judged fresh on a redrawn sample after
  the last fix; B6 verdicts were not carried over, and the B6
  error rate (0.5357) is not carried forward either.

## How the checked paths were chosen

- After the last fix, the sample was redrawn with the brief
  command `python3 -I tools/verify_sample.py MMEX 30 20261025`
  (seed 20261025): 30 of 3430 reachable methods, 344 distinct
  edges on their routes. Strata: NONSTD 4, INFERRED 4,
  STATE 3, ENV 6, LONG 6, PLAIN 7.
- Every route was printed step by step (30 prints in
  `graphs/MMEX/scratch/route_print_final2/`) and every step
  judged against its printed source lines, including if,
  catch, and for conditions. The table covers only this
  final draw; routes whose steps changed were re-read and
  re-judged.
- One path row per route in this final sample appears in
  `verification.csv`; the label rows cover all 840
  UNREACHABLE methods plus the 30 sampled reachable methods.
- The sample above was drawn before the log step (the B7
  writer run) wrote `verification.csv`. The label rows the
  log step wrote change which 30 methods the sampler picks
  on the final graph, so a fresh sampler run now draws a
  different 30; the judged routes in this table are still
  current — the writer's STALE check passed (every path
  row's edges equal the method's current `route_edge_ids`,
  0 STALE refusals) and the cdab515a status-check rebuild
  ran with checks 2/4 at 0 and 0 STALE warnings.
- Why `verification.csv` has 0 edge rows although the final
  table has 14 FIXED steps: an edge row is emitted for
  exactly one thing — a corrected graph edge listed in
  `scratch/corrected_edges.tsv` (writer docstring and code;
  B7 run-log section 5). The 14 FIXED steps are judging
  corrections (guard/citation readings recorded on the
  route's path row), not corrections to any graph edge's
  text, and no audited MMEX source names a corrected edge
  with an id and ref; the B6 construction changes (edges
  added, suppressed, retargeted) are already represented
  through the path rows' current `route_edge_ids`, and
  re-listing them as edge rows would double-count
  construction as route-check evidence. `corrected_edges.tsv`
  is therefore explicitly empty (0 bytes), which is the
  writer's required way to record zero edge rows — not a
  missing input. Inventing edge rows from FIXED steps would
  violate the no-invention rule; if a qualifying corrected
  edge with audited evidence is later identified, the remedy
  is to populate `corrected_edges.tsv` and re-run the writer,
  never to hand-add a row to `verification.csv`.

## What waits for a device (API 27)

- Everything device-side. This CSV carries SOURCE/INFERRED
  rows only; no DEVICE row appears (DEVICE rows are a later,
  separate change, when device results exist). No emulator
  run was started in this phase, and none is claimed.
- The two UNCLEAR routes need device-side confirmation most:
  route 5 (Passcode.savePasscode, steps 21 and 27: androidx
  fragment result dispatch routing is not in the framework
  sources held) and route 19 (ExceptionHandler.getLogcat,
  step 16: reached only inside a catch, with no printed
  trigger for the throw on this prefix).
- Routes whose steps rest on INFERRED framework or library
  delivery (flagged as such in the table) were judged CORRECT
  under the INFERRED-delivery standard, not by device
  observation; a device run may still confirm or overturn
  those steps.

## Hazard candidates (from reading the code, not reproduced)

- The @GROUP drawer prefix still inherits the auto
  `showFragment(Class)` fan-out, so a group prefix can still
  reach a child item (e.g. AccountListFragment.<init>);
  fully partitioning that fan-out is a separate follow-up,
  not part of this log.
- Passcode's fragment result dispatch (route 5, steps 21 and
  27): the androidx FragmentActivity dispatch that would
  route an activity result to the requesting fragment is not
  in the held framework sources, so the dispatch step is
  UNCLEAR rather than verified.
- ExceptionHandler.getLogcat (route 19, step 16): the method
  is reached only inside the catch at
  log/ExceptionHandler.java:119, and no printed trigger for
  `Toast.makeText(...).show()` throwing on this prefix was
  found (BadToken/finishing/destroyed searched, none;
  mContext null-guarded, main-looper handler, non-null
  string resource). Not WRONG, since a throw cannot be
  proved impossible; not CORRECT, since no trigger is shown.

## Limits

- Coverage: 30 sampled routes out of 3430 reachable methods.
  The error rate describes the sample only, with UNCLEAR
  excluded by the brief's formula; it is not a whole-graph
  error rate.
- Label notes in `verification.csv` are cut at 300
  characters with an explicit `…[truncated]` marker (215
  rows); the full UNREACHABLE reason texts live in the built
  trigger JSON, not in the CSV.
- The writer mechanically cross-checks method + verdict
  against the route table, not `ref`/`note`; the judgments
  file was generated mechanically from the table to remove
  the transcription step (see `B7_RUN_LOG.md` section 9).
- The tree's committed `out/` is stale (8256 edges) and was
  not used here; the authoritative build at F1 time is the
  CI rebuild, against which these rows must still agree
  (same sources, same numbers — the private rebuild already
  reproduces them).
- Open follow-ups, not blockers for this log: the Ecdf1af97
  range correction in the Sync record (applying it would
  change a drawn-route edge id, so it needs its own design
  and audit); the @GROUP showFragment residual above.

## JSON shape (short)

```
{ "schema": 2, "title", "screens": {page: description}, "methods": [...], "verdict": {method: REACHABLE|UNREACHABLE},
  "labels": {method: {unreachable: {kind, text}, env: [{kinds, text}], state: [{kinds, text}], route_edge_classes, explicit_standard_route,
                      confirmed_by, source_ref, path_status}},
  "edges": [ {id, src, dst, kind, edge_class, via, trigger, gui[], guard, reads[], writes[], note, needs_state, state_kinds, env, env_kinds, evidence, class_basis} ],
  "paths": [ {method, edges[], edge_classes, explicit_standard_only, env, state, verified_by, ref} ], "verification": {...} }
```

`src`/`dst` are methods (`Class.method`, overloads as `Class.method(Type,Type)`) or pages (`S_...`). A suffix `@CONTEXT` is the same method or page in a specific context. Edge ids are a hash of the edge content, so they stay stable when other edges change.
