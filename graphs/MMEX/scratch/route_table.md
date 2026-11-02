# MMEX final route table (redrawn sample final2, judged fresh, audit PASS)

- Sample: `graphs/MMEX/scratch/sample_30_final2.txt` — 30 of 3430
  reachable methods, 344 distinct edges, seed 20261025, drawn with
  `python3 -I tools/verify_sample.py MMEX 30 20261025` AFTER all
  post-B6 repairs (routes 8+18, showPrerequisite guard, section-9
  getContext, Sync re-feed v2, route 14). Staged in the tree as
  graphs/MMEX/scratch/route_table.md with the sample and the 30
  route prints beside it.
- Build at redraw time (private rebuild of the final tree sources):
  4270 methods, 3430 REACHABLE / 840 UNREACHABLE, 8441 edges,
  errors 0, warnings 0.
- Judging: every step judged fresh on the final2 prints in
  `graphs/MMEX/scratch/route_print_final2/` against printed source.
  B6 verdicts were NOT carried over, even for retained methods at
  identical step counts. Full per-step evidence is in the merger work
  dir (helper/final-judge/JUDGING.md, audit PASS in
  audit/final-judge/AUDIT.md).
- Route verdict rule: WRONG if any step WRONG; else UNCLEAR if any
  step UNCLEAR; else FIXED if any step FIXED; else CORRECT.

## Final tally

- Routes: CORRECT 20 / FIXED 8 / WRONG 0 / UNCLEAR 2 = 30.
- Steps: correct 433 / fixed 14 / wrong 0 / unclear 3 = 450.
- Final error rate = (fixed + wrong) / (correct + fixed + wrong)
  = (8 + 0) / (20 + 8 + 0) = 8 / 28 = 0.2857.
  (UNCLEAR excluded per the formula. The B6 rate 0.5357 is NOT
  carried forward; this rate is computed from this table only.)

## Per-route verdicts (in sample order)

### 1. DbModule_ProvideSqlBriteFactory.get — NONSTD, 27 steps — CORRECT
- Steps 1-27 CORRECT. Drawer @GROUP prefix verified (Budgets group,
  null children, item menu_budgets); Dagger Lazy/Provider tail
  (steps 26-27) INFERRED but topologically sound (DbModule.java:53 is
  the file's only SqlBrite provider; databaseLazy :85, get() :278).

### 2. SplitCategoriesActivity$1.<init> — NONSTD, 24 steps — FIXED
- Steps 1-23 CORRECT; step 24 FIXED (citation only: the listener is
  instantiated at SplitCategoriesActivity.java:321, not the cited
  :320 (setMessage); builder :318, listener :321; $1 identity holds).
  @CHECKING host, @SPLIT calculator (requestId + 1000 offset), @AMOUNT
  return verified, incl. RESULT_OK + data guard (:129) and requestCode
  >= 1000 guard (:142).

### 3. InvestmentTransactionEditActivity.onActivityResult — NONSTD, 25 steps — CORRECT
- Steps 1-25 CORRECT. Plain method's REACHABLE comes via the
  first_variant mapping to the @NUM_SHARES variant handlers: the
  methods.csv shortest_path ends at onActivityResult@NUM_SHARES.
  Portfolio prefix, numSharesView tap (@OnClick :211, generated
  binding INFERRED), Calculator launched with REQUEST_NUM_SHARES (= 1),
  equals key -> returnResult (setResult :443, finish :444) -> 
  onActivityResult@NUM_SHARES (guard requestCode == NUM_SHARES and
  RESULT_OK with data non-null, :119-158).

### 4. AllDataListFragment.displayRunningBalances — NONSTD, 24 steps — FIXED
- Steps 1-15 CORRECT; step 16 FIXED (guarded call: loadTransactions()
  at :587 only inside if(result) at :576; status cases :555-569,
  default :570-573 sets result false; tapped item must be a
  transaction-status item); steps 17-24 CORRECT (loader delivery,
  AsyncTask chain with FW-SRC evidence, EventBus post at
  CalculateRunningBalanceTask2.java:99 -> onEvent -> 
  displayRunningBalances).

### 5. Passcode.savePasscode — INFERRED, 29 steps — UNCLEAR
- Steps 1-20 CORRECT; step 21 UNCLEAR (PasscodeActivity onClick ->
  fragment onActivityResult, first visit — androidx FragmentActivity
  result dispatch routing to the requesting fragment is not in fw_src;
  platform dispatch :7260-7293 serves the android.app.Fragment
  registry only); step 22 CORRECT; step 23 CORRECT (citation now
  :43, B6 FIXED item resolved); steps 24-26 CORRECT; step 27 UNCLEAR
  (same dispatch gap, second/REINSERT visit; its guard correctly
  includes the editTextPasscode5 precondition); steps 28-29 CORRECT.
  GROUP prefix + @REINSERT chain verified fresh.

### 6. SplitRecurringCategoriesRepository.insert — INFERRED, 23 steps — CORRECT
- Steps 1-23 CORRECT. @RECURRING chain verified (drawer group tap,
  showFragment chain, FAB, editor, save case :171); split guard matches
  exactly (RecurringTransactionEditActivity.java:571-580:
  hasSplitCategories, id == null OR == NOT_SET, then insert).

### 7. StockHistoryRepository$UpdateType.<init> — INFERRED, 21 steps — CORRECT
- Steps 1-21 CORRECT. Watchlist prefix (INVESTMENT guard), Update-
  prices dialog OK ($4.onClick :463-476), Morningstar guard present
  in this print (SecurityPriceUpdaterFactory.java:38-42) — B6 FIXED
  step 14 resolved; step 10 wording FIXED item also resolved (plain
  lifecycle statement, no "attached" gap). RxJava doOnNext (step 16)
  INFERRED, flagged, acceptable under the consensus standard.

### 8. CurrencyRepository.saveExchangeRate — INFERRED, 20 steps — FIXED
- Steps 1-10 CORRECT; step 11 FIXED (only the Update-exchange-rate
  item, case 2 at CurrencyListFragment.java:264-266, continues to the
  :266 call; the print lists all four menu items without narrowing);
  steps 12-20 CORRECT (FixerService dispatch, Retrofit onResponse
  INFERRED, EventBus post :120 -> onEvent while the currency list is
  started, direct calls :357, :99, :490).

### 9. CategoryListFragment$2.onClick — STATE, 16 steps — FIXED
- Steps 1-14 CORRECT; step 15 FIXED (needs DELETE-case guard,
  CategoryListFragment.java:213-217; call at :217 inside case DELETE
  :216); step 16 FIXED, not WRONG (by anonymous-class file order, $2 =
  confirm-delete OK listener (:483, deletes the row, toasts on 0 rows,
  restarts loader), $3 = Cancel listener (:500, dialog.cancel()); the
  print's "Cancel" description is $3, not $2; wording only, no edge
  change).

### 10. Core.resolveColorAttribute — STATE, 18 steps — CORRECT
- Steps 1-18 CORRECT. Child-click prefix verified (Payee is the first
  entry of childReports, MainActivity.java:898) + Payee-specific
  variant chain (PayeesReportActivity -> PayeeReportFragment ->
  BaseReportFragment onCreate/onActivityCreated/startLoader/
  onCreateLoader@Payee -> PayeeReportAdapter.bindView ->
  resolveColorAttribute at PayeeReportAdapter.java:75); no
  CategoriesReport leak.

### 11. DatabaseMetadataFactory.getInstance(String,String) — STATE, 13 steps — FIXED
- Steps 1-8 CORRECT; step 9 FIXED (citation only: triggerSync flags
  are at SyncService.java:177-178, branch test at :206, not the cited
  :180-181 / :207-210; claims true, citations off — follow-up
  correction flagged in the fix log, not applied here); steps 10-13
  CORRECT (handler delivery with MainActivity-started guard
  :141/:146 and Activity-context Messenger guard :209-212, then
  direct calls :529, :376).

### 12. IncomeVsExpensesListFragment$1.run — ENV, 14 steps — FIXED
- Steps 1-2 CORRECT; step 3 FIXED (guard annotation missing on the
  :238 edge E5d5a9c2f: gate :184-187 plus zero returns :188-243
  proves !showPrerequisite() whenever :238 executes, so topology is
  sound, but the graph edge still carries no guard — the :238 guard
  follow-up is separate and NOT claimed as applied); step 4 CORRECT;
  steps 5-14 CORRECT (card tap, IncomeVsExpensesActivity, list
  fragment, sealed YEARS -> startLoader -> REPORT chain with ids
  Ebfbf7e82, E6df1962a, E428631c7, Ed2e1013e, E645f3932, Ef27e0542;
  dual-panel guard :188 and null-data return :171). The B6 step-11
  WRONG is repaired by this chain.

### 13. RecurringTransactionIntentService.onHandleWork — ENV, 7 steps — CORRECT
- Steps 1-7 CORRECT. BOOT_COMPLETED receiver, setAlarm, AlarmManager
  repeating broadcast PendingIntent (INFERRED, flagged), receiver
  onReceive (setting-on guard), enqueueWork, JobIntentService delivery
  (INFERRED, flagged; JOB_ID 1001).

### 14. RecurringTransactionListActivity.onActivityResult — ENV, 9 steps — CORRECT
- Steps 1-9 CORRECT. Step 3 CORRECT now: the shared edge is E00ecbc65
  with the full !showPrerequisite() guard printed (:184-187;
  definition :1478-1499) — the B6 FIXED item is resolved by the
  applied showPrerequisite guard. Notification PendingIntent tap
  (step 7, INFERRED, flagged) and passcode STATE (step 9, :50-56)
  verified.

### 15. TutorialActivity.onOptionsItemSelected — ENV, 8 steps — CORRECT
- Steps 1-8 CORRECT. showPrerequisite -> showTutorial (:1481),
  first-run STATE (getShowTutorial default true), tutorial screen,
  settings item (action_settings :113, returns true :114; hardware
  menu key ENV). Step 8 INFERRED androidx dispatch passthrough
  acceptable under the consensus standard.

### 16. SingleAccountWidgetConfigureActivity.saveTitlePref — ENV, 4 steps — FIXED
- Steps 1-2 CORRECT; step 3 FIXED (needs a valid EXTRA_APPWIDGET_ID
  — listener wired at :65, then :76-78 finish/return if mAppWidgetId
  == INVALID_APPWIDGET_ID; the print states no such guard); step 4
  CORRECT.

### 17. Authenticator.addAccount — ENV, 4 steps — CORRECT
- Steps 1-4 CORRECT. System Settings Add-account flow (ENV outside
  package; authenticator.xml:20, accountType example.com; manifest
  service :455-465, exported=false); service onCreate (:33-37),
  onBind (:42-45, returns getIBinder()), binder stub dispatches
  addAccount (INFERRED, flagged; Authenticator.java:43-46, returns
  null).

### 18. CurrencyRepositorySql_Factory.get — LONG, 17 steps — CORRECT
- Steps 1-17 CORRECT. Account-edit prefix (Edit item guard :462),
  initial-balance calculator (AMOUNT :307), displayFormattedAmount ->
  getFormattedAmount, Dagger chain (steps 15-17, INFERRED generated
  factories with bytecode-offset evidence: Lazy get, provider offset
  25, CurrencyService_Factory -> CurrencyRepositorySql_Factory).

### 19. ExceptionHandler.getLogcat — LONG, 16 steps — UNCLEAR
- Steps 1-4 CORRECT; step 5 FIXED (only the Balance tap continues,
  HomeFragment.java:470-471, null-account early return :454-455);
  steps 6-10 CORRECT (steps 7-8 INFERRED DialogFragment show/
  onCreateDialog acceptable under the consensus standard); step 11
  FIXED (requires getCurrency(mCurrencyId) == null — formatWithLocale
  only in that else-branch, AmountInputDialog.java:471); step 12
  CORRECT; step 13 FIXED (requires base currency == null —
  showMessage only inside that branch, FormatUtilities.java:109-111);
  steps 14-15 CORRECT; step 16 UNCLEAR (getLogcat reached only inside
  the catch at log/ExceptionHandler.java:119 — only other call at :80
  in a different caller; no printed trigger for Toast.makeText(...).
  show() throwing on this prefix — BadToken/finishing/destroyed
  searched, none; mContext null-guarded :111, main-looper handler,
  non-null string resource; not WRONG since a throw cannot be proved
  impossible, not CORRECT since no trigger is shown).

### 20. AboutFragment.getLogcat — LONG, 17 steps — CORRECT
- Steps 1-17 CORRECT. GROUP prefix verified (Help childItems null,
  MainActivity.java:927-928; item at :1118-1120; group-click Runnable);
  position == 0 guard (AboutTabAdapter.java:51-52) and mInstance ==
  null guard (AboutFragment.java:54-56) verified; $3 anonymous-
  listener numbering confirmed by source-order counting.

### 21. DefinedDateRange$1.<init> — LONG, 20 steps — CORRECT
- Steps 1-20 CORRECT. @GROUP drawer variant verified (Settings is a
  null-children group, MainActivity.java:924-925, :1107, case at
  :664-665); no EXTRA_FRAGMENT=PerDatabaseFragment so the default
  SettingsFragment shows (SettingsActivity.java:61-69); preference
  non-null guards hold (SettingsFragment.java:70-74;
  LookFeelPreferenceFragment.java:109-114); $1 is the sole anonymous
  class (CREATOR) in DefinedDateRange.java:56.

### 22. QueryAccountBills.setReconciled — LONG, 12 steps — FIXED
- Steps 1-9 CORRECT (onStart/onResume/startLoaders/onCreateLoader/
  onLoadFinished, loader-id guard :288-291); step 10 FIXED (cursor !=
  null guard, renderAccountsList); step 11 FIXED (>=1-row moveToNext()
  guard, showAccountTotals); step 12 FIXED (columnCount ==
  getAllColumns().length guard, setValueFromCursor at
  QueryAccountBills.java:210-221; satisfiable — the loader query is
  built from exactly getAllColumns()).

### 23. DateRange.<init>() — LONG, 24 steps — CORRECT
- Steps 1-24 CORRECT. Drawn path is @RESTORED -> createFromParcel (not
  the fresh-Bundle path); stratum change STATE -> LONG is a sampler
  effect only, steps identical to B6. Restored-filter non-null guard
  (TransactionFilter.java:33; DateRange.java:27-29); FW-SRC
  Bundle/Parcel unparcel -> creator chain printed (Bundle.java:
  938-939, Parcel.java:2744-2745, :2841-2851).

### 24. NumericHelper.getNumberOfDecimals — PLAIN, 8 steps — CORRECT
- Steps 1-8 CORRECT. All guards present on the new dumps and matching
  source (widget-update FW :61/63/65-66; getCurrency non-null,
  CurrencyService.java:297-309, format only :309; currency non-null,
  FormatUtilities.java:157, :159-160). Step 1 INFERRED AMS broadcast
  acceptable under the consensus standard; both framework endpoints
  printed.

### 25. AccountRepository.first — PLAIN, 7 steps — CORRECT
- Steps 1-7 CORRECT. Guards present + matching (widget-update;
  defaultAccountId != null, :174; NOT_SET, :52 = -1). Step 1
  INFERRED-delivery acceptable as in route 24.

### 26. MmxContentProvider.prepareQuery — PLAIN, 10 steps — CORRECT
- Steps 1-10 CORRECT. Step 3 CORRECT now: shared edge E00ecbc65 with
  the full !showPrerequisite() guard printed — the B6 FIXED item is
  resolved by the applied showPrerequisite guard. All other
  brief-listed guards present + matching (populate :1234/:1236/
  :1248/:1259/:1261/:1264, NOT_SET :64, readable-database + Dataset
  :385-388, :393, :395). Step 8 INFERRED ContentResolver routing
  acceptable under the consensus standard.

### 27. MmxContentProvider.logUpdate — PLAIN, 9 steps — CORRECT
- Steps 1-9 CORRECT. Step 3 CORRECT: same E00ecbc65 guard as route 26,
  closing the B6 unrecorded step-3 text gap. Guards present +
  matching (populate :1234/:1236/:1248/:1259/:1261/:1282;
  moveNextOccurrence :178-186/:192-196/:200-203/:240; update ->
  logUpdate :202/:204/:205; TABLE guard :202/:204, dataset
  "billsdeposits_v1" registered at MmxContentProvider.java:115).

### 28. SyncPreferences.getUploadImmediately — PLAIN, 8 steps — CORRECT
- Steps 1-8 CORRECT. Joint condition recorded explicitly: only a
  stored EMPTY (non-null) UID satisfies steps 3+4 — step 3 (uid
  null-or-empty triggers setInfoValue) + step 4 (exists =
  getInfoValue != null takes the update branch); null fails step 4
  via the insert branch; non-empty fails step 3. updateResult != 0
  guard + SyncManager guard chain (isSyncEnabled + remote path +
  !mAutoUploadDisabled + canSync) hold.

### 29. AppSettings.getPreferences — PLAIN, 8 steps — CORRECT
- Steps 1-8 CORRECT. handleIntent after the prerequisite check passes
  (step 3 guard !showPrerequisite() :184-187); intent/data/exception
  guards (step 4, :1186/:1189/:1192-1198); direct calls :546, :210,
  :38, :90.

### 30. RecentDatabasesProvider.toJson — PLAIN, 8 steps — CORRECT
- Steps 1-8 CORRECT. migrateRecentDatabases (:190, after the
  :184-187 gate) -> getCurrent (:1523) -> add (:130) -> add (:81) ->
  save (:75) -> toJson (:171); all calls unconditional in their
  method bodies once reached.

## Targeted re-judges (NOT table rows — see JUDGING.md)

- StockHistoryRepository.getContentValues — 21 steps — FIXED (step 13:
  only the Edit-price item continues).
- Stock.getNumberOfShares — 20 steps — CORRECT (pre-fill route,
  :213, no calculator delivery involved).
- SyncPreferenceFragment.onEvent — 11 steps — FIXED (step 9 citation
  only; step 11 delivery edge E75720ed3 CORRECT, session STATE
  subscriber-open + U+2019 guard verified).
- DatabaseManager.getContext — 12 steps — FIXED (step 8
  menu_open_database case guard, step 9 catch-branch guard unstated;
  FileStorageHelper.java:60-70, call at :69 verified).
- MainActivity.onEvent(DbFileDownloadedEvent) — 11 steps — FIXED
  (step 9 citation only).
- WatchlistFragment.onPriceDownloaded — 18 steps — CORRECT.

## WRONG-route statement

No route in this table is WRONG, so no remaining graph fix and no
tools edit is specified here. FIXED steps above are guard/wording/
citation annotations for the merger to consider at B7 time.
