# MMEX 2024.06.14: method-level trigger graph (schema 2)

How every method of **MMEX** is triggered, in the standard configuration: the instrumented debug build (`moneymanagerex/android-money-manager-ex@2024.06.14.1033`, commit `f6e8d005340b`, APK sha256 `5bedb170...`), an API 27 emulator, permissions and fixtures as in `final_java_only`. Labels follow `handoff/SCHEMA_V2.md`: REACHABLE or UNREACHABLE, ENV and STATE gates, edge classes (explicit, standard, non-standard), and how each label was confirmed.

## What is in this folder

| File | What it is |
|---|---|
| `build_004b_trigger_graph.json` | pages, methods, `verdict`, `labels` (per-method fields), `edges` (with `edge_class`, `env_kinds`, `state_kinds`, stable ids), `paths` (verified paths only), `verification` (counts) |
| `methods.csv` | one row per method: verdict, UNREACHABLE reason, ENV and STATE kinds and texts, edge classes on the best route, whether an explicit/standard-only route exists, how the label was confirmed, path status, and the derived best route (`shortest_path`, `route_edge_ids`) |
| `../verification.csv` | the audit log: one row per label, edge or path that was checked, with result, how, and where (file:line) |
| `sanity_check.csv` | tool coverage (Monkey / APE, API 27) next to the labels; a one-way check only, it never sets a label |
| `build_004b_trigger_graph.html`, `build_report.txt` | the viewer and the validation report |

## Numbers

- **4270 methods**, **4 pages** (including pseudo pages), **7610 edges**. Verdicts: **3430 REACHABLE**, **840 UNREACHABLE**.
- UNREACHABLE by reason: branch_never_taken 13, closed_by_api_level 9, framework_never_calls 77, no_trigger_in_app 741.
- ENV gates (methods): hardware 9, network 4, other 11, other_app 44, system_event 28, time 6. STATE gates (methods): account 341, data 42, session 5, settings 434. Methods with no gate: 2910.
- Edge classes: explicit 7554, page 3, standard 53. Non-standard edges: 0.
- 1500 reachable methods have a non-standard edge on their best route; 894 have no explicit-or-standard-only route at all.
- Labels confirmed by: INFERRED 4163, SOURCE 107 (SOURCE: every edge of the best route cites a source line, in the app or in the Android 8.1 / library source; INFERRED: some edge rests on inference or on another app).

## How much to trust it

No verification log yet: every label is `UNCHECKED` and nothing is claimed beyond what the evidence column says.

Edges whose evidence is not a source line (14 of 7610): E19395ce1 (S_ENTRY -> PayeeActivity.<clinit>); E76a7aa66 (SearchParametersFragment$1.onClick -> PayeeActivity.<clinit>); E6f579f87 (EditTransactionCommonFunctions$9.onClick -> PayeeActivity.<clinit>); E87a1872f (AboutActivity.onCreate -> AboutTabAdapter.getCount); Ee835bc9a (AboutActivity.onCreate -> AboutTabAdapter.getItem); Eb0b17b72 (S_ABOUT_ACTIVITY -> AboutTabAdapter.getItem); E388582e3 (AboutActivity.onCreate -> AboutTabAdapter.getPageTitle); E503e054a (AboutActivity.onCreate -> AboutActivity.onRestoreInstanceState); Ea0013de2 (AboutCreditsFragment.<init> -> AboutCreditsFragment.onCreateView); Eeff0a2bf (AboutCreditsFragment.onCreateView -> AboutCreditsFragment.onActivityCreated); Ecef22362 (AboutFragment.<init> -> AboutFragment.onCreateView); E9a349a2e (S_ABOUT_TAB -> AboutFragment$1.onClick) ...

Sanity check against tool coverage (never used to set a label): 271 methods ran in the 1-hour Monkey / APE runs on API 27; **0** of them are labelled UNREACHABLE.

## JSON shape (short)

```
{ "schema": 2, "title", "screens": {page: description}, "methods": [...], "verdict": {method: REACHABLE|UNREACHABLE},
  "labels": {method: {unreachable: {kind, text}, env: [{kinds, text}], state: [{kinds, text}], route_edge_classes, explicit_standard_route,
                      confirmed_by, source_ref, path_status}},
  "edges": [ {id, src, dst, kind, edge_class, via, trigger, gui[], guard, reads[], writes[], note, needs_state, state_kinds, env, env_kinds, evidence, class_basis} ],
  "paths": [ {method, edges[], edge_classes, explicit_standard_only, env, state, verified_by, ref} ], "verification": {...} }
```

`src`/`dst` are methods (`Class.method`, overloads as `Class.method(Type,Type)`) or pages (`S_...`). A suffix `@CONTEXT` is the same method or page in a specific context. Edge ids are a hash of the edge content, so they stay stable when other edges change.
