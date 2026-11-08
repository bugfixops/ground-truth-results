# UNVERIFIED PROPOSAL — DO NOT RELY ON, MERGE, OR USE AS EVIDENCE YET

**Status: UNVERIFIED.** This is a coordinator first part from 2026-10-31, saved here so it is not lost. It has NOT passed a build, sampler, full-repo grep, or C1 checks on a full local checkout, and must be re-checked from printed source before any label, route, or graph change is relied on or merged.

**Branch rule:** work in progress is on work-2026-10-31 only, never main, and the 'result' branch is not used for work in progress unless the user says so.

---

# MMEX WP2 route-check — first proposed set (PENDING, NOT PUSHABLE)

- App: MMEX. Repo: bugfixops/ground-truth-results, source branch work-2026-10-31.
- Status: PENDING. Do NOT merge/push as verified. Nothing was edited, merged or pushed by this helper.
- Why pending: (1) tools/verify_sample.py was NOT run — no local clone on this VM, and the connector alone cannot run it or tools/build_graph.py on a full checkout, so there is NO sample_30 output and no WP2 sample error rate; (2) one part-146 edge is judged wrong (ScreenTree, debug config); (3) one INFERRED entry is judged unclear (getPageTitle, CircleIndicator step unprinted); (4) C1 checks were not run. The orchestrator must decide/merge the proposed fixes below and re-run the build + sampler before any push to branch `result`.
- Standard configuration used: debug build, fresh install, API 27, permissions only where a route needs them.
- Hard-rule compliance: no tool coverage, old generated graphs, or REACHABLE counts were used as evidence. confirmed_by values below are only SOURCE or INFERRED. Framework claims below cite only printed fw_src/android-8.1.0_r1/ lines, except where explicitly marked INFERRED (source not read).
- Correction to the task premise: graphs/MMEX/parts/label_137.md row 5 lists MmxDatabaseUtils.<clinit> as REACHABLE (INFERRED), not UNREACHABLE. It is judged below as a reachable route, not as an UNREACHABLE entry.
- verification.csv: absent on work-2026-10-31 (connector read returned "does not exist"), consistent with 0 route checks started. graphs/MMEX/graph_def.py (1,348,082 bytes) is too large for the connector to display, so part 146/147 edges were read from graphs/MMEX/parts/label_146.py and label_147.py, not from graph_def.py itself.

## Counts — only for items actually judged here (NOT the WP2 sample)

- Fully judged items (printed source lines checked by this helper): 20
  - correct: 18
  - wrong: 1 (one edge, not a method label — see R9)
  - unclear: 1 (R1)
  - fixed by this helper: 0 (helpers must not edit graph_def.py)
- Edge-level rate on the judged set only, for orientation — NOT the WP2 error rate:
  (fixed + wrong) / (correct + fixed + wrong) = 1 / 19 = 5.3%. Unclear is excluded, as in the WP2 formula.
- NOT counted: Dagger MembersInjector/Factory entries in batches 133 and 137 other than the unbind rows, and MmxDatabaseUtils.createDatabase* / cleanupFilename / isEncryptedDatabase SOURCE claims. Those were read in label_133.py / label_137.py but their underlying grep/auto_calls evidence was not re-printed by this helper, so they are listed under "Not checked" below, not judged.

## Judged routes/methods (printed-source citations per step)

Source root in the repo: final_java_only/MMEX/app/MMEX-#v2024.06.14/app/src/main/java/com/money/manager/ex/
FW-SRC root in the repo: fw_src/android-8.1.0_r1/

### R1 — TutorialPagerAdapter.getPageTitle — UNREACHABLE, framework_never_calls, INFERRED — UNCLEAR
- Label in graphs/MMEX/parts/label_135.py:122-125; grep evidence graphs/MMEX/parts/label_135.grep.txt section 3.
- Printed and confirmed: TutorialPagerAdapter.java:68-70 defines getPageTitle returning "OBJECT " + (position + 1); TutorialActivity.java:61-64 sets the ViewPager adapter and calls circleIndicator.setViewPager(viewpager); res/layout/activity_tutorial.xml contains only ViewPager, me.relex.circleindicator.CircleIndicator, and a TextView — no TabLayout, PagerTitleStrip or PagerTabStrip. label_135.grep.txt section 3 finds getPageTitle only in TutorialPagerAdapter.java:68 and AboutTabAdapter.java:66 (the About case, which does have a TabLayout at AboutActivity.java:54).
- NOT printed, therefore not checked (KIRO §4: a step not printed counts as not checked): androidx ViewPager / FragmentStatePagerAdapter behaviour, and CircleIndicator behaviour. CircleIndicator holds the ViewPager/adapter, so its source is the one library step that could in principle call getPageTitle. The label's INFERRED status is therefore justified, but the route cannot be marked correct on app-side evidence alone.
- Proposed fix (not merged): print CircleIndicator source (external library — orchestrator decision needed on whether external library source counts as evidence) and androidx ViewPager title handling. If neither calls getPageTitle, keep the label and record the print; if CircleIndicator does call it, relabel REACHABLE with that route. Do not change the label on this check alone.

### R2 — TutorialActivity_ViewBinding.unbind — UNREACHABLE, no_trigger_in_app, INFERRED — CORRECT
- Label in label_135.py:117-120. Printed: TutorialActivity.java:57 `ButterKnife.bind(this);` — the returned Unbinder is discarded (statement alone, no assignment). No caller can therefore call unbind on a retained binding. Generated binding source itself is not in the source root, so INFERRED is correctly retained; no label change proposed.

### R3 — EditTransactionViewHolder_ViewBinding.unbind — UNREACHABLE, no_trigger_in_app, INFERRED — CORRECT
- Label in label_133.py:130-133. Printed: transactions/EditTransactionViewHolder.java:45 `ButterKnife.bind(this, view);` (discarded); a full-file search printed by this helper found zero `unbind` occurrences in that file. INFERRED retained for the generated class / "ButterKnife does not call unbind automatically" step, which is not printed. No label change proposed.

### R4 — SplitCategoriesActivity_ViewBinding.unbind — UNREACHABLE, no_trigger_in_app, INFERRED — CORRECT
- Label in label_133.py:135-138. Printed: transactions/SplitCategoriesActivity.java:101 `ButterKnife.bind(this);` (discarded); full-file searches printed by this helper found zero `unbind` and zero `onDestroy` occurrences in that file. INFERRED retained as for R3. No label change proposed.

### R5 — AccountBillsWidgetService.onGetViewFactory — UNREACHABLE, framework_never_calls, INFERRED — CORRECT
- Label in label_143.py (onGetViewFactory entry). Printed chain, step by step:
  1. widget/AccountBillsWidgetService.java:25-28 — onGetViewFactory returns new AllAccountBillsViewFactory(...).
  2. widget/AccountBillsWidgetProvider.java — onUpdate builds svcIntent for AccountBillsWidgetService and calls remoteViews.setRemoteAdapter(R.id.listViewAccountBills, svcIntent).
  3. FW-SRC RemoteViewsAdapter.java:178 (mgr.bindRemoteViewsService(...)) and 184-188 (catch Exception, log, mIsConnected=false).
  4. FW-SRC core/java/android/widget/RemoteViewsService.java:235-243 — onBind calls onGetViewFactory at line 241, but only if binding reaches onBind.
  5. FW-SRC services/appwidget/java/com/android/server/appwidget/AppWidgetServiceImpl.java:1251 (enforceServiceExistsAndRequiresBindRemoteViewsPermission call) and 3598-3612 (throws SecurityException unless serviceInfo.permission equals BIND_REMOTEVIEWS).
  6. AndroidManifest.xml:401-403 — the service declares android:permission="android.permission.BIND_JOB_SERVICE", not BIND_REMOTEVIEWS, so step 5 throws and step 4 never runs.
- INFERRED retained, exactly as the label states, for the one unprinted link: AppWidgetManager.bindRemoteViewsService delegation (AppWidgetManager.java was not found in fw_src at core/java/android/appwidget/AppWidgetManager.java). No label change proposed. Optional strengthening: if AppWidgetManager is located elsewhere in fw_src, print it and the label could be re-examined for SOURCE; do not upgrade on this check alone.

### R6 — AccountBillsWidgetService.<init> — UNREACHABLE, framework_never_calls, INFERRED — CORRECT
- Same chain as R5. Printed: widget/AccountBillsWidgetService.java:22-23 (implicit constructor at the class declaration); label_143.grep.txt Q1 shows 0 incoming auto_calls records for <init> and for onGetViewFactory. The framework creates the service only on bind, and the bind is refused (R5), so the constructor never runs. INFERRED retained as for R5. No label change proposed.

### R7 — MmxDatabaseUtils.<clinit> — REACHABLE, INFERRED — CORRECT (as REACHABLE)
- Label in label_137.md row 5 (REACHABLE, not UNREACHABLE — see correction at top). Printed:
  1. home/MainActivity.java:545 `MmxDatabaseUtils dbUtils = new MmxDatabaseUtils(this);` — first use of the class.
  2. utils/MmxDatabaseUtils.java:358 and 361 — `assert client != null;` and `assert provider != null;` in resetContentProvider, the asserts the label cites as the reason javac generates a <clinit> ($assertionsDisabled).
  3. utils/MmxDatabaseUtils.java:92-98 — the constructor calls MmexApplication.getApp().iocComponent.inject(this).
- The JVM class-initialisation step (first new/static use runs <clinit> before <init>) and the javac assert-field step are INFERRED, not printed from a JVM/javac source, so INFERRED is correctly retained. No label change proposed.

### R8 — PasscodeActivity.onEvent via DebugTree.log — REACHABLE, part 146 — CORRECT (with env-text note)
- Edge in label_146.py (DebugTree.log -> PasscodeActivity.onEvent, ASYNC, non_standard via EventBus, INFERRED). Printed:
  1. MmexApplication.java:134-135 — debug branch plants DebugTree.
  2. log/DebugTree.java:36-38 (minLevel INFO, guard priority >= minLevel), 45-46 (hasSubscriberForEvent(ErrorRaisedEvent) then post(new ErrorRaisedEvent(...))).
  3. PasscodeActivity.java:202-206 (onStart registers with EventBus), 214-218 (@Subscribe onEvent(ErrorRaisedEvent), shows toast).
- Proposed fix (not merged, wording only, no label change): the edge env text says "an error is logged", but DebugTree posts for any Timber log at INFO or above, not only errors. Widen the env text to "a Timber log at INFO or above while PasscodeActivity is registered" or add guard `priority >= Log.INFO` (DebugTree.java:36-38). EventBus dispatch itself remains INFERRED (library source not read), as the edge already states.

### R9 — PasscodeActivity.onEvent via ScreenTree.log — part 146 edge — WRONG (edge only; method stays REACHABLE via R8)
- Edge in label_146.py (ScreenTree.log -> PasscodeActivity.onEvent). Printed contradiction:
  1. MmexApplication.java:136-139 — ScreenTree is planted only in the `else` (release) branch; the debug branch at 134-135 plants DebugTree instead.
  2. log/ScreenTree.java:19, 26-27 — same INFO guard and post logic as DebugTree, so the edge would run in a release build, but not under the standard configuration (debug build).
- This matches the mistakes-list pattern: a branch that only runs when !DEBUG never runs in the debug build.
- Proposed fix (not merged): remove the ScreenTree dispatch edge from the standard-config graph, or annotate it explicitly as release-only and exclude it from the debug route set. Do NOT relabel PasscodeActivity.onEvent: R8 (DebugTree) is a valid debug-build route, so the method remains REACHABLE. Rebuild and re-print after the fix; the edge count and any route that used ScreenTree as its sole source must be re-checked.

### R10 — BudgetsActivity.onEvent — REACHABLE, part 146 — CORRECT (with citation-gap fix)
- Edge in label_146.py (BudgetListFragment.onListItemClick -> BudgetsActivity.onEvent, ASYNC, non_standard via EventBus, INFERRED). Printed:
  1. budget/BudgetListFragment.java:208-215 — onListItemClick posts new BudgetSelectedEvent(id, budgetName) at line 215.
  2. budget/BudgetsActivity.java:82-85 — @Subscribe onEvent(BudgetSelectedEvent) calls showBudgetDetails.
  3. common/MmxBaseFragmentActivity.java:134-146 — base class onStart registers (line 141) and onStop unregisters (line 146); BudgetsActivity extends MmxBaseFragmentActivity (BudgetsActivity.java:35-36) and has no register call of its own (full-file search printed by this helper found zero `register`/`EventBus` occurrences in BudgetsActivity.java).
- Proposed fix (not merged, citation only): add `SRC common/MmxBaseFragmentActivity.java:134-146` to the edge evidence, since the registration step is inherited and is not cited in label_146.py. No label change. Minor note: the route needs at least one budget row to tap (cursor row at BudgetListFragment.java:212-213); a STATE `data` note could be added, but it does not change the verdict.

### R11 — MmexApplication.lambda$onCreate$0 — REACHABLE, part 146 — CORRECT (INFERRED)
- Edge in label_146.py (MmexApplication.onCreate -> lambda$onCreate$0, CALL, non_standard via Amplitude). Printed: MmexApplication.java:147-154 — AmplitudeKt.Amplitude(..., configuration -> { setDefaultTracking(...); setOptOut(!...getSendUsage()); ... }) at lines 149-153. The library's call of the configuration block while building the client is INFERRED (com.amplitude.android not in the dataset), as the edge already states. The setOptOut line is inside the lambda body, not a gate for the lambda running. No label change proposed.

### R12 — BehaviourSettingsFragment.lambda$showTimePicker$0 — REACHABLE, part 146 — CORRECT (INFERRED)
- Edge in label_146.py (showTimePicker -> lambda$showTimePicker$0, FRAMEWORK, non_standard via TimePickerDialog). Printed: settings/BehaviourSettingsFragment.java:101-104 (lambda: setNotificationTime), 106-112 (TimePickerDialog construction with that listener), 114 (show()). TimePickerDialog calling its OnTimeSetListener is INFERRED (framework source not in fw_src), as the edge already states. No label change proposed.

### R13 — CategoriesReportFragment.onCreateOptionsMenu — REACHABLE, part 147 — CORRECT (INFERRED)
- Edge in label_147.py (BaseReportFragment.onActivityCreated@CategoriesReportFragment -> onCreateOptionsMenu, FRAMEWORK). Printed: reports/BaseReportFragment.java:74-79 (onActivityCreated, setHasOptionsMenu(true) at 79); reports/CategoriesReportFragment.java:102-113 (onCreateOptionsMenu, super at 104). androidx FragmentManager dispatch is INFERRED (library not read), as the edge states. The @Recv copy linkage itself rests on an auto_calls.json record cited in the edge (line 55523) which was not re-printed by this helper — noted as a residual gap, not a contradiction. No label change proposed.

### R14 — PayeeReportFragment.onCreateOptionsMenu — REACHABLE, part 147 — CORRECT (INFERRED)
- Same pattern as R13. Printed: reports/BaseReportFragment.java:74-79 (setHasOptionsMenu at 79); reports/PayeeReportFragment.java:194-196 (onCreateOptionsMenu, super at 196). androidx dispatch INFERRED as stated. Auto_calls @Recv record (line 55891, cited in the edge) not re-printed by this helper. No label change proposed.

### R15 — BaseExpandableListFragment.setResultAndFinish@CategoryListFragment — REACHABLE, part 147 — CORRECT (guard omission — proposed fix below)
- Edge in label_147.py (CALL, standard). Printed: common/BaseExpandableListFragment.java:158-164 (home arrow calls setResultAndFinish at 164, unless the activity is MainActivity at 161-162), 260-265 (setResultAndFinish calls this.setResult() at 262, then finish at 264); common/CategoryListFragment.java:313-315 (setResult override, ACTION_PICK check at 314, early return if adapter null at 315), 661-675 and 681-695 (row taps call setResultAndFinish at 675 and 695, only when mAction equals ACTION_PICK at 661).
- Proposed fix (not merged): add the ACTION_PICK gate to the edge (guard / needs_state): the override path runs only for ACTION_PICK pickers with a non-null adapter. The method remains REACHABLE via that picker route, so no label change; the edge text as written overstates the route (it omits the ACTION_PICK condition, a mistakes-list guard omission).

### R16 — BaseExpandableListFragment.onPreQueryTextChange@CategoryListFragment — REACHABLE, part 147 — CORRECT (minor note)
- Edge in label_147.py (CALL, standard). Printed: common/BaseExpandableListFragment.java:206-215 (onPreQueryTextChange at 206, calls onQueryTextChange at 210, base returns true at 213-215); common/CategoryListFragment.java:230-235 (onQueryTextChange override, sets filter, restarts loader). androidx SearchView calling the listener on each text change is INFERRED as stated. Note only: BaseExpandableListFragment.java:207 applies a "%" prefix when PREF_TEXT_SEARCH_TYPE is true — that changes the query text, not whether the override runs, so no verdict change and no fix proposed beyond recording the guard if the orchestrator wants it.

### R17 — BaseListFragment.setResultAndFinish@AccountListFragment — REACHABLE, part 147 — CORRECT (guard omission — proposed fix below)
- Edge in label_147.py (CALL, standard). Printed: common/BaseListFragment.java:151-161 (home arrow calls setResultAndFinish at 157, unless MainActivity at 154), 177-180 (setResultAndFinish calls setResult at 178, finish at 179); account/AccountListActivity.java:60-68 (onKeyUp BACK calls fragment.setResultAndFinish at 64, only if fragment non-null at 63); account/AccountListFragment.java:221-223 (setResult override, ACTION_PICK check at 223).
- Proposed fix (not merged): same as R15 — add the ACTION_PICK gate to the edge text. No label change; the account-picker route (ACTION_PICK) is the valid route.

### R18 — PayeeListFragment.lambda$onContextItemSelected$0 — REACHABLE, part 147 — CORRECT
- Edge in label_147.py (FRAMEWORK, needs_state data). Printed: fragment/PayeeListFragment.java:217-229 (DELETE case, isPayeeUsed at 219, warning dialog with positive-button lambda `(dialog, which) -> dialog.dismiss()` at 226, show at 228). The state text is correct: isPayeeUsed true takes the `else` branch (221) to the warning dialog; isPayeeUsed false takes showDialogDeletePayee (220). FW-SRC core/java/com/android/internal/app/AlertController.java:1022-1023 (setButton BUTTON_POSITIVE), 127-130 and 139-146 (click obtains/posts the button message), 149-166 (ButtonHandler calls the OnClickListener at 166). No label change proposed.

### R19 — EditTransactionCommonFunctions$5.lambda$onClick$0 — REACHABLE, part 147 — CORRECT
- Edge in label_147.py (FRAMEWORK). Printed: transactions/EditTransactionCommonFunctions.java:488-496 (anonymous $5 onClick at 490, OnDateSetListener lambda at 493-496 setting the date), 498-507 (DatePickerDialog construction with that listener, show at 507). FW-SRC core/java/android/app/DatePickerDialog.java:122-123 (positive button with `this` as listener), 164-171 (onClick BUTTON_POSITIVE calls mDateSetListener.onDateSet at 171-172); FW-SRC AlertController.java:127-130, 149-166 as for R18. No label change proposed.

## Not checked (read, not re-printed — do not count as judged)

- Batch 133 Dagger: EditTransactionCommonFunctions_MembersInjector.<init> / create / injectMembers (label_133.py:115-128) — grep G2/G3 and auto_calls 0-incoming claims not re-printed by this helper.
- Batch 137 Dagger: MmxDatabaseUtils_Factory.<init> / create / get / newMmxDatabaseUtils, MmxDatabaseUtils_MembersInjector.<init> / create / injectMembers (label_137.py:74-115) — MmxComponent.java:101 and DaggerMmxComponent.java:533-537 claims not re-printed by this helper.
- Batch 137 SOURCE claims: MmxDatabaseUtils.createDatabase() (java:133-135, printed by this helper), createDatabase(String) (143-152, printed), createDatabase_Internal (261-288, partially printed), cleanupFilename, isEncryptedDatabase (74-76, printed) — the "no caller in the source root" grep claims were not re-printed by this helper, so these are not judged here.
- Out/methods.csv route columns and any out/* build output — not printed by this helper (out/ listing is per-build files; no single current methods.csv route was verified). The handover counts (4270 labelled, 3430 REACHABLE / 840 UNREACHABLE, 0/0, build p147) were NOT re-checked by a build run and must not be copied as verified; they match graphs/MMEX/AGENT_NOTES.md "Current step" text only.
- Sample_30 (seed 20261025) — not drawn. No WP2 sample table, no WP2 error rate, no verification.csv rows are proposed here; the orchestrator must draw the sample on a full checkout and re-check.

## Proposed fixes summary (all NOT merged — orchestrator to apply, rebuild, re-print)

1. P146 ScreenTree edge (R9, wrong under debug config): remove the ScreenTree.log -> PasscodeActivity.onEvent edge from the standard-config graph, or annotate it release-only and exclude it from debug routes. Keep DebugTree edge (R8). Rebuild, re-print PasscodeActivity.onEvent route.
2. P146 DebugTree env text (R8, wording): widen to "a Timber log at INFO or above while PasscodeActivity is registered" / add guard priority >= Log.INFO (DebugTree.java:36-38).
3. P146 BudgetsActivity citation (R10): add SRC common/MmxBaseFragmentActivity.java:134-146 to the edge evidence.
4. P147 picker guards (R15, R17): add ACTION_PICK gate to both setResultAndFinish@ edges (CategoryListFragment.java:314, AccountListFragment.java:223; row-tap handlers only under ACTION_PICK, CategoryListFragment.java:661).
5. R1 getPageTitle (unclear): print CircleIndicator + androidx ViewPager title handling before any label decision (see R1).
6. R5 optional strengthening: locate AppWidgetManager.bindRemoteViewsService in fw_src if it exists elsewhere; otherwise keep INFERRED.

## Blockers / decisions needed (for the parent orchestrator, not decided here)

- D1: Is external library source (CircleIndicator, androidx ViewPager) admissible as route-check evidence, or does an INFERRED label stand on app-side evidence + saved grep alone? This decides R1 (unclear vs correct).
- D2: Confirm the ScreenTree removal (R9) does not break any other route that relied on ScreenTree as its sole source; rebuild diff needed on a full checkout.
- D3: Sampler + build + C1 checks require a full local checkout; this connector-only check cannot run them. The part must stay PENDING until the orchestrator runs tools/verify_sample.py MMEX 30 20261025, tools/build_graph.py, and the section-2 checks and re-draws the sample after fixes.
- D4: graph_def.py is too large for connector display; part 146/147 edges were verified from parts/label_146.py and label_147.py. The orchestrator should confirm those part files are byte-identical to the merged graph_def.py sections before merging any fix.
- No push was made by this helper, per the updated push rule and the original "do NOT push" brief. This file is the separable proposed set for a later, separately-approved commit to branch `result` only (never work-2026-10-31 or main), once D3 is satisfied.

## Handover sections read

- handoff/MUSE_HANDOVER.md §2 (rules) and WP2 (full text read via connector, work-2026-10-31).
- handoff/KIRO_CONVERT_APPS.md §4 (route checks), §5 (framework/library claims) — read via connector.
- handoff/AGENT_BRIEF_V2.md §5 (mistakes list) — read via connector in full.
- handoff/SCHEMA_V2.md — read via connector in full.
- graphs/MMEX/AGENT_NOTES.md — read via connector (166,839 bytes); part 146/147 summaries and build p147 line used only as pointers, not as verified counts.
- handoff/HANDOFF_V2.md "Convert run decisions (MMEX overnight labelling, 2026-10-31)" — read via connector (parts 133/135/137/143/144/146/147 entries).
- graphs/MMEX/parts/label_133.py, label_135.py (+ label_135.grep.txt), label_137.py (+ label_137.md), label_143.py (+ label_143.grep.txt), label_146.py, label_147.py — read via connector.
