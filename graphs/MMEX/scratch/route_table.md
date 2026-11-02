# MMEX B6 — FINAL route table (redrawn sample, audited)

- Sample: `scratch/sample_30_final.txt` — 30 of 3430 reachable methods,
  341 distinct edges, seed 20261025, drawn with
  `python3 -I tools/verify_sample.py MMEX 30 20261025` AFTER all fix groups.
  First-draw `sample_30.txt` untouched for history.
- Build at redraw time: 4270 methods, 3430 REACHABLE / 840 UNREACHABLE,
  8256 edges, errors 0, warnings 0 (final build after the guard group).
- Why the 30 differ from the first draw: the sampler is a greedy-coverage
  pick over strata + a seeded shuffle of methods.csv row order, and the fix
  phase changed routes, strata, edge ids, and row order. The tool's output
  on the fixed graph IS the final sample per the brief ("final sample
  redrawn after last fix"). Composition: 10 of the 15 fixed WRONG routes +
  the getContext fallback + all 6 FIXED + all 3 CORRECT + 4 UNCLEAR +
  6 never-judged routes. The 6 first-draw routes NOT resampled are listed
  at the end (their fixes stand on fix-phase reprint verifications).
- Judging: helpers b6-redraw-h1..h10 (max 3 routes each), every step judged
  fresh on the NEW dumps in `scratch/route_print_final/` against printed
  source. Every helper output independently audited (a1..a10) before
  acceptance; audit verdicts below. The table incorporates all audit
  corrections (verdict changes + citation/wording corrections).
- Route verdict rule: WRONG if any step WRONG; else UNCLEAR if any step
  UNCLEAR; else FIXED if any step FIXED; else CORRECT.
- INFERRED-delivery standard (auditor consensus, a1-a10): an INFERRED
  library/framework delivery step is CORRECT/FIXED when its app-side
  endpoints are verified in printed source, the dispatch is the standard
  mechanism for that library, the step is explicitly flagged INFERRED, and
  nothing printed contradicts it (a1's 5-condition test). UNCLEAR is
  reserved for genuine app-side doubt (ambiguous logic, unverified guard,
  unknown branch, hidden identity routing such as androidx FragmentActivity
  dispatch). A verifiably failed app-side precondition is WRONG, not
  UNCLEAR (a3); proven absence of a subscriber/recipient is WRONG, not
  UNCLEAR (a9). The strict blanket line ("any INFERRED blocks") was
  considered and rejected by the auditors (a5's infinite-regress argument:
  printed ActivityThread snippets themselves rest on unprinted AMS/Binder
  internals). FW-SRC analogies are analogy only, never SOURCE (a1).

## Final tally (audited)

- Routes: CORRECT 13 / FIXED 10 / WRONG 5 / UNCLEAR 2 = 30.
- Steps: correct 423 / fixed 24 / wrong 7 / unclear 3 = 457.
- Final error rate = (fixed + wrong) / (correct + fixed + wrong)
  = (10 + 5) / (13 + 10 + 5) = 15 / 28 = **0.5357**.
  (UNCLEAR excluded per the formula. First-draw rate was 21/24 = 0.875 on
  a DIFFERENT 30 — the comparison is indicative, not apples-to-apples,
  because the samples differ; the final rate is on the redrawn sample.)
- Audited WRONG routes (5): SyncPreferenceFragment.onEvent,
  IncomeVsExpensesListFragment$1.run, DatabaseManager.getContext
  (wrong-with-reason fallback), StockHistoryRepository.getContentValues,
  Stock.getNumberOfShares. The last two are NEW routes (never judged,
  untouched by the fix phase); the Sync defect is a CONFIRMED fix-phase
  defect (see route 12). No second fix phase is started unilaterally:
  repairs need coordinator authorization (see STOP note at the end).

## Per-route verdicts (in sample order)

### 1. DbModule_ProvideSqlBriteFactory.get — NONSTD, 27 steps — CORRECT
- Steps 1-27 CORRECT. Drawer @GROUP prefix verified (Budgets group, null
  children, item menu_budgets; group-click -> Runnable -> @GROUP dispatcher
  -> menu_budgets case). Dagger Lazy/Provider tail (steps 26-27) INFERRED
  (generated code not read, as flagged) but topologically sound under the
  5-condition test (DbModule.java:53 is the file's only SqlBrite provider).
- Judge h1; audit a1 PASS-WITH-CORRECTIONS (no verdict change; 60/72
  CORRECT steps spot-checked, 83%).

### 2. SplitCategoriesActivity$1.<init> — NONSTD, 24 steps — FIXED
- Steps 1-23 CORRECT; step 24 FIXED (evidence citation only: the listener
  is instantiated at SplitCategoriesActivity.java:321, not the cited :320
  (setMessage); corrected citation
  transactions/SplitCategoriesActivity.java:318-321 — builder :318,
  listener :321; $1 identity holds, file's only anonymous class).
  @CHECKING host, @SPLIT calculator (requestId + 1000 offset), @AMOUNT
  return verified, incl. RESULT_OK + data guard (:129) and requestCode >=
  1000 guard (:142).
- Judge h1; audit a1 PASS-WITH-CORRECTIONS.

### 3. AllDataListFragment.displayRunningBalances — NONSTD, 24 steps — FIXED
- Steps 1-15 CORRECT; step 16 FIXED (wording: "Direct call" -> guarded
  call — loadTransactions() at :587 only inside if(result) at :576, status
  cases :555-569, default :570-573 sets result false; tapped item must be
  a transaction-status item; step 14 narrowed accordingly but stays
  CORRECT as the unconditional menu-dispatch step); steps 17-21 CORRECT;
  step 22 FIXED (delete the stale "(AsyncTask.java not found)" dump
  parenthetical — file IS present in fw_src, :429 = base-class onPostExecute
  declaration, executed override at CalculateRunningBalanceTask2.java:98-99;
  chain postResult -> handleMessage -> finish -> onPostExecute verified);
  steps 23-24 CORRECT. Options-menu middle (the spec's accepted middle).
- Judge h1; audit a1 PASS-WITH-CORRECTIONS.

### 4. Stock.setSymbol — NONSTD, 22 steps — FIXED
- Steps 1-7 CORRECT; step 8 FIXED (guard missing from the dump: newInstance
  called only if no PortfolioFragment with that tag exists yet,
  MainActivity.java:791-797; edge sound); steps 9-22 CORRECT. First-draw
  EventBus UNCLEAR closed: post (HomeFragment.java:473-474), @Subscribe
  (MainActivity.java:464-467), registration via MmxBaseFragmentActivity
  .onStart (:141) all verified; greenrobot delivery itself INFERRED,
  acceptable under the consensus standard.
- Judge h4; audit a4 PASS.

### 5. Passcode.savePasscode — INFERRED, 29 steps — UNCLEAR
- Steps 1-20 CORRECT; step 21 UNCLEAR (PasscodeActivity onClick ->
  fragment onActivityResult, first visit — androidx FragmentActivity result
  dispatch routing to the requesting fragment is not in fw_src; the guard
  edit governs the handler, not delivery); step 22 CORRECT; step 23 FIXED
  (citation only: REQUEST_REINSERT_PASSCODE at :43, not :45 — line 45 is
  `private String passcode = null;`; topology :106 -> :168-175 sound);
  steps 24-26 CORRECT; step 27 UNCLEAR (same dispatch gap, second/REINSERT
  visit; its guard correctly includes the editTextPasscode5 precondition);
  steps 28-29 CORRECT. GROUP prefix + @REINSERT chain verified fresh.
  Audit a2 strengthened the UNCLEAR: platform Activity.dispatchActivityResult
  (:7260-7293) serves the android.app.Fragment registry only and cannot
  deliver to this androidx PreferenceFragmentCompat fragment; upgrading
  needs printed androidx dispatch, not a guard edit.
- Judge h2; audit a2 PASS-WITH-CORRECTIONS (citation :45 -> :43 only).

### 6. SplitRecurringCategoriesRepository.insert — INFERRED, 23 steps — CORRECT
- Steps 1-23 CORRECT. @RECURRING chain verified (MainActivity.java:651-652,
  734-752, 758-770, 1446-1466); split guard matches exactly
  (RecurringTransactionEditActivity.java:571-580: hasSplitCategories, id ==
  null OR == NOT_SET, then insert). FAB wiring verified beyond the dump's
  note (BaseListFragment.java:238-244).
- Judge h2; audit a2.

### 7. StockHistoryRepository$UpdateType.<init> — INFERRED, 21 steps — FIXED
- Steps 1-9 CORRECT; step 10 FIXED (wording: "after the committed fragment
  is attached" — showWatchlistFragment -> showFragment ->
  showFragment_Internal transaction commit); steps 11-13 CORRECT; step 14
  FIXED (guard: quote provider == Morningstar — SecurityPriceUpdaterFactory
  returns Morningstar only for Morningstar; YahooYql/YahooCsv/default return
  Yql updaters); steps 15-21 CORRECT. INFERRED-delivery steps 5
  (ExpandableListView), 6 (EventBus — subscriber registered via onStart,
  alive on prefix), 11 (androidx lifecycle), 16 (RxJava doOnNext)
  acceptable under the consensus standard.
- Judge h9; audit a9 PASS.

### 8. StockHistoryRepository.getContentValues — INFERRED, 20 steps — WRONG
- Steps 1-10 CORRECT; step 11 FIXED (must be case 2, Update exchange rate,
  :264-266); steps 12-13 CORRECT; step 14 CORRECT (unconditionally
  FixerService — ExchangeRateUpdaterFactory returns it in both branches);
  steps 15-16 CORRECT; step 17 WRONG (FixerService's PriceDownloadedEvent
  cannot reach WatchlistFragment on this prefix: no WatchlistFragment ever
  created/started/registered in steps 1-16 — the only Watchlist mention is
  step 17's own STATE guard; sole registration WatchlistFragment.onStart
  (:128-131) never runs; FixerService post (:120) has no subscriber; the
  dump's "user returned to the watchlist" STATE invents navigation not in
  the route; corroborating: onPriceDownloaded (:341) dereferences
  mDataFragment, set only in onCreateView (:164-171), never run);
  steps 18-20 locally CORRECT but unreachable.
- Judge h9; audit a9 PASS. NEW route (not in the first draw, not touched
  by the fix phase) — carried as WRONG; repair needs coordinator
  authorization.

### 9. CategoryListFragment$2.onClick — STATE, 16 steps — FIXED
- Steps 1-14 CORRECT; step 15 FIXED (needs DELETE-case guard,
  CategoryListFragment.java:213-217; call at :217 inside case DELETE
  :216); step 16 FIXED, not WRONG (by anonymous-class file order, $1 =
  cannot-delete OK listener (:466, dismiss only), $2 = confirm-delete OK
  listener (:483, deletes the row via CategoryRepository, toasts on 0
  rows, restarts loader), $3 = Cancel listener (:500, dialog.cancel());
  the dump's "Cancel" description is $3, not $2; the stated STATE (category
  row, unused) is exactly right for $2's dialog; wording only, no edge
  change).
- Judge h4; audit a4 PASS (independent inventory confirmed :466/:483/:500,
  no earlier anonymous class, no named inners shifting numbering).

### 10. Core.resolveColorAttribute — STATE, 18 steps — CORRECT
- Steps 1-18 CORRECT. Child-click prefix verified (Payee is the first entry
  of childReports, MainActivity.java:898) + Payee-specific variant chain
  (PayeesReportActivity -> PayeeReportFragment -> BaseReportFragment
  .onCreate/onActivityCreated/startLoader/onCreateLoader@Payee ->
  PayeeReportAdapter.bindView -> resolveColorAttribute at
  PayeeReportAdapter.java:75); no CategoriesReport leak.
- Judge h3; audit a3 PASS.

### 11. DateRange.<init>() — STATE, 24 steps — CORRECT
- Steps 1-24 CORRECT. Drawn path is @RESTORED -> createFromParcel (not the
  fresh-Bundle path); restored-filter non-null guard has an in-route
  producer (AccountTransactionListFragment onCreate calls
  updateFilterDateRange, :143-146, :890-897); FW-SRC Bundle/Parcel
  unparcel -> creator chain printed (Bundle.java:938-939, Parcel
  .java:2744-2745, :2841-2851).
- Judge h2; audit a2.

### 12. SyncPreferenceFragment.onEvent — ENV, 10 steps — WRONG
- Steps 1-7 CORRECT; step 8 WRONG (action == DOWNLOAD guard false on this
  prefix: triggerSynchronization hardcodes INTENT_ACTION_SYNC
  (SyncManager.java:348, preserved verbatim by IntentFactory setAction
  :42, no different action set by invokeSyncService); onHandleWork switches
  on intent.getAction() (SyncService.java:90-93) -> SYNC branch (:134-135,
  triggerSync) fires, never the DOWNLOAD case (:126-128)); step 9 WRONG (no
  message is sent on this prefix — send/handler/EventBus machinery itself
  is sound (code 0x000A, parse :61-63, post :89, @Subscribe :120-123) but
  as steps of this route they cannot happen); step 10 WRONG (subscriber
  never registered: SyncPreferenceFragment registers only in onStart
  (:103-107, unregisters onStop) and the drawn prefix has no
  Settings/fragment-open step; the step-10 ENV text describes the
  different forceDownload prefix (click :236 -> forceDownload :307-308 ->
  triggerDownload -> DOWNLOAD at SyncManager.java:356-357)).
- Valid non-shortest alternative (NOT drawn): the triggerSync
  remote-only-modified branch (SyncService.java:206-210, pullDatabase +
  DOWNLOAD_COMPLETE, reachable only after the no-change and both-modified
  returns) — but only with that extra guard PLUS a subscriber-open prefix,
  neither in the drawn route. The drawn route cannot be rescued by wording
  alone.
- Judge h3; audit a3 PASS (confirmed line by line; no alternative verdict
  supported). CONFIRMED event-fix defect: the onHandleWork ->
  sendMessage@DOWNLOAD edge is fed by a SYNC-action prefix. Repair (re-feed
  @DOWNLOAD from the triggerSync branch + subscriber-open prefix +
  re-redraw + re-judge) needs coordinator authorization — see STOP note.

### 13. RecurringTransactionIntentService.onHandleWork — ENV, 7 steps — CORRECT
- Steps 1-7 CORRECT, as corrected by audit a5 (helper verdict UNCLEAR
  overturned). Step 4 CORRECT (was UNCLEAR: standard AlarmManager
  broadcast delivery; app-side notify gate, explicit PendingIntent,
  setRepeating verified). Step 7 CORRECT (was UNCLEAR: standard
  JobIntentService dispatch; JOB_ID 1001 delegation verified).
- Judge h5; audit a5 PASS-WITH-CORRECTIONS.

### 14. IncomeVsExpensesListFragment$1.run — ENV, 11 steps — WRONG
- Steps 1-2 CORRECT; step 3 FIXED (needs !showPrerequisite() guard —
  onCreate :184-187 returns before the initHomeFragment call :238);
  step 4 CORRECT; steps 5-9 CORRECT, as corrected by audit a5 (helper
  verdicts UNCLEAR overturned: standard dispatch; step 5 + FW-SRC
  View.java:5046, :5350-5408 DeclaredOnClickListener citation); step 10
  FIXED (was UNCLEAR: annotate "YEARS loader" — delivery standard,
  identity wording only); step 11 WRONG (Handler post creating the $1
  Runnable sits inside the REPORT-loader branch only, :188-196; the YEARS
  branch reached at step 9, :199-212, calls startLoader() at :212 and never
  posts; the route omits YEARS -> startLoader -> restartLoader(REPORT)
  (:401-410) -> onCreateLoader(REPORT) -> onLoadFinished(REPORT)).
- Judge h5; audit a5 PASS-WITH-CORRECTIONS. Note: h5's own tally table
  miscounted this route (6c/3u) against its step table (5c/4u); a5's
  corrections applied to the step tables give the consistent corrected
  counts used here (8c/2f/1w). The step tables are authoritative.

### 15. RecurringTransactionListActivity.onActivityResult — ENV, 9 steps — FIXED
- Steps 1-2 CORRECT; step 3 FIXED (needs showPrerequisite()==false guard —
  :184-186 return before :244 populateScheduledTransactions in the same
  onCreate, no other return between; corrected citation :1478-1489:
  tutorial branch :1480-1482 + no-database branch :1486-1488);
  steps 4-9 CORRECT. (Step 7 INFERRED-delivery PendingIntent tap
  acceptable under the consensus standard; the stricter SOURCE-only
  reading is recorded in the helper file.)
- Judge h6; audit a6 PASS-WITH-CORRECTIONS (citation :1478-1482 ->
  :1478-1489 only).

### 16. TutorialActivity.onOptionsItemSelected — ENV, 8 steps — CORRECT
- Steps 1-8 CORRECT. (Step 8 INFERRED-delivery androidx menu-dispatch
  passthrough acceptable under the consensus standard; framework
  Activity.java:3439-3450 dispatch itself printed; no androidx source in
  fw_src.)
- Judge h6; audit a6.

### 17. SingleAccountWidgetConfigureActivity.saveTitlePref — ENV, 4 steps — FIXED
- Steps 1-2 CORRECT; step 3 FIXED (needs a valid EXTRA_APPWIDGET_ID —
  listener wired at :65, then :76-78 finish/return if mAppWidgetId ==
  INVALID_APPWIDGET_ID); step 4 CORRECT.
- Judge h6; audit a6.

### 18. Stock.getNumberOfShares — LONG, 17 steps — WRONG
- Steps 1-14 CORRECT; step 15 WRONG (calculator launched by
  AccountEditActivity for RequestCodes.AMOUNT (= 2, :301-307; Calculator
  .show -> startActivityForResult); FW-SRC ActivityThread.deliverResults ->
  dispatchActivityResult delivers to the starting activity, whose handler
  covers AMOUNT; InvestmentTransactionEditActivity never appears in steps
  1-14; its own launch (:215-218) uses REQUEST_NUM_SHARES (= 1) and its
  handler (:119-158) dispatches on that code); steps 16-17 locally CORRECT
  but unreachable (dependent on step 15).
- Judge h9; audit a9 PASS (double proof). NEW route — carried as WRONG;
  repair needs coordinator authorization.

### 19. ExceptionHandler.getLogcat — LONG, 16 steps — UNCLEAR
- Steps 1-4 CORRECT; step 5 FIXED (only the Balance tap continues,
  HomeFragment.java:470-471, null-account early return :454-455);
  steps 6-10 CORRECT (steps 7-8 INFERRED-delivery DialogFragment
  show/onCreateDialog acceptable under the consensus standard); step 11
  FIXED (requires getCurrency(mCurrencyId) == null — formatWithLocale only
  in that else-branch, AmountInputDialog.java:471); step 12 CORRECT;
  step 13 FIXED (requires base currency == null — showMessage only inside
  that branch, FormatUtilities.java:109-111); steps 14-15 CORRECT;
  step 16 UNCLEAR (getLogcat reached only inside the catch at
  log/ExceptionHandler.java:119 — only other call at :80 in a different
  caller; no printed trigger for Toast.makeText(...).show() throwing on
  this prefix — BadToken/finishing/destroyed searched, none; mContext
  null-guarded :111, main-looper handler, non-null string resource; not
  WRONG since a throw cannot be proved impossible, not CORRECT since no
  trigger is shown). Route UNCLEAR follows from step 16 alone (it does not
  depend on the INFERRED-delivery ruling).
- Judge h10; audit a10 PASS (agrees with the strict-rule caveat in
  substance: under strict printed-source-only, all three h10 routes would
  be UNCLEAR; strictly 6 of the 9 flagged steps are currently CORRECT and
  3 FIXED, so a strict step tally would read 33/5/0/10 — observation only,
  no judgment change under the adopted rule).

### 20. AboutFragment.getLogcat — LONG, 17 steps — CORRECT
- Steps 1-17 CORRECT. GROUP prefix verified (Help childItems null,
  MainActivity.java:927-928; item at :1118-1120; group-click Runnable);
  position == 0 guard (AboutTabAdapter.java:51-52) and mInstance == null
  guard (AboutFragment.java:54-56) verified; $3 anonymous-listener
  numbering confirmed by source-order counting (intervening
  OnClickListenerUrl instances are a named class and do not shift
  numbering).
- Judge h3; audit a3 PASS.

### 21. DefinedDateRange$1.<init> — LONG, 20 steps — CORRECT
- Steps 1-20 CORRECT. @GROUP drawer variant verified (Settings is a
  null-children group, MainActivity.java:924-925, :1107, case at :664-665);
  no EXTRA_FRAGMENT=PerDatabaseFragment so the default SettingsFragment
  shows (SettingsActivity.java:61-69); preference non-null guards hold
  (SettingsFragment.java:70-74; LookFeelPreferenceFragment.java:109-114);
  $1 is the sole anonymous class (CREATOR) in DefinedDateRange.java:56.
- Judge h4; audit a4 PASS.

### 22. QueryAccountBills.setReconciled — LONG, 12 steps — FIXED
- Steps 1-9 CORRECT (steps 5, 7, 8 INFERRED-delivery FragmentActivity
  dispatch / LoaderManager restart+delivery acceptable under the consensus
  standard; fragment attachment established by MainActivity.onCreate:238
  calling initHomeFragment, even though that step is not separately
  listed); step 10 FIXED (cursor != null guard, renderAccountsList);
  step 11 FIXED (>=1-row moveToNext() guard, showAccountTotals); step 12
  FIXED (columnCount == getAllColumns().length guard, setValueFromCursor
  at QueryAccountBills.java:210-221; satisfiable — the loader query is
  built from exactly getAllColumns(), HomeFragment.java:243-245).
- Judge h10; audit a10 PASS.

### 23. Budget.setName — LONG, 20 steps — FIXED
- Steps 1-10 CORRECT (drawer alignment verified from printed source:
  Budgets is index 6 in both the group list (menu_budgets at :1090-1093)
  and the child list (null at :890)); step 11 FIXED (only EDIT, not
  Delete/Copy, continues — BudgetListFragment.java:188-195, cast at
  :182-183); steps 12-15 CORRECT; step 16 FIXED (only the save item, not
  the Up/home item which just breaks to super, reaches onActionDoneClick
  — BudgetEditActivity.java:86-96); steps 17-20 CORRECT. (Steps 5, 11, 16
  INFERRED-delivery acceptable under the consensus standard.)
- Judge h10; audit a10 PASS.

### 24. NumericHelper.getNumberOfDecimals — PLAIN, 8 steps — CORRECT
- Steps 1-8 CORRECT. All guards present on the new dumps and matching
  source (widget-update FW :61/63/65-66; getCurrency non-null,
  CurrencyService.java:297-309, format only :309; currency non-null,
  FormatUtilities.java:157, :159-160). (Step 1 INFERRED-delivery AMS
  broadcast acceptable under the consensus standard; both framework
  endpoints printed.)
- Judge h7; audit a7 PASS (18/24 CORRECT steps spot-checked, 75%).

### 25. AccountRepository.first — PLAIN, 7 steps — CORRECT
- Steps 1-7 CORRECT. Guards present + matching (widget-update;
  defaultAccountId != null, :174; NOT_SET, :52 = -1). (Step 1
  INFERRED-delivery acceptable as in route 24.)
- Judge h7; audit a7 PASS.

### 26. MmxContentProvider.prepareQuery — PLAIN, 10 steps — FIXED
- Steps 1-2 CORRECT; step 3 FIXED (needs showPrerequisite()==false guard —
  onCreate returns early :184-186 before populateScheduledTransactions at
  :244 in the same method, no return strictly between :186 and :244;
  showPrerequisite :1478-1500 true only for tutorial-needed or
  no-database; the same systematic gap as route 15, independently
  corroborated by two helpers + two auditors); steps 4-10 CORRECT. All
  other brief-listed guards present + matching (populate :1234/:1236/
  :1248/:1259/:1261/:1264, entry-false + setting-true joint reading;
  NOT_SET, RecurringTransactionRepository.java:64; readable-database +
  Dataset, MmxContentProvider.java:385-388, :393, :395). (Step 8
  INFERRED-delivery ContentResolver routing acceptable under the consensus
  standard; destination independently corroborated: manifest provider
  authority, onCreate :103/:116/:133, Dataset.getUri :79-83, basepath
  "billsdeposits".)
- Judge h7; audit a7 PASS.

### 27. MmxContentProvider.logUpdate — PLAIN, 9 steps — CORRECT
- Steps 1-9 CORRECT. Guards present + matching (populate :1234/:1236/
  :1248/:1259/:1261/:1282; moveNextOccurrence :178-186/:192-196/:200-203/
  :240; update -> logUpdate :202/:204/:205); TABLE-guard satisfiability
  confirmed (RecurringTransactionRepository constructed with
  DatasetType.TABLE "billsdeposits_v1", registered in the provider's
  dataset list at MmxContentProvider.java:115; getObjectFromUri returns the
  map entry); Recurrence.valueOf nuance (throws InvalidParameterException
  at :66, null return commented out — service's null branch dead, but the
  reachable set is unchanged: returns a value or throws). No
  INFERRED-delivery steps (FW-SRC lifecycle + content-provider dispatch do
  not count). Citation correction (no verdict change): route step 9 note
  cites RecurringTransactionRepository.java:37 for the TABLE construction;
  the super(...) call is at :36 (constructor at :35).
- Judge h8; audit a8 PASS-WITH-CORRECTIONS (25/25 steps checked, 100%;
  citation :37 -> :36 only).

### 28. SyncPreferences.getUploadImmediately — PLAIN, 8 steps — CORRECT
- Steps 1-8 CORRECT. Joint condition recorded explicitly (and confirmed by
  a8, including the link the helper did not spell out): only a stored
  EMPTY (non-null) UID satisfies steps 3+4 — step 3 (uid null-or-empty
  triggers setInfoValue) + step 4 (exists = getInfoValue != null takes the
  update branch); null fails step 4 via the insert branch; non-empty fails
  step 3; getInfoValue returns cursor.getString(...), so a stored "" comes
  back non-null. updateResult != 0 guard + SyncManager guard chain
  (isSyncEnabled + remote path + !mAutoUploadDisabled + canSync) hold.
- Judge h8; audit a8.

### 29. DatabaseManager.getContext — PLAIN, 8 steps — WRONG (drawn prefix only)
- Steps 1-4 CORRECT; step 5 WRONG (guard contradiction, proved line by
  line by h5 and confirmed by a5: step-3 !showPrerequisite() requires a
  non-empty stored path whose file exists — MainActivity.java:184-187,
  :1478-1499, isDatabaseAvailable :1339-1349, same pref_database_path
  source (DatabaseSettings.java:32-35); step-5 fall-through requires that
  path empty OR its file missing — DatabaseManager.java:44-54; intervening
  methods checked individually: migrateRecentDatabases only clears/
  rebuilds the in-memory recent-files map (keeps the current entry, never
  calls setDatabasePath); handleIntent -> changeDatabase -> useDatabase
  throws BEFORE setDatabasePath if the file is not a valid database, and
  otherwise sets the path only to that valid, existing file (then restarts
  the activity); restoreInstanceState restores two booleans only;
  handleDeviceRotation pops the back stack / updates orientation only;
  the .emb + password nuance does not help — getDatabasePath :44-49 has no
  password check, so a .emb path that passed step 3 still early-returns at
  step 5); step 6 CORRECT (conditional on step 5); step 7 FIXED (evidence
  wording only: the file exists — same path as step 5 — so the dump's
  "(not found)" parenthetical is false; call + guard :90-97 verified,
  topology sound conditional on step 5); step 8 CORRECT (conditional on
  step 5).
- Valid non-shortest alternatives (in the graph AND in source, NOT drawn —
  the method is reachable, just not via the drawn prefix):
  backup-agent prefix (S_ENTRY -> MoneyManagerBackupAgentHelper.<init>
  [system_event env] -> onCreate -> getDatabasePath; manifest
  allowBackup + backupAgent :56-57; source :46; edges
  E3f865c2d/E58735491/E5385d81d; no prerequisite guard applies, so the
  fall-through is satisfiable) and broadcast prefix (SyncBroadcastReceiver
  -> SyncManager.triggerSynchronization -> getDatabasePath, with canSync
  + sync-interval guards, SyncBroadcastReceiver.java:36-45; edges
  E06f7fcf0/E607405ea/E930866bd; NOT SyncService.triggerSync — zero such
  edges exist in the graph).
- Fallback rationale (merger decision, for user/Yang review; full 32-edge
  repair design recorded in the merger fix log §9, NOT applied): the
  caller list is messy (6 uniformly contradicted callers + 1 mixed), and
  the full fix needs 6 dead-ends + a triggerSync prefix-partition (4
  MainActivity feeders -> @MAIN + mirrors of triggerSync's 10
  non-getDatabasePath outs + 10 plain re-asserts) + backup feeding
  variant — disproportionate in the B6 fix phase for a single sample route,
  with blast risk to the sync subtree. The task authorizes fallback when
  the caller list is messy. This is the ONLY first-draw WRONG route to
  fall back (the other 14 were fixed by the dispatcher splits).
- Judge h5; audit a5 PASS-WITH-CORRECTIONS (contradiction + both
  alternatives confirmed in the graph JSON).

### 30. MmxOpenHelper.<init> — PLAIN, 8 steps — CORRECT
- Steps 1-8 CORRECT. Guards present + matching (!showPrerequisite;
  intent + data + decode/factory; isValidDbFile + recent-databases add).
  Compatibility note recorded explicitly: the guards describe the
  already-configured-database + intent-file case, NOT cold start (cold
  start fails showPrerequisite at :184-187 and never reaches handleIntent
  at :210; showPrerequisite :1478-1495 true on tutorial-needed or
  no-valid-database).
- Judge h8; audit a8.

## Audit table (helper -> auditor -> verdict)

| Helper routes | Auditor | Audit verdict | Verdict changes |
|---|---|---|---|
| h1: DbModule / $1 / displayRunningBalances | a1 | PASS-WITH-CORRECTIONS | None (wording/citation only: $1 step 24 :320 -> :318-321; display step 16 guarded call + step 14 narrowing; display step 22 delete stale note) |
| h2: Passcode / Split insert / DateRange | a2 | PASS-WITH-CORRECTIONS | None (citation only: Passcode step 23 :45 -> :43) |
| h3: Core / Sync / About | a3 | PASS | None |
| h4: DefinedDateRange / Stock / CategoryList$2 | a4 | PASS | None |
| h5: onHandleWork / IncomeVsExpenses / getContext | a5 | PASS-WITH-CORRECTIONS | onHandleWork UNCLEAR -> CORRECT (steps 4, 7); IncomeVsExpenses steps 5, 8, 9 UNCLEAR -> CORRECT, step 10 UNCLEAR -> FIXED; route stays WRONG; getContext unchanged |
| h6: RecurringList / Tutorial / WidgetConfigure | a6 | PASS-WITH-CORRECTIONS | None (citation only: Recurring step 3 :1478-1482 -> :1478-1489) |
| h7: NumericHelper / AccountRepository / prepareQuery | a7 | PASS | None |
| h8: logUpdate / getUploadImmediately / MmxOpenHelper | a8 | PASS-WITH-CORRECTIONS | None (citation only: logUpdate step 9 note :37 -> :36) |
| h9: $UpdateType / getContentValues / getNumberOfShares | a9 | PASS | None |
| h10: ExceptionHandler / QueryAccountBills / Budget | a10 | PASS | None |

No helper output was FAILed; no route required re-judging. All 10 audits
are PASS or PASS-WITH-CORRECTIONS with the corrections incorporated above.

## FIXED-step inventory (24 steps — guard/wording corrections only, no topology change)

- $1 step 24 (citation :321); displayRunningBalances steps 16 (guarded
  call), 22 (stale note); Stock.setSymbol step 8 (newInstance guard);
  Passcode step 23 (citation :43); $UpdateType steps 10 (wording), 14
  (Morningstar guard); getContentValues step 11 (case 2);
  CategoryList$2 steps 15 (DELETE guard), 16 ($2 wording);
  IncomeVsExpenses steps 3 (!showPrerequisite), 10 ("YEARS loader");
  RecurringList step 3 (showPrerequisite guard); WidgetConfigure step 3
  (EXTRA_APPWIDGET_ID); ExceptionHandler steps 5 (Balance tap), 11
  (getCurrency null), 13 (base currency null); QueryAccountBills steps
  10 (cursor non-null), 11 (moveToNext), 12 (column count);
  Budget steps 11 (EDIT only), 16 (save item only); prepareQuery step 3
  (showPrerequisite guard); getContext step 7 (file-exists wording).
- Systematic guard gap found twice independently (h6 + h7, confirmed by a6
  + a7): the MainActivity.onCreate -> :244 populate edge lacks a
  showPrerequisite()==false guard, affecting routes 15 and 26. Recorded
  here as FIXED steps; applying the guard to the graph is a follow-up
  (not done in this task — STOP after the final table).
- The redraw-wave FIXED guards are NOT applied to the graph in this task.
  They are recorded verdicts in this table. Applying them (and the
  §9 getContext repair, and the route-12 Sync re-feed, and the routes 8 +
  18 recipient-identity repairs) is future work requiring coordinator
  authorization, followed by a fresh redraw + re-judge — not a silent
  edit after an audited table.

## First-draw routes NOT in the redrawn sample (6)

- WRONG-fixed, fix-phase reprints verified (node-for-node at apply time,
  recorded in the merger fix log): WatchlistItemsFragment.getAccount (14
  steps via own context-menu path), EditTransactionCommonFunctions
  .resetCategory (17 steps via @CHECKING), BudgetListFragment.onLoaderReset
  (19 steps via @GROUP + variant onCreateView), TransactionStatuses.<init>
  (15 steps via search/all-data route). Their fixes stand; they are NOT
  in the final sample and are NOT re-judged here.
- UNCLEAR in the first draw, no fix applied, not resampled:
  SqlRepositoryBase.first, HomeAccountsExpandableAdapter.getAccountData.
  Their new paths are unjudged; nothing is claimed about them.

## STOP — audit-gated push (NOT pushed yet)

This table completes the B6 redraw + judging work. Per the task, STOP here
for independent fix audits — the B6 package is NOT pushed yet. The push,
then B7 logs, then D1/D3/D7, then F1-readiness come after those audits
PASS. The B6 push manifest (for the audit-gated push) is:

- graphs/MMEX/graph_def.py (603,512 B)
- graphs/MMEX/graph_def_mod/01.py (596,054 B)
- graphs/MMEX/graph_def_mod/02.py (145,852 B)
- graphs/MMEX/graph_def_mod/03.py (NEW, 109,130 B — all B6 fix edges)
- graphs/MMEX/scratch/sample_30.txt (first-draw sample, 2,093 B)
- graphs/MMEX/scratch/sample_30_final.txt (redrawn sample, 2,064 B)
- graphs/MMEX/scratch/route_table.md (this file, 33,298 B)
- graphs/MMEX/scratch/route_print/ (first-draw dumps, 30 files, 500,592 B)
- graphs/MMEX/scratch/route_print_final/ (redrawn dumps, 30 files, 435,461 B)
- Total ~2.4 MB; every file < 900 KB. EXCLUDED: out/ (never pushed;
  rebuilt by CI), __pycache__/ (build artifacts), the merger work-dir
  documents (fix_log.md, MERGER_REPORT.md, dump_routes.py,
  redraw_wave1_notes.md — available for coordinator review, not in the
  push unless the coordinator directs). ABSENT claims for the new/changed
  paths MUST be re-verified with the connector's `ref` parameter (not
  `branch`) immediately before any push call, under the push-lock protocol.
- Open follow-ups for the coordinator (NOT started here): (1) Sync
  re-feed (route 12 defect — @DOWNLOAD from the triggerSync
  remote-only-modified branch + subscriber-open prefix); (2) routes 8 + 18
  recipient-identity repairs (WatchlistFragment event delivery;
  Calculator result recipient); (3) the showPrerequisite guard on the
  onCreate -> :244 edge (routes 15 + 26 FIXED steps); (4) the §9
  getContext 32-edge repair design (recorded, not applied); (5) B7 logs +
  D1/D3/D7 device prep from THIS final sample only. Each repair needs a
  fresh redraw + re-judge after it lands — the rate above (0.5357) is the
  audited rate for the CURRENT graph, not a promise about a repaired one.
