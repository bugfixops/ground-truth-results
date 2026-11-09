# Handoff: Android trigger-graph task

State as of 2026-10-24, after one Claude Code session.

## Context
- Darshan (student) is helping Yang (collaborator) build a ground truth for 13 Java Android apps. Baseline: APE and Monkey, 1-hour runs on API 27.
- The **ground truth** says, for each app, which methods a user can reach through the GUI, and how.
- **Task (confirmed with Darshan):** for each of the **13 Java-only apps**, produce the same output Yang made for Currency in `share.zip`: a trigger graph JSON, `methods.csv`, a README, and optionally the HTML viewer. **The data (JSON + CSV) matters most; the HTML page is optional.**
- Apps: Aegis, AmazeFileManager, AnkiDroid, AnyMemo, Currency, Diary, hash-checker, LibreTorrent, Markor, MMEX, Omni-Notes, openlauncher, Vanilla-Music. Vinyl-Music-Player (4 .kt files) is excluded.

## Inputs (in `/Users/darshan/Desktop/yang/`)
- `GRAPH_PROMPT.md`: the recipe for a source-only graph, plus the JSON schema. `GENERIC_PROMPT.md`: the full version, which adds framework-source checks and emulator verification. Yang wrote both.
- `share.zip`: Yang's Currency **v1.33** example. Unzipped in `work/share_example/`.
- `final_java_only.zip`: the 13 apps (instrumented APK, source, class files, APE + Monkey JaCoCo reports). Unzipped in `work/final_java_only/`.

## Workspace: `/Users/darshan/Desktop/yang/work/`
```
final_java_only/<App>/app/...     dataset (source, classes, APK, class_files.json)
final_java_only/<App>/{ape,monkey}/report/report.xml   1-hour baseline JaCoCo reports (API 27, seed 20261016)
share_example/                    Yang's v1.33 example
tools/list_methods.py             method universe from .class files (no JDK on this Mac, so no javap)
tools/coverage_methods.py         per-method Monkey/APE hit flags from the JaCoCo XML
tools/build_graph.py              runs graph_def.py, validates, BFS shortest paths, baseline cross-check, writes out/
tools/viewer_template.html        Yang's viewer with /*DATA*/ placeholder
graphs/Currency/                  finished app 1 of 13
  method_list.json, coverage_baseline.json, graph_def.py (hand-written edges)
  out/ currency_trigger_graph.json, methods.csv, currency_trigger_graph.html, build_report.txt, README.md
handoff/                          this file + conversation.md
```

## Per-app recipe (how Currency was done)
1. `python3 -I tools/list_methods.py <classes_dir> --exclude JacocoInstrument --exclude '/R$' --exclude BuildConfig --json graphs/<App>/method_list.json` (the classes dir is in `final_java_only/<App>/app/class_files.json`).
2. `python3 -I tools/coverage_methods.py final_java_only/<App> --json graphs/<App>/coverage_baseline.json`
3. **Manual (an agent reads the code):** manifest, layouts, menus, preference XML, every Java file. Define pages as (window, mode). Write `graphs/<App>/graph_def.py` with `e(src, dst, kind, trigger, gui=[...], guard=..., reads=[...], writes=[...], note=..., needs_state=..., evidence='SRC File.java:line' | 'FW-MEMORY ...' | 'INFERRED ...' | 'DYN ...', env=...)`, plus `SCREENS`, `DEAD`, `FRAMEWORK_ONLY`, `NOTES`, `TITLE`. Use `graphs/Currency/graph_def.py` as the template.
4. `python3 -I tools/build_graph.py graphs/<App> <prefix>`: it must report 0 errors. Check the baseline cross-check: a DEAD/FRAMEWORK_ONLY method that ran in APE/Monkey means the graph is wrong.
5. Read ~30 shortest paths in `out/methods.csv`. Fix shortcuts (a path that skips a needed user action or crosses contexts) with `@CONTEXT` variants, `needs_state`, or `env`. Rebuild.
6. Write `out/README.md` (copy the structure of `graphs/Currency/out/README.md`).

## Conventions
- Edge kinds and schema: as in `GRAPH_PROMPT.md` section 5. GUI edges go page -> method, ENTERS edges go method -> page, a dialog opened directly from a page is an ENTERS page -> page edge (same as Yang's example).
- Overloads are named `Class.method(Type,Type)`; arrays are `Object[]`.
- `methods.csv` has Yang's columns plus `jvm_descriptor`, `monkey_hit`, `ape_hit`. A blank hit flag means JaCoCo filtered the method (trivial private constructors).
- The `env` field marks edges that need network, a successful download, or the network off. The CSV note then says "needs environment: ...".

## Status
- **Currency v1.58 done**: 145 methods, 22 pages, 391 edges; 140 reachable, 2 dead, 3 framework-only; 0 contradictions with the baseline; **not checked on a device**. 74 edges are FW-MEMORY (framework behaviour from memory), the least certain.
- Compared with Yang's v1.33 graph: identical verdicts on all 106 shared methods, and the same dead and framework-only methods. Found a small bug in Yang's `share/methods.csv`: 4 rows drop the final tap when the path ends at an `onOptionsItemSelected`. The graph itself is fine.
- One lesson: the baseline coverage refuted a framework-from-memory claim (the app's implicit widget broadcast **was** delivered on API 27). Always run the cross-check.

## Open questions for Yang (not answered yet)
1. Should each app also be verified on an emulator, like his 77 Currency scenarios? This Mac (M1, 8 GB RAM, 20 GB free) has **no JDK, Android SDK or emulator**. The baseline runs were done on another machine (`/Users/poyu/...`, `emulator-5560`).
2. Baseline: an earlier description says Monkey, but `tool_run_set_38.csv` says APE.
3. `fixtures/Documents` is missing (Markor and AmazeFileManager need it).
4. Aegis/MMEX setup: baseline coverage is only 4–21%, so the setup was probably not done.
5. An earlier description still says 41 apps.

## Next steps
- Get Yang's feedback on the Currency output before scaling up.
- Recommended: write a script that extracts direct call edges (and manifest, menu and listener registrations) from bytecode or source automatically. About a third of the edges are mechanical, and the big apps (LibreTorrent, MMEX, AnkiDroid have ~4,000+ methods each) are not feasible by hand without it.
- Then the apps, smallest first: Diary (287 methods), hash-checker (525), openlauncher (901), Omni-Notes, Vanilla-Music, AnyMemo, Markor, AmazeFileManager, Aegis, AnkiDroid, MMEX, LibreTorrent.

## Working style
Darshan is new to this research area. Explain each step in plain terms as the work happens: what it is, why, what was found.

---

## Update (hash-checker done; Kiro stopped)

**Status of the 13 apps:** Currency (`graphs/Currency/out`), Diary (`graphs/Diary/out`, built by Kiro with the older tools), hash-checker (`graphs/hash-checker/out`) are done. The other 10 are not started. Kiro was stopped to save credits; its 11 UI maps in `work/.agents/tasks/ui-map-<App>.md` are optional background reading (screens, setup gates, why APE/Monkey missed code, dead-code suspects) and are worth skimming before each app.

**Tools (work/tools/), newer than the recipe above:**
- `list_methods.py <classes_dir> --jacoco <report.xml> --exclude ... --json method_list.json` aligns the universe with JaCoCo (drops Dagger/enum/synthetic methods; keeps private empty constructors that JaCoCo hides).
- `extract_calls.py <graph_dir> <classes_dir>` reads the bytecode and writes `auto_calls.json`: direct app-to-app call edges (exact + class-hierarchy), lambda creations as REGISTER, calls collapsed through generated code, receiver-class variants for inherited "template methods" (`BaseFragment.onResume@HistoryFragment`) and an `impl` table.
- `build_graph.py <graph_dir> <prefix>`: `graph_def.py` may set `USE_AUTO = True` (adds the bytecode edges for every caller/callee pair not written by hand), `SUPPRESS` (pairs, or a node name to drop all its auto edges), and may call `impl(Class, method)` and read `AUTO`. It prints, per method, the path with the fewest environment gates.
- Template for the newer style: `graphs/hash-checker/graph_def.py` (loops for repeated patterns; hand edges only for entry, lifecycle, gestures, framework callbacks, conditions).

**Rules learned (each caused a real shortcut):**
1. A shared node must not carry context-dependent continuations. If a method behaves differently per caller or state, write context variants (`@TEXT`, `@NONE`) and wire each by hand; a hand edge for a caller/callee pair makes the script skip the auto edge for that pair.
2. Never chain lifecycle callbacks through a shared base-class node (`BaseFragment.onCreate`); make them siblings of `onAttach`.
3. A return edge ("Back", "dialog closed") may only go to the least-state page (e.g. the empty calculator) or to the exact page you came from; never to every mode.
4. Calls inside `catch` blocks, and calls that need data or a prior action, need `env` or `needs_state`; otherwise the auto edge makes them look free.
5. Read at least 30 shortest paths per app (60 for large ones). The validator cannot see shortcuts.

**Open questions for Yang** are unchanged (emulator verification, Monkey vs APE baseline, `fixtures/Documents`, Aegis/MMEX setup, 41 vs 13 apps), plus new baseline findings: the launch dump `00000.ec` is excluded from `merged.ec` (first-launch code looks "missed by Monkey"), and each run has one unreadable dump.

---

## Update (openlauncher done)

**Status:** Currency, Diary (Kiro, older tools), hash-checker, **openlauncher** (`graphs/openlauncher/out`: 900 methods, 43 pages, 1,606 edges; 592 reachable / 135 after setup / 162 dead / 11 framework-only; 0 contradictions with the baseline; not device-verified) are done. Next: Omni-Notes, Vanilla-Music, AnyMemo, Markor, AmazeFileManager, Aegis, AnkiDroid, MMEX, LibreTorrent.

**Tool change:** `build_graph.py` path choice is now fewest env gates, then fewest `needs_state` edges, then fewest steps (backup `build_graph_v3_backup.py`). Currency, hash-checker and Diary were rebuilt: verdicts unchanged, only some path texts changed.
`graph_def.py` also sees `METHODS` (the method universe) and `AUTO['calls']` (entries with src, dst, file, line): use them for loops such as "move the auto edges of node N into per-type variants" (see the end of `graphs/openlauncher/graph_def.py`).

**More rules learned (openlauncher):**
6. A default-on setting is a `guard`, not `needs_state` (a minibar that is on by default was making a whole subtree "after setup").
7. A factory with a type switch (`ItemViewFactory.getItemView`) needs one variant per type, reached from the matching caller; suppress its auto edges and re-add them per type with `AUTO['calls']`.
8. Callbacks reached through an interface held by several containers (`callBack.setLastItem`: desktop or dock) need one edge per container with its own state.
9. Methods only reachable from dead code are dead: `SUPPRESS |= set(DEAD)`. A permission that is commented out of the manifest makes its whole feature dead, not "env".
10. Framework callbacks recalled from memory (`getItemPosition`, `getPageTitle`, adapter `getItem`) must name their real trigger (`notifyDataSetChanged` caller, a tab strip in a layout); otherwise mark `FRAMEWORK_ONLY`.
11. After building, list (a) methods the baseline ran that the graph gates behind setup or env, and (b) reachable methods the baseline never ran, and read their paths. Both lists exposed shortcuts the validator could not.

---

## Update (Omni-Notes done)

**Status:** Currency, Diary (Kiro), hash-checker, openlauncher, **Omni-Notes** (`graphs/Omni-Notes/out`: 1,456 methods, 68 pages, 3,780 edges; 731 reachable / 474 after setup / 205 dead / 46 framework-only; 0 contradictions with the baseline; not device-verified) are done. Remaining: Vanilla-Music (1,478 JaCoCo methods), AnyMemo (2,202), Markor (2,865), Aegis (2,967), AmazeFileManager (2,992), AnkiDroid (4,188), MMEX (4,279), LibreTorrent (4,738). They are 1x to 3x the size of Omni-Notes: expect several hundred thousand tokens each.

**Tool facts that matter (build_graph.py):**
- A variant node `X@CTX` **inherits every auto (bytecode) edge of the base `X`** unless that (src, dst) pair is suppressed or covered by a hand edge from any variant of X. To wire a variant exactly, `SUPPRESS` the base node (whole source) and re-add its calls with `clone_auto(src, variant, exclude=..., only=...)` (helper at the top of `graphs/Omni-Notes/graph_def.py`) or by hand.
- `PREFER_SETUP_OVER_ENV = True` in graph_def.py: a method reachable by in-app setup alone is `REACHABLE_AFTER_SETUP` even if another route reaches it without setup through an env gate. Default False (the earlier four apps keep the old rule; backup `tools/build_graph_v4_backup.py`).
- Path choice order: fewest env gates, then fewest needs_state edges, then fewest steps.

**More rules learned (Omni-Notes):**
12. A callback implemented by lambdas (password validator, permission callback, result listener) must be wired per caller: one dialog page per caller and per-caller variants of the shared button lambdas, otherwise every dialog reaches every caller's continuation.
13. EventBus: write poster -> handler edges (FRAMEWORK) with the register/unregister window as `needs_state`; ENTERS the page at the GUI trigger, not at the shared handler.
14. AsyncTask chains: `execute` edge from the caller, `doInBackground -> onPostExecute` ASYNC; template-method task classes (`NoteProcessor`) need one chain per subclass.
15. The baseline refutes environment gates: if APE or Monkey ran code behind an "env" edge (location fix, recorder, camera start), remove the env flag. Pre-granted permissions are `needs_state` ("granted on the baseline emulators"), not env.
16. `ButterKnife` view bindings: `X_ViewBinding.<init>(X,View)` is called by `ButterKnife.bind`; the one-argument activity constructor and every `unbind()` are FRAMEWORK_ONLY.
17. Read the "clean-reachable but never run" list (here 23 methods): these are the reachable methods the baseline runs missed, and every entry must have an honest path.

---

## Overnight plan (generator method), written 2026-10-24 night

**Why:** hand-writing `graph_def.py` took ~2.5 h and ~450k tokens for Omni-Notes (1,456 methods). The 8 remaining apps have 1.5k-4.7k methods each, so they cannot be hand-written in one night. Method now: a generator derives the framework-driven edges from bytecode + manifest + res/ XML, and per-app work is limited to (1) baseline contradictions, (2) a dead-code review, (3) gating clusters (needs_state / env) for the biggest "reachable but never run" groups, (4) README.

**Tools (all in work/tools/):**
- `prep_app.sh <App>`: builds `graphs/<App>/{method_list.json, coverage_baseline.json, auto_calls.json}` (list_methods with `--jacoco`, coverage_methods, extract_calls). Already run for all 8 remaining apps.
- `new_graph_def.sh <App> "<Title>"`: writes the stub `graph_def.py`: `CFG = {...}` + `gen_edges.apply(globals(), GDIR, '<App>', CFG)` + a "hand-written refinement" section below it (plain `e(...)`, `SUPPRESS`, `DEAD`, `NOTES`, exactly as in the hand-written apps).
- `gen_edges.py` (docstring lists the cfg keys): ENTRY (application, launcher, exported components with env gate), LIFECYCLE / pages (S_<Class> for activities and fragments, ENTERS, GUI edges for user callbacks of the page class, SYSTEM edges for onPause/onSaveInstanceState...), callbacks of every constructed class that has a framework ancestor (edge from `<init>` to each callback that nobody in the app calls, or that is on the known-callback lists), lambdas (creator method -> body, gui text from the source line), class literals / custom intent actions / class-name strings (`startActivity(new Intent(ctx, X.class))` -> `X.<init>` INTENT), classes named in layout / xml / menu / navigation files (edge from the method that mentions `R.layout.NAME`; includes followed; view-binding callers), `onActivityResult` / `onRequestPermissionsResult` (RESULT from the start / request call sites), ButterKnife binders, EventBus 2 and 3 subscribers (post sites), `Handler.handleMessage` (from every send site), static initialisers, template-method receiver variants (`Base.m@Sub` reached from every caller of `Base.m` when Sub is constructed), `case R.id.X:` labels on menu / click handler call edges. Adapter row callbacks and row-based listeners (`onItemClick`, CAB) get `needs_state` = "the list shows at least one row".
- `build_graph.py`: new `AUTO_DEAD = '<note>'` in graph_def: methods with no route become DEAD with that note (instead of an UNRESOLVED error), pages nothing reaches are dropped. Predefined names in graph_def: `GDIR`, `TOOLS`.
- `build_all.sh App:prefix ...` builds several apps and prints a summary; `compare_graphs.py hand.json gen.json` prints a verdict confusion table; `check_gen.sh` rebuilds `graphs/_t_openlauncher` and `graphs/_t_Omni-Notes` (the generator applied to the two hand-written apps) and prints the agreement: dead-vs-alive about 93%, exact about 63-77% (the gap is `needs_state` gating that only a human reads out of the code). Run it after every change to gen_edges.py (it must keep 0 contradictions).

**Per-app workflow (generated apps):**
1. `tools/build_all.sh <App>:<prefix>`. Contradictions (baseline ran it, graph says DEAD) are generator gaps: read the source of the first few, add a general rule to gen_edges.py if the pattern is general, else a hand edge in the app's graph_def.py. Re-run `tools/check_gen.sh`.
2. List the DEAD methods by class (`out/methods.csv`), spot-check classes that look alive (reflection, XML, JNI, data binding, generated code), fix or leave.
3. List the reachable-but-never-run methods by class; for the big clusters read just enough source to set a gate in `CFG['GROUPS']` (`(regex on node, 'needs'|'env'|'guard', text)`; applied to every edge that enters the group from outside), or add DEAD entries with the reason (permission commented out of the manifest, feature disabled in this build, release-only).
4. Read ~30 shortest paths for sanity, write `out/README.md` (say "generated by tools/gen_edges.py and reviewed", list what is modelled and what is not, recompute every number from the final out/ files), tick PROGRESS.md, add 3-6 lines to this file, update the memory file `trigger-graph-task.md`.

**Honest limits to state in every generated README:** state gates beyond adapter rows (data, settings, earlier actions) are only modelled where a human added them, so `REACHABLE` means "no modelled setup", not "no setup"; callbacks are reachable as soon as an instance is constructed; reflection / JNI / generated-code entries are not modelled; `Handler.handleMessage` and event handlers are linked from every send / post site.

---

## Update (all 13 apps done, 2026-10-25 ~01:00)

**Status:** every app in PROGRESS.md is ticked; numbers and findings are in `FINAL_SUMMARY.md` and `graphs/SUMMARY.md` (both written by `tools/write_summaries.py` from the final files). The resume watcher was stopped (`STOP_AUTO_RESUME`), the in-session cron deleted.

**Tools added or changed tonight (all in work/tools/, the five hand-written graphs were rebuilt with them and came out identical):**
- `gen_edges.py` (generator, see "Overnight plan"), `gen_readme.py <App> <prefix>` (README with recomputed numbers, frontier summary, `graphs/<App>/review_notes.md` appended), `write_summaries.py`, `summary_table.py`.
- `build_graph.py`: `AUTO_DEAD`, unique node names (classes that share a simple name get a package prefix: LibreTorrent's two `TagsAdapter`), coverage keyed by class + name + descriptor, a report section "env-gated but hit", and (when coverage exists) five `frontier_*` columns in methods.csv (multi-source BFS from the methods the baseline ran: the edge where the chain first enters never-run code).
- `extract_calls.py`: also records ldc class / string constants, `new` / static class references, lambda interface + SAM name, method annotations, line ranges; implicit `<clinit>` calls (first use of a class); framework calls that are inherited methods called on app-typed receivers (`this.startActivityForResult`) now appear in `framework_calls`.
- Analysis helpers: `sample_paths.py`, `hubs.py` (nodes on the most shortest paths = shortcut candidates), `dead_by_class.py`, `unhit_by_class.py`, `keyword_clusters.py` (classes that look network / account / hardware / file / system dependent), `contra.py`, `compare_graphs.py`, `check_gen.sh`, `build_all.sh`, `prep_app.sh`, `new_graph_def.sh`.

**More rules learned (generator work):**
18. ENTERS edges must start at a node declared in the page's own class; an inherited lifecycle node (`MmxBaseFragmentActivity.onStart`) is shared by sibling screens and creates cross-screen shortcuts.
19. A class literal of a manifest component is a start only if the method (or a direct caller) calls a starter API; for receivers only `sendBroadcast` / `PendingIntent.getBroadcast` / alarms count (`ComponentName` is also used to query or enable a receiver). A class literal of an abstract class instantiates only generated-looking subclasses (`*_Impl`, `Generated*`, `Dagger*`), never every subclass (Dagger's `BaseActivity.class` check would otherwise "construct" every activity).
20. Components the system creates (services, receivers, providers, application, backup agent) get callbacks from a pseudo page `S_SYS_<Class>`, not from `<init>`, because app code may also `new` them (widget `checkEnabled`). A class whose default constructor JaCoCo hides gets a pseudo page `S_NEW_<Class>`.
21. Configured gates (`CFG['GROUPS']`) apply to every edge into a method the baseline never ran, not to methods it ran; env gates on non-ENTRY edges disappear when the baseline ran the target, ENTRY edges keep theirs (path choice then prefers an in-app route).
22. `onActivityResult` / `onRequestPermissionsResult`, EventBus subscribers and `Handler.handleMessage` are reached only from their request / post / send sites; the fallback (every site) is marked INFERRED.
23. Do not attribute the nested intent-filters of `<application>` to the application or backup-agent component (it made the backup agent a launcher).
24. `DATASET.txt` has `source_commit` and its value on two lines: allow whitespace before the colon.
25. zsh does not word-split `set -- $var`: loop in a bash script (`#!/bin/bash`).
26. Implicit `VIEW` / `SEND` intents are linked to the app's own exported activity only if the method creates an intent (`Intent.<init>` ...) and the app starts that activity nowhere explicitly.

**If more time is spent:** hand-curate state gates of the biggest never-run clusters (each generated README lists the ten frontier nodes that unlock the most), re-run `tools/check_gen.sh`, rebuild Diary with the current tools (its `method_list.json` / `auto_calls.json` are not in `graphs/Diary/`).

**Frontier curation round (2026-10-25, after the first pass):** `tools/show_frontier.py <App> [N] [ctx]` prints the source around the N frontier edges that unlock the most never-run methods (where the baseline stopped). Reading those lines gave precise gates, added as `CFG['EDGES']` (`(src regex, dst regex, 'needs'|'env'|'guard', text)`, branch-specific, applied to bytecode and generated edges): MMEX `MainActivity.onCreate` returns early when `showPrerequisite()` is true (tutorial not done / no valid database); Aegis `handleIncomingIntent` branches (incoming intent: env), `ImportEntriesActivity` import-from-app needs a root shell (env), `TransferEntriesActivity` needs an entry, `startAuthActivity` needs a locked vault; AnyMemo `handleOpenIntent` needs a VIEW intent, picker results (env), TTS completion (env); Amaze tile-preference intent / SMB row / archive launch intent (env); AnkiDroid advanced-statistics setting and type-in answer diff (needs); LibreTorrent torrent-dependent branches (needs) and the save-location picker (env). The same reading showed two wrong statements in my first review notes (AnyMemo's baseline did open decks; Aegis's vault list was empty), both corrected: **check a claim against the frontier / hit counts before writing it into a README.** Every build still has 0 contradictions and `tools/check_gen.sh` is unchanged.

**Later tweaks (same night):** `family_reach` (the code that runs on behalf of an activity / fragment, used to find the request sites of `onActivityResult` / `onRequestPermissionsResult`) now follows lambda links and constructed objects' own methods, which cut the "every request site assumed" fallback from 36 / 7 / 4 / 27 / 106 edges to 18 / 0 / 0 / 0 / 26 (AnyMemo, Markor, Amaze, AnkiDroid, MMEX). More `CFG['EDGES']` gates were added from frontier ranks 11-30 (Aegis: picker results, backup setting, entry-dependent calls; AnkiDroid: whiteboard, sound, review queue, TTS and fullscreen settings, API <= 10 and release-only branches, DeckTask task-type guard; LibreTorrent: torrent-dependent calls, IP filter, magnet fetch, auto-download feeds, crash screen; Amaze: root, apk, cloud, storage permission; Markor: PROCESS_TEXT intent, AsciiDoc; MMEX: the rest of `onCreate` after `showPrerequisite()`, the permission callback).

**Emulator test plan (2026-10-25):** `handoff/EMULATOR_TEST_PLAN.md` (redroid on EC2, all 13 apps at once, five questions, phases, per-app base state). `tools/make_test_manifest.py` writes `emulator_tests/<App>/targets.csv` (1,057 targets with expected outcome) and `emulator_tests/SUMMARY.md`. Correction made while preparing it: the fixtures hold more than my first review notes said (`table.csv`, `todo.txt`, `tasks.org`, `notes.md`, `sample_deck.apkg`, `sample.pdf` ... in Download); the Markor / AnkiDroid / AnyMemo notes, two gate texts and the summaries were corrected, verdicts did not change.
