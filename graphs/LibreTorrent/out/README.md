# LibreTorrent 3.5.2 — source re-audit: method-level trigger graph (schema 2)

How every method of **LibreTorrent** is triggered, in the standard configuration: the instrumented debug build (`proninyaroslav/libretorrent@3.5.2`, commit `d93e92eacebc`, APK sha256 `5e05d2ff...`), an API 27 emulator, permissions and fixtures as in `final_java_only`. Labels follow `handoff/SCHEMA_V2.md`: REACHABLE or UNREACHABLE, ENV and STATE gates, edge classes (explicit, standard, non-standard), and how each label was confirmed.

## What is in this folder

| File | What it is |
|---|---|
| `libretorrent_trigger_graph.json` | pages, methods, `verdict`, `labels` (per-method fields), `edges` (with `edge_class`, `env_kinds`, `state_kinds`, stable ids), `paths` (verified paths only), `verification` (counts) |
| `methods.csv` | one row per method: verdict, UNREACHABLE reason, ENV and STATE kinds and texts, edge classes on the best route, whether an explicit/standard-only route exists, how the label was confirmed, path status, and the derived best route (`shortest_path`, `route_edge_ids`) |
| `../verification.csv` | the audit log: one row per label, edge or path that was checked, with result, how, and where (file:line) |
| `sanity_check.csv` | tool coverage (Monkey / APE, API 27) next to the labels; a one-way check only, it never sets a label |
| `libretorrent_trigger_graph.html`, `build_report.txt` | the viewer and the validation report |

## Numbers

- **4732 methods**, **1 pages** (including pseudo pages), **6329 edges**. Verdicts: **1986 REACHABLE**, **2746 UNREACHABLE**.
- UNREACHABLE by reason: no_trigger_in_app 480, unclassified 2266.
- ENV gates (methods): other_app 1958, system_event 13. STATE gates (methods): data 11, session 61. Methods with no gate: 15.
- Edge classes: explicit 5303, non_standard 531, standard 495. Non-standard edges: 531 (Android PopupMenu listener; AndroidX Activity Result API; AndroidX ActivityResult API; AndroidX ActivityResultRegistry; AndroidX AlertDialog; AndroidX AppCompat ActionMode; AndroidX AppCompat Toolbar; AndroidX AppCompat action bar; AndroidX DialogFragment lifecycle; AndroidX EditTextPreference; Andr).
- 1639 reachable methods have a non-standard edge on their best route; 1627 have no explicit-or-standard-only route at all.
- Labels confirmed by: INFERRED 4140, SOURCE 592 (SOURCE: every edge of the best route cites a source line, in the app or in the Android 8.1 / library source; INFERRED: some edge rests on inference or on another app).

## How much to trust it

No verification log yet: every label is `UNCHECKED` and nothing is claimed beyond what the evidence column says.

Edges whose evidence is not a source line (534 of 6329): E6f0891c5 (S_ENTRY -> MainApplication.<clinit>); E50191c30 (S_ENTRY -> MainActivity.<clinit>); E0f555379 (S_ENTRY -> AddTorrentActivity.<clinit>); E6c221f79 (S_ENTRY -> SettingsActivity.<clinit>); E70444373 (MainActivity.initDrawer -> DrawerExpandableAdapter.onBindChildViewHolder); E79785310 (MainActivity.initDrawer -> MainActivity.lambda$initDrawer$0); Eea644f43 (MainActivity.initDrawer -> MainActivity.lambda$initDrawer$0); Ecebe3a05 (MainActivity.initDrawer -> MainActivity.lambda$initDrawer$1); Ed0bb2c8b (MainActivity.initDrawer -> MainActivity.lambda$initDrawer$1); Ec7ef9327 (MainActivity$3.onTagMenuClicked -> MainActivity$3.lambda$onTagMenuClicked$0); E83e4ed2d (MainActivity$3.onTagMenuClicked -> MainActivity$3.lambda$onTagMenuClicked$0); E34551cd4 (MainActivity$3.onTagMenuClicked -> MainActivity$3.lambda$onTagMenuClicked$1) ...

Sanity check against tool coverage (never used to set a label): 2080 methods ran in the 1-hour Monkey / APE runs on API 27; **931** of them are labelled UNREACHABLE.

## JSON shape (short)

```
{ "schema": 2, "title", "screens": {page: description}, "methods": [...], "verdict": {method: REACHABLE|UNREACHABLE},
  "labels": {method: {unreachable: {kind, text}, env: [{kinds, text}], state: [{kinds, text}], route_edge_classes, explicit_standard_route,
                      confirmed_by, source_ref, path_status}},
  "edges": [ {id, src, dst, kind, edge_class, via, trigger, gui[], guard, reads[], writes[], note, needs_state, state_kinds, env, env_kinds, evidence, class_basis} ],
  "paths": [ {method, edges[], edge_classes, explicit_standard_only, env, state, verified_by, ref} ], "verification": {...} }
```

`src`/`dst` are methods (`Class.method`, overloads as `Class.method(Type,Type)`) or pages (`S_...`). A suffix `@CONTEXT` is the same method or page in a specific context. Edge ids are a hash of the edge content, so they stay stable when other edges change.
