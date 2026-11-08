# hash-checker v3.7.3: UI map and modeling plan (read-only investigation)

App `com.smlnskgmail.jaman.hashchecker.thirdparty` (flavor thirdPartyStores, debug build). Brief: `work/.agents/tasks/ui-map-brief-hash-checker.md`.

## Summary

- **One activity, five fragments, many overlays.** `MainActivity` stacks five fragments on `android.R.id.content` with `add()` + `addToBackStack()`: calculator, history, settings, feedback and web view. Everything else is an overlay: 8 bottom sheets, a text-input dialog, 4 uses of one alert-dialog helper, a progress dialog, snackbars, and system windows (SAF pickers, browser, email chooser). The app has no services, no app receivers (only the coverage harness), no app providers, no widgets, no runtime-permission prompts, no accounts and no onboarding. The main screen works on first launch.
- **Proposed pages: 40.** 7 pseudo pages (entry, exit, five `_PAUSED` states), 5 external/system windows, and 28 in-app pages. The modes are: which source is selected (none, text, file or folder), whether a result is shown, generating, history loading/empty/list, and feedback typed.
- **Why 661 methods in the class files but 525 in JaCoCo.** JaCoCo drops 138 class-file methods: 114 Dagger `@DaggerGenerated`, 14 enum `values`/`valueOf`, 6 private empty constructors, 2 empty enum constructors, and 2 `<clinit>` of synthetic switch-map classes. It also counts the 2 `BuildConfig` methods that the recipe excludes. So 661 − 138 + 2 = 525.
- **Static DEAD / FRAMEWORK_ONLY candidates: 81 method nodes.**
  - 54 Dagger factory/injector instance methods.
  - 7 constructors of static-only classes.
  - 7 enum synthetic methods.
  - `OrmLiteConfigUtil` (2), `DbEntity.get/setId`, `HistoryItem.equals/hashCode`.
  - 3 base methods that every subclass overrides.
  - The googlePlay-only rate listener.
  - `App.onTerminate`, `releaseHelper`, `onUpgrade`.
- **No baseline run ever computed a hash.** Every method Monkey hit was also hit by APE. The 66 JaCoCo methods of the hash engine are unhit. The likely gates:
  - The SAF pickers belong to another package. Both runs used `-p <app>` only, and `onActivityResult` never got any data.
  - The text path needs From → Text → type → Add → Action → Generate in one fragment lifetime.
  - History rows, export and the rate dialog all need stored hashes first.
- **Coverage-harness artifacts.**
  - `merged.ec` leaves out segment `00000`, the launch before the tool starts. So 8 first-launch-only methods look "missed" by Monkey.
  - Coverage of a process that dies between the 30-second dumps is lost (APE: 45 process starts, Monkey: 8). APE showed history rows although no hash generation was ever recorded.
- **One agent is enough.** About 858 direct app→app call pairs can be pulled from the bytecode, and the Dagger and engine parts are mechanical. If you want two agents in parallel, split into UI (70 classes, 349 method nodes) and CORE (57 classes, 312 method nodes).

## Conventions

Path abbreviations:
- `J/` = `/Users/darshan/Desktop/yang/work/final_java_only/hash-checker/app/hash-checker-#v3.7.3/app/src/main/java/com/smlnskgmail/jaman/hashchecker/`
- `T/` = `.../app/src/thirdPartyStores/java/com/smlnskgmail/jaman/hashchecker/` (contains only `MainActivity.java`, the compiled flavor copy)
- `R/` = `.../app/src/main/res/`; `M` = `.../app/src/main/AndroidManifest.xml`; `DM` = `.../app/src/debug/AndroidManifest.xml`
- `C/` = `.../app/build/intermediates/javac/thirdPartyStoresDebug/classes/com/smlnskgmail/jaman/hashchecker/`
- `MK` / `AP` = `work/final_java_only/hash-checker/{monkey,ape}/report/report.xml`; `MSEG/n` / `ASEG/n` = `.../{monkey,ape}/coverage/n.ec` (30-second dumps)

Evidence labels:
- `SRC`: read in the app source; file:line given.
- `BC`: my own read-only scan of the `.class` files (constant pool, invoke and invokedynamic opcodes, CHA).
- `JAC`: report.xml.
- `SEG`: per-segment `.ec` parsing.
- `APK`: binary `AndroidManifest.xml` decoded from `hash-checker-v3.7.3-rebuilt.apk` in memory.
- `FW-MEMORY`: Android, androidx, Dagger, ORMLite or JaCoCo behaviour recalled but not checked against source.
- `INFERRED`, `UNVERIFIED`.

Method names follow the graph schema (`Class.method`, `Outer$Inner.method`, `<init>`). Line numbers are from `grep -n`/`awk`. The IDE search tool shows them off by one.

---

## 0. Method universe: 661 vs 525

Running `tools/list_methods.py C/.. --exclude JacocoInstrument --exclude BuildConfig` gives **661** method nodes: 31 lambdas, 107 constructors, 15 `<clinit>` and 508 others. JaCoCo reports **525** (both report.xml files have the same key set). `BC` diff:

| Group not in JaCoCo | # | Members | Why (JaCoCo filter, FW-MEMORY) |
|---|---|---|---|
| Dagger generated | 114 | `DaggerAppComponent` (30), 4 `*_…Factory` × 4 (16), 14 `*_MembersInjector` (68) | Each class carries `dagger.internal.DaggerGenerated` (byte string present in the 19 class files, `BC`). JaCoCo drops classes and methods annotated with a CLASS/RUNTIME annotation whose name contains "Generated". The `<class>` elements appear in report.xml with 0 methods. |
| enum `values()` / `valueOf(String)` | 14 | HashType, Language, Theme, Action, UserActionType, WebLink, SettingsPresenter$SaveUserDataResult | EnumFilter |
| private empty no-arg constructors | 6 | `UIUtils`, `AppUtils`, `WebUtils`, `JdkHashUtils`, `JdkHashCalculatorDigest`, `DaggerAppComponent$Builder` | PrivateEmptyNoArgConstructorFilter |
| empty enum constructors `<init>(String,int)` | 2 | `UserActionType`, `SaveUserDataResult` | EnumEmptyConstructorFilter |
| `<clinit>` of synthetic classes | 2 | `HashCalculatorFragment$2`, `SettingsFragment$1` (enum switch maps, class flags `0x1020` = synthetic, `BC`) | JaCoCo skips synthetic classes |
| **Total** | **138** | | |

JaCoCo also has `BuildConfig.<init>` and `BuildConfig.<clinit>`, which the recipe leaves out. So 661 − 138 + 2 = 525. Consequence: these 138 nodes get blank Monkey/APE flags in `methods.csv` (HANDOFF convention) and can never become targets. 60 of the 114 Dagger methods are reachable (§5.1).

---

## 1. Entry points

`build/` has only `intermediates/javac/`, so there is no merged manifest. I decoded the APK's binary manifest (`APK`) and cross-checked it with `M` and `DM`. No flavor manifest exists: `src/thirdPartyStores` has Java only.

| Component | Kind | exported | Intent filters / triggers | Attributes | Evidence |
|---|---|---|---|---|---|
| `.App` | Application | – | Process start by any component, including the harness broadcast | `allowBackup=false`, `resizeableActivity=true`, `supportsRtl`, theme `AppThemeLight` (overridden at run time, §2.1), `debuggable=true` | M:9-17; APK |
| `.MainActivity` | Activity (the only one) | **true** | **F1** MAIN + LAUNCHER, plus 3 custom actions `…ACTION_START_WITH_{TEXT,FILE,FOLDER}_SELECTION` (M:26-33). **F2** VIEW, DEFAULT + BROWSABLE, `scheme=content`, `host=*`, `mimeType=*/*` (M:35-44). **F3** SEND with category **LAUNCHER** (not DEFAULT), mime `application/*`, `audio/*`, `video/*`, `image/*` (M:46-54) | launchMode standard (no attribute), `screenOrientation=portrait` (M:22), `windowSoftInputMode=adjustPan` (M:23), no `configChanges`, no dialog theme | M:19-56; APK |
| `JacocoInstrument.SMSInstrumentedReceiver` | Receiver | true | `edu.gatech.m3.emma.COLLECT_COVERAGE` | Coverage harness, out of scope | M:59-64 |
| `androidx.startup.InitializationProvider` | Provider (library) | false | meta-data EmojiCompatInitializer, ProcessLifecycleInitializer | Library code, not modelled | APK |
| Dynamic launcher shortcuts | ShortcutManager | – | `shortcut_text`, `shortcut_file`, `shortcut_folder`: explicit Intent to MainActivity with action `ACTION_START_WITH_TEXT`/`_FILE`/`_FOLDER` | Created once (pref `shortcuts_created`), only on API ≥ 26 | `J/App.java:40-42, 76-79, 83-97, 137-150` |
| Permissions | – | – | VIBRATE (M:6). Debug only: DISABLE_KEYGUARD, WAKE_LOCK, INTERNET, WRITE/READ_EXTERNAL_STORAGE, CHANGE_CONFIGURATION (DM:6-14). Plus androidx `…DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION` | No runtime request in code (no `requestPermissions`/`checkSelfPermission` in J/ or T/, SRC grep) | M, DM, APK |

There are no services, widgets, search, http(s) deep links or static `shortcuts.xml`.

How `MainActivity.create()` (`T/MainActivity.java:68-94`) treats each entry:

1. **Launcher icon or restart** (action MAIN or null) → `getBundleForShortcutAction` sets no flag → `S_MAIN_EMPTY` (T:89-93, 113-123).
2. **Shortcut "Text"** → flag `ACTION_START_WITH_TEXT` → `HashCalculatorFragment.onViewCreated` calls `userActionSelect(ENTER_TEXT)` → `S_DLG_TEXT_INPUT` (T:116-117; `J/features/hashcalculator/HashCalculatorFragment.java:490-492`).
3. **Shortcut "File"** → `userActionSelect(SEARCH_FILE)` → SAF picker (T:118-119; HCF:493-495).
4. **Shortcut "Folder"** does nothing special in this flavor. `T/MainActivity.java:113-123` has no FOLDER branch, while the googlePlay copy has one (`src/googlePlay/.../MainActivity.java`, `switch` incl. `case ACTION_START_WITH_FOLDER`). So `startWithFolderSelection` is never true and the user lands on `S_MAIN_EMPTY` (HCF:496-498 is unreachable in this build).
5. **VIEW with scheme content or file** → `getConfiguredBundleWithDataUri(intent.getData())` + `setGenerateFromShareIntentMode(true)` → `onViewCreated` → `checkExternalDataPresence` → `validateSelectedFile` → `S_MAIN_FILE` (T:82-86, 106-110; HCF:501-504, 539-546, 316-323). A `file://` URI needs an explicit component (F2 lists only `content`).
6. **SEND with ClipData** → `clipData.getItemAt(0).getUri()`, then the same path as 5 (T:74-78, 87-89).
   - Implicit SEND and the share sheet need CATEGORY_DEFAULT, which F3 lacks (M:48), so the app is not offered as a share target. FW-MEMORY.
   - `adb am start` does not fill ClipData: the EXTRA_STREAM → ClipData migration happens in the sending app's Instrumentation. FW-MEMORY.
   - So the ClipData branch needs a helper app that sends an explicit SEND. UNVERIFIED.
7. **The `*_SELECTION` actions in F1** (M:28-30) are not the actions the code compares against (App.java:40-42, T:116-119). They are inert.

---

## 2. First-run flow and setup gates

### 2.1 What happens on first launch

`App.onCreate` (`J/App.java:53-81`) runs, in order:
- registers `KeccakjProvider` (55);
- creates the ORMLite helper without opening the DB (56);
- creates `SharedPreferencesSettings` and `LanguageConfigImpl` (57-67);
- calls `setTheme(getSelectedTheme())` (68). The default theme is **DARK** (`J/components/settings/impl/SharedPreferencesSettings.java:109, 119`), not the manifest's Light;
- builds Dagger (69-75);
- creates shortcuts once (76-79);
- calls `setLocale()` (80). On first run this compares `Locale.getDefault().toString()` with `Language.code()` and falls back to EN (152-167). An "en_US" device therefore gets EN (INFERRED from code).

Then `MainActivity.onCreate` injects, applies the language (`J/ui/BaseActivity.java:17-19`), calls `create()` and shows the calculator.

There is no intro, no permission prompt, no account and no data import. The DB file is created at the first DAO use (`OrmLiteLocalDataStorage.onCreate`, `J/components/localdatastorage/impl/ormlite/OrmLiteLocalDataStorage.java:43-53`; FW-MEMORY: `SQLiteOpenHelper` calls onCreate on the first open).

### 2.2 Functional gates inside the app

| Gate | Enforced by (SRC) | Blocks |
|---|---|---|
| A source must be selected (text, file or folder) | HCF:216 / 244-246 (`generateHash`), 266-270 (export) | Engine, result, export, rate, history rows |
| File and folder sources come only from the SAF pickers (DocumentsUI, another package) or from VIEW/SEND | HCF:191-201, 203-213 (pickers), 585-607 (`onActivityResult` needs `data != null` and `RESULT_OK`) | `S_MAIN_FILE`/`S_MAIN_FOLDER`, the file and folder engine paths |
| Export ".txt" needs a source, a non-empty generated field, and a document from the SAF create dialog | HCF:265-291, 593-598 | `writeHashToFile` |
| Compare needs both EditTexts non-empty | HCF:249-258 | match / no-match branch (the user can type in both fields) |
| Copy and clear icons show only for a non-empty field (INVISIBLE otherwise; FW-MEMORY: INVISIBLE views take no touches) | HCF:515-529, 531-537 | copy and clear lambdas |
| History rows need at least one generation with "Save result to History" on (default true) | HCF:118-130; SharedPreferencesSettings.java:85-90; `R/xml/settings.xml:18-22` | `S_HISTORY_LIST`, the clear-dialog OK, export user data |
| Export user data needs at least one row. The method name is inverted: `isHistoryItemsListIsEmpty()` returns `countOf() > 0` | `J/features/settings/presenter/SettingsPresenterImpl.java:43-57`; OrmLite…:107-115 | `S_EXT_CREATE_ZIP`, `copyUserDataToUserFolder` |
| The rate dialog shows only when the counter equals 5, i.e. at the 6th successful generation, once | HCF:131-146; SharedPreferencesSettings.java:198-212; `J/components/settings/api/Settings.java:13` | `S_DLG_RATE_APP`, `WebUtils.openGooglePlay` |
| Theme dialog only when the tapped theme differs from the current one | `J/features/settings/view/lists/themes/ThemesListAdapter.java:48-54` | theme restart |
| Rate preference hidden in this flavor (`FLAVOR = "thirdPartyStores"` in `C/BuildConfig.class`, BC) | `J/features/settings/view/SettingsFragment.java:243-260` | `SettingsFragment.lambda$initRate$7` (DEAD) |

### 2.3 Screens the baseline never reached

Monkey's hits are a strict subset of APE's: 355 both, 0 Monkey-only, 49 APE-only, 121 neither (JAC).

| Screen / window | Monkey | APE | Evidence (JAC method flags, M = Monkey, A = APE) | Most likely gate |
|---|---|---|---|---|
| `S_MAIN_EMPTY`, Source/Actions/hash-type sheets | yes | yes | `HashCalculatorFragment.onViewCreated`, lambdas $4-$10, `ActionHolder.callItemClick`, `HashesListHolder.callItemClick` all MA | – |
| `S_DLG_TEXT_INPUT` | shown | shown, Add pressed | `TextInputDialog.initializeDialog` MA; `lambda$initializeDialog$0` (Add) A only; `BaseDialog.lambda$initializeDialog$0` (Close) never | Monkey taps outside, which cancels, or misses Add under the IME (INFERRED) |
| `S_MAIN_TEXT` | no | yes | `textValueEntered`, `setResult` A only | as above |
| `S_EXT_PICK_FILE` / `S_EXT_PICK_FOLDER` | launched | launched | `openSystemFileManager`/`openSystemFolderManager` MA; `onActivityResult` MA; `selectFileFromSystemFileManager`/`…Folder…` never | Both commands use `-p com.smlnskgmail.jaman.hashchecker.thirdparty` only (`{ape,monkey}/status.json` "command"). FW-MEMORY: Monkey's ActivityController aborts other-package starts and the caller gets RESULT_CANCELED with null data. No `LogUtils.e` hit, so no ActivityNotFoundException happened. |
| `S_MAIN_FILE` / `S_MAIN_FOLDER` | no | no | `validateSelectedFile/Folder`, `fileNameFromUri`, `folderNameFromUri`, `getConfiguredBundleWithDataUri` never | SAF blocked; no VIEW/SEND intents were sent |
| `S_MAIN_GENERATING`, `S_MAIN_RESULT` | no | no (recorded) | `AppProgressDialog.*`, `HashType.getHashTypeFromString` (HCF:217, the first statement of the generate branch), `HashCalculatorTask.*`, the whole engine, `lambda$new$1` never | Text gate above plus the SAF gate. See §2.4 for lost APE coverage. |
| `S_DLG_RATE_APP` | no | no | `canShowRateAppDialog`, `lambda$new$0`, `openGooglePlay` never | needs 6 generations |
| `S_EXT_CREATE_TXT` | no | no | `saveTextFile`, `writeHashToFile` never (`saveGeneratedHashAsTextFile` MA, snackbar branch) | needs a result |
| `S_MAIN_EXIT_PENDING` | yes | yes, "Exit now" tapped | `appBackClick`, `lambda$appBackClick$3` MA; `lambda$appBackClick$2` A only | – |
| `S_SNACKBAR_INFO` (OK tapped) | no | yes | `AppSnackbar.lambda$show$0` A only | – |
| `S_HISTORY_LOADING` / `S_HISTORY_EMPTY` | yes | yes | `setLoading`, `setLoaded`, loader task MA | – |
| `S_HISTORY_LIST` | no | yes | `HistoryItemHolder.*`, `HistoryItem.<init>()` and getters, `HistoryFragment$1.onScrolled` A only | needs stored hashes |
| `S_DLG_CLEAR_HISTORY` | no | shown, OK never | `HistoryFragment.onOptionsItemSelected`, `AppAlertDialog.*` A only; `lambda$onOptionsItemSelected$0`, `clearHistory`, `deleteAllHistoryItems` never | – |
| `S_SETTINGS`, Languages/Themes/Privacy/Author/Libraries sheets, `S_WEB_PRIVACY`, `S_FEEDBACK(_TYPED)` | yes | yes | `SettingsFragment` 30/34 MA; `WebFragment` 9/9; `FeedbackFragment` 15/15; `WebLinksListHolder.callItemClick` MA | – |
| `S_DLG_CHANGE_LANGUAGE` / `S_DLG_CHANGE_THEME` + restart | no (never tapped a row) | yes | `LanguagesListHolder.callItemClick` + lambda, `ThemesListHolder.callItemClick`…`configureNewTheme`, `AppUtils.restartApp` A only | – |
| `S_EXT_CREATE_ZIP` | no | launched | `SettingsFragment.onActivityResult` A only; `copyUserDataToUserFolder`, `LocalDataExporter.*` never | `-p` (as SAF) |
| Process-level: `App.onConfigurationChanged` | no | yes | A only | APE rotates the device (global configuration change; FW-MEMORY) |

### 2.4 Coverage-harness artifacts (affect target selection)

1. **The launch segment is excluded.** `merged.ec` is exactly the union of all valid segments **except `00000.ec`** in both runs (`SEG`: union of segments 1..N equals merged, probe for probe; adding 00000 changes `App`, `LanguageConfigImpl` and `SharedPreferencesSettings` for Monkey). Segment 00000 is dumped just before the tool starts (`coverage/00000.json` time 13:20:21.82 vs `status.json` started 13:20:21.99). For Monkey, the first-run code that ran at launch therefore counts as missed:
   - `App.createShortcuts`, `getShortcutForTextType`/`File`/`Folder`, `getShortcut`;
   - `LanguageConfigImpl.setLanguage(Language)`;
   - `SharedPreferencesSettings.saveLanguage`, `saveShortcutsStatus`.

   These 8 are among the 49 APE-only methods. APE got them again only because its app data was reset three times (point 3). Attribution of the 8 is INFERRED: probe→method mapping was not done, but these are exactly the APE-only methods of the three changed classes that a fresh launch executes.
2. **Coverage is lost when a process dies.** The receiver dumps with `getExecutionData(reset=true)` (`J/JacocoInstrument/JacocoInstrumentation.java`, `generateCoverageReport`). Whatever a process ran after its last dump disappears if it dies before the next one.
   - APE: 45 process starts (segments where `App.<init>` runs again); Monkey: 8 (`SEG`).
   - Each run has one failed dump containing the text "cat: files/coverage.ec: No such file or directory": `ASEG/00019`, `MSEG/00047`.
   - Concrete symptom: APE displays history rows from `ASEG/00036` on (`HistoryItem.<init>()`, getters, `HistoryItemHolder.bind`), yet `HashCalculatorTask`, `lambda$new$1`, `addHistoryItem` and the 5-argument `HistoryItem` constructor have no hit in any of 119 valid segments. Some hash generation most likely ran in lost time (INFERRED).
   - So "never hit" does not prove "never ran", above all for APE.
3. **APE's app data was reset mid-run.** `App` shows the first-run probe pattern again in `ASEG/00020`, `00064` and `00107`, together with `OrmLiteLocalDataStorage.onCreate` (DB re-created). The cause (APE action, harness `pm clear`, crash handling) is UNVERIFIED.

### 2.5 What a harness must prepare

- **Files.** Push `_fixtures/Download/*` to `/sdcard/Download/` (any file type works). Folder hashing reads the direct children of a tree (`J/components/hashcalculator/jdk/JdkHashCalculator.java:124-153`). Add a subfolder to reach the per-child exception path (`:144-146`; a directory cannot be opened as a stream, FW-MEMORY). No `Documents/` folder is needed.
- **SAF access.** Let the tool act inside `com.android.documentsui`, for example Monkey/APE `-p <app> -p com.android.documentsui`. Otherwise the pickers and create dialogs never return data (FW-MEMORY).
- **Or inject files by intent.** `adb shell am start -n com.smlnskgmail.jaman.hashchecker.thirdparty/com.smlnskgmail.jaman.hashchecker.MainActivity -a android.intent.action.VIEW -d file:///sdcard/Download/sample.pdf` together with `pm grant <pkg> android.permission.READ_EXTERNAL_STORAGE`. The debug manifest declares that permission (DM:11) but the code never requests it (FW-MEMORY: API 27 needs the runtime grant to read `/sdcard`).
- **Settings and state.** Nothing is required for the basic UI.
  - The rate dialog needs 6 successful generations, or a seeded `hash_generation_count=5` in `shared_prefs/com.smlnskgmail.jaman.hashchecker.thirdparty_preferences.xml` (default-prefs file name is FW-MEMORY).
  - `getThemeAnalogue` needs a legacy `selected_theme` value that is neither LIGHT nor DARK (SharedPreferencesSettings.java:116-139).
  - `setRefreshSelectedFileStatus` needs `refresh_selected_file=true`; no app code ever writes true (HCF:573-582).
- **Accounts.** None. The browser, Play Store and email apps are optional; they only change which fallback branch runs (`J/utils/WebUtils.java:28-46`, `J/features/feedback/view/FeedbackFragment.java:107-127`).
- **Network.** Only for the WebView page content (`INTERNET` is in the debug manifest, DM:8). The code path does not depend on it.

---

## 3. Screens and navigation

### 3.1 Windows

| Window | Class (SRC) | How shown | Handlers |
|---|---|---|---|
| Main activity | `T/MainActivity.java` | ENTRY | `onOptionsItemSelected` (126-138), `onBackPressed` (151-164) |
| Calculator | `HashCalculatorFragment` (`fragment_hash_calculator.xml`), tag `CURRENT_FRAGMENT` | `create()` → `showFragment` (T:93, 96-103) | hash-type text (HCF:473), From (476-479), Action (482-485), copy/clear ×2 (446-455), two TextWatchers (457-468), menu `menu_main` (History, Settings icons; `R/menu/menu_main.xml:6-18`) |
| History | `HistoryFragment` (`fragmant_history.xml`) | menu History → `showFragment(new HistoryFragment())` (T:132-133) | trash icon `menu_item_clean_history` (`R/menu/menu_history.xml:5-9`; `J/features/history/view/HistoryFragment.java:89-109`), row tap (`J/features/history/view/list/HistoryItemHolder.java:46`), scroll listener (HF:61-77), Up |
| Settings | `SettingsFragment` (PreferenceFragmentCompat, `R/xml/settings.xml`) | menu Settings (T:129-130) | 4 SwitchPreferences (framework persists them, no app listener; settings.xml:6-34); click listeners on Privacy, Export, Language, Theme, Help, Feedback, Author, Libraries, Version (SettingsFragment.java:158-288); Rate hidden (256); empty menu (330-332); Up (336-346) |
| Feedback | `FeedbackFragment` (`fragment_feedback.xml`) | Settings → Feedback → `activity.showFragment` (SettingsFragment.java:265-271) | menu Send (`R/menu/menu_feedback.xml:5-9`; FeedbackFragment.java:68-78), Up with close icon (61-67, 141-143) |
| Privacy web page | `WebFragment(url)` (`web_view.xml`) | Privacy sheet row → `activity.showFragment(new WebFragment(link))` (`J/features/settings/view/lists/weblinks/WebLinksListAdapter.java:57-63`) | empty menu (`menu_webview.xml`), Up |
| 8 bottom sheets | `BaseListBottomSheet` subclasses (RecyclerView `rv_bottom_sheet_list_items`) | `show(fragmentManager, …)` | row tap → `BaseListHolder.lambda$bind$0` → `callItemClick` (`J/ui/bottomsheets/lists/adapter/BaseListHolder.java:44`) |
| …Source | `SourceSelectActionsBottomSheet`: Text, File, Folder (`…/actions/ui/SourceSelectActionsBottomSheet.java:37-43`) | HCF:476-479 | `ActionHolder.callItemClick` → `userActionSelect` (`…/ActionsListAdapter.java:55-60`) |
| …Actions | `ActionSelectActionsBottomSheet`: Generate, Compare, Export ".txt" (`…/ActionSelectActionsBottomSheet.java:37-43`) | HCF:482-485 | same |
| …Hash type | `GenerateToBottomSheet`: 18 `HashType.values()` (`…/hashtypes/GenerateToBottomSheet.java:38-47`) | tap hash-type text (HCF:260-263, 473) | `HashesListHolder.callItemClick` → `hashTypeSelect` (`…/HashesListAdapter.java:57-64`; HCF:430-433) |
| …Languages | `LanguagesBottomSheet`: 21 languages | SettingsFragment.java:161-165 | `LanguagesListHolder.callItemClick` → alert (`…/languages/LanguagesListAdapter.java:55-72`) |
| …Themes | `ThemesBottomSheet`: Light, Dark | SettingsFragment.java:173-177 | `ThemesListHolder.callItemClick` (`…/ThemesListAdapter.java:48-82`) |
| …Privacy / Author / Libraries | `PrivacyPolicyWebLinksBottomSheet` (1 row), `AuthorWebLinksBottomSheet` (6), `LibrariesWebLinksBottomSheet` (2) | SettingsFragment.java:185-189, 208-212, 220-224 | `WebLinksListHolder.callItemClick`: privacy → WebFragment, others → `WebUtils.openWebLink` (WebLinksListAdapter.java:55-67) |
| Text input dialog | `TextInputDialog extends BaseDialog` (`android.app.Dialog`, `dialog_text_input.xml`) | `enterText()` (HCF:365-368) | Add (`TextInputDialog.java:37-40`), Close (`J/ui/dialogs/BaseDialog.java:34`), Back/outside cancel (FW-MEMORY), IME forced visible (TextInputDialog.java:52-55) |
| Alert dialog ×4 | `AppAlertDialog` (appcompat AlertDialog; `J/ui/dialogs/system/AppAlertDialog.java:37-51`) | rate (HCF:135-142), clear history (HF:93-103), language (LLA:56-70), theme (TLA:62-78) | positive listener, Cancel → `lambda$show$0`, onShow → `lambda$show$1` |
| Progress dialog | `AppProgressDialog` → `ProgressDialog`, not cancelable (`AppProgressDialog.java:23-35`) | `generateHash` (HCF:218-219) | none; dismissed in the task callback (HCF:148-150) |
| Snackbars | `AppSnackbar` (`AppSnackbar.java:62-94`) | many callers | OK action → `lambda$show$0` (68-71), or custom action (exit, HCF:377-383); vibrates if the pref is on (91-93) |
| External | DocumentsUI (OPEN_DOCUMENT, OPEN_DOCUMENT_TREE, CREATE_DOCUMENT), browser, market, email chooser | `startActivityForResult` / `startActivity` | outside the app |

There are no context menus, popup menus, action modes, view pagers, tabs, drawers, search UI, navigation graph, `onSaveInstanceState`/`onRestoreInstanceState`, `onNewIntent`, long-click or editor-action listeners (SRC grep of J/ and T/).

### 3.2 Navigation and back stack (SRC)

- **Push.** Every screen fragment is *added* (not replaced) to `android.R.id.content` with the same tag and `addToBackStack(null)`, the root calculator included (T:96-103). So all screen fragments stay added and resumed underneath (FW-MEMORY).
- **Back.** `MainActivity.onBackPressed` never calls `super` (T:151-164). It takes `findFragmentByTag("CURRENT_FRAGMENT")` (FW-MEMORY: the most recently added fragment with that tag) and calls `appBackClick()`:
  - **Calculator.** The first Back shows the exit snackbar (text: "Long press on back button…", `R/values/strings.xml:12`) and sets `isBackButtonDoubleTap`. A Handler resets it after 300 ms (HCF:384). A second Back within 300 ms, or the snackbar's "Exit now", calls `finish()` (HCF:371-390).
  - **History, Feedback, Web** (`BaseFragment.appBackClick`, `J/ui/BaseFragment.java:124-129`) and **Settings** (SettingsFragment.java:349-351): `UIUtils.removeFragment` = `remove().commit()` + `popBackStackImmediate()` (`J/utils/UIUtils.java:14-18`).
  - Then it calls `appResume()` on the last fragment in `getFragments()` (T:157-162). For the calculator this re-runs `validateTextCase`, `checkMultilinePreference`, `checkFileManagerChanged` and `hashTypeSelect` on every Back (HCF:548-554).
- **Up.** `setDisplayHomeAsUpEnabled(true)` for History, Feedback and Web (BaseFragment.java:48-64) and for Settings (SettingsFragment.java:354-358). Home goes to `BaseFragment.onOptionsItemSelected` (84-93), `FeedbackFragment.onOptionsItemSelected` (61-67) or `SettingsFragment.onOptionsItemSelected` (336-346), each calling `activity.onBackPressed()`. On the calculator Up is disabled (`setAllowBackAction` false, HCF:665-667).
- **Restart.** After a language or theme change, `AppUtils.restartApp` starts a new MainActivity and finishes the old one (`J/utils/AppUtils.java:16-20`) → new `S_MAIN_EMPTY`; the old instance goes to `S_EXIT`.
- **Possible stacks.** Calculator → History; Calculator → Settings → Feedback; Calculator → Settings → Web. History and Settings menus are not available on deeper pages because each top fragment clears the menu (§3.3).

### 3.3 Menus

- `BaseFragment.onCreate` calls `setHasOptionsMenu(true)` (BaseFragment.java:96-99). `onCreateOptionsMenu` clears the menu and inflates the fragment's own menu (67-75). Settings only clears it (SettingsFragment.java:330-332). FW-MEMORY: every added fragment's `onCreateOptionsMenu` runs in add order, so the top fragment's menu wins.
- History keeps a reference to its trash item (`primaryMenuButton`, BaseFragment.java:71-74; HF:145-147) and hides it after an empty first load or after clearing (HF:100, 128-129).
- Item taps first reach `MainActivity.onOptionsItemSelected`. It always calls `hideKeyboard()` and, through `super`, returns false (T:126-138). FW-MEMORY: the item is then offered to the fragments in add order until one returns true. `android.R.id.home` reaches the fragments only when up is enabled.

### 3.4 Modes per window

| Window | Mode variables (SRC) | Effect |
|---|---|---|
| Calculator | `fileUri`, `folderUri`, `isTextSelected` (HCF:97-98, 107, 316-333, 359-363) | Generate branch (216-246), Export guard (266), dialog pre-fill (366) |
| Calculator | `etGeneratedHash` / `etCustomHash` empty or not | Export (266), Compare (250), copy/clear icon visibility (519-527) |
| Calculator | progress dialog showing | modal, Back ignored (`setCancelable(false)`, AppProgressDialog.java:26) |
| Calculator | `isBackButtonDoubleTap` (300 ms) | Back finishes (374-388) |
| Calculator | prefs upper case, multiline, save to history, vibrate, `hash_generation_count`, `last_type_value` | guards only (409-428, 556-571, 118, AppSnackbar.java:91, 131) |
| History | loading (`isLoading`; progress bar visible), loaded empty (message view, trash hidden), loaded with rows | HistoryPresenterImpl.java:35-41, 50-53; HF:111-131 |
| History | paging: `HistoryPortion.isLoaded`, page size 30 | never loads page 2 (§5.5) |
| Settings | history empty or not | Export result EMPTY snackbar vs CREATE_DOCUMENT (SettingsPresenterImpl.java:44-56) |
| Themes sheet | tapped item == current theme | dismiss vs dialog (TLA:48-54) |
| Feedback | message empty or not | Send does nothing vs builds an email intent (FeedbackFragment.java:68-78) |
| Text dialog | `textValue` null or not | new vs edit (TextInputDialog.java:43-48) |

Theme (Light/Dark) and language change resources only; they enable no extra handlers.

### 3.5 Candidate page list

| Page | One-line description | Window class | Mode predicate |
|---|---|---|---|
| `S_ENTRY` | Outside the app: launcher icon, launcher shortcuts (long-press), other apps or adb sending VIEW/SEND | – | – |
| `S_EXIT` | MainActivity finished (double Back, "Exit now", old instance after restart); process may survive (`App.appComponent` static, pending Clipboard Handler) | – | – |
| `S_MAIN_PAUSED` | Calculator on top, activity stopped (Home, recents, external window) | MainActivity | !resumed, top = calculator |
| `S_HISTORY_PAUSED` | same with History on top | MainActivity | top = HistoryFragment |
| `S_SETTINGS_PAUSED` | same with Settings on top | MainActivity | top = SettingsFragment |
| `S_FEEDBACK_PAUSED` | same with Feedback on top | MainActivity | top = FeedbackFragment |
| `S_WEB_PAUSED` | same with the WebView on top | MainActivity | top = WebFragment |
| `S_MAIN_EMPTY` | Calculator, no source; Generate and Export show hint snackbars | HashCalculatorFragment | `fileUri == null && folderUri == null && !isTextSelected` |
| `S_MAIN_TEXT` | Text source selected (button reads "Text") | HashCalculatorFragment | `isTextSelected` |
| `S_MAIN_FILE` | File source selected via SAF, VIEW or SEND (button reads "File") | HashCalculatorFragment | `fileUri != null` |
| `S_MAIN_FOLDER` | Folder source selected via OPEN_DOCUMENT_TREE (button also reads "File") | HashCalculatorFragment | `folderUri != null` |
| `S_MAIN_RESULT` | Source selected and generated field non-empty: Export creates a .txt, Compare compares | HashCalculatorFragment | source ≠ none && `etGeneratedHash` non-empty (variants @TEXT/@FILE/@FOLDER) |
| `S_MAIN_GENERATING` | Modal "Generating hash, please wait…" while HashCalculatorTask runs | ProgressDialog over calculator | task running |
| `S_MAIN_EXIT_PENDING` | Exit snackbar with "Exit now"; a second Back within 300 ms finishes | AppSnackbar (action) | `isBackButtonDoubleTap` / snackbar visible |
| `S_SNACKBAR_INFO` | Info snackbar with OK (non-modal), variants @MAIN, @SETTINGS | AppSnackbar | snackbar visible (LENGTH_SHORT) |
| `S_SHEET_SOURCE` | Text / File / Folder | SourceSelectActionsBottomSheet | – |
| `S_SHEET_ACTIONS` | Generate / Compare / Export ".txt"; outcome depends on the calculator mode | ActionSelectActionsBottomSheet | variants @EMPTY/@TEXT/@FILE/@FOLDER/@RESULT |
| `S_SHEET_HASH_TYPE` | 18 algorithms, check mark on the last used one | GenerateToBottomSheet | – |
| `S_DLG_TEXT_INPUT` | Text field + Close + Add, keyboard shown | TextInputDialog | @NEW (no text source) / @EDIT (pre-filled) |
| `S_DLG_RATE_APP` | "If you like the app…" Rate / Cancel | AppAlertDialog | counter == 5 at a successful result |
| `S_EXT_PICK_FILE` | DocumentsUI ACTION_OPEN_DOCUMENT `*/*` | external | – |
| `S_EXT_PICK_FOLDER` | DocumentsUI ACTION_OPEN_DOCUMENT_TREE | external | – |
| `S_EXT_CREATE_TXT` | DocumentsUI CREATE_DOCUMENT text/plain, name `<object>.<ext>.txt` | external | result goes to HashCalculatorFragment |
| `S_EXT_CREATE_ZIP` | DocumentsUI CREATE_DOCUMENT application/zip, `hash_checker_user_data.zip` | external | result goes to SettingsFragment |
| `S_EXT_OTHER_APP` | Browser, market://, email chooser; no result | external | – |
| `S_HISTORY_LOADING` | Progress bar while HistoryItemsLoaderTask runs | HistoryFragment | `isLoading` |
| `S_HISTORY_EMPTY` | "History items not found", trash hidden | HistoryFragment | loaded && 0 rows |
| `S_HISTORY_LIST` | Rows (tap copies the hash), trash visible | HistoryFragment | loaded && ≥ 1 row |
| `S_DLG_CLEAR_HISTORY` | "Delete all history items?" OK / Cancel | AppAlertDialog | – |
| `S_SETTINGS` | Preference list (Rate hidden) | SettingsFragment | guard: history non-empty for Export |
| `S_SHEET_LANGUAGES` | 21 languages, check on the current one | LanguagesBottomSheet | – |
| `S_DLG_CHANGE_LANGUAGE` | Restart warning, OK / Cancel | AppAlertDialog | – |
| `S_SHEET_THEMES` | Light / Dark | ThemesBottomSheet | – |
| `S_DLG_CHANGE_THEME` | Restart warning, OK / Cancel | AppAlertDialog | tapped theme ≠ current |
| `S_SHEET_PRIVACY` | 1 row → WebFragment | PrivacyPolicyWebLinksBottomSheet | – |
| `S_SHEET_AUTHOR` | 6 rows → browser | AuthorWebLinksBottomSheet | – |
| `S_SHEET_LIBRARIES` | 2 rows → browser | LibrariesWebLinksBottomSheet | – |
| `S_FEEDBACK` | Empty message, device info, Send does nothing | FeedbackFragment | message empty |
| `S_FEEDBACK_TYPED` | Message typed, Send opens the email chooser | FeedbackFragment | message non-empty |
| `S_WEB_PRIVACY` | Privacy policy in a WebView | WebFragment | – |

Total 40 pages: 7 pseudo, 5 external, 28 in-app. I chose separate `*_PAUSED` pseudo pages instead of `S_MAIN_PAUSED@X` so that every name ends in `_PAUSED`, which the viewer hides (GRAPH_PROMPT Step 1). The resume target then follows without variants.

### 3.6 Recommended `@CONTEXT` variants

These are shared handlers whose continuation depends on the caller.

| Variant | Reason |
|---|---|
| `ActionsListAdapter$ActionHolder.callItemClick@SOURCE` / `@ACTIONS`; `HashCalculatorFragment.userActionSelect@SOURCE` / `@ACTIONS` / `@SHORTCUT` | One switch, six cases (HCF:166-189) |
| `BaseListHolder.bind` / `lambda$bind$0`, `BaseListAdapter.onCreateViewHolder` / `onBindViewHolder` / `getItemCount` / `dismissBottomSheet`, `BaseListBottomSheet.onCreateView` / `onViewCreated` @SOURCE, ACTIONS, HASHTYPE, LANGUAGES, THEMES, PRIVACY, AUTHOR, LIBRARIES | The same base code serves 8 sheets |
| `AppAlertDialog.<init>` / `show` / `lambda$show$0` / `lambda$show$1` @RATE, CLEAR, LANGUAGE, THEME | 4 different positive actions |
| `AppSnackbar.show@MAIN` / `@SETTINGS` / `@EXIT`, `AppSnackbar.lambda$show$0@MAIN` / `@SETTINGS` | Origin page |
| `BaseFragment.appResume` / `onCreateOptionsMenu` / `onOptionsItemSelected` / `appBackClick` @MAIN, HISTORY, FEEDBACK, WEB; `MainActivity.onBackPressed@<top>`, `MainActivity.onOptionsItemSelected@<page>` | Dispatch target |
| `HashCalculatorTask.<init>` / `doInBackground` / `onPostExecute` @TEXT, FILE, FOLDER; `JdkHashCalculatorDigest.setHashType` / `update` / `result` @CRC, BLAKE, FNV, MD, SHA3 | Engine path (`JdkHashCalculatorDigest.java:49-115`; `JdkHashCalculator.java:29-40`) |
| `WebUtils.openWebLink@HELP` / `@VERSION` / `@AUTHOR` / `@LIBRARIES`; `Clipboard.copy@CUSTOM` / `@GENERATED` / `@HISTORY`; `AppUtils.restartApp@LANGUAGE` / `@THEME`; `TextInputDialog.initializeDialog@NEW` / `@EDIT`; `LanguageConfigImpl.setLanguage(Language)@FIRST_RUN` / `@SETTINGS` | Caller-dependent continuation |

### 3.7 Lifecycle and framework facts that create or remove edges

All of these are FW-MEMORY unless marked otherwise.

1. **Resume.** Activity resume sends `onResume` to every added fragment, so returning from Home to Settings also runs `HashCalculatorFragment.onResume` → `appResume`. Popping a fragment resumes nothing, which is why `MainActivity.onBackPressed` calls `appResume` itself (SRC T:157-162).
2. **Activity results.** `Fragment.startActivityForResult` routes the result to that fragment's `onActivityResult` (fragment 1.3.x via ActivityResultRegistry), before `onResume`. Request code 3 (`Settings.FILE_CREATE`) is used by both HCF:286 and SettingsFragment.java:294 without cross-delivery.
3. **Blocked starts.** Monkey/APE `-p` aborts other-package activity starts. The caller gets `RESULT_CANCELED` with null data, and `startActivity` does not throw.
4. **AsyncTask.** `execute()` runs on the serial executor and `onPostExecute` runs on the main thread. Neither task is cancelled when the view is destroyed (SRC: no `cancel` calls).
5. **RecyclerView.** It calls `onScrolled(0,0)` after a layout that changes the visible range, so `HistoryFragment$1.onScrolled` runs without scrolling once rows exist.
6. **setText.** `setText` notifies TextWatchers: `validateTextCase` → `convertTo*Case` → `HashCalculatorFragment$1.onTextChanged` on every resume (SRC HCF:417-422, 641-647).
7. **Orientation.** The portrait lock (M:22) means rotation does not recreate MainActivity. A global configuration change still reaches `App.onConfigurationChanged`.
8. **Recreation.** It happens on multi-window resize (`resizeableActivity=true`, no `configChanges`), a system locale or font change, or restore after process death. It re-runs `MainActivity.create()` (SRC BaseActivity.java:19), which adds a *second* calculator. A `WebFragment` in the stack cannot be re-instantiated because it has no no-arg constructor (SRC `WebFragment.java:27-29`).
9. **`Application.onTerminate`** is never called on real devices.

---

## 4. Framework mechanisms

| Mechanism | App classes (SRC) | Edge notes |
|---|---|---|
| RecyclerView adapters | `BaseListAdapter` (+ Actions, Hashes, Languages, Themes, WebLinks adapters and their `$…Holder`s) in BottomSheetDialogFragments; `HistoryItemsAdapter` / `HistoryItemHolder` inside `AdaptiveRecyclerView` (library; empty-state view via `setMessageView`, HF:60) | FRAMEWORK: `setAdapter` (BaseListBottomSheet.java:38; HF:126, 136) → `onCreateViewHolder`/`onBindViewHolder`/`getItemCount`; `notifyItemRangeInserted` (HistoryItemsAdapter.java:22); the click listener is registered inside `bind` (BaseListHolder.java:44; HistoryItemHolder.java:46). Library behaviour UNVERIFIED (no source). |
| AsyncTask | `HashCalculatorTask` (`J/components/hashcalculator/api/HashCalculatorTask.java:64-87`) → `HashCalculatorTaskTarget` lambda (HCF:111-151); `HistoryItemsLoaderTask` (`…/history/view/loader/HistoryItemsLoaderTask.java:27-42`) → `HistoryPresenterImpl.postLoad` | ASYNC edges |
| Handler.postDelayed | `Clipboard` clears after 60 s (`Clipboard.java:20, 30-31, 35-39`); exit double-tap reset after 300 ms (HCF:384) | ASYNC / SYSTEM with needs_state |
| Fragments / back stack / options menus | `MainActivity.showFragment`, `UIUtils.removeFragment`, `BaseFragment`, `SettingsFragment` | §3.2-3.3 |
| Bottom sheets, dialogs, snackbars | `BaseListBottomSheet` (material BottomSheetDialogFragment), `TextInputDialog`/`BaseDialog` (android.app.Dialog), `AppAlertDialog` (appcompat), `AppProgressDialog` (ProgressDialog), `AppSnackbar` (material Snackbar) | GUI edges for buttons and actions; Back/outside cancel is FRAMEWORK/SYSTEM |
| Preferences | androidx `PreferenceFragmentCompat`, `addPreferencesFromResource(R.xml.settings)` (SettingsFragment.java:86); `OnPreferenceClickListener` lambdas $0-$9 | Switches persist without app code; their effect shows at the next `HashCalculatorFragment.appResume`. No preference-change listeners. |
| SharedPreferences | `SharedPreferencesSettings` (default prefs, App.java:58-67), keys in `R/values/strings-non-translatable.xml:10-32` | `reads`/`writes`: `pref:last_type_value`, `language`, `selected_theme`, `shortcuts_created`, `generate_from_share_intent` (written, never read), `refresh_selected_file`, `hash_generation_count`, `upper_case`, `multiline`, `save_result_to_history`, `vibrate` |
| Storage Access Framework | OPEN_DOCUMENT (193), OPEN_DOCUMENT_TREE (194), CREATE_DOCUMENT (3) in HCF:191-213, 273-291; CREATE_DOCUMENT zip (SettingsPresenterImpl.java:46-50; SettingsFragment.java:293-295); tree children via `DocumentsContract` (JdkHashCalculator.java:124-153); writes via `openFileDescriptor(uri,"w")` (HCF:619-631; SettingsFragment.java:126-142) | INTENT + RESULT |
| Database | ORMLite `OrmLiteLocalDataStorage extends OrmLiteSqliteOpenHelper`, DB `hashchecker.db` v1, table `history` (`HistoryItem`, `DbEntity`), config `R/raw/ormlite_config.txt` | Add, delete, count and WAL checkpoint run on the main thread; queries run in the loader. The first DAO use opens the DB → FRAMEWORK edge to `onCreate`; reading rows builds `HistoryItem.<init>()` by reflection (FW-MEMORY). |
| Export | `LocalDataExporter` zips the DB into `dataDir/hash_checker_user_data.zip`, then the app copies it to the SAF URI (`LocalDataExporter.java:18-58`) | CALL chain after RESULT |
| WebView | `WebFragment` with the default `WebViewClient` and `loadUrl` (`WebFragment.java:38-43`); no JS bridge | network only for content |
| Intents to other apps | `WebUtils.openWebLink` / `openGooglePlay` (market:// then https fallback), `FeedbackFragment.sendEmail` (chooser over ACTION_SEND with an ACTION_SENDTO selector; `FeedbackPresenterImpl.java:35-46`) | INTENT with no result |
| Shortcuts | `App.createShortcuts` (ShortcutManager, API ≥ 26) | ENTRY variants |
| Dependency injection | Dagger 2.40.2 (`app/build.gradle` dependencies): `App.appComponent` built in `App.onCreate`; `inject(this)` in 14 places (MainActivity:51, HCF:156, HF:50, FeedbackFragment:40, SettingsFragment:77, WebFragment:33, GenerateToBottomSheet:31, ActionSelect…:24, SourceSelect…:24, LanguagesBottomSheet:29, ThemesBottomSheet:30 *in onViewCreated*, Author:22, Libraries:22, PrivacyPolicy:23) | CALL chains `DaggerAppComponent.inject(X)` → `injectX` → static `X_MembersInjector.injectField` + `…Factory.xxxHelper(module)` → `XxxModule.xxxHelper()` (BC) |
| Locale and theme | `LanguageConfigImpl` (`Resources.updateConfiguration`), `ThemeConfigImpl` (`Theme.applyStyle`, attribute colours), `BaseActivity.getTheme` override (framework calls it repeatedly) | FRAMEWORK edges from activity creation |
| Clipboard, Vibrator, Security provider | `Clipboard` (ClipboardManager), `Vibrator` (API ≥ 26 VibrationEffect branch, `Vibrator.java:17-30`), `KeccakjProvider` (App.java:55) for SHA3 | – |
| Not present | LiveData/ViewModel, RxJava, executors/threads, WorkManager/JobScheduler/AlarmManager, services, app broadcast receivers, app content providers, data binding, notifications, home-screen widgets | SRC grep |

---

## 5. Unreachable-code candidates (evidence; final verdicts are for the graph builders)

### 5.1 No caller (static reachability from framework callbacks, BC + CHA)

| Candidate | # | Evidence | JaCoCo |
|---|---|---|---|
| Dagger `*_MembersInjector.<init>`, `create`, `injectMembers(T)` (14 classes) | 42 | `DaggerAppComponent.injectX` calls only static `injectField` and `Factory.xxxHelper` (BC dump); the instance APIs are reached only via `create` and bridges, which nothing calls | filtered |
| Dagger `*_…Factory.<init>`, `create`, `get()` (4 classes) | 12 | same | filtered |
| Constructors of static-only classes: `HashConstants`, `JdkHashUtils` (private), `LocalDataExporter`, `AppUtils` (private), `LogUtils`, `UIUtils` (private), `WebUtils` (private) | 7 | No `new` in BC | 3 in JaCoCo (HashConstants, LocalDataExporter, LogUtils), never hit |
| `OrmLiteConfigUtil.<init>`, `main(String[])` | 2 | Build-time config generator (`…/OrmLiteConfigUtil.java:5-10`), package-private, no caller | never |
| `DbEntity.getId`, `setId` | 2 | No app caller; FW-MEMORY: ORMLite uses field access unless `useGetSet` (`DbEntity.java:7-17`) | never |
| `HistoryItem.equals`, `hashCode` | 2 | No app caller (HistoryItem.java:83-102); only lists, no hashing collections | never |
| Enum synthetic methods: `Theme.valueOf`, `Action.valueOf`, `Action.values`, `UserActionType.valueOf`, `SaveUserDataResult.valueOf`, `WebLink.valueOf`, `WebLink.values` | 7 | No caller (BC). By contrast, `HashType.values/valueOf`, `Language.values/valueOf`, `Theme.values` are called, and `UserActionType.values()` and `SaveUserDataResult.values()` are called from the switch-map `<clinit>`s | filtered |
| `App.onTerminate` → `OrmLiteLocalDataStorage.releaseHelper` (only caller) | 2 | App.java:176-179; OrmLite…:61-63; FW-MEMORY: `onTerminate` never runs on devices | never |
| `OrmLiteLocalDataStorage.onUpgrade` | 1 | DB version is 1 (OrmLite…:31-33) → no upgrade possible | never |

### 5.2 Reachable call target but never executed (needs override or flavor reasoning)

| Candidate | Evidence | JaCoCo |
|---|---|---|
| `BaseFragment.setAllowBackAction` | Overridden by every concrete `BaseFragment` (HCF:665, HF:155, FeedbackFragment:136, WebFragment:58) | never |
| `BaseFragment.getBackActionIconResId` | Called only when `setAllowBackAction()` is true (BaseFragment.java:53-60); the calculator returns false, the others override it | never |
| `AppTextWatcher.onTextChanged` | The only subclass `HashCalculatorFragment$1` overrides it (HCF:516-528) | never |
| `SettingsFragment.lambda$initRate$7` | Registered only if `BuildConfig.FLAVOR.equals("googlePlay")` (SettingsFragment.java:247-257); FLAVOR is "thirdPartyStores" (BC `C/BuildConfig.class`) | never |
| `BuildConfig.<init>` (outside the 661) | Never instantiated. `<clinit>` runs only when `BuildConfig.DEBUG` is read in `LogUtils.e` (`J/utils/LogUtils.java:10`); the other fields are compile-time constants (BC) | never |

Cross-check: none of the 16 candidates that JaCoCo reports were hit by Monkey or APE, so the baseline does not contradict them.

### 5.3 Reachable only after setup, or gated by state, environment or API (not dead)

- **Needs a generated hash.** Engine (66 JaCoCo methods), `lambda$new$1`, `canSaveResultToHistory`, `canShowRateAppDialog`, `increaseHashGenerationCount`, `get/saveIntPreference`, `addHistoryItem`, the 5-argument `HistoryItem.<init>`, `AppProgressDialog.*`. Plus, after 6 generations, `lambda$new$0` and `WebUtils.openGooglePlay` (HCF:111-151).
- **Needs SAF interaction or VIEW/SEND.** `validateSelected*`, `fileNameFromUri`, `folderNameFromUri`, `select*FromSystemFileManager`, `saveTextFile`, `writeHashToFile`, `copyUserDataToUserFolder`, `copyFile`, `LocalDataExporter.*`, `backupCheckpoint`, `getDatabaseFolder`/`FileName`, the stream and folder engine methods, `MainActivity.getConfiguredBundleWithDataUri`.
- **Needs history rows and confirmation.** `lambda$onOptionsItemSelected$0`, `clearHistory`, `deleteAllHistoryItems`, `refreshHistory`.
- **Exception paths only.** `LogUtils.e` (23 call sites, all in `catch` blocks, e.g. HCF:198, 209, 288, 343, 597; `JdkHashCalculator.java:38, 57, 77, 90, 110`; `WebUtils.java:38, 54`) and `BuildConfig.<clinit>`. Triggers: unreadable or ungranted URI, `file://` without the storage grant, a missing SAF app, a missing browser, a corrupt `last_type_value`.
- **Pre-seeded preferences only.** `SharedPreferencesSettings.getThemeAnalogue` (legacy theme value, :116-139) and `setRefreshSelectedFileStatus` (HCF:573-582; no app code writes `refresh_selected_file=true`). Without seeding, treat the latter as effectively DEAD.
- **API level.** `App.createShortcuts` body and `getShortcut*` need API ≥ 26 (App.java:84; `@RequiresApi(N_MR1)`), fine on API 27. The pre-O vibrate branch (`Vibrator.java:27`) is branch-dead on API 27.
- **Environment.** `FeedbackFragment.sendEmail` catch/ShareCompat branch (FeedbackFragment.java:114-127): FW-MEMORY, `createChooser` always resolves, so this is branch-dead. ERROR branches with no DocumentsUI: SettingsPresenterImpl.java:51-53; SettingsFragment.java:296-307.

### 5.4 Branch-level dead code inside reachable methods (put in `note`)

- Folder shortcut flag never set in this flavor (HCF:496-498; T:113-123).
- The `default: throw` in `userActionSelect` (HCF:186-187) is unreachable: all enum cases are handled.
- History "load more" never fires. `isLoaded()` returns `!isLoading && !portion.isLoaded()` (HistoryPresenterImpl.java:30-32). `canLoad` needs it false (HF:74-76), but `load()` returns early when the portion is complete (HPI:36). So page 2 (offset 30, OrmLite…:87-89) is never requested.
- `OrmLiteLocalDataStorage.historyItems`: `page != -1` is always true (:87).
- `MainActivity.create`: the shortcut `else if (intent != null)` (T:89) always runs for a launcher start; the `intent == null` case is unreachable for framework launches (FW-MEMORY).

### 5.5 Hazard candidates (from reading the code; not reproduced)

- **Empty-history NPE.** `HistoryFragment.setLoaded` calls `primaryMenuButton.setVisible(false)` for an empty first page (HF:128-129). `primaryMenuButton` is set only in `onCreateOptionsMenu` (BaseFragment.java:71-74). If the loader finishes before the menu is created, this is a NullPointerException (timing UNVERIFIED).
- **WebFragment restore crash** on recreation or process-death restore (no no-arg constructor, WebFragment.java:27-29). Recreation also duplicates the calculator (BaseActivity.java:19 → T:93).
- **Task callbacks outlive the view.** `HashCalculatorTask` keeps the fragment `context` and calls `progressDialog.dismiss()` and `etGeneratedHash.setText` after the view may be gone (HCF:111-151).
- **Misleading exit text.** It says "Long press on back button…" (strings.xml:12) but the code needs a double tap within 300 ms (HCF:374-388).

---

## 6. Decomposition

**Recommendation: one agent models the whole app.**
- 661 method nodes and about 40 pages. Of the nodes, 128 are DI code: 114 `@DaggerGenerated`, 6 in the generated `DaggerAppComponent$Builder`, 8 in the 4 hand-written modules. 54 of these are DEAD and 74 are trivial CALL chains. Another 77 are the engine (pure CALL chains under one ASYNC edge).
- BC scan: 981 invoke sites → 858 unique app→app caller/callee pairs, plus 32 invokedynamic registrations (31 lambdas + `Clipboard::clear`). That CALL layer can be generated mechanically (HANDOFF "Next steps"). By hand, roughly 4× Currency.

**Optional two-area split** if two agents must work in parallel. Overlap is limited to calls through interfaces (`Settings`, `ThemeConfig`, `LanguageConfig`, `LocalDataStorage`, `HashCalculatorTask`, `HashType`). Rule: each agent writes the edges whose `src` is in its area.

| Area | Owns (packages/classes) | Classes | Method nodes (661 universe) | JaCoCo methods | Pages | Entry edges from the other area |
|---|---|---|---|---|---|---|
| **UI** | `MainActivity`; `features/**` except `*_MembersInjector` (hashcalculator UI incl. `HashCalculatorFragment$1/$2`, input, lists; history incl. loader, presenter, list; settings incl. presenter, lists, `$1`; feedback; webview); `ui/**` (BaseActivity, BaseFragment, bottom-sheet bases, dialogs, AppSnackbar, states, watchers); `utils/**` (AppUtils, LogUtils, UIUtils, WebUtils) | 70 | 349 | 334 | all 40 pages | from CORE: `S_ENTRY` → `App` process start precedes MainActivity; `HashCalculatorTask.onPostExecute` → `HashCalculatorFragment.lambda$new$1` (ASYNC callback); engine and storage `catch` blocks → `LogUtils.e` |
| **CORE** | `App`, `App$1`, `BuildConfig`; `di/**` + all 14 `*_MembersInjector`; `components/**` (hashcalculator engine incl. `HashType`, `HashCalculatorTask`; localdatastorage incl. models and exporter; settings impl; theme; locale; clipboard; vibrator) | 57 | 312 (BuildConfig not counted) | 191 (incl. BuildConfig 2) | none (only ENTRY into `App`, CALL, ASYNC, FRAMEWORK) | from UI: the 14 `inject(this)` sites (§4); `generateHash` → `new HashCalculatorTask(...)` + `execute` (HCF:220-242); `Settings`/`ThemeConfig`/`LanguageConfig` calls (BaseActivity:17, 26; BaseFragment:34; HCF many; AppSnackbar:79-93; BaseListHolder:47-57; SettingsFragment:115; Themes/Languages adapters); storage calls (HCF:129; HistoryItemsLoaderTask:28; HPI:45; SettingsPresenterImpl:44; SettingsFragment:129-140); `HistoryItemHolder.bind` → HistoryItem getters and `HashType.getTitle`; `Clipboard` (HCF:534; HistoryItemHolder:46); `Vibrator` (AppSnackbar:92); `HashType` list items via `ListItem` (BaseListHolder.bind) |

- **Shared infrastructure.** CORE owns process start, DI, preferences, theme, locale, storage and the engine. UI owns the base UI classes and `utils/`.
- **Leftovers.** The 22 classes with no method node are assigned by package: 21 interfaces (`HashCalculator`, `HashCalculatorTask$HashCalculatorTaskTarget`, `LocalDataStorage`, `LanguageConfig`, `Settings`, `ThemeConfig`, `AppComponent`, `ApplicationScope`, `FeedbackPresenter`, `FeedbackView`, `TextValueTarget`, `UserActionTarget`, `HashTypeSelectTarget`, `HistoryPresenter`, `HistoryView`, `HistoryItemsLoaderTaskTarget`, `SettingsPresenter`, `SettingsView`, `ListItem`, `AppBackClickTarget`, `AppResumeTarget`) and the synthetic `DaggerAppComponent$1`. `JacocoInstrument` (3 classes) is out of scope. 70 + 57 = 127 classes = all compiled classes except JacocoInstrument.

---

## 7. Baseline coverage by area and screen (JaCoCo methods, either run)

| Area / sub-area | Classes | JaCoCo methods | Both | Monkey only | APE only | Neither |
|---|---|---|---|---|---|---|
| **UI** | 70 | 334 | 278 | 0 | 30 | 26 |
| · MainActivity | 1 | 11 | 10 | 0 | 0 | 1 |
| · calculator UI | 17 | 97 | 83 | 0 | 4 | 10 |
| · history | 10 | 46 | 31 | 0 | 12 | 3 |
| · settings, feedback, web | 25 | 123 | 113 | 0 | 7 | 3 |
| · ui base + utils | 17 | 57 | 41 | 0 | 7 | 9 |
| **CORE** | 57 | 191 | 77 | 0 | 19 | 95 |
| · App + BuildConfig | 3 | 14 | 5 | 0 | 6 | 3 |
| · DI (Builder + modules only; the rest is filtered) | 27 | 13 | 13 | 0 | 0 | 0 |
| · engine | 10 | 73 | 7 | 0 | 0 | 66 |
| · storage | 6 | 31 | 4 | 0 | 8 | 19 |
| · prefs, theme, locale, clipboard, vibrator | 11 | 60 | 48 | 0 | 5 | 7 |
| **Total** | 127 | 525 | 355 | 0 | 49 | 121 |

Screens never reached and the likely reason (details and evidence in §2.3):

| Area | Screens | Likely reason |
|---|---|---|
| UI, neither run | `S_MAIN_FILE`, `S_MAIN_FOLDER`, `S_MAIN_GENERATING`, `S_MAIN_RESULT`, `S_DLG_RATE_APP`, `S_EXT_CREATE_TXT` (and successful returns from all SAF pages) | SAF in another package, blocked by `-p`; the multi-step text path; no external VIEW/SEND intents |
| UI, APE only | `S_MAIN_TEXT`, `S_HISTORY_LIST`, `S_DLG_CLEAR_HISTORY` (OK never), language and theme dialogs + restart, `S_EXT_CREATE_ZIP` (launch only) | – |
| CORE | no own pages; 66 engine methods and 11 storage methods (add, delete, export) never ran | upstream UI gates; for APE also lost coverage (§2.4) |
| CORE, APE only | first-run methods (8), `App.onConfigurationChanged`, `ThemeConfigImpl.setCurrentTheme`/`saveTheme`, DB `onCreate`, row reading | launch segment excluded for Monkey (§2.4.1); APE rotation and theme change |

### Lists (JAC)

**Never hit by either run (121)**
- engine (66): all `Blake2B` (20), `FNV1a` (19), `JdkHashCalculator` (9), `JdkHashCalculatorDigest` (6), `JdkHashUtils` (3), `HashCalculatorTask` (5), `HashConstants.<init>`, `HashType.getHashTypeFromString`/`getFileExtension`/`isKeccakj`.
- storage (19): `OrmLiteConfigUtil.<init>`/`main`; `OrmLiteLocalDataStorage.onUpgrade`/`releaseHelper`/`addHistoryItem`/`deleteAllHistoryItems`/`backupCheckpoint`/`getDatabaseFolder`/`getDatabaseFileName`; `HistoryItem.<init>(5 args)`/`equals`/`hashCode`; `DbEntity.getId`/`setId`; `LocalDataExporter` (5).
- calculator (10): `saveTextFile`, `validateSelectedFile`, `validateSelectedFolder`, `fileNameFromUri`, `folderNameFromUri`, `selectFileFromSystemFileManager`, `selectFolderFromSystemFileManager`, `writeHashToFile`, `lambda$new$1`, `lambda$new$0`.
- prefs (7): `canSaveResultToHistory`, `getThemeAnalogue`, `setRefreshSelectedFileStatus`, `canShowRateAppDialog`, `increaseHashGenerationCount`, `saveIntPreference`, `getIntPreference`.
- app (4): `App.onTerminate`, `MainActivity.getConfiguredBundleWithDataUri`, `BuildConfig.<init>`/`<clinit>`.
- history (3): `HistoryFragment.refreshHistory`, `lambda$onOptionsItemSelected$0`, `HistoryPresenterImpl.clearHistory`.
- ui/utils (9): `AppTextWatcher.onTextChanged`, `WebUtils.openGooglePlay`, `LogUtils.<init>`/`e`, `AppProgressDialog.<init>`/`getDialog`, `BaseDialog.lambda$initializeDialog$0`, `BaseFragment.setAllowBackAction`/`getBackActionIconResId`.
- settings (3): `SettingsFragment.copyUserDataToUserFolder`, `copyFile`, `lambda$initRate$7`.

**APE only (49)**
- first launch (8): `App.createShortcuts`, `getShortcutForTextType`/`File`/`Folder`, `getShortcut`, `LanguageConfigImpl.setLanguage(Language)`, `SharedPreferencesSettings.saveLanguage`, `saveShortcutsStatus`.
- `App.onConfigurationChanged`.
- text source: `TextInputDialog.lambda$initializeDialog$0`, `HashCalculatorFragment.textValueEntered`, `setResult`.
- snackbars: `HashCalculatorFragment.lambda$appBackClick$2`, `AppSnackbar.lambda$show$0`.
- `AppAlertDialog` (4).
- language and theme change: `LanguagesListHolder.callItemClick` + lambda; `ThemesListHolder.callItemClick`/`showThemeApplyDialog`/`configureNewTheme`/lambda; `ThemeConfigImpl.setCurrentTheme`; `SharedPreferencesSettings.saveTheme`; `BaseListAdapter.getBottomSheet`; `AppUtils.restartApp`.
- history with rows: `HistoryFragment$1.onScrolled`/`canLoad`; `HistoryFragment.onOptionsItemSelected`; `HistoryItemHolder` (6); `HistoryItemsAdapter.onBindViewHolder`/`onCreateViewHolder`; `HistoryPresenterImpl.isLoaded`; `HistoryItem.<init>()` + 5 getters; `DbEntity.<init>`; `OrmLiteLocalDataStorage.onCreate`.
- `SettingsFragment.onActivityResult`.

---

## Conclusions and recommendations (nothing implemented)

1. **Method list.** Build it with `tools/list_methods.py … --exclude JacocoInstrument --exclude BuildConfig` (661). Leave the 138 JaCoCo-filtered nodes with blank baseline flags. Give the 81 candidates in §5.1-5.2 DEAD or FRAMEWORK_ONLY, and note `setRefreshSelectedFileStatus`/`getThemeAnalogue` as "seeded prefs only".
2. **Targets.** Do not treat the 8 first-launch methods as genuine Monkey misses. They ran in the excluded segment `00000` (§2.4.1). Flag this harness rule to Yang: it removes launch-time code for every tool alike, unless a tool clears data mid-run as APE apparently did.
3. **Lost coverage.** Process deaths lose coverage, so APE's "never hit" engine methods may in fact have run (§2.4.2). Shorter dump intervals, or a dump on `onTrimMemory`/crash, would fix this in future runs.
4. **Page modelling.** Use the 40 pages in §3.5 and the variants in §3.6. Model the SAF windows as external pages with RESULT edges. Mark them `env: "tool must be allowed to act in com.android.documentsui"`, because `-p` blocks them (FW-MEMORY).
5. **Edge extraction.** Generate the CALL layer (858 pairs) and the lambda registrations from bytecode. Write the GUI, ENTERS, FRAMEWORK and ASYNC edges by hand from §3-§4.

## Appendix: read-only commands used

- `python3 -I -B tools/list_methods.py <C>/.. --exclude JacocoInstrument --exclude BuildConfig` (stdout only).
- Inline Python (stdin, no files written):
  - JaCoCo XML aggregation per class and area;
  - JaCoCo-vs-classfile diff;
  - class-file scan (constant pool, access flags, invoke/invokedynamic opcodes, `BootstrapMethods`, CHA reachability from framework callbacks);
  - JaCoCo `.ec` segment parser (blocks 0x01/0x10/0x11, probe bit arrays);
  - in-memory AXML decoder for the APK manifest.
- No files were written except this report. A few early stdout redirects to `/tmp` were deleted right away.
