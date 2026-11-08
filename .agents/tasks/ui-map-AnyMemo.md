# AnyMemo 10.12.2 (pro flavor): UI map and modeling plan for the trigger graph

Read-only investigation. No project file was changed; this report is the only file written (one scratch file in `/tmp` was created during the bytecode scan and then deleted).

## Summary

- **Method universe.** The JaCoCo universe is **2192 methods** (633 class files in `proDebug`, JacocoInstrument excluded); `tools/list_methods.py` counts **2626**. The net difference of 434: the script keeps 436 methods that JaCoCo filters out (365 Dagger factory/injector methods, 47 enum helpers, 16 private empty constructors, 8 switch-map `<clinit>`) and drops 2 BuildConfig methods that JaCoCo keeps (§0).
- **Entry points.** 19 real activities with a launcher main activity `ui.AnyMemo` (drawer plus 4 bottom tabs Recent/Open/Download/Misc), 3 services, 3 receivers (the alarm one in `:remote`), 2 exported providers, a FileProvider and a widget. Exported entries: VIEW `content://…*.db`, SEND `text/*`, the deep link `anymemo-dropbox://`, BOOT. 8 manifest activities (Google/Quizlet) have no class in the APK (§1).
- **No login or onboarding.** On API 27 the only gates are the storage permission (`AnyMemo.java:124-129`) and a first-run "What's new" dialog; the first run also installs a 28-card sample deck. Both baselines had permissions pre-granted (INFERRED), and their first run fell into a warm-up dump (`coverage/00000.ec`) that **is not in either report** (§2.2).
- **What blocked the baseline:**
  - every import, export and conversion needs the SAF pickers (DocumentsUI, outside the package);
  - sharing needs the system chooser;
  - Dropbox needs an OAuth consumer key, which is empty here (`AMSecrets.java:27`);
  - the widget, the alarm (`:remote`, never dumped), boot, the providers and the VIEW/SEND intents are outside the GUI.
- **Baseline runs.** Monkey (670 methods) looped between the Recent list, Study and Detail for about 48 minutes and never opened the Open or Download tabs or the drawer. APE (1227) reached most screens, but never opened `CardListActivity`, the card player (113 methods), `DatabaseMerger` or `ShareScreen`, and never used double-sided cards (§2.3, §7).
- **Modeling plan.**
  - Pages: 121 page rows, about 150 names with `@` variants, 13 of them hidden `_PAUSED` pages (§3.3).
  - 6 areas with an explicit class-assignment rule and cross-area node names (§6), sized in methods: A1 shell/platform 372, A2 decks/files/import-export 399, A3 review sessions 511, A4 editing/list/settings/statistics 354, A5 downloaders/cloud 226, A6 data layer 330.
- **Unreachable code.** A bytecode reference scan plus data-flow checks give **227 DEAD** and **47 FRAMEWORK_ONLY** candidates, none hit by either baseline (§5). That leaves **1248 reachable methods that Monkey missed** (the target pool before env/`needs_state` refinement); 647 of them were missed by APE too (§7).
- **Likely crash paths:**
  - the card player on an empty deck throws an NPE before its "no item" dialog;
  - Dropbox logout throws an NPE (`DropboxListActivity` is never injected);
  - several PreviewEdit menu items throw an NPE on an empty deck (§5.5).

**Conventions.** Paths: `APP` = `/Users/darshan/Desktop/yang/work/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app`; `J/` = `APP/src/main/java/org/liberty/android/fantastischmemo/`; `R/` = `APP/src/main/res/`; `MAN` = `APP/src/main/AndroidManifest.xml`; `MK` / `AP` = `final_java_only/AnyMemo/{monkey,ape}/report/report.xml`. Evidence labels: SRC (file:line), DYN (from baseline coverage), FW-MEMORY (Android behaviour recalled, not checked against AOSP), INFERRED, UNVERIFIED. "M" or "A" next to a method means Monkey or APE hit it.

**What was read.** I read these files completely: all of `ui/*`, `downloader/*`, `service/*`, `receiver/*`, `widget/*`, `provider/*`, `common/*` and the component and module interfaces in `modules/`. I also read `utils/{AboutUtil,AMFileUtil,AMGUIUtility,CardTTSUtil,DatabaseImportUtil,DatabaseOperationDialogUtil,DatabaseUtil,DictionaryUtil,ErrorUtil,FolderImportExportUtil,NotificationUtil,RecentListActionModeUtil,RecentListUtil,ShareUtil,AnyMemoExecutor}`, `tts/*` and `entity/Option`, plus the manifest, the layouts, menus and xml resources referenced below, and `build.gradle`. I did not read every line of `dao/*Impl`, `converter/*`, `queue/*`, `scheduler/*` or `entity/*` (other than Option). For those I used targeted greps and the JaCoCo data.

## 0. Method universe: why 2626 vs 2192

I parsed the class files read-only with a small Python reader (there is no JDK on this Mac) and matched every method against `MK`. The two reports contain the same method set.

| Bucket | Methods | Evidence / note |
|---|---|---|
| Methods with a Code attribute in the class dir | 2874 | 633 class files |
| − JacocoInstrument (excluded by the brief) | 10 | 3 classes |
| − synthetic: bridge 213, `$values` 16, `access$` 7 | 236 | `list_methods.py` drops these too; there are no `lambda$` methods because the code uses anonymous classes only |
| − BuildConfig `<init>`, `<clinit>` | 2 | `list_methods.py --exclude BuildConfig`; **JaCoCo keeps them** |
| = `list_methods.py` count | **2626** | |
| JaCoCo-filtered, non-synthetic: Dagger `@DaggerGenerated` classes | 365 | 196 methods in 49 `*_Factory` / `*Module_Provides*Factory` classes, 167 in 32 `*_MembersInjector` classes, 2 in `DaggerAppComponents` itself (`<init>`, `builder`). The Dagger inner classes (`DaggerAppComponents$AppComponentsImpl`, `$ActivityComponentsImpl`, `$FragmentComponentsImpl`, builders) are **not** annotated and stay in JaCoCo (118 methods in package `modules`). |
| JaCoCo-filtered: enum `values()` 16, `valueOf(String)` 16, empty enum constructors 15 | 47 | e.g. `Option$ButtonStyle`, `GestureName`, `CardPlayerState`, `CardListActivity$SortMethod` |
| JaCoCo-filtered: private empty no-arg constructors | 16 | `AMGUIUtility`, `RecentListFragment$RecentItem`, `StatisticsScreen$Chart*Formatter` (2), `DataBinderMapperImpl$Inner*Lookup` (2), `DaggerAppComponents$Builder`, 9 `AppModules_*Factory$InstanceHolder` |
| JaCoCo-filtered: `<clinit>` of synthetic switch-map classes | 8 | `CardPlayerState$6`, `CardFragment$2`, `CardListActivity$12`, `FileBrowserFragment$8`, `GradeButtonsFragment$7`, `PreviewEditActivity$13`, `QACardActivity$9`, `StudyActivity$7`. These classes are absent from the report (625 classes in the report vs 633 files). |
| **JaCoCo universe** | **2192** | = 2626 − 436 + 2 (BuildConfig) |

Other scope facts:
- The APK's 19 dex files contain all 633 class-dir classes. They also contain 15 `R$*` classes and 610 `*$$ExternalSynthetic$Condy0` helpers that D8 created for the JaCoCo probes. Neither group is in the class dir, so both are out of scope. The phantom Google/Quizlet classes are **not** in the dex (checked read-only with a Python dex reader).
- `class_files.json` lists `src/androidTest/java/` as a source dir, but its 38 test files (package `…fantastischmemo.test`) are not compiled into the class dir. Several "no caller" methods are called **only from these tests**, which are not in the APK, so the calls do not count: `Converter.getSrcExtension/getDestExtension` (`AbstractConverterTest`), `CardDao.getRandomReviewedCards`/`searchPrevCard` (`CardDaoTest`), `CardImageGetter.scaleBitmap` (`CardImageGetterTest`), `RecentListUtil.getRecentDBPath` (`RecentListUtilTest`).
- Recommendation: use the JaCoCo universe (2192) as the method set, and keep the 436 filtered methods out of the verdict counts, the same way Currency left out `Data.<init>`.

## 1. Entry points

There is **no merged manifest** under `APP/build/intermediates`; only `javac/{free,pro,dev}Debug` exist. I used `MAN` plus the `pro` flavor, which overrides only `R/../pro/res/values/strings.xml`: `app_name` = "AnyMemo Pro". I then decoded the **APK's binary manifest** read-only. It matches `MAN` after placeholder substitution (`${packageName}` = `${applicationId}` = `org.liberty.android.fantastischmemopro`, `APP/build.gradle:66-69`) and adds the library components shown at the end of the table. SDK levels: minSdk 23, targetSdk 36, versionCode 241 (`APP/build.gradle:27-32`).

| Component | Kind | exported | Intent filters / special attributes | launchMode / theme / configChanges | Class in APK |
|---|---|---|---|---|---|
| `.common.AMApplication` | Application | – | meta-data `roboguice.modules`=`AMModules` (class absent, unused) | – | yes (`MAN:17-22`) |
| `.ui.AnyMemo` | Activity | **true** | MAIN/LAUNCHER; **VIEW** + DEFAULT + BROWSABLE, `scheme=content`, `mimeType=application/octet-stream`, `pathPattern=/.*\.db` | standard / NoActionBar | yes (`MAN:23-46`) |
| `.downloader.anymemo.AnyMemoDownloaderActivity` | Activity | false | – | standard | yes (`MAN:47-48`) |
| `.downloader.quizlet.QuizletLauncher` | Activity | false | – | – | **no (phantom)** (`MAN:49-50`) |
| `.downloader.google.GoogleAccountActivity` | Activity | **true** | VIEW scheme `com.googleusercontent.apps.359646043594-…` | singleTask, orientation\|keyboardHidden | **no (phantom)** (`MAN:51-62`) |
| `.downloader.google.SpreadsheetListScreen`, `.UploadGoogleDriveScreen` | Activity | false | – | orientation\|keyboardHidden | **no (phantom)** (`MAN:63-68`) |
| `.downloader.dropbox.DropboxListActivity` | Activity | false | – | NoActionBar, orientation\|keyboardHidden | yes (`MAN:69-72`) |
| `.downloader.dropbox.UploadDropboxActivity` | Activity | false | – | NoActionBar, orientation\|keyboardHidden | yes (`MAN:73-76`) |
| `.downloader.dropbox.DropboxOauth2AccountActivity` | Activity | **true** | VIEW + DEFAULT + BROWSABLE, `scheme=anymemo-dropbox` (OAuth redirect `anymemo-dropbox://oauth`, `J/common/AMEnv.java:62`) | **singleTask**, orientation\|keyboardHidden | yes (`MAN:77-88`) |
| `.downloader.quizlet.{QuizletUserPrivateActivity, QuizletUploadActivity, QuizletSearchByTitleActivity, QuizletSearchByUsernameActivity}` | Activity | false | – | – | **no (phantom)** (`MAN:89-96`) |
| `.ui.CardEditor` | Activity | false | – | orientation\|keyboardHidden | yes (`MAN:97-99`) |
| `.ui.DetailScreen` | Activity | false | – | orientation\|keyboardHidden | yes (`MAN:100-102`) |
| `.ui.SettingsScreen` | Activity | false | – | – | yes (`MAN:103-104`) |
| `.ui.CardListActivity` | Activity | false | – | – | yes (`MAN:105-106`) |
| `.ui.FileBrowserActivity` | Activity | false | – | orientation\|keyboardHidden | yes (`MAN:107-109`) |
| `.ui.OptionScreen` | Activity (`PreferenceActivity`) | false | – | – | yes (`MAN:110-111`) |
| `.ui.AlgorithmCustomizationScreen` | Activity (`PreferenceActivity`) | false | – | orientation\|keyboardHidden | yes (`MAN:112-114`) |
| `.ui.DatabaseMerger` | Activity | false | – | orientation\|keyboardHidden | yes (`MAN:115-117`) |
| `.ui.StatisticsScreen` | Activity | false | – | NoActionBar | yes (`MAN:118-120`) |
| `.ui.StudyActivity` | Activity | false | parentActivityName=AnyMemo (up is never enabled in code) | – | yes (`MAN:122-128`) |
| `.ui.PreviewEditActivity` | Activity | false | parentActivityName=AnyMemo (used by `TaskStackBuilder` in `ConvertIntentService`) | – | yes (`MAN:130-136`) |
| `.ui.QuizActivity`, `.ui.CardPlayerActivity` | Activity | false | – | – | yes (`MAN:138-141`) |
| `.ui.ShareScreen` | Activity | **true** | **SEND** + DEFAULT, `mimeType=text/*` | – | yes (`MAN:164-172`) |
| `.receiver.AlarmReceiver` | Receiver | false | none (explicit PendingIntent from `SetAlarmReceiver`) | **`process=":remote"`** | yes (`MAN:142-144`) |
| `.receiver.SetAlarmReceiver` | Receiver | **true** | `BOOT_COMPLETED` | – | yes (`MAN:145-152`) |
| `.widget.AnyMemoWidgetProvider` | Receiver (AppWidgetProvider) | **true** | `APPWIDGET_UPDATE`; `@xml/widget_info` (110×110dp, `updatePeriodMillis=0`, no configure activity, `R/xml/widget_info.xml:1-6`) | – | yes (`MAN:153-163`) |
| `.widget.UpdateWidgetService` | Service (RemoteViewsService) | false | permission `BIND_REMOTEVIEWS` | – | yes (`MAN:173-175`) |
| `.service.CardPlayerService` | Service (bound; foreground `mediaPlayback`) | false | – | – | yes (`MAN:176-179`) |
| `.service.ConvertIntentService` | Service (IntentService) | false | – | – | yes (`MAN:180-181`) |
| `.provider.CardProvider` | Provider | **true**, no permission, multiprocess | authority `org.liberty.android.fantastischmemopro.cardprovider`; URIs `*/count`, `*/random/#`, `*/ordinal/#`, `*/id/#`, `*/start_ordinal/#/count/#`, `*/all` (`J/provider/CardProvider.java:61-79`) | – | yes (`MAN:183-187`) |
| `.provider.DatabasesProvider` | Provider | **true**, no permission | authority `…databasesprovider` (lists `*.db` in the AnyMemo dir) | – | yes (`MAN:188-192`) |
| `androidx.core.content.FileProvider` | Provider (library) | false, grantUriPermissions | authority `…fileprovider`, `external-path name=external_files path="."` (`R/xml/file_provider_paths.xml:2-4`) | – | library |
| `.JacocoInstrument.SMSInstrumentedReceiver` | Receiver (harness, **excluded**) | true | `edu.gatech.m3.emma.COLLECT_COVERAGE` | – | yes (`MAN:202-207`) |
| `androidx.startup.InitializationProvider` | Provider (library; APK manifest only) | false | EmojiCompat, ProcessLifecycle, ProfileInstaller initializers | – | library |
| `androidx.profileinstaller.ProfileInstallReceiver` | Receiver (library; APK manifest only) | true, permission DUMP | 4 profileinstaller actions | – | library |

Additional facts:
- Permissions: INTERNET, WRITE_EXTERNAL_STORAGE and READ_EXTERNAL_STORAGE (maxSdk 29), RECORD_AUDIO, FOREGROUND_SERVICE (+ MEDIA_PLAYBACK), RECEIVE_BOOT_COMPLETED, POST_NOTIFICATIONS (`MAN:6-13`). The APK manifest also has `…DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION`, added for `ContextCompat.registerReceiver` (`J/ui/CardPlayerFragment.java:84`).
- There are no activity-aliases, no app shortcuts, no searchable activity, no dialog-themed activities and no `<queries>`.
- The phantom activities cannot run any app code. Starting one, for example through the exported `GoogleAccountActivity` deep link, crashes in the framework with ClassNotFoundException (FW-MEMORY). If the process was not running, only `AMApplication.onCreate` runs. Do not model them as pages.
- Process-start side effects: any component start creates the process, and so does the harness broadcast to `SMSInstrumentedReceiver` that dumps coverage. That runs `AMApplication.<init>/attachBaseContext/onCreate` (`J/common/AMApplication.java:57-74`) and the two app providers' `<init>/onCreate`. All of these were hit in both runs, even without any GUI action. Model them as ENTRY "process start" edges.

## 2. First-run flow and setup gates

### 2.1 What a new user goes through (code order)

1. **Process start.** `AMApplication.onCreate` (`J/common/AMApplication.java:63-74`) runs `AMEnv.init`, which sets every path below `getExternalFilesDir(null)/anymemo/`: `DEFAULT_ROOT_PATH`, plus the `voice/`, `images/` and `tmp/` subdirectories (`J/common/AMEnv.java:48-54`). On API 27 this is `/sdcard/Android/data/org.liberty.android.fantastischmemopro/files/anymemo/` (FW-MEMORY). It then builds the Dagger component and creates the notification channels (`J/utils/NotificationChannelUtil.java:35-…`, only on API ≥ 26). `AMEnv.<clinit>` loads `AMSecrets` by reflection (`J/common/AMEnv.java:72-93`).
2. **Storage permission (gate 1).** In `AnyMemo.onCreate`, when SDK ≤ Q and WRITE_EXTERNAL_STORAGE is not granted, the app calls `requestPermissions` (`J/ui/AnyMemo.java:124-129`). That opens a system dialog outside the app package.
   - `onRequestPermissionsResult` (`:165-182`): if granted, the app runs `loadUiComponents`; if denied, it shows a toast and calls `finish()` (`:176-178`).
   - `onResume` (`:146-162`) also loads the UI if the permission is already granted.
   - Until the permission is granted the main window is an empty frame.
3. **`loadUiComponents`** (`:184-200`):
   - `initDrawer` (`:205-267`): toolbar, drawer listener and bottom-nav listener. It then selects the Recent tab programmatically (`:263`).
   - `prepareStoreage` (`:269-285`): if `anymemo/` is not readable, it shows the "SD card not available" dialog with an Exit button (`AnyMemo$3`).
   - `prepareFirstTimeRun` (`:287-383`): when `first_time` is true or the saved version is below 154, it clears the preferences (`:305-310`). It then stores recent path 0 = sample deck, copies `assets/french-body-parts.db` (28 cards, 2 categories, `SINGLE_SIDED`, question TTS "US" and answer TTS "FR", user_version 2, read-only check with sqlite3) into `anymemo/`, and copies `assets/empty.db` into `files/` (`:315-330`).
   - If the saved version code differs from 241, it shows the **"What's new" dialog** (`:333-382`): OK; "About version" (`AnyMemo$5`), which opens a browser; an HTML link to the website (URLSpan through LinkMovementMethod); and an `import_folder` link that the code replaces with a ClickableSpan (`AnyMemo$4`). That span starts `ACTION_OPEN_DOCUMENT_TREE`, and its result goes to `onActivityResult` (`:425-434`) and then `FolderImportExportUtil.importFolder`. The `import_folder` span exists only in `upgrade_note_10_12`, which is appended when the saved version is below 239 or on a first run (`:344`; `R/values/strings.xml:157`).
   - `prepareNotification` (`:385-388`) re-arms the daily review alarm.
   - A VIEW intent is handled by `handleOpenIntent` (`:193-198`, `:393-397`).
4. There is **no account, login, password or onboarding wizard**. The sample deck makes Recent → Study usable immediately.

### 2.2 What the baseline shows about the gates

- **Permissions were pre-granted.** Both runs hit `AnyMemo.loadUiComponents` and neither ever hit `AnyMemo.onRequestPermissionsResult` (MK, AP). RECORD_AUDIO was also granted: APE hit `CardEditor.startAudioRecorder` and `AudioRecorderFragment.startRecording`, but never `CardEditor.onRequestPermissionsResult`. This is INFERRED: the harness probably installed with `-g`.
- **The first run happened in a warm-up process that is not in the reports.**
  - Segment `coverage/00000.ec` is a separate session for both tools: Monkey `unknownhost-16c575a`, device clock 05:15:11–05:15:15; APE `unknownhost-cef5d44e`. `merged.ec` and `report.xml` start with segment 1 (Monkey: 119 session entries, first 05:15:19; APE: first 22:11:09).
  - Segment 0 contains `AnyMemo$4` and `AnyMemo$5` (the What's-new dialog), yet `AnyMemo$5.<init>` is unhit in `MK`.
  - Consequence: first-launch-only code (the What's-new dialog, `AMFileUtil.copyFileFromAsset`, and the first `onUpgrade` of the sample deck) counts as "not hit by Monkey" even though it ran. Model these methods with `needs_state` "fresh app data".
  - APE re-triggered the first run by tapping Misc → "Reset all preferences" → OK (`MiscTabFragment$1.onClick` hit, `J/ui/MiscTabFragment.java:350-365`). That clears the preferences and finishes the activity, so the next launch takes the first-run path again. This is why AP shows `AnyMemo$5.onClick` and `AMFileUtil.copyFileFromAsset`.
- **Monkey ran in a single process for the whole hour** (one session id across segments 1–119), so it never crashed. **APE ran in 17 processes** (16 restarts). Coverage recorded since the last 30-s dump is lost when a process dies, so "never hit" is not strictly "never executed" for crash-prone handlers (DYN).
- **Monkey timeline** (first segment in which a class has any probe; one segment ≈ 30 s):
  - `StudyActivity`, `QACardActivity`, `GradeButtonsFragment` at seg 1; `DetailScreen` at 4.
  - Then nothing new until `CategoryEditorFragment` at 41, `MiscTabFragment`, `ConverterFragment` and `ExportAnyMemoDbFragment` at 98, `OptionScreen` and `AlgorithmCustomizationScreen` at 99.
  - Segments 100–119 show only 2–18 classes with probes, so the app was essentially idle (cause UNVERIFIED).
  - Monkey's line coverage of `AnyMemo.java` covers `:240-241` and `:249-250` but not `:243-248` (Open/Download tab creation) or `:213-229` (drawer listener).
  - So Monkey looped between the Recent list (a row tap opens Study, `J/ui/RecentListFragment.java:413-428`) and the Study screen.
- **APE** first reached the Open tab at seg 1, Misc and Options at 2, Download/Dropbox auth and OpenActions at 9, Study/PreviewEdit at 10, CardEditor at 11, the AnyMemo downloader at 30, Settings at 45, FileBrowserActivity at 51, Statistics at 58, and Quiz at 64–65.

### 2.3 Screens the baseline never reached, and the most likely gate

| Screen / component | Monkey | APE | Most likely gate |
|---|---|---|---|
| `CardListActivity` (66 methods) | 0 | 0 | Not explored. Reachable from OpenActions "List" (`J/ui/OpenActionsFragment.java:139-145`) and PreviewEdit menu `editmenu_list_id` (`J/ui/PreviewEditActivity.java:285-294`). APE line coverage shows the `if` tested and the body (`:140-144`, `:287-293`) missed. No crash path was found in `onCreate`. |
| `CardPlayerActivity`, `CardPlayerFragment`, `CardPlayerSettingDialogFragment`, `CardPlayerService`, `service/cardplayer/*` (113) | 0 | 0 | Not explored. OpenActions "Card player" (`:192-197`, APE missed `:193-196`) and PreviewEdit `menu_card_player` (`:307-316`, missed). On an empty deck it crashes, see §5.6. |
| `DatabaseMerger` (8) | 0 | 0 | Not explored: Misc "Merge" (`J/ui/MiscTabFragment.java:346-349`, missed) and PreviewEdit "more → merge" (`:400-404`, missed). |
| `ShareScreen` (4) | 0 | 0 | Entered only through SEND text/*. Inside the app that means Study/PreviewEdit "Share" → system chooser (`J/utils/ShareUtil.java:38-44`), which is outside the package. Monkey/APE `-p` block foreign activities (FW-MEMORY). |
| `DropboxListActivity`, `DropboxListFragment`, `UploadDropboxActivity` (33) | 0 | 0 | OAuth: `getLoginUrl` uses the empty consumer key (`J/downloader/dropbox/DropboxOauth2AccountActivity.java:38-42`, `J/common/AMSecrets.java:27`); `requestAuth` opens a Custom Tab (`J/downloader/oauth/Oauth2AccountActivity.java:127-132`). APE hit `requestAuth` but never `onNewIntent`. |
| `ConvertIntentService` + all `converter/*` `convert` methods; `DatabaseImportUtil`, `FolderImportExportUtil` (bodies) | 0 | 0 | SAF: `ACTION_OPEN_DOCUMENT` / `OPEN_DOCUMENT_TREE` / `CREATE_DOCUMENT` (`J/ui/MiscTabFragment.java:247-264,408-414`; `J/ui/RecentListFragment.java:186-193`; `J/ui/FileBrowserFragment.java:311-316`; `J/ui/ConverterFragment.java:130-134`; `J/ui/ExportAnyMemoDbFragment.java:45-52`). Results came back canceled: `onActivityResult` was hit (AnyMemo M+A, Misc M, Recent A, FileBrowser A) with only the non-OK branches. |
| `FlipableCardFragment` (7) | 0 | 0 | Setting: per-deck card style `DOUBLE_SIDED` (`J/ui/QACardActivity.java:371-386`). The sample deck is SINGLE_SIDED, and APE never saved that spinner value. |
| `AnyMemo` VIEW handling (`handleOpenIntent` + loader classes: 8) | 0 | 0 | Needs an external VIEW intent with a `content://…/*.db` URI. |
| `AlarmReceiver`, `NotificationUtil.showNotification` | 0 | 0 | Time-gated: the alarm fires at 07:02:03 + interval (≥ 1 h) (`J/receiver/SetAlarmReceiver.java:45-93`). It runs in `:remote`, which is never dumped (the harness receiver runs in the main process). |
| `SetAlarmReceiver.onReceive` | 0 | 0 | `BOOT_COMPLETED` only. |
| Widget (`AnyMemoWidgetProvider.onUpdate`, `UpdateWidgetService`, `WidgetRemoteViewsFactory`: 17) | 1 (`updateWidget`) | 1 | A widget must be placed on the home screen (outside the package). |
| Provider `query/insert/update/delete/getType` | 0 | 0 | Only reachable from outside (`adb shell content …`). |
| `EditTabFragment`, `OauthAccountActivity`, `OauthAccessCodeRetrievalFragment`, `ErrorUtil` | 0 | 0 | DEAD (no instantiation or subclass, §5). |
| Partially reached: PreviewEdit (38/68 A), SettingsScreen (39/50 A), Statistics (21/27 A), CardEditor (35/50 A), Quiz (29/37 A) | 0 | partial | Monkey never left Study; APE skipped submenus, the search action view, gestures and some dialogs (§7). |

### 2.4 What a harness must prepare to reach the rest

1. **Permissions.** Grant WRITE_EXTERNAL_STORAGE (API ≤ 29) and RECORD_AUDIO up front, or let the tool handle the system dialog. Without storage, `loadUiComponents` never runs.
2. **App data state.**
   - A fresh install, or Misc → Reset, covers the first-run code.
   - Keep at least one deck in the recent list: OpenActions "Delete" on the only deck empties the Recent tab, and most deck screens then need Open → FAB "Create DB" first (`J/ui/FileBrowserFragment.java:447-461`).
3. **Files in the app dir** `/sdcard/Android/data/org.liberty.android.fantastischmemopro/files/anymemo/`, which the in-app file browsers use:
   - a second `.db` (a copy of `assets/french-body-parts.db`) for merge source/target and Open-tab file actions;
   - an **empty deck** (`assets/empty.db`) for all "no item" dialogs and `S_PREVIEW_EMPTY`;
   - a deck with several categories;
   - a deck whose cards contain `<img src="photo_1.jpg">` and audio names, with the files in `anymemo/images/<db>/` and `anymemo/voice/<db>/` (`J/ui/QACardActivity.java:218-227`, `J/tts/SpeakWord.java:47-62`);
   - a `.ttf` font (none in `_fixtures`) for the typeface pickers (`J/ui/SettingsScreen.java:712-733`);
   - a deck with ≥ 10 due cards, because the notification threshold is `revCount < 10 → return` (`J/utils/NotificationUtil.java:44-46`);
   - a pre-9.0 deck with `dict_tbl`/`learn_tbl` tables and user_version 0 for `convertOldDatabase` (`J/common/AnyMemoDBOpenHelper.java:73-…`), and a DB with user_version > 5 for `onDowngrade`.
4. **Files for SAF** in `/sdcard/Download`, picked through DocumentsUI:
   - an AnyMemo `.db` (the `_fixtures` folder has none);
   - a CSV with ≥ 2 columns (`_fixtures/Download/table.csv` works; format at `J/converter/CSVImporter.java:83-108`);
   - a `Q:`/`A:` text file (`todo.txt` does not match `J/converter/QATxtImporter.java:76-106`);
   - a tab-separated txt;
   - Mnemosyne XML, SuperMemo XML, SuperMemo 2008 XML, a Mnemosyne 2 `.cards` file and a `.zip` that contains a `.db` (`archive.zip` contains only txt files);
   - a folder for the folder import/export.
   - `Pictures/*.jpg`, `Download/image_*.png` and `Music/*.mp3|*.wav` can be picked through `FileBrowserActivity` by navigating up from `anymemo/`, because the extension filters are `.png,.jpg,.tif,.bmp` (`J/ui/CardEditor.java:180-186`) and `.3gp,.ogg,.mp3,.wav,.amr` (`:290-295`).
5. **Settings that unlock modes:**
   - per-deck (SettingsScreen): card style double-sided; audio locale "disabled" (gives `NullAnyMemoTTS`) or user audio; custom colors; fonts; HTML and field options;
   - global (OptionScreen): `speech_ctl` AUTO/AUTOTAP/MANUAL, `button_style` ANYMEMO/MNEMOSYNE (Anki hides grades 1/3/4: `R/layout/grade_buttons_anki.xml:24,43,53`), `enable_volume_key`, `copy_to_clipboard`, `dict_app`, `shuffling_cards`, `fullscreen_mode`, `allow_orientation`, `enable_animation`, `notification_interval`, `recent_count`, `interface_locale` (`R/xml/option_screen.xml:11-90`);
   - gestures enabled (checkbox in `GestureSelectionDialogFragment`, `J/ui/GestureSelectionDialogFragment.java:193-200`);
   - card-player repeat/shuffle and intervals.
6. **Other apps:**
   - a browser with Custom Tabs (help/website links, Dropbox login);
   - share targets;
   - an image viewer (ACTION_VIEW image/*, `J/ui/QACardActivity.java:712-720`);
   - a dictionary app: `colordict.intent.action.SEARCH`, `com.ngc.fora.action.LOOKUP` or `bluedict.intent.action.FLOATSEARCH` (`J/utils/DictionaryUtil.java:115-160`). Without one, the code takes the `displayException` path, which APE did hit.
   - A TTS engine: present on the baseline emulator, since `AnyMemoTTSImpl.onInit` and `$2.onUtteranceCompleted` were hit (DYN).
7. **Network:** `https://anymemo.org/api/legacy_database/list` and `/download/<name>` (`J/downloader/anymemo/AnyMemoDownloaderFragment.java:27-29,96-…`). It worked for APE: `RetrieveTask`, `openCategory` and `FetchDatabaseTask` were all hit. The Dropbox API also needs the network.
8. **Accounts/keys:** Dropbox needs a rebuilt APK with a consumer key and a real account. Workaround: while `DropboxOauth2AccountActivity` is running (singleTask), deliver `am start -a android.intent.action.VIEW -d "anymemo-dropbox://oauth#access_token=X"`. `onNewIntent` → `fetchAuthTokenFromCallback` → `onAuthenticated` → `DropboxListActivity` (`J/downloader/oauth/Oauth2AccountActivity.java:59-103`). With a fake token the listing fails into `displayError`, but the activity, fragment and helper code runs (INFERRED).
9. **System or adb actions:**
   - place the widget;
   - reboot, or a root broadcast of `BOOT_COMPLETED`, which is a protected broadcast (FW-MEMORY);
   - fire the alarm by changing the time, with `cmd alarm`, or through a root broadcast to `AlarmReceiver` with extra `request_code` (`J/receiver/AlarmReceiver.java:44-71`);
   - `content query --uri content://org.liberty.android.fantastischmemopro.cardprovider/french-body-parts.db/count`;
   - a VIEW intent with `-t application/octet-stream -d content://org.liberty.android.fantastischmemopro.fileprovider/external_files/Download/x.db` (the app can read its own FileProvider; INFERRED);
   - a SEND intent to `ShareScreen` (it NPEs without an action, `J/ui/ShareScreen.java:84`).
10. **Coverage:** `AlarmReceiver` and everything it calls run in `:remote`, which the harness never dumps. Either add a dump in that process or mark these methods "not observable".

## 3. Screens and navigation

### 3.1 Window inventory: handlers and transitions

Menus are inflated as listed. Leftover resources that no code references are not windows: menus `add_screen_menu`, `edit_screen_menu`, `editscreen_context_menu`, `export_menu`, `google_drive_spreadsheet_list_menu`, `import_menu`, `open_screen_context_menu`, `quizlet_cardsets_menu`, and layouts `about_screen`, `cardsets_list_screen`, `color_picker`, `downloader`, `drawer_list_item`, `dropbox_launcher`, `filter_dialog`, `flashcard_screen`, `login_dialog`, `memo_screen_layout`, `quizlet_launcher`, `spreadsheet_list_screen`, `upload_google_drive_screen`, `upload_quizlet_screen` (grep of `R.menu.*` / `R.layout.*` / `@layout` / `@menu`).

**A. `ui.AnyMemo`** (main activity; `R/layout/main_tabs.xml`: DrawerLayout + Toolbar + `page_fragment_container` + BottomNavigationView + NavigationView, data binding `MainTabsBinding`)
- Toolbar home (hamburger): `onOptionsItemSelected(android.R.id.home)` → `openDrawer` (`J/ui/AnyMemo.java:414-420`). Up is enabled at `:265-266`.
- **Drawer** (`R/menu/main_screen_drawer_menu.xml:3-34`), handled by `AnyMemo$1.onNavigationItemSelected` (`:209-232`): recent, open, download and misc each call `bottomNavigation.setSelectedItemId`; `option_tab_menu` → `startActivity(OptionScreen)`; `about_tab_menu` → `AboutUtil.createAboutDialog`; then `closeDrawers`.
- **Bottom nav** (`R/menu/main_tab_items.xml:3-19`), handled by `AnyMemo$2` (`:234-261`): it replaces the content with `RecentListFragment` / `OpenTabFragment` (args `EXTRA_SHOW_CREATE_DB_BUTTON=true`) / `DownloadTabFragment` / `MiscTabFragment`. The listener also fires on the programmatic `setSelectedItemId(recent)` at `:263`. That is FW-MEMORY, and it is consistent with Monkey: `AnyMemo$2.onNavigationItemSelected` was hit although Monkey never opened the Open or Download tabs.
- Dialogs: the What's-new dialog (§2.1) and `AnyMemo$3` (storage Exit → `finish`).
- `onActivityResult` (`:424-434`): only `REQUEST_CODE_IMPORT_FOLDER` + OK → `FolderImportExportUtil.importFolder`. As an override it is called for every result delivered to the activity, including fragment results, which super dispatches (FW-MEMORY).
- VIEW intent → `HandleOpenIntentLoaderCallbacks` → `FileAsyncTaskLoader.loadInBackground` (copies the URI to `anymemo/`, runs `checkDatabase`) → `onLoadFinished`. A null result shows a Snackbar; otherwise the deck is added to the recent list and `PreviewEditActivity` starts (`:436-531`).
- `onDestroy` (`:399-412`) calls `AnyMemoWidgetProvider.updateWidget` and `NotificationUtil.cancelNotification`.

**B. Tab fragments inside AnyMemo**
- **`RecentListFragment`** (RecyclerView + `RecentListAdapter extends SelectableAdapter`; FAB `import_fab`)
  - Row tap (`$RecentListAdapter$1`, `J/ui/RecentListFragment.java:413-428`): with no selection it adds the deck to the recent list and starts `StudyActivity(dbpath)`; otherwise it toggles the selection. Either way it then calls `updateActionMode`.
  - Long-press (`$2`, `:430-440`): starts the action mode if nothing is selected, then toggles.
  - "More" button (`$3`, `:442-452`) → `OpenActionsFragment` dialog.
  - FAB (`$3` of the fragment, `:186-193`) → SAF OPEN_DOCUMENT; `onActivityResult` (`:201-213`) → `DatabaseImportUtil.handleImportDbResult(…, onSuccess = onResume)`.
  - Menu (`R/menu/open_screen_menu.xml:4-6`): `openmenu_clear` → `clearRecentList` + `onResume` (`:228-235`).
  - `onResume` restarts loaders 1 and 2 (name list, then detail list), which call `setItems` and `notifyDataSetChanged` (`:216-310`).
  - Action mode through `RecentListActionModeUtil` LocalBroadcasts (`J/utils/RecentListActionModeUtil.java:35-142`): CAB `action_menu_remove` (`R/menu/action_menu.xml:4-9`) → `ACTION_REMOVE_SELECTED` → `RecentListFragment$1.onReceive` → `removeSelected`. `onDestroyActionMode` → `ACTION_DESELECT_ALL` → `$2.onReceive` → `deselectAll`. When the count reaches 0 the CAB finishes (`:44-55`).
- **`OpenTabFragment extends FileBrowserFragment`** (embedded):
  - Row tap → `openFile`: `..` or a directory → `browseTo`; a file → `OpenTabFragment$1.onFileBrowserFileClick` → `OpenActionsFragment` (`J/ui/OpenTabFragment.java:41-50`).
  - Long-press on a file → item dialog (Delete / Clone / Rename), each through a `DatabaseOperationDialogUtil` Maybe (`J/ui/FileBrowserFragment.java:521-585`).
  - FAB → create-DB dialog (`:447-461`).
  - Menu (`R/menu/file_browser_menu.xml:4-14`): `file_browser_createdb`, `file_browser_importdb` (SAF OPEN_DOCUMENT → `onActivityResult` → overwrite dialog / `importDb`), `file_browser_createdirectory`, `file_browser_gohome` (`:289-322`).
- **`DownloadTabFragment`**: `source_anymemo` → `AnyMemoDownloaderActivity`; `source_dropbox` → `DropboxOauth2AccountActivity` (`J/ui/DownloadTabFragment.java:63-70`).
- **`MiscTabFragment`**, `onClick` (`J/ui/MiscTabFragment.java:225-399`):
  - `misc_options` → `OptionScreen`.
  - `misc_import` / `misc_export` toggle the sections (`:229-245`).
  - Import: AnyMemo DB → SAF OPEN; AnyMemo folder → SAF TREE; Mnemosyne XML / Mnemosyne 2 / SuperMemo / CSV / Tab / QA / SuperMemo 2008 / Zip → `launchImportConvert` → SAF OPEN (`:408-414`) → `onActivityResult` (`:417-466`) → merge dialog (`$3` Yes, `$4` No) or `invokeImportConversion` → `startService(ConvertIntentService)`.
  - Export: AnyMemo DB → `ExportAnyMemoDbFragment`; folder → SAF TREE; XML / Mnemosyne 2 / CSV / Tab / QA / Zip → `ConverterFragment(EXTRA_CONVERTER_CLASS)` (`:288-337`).
  - `misc_default_settings` → `SettingsScreen(files/empty.db)` (`:339-345`); `misc_merge` → `DatabaseMerger`.
  - `misc_reset` → confirm (`$1`: clear prefs + `mActivity.finish()`).
  - `misc_donate` is **GONE in pro** (`:212-215`).
  - `misc_help` → browser; `misc_about` → AboutUtil.

**C. Dialog fragments and dialogs over AnyMemo**
- **`OpenActionsFragment`** (STYLE_NO_TITLE; `R/layout/open_actions_layout.xml`), `buttonClickListener` (`J/ui/OpenActionsFragment.java:119-200`):
  - study → `StudyActivity`; edit → `PreviewEditActivity` (start id from prefs); list → `CardListActivity`; quiz → `QuizLauncherDialogFragment`; settings → `SettingsScreen`; statistics → `StatisticsScreen`; share → `ShareUtil.shareDb` (chooser); card player → `CardPlayerActivity`.
  - delete → confirm (`$1$1`: `deleteDbSafe` + `deleteFromRecentList` + `AnyMemo.restartActivity`).
  - Every tap dismisses the dialog.
- **`ExportAnyMemoDbFragment`** (`FileBrowserFragment` shown as a dialog): file tap → SAF CREATE_DOCUMENT → `onActivityResult` → Rx copy → toast + dismiss (`J/ui/ExportAnyMemoDbFragment.java:33-102`).
- **`ConverterFragment`** (`FileBrowserFragment` as a dialog): file tap → `startConversion` → for exporters (destination ≠ db) SAF CREATE_DOCUMENT → `onActivityResult` → `invokeConverterService` → `ConvertIntentService` (`J/ui/ConverterFragment.java:83-168`).
- `DatabaseOperationDialogUtil` dialogs: create DB (`:39-84`), delete (`:86-117`), clone (no dialog on success; error dialog, `:119-139`), rename (`:141-181`), create folder (`:183-219`).
- `DatabaseImportUtil` overwrite dialog (`J/utils/DatabaseImportUtil.java:37-62`); `AboutUtil` dialog (`J/utils/AboutUtil.java:29-60`).

**D. Review windows (all `QACardActivity` subclasses)**
- **`QACardActivity`** base:
  - `startInit` registers the setting and TTS loaders with `MultipleLoaderManager` and shows a non-cancelable ProgressDialog (`J/ui/loader/MultipleLoaderManager.java:79-102`); once all loaders finish, the runnable calls `onPostInit` (`J/ui/QACardActivity.java:147-171`).
  - `displayCard` builds `CardFragment.Builder`s and replaces `card_root` with `TwoFieldsCardFragment` (single-sided: two ViewPagers with `FragmentStatePagerAdapter`) or `FlipableCardFragment` (double-sided) (`:197-417`).
  - Listeners: question/answer text taps (`$4`/`$5`), question/answer view taps (`$6`/`$7`), the buttons area (`$1`), long-press on text for an image (`$3` → ACTION_VIEW image), and gestures (`$8`, `GestureOverlayView` enabled only when `card_gesture_enabled`, `:541`).
  - Keys: volume keys handled in `onKeyDown`/`onKeyUp` when `enable_volume_key` is set (`:596-623`). `copyToClipboard` runs when the answer is shown (`:626-656`).
  - `onDestroy` releases the helper and TTS and updates the widget (`:489-503`).
- **`StudyActivity`** (`R/layout/qa_card_layout_study.xml` + `GradeButtonsFragment` in `buttons_root`)
  - Menu (`R/menu/study_activity_menu.xml:4-41`), dispatched in `onOptionsItemSelected` (`J/ui/StudyActivity.java:145-194`):
    - `menuundo` → `undoCard`: with a previous card it calls `restartActivity`, else the undo-fail dialog.
    - `menudetail` → `DetailScreen` for result.
    - `menusettings` → `SettingsScreen` for result.
    - `menuspeakquestion` / `menuspeakanswer`.
    - `menu_memo_category` → `CategoryEditorFragment`.
    - `menu_memo_help` → browser.
    - `menu_context_edit` → `CardEditor` for result.
    - `menu_share` → chooser.
    - `menu_context_delete` → confirm.
    - `menu_mark_as_learned_forever` → confirm.
    - `menu_context_gotoprev` → `PreviewEditActivity`.
    - `menu_context_lookup` → `DictionaryUtil` list dialog.
    - `menu_gestures` → `GestureSelectionDialogFragment`.
  - `onActivityResult` with a non-canceled result → `restartActivity` (finish + new StudyActivity) (`:205-245`, `:260-271`).
  - Grade button tap → `GradeTask` (AsyncTask) → `onCardChanged` (`$4`, `:589-620`) → next card, or the no-item dialog.
  - Long-press on a grade → help toast.
  - No-item dialog (`$2`/`$1`) → `onBackPressed`.
- **`QuizActivity`**: menu `menu_lookup`, `menu_speak_question`, `menu_speak_answer` (`R/menu/quiz_activity_menu.xml:4-11`; `J/ui/QuizActivity.java:154-165`). Grading → `ChangeCardTask` → complete-new dialog (Review / Cancel) and complete-all dialog (`:354-450`).
- **`QuizLauncherDialogFragment`** (AlertDialog):
  - Radios group / category / range toggle their settings panels (`$1`).
  - Four TextWatchers and two focus listeners (`$4`–`$9`).
  - The category button opens `CategoryEditorFragment` (`$3`).
  - Start (`$2`, `J/ui/QuizLauncherDialogFragment.java:230-268`) → `QuizActivity` with category, range or group extras.
- **`CardPlayerActivity`**: binds `CardPlayerService` (`J/ui/CardPlayerActivity.java:210-234`). `CardPlayerFragment` buttons play/stop, previous, next, repeat, shuffle (`J/ui/CardPlayerFragment.java:148-193`). Menu `card_player_settings` → `CardPlayerSettingDialogFragment` (seek bars; `onDismiss` saves the preferences). Back → `RESULT_OK` with the current card id (`:180-185`). The service broadcasts `ACTION_GO_TO_CARD` / `PLAYING_STOPPED` (`J/service/CardPlayerService.java:226-244`) to the fragment's receiver (`J/ui/CardPlayerFragment.java:220-249`).

**E. Editing and deck tools**
- **`PreviewEditActivity`** (`R/layout/qa_card_layout_preview_edit.xml`: New / Edit / Prev / Next buttons)
  - Buttons: New and Edit → `CardEditor` for result; Prev and Next → `gotoPrev` / `gotoNext` (`J/ui/PreviewEditActivity.java:591-627`).
  - Menu (`R/menu/preview_edit_activity_menu.xml:4-71`):
    - `action_search` (SearchView; submit → `SearchCardTask`, `:690-761`);
    - `editmenu_delete_id` → confirm → `DeleteCardTask`;
    - `editmenu_list_id` → `CardListActivity` for result;
    - speak question / answer;
    - `editmenu_settings_id`, `editmenu_detail_id` (for result);
    - `menu_edit_categories`;
    - `menu_card_player` (for result);
    - copy, paste, swap current, reset current, share, gestures;
    - submenu: wipe, swap all, remove duplicates, merge DB, shuffle (via `AMGUIUtility.doConfirmProgressTask` / `doProgressTask`);
    - `editmenu_help`.
  - Left / right swipe gestures → next / prev (`:432-452`).
  - `onPause` saves the start id.
- **`CardEditor`**
  - Menu (`R/menu/card_editor_menu.xml:4-21`; `J/ui/CardEditor.java:168-204`): save; `editor_menu_br`; `editor_menu_image` (focus-dependent → `FileBrowserActivity` for result); `add_existing_audio`; `add_new_audio` (permission → `AudioRecorderFragment`); `remove_audio`.
  - Category button → `CategoryEditorFragment`.
  - Radio add-here / add-back, new card only (`:421-459`).
  - Back → unsaved dialog in edit mode when the text changed (`:127-159`).
- **`AudioRecorderFragment`** (AlertDialog): record / play / save toggles (`J/ui/AudioRecorderFragment.java:44-81`).
- **`DetailScreen`**: menu save (confirm → `SaveCardTask`; a parse error goes to `displayException`) and reset (`R/menu/detail_screen_menu.xml:6-10`; `J/ui/DetailScreen.java:115-150`).
- **`CardListActivity`**
  - Menu: `action_search` (SearchView → adapter `Filter`), `sort` (single-choice dialog), `show_hide_answers` (`R/menu/card_list_activity_menu.xml:5-15`; `J/ui/CardListActivity.java:177-186,410-420`).
  - Row tap: if the answer is hidden it reveals it; otherwise PopupMenu mark learned / forgotten / new / learned forever (`:423-435`, `:188-210`).
  - Row long-press: PopupMenu edit / detail / preview edit (`:437-446`, `:212-234`).
- **`CategoryEditorFragment`** (dialog, ListView + `ArrayAdapter`)
  - Buttons OK / New / Edit / Delete. Delete is a `DoubleClickButton`: the first tap shows a toast, a second tap within 5 s acts (`R/layout/category_dialog.xml:67-76`).
  - The listeners are attached only after `InitTask.onPostExecute` (`J/ui/CategoryEditorFragment.java:170`) and detached while the Edit and New tasks run (`:184`, `:242`).
- **`SettingsScreen`**
  - The layout is set only after the setting loader finishes (`J/ui/SettingsScreen.java:268-353`).
  - Controls: 9 `AMSpinner`s; checkboxes color / typeface Q / typeface A / HTML / field1 / field2; color button → picker; typeface edits → font picker (`FileBrowserFragment` dialog) (`:640-735`).
  - Menu save / load default / help (`R/menu/settings_menu.xml:5-12`).
  - Back with changes → unsaved dialog (`:195-222`).
- **`StatisticsScreen`**: hamburger → drawer (`R/menu/statistics_screen_menu.xml:5-15`, 4 charts) → ChartTask subclasses (`J/ui/StatisticsScreen.java:109-150`).
- **`OptionScreen`** and **`AlgorithmCustomizationScreen`** (PreferenceActivity): the preference XML (`R/xml/option_screen.xml`, `R/xml/algorithm_customization_screen.xml`). Custom preference click on `customize_scheduling_algorithm_key` → warning → `AlgorithmCustomizationScreen`; `reset_customized_scheduling_algorithm` → confirm → finish + `SchedulingAlgorithmParameters.reset` (`J/ui/OptionScreen.java:44-84`; `J/ui/AlgorithmCustomizationScreen.java:42-80`).
- **`DatabaseMerger`**: target / source edits → `FileBrowserActivity` for result; merge → `AMGUIUtility.doProgressTask` → toast + finish, or the "same DB" toast, or the exception dialog; cancel (`J/ui/DatabaseMerger.java:53-136`).
- **`ShareScreen`**: save, save & preview (→ `PreviewEditActivity`), cancel, and the DB name field (→ `FileBrowserActivity`) (`J/ui/ShareScreen.java:64-158`).
- **`FileBrowserActivity`**: embeds `FileBrowserFragment`; a file tap returns `RESULT_OK` with `EXTRA_RESULT_PATH` (`J/ui/FileBrowserActivity.java:38-73`). The fragment's options menu (create DB / import DB / create dir / home) is also active here (INFERRED: the activity has the default action bar theme).

**F. Downloaders**
- **`AnyMemoDownloaderActivity`** (layout `<fragment>` = `AnyMemoDownloaderFragment`, `R/layout/anymemo_downloader.xml:2-6`)
  - `RetrieveTask` (non-cancelable ProgressDialog) → list of categories.
  - Row tap (`DownloadListAdapter$1`): Category → `openCategory`; Back (`..`) → `goBack`; Database → confirm → `FetchDatabaseTask` → success dialog. A connection error → `AMGUIUtility.displayError` (finish) (`J/downloader/common/AbstractDownloaderFragment.java:179-435`).
- **`DropboxOauth2AccountActivity`**: no UI of its own. If a token is saved → verify (network) → `DropboxListActivity`; otherwise a Custom Tab login (`J/downloader/oauth/Oauth2AccountActivity.java:38-132`).
- **`DropboxListActivity`**: list (same fragment base), FAB → `UploadDropboxActivity` for result, menu logout (`R/menu/dropbox_list_menu.xml:4-5`; `J/downloader/dropbox/DropboxListActivity.java:36-104`).
- **`UploadDropboxActivity`**: an embedded `FileBrowserFragment` with no listener, so `notifyFileClick` falls through to the activity's `onFileBrowserFileClick` (`J/ui/FileBrowserFragment.java:434-440`). It then shows the upload confirm, runs the Rx upload, and shows a success or exception dialog (`J/downloader/dropbox/UploadDropboxActivity.java:77-126`).

**G. Outside the GUI**
- Widget rows → `StudyActivity` (fill-in `dbpath`; `J/widget/WidgetRemoteViewsFactory.java:74-94`, template at `J/widget/AnyMemoWidgetProvider.java:70-74`).
- Review notification → `AnyMemo` (`J/utils/NotificationUtil.java:41-69`).
- Conversion notification: for a `.db` → `PreviewEditActivity` with a synthesized AnyMemo parent; otherwise → `AnyMemo` (`J/service/ConvertIntentService.java:181-212`).
- Card-player notification → `CardPlayerActivity` with SINGLE_TOP (`J/service/CardPlayerService.java:198-224`).

### 3.2 Modes that change active handlers

| Window | Modes (predicate) | Evidence |
|---|---|---|
| AnyMemo | tab ∈ {RECENT, OPEN, DOWNLOAD, MISC} (fragment in `page_fragment_container`); drawer open; permission pending (empty frame); What's-new shown (first run or upgrade) | `J/ui/AnyMemo.java:124-129,234-263,333` |
| Recent tab | empty vs non-empty (`items.size()`); **selection / action mode** (`getSelectedItemCount() > 0`): a row tap toggles instead of opening Study | `J/ui/RecentListFragment.java:416,433`; `J/utils/RecentListActionModeUtil.java:37-55` |
| FileBrowserFragment (any host) | host context: OPEN tab (FAB visible: `showCreateDbButton`), dialog (Export / Converter / Font), picker activity, upload activity; dismiss-on-select (font picker); current directory listable or not (toast) | `J/ui/FileBrowserFragment.java:131-175,196,222-235,412-421` |
| Misc tab | import section expanded; export section expanded (independent); donate hidden (pro) | `J/ui/MiscTabFragment.java:212-245` |
| QACardActivity subclasses | loading (ProgressDialog) vs loaded; **answer shown** (`isAnswerShown`); **card style** SINGLE vs DOUBLE (different fragment and tap semantics); gestures enabled; volume-key shortcut; speaking type TAP / AUTO / AUTOTAP / MANUAL; copy-to-clipboard; button style (Anki hides 3 grade buttons) | `J/ui/QACardActivity.java:321,371,541,597-623`; `J/ui/StudyActivity.java:303-323,338-380`; `J/ui/GradeButtonsFragment.java:132-145` |
| StudyActivity | queue empty → no-item dialog; undo possible (`prevCard != null`); category filter active | `J/ui/StudyActivity.java:286-292,549-572` |
| QuizActivity | question/answer; new cards done (complete-new dialog shown once); queue empty | `J/ui/QuizActivity.java:434-450` |
| QuizLauncher | radio group / category / range (panel visibility) | `J/ui/QuizLauncherDialogFragment.java:216-228` |
| CardPlayer | stopped vs playing (`playButton.isSelected()`); service bound vs not yet (`cardPlayerService == null` → NPE on tap); repeat / shuffle | `J/ui/CardPlayerFragment.java:158-193`; `J/ui/CardPlayerActivity.java:221-234` |
| PreviewEdit | current card present vs empty deck/category; search expanded; copied card present (paste needs `savedCardId`) | `J/ui/PreviewEditActivity.java:164,317-333,245-255` |
| CardEditor | new vs edit (`isEditNew`: radio visible; unsaved dialog only in edit mode); **focus** in question / answer / note (menu items act only when focused) | `J/ui/CardEditor.java:168-204,224-231,421-459` |
| AudioRecorder | idle / recording / recorded / playing (button enablement) | `J/ui/AudioRecorderFragment.java:44-81` |
| CardList | answers visible vs hidden (row tap reveals vs popup); search filter active | `J/ui/CardListActivity.java:303-317,423-435` |
| CategoryEditor | loading (no listeners) vs loaded; task running (listeners detached) | `J/ui/CategoryEditorFragment.java:170,184,242,412-424` |
| SettingsScreen | loading (no content view) vs loaded; color row visible; typeface edits visible; changed (`settingsChanged` → unsaved dialog on Back) | `J/ui/SettingsScreen.java:268-353,640-735,195-222` |
| Downloader | loading / category list / inside category (Back row) | `J/downloader/anymemo/AnyMemoDownloaderFragment.java:42-72` |
| DropboxOauth2 | token saved vs not; callback received (`onNewIntent`) | `J/downloader/oauth/Oauth2AccountActivity.java:38-63` |

### 3.3 Candidate page list

There are 121 page rows. Expanding the `@X` variants listed in a row gives about 150 page names; collapse `S_DLG_PREF@KEY` to 3 pages (`@LIST`, `@FLOAT`, `@INT`), because only the Float/Integer preferences run app code. 13 rows are hidden `*_PAUSED` pages, one for each activity that can sit under another window: Main, Options, Merge, Share, Study, Quiz, Player, Preview, Editor, List, Settings, DropboxAuth and DropboxList.

| # | Page | Window class | Mode predicate / description | Area |
|---|---|---|---|---|
| 1 | S_ENTRY | – | Outside the app (launcher, home, adb). Root of the search. | A1 |
| 2 | S_EXIT | – | App finished or crashed; process statics may survive (`AnyMemoDBOpenHelperManager` maps, `AnyMemoExecutor`, `AMEnv`) | A1 |
| 3 | S_MAIN_PAUSED | AnyMemo | stopped under another window | A1 |
| 4 | S_PERMISSION@STORAGE | system GrantPermissionsActivity | SDK ≤ 29 and storage not granted, over AnyMemo | A1 |
| 5 | S_PERMISSION@RECORD_AUDIO | system | RECORD_AUDIO not granted, over CardEditor | A1 |
| 6 | S_EXT_SAF_OPEN | DocumentsUI | ACTION_OPEN_DOCUMENT picker | A1 |
| 7 | S_EXT_SAF_TREE | DocumentsUI | ACTION_OPEN_DOCUMENT_TREE | A1 |
| 8 | S_EXT_SAF_CREATE | DocumentsUI | ACTION_CREATE_DOCUMENT | A1 |
| 9 | S_EXT_CHOOSER | system chooser | `Intent.createChooser(ACTION_SEND)`; AnyMemo `ShareScreen` is a target for text | A1 |
| 10 | S_EXT_BROWSER | browser / Custom Tab | help and website links, Dropbox OAuth page | A1 |
| 11 | S_EXT_APP | other app | dictionary intents, image viewer | A1 |
| 12 | S_HOME_WIDGET | launcher | widget placed (rows = recent decks) | A1 |
| 13 | S_NOTIFICATIONS | status bar | any AnyMemo notification posted | A1 |
| 14 | S_MAIN_DRAWER | AnyMemo | NavigationView drawer open | A1 |
| 15 | S_DLG_WHATS_NEW | AlertDialog over AnyMemo | saved version ≠ 241 (first run or reset) | A1 |
| 16 | S_DLG_SDCARD | AlertDialog | `!anymemo/.canRead()` (Exit) | A1 |
| 17 | S_DLG_ABOUT | AlertDialog (AboutUtil) | from drawer or Misc | A1 |
| 18 | S_OPTIONS | OptionScreen | global preferences | A1 |
| 19 | S_OPTIONS_PAUSED | OptionScreen | under AlgorithmCustomizationScreen | A1 |
| 20 | S_DLG_PREF@KEY | Preference dialog | ListPreference / EditTextPreference dialog of a key (`speech_ctl`, `copy_to_clipboard`, `button_style`, `dict_app`, `interface_locale`, `notification_interval`, `recent_count`, `learning_queue_size`, `review_ordering`, 17 float keys) | A1 |
| 21 | S_DLG_ALGO_WARNING | AlertDialog | before AlgorithmCustomizationScreen | A1 |
| 22 | S_ALGO | AlgorithmCustomizationScreen | scheduler preferences | A1 |
| 23 | S_DLG_ALGO_RESET | AlertDialog | reset confirm | A1 |
| 24 | S_DLG_ERROR@CTX | AMGUIUtility.displayError | Back finishes the caller (downloader, ShareScreen) | A1 |
| 25 | S_DLG_EXCEPTION@CTX | AMGUIUtility.displayException | Back dismisses (dictionary missing, download / upload / merge / save failed) | A1 |
| 26 | S_DLG_CONFIRM_TASK@CTX | AMGUIUtility.doConfirmProgressTask | WIPE / REMOVE_DUP / SHUFFLE (from PreviewEdit) | A1 |
| 27 | S_MAIN_RECENT | AnyMemo + RecentListFragment | ≥ 1 row, no selection | A2 |
| 28 | S_MAIN_RECENT_EMPTY | AnyMemo + RecentListFragment | 0 rows | A2 |
| 29 | S_MAIN_RECENT_SELECT | AnyMemo + action mode | ≥ 1 row selected, CAB "Delete" | A2 |
| 30 | S_MAIN_OPEN | AnyMemo + OpenTabFragment | file browser with FAB and menu | A2 |
| 31 | S_MAIN_MISC | AnyMemo + MiscTabFragment | sections collapsed | A2 |
| 32 | S_MAIN_MISC_IMPORT | MiscTabFragment | import list visible | A2 |
| 33 | S_MAIN_MISC_EXPORT | MiscTabFragment | export list visible | A2 |
| 34 | S_DLG_OPEN_ACTIONS@RECENT / @OPEN | OpenActionsFragment | 9 actions on one deck | A2 |
| 35 | S_DLG_DELETE_DB | AlertDialog | confirm delete from OpenActions | A2 |
| 36 | S_DLG_RESET_PREFS | AlertDialog | Misc reset confirm | A2 |
| 37 | S_DLG_DONATE | AlertDialog | **unreachable in pro** (button GONE) | A2 |
| 38 | S_DLG_FB_ITEM@CTX | AlertDialog list | long-press file: Delete / Clone / Rename | A2 |
| 39 | S_DLG_FB_DELETE | AlertDialog | confirm | A2 |
| 40 | S_DLG_FB_RENAME | AlertDialog + EditText | rename | A2 |
| 41 | S_DLG_FB_CREATE_DB | AlertDialog + EditText | create DB (FAB or menu) | A2 |
| 42 | S_DLG_FB_CREATE_DIR | AlertDialog + EditText | create folder | A2 |
| 43 | S_DLG_FB_MSG | AlertDialog | clone or rename failed, `openFile` exception | A2 |
| 44 | S_DLG_OVERWRITE_DB@FB / @IMPORT | AlertDialog | imported file name exists | A2 |
| 45 | S_DLG_EXPORT_DB | ExportAnyMemoDbFragment | `.db` chooser dialog | A2 |
| 46 | S_DLG_EXPORT_FMT@FMT | ConverterFragment | FMT ∈ {XML, CARDS, CSV, TAB, QA, ZIP} | A2 |
| 47 | S_DLG_IMPORT_MERGE | AlertDialog | import target `.db` exists (Yes / No / Cancel) | A2 |
| 48 | S_FILE_PICKER@CTX | FileBrowserActivity | CTX ∈ {IMAGE, AUDIO (CardEditor), MERGE_TARGET, MERGE_SOURCE, SHARE_DB} | A2 |
| 49 | S_DLG_FONT_PICKER@Q / @A | FileBrowserFragment dialog | `.ttf` picker from SettingsScreen | A2 |
| 50 | S_MERGE | DatabaseMerger | target / source fields | A2 |
| 51 | S_MERGE_PAUSED | DatabaseMerger | under FileBrowserActivity | A2 |
| 52 | S_SHARE | ShareScreen | SEND text received | A2 |
| 53 | S_SHARE_PAUSED | ShareScreen | under FileBrowserActivity | A2 |
| 54 | S_STUDY_Q | StudyActivity | single-sided, answer hidden (grade buttons INVISIBLE) | A3 |
| 55 | S_STUDY_A | StudyActivity | answer shown (grade buttons VISIBLE) | A3 |
| 56 | S_STUDY_DS_FRONT | StudyActivity | double-sided, front (grade buttons GONE) | A3 |
| 57 | S_STUDY_DS_BACK | StudyActivity | double-sided, back shown | A3 |
| 58 | S_STUDY_PAUSED | StudyActivity | under Editor, Detail, Settings, PreviewEdit or an external app | A3 |
| 59 | S_DLG_STUDY_NO_ITEM | AlertDialog | no card to learn | A3 |
| 60 | S_DLG_UNDO_FAIL | AlertDialog | undo with `prevCard == null` | A3 |
| 61 | S_DLG_STUDY_DELETE | AlertDialog | delete current card | A3 |
| 62 | S_DLG_MARK_FOREVER | AlertDialog | mark learned forever | A3 |
| 63 | S_DLG_GESTURES@STUDY / @PREVIEW | GestureSelectionDialogFragment | gesture list + enable checkbox | A3 |
| 64 | S_DLG_LOOKUP@STUDY / @QUIZ | AlertDialog + ListView | word list (DictionaryUtil) | A3 |
| 65 | S_DLG_QUIZ_LAUNCHER | QuizLauncherDialogFragment | group mode (default) | A3 |
| 66 | S_DLG_QUIZ_LAUNCHER_CATEGORY | same | category radio checked | A3 |
| 67 | S_DLG_QUIZ_LAUNCHER_RANGE | same | range radio checked | A3 |
| 68 | S_QUIZ_Q | QuizActivity | answer hidden | A3 |
| 69 | S_QUIZ_A | QuizActivity | answer shown | A3 |
| 70 | S_QUIZ_PAUSED | QuizActivity | under an external app | A3 |
| 71 | S_DLG_QUIZ_NO_ITEM | AlertDialog | empty quiz | A3 |
| 72 | S_DLG_QUIZ_DONE_NEW | AlertDialog | new cards done (score; Review / Cancel) | A3 |
| 73 | S_DLG_QUIZ_DONE_ALL | AlertDialog | queue empty | A3 |
| 74 | S_PLAYER_STOPPED | CardPlayerActivity + CardPlayerFragment | bound, not playing | A3 |
| 75 | S_PLAYER_PLAYING | same | playing (foreground notification) | A3 |
| 76 | S_PLAYER_PAUSED | same | Home or another window on top | A3 |
| 77 | S_DLG_PLAYER_SETTINGS | CardPlayerSettingDialogFragment | two seek bars | A3 |
| 78 | S_PREVIEW | PreviewEditActivity | current card present | A4 |
| 79 | S_PREVIEW_EMPTY | PreviewEditActivity | no card (empty deck or category) | A4 |
| 80 | S_PREVIEW_SEARCH | PreviewEditActivity | SearchView expanded | A4 |
| 81 | S_PREVIEW_PAUSED | PreviewEditActivity | under Editor, Settings, Detail, List, Player, Merger or browser | A4 |
| 82 | S_DLG_PREVIEW_DELETE | AlertDialog | delete card | A4 |
| 83 | S_DLG_SWAP_ALL | AlertDialog | Swap / Swap dup / Cancel | A4 |
| 84 | S_EDITOR_NEW | CardEditor | `isEditNew` (radio visible) | A4 |
| 85 | S_EDITOR_EDIT | CardEditor | editing an existing card | A4 |
| 86 | S_EDITOR_PAUSED | CardEditor | under FileBrowserActivity or the permission dialog | A4 |
| 87 | S_DLG_EDITOR_UNSAVED | AlertDialog | Back with edits (Yes / No / Cancel) | A4 |
| 88 | S_DLG_AUDIO_OVERRIDE | AlertDialog | field already has `src=` | A4 |
| 89 | S_DLG_RECORDER | AudioRecorderFragment | idle or recorded | A4 |
| 90 | S_DLG_RECORDER_RECORDING | same | recording | A4 |
| 91 | S_DLG_RECORDER_PLAYING | same | playing back | A4 |
| 92 | S_DETAIL | DetailScreen | loaded | A4 |
| 93 | S_DLG_DETAIL_SAVE | AlertDialog | update warning | A4 |
| 94 | S_LIST | CardListActivity | answers visible | A4 |
| 95 | S_LIST_HIDDEN | CardListActivity | answers hidden | A4 |
| 96 | S_LIST_SEARCH | CardListActivity | SearchView expanded | A4 |
| 97 | S_LIST_PAUSED | CardListActivity | under Editor, Detail or PreviewEdit | A4 |
| 98 | S_POPUP_LIST_MARK | PopupMenu | learned / forgotten / new / forever | A4 |
| 99 | S_POPUP_LIST_OPEN | PopupMenu | edit / detail / preview edit | A4 |
| 100 | S_DLG_LIST_SORT | AlertDialog single-choice | sort method | A4 |
| 101 | S_DLG_CATEGORY@CTX | CategoryEditorFragment | loaded; CTX ∈ {STUDY, PREVIEW, EDITOR, QUIZ} | A4 |
| 102 | S_SETTINGS@DECK / @DEFAULT | SettingsScreen | loaded; DEFAULT = `files/empty.db` from Misc | A4 |
| 103 | S_SETTINGS_PAUSED | SettingsScreen | under the browser or Home | A4 |
| 104 | S_DLG_SETTINGS_UNSAVED | AlertDialog | Back with changes | A4 |
| 105 | S_DLG_LOAD_DEFAULT | AlertDialog | load defaults confirm | A4 |
| 106 | S_DLG_COLOR_PICKER | AlertDialog + ColorPickerView | color edit | A4 |
| 107 | S_DLG_CARD_FIELDS@HTML / @F1 / @F2 | AlertDialog multi-choice | fields | A4 |
| 108 | S_STATS | StatisticsScreen | chart shown | A4 |
| 109 | S_STATS_DRAWER | StatisticsScreen | chart drawer open | A4 |
| 110 | S_MAIN_DOWNLOAD | AnyMemo + DownloadTabFragment | 2 sources | A5 |
| 111 | S_DL_ANYMEMO | AnyMemoDownloaderActivity | category list loaded | A5 |
| 112 | S_DL_ANYMEMO_CAT | same | inside a category (`..` + decks) | A5 |
| 113 | S_DLG_DL_CONFIRM@ANYMEMO / @DROPBOX | AlertDialog | download? Yes / No | A5 |
| 114 | S_DLG_DL_DONE | AlertDialog | download success | A5 |
| 115 | S_DROPBOX_AUTH | DropboxOauth2AccountActivity | verifying, or waiting for the callback | A5 |
| 116 | S_DROPBOX_AUTH_PAUSED | same | under the Custom Tab | A5 |
| 117 | S_DROPBOX_LIST | DropboxListActivity | file list | A5 |
| 118 | S_DROPBOX_LIST_PAUSED | same | under UploadDropboxActivity | A5 |
| 119 | S_DROPBOX_UPLOAD | UploadDropboxActivity | file browser | A5 |
| 120 | S_DLG_UPLOAD_CONFIRM | AlertDialog | upload? | A5 |
| 121 | S_DLG_UPLOAD_DONE | AlertDialog | success | A5 |

Pages deliberately not created:
- Transient non-cancelable ProgressDialogs (`MultipleLoaderManager`, AsyncTasks, `doProgressTask`, `RetrieveTask`): model them as ASYNC edges.
- The 4 chart types in StatisticsScreen: they share the same handlers.
- Spinner drop-downs in SettingsScreen: only `colorSpinner` has a selection listener.
- Toasts and the Snackbar.

### 3.4 Shared code that needs `@CONTEXT` variants

- `FileBrowserFragment.*` @OPEN, @EXPORT_DB, @CONVERT, @PICKER, @FONT, @UPLOAD. The file-click continuation differs: OpenActions, CREATE_DOCUMENT, `setResult`, `setText` or upload (`J/ui/FileBrowserFragment.java:412-417`).
- `OpenActionsFragment$1.onClick` @RECENT / @OPEN.
- `CategoryEditorFragment.*` and the result listeners @STUDY / @PREVIEW / @EDITOR / @QUIZ (`J/ui/StudyActivity.java:577-586`, `J/ui/PreviewEditActivity.java:632-637`, `J/ui/CardEditor.java:634-640`, `J/ui/QuizLauncherDialogFragment.java:520-531`).
- `QACardActivity.*` (`startInit`, `displayCard`, `onPostInit`, listeners, `onDestroy`) @STUDY / @QUIZ / @PREVIEW / @PLAYER. The subclasses override different hooks: PreviewEdit keeps the default `onClick*`/`onVolume*`/`onPostDisplayCard`; CardPlayer keeps the default `onGestureDetected` and `onClick*`.
- `GradeButtonsFragment.*` @STUDY / @QUIZ (Quiz uses `grade_buttons_quiz`; `J/ui/GradeButtonsFragment.java:143-145`).
- `GestureSelectionDialogFragment.onDismiss` → `mActivity.restartActivity()` @STUDY / @PREVIEW (`:182-186`).
- `DictionaryUtil.*` @STUDY / @QUIZ. `AMGUIUtility.*` @caller. `DatabaseImportUtil.handleImportDbResult` @RECENT / @MISC.
- `FolderImportExportUtil.importFolder` @WHATS_NEW / @MISC.
- `BaseActivity.onCreate/onResume/onPause/onStop` @each subclass.
- `SettingsScreen.*` @DECK / @DEFAULT.

## 4. Framework mechanisms that need FRAMEWORK, ASYNC or LIFECYCLE edges

| Mechanism | App classes (callbacks that the framework calls) | Notes for edges |
|---|---|---|
| RecyclerView adapters | `RecentListFragment$RecentListAdapter` (+ `ui/helper/SelectableAdapter`), `FileBrowserFragment$FileBrowserAdapter`, `RecentListFragment$DividerItemDecoration` (`onDraw`, `getItemOffsets`) | `onCreateViewHolder`/`onBindViewHolder`/`getItemCount` run on layout and `notify*`. Click listeners are registered in `onBindViewHolder` (REGISTER edges). |
| ListView / ArrayAdapter | `CategoryEditorFragment$CategoryAdapter.getView`, `CardListActivity$CardListAdapter` (`getView`, `SectionIndexer`, `getFilter` → `Filter.performFiltering` on a worker thread / `publishResults`, `iterator`), `AbstractDownloaderFragment$DownloadListAdapter.getView`, `GestureSelectionDialogFragment$GesturesAdapter.getView`, `DictionaryUtil` (plain ArrayAdapter), `AMSpinner` | `CardListAdapter.getSectionForPosition/getPositionForSection/getSections` are called by the fast scroller (`setFastScrollEnabled(true)`, `J/ui/CardListActivity.java:647`; FW-MEMORY). |
| ViewPager + FragmentStatePagerAdapter | `TwoFieldsCardFragment$1/$2` (`getItem`/`getCount`), `FlipableCardFragment$1` | The pager calls `getItem` → `CardFragment.Builder.build` → `CardFragment` lifecycle (child fragments). |
| Fragments and DialogFragments | every `ui/*Fragment`. `FileBrowserFragment` is embedded (tab, picker, upload) or shown as a dialog (`show()`). | An embedded DialogFragment behaves as a plain fragment when it has a container (FW-MEMORY). `setHasOptionsMenu(true)` in FileBrowser, Recent and CardPlayer adds `onCreateOptionsMenu` / `onOptionsItemSelected` FRAMEWORK edges. `CardFragment.onCreateAnimation` is called on transactions with animations. |
| Loader framework (androidx.loader) | `MultipleLoaderManager` (orchestrates `initLoader`/`restartLoader` + `checkAllLoadersCompleted` → `Handler.post(onAllLoaderCompletedRunnable)`), `DBLoader` subclasses `SettingLoader`, `CardTTSUtilLoader`, `CardWrapperListLoader`, `StudyActivity$LearnQueueManagerLoader`, `QuizActivity$QuizQueueManagerLoader`; the `*LoaderCallbacks` in QACard, Study, Quiz, CardList, Settings; `RecentListFragment` (2 anonymous AsyncTaskLoaders); `AnyMemo$FileAsyncTaskLoader` | ASYNC: `onCreateLoader` → `loadInBackground` (worker) → `onLoadFinished` (main). **`onLoaderReset` of the activity loaders was never hit in 1 h of either tool**, although FW-MEMORY expects it on destroy. Only the fragment loaders in `RecentListFragment` hit it. UNVERIFIED; treat as FRAMEWORK_ONLY candidates. |
| AsyncTask | CardEditor `InitTask`/`SaveCardTask`; DetailScreen `InitTask`/`SaveCardTask`; CategoryEditor `Init`/`Edit`/`New`/`DeleteCategoryTask` (`onCancelled` via `cancel(true)` in `onPreExecute`); `GradeButtonsFragment$GradeTask`; PreviewEdit `DeleteCardTask`/`SearchCardTask`; `QuizActivity$ChangeCardTask`; `QuizLauncherDialogFragment$InitTask`; SettingsScreen `SaveButtonTask`/`LoadDefaultTask`; `StatisticsScreen$ChartTask` + 4 subclasses; `AbstractDownloaderFragment` `Retrieve`/`LoadMore`/`FetchDatabaseTask` | ASYNC: `onPreExecute` → `doInBackground` → `onPostExecute` / `onCancelled`. |
| RxJava 2 | `DatabaseOperationDialogUtil` (5 `Maybe.create` wrapping dialogs; `subscribe` runs at subscription), FileBrowserFragment Consumers, ExportAnyMemoDb, `DatabaseImportUtil`, `FolderImportExportUtil` (`fromCallable` on `Schedulers.io()` → main), `Oauth2AccountActivity` (Single / Completable observers), `DropboxApiHelper` (`Single.create` / `Completable.create` / `Observable.create` / `fromCallable`, with OkHttp `Callback.onFailure/onResponse` on OkHttp threads), `UploadDropboxActivity` (`Action` / `Consumer`), `DropboxListFragment.initialRetrieve` (`blockingForEach` → `$1.accept`) | ASYNC edges with the scheduler noted. Dialog-backed Maybes complete from dialog button callbacks. |
| Handler / Thread / Executor | `BaseActivity` (`postDelayed` immersive restore, `$1$1.run`), `GradeButtonsFragment.setVisibility` (`$6.run`), `MultipleLoaderManager`, `AMGUIUtility.doProgressTask` (`new Thread` `$4` + `handler.post` `$4$1`/`$4$2`/`$4$3`), `CardPlayerState` (`postDelayed` between Q/A), `SpeakWord` (`new Thread` `$3`), `LearnQueueManager` (`AnyMemoExecutor.submit` single-thread executor → `$1.run`, `$1$1.call`), ORMLite `callBatchTasks(Callable)` in CardDao, Category, LearningData and DatabaseUtil | ASYNC. |
| LocalBroadcastManager | `RecentListActionModeUtil` (start / update / stop receivers `$1`/`$2`/`$3`), `RecentListFragment` (`$1` remove-selected, `$2` deselect-all) | ASYNC: delivery is posted to the main looper (FW-MEMORY). |
| Context broadcast | `CardPlayerFragment.serviceEventListener` (registered in `onResume` with `RECEIVER_NOT_EXPORTED`; sender `CardPlayerService` with `setPackage`) | ASYNC from service to UI. |
| Action mode / PopupMenu / SearchView / Drawer / BottomNav | `RecentListActionModeUtil$ActionModeCallback` (create / prepare / clicked / destroy); `CardListActivity` PopupMenus (`$1`/`$2` `onMenuItemClick`); SearchView `OnQueryTextListener` in PreviewEdit (`$12`) and CardList (`$9`); NavigationView in AnyMemo (`$1`) and Statistics (`$1`); BottomNavigationView (`AnyMemo$2`) | Menu creation is deferred; `invalidateOptionsMenu` is not used anywhere (grep), FW-MEMORY. |
| Data binding | `MainTabsBinding(Impl)`, `DropboxListActivityBinding(Impl)`, `UploadDropboxScreenBinding(Impl)`, `DataBinderMapperImpl` | `DataBindingUtil.setContentView` → `DataBinderMapperImpl.getDataBinder` → `*BindingImpl.<init>`/`invalidateAll`/`executeBindings` (FRAMEWORK). The static `inflate`/`bind` helpers are never called (§5). |
| Dagger 2 | `DaggerAppComponents` + inner `*Impl` / `*Builder` | CALL edges: `AMApplication.onCreate` → `Builder.build`; `BaseActivity.activityComponents()` → `ActivityComponentsBuilder`; `inject*` sets the `@Inject` fields and calls the `AppModules.provides*` / `ActivityModules.provides*` methods, which are **called from the JaCoCo-invisible `*_Factory` classes**. Model `provides*` as reachable from the `inject` method of the consumer. |
| ORMLite | `AnyMemoDBOpenHelper` (`onCreate` / `onUpgrade` / `onDowngrade` from `SQLiteOpenHelper`); DAO impls created reflectively through `daoClass=` in `@DatabaseTable` (`J/entity/Card.java:12` etc.) using the `(ConnectionSource, Class)` constructor; `TableUtils.createTable` instantiates the DAOs of all 6 tables in `onCreate` | FRAMEWORK. The `(ConnectionSource, DatabaseTableConfig)` constructors were never hit (no table config is passed to the helper, `J/common/AnyMemoDBOpenHelper.java:254-256`). |
| XML / CSV parsers | SAX `DefaultHandler` callbacks in `MnemosyneXMLImporter`, `SupermemoXMLImporter`, `Supermemo2008XMLImporter` (`startDocument`/`startElement`/`characters`/`endElement`/`endDocument`/`setDocumentLocator`); XmlPullParser in `Mnemosyne2CardsImporter`; OpenCSV in `CSVImporter`/`CSVExporter` | FRAMEWORK edges from `XMLReader.parse` (all run inside `ConvertIntentService`). |
| MPAndroidChart | `StatisticsScreen$Chart(YAxis)ValueFormatter.getFormattedValue` | FRAMEWORK, called during chart drawing. |
| TTS / media / gestures / clipboard | `AnyMemoTTSImpl` (`TextToSpeech.OnInitListener.onInit`, `$2.onUtteranceCompleted`), `SpeakWord` (`MediaPlayer.OnCompletionListener` `$2`), `AudioRecorderFragment` (`MediaRecorder`, `MediaPlayer` `$2.onCompletion`), `QACardActivity$8.onGesturePerformed` (`GestureLibraries.fromRawResource(R.raw.gestures)`), `QACardActivity.copyToClipboard` | FRAMEWORK / ASYNC. TTS init is asynchronous (`J/tts/AnyMemoTTSImpl.java:56-90,92-107`). |
| Html | `CardTextUtil` (`Html.fromHtml` with `CardImageGetter.getDrawable` as `ImageGetter` and `CardTextUtil$1.handleTag` as `TagHandler`) | FRAMEWORK: `getDrawable` only for `<img>`, `handleTag` for unknown tags. |
| Services | `CardPlayerService` (bound: `onCreate` → `onBind` → `LocalBinder.getService`; `onUnbind` returns false; `startForeground` in `showNotification`, `J/service/CardPlayerService.java:88-131,198-224`); `ConvertIntentService` (IntentService: `onCreate` → `onHandleIntent` on a worker thread); `UpdateWidgetService.onGetViewFactory` | LIFECYCLE / ASYNC. |
| Receivers / AlarmManager | `SetAlarmReceiver` (BOOT_COMPLETED; static `setNotificationAlarm` uses `setInexactRepeating` RTC at 07:02:03 + interval, `J/receiver/SetAlarmReceiver.java:45-93`); `AlarmReceiver` (`:remote`, PendingIntent extra `request_code`); `AnyMemoWidgetProvider` (`onUpdate`/`onEnabled`/`onDisabled` from AppWidgetManager) | SYSTEM edges with time, boot or launcher guards. |
| Content providers | `CardProvider`, `DatabasesProvider` (`onCreate` at process start; `query`/`getType`/`insert`/`update`/`delete` only from external clients); androidx `FileProvider` (used by `ShareUtil.shareDb` and the image viewer) | ENTRY from `S_ENTRY` (adb / other apps). |
| Storage Access Framework | `ACTION_OPEN_DOCUMENT` (Recent FAB, Misc import DB, Misc converters, FileBrowser "Import DB"), `ACTION_OPEN_DOCUMENT_TREE` (What's-new link, Misc folder import/export), `ACTION_CREATE_DOCUMENT` (ExportAnyMemoDb, Converter), `DocumentFile` in `FolderImportExportUtil` | INTENT to `S_EXT_SAF_*`, then RESULT back to `onActivityResult`. Add `env` "needs DocumentsUI interaction". |
| Notifications | `NotificationChannelUtil` (3 channels), `NotificationUtil` (review), `ConvertIntentService` (progress / success / failure; `TaskStackBuilder`), `CardPlayerService` (foreground) | PendingIntent → INTENT edges from `S_NOTIFICATIONS`. |
| Widget | `AnyMemoWidgetProvider`, `UpdateWidgetService`, `WidgetRemoteViewsFactory` (`onCreate`/`onDataSetChanged`/`getCount`/`getViewAt`/`getLoadingView`/`getViewTypeCount`/`getItemId`/`hasStableIds`/`onDestroy` from the launcher host) | FRAMEWORK, from `S_HOME_WIDGET`. `updateWidget` → `notifyAppWidgetViewDataChanged` → `onDataSetChanged` only if a widget exists. |
| Custom Tabs / OkHttp / WebView | `Oauth2AccountActivity.requestAuth` (Custom Tabs, `FLAG_ACTIVITY_NO_HISTORY`); OkHttp in `DownloaderUtils` (sync) and `DropboxApiHelper` (sync and async); WebView only in the DEAD `OauthAccessCodeRetrievalFragment` (`J/downloader/oauth/OauthAccessCodeRetrievalFragment.java:93,166-180`) | No JS bridges anywhere (grep `addJavascriptInterface`: none). |
| Preferences | `OptionScreen`, `AlgorithmCustomizationScreen` (PreferenceActivity); `Float`/`IntegerEditTextPreference.getPersistedString`/`persistString` (called by EditTextPreference when the dialog opens or is saved) | FRAMEWORK. There is no `OnSharedPreferenceChangeListener` anywhere: preferences are read on demand through `Option`/`SchedulingAlgorithmParameters`. |
| Runtime permissions | `AnyMemo.onRequestPermissionsResult`, `CardEditor.onRequestPermissionsResult` | RESULT from `S_PERMISSION@*`. |

There is no WorkManager, JobScheduler, LiveData or ViewModel in app code (grep).

## 5. Unreachable-code candidates (evidence only; final verdicts are for the graph builders)

### 5.1 How the candidates were found

1. **Bytecode reference scan.** I ran a read-only Python parser over all 633 class files. It decodes every `invokevirtual`/`invokespecial`/`invokestatic`/`invokeinterface` and matches each call site to its targets: an exact owner for constructors and private methods; owner, supertypes or subtypes (CHA) for virtual and interface calls. JacocoInstrument is excluded, and the androidTest sources are not compiled into this dir. Of the 2192 JaCoCo methods, 507 have no call site; 171 of those ran in a baseline (framework callbacks such as `onCreate`, plus `Card.equals`/`hashCode` called by JDK collections). The other 336 were reviewed by hand.
2. **Roots outside bytecode:**
   - manifest components (§1);
   - classes named in layouts and XML: `AMSpinner` and `DoubleClickButton` with the `(Context, AttributeSet)` constructor; `AnyMemoDownloaderFragment` via `<fragment>` (`R/layout/anymemo_downloader.xml:2-6`); `Float`/`IntegerEditTextPreference` (`R/xml/*.xml`);
   - reflection: ORMLite creates DAOs via `@DatabaseTable(daoClass=…)` with the `(ConnectionSource, Class)` constructor and sets entity fields by reflection. No entity uses `useGetSet` (grep), so entity getters and setters are only app-called. `AMEnv` loads `AMSecrets` with `Class.forName` and reads only static fields (`J/common/AMEnv.java:72-93`);
   - Dagger factories (JaCoCo-invisible but in the class dir, so they are included in the scan).
3. **Data-flow and guard checks** for methods that do have call sites but whose callers can never pass the needed value (listed with reasons below).
4. **Resource and manifest search** for the dead classes: no layout, menu, xml or manifest entry names `EditTabFragment`, `ErrorUtil`, `OauthAccountActivity`, `OauthAccessCodeRetrievalFragment`, `Deck`, `Filter` or `Stat`. The only stale reference is `meta-data roboguice.modules = …AMModules` (`MAN:22`), a class that does not exist.

Result: **227 DEAD candidates and 47 FRAMEWORK_ONLY candidates** (JaCoCo universe). **None of them was hit by Monkey or APE**, so the baseline contradicts no candidate.

### 5.2 DEAD candidates (227 methods)

| Group | Methods | Evidence |
|---|---|---|
| OAuth1 framework: `downloader/oauth/OauthAccountActivity` (+`$1`, `$2`, `$GetAccessTokenTask`, `$ValidateAccessTokenAndRunCallbackTask`) and `OauthAccessCodeRetrievalFragment` (+`$RequestTokenTask`, `$RequestTokenTask$1`, `$2`; contains the only WebView) | 19 + 15 | Both are abstract with no subclass in the class dir (`J/downloader/oauth/OauthAccountActivity.java:41`, `OauthAccessCodeRetrievalFragment.java:43`). Their Quizlet/Google subclasses were removed; the manifest still lists them as phantom activities. |
| `ui/EditTabFragment` (+`$1`) | 5 | Never instantiated, not in any layout (`J/ui/EditTabFragment.java:29`). Its `setRecentListUtil` `@Inject` method is called only by `EditTabFragment_MembersInjector`, which no component uses (FragmentComponents has no `inject(EditTabFragment)`, `J/modules/FragmentComponents.java`). |
| `utils/ErrorUtil` (+`$1`–`$3`) | 10 | No `@Inject ErrorUtil` field or parameter anywhere. The only reference is an unused import (`J/modules/ActivityModules.java:10`). `ErrorUtil_Factory` is generated but never called. |
| `entity/Deck`, `entity/Filter`, `entity/Stat`, `dao/StatDaoImpl` | 11 + 11 + 1 + 2 | The tables are created (`J/common/AnyMemoDBOpenHelper.java:55,57`), which instantiates `DeckDaoImpl`/`FilterDaoImpl` (reached, hit by APE), but no row is ever queried or created, so the entity constructors and accessors never run. `getDeckDao`/`getFilterDao` have no callers (`:183-213`). `Stat` has no table and no `getDao`. |
| Trivial generated or utility constructors: `BR.<init>` ×2, `BuildConfig.<init>`, `DataBindingTriggerClass.<init>`, `AMEnv`/`AMPrefKeys`/`AMSecrets`/`AnyMemoDBOpenHelperManager`/`AMStringUtils`/`AMZipUtils`/`AnyMemoExecutor` `.<init>`, `AppModules.<init>` (all `@Provides` are static), `ActivityModules.<init>` (abstract) | 13 | No `new` anywhere. |
| `BuildConfig.<clinit>` | 1 | `DEBUG = Boolean.parseBoolean("true")` (constant pool of `BuildConfig.class`). The only read is inside `catch (NameNotFoundException)` for the app's own package (`J/ui/AnyMemo.java:295-299`); `FLAVOR`/`APPLICATION_ID` are inlined constants. Infeasible guard (FW-MEMORY: own package always found). |
| Data-binding static helpers `MainTabsBinding`, `DropboxListActivityBinding`, `UploadDropboxScreenBinding` `.inflate` ×4 / `.bind` ×2 each | 18 | The app only uses `DataBindingUtil.setContentView` (`J/ui/AnyMemo.java:121`, Dropbox activities). Generated API with no caller. |
| Dagger leftovers: `DaggerAppComponents$ActivityComponentsImpl.inject(CardEditor)`, `$AppComponentsImpl.inject(StudyActivity$LearnQueueManagerLoader)`, `.inject(QuizActivity$QuizQueueManagerLoader)`, `AppModules.provideExecutorService`, `AppModules_ProvideExecutorServiceFactory$InstanceHolder.<clinit>` | 5 | `CardEditor` and the two loaders never call `inject` (`J/ui/CardEditor.java:102-107`). No consumer of `ExecutorService` (grep). |
| Unused base or helper methods: `BaseActivity.appComponents`/`isActivityCreated`, `BaseFragment.appComponents`, `BaseDialogFragment.appComponents`, `AnyMemoDBOpenHelper.getDeckDao`/`getFilterDao`, `FilterDaoImpl.getActiveFilter`, `CardDaoImpl.getRandomReviewedCards`/`searchPrevCard` (androidTest only), `CategoryDaoImpl.populateCategory` + `$1` (3 in total), `AMGUIUtility.getDialogFinishListener` + `$6` (3 in total), `AMStringUtils.isInteger`, `AMUiUtil.convertPxToDp`, `AnyMemoExecutor.waitTask`, `NotificationUtil$DatabaseInfo.getNewCount`, `RecentListUtil.getRecentDBPath` (androidTest only), `CardFragment$Builder.setCardOnLongClickListener`, `CardImageGetter.scaleBitmap` (androidTest only), `FlipableCardFragment.flipTo`, `GradeButtonsFragment.setButtonText` (`@SuppressWarnings("unused")`, `J/ui/GradeButtonsFragment.java:219-227`), `RecentListFragment$RecentListAdapter.getList`, `AMSpinner.getItemValueForPosition`, `CardPlayerSettingDialogFragment.newInstance`, `CardPlayerService$LocalBinder.getCurrentPlayingCard`, `SetAlarmReceiver.setWidgetUpdateAlarm`/`cancelWidgetUpdateAlarm`, `AbstractDownloaderFragment.getDownloadItemCount`, `$DownloadListAdapter.getList`, `DownloadItem.setExtras`/`getExtras`/`clone` (only its own bridge calls it), `DownloaderUtils.validateEmail`/`validateDBName`, `DropboxApiHelper.createFolder` + `$2` + `$2$1` (6 in total) | 43 | Zero call sites in the bytecode scan; grep of the main sources agrees. |
| Entity accessors never called (ORMLite uses fields): `Card.getCardType`/`setCardType`/`getCreationDate`/`getUpdateDate`; `Category.setId`/`getCreationDate`/`getUpdateDate`; `LearningData.getUpdateDate`/`setUpdateDate` (LearningData does **not** implement `VersionableDomainObject`, `J/entity/LearningData.java:13`, so `AbstractHelperDaoImpl.create/update` never call them, `J/dao/AbstractHelperDaoImpl.java:104-125`); `Setting.getId`/`setId`/`getName`/`setName`/`getDescription`/`setDescription`/`getDisplayInHTML`/`setDisplayInHTML`/`getQuestionField`/`setQuestionField`/`getAnswerField`/`setAnswerField`/`setAnswerFieldEnum` (SettingsScreen calls `setAnswerEnum` instead)/`getCreationDate`/`getUpdateDate`; `Option.getEnableArabicEngine`/`setEnableArabicEngine`/`setButtonStyle`/`setVolumeKeyShortcut`/`setCopyClipboard`; `Option$CopyToClipboard.parse` (`getCopyClipboard` uses `valueOf`) | 30 | Zero call sites. |
| Converter metadata: `getSrcExtension` in all 13 classes that define it; `getDestExtension` in the 7 importers | 20 | `getSrcExtension` is called only from androidTest. `getDestExtension` is called only from `ConverterFragment.startConversion` (`J/ui/ConverterFragment.java:89,93`), and `ConverterFragment` is only created with the six **exporter** classes (`J/ui/MiscTabFragment.java:290-337`). |
| `ConverterFragment$2`, `$3` (merge Yes/No dialog) | 4 | Only in the `getDestExtension().equals("db")` branch (`J/ui/ConverterFragment.java:93-126`). No exporter has destination `db`. |
| `MiscTabFragment$2` (donate → "Buy pro") | 2 | The donate button is GONE in the pro flavor (`J/ui/MiscTabFragment.java:212-215`; `BuildConfig.FLAVOR="pro"`). Flavor-gated. |
| `CardPlayerActivity.showNoItemDialog` + `$1`, `$2` | 5 | `onPostInit` calls `bindCardPlayerService()` **before** the null check (`J/ui/CardPlayerActivity.java:111-114`), and `bindCardPlayerService` dereferences `getCurrentCard().getId()` (`:213`). An empty deck crashes with an NPE first. Infeasible guard; hazard in §5.5. |
| `AbstractDownloaderFragment$3.onClick` (load-more footer), `$LoadMoreTask` (4), `AnyMemoDownloaderFragment.loadMore`, `DropboxListFragment.loadMore` | 7 | The footer is added only `if (hasMore())` (`J/downloader/common/AbstractDownloaderFragment.java:231-232,270-271`), and both subclasses return `false` (`J/downloader/anymemo/AnyMemoDownloaderFragment.java:55`, `J/downloader/dropbox/DropboxListFragment.java:92`). |
| `DropboxListFragment.openCategory`/`goBack` | 2 | Dropbox items are built with `new DownloadItem()` and type `null` (`J/downloader/dropbox/DropboxApiHelper.java:266-283`), so the adapter click always takes the `showFetchDatabaseDialog` branch (`J/downloader/common/AbstractDownloaderFragment.java:409-434`). |
| `QuizQueueManager.release` | 1 | The only `release()` calls are on StudyActivity's queue (`J/ui/StudyActivity.java:250,555`), which is always a `LearnQueueManager`. QuizActivity never releases its queue. |
| `QACardActivity.getContentView` | 1 | Abstract class; all four concrete subclasses override it (Study `:133`, PreviewEdit `:135`, Quiz `:87`, CardPlayer `:84`). |
| `CardEditor.restartActivity` | 1 | `restartActivity()` is invoked on `mActivity` only from OpenActions (host AnyMemo) and GestureSelection (hosts Study/PreviewEdit); CardEditor never calls it itself. |

Branch-level dead code inside reachable methods (no method verdict, but useful for guards):
- `StudyActivity.onActivityResult` `case ACTIVITY_FILTER` (no `startActivityForResult` uses it, `J/ui/StudyActivity.java:213`).
- On API 27, the `SDK_INT > Q` branches in `AnyMemo.onCreate/onResume` (`:124-145,148-152`) and the `SDK_INT >= Q` branch in `CardPlayerService.showNotification` (`:215-216`).
- In `RecentListFragment.loadRecentItemsWithDetails`, the catch is only for broken DBs.

### 5.3 FRAMEWORK_ONLY candidates (47 methods)

| Methods | Reason |
|---|---|
| `StudyActivity.onCreateContextMenu` | No `registerForContextMenu` / `openContextMenu` anywhere (grep), so `memoscreen_context_menu` is never shown. |
| `RecentListFragment.setUserVisibleHint` → `RecentListAdapter.stopActionMode` → `RecentListActionModeUtil.stopActionMode` → `RecentListActionModeUtil$3.onReceive` (4) | `setUserVisibleHint` is only called by pager adapters; the fragment is added with `replace()` (`J/ui/AnyMemo.java:253-257`). FW-MEMORY. The rest of the chain has no other caller (`J/ui/RecentListFragment.java:159-166,470-472`). |
| `onConfigurationChanged` in `BaseActivity`, `CardEditor`, `SettingsScreen`, `OptionScreen`, `AlgorithmCustomizationScreen` (5) | SettingsScreen and OptionScreen declare no `configChanges`. The others declare `orientation\|keyboardHidden` but not `screenSize`/`keyboard`, so a rotation or keyboard attach recreates the activity at targetSdk 36 (FW-MEMORY). Only a keyboardHidden-only change would deliver it (env). |
| `CardPlayerService.onStartCommand`, `onRebind` (2) | The service is only bound (`J/ui/CardPlayerActivity.java:214`, no `startService` for it, grep). `onUnbind` returns `false` (`J/service/CardPlayerService.java:124-131`), so `onRebind` is never called (FW-MEMORY). |
| ORMLite `(ConnectionSource, DatabaseTableConfig)` constructors of `AbstractHelperDaoImpl`, `CardDaoImpl`, `CategoryDaoImpl`, `DeckDaoImpl`, `FilterDaoImpl`, `LearningDataDaoImpl`, `SettingDaoImpl` (7) | DaoManager uses the `(ConnectionSource, Class)` constructor when no table config is registered; the helper passes no config file (`J/common/AnyMemoDBOpenHelper.java:254-257`). FW-MEMORY; consistent with DYN (only the Class constructors ran). |
| Data binding: `setVariable`/`onFieldChange` of the 3 `*BindingImpl` (6); `DataBinderMapperImpl.getDataBinder(…, View[], int)`, `getLayoutId`, `convertBrIdToString`, `$InnerBrLookup.<clinit>`, `$InnerLayoutIdLookup.<clinit>` (5) | The layouts declare no `<variable>` and no observables; the merge/tag lookups are only used by `DataBindingUtil.inflate`/`bind` paths that the app never takes (FW-MEMORY). |
| `onLoaderReset` of the activity-scoped loader callbacks: `QACardActivity$SettingLoaderCallbacks`, `$CardTTSUtilLoaderCallbacks`, `StudyActivity$LearnQueueManagerLoaderCallbacks`, `QuizActivity$QuizQueueManagerLoaderCallbacks`, `SettingsScreen$SettingLoaderCallbacks`, `CardListActivity$CardWrapperLoaderCallbacks`, `AnyMemo$HandleOpenIntentLoaderCallbacks` (7) | Never ran in 2 h of baseline although these activities were destroyed many times (DYN), while the fragment-scoped `RecentListFragment` callbacks did run. Likely androidx.loader removes the lifecycle-bound observer before clearing the ViewModelStore, and `restartLoader` uses `destroy(false)` (FW-MEMORY). **UNVERIFIED**; check `androidx.loader` 1.x source. |
| `DoubleClickButton.<init>(Context)` / `(Context, AttributeSet, int)`; `Float`/`IntegerEditTextPreference.<init>(Context)` / `(Context, AttributeSet, int)` (6) | Inflation uses the 2-argument constructor (FW-MEMORY); no app `new`. |
| `GradeButtonsFragment$1.onClick` | The same view has an `OnTouchListener` that returns `true` (`J/ui/GradeButtonsFragment.java:150-162`), which consumes the touch before click handling (FW-MEMORY). Only an accessibility `performClick` could reach it. |
| `SettingsScreen$8.onNothingSelected` | The AMSpinner adapters are never emptied (FW-MEMORY). |
| `CategoryEditorFragment$NewCategoryTask.onCancelled`; `$DeleteCategoryTask.onCancelled` (2) | New never calls `cancel()`. Delete cancels only when `getCheckedItemPosition()` is INVALID (`J/ui/CategoryEditorFragment.java:286-291`), but the listeners are attached only after an item has been checked in single-choice mode (`:165-170`). **UNVERIFIED**. |

Guarded or environment-only but **reachable**; these are not candidates:
- `AnyMemoDBOpenHelper.onDowngrade` (needs a DB with user_version > 5) and `convertOldDatabase` (needs a pre-9 DB with `dict_tbl`).
- `AnyMemo$3` (storage unreadable).
- `AnyMemo.onRequestPermissionsResult` and `CardEditor.onRequestPermissionsResult` (permission not pre-granted).
- the VIEW, SEND, provider, widget, boot and alarm entries.
- `NullAnyMemoTTS` (deck audio "disabled").
- `SpeakWord$2`/`$3` and `AnyMemoTTSImpl$1` (user audio files).
- `CardImageGetter` remote images (`new URL(source)`, network).
- the volume-key and gesture handlers (options).
- all SAF result paths.

### 5.4 Gates by API level, hardware, network, accounts and build config

- **API level (emulator API 27):** only branches are affected (see 5.2), no whole method. The storage permission flow exists only on API ≤ 29.
- **Hardware/system:**
  - microphone (`AudioRecorderFragment`, RECORD_AUDIO);
  - a TTS engine (`AnyMemoTTSImpl`);
  - hardware volume keys with `enable_volume_key` (APE did reach `StudyActivity.onVolumeDownKeyPressed`, so it toggled the option);
  - gesture input on `GestureOverlayView` (APE hit `QACardActivity$8.onGesturePerformed`);
  - clipboard;
  - launcher widget host;
  - AlarmManager time;
  - boot.
- **Network:** the anymemo.org downloader; the Dropbox REST API; remote `<img>` URLs in cards; browser links.
- **Accounts/keys:** Dropbox needs `AMSecrets.DROPBOX_CONSUMER_KEY`, which is empty in this build, plus an account. Workaround via the deep link in §2.4.
- **Build config/flavor:** pro hides donate. `BuildConfig.DEBUG` is only in the catch. No flavor-specific Java exists (`src/{free,pro,dev}` contain only `strings.xml`). No debug-only features.
- **Test helpers in main code:** `QACardActivity.getCardTTSUtil()` is commented "for testing only" (`J/ui/QACardActivity.java:121-126`) but is also used by Study, Quiz, PreviewEdit and CardPlayer, so it is reachable. Unused resources: `R/xml/remote_config_defaults.xml` (Firebase endpoint, no code), and the 8 menus and 14 layouts listed in §3.1.

### 5.5 Crash hazards relevant to edges (from reading the code, not reproduced)

| Hazard | Where | Effect |
|---|---|---|
| Card player on an empty deck (or a start id that does not exist) | `CardPlayerActivity.onPostInit` → `bindCardPlayerService` (`J/ui/CardPlayerActivity.java:111,213`) | NPE → S_EXIT. OpenActions "Card player" on an empty deck triggers it. |
| Dropbox logout | `DropboxListActivity` has `@Inject Oauth2TokenUtil` but is never injected (no `inject(DropboxListActivity)` in ActivityComponents; `J/downloader/dropbox/DropboxListActivity.java:25,36-39,74-77`) | NPE on the logout menu item. |
| PreviewEdit on an empty deck: Delete, Swap current, Reset current, Share | `J/ui/PreviewEditActivity.java:274-276,334-340,417-419`; `Preconditions.checkNotNull` at `:510-511`; `ShareUtil.shareCard` `J/utils/ShareUtil.java:41` | NPE → S_EXIT from `S_PREVIEW_EMPTY`. |
| Card player buttons before the service connects | `CardPlayerFragment$1.onClick` → `activity.getCardPlayerService().skipToPrev()` (`J/ui/CardPlayerFragment.java:151-193`) | NPE race (INFERRED). |
| Quiz launcher "range" with an emptied field | `Integer.parseInt(…getText())` (`J/ui/QuizLauncherDialogFragment.java:242-243`); sanitized only on focus loss | NumberFormatException (INFERRED). |
| ShareScreen started without an action | `intent.getAction().equals(…)` (`J/ui/ShareScreen.java:84`) | NPE (only via an explicit adb or app intent). |

## 6. Decomposition into 6 areas for parallel modeling

### 6.1 Assignment rules (apply in order; the first match wins; every class in the class dir is covered)

1. `JacocoInstrument/*` → **excluded** (3 classes, 10 methods).
2. Dagger-generated classes (`*_Factory`, `*_MembersInjector`, `*Module_Provides*Factory` and their `$InstanceHolder`, `modules/DaggerAppComponents` and all its inner classes) → **A1**, whatever class they serve (99 classes).
3. `downloader/**`, `databinding/DropboxListActivityBinding*`, `databinding/UploadDropboxScreenBinding*`, `ui/DownloadTabFragment` → **A5**.
4. `dao/**`, `entity/**`, `common/AnyMemoDBOpenHelper`, `common/AnyMemoDBOpenHelperManager`, `ui/loader/{MultipleLoaderManager,DBLoader,SettingLoader}` → **A6**.
5. `ui/{QACardActivity, StudyActivity, QuizActivity, QuizLauncherDialogFragment, CardPlayerActivity, CardPlayerFragment, CardPlayerSettingDialogFragment, CardFragment, TwoFieldsCardFragment, FlipableCardFragment, GradeButtonsFragment, GestureSelectionDialogFragment, GestureName, CardImageGetter}`, `ui/loader/CardTTSUtilLoader`, `queue/**`, `scheduler/**`, `tts/**`, `service/CardPlayerService`, `service/cardplayer/**`, `utils/{CardTTSUtil, CardTextUtil, DictionaryUtil, AMDateUtil, AnyMemoExecutor}` → **A3**.
6. `ui/{PreviewEditActivity, CardEditor, AudioRecorderFragment, DetailScreen, CardListActivity, CategoryEditorFragment, SettingsScreen, StatisticsScreen}`, `ui/loader/CardWrapperListLoader`, `ui/widgets/{AMSpinner, DoubleClickButton}` → **A4**.
7. `ui/{RecentListFragment, OpenTabFragment, EditTabFragment, MiscTabFragment, OpenActionsFragment, FileBrowserFragment, FileBrowserActivity, ExportAnyMemoDbFragment, ConverterFragment, DatabaseMerger, ShareScreen}`, `ui/helper/**`, `converter/**`, `service/ConvertIntentService`, `utils/{RecentListUtil, RecentListActionModeUtil, DatabaseOperationDialogUtil, DatabaseImportUtil, FolderImportExportUtil, AMFileUtil, AMZipUtils, DatabaseUtil, ShareUtil}` → **A2**.
8. Everything else → **A1**.

Inner and anonymous classes (`X$…`) go with `X`, including the 8 JaCoCo-invisible switch-map classes. Result: A1 182 classes, A2 123, A3 124, A4 94, A5 55, A6 52, excluded 3; total 633, no leftovers.

### 6.2 Areas

| Area | Owns (top-level classes) | JaCoCo methods | Pages (§3.3 rows) | Entry edges from other areas (exact node names) |
|---|---|---|---|---|
| **A1 Shell, platform and shared infrastructure** | `ui/AnyMemo` (activity, drawer, bottom nav, What's-new, VIEW loader), `ui/OptionScreen`, `ui/AlgorithmCustomizationScreen`, `ui/widgets/{Float,Integer}EditTextPreference`; `common/{AMApplication, AMEnv, AMPrefKeys, AMSecrets, BaseActivity, BaseFragment, BaseDialogFragment, BaseService, BaseIntentService}`; `modules/*` + all Dagger-generated classes; data binding infra (`BR` ×2, `DataBinderMapperImpl` ×2, `DataBindingComponent`, `DataBindingTriggerClass`, `databinding/MainTabsBinding*`), `BuildConfig`; `provider/*`, `receiver/*`, `widget/*`; `utils/{AMGUIUtility, AMPrefUtil, AMStringUtils, AMUiUtil, AboutUtil, ErrorUtil, NotificationChannelUtil, NotificationUtil}` (49 top-level + 99 generated) | 372 | 1–26: S_ENTRY, S_EXIT, S_MAIN_PAUSED, S_PERMISSION@*, S_EXT_*, S_HOME_WIDGET, S_NOTIFICATIONS, S_MAIN_DRAWER, What's-new, SD card and About dialogs, S_OPTIONS(+_PAUSED), S_DLG_PREF*, S_ALGO + dialogs, S_DLG_ERROR/EXCEPTION/CONFIRM_TASK@* | From every activity: `BaseActivity.onCreate/onResume/onPause/onStop@<Activity>`, `BaseActivity.activityComponents@<Activity>` → `DaggerAppComponents$ActivityComponentsImpl.inject(<Activity>)`. From fragments: `BaseFragment/BaseDialogFragment.fragmentComponents@<Fragment>` → `…FragmentComponentsImpl.inject(<Fragment>)`. From the services and AlarmReceiver: `…AppComponentsImpl.inject(…)`. `AMGUIUtility.displayError/displayException/doProgressTask/doConfirmProgressTask@<caller>` (A2 merge, A3 lookup, A4 PreviewEdit/Detail, A5 downloads). `AboutUtil.createAboutDialog` (A2 Misc). `AnyMemoWidgetProvider.updateWidget`, `NotificationUtil.cancelNotification` (A3 `QACardActivity.onDestroy`). `AMPrefUtil.*` (A2, A3, A4). |
| **A2 Decks, files, import/export, sharing** | `ui/{RecentListFragment, OpenTabFragment, EditTabFragment, MiscTabFragment, OpenActionsFragment, FileBrowserFragment, FileBrowserActivity, ExportAnyMemoDbFragment, ConverterFragment, DatabaseMerger, ShareScreen}`, `ui/helper/SelectableAdapter`, `converter/*` (15), `service/ConvertIntentService`, `utils/{RecentListUtil, RecentListActionModeUtil, DatabaseOperationDialogUtil, DatabaseImportUtil, FolderImportExportUtil, AMFileUtil, AMZipUtils, DatabaseUtil, ShareUtil}` (37 top-level) | 399 | 27–53: S_MAIN_RECENT(_EMPTY/_SELECT), S_MAIN_OPEN, S_MAIN_MISC(_IMPORT/_EXPORT), OpenActions and file dialogs, export/convert dialogs, S_FILE_PICKER@*, font picker, S_MERGE(+_PAUSED), S_SHARE(+_PAUSED) | From A1: `AnyMemo$2.onNavigationItemSelected` → `RecentListFragment.<init>`, `OpenTabFragment.<init>`, `MiscTabFragment.<init>` (+ FragmentManager LIFECYCLE into `onAttach`); `AnyMemo.onCreate` → `RecentListActionModeUtil.registerForActivity`; `AnyMemo.prepareFirstTimeRun` → `AMFileUtil.copyFileFromAsset`; `AnyMemo.onActivityResult` → `FolderImportExportUtil.importFolder@WHATS_NEW`; `AnyMemo$FileAsyncTaskLoader.loadInBackground` → `AMFileUtil.*`, `DatabaseUtil.checkDatabase`. S_ENTRY SEND → `ShareScreen.<init>`. From A4: `CardEditor.onOptionsItemSelected` → INTENT `FileBrowserActivity.<init>@IMAGE/@AUDIO`; `SettingsScreen$10.onClick` → `FileBrowserFragment.<init>@FONT`; PreviewEdit merge → INTENT `DatabaseMerger.<init>`. From A5: `UploadDropboxActivity.onCreate` → `FileBrowserFragment.<init>@UPLOAD`; `RecentListUtil.addToRecentList`, `AMZipUtils.unZipFile`, `AMFileUtil.deleteFileWithBackup`. From A3/A4: `ShareUtil.shareCard`, `AMFileUtil.findFileInPaths`. From A4: `DatabaseUtil.readDefaultSetting`. |
| **A3 Review sessions (study, quiz, card player) and card rendering** | `ui/{QACardActivity, StudyActivity, QuizActivity, QuizLauncherDialogFragment, CardPlayerActivity, CardPlayerFragment, CardPlayerSettingDialogFragment, CardFragment, TwoFieldsCardFragment, FlipableCardFragment, GradeButtonsFragment, GestureSelectionDialogFragment, GestureName, CardImageGetter}`, `ui/loader/CardTTSUtilLoader`, `queue/*`, `scheduler/*`, `tts/*`, `service/CardPlayerService`, `service/cardplayer/*`, `utils/{CardTTSUtil, CardTextUtil, DictionaryUtil, AMDateUtil, AnyMemoExecutor}` (35 top-level) | 511 | 54–77: S_STUDY_*, Study dialogs, gestures and lookup dialogs, quiz launcher ×3, S_QUIZ_*, quiz dialogs, S_PLAYER_*, player settings | From A2: `RecentListFragment$RecentListAdapter$1.onClick` and `OpenActionsFragment$1.onClick@*` → INTENT `StudyActivity.<init>`; OpenActions → `QuizLauncherDialogFragment.<init>`, INTENT `CardPlayerActivity.<init>`. From A1: S_HOME_WIDGET row → `StudyActivity.<init>@WIDGET`; S_NOTIFICATIONS (player) → `CardPlayerActivity.<init>`. From A4: `PreviewEditActivity.onCreate` → `QACardActivity.onCreate@PREVIEW` / `startInit@PREVIEW` (all QACardActivity @PREVIEW edges are written by A3); PreviewEdit `menu_card_player` → INTENT `CardPlayerActivity.<init>` (for result); `PreviewEditActivity.showGesturesDialog` → `GestureSelectionDialogFragment.<init>@PREVIEW`; `CardListActivity` → `CardTextUtil.<init>/getSpannableText`, `Scheduler.schedule/isCardNew/isCardForReview`. |
| **A4 Editing, card list, deck settings, statistics** | `ui/{PreviewEditActivity, CardEditor, AudioRecorderFragment, DetailScreen, CardListActivity, CategoryEditorFragment, SettingsScreen, StatisticsScreen}`, `ui/loader/CardWrapperListLoader`, `ui/widgets/{AMSpinner, DoubleClickButton}` (11 top-level) | 354 | 78–109: S_PREVIEW_*, editor pages and dialogs, recorder ×3, S_DETAIL, S_LIST_* + popups, sort dialog, S_DLG_CATEGORY@*, S_SETTINGS@* + dialogs, S_STATS(+_DRAWER) | From A2: `OpenActionsFragment$1.onClick` → INTENT `PreviewEditActivity.<init>`, `CardListActivity.<init>`, `SettingsScreen.<init>@DECK`, `StatisticsScreen.<init>`; `MiscTabFragment.onClick` → `SettingsScreen.<init>@DEFAULT`; `ShareScreen.onClick` → `PreviewEditActivity.<init>`. From A1: `AnyMemo$HandleOpenIntentLoaderCallbacks.onLoadFinished` → `PreviewEditActivity.<init>`; S_NOTIFICATIONS (conversion) → `PreviewEditActivity.<init>`. From A3: `StudyActivity.showEditDialog/gotoDetail/gotoSettings/gotoPreviewEdit/showCategoriesDialog` → `CardEditor.<init>@STUDY`, `DetailScreen.<init>@STUDY`, `SettingsScreen.<init>@DECK`, `PreviewEditActivity.<init>`, `CategoryEditorFragment.<init>@STUDY`; `QuizLauncherDialogFragment.showCategoriesDialog` → `CategoryEditorFragment.<init>@QUIZ`; virtual calls from `QACardActivity.*@PREVIEW` into the PreviewEdit overrides `getContentView` (from `onCreate`), `onPostInit` (from `QACardActivity$2.run`), `onGestureDetected` (from `QACardActivity$8`), `copyToClipboard` (from `displayCard`). |
| **A5 Downloaders and cloud** | `ui/DownloadTabFragment`, `downloader/anymemo/*`, `downloader/common/*`, `downloader/dropbox/*` (incl. `entity/UserInfo`), `downloader/oauth/*`, Dropbox binding classes (20 top-level) | 226 | 110–121: S_MAIN_DOWNLOAD, S_DL_ANYMEMO(_CAT), download dialogs, S_DROPBOX_AUTH(+_PAUSED), S_DROPBOX_LIST(+_PAUSED), S_DROPBOX_UPLOAD + dialogs | From A1: `AnyMemo$2.onNavigationItemSelected` → `DownloadTabFragment.<init>`. From S_ENTRY: deep link `anymemo-dropbox://oauth#access_token=…` → `DropboxOauth2AccountActivity.onNewIntent` (singleTask; `needs_state` "auth activity alive"); S_EXT_BROWSER return. |
| **A6 Data layer** | `common/{AnyMemoDBOpenHelper, AnyMemoDBOpenHelperManager}`, `dao/*`, `entity/*` (incl. `Option`, `SchedulingAlgorithmParameters`, `ReviewOrdering`), `ui/loader/{MultipleLoaderManager, DBLoader, SettingLoader}` (32 top-level) | 330 | none | CALL edges from all areas: `AnyMemoDBOpenHelperManager.getHelper/releaseHelper/forceRelease`, `AnyMemoDBOpenHelper.get*Dao`, DAO and entity methods, `Option.*`, `SchedulingAlgorithmParameters.*`, `MultipleLoaderManager.registerLoaderCallbacks/setOnAllLoaderCompletedRunnable/startLoading/checkAllLoadersCompleted/destroy@<ctx>`, `DBLoader.loadInBackground@<loader>`, `SettingLoader.<init>`. |

### 6.3 Shared-infrastructure ownership and the edge-writing protocol

- **Who writes an edge:** the area that owns its `src`. GUI edges are written by the page owner, ENTERS edges by the method owner. A RESULT edge is written by the area of the finishing method, using a caller variant: e.g. A4 writes `CardEditor$SaveCardTask.onPostExecute@STUDY → StudyActivity.onActivityResult` and `…@PREVIEW → PreviewEditActivity.onActivityResult`.
- **Base classes and DI** (A1): every area emits `X.onCreate → BaseActivity.onCreate@X`; A1 writes the bodies of the `@X` variants, which are identical, plus the Dagger chains.
- **QACardActivity** (A3) is the base of PreviewEditActivity (A4). A3 writes every `QACardActivity.*@PREVIEW` edge, including its virtual calls into the PreviewEdit overrides. A4 writes only the PreviewEdit methods.
- **FileBrowserFragment** (A2) is hosted by A2, A4 and A5. A2 writes every `FileBrowserFragment.*@<host>` edge; hosts write the INTENT/CALL into `<init>@<host>` and the FragmentManager LIFECYCLE into `onAttach@<host>`.
- **CategoryEditorFragment** (A4) is used by A3 (Study, QuizLauncher) and A4 (PreviewEdit, CardEditor). A4 writes all `@STUDY/@QUIZ/@PREVIEW/@EDITOR` variants, ending in the caller's result listener (`StudyActivity$3`, `QuizLauncherDialogFragment$10`, `PreviewEditActivity$11`, `CardEditor$8`).
- **MultipleLoaderManager** (A6) needs caller variants @MAIN_VIEW, @STUDY, @QUIZ, @PREVIEW, @PLAYER, @SETTINGS, @LIST. Its completion posts the caller's runnable: `QACardActivity$2.run@<ctx>`, `SettingsScreen$6.run`, `CardListActivity$11.run`, and for AnyMemo none (`setOnAllLoaderCompletedRunnable` is not called).
- **Dialog helpers** (`AMGUIUtility`, `AboutUtil`, `DatabaseOperationDialogUtil`, `DatabaseImportUtil`, `DictionaryUtil`) need `@caller` variants written by their owners.
- **Suggested order:** all six areas can start in parallel once the node names in §6.2 are fixed. A6 and the A1 DI/base part are mostly mechanical CALL edges, so the bytecode auto-edges of tooling v2 should cover them first.

## 7. Baseline coverage by area and screen

### 7.1 Per area (JaCoCo methods; DEAD/FW = candidates from §5)

| Area | Methods | Both | Monkey only | APE only | Neither | DEAD cand. | FW-only cand. | Reachable, not hit by Monkey (target pool) | Reachable, hit by neither |
|---|---|---|---|---|---|---|---|---|---|
| A1 Shell/platform/infra | 372 | 138 | 17 | 53 | 164 | 44 | 15 | 158 | 105 |
| A2 Decks/files/import-export | 399 | 99 | 27 | 99 | 174 | 34 | 4 | 235 | 136 |
| A3 Review sessions | 511 | 210 | 0 | 139 | 162 | 15 | 8 | 278 | 139 |
| A4 Editing/list/settings/stats | 354 | 38 | 0 | 169 | 147 | 2 | 9 | 305 | 136 |
| A5 Downloaders/cloud | 226 | 0 | 0 | 78 | 148 | 68 | 4 | 154 | 76 |
| A6 Data layer | 330 | 141 | 0 | 63 | 126 | 64 | 7 | 118 | 55 |
| **Total** | **2192** | **626** | **44** | **601** | **921** | **227** | **47** | **1248** | **647** |

Totals check: Monkey 626 + 44 = 670; APE 626 + 601 = 1227; either 1271; neither 921. The target pool is 2192 − 670 − 227 − 47 = 1248, before any env or `needs_state` refinement.

- **Monkey-only methods (44)** all come from Monkey opening Misc → Export → a ConverterFragment or ExportAnyMemoDbFragment dialog. That instantiated the Dagger converter map: `DaggerAppComponents$AppComponentsImpl.mapOfClassOfAndConverter`, 14 `AppModules.provides*`, `FragmentComponentsImpl.inject/injectConverterFragment`, and 17 converter `<init>`/`<clinit>`/`setSeparator` methods. It also covered `ConverterFragment` (4), `ExportAnyMemoDbFragment` (5) and `MiscTabFragment.onActivityResult` (MK line coverage `J/ui/MiscTabFragment.java:253-255,290-296,314-320`). APE never opened an export item.
- **A5 has no Monkey coverage**: Monkey never opened the Download tab. **A4 has 38 Monkey methods**, all from `DetailScreen` (13), `CategoryEditorFragment` (21) and `DoubleClickButton` (4, the category dialog's Delete button).

### 7.2 Per screen (methods incl. inner classes: total / Monkey / APE)

| Area | Window | Total | M | A | Never-reached reason, or what is missing |
|---|---|---|---|---|---|
| A1 | AnyMemo | 30 | 13 | 18 | VIEW intent path (8) and permission result never exercised; Monkey never opened the drawer |
| A1 | OptionScreen / AlgorithmCustomization | 7 / 7 | 6 / 5 | 6 / 6 | only `onConfigurationChanged` (FW) is missing |
| A1 | Widget (provider, service, factory) | 18 | 1 | 1 | needs a placed widget (launcher, outside the package) |
| A1 | AlarmReceiver / SetAlarmReceiver.onReceive | 3 / 1 | 0 | 0 | time-gated alarm in `:remote` (not dumped); boot broadcast |
| A1 | CardProvider / DatabasesProvider queries | 8 / 8 | 0 | 0 | external clients only (only `<init>/onCreate` ran) |
| A1 | NotificationUtil.showNotification + `$DatabaseInfo` | 6 | 0 | 0 | alarm-triggered, and ≥ 10 due cards |
| A2 | RecentListFragment | 54 | 41 | 49 | `setUserVisibleHint` chain (FW), SAF import result |
| A2 | OpenTab / FileBrowserFragment | 4 / 58 | 0 / 24 | 4 / 47 | Monkey never opened the Open tab; SAF import, overwrite and import callbacks missing in both |
| A2 | MiscTabFragment | 18 | 7 | 9 | the SAF result branches and the import-merge dialogs |
| A2 | OpenActionsFragment | 8 | 0 | 7 | the delete confirmation was never accepted |
| A2 | ExportAnyMemoDb / ConverterFragment | 14 / 12 | 5 / 4 | 0 / 0 | the file tap leads to SAF CREATE_DOCUMENT (outside the package) |
| A2 | ConvertIntentService + converters | 8 + 82 | 0 + 17 | 0 + 0 | conversion starts only after a SAF result |
| A2 | FileBrowserActivity | 6 | 0 | 4 | a file tap that returns a result never happened |
| A2 | DatabaseMerger / ShareScreen | 8 / 4 | 0 | 0 | not explored / needs the SEND chooser |
| A3 | StudyActivity + QACardActivity | 56 + 59 | 31 + 45 | 49 + 54 | gestures (Monkey), volume keys, the mark-forever OK, `onCreateContextMenu` (FW), double-sided |
| A3 | GradeButtonsFragment, CardFragment, TwoFields | 31, 22, 9 | 26, 21, 9 | 28, 21, 9 | `$1.onClick` (FW) and `$2.onTouch` |
| A3 | FlipableCardFragment | 7 | 0 | 0 | the card style is never DOUBLE_SIDED |
| A3 | QuizLauncher / QuizActivity | 42 / 37 | 0 / 0 | 42 / 29 | quiz complete-all, no-item and cancel dialogs |
| A3 | CardPlayer activity/fragment/settings/service + state machine | 24+18+13+22+36 | 0 | 0 | never opened (OpenActions "Card player", PreviewEdit menu) |
| A3 | GestureSelectionDialogFragment | 11 | 0 | 11 | Monkey never opened the Study overflow "gestures" item |
| A4 | PreviewEditActivity | 68 | 0 | 38 | search submit, the More submenu (wipe/swap all/remove dup/shuffle), gestures dialog, categories result |
| A4 | CardEditor / AudioRecorder | 50 / 15 | 0 | 35 / 10 | Back with unsaved edits, existing-audio picker, permission result, playback |
| A4 | DetailScreen | 20 | 13 | 20 | fully reached by APE |
| A4 | CardListActivity | 66 | 0 | 0 | never opened |
| A4 | CategoryEditorFragment | 44 | 21 | 35 | Delete (needs a double tap within 5 s), Edit task body |
| A4 | SettingsScreen | 50 | 0 | 39 | Back with changes, font pickers, `onNothingSelected` (FW) |
| A4 | StatisticsScreen | 27 | 0 | 21 | the "accumulative" and "grade" charts |
| A5 | DownloadTab / AnyMemo downloader (activity+fragment / abstract base) | 4 / 16+39 | 0 | 4 / 15+32 | every never-hit method here is a DEAD candidate (load-more path, unused helpers); error dialogs are branch-level only |
| A5 | Dropbox OAuth / list / upload | 5+14 / 19 / 14 | 0 | 3+4 / 0 / 0 | empty consumer key; no OAuth callback |
| A5 | OAuth1 classes | 34 | 0 | 0 | DEAD |

### 7.3 Main reasons the baseline missed code (most methods first)

1. **SAF and other system UI outside the app package** (about 120 never-hit methods in A2, plus the A1 What's-new import): DocumentsUI pickers, the share chooser and the permission dialogs. Monkey and APE with `-p` cannot complete those flows (FW-MEMORY).
2. **Screens never opened**: the card player (113), `CardListActivity` (68 with its loader), `DatabaseMerger`/`ShareScreen` (12).
3. **DEAD or FRAMEWORK_ONLY candidates** (274, §5): no tool can reach them; they should not become targets.
4. **Accounts and keys**: Dropbox. All 76 reachable never-hit methods of A5 (62 in `downloader/dropbox|oauth`, 14 in the Dropbox binding classes) sit behind the OAuth callback.
5. **Outside the GUI**: widget (17), alarm and boot receivers (5), provider queries (16), the review notification (6), the VIEW intent (8) and the SEND entry (4): 56 never-hit methods in A1/A2, 2 of which are §5 candidates (`NotificationUtil$DatabaseInfo.getNewCount`, `AnyMemo$HandleOpenIntentLoaderCallbacks.onLoaderReset`).
6. **Settings-dependent modes**: double-sided cards, audio disabled (`NullAnyMemoTTS`), user audio files, gestures, volume keys, speaking type AUTO (Monkey only), the Anki/Mnemosyne button styles.
7. **Data-dependent branches**: empty decks (no-item dialogs), ≥ 10 due cards, legacy DB formats (`convertOldDatabase`, `onDowngrade`), images in cards.
8. **Monkey specifically** was confined to Recent → Study → Detail for about 48 minutes (§2.2), so it covered almost nothing in A4 or A5.

## 8. Conclusions and recommendations

1. **Method set.** Use the JaCoCo universe of 2192 methods. With `tools/list_methods.py` you get 2626, so either exclude the 365 Dagger-generated methods, the 47 enum helpers, the 16 private empty constructors and the 8 switch-map `<clinit>`, and add back `BuildConfig.<init>/<clinit>`; or join by JVM descriptor against `report.xml`, as Currency did.
2. **Pages.** Start from the 121 rows in §3.3. Collapse the preference dialogs to 3 pages, since only the Float/Integer preferences run app code, and expand `@` variants only where the continuation differs (§3.4). That gives about 150 page names.
3. **Parallel build.** Use the 6 areas of §6, with the "src owner writes the edge" protocol and the cross-area node names in §6.2. A6 and the DI part of A1 are mostly mechanical: generate them from bytecode CALL edges first.
4. **Verdicts.** Carry the 227 DEAD and 47 FRAMEWORK_ONLY candidates (§5) into the graph, but confirm the FW-MEMORY ones before the paper. Most uncertain: the loader `onLoaderReset` (7), the data-binding mapper methods (5), the `onConfigurationChanged` set (5) and `CategoryEditorFragment$DeleteCategoryTask.onCancelled` (UNVERIFIED). None contradicts the baseline.
5. **Mark `needs_state` / `env`** on:
   - first-run paths ("fresh data or after Misc → Reset");
   - SAF flows (`env: DocumentsUI interaction`);
   - Dropbox (`env: consumer key + account, or deep-link injection`);
   - network (anymemo.org);
   - widget, alarm and boot (`env: launcher/system`);
   - the `:remote` alarm process ("coverage not observable").
6. **Fix the baseline harness for the next runs** (not part of this task):
   - include `coverage/00000.ec` in the merged report, or start from a fresh install after the warm-up, so the first-run code is credited;
   - add a coverage dump for the `:remote` process;
   - pre-place the fixtures from §2.4 (a second deck, an empty deck, a multi-category deck, a media deck, a `.ttf`, importable files in `Download/`). The `_fixtures` folder has no AnyMemo-format `.db`, no Q/A text, no XML deck and no zip that contains a `.db`.
7. **Hazards worth one emulator check each** (§5.5): the card player on an empty deck, Dropbox logout, and the PreviewEdit menu actions on an empty deck. These are likely crash paths, so the graph should model them as edges to S_EXIT.

