# Money Manager Ex 2024.06.14: page-jump and method-call graph (generated)

A map of how every method of the open-source Android app **MMEX** (moneymanagerex/android-money-manager-ex@2024.06.14.1033, source commit `f6e8d005`, package `com.money.manager.ex`, APK sha256 `5bedb170…d9f18aeb`) can be triggered: from which page, by which user gesture or system event, through which framework callback or call. It is the build in `final_java_only/MMEX`.

**How this one differs from Currency, hash-checker, openlauncher and Omni-Notes:** those graphs were written by hand from reading the source. This one was **generated** by `tools/gen_edges.py` from the bytecode, `AndroidManifest.xml` and `res/` XML, and then checked against the baseline coverage and reviewed (see "How much to trust it"). Every number below is recomputed from the files in this folder.

## What is in this folder

| File | What it is |
|---|---|
| `mmex_trigger_graph.json` | The graph: pages, methods, verdicts, edges. Every edge has an `evidence` label; an edge may carry `env` (needs something outside the app) and `needs_state` (needs an earlier action or setting). |
| `methods.csv` | One row per method: verdict, steps from launch, the user taps on the best path, the path, number of incoming edges, note. Extra columns: `jvm_descriptor`, `monkey_hit`, `ape_hit` (1-hour API 27 baseline runs; empty = JaCoCo does not report the method), and for methods the baseline never ran `frontier_from`, `frontier_first_unrun`, `frontier_edge_kind`, `frontier_edge_evidence`, `steps_after_frontier` (where the chain from code that ran first enters code that never ran). |
| `mmex_trigger_graph.html` | The same data in the viewer from the Currency example. Optional. |
| `build_report.txt` | Output of the validation script (0 errors, 0 warnings, baseline cross-check, the list of reachable methods the baseline never ran). |

## Numbers

- **4270 methods** (the app's own code, aligned with what JaCoCo reports), **104 pages** (7 of them `S_NEW_<Class>` anchors: a class whose empty default constructor is not in the JaCoCo method universe is constructed through such a node), **10886 edges**: 3484 from the bytecode call extractor, 7402 added by the generator or by hand.
- Edge kinds: ASYNC 99, CALL 7364, ENTERS 78, ENTRY 29, FRAMEWORK 1608, GUI 97, INTENT 113, LIFECYCLE 1253, RESULT 94, SYSTEM 151.
- Verdicts: **663 reachable**, **3067 reachable after setup**, **540 dead**, 0 framework-only.
- 579 edges are gated by an outside environment, 5009 need an earlier action or setting; 388 methods are reached only through an environment gate, 3067 only after setup. Average route length: 12.8 edges.
- Evidence labels: 3470 `FW-MEMORY`, 98 `INFERRED`, 7318 `SRC`.
- Largest dead groups (auto-classified, see limits): `CurrencyRecyclerListFragment` (17 of 26), `DashboardFragment` (16 of 16), `AccountSpinnerAdapter` (12 of 12), `Encryptor` (10 of 10), `CursorRecyclerViewAdapter` (10 of 10), `WebViewActivity` (9 of 9), `EditPriceDialog` (9 of 11), `MmxDate` (9 of 56), `InsecureSHA1PRNGKeyDerivator` (8 of 8), `SyncManager` (8 of 30), `ex.DataBinderMapperImpl` (7 of 7), `SearchViewFormatter` (7 of 13), `DividerItemDecoration` (7 of 7), `FilterDatePeriods` (5 of 5).

## Comparison with the baseline coverage (APE and Monkey, 1 hour each, API 27)

- 271 of the 4267 observable methods ran in at least one run (Monkey 261, APE 261, both 251). **0 dead or framework-only methods ran**, so the coverage contradicts no verdict.
- **3996 methods were run by neither tool.** By the graph: 538 are dead; 388 are reachable only through an outside environment; 2892 need an earlier in-app action or setting; **178 are reachable with no modelled setup and no outside help, yet were never run** (the clearest target list for the paper). Classes holding most of them: `MmxOpenHelper` (18), `MmxContentProvider` (14), `RepositoryBase` (13), `FileStorageHelper` (10), `DatabaseManager` (8), `QueryCategorySubCategory` (8), `MmxDatabaseUtils` (8), `AttachmentRepository` (5), `MmexApplication` (4), `CalculatorActivity$$Icepick` (4), `DaggerMmxComponent` (4), `WhereStatementGenerator` (4), `MmxBaseFragmentActivity` (3), `MoneyBundler` (3).
- **Where the baseline stopped (frontier).** For 3348 of the never-run reachable methods the graph gives the edge where the chain from methods that ran first enters code that never ran (`frontier_*` columns of `methods.csv`: `frontier_from` is the source of that edge, a method that ran or a screen entered from one; `frontier_first_unrun` is its target): 2707 CALL, 473 FRAMEWORK, 93 LIFECYCLE, 61 RESULT, 14 ASYNC. A `CALL` frontier is a branch inside code that ran and was not taken (a data, setting or error condition); a `FRAMEWORK`, `GUI`, `INTENT` or `SYSTEM` frontier is a callback, tap or start that no tool triggered. The ten frontier nodes that unlock the most never-run methods:
  - `MainActivity.initHomeFragment` (1650 never-run methods behind it): reached from `MainActivity.onCreate` by a `CALL` edge (SRC MainActivity.java:238 (bytecode))
  - `MainActivity.populateScheduledTransactions` (496 never-run methods behind it): reached from `MainActivity.onCreate` by a `CALL` edge (SRC MainActivity.java:244 (bytecode))
  - `MainActivity.initializeDrawer` (391 never-run methods behind it): reached from `MainActivity.onCreate` by a `CALL` edge (SRC MainActivity.java:240 (bytecode))
  - `MmxBaseFragmentActivity.onPermissionGranted` (291 never-run methods behind it): reached from `GeneralSettingsActivity.<init>` by a `FRAMEWORK` edge (FW-MEMORY the framework creates the component and calls its lifecycle callbacks)
  - `MainActivity.initializeSync` (79 never-run methods behind it): reached from `MainActivity.onCreate` by a `CALL` edge (SRC MainActivity.java:242 (bytecode))
  - `MainActivity.onResume` (60 never-run methods behind it): reached from `MainActivity.<init>` by a `LIFECYCLE` edge (FW-MEMORY the framework creates the component and calls its lifecycle callbacks)
  - `MainActivity.onActivityResult` (35 never-run methods behind it): reached from `FileStorageHelper.showCreateFilePicker` by a `RESULT` edge (FW-MEMORY the system delivers the result of startActivityForResult / requestPermissions to the caller)
  - `SyncPreferenceFragment.onActivityResult` (25 never-run methods behind it): reached from `FileStorageHelper.showCreateFilePicker` by a `RESULT` edge (FW-MEMORY the system delivers the result of startActivityForResult / requestPermissions to the caller)
  - `MainActivity.onStart` (23 never-run methods behind it): reached from `MainActivity.<init>` by a `LIFECYCLE` edge (FW-MEMORY the framework creates the component and calls its lifecycle callbacks)
  - `DbModule.provideOpenHelper` (21 never-run methods behind it): reached from `MmexApplication.onCreate` by a `FRAMEWORK` edge (FW-MEMORY Dagger / Hilt: the generated component and factories call @Provides methods and @Inject constructors when the graph is built)
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

What was reviewed by hand (class level, from method names, the manifest, the source of the suspicious dead classes and the baseline hit counts per package):

- **What the baseline reached.** Only 271 of 4,270 methods ran. The hits are the application and Dagger set-up (`MmexApplication`, `DaggerMmxComponent`, `MmxModule*`, `DbModule*`, `Core`), the tutorial (`TutorialActivity`, the five `Tutorial*Fragment` classes), `SelectDatabaseActivity`, `PasswordActivity`, `MmxFileUtils`, the general settings (`GeneralSettingsActivity`, `GeneralSettingsFragment`, `AppSettings`, `GeneralSettings`, `BehaviourSettings`) and a part of `MainActivity`. **No method of the packages `account`, `transactions`, `investment`, `reports`, `recurring`, `search`, `fragment`, `adapter`, `viewmodels`, `widget`, `about`, `notifications` or `passcode` ran, and `HomeFragment` was never created.** This is the open question about the MMEX baseline setup (coverage about 6%).
- **Assumption built into the verdicts.** Because the data screens never ran, the generator gates the methods of those packages (when the baseline never ran them) behind `needs_state`: `A money database is open ...` for `account`, `home`, `currency`, `search`, `fragment`, `adapter`, `viewmodels`, `servicelayer`, `domainmodel`, `about`, `notifications`, `passcode`, and `... holds at least one account` for `transactions`, `investment`, `recurring`, `reports`, `budget`. This is an inference from the hit counts, not something verified on a device: if the app creates a default database on its own, these methods are plainly reachable, and `REACHABLE_AFTER_SETUP` would then mean "never reached by the baseline for a reason this graph does not know". Methods the baseline did run keep their ungated route.
- **Environment gates:** the price / exchange-rate / sync stack (`Sync*`, `YahooCsvQuoteDownloaderRetrofit`, `YqlSecurityPriceUpdaterRetrofit`, `FixerService`, `MorningstarPriceUpdater*`, `NetworkUtils`, `StubSyncProvider`: network and external servers), the widgets (`AccountBillsWidget*`, `ButtonAddTransactionWidgetProvider`, `SummaryWidgetProvider`, `SingleAccountWidget*`) and `SmsReceiverTransactions`. `MmxContentProvider` operations carry `env` unless the app calls the same `ContentResolver` operation.
- **Libraries linked by rules:** Dagger 2 (`DaggerMmxComponent`, `*_Factory`, `*_MembersInjector`, `@Provides`, `@Inject`), EventBus 3 (`@Subscribe` methods are linked from every `EventBus.post` that creates or receives the event class), ButterKnife (`*_ViewBinding`), Icepick (`*$$Icepick`), Parceler (`*$$Parcelable`), Retrofit interfaces, and data binding (`DataBinderMapperImpl`).
- **Dead code** includes `DashboardFragment` (all 16 methods: nothing instantiates it), `AccountSpinnerAdapter` (only a commented-out use), `CurrencyRecyclerListFragment` (17 of 26: its host activity is never started), `Encryptor` and `InsecureSHA1PRNGKeyDerivator` (an unused legacy database-encryption helper), `CursorRecyclerViewAdapter`, `WebViewActivity`, `EditPriceDialog`, `DividerItemDecoration`, and the generated Dagger members injectors of those classes.
- **Not gated but never run (the target list):** database infrastructure (`MmxOpenHelper`, `RepositoryBase`, `DatabaseManager`, `MmxDatabaseUtils`, `FileStorageHelper`: they run when a database is created or opened) and a few startup branches (`MmexApplication.createDbInstance`, `MmxBaseFragmentActivity.onPermissionGranted`).

## JSON shape (short)

```
{ "title", "screens": {page: description}, "methods": [...], "verdict": {method: REACHABLE|REACHABLE_AFTER_SETUP|DEAD|FRAMEWORK_ONLY},
  "dead": {method: reason}, "framework_only": {method: reason},
  "edges": [ {id, src, dst, kind, trigger, gui[], guard, reads[], writes[], note, needs_state, evidence, env} ] }
```
`src`/`dst` are methods (`Class.method`, overloads as `Class.method(Type,Type)`, classes that share a simple name get a package prefix) or pages (`S_...`). A suffix `@CONTEXT` is the same method in a specific receiver class (`Base.m@Sub`) or context.
