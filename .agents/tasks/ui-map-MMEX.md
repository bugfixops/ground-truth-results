# MMEX v2024.06.14 — UI map and modeling plan (read-only investigation)

## Summary

- **The baseline was stuck at the "no database" gate.** Both tools passed the tutorial, then `MainActivity.showPrerequisite()` sent every launch to `SelectDatabaseActivity` because no database path was stored (J/home/MainActivity.java:184-187, 1338-1349, 1478-1500). Its two buttons open the Storage Access Framework picker of DocumentsUI (`ACTION_CREATE_DOCUMENT`/`ACTION_OPEN_DOCUMENT`, J/core/docstorage/FileStorageHelper.java:56-87). That picker is in another package, so Monkey/APE's `-p com.money.manager.ex` filter blocks it and the app only ever receives `RESULT_CANCELED` (FW-MEMORY; matching coverage below). `FileStorageHelper.createDatabase/selectDatabase`, `DatabaseManager`, `MmxOpenHelper` and every screen behind `MainActivity` have 0 coverage.
- **What a harness must prepare:** set `prefshowtutorial=false`, give it a usable `.mmb` database (pref `databasepath`), and register that database in the recent-DB list with a **non-empty `remotePath`**. Without the last item the transaction editor crashes (J/transactions/EditTransactionCommonFunctions.java:735-736). The simplest way is to go through the real SAF "Create database" flow once by hand or with UIAutomator, add sample data, and snapshot. The APK is `debuggable=true`, so `run-as` seeding also works (§2.5).
- **Size:** 4269 methods (JaCoCo, JacocoInstrument excluded), of which 616 are in generated classes (Dagger, ButterKnife, Icepick, Parceler, DataBinding). 825 class files, 408 Java sources, about 60k lines. 40 concrete activities, about 50 fragment classes (10 preference fragments, 5 DialogFragments), about 30 AlertDialog sites, 9 context menus (8 live), 1 action mode, 10 preference screens, 1 drawer, 2 pagers, 4 widgets.
- **Proposed page set:** about 140 base pages, including 21 `_PAUSED` pages and the pseudo pages. With the `@CONTEXT` variants it is about 210 nodes (§3.4).
- **Proposed areas (8):** SHELL (500 methods), TXN (858), MASTER (317), INVEST (337), BRS (346), SETSYNC (509), DATA (663), KIT (739). Every class file is assigned; there are no leftovers (§6).
- **Unreachable candidates:** about 32 source classes have no reference at all. Others are dead through commented-out callers (sync start/stop events, CSV export menu, `EditPriceDialog`, WorkManager workers, sync adapter trigger). Some are dead by build config or API level (`ScreenTree`/`SysLogTree` in a debug build, `SimpleCrypto` on API > 23). Some are environment-gated (SMS receiver without `RECEIVE_SMS`, defunct price/rate web APIs, widgets, launcher shortcut). There are also 8 phantom manifest components with no class (§5).
- **Baseline coverage by area (methods hit by either tool):** SHELL 83/500, SETSYNC 50/509, KIT 95/739, DATA 39/663, MASTER 3/317, BRS 2/346, TXN 0/858, INVEST 0/337. Monkey-only: 10 methods, all in the tutorial. APE-only: 10 methods, toasts/error events plus one settings listener (§7).

---

## 0. Scope, sources, labels

- App folder: `/Users/darshan/Desktop/yang/work/final_java_only/MMEX/app/`. Compiled classes: `MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/` (825 `.class` files, 3 of them `JacocoInstrument`). Sources: `MMEX-#v2024.06.14/app/src/main/java/` (408 `.java` files). The only source file without a class is `currency/MmxExchangeRateProvider.java`, which is fully commented out.
- Path abbreviations used below:
  - `J/` = `.../MMEX-#v2024.06.14/app/src/main/java/com/money/manager/ex/`
  - `RES/` = `.../app/src/main/res/`
  - `MAN` = `.../app/src/main/AndroidManifest.xml`
  - `APKMAN` = the binary `AndroidManifest.xml` inside `MMEX-v2024.06.14-rebuilt.apk`, decoded read-only with a small Python AXML reader. There is **no merged manifest under `build/intermediates`**: only `javac/` exists. APKMAN is the real merged manifest and matches MAN plus library components.
  - `MK` / `APE` = `monkey/report/report.xml` / `ape/report/report.xml`.
- Build facts: `app/build.gradle` has no product flavors (commented out). `debug.setRoot('build-types/debug')` points at a folder that does not exist. `src/beta` holds only icons and an empty manifest, and `beta` is not a build type, so only `src/main` is compiled. `minSdk 22`, `targetSdk 31` (APKMAN `uses-sdk`). `debuggable=true` (APKMAN `application`). `testCoverageEnabled true`.
- Labels: `SRC` (read in app source/resources), `FW-MEMORY` (Android/Monkey behaviour recalled, not checked against AOSP; no framework source was available), `INFERRED`, `UNVERIFIED`.

---

## 1. Entry points (merged manifest = APKMAN; line numbers from MAN)

### 1.1 Application and providers (created at process start)

| Component | Exported | Notes | Evidence |
|---|---|---|---|
| `MmexApplication` (extends `MultiDexApplication`) | – | `onCreate`: font, Timber (`DebugTree` because `BuildConfig.DEBUG`), Dagger `DaggerMmxComponent`, Amplitude analytics (opt-out unless `pref_anonymous_usage`). `backupAgent=.core.MoneyManagerBackupAgentHelper`, `allowBackup=true`, theme `Theme.Splash`, `debuggable=true` | MAN:54-62; J/MmexApplication.java:114-157, 134-140, 200-205 |
| `.MmxContentProvider` | false | authority `com.money.manager.ex.provider`. `onCreate` registers 21 datasets in a `UriMatcher`. The DB is opened lazily on the first query/insert/update/delete | MAN:375-378; J/MmxContentProvider.java:99-138, 358-362, 372-390 |
| `androidx.core.content.FileProvider` | false | `com.money.manager.ex.fileprovider`, used to share QIF/CSV/price exports | MAN:380-388 |
| `.sync.adapter.StubSyncProvider` | false | `com.money.manager.ex.datasyncprovider`, `syncable=true` (sync-adapter stub) | MAN:390-394 |
| Library: `androidx.startup.InitializationProvider` (WorkManager init), `com.squareup.picasso.PicassoProvider` | false | library code, out of scope | APKMAN |

FW-MEMORY: content providers are created (`onCreate`) after `Application.attachBaseContext` and before `Application.onCreate`. The baseline hit `MmxContentProvider.onCreate` and `StubSyncProvider.onCreate` on every start.

### 1.2 Activities

`launchMode` is standard and there is no `configChanges` unless listed. No activity uses a dialog theme. All `MmxBaseFragmentActivity` subclasses set the light or dark theme at runtime (J/common/MmxBaseFragmentActivity.java:56-60, 256-262; J/core/UIHelper.java:175-191).

| Activity | Exported | Intent filters / attributes | Started in-app by | MAN |
|---|---|---|---|---|
| `.home.MainActivity` | true | MAIN/LAUNCHER (+ Samsung MULTIWINDOW_LAUNCHER). VIEW + DEFAULT + BROWSABLE, `scheme=file`, `mimeType=*/*`, `pathPattern .*\.mmb` / `.*\.emb` (multi-dot variants). meta-data `android.app.shortcuts` → `@xml/shortcuts` | launcher; Tutorial; SelectDatabase; widgets; sync; restart | 135-179 |
| `.transactions.CheckingTransactionEditActivity` | true | EDIT, INSERT (no category, no data) | Home FAB, account list, recurring "enter", widgets, launcher shortcut (`RES/xml-v25/shortcuts.xml:19-32`, explicit INSERT) | 180-189 |
| `.PayeeActivity` | true | PICK, EDIT | transaction editor, search (PICK) | 190-197 |
| `.account.AccountListActivity` | true | PICK, EDIT | **no in-app starter** (only result handling at J/transactions/EditTransactionCommonFunctions.java:869-871) | 198-203 |
| `.common.CategoryListActivity` | true | PICK, EDIT | editor, split, search (PICK) | 204-209 |
| `.currency.list.CurrencyListActivity` | true | PICK, EDIT | drawer (EDIT), account edit and per-DB settings (PICK) | 210-215 |
| `.about.AboutActivity` | false | – | drawer About, Settings › Info | 216-218 |
| `.currency.CurrencyEditActivity` | true | EDIT, INSERT | currency list | 219-226 |
| `.account.AccountEditActivity` | true | EDIT, INSERT | Home (welcome button, context menu), account list, txn-list header, watchlist header, filter dialog | 227-234 |
| `.recurring.transactions.RecurringTransactionListActivity` | false | – | recurring notification only | 235 |
| `.recurring.transactions.RecurringTransactionEditActivity` | true | EDIT, INSERT | recurring list | 236-243 |
| `.settings.SettingsActivity` / `GeneralSettingsActivity` / `LookFeelSettingsActivity` / `BehaviourSettingsActivity` / `InvestmentSettingsActivity` / `BudgetSettingsActivity` / `SecuritySettingsActivity` / `DatabaseSettingsActivity` | false | – | drawer Settings, Settings fragment, Tutorial "Close" (General) | 244-267 |
| `.settings.SyncPreferencesActivity` | true | `launchMode=singleTask`. VIEW + DEFAULT + BROWSABLE `scheme=com.money.manager.ex` (old OAuth redirect; `onNewIntent` only logs) | Settings › Synchronization | 268-280; J/settings/SyncPreferencesActivity.java:41-56 |
| `.PasscodeActivity` | true | `com.money.manager.ex.custom.intent.action.REQUEST_PASSWORD` | MainActivity.onStart, security settings, recurring list | 281-285 |
| `.reports.IncomeVsExpensesActivity` / `PayeesReportActivity` / `CategoriesReportActivity` | false | – | drawer Reports; Home income/expense card (`android:onClick`) | 286-294 |
| `.search.SearchActivity` | false | – | drawer Search, Home search menu, "view transactions", reports | 295-297 |
| `.transactions.SplitCategoriesActivity` | false | – | transaction / recurring editors | 298-300 |
| `.HelpActivity` | true | `...WEB_VIEW_RAW_FILE`, `...WEB_VIEW_URL`, DEFAULT, `file`, `*/*` | `case R.id.menu_help` only, and **no drawer item has that id** (J/home/MainActivity.java:685-687 vs 1046-1125) | 301-313 |
| `.tutorial.TutorialActivity` | false | theme `@android:style/Theme.NoTitleBar.Fullscreen`, `screenOrientation=portrait`, `configChanges=keyboardHidden\|orientation\|screenSize` | MainActivity.showTutorial | 314-319 |
| `.currency.CurrencyChartActivity` | false | `screenOrientation=landscape` | currency context menu | 320-323 |
| `.budget.BudgetsActivity` | false | – | drawer Budgets | 324-326 |
| `.widget.SingleAccountWidgetConfigureActivity` | true | `APPWIDGET_CONFIGURE` (but the widget XML's `android:configure` is commented out: RES/xml/widget_info_single_account.xml:27-28) | none in-app (J/widget/SingleAccountWidget.java:83 only mentions it) | 327-331 |
| `.investment.InvestmentTransactionEditActivity` | false | – | portfolio, watchlist | 332-334 |
| `.common.WebViewActivity` | false | – | **none** | 335-337 |
| `.database.PasswordActivity` | false | – | SelectDatabase, drawer open/create/recent DB, VIEW intent | 348-350 |
| `.investment.PortfolioActivity` | false | – | **none** | 351-353 |
| `.budget.BudgetEditActivity` | false | – | budget list | 357 |
| `.currency.recycler.CurrencyRecyclerListActivity` | false | – | **none** (call commented out at J/home/MainActivity.java:645) | 359 |
| `.home.SelectDatabaseActivity` | false | – | MainActivity gate | 368 |
| `.common.CalculatorActivity` | false | – | `Calculator` builder (editors, search, price) | 369-371 |
| `.investment.PriceEditActivity` | false | – | watchlist context menu "Edit price" | 500 |
| **Phantom (declared, no class in APK):** `.assetallocation.editor.AssetAllocationEditorActivity`, `.assetallocation.AssetClassEditActivity`, `.assetallocation.SecurityListActivity`, `.assetallocation.AssetAllocationReportActivity`, `.assetallocation.list.AssetClassListActivity`, `.assetallocation.overview.AssetAllocationOverviewActivity` | false | – | none | 338-347, 354-356, 358, 360-367 |
| Library: `com.github.pedrovgs.lynx.LynxActivity` (logcat viewer, from About), `com.mikepenz.aboutlibraries.ui.LibsActivity` | (default) | library code, in the app package | AboutFragment "logcat" | APKMAN; J/about/AboutFragment.java:181-188 |

FW-MEMORY: implicit `startActivity` adds `CATEGORY_DEFAULT`, so the EDIT/INSERT/PICK filters without DEFAULT match only explicit intents. In practice they just make those activities exported, so `adb am start -n` can reach them.

### 1.3 Receivers

| Receiver | Exported | Filter | Notes | MAN |
|---|---|---|---|---|
| `.widget.ButtonAddTransactionWidgetProvider` | true | APPWIDGET_UPDATE | `@xml/widget_button_add_transaction`. Tap opens the editor with INSERT | 67-77; J/widget/ButtonAddTransactionWidgetProvider.java:36-41 |
| `.widget.SummaryWidgetProvider` | true | APPWIDGET_UPDATE | `updatePeriodMillis=180000`. Logo opens Main, refresh button sends a self-broadcast | 78-88; J/widget/SummaryWidgetProvider.java:49-62 |
| `.widget.AccountBillsWidgetProvider` | true | APPWIDGET_UPDATE | `RES/xml-v11/widget_account_bills.xml`. Remote list via `AccountBillsWidgetService` | 89-99; J/widget/AccountBillsWidgetProvider.java:40-75 |
| `.widget.SingleAccountWidget` | true | APPWIDGET_UPDATE | `updatePeriodMillis=86400000`, home_screen\|keyguard | 114-124 |
| `.sync.SyncSchedulerBroadcastReceiver` | true | BOOT_COMPLETED, `${applicationId}.intent.action.START_SYNC_SERVICE` / `STOP_SYNC_SERVICE` | sets or cancels the `AlarmManager` heartbeat towards `SyncBroadcastReceiver` | 100-106; J/sync/SyncSchedulerBroadcastReceiver.java:44-90 |
| `.sync.SyncBroadcastReceiver` | false | – | alarm target: `SyncManager.triggerSynchronization` | 107; J/sync/SyncBroadcastReceiver.java:36-45 |
| `.core.RecurringTransactionBootReceiver` | true | BOOT_COMPLETED | also explicit broadcast from `MainActivity.populateScheduledTransactions` (J/home/MainActivity.java:1245-1246); sets a daily alarm | 108-112; J/core/RecurringTransactionBootReceiver.java:40-85 |
| `.notifications.RecurringTransactionReceiver` | false | – | alarm target → `RecurringTransactionIntentService.enqueueWork` | 113; J/notifications/RecurringTransactionReceiver.java:31-40 |
| `.notifications.SmsReceiverTransactions` | true | `android.provider.Telephony.SMS_RECEIVED` | **`RECEIVE_SMS` is not requested** (MAN:36-38 commented out) and `pref_sms_auto_trans` defaults to false | 126-131; J/notifications/SmsReceiverTransactions.java:96-113 |
| `.JacocoInstrument.SMSInstrumentedReceiver` | true | `edu.gatech.m3.emma.COLLECT_COVERAGE` | harness, ignore | 502-507 |
| Library (WorkManager): `ForceStopRunnable$BroadcastReceiver`, 4 `ConstraintProxy*` and `RescheduleReceiver` (disabled), `ConstraintProxyUpdateReceiver`, `DiagnosticsReceiver` (exported, `DUMP` permission) | – | – | library code | APKMAN |

### 1.4 Services

| Service | Exported | Filter / permission | Notes | MAN |
|---|---|---|---|---|
| `.notifications.RecurringTransactionIntentService` (JobIntentService) | false | `BIND_JOB_SERVICE` | `onHandleWork` → `RecurringTransactionNotifications.notifyRepeatingTransaction` | 398-400; J/notifications/RecurringTransactionIntentService.java:38-48 |
| `.widget.AccountBillsWidgetService` (RemoteViewsService) | false | **`BIND_JOB_SERVICE`** (a RemoteViewsService normally requires `BIND_REMOTEVIEWS`) | FW-MEMORY: AppWidgetService refuses to bind a RemoteViewsService not protected by `BIND_REMOTEVIEWS`, so the list would stay empty. UNVERIFIED | 401-403 |
| `.sync.SyncService` (JobIntentService) | false | `${applicationId}.sync.action.SYNC/DOWNLOAD/UPLOAD`, `BIND_JOB_SERVICE` | `enqueueWork` from `SyncManager.invokeSyncService`; replies through a `Messenger` | 444-453; J/sync/SyncManager.java:188-222; J/sync/SyncService.java:79-152 |
| `.sync.adapter.AuthenticatorService` | false | `android.accounts.AccountAuthenticator`, `@xml/authenticator` | stub authenticator | 454-465 |
| `.sync.adapter.SyncAdapterService` | true | `android.content.SyncAdapter`, `process=:sync` | only triggered by `SyncAdapterTrigger`, which nothing references (§5) | 466-477 |
| **Phantom:** `.widget.SummaryDashExtension`, `.widget.AccountBillsDashExtension` | true | `com.google.android.apps.dashclock.Extension` | no class in the APK (`tools:ignore="MissingClass"`) | 404-443 |
| Library: WorkManager `SystemAlarmService`, `SystemJobService` (exported), `SystemForegroundService`; Room `MultiInstanceInvalidationService` | – | – | library code | APKMAN |

### 1.5 Other external surfaces

- **Launcher shortcut** (API 25+): "New transaction" → explicit INSERT to `CheckingTransactionEditActivity` (RES/xml-v25/shortcuts.xml:19-32). This bypasses the MainActivity gate.
- **Widgets:** the 4 providers above (home-screen or keyguard). Configuration is not wired.
- **Backup:** `MoneyManagerBackupAgentHelper` (FW-MEMORY: reachable through `adb shell bmgr backupnow/restore`).
- **Notifications:** recurring-transactions notification (content intent → `RecurringTransactionListActivity`, J/notifications/RecurringTransactionNotifications.java:86-121), sync notifications (J/sync/SyncNotificationFactory.java, J/sync/SyncService.java:155-172 → MainActivity), SMS notification (J/notifications/SmsReceiverTransactions.java:1075-1090).
- **Search / SEND / share / file-type filters:** none, except MainActivity VIEW for `*.mmb`/`*.emb` files. Outgoing SEND chooser: J/about/AboutFragment.java:91-96, 235-245; J/core/file/TextFileExport.java:156-163; J/log/ExceptionHandler.java:194-205.

---

## 2. First-run flow and setup gates

### 2.1 The gate chain (fresh install)

1. **App start.** `MainActivity.onCreate` injects dependencies, then calls `showPrerequisite()` **before** anything else, including `handleIntent()` (J/home/MainActivity.java:179-187 vs 210). When a prerequisite screen is shown, it calls `finish()` and returns.
2. **G1 – Tutorial.** `isTutorialNeeded()` returns `BehaviourSettings.getShowTutorial()`, default **true** (pref key `prefshowtutorial`, RES/values/prefids.xml:77; J/settings/BehaviourSettings.java:86-88; J/home/MainActivity.java:1351-1352, 1478-1483).
   - `showTutorial()` starts `TutorialActivity` with `FLAG_ACTIVITY_CLEAR_TOP` (J/home/MainActivity.java:812-817).
   - The tutorial is a 5-page `ViewPager` with a `FragmentStatePagerAdapter` (J/tutorial/TutorialActivity.java:59-64; J/tutorial/TutorialPagerAdapter.java:36-65).
   - The only way out is the "Close" text `skipTextView`, a ButterKnife `@OnClick`. It starts `GeneralSettingsActivity` for result (J/tutorial/TutorialActivity.java:90-96; RES/layout/activity_tutorial.xml:45-46).
   - On return, any result (Back is enough) sets `prefshowtutorial=false` and starts MainActivity with `CLEAR_TOP` (J/tutorial/TutorialActivity.java:76-88, 120-128).
3. **G2 – Database present.** `isDatabaseAvailable()` (J/home/MainActivity.java:1338-1349) requires all of:
   - `databasepath` is non-empty (J/settings/DatabaseSettings.java:32-35; RES/values/prefids.xml:34);
   - if the path ends with `.emb`, `MmexApplication.getPassword()` is non-empty. The password lives in memory only (J/MmexApplication.java:78, 89-90);
   - the file exists.

   Otherwise `showSelectDatabaseActivity()` runs (`CLEAR_TOP`, J/home/MainActivity.java:1502-1507).
4. **SelectDatabaseActivity** (J/home/SelectDatabaseActivity.java:53-123).
   - `onCreate` requests READ and WRITE external storage (G3, J/utils/MmxFileUtils.java:140-166).
   - "Create database" (`createDatabaseButton`): `startActivity(PasswordActivity)`, then `FileStorageHelper.showCreateFilePicker()`, which is `ACTION_CREATE_DOCUMENT` with title `your_data.mmb`, request 16 (J/home/SelectDatabaseActivity.java:99-104; J/core/docstorage/FileStorageHelper.java:74-87).
   - "Open database" (`openDatabaseButton`): PasswordActivity, then `ACTION_OPEN_DOCUMENT`, request 15 (J/home/SelectDatabaseActivity.java:106-111; FileStorageHelper.java:56-72).
   - The picker ends up on top of PasswordActivity. The picker result is queued for SelectDatabaseActivity, and FW-MEMORY says it is delivered when that activity resumes, i.e. after PasswordActivity's OK.
   - With `RESULT_OK`, `FileStorageHelper.createDatabase/selectDatabase` does the following (FileStorageHelper.java:94-175, 220-247, 340-361; J/utils/MmxDatabaseUtils.java:202-224):
     - `takePersistableUriPermission`;
     - reads display name and modification date of the document;
     - local path = default DB directory + display name;
     - copies the document there;
     - `MmxDatabaseUtils.useDatabase()`. This **throws if the name does not end in `.mmb`/`.emb`** or the file is not readable/writable (MmxDatabaseUtils.java:78-88, 202-206; the `Toast` "Not a .mmb file" is at FileStorageHelper.java:164-169), then sets `databasepath`, adds the recent-DB entry with `remotePath` = document URI, re-initialises the open helper and resets the provider.
   - After that, `onDatabaseSelected()` starts MainActivity with `NEW_TASK|CLEAR_TASK` (J/home/SelectDatabaseActivity.java:119-123; J/core/IntentFactory.java:67-77). An empty created document gives a 0-byte `.mmb`. The schema is then built by `MmxOpenHelper.onCreate` (`tables_v1.sql`, base currency, date format, J/database/MmxOpenHelper.java:94-103, 227-307).
5. **G4 – PasswordActivity** (J/database/PasswordActivity.java:39-73). It is always shown on create/open (and for recent DBs and VIEW intents). The user taps OK (`btnSubmit`), and the typed text goes into `MmexApplication.mPassword`; an empty value is fine for `.mmb`. The open helper uses it as the SQLCipher key (J/database/MmxOpenHelper.java:66-71, 132-154; J/core/ioc/DbModule.java:61-70). Typing a non-empty password while creating a `.mmb` probably encrypts the new file, after which the next process (password "") cannot open it (FW-MEMORY/UNVERIFIED). **The harness should leave it empty.**
6. **MainActivity proper** (J/home/MainActivity.java:189-245):
   - `migrateRecentDatabases()`;
   - `setContentView(main_activity)`, toolbar, dual-panel detection;
   - `handleIntent()`. A VIEW of a `.mmb` file goes through PasswordActivity and `changeDatabase`;
   - `showCurrentDatabasePath` toast;
   - writes InfoTable `UID` (first DB read);
   - `initHomeFragment`, `initializeDrawer`;
   - `initializeSync()`. If sync is active (enabled, online, `remotePath` set) it starts the heartbeat and, when `pref_sync_on_app_start` (default true) is set, `triggerSynchronization` (J/home/MainActivity.java:1210-1229; J/sync/SyncManager.java:231-247, 332-354);
   - `populateScheduledTransactions()`. If recurring notifications are on (default true) it posts the notification and **auto-inserts every due recurring transaction** (J/home/MainActivity.java:1231-1287).
7. **G5 – Passcode** (only if one was set): `MainActivity.onStart` starts `PasscodeActivity` for result when `Passcode.hasPasscode()`. The passcode is a row in the DB `INFOTABLE`, stored in plain text on API > 23 (J/home/MainActivity.java:248-266, 335-360; J/core/Passcode.java:70-72, 101-147). A wrong or cancelled code calls `finish()`.
8. **G6 – Empty database.** HomeFragment shows the welcome view instead of the account list while there are 0 accounts. The welcome view has two buttons: Settings and "Add account" (J/home/HomeFragment.java:590-620, 792-794). Most of the app (transactions, investments, budgets, reports) needs at least one account, and investments need an "Investment" account (J/account/AccountTypes.java:25-32).

### 2.2 Gate table

| Gate | Enforced by | Pass condition | Stored in | Baseline (MK/APE) |
|---|---|---|---|---|
| G1 tutorial | MainActivity.java:1478-1483 | tap "Close", then leave General settings | default prefs `prefshowtutorial=false` | **passed**: `TutorialActivity.onActivityResult`, `BehaviourSettings.setShowTutorial` hit by both |
| G2 database | MainActivity.java:1338-1349, 1486-1490 | SAF create/open returns OK and a `.mmb` name; or seeded prefs | default prefs `databasepath`; `com.money.manager.ex.recent_db.xml` key `LIST` (J/home/RecentDatabasesProvider.java:43, 202-205; J/settings/PreferenceConstants.java:62) | **never passed** |
| G3 storage permission | SelectDatabaseActivity.java:62-64 | grant (denial does not block; the DB dir falls back to `getExternalFilesDir`, J/core/database/DatabaseManager.java:86-101) | runtime permission | not a blocker (§2.3) |
| G4 password | PasswordActivity; MainActivity.java:1344 for `.emb` | tap OK (empty is fine for `.mmb`) | memory only | reached; `returnPassword` hit |
| G5 passcode | MainActivity.java:248-266 | type the 5-digit code | DB INFOTABLE `PASSCODE` | n/a |
| G6 accounts | HomeFragment.java:792-794 | create ≥1 account (and ≥1 Investment account for INVEST) | DB | n/a |

There is no login, cloud account, network or data import requirement for the core app. Sync needs a SAF document as remote file. Price/exchange-rate downloads need network services that are probably defunct (§5.5).

### 2.3 Which gate stopped the baseline (per-class JaCoCo evidence)

- Tutorial fully covered: `TutorialActivity` 7/7, all 5 page fragments. Monkey alone reached pages 4-5: `TutorialFinancialOverviewFragment` and `TutorialSyncFragment` are Monkey-only.
- `MainActivity` 10/79: `onCreate`, `showPrerequisite`, `isTutorialNeeded`, `isDatabaseAvailable`, `showSelectDatabaseActivity`, `showTutorial`, `onDestroy`, etc. `migrateRecentDatabases` was **never** hit, and it is the first statement after the gate (MainActivity.java:190). MainActivity never got past `showPrerequisite()`, and its layout was never inflated.
- `SelectDatabaseActivity` 5/7: `onCreate`, `onCreateDatabaseClick`, `onOpenDatabaseClick`, `onActivityResult`. Not hit: `onDatabaseSelected`, `onRequestPermissionsResult`.
- `FileStorageHelper` 3/25: `<init>`, `showStorageFilePicker`, `showCreateFilePicker`. Not hit: `createDatabase`, `selectDatabase`, `pullDatabase`.
- `PasswordActivity` 6/6.
- `DatabaseManager` 0/8, `MmxOpenHelper` 0/19, `DbModule.provideOpenHelper` not hit (its factory `get` is not hit).
- **Conclusion:** results came back to `SelectDatabaseActivity.onActivityResult` but never with `RESULT_OK` (J/home/SelectDatabaseActivity.java:73-76), and the database was never opened.
- **Why:**
  - Both runs used `monkey -p com.money.manager.ex` (`monkey/status.json`, `ape/status.json` `command`). FW-MEMORY: Monkey's `IActivityController.activityStarting` rejects activities of packages outside `-p`, and AMS then sends `RESULT_CANCELED` to the caller. The DocumentsUI picker (`com.android.documentsui` on API 27, FW-MEMORY) is such an activity, so the SAF flow can never complete under either tool.
  - Even unrestricted, a random tester would have to pick a location, keep a `.mmb` name, press SAVE and then OK.
  - The VIEW intent for `.mmb` files cannot bypass the gate either: `showPrerequisite` runs before `handleIntent` (MainActivity.java:184 vs 210).
- **The storage permission dialog was probably not the blocker.**
  - `MmxFileUtils.requestExternalStoragePermissions/requestPermission` ran many times, yet `SelectDatabaseActivity.onRequestPermissionsResult` (J/home/SelectDatabaseActivity.java:90-97) **never** ran.
  - On API 27 a blocked, denied or second concurrent `requestPermissions` still delivers `onRequestPermissionsResult` (FW-MEMORY).
  - So the permissions were most likely already granted, e.g. by `adb install -g`. INFERRED; check the harness install command.
- The tools also changed the app language and theme in General settings: `GeneralSettingsFragment$1/$2.onPreferenceChange` hit by both, `$4` (anonymous-usage switch) only by APE (J/settings/GeneralSettingsFragment.java:58-128). Later runs may therefore show a non-English UI.

### 2.4 Screens the baseline never reached

Reached at all: `TutorialActivity` (+5 fragments), `GeneralSettingsActivity`/`GeneralSettingsFragment`, `SelectDatabaseActivity`, `PasswordActivity`. `MainActivity` ran only its gate code and showed no UI.

**Never reached:** every other activity, fragment and dialog. That covers the Home/drawer UI, accounts and transactions, recurring, categories/payees/currencies, investments, budgets, search, reports, all other settings screens, About/Help, the calculator, passcode, widgets and notifications. All of them sit behind G2. The only exceptions are the exported activities and the launcher shortcut, which the tools never start (they only launch the MAIN/LAUNCHER activity, FW-MEMORY).

### 2.5 What a test harness has to prepare

**Recipe A (recommended, faithful to the app).**

1. Install with `adb install -g` so both storage permissions are granted. The DB then goes to `/sdcard/MoneyManagerEx/`, otherwise to `/sdcard/Android/data/com.money.manager.ex/files/databases/` (J/core/database/DatabaseManager.java:86-155).
2. Outside the tool, by hand or with UIAutomator, which is not limited by `-p`:
   - launch the app, tap "Close" on the tutorial, press Back in General settings;
   - tap "Create database";
   - in DocumentsUI pick e.g. Downloads, keep `your_data.mmb`, tap Save;
   - in PasswordActivity leave the field empty and tap OK.

   This produces a real `remotePath` content URI, a persisted URI permission and the schema.
3. Add data through the UI or by SQL on the pulled DB file:
   - several accounts of each type (Checking, Cash, Credit Card, Term, Loan, **Investment**, Shares; AccountTypes.java:25-32);
   - 2+ currencies;
   - payees, categories and sub-categories;
   - withdrawals, deposits, a **transfer**, a **split** transaction, rows with each status (R/V/F/D) and a future-dated row;
   - a recurring transaction due today or overdue (for the notification, "enter next occurrence" and the auto-insert in `populateScheduledTransactions`);
   - a budget with entries;
   - stocks with price history in the Investment account;
   - optionally a passcode in a separate snapshot to exercise G5.
4. Snapshot the AVD, or archive `/data/data/com.money.manager.ex` and the external DB file and SAF document, then restore before each run.
5. Optional: set `pref_sync_on_app_start=false` in `com.money.manager.ex.sync_preferences.xml` (J/settings/PreferenceConstants.java:63). This avoids the non-cancelable sync `ProgressDialog` at every MainActivity creation (J/sync/SyncManager.java:188-222). The key name may be prefixed by `SyncPreferences.getKey` (UNVERIFIED).

**Recipe B (seeding only; the APK is `debuggable=true`, so `adb shell run-as com.money.manager.ex` works).**

1. Write `shared_prefs/com.money.manager.ex_preferences.xml` with `prefshowtutorial=false` and `databasepath=<abs path>.mmb`. A 0-byte `.mmb` is enough: `MmxOpenHelper.onCreate` creates the schema (INFERRED from the app's own create path, which copies an empty document).
2. **Also** write `shared_prefs/com.money.manager.ex.recent_db.xml`, key `LIST`, holding JSON `{"<path>": {"localPath": "<path>", "remotePath": "<non-empty>", ...}}` (fields in J/home/DatabaseMetadata.java:29-43). Without it, `RecentDatabasesProvider.getCurrent()` creates an entry with `remotePath=""` (J/home/RecentDatabasesProvider.java:119-133; J/home/DatabaseMetadataFactory.java:69-82). `CheckingTransactionEditActivity.onCreate` → `initAttachmentControls` then throws on `"".substring(0, 2)` (J/transactions/CheckingTransactionEditActivity.java:383; J/transactions/EditTransactionCommonFunctions.java:735-736), so every add/edit-transaction path crashes.
3. A fake `remotePath` makes `SyncManager.isActive()` true when online, so also disable sync (`pref_sync_enabled=false` in the sync prefs file) or use a real SAF URI.
4. Do not use `.emb`: it needs a password in memory at every process start (MainActivity.java:1344).

**Either way:** the `-p` filter keeps blocking every flow that leaves the package, so those stay unreachable for the tools:

- SAF open/create/backup (drawer "Open/Create database", Settings › Database › backup);
- the share/e-mail choosers;
- browser links in About;
- the attachment viewer.

System date/time pickers run in-process and are not affected. The drawer "Open/Create database" items also leave PasswordActivity on screen (J/home/MainActivity.java:618-632).

---

## 3. Screens and navigation

### 3.1 Activities: inputs, menus and modes (all SRC unless marked)

| Activity (area) | Layout / hosted fragments | Main gestures → handler | Options menu | Modes that change active handlers |
|---|---|---|---|---|
| `MainActivity` (SHELL) | `main_activity`. Content: `fragmentMain` (phone), `fragmentDetail` (tablet). Hosts `HomeFragment` (initial), `AccountListFragment`, `CategoryListFragment`, `PayeeListFragment`, `RecurringTransactionListFragment`, `AccountTransactionListFragment`, `WatchlistFragment`, `PortfolioFragment` | Nav icon (`android.R.id.home`) or hardware MENU toggles the drawer (MainActivity.java:387-421). Back closes the drawer first (440-451). Drawer group/child click → `Handler.postDelayed(200)` → `onDrawerMenuAndOptionMenuSelected` (936-985, 589-697). `onClickCardViewIncomesVsExpenses` comes from RES/layout/home_fragment.xml:127 (832-834) | `onCreateOptionsMenu` only adds the sync-progress item when `mIsSynchronizing` (372-384); that is **never true** (§5.3) | drawer open/closed; single vs dual panel (`fragmentDetail` visible, 200-201); restart pending (`mRestartActivity`, static) → `onResume` → `restartActivity()` (271-283, 702-716); in-authentication |
| `SelectDatabaseActivity` (SHELL) | `activity_select_database` | Create / Open buttons via `_ViewBinding$1/$2.doClick` (99-111) | none | – |
| `PasswordActivity` (SHELL) | `activity_password` | OK (`btnSubmit`) → `returnPassword` (50-73) | none | caller context: create, open, recent DB (for result `REQUEST_PASSWORD`), VIEW intent |
| `PasscodeActivity` (SHELL) | `passcode_activity` | 10 digit buttons (shared listener, 5 fields, auto-submit on the 5th: PasscodeActivity.java:99-140). Backspace `@OnClick buttonPasscodeKeyBack` (220). Fingerprint via `FingerprintHandler` | none | fingerprint hardware/enrolled (163-200); caller context (unlock, set, re-insert, edit-old, disable, notification) |
| `TutorialActivity` (SHELL) | `activity_tutorial`. `ViewPager` + `TutorialPagerAdapter` (5 fragments) + CircleIndicator | swipe pages; "Close" (`skipTextView`) → `onCloseClicked` (90-96) | `menu_tutorial` (`action_settings`, no-op) through the hardware MENU panel (98-118; Monkey-only hits) | page index (fragment lifecycle only) |
| `AboutActivity` (SHELL) | `about_activity`. ViewPager + `TabLayout`, `AboutTabAdapter`: `AboutFragment`, `WebChangelogFragment`, `AboutCreditsFragment`, AboutLibraries fragment (J/about/AboutTabAdapter.java:46-60) | tabs/swipe. About tab: about 11 link click listeners (mail chooser, browser links, Lynx logcat, send logcat; J/about/AboutFragment.java:85-200) | none | tab; online vs offline changelog (J/about/WebChangelogFragment.java:82-99) |
| `HelpActivity` (SHELL) | `webview_activity` | Back → `WebView.goBack` (HelpActivity.java:67-75) | none | intent data scheme `android.resource` vs URL (50-63) |
| `WebViewActivity` (SHELL, dead) | `activity_web_view` | – | `menu_web_view` | – |
| `AccountListActivity` (TXN, external only) | `base_toolbar_activity` + `AccountListFragment` (PICK) | Back key → `setResultAndFinish` (`onKeyUp`, AccountListActivity.java:58-68) | via fragment | PICK vs EDIT (intent action) |
| `AccountEditActivity` (TXN) | `activity_account_edit` (+ ViewHolder) | spinners (type, status), currency → `CurrencyListActivity` PICK (390-395), initial date → `DatePickerDialog` (400-420), initial balance → Calculator (301-310), favourite/default checkboxes, toolbar done/cancel (AccountEditActivity.java:138-541) | save/cancel (177-) | INSERT vs EDIT (84, 109) |
| `CheckingTransactionEditActivity` (TXN) | `activity_edit_checking_account_transaction`, logic in `EditTransactionCommonFunctions` | type buttons Withdrawal/Deposit/Transfer (ETCF:753-790); account spinners (381, 388); amount/amount-to → Calculator (419-450); payee → PayeeActivity PICK (571-580); category → CategoryListActivity PICK (459-467); split → SplitCategoriesActivity (599-625, 1511-1528); date → DatePicker (488-500), prev/next day (511-525); status spinner (646); trans-number auto button (691-723); notes watcher (551); attachments (729-750); Back → cancel confirm (CTEA:184-191; ETCF:822-840) | `MenuHelper.addSaveToolbarIcon` (save) + Up (CTEA:140-160) | INSERT / EDIT / PASTE (duplicate) / INSERT with recurring id / external data URI (CTEA:465-505, 279-350); **transfer vs non-transfer** (ETCF:975-993); **split vs not** (961-967, 1557-1573); dirty |
| `SplitCategoriesActivity` (TXN) | `activity_split_categories`, RecyclerView `SplitCategoriesAdapter` + `ItemTouchHelper` swipe (272) | FAB add (`@OnClick fab`, 191); row amount → Calculator (`AmountEntryRequestedEvent`, 206-212); row category → CategoryListActivity PICK (`CategoryRequestedEvent`, 214, 308-314); swipe to remove (`SplitItemRemovedEvent`, 201) | done/cancel (109-) | list empty/non-empty |
| `CalculatorActivity` (TXN) | `activity_calculator` | number/operator buttons (330-350), delete (`@OnClick deleteButton`, 236), equals (247), done → `setResult` (441-444) | (137-) | caller context (request code) |
| `RecurringTransactionListActivity` (TXN) | `base_toolbar_activity` + `RecurringTransactionListFragment` | passcode check when launched from the notification (51-57) | via fragment | launched-from-notification and passcode set |
| `RecurringTransactionEditActivity` (TXN) | `activity_edit_recurring_transaction` + `EditTransactionCommonFunctions` (no attachments) | same as the transaction editor, plus recurrence spinner (329), next-occurrence date → DatePicker (355-375), payment-date buttons (382, 390) | save + Up (156-170) | INSERT / EDIT (116, 127); transfer / split / dirty as above |
| `CategoryListActivity` (MASTER) | `base_toolbar_activity` + `CategoryListFragment` | Back key → `setResultAndFinish` (CategoryListActivity.java:73-84) | via fragment | PICK vs EDIT (`listFragment.mAction = intent.getAction()`, 54-58) |
| `PayeeActivity` (MASTER) | `base_toolbar_activity` + `PayeeListFragment` | Back key → `RESULT_CANCELED` (PayeeActivity.java:62-75) | via fragment | PICK vs EDIT. **`PayeeListFragment.mAction` is static** (J/fragment/PayeeListFragment.java:67) |
| `CurrencyListActivity` (MASTER) | `base_toolbar_activity` + `CurrencyListFragment` | Back key → `setResultAndFinish` (71-80) | via fragment | PICK vs EDIT (CurrencyListFragment.java:92-98, null action → NPE) |
| `CurrencyEditActivity` (MASTER) | `currency_edit_activity` | fields + done/cancel | save | INSERT / EDIT (96, 106) |
| `CurrencyChartActivity` (MASTER) | `activity_currency_chart` (landscape; Yahoo chart URL) | – | `menu_currency_chart` (`action_settings`) | online / offline |
| `CurrencyRecyclerListActivity` (MASTER, dead) | `base_toolbar_activity` + `CurrencyRecyclerListFragment` | – | – | – |
| `InvestmentTransactionEditActivity` (INVEST) | `activity_investment_transaction_edit` | `@OnClick` numShares / purchasePrice / commission / currentPrice → Calculator (211-242); account spinner (339); date → DatePicker (345-365); buttons (376, 383) | save (161-) | INSERT / EDIT |
| `PriceEditActivity` (INVEST) | `activity_price_edit` | `@OnClick` amount → Calculator (135), date → DatePicker (143-160), previous/next day (164-178) | save + Up (102-122) | – |
| `PortfolioActivity` (INVEST, dead) | `activity_portfolio` | – | – | – |
| `BudgetsActivity` (BRS) | `activity_budgets` + `BudgetListFragment`, then `BudgetDetailFragment` (back stack on phone) | `BudgetSelectedEvent` → `showBudgetDetails` / `showFragment` (82-84, 132-170) | `onCreateOptionsMenu` returns true with no items (58-60) | single vs dual panel |
| `BudgetEditActivity` (BRS) | `activity_budget_edit` | `@OnClick` year → AlertDialog (98-125), month → AlertDialog (129-155), done/cancel | (76-88) | INSERT / EDIT (174-185) |
| `SearchActivity` (BRS) | `search_activity`: `SearchParametersFragment`, then `AllDataListFragment` results (`replace` + back stack on phone) | search item → `performSearch` (SearchActivity.java:107-118, 166-213) | `menu_search` (`searchMenuItem`) | parameters vs results; started with `EXTRA_SEARCH_PARAMETERS` → searches immediately (151-164) |
| `CategoriesReportActivity` / `PayeesReportActivity` / `IncomeVsExpensesActivity` (BRS) | `report_chart_fragments_activity`: list fragment (+ chart fragment in `fragmentChart` on tablet, else `replace` + back stack) | list row → `SearchActivity`; chart toggle; period menus | see §3.2 | list vs chart; CategoriesReport filters `REPORT_FILTERS` = Withdrawal / Deposit / none (MainActivity.java:661-681) |
| `SettingsActivity` (SETSYNC) | `settings_activity` + `SettingsFragment` or `PerDatabaseFragment` (`EXTRA_FRAGMENT`, SettingsActivity.java:55-72) | preference clicks | – | which fragment |
| `GeneralSettingsActivity`, `LookFeelSettingsActivity`, `BehaviourSettingsActivity`, `InvestmentSettingsActivity`, `BudgetSettingsActivity`, `SecuritySettingsActivity`, `DatabaseSettingsActivity`, `SyncPreferencesActivity` (SETSYNC) | `settings_activity` + one `PreferenceFragmentCompat` (`BaseSettingsFragmentActivity.setSettingFragment`, BaseSettingsFragmentActivity.java:71-92) | preference click/change listeners (§3.2) | Up only | General: started for result by Tutorial vs by SettingsFragment; Security: passcode set or not; Sync: enabled / remote file set |
| `SingleAccountWidgetConfigureActivity` (SETSYNC, external only) | `single_account_widget_configure` | account spinner + add button (65-102) | – | – |

### 3.2 Fragments, dialogs, menus, action modes, preference screens

**Fragments inside `MainActivity`.** All are switched with `showFragment_Internal`: `replace(fragmentMain)` + `addToBackStack(null)` (MainActivity.java:1446-1470).

- **`HomeFragment`** (`home_fragment`).
  - Inputs: FAB → new transaction (185-191); search menu `home_menu` → SearchActivity (355-366).
  - Expandable account list: child click → `RequestAccountFragmentEvent`, or `RequestWatchlistFragmentEvent` for Investment (686-705). Group expand/collapse is stored in prefs (710-735).
  - Long-press child → context menu built from `R.array.context_menu_account_dashboard` ("Edit") + "Balance account" (transaction account types only) + "Portfolio" (Investment only) (409-447). Selection matches by title (450-480). Balance opens `AmountInputDialog`, whose `AmountEnteredEvent` opens the editor with a data URI (539-548, 490-527).
  - Welcome view buttons: Settings / Add account (590-620). Loaders: account bills + income/expense (221-353).
  - **Modes:** empty (welcome) vs non-empty; loading (progress bar) vs loaded (672-680).
- **`AccountListFragment`** (BaseListFragment).
  - Inputs: FAB → `AccountEditActivity` INSERT; long-press → ctx Edit/Delete (99-133); Delete → "in use" notice or confirm (134, 264); search view (BaseListFragment.java:113-150).
  - **Modes:** PICK (multiple-choice layout, returns on Back) vs EDIT (69-81, 221-245).
- **`AccountTransactionListFragment`** + child `AllDataListFragment`.
  - Header: favourite star toggle (518-534), "go to account" → `AccountEditActivity` (536-543).
  - Action-bar account `Spinner` (custom view) → `switchAccount` (605-633).
  - Menus: `menu_period_picker_transactions` (submenu of 10 periods), `menu_transaction_status_selector` (submenu of 5 statuses), `menu_transaction_filters` → `FilterDialogFragment` (227-249, 286-325, 417-437, 547-604, 828-831).
  - Running balance via `CalculateRunningBalanceTask2` (AsyncTask) → `RunningBalanceCalculatedEvent` (409-415, 638-648).
  - `menu_add_transaction_account` and `menu_export_to_csv` cases (299-307) belong to **no inflated menu** (§5.3).
- **`AllDataListFragment`** (shared by account list and search results).
  - Row click → edit transaction (158-170, 785-801). FAB → new (382-384). `CHOICE_MODE_MULTIPLE_MODAL` + `AllDataMultiChoiceModeListener` (154-155).
  - Long-press starts the **action mode** `menu_all_data_adapter`: duplicate / change status / delete / select all, plus status ids (AllDataMultiChoiceModeListener.java:48-101; AllDataListFragment.java:392-453). Change status → list dialog (859-913). Delete → confirm (704-777). Duplicate → editor PASTE (916-932).
  - `registerForContextMenu` (186) has no `onCreateContextMenu`; FW-MEMORY: long-press in multiple-modal starts the action mode instead.
  - QIF export menu (`menu_alldata_operations`) only inside SearchActivity (301-327, 361-372, 934-938).
- **`CategoryListFragment`** (BaseExpandableListFragment).
  - EDIT: long-press ctx Edit / Delete / View transactions (160-228); FAB → type selector dialog → new category / sub-category dialogs (707-731, 512-657); delete confirm / in-use (450-510); View transactions → SearchActivity (733-738).
  - PICK: child/group click returns the result (659-700, 313-360). Search view (BaseExpandableListFragment.java:120-205).
- **`PayeeListFragment`.** Sort submenu (name / usage, 124-169); ctx Edit / Delete / View transactions (178-237); FAB → new payee dialog (361-411); delete (222, 335); PICK returns the result (304-331).
- **`RecurringTransactionListFragment`.** `menu_item_calendar` → `CaldroidFragment` with `CaldroidListener` (134-150, 357-411). ctx `contextmenu_repeating_transactions`: enter next occurrence → editor INSERT with recurring id; skip → confirm; edit → recurring editor; delete → confirm (164-210, 304-343, 428-458). FAB → recurring editor INSERT.
- **`WatchlistFragment`** + child `WatchlistItemsFragment`.
  - Header: account, "go to account" (549-579). Account spinner (519-535).
  - `menu_watchlist`: update prices (confirm, 384) / export prices (CSV share) / purge history (confirm, 459) / change provider (single-choice dialog, 614) (213-266).
  - Price events from the updaters (285-305).
  - Items: row click → InvestmentTransactionEditActivity (140, 462-470); ctx Download price / Edit price (→ PriceEditActivity) / Delete (190-260, 475).
- **`PortfolioFragment`.** Row click → InvestmentTransactionEditActivity INSERT/EDIT (140-203).

**Fragments in other hosts.**

- `BudgetListFragment`: row click → `BudgetSelectedEvent`; ctx Edit / Delete (Copy is a todo; 164-215); FAB → BudgetEditActivity INSERT (235-253).
- `BudgetDetailFragment`: simple vs full layout per `BudgetSettings` (99).
- `SearchParametersFragment`: account and status spinners; payee/category pickers (189-204); from/to date pickers (344-395); from/to amount → Calculator (398-415); `menu_clear` (290-305).
- Report fragments:
  - `BaseReportFragment` → `CategoriesReportFragment`, `PayeeReportFragment`: `menu_report` (chart toggle; the `menu_option1` submenu items get negative ids for categories) + `menu_period_picker` (7 periods incl. custom dates dialog, 101-195, 262-300). Row click → SearchActivity (CategoriesReportFragment.java:370-383; PayeeReportFragment.java:308-321). Chart → `PieChartFragment` (`OnChartValueSelectedListener`, 147-188).
  - `IncomeVsExpensesListFragment` (`menu_report_income_vs_expenses`: chart, sort asc/desc, period → years dialog, 220-300) → row click → SearchActivity (363-392), chart → `IncomeVsExpensesChartFragment` (bar chart listener, 142-168).
- Tutorial: 5 static page fragments. About: 4 tab fragments (`AboutChangelogFragment` is unused).

**Dialogs (windows that capture input).**

- `AmountInputDialog`: keypad DialogFragment, posts `AmountEnteredEvent` (J/common/AmountInputDialog.java:158-260). Callers: HomeFragment balance, InvestmentSettingsFragment threshold, and `EditPriceDialog` (dead).
- `FilterDialogFragment` (113-184).
- `YesNoDialog`: posts `DialogPositive/NegativeClickedEvent` (J/transactions/YesNoDialog.java:65-83).
- `TipsDialogFragment`: shown by BaseListFragment / BaseExpandableListFragment `onStart` only when `pref_text_search_type == false` (BaseListFragment.java:93-110).
- `EditPriceDialog` (never instantiated).
- About 30 `AlertDialog.Builder` sites: confirmations, name editors, single-choice lists. Main sites: CategoryListFragment:462/479/530/610/708; PayeeListFragment:222/335/370; AccountListFragment:134/264; AllDataListFragment:708/887; ETCF:824/1473/1536; SplitCategoriesActivity:318; RecurringTransactionListFragment:304/333; BudgetEditActivity:113/143; BudgetListFragment:253; CurrencyUIFeatures:71/115/138/161/192; WatchlistFragment:384/459/614; WatchlistItemsFragment:475; BaseReportFragment:277; IncomeVsExpensesListFragment:290; PerDatabaseFragment:328; UIHelper.binaryDialog:85-121; Core.alert:78-100.
- System pickers: `DatePickerDialog` (AccountEdit:411, ETCF:498, RecurringEdit:365, InvestmentEdit:358, PriceEdit:152, SearchParams:348/375); `TimePickerDialog` (BehaviourSettingsFragment:106).
- Non-interactive `ProgressDialog`s: PriceUpdaterBase:44, ExportToCsvFile:54, SyncManager:200, CurrencyUIFeatures:230.
- Preference-framework dialogs (FW): ListPreference / EditTextPreference dialogs on the settings screens.

**Context menus (9, 8 live).** Home account; account list; category; payee; currency (`R.array.context_menu_currencies`: Edit / Chart / Update rate / Delete, CurrencyListFragment.java:216-262); recurring; budget; watchlist item; currency-recycler (dead). `AllDataListFragment` registers one but defines no `onCreateContextMenu`; `ExpandableListFragment.onCreateContextMenu` is empty. There is no PopupMenu, no BottomSheet and no navigation graph.

**Action mode (1).** `AllDataMultiChoiceModeListener`.

**Drawer (1).**

- Expandable list built in `getDrawerMenuItems` / `createExpandableDrawer` (MainActivity.java:1046-1125, 840-934):
  - Home;
  - Open database (children: recent DBs + "Other");
  - Create database;
  - Synchronize;
  - Entities (Accounts, Categories, Currencies, Payees);
  - Recurring;
  - Budgets;
  - Search;
  - Reports (Payees, Where money goes, Where money comes from, Categories, Income vs expenses);
  - Settings;
  - About.
- There is no Help item.

**Pagers (2).** Tutorial, About (with tabs). **Toolbar spinners (2).** Account selector in the account transactions and watchlist views.

**Preference screens (10).**

- `preferences.xml` (SettingsFragment, 10 rows, each starts an activity: SettingsFragment.java:49-229).
- `preferences_general` (locale / theme → restart; default status / payee; anonymous usage; GeneralSettingsFragment.java:46-143).
- `preferences_per_database` (user name, base currency → CurrencyList PICK + confirm, default account, date format, financial year: PerDatabaseFragment.java:71-342).
- `preferences_look_and_feel` (LookFeelPreferenceFragment.java:48-176).
- `preferences_behaviour` (notifications switch + check time → TimePicker, focus filter, search type, SMS switches, auto number, show tutorial: BehaviourSettingsFragment.java:55-165).
- `preferences_investment` (threshold → AmountInputDialog, quote and exchange-rate provider lists: InvestmentSettingsFragment.java:61-181).
- `preferences_budget` (one switch).
- `preferences_security` (activate / edit / disable passcode → PasscodeActivity sequences; enabled state from `onResume`: SecuritySettingsFragment.java:50-175).
- `preferences_database` (path, remote path, version, clear recent files, backup → SAF CREATE_DOCUMENT, integrity, schema, fix duplicates, SQLite version: DatabaseSettingsFragment.java:67-310).
- `preferences_sync` (enabled, interval, remote file (click is a no-op now: SyncPreferenceFragment.java:197-206), download, upload, sync on start, Wi-Fi only, reset: 176-276).

### 3.3 Navigation mechanics

- **Activity transitions:**
  - `startActivity` / `startActivityForResult` (call sites listed in §3.1).
  - Result pairs, `RequestCodes` (J/core/RequestCodes.java:26-46): CATEGORY=10, PAYEE=8, ACCOUNT=12 (no starter), CURRENCY=11, AMOUNT / AMOUNT_FROM / AMOUNT_TO = 2/3/4 (Calculator), SPLIT_TX=14, PRICE=9, PASSCODE=7, SELECT_DOCUMENT=15, CREATE_DOCUMENT=16 (= CODE_BACKUP), SELECT_FILE=6, REQUEST_PASSWORD=20.
  - Result handlers: `MainActivity.onActivityResult` (298-361), `ETCF.onActivityResult` (848-904), `SplitCategoriesActivity` (133-150), `InvestmentTransactionEditActivity` (~120-135), `SecuritySettingsFragment` (94-150), `PerDatabaseFragment`, `SearchParametersFragment`, `SettingsFragment` (REQUEST_GENERAL_PREFERENCES → `recreate`, 201-209), `TutorialActivity`, `SelectDatabaseActivity`, `RecurringTransactionListActivity` (72-99).
- **MainActivity content:** fragment `replace` + `addToBackStack`, so Back pops to the previous fragment and finally to Home (1446-1470). EventBus requests drive navigation from HomeFragment: `RequestAccountFragmentEvent` / `RequestWatchlistFragmentEvent` / `RequestPortfolioFragmentEvent` → `showAccountFragment` / `showWatchlistFragment` / `showPortfolioFragment` (454-468, 782-808). `RequestOpenDatabaseEvent` has a subscriber (469-474) but **no poster**.
- **Up / Back:**
  - `MmxBaseFragmentActivity.onOptionsItemSelected`: `android.R.id.home` → `setResult(CANCELED)` + `finish` when `setDisplayHomeAsUpEnabled(true)` was called (J/common/MmxBaseFragmentActivity.java:107-128).
  - List activities intercept `KEYCODE_BACK` in `onKeyUp` to return the picked item.
  - Editors map Back → cancel-confirm.
- **Restart mechanism:** settings set the static `MainActivity.mRestartActivity = true` (GeneralSettingsFragment.java:142-145; LookFeelPreferenceFragment.java:67/86/100; RecentDatabasesProvider.clear:98). `MainActivity.onResume` then calls `restartActivity()`, which starts a new MainActivity with `NEW_TASK|CLEAR_TASK` and finishes (271-283, 702-716). After a DB change: `changeDatabase` → `restartActivity` (536-564).
- **Process statics persisting across launches:** `MainActivity.mRestartActivity`, `MmexApplication.mPassword` and `userName`, `PayeeListFragment.mAction`, `RobotoView` font, `MmxFileUtils.rawHashMap` cache. These justify `needs_state` (prompt §3 item 10).
- **Rotation:** activities without `configChanges` are recreated. Icepick (`$$Icepick`) and `onSaveInstanceState` restore state. `MainActivity.handleDeviceRotation` pops the back stack on tablets only (1169-1182). `CurrencyChartActivity` (landscape) and `TutorialActivity` (portrait) are fixed.

### 3.4 Candidate page list

How to read the table:

- A page is (window, mode). `@X` marks a variant whose continuation differs by caller.
- **Assumptions:** phone layout (single panel, drawer present); `pref_text_search_type` default (no tips dialog); the database prepared as in §2.5.
- Tablet / dual-panel would add variants. They are not listed.
- Size: about 140 base page names (21 of them `_PAUSED`), about 210 nodes once the `@` variants are counted.
- If that is too fine for one agent, the dialog variants can be collapsed into their base page.

**Pseudo and outside-app pages.**

| Page | Description | Window class | Mode predicate | Area |
|---|---|---|---|---|
| S_ENTRY | outside the app: launcher icon or shortcut, notification shade, `adb am start/broadcast`, boot | – | – | SHELL |
| S_EXIT | app finished or crashed; statics may survive (§3.3) | – | – | SHELL |
| S_SAF_PICKER@OPEN_DB / @CREATE_DB / @BACKUP | DocumentsUI picker, outside the package (blocked by `-p`) | external | request code 15 / 16 / CODE_BACKUP | SHELL |
| S_EXT_APP | any other external activity: chooser (mail/share), browser, attachment viewer | external | – | SHELL |
| S_LIB_ACTIVITY | in-package library activity: LynxActivity, LibsActivity | library | – | SHELL |
| S_HOME_WIDGETS | launcher with MMEX widgets placed (add-txn button, summary, all accounts, single account) | launcher | widget placed | SETSYNC |

**SHELL.**

| Page | Description | Window class | Mode predicate | Area |
|---|---|---|---|---|
| S_TUTORIAL | tutorial pager (5 pages) + Close | TutorialActivity | `prefshowtutorial` true | SHELL |
| S_TUTORIAL_PAUSED | General settings on top | TutorialActivity | – | SHELL |
| S_SELECT_DB | Create / Open database buttons | SelectDatabaseActivity | `databasepath` invalid | SHELL |
| S_SELECT_DB_PAUSED | Password / picker on top | SelectDatabaseActivity | – | SHELL |
| S_PASSWORD@CREATE / @OPEN / @RECENT / @VIEW | password field + OK | PasswordActivity | caller (only @RECENT returns a result) | SHELL |
| S_PASSCODE@UNLOCK / @NOTIF / @SET / @REINSERT / @EDIT_OLD / @DISABLE | 5-digit keypad (+ fingerprint if present) | PasscodeActivity | caller / request code | SHELL |
| S_MAIN_HOME_EMPTY | welcome view: Settings, Add account; FAB; search menu | MainActivity + HomeFragment | account-bills cursor count == 0 | SHELL |
| S_MAIN_HOME | account groups by type, totals, FAB, search, income/expense card | MainActivity + HomeFragment | count > 0 | SHELL |
| S_HOME_ACCOUNT_CTX@TXN / @INVEST / @OTHER | context menu: Edit (+ Balance account / + Portfolio) | context menu over HomeFragment | account type (HomeFragment.java:433-446) | SHELL |
| S_DRAWER | navigation drawer open (groups and children incl. recent DBs) | DrawerLayout in MainActivity | drawer open | SHELL |
| S_MAIN_PAUSED | MainActivity under another activity or in background | MainActivity | – | SHELL |
| S_ABOUT_INFO / S_ABOUT_CHANGELOG / S_ABOUT_CREDITS / S_ABOUT_LIBS | About tabs | AboutActivity + tab fragment | selected tab; changelog online/offline | SHELL |
| S_ABOUT_PAUSED | chooser / browser / Lynx on top | AboutActivity | – | SHELL |
| S_HELP | help WebView (external start only) | HelpActivity | – | SHELL |

**TXN.**

| Page | Description | Window class | Mode predicate | Area |
|---|---|---|---|---|
| S_ACCOUNTS | account list + FAB + search | MainActivity + AccountListFragment | EDIT | TXN |
| S_ACCOUNTS_CTX | Edit / Delete | context menu | – | TXN |
| S_DLG_ACCOUNT_DELETE@CONFIRM / @IN_USE | delete confirm / attention | AlertDialog | `isAccountUsed` | TXN |
| S_ACCOUNTS_PICK | account picker (external only) | AccountListActivity + AccountListFragment | PICK | TXN |
| S_ACCOUNT_EDIT@INSERT / @EDIT | account form | AccountEditActivity | intent action | TXN |
| S_ACCOUNT_EDIT_PAUSED | currency picker / calculator on top | AccountEditActivity | – | TXN |
| S_DLG_DATE@ACCOUNT | initial date | DatePickerDialog | – | TXN |
| S_ACCOUNT_TXNS | header, account spinner, period/status/filter menus, rows, FAB | MainActivity + AccountTransactionListFragment + AllDataListFragment | ≥1 row | TXN |
| S_ACCOUNT_TXNS_EMPTY | same without rows | same | 0 rows | TXN |
| S_TXN_LIST_SELECT@ACCOUNT / @SEARCH | action mode: duplicate / change status / delete / select all | AllDataListFragment action mode | checked items > 0 | TXN |
| S_DLG_TXN_STATUS | status list (none / reconciled / follow-up / duplicate / void) | AlertDialog (AllDataListFragment:887) | from action mode | TXN |
| S_DLG_TXN_DELETE | delete confirm | AlertDialog (AllDataListFragment:708) | – | TXN |
| S_TXN_FILTER | filter dialog (+ edit account) | FilterDialogFragment | – | TXN |
| S_TXN_EDIT@INSERT / @EDIT / @PASTE / @RECURRING / @EXTERNAL | withdrawal/deposit form | CheckingTransactionEditActivity | type ≠ Transfer and not split; caller context | TXN |
| S_TXN_EDIT_TRANSFER | to-account + amount-to rows, payee hidden | same | type == Transfer | TXN |
| S_TXN_EDIT_SPLIT | amounts disabled, split button opens the split screen | same | `isSplitSelected()` | TXN |
| S_TXN_EDIT_PAUSED | picker / calculator / split on top | same | – | TXN |
| S_DLG_TXN_DISCARD@TXN / @RECURRING | "discard changes?" | AlertDialog (ETCF:824) | dirty on cancel | TXN |
| S_DLG_TRANSFER_SPLIT@TXN / @RECURRING | convert to transfer / remove splits | YesNoDialog (ETCF:1452) / AlertDialog (ETCF:1473) | split → transfer | TXN |
| S_DLG_SPLIT_RESET@TXN / @RECURRING | split reset notice | AlertDialog (ETCF:1536) | – | TXN |
| S_DLG_DATE@TXN / @RECURRING | date | DatePickerDialog | – | TXN |
| S_SPLIT | split rows + FAB + swipe | SplitCategoriesActivity | ≥1 row | TXN |
| S_SPLIT_PAUSED | category picker / calculator on top | same | – | TXN |
| S_DLG_SPLIT | split-activity alert (SplitCategoriesActivity:318) | AlertDialog | – | TXN |
| S_CALCULATOR@TXN_AMOUNT / @TXN_AMOUNT_TO / @SPLIT / @ACCOUNT / @SEARCH_FROM / @SEARCH_TO / @INV_SHARES / @INV_PRICE / @INV_COMMISSION / @INV_CURRENT / @PRICE | keypad | CalculatorActivity | request code / caller | TXN |
| S_AMOUNT_DLG@BALANCE / @THRESHOLD | keypad dialog | AmountInputDialog | caller | TXN |
| S_RECURRING | recurring list + FAB + calendar menu | MainActivity + RecurringTransactionListFragment | ≥1 row (S_RECURRING_EMPTY otherwise) | TXN |
| S_RECURRING_CTX | enter next / skip next / edit / delete | context menu | – | TXN |
| S_DLG_RECURRING_SKIP / S_DLG_RECURRING_DELETE | confirms | AlertDialog (:304, :333) | – | TXN |
| S_RECURRING_CALENDAR | month calendar with event dates | CaldroidFragment in MainActivity | after menuCalendar | TXN |
| S_RECURRING_ACT | recurring list opened from the notification | RecurringTransactionListActivity | `INTENT_EXTRA_LAUNCH_NOTIFICATION` | TXN |
| S_RECURRING_ACT_PAUSED | passcode / editor on top | same | – | TXN |
| S_RECURRING_EDIT@INSERT / @EDIT | recurring form | RecurringTransactionEditActivity | intent action; non-transfer, non-split | TXN |
| S_RECURRING_EDIT_TRANSFER / S_RECURRING_EDIT_SPLIT | as the TXN modes | same | type / split | TXN |
| S_RECURRING_EDIT_PAUSED | picker / split / calculator on top | same | – | TXN |

**MASTER.**

| Page | Description | Window class | Mode predicate | Area |
|---|---|---|---|---|
| S_CATEGORIES | category tree + FAB + search | MainActivity + CategoryListFragment | EDIT | MASTER |
| S_CATEGORIES_PICK@TXN / @SPLIT / @SEARCH | category picker | CategoryListActivity + CategoryListFragment | PICK; caller | MASTER |
| S_CATEGORY_CTX | Edit / Delete / View transactions | context menu | category vs sub-category row | MASTER |
| S_DLG_CATEGORY_TYPE | new category vs sub-category | AlertDialog (:708) | – | MASTER |
| S_DLG_CATEGORY_EDIT@INSERT / @UPDATE | category name | AlertDialog (:530) | – | MASTER |
| S_DLG_SUBCATEGORY_EDIT@INSERT / @UPDATE | sub-category name + parent spinner | AlertDialog (:610) | – | MASTER |
| S_DLG_CATEGORY_DELETE@CONFIRM / @IN_USE | delete | AlertDialog (:462, :479) | used or not | MASTER |
| S_PAYEES | payee list + sort + FAB + search | MainActivity + PayeeListFragment | EDIT (static `mAction`) | MASTER |
| S_PAYEES_PICK@TXN / @SEARCH | payee picker | PayeeActivity + PayeeListFragment | PICK | MASTER |
| S_PAYEE_CTX | Edit / Delete / View transactions | context menu | – | MASTER |
| S_DLG_PAYEE_EDIT@INSERT / @UPDATE | payee name | AlertDialog (:370) | – | MASTER |
| S_DLG_PAYEE_DELETE@CONFIRM / @IN_USE | delete | AlertDialog (:335 / :222) | used or not | MASTER |
| S_CURRENCIES | used currencies + menu (update rates, import all, show used) | CurrencyListActivity + CurrencyListFragment | EDIT | MASTER |
| S_CURRENCIES_PICK@ACCOUNT / @BASE_CURRENCY | all currencies, tap returns | same | PICK | MASTER |
| S_CURRENCIES_PAUSED | editor / chart on top | CurrencyListActivity | – | MASTER |
| S_CURRENCY_CTX | Edit / Chart / Update rate / Delete | context menu | – | MASTER |
| S_DLG_CURRENCY_DELETE, S_DLG_RATES_UPDATE, S_DLG_IMPORT_CURRENCIES | currency dialogs | AlertDialog (CurrencyUIFeatures:71-200) | – | MASTER |
| S_CURRENCY_EDIT@INSERT / @EDIT | currency form | CurrencyEditActivity | intent action | MASTER |
| S_CURRENCY_CHART | landscape chart image | CurrencyChartActivity | online / offline | MASTER |

**INVEST.**

| Page | Description | Window class | Mode predicate | Area |
|---|---|---|---|---|
| S_WATCHLIST | header, account spinner, stock rows, menu (update / export / purge / provider) | MainActivity + WatchlistFragment + WatchlistItemsFragment | ≥1 stock (S_WATCHLIST_EMPTY otherwise) | INVEST |
| S_WATCHLIST_CTX | Download price / Edit price / Delete | context menu | – | INVEST |
| S_DLG_PRICES_UPDATE, S_DLG_PURGE_HISTORY, S_DLG_PROVIDER, S_DLG_STOCK_DELETE | watchlist dialogs | AlertDialog (WatchlistFragment:384 / 459 / 614; WatchlistItemsFragment:475) | – | INVEST |
| S_PORTFOLIO | portfolio list | MainActivity + PortfolioFragment | from Home context menu | INVEST |
| S_INVEST_TXN_EDIT@INSERT / @EDIT | investment transaction form | InvestmentTransactionEditActivity | intent action | INVEST |
| S_INVEST_TXN_EDIT_PAUSED | calculator on top | same | – | INVEST |
| S_DLG_DATE@INVEST / @PRICE | date | DatePickerDialog | – | INVEST |
| S_PRICE_EDIT | price form (amount, date, prev/next) | PriceEditActivity | – | INVEST |
| S_PRICE_EDIT_PAUSED | calculator on top | same | – | INVEST |

**BRS.**

| Page | Description | Window class | Mode predicate | Area |
|---|---|---|---|---|
| S_BUDGETS | budget list + FAB | BudgetsActivity + BudgetListFragment | ≥1 budget (S_BUDGETS_EMPTY otherwise) | BRS |
| S_BUDGET_CTX | Edit / Delete | context menu | – | BRS |
| S_DLG_BUDGET_DELETE | confirm | AlertDialog (:253) | – | BRS |
| S_BUDGET_DETAIL | budget lines | BudgetsActivity + BudgetDetailFragment | simple view pref | BRS |
| S_BUDGETS_PAUSED | editor on top | BudgetsActivity | – | BRS |
| S_BUDGET_EDIT@INSERT / @EDIT | year / month fields | BudgetEditActivity | intent action | BRS |
| S_DLG_BUDGET_YEAR / S_DLG_BUDGET_MONTH | pickers | AlertDialog (:113 / :143) | – | BRS |
| S_SEARCH | search parameters + Clear + Search | SearchActivity + SearchParametersFragment | parameters shown | BRS |
| S_SEARCH_RESULTS | results list (+ QIF export menu) | SearchActivity + AllDataListFragment | after search | BRS |
| S_SEARCH_PAUSED | picker / calculator / editor on top | SearchActivity | – | BRS |
| S_DLG_DATE@SEARCH_FROM / @SEARCH_TO | dates | DatePickerDialog | – | BRS |
| S_REPORT_CATEGORIES@ALL / @WITHDRAWAL / @DEPOSIT | category totals + chart + period menus | CategoriesReportActivity + CategoriesReportFragment | `REPORT_FILTERS` extra | BRS |
| S_REPORT_PAYEES | payee totals | PayeesReportActivity + PayeeReportFragment | – | BRS |
| S_REPORT_PIE@CATEGORIES / @PAYEES | pie chart | PieChartFragment | after chart | BRS |
| S_DLG_REPORT_DATES@CATEGORIES / @PAYEES | custom date range | AlertDialog (BaseReportFragment:277) | – | BRS |
| S_REPORT_IVE | yearly / monthly table + sort / chart / period | IncomeVsExpensesActivity + IncomeVsExpensesListFragment | – | BRS |
| S_REPORT_IVE_CHART | bar chart | IncomeVsExpensesChartFragment | after chart | BRS |
| S_DLG_IVE_YEARS | year selection | AlertDialog (:290) | – | BRS |
| S_REPORT_CATEGORIES_PAUSED / S_REPORT_PAYEES_PAUSED / S_REPORT_IVE_PAUSED | search on top | report activity | – | BRS |

**SETSYNC.**

| Page | Description | Window class | Mode predicate | Area |
|---|---|---|---|---|
| S_SETTINGS | settings hub (10 rows) | SettingsActivity + SettingsFragment | no `EXTRA_FRAGMENT` | SETSYNC |
| S_SETTINGS_PAUSED | sub-screen on top | SettingsActivity | – | SETSYNC |
| S_SETTINGS_GENERAL@TUTORIAL / @SETTINGS | general preferences | GeneralSettingsActivity + GeneralSettingsFragment | caller (result consumer) | SETSYNC |
| S_SETTINGS_PERDB | per-database preferences | SettingsActivity + PerDatabaseFragment | `EXTRA_FRAGMENT` = PerDatabaseFragment | SETSYNC |
| S_SETTINGS_PERDB_PAUSED | currency picker on top | SettingsActivity | – | SETSYNC |
| S_SETTINGS_LOOK / S_SETTINGS_BEHAVIOUR / S_SETTINGS_INVEST / S_SETTINGS_BUDGET | preference screens | respective activity + fragment | – | SETSYNC |
| S_SETTINGS_SECURITY@NO_PASSCODE / @HAS_PASSCODE | security preferences | SecuritySettingsActivity + fragment | `Passcode.hasPasscode()` (enabled items, onResume 155-166) | SETSYNC |
| S_SETTINGS_SECURITY_PAUSED | passcode on top | same | – | SETSYNC |
| S_SETTINGS_DATABASE | database preferences | DatabaseSettingsActivity + fragment | – | SETSYNC |
| S_SETTINGS_DATABASE_PAUSED | SAF backup on top | same | – | SETSYNC |
| S_SETTINGS_SYNC@DISABLED / @ENABLED | sync preferences | SyncPreferencesActivity + SyncPreferenceFragment | `pref_sync_enabled` (dependents enabled) | SETSYNC |
| S_DLG_PREF_LIST@LOCALE / @THEME / @STATUS / @PAYEE / @SHOW_TXN / @FONT / @FONT_SIZE / @DEFAULT_ACCOUNT / @DATE_FORMAT / @FY_MONTH / @QUOTE_PROVIDER / @RATE_PROVIDER / @SYNC_INTERVAL | ListPreference dialogs | framework ListPreference dialog | which preference | SETSYNC |
| S_DLG_PREF_TEXT@USERNAME / @FY_DAY | EditTextPreference dialogs | framework | which preference | SETSYNC |
| S_DLG_BASE_CURRENCY | base-currency change confirm | AlertDialog (PerDatabaseFragment:328) | – | SETSYNC |
| S_DLG_TIME | notification time | TimePickerDialog (BehaviourSettingsFragment:106) | notifications on | SETSYNC |
| S_WIDGET_CONFIG | widget account chooser (external only) | SingleAccountWidgetConfigureActivity | – | SETSYNC |

**KIT.**

| Page | Description | Window class | Mode predicate | Area |
|---|---|---|---|---|
| S_TIPS@\<host\> | wildcard-search tip with "don't show again" | TipsDialogFragment | `pref_text_search_type == false` and not dismissed for good (`needs_state`) | KIT |

Non-interactive progress dialogs (price download, sync, currency import, CSV) are better treated as part of the `ASYNC` edge than as pages.

---

## 4. Framework mechanisms that need framework, async or lifecycle edges

| Mechanism | App classes (evidence) | Modeling note |
|---|---|---|
| **Content provider + loaders** (main data path) | `MmxContentProvider.query/insert/update/delete` with a UriMatcher over 21 datasets (J/MmxContentProvider.java:99-265; `notifyChange` 487-492). `MmxCursorLoader extends CursorLoader` (J/common/MmxCursorLoader.java). `LoaderCallbacks` in HomeFragment, AccountListFragment, AccountTransactionListFragment, AllDataListFragment, CategoryListFragment, PayeeListFragment, CurrencyListFragment, BudgetListFragment, BudgetDetailFragment, RecurringTransactionListFragment, BaseReportFragment (+ 2 subclasses), IncomeVsExpensesListFragment, PortfolioFragment, WatchlistItemsFragment, DashboardFragment (dead) | `initLoader/restartLoader` → `onCreateLoader` (FRAMEWORK) → `loadInBackground` (ASYNC, loader thread) → `ContentResolver.query` → provider `query` (FRAMEWORK, same process) → `onLoadFinished` (main thread). Writes call `notifyChange`, which reloads active loaders (FRAMEWORK, FW-MEMORY) |
| **Repositories / DB** | `RepositoryBase` (ContentResolver based, J/datalayer/RepositoryBase.java:47-246). `SqlRepositoryBase` on SqlBrite `BriteDatabase`, used synchronously (J/datalayer/SqlRepositoryBase.java:38-134; J/core/ioc/DbModule.java:53-70). `MmxOpenHelper` callback over SQLCipher `SupportFactory` (`onCreate/onUpgrade/onOpen`, J/database/MmxOpenHelper.java:94-154). Query datasets with raw SQL in `RES/raw/query_*.sql` | `onCreate`/`onUpgrade` are FRAMEWORK callbacks of `getReadable/WritableDatabase`: first open of an empty file, or a version below 19 |
| **Dagger 2** | `DaggerMmxComponent` (generated, 78 methods), `*_Factory`, `*_MembersInjector`, modules `MmxModule`, `DbModule`, `RepositoryModule`. `inject(this)` calls in about 35 classes (J/core/ioc/MmxComponent.java:66-123) | direct CALL chains in bytecode only; `Lazy.get()` → `Module_ProvideXFactory.get` → `provideX` |
| **ButterKnife** | `*_ViewBinding` + `$N extends DebouncingOnClickListener` (15 binding classes, incl. 5 for view holders). `@OnClick` in SelectDatabase, Tutorial, Passcode, BudgetEdit, InvestmentTransactionEdit, PriceEdit, SplitCategories, Calculator, SearchParameters | REGISTER in `X_ViewBinding.<init>` (from `ButterKnife.bind`); GUI → `X_ViewBinding$N.doClick` → CALL `X.onXxxClick` |
| **Icepick / Parceler** | `$$Icepick` (MainActivity, HomeFragment, AccountEdit, CheckingTxnEdit, RecurringEdit, AmountInputDialog, Calculator, EditPriceDialog) via `Icepick.restoreInstanceState` / `saveInstanceState` (J/common/MmxBaseFragmentActivity.java:74, 155). `$$Parcelable` for domain models and filters via `Parcels.wrap/unwrap` (reflection) | FRAMEWORK edges from `onCreate(savedState)` / `onSaveInstanceState`. Parcelable `writeToParcel` / `CREATOR.createFromParcel` run when Bundles or Intents are marshalled (FW-MEMORY); `describeContents` / `newArray` are likely FRAMEWORK_ONLY |
| **EventBus (greenrobot 3.3.1)** | register/unregister in `onStart/onStop` of MmxBaseFragmentActivity (141-147), HomeFragment, AccountTransactionListFragment, CurrencyListFragment, WatchlistFragment, SyncPreferenceFragment, EditPriceDialog, InvestmentSettingsFragment, PasscodeActivity. 29 `post` sites and 38 `@Subscribe` methods (grep over J/) | default `ThreadMode.POSTING` (FW-MEMORY), so `post` → subscriber is a synchronous CALL-like edge, guarded by "subscriber registered (started)". **Every registered subscriber of the type receives the event**, e.g. `AmountEnteredEvent` reaches HomeFragment, CheckingTransactionEditActivity, RecurringTransactionEditActivity, EditPriceDialog and InvestmentSettingsFragment if they are started. Model with `@CONTEXT` variants |
| **RxJava 1 (+ RxAndroid)** | `HomeFragment.loadUsername` (`Single`, io → main, J/home/HomeFragment.java:638-662); `CurrencyUIFeatures.importCurrencies` (Observable io → main, 226-250); `MorningstarPriceUpdater` (Retrofit Rx, 180-200); `UIHelper.binaryDialog` (Observable over an AlertDialog, 85-121; used by SyncPreferenceFragment, CurrencyUIFeatures); `MainActivity.onEvent(SyncStarting/Stopping)` (dead) | ASYNC edges with main-thread callbacks; disposed through `compositeSubscription.unsubscribe` in `onDestroy` (MmxBaseFragmentActivity.java:159-165) |
| **AsyncTask / executors / Handler** | `CalculateRunningBalanceTask2` (J/account/CalculateRunningBalanceTask2.java:51-104); `ExportToCsvFile` (dead, §5); `Executors.newSingleThreadExecutor` + `runOnUiThread` for the default payee (J/transactions/CheckingTransactionEditActivity.java:514-530); `Handler.postDelayed` for the drawer 200 ms (MainActivity.java:953, 975), report chart 1000 ms (CategoriesReportFragment:148-149, PayeeReportFragment:155-156, IncomeVsExpensesListFragment:189-190), list focus (AbsListFragment:41-50, ExpandableListFragment:56-59), SAF poll (FileStorageHelper:402-431); `SyncServiceMessageHandler extends Handler` over a `Messenger` from SyncService (J/sync/SyncManager.java:209-217; J/sync/SyncService.java:174-229) | ASYNC edges |
| **AlarmManager** | daily recurring check (J/core/RecurringTransactionBootReceiver.java:79-84); sync heartbeat `setInexactRepeating` (J/sync/SyncSchedulerBroadcastReceiver.java:70-90); delayed upload (J/sync/SyncManager.java:496-522, caller commented out) | SYSTEM/ASYNC edges with long delays; mark `needs_state` / env |
| **JobIntentService** | `RecurringTransactionIntentService`, `SyncService` (`enqueueWork`) | ASYNC to `onHandleWork` (worker thread, FW-MEMORY) |
| **WorkManager** | `DownloadWorker`, `SyncWorker`, `UploadWorker`: **never enqueued** (no WorkManager call in app code) | DEAD / FRAMEWORK_ONLY |
| **Sync adapter / authenticator** | `Authenticator`, `AuthenticatorService`, `SyncAdapter`, `SyncAdapterService` (`:sync` process), `StubSyncProvider`; trigger `SyncAdapterTrigger` unreferenced | FRAMEWORK_ONLY, except `StubSyncProvider.onCreate` at process start. The authenticator may appear in system Settings › Accounts (FW-MEMORY, UNVERIFIED) |
| **Broadcast receivers** | widgets (APPWIDGET_UPDATE from the launcher / AppWidgetService, plus self-broadcast refresh PendingIntents); boot receivers; explicit broadcasts from MainActivity (1245-1246) and SyncManager (268-290) | `ENTRY`/`SYSTEM` from outside; `INTENT` for explicit in-app broadcasts |
| **Notifications** | recurring (content intent → RecurringTransactionListActivity), sync (SyncNotificationFactory, SyncService:155-172, 251-265), SMS (SmsReceiverTransactions:1075-1090), channels (J/utils/NotificationUtils.java:44-98) | `ENTRY` from S_ENTRY ("tap notification") with `needs_state` |
| **Home-screen widgets** | 4 `AppWidgetProvider`s, `AccountBillsWidgetService` + `AllAccountBillsViewFactory` (RemoteViewsFactory), `SingleAccountWidgetConfigureActivity` | launcher-mediated; see the permission issue in §1.4 |
| **List/pager adapters** | CursorAdapter: AllDataAdapter, CurrencyListAdapter, PortfolioCursorAdapter, StocksCursorAdapter, Categories/Payee/IncomeVsExpenses report adapters. SimpleCursorAdapter: MoneySimpleCursorAdapter, BudgetAdapter, ToolbarSpinnerAdapter. BaseExpandableListAdapter: HomeAccountsExpandableAdapter, CategoryExpandableListAdapter, DrawerMenuGroupAdapter. ArrayAdapter: DrawerMenuItemAdapter. RecyclerView: SplitCategoriesAdapter, AttachmentAdapter (+ dead DrawerMenuItemRecyclerAdapter, CursorRecyclerViewAdapter, CurrencySection). ItemTouchHelper: SplitItemTouchCallback. Pagers: TutorialPagerAdapter (FragmentStatePagerAdapter), AboutTabAdapter (FragmentPagerAdapter) | count/view callbacks are FRAMEWORK on layout and data change; `getItem` of plain ListView adapters is usually not called by the framework (prompt §3 item 7; FW-MEMORY) |
| **ViewModel / LiveData / data binding** | no Jetpack ViewModel or LiveData. `BudgetViewModel extends BaseObservable` (used manually by BudgetEditViewHolder). Data-binding glue is generated (`DataBinderMapperImpl`, `BR`, `DataBindingTriggerClass`), but **no layout uses `<layout>`** (searched all `RES/layout*`) | generated mapper methods are FRAMEWORK_ONLY / DEAD candidates |
| **WebView** | HelpActivity (raw resource or URL), WebChangelogFragment (GitHub URL, online check), AboutCreditsFragment (raw HTML), TipsDialogFragment (raw HTML, J/fragment/TipsDialogFragment.java:91-115), WebViewActivity + MyWebChromeClient (dead). No `addJavascriptInterface` | – |
| **SAF / file pickers / sharing** | `FileStorageHelper` (OPEN/CREATE_DOCUMENT, GET_CONTENT fallback that is only reached on `ActivityNotFoundException`, 56-87, 368-389); DatabaseSettingsFragment backup (CREATE_DOCUMENT, 212-256); `MmxBaseFragmentActivity` result launchers `openDocumentLauncher` / `directoryPickerLauncher` (78-95; their launchers have **no callers**); `TextFileExport` (FileProvider + `ACTION_SEND` chooser, 150-166) for QIF and price CSV; AttachmentAdapter `ACTION_VIEW` (77-84) | external pages, blocked under `-p` |
| **Charts / calendar** | MPAndroidChart (PieChartFragment, IncomeVsExpensesChartFragment, `onValueSelected`/`onNothingSelected`); Caldroid (`CaldroidListener`, RecurringTransactionListFragment:389-411) | GUI edges via library callbacks |
| **Preferences framework** | `PreferenceFragmentCompat` subclasses; `OnPreferenceClick/ChangeListener` (§3.2) | change listeners fire only when the value changes (prompt §3 item 8) |
| **Network (Retrofit / HTTP)** | Morningstar, Yahoo YQL, Yahoo CSV, Fixer (`https://api.fixer.io`) price/rate updaters (J/investment/**, FixerService.java:132); Yahoo chart image (CurrencyChartActivity.java:85); Amplitude analytics (MmexApplication.java:147-156) | env-gated (§5.5) |
| **Fingerprint** | `FingerprintHandler extends FingerprintManager.AuthenticationCallback` (J/passcode/FingerprintHandler.java:18-63; PasscodeActivity.java:163-200) | hardware-gated callbacks |
| **Backup agent** | `MoneyManagerBackupAgentHelper` | `bmgr` only |

---

## 5. Unreachable-code candidates (evidence only; final verdicts are left to the graph builders)

### 5.1 Source classes with no reference at all

Method: a read-only script did a transitive reachability pass over the source classes.

- Roots: classes named in MAN or in `RES/layout*`, `xml*` and `menu*`, with comments stripped.
- Edges: textual class-name references, with comments stripped.

32 source files were not reached. Generated callers (Dagger, ButterKnife) live only in bytecode, but none of these classes has a generated user.

- `about/AboutChangelogFragment` — its use in `AboutTabAdapter` is commented out (AboutTabAdapter.java:52-54).
- `account/AccountSpinnerAdapter`
- `common/BaseRecyclerListFragment`
- `core/FilterDatePeriods`
- `currency/MmxExchangeRateProvider` — no class at all.
- `database/TableAssets`
- `home/DashboardFragment` (16 methods)
- `home/DrawerMenuItemRecyclerAdapter`
- `home/RecentDatabaseEntryComparator`
- `home/events/MessageEvent`
- `investment/dummy/DummyContent` (sample helper)
- `investment/prices/ExchangeRateUpdaterBase`
- `investment/prices/SecurityPriceUpdaterBase`
- `investment/watchlist/WatchlistDataset`
- `log/CrashReportingTree`
- `log/FileLoggingTree`
- `passcode/Encryptor` — only mentioned in a comment at Passcode.java:126.
- `passcode/InsecureSHA1PRNGKeyDerivator` — only used by `Encryptor`.
- `search/ParameterizedWhereClause`
- `sync/CloudItemViewHolder`
- `sync/CloudStorageProviderEnum`
- `sync/ICloudService`
- `sync/SyncCommon`
- `sync/adapter/SyncAdapterTrigger`
- `sync/jobmanager/DownloadWorker`
- `sync/jobmanager/SyncWorker`
- `sync/jobmanager/UploadWorker`
- `utils/DrawableUtils`
- `utils/MathUtils`
- `view/DateDisplay` — its tag in RES/layout/activity_price_edit.xml is inside a comment.
- `view/GestureWebView`
- `view/recycler/CursorRecyclerViewAdapter`

### 5.2 Classes referenced but never started or instantiated by live code

| Candidate | Evidence |
|---|---|
| `currency/recycler/*` (`CurrencyRecyclerListActivity`, `CurrencyRecyclerListFragment`, `CurrencySection`, `CurrencyListItemViewHolder`, `RecyclerItemClickListener`, `CurrencyContentObserver`), plus `view/recycler/ContextMenuRecyclerView`, `RecyclerViewContextMenuInfo`, `DividerItemDecoration` (only used there) | activity declared (MAN:359) but its start is commented out (MainActivity.java:645); about 60 methods |
| `investment/PortfolioActivity` | MAN:351-353 only; `PortfolioFragment` is shown inside MainActivity instead (MainActivity.java:791-798) |
| `common/WebViewActivity` + `core/MyWebChromeClient` | no `startActivity` anywhere (§3, intent scan) |
| `investment/EditPriceDialog` (+ `$$Icepick`, `_MembersInjector`, `EditPriceViewHolder` + binding) | only constants are used; `new EditPriceDialog()` is commented out (WatchlistItemsFragment.java:255) |
| `HelpActivity` (from the UI) | only `case R.id.menu_help`, which no drawer item produces (MainActivity.java:685-687, 1046-1125); exported, so external start only |
| `AccountListActivity`, `SingleAccountWidgetConfigureActivity` | no in-app starter; exported, so external only |
| Sync adapter: `Authenticator`, `AuthenticatorService`, `SyncAdapter`, `SyncAdapterService` | only `SyncAdapterTrigger` (unreferenced) requests a sync; FRAMEWORK_ONLY candidates |
| WorkManager workers | no `WorkManager`/`WorkRequest` call in app code (grep over J/) |
| Data binding glue (`DataBinderMapperImpl` ×2, `BR` ×2, `DataBindingTriggerClass`, `DataBindingComponent`) | no `<layout>` root in any `RES/layout*` |
| Phantom manifest components (6 asset-allocation activities, 2 DashClock services) | no class in the APK; starting them would throw `ClassNotFoundException` (FW-MEMORY) |

### 5.3 Dead through commented-out or missing callers (method or branch level)

- **Sync start/stop events.**
  - All calls to `SyncService.sendStartEvent/sendStopEvent` are commented out (J/sync/SyncService.java:95, 108, 116, 186, 198).
  - So `MainActivity.onEvent(SyncStartingEvent)`, `onEvent(SyncStoppingEvent)` and their `Callable`s never run (MainActivity.java:489-523).
  - `mIsSynchronizing` therefore never becomes true, and the sync branch of `onCreateOptionsMenu` (`createSyncToolbarItem`, `startSyncIconRotation`) is dead (372-384).
  - Also uncalled: `SyncService.showNotificationUploading/showNotificationUploadComplete`, `SyncManager.scheduleDelayedUpload/abortScheduledUpload` (callers commented at SyncManager.java:150, 220), `SyncCommon.getIntentForOpenDatabase`.
- **`MainActivity.onEvent(RequestOpenDatabaseEvent)`** (469-474): `RequestOpenDatabaseEvent` is never instantiated.
- **CSV export.** `R.id.menu_export_to_csv` appears only in `menu_main.xml` and `menu_search_transaction.xml`, and neither is ever inflated. So `AllDataListFragment.exportDataToCSVFile(×2)` (364-367, 464-480), `AccountTransactionListFragment` case `menu_export_to_csv` (303-307) and all of `core/ExportToCsvFile` are dead.
- **`AccountTransactionListFragment` case `menu_add_transaction_account`** (299-302): same reason; the FAB is the real "add".
- **`BudgetListFragment` case COPY:** its menu item is a todo, so the branch is dead (BudgetListFragment.java:164-200).
- **`SyncPreferenceFragment.onActivityResult` → `handleFileSelection`** (94-163): `REQUEST_REMOTE_FILE` is never requested (the start is commented at 200-203).
- **`MmxBaseFragmentActivity.onPermissionGranted` / `openDirectoryPicker`** (265-278): no callers, so their result lambdas (78-95) are FRAMEWORK_ONLY.
- **`FileStorageHelper`:** `showSelectLocalFileDialog` only runs on `ActivityNotFoundException` (66-70); `deleteRemoteFile` has no caller.
- **`Core.isToDisplayChangelog/showChangelog`:** the call is commented out (MainActivity.java:1491-1497).
- **`CurrencyListFragment.initializeSwipeToRefresh`** (494): no caller.
- **`MmexApplication.killApplication`, `onTerminate`** (FW-MEMORY: `onTerminate` never runs on devices).
- **`CheckingTransactionEditActivity.onEvent(AmountEnteredEvent)`** (206-216) and **`RecurringTransactionEditActivity.onEvent(AmountEnteredEvent)`** (219-225): the editors now use `CalculatorActivity`, and `AmountEnteredEvent` is only posted by an `AmountInputDialog` opened from Home or Investment settings while the editors are stopped. FRAMEWORK_ONLY candidates; split screen could change this (UNVERIFIED).
- **`MainActivity.onConfigurationChanged`** (364-368): MainActivity declares no `configChanges`, so FW-MEMORY says this is called only for non-relaunching changes such as a multi-window resize. Candidate FRAMEWORK_ONLY.
- **Name-based scan for uncalled methods.**
  - What it does: lists methods whose name is declared once and never appears as `name(` elsewhere in J/, excluding generated classes, `<init>`, lambdas and `on*` / adapter callback names.
  - Result: **97 candidates**, for example `AccountTransactionListFragment.populateRunningBalanceRx`, `AboutFragment.useProcessBuilder`, `RepositoryBase.bulkDelete/bulkUpdate`, `StockRepository.loadForSymbols`, `AccountService.createAccount`, `CategoryService.createNewSubcategory`, `MmxDate.getCalendar/getHour/getMinute/setCalendar/setTimeToEndOfDay`, `SearchViewFormatter` setters, `Attachment` setters.
  - Caveats: `DbModule/MmxModule/RepositoryModule.provide*` are called by generated factories, and `SyncServiceMessageHandler.handleMessage` and `WebViewActivity$1.shouldOverrideUrlLoading` are framework callbacks, so those are false positives.
  - Re-running the scan on bytecode (`javap -c`) is recommended before assigning DEAD.

### 5.4 Build-config and API-level gates (debug APK on API 27)

- `ScreenTree`, `SysLogTree` are planted only when `!BuildConfig.DEBUG` (MmexApplication.java:134-140), so they are dead in this build.
- `SimpleCrypto` is used only when `SDK_INT <= 23` (Passcode.java:104-105, 123-124), so it is unreachable on API 27.
- `MmxDatabaseUtils.resetContentProvider` `client.release()` branch (SDK < 24, 364-368): unreachable on API 27.
- `MmxFileUtils` `JELLY_BEAN` check and `PasscodeActivity` `JELLY_BEAN` check: always true.
- `FingerprintManager` (API 23+) is used without a guard (PasscodeActivity.java:163-200). The fingerprint branch needs AVD fingerprint support (FW-MEMORY: `adb emu finger touch`).
- Tablet-only branches (`fragmentDetail` visible: RES/layout-sw600dp-land/main_activity.xml, activity_budgets.xml, search_activity.xml, report_chart_fragments_activity.xml) are unreachable on a phone AVD. Examples: `MainActivity.handleDeviceRotation` back-stack pop, `BudgetsActivity`/`SearchActivity` dual panel, report `fragmentChart`.

### 5.5 Environment-gated features

| Feature | Gate |
|---|---|
| Price / exchange-rate download (Morningstar `http://quotes.morningstar.com`, Yahoo YQL `https://query.yahooapis.com`, Yahoo CSV `https://download.finance.yahoo.com`, Fixer `https://api.fixer.io`; MorningstarPriceUpdater.java:292, YqlSecurityPriceUpdaterRetrofit.java:210, YahooCsvQuoteDownloaderRetrofit.java:131, FixerService.java:132) | network; these services are probably defunct, so success callbacks and `PriceDownloadedEvent` handling may never run (UNVERIFIED; no network check was done) |
| `CurrencyChartActivity` image (Yahoo chart URL, :85); `WebChangelogFragment` (GitHub); About links; Amplitude | network / browser (external) |
| SMS auto-transactions (`SmsReceiverTransactions`, 18 methods) | `RECEIVE_SMS` not requested (MAN:36-38), so FW-MEMORY says the system never delivers `SMS_RECEIVED`; also `pref_sms_auto_trans` defaults to false |
| Widgets (4 providers, RemoteViews factory, configure activity) | launcher outside the package; `AccountBillsWidgetService` permission issue (§1.4) |
| Launcher shortcut | launcher long-press |
| Sync (SyncManager / SyncService / receivers / notifications) | `remotePath` set (SAF), sync enabled, online, alarms |
| Recurring notification + alarm | `pref_repeating_transaction_notifications` (default true), a due recurring transaction, alarm time (default 08:00) or the MainActivity start path |
| Boot receivers | device reboot (FW-MEMORY: `BOOT_COMPLETED` is protected and cannot be sent from shell without root) |
| Backup agent | `bmgr` |
| Passcode / fingerprint | passcode set in Security settings; fingerprint hardware |
| Attachments (`AttachmentAdapter`) | ATTACHMENT rows in the DB (desktop MMEX feature) plus an external viewer |
| Investments | an Investment account with stocks; price providers above |

### 5.6 Hazards that affect "reachable" (from reading the code, not reproduced)

- `EditTransactionCommonFunctions.initAttachmentControls` throws when the current DB's `remotePath` is `""` (735-736). That is the case for any DB not opened through SAF:
  - prefs-seeded DBs;
  - VIEW-intent DBs (`DatabaseMetadataFactory.getInstance` sets `remotePath=""`, DatabaseMetadataFactory.java:36-41);
  - the default DB created implicitly by `DatabaseManager.getDatabasePath` (DatabaseManager.java:38-67) when an exported activity, the shortcut or a widget touches the DB first.
  
  It is called from `CheckingTransactionEditActivity.onCreate` (383), so every new/edit-transaction path would crash.
- `CurrencyListFragment.onCreate` throws an NPE when started without an intent action (92-93); this can only happen via an external `am start`.
- `MainActivity.onKeyDown` dereferences `mDrawer` without a null check (407-418). On a tablet layout without a drawer the hardware MENU key would crash (UNVERIFIED).
- Typing a non-empty password in PasswordActivity during "Create database" probably SQLCipher-encrypts the new `.mmb`; later processes have an empty password and cannot open it (§2.1, step 5).
- `MainActivity.populateScheduledTransactions` inserts every due recurring transaction at each MainActivity creation (1261-1284). This changes the data during exploration.

---

## 6. Decomposition into 8 areas

Method counts are JaCoCo method entries (MK), JacocoInstrument excluded. "gen" = methods in generated classes (`_ViewBinding`, `_MembersInjector`, `*Factory`, `DaggerMmxComponent`, `$$Icepick`, `$$Parcelable`, BR, DataBinder*, BuildConfig). Class files are counted from the classes directory (825 = 822 + 3 harness).

| Area | Owns (by package / class) | Class files (top-level) | Methods (hand / gen) | Pages owned (§3.4) | Entry edges from other areas | Notes |
|---|---|---|---|---|---|---|
| **SHELL** – app shell, onboarding, DB selection | `MmexApplication`, `HelpActivity`, `PasscodeActivity`; `home/**` (MainActivity, HomeFragment, drawer adapters and items, DatabaseMetadata*, RecentDatabasesProvider, SelectDatabaseActivity, DashboardFragment, `home/events`); `tutorial/**`; `about/**`; `passcode/**`; `core/Passcode`; `core/docstorage/**`; `core/database/DatabaseManager`; `database/PasswordActivity`; `common/WebViewActivity`; `core/MyWebChromeClient`; `view/GestureWebView` | 93 (58) | 500 (451 / 49) | S_ENTRY, S_EXIT, S_SAF_PICKER, S_EXT_APP, S_LIB_ACTIVITY, tutorial, select-DB, password, passcode, Home (empty / non-empty, ctx), drawer, About ×4, help, S_MAIN_PAUSED, … | `ENTRY` (launcher, VIEW intent); from SETSYNC: Tutorial ↔ General settings, Settings › About, Security → Passcode, `setRestartActivity`, widgets / sync notification → MainActivity, `SyncManager.useDownloadedDatabase` → `IntentFactory.getMainActivityNew`; from TXN: RecurringTransactionListActivity → Passcode | owns **the MainActivity host**: `showFragment*`, drawer dispatch and the EventBus navigation subscribers. Other areas' fragments are entered through it |
| **TXN** – accounts, transactions, recurring, notifications | `account/**`; `transactions/**`; `common/AllDataListFragment`, `AllDataMultiChoiceModeListener`, `IAllDataMultiChoiceModeListenerCallbacks`, `AmountInputDialog`, `Calculator`, `CalculatorActivity`, `CommonSplitCategoryLogic`, `common/events/AmountEnteredEvent`; `adapter/AllDataAdapter`, `AllDataViewHolder`; `viewmodels/AccountTransactionDisplay`; `servicelayer/AccountService`, `RecurringTransactionService`, `servicelayer/qif/**`; `core/ExportToCsvFile`, `core/RecurringTransactionBootReceiver`; `recurring/**`; `notifications/**` (recurring + SMS) | 161 (73) | 858 (771 / 87) | accounts, account edit, account txns (+ empty), list select (`@ACCOUNT` / `@SEARCH`), txn dialogs, TXN edit ×3 modes, split, calculator, amount dialog, recurring list / ctx / calendar / activity / edit ×3 | from SHELL (drawer Accounts / Recurring, Home FAB / child click / ctx / welcome, `populateScheduledTransactions`); from BRS (search results use `AllDataListFragment`, search uses Calculator); from INVEST (Calculator, AccountEdit from header); from SETSYNC (widgets → editor, Investment settings → AmountInputDialog); `ENTRY` (shortcut, recurring notification, SMS, boot) | largest area; consider two agents (accounts + txn editor, recurring + notifications) that share `EditTransactionCommonFunctions` variants |
| **MASTER** – categories, payees, currencies | `PayeeActivity`; `common/CategoryListActivity`, `CategoryListFragment`; `adapter/CategoryExpandableListAdapter`, `CategoryListItemViewHolder*`; `fragment/PayeeListFragment`; `servicelayer/CategoryService`, `PayeeService`; `currency/**` (incl. `CurrencyService`, `CurrencyRepository`, `recycler/**` dead); `investment/prices/FixerService`, `IFixerService`, `IExchangeRateUpdater`, `ExchangeRateUpdaterBase`; `investment/ExchangeRateProviders` | 69 (34) | 317 (307 / 10) | categories (+ pick, ctx, 4 dialogs), payees (+ pick, ctx, 2 dialogs), currencies (+ pick, ctx, 3 dialogs), currency edit, chart | from SHELL drawer (Categories, Payees, Currencies); from TXN (payee / category / currency pickers); from BRS (search pickers); from SETSYNC (base currency pick, currency list) | **`CurrencyService` is a shared service**, used for formatting by HomeFragment, widgets, `FormatUtilities` and `MmxOpenHelper`. MASTER defines its nodes and callers add CALL edges |
| **INVEST** – investments | `investment/**` except the exchange-rate classes above (watchlist, portfolio, edit activities, price updaters Morningstar / YQL / Yahoo CSV, PriceUpdaterBase, events, dummy, `EditPriceDialog` dead); `core/bundlers/PriceDownloadedEventBundler` | 89 (46) | 337 (272 / 65) | watchlist (+ empty, ctx, 4 dialogs), portfolio, investment txn edit, price edit, date pickers | from SHELL (Home child click on an Investment account → `RequestWatchlistFragmentEvent`; ctx "Portfolio"); reads SETSYNC investment settings | depends on network services (§5.5) |
| **BRS** – budgets, reports, search | `budget/**`, `reports/**`, `search/**`, `viewmodels/IncomeVsExpenseReportEntity` | 67 (40) | 346 (303 / 43) | budgets (+ ctx, detail, edit, dialogs), search params / results, 3 reports (+ pie / bar, date dialogs) | from SHELL drawer (Budgets, Search, Reports ×5) + Home search menu + income/expense card; from MASTER "View transactions" → `IntentFactory.getSearchIntent` | `BudgetQuery` is instantiated by `MmxContentProvider.onCreate` (DATA → BRS edge) |
| **SETSYNC** – settings, sync, widgets | `settings/**`, `sync/**` (incl. `adapter/`, `jobmanager/`, `events/`), `widget/**`, `core/MoneyManagerBackupAgentHelper` | 130 (73) | 509 (450 / 59) | settings hub + 9 screens, preference dialogs, time picker, widget config, S_HOME_WIDGETS | from SHELL (drawer Settings / Synchronize, welcome Settings button, Tutorial "Close", `initializeSync`); from DATA (`MmxOpenHelper.onUpgrade` → `SyncManager.dataChanged`, J/database/MmxOpenHelper.java:128-130); `ENTRY` (widgets, boot, deep link, backup) | settings `*Settings` classes (`AppSettings` …) are read everywhere: SETSYNC owns them, callers add CALL edges |
| **DATA** – database layer | `MmxContentProvider` (+ injector); `database/**` except PasswordActivity; `datalayer/**`; `domainmodel/**` (+ `$$Parcelable`); `servicelayer/ServiceBase`, `InfoService`; `info/javaperformance/money/Money$$Parcelable` | 87 (64) | 663 (539 / 124) | none | every area (repositories, `ContentResolver` → provider, `InfoService`); `ENTRY` (provider `onCreate` at process start) | mostly CALL edges and getter/setter verdicts; good candidate for automated extraction |
| **KIT** – DI, base UI classes, utilities, logging, generated glue | `BR`, `BuildConfig`, `Constants`, `DataBinderMapperImpl`, `DataBindingTriggerClass`, `androidx/databinding/**`; `core/**` not listed above (Core, UIHelper, FormatUtilities, IntentFactory, MenuHelper, NumericHelper, AbsListFragment, DefinedDateRange*, …, `core/ioc/**`, `core/bundlers/MoneyBundler`, `core/file/TextFileExport`); `common/MmxBaseFragmentActivity`, `BaseListFragment`, `BaseExpandableListFragment`, `ExpandableListFragment`, `BaseRecyclerListFragment`, `MmxCursorLoader`, `MoneyParcelConverter`, `common/events/ListItemClickedEvent`; `fragment/TipsDialogFragment`; `adapter/MoneySimpleCursorAdapter`; `utils/**`; `view/**` except GestureWebView; `log/**` | 126 (94) | 739 (560 / 179) | S_TIPS@… | everyone: base-class lifecycle (`super.onCreate` …), `UIHelper`, `Core`, Dagger `inject`, Timber `log` → `ErrorRaisedEvent` → `MmxBaseFragmentActivity.onEvent` toast | owns **singletons and base classes**. Lifecycle methods of base classes get per-page `@CONTEXT` variants supplied by the caller areas |

**Assignment check.** Every one of the 825 class files maps to exactly one area under the package/class rules in the table: SHELL 93, TXN 161, MASTER 69, INVEST 89, BRS 67, SETSYNC 130, DATA 87, KIT 126, harness 3. **Leftovers: none** (script over the classes directory). The only hand-picked exceptions to "class goes with its package" are:

- `PayeeActivity` → MASTER;
- `PasswordActivity`, `Passcode`, `WebViewActivity`, `MyWebChromeClient`, `GestureWebView` → SHELL;
- the exchange-rate classes in `investment/prices` and `ExchangeRateProviders` → MASTER;
- `PriceDownloadedEventBundler` → INVEST;
- the `common` / `adapter` / `servicelayer` / `viewmodels` / `core` splits listed above.

**Cross-area conventions (to keep agents independent).**

1. The area that owns the *source* method writes the edge. Destination names come from §3.4 and from the callee area's class list.
2. Owners of shared callees publish these variants up front so callers can link to them before the callee is modeled:
   - `MainActivity.showFragment_Internal@<page>`;
   - `AllDataListFragment.*@ACCOUNT/@SEARCH`;
   - `CalculatorActivity.*@<caller>`;
   - `AmountInputDialog.*@BALANCE/@THRESHOLD`;
   - `PasscodeActivity.*@<caller>`;
   - `PasswordActivity.*@<caller>`;
   - `CategoryListFragment.*@MAIN/@PICK`;
   - `PayeeListFragment.*@MAIN/@PICK`;
   - `CurrencyListFragment.*@EDIT/@PICK`;
   - `GeneralSettingsActivity.*@TUTORIAL/@SETTINGS`;
   - `EditTransactionCommonFunctions.*@TXN/@RECURRING`.
3. EventBus `post` → `onEvent` edges are written by the poster's area. The subscriber's area marks "registered between `onStart`/`onStop`" as the guard.
4. Base-class lifecycle (KIT) and Dagger chains (KIT/DATA) are written once by their owners. Feature areas only add the edge from their own `onCreate` to `MmxBaseFragmentActivity.onCreate@<page>`.

---

## 7. Baseline coverage by area and screen

### 7.1 Methods hit (JaCoCo METHOD counter covered > 0)

| Area | Methods | Both | Monkey only | APE only | Neither | What was hit |
|---|---|---|---|---|---|---|
| SHELL | 500 | 72 | 10 | 1 | 417 | MmexApplication 15/27 (`generateAndStoreUUID` APE-only); MainActivity gate part 10/79 (+ `$$Icepick` 3, injector 1); SelectDatabaseActivity 5/7 (+ binding 5, injector 1); PasswordActivity 6/6; tutorial 32 methods (activity 7/7, binding 3/5, 5 fragments, pager adapter 3/4); FileStorageHelper 3/25; RecentDatabasesProvider_Factory 2 |
| TXN | 858 | 0 | 0 | 0 | 858 | nothing |
| MASTER | 317 | 3 | 0 | 0 | 314 | `CurrencyRepository.<init>` (provider `onCreate`), `CurrencyService_Factory` (Dagger build) |
| INVEST | 337 | 0 | 0 | 0 | 337 | nothing |
| BRS | 346 | 2 | 0 | 0 | 344 | `BudgetQuery.<init>/<clinit>` (provider `onCreate`) |
| SETSYNC | 509 | 49 | 0 | 1 | 459 | AppSettings / GeneralSettings / BehaviourSettings / DatabaseSettings / SettingsBase getters and setters; GeneralSettingsActivity 3/3; GeneralSettingsFragment 15/15 (`$4.onPreferenceChange` APE-only); BaseSettingsFragmentActivity 3/4; StubSyncProvider 2/7 |
| DATA | 663 | 39 | 0 | 0 | 624 | repository and dataset constructors from `MmxContentProvider.onCreate` (5/20), `Dataset` 4/7, `SplitCategory` / `SplitRecurringCategory` `<clinit>` |
| KIT | 739 | 87 | 0 | 8 | 644 | Dagger component and module factories 42; Core 4/22; UIHelper 7/31 (toast path APE-only: `showToast` ×2, `getContext`, `$3`); MmxBaseFragmentActivity 11/26 (`onEvent`, `onOptionsItemSelected` APE-only); MmxFileUtils 6/8; Roboto* 14; DebugTree 2/2; ErrorRaisedEvent (APE-only); BuildConfig |
| **Total** | **4269** | **252** | **10** | **10** | **3997** | Monkey 262, APE 262, either 272 (matches the brief) |

- **Monkey-only (10):** `TutorialActivity.onCreateOptionsMenu`, `TutorialActivity.onOptionsItemSelected` (hardware MENU panel), and `TutorialFinancialOverviewFragment` / `TutorialSyncFragment` (`newInstance`, `<init>`, `onCreate`, `onCreateView`). Monkey swiped to pages 4-5; APE did not.
- **APE-only (10):** `MmexApplication.generateAndStoreUUID`, `MmxBaseFragmentActivity.onEvent(ErrorRaisedEvent)` and `onOptionsItemSelected` (Up in General settings), `UIHelper.getContext`, `showToast(String)`, `showToast(String,int)`, `UIHelper$3.<init>/run`, `ErrorRaisedEvent.<init>`, `GeneralSettingsFragment$4.onPreferenceChange`.

### 7.2 Screens never reached and the likely reason

| Area | Never reached | Reason |
|---|---|---|
| SHELL | Home (empty and full), Home context menu, drawer, About (4 tabs), Help, Passcode, SAF picker | G2 (no DB): MainActivity returns at J/home/MainActivity.java:184-187 before `setContentView`; SAF picker blocked by `-p` (FW-MEMORY); Passcode needs a passcode in the DB; Help has no UI entry |
| TXN | all screens (accounts, transaction lists and editors, split, calculator, recurring, notifications) | G2. After G2: G6 (needs accounts) for lists and the editor; recurring notification needs a due recurring transaction + alarm; SMS needs `RECEIVE_SMS` (absent) |
| MASTER | categories, payees, currencies, currency edit and chart | G2. Chart and rate update also need network services that are probably defunct |
| INVEST | watchlist, portfolio, investment / price editors | G2, then an Investment account with stocks; price download needs network |
| BRS | budgets, search, all reports and charts | G2; meaningful content needs transactions and budgets |
| SETSYNC | settings hub and all sub-screens except General, sync screen, widgets, widget config | G2 for the hub (only reachable from the drawer or Home welcome); General was reached only through the tutorial; widgets need the launcher; sync needs a SAF remote |
| DATA | every query / insert / update path, `MmxOpenHelper` | the database was never opened (`DatabaseManager` 0/8, `MmxOpenHelper` 0/19) |
| KIT | list base classes, tips dialog, utilities used by feature screens | follow from the above |

---

## 8. Conclusions and recommendations

1. **Re-run the baseline with a prepared database** (Recipe A or B, §2.5) before computing targets.
   - The present data says almost nothing about TXN, INVEST, BRS, MASTER and most of SETSYNC.
   - Seed a **non-empty `remotePath`** or use the real SAF flow, otherwise the transaction editor crashes.
   - Keep the password empty and `prefshowtutorial=false`.
   - Pre-populate data (accounts of every type incl. Investment, transfers, splits, recurring due, budget, stocks).
   - Install with `-g`.
   - Expect SAF / share / browser flows to stay blocked under `-p`.
2. **Modeling order:** DATA + KIT (mostly mechanical, can be script-extracted from bytecode), then SHELL (host, gates, drawer), then the feature areas in parallel. Split TXN into two agents if needed.
3. **Mandatory pseudo pages and states:** S_SAF_PICKER, S_EXT_APP, S_LIB_ACTIVITY, S_HOME_WIDGETS. Mark these edges `needs_state`:
   - after tutorial;
   - DB present;
   - accounts present;
   - Investment account;
   - passcode set;
   - due recurring transaction;
   - remote file set;
   - `pref_text_search_type` off;
   - static `PayeeListFragment.mAction == PICK` left over from an earlier picker in the same process.
4. **Verify before assigning verdicts:**
   - the 97 name-scan candidates on bytecode;
   - the FW-MEMORY claims: Monkey `-p` blocking DocumentsUI, `RemoteViewsService` permission, SMS delivery without `RECEIVE_SMS`, `onConfigurationChanged` without `configChanges`, `CHOICE_MODE_MULTIPLE_MODAL` long-press;
   - whether the price / rate endpoints still answer (needs network).
5. **Open questions (UNVERIFIED):** the exact baseline install flags (was `-g` used?); whether a 0-byte `.mmb` opens cleanly through SQLCipher `SupportFactory` with an empty key (the app's own create path relies on it); the `SyncPreferences.getKey` prefixing of sync pref keys; AVD screen size (phone layout assumed throughout).



