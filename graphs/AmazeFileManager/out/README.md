# AmazeFileManager 3.4.2: method-level trigger graph (schema 2)

How every method of **AmazeFileManager** is triggered, in the standard configuration: the instrumented debug build (`tingsu/AmazeFileManager@instrumented-version-3.2.1`, commit `5d25735ae846`, APK sha256 `9269b957...`), an API 27 emulator, permissions and fixtures as in `final_java_only`. Labels follow `handoff/SCHEMA_V2.md`: REACHABLE or UNREACHABLE, ENV and STATE gates, edge classes (explicit, standard, non-standard), and how each label was confirmed.

## What is in this folder

| File | What it is |
|---|---|
| `trace_trigger_graph.json` | pages, methods, `verdict`, `labels` (per-method fields), `edges` (with `edge_class`, `env_kinds`, `state_kinds`, stable ids), `paths` (verified paths only), `verification` (counts) |
| `methods.csv` | one row per method: verdict, UNREACHABLE reason, ENV and STATE kinds and texts, edge classes on the best route, whether an explicit/standard-only route exists, how the label was confirmed, path status, and the derived best route (`shortest_path`, `route_edge_ids`) |
| `../verification.csv` | the audit log: one row per label, edge or path that was checked, with result, how, and where (file:line) |
| `sanity_check.csv` | tool coverage (Monkey / APE, API 27) next to the labels; a one-way check only, it never sets a label |
| `trace_trigger_graph.html`, `build_report.txt` | the viewer and the validation report |

## Numbers

- **2981 methods**, **12 pages** (including pseudo pages), **8182 edges**. Verdicts: **2509 REACHABLE**, **472 UNREACHABLE**.
- UNREACHABLE by reason: closed_by_api_level 9, framework_never_calls 39, no_trigger_in_app 424.
- ENV gates (methods): other_app 8, system_event 7. STATE gates (methods): session 3. Methods with no gate: 2493.
- Edge classes: explicit 6936, non_standard 23, page 1, standard 1222. Non-standard edges: 23 (Glide generated code).
- 47 reachable methods have a non-standard edge on their best route; 45 have no explicit-or-standard-only route at all.
- Labels confirmed by: CALL 8, INFERRED 1726, SOURCE 1246, toString overrides are typically for debugging/logging and may be called reflectively 1 (SOURCE: every edge of the best route cites a source line, in the app or in the Android 8.1 / library source; INFERRED: some edge rests on inference or on another app).

## How much to trust it

No verification log yet: every label is `UNCHECKED` and nothing is claimed beyond what the evidence column says.

Edges whose evidence is not a source line (613 of 8182): E9c493cd5 (MainActivity.onResume -> MainActivity.onCreateOptionsMenu); E7a0b9a37 (MainActivity.onCreateOptionsMenu -> MainActivity.onOptionsItemSelected); E745b85ef (MainActivity$1.<init> -> MainActivity$1.doInBackground); Ed18978e9 (MainActivity$1.doInBackground -> MainActivity$1.onPostExecute); E1b6c2791 (TabFragment.onCreateView -> MainFragment.<init>); E3f533b40 (MainFragment.<init> -> MainFragment.onCreate); Ebd761bbf (MainFragment.onCreate -> MainFragment.onCreateView); E9adbdc5d (MainFragment.onCreateView -> MainFragment.onActivityCreated); E199e866f (RecyclerAdapter.<init> -> RecyclerAdapter.onCreateViewHolder); Ee1989850 (RecyclerAdapter.onCreateViewHolder -> RecyclerAdapter.onBindViewHolder); E6c3cfc3a (RecyclerAdapter.setItems(RecyclerView,ArrayList,boolean) -> RecyclerPreloadModelProvider.getPreloadRequestBuilder); Eacc36ed3 (Drawer.<init> -> Drawer.onNavigationItemSelected) ...

Sanity check against tool coverage (never used to set a label): 1132 methods ran in the 1-hour Monkey / APE runs on API 27; **21** of them are labelled UNREACHABLE.

## JSON shape (short)

```
{ "schema": 2, "title", "screens": {page: description}, "methods": [...], "verdict": {method: REACHABLE|UNREACHABLE},
  "labels": {method: {unreachable: {kind, text}, env: [{kinds, text}], state: [{kinds, text}], route_edge_classes, explicit_standard_route,
                      confirmed_by, source_ref, path_status}},
  "edges": [ {id, src, dst, kind, edge_class, via, trigger, gui[], guard, reads[], writes[], note, needs_state, state_kinds, env, env_kinds, evidence, class_basis} ],
  "paths": [ {method, edges[], edge_classes, explicit_standard_only, env, state, verified_by, ref} ], "verification": {...} }
```

`src`/`dst` are methods (`Class.method`, overloads as `Class.method(Type,Type)`) or pages (`S_...`). A suffix `@CONTEXT` is the same method or page in a specific context. Edge ids are a hash of the edge content, so they stay stable when other edges change.
