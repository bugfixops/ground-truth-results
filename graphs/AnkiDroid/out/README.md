# AnkiDroid 2.6beta6: page-jump and method-call graph (generated)

A map of how every method of the open-source Android app **AnkiDroid** (tingsu/Anki-Android@instrumented-version-2.6beta6, source commit `58725f6d`, package `com.ichi2.anki`, APK sha256 `e21f15cb…0690e91a`) can be triggered: from which page, by which user gesture or system event, through which framework callback or call. It is the build in `final_java_only/AnkiDroid`.

**How this one differs from Currency, hash-checker, openlauncher and Omni-Notes:** those graphs were written by hand from reading the source. This one was **generated** by `tools/gen_edges.py` from the bytecode, `AndroidManifest.xml` and `res/` XML, and then checked against the baseline coverage and reviewed (see "How much to trust it"). Every number below is recomputed from the files in this folder.

## What is in this folder

| File | What it is |
|---|---|
| `ankidroid_trigger_graph.json` | The graph: pages, methods, verdicts, edges. Every edge has an `evidence` label; an edge may carry `env` (needs something outside the app) and `needs_state` (needs an earlier action or setting). |
| `methods.csv` | One row per method: verdict, steps from launch, the user taps on the best path, the path, number of incoming edges, note. Extra columns: `jvm_descriptor`, `monkey_hit`, `ape_hit` (1-hour API 27 baseline runs; empty = JaCoCo does not report the method), and for methods the baseline never ran `frontier_from`, `frontier_first_unrun`, `frontier_edge_kind`, `frontier_edge_evidence`, `steps_after_frontier` (where the chain from code that ran first enters code that never ran). |
| `ankidroid_trigger_graph.html` | The same data in the viewer from the Currency example. Optional. |
| `build_report.txt` | Output of the validation script (0 errors, 0 warnings, baseline cross-check, the list of reachable methods the baseline never ran). |

## Numbers

- **4186 methods** (the app's own code, aligned with what JaCoCo reports), **78 pages** (10 of them `S_NEW_<Class>` anchors: a class whose empty default constructor is not in the JaCoCo method universe is constructed through such a node), **11395 edges**: 7379 from the bytecode call extractor, 4016 added by the generator or by hand.
- Edge kinds: ASYNC 76, CALL 8248, ENTERS 61, ENTRY 6, FRAMEWORK 568, GUI 48, INTENT 48, LIFECYCLE 2234, RESULT 50, SYSTEM 56.
- Verdicts: **3376 reachable**, **280 reachable after setup**, **530 dead**, 0 framework-only.
- 421 edges are gated by an outside environment, 212 need an earlier action or setting; 338 methods are reached only through an environment gate, 280 only after setup. Average route length: 13.5 edges.
- Evidence labels: 3141 `FW-MEMORY`, 152 `INFERRED`, 8102 `SRC`.
- Largest dead groups (auto-classified, see limits): `AddContentApi` (30 of 30), `Base64` (29 of 29), `Collection` (23 of 105), `PlotSheet` (16 of 50), `Decks` (12 of 62), `Finder` (12 of 40), `FunctionDrawer` (12 of 16), `FunctionDrawer_y` (12 of 16), `XAxisHistoGram` (12 of 19), `YAxisHistoGram` (12 of 19), `DeckTask$TaskData` (11 of 33), `XAxisBarGraph` (11 of 17), `YAxisBarGraph` (11 of 17), `CustomExceptionHandler` (10 of 10).

## Comparison with the baseline coverage (APE and Monkey, 1 hour each, API 27)

- 2011 of the 4174 observable methods ran in at least one run (Monkey 224, APE 2003, both 216). **0 dead or framework-only methods ran**, so the coverage contradicts no verdict.
- **2163 methods were run by neither tool.** By the graph: 521 are dead; 338 are reachable only through an outside environment; 239 need an earlier in-app action or setting; **1065 are reachable with no modelled setup and no outside help, yet were never run** (the clearest target list for the paper). Classes holding most of them: `AbstractFlashcardViewer` (27), `DeckPicker` (26), `TopLevelParser` (21), `DeckTask` (19), `Sched` (18), `StatsMetaInfo` (17), `PlotSheet` (16), `ImageField` (15), `Whiteboard` (14), `NoteEditor` (12), `CompatV10` (12), `Decks` (12), `Media` (12), `Models` (12).
- **Where the baseline stopped (frontier).** For 1638 of the never-run reachable methods the graph gives the edge where the chain from methods that ran first enters code that never ran (`frontier_*` columns of `methods.csv`: `frontier_from` is the source of that edge, a method that ran or a screen entered from one; `frontier_first_unrun` is its target): 1237 CALL, 305 FRAMEWORK, 47 ASYNC, 26 LIFECYCLE, 14 RESULT, 7 GUI, 2 SYSTEM. A `CALL` frontier is a branch inside code that ran and was not taken (a data, setting or error condition); a `FRAMEWORK`, `GUI`, `INTENT` or `SYSTEM` frontier is a callback, tap or start that no tool triggered. The ten frontier nodes that unlock the most never-run methods:
  - `Connection.sync` (169 never-run methods behind it): reached from `DeckPicker.sync(String)` by a `CALL` edge (SRC DeckPicker.java:1284 (bytecode))
  - `AdvancedStatistics.runFilter` (104 never-run methods behind it): reached from `Hooks.runFilter` by a `CALL` edge (SRC Hooks.java:150 (bytecode))
  - `ReliefDrawer.paint` (87 never-run methods behind it): reached from `DrawableContainer.paint` by a `CALL` edge (SRC DrawableContainer.java:49 (bytecode))
  - `BasicTextFieldController$3.onClick` (50 never-run methods behind it): reached from `BasicTextFieldController$3.<init>` by a `FRAMEWORK` edge (FW-MEMORY the framework / library calls this callback on an instance created by the app)
  - `BasicTextFieldController$2.onClick` (49 never-run methods behind it): reached from `BasicTextFieldController$2.<init>` by a `FRAMEWORK` edge (FW-MEMORY the framework / library calls this callback on an instance created by the app)
  - `DeckTask.doInBackgroundImportAdd` (39 never-run methods behind it): reached from `DeckTask.doInBackground` by a `CALL` edge (SRC DeckTask.java:277 (bytecode))
  - `DeckTask.onCancelled` (30 never-run methods behind it): reached from `DeckTask.<init>` by a `ASYNC` edge (FW-MEMORY the framework / library calls this callback on an instance created by the app)
  - `DiffEngine.diffedHtmlStrings` (25 never-run methods behind it): reached from `AbstractFlashcardViewer.typeAnsAnswerFilter` by a `CALL` edge (SRC AbstractFlashcardViewer.java:769 (bytecode))
  - `TopLevelParser.f(double)` (25 never-run methods behind it): reached from `BarGraph.paint` by a `CALL` edge (SRC BarGraph.java:133 (bytecode))
  - `CardBrowserMySearchesDialog.newInstance` (23 never-run methods behind it): reached from `CardBrowser.onOptionsItemSelected` by a `CALL` edge (INFERRED SRC CardBrowser.java:652 (bytecode))
- Harness facts that matter for target selection: `merged.ec` omits the launch dump `00000.ec`, so first-launch code can show `monkey_hit = 0` although it ran; one dump per tool may be unreadable, and a process that dies between 30-second dumps loses its coverage, so "never hit" does not strictly prove "never ran".

## How much to trust it

- **Method.** `gen_edges.py` applies Android framework rules to the compiled classes: process entry (Application, launcher, exported components behind an `env` gate), lifecycle callbacks and one page `S_<Activity|Fragment>` per screen, UI and system callbacks of every constructed class with a framework ancestor, lambdas and method references (creator method -> body, the tap label is read from the source line), `startActivity(new Intent(ctx, X.class))` and custom intent actions, classes named in layout / xml / menu / navigation files and where they are inflated, activity and permission results, `Handler` messages, ButterKnife / EventBus / data binding / Dagger / Glide / Icepick / Parceler / ORMLite / Room glue, static initialisers, and template-method receiver variants (`Base.m@Sub`). Direct calls come from the bytecode (`extract_calls.py`, class-hierarchy analysis for virtual calls). Methods that nothing reaches are reported DEAD (`AUTO_DEAD`).
- **Calibration on the five hand-written apps** (the generator run on the same inputs, compared with the hand-written verdicts; `tools/calibrate.py`): dead-versus-alive agreement 97.2% (Currency), 96.5% (Diary), 98.5% (hash-checker), 92.9% (openlauncher), 93.8% (Omni-Notes); exact verdict agreement 93.8% (Currency), 95.5% (Diary), 71.1% (hash-checker), 76.9% (openlauncher), 63.1% (Omni-Notes). The gap is almost entirely `needs_state`: a human reads "needs a note / a folder / a setting" out of the code, the generator only knows list rows. (openlauncher and Omni-Notes were used while the generator rules were developed; Currency, Diary and hash-checker were not.)
- **Checks done on this app:** the validation script (0 errors, 0 warnings: every method has a route or a DEAD verdict, every page is reachable); the baseline cross-check above (0 contradictions after the generator rules were completed by reading the contradictions one by one); random shortest paths were read for shortcuts.
- **Not checked on a device.** Framework rules are `FW-MEMORY` (recalled, not checked against AOSP source); guesses are `INFERRED`.

## Limits (read before using a verdict)

- **`REACHABLE` means "no modelled setup", not "no setup".** Gates beyond list rows (data that must exist, settings, earlier actions, incoming intents, files on the device) are modelled only where listed in the review notes. Adapter row callbacks, row-based listeners and action modes carry `needs_state` = "the list shows at least one row".
- A callback is reachable as soon as an instance of its class is constructed; the real trigger (a tap on one specific control) is shown in the `gui_steps` column only where the source line names the control. Menu and click handlers that switch on `R.id.x` give one labelled edge per case (`case R.id.x`), found by the nearest preceding case label (`INFERRED`).
- `Handler.handleMessage`, EventBus subscribers and Dagger-provided objects are linked from every send / post / graph-build site (`INFERRED`), so their routes can be shorter than the real ones.
- DEAD is automatic: nothing in the bytecode, manifest, XML or the modelled libraries reaches the method. Entries through reflection, JNI, other generated code or libraries that are not modelled would be missed (the baseline contradiction check found and fixed every such case that the 1-hour runs exercised).
- Calls inside catch blocks, data-dependent branches and feature flags are ordinary calls unless the review notes say otherwise.

## Review notes for this app

What was reviewed by hand (class level, from method names, the manifest, the layouts and the fixtures on the baseline device):

- **Environment gates (edges into these classes, when the baseline never ran the target, carry `env`):** the AnkiWeb sync stack (`Syncer`, `HttpSyncer`, `FullSyncer`, `RemoteServer`, `RemoteMediaServer`, `MediaSyncer`, `Connection`, `EasySSLSocketFactory`, `HttpFetcher`, `MyAccount`: an AnkiWeb account and network); `TranslationActivity` and `LoadPronounciationActivity` (external translation / pronunciation web services); `CardContentProvider` (the API provider that other apps call; AnkiDroid does not query its own provider); the home-screen widget (`AnkiDroidWidget*`); `SdCardReceiver` (SD card broadcast).
- **Content gates (`needs_state`):** `Anki2Importer`, `AnkiPackageImporter`, `Importer` (a `.apkg` / `.anki2` / `.colpkg` file is selected in the import dialog: `sample_deck.apkg` is in the Download fixtures, so this is a tap path that the baseline did not take); `AdvancedStatistics` (Settings > Advanced statistics > Enable advanced statistics: a preference of the statistics screen; the frontier shows `Hooks.runFilter` as the entry); the diff of a typed answer (`AbstractFlashcardViewer.typeAnsAnswerFilter` -> `DiffEngine`: a card with a `{{type:Field}}` answer and a wrong answer typed). The sync stack is entered only when `DeckPicker.sync` finds a stored `hkey` (otherwise the not-logged-in dialog shows), i.e. an AnkiWeb login.
- **Two source sets.** The class files cover the `AnkiDroid` app module and the `api` module (see `class_files.json`).
- **Dead code** is mostly code of the `api` module and bundled libraries that the app never calls: `AddContentApi` (all 30 methods: the helper for other apps), the bundled `Base64` (all 29), `api.Utils`, the plotting library behind the statistics screens (`PlotSheet`, `FunctionDrawer*`, `XAxisHistoGram`, `YAxisBarGraph`, `YAxis`, ...: the unused parts), `CustomExceptionHandler` (all 10), and unused methods of `libanki.Collection`, `Decks`, `Finder`, `DeckTask$TaskData` constructors.
- **Reflection.** `Sched._cntFnNew` / `_cntFnRev` are called through `getDeclaredMethod("_cntFnNew")`; the generator links them from the method that holds the string.
- **Not gated but never run (the target list):** the statistics stack (`Statistics`, `AdvancedStatistics`, `StatsMetaInfo`, the plot classes), `Media` (media check), `DiffEngine`, `Whiteboard`, the `NoteEditor` field-remap / note-type helpers, the `AbstractFlashcardViewer` clipboard and gesture commands, the `DeckPicker` context-menu actions (`deleteContextMenuDeck`, `importAdd`, `emailFile`), the multimedia field controllers (`ImageField`, `AudioField`).
- **Large paths.** Almost every route starts `IntentHandler.onCreate` -> `DeckPicker.<init>` (the launcher activity is a trampoline); long chains through `DeckTask.launchDeckTask` / `doInBackground` are AsyncTask hops.

## JSON shape (short)

```
{ "title", "screens": {page: description}, "methods": [...], "verdict": {method: REACHABLE|REACHABLE_AFTER_SETUP|DEAD|FRAMEWORK_ONLY},
  "dead": {method: reason}, "framework_only": {method: reason},
  "edges": [ {id, src, dst, kind, trigger, gui[], guard, reads[], writes[], note, needs_state, evidence, env} ] }
```
`src`/`dst` are methods (`Class.method`, overloads as `Class.method(Type,Type)`, classes that share a simple name get a package prefix) or pages (`S_...`). A suffix `@CONTEXT` is the same method in a specific receiver class (`Base.m@Sub`) or context.
