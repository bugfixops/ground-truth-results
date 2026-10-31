# AnkiDroid 2.6beta6 (#4200): UI map and modeling plan

Read-only investigation for the trigger-graph build. Package `com.ichi2.anki`, debug build (`BuildConfig.DEBUG = Boolean.parseBoolean("true")`, read from `BuildConfig.class`), minSdk 10, targetSdk 23 (`AnkiDroid/build.gradle:12-13`), baseline on API 27.

## Summary

- **Size and entry points.** The JaCoCo method universe is 4178 methods in 648 classes (258 source files, JacocoInstrument excluded). The launcher entry is a transparent trampoline (`IntentHandler`) that forwards to the home screen `DeckPicker`. Other external entries: `VIEW *.apkg` (IntentHandler), `SEND text/plain` and `CREATE_FLASHCARD` (NoteEditor), the Tasker action `DO_SYNC`, an exported ContentProvider, a home-screen widget and an SD-card receiver.
- **Gates.** There is no intro or onboarding screen. Before the main UI works, the app needs (1) the storage permission, (2) an AnkiDroid folder it can create and write, and (3) cards (a new collection has only an empty Default deck). An AnkiWeb login is needed **only for sync** (about 184 methods), not for the rest of the app.
- **Why Monkey collapsed (3%).** In all 20 Monkey processes, `CollectionHelper.initializeAnkiDroidDirectory` failed at `mkdirs()` (`CollectionHelper.java:171-172` covered, line 174 never reached). When that happens, `DeckPicker.onCreate` opens the *Advanced settings* screen and finishes itself as soon as that screen closes (`DeckPicker.java:425-429, 673-675`). So the collection never opened, and Monkey spent the hour in Settings and About (Preferences classes appear in 105 of the 117 readable coverage segments).
- **APE had the same failure.** APE's first 16 processes (about 13 minutes) failed the same way. From process 17 on, every process opened the collection. The app code does not show what changed: the in-app path editor never accepted a value (`Preferences.java:317` is uncovered in both runs). Cause: **UNVERIFIED**, a device-side state.
- **Setup was never done.** Neither run performed the dataset's setup step: the VIEW-import branch `IntentHandler.java:47-125` is uncovered and the importer package is 0/41. Neither run logged in (sync 0/131 incl. `Connection`), and neither used the widget or the provider API.
- **Plan.** 140 candidate pages (section 3.3) and 8 feature areas (section 6): Platform 588 methods, Home 395, Sync 184, Study 477, Browse/Edit 591, Config 369, Stats 780, Core/libanki 794.
- **Unreachable candidates.** About 450 methods (11%) are in classes with no caller or behind build-config, API or hardware gates. Examples: the `api` client module (62), unused wildplot parsing and renderers (263), `Base64` (42), `CustomExceptionHandler` (10), the release-only crash tree (10). About 300 more are behind an account or network, a file to import, or external-only entries (widget, provider, other apps).

**Conventions.** `M:n` = `AnkiDroid-#4200/AnkiDroid/src/main/AndroidManifest.xml` line n. `anki/X.java:n` = `AnkiDroid-#4200/AnkiDroid/src/main/java/com/ichi2/anki/X.java`; the same pattern holds for `libanki/`, `async/`, `compat/`, `widget/`, `utils/`, `ui/`, `themes/`, `preferences/`, `wildplot/` (= `com/wildplot/android/`). `api/X.java` = `AnkiDroid-#4200/api/src/main/java/com/ichi2/anki/api/X.java`. `res/...` = `AnkiDroid/src/main/res/...`. Coverage: `monkey|ape/report/report.xml` and segments `monkey|ape/coverage/NNNNN.ec` under `final_java_only/AnkiDroid/`. "M+/A+" = line or method covered by Monkey or APE. Labels: **SRC** = read in source, **FW-MEMORY** = Android behaviour recalled and not checked, **INFERRED**, **UNVERIFIED**.

**What was read.** Read completely: both manifests, both `build.gradle`; `IntentHandler`, `AnkiDroidApp`, `CollectionHelper`, `AnkiActivity`, `NavigationDrawerActivity`, `DeckPicker`, `Preferences`, `Info`, `Reviewer`, `StudyOptionsActivity`, `Previewer`, `MyAccount`, `DialogHandler`, `CollectionLoader`, `WidgetStatus`, `AnkiDroidWidgetSmall`, `SdCardReceiver`, `NotificationService`, `DeckPickerContextMenu`, `ImportDialog`, `Hooks`.
Read in part: `AbstractFlashcardViewer` (listeners, lifecycle, task handlers), `DeckTask` (dispatch), `CardBrowser`, `NoteEditor`, `CardTemplateEditor`, `DeckOptions`, `Statistics`, `StudyOptionsFragment`, `CustomStudyDialog`, `MultimediaEditFieldActivity`, `BasicTextFieldController`, `CardContentProvider`, `Collection`, `Storage`, `BackupManager`, `TagsDialog`.
Everything else was mapped with targeted greps (declarations, listeners, menus, intents, dialogs). Most of libanki, wildplot and the multimedia field classes were **not** read line by line; the graph builders must read them.

Read-only analyses run: JaCoCo XML aggregation per package, class, method and line; decoding of the per-segment `.ec` files (session ids and per-class probe hits; 3 Monkey segments are not `.ec` data but the text `cat: files/coverage.ec: No such file or directory`); a name-based caller search over all Java sources and XML resources; and the fixture `sample_deck.apkg` opened in memory with `zipfile` and `sqlite3.deserialize`.

---

## 1. Entry points

No merged manifest exists: `AnkiDroid/build/intermediates` contains only `javac/debug/.../classes`. Used instead: `src/main/AndroidManifest.xml` plus `api/src/main/AndroidManifest.xml`. The api manifest adds `uses-permission com.ichi2.anki.permission.READ_WRITE_DATABASE` (`api/src/main/AndroidManifest.xml:3`). The build types are debug and release, with no product flavors (`AnkiDroid/build.gradle:29-37`); the APK is the debug variant. androidTest sources (`src/androidTest/java/com.ichi2.anki.tests/*`, 5 files) are not in the class dirs.

Permissions requested (`M:52-57`): `WRITE_EXTERNAL_STORAGE` and `RECORD_AUDIO` (runtime on API 23+), plus `VIBRATE`, `INTERNET`, `ACCESS_NETWORK_STATE`, `WAKE_LOCK`. The app defines `com.ichi2.anki.permission.READ_WRITE_DATABASE` with protection level `dangerous` (`M:58-61`).

| # | Component | Kind | exported | Intent filters / how it starts | launchMode / theme / configChanges | Evidence |
|---|---|---|---|---|---|---|
| 0 | `AnkiDroidApp` | Application | – | Process start. ACRA init; in DEBUG it forces `reportErrorMode="1"` (ACRA off) and plants `Timber.DebugTree`; creates the AnkiDroid folder if it has the storage permission | – | `M:73-79`; `anki/AnkiDroidApp.java:147-200` (DEBUG branch 155-163, folder 188-199) |
| 1 | `IntentHandler` | Activity | yes (has filters) | (a) MAIN/LAUNCHER (+`MULTIWINDOW_LAUNCHER`); (b) VIEW + BROWSABLE, schemes http/https/content/file, host `*`, mime `*/*`, `pathPattern .*\.apkg`; (c) VIEW with mime `application/apkg`, `application/x-apkg`, `application/octet-stream` (content), `application/zip` (content); (d) action `com.ichi2.anki.DO_SYNC` (Tasker) | standard; `@android:style/Theme.Translucent.NoTitleBar` (invisible trampoline); `keyboardHidden\|orientation\|screenSize\|locale` | `M:80-131`; handler `anki/IntentHandler.java:38-141` |
| 2 | `DeckPicker` | Activity (home) | false | From IntentHandler, drawer "Decks", notifications, `CLEAR_TOP\|NEW_TASK` returns | `Theme_Dark_Compat.Launcher`; kh\|or\|ss\|locale | `M:132-138` |
| 3 | `StudyOptionsActivity` | Activity | false | `DeckPicker.openStudyOptions` | parent DeckPicker; kh\|locale\|or\|ss | `M:139-149` |
| 4 | `CardBrowser` | Activity | false | Drawer "Card browser", DeckPicker/Reviewer `openCardBrowser` | parent DeckPicker | `M:150-160` |
| 5 | `ModelBrowser` | Activity | false | DeckPicker menu "Manage note types" | – | `M:161-165` |
| 6 | `ModelFieldEditor` | Activity | false (no filter) | ModelBrowser list tap | – | `M:166-169` |
| 7 | `Reviewer` | Activity | false | DeckPicker, StudyOptions, CustomStudyDialog | `adjustResize`; parent DeckPicker | `M:170-180` |
| 8 | `VideoPlayer` | Activity | false | `AbstractFlashcardViewer.playVideo` | `Theme.NoTitleBar.Fullscreen` | `M:181-185`; `anki/AbstractFlashcardViewer.java:2799-2804` |
| 9 | `MyAccount` | Activity | false | `DeckPicker.loginToSyncServer`; intent in `res/xml/preferences_general.xml` ("syncAccount") | – | `M:186-190` |
| 10 | `Preferences` | Activity (PreferenceActivity) | false | Drawer "Settings"; DeckPicker path gate; subscreen intents | `LegacyActionBarLight` | `M:191-196` |
| 11 | `DeckOptions` | Activity (PreferenceActivity) | false | Deck context menu, StudyOptions, Reviewer, CustomStudyDialog | `LegacyActionBarLight` | `M:197-202` |
| 12 | `FilteredDeckOptions` | Activity (PreferenceActivity) | false | Deck context menu (filtered deck), StudyOptions | `LegacyActionBarLight` | `M:203-208` |
| 13 | `Info` | Activity | false | Advanced settings "About" (`res/xml/preferences_advanced.xml:137-143`); DeckPicker new-version screen (release builds only, see 2.2) | `configChanges="locale"` only, so rotation recreates it | `M:209-213` |
| 14 | `NoteEditor` | Activity | **true** | `org.openintents.action.CREATE_FLASHCARD` (`M:219-222`); `SEND` `text/plain` (`M:223-227`); internal callers set `EXTRA_CALLER` | kh\|or\|locale\|ss | `M:214-228`; `anki/NoteEditor.java:287-310` |
| 15 | `dialogs.AnkiDroidCrashReportDialog` | Activity (ACRA dialog) | false (no filter) | Started by ACRA when a report is handled in DIALOG mode | **singleInstance**, excludeFromRecents, finishOnTaskLaunch, `Theme.CrashReportDialog` (dialog theme) | `M:229-233`; `anki/AnkiDroidApp.java:54-111` |
| 16 | `Statistics` | Activity | false | Drawer "Statistics" | parent DeckPicker | `M:234-243` |
| 17 | `Previewer` | Activity | false | CardBrowser context menu "Card info/preview", CardTemplateEditor "Preview" | `configChanges="locale"` (rotation recreates) | `M:244-248` |
| 18 | `services.NotificationService` | started Service | false | `WidgetStatus` `startService` when due-card notifications are on | – | `M:250`; `widget/WidgetStatus.java:89-121` |
| 19 | `widget.AnkiDroidWidgetSmall` | Receiver (AppWidgetProvider) | yes (filter) | `APPWIDGET_UPDATE`; meta `@xml/widget_provider_small` (`updatePeriodMillis=3600000`) | – | `M:253-264`; `res/xml/widget_provider_small.xml` |
| 20 | `widget.AnkiDroidWidgetSmall$UpdateService` | started Service | false | `WidgetStatus` when `widgetSmallEnabled` | – | `M:266` |
| 21 | `receiver.SdCardReceiver` | Receiver | **true** (explicit), enabled | `MEDIA_MOUNTED`, `MEDIA_EJECT`, scheme `file`. Re-broadcasts custom `com.ichi2.anki.action.MEDIA_EJECT/MOUNT` | – | `M:268-282`; `anki/receiver/SdCardReceiver.java:36-58` |
| 22 | `multimediacard.activity.MultimediaEditFieldActivity` | Activity | false | NoteEditor field media popup | – | `M:284-289` |
| 23 | `multimediacard.activity.TranslationActivity` | Activity | false | Text field "Translate", choice Glosbe | – | `M:290-295` |
| 24 | `multimediacard.activity.LoadPronounciationActivity` | Activity | false | Text field "Pronounce" | – | `M:296-301` |
| 25 | `CardTemplateEditor` | Activity | false | NoteEditor "Cards" button, ModelBrowser context menu "Templates" | `stateAlwaysHidden\|adjustPan` | `M:302-308` |
| 26 | `provider.CardContentProvider` | ContentProvider | **true** | authority `com.ichi2.anki.flashcards`, meta `com.ichi2.anki.provider.spec=2`. No manifest permission attributes. The code requires `READ_WRITE_DATABASE` on API ≥ 23 (`shouldEnforce*` → `isMarshmallow()`); the DEBUG build also allows self-calls | – | `M:324-330`; `anki/provider/CardContentProvider.java:199-212, 1303-1308` |
| 27 | `JacocoInstrument.SMSInstrumentedReceiver` | Receiver | yes | `edu.gatech.m3.emma.COLLECT_COVERAGE` (coverage harness, **excluded**) | – | `M:332-336` |
| – | `compat.customtabs.KeepAliveService` | Service class | **not in manifest** | Only passed as a ComponentName to Chrome Custom Tabs (`compat/customtabs/CustomTabsHelper.java:51`); without a manifest entry it cannot be bound (FW-MEMORY) | – | grep of `M` |

Not present: activity-aliases, launcher shortcuts, search, SEND for files, other deep links, `launchMode` on any normal activity, data binding.

**Rotation (FW-MEMORY).** All activities except `Info`, `Previewer` and the crash dialog declare `orientation|screenSize`, so rotation calls `onConfigurationChanged` and does not recreate them. `onRestoreInstanceState` is then reachable mainly after process death or task restore. Monkey hit `DeckPicker.onRestoreInstanceState` (`anki/DeckPicker.java:723-726`), which fits task restore after its 26 app crashes (`final_java_only/comparison_ape_vs_monkey_api27.csv`; INFERRED).

---

## 2. First-run flow and setup gates

### 2.1 Start-up sequence (SRC)

1. **Process start.** `CardContentProvider.<clinit>/<init>/onCreate` run before `Application.onCreate` (FW-MEMORY). This matches the evidence: both tools hit exactly these 3 provider methods and nothing else in the provider.
2. **`AnkiDroidApp.onCreate`** (`anki/AnkiDroidApp.java:147-200`): ACRA off in DEBUG (155-163), language, WebView cookies, swipe defaults; if the storage permission is held, `initializeAnkiDroidDirectory(deckPath)` (188-199).
3. **`IntentHandler.onCreate`** (`anki/IntentHandler.java:38-141`): MAIN → `startActivityIfNeeded(DeckPicker, NEW_TASK|CLEAR_TASK)` and finish (134-139). VIEW → validate and copy the file (46-125), store `MSG_SHOW_COLLECTION_IMPORT_*` in `DialogHandler.sStoredMessage` (148-168), start DeckPicker with `CLEAR_TOP`, or show an error dialog (110-124). DO_SYNC → store `MSG_DO_SYNC` (126-131, 173-178).
4. **`DeckPicker.onCreate`** (`anki/DeckPicker.java:353-436`): `firstCollectionOpen()` (442-455) either requests the permission (450) or calls `getColSafe` → `CollectionHelper.getCol` (`anki/CollectionHelper.java:87-102`) → `initializeAnkiDroidDirectory` (169-187) → `Storage.Collection(..., create=true)`. Then it sets up the UI: drawer (372), RecyclerView adapter and listeners (383-388), FAB (391-405).
   - If the collection opened: `showStartupScreensAndDialogs(prefs, 0)` (417).
   - Otherwise (419-435), in order:
     - no permission → wait for `onRequestPermissionsResult`;
     - SD card not mounted → toast and finish;
     - folder inaccessible → **Advanced settings for result `REQUEST_PATH_UPDATE`** plus the toast "directory inaccessible" (425-429);
     - cursor limit or load failed → `DatabaseErrorDialog`.
5. **`AnkiActivity.onResume`** (`anki/AnkiActivity.java:78-83`) cancels the simple notification and replays the stored DialogHandler message (`dialogs/DialogHandler.java:130-136`, `handleMessage` 56-117 casts the activity to DeckPicker).
6. **`showStartupScreensAndDialogs`** (`anki/DeckPicker.java:847-961`):
   - low disk → `DeckPickerNoSpaceLeftDialog` (848-851);
   - earlier backup failure → `DeckPickerBackupNoSpaceLeftDialog` (852-854);
   - **fresh install**: `lastVersion` empty → store it, then `onFinishedStartup` (855-858), with **no intro screen**;
   - upgrade path (859-955) only when `lastVersion` holds an older version;
   - otherwise `onFinishedStartup` (957-960).
7. **`onFinishedStartup`** (806-832): background backup (`BackupManager.performBackupInBackground`), the upgrade-only full-sync prompt, the tablet fragment, `automaticSync` (760-772: needs `hkey`, pref `automaticSyncMode`, online, and more than 10 minutes since the last sync). `onResume` (700-712) then loads the deck list (DeckTask `LOAD_DECK_COUNTS`, 1822-1886).

### 2.2 Gates and the code that enforces them

| Gate | Enforced by (SRC) | Passes when | Baseline evidence |
|---|---|---|---|
| G1 Storage runtime permission | `anki/DeckPicker.java:442-455` (request at 450); result `680-696`: if denied, toast, finish and open the system app-details settings (689-693); the handler acts only if `permissions.length == 1` (681) | `WRITE_EXTERNAL_STORAGE` granted | Granted in both runs: line 450 and lines 681-693 never covered (M- A-). |
| **G2 AnkiDroid folder creatable/writable** | `anki/CollectionHelper.java:169-187` (`!exists && !mkdirs` → throw at 172; `!canWrite` 174-176; `.nomedia` 178-185). Callers: `getCol` 87-102 returns null; `isCurrentAnkiDroidDirAccessible` 193-200. **Trap:** `anki/DeckPicker.java:425-429` opens `CompatHelper.getPreferenceSubscreenIntent(..."com.ichi2.anki.prefs.advanced")` for result; `673-675` `REQUEST_PATH_UPDATE` → `finishWithoutAnimation()` | Folder `deckPath` (default `<external storage>/AnkiDroid`, 205-231) exists or can be created, and is writable | **Failed**: Monkey in all 20 processes, APE in its first 16. Monkey covered line 172 (branch 171 2/4) and never reached 174-186, so `mkdirs()` returned false every time. |
| G2' In-app escape (folder setting) | `anki/Preferences.java:307-323`: the `deckPath` change listener calls `initializeAnkiDroidDirectory(newPath)`; on failure it shows a toast and rejects the value | The user types a creatable absolute path | Never accepted: line 317 `return true` uncovered in both; catch 318-321 covered in both. |
| G3 SD card mounted | `anki/DeckPicker.java:422-424`; `AnkiDroidApp.isSdCardMounted` (`anki/AnkiDroidApp.java:239-241`) | `Environment.MEDIA_MOUNTED` | True in all processes (line 424 never covered). |
| G4 Collection DB opens | `anki/DeckPicker.java:430-434` → `DatabaseErrorDialog` `CURSOR_SIZE_LIMIT_EXCEEDED`/`LOAD_FAILED` | Valid `collection.anki2` | Never failed this way. |
| G5 Disk space | `anki/DeckPicker.java:848-854`; `BackupManager` sets pref `noSpaceLeft` | Enough space | Not hit. |
| G6 Version screens | Upgrade branch `anki/DeckPicker.java:859-955`; `Info` new-version screen only if `VersionUtils.isReleaseVersion()` (`utils/VersionUtils.java:71-73`: 3rd-last digit of the versionCode must be `3`; `20600206` has `2`, i.e. beta). `SHOW_INFO_WELCOME` and `REPORT_ERROR` are never used as request codes (only at 645-653) | Older `lastVersion` in prefs (and a release build for Info) | Unreachable on a clean install of this build. |
| G7 Data present | `handleDeckSelection` `anki/DeckPicker.java:1717-1805`: due cards → Reviewer (phone) or StudyOptions; limits reached / empty schedule / empty deck → snackbars; filtered deck → StudyOptions | Cards exist | A new collection has only "Default" and 4 standard note types (`libanki/Storage.java:66-72`). |
| G8 Import | `ImportDialog.java:86-96`: the list comes from `libanki/Utils.getImportableDecks` (= `*.apkg` files directly in the AnkiDroid folder); else toast and auto-cancel. VIEW path `anki/IntentHandler.java:46-125` → `DialogHandler` → `ImportDialog` ADD/REPLACE | `.apkg` in `/sdcard/AnkiDroid` or a VIEW intent | **Never**: `IntentHandler.java:47-125` uncovered in both; `libanki/importer` 0/41; ImportDialog ADD/REPLACE cases uncovered. The dataset setup step was not performed. |
| G9 AnkiWeb login (sync only) | `anki/DeckPicker.java:1278-1289`: empty `hkey` → `SyncErrorDialog.DIALOG_USER_NOT_LOGGED_IN_SYNC` → `loginToSyncServer` (1570-1575) → `MyAccount`. `MyAccount.login` needs a non-empty username and password (`anki/MyAccount.java:125-145`); `Connection.login` needs network (`async/Connection.java:83`) | Valid account (or a custom sync server, `res/xml/preferences_custom_sync_server.xml`) plus network | APE reached the login form (`MyAccount.login` M- A+) but never called `Connection.login` (`Connection` 0/27). |
| G10 Synced collection | `Collection.modSchema(check)` throws `ConfirmModSchemaException` only when `!schemaChanged()` = `scm <= ls` (`libanki/Collection.java:364-382`). A new collection has `ls=0` (`libanki/Storage.java:316-318`); `ls` is set only by sync (`libanki/sync/Syncer.java:428`, `libanki/Collection.java:395-407`). The fixture also has `ls=0` | A successful sync | Never. All "a full sync will be required" confirmations are gated by G9 (list in 5.2). |
| G11 Network / external apps | Translation (Glosbe, `TranslationActivity.java:196-243`), pronunciation (Beolingus), shared decks, help, feedback, sign-up (custom tabs), Play Store, email, gallery, camera, ColorDict, dictionary apps (`Lookup`), TTS engine | Network and the apps | Partly (custom tabs bound; `compat/customtabs/ServiceConnection` hit). |

**"AnkiDroid needs a login"** (`final_java_only/README.md:10`) is true only for the sync area. All decks, review, browser, editor, note types, settings and statistics work offline without an account. SRC: `grep '"hkey"'` finds the login token only in `MyAccount.java:92/120/151`, `DeckPicker.java:765` (automaticSync), `1280` (sync), `1427` (bad auth), `DialogHandler.java:102` (DO_SYNC) and the ACRA exclusion list (`AnkiDroidApp.java:66`).

### 2.3 What the baseline reached and what stopped it

Per-process view, decoded from the coverage segments. X = `StorageAccessException` hit; C = `libanki/Storage` hit, i.e. the collection opened:

- **Monkey, 20 processes** (incl. pre-run session `e42ed6f1` in `00000.ec`): all X, none C. The collection **never** opened; `libanki/*` core 0 methods.
- **APE, 28 processes**: the first 16 are X (from `00000.ec`, pre-run, to `00025.ec` at 02:35:20Z). The remaining 12 are all C, starting with session `96e2b7d8` in `00026.ec` (02:35:50Z, about 13 minutes into the run). After that: notes added (`DeckTask.doInBackgroundAddNote` A+), reviews (`Sched.answerCard` A+), export (`doInBackgroundExportApkg` A+), filtered decks (`rebuildDyn`/`emptyDyn` A+), backups (`BackupManager$1` A+).
- What fixed APE's environment is **UNVERIFIED**: the in-app folder editor never succeeded (G2'). To resolve, on the baseline image check `adb shell ls -ld /sdcard /sdcard/AnkiDroid`, `adb shell dumpsys package com.ichi2.anki | grep -A2 WRITE_EXTERNAL_STORAGE`, `adb shell appops get com.ichi2.anki`, and logcat tag `AnkiDroid` for "Could not initialize AnkiDroid directory" (logged at `CollectionHelper.java:94`).

**Monkey's loop** (SRC plus coverage):
1. Launcher → `IntentHandler` → `DeckPicker` (no collection, menu suppressed: `DeckPicker.java:505-510`).
2. → `Preferences` Advanced subscreen + toast.
3. Monkey taps around in Advanced: "About" → `Info` (`res/xml/preferences_advanced.xml:137-143`; Monkey hit 5/5 `Info` methods incl. `copyDebugInfo`); "Custom sync server" and "Advanced statistics" subscreens (`Preferences.java:327-344`; `Preferences$6/$7` 2/2). In the latter it toggled the pref, which installs `AdvancedStatistics` (`Preferences.java:484-490`) — 5 of Monkey's 8 Monkey-only methods are `AdvancedStatistics.<init>/install/uninstall` and two inner constructors; the other 3 are `SeekBarPreference` callbacks.
4. Back → `DeckPicker.onActivityResult(REQUEST_PATH_UPDATE)` → finish → the app is gone → Monkey relaunches.

**Window classes never reached** (method-level JaCoCo; M = Monkey, A = APE):

| Window | M | A | Likely reason |
|---|---|---|---|
| Everything except IntentHandler, DeckPicker (15/77), Preferences (+SettingsFragment), Info, NavigationDrawerActivity (init only) | 0 | – | G2 trap (above) |
| `VideoPlayer` | 0 | 0 | Needs a card that plays a video file; no media in any deck |
| `Whiteboard` | 0 | 0 | Reviewer overflow "Enable whiteboard" never chosen (`Reviewer.java:194-201` uncovered) |
| `TranslationActivity`, `LoadPronounciationActivity`, `PickStringDialogFragment` | 0 | 0 | Need text typed in the multimedia text editor before Translate/Pronounce (`BasicTextFieldController.java:128-131, 153-157`), and network for the actual lookup |
| `AnkiDroidCrashReportDialog` | 0 | 0 | ACRA disabled on every start in DEBUG (`AnkiDroidApp.java:155-160`) |
| `CardBrowserContextMenu`, `ModelBrowserContextMenu` | 0 | 0 | Long-press on a list row never happened (`CardBrowser.java:499-512`, `ModelBrowser.java:283-292`) |
| `CardBrowserMySearchesDialog` | 0 | 0 | "Save search" is visible only with a non-empty query, "My searches" only with saved searches (`CardBrowser.java:575-578, 597-603`) |
| `DeckPickerConfirmDeleteDeckDialog` | 0 | 0 | Shown only for decks with cards; empty decks are deleted silently (`DeckPicker.java:1993-1997`) |
| `DeckPickerNoSpaceLeftDialog`, `DeckPickerBackupNoSpaceLeftDialog` | 0 | 0 | Low-disk environment |
| `NoteEditorRescheduleCard` | 0 | 0 | NoteEditor in edit mode, menu "Reschedule" (`NoteEditor.java:871-874`); APE used only add mode (NoteEditor menu: only `home` and `action_save` covered) |
| Widget (`AnkiDroidWidgetSmall*`), provider CRUD, `api/*` | 0 | 0 | Home screen and other apps, outside `-p com.ichi2.anki`; api is a client library (5.1) |
| Sync (`Connection`, `libanki/sync/*`, most of `SyncErrorDialog`) | 0 | 0 | G9 |
| `libanki/importer/*` | 0 | 0 | G8 |

### 2.4 What a harness must prepare

1. **Pre-grant runtime permissions**: `adb install -g`, or `pm grant com.ichi2.anki android.permission.WRITE_EXTERNAL_STORAGE` and `...RECORD_AUDIO`.
   - Otherwise the system permission dialog belongs to another package. Monkey/APE `-p` abort that activity start, and the requester gets a cancelled result, i.e. `onRequestPermissionsResult` with empty arrays (FW-MEMORY).
   - `DeckPicker.java:681` then does nothing, and the app stays in `S_DECKPICKER_NOCOL` forever.
   - For RECORD_AUDIO, `MultimediaEditFieldActivity.java:322-327` does nothing either, and the audio editor UI is never built.
2. **Verify the AnkiDroid folder before the run.** Launch once and check that `/sdcard/AnkiDroid/collection.anki2` and `.nomedia` were created; this is the G2 check that failed in both baselines.
   - Fallback: preset `deckPath` in `shared_prefs/com.ichi2.anki_preferences.xml` (debug build, so `run-as` works; INFERRED) to a writable directory.
3. **Seed data.**
   - (a) Copy `_fixtures/Download/sample_deck.apkg` into `/sdcard/AnkiDroid/`, so that Import → select list works (`ImportDialog.java:86-123`), and/or
   - (b) the VIEW intent: `adb shell am start -n com.ichi2.anki/.IntentHandler -a android.intent.action.VIEW -d file:///sdcard/Download/sample_deck.apkg -t application/apkg`, then tap **Add**. The `file` branch needs a path ending in `.apkg` (`IntentHandler.java:93-102`).
   - Fixture content (read in memory): 40 notes/40 new cards in deck "Sample Deck", note type "Basic" (2 fields, 1 template), tag `sample`, no media, `ls=0`.
4. **Richer fixture strongly recommended.** One `.apkg` containing:
   - a note type with ≥ 2 templates (bury/suspend-note submenus need siblings: `Reviewer.java:555-574`);
   - cloze and `{{type:}}` templates (type-answer mode, `AbstractFlashcardViewer.java:657-712`);
   - `[sound:]` mp3 from `_fixtures/Music`, an image from `_fixtures/Pictures`, a video file (VideoPlayer);
   - LaTeX, sub-decks, a filtered deck, suspended/marked/buried cards, tags;
   - cards with review history and due reviews (StudyOptions congrats, limits snackbar, statistics charts).
5. **Account.** An AnkiWeb test account (or a custom sync server) plus network unlocks the sync area and, after one sync, the schema-change confirmations (G10).
6. **Optional environment.** Place the home-screen widget; set "Notify when" (`minimumCardsDueForNotification` < 1000000) for NotificationService; install ColorDict or a dictionary app and set pref `dictionary`; a TTS engine; a camera; a tablet (xlarge) AVD for the `mFragmented` layout; low disk for the no-space dialogs; SD eject/mount broadcasts.
   - The custom actions `com.ichi2.anki.action.MEDIA_EJECT/MOUNT` are not protected, so `adb shell am broadcast` reaches the dynamic receivers (INFERRED).

---

## 3. Screens and navigation

### 3.1 Navigation mechanisms (SRC)

- **Explicit intents.** Almost every screen change is `startActivity*` or `startActivityForResult*` through the `AnkiActivity` wrappers (`anki/AnkiActivity.java:153-209`), with request codes:
  - DeckPicker: `ADD_NOTE=12`, `SHOW_STUDYOPTIONS=11`, `LOG_IN_FOR_SYNC=6`, `REQUEST_PATH_UPDATE=1` (`DeckPicker.java:126-135`);
  - `AnkiActivity.REQUEST_REVIEW=901` (`AnkiActivity.java:46`);
  - NavigationDrawerActivity: `REQUEST_PREFERENCES_UPDATE=100`, `REQUEST_BROWSE_CARDS=101`, `REQUEST_STATISTICS=102` (`NavigationDrawerActivity.java:58-60`).
  - Results flow back through `onActivityResult`: `DeckPicker.java:634-677`, `NavigationDrawerActivity.java:210-237`, `AbstractFlashcardViewer.java:1060-1103`, `Reviewer.java:533-548`, `StudyOptionsFragment.java:393-446`, `CardBrowser.java:686-717`, `NoteEditor.java:1018-1065`.
- **Back to home.** `Intent(DeckPicker)` with `CLEAR_TOP|NEW_TASK`, from `AnkiActivity.onCollectionLoadError` (`AnkiActivity.java:266-271`), `dismissSimpleMessageDialog(reload)` (453-461) and drawer "Decks" (`NavigationDrawerActivity.java:257-261`).
- **Task restart.** `restartActivityInvalidateBackstack` uses a TaskStackBuilder (`compat/CompatV11.java:24-31`), after a night-mode switch or a theme/path change (`NavigationDrawerActivity.java:93-103, 210-237`). `AnkiActivity.restartActivity` (471-479).
- **Fragments.**
  - `StudyOptionsFragment`: in `StudyOptionsActivity` (`StudyOptionsActivity.java:50-58`) or embedded in DeckPicker on tablets (`DeckPicker.java:1650-1655`).
  - `Preferences$SettingsFragment` via `EXTRA_SHOW_FRAGMENT` + `subscreen` (`compat/CompatV11.java:38-46`; headers `res/xml/preference_headers.xml:24-73`).
  - `CardTemplateEditor$CardTemplateFragment` and the `Statistics` fragments in FragmentPagerAdapters.
- **Dialogs.**
  - `AnkiActivity.showDialogFragment` adds the dialog on the back stack under tag "dialog" (337-351); `dismissAllDialogFragments` pops it (464-467).
  - `showAsyncDialogFragment` (360-373) falls back to a stored `DialogHandler` message plus a notification when the activity is stopped.
- **DialogHandler pump.** A static stored message is replayed in every `AnkiActivity.onResume` (82), and handled with casts to `DeckPicker` (`DialogHandler.java:56-117`). Hazard: a stored message replayed by another AnkiActivity throws ClassCastException (INFERRED, not reproduced).
- **Drawer.** `NavigationView` (`res/menu/navigation_drawer.xml`) in `DeckPicker`, `StudyOptionsActivity`, `CardBrowser`, `Statistics`, `AbstractFlashcardViewer` (`initNavigationDrawer` calls at `DeckPicker.java:372`, `StudyOptionsActivity.java:44`, `CardBrowser.java:347`, `Statistics.java:87`, `AbstractFlashcardViewer.java:857`). `Previewer` disables the drawer swipe and shows a back arrow (`Previewer.java:39-41`).
- **Not used:** ActionMode/CAB, `registerForContextMenu`, bottom sheets, navigation graphs, Jetpack (grep). "Context menus" are DialogFragments shown on long-press.

### 3.2 Windows, how they are reached, and their modes

| Window | Reached from (SRC) | Modes that change active handlers / menu items (SRC) |
|---|---|---|
| `IntentHandler` (invisible) | Launcher, VIEW, DO_SYNC (`M:80-131`) | Action MAIN / VIEW-ok / VIEW-error (error dialog `IntentHandler.java:110-124`) / DO_SYNC |
| `DeckPicker` | IntentHandler, drawer, notifications, CLEAR_TOP returns | **no collection** vs open (`DeckPicker.java:357, 415-435`; menu suppressed `505-510`). **FAB** collapsed vs expanded (`777-779`). **Drawer** open (`775-776`). **Undo** visible iff `undoAvailable() && !mFragmented` (`511-517`). Sync/filtered/check items disabled without SD (`523-532`). Import/export/restore hidden on Chromebook (`534-538`). **Tablet** `mFragmented` (`365-367`). **Snackbar** shown after a deck tap (`1745-1800`). **Deck state** decides the tap result (`1717-1805`). Progress dialogs during tasks; the sync progress dialog has a Back handler (`1321-1360`). |
| `StudyOptionsActivity` + `StudyOptionsFragment` | `DeckPicker.openStudyOptions` (`1695-1706`), new filtered deck (`589`) | Content STUDY / CONGRATS / EMPTY (`StudyOptionsFragment.java:560-590`). **Filtered deck**: rebuild/empty shown, custom study hidden (`346-356`). Tablet-only rename/delete/export (`360-368`). Unbury iff `haveBuried` (`370`). Undo iff `undoAvailable` (`372-376`). Start → Reviewer, or the custom-study menu in CONGRATS (`125-131`). |
| `Reviewer` (`AbstractFlashcardViewer`) | `DeckPicker.openReviewer` (`2128-2132`), StudyOptions Start (`StudyOptionsFragment.java:227-238`; phone: `FLAG_ACTIVITY_FORWARD_RESULT` and finish), `CustomStudyDialog.java:485` | **Loading** (Loader → `onCollectionLoaded` → `ANSWER_CARD(null)`, `Reviewer.java:97-121`). **Question** vs **answer** (`sDisplayAnswer`; `displayCardQuestion` 1914, `displayCardAnswer` 1991, ease buttons 1562-1663). **Type-answer** field present iff the template has `{{type:}}` (657-712, 1678-1710). **Whiteboard** enabled/visible (`Reviewer.java:444-488`; the touch listener switches between whiteboard and gestures at 463-471). **Gestures** pref on/off (`AnkiDroidApp.initiateGestures` 305-318; `MyGestureDetector` 2661-2760; `executeCommand` 2487-2580). **Fullscreen** mode 0/1/2 (`Reviewer.java:82-95`). Bury/suspend **submenus** iff the note has eligible siblings (`Reviewer.java:555-574, 576-656`). Menu items hidden by custom-button prefs (`setCustomButtons` 237-247) or for a filtered deck (deck options hidden, 302-304). Timer and auto-advance (`mShowAnswerTask/mShowQuestionTask` 1861-1880). Leaves: NoteEditor edit (1183-1190) and add (`Reviewer.java:230-234`), DeckOptions (208-211), CardBrowser via drawer (508-519), VideoPlayer, links (1458-1550). `closeReviewer` (2593-2607) returns `RESULT_NO_MORE_CARDS` and similar. |
| `Previewer` | CardBrowser context "details" (`CardBrowser.java:206-211`), CardTemplateEditor preview (`CardTemplateEditor.java:478-506`) | Question/answer; no gestures (`Previewer.java:85-86`); no ease buttons (69-76) |
| `CardBrowser` | Drawer, DeckPicker/Reviewer `openCardBrowser` | **Loading** vs list (search task `794-816`; render-on-scroll `1139-1174`). **Search** expanded/collapsed (`580-620`). "Save search" visible iff the query is non-empty (600). "My searches" visible iff saved searches exist (578). Deck and column spinners (`372-482`). Item tap → NoteEditor edit (485-497). Long-press → context menu (499-512). |
| `NoteEditor` | DeckPicker FAB (`840-844`), Reviewer (edit/add), CardBrowser (edit/add), NoteEditor copy card (`839-849`), external SEND/CREATE_FLASHCARD | **Add** vs **edit** (`mAddNote`, `NoteEditor.java:363-415`; menu `801-823`). **Edit-model** (type changed → remap buttons, `1505-1512, 1592-1640`). Copy card enabled iff a field is non-empty (811-821). Unsaved changes → discard dialog (`625-654, 907-930`). |
| `MultimediaEditFieldActivity` | NoteEditor field media popup (`NoteEditor.java:1129-1184, 1235-1241`) | Field type **text / image / audio** (`recreateEditingUi` 116-147; the menu switches type 161-193). Audio needs RECORD_AUDIO (128-134). |
| `TranslationActivity`, `LoadPronounciationActivity` | Text-field buttons (`BasicTextFieldController.java:123-200, 364-400`) | Idle vs busy (ProgressDialog); offline → toast (`TranslationActivity.java:196-201`) |
| `ModelBrowser` | DeckPicker menu (`DeckPicker.java:610-614`) | Loading vs list (COUNT_MODELS, `ModelBrowser.java:237-252`) |
| `ModelFieldEditor` | ModelBrowser item (`ModelBrowser.java:271-281`) | One mode; field context menu on tap (`ModelFieldEditor.java:135-141`) |
| `CardTemplateEditor` | NoteEditor "Cards" (`NoteEditor.java:353-359, 1001-1014`), ModelBrowser context "Templates" (`ModelBrowser.java:549-553`) | Loading vs loaded (`CardTemplateEditor.java:187-200`). Tab = template index. Changed vs unchanged (Up → discard dialog, `171-185, 250-280`). Delete refused when there is only 1 template (`465-469`). |
| `Preferences` | Drawer (`NavigationDrawerActivity.java:273-278`), DeckPicker path gate, subscreen links | Headers vs subscreen (`EXTRA_SHOW_FRAGMENT`). Subscreens general/reviewing/appearance/gestures/advanced/custom_buttons/custom_sync_server/advanced_statistics (`Preferences.java:233-372`). Collection prefs disabled when the collection is closed (`Preferences.java:434-437`). |
| `DeckOptions` / `FilteredDeckOptions` | Deck context menu (`DeckPicker.java:1889-1903`), StudyOptions (`StudyOptionsFragment.java:294-302, 138-153`), Reviewer, CustomStudyDialog (`CustomStudyDialog.java:125-131`) | Nested PreferenceScreens (`res/xml/deck_options.xml`): options group, new, reviews, lapses, general/description. Filtered: `res/xml/cram_deck_options.xml`. |
| `Statistics` | Drawer "Statistics" (`NavigationDrawerActivity.java:265-269`) | Loading vs loaded. Deck = whole collection vs one deck (`Statistics.java:242-260`). Period month/year/all (204-240). Tab 0-8 (287-337). |
| `MyAccount` | Sync error dialog "Log in", Settings "Sync account" | **Logged out** (login form) vs **logged in** (`MyAccount.java:57-98`). Login in progress. |
| `Info` | Advanced settings "About" | TYPE_ABOUT only in this build (`Info.java:60-160`) |
| `VideoPlayer` | Reviewer | One mode |

**DialogFragments** (`anki/dialogs/*` + `multimediacard/activity/PickStringDialogFragment`):
- DeckPicker family: `DeckPickerContextMenu`, `DeckPickerConfirmDeleteDeckDialog`, `DeckPickerExportCompleteDialog`, `DeckPickerNoSpaceLeftDialog`, `DeckPickerBackupNoSpaceLeftDialog`, `DatabaseErrorDialog` (10 types, `DatabaseErrorDialog.java:27-36`), `MediaCheckDialog` (2), `ImportDialog` (4), `ExportDialog`, `SyncErrorDialog` (9, `SyncErrorDialog.java:12-20`).
- Study: `CustomStudyDialog` (menus 0-2, inputs ≥ 100).
- Browser and editor: `CardBrowserContextMenu`, `CardBrowserOrderDialog`, `CardBrowserMySearchesDialog` (list/save), `TagsDialog` (3 types), `NoteEditorRescheduleCard`.
- Note types: `ModelBrowserContextMenu`, `ModelEditorContextMenu`.
- Generic: `SimpleMessageDialog`, `ConfirmationDialog` (abstract, subclassed anonymously).
- Plain MaterialDialogs are built inline in DeckPicker (4), ModelBrowser (3), ModelFieldEditor (3), CardBrowser, NoteEditor, AbstractFlashcardViewer, ReadText, Lookup, DeckOptions, CardTemplateEditor, Preferences, IntentHandler, TagsDialog (add tag) and CompatV10 (API < 14 only).

**Menus and popups.**
- Options menus:
  - `deck_picker.xml` (10 items), `reviewer.xml` (14) with action-provider submenus `reviewer_bury.xml` and `reviewer_suspend.xml`;
  - `card_browser.xml` (8, SearchView action view), `note_editor.xml` (5), `card_template_editor.xml` (4, per fragment);
  - `model_browser.xml`, `model_editor.xml`, `anki_stats.xml` (time submenu), `activity_edit_text.xml` (4).
- Toolbar menus: `study_options_fragment.xml` (9, `StudyOptionsFragment.java:186, 287-340`) and `tags_dialog_menu.xml` (filter SearchView/add/select-all).
- Drawer: `navigation_drawer.xml` (decks, browser, stats, night-mode switch, settings, help, feedback).
- PopupMenus: `popupmenu_multimedia_options.xml` (`NoteEditor.java:1145`) and the remap popup (`1192`).
- Spinners: DeckPicker has none. CardBrowser has 3, NoteEditor 2, Statistics 1, ModelBrowser 1 (in a dialog), TranslationActivity 2, LoadPronounciationActivity 1.

### 3.3 Candidate page list

The area column refers to section 6. `@X` marks variants that agents should model as `S_PAGE@X` (same window, different handlers or continuation). Base pages: 140, of which 19 are `_PAUSED` pseudo pages.

| Page | Description | Window class | Mode predicate | Area |
|---|---|---|---|---|
| **Pseudo / outside** |||||
| S_ENTRY | Outside the app: launcher, file manager/browser (VIEW .apkg), share sheet (SEND text), Tasker (DO_SYNC), API client app (provider) | – | – | PL |
| S_EXIT | App finished; the process may survive with statics (`CollectionHelper` singleton, `DialogHandler.sStoredMessage`, `Hooks.sInstance`) | – | – | PL |
| S_SYS_PERMISSION | System runtime-permission dialog (@STORAGE `DeckPicker.java:450`, @AUDIO `MultimediaEditFieldActivity.java:130-133`) | packageinstaller | permission not granted | PL |
| S_OTHER_APP | Another app in front (@BROWSER custom tab or ACTION_VIEW, @MARKET, @EMAIL, @APP_SETTINGS, @GALLERY, @CAMERA, @COLORDICT, @DICTIONARY) | external | – | PL |
| S_HOME_WIDGET | Launcher with the AnkiDroid small widget (tap → IntentHandler MAIN, `AnkiDroidWidgetSmall.java:164-169`) | AnkiDroidWidgetSmall | widget placed | PL |
| S_NOTIFICATION | AnkiDroid notification in the shade (content intent → DeckPicker) | NotificationService / `AnkiActivity.showSimpleNotification` | posted | PL |
| **Platform** |||||
| S_INTENT_IMPORT_ERROR | "Not a valid apkg" dialog; OK finishes | IntentHandler MaterialDialog | VIEW validation failed (`IntentHandler.java:110-124`) | PL |
| S_DRAWER | Navigation drawer open (@DECKPICKER, @STUDYOPTIONS, @BROWSER, @STATS, @REVIEWER): decks/browser/stats/night mode/settings/help/feedback | NavigationView | `isDrawerOpen()`; tapping the checked item does nothing (`NavigationDrawerActivity.java:252-255`) | PL |
| S_DLG_SIMPLE_MESSAGE | Message with OK (@RELOAD restarts DeckPicker) | SimpleMessageDialog | – | PL |
| S_DLG_CONFIRM | Confirm OK/Cancel; one variant per anonymous subclass: @EMPTY_CARDS, @RESET_PROGRESS, @CARDS_LOST, @DELETE_MODEL, @DELETE_FIELD, @DELETE_TEMPLATE, @UPGRADE_FULLSYNC, @FULLSYNC_{NOTETYPE,MODEL,FIELD,TEMPLATE} (sites in 5.2) | ConfirmationDialog + subclasses | caller-specific | PL (variants owned by the caller's area) |
| S_PROGRESS | Modal progress dialog (@IMPORT, @EXPORT, @CHECK_DB, @CHECK_MEDIA, @DELETE_DECK, @REPAIR, @REORDER, @EMPTY_CARDS) | StyledProgressDialog | task running | PL |
| S_CRASH_REPORT | ACRA crash report dialog | AnkiDroidCrashReportDialog | `reportErrorMode` ≠ "1" in this process + an exception report | PL |
| S_INFO_ABOUT | About page (WebView, Rate, Copy debug info) | Info | `infoType==0` (`Info.java:62`) | PL |
| **Home (DeckPicker and maintenance)** |||||
| S_DECKPICKER_NOCOL | Deck list empty, options menu suppressed; waiting for the permission result or behind an error | DeckPicker | `!colOpen` | HO |
| S_DECKPICKER | Deck list, toolbar menu, FAB collapsed (phone layout) | DeckPicker | colOpen ∧ ¬FAB ∧ ¬drawer ∧ ¬mFragmented | HO |
| S_DECKPICKER_FAB | FAB expanded: Add deck / Get shared decks / Add note | DeckPicker | `mActionsMenu.isExpanded()` | HO |
| S_DECKPICKER_SNACK | Snackbar with action: @LIMITS "Study more", @EMPTY_SCHED "Custom study", @EMPTY_DECK "Help" | DeckPicker | shown by `handleDeckSelection` (1745-1800) | HO |
| S_DECKPICKER_TABLET | Deck list + embedded StudyOptionsFragment (xlarge only) | DeckPicker | `mFragmented` | HO (fragment edges ST) |
| S_DLG_DECK_CONTEXT | Long-press deck menu: @NORMAL (rename, options, custom study, delete, export[, unbury]) / @FILTERED (rebuild, empty, rename, options, delete, export[, unbury]) | DeckPickerContextMenu | `isDyn`, `haveBuried` (`DeckPickerContextMenu.java:95-113`) | HO |
| S_DLG_NEW_DECK | New deck name | MaterialDialog (`DeckPicker.java:460-485`) | – | HO |
| S_DLG_NEW_FILTERED_DECK | New filtered deck name | MaterialDialog (569-592) | – | HO |
| S_DLG_RENAME_DECK | Rename deck | MaterialDialog (1925-1966) | – | HO |
| S_DLG_DELETE_DECK | Confirm deleting a deck with cards | DeckPickerConfirmDeleteDeckDialog | cnt > 0 ∧ did ≠ 1 (1972-2011) | HO |
| S_DLG_EXPORT | Export: include scheduling/media (@COLLECTION, @DECK) | ExportDialog | did null / set | HO |
| S_DLG_EXPORT_DONE | Export done: email or close | DeckPickerExportCompleteDialog | export path ≠ null | HO |
| S_DLG_IMPORT_HINT | "Put .apkg files in folder …" | ImportDialog type 0 | – | HO |
| S_DLG_IMPORT_SELECT | List of .apkg files | ImportDialog type 1 | `getImportableDecks` non-empty (else toast + cancel) | HO |
| S_DLG_IMPORT_ADD | Confirm import (add) | ImportDialog type 2 | path chosen / VIEW message | HO |
| S_DLG_IMPORT_REPLACE | Confirm replacing the collection | ImportDialog type 3 | file named `collection.apkg` | HO |
| S_DLG_DBCHECK_CONFIRM | Confirm check database | DatabaseErrorDialog 6 | – | HO |
| S_DLG_RESTORE_CONFIRM | Confirm restore from backup | DatabaseErrorDialog 7 | – | HO |
| S_DLG_RESTORE_LIST | Pick a backup | DatabaseErrorDialog 4 | backups exist | HO |
| S_DLG_DBERROR | Error dialogs (@LOAD_FAILED, @DB_ERROR, @ERROR_HANDLING, @REPAIR, @NEW_COLLECTION, @FULL_SYNC_FROM_SERVER, @CURSOR_LIMIT) | DatabaseErrorDialog 0,1,2,3,5,8,9 | broken collection or task DB error | HO |
| S_DLG_MEDIACHECK_CONFIRM | Confirm media check | MediaCheckDialog 0 | – | HO |
| S_DLG_MEDIACHECK_RESULTS | Results; "delete unused" if any | MediaCheckDialog 1 | CHECK_MEDIA done | HO |
| S_DLG_NO_SPACE | Not enough space for a backup | DeckPickerNoSpaceLeftDialog | low disk | HO |
| S_DLG_BACKUP_NO_SPACE | Last backup failed (no space) | DeckPickerBackupNoSpaceLeftDialog | pref `noSpaceLeft` | HO |
| **Sync and account** |||||
| S_DLG_SYNC_ERROR | @NOT_LOGGED_IN, @CONNECTION, @CONFLICT, @KEEP_LOCAL, @KEEP_REMOTE, @SANITY, @SANITY_LOCAL, @SANITY_REMOTE, @MEDIA | SyncErrorDialog | dialogType | SY |
| S_SYNC_PROGRESS | Sync progress; Back cancels (< 2 s) or asks | StyledProgressDialog + OnKeyListener (`DeckPicker.java:1321-1360`) | sync running | SY |
| S_DLG_SYNC_CANCEL | "Cancel sync?" | MaterialDialog (1345-1358) | cancellable ∧ > 2 s | SY |
| S_MYACCOUNT_LOGIN | Username/password, Log in, Reset password (browser), Sign up (custom tab) | MyAccount | `hkey` empty | SY |
| S_MYACCOUNT_LOGGEDIN | User name, Log out | MyAccount | `hkey` non-empty | SY |
| S_MYACCOUNT_BUSY | Logging in… | StyledProgressDialog | login running | SY |
| **Study and review** |||||
| S_STUDYOPTIONS | Deck overview, Start | StudyOptionsActivity+Fragment | content STUDY ∧ ¬dyn | ST |
| S_STUDYOPTIONS_CONGRATS | Nothing due now; Start opens the custom-study menu | same | `CONTENT_CONGRATS` | ST |
| S_STUDYOPTIONS_EMPTY | Empty normal deck | same | totalCards = 0 ∧ ¬dyn | ST |
| S_STUDYOPTIONS_FILTERED | Filtered deck: Rebuild/Empty in toolbar | same | `isDyn(selected)` | ST |
| S_DLG_CUSTOM_STUDY | Custom-study menu (@STANDARD, @LIMITS, @EMPTY_SCHED) | CustomStudyDialog id < 100 | `CustomStudyDialog.java:329-353` | ST |
| S_DLG_CUSTOM_STUDY_INPUT | Number input (@NEW, @REV, @FORGOT, @AHEAD, @RANDOM, @PREVIEW) | CustomStudyDialog id ≥ 100 | – | ST |
| S_REVIEWER_LOADING | Before the first card | Reviewer | mCurrentCard = null | ST |
| S_REVIEWER_Q | Question; Show answer; menu; gestures if enabled | Reviewer | ¬sDisplayAnswer | ST |
| S_REVIEWER_Q_TYPING | Question with the type-answer field focused | Reviewer | `{{type:}}` card ∧ field focused | ST |
| S_REVIEWER_A | Answer; ease buttons 1-4 | Reviewer | sDisplayAnswer | ST |
| S_REVIEWER_WHITEBOARD | Whiteboard shown (touch draws; undo erases strokes) | Reviewer + Whiteboard | mPrefWhiteboard ∧ mShowWhiteboard | ST |
| S_REVIEWER_SUBMENU | Bury/suspend drop-down (@BURY, @SUSPEND) | ActionProvider submenu | sibling cards eligible | ST |
| S_DLG_DELETE_NOTE | Confirm delete note | MaterialDialog (`AbstractFlashcardViewer.java:1239-1257`) | – | ST |
| S_DLG_TTS_LANG | Choose TTS language | MaterialDialog (`ReadText.java:89`) | pref `tts` | ST |
| S_DLG_LOOKUP_LEO | Leo dictionary language | MaterialDialog (`Lookup.java:110`) | pref `dictionary` = Leo | ST |
| S_PREVIEWER_Q | Preview question | Previewer | ¬sDisplayAnswer | ST |
| S_PREVIEWER_A | Preview answer | Previewer | sDisplayAnswer | ST |
| S_VIDEOPLAYER | Full-screen video | VideoPlayer | – | ST |
| **Browse and edit** |||||
| S_BROWSER_LOADING | Search/render tasks running | CardBrowser | SEARCH_CARDS running | ED |
| S_BROWSER | Card list; deck and column spinners; menu | CardBrowser | search collapsed | ED |
| S_BROWSER_SEARCH | SearchView expanded | CardBrowser | expanded | ED |
| S_BROWSER_DROPDOWN | Spinner list open (@DECK, @COLUMN1, @COLUMN2) | Spinner popup | – | ED |
| S_DLG_CARD_CONTEXT | Mark, suspend, delete, preview | CardBrowserContextMenu | – | ED |
| S_DLG_CARD_DELETE | Confirm delete note | MaterialDialog (`CardBrowser.java:185-205`) | – | ED |
| S_DLG_BROWSER_ORDER | Sort order | CardBrowserOrderDialog | – | ED |
| S_DLG_SAVE_SEARCH | Name the search | CardBrowserMySearchesDialog (save) | query non-empty | ED |
| S_DLG_MY_SEARCHES | Saved searches (tap runs, X removes) | CardBrowserMySearchesDialog (list) | saved filters exist | ED |
| S_DLG_TAGS | Tag picker (@ADD NoteEditor, @FILTER browser, @CUSTOM_STUDY); toolbar filter/add/select all; the options radio group is shown except in @ADD | TagsDialog | type 0/1/2 | ED |
| S_DLG_ADD_TAG | New tag name | MaterialDialog (`TagsDialog.java:202-215`) | – | ED |
| S_NOTEEDITOR_ADD | Add note: type/deck spinners, fields, tags, cards; Save | NoteEditor | mAddNote | ED |
| S_NOTEEDITOR_EDIT | Edit note: + Add card, Copy card, Reset progress, Reschedule | NoteEditor | ¬mAddNote | ED |
| S_NOTEEDITOR_REMAP | Edit note after choosing another note type: remap buttons | NoteEditor | type changed | ED |
| S_NOTEEDITOR_DROPDOWN | Spinner open (@TYPE, @DECK) | Spinner | – | ED |
| S_POPUP_FIELD_MEDIA | Field media popup: photo/audio/text | PopupMenuWithIcons | – | ED |
| S_POPUP_FIELD_REMAP | Remap popup | PopupMenu | remap mode | ED |
| S_DLG_DISCARD_NOTE | Discard unsaved changes? | MaterialDialog (`NoteEditor.java:916-930`) | unsaved changes | ED |
| S_DLG_RESCHEDULE | Reschedule in N days | NoteEditorRescheduleCard | edit mode | ED |
| S_MMEDIT_TEXT | Text field editor: clone, clear, translate, pronounce | MultimediaEditFieldActivity + BasicTextFieldController | TextField | ED |
| S_MMEDIT_IMAGE | Image field: gallery, camera, preview | + BasicImageFieldController | ImageField | ED |
| S_MMEDIT_AUDIO | Audio field: record, play, stop | + BasicAudioFieldController / AudioView | AudioField ∧ RECORD_AUDIO | ED |
| S_DLG_PICK_STRING | Choice list (@TRANSLATION_SOURCE, @CLONE_FIELD, @TRANSLATION_RESULT) | PickStringDialogFragment | – | ED |
| S_TRANSLATION | Glosbe translation: language spinners, Done | TranslationActivity | idle | ED |
| S_TRANSLATION_BUSY | Request running | ProgressDialog | online | ED |
| S_PRONUNCIATION | Pronunciation search | LoadPronounciationActivity | idle | ED |
| S_PRONUNCIATION_BUSY | Fetch/download running | ProgressDialog | online | ED |
| **Configuration (settings, deck options, note types)** |||||
| S_PREFS_HEADERS | Settings headers | Preferences | no fragment extra | CF |
| S_PREFS_GENERAL | General | Preferences+SettingsFragment | subscreen general | CF |
| S_PREFS_REVIEWING | Reviewing | same | reviewing | CF |
| S_PREFS_APPEARANCE | Appearance | same | appearance | CF |
| S_PREFS_GESTURES | Gestures | same | gestures | CF |
| S_PREFS_ADVANCED | Advanced (**@PATH_GATE** when DeckPicker opened it for `REQUEST_PATH_UPDATE`: closing ends the app) | same | advanced | CF |
| S_PREFS_CUSTOM_BUTTONS | Reviewer button visibility | same (new activity) | custom_buttons | CF |
| S_PREFS_SYNC_SERVER | Custom sync server | same (new activity) | custom_sync_server | CF |
| S_PREFS_ADV_STATS | Advanced statistics | same (new activity) | advanced_statistics | CF |
| S_DLG_PREF_LIST | ListPreference dialog (@key) | framework | – | CF |
| S_DLG_PREF_TEXT | EditTextPreference dialog (@deckPath, @syncBaseUrl, @syncMediaUrl, deck options @confAdd/@confRename/@desc, filtered @search/@limit) | framework | – | CF |
| S_DLG_PREF_SEEKBAR | SeekBarPreference dialog (@key) | ui/SeekBarPreference | – | CF |
| S_DLG_PREF_NUMBER | NumberRangePreference/StepsPreference/CustomDialogPreference dialog (@key) | preferences/* | – | CF |
| S_DECKOPTIONS | Deck options main | DeckOptions | – | CF |
| S_DECKOPTIONS_SUB | Nested screen (@GROUP, @NEW, @REVIEWS, @LAPSES, @GENERAL) | nested PreferenceScreen | – | CF |
| S_FILTEREDOPTIONS | Filtered deck options | FilteredDeckOptions | – | CF |
| S_MODELBROWSER_LOADING | Note types loading | ModelBrowser | COUNT_MODELS running | CF |
| S_MODELBROWSER | Note type list | ModelBrowser | loaded | CF |
| S_DLG_MODEL_CONTEXT | Templates / rename / delete | ModelBrowserContextMenu | – | CF |
| S_DLG_ADD_MODEL | Choose base type (spinner) | MaterialDialog (`ModelBrowser.java:309-396`) | – | CF |
| S_DLG_ADD_MODEL_NAME | Name the new type | MaterialDialog | – | CF |
| S_DLG_RENAME_MODEL | Rename note type | MaterialDialog (497-535) | – | CF |
| S_FIELDEDITOR | Field list | ModelFieldEditor | – | CF |
| S_DLG_FIELD_CONTEXT | Reposition, sort by, rename, delete | ModelEditorContextMenu | – | CF |
| S_DLG_FIELD_INPUT | @ADD, @RENAME, @REPOSITION | MaterialDialog (`ModelFieldEditor.java:175-420`) | – | CF |
| S_TEMPLATEEDITOR_LOADING | Before the collection loads | CardTemplateEditor | – | CF |
| S_TEMPLATEEDITOR | Tab per template (front/styling/back); fragment menu preview/save/add/delete | CardTemplateEditor + CardTemplateFragment | tab i | CF |
| S_DLG_DISCARD_TEMPLATE | Discard template changes? | MaterialDialog (`CardTemplateEditor.java:255-280`) | modelHasChanged | CF |
| S_DLG_HEBREW_FONT | Hebrew font hint | `Preferences.onCreateDialog` | unreachable on API ≥ 16 (5.2) | CF |
| **Statistics** |||||
| S_STATS_LOADING | Charts computing | Statistics | AsyncTasks running | SA |
| S_STATS | 9-tab pager (@OVERVIEW, @FORECAST, @REVIEW_COUNT, @REVIEW_TIME, @INTERVALS, @HOURLY, @WEEKLY, @ANSWER_BUTTONS, @CARD_TYPES) | Statistics + fragments | tab k; deck/collection; period | SA |
| S_STATS_DROPDOWN | Deck spinner open | Spinner | – | SA |
| S_STATS_PERIOD | Period submenu | `anki_stats.xml` submenu | – | SA |
| **Paused pseudo pages (hidden in the viewer)** |||||
| S_DECKPICKER_PAUSED, S_STUDYOPTIONS_PAUSED, S_REVIEWER_PAUSED, S_PREVIEWER_PAUSED, S_BROWSER_PAUSED, S_NOTEEDITOR_PAUSED, S_MMEDIT_PAUSED, S_TRANSLATION_PAUSED, S_PRONUNCIATION_PAUSED, S_MODELBROWSER_PAUSED, S_FIELDEDITOR_PAUSED, S_TEMPLATEEDITOR_PAUSED, S_PREFS_PAUSED, S_DECKOPTIONS_PAUSED, S_FILTEREDOPTIONS_PAUSED, S_STATS_PAUSED, S_MYACCOUNT_PAUSED, S_INFO_PAUSED, S_VIDEOPLAYER_PAUSED | Activity in the back stack or app in the background | – | – | owner of the activity |

---

## 4. Framework mechanisms that need framework, async or lifecycle edges

Not used anywhere (grep over all sources): LiveData/ViewModel, RxJava, WorkManager, JobScheduler, AlarmManager, data binding, the Storage Access Framework (`ACTION_OPEN_DOCUMENT`/`GET_CONTENT`), and `addJavascriptInterface`.

| Mechanism | Main app classes (SRC) | Modeling note |
|---|---|---|
| **Async engine `DeckTask`** (serial AsyncTask chain) | `async/DeckTask.java`: 34 task types (68-101); `launchDeckTask` 129-134; `doInBackground` waits for the previous task, skips everything except REPAIR when `getColSafe` is null (203-232), then dispatches with `switch(mType)` to `doInBackgroundX` (233-336); `onPreExecute`/`onProgressUpdate`/`onPostExecute`/`onCancelled` forward to the `Listener` (344-370); the `TaskListener` adapter (1276-1314). Listeners are anonymous classes in callers (`new DeckTask.TaskListener()`/`Listener()` per file): DeckPicker 11, CardBrowser 5, AbstractFlashcardViewer 3, CardTemplateEditor 2, ModelBrowser 2, and 1 each in NoteEditor, ModelFieldEditor, DeckOptions, StudyOptionsFragment, CustomStudyDialog, UIUtils | Use variants `DeckTask.doInBackground@<TASK_TYPE>` and `<Listener>.onPostExecute` as ASYNC edges. The task body belongs to A8, the listener to the caller's area. `UIUtils.saveCollectionInBackground` (SAVE_COLLECTION) runs from many `onStop` methods. |
| `async/Connection` (login/sync AsyncTask) | `login` 160-164, `sync` 166-171, `doInBackground` 173, `onPostExecute` 138; `isOnline` 475-484; listeners `DeckPicker.mSyncListener` (1291-1555), `MyAccount.loginListener` (221-273) | ASYNC + env (network + account) |
| Loader (`AsyncTaskLoader`) | `AnkiActivity.startLoadingCollection` → `CollectionLoader` → `onLoadFinished` → `onCollectionLoaded` or `onCollectionLoadError` (`AnkiActivity.java:255-297`; `async/CollectionLoader.java`). Used by AbstractFlashcardViewer (859), CardBrowser (348), NoteEditor (309), CardTemplateEditor (157), ModelBrowser (191), ModelFieldEditor (75), Statistics (88) | LIFECYCLE → ASYNC → `onCollectionLoaded@<Activity>`. On failure → DeckPicker (CLEAR_TOP). |
| Other AsyncTasks | `widget/WidgetStatus$UpdateDeckStatusAsyncTask` (79-136); `anki/stats/AnkiStatsTaskHandler` `CreateChartTask` 81, `CreateStatisticsOverview` 132, `DeckPreviewStatistics` 186 (the DeckPicker summary line); `LoadPronounciationActivity$BackgroundPost` 192, `$DownloadFileTask` 245; `TranslationActivity$BackgroundPost` 178; `libanki/hooks/ExternalHookLoader$PrepareDexTask` 114 (dead) | ASYNC |
| Threads and Handlers | `BackupManager` thread (`BackupManager.java:174`); `StudyOptionsFragment` full-new-count thread + `runOnUiThread` (618-640); AbstractFlashcardViewer: `mHandler`/`longClickHandler`/runnables (349-380), `removeChosenAnswerText` (823-831), show-answer/question timeouts (1861-1880, `postDelayed` 1949/2033), scroll handler (2645-2660), `mFullScreenHandler` (2763-2781); `ReadText` handler (134-140); `Leech` hook `runOnUiThread` (`libanki/hooks/Leech.java:46`); `DialogHandler` (Handler) | ASYNC/FRAMEWORK. The timeouts need prefs `timeoutAnswer*`. |
| Persisted dialog messages | `DialogHandler.storeMessage` (122-127), `readMessage` (130-136) from `AnkiActivity.onResume` (82). Writers: IntentHandler (148-178), `AnkiActivity.showAsyncDialogFragment` fallback (360-373) | Cross-activity edge with `needs_state` ("message stored") |
| RecyclerView adapter | `anki/widgets/DeckAdapter.java`: `onCreateViewHolder` 155, `onBindViewHolder` 162 (registers the click, long-click, counts and expander listeners 182-216), `getItemCount` 220, `buildDeckList` 144; `DividerItemDecoration`; `dialogs/TagsDialog$TagsArrayAdapter` (+ `TagsFilter.performFiltering/publishResults`, Filter framework) | REGISTER happens in `onBindViewHolder`; FRAMEWORK edges from `notifyDataSetChanged` (`DeckPicker.java:205, 222`) |
| ListView / Spinner adapters | `CardBrowser$MultiColumnListAdapter` (BaseAdapter, 1176-1305) and `RenderOnScroll` (1139-1174, launches RENDER_BROWSER_QA); `ModelBrowser$DisplayPairAdapter`; `widgets/DeckDropDownAdapter` (CardBrowser and Statistics spinners); NoteEditor spinners (ArrayAdapter); `CardBrowserMySearchesDialog$MySearchesArrayAdapter`; MaterialDialog `items`/`itemsIds` list callbacks | `getView`/`getCount` are FRAMEWORK. Whether `getItem`/`getItemId` are called by the framework is UNVERIFIED (check AbsListView/Spinner source). |
| ViewPager / FragmentPagerAdapter | `Statistics$SectionsPagerAdapter` (287-337; offscreen limit 8 at 124, so all 9 fragments are created; `getItemPosition` calls `checkAndUpdate`); `CardTemplateEditor$TemplatePagerAdapter` (302-362, `POSITION_NONE`); `ui/SlidingTabLayout`/`SlidingTabStrip` (tab click → `setCurrentItem`) | FragmentPagerAdapter hides non-primary fragment menus, so only the visible template's `setHasOptionsMenu` menu is active (`CardTemplateEditor.java:420`; FW-MEMORY) |
| Options menus | 14 menu XMLs (3.2); `invalidateOptionsMenu` on every new card (`Reviewer.java:251-252` comment); drawer open/close (`NavigationDrawerActivity.java:108-120`); ActionProvider submenus (`Reviewer.java:576-656`) | `onOptionsItemSelected@<MODE>`. `ActionBarDrawerToggle.onOptionsItemSelected` consumes `android.R.id.home` first in drawer activities (FW-MEMORY), see 5.4. |
| Started services | `services/NotificationService` (`onStartCommand` 54-89, `START_STICKY`, `onBind` returns null 93); `widget/AnkiDroidWidgetSmall$UpdateService` (`onStart`, `onBind`); both started from `WidgetStatus$UpdateDeckStatusAsyncTask.onPostExecute` (`WidgetStatus.java:102-116`) | `WidgetStatus.update` runs from many `onStop` methods (DeckPicker 738-746, Reviewer, StudyOptionsActivity …) and `AnkiDroidWidgetSmall.onUpdate` |
| Bound service | Chrome Custom Tabs: `AnkiActivity.onStart/onStop` bind/unbind (`AnkiActivity.java:65-74`) → `compat/customtabs/ServiceConnection.onCustomTabsServiceConnected` (36-39) → `CustomTabActivityHelper.onServiceConnected` (121); `mayLaunchUrl` (110); `CompatV16.openUrl` → `openCustomTab` (`compat/CompatV16.java:77-87`) with fallback `CustomTabsFallback` (ACTION_VIEW) | FRAMEWORK; env: Chrome installed (Monkey and APE both hit `ServiceConnection`) |
| Broadcast receivers | Manifest: `SdCardReceiver` (MEDIA_EJECT/MOUNTED → custom broadcasts), `AnkiDroidWidgetSmall` (`onUpdate/onEnabled/onDisabled/onReceive`). Dynamic receivers for the custom MEDIA_EJECT/MOUNT: DeckPicker (1670-1688), AbstractFlashcardViewer (1125-1140), NoteEditor (890-905), CardBrowser (1318-1333), DeckOptions (760-775), FilteredDeckOptions (501-516); widget mount receiver (`AnkiDroidWidgetSmall.java:101-133`) | SYSTEM edges (SD eject/mount) |
| ContentProvider | `provider/CardContentProvider`: `getType` 161, `query` 208, `update` 416, `delete` 673, `bulkInsert` 710, `insert` 812; permission check 1303-1308 | Only external callers. ENTRY from S_ENTRY, with the guard "caller holds `READ_WRITE_DATABASE`" |
| Database layer | `libanki/DB` (SQLite wrapper; reflection on Cursor getters `DB.java:214`), `Storage` (create/open/upgrade), `Collection`, `Sched` (**reflection**: `getDeclaredMethod("_cntFnNew"/"_cntFnRev"/"_deckNewLimitSingle"/"_deckRevLimitSingle")` 564-565, 698, 1197, 1225-1226; `invoke` 337-353, 706), `Decks`, `Models`, `Media` (separate media DB), `Tags`, `Finder` (search), `Note`, `Card`; app-side `anki/MetaDB` (its own SQLite for languages, whiteboard state, widget counts) | CALL edges are mostly mechanical. Reflection targets need explicit edges. |
| Hooks registry | `libanki/hooks/Hooks` (constructor installs FuriganaFilters, HintFilter, LaTeX, Leech, plus pref-gated HebrewFixFilter, ChessFilter, AdvancedStatistics: 45-64; `addHook` 73; `runHook` 114; `runFilter` 138). Settings toggle filters at runtime (`Preferences.java:469-490`) | Dispatch keyed by string → model as `Hooks.runFilter@<hookName>` → `X.runFilter` |
| WebView | Card WebView: `AbstractFlashcardViewer.createWebView` (1435-1550). `shouldOverrideUrlLoading` handles `playsound:`, `file`/`data:`, `typeblurtext:`, `typeentertext:`, `signal:typefocus`, `intent:`/`android-app:`, other URLs → `openUrl`. `AnkiDroidWebChromeClient.onJsAlert` (2583-2591). `MyWebView` (2614-2659, `onScrollChanged`). Info WebView + WebChromeClient (`Info.java:79-87`) | FRAMEWORK edges from page content: needs cards with sound links, type-answer fields, links |
| External pickers and intents (no SAF) | Gallery `ACTION_PICK` and camera `ACTION_IMAGE_CAPTURE` (`BasicImageFieldController.java:100-127`) → result via `MultimediaEditFieldActivity.onActivityResult` (312-319) → `controller.onActivityResult` (157-180); ColorDict (`BasicTextFieldController.java:364-390`); dictionary apps (`Lookup`); email `ACTION_SEND` (`DeckPicker.emailFile` 1627-1645); Play Store, browser; app-details settings (`DeckPicker.java:689-693`) | INTENT/RESULT through S_OTHER_APP |
| Runtime permissions | `ActivityCompat.requestPermissions` → `onRequestPermissionsResult` (`DeckPicker.java:450, 680-696`; `MultimediaEditFieldActivity.java:130-133, 322-327`) | FRAMEWORK via S_SYS_PERMISSION. Baseline: pre-granted, so never fired. |
| Notifications | `AnkiActivity.showSimpleNotification` (410-445, content PendingIntent → DeckPicker; cancelled in `onResume` 80); `NotificationService` notification (content → DeckPicker) | S_NOTIFICATION → DeckPicker |
| Home-screen widget | `AnkiDroidWidgetSmall` + `UpdateService.buildUpdate` (RemoteViews; click → IntentHandler MAIN, 164-169) | Outside the app package |
| Preferences framework | `ui/AppCompatPreferenceActivity` (base). Headers and `SettingsFragment` (`Preferences.java:783-815`; `onSharedPreferenceChanged` → `updatePreference` switch on key 455-574). `OnPreferenceChangeListener`/`ClickListener` (`Preferences.java:248, 262, 285, 312, 327, 337, 347`). Preference intents in XML. Custom preferences inflated from XML: `NumberRangePreference`, `StepsPreference`, `CustomDialogPreference`, `SeekBarPreference`. **`DeckPreferenceHack`**: a custom SharedPreferences returned by `getSharedPreferences` (`DeckOptions.java:492-496`; `FilteredDeckOptions.java:344-348`); `Preference.persist*` → `Editor.commit` switches on key and launches DeckTask CONF_*/REORDER (`DeckOptions.java:150-336`) | FRAMEWORK edges from preference widgets; "change listener fires only on change" (GRAPH_PROMPT item 8) applies to `onSharedPreferenceChanged` |
| Text, keys and IME | `CardTemplateEditor` TextWatcher (396-417); NoteEditor field watcher (`NoteEditor.java:1253`); answer field editor-action and key listeners (`AbstractFlashcardViewer.java:1689-1710`); SearchView query listeners (`CardBrowser.java:597-618`; `TagsDialog.java:229-243`); hardware keys (`Reviewer.onKeyUp` 331-394; `AbstractFlashcardViewer.onKeyDown/onKeyUp` 977-1022) | GUI edges for keyboard input (Monkey sends key events) |
| Gestures and touch | `MyGestureDetector` (`onFling`, `onDoubleTap`, `onSingleTapUp`, `onSingleTapConfirmed`: 2661-2760); touch layer listener (428-466); long-click → lookup (468-481); Whiteboard touch (`Reviewer.java:463-471`) | Guarded by pref `gestures` and the per-gesture prefs |
| Media and TTS | `libanki/Sound` (MediaPlayer), `multimediacard/AudioView` (MediaPlayer/MediaRecorder), `VideoPlayer` (SurfaceHolder callbacks 49-71), `ReadText` (TextToSpeech) | Env: audio files, microphone, TTS engine |
| Crash reporting | ACRA (`@ReportsCrashes`, `AnkiDroidApp.java:54-111`); `AnkiDroidCrashReportDialog` | Off in DEBUG (5.2) |

---

## 5. Unreachable-code candidates (evidence only, no final verdicts)

Method counts are from JaCoCo; M/A = methods hit by Monkey/APE.

### 5.1 Whole classes with no apparent caller (DEAD candidates, about 425 methods)

With the build- and hardware-gated classes from 5.2 (`ProductionCrashReportingTree` 10, crash dialog 6, `HebrewFixFilter` 8, Nook compat 2), the total is about 450 methods.

| Classes | Methods | M/A | Evidence |
|---|---|---|---|
| `com.ichi2.anki.api.*` (`AddContentApi` + `$CompatV1/$CompatV2`, `NoteInfo`, `Utils`, `BasicModel`, `Basic2Model`, `api.BuildConfig`) | 62 | 0/0 | Client library for third-party apps, compiled in through `compile project(":api")` (`AnkiDroid/build.gradle:69`). No app source references `com.ichi2.anki.api` (grep; the hits for "BasicModel" in `ModelBrowser`/`Storage`/`Models` are libanki's own `Models.addBasicModel`). |
| `FlashCardsContract` and inner classes | 13 | 0/0 | Only `CardContentProvider` references it, and only compile-time `String` constants, which javac inlines. The `<clinit>` methods that build `Uri` constants (`FlashCardsContract.java:116, 275, 281, 443`) never run; the other methods are private constructors. |
| `Manifest`, `Manifest$permission`; `BuildConfig.<init>` | 2 (+1) | 0/0 | Generated; never instantiated |
| `CustomExceptionHandler` | 10 | 0/0 | Only reference is a commented-out line (`AnkiDroidApp.java:249`) |
| `utils/Base64` and inner classes | 42 | 0/0 | No reference (grep `Base64.` and the import) |
| `utils/HttpUtility` | 2 | 0/0 | No reference |
| `utils/MethodLogger` | 3 | 0/0 | Called only under `if (DEBUG)` with `private static final boolean DEBUG = false` (`async/BaseAsyncTask.java:27, 37-39, 40-97`). javac removes constant-false blocks. |
| `libanki/hooks/ExternalHookLoader` (+ `$PrepareDexTask`) | 7 | 0/0 | No reference |
| `libanki/importer/TextImporter`, `NoteImporter` | 7 | 0/0 | `TextImporter` is never referenced; `NoteImporter` only by `TextImporter` |
| `libanki/CardStats` | 2 | 0/0 | No reference |
| `multimediacard/impl/NoteFactory`; `multimediacard/test/Mock*` (3 classes, in the **main** source set) | 2 + 6 | 0/0 | No reference; `Mock*` appear only in comments (`LoadPronounciationActivity.java:204, 208`) |
| `compat/customtabs/KeepAliveService` | 3 | 0/0 | Not declared in the manifest (section 1) |
| wildplot `parsing/**` (`TopLevelParser`, `Expression`, `Term`, `Factor`, `Pow`, `Atom`, `AtomTypes/*`) | 98 | 0/0 | `new TopLevelParser` exists only inside `TopLevelParser.java:165`; no app or renderer instantiates it |
| wildplot renderers `FunctionDrawer`, `FunctionDrawer_y`, `ReliefDrawer` (+inner), `Integral`, `PointDrawer2D`, `XAxisHistoGram`, `YAxisHistoGram`, `XAxisBarGraph`, `YAxisBarGraph`, `LinesPoints`, `RelativeColorGradient`, `graphics/wrapper/BufferedImageWrap` | 165 | 0/0 | No `new X` anywhere. `LinesPoints` appears only in a comment (`wildplot/rendering/Lines.java:24-25`). `RelativeColorGradient` and `BufferedImageWrap` are used only by `ReliefDrawer`, and `GraphicsWrap.drawImage(BufferedImageWrap…)` (103). AnkiDroid uses only `BarGraph`, `LegendDrawable`, `Lines`, `PieChart`, `PlotSheet`, `XAxis`, `XGrid`, `YAxis`, `YGrid` and the wrappers (imports in `anki/stats/*`). |

### 5.2 Compiled in, but gated by build config, API level, hardware, account or network

| Code | Methods | Gate (evidence) |
|---|---|---|
| `AnkiDroidApp$ProductionCrashReportingTree` | 10 | Planted only if `!BuildConfig.DEBUG` (`AnkiDroidApp.java:155, 166`); this APK is debug → DEAD for this build |
| `dialogs/AnkiDroidCrashReportDialog` | 6 | ACRA disabled on every start in DEBUG (`AnkiDroidApp.java:159-160`). Reachable only if the user sets General → "Error reporting" (`Preferences.java:532-537` → `setAcraReportingMode`) and an exception report then happens in the same process (`AnkiDroidApp.sendExceptionReport` 243-269). ACRA showing the dialog is FW-MEMORY. |
| `libanki/hooks/HebrewFixFilter`, `Preferences.onCreateDialog` (Hebrew font dialog) | 8 + 1 | Pref `fixHebrewText` is removed from the screen on SDK ≥ 16 (`Preferences.java:723-725`). Can only be installed from a preset pref (`Hooks.java:55-57`); the dialog is shown only from the toggle (`Preferences.java:476-483`). |
| `Preferences.onSharedPreferenceChanged` (activity) and the bodies of `onPause`/`onResume` | 1 (+bodies) | The activity registers itself only when `!CompatHelper.isHoneycomb()` (`Preferences.java:164-188`). On API 27 the `SettingsFragment` listener is used instead (`Preferences.java:793-815`). Baseline: activity listener M-/A-, fragment listener M+/A+. |
| `compat/CompatV15NookHdOrHdPlus` | 2 | Chosen only on a Nook HD with SDK 15 (`compat/CompatHelper.java:33`) |
| `compat/CompatV10..V19` methods overridden by `CompatV21` | part of 74 | API 27 selects `CompatV21` (`CompatHelper.java:35`). Superclass methods that V21 overrides are unreachable. `else if (getSdkVersion() >= 12)` after `>= 11` can never be true (45-48). `CompatV10.supportAddContentMenu` (2 MaterialDialogs) is used only when the FAB menu is missing, i.e. API < 14 (`DeckPicker.java:394-405`). |
| `MultimediaEditFieldActivity.createSpareMenu` | 1 | Only on API ≤ 10 (`MultimediaEditFieldActivity.java:100-105`) |
| Info new-version screen; `DeckPicker` upgrade path (`upgradePreferences`, upgrade-triggered `integrityCheck`, `MSG_SHOW_FORCE_FULL_SYNC_DIALOG`) | branches + `upgradePreferences` | Release builds only / older `lastVersion` (2.2 G6) |
| `DeckPicker.onActivityResult` branches `REPORT_ERROR`, `SHOW_INFO_WELCOME` | branch | These request codes are never passed to `startActivityForResult` (`DeckPicker.java:126-135, 645-653`) |
| Sync: `async/Connection` (27), `libanki/sync/*` (91), `org.apache…ssl.*` (13), most of `SyncErrorDialog`, `MyAccount.saveUserInformation/logout`, the `DeckPicker.mSyncListener` result branches | ≈ 150+ | G9 (account + network) |
| Schema-change confirmations: anonymous `ConfirmationDialog` subclasses at `NoteEditor.java:751`, `ModelBrowser.java:451, 468`, `ModelFieldEditor.java:203, 258, 319, 382, 465`, `CardTemplateEditor.java:644, 679`, `DeckOptions.java:252-271`, plus the DeckTask catch blocks `DeckTask.java:1038-1200` | tens | G10 (needs `scm ≤ ls`, i.e. after a sync) |
| `libanki/importer/*` (41), `IntentHandler` VIEW helpers (`hasValidZipFile`, `copyFileToCache`, `sendShowImportFileDialogMsg`) | ≈ 45 | G8: a file must be present; external VIEW intent |
| `libanki/hooks/AdvancedStatistics` and inner classes | 99 | Pref `advanced_statistics_enabled` (`Hooks.java:61-63`; `Preferences.java:484-490`) and then Statistics. Monkey installed it but never reached Statistics; APE never enabled it. |
| `widget/AnkiDroidWidgetSmall*` | 12 | Widget placed on the home screen (outside the app package) |
| `CardContentProvider` CRUD (29 of 32) | 29 | External client holding `READ_WRITE_DATABASE` |
| Tablet path (`DeckPicker.loadStudyOptionsFragment`, `mFragmented` branches; StudyOptions rename/delete/export) | several | xlarge screen (`res/layout-xlarge/homescreen.xml`); never ran in the baseline (`loadStudyOptionsFragment` M-/A-) |
| Kindle (`Info.java:91-95`), Chromebook (`DeckPicker.java:534-538`; `BasicImageFieldController.java:132`; `BasicTextFieldController.java:171`), Kana/Emoji/scroll keys (`Preferences.java:686-700`) | branches | Hardware / device identity |
| `Lookup` (8), `ReadText` (10), VideoPlayer, translation/pronunciation | ≈ 100 | Pref + external app (dictionary, TTS engine), media files, network |

### 5.3 Method-level candidates with no call site found by name (lower bound)

A name scan was used: a method is listed if its name never appears as `name(` outside declarations in any Java source or XML resource (comments stripped), excluding framework-callback names. Same-name methods elsewhere hide true dead methods, so this list is incomplete; the bytecode extractor (tools v2) should decide.

- `anki/`: `FieldEditText.cleanText`; `BackupManager.isActivated`; `MetaDB.stripQuotes`, `resetDB`, `resetDeckLanguages`, `getLookupDictionary`, `storeLookupDictionary`.
- `multimediacard/`: `AudioView.createPlayerInstance`, `setRecordButtonVisible`.
- Glosbe JSON beans: `Response.get/setDest`, `get/setFrom`, `setPhrase`, `setTuc`; `Tuc.get/setAuthors`, `get/setMeaningId`, `setMeanings`, `setPhrase`. Gson fills fields, not setters (FW-MEMORY).
- `servicelayer/NoteService.updateJsonNoteFromMultimediaNote`; `async/DeckTask$TaskData.setCards`, `getComparator`.
- `compat/CompatHelper.isNook`; `compat/customtabs/CustomTabsHelper.getPackages`.
- `libanki/`: `Card.shouldShowTimer`, `Card.setCol`, `Sched.setToday`, `Sched.leechActionSuspend`, `Media.strip`, `Models.copy`, `Models.moveTemplate`, `Models.getTemplateNames`, `Collection.noteCount`, `Collection.emptyCardReport`, `Collection.setTimeLimit`, `Collection.getTimeLimit`, `Decks.collapseBrowser`, `Decks.renameForDragAndDrop`, `Decks.nameOrNone`, `Decks.setDeck`, `Utils.replaceLineBreak`, `Utils.printDate`, `Note.setItem`, `Tags.bulkRem`.
- `importer/`: `Importer.ts`, `Anki2Importer.setDupeOnSchemaChange`, `getDupes`, `getAdded`, `getUpdated`.
- `AdvancedStatistics$Review.writeLog`, `$ArrayUtils.createIntMatrix`, `nRows`, `nCols`.
- `themes/StyledProgressDialog.setProgressStyle`; `ui/SlidingTabLayout.setCustomTabView`; `utils/Threads.newSingleThreadChecker`, `newCurrentThreadChecker`, `newLazySingleThreadChecker`.
- About 75 wildplot setters/getters (e.g. `PlotSheet.setLogX/unsetLogX/setBorder`, `XAxis.setyOffset`, `YAxis.setLog`, `XGrid.setGridOnUpside`, `GraphicsWrap.getCanvas/dispose/unsetShadow`, `RectangleWrap.getRect`).

Flagged by the scan but **not dead** (framework or reflection callers; several ran in APE): `Sched._cntFnNew/_cntFnRev` (reflection, A+); `TagsFilter.performFiltering/publishResults` (Filter); `TextWatcher.before/afterTextChanged` in `CardTemplateEditor$CardTemplateFragment$1` and `NoteEditor$13`; `DeckAdapter.getItemCount`; `NumberRangePreference.getPersistedString/persistString`; `MySearchesArrayAdapter.areAllItemsEnabled`; `HttpSyncer$ProgressByteEntity.*` (called by Apache HttpClient during sync).

### 5.4 FRAMEWORK_ONLY candidates and dead branches inside reachable methods

- **Started services never bound:** `NotificationService.onBind`, `AnkiDroidWidgetSmall$UpdateService.onBind`; `KeepAliveService.*` (not in the manifest).
- **Home button in drawer activities:** `Reviewer.onOptionsItemSelected` `case android.R.id.home` (`Reviewer.java:131-134`) and `StudyOptionsActivity` home (`StudyOptionsActivity.java:66-75`) come after `getDrawerToggle().onOptionsItemSelected(item)`, which consumes Home while the drawer indicator is enabled (FW-MEMORY). APE: `home` case uncovered in Reviewer.
- **Adapter `getItem`/`getItemId`** of BaseAdapters (CardBrowser, DeckDropDownAdapter, ModelBrowser): UNVERIFIED; resolve against AbsListView/AdapterView source.
- **Permission dialog blocked:** `DeckPicker.onRequestPermissionsResult` with an empty result (the Monkey `-p` case) does nothing (681).
- **Snackbar callback bodies:** `DeckPicker.mSnackbarShowHideCallback` has `!isHoneycomb()` bodies (2151-2170), dead on API 27.
- **Legacy settings:** `Preferences.onCreate` legacy headers branch (116-125), dead on API ≥ 11.
- **Build-dependent provider check:** `CardContentProvider.hasReadWritePermission` takes the DEBUG branch (1303-1305). `knownRogueClient` matters only below API 23.

---

## 6. Decomposition into feature areas

Eight areas with one owner per source file. All 258 JaCoCo source files and all 648 JaCoCo classes are assigned exactly once (checked with a script over the JaCoCo `sourcefilename` of each class).

**Leftovers:**
- **25 synthetic classes** are compiled but not in JaCoCo: `$1` switch-map and accessor-tag classes such as `Statistics$2`, `Whiteboard$1`, `DeckTask$2`, `Collection$1`, `SlidingTabLayout$1`, `wildplot/parsing/*$1`, `ReliefDrawer$1`, `api/AddContentApi$1`. They have no app methods; each goes to the area of its outer class.
- **3 JacocoInstrument classes** are excluded.
- **Interfaces** with no method bodies (e.g. `Compat`, `IField`, `HookPlugin`, `ReviewerExt`, `ServiceConnectionCallback`, `PreferenceContext` (declared in `Preferences.java:82`), `wildplot/rendering/interfaces/*`) appear with 0 methods and go to the area of their file.
- `R` classes are not in the class dirs (AGP 3.2 keeps them in a separate R.jar).

| Area | Owns (files → classes) | Methods | Pages owned (3.3) | Entry edges from other areas | Notes |
|---|---|---|---|---|---|
| **A1 Platform & entry (PL)** | `anki/AnkiDroidApp`, `IntentHandler`, `AnkiActivity`, `NavigationDrawerActivity`, `CollectionHelper`, `CustomExceptionHandler`, `Info`, `UIUtils`, `MetaDB`, `BuildConfig`, `Manifest`, `FlashCardsContract`, `api/*`, `provider/*`, `receiver/*`, `services/*`, `widget/*`, `compat/**`, `themes/*`, `anim/ActivityTransitionAnimation`, `ui/{DividerItemDecoration,SlidingTabLayout,SlidingTabStrip}`, `anki/widgets/DeckDropDownAdapter`, `utils/{Base64,HttpUtility,LanguageUtil,MethodLogger,Threads,VersionUtils}`, `anki/exception/*`, `upgrade/*`, `dialogs/{AnkiDroidCrashReportDialog,DialogHandler,AsyncDialogFragment,SimpleMessageDialog,ConfirmationDialog,ContextMenuHelper}` (66 files, 111 classes) | **588** | S_ENTRY, S_EXIT, S_SYS_PERMISSION, S_OTHER_APP, S_HOME_WIDGET, S_NOTIFICATION, S_INTENT_IMPORT_ERROR, S_DRAWER(@host), S_DLG_SIMPLE_MESSAGE, S_DLG_CONFIRM (base), S_PROGRESS (base), S_CRASH_REPORT, S_INFO_ABOUT, S_INFO_PAUSED | From S_ENTRY (launcher, VIEW, DO_SYNC, widget, notification, provider) and from every area: base-class lifecycle, drawer GUI in all drawer hosts, generic dialogs, `WidgetStatus.update` in `onStop` methods, `CollectionHelper.getCol` | Owns **shared infrastructure**: base activities and their lifecycle edges `@<Activity>`, the singletons (`AnkiDroidApp`, `CollectionHelper`, `DialogHandler`, `MetaDB`), compat, themes, generic dialogs, shared widgets |
| **A2 Home & collection maintenance (HO)** | `anki/DeckPicker` (+32 inner), `widgets/{DeckAdapter,FabBehavior}`, `dialogs/{DeckPicker*,DatabaseErrorDialog,MediaCheckDialog,ImportDialog,ExportDialog}`, `BackupManager`, `libanki/AnkiPackageExporter`, `libanki/importer/*` (19 files, 87 classes) | **395** | S_DECKPICKER_NOCOL … S_DLG_BACKUP_NO_SPACE (24) + S_DECKPICKER_PAUSED | From A1: IntentHandler → DeckPicker (`IntentHandler.java:134-139, 104-109, 126-131`), drawer "Decks", `onCollectionLoadError`/reload, notifications, DialogHandler messages. From A4: results `RESULT_NO_MORE_CARDS` (`DeckPicker.java:656-664`), `CustomStudyListener` (2134-2147), `onRequireDeckListUpdate` (2123-2126). From A6: path gate result (673-675). From A3: `SyncErrorDialog` → `sync()`/`loginToSyncServer()`/`mediaCheck()`; `Connection` → `mSyncListener` (inner class of DeckPicker, so owned here). From A5: `REQUEST_BROWSE_CARDS` result (665-672). | Writes the INTENT edges into A3–A7 entry methods (Reviewer, StudyOptions, NoteEditor, CardBrowser, ModelBrowser, DeckOptions, MyAccount) |
| **A3 Sync & account (SY)** | `anki/MyAccount`, `async/Connection`, `dialogs/SyncErrorDialog`, `libanki/sync/*`, `org/apache/commons/httpclient/contrib/ssl/*` (11 files, 31 classes) | **184** | S_DLG_SYNC_ERROR(@type), S_SYNC_PROGRESS, S_DLG_SYNC_CANCEL, S_MYACCOUNT_LOGIN, S_MYACCOUNT_LOGGEDIN, S_MYACCOUNT_BUSY, S_MYACCOUNT_PAUSED | From A2: `DeckPicker.sync` (1266-1290), `showSyncErrorDialog`, `DatabaseErrorDialog` FULL_SYNC_FROM_SERVER (`DatabaseErrorDialog.java:322-332`). From A1: DO_SYNC via `DialogHandler.MSG_DO_SYNC` (`DialogHandler.java:99-116`). From A6: "Sync account" preference intent → MyAccount. | Almost all edges carry `env: network + AnkiWeb account` |
| **A4 Study & review (ST)** | `anki/{StudyOptionsActivity,StudyOptionsFragment,AbstractFlashcardViewer,Reviewer,Previewer,Whiteboard,ReadText,Lookup,VideoPlayer,AnkiFont}`, `dialogs/CustomStudyDialog`, `reviewer/*`, `anim/ViewAnimation`, `utils/DiffEngine`, `libanki/{Sound,LaTeX}`, `libanki/template/*`, `libanki/hooks/*` except AdvancedStatistics (28 files, 91 classes) | **477** | S_STUDYOPTIONS … S_VIDEOPLAYER (18) + 4 PAUSED; edges of S_DECKPICKER_TABLET's fragment | From A2: `openReviewer` (2128-2132), `openStudyOptions` (1695-1706), CustomStudyDialog from snackbar/context menu (1745-1754, 1785-1794; `DeckPickerContextMenu.java:132-138`). From A5: Previewer (`CardBrowser.java:206-211`). From A6: Previewer (`CardTemplateEditor.java:478-506`). | Owns the **Hooks registry** (rendering filters). A6 and A7 call `Hooks.getInstance`. |
| **A5 Browse, edit & multimedia (ED)** | `anki/{CardBrowser,NoteEditor,FieldEditText}`, `dialogs/{CardBrowserContextMenu,CardBrowserMySearchesDialog,CardBrowserOrderDialog,TagsDialog,NoteEditorRescheduleCard}`, `multimediacard/**`, `web/HttpFetcher`, `utils/{BitmapUtil,ExifUtil}`, `widgets/PopupMenuWithIcons`, `servicelayer/*`, `runtimetools/*` (47 files, 137 classes) | **591** | S_BROWSER_LOADING … S_PRONUNCIATION_BUSY (27) + 5 PAUSED; owns the TagsDialog page incl. @CUSTOM_STUDY | From A2: FAB `addNote` (840-844), `openCardBrowser` (1708-1715). From A4: `editCard` (`AbstractFlashcardViewer.java:1183-1190`), `Reviewer.addNote` (230-234), Reviewer → CardBrowser (508-519), CustomStudyDialog → TagsDialog (`CustomStudyDialog.java:139-188`). From A1: SEND/CREATE_FLASHCARD → NoteEditor, drawer "Card browser". | `NoteEditor` writes the INTENT edge into A6's `CardTemplateEditor` |
| **A6 Configuration (CF)** | `anki/{Preferences,DeckOptions,FilteredDeckOptions,ModelBrowser,ModelFieldEditor,CardTemplateEditor}`, `dialogs/{ModelBrowserContextMenu,ModelEditorContextMenu}`, `ui/{AppCompatPreferenceActivity,SeekBarPreference}`, `preferences/*` (13 files, 66 classes) | **369** | S_PREFS_HEADERS … S_DLG_HEBREW_FONT (29) + 6 PAUSED | From A1: drawer "Settings" (`NavigationDrawerActivity.java:273-278`). From A2: model browser (610-614), deck options (1889-1903), path gate (425-429). From A4: `Reviewer` (208-211), StudyOptions (294-302, 138-153), CustomStudyDialog (125-131). From A5: NoteEditor "Cards" (1001-1014). | Settings writes prefs read everywhere; model reads as `reads: pref:<key>` |
| **A7 Statistics & charts (SA)** | `anki/Statistics`, `anki/stats/*`, `com/wildplot/**`, `libanki/Stats`, `libanki/hooks/AdvancedStatistics` (57 files, 92 classes) | **780** | S_STATS_LOADING, S_STATS, S_STATS_DROPDOWN, S_STATS_PERIOD, S_STATS_PAUSED | From A1: drawer "Statistics" (`NavigationDrawerActivity.java:265-269`). From A2: summary line `AnkiStatsTaskHandler.createReviewSummaryStatistics` in `DeckPicker.updateDeckList` (1822-1886). From A6: `AdvancedStatistics.install` (`Preferences.java:484-490`). | 263 methods are DEAD candidates (5.1). Mostly mechanical CALL edges. |
| **A8 Core data layer & async engine (CO)** | `libanki/{Collection,Sched,Decks,Models,Media,Note,Card,CardStats,DB,Storage,Tags,Finder,Utils,Consts}`, `async/{DeckTask,BaseAsyncTask,CollectionLoader}` (17 files, 33 classes) | **794** | none (no windows) | From all areas: `DeckTask.launchDeckTask` (the caller area writes the edge to `DeckTask.<init>`/`execute`; A8 writes `doInBackground@<TYPE>` → `doInBackgroundX` → libanki), `getCol()` → `Storage.Collection`, Loader | Owns the **database layer**. The DeckTask listener callbacks live in caller files and are owned by the callers. Reflection edges in `Sched` (section 4). |
| Total | 258 files, 648 classes | **4178** | 140 base pages | | |

**Conventions the parallel agents should share** (to avoid duplicate or conflicting nodes):
- **Who writes a cross-area edge.** The caller's area writes it, ending at the callee's entry method (`<init>`, `onCreate`, `newInstance`, `show`). The callee's area writes everything after that.
- **Variant names**, so agents do not invent different ones:
  - `DeckTask.doInBackground@<TASK_TYPE>` and `DeckTask.onPostExecute@<CallerListenerClass>`;
  - `AnkiActivity.onCreate|onResume|onStop@<Activity>`, `NavigationDrawerActivity.initNavigationDrawer|onActivityResult|onNavigationItemSelected@<Host>`, `AnkiActivity.onCollectionLoaded@<Activity>`;
  - `DialogHandler.handleMessage@<MSG>`;
  - `ConfirmationDialog.onCreateDialog@<caller>`;
  - `TagsDialog.*@ADD|FILTER|CUSTOM_STUDY`, `CustomStudyDialog.onCreateDialog@<id>`, `DatabaseErrorDialog.onCreateDialog@<type>`, `SyncErrorDialog.onCreateDialog@<type>`, `ImportDialog.onCreateDialog@<type>`;
  - `Preferences.initSubscreen@<subscreen>` and `Preferences.updatePreference@<key>`;
  - `Hooks.runFilter@<hook>`.
- **Environment** in the edge `env` field: `network`, `account`, `media-file`, `tts-engine`, `dictionary-app`, `xlarge-screen`, `low-disk`, `sd-eject`.
- **`needs_state`** for "collection has cards", "note has sibling cards", "collection synced (ls ≥ scm)" and "DialogHandler message stored".

---

## 7. Baseline coverage by area and screen

Method-level, from `monkey|ape/report/report.xml` (METHOD counter covered > 0), JacocoInstrument excluded:

| Area | Methods | Both | Monkey only | APE only | Neither | Either % | DEAD candidates among "neither" (5.1/5.2) |
|---|---|---|---|---|---|---|---|
| A1 Platform | 588 | 105 | 0 | 145 | 338 | 42.5 | ≈ 155 (api, contract, Base64, crash tree/dialog, …) |
| A2 Home | 395 | 37 | 0 | 154 | 204 | 48.4 | 7 (Text/NoteImporter) |
| A3 Sync | 184 | 0 | 0 | 22 | 162 | 12.0 | 0 (gated by account) |
| A4 Study | 477 | 26 | 0 | 220 | 231 | 51.6 | 15 (ExternalHookLoader, HebrewFixFilter) |
| A5 Edit | 591 | 0 | 0 | 275 | 316 | 46.5 | 8 (NoteFactory, Mock*) |
| A6 Config | 369 | 48 | 3 | 185 | 133 | 64.0 | – (Hebrew dialog, legacy listener) |
| A7 Stats | 780 | 0 | 5 | 276 | 499 | 36.0 | 263 (wildplot) |
| A8 Core | 794 | 1 | 0 | 510 | 283 | 64.4 | 2 (CardStats) |
| **Total** | **4178** | **217** | **8** | **1787** | **2166** | **48.2** | **≈ 450** |

The totals match the brief: Monkey 225, APE 2004, either 2012. Line coverage computed from the class LINE counters (excluding JacocoInstrument) is 3.27% (Monkey) and 40.0% (APE); `comparison_ape_vs_monkey_api27.csv` reports 3.34/39.89. The small difference comes from counting method versus report-level lines (UNVERIFIED which one the CSV used).

What Monkey's 225 methods are:
- start-up and trap code (A1 + DeckPicker `onCreate`/lifecycle in A2);
- Settings subscreens and SettingsFragment, About (A6/A1);
- hook constructors via `Hooks.getInstance` from the settings toggles (A4 "both" 26: FuriganaFilters, HintFilter, LaTeX, Leech, ChessFilter);
- the 8 Monkey-only methods (AdvancedStatistics ×5, SeekBarPreference ×3).

**Screens never reached, by area** (pages from 3.3; coverage evidence; likely reason):

- **A1:** S_HOME_WIDGET, S_NOTIFICATION tap, provider CRUD, `api/*` — outside the `-p` package or external clients. S_CRASH_REPORT — ACRA off in DEBUG. S_INTENT_IMPORT_ERROR — no VIEW intents (`IntentHandler.java:47-125` uncovered). S_SYS_PERMISSION — permissions pre-granted.
- **A2:**
  - S_DLG_IMPORT_ADD/REPLACE — no `.apkg` in the folder and no VIEW intent; ImportDialog HINT/SELECT covered, ADD/REPLACE not.
  - S_DLG_DELETE_DECK — only for decks with cards.
  - S_DLG_RESTORE_LIST and S_DLG_DBERROR — RESTORE_BACKUP and all error types uncovered; only the confirm types were covered.
  - S_DLG_MEDIACHECK_RESULTS — the CHECK_MEDIA task never ran.
  - Undo item (`action_undo` uncovered).
  - S_DECKPICKER_TABLET — phone AVD.
  - No-space dialogs — disk.
  - Monkey reached only S_DECKPICKER_NOCOL (trap).
- **A3:** everything except S_DLG_SYNC_ERROR@NOT_LOGGED_IN and S_MYACCOUNT_LOGIN — no account; `Connection.login` never called.
- **A4:**
  - S_REVIEWER_WHITEBOARD, S_REVIEWER_SUBMENU, S_DLG_DELETE_NOTE, S_DLG_TTS_LANG, S_DLG_LOOKUP_LEO — Reviewer menu cases other than undo and mark are uncovered.
  - S_REVIEWER_Q_TYPING — no `{{type:}}` cards.
  - S_VIDEOPLAYER — no media.
  - Custom-study inputs @NEW/@REV/@FORGOT/@AHEAD/@RANDOM (only @PREVIEW and tags covered).
  - StudyOptions undo/unbury.
  - Likely reasons: the APE-made notes were simple (no siblings or media) and the overflow menu items were not explored.
- **A5:**
  - S_DLG_CARD_CONTEXT, S_DLG_CARD_DELETE — no long-press on a card row.
  - S_DLG_SAVE_SEARCH, S_DLG_MY_SEARCHES.
  - **S_NOTEEDITOR_EDIT and S_NOTEEDITOR_REMAP** — NoteEditor never opened in edit mode (`NoteEditor.java:371-393` uncovered; only add callers 383/397 covered).
  - S_DLG_RESCHEDULE.
  - S_DLG_PICK_STRING, S_TRANSLATION*, S_PRONUNCIATION* — text required, then network.
- **A6:** S_DLG_MODEL_CONTEXT — no long-press; all S_DLG_CONFIRM@FULLSYNC_* variants — G10; S_DLG_HEBREW_FONT — API.
- **A7:** Statistics was reached by APE (13/13 activity methods). `AdvancedStatistics` never ran together with Statistics (APE never enabled it; Monkey enabled it in the trap but never reached Statistics). The rest of the "neither" count is wildplot dead code.
- **A8:** the unreached libanki methods are mainly behind import (`Anki2Importer` and media copy), sync (`Collection.beforeUpload`, `setLs`) and rarely used operations (5.3).

---

## Conclusions and recommendations

1. **The 3% Monkey result is an environment failure, not a Monkey-versus-APE difference in exploration.** The app's own failure handling (`DeckPicker.java:425-429, 673-675`) turns a non-creatable `/sdcard/AnkiDroid` into a loop of Advanced settings → app exit, and both tools started in it. Before the baseline for AnkiDroid is used in the study, re-run it after checking G1/G2 (2.4 items 1-2) and performing the documented setup (2.4 item 3). Otherwise "targets = reachable but missed by Monkey" would contain almost the whole app.
2. **The cause of the folder failure is UNVERIFIED.** Look at the device state and the harness setup log for the Monkey emulator (`emulator-5582`) and for the APE emulator (`emulator-5562`) around 02:35Z. The code-side fact is precise: `mkdirs()` returned false while the permission was granted and the storage state was `MEDIA_MOUNTED`.
3. **For the graph:**
   - Model S_DECKPICKER_NOCOL and S_PREFS_ADVANCED@PATH_GATE explicitly, with guard `env: AnkiDroid folder not creatable`, so the Monkey trap is a legitimate page.
   - Mark the import, sync and schema-confirmation branches with `needs_state`/`env`.
   - Treat the classes in 5.1 as DEAD candidates. Confirm them with the bytecode extractor (tools v2): javac-inlined constants and the `DEBUG=false` elimination mean that a source grep and the bytecode can differ.
4. **Parallel build:** use the 8 areas of section 6. A7 and A8 are large but mostly mechanical. A2 and A4 contain most of the framework-mediated edges: DeckTask listeners, DialogHandler, results, gestures, WebView.
5. **Hazards seen while reading** (not reproduced):
   - a `DialogHandler` stored message replayed by a non-DeckPicker activity would throw ClassCastException (`DialogHandler.java:56-117`);
   - `Preferences` "Force full sync" calls `getCol()` without a null check (`Preferences.java:347-354`), which would throw an NPE when the collection is inaccessible (the trap state);
   - `DeckPicker.onRequestPermissionsResult` silently ignores an empty result (681), so a blocked permission dialog leaves the home screen unusable.
