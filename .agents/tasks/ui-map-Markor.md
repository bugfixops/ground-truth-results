# Markor v2.16.1 (`net.gsantner.markor_test`): UI map and modeling plan

Read-only investigation for the method-level trigger graph (ICST 2027 study). Nothing in the app folder was modified; the only file written is this report.

## Summary

- **Scope.** 320 compiled classes (the 3 `JacocoInstrument` classes excluded) from 139 source files: 125 in `src/main/java` and 14 in `thirdparty/java` (package `other.*`). `thirdparty/java` is compiled in (`APP/build.gradle:64`) but is missing from `class_files.json` "sourcefiles". JaCoCo lists 2855 methods. Two of them belong to `BuildConfig`, which never shows up in any execution-data segment, so treat it as excluded, as the Currency graph did. The app has no Kotlin, no database (only SharedPreferences and plain files), no services apart from two widget `RemoteViewsService`s, no notifications and no network code in use.
- **Entry points.** The launcher opens `MainActivity` (singleTop). `DocumentActivity` is exported for VIEW/EDIT on text MIME types and 26 file extensions, and for SEND/CREATE_NOTE. There are also 3 *disabled* launcher activities, a *disabled* PROCESS_TEXT alias, an exported widget-configure activity, 2 widget providers, dynamic and pinned shortcuts, and a no-UI trampoline (`OpenFromShortcutOrWidgetActivity`).
- **First run.** A 5-slide AppIntro with Skip disabled. `MainActivity.onResume` reopens it until Done is pressed (`MainActivity.java:301`, `IntroActivity.java:25-36,52,70-75`). Next comes the storage-permission gate (`MainActivity.java:281-283`), which was pre-granted in both baseline runs (its UI never ran), and then a one-time changelog dialog. No account, login, vault or database gate exists.
- **Baseline timeline**, rebuilt from the 120 reset-on-dump coverage segments of about 30 s each:
  - Monkey spent about 15.5 min in the intro and about 13 min in `MainActivity`. In that time it never opened `DocumentActivity`, never tapped the FAB and never selected a file. It spent the last ~31 min inside Settings' full-screen folder picker (`GsFileBrowserDialog`).
  - APE spent 5 min in the intro, then 35 min exploring broadly. After a process restart at segment 80 the intro was shown again and held APE for the last 20 min. The cause is UNVERIFIED.
- **Never reached by either tool:** share-into, widgets and widget config, shortcut and launcher trampolines, rename/move/copy/import, backup/restore, encryption, every editor other than Markdown/todo.txt, the text-selection action mode, todo.txt priority/due-date/archive, snippets, and link taps in view mode. The main reasons:
  - the notebook folder `/sdcard/Documents/marder` was empty, because `fixtures/Documents` was never pushed;
  - several entry points start outside the app package;
  - the two traps above.
- **Plan.** 6 feature areas: SHELL (282 methods), FILES (313), EDITOR (577), ACTIONS (461), RENDER (398) and INFRA (824). The page list has 109 candidate pages. 4 whole classes (46 methods) and 118 further methods have no call site; 100 more are framework-callback implementations that the baseline never triggered.

**Path conventions.** `APP/` stands for `/Users/darshan/Desktop/yang/work/final_java_only/Markor/app/Markor-#v2.16.1/app/`. Java files are cited by bare file name plus line (names are unique in the tree), resources as `res/...:line`, and the manifest as `Manifest:line` (`APP/src/main/AndroidManifest.xml`). Labels:
- **FW-MEMORY**: Android or library behaviour I recalled but did not check against source.
- **UNVERIFIED**: not confirmed.

**How this was produced.**
- Read in full: `MainActivity`, `DocumentActivity`, `IntroActivity`, `StoragePermissionActivity`, `MarkorBaseActivity`, `ApplicationObject`, `GsActivityBase`, `GsFragmentBase`, `GsFileBrowserFragment`, `GsFileBrowserListAdapter`, `GsFileBrowserDialog`, `SettingsActivity`, `DocumentEditAndViewFragment`, `MoreFragment`, `MoreInfoFragment`, `FormatRegistry`, `NewFileDialog`, `WrWidgetConfigure`, `OpenEditor*`, `TodoWidgetProvider`, `WrMarkorWidgetProvider`, `ShortcutUtils`, the JaCoCo harness, the manifest and all menus.
- Read in part: `ActionButtonBase`, `AppSettings`, `Document`, `GsContextUtils`, `GsPreferenceFragmentBase`, `HighlightingEditor`, `MarkorDialogFactory`, `TodoTxtActionButtons`, `DocumentShareIntoFragment`, `TextSearchFragment`, `FileSearchEngine`, `GsSearchOrCustomTextDialog`, the action lists of all `*ActionButtons`, `res/xml/preferences_master.xml` (structure) and the layouts.
- Not read line by line: the format highlighters and converters, `TextViewUtils`, `SyntaxHighlighterBase` internals, `LineNumbersView`, `TextSearchHandler`, `AttachLinkOrFileDialog`, `DatetimeFormatDialog`, `SearchAndReplaceTextDialog`, `FileSearchResultSelectorDialog`, `WrRenameDialog`, `WrMarkorSingleton`, the katex extension, the crypto code, and `GsFileUtils`/`GsCollectionUtils`/`GsTextUtils`. Graph agents must read these.
- Read-only scripts parsed: the two JaCoCo XML reports; the 2×120 `coverage/*.ec` segment files (exec format, per-class probe hits per segment); the binary `AndroidManifest.xml` inside `Markor-#v2.16.1-rebuilt.apk`; the constants in the compiled `BuildConfig.class`; and a comment- and string-aware grep for call sites.

---

## 1. Entry points

There is no merged manifest under `APP/build/intermediates` (only `javac/` outputs exist). `src/flavorAtest` has no manifest; `src/flavorGplay/AndroidManifest.xml:17` only removes `REQUEST_INSTALL_PACKAGES` and is not the built flavor. The source manifest was therefore cross-checked against the **binary manifest in the APK**, which matches and adds only library entries: `androidx.startup.InitializationProvider` (authority `net.gsantner.markor_test.androidx-startup`, exported=false), the permission `net.gsantner.markor_test.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION`, and optional `uses-library androidx.window.extensions/sidecar`. The APK gives minSdk 18 and targetSdk 35 and has no `<instrumentation>` element.

### 1.1 Manifest components

| Component | Kind | exported | enabled | Intent filters / meta | launchMode, theme, flags | Evidence |
|---|---|---|---|---|---|---|
| `net.gsantner.markor.ApplicationObject` | Application | – | – | – | app theme `AppTheme.Unified.StartupFlash`, `requestLegacyExternalStorage`, `allowBackup` | Manifest:39-53; `ApplicationObject.java:39-49` (creates `AppSettings`, warms up a `WebView`) |
| `.activity.MainActivity` | Activity | true | true | MAIN/LAUNCHER | **singleTop**, `stateUnchanged\|adjustResize` | Manifest:61-71 |
| `.activity.SettingsActivity` | Activity | (no filter) | – | – | parent MainActivity | Manifest:73-76 |
| `.activity.StoragePermissionActivity` | Activity | (no filter) | – | – | parent MainActivity | Manifest:78-81 |
| `.activity.ActionButtonSettingsActivity` | Activity | (no filter) | – | – | parent SettingsActivity | Manifest:83-89 |
| `other.writeily.widget.WrWidgetConfigure` | Activity | **true** | – | `APPWIDGET_CONFIGURE` | – | Manifest:91-97; `WrWidgetConfigure.java:35-47` (shows a folder picker only with a valid `EXTRA_APPWIDGET_ID`) |
| `other.writeily.widget.WrMarkorWidgetProvider` | Receiver | true | – | `APPWIDGET_UPDATE`; `res/xml/markor_widget.xml` (configure=WrWidgetConfigure, update every 30 min) | – | Manifest:99-108 |
| `other.writeily.widget.WrFilesWidgetService` | Service (RemoteViews) | (permission `BIND_REMOTEVIEWS`) | – | – | – | Manifest:110-112 |
| `.widget.TodoWidgetProvider` | Receiver | true | – | `APPWIDGET_UPDATE`; `res/xml/todo_widget.xml` | – | Manifest:114-123 |
| `.widget.TodoWidgetService` | Service (RemoteViews) | (`BIND_REMOTEVIEWS`) | – | – | – | Manifest:125-127 |
| `androidx.core.content.FileProvider` | Provider (library) | false | – | authority `net.gsantner.markor_test.provider`, grantUriPermissions, `res/xml/provider_paths.xml` (external "." and root "/") | – | Manifest:129-137 |
| `.activity.openeditor.OpenEditorTodoActivity` | Activity | true | **false** | MAIN/LAUNCHER (icon "To-Do") | noHistory | Manifest:139-150 |
| `.activity.IntroActivity` | Activity | (no filter) | – | – | label "About" | Manifest:152-154 |
| `.activity.openeditor.OpenEditorQuickNoteActivity` | Activity | true | **false** | MAIN/LAUNCHER | noHistory | Manifest:156-167 |
| `.activity.openeditor.OpenShareIntoActivity` | Activity | true | **false** | MAIN/LAUNCHER | noHistory | Manifest:169-180 |
| `.activity.openeditor.OpenFromShortcutOrWidgetActivity` | Activity | (no filter) | – | – | standard, `@android:style/Theme.NoDisplay` | Manifest:182-185; `OpenFromShortcutOrWidgetActivity.java:16-20` (finish, then `DocumentActivity.launch(this, getIntent())`) |
| `.activity.DocumentActivity` | Activity | **true** | – | (a) SEND, `com.google.android.gm.action.AUTO_SEND`, `com.google.android.gms.actions.CREATE_NOTE`; categories DEFAULT, `voicesearch.SELF_NOTE`; mime `text/plain`, `text/*`, `*/*` (Manifest:195-206). (b) VIEW/EDIT, DEFAULT, mime `text/*`, `text/plain(+md)`, `text/markdown`, `text/x-markdown`, `text/htm(l)` (208-221). (c) EDIT/VIEW, DEFAULT, schemes content/file, host `*`, text mimes plus `application/octet-stream`, and `pathPattern` for 26 extensions (.markdown .md .jenc .mdown .mdwn .mkd .mkdn .Rmd .text .txt .taskpaper .adoc .patch .diff .ldg .ledger .org .yml .yaml .xlf .toml .vcf .ics .ini .json .csv; 223-1088) | standard, `maxRecents=5`, theme StartupFlash, `stateUnchanged\|adjustResize` | Manifest:187-1089 |
| `AliasDocumentProcessText` → DocumentActivity | activity-alias | true | **false** | PROCESS_TEXT (`text/plain`, `text/*`) | – | Manifest:1091-1104 |
| `.JacocoInstrument.SMSInstrumentedReceiver` | Receiver | true | – | `edu.gatech.m3.emma.COLLECT_COVERAGE` | coverage harness, out of scope | Manifest:1105-1110 |
| `androidx.startup.InitializationProvider` | Provider (library, merged) | false | – | EmojiCompat and ProcessLifecycle initializers | – | APK manifest |

- Permissions: READ/WRITE_EXTERNAL_STORAGE, INTERNET, INSTALL_SHORTCUT, REQUEST_INSTALL_PACKAGES and MANAGE_EXTERNAL_STORAGE (Manifest:17-25). `<queries>` covers browsers, IMAGE_CAPTURE and VIEW https (Manifest:1114-1135).
- **No `configChanges`** anywhere, so rotation, locale and night-mode changes recreate activities (FW-MEMORY default).
- No dialog-themed activity. The only special theme is `Theme.NoDisplay` on the trampoline.
- No http(s) deep links, no SEARCH filter, no static `shortcuts.xml`, no boot or other system receivers.

### 1.2 Programmatic and external entry points

- **Special launchers.** `MarkorContextUtils.applySpecialLaunchersVisibility` enables or disables the 3 `OpenEditor*` launchers and the alias (`MarkorContextUtils.java:45-51`). The Settings toggle "Launcher (special documents)" calls it with the preference value (`SettingsActivity.java:226-228`). However, `MainActivity.onCreate` calls it again on every creation (`MainActivity.java:123`) with `AppSettings.isSpecialFileLaunchersEnabled()`, which returns **false in test builds** (`AppSettings.java:254-259`). The compiled `BuildConfig.IS_TEST_BUILD` is true. In this APK the launchers can therefore only be enabled briefly from Settings or with `pm enable`.
- **Dynamic shortcuts** (API ≥ 25): `ShortcutUtils.setShortcuts` (`ShortcutUtils.java:53-118`) builds To-Do, QuickNote and the most recent document. It is called from `AppSettings.addRecentFile` (`AppSettings.java:398`) on every `DocumentEditAndViewFragment.onPause` (`DocumentEditAndViewFragment.java:277-290`). The shortcuts target the trampoline with `ACTION_EDIT`.
- **Pinned shortcut**: notebook menu "Create shortcut" (`GsFileBrowserFragment.java:385-390`) → `MarkorContextUtils.createLauncherDesktopShortcut` (`MarkorContextUtils.java:67-76`) → `ShortcutManagerCompat.requestPinShortcut` (`GsContextUtils.java:1189-1200`).
- **Widget PendingIntents.**
  - `WrMarkorWidgetProvider.onUpdate` (`WrMarkorWidgetProvider.java:40-115`): new note (SEND → share-into), header and home (`MainActivity` VIEW with `EXTRA_FILE` folder), To-Do and QuickNote (EDIT via the trampoline), and list rows (fill-in `EXTRA_FILE`, `WrFilesWidgetFactory.java:85`).
  - `TodoWidgetProvider.onUpdate` (`TodoWidgetProvider.java:21-50`): container and list rows open the To-Do file.
- **Intent extras understood:** `Document.EXTRA_FILE` (`java.io.File`), `EXTRA_FILE_LINE_NUMBER` and `EXTRA_DO_PREVIEW` (`Document.java:51-54`); a `?line=` query on the data URI (`DocumentActivity.java:192`); a file name starting with `index.` forces preview (`DocumentActivity.java:201`). `MainActivity` accepts a folder or file in its intent (`MainActivity.java:125-134`, `onNewIntent` 223-236).
- **Self-broadcasts.** `updateLauncherWidgets` and `updateTodoWidgets` send an explicit `ACTION_APPWIDGET_UPDATE` to the app's own providers (`WrMarkorWidgetProvider.java:118-135`, `TodoWidgetProvider.java:52-69`). Callers: `MainActivity.onPause` (569-572), `DocumentEditAndViewFragment.onPause` (to-do file only, 286-288), `SettingsFragmentMaster.onPreferenceChanged` for path keys (`SettingsActivity.java:242-245`) and `WrWidgetConfigure.onStop` (49-52). In the baseline both providers' `<init>` ran but `onUpdate` never did. FW-MEMORY: `AppWidgetProvider.onReceive` only calls `onUpdate` for a non-empty id array, so no widget was placed.

---

## 2. First-run flow and setup gates

### 2.1 What a fresh install goes through

1. **Application and MainActivity start.** Launcher → `ApplicationObject.onCreate` → `MainActivity.onCreate` (`MainActivity.java:76-137`), which:
   - creates the notebook folder (80-84) at `Environment.getExternalStorageDirectory()/Documents/<app_name lowercased>` (`AppSettings.java:97-107`). `app_name` is **"Marder"** in this flavor (`APP/src/flavorAtest/res/values/string-not_translatable.xml:12`), so the folder is `/sdcard/Documents/marder`; QuickNote is `.../QuickNote.md` and To-Do is `.../todo.txt` (`res/values/string-not_translatable.xml:45-46`);
   - wires the FAB, ViewPager2, bottom nav and toolbar;
   - registers a gene-rate rating prompt (247-257).
2. **`MainActivity.onResume`** (279-315):
   - (a) `if (!IntroActivity.isFirstStart) StoragePermissionActivity.requestPermissions(this)` (281-283) is skipped on the very first start;
   - (b) the recreate-main flag (285-293);
   - (c) `IntroActivity.optStart` (301). If the default-SharedPreferences boolean `net.gsantner.markor.activity.IntroActivitywas_shown` is false (`IntroActivity.java:22,33-36`), it calls `startActivityForResult(IntroActivity)` (25-31).
3. **IntroActivity**: 5 `AppIntroFragment` slides (`IntroActivity.java:45-49`), `setSkipButtonEnabled(false)` (52), swiping allowed (53). Only `onDonePressed` writes the flag (70-75). Leaving any other way keeps the flag false, and the next `MainActivity.onResume` starts the intro again. That is the "first-run tutorial trap". FW-MEMORY (AppIntro 6.2.0): Next arrow on slides 1-4, Done on slide 5, Back on slide 1 finishes the activity.
4. **Storage gate** (from the second resume on): `StoragePermissionActivity.requestPermissions` checks `checkExternalStoragePermission` (`StoragePermissionActivity.java:18-23`). On API 23-29 that is `WRITE_EXTERNAL_STORAGE` (`GsContextUtils.java:2419-2429`); on API ≥ 30 it is `isExternalStorageManager` (2423-2425). If the check fails, the activity starts `StoragePermissionActivity` and **finishes MainActivity**. The permission activity shows an AlertDialog (Exit / Yes) that cannot be dismissed by an outside touch (32-42). Yes calls `requestExternalStoragePermission` (`GsContextUtils.java:2386-2402`); then `onRequestPermissionsResult`/`onActivityResult` → `processPermissionState` → back to Main, or the dialog again (44-62). The same gate runs in `DocumentActivity.onCreate` (`DocumentActivity.java:137`) and `OpenEditorActivity.onCreate` (`OpenEditorActivity.java:24-27`).
5. **Changelog dialog**, once per versionCode, on the same resume (`MainActivity.java:303-310`; `AppSettings.java:350-356`). The compiled `BuildConfig.VERSION_CODE` is 260902 and `VERSION_NAME` is `2.16.1-0946`.
6. **Rate prompt** after 4 counted launches and 30 min since install (`MainActivity.java:247-257`). Its appearance and UI are library behaviour (UNVERIFIED).

Optional in-app gates:
- **Encryption password** (Settings → General, API ≥ 23: `SettingsActivity.java:185-188, 374-376`; `AppSettings.java:943-946`). Without it, `.jenc` files are read raw and a toast warns (`Document.java:246-255`).
- **SD-card/SAF mount** dialog for folders on a mounted volume (`MainActivity.java:353-356`, `DocumentEditAndViewFragment.java:937-944`).

### 2.2 Gates

| Gate | Enforced by | How to pass | Baseline evidence |
|---|---|---|---|
| Intro | `MainActivity.java:301`, `IntroActivity.java:25-36` | Done on slide 5 (`IntroActivity.java:70-75`) | `onDonePressed` hit by both; Monkey trapped about 15.5 min, APE 5 min plus 20 min later |
| Storage permission | `MainActivity.java:281-283`, `DocumentActivity.java:137`, `OpenEditorActivity.java:26` | WRITE_EXTERNAL_STORAGE granted | `askForPermissions`, `processPermissionState` and `onRequestPermissionsResult` never ran in either run, so it was granted before the run. How (for example `install -g`) is UNVERIFIED |
| Changelog dialog | `MainActivity.java:303-310` | dismiss | `GsContextUtils.showDialogWithHtmlTextView` hit by both |
| Empty notebook (state, not code) | `/sdcard/Documents/marder` created empty (`MainActivity.java:80-84`) | put files there | Monkey never opened, selected or long-pressed a notebook row (`GsFileBrowserFragment.onFsViewerSelected`, `GsFileBrowserListAdapter.toggleSelection`/`onLongClick` not hit by Monkey); APE created files (`NewFileDialog` hit) |
| Writable folder | `MainActivity.java:343-350` | FAB in a writable folder (otherwise it jumps to the notebook) | – |
| Encryption password | `NewFileDialog.java:117`, `Document.java:246-255` | set via Settings | `showSetPasswordDialog`, `PasswordStore.storeKey` and `JavaPasswordbasedCryption.encrypt` never hit |
| Outside-app entries | manifest | SEND/VIEW intents, widgets, shortcuts, `pm enable` | all unhit |

### 2.3 Baseline timeline from the coverage segments

`SMSInstrumentedReceiver` dumps with `getExecutionData(true)` (`JacocoInstrumentation.java:60-61`), so each `coverage/NNNNN.ec` holds only the probes hit since the previous dump (about 30 s; the `status.json` files show 3600 s and 118 segments, and the folders hold 120 files). Per-class probe hits per segment give this picture:

- **Monkey** (`monkey -p ... --throttle 500`, `monkey/status.json`):
  - Segments 0-31 (0 to ~15.5 min): only `IntroActivity` and AppIntro library classes are active (AppIntroBase probes in every segment). IntroActivity has an onCreate-sized burst in segment 7, which looks like it was re-created.
  - Segments 31-57 (~15.5 to 29 min): `MainActivity`, the notebook fragment, the To-Do/QuickNote editors (`DocumentEditAndViewFragment`, `HighlightingEditor`), the More tab, then Settings at 57. `DocumentActivity` never ran (0 of 25 methods).
  - Segments 58-119 (~29 to 60 min): only `SettingsActivity`, `GsFileBrowserDialog` and its adapter ran; `MainActivity` never executed again. Monkey changed the notebook folder and the To-Do file. The Monkey-only hits are `SettingsFragmentMaster$2/$4.onFsViewerSelected` and `AppSettings.setNotebookDirectory`/`setTodoFile`. The picker is full-screen (`GsFileBrowserDialog.java:343-350`) and Back walks the folder history before it dismisses (`GsFileBrowserDialog.java:86-95`; `$1.onBackPressed` is a Monkey-only hit).
  - `androidx.startup.AppInitializer` probes appear only in segments 0-1, so the process was never restarted.
- **APE** (`--ape sata --running-minutes 60`, `ape/status.json`):
  - Segments 0-10: intro.
  - Segments 10-79: broad exploration. `DocumentActivity` from segment 17, `NewFileDialog` 33, `ActionButtonSettingsActivity` 36, `WrMarkorSingleton.deleteSelectedItems` at 50.
  - Process starts (AppInitializer) at segments 0, 1, 14, 32, 40, 45, 54, 61, 69, 80, 87, 99, 111 and 115.
  - At segment 80 a new process runs `MainActivity.onCreate` and the `optStart` launch branch. From 81 to 119 the AppIntro pager is active (about 159 AppIntroBase probes per segment), so APE spent the last ~20 min in the intro again.
- **Why the intro re-armed (UNVERIFIED).** The flag is only ever written in `IntroActivity.java:72`, and no app code clears it. `GsSharedPreferencesPropertyBackend.resetSettings` clears only the "app" file and has no caller (`GsSharedPreferencesPropertyBackend.java:89-97`). Candidates:
  - the tool cleared app data;
  - a file deletion through the browser. The "AppData (private)" virtual folder maps to `getFilesDir()` and ".." leads up to the app data root (`GsFileBrowserListAdapter.java:155, 540-556`).

  The restarts at 54, 61 and 69 still skipped the intro, though. The APE event log would settle it.

### 2.4 Windows the baseline never reached, and the probable gate

| Window / feature (probe method) | Monkey | APE | Probable reason |
|---|---|---|---|
| StoragePermissionActivity UI (`askForPermissions`) | – | – | permission pre-granted (expected) |
| DocumentActivity (`onCreate`) | – | ✔ | Monkey: empty notebook, FAB never tapped, ~46 min lost in the two traps |
| NewFileDialog (`onCreateDialog`), FAB (`MainActivity.onClickFab`/`onLongClickFab`) | – | ✔ | Monkey never hit the FAB |
| Notebook selection mode (`toggleSelection`, `onLongClick`), sort, filter, search results | – | ✔ | no file rows to long-press for Monkey |
| Rename (`WrRenameDialog.onCreateDialog`), Move/Copy (`askForMoveOrCopy`), Import (`importFile`), Select-all (`selectAll`) | – | – | need a single writable selection plus the menu item, or picking a file in the import picker |
| View mode / WebView (`setupWebViewIfNeeded`) | – | ✔ | Monkey never toggled preview |
| Search & replace (`showSearchReplaceDialog`) | – | ✔ | reached only through the todo search or the find-bar filter |
| Text-selection ActionMode (`HighlightingEditor$2.onCreateActionMode`) | – | – | QuickNote/To-Do were empty, so there was nothing to select |
| Link tap in view mode (`MarkorWebViewClient.shouldOverrideUrlLoading`) | – | – | no document with links |
| Wikitext, AsciiDoc, Org, CSV, key-value and plaintext editors (their `generateSpans`, `*ActionButtons.onActionClick`) and converters (`convertMarkup`) | – | – | no such files; APE only switched formats from the Format submenu (Asciidoc/Orgmode ActionButtons constructors hit) |
| Embed-binary viewer (`EmbedBinaryTextConverter.convertMarkup`) | – | – | no image/audio file opened |
| todo.txt priority, archive, due date, update items, table row, snippet, ASCIIDOC special key | – | – | empty todo.txt or non-markdown formats needed |
| Date/time pickers (`DatetimeFormatDialog` lambdas `$6`–`$9`) | – | – | – |
| ActionButtonSettingsActivity | – | ✔ | – |
| Backup/restore (`BackupUtils.*`), set password, encryption | – | – | never chosen in Settings |
| Share-into (`DocumentShareIntoFragment.onViewCreated`) | – | – | needs a SEND/PROCESS_TEXT intent from outside |
| Widgets, widget config, launcher trampolines (`*.onUpdate`, `WrWidgetConfigure.onCreate`, `OpenEditorActivity.onCreate`, `OpenFromShortcutOrWidgetActivity.onCreate`) | – | – | home screen or launcher, outside the package; launchers disabled |
| "Not supported" / "Open with" dialogs (`DocumentActivity.showNotSupportedMessage`, `askUserIfWantsToOpenFileInThisApp`) | – | – | need a bad intent, or a text file with an unknown extension |
| Mount-SD dialog (`GsContextUtils.showMountSdDialog`) | – | – | no SAF volume |
| Load epub (`GsCoolExperimentalStuff.convertEpubToText`) | – | – | needs an `.epub` |

### 2.5 What a harness should prepare

1. **Permission:** `adb install -g …` or `pm grant net.gsantner.markor_test android.permission.WRITE_EXTERNAL_STORAGE` (plus READ) on API 27.
2. **Skip the intro and changelog** (debug build, so `run-as` works). In `shared_prefs/net.gsantner.markor_test_preferences.xml` set `<boolean name="net.gsantner.markor.activity.IntroActivitywas_shown" value="true"/>`. In `shared_prefs/app.xml` set `<int name="pref_key__app_first_start_current_version" value="260902"/>`. Or script the intro: 4× Next, then Done.
3. **Fill `/sdcard/Documents/marder/`** (this is what the missing `fixtures/Documents` should have provided). Prefill `QuickNote.md` and `todo.txt` in it, since the tabs open those exact files.
   - From `_fixtures/Download`: `notes.md`, `journal.md`, `todo.txt` (tasks with `(A)` priorities, `@context`, `+project`, `due:`, done `x` lines), `table.csv`, `tasks.org`, `data.json`, `contacts.vcf`, `events.ics`, `config.xml`, `page.html`, images, `.mp3`/`.wav` (embed-binary viewer), `sample.pdf` (external-file path), `archive.zip`/`.apkg` (open-with-other-app path).
   - Missing from the fixtures, to add:
     - a Zim wikitext `.txt` whose first line is `Content-Type: text/x-zim-wiki` (`WikitextTextConverter.java:206-209`);
     - an `.adoc`, a code file (`.py`/`.js`), a `.m3u` playlist and `index.html` (forced preview);
     - a sub-folder and a dot-file;
     - `.app/snippets/*.md` (snippet dialog; `AppSettings.java:133-137`) and a `_res/` attachment folder;
     - Markdown with links, images, `$math$`, headings/TOC, front matter, tables and checklists;
     - a text file with an unknown extension (Open-with dialog), an `.apk` (installer path) and an `.epub` (experimental loader).
   - The app's own templates in `APP/src/main/assets/templates/` (`asciidoc-reference.adoc`, `orgmode-reference.org`, `sample.csv`, `todo.example.txt`, `zim-wiki-empty.txt`, …) are ready-made samples.
4. **Optional settings:** an encryption password (Settings → General) and a `.jenc` file created with NewFileDialog's encrypt checkbox. The password is kept through the Android Keystore (`PasswordStore`), so it cannot be pre-seeded by copying files. Experimental features are already on by default in this build (`AppSettings.java:921-923`).
5. **Outside entries via adb:**
   - share-into: `am start -n net.gsantner.markor_test/net.gsantner.markor.activity.DocumentActivity -a android.intent.action.SEND -t text/plain --es android.intent.extra.TEXT "…"`;
   - open a file: `-a android.intent.action.VIEW -d file:///sdcard/Documents/marder/notes.md -t text/markdown`;
   - widget config: `am start -n net.gsantner.markor_test/other.writeily.widget.WrWidgetConfigure --ei appWidgetId <id>`;
   - launchers: `pm enable net.gsantner.markor_test/net.gsantner.markor.activity.openeditor.OpenEditorTodoActivity` (and QuickNote/ShareInto/alias), then `am start`;
   - widgets need launcher interaction outside the package.

   FW-MEMORY: tools restricted with `-p` cannot drive other packages, and Monkey's app-switch only launches the MAIN/LAUNCHER activities it enumerated at startup.

---

## 3. Screens and navigation

### 3.1 Window inventory

- **Activities**
  - `MainActivity`: toolbar, ViewPager2 with 4 tabs, BottomNavigationView, FAB (`res/layout/main__activity.xml:29-61`).
  - `DocumentActivity`: one fragment container `document__placeholder_fragment` (`DocumentActivity.java:342-351`).
  - `SettingsActivity`; `ActionButtonSettingsActivity` (RecyclerView with drag handle and switches); `IntroActivity` (AppIntro pager); `StoragePermissionActivity` (dialog only); `WrWidgetConfigure` (blank activity plus picker); `OpenEditor{Todo,QuickNote,ShareInto}Activity` and `OpenFromShortcutOrWidgetActivity` (trampolines, no UI).
- **Fragments**
  - `GsFileBrowserFragment` (Notebook tab).
  - `DocumentEditAndViewFragment` (To-Do and QuickNote tabs, and inside DocumentActivity; layout `res/layout/document__fragment__edit.xml` with `HighlightingEditor`, `LineNumbersView`, action bar `GsHorizontalScrollView`, a `ViewStub` for the WebView, and `topViewContainer` for the find bar at :27).
  - `MoreFragment` holding `MoreInfoFragment` (preference list).
  - `DocumentShareIntoFragment` holding `ShareIntoImportOptionsFragment`.
  - `SettingsActivity.SettingsFragmentMaster`; `TextSearchFragment` (find/replace bar, `ActionButtonBase.java:110-121`); placeholder `new Fragment()` for unvisited tabs (`MainActivity.java:509-513`).
- **DialogFragments:** `NewFileDialog`, `FileInfoDialog`, `WrRenameDialog`, `GsFileBrowserDialog` (full-screen picker), `TodoTxtActionButtons$DateFragment` (DatePickerDialog).
- **AlertDialogs:**
  - the generic list/search dialog `GsSearchOrCustomTextDialog` (`GsSearchOrCustomTextDialog.java:84-180`), used by about 25 `MarkorDialogFactory` dialogs (`MarkorDialogFactory.java:85-1266`);
  - `FileSearchDialog`, `FileSearchResultSelectorDialog`, `SearchAndReplaceTextDialog`, `AttachLinkOrFileDialog`, `DatetimeFormatDialog` (plus framework DatePicker/TimePicker, `DatetimeFormatDialog.java:166-180`);
  - permission dialog, DocumentActivity "open with" and "not supported" (`DocumentActivity.java:119-131, 243-252`);
  - `GsContextUtils` dialogs: HTML text (2581), raw file in WebView (2605), mount SD (2260);
  - speed read (`GsCoolExperimentalStuff.java:83`); library dialogs for preferences, `ColorPreference` and the gene-rate prompt.
- **Popups:** `ListPopupWindow` in NewFileDialog (title formats, `NewFileDialog.java:144-152`), DatetimeFormatDialog (98) and SearchAndReplace (128); `PopupWindow` suggesting a template name (`MarkorDialogFactory.java:1265-1276`, called from `NewFileDialog.java:174`).
- **Action mode:** custom text-selection callback in `HighlightingEditor` adds a "☰ select lines" item (`HighlightingEditor.java:570-600`, registered in the constructor at 122).
- **Menus:**
  - `res/menu/main__menu.xml` (Settings, hidden: `AppSettings.java:334-336`);
  - `filesystem__menu.xml` (16 items);
  - `document__edit__menu.xml` (undo, redo, save, preview, edit, search, SearchView, and submenus File settings, Format, Share, Tools, plus file browser, info, reload);
  - `action_order__menu.xml` (Reset);
  - `main__bottom_nav.xml` (4 tabs).
- **Preference screens:** `res/xml/preferences_master.xml` root (10) with General (17-117), Other (120-203), Edit mode (206-382, nesting Basic color scheme 235-296), View mode (385-439), Markdown (446), todo.txt (509), Wikitext (551), Plaintext (569), AsciiDoc (583) and Orgmode (613); `prefactions__more_information.xml`; `prefactions_share_into.xml`.
- **Absent** (checked by grep): navigation drawer, bottom sheet, context menu (`registerForContextMenu`), `PopupMenu`, `TabLayout`, navigation graph, `onConfigurationChanged`.

### 3.2 Navigation

| From | Gesture / event | Mechanism | To | Evidence |
|---|---|---|---|---|
| Launcher | tap icon | MAIN/LAUNCHER, singleTop (`onNewIntent` if on top) | MainActivity, start tab from `pref_key__app_start_tab_v2` (default Notebook) | Manifest:61-71; `MainActivity.java:139-147, 223-236`; `AppSettings.java:780-782` |
| Main (any tab) | bottom-nav item or horizontal swipe | ViewPager2 + FragmentStateAdapter (lazy `ensureRealized`) | tab 0 Notebook, 1 To-Do, 2 QuickNote, 3 More | `MainActivity.java:93-116, 391-397, 443-456, 497-561` |
| Main | Back | `MainActivity.onBackPressed` → tab fragment `onBackPressed` (Notebook: folder history) → finish | previous folder or S_EXIT | `MainActivity.java:374-380`; `GsFileBrowserFragment.java:313-318` |
| Main (toolbar) | tap / long-press | `GsActivityBase.onToolbarClick`/`LongClick` → visible resumed `GsFragmentBase` | Notebook: filter dialog; editor: format title action / jump top-bottom | `GsActivityBase.java:116-135`; `GsFileBrowserFragment.java:175-178`; `DocumentEditAndViewFragment.java:1090-1102` |
| Notebook | tap file | adapter `onClick` → `GsFileBrowserFragment.onFsViewerSelected` → `MainActivity$2.onFsViewerSelected` → `DocumentActivity.launch` | DocumentActivity, MainActivity (folder), installer (.apk), or "Open with" dialog | `GsFileBrowserListAdapter.java:404-446`; `MainActivity.java:489-491`; `DocumentActivity.java:64-117` |
| Notebook | FAB / long-press FAB | `onClickFab` → `NewFileDialog.show`; `onLongClickFab` cycles Recent/Favourites/previous | S_DLG_NEW_FILE → callback → DocumentActivity | `MainActivity.java:322-371` |
| Notebook | overflow → Settings | `MainActivity.onOptionsItemSelected` (item made visible by `GsFileBrowserFragment.java:280`) | SettingsActivity | `MainActivity.java:259-266` |
| More | "Settings" row | `animateToActivity(..., 124)` | SettingsActivity | `MoreInfoFragment.java:66-68` |
| More | other rows | external browser or HTML dialogs | S_EXTERNAL / S_MORE_* | `MoreInfoFragment.java:59-136` |
| Editor (Main tab or Document) | menu "File browser" | `MainActivity.launch(file)` after 250 ms | MainActivity showing the file | `DocumentEditAndViewFragment.java:628-631`; `MainActivity.java:238-245` |
| Editor | menu Preview/Edit, Ctrl+/, swipe (experimental) | `setViewModeVisibility` → `supportInvalidateOptionsMenu` | view or edit mode of the same page | `DocumentEditAndViewFragment.java:454-465, 1049-1078`; `DocumentActivity.java:258-283` |
| Editor | action button | `ActionButtonBase.appendActionButtonToBar` click/long-click → `onActionClick`/`onActionLongClick` (format override, else `runCommonAction`) | dialogs, other documents, external apps | `ActionButtonBase.java:99-108, 343-374, 640-858` |
| DocumentActivity | Back | top fragment `onBackPressed`, else `finishAndRemoveTask` | caller (Main) or S_EXIT. FW-MEMORY: for a non-root activity `finishAndRemoveTask` finishes only that activity | `DocumentActivity.java:317-336` |
| Settings | tap sub-screen | `onPreferenceStartScreen` swaps the screen in place (back stack list) | sub-screen; Back → `goBack` | `GsPreferenceFragmentBase.java:343-350, 433-441`; `SettingsActivity.java:134-140` |
| Settings | "Reorder actions" (6 formats) | `startActivity` with `EXTRA_FORMAT_KEY` | ActionButtonSettingsActivity | `SettingsActivity.java:365-372` |
| Settings | Up / Back from root | `onBackPressed` | Main (recreated if `isRecreateMainRequired`) | `SettingsActivity.java:79, 134-140`; `MainActivity.java:285-293` |
| Widget / shortcut | tap | PendingIntent / shortcut intent → trampoline | DocumentActivity, or Main for folders | §1.2 |
| External app | SEND/VIEW/EDIT | intent filters | DocumentActivity → share-into or editor | `DocumentActivity.java:158-232` |

### 3.3 Modes per window

| Window | Mode variable | What it changes | Evidence |
|---|---|---|---|
| MainActivity | current tab | FAB only on Notebook; menu = `main__menu` + tab fragment menu (FW-MEMORY: ViewPager2 sets menu visibility for the primary item); Back and toolbar routed to the tab | `MainActivity.java:443-456, 523-524, 374-380` |
| MainActivity | tab realized or placeholder | first visit creates the real fragment | `MainActivity.java:509-561` |
| GsFileBrowserFragment | selection count 0 / 1 / ≥2 and its types (files only, dirs only, text, writable, favourites), folder virtual (root, Recent, Favourites, Popular), SAF folder, sortable | visibility of 16 menu items, subtitle `(n / total)`, Settings item | `GsFileBrowserFragment.java:245-311` |
| GsFileBrowserListAdapter | `areItemsSelected` | row tap toggles selection instead of opening | `GsFileBrowserListAdapter.java:404-446, 496-526` |
| Notebook / Main | current folder writable | FAB opens NewFileDialog or jumps to the notebook folder; SAF → mount dialog | `MainActivity.java:343-362` |
| Notebook | folder empty | only ".." row plus empty hint | `GsFileBrowserFragment.java:230-237`; `GsFileBrowserListAdapter.java:186-188` |
| DocumentEditAndViewFragment | `_isPreviewVisible` (edit / view) | menu: undo, redo, save, preview vs edit, search vs SearchView, Format submenu; action bar `DisplayMode.EDIT`/`VIEW` | `DocumentEditAndViewFragment.java:299-337, 1049-1078` |
| " | `isText` (binary file) | text menus hidden, view forced | `:306, 1055` |
| " | format id | highlighter, auto-format filter/watcher, action buttons, title tap, `onSearch`, key handling | `:649-668`; `FormatRegistry.java:128-215` |
| " | hosted in Main or DocumentActivity | "Send debug log" only in DocumentActivity, edit mode, `IS_DEBUG_ENABLED` (true in this build, `MainActivity.java:78`); wrap forced in Main; title set only in DocumentActivity | `:170, 200, 310` |
| " | can undo / redo, text changed | enabled state and alpha of undo/redo/save | `:363-376, 638-645` |
| " | experimental features (default on) | "Convert & load epub" item; extra settings | `:329`; `AppSettings.java:921-923` |
| " | find bar shown, replace row shown | TextSearchFragment handlers | `TextSearchFragment.java:281-299, 346-375` |
| HighlightingEditor | non-empty selection | floating ActionMode with "☰" (FW-MEMORY trigger) | `HighlightingEditor.java:570-600` |
| DocumentActivity | current fragment (editor or share-into) | handlers, title | `DocumentActivity.java:172-180, 304-307` |
| DocumentShareIntoFragment | shared text vs file; text has links; most recent file exists | "as link" checkbox; options shading | `DocumentShareIntoFragment.java:90-180, 254-278` |
| SettingsActivity | current PreferenceScreen; experimental; API | visible preferences (multi-window API ≥ 21, password API ≥ 23) | `SettingsActivity.java:157-205` |
| IntroActivity | slide index | Next vs Done (FW-MEMORY) | `IntroActivity.java:45-57` |
| StoragePermissionActivity | permission granted | proceed or ask again | `StoragePermissionActivity.java:44-57` |
| GsFileBrowserDialog | `doSelectFile` / `Folder` / `Multiple`, items selected, search field visible, neutral button | OK visibility, filtering, neutral action | `GsFileBrowserDialog.java:110-190, 209-241, 305-317` |
| NewFileDialog | password set and API ≥ 23; experimental; `allowCreateDir`; name exists | encrypt checkbox, BOM checkbox, "Folder" button, red title | `NewFileDialog.java:117, 124, 362-364, 267` |
| GsSearchOrCustomTextDialog | `selectionMode` SINGLE/MULTIPLE/NONE, `isSearchEnabled`, neutral button | OK and neutral handlers, filter | `GsSearchOrCustomTextDialog.java:104-150` |
| ActionButtonSettingsActivity | format key | list content | `ActionButtonSettingsActivity.java:118-140` |

### 3.4 Candidate page list (109 pages)

"Area" is the owning area from §6. "Base" is the baseline reach: M = Monkey, A = APE, – = neither, ? = could not be decided from class-level data.

| # | Page | Description | Window class | Mode predicate / guard | Area | Base |
|---|---|---|---|---|---|---|
| 1 | S_ENTRY | Outside the app (launcher, home, adb, other apps); search root | – | – | SHELL | n/a |
| 2 | S_EXIT | App closed (root finished or task removed); process and statics may survive | – | – | SHELL | n/a |
| 3 | S_EXTERNAL | Foreign window on top: browser/Custom Tab, chooser, mail, calendar, print, camera, gallery, recorder, installer, system permission or SAF picker | other package | returns by Back / RESULT | SHELL | n/a |
| 4 | S_HOME_WIDGETS | Home screen with the files and/or To-Do widget placed | launcher + RemoteViews | widget placed | SHELL | – |
| 5 | S_LAUNCHER_SHORTCUTS | Launcher long-press shortcuts (To-Do, QuickNote, last document) or a pinned shortcut | launcher | API ≥ 25 / shortcut created | SHELL | – |
| 6 | S_INTRO | Intro slides 1-4 (Next, swipe, Back) | IntroActivity | slide < 5 | SHELL | MA |
| 7 | S_INTRO_LAST | Intro slide 5 (Done) | IntroActivity | slide = 5 | SHELL | MA |
| 8 | S_PERMISSION | Storage-permission AlertDialog (Exit / Yes) | StoragePermissionActivity | !checkExternalStoragePermission | SHELL | – |
| 9 | S_MAIN_CHANGELOG | Licence + changelog HTML dialog over Main | AlertDialog | intro done and first resume of versionCode 260902 | SHELL | MA |
| 10 | S_MAIN_RATE | gene-rate rating prompt over Main | library | ≥4 launches, ≥30 min | SHELL | ? |
| 11 | S_MAIN_MORE | Main, More tab (MoreInfoFragment list) | MoreFragment / MoreInfoFragment | tab = More | SHELL | MA |
| 12 | S_MORE_HTML | HTML dialog (licences, contributors, changelog) | AlertDialog | – | SHELL | MA |
| 13 | S_MORE_LICENSE | `license.txt` in a WebView dialog | AlertDialog | – | SHELL | M |
| 14 | S_SETTINGS | Settings root (sub-screen links, Theme, Language) | SettingsActivity / SettingsFragmentMaster | screen = root | SHELL | MA |
| 15 | S_SETTINGS_GENERAL | General (paths, start tab/folder, password, search, features) | " | screen = General | SHELL | MA |
| 16 | S_SETTINGS_OTHER | Other (UI flags, share format, attachments, snippets, Custom Tabs, backup/restore) | " | screen = Other | SHELL | ? |
| 17 | S_SETTINGS_EDITOR | Edit mode (font, size, highlighting, spacing*, padding, line breaking, list character) | " | screen = Edit mode | SHELL | ? |
| 18 | S_SETTINGS_COLORS | Basic color scheme (4 colors, 7 presets) | " | nested in Edit mode | SHELL | ? |
| 19 | S_SETTINGS_VIEW | View mode (preview first, swipe*, inject, link color, RTL, font size) | " | screen = View mode | SHELL | ? |
| 20 | S_SETTINGS_MD | Markdown settings | " | – | SHELL | A |
| 21 | S_SETTINGS_TODO | todo.txt settings | " | – | SHELL | ? |
| 22 | S_SETTINGS_WIKI | Wikitext settings | " | – | SHELL | ? |
| 23 | S_SETTINGS_PLAIN | Plaintext settings | " | – | SHELL | ? |
| 24 | S_SETTINGS_ADOC | AsciiDoc settings | " | – | SHELL | ? |
| 25 | S_SETTINGS_ORG | Orgmode settings | " | – | SHELL | ? |
| 26 | S_DLG_PREF_LIST | ListPreference dialog (@KEY: start tab, start folder, depth, nav color, list char, theme, language, font) | preference dialog | – | SHELL | MA |
| 27 | S_DLG_PREF_MULTI | MultiSelectListPreference (TOC levels) | " | – | SHELL | ? |
| 28 | S_DLG_PREF_TEXT | EditTextPreference dialog (@KEY) | " | – | SHELL | ? |
| 29 | S_DLG_COLOR | ColorPreference picker (@KEY) | rarepebble | – | SHELL | ? |
| 30 | S_ACTION_ORDER | Reorder/enable action buttons of one format; menu Reset; drag | ActionButtonSettingsActivity | EXTRA_FORMAT_KEY | SHELL | A |
| 31 | S_WIDGET_CONFIG | Blank activity hosting S_FSDLG_FOLDER@WIDGET_DIR | WrWidgetConfigure | valid EXTRA_APPWIDGET_ID | SHELL | – |
| 32 | S_MAIN_PAUSED | Main stopped (child activity, external app, Home) | MainActivity | – | SHELL | n/a |
| 33 | S_SETTINGS_PAUSED | Settings stopped | SettingsActivity | – | SHELL | n/a |
| 34 | S_ACTION_ORDER_PAUSED | ActionButtonSettings stopped | – | – | SHELL | n/a |
| 35 | S_INTRO_PAUSED | Intro stopped (Home) | – | – | SHELL | n/a |
| 36 | S_PERMISSION_PAUSED | Permission activity under the system dialog | – | – | SHELL | n/a |
| 37 | S_NB_BROWSE | Notebook tab, real folder with entries, no selection | GsFileBrowserFragment in MainActivity | sel = 0, not virtual, entries ≥ 1 | FILES | MA |
| 38 | S_NB_EMPTY | Notebook tab, empty folder (".." plus hint), fresh-install state | " | `adapterData.size() < 2` | FILES | MA |
| 39 | S_NB_VIRTUAL | /storage root, Recent, Favourites or Popular (search/import hidden) | " | `isCurrentFolderVirtual` | FILES | ? |
| 40 | S_NB_SELECT1 | Exactly one entry selected (rename, info, delete, favourite, clipboard, shortcut, move, copy, share) | " | sel = 1 | FILES | A |
| 41 | S_NB_SELECTN | Two or more selected (delete, move, copy, share, favourite, select all, clear) | " | sel ≥ 2 | FILES | ? |
| 42 | S_DLG_NEW_FILE | New file/folder dialog (@MAIN with Folder button, @SHARE without) | NewFileDialog | allowCreateDir, password, experimental | FILES | A |
| 43 | S_POPUP_TITLE_FORMATS | Saved title-format list | ListPopupWindow | – | FILES | A |
| 44 | S_POPUP_TEMPLATE_NAME | "Use template name" popup | PopupWindow | template chosen after 2 spinner events | FILES | A |
| 45 | S_DLG_RENAME | Rename file/folder | WrRenameDialog | single writable selection, not virtual | FILES | – |
| 46 | S_DLG_RENAME_CLASH | Name-clash dialog during rename | AlertDialog | target exists | FILES | – |
| 47 | S_DLG_FILE_INFO | File details (@NB from selection, @DOC from editor menu) | FileInfoDialog | – | FILES | MA |
| 48 | S_DLG_FILE_SEARCH | File search options | FileSearchDialog | not already searching | FILES | MA |
| 49 | S_FILE_SEARCH_RUNNING | Snackbar while `QueueSearchFilesTask` runs | Snackbar | `isSearchExecuting` | FILES | A |
| 50 | S_DLG_SEARCH_RESULTS | Expandable results (files, matching lines) | FileSearchResultSelectorDialog | results ready | FILES | A |
| 51 | S_FSDLG_FOLDER | Folder picker (@MOVE, @COPY, @NOTEBOOK_DIR, @SNIPPET_DIR, @BACKUP_WRITE, @WIDGET_DIR) | GsFileBrowserDialog | doSelectFolder | FILES | MA |
| 52 | S_FSDLG_FILE | File picker (@QUICKNOTE_FILE, @TODO_FILE, @BACKUP_READ, @ATTACH, @EPUB, @SHARE_TARGET) | GsFileBrowserDialog | doSelectFile && !multiple | FILES | MA |
| 53 | S_FSDLG_MULTI | Multi-select picker (@IMPORT) | GsFileBrowserDialog | doSelectMultiple | FILES | MA |
| 54 | S_FSDLG_FILTER | Any picker with the filter field shown | GsFileBrowserDialog | search field visible | FILES | M |
| 55 | S_DLG_MOUNT_SD | SAF "mount storage" explanation | AlertDialog (GsContextUtils) | SAF folder, no tree URI | FILES | – |
| 56 | S_DOC_EDIT_MD | DocumentActivity, edit, Markdown action bar | DocumentActivity + DocumentEditAndViewFragment | !preview, format = markdown | EDITOR | A |
| 57 | S_DOC_EDIT_TODO | Edit, todo.txt action bar | " | format = todotxt | EDITOR | ? |
| 58 | S_DOC_EDIT_WIKI | Edit, Zim wikitext | " | format = wikitext | EDITOR | – |
| 59 | S_DOC_EDIT_ADOC | Edit, AsciiDoc | " | format = asciidoc | EDITOR | A |
| 60 | S_DOC_EDIT_ORG | Edit, Org | " | format = orgmode | EDITOR | A |
| 61 | S_DOC_EDIT_PLAIN | Edit, plaintext, CSV or key-value (PlaintextActionButtons) | " | format ∈ {plain, csv, keyvalue} | EDITOR | ? |
| 62 | S_DOC_VIEW | View mode (WebView), @FORMAT | " | preview && isText | EDITOR | A |
| 63 | S_DOC_VIEW_BINARY | Image/audio/video viewer | " | `isBinaryFileNoTextLoading` | EDITOR | – |
| 64 | S_DOC_SELECT | Edit mode with text-selection ActionMode (@MAIN variant) | HighlightingEditor ActionMode | selection non-empty | EDITOR | – |
| 65 | S_DOC_FIND | Find bar (prev/next, toggles, filter, close) (@MAIN) | TextSearchFragment | shown, replace hidden | EDITOR | MA |
| 66 | S_DOC_FIND_REPLACE | Find bar with replace row (@MAIN) | TextSearchFragment | replace visible | EDITOR | A |
| 67 | S_DOC_VIEW_FIND | View mode with SearchView expanded | SearchView + WebView find | preview, SearchView open | EDITOR | A |
| 68 | S_MAIN_TODO_EDIT | Main To-Do tab, edit | DocumentEditAndViewFragment in MainActivity | tab = To-Do, !preview | EDITOR | MA |
| 69 | S_MAIN_TODO_VIEW | Main To-Do tab, view | " | tab = To-Do, preview | EDITOR | A |
| 70 | S_MAIN_QN_EDIT | Main QuickNote tab, edit | " | tab = QuickNote, !preview | EDITOR | MA |
| 71 | S_MAIN_QN_VIEW | Main QuickNote tab, view | " | tab = QuickNote, preview | EDITOR | A |
| 72 | S_DOC_NOT_SUPPORTED | "Cannot open" dialog; dismiss finishes | AlertDialog | file null or not writable | EDITOR | – |
| 73 | S_DOC_OPEN_WITH | "Open with" (Markor / other app) | AlertDialog | unsupported extension but plain text | EDITOR | – |
| 74 | S_SHARE_INTO | Share-into: editable text + options (QuickNote, To-Do, recent, select/create, search, re-share, clipboard, browser, calendar) | DocumentShareIntoFragment | SEND / PROCESS_TEXT | EDITOR | – |
| 75 | S_DLG_SEARCH_REPLACE | Search & replace | SearchAndReplaceTextDialog | – | EDITOR | A |
| 76 | S_POPUP_RECENT_REPLACES | Recent replaces popup | ListPopupWindow | recents exist | EDITOR | ? |
| 77 | S_DLG_SPEED_READ | Speed-read dialog (Tools) | AlertDialog | – | EDITOR | A |
| 78 | S_DOC_PAUSED | DocumentActivity stopped | – | – | EDITOR | n/a |
| 79 | S_DLG_FONT_SIZE | Font-size list (edit or view size) | GsSearchOrCustomTextDialog | – | ACTIONS | MA |
| 80 | S_DLG_HEADLINE | Headings list (title tap, Markdown/Wikitext) | " | format md/wiki | ACTIONS | MA |
| 81 | S_DLG_SPECIAL_KEY | Special keys (common action) | " | – | ACTIONS | MA |
| 82 | S_DLG_ADOC_KEY | AsciiDoc special keys | " | asciidoc | ACTIONS | – |
| 83 | S_DLG_SNIPPET | Insert snippet (`.app/snippets`) | " | – | ACTIONS | – |
| 84 | S_DLG_DATETIME | Date/time format dialog | DatetimeFormatDialog | – | ACTIONS | MA |
| 85 | S_POPUP_DATETIME | Format list popup | ListPopupWindow | – | ACTIONS | ? |
| 86 | S_SYS_DATE | Date picker (from datetime dialog) | DatePickerDialog | – | ACTIONS | – |
| 87 | S_SYS_TIME | Time picker | TimePickerDialog | – | ACTIONS | – |
| 88 | S_DLG_ATTACH | Insert image/link/audio (@IMAGE, @LINK, @AUDIO) | AttachLinkOrFileDialog | – | ACTIONS | M |
| 89 | S_DLG_SPECIAL_FILE | Pick a special file / glob (from attach) | GsSearchOrCustomTextDialog | – | ACTIONS | – |
| 90 | S_DLG_CASE | Text-case options | " | – | ACTIONS | A |
| 91 | S_DLG_INDENT | Indent size (long-press indent) | " | – | ACTIONS | A |
| 92 | S_DLG_TABLE | Insert table row/header (Markdown) | " | md | ACTIONS | – |
| 93 | S_DLG_CHECKLIST | Markdown checklist dialog | " | md | ACTIONS | A |
| 94 | S_DLG_STT_PRIORITY | Priority list | " | todo | ACTIONS | – |
| 95 | S_DLG_STT_SORT | Sort-by list | " | todo | ACTIONS | A |
| 96 | S_DLG_STT_ARCHIVE | Archive file name | " | todo | ACTIONS | – |
| 97 | S_DLG_STT_DATE | Due-date picker with Clear | TodoTxtActionButtons$DateFragment | todo | ACTIONS | – |
| 98 | S_DLG_STT_UPDATE | Add/remove contexts or projects (@CONTEXT, @PROJECT) | GsSearchOrCustomTextDialog | todo | ACTIONS | – |
| 99 | S_DLG_STT_FILTER | Browse/filter menu (title tap) | " | todo | ACTIONS | MA |
| 100 | S_DLG_STT_KEYS | Browse by context, project, priority or due (@TYPE) | " | todo | ACTIONS | M |
| 101 | S_DLG_STT_LINES | Matching-task list (@FILTER, @KEYS, @SEARCH, @VIEW) | " | todo | ACTIONS | A |
| 102 | S_DLG_STT_SAVE_QUERY | Save-query name | " | todo | ACTIONS | – |
| 103 | S_DLG_TEXT_LINES | Matching lines (find-bar filter button) | " | – | ACTIONS | A |
| 104 | S_DLG_CONFIRM | Confirm (@DELETE, @OVERWRITE, @STT_DELETE_VIEW) | " | – | ACTIONS | A |
| 105 | S_DLG_COPY_MOVE_CONFLICT | Target exists during move/copy | " | – | ACTIONS | – |
| 106 | S_DLG_FOLDER_SORT | Sort options of a folder | " | – | ACTIONS | A |
| 107 | S_DLG_NB_FILTER | Notebook quick filter (toolbar tap) | " | – | ACTIONS | A |
| 108 | S_DLG_SET_PASSWORD | Encryption password | AlertDialog | API ≥ 23 | ACTIONS | – |
| 109 | S_DLG_NEW_DIR | New folder name (picker button) | GsSearchOrCustomTextDialog | – | ACTIONS | M |

`*` = visible only with experimental features, which default to on in this build. RENDER and INFRA own no pages: their methods are reached through CALL and FRAMEWORK edges.

### 3.5 Variants

- **Shared dialogs.** Use `@CALLER` variants for the shared dialogs whose result goes back to different callers:
  - `GsFileBrowserDialog.onFsViewerSelected@NOTEBOOK_DIR` vs `@IMPORT`, and so on;
  - `GsSearchOrCustomTextDialog.<handler>@HEADLINE` vs `@STT_FILTER`;
  - `FileInfoDialog.*@NB` vs `@DOC`;
  - `NewFileDialog.callback@MAIN` vs `@SHARE`.
- **Format-specific handlers.** Use `@MD` / `@TODO` / … for `DocumentEditAndViewFragment.onToolbarClicked` and `onOptionsItemSelected` when the format changes the continuation.
- **Embed-binary menu item.** The Format submenu contains `@string/action_format_embedbinary` (`res/menu/document__edit__menu.xml:144-147`), but `onOptionsItemSelected` has no case for it (`DocumentEditAndViewFragment.java:525-532`), so that item falls to `default`.

---

## 4. Framework mechanisms that need FRAMEWORK, ASYNC or LIFECYCLE edges

| Mechanism | App classes / call sites | Notes |
|---|---|---|
| ViewPager2 + FragmentStateAdapter | `MainActivity$SectionsPagerAdapter` (`createFragment`, `getItemCount`, `getItemId`, `containsItem`), `MainActivity$1.onPageSelected` | Lazy realization through `notifyItemChanged` (`MainActivity.java:497-561`); reflection on touch slop (205-221) |
| RecyclerView adapters | `GsFileBrowserListAdapter` (`onCreateViewHolder`/`onBindViewHolder`/`getItemId`/`onAttachedToRecyclerView`), `ActionButtonSettingsActivity$OrderAdapter`, `GsPreferenceFragmentBase$DividerDecoration.getItemOffsets` | Row listeners are registered in `onBindViewHolder` (`GsFileBrowserListAdapter.java:265-272`) |
| BaseAdapter / ExpandableListAdapter / ArrayAdapter / Filter | `GsSearchOrCustomTextDialog$Adapter`, `FileSearchResultSelectorDialog$ExpandableSearchResultsListAdapter`, `GsFileBrowserListAdapter$StringFilter` (`performFiltering` on a worker, `publishResults` on main; FW-MEMORY) | Child methods of the expandable adapter run only when a group is expanded |
| ItemTouchHelper | `ActionButtonSettingsActivity$ReorderCallback` (`onMove`, `onSwiped`, `onSelectedChanged`, `clearView`) | Swipe is disabled (`ActionButtonSettingsActivity.java:236-240`), so `onSwiped` is FRAMEWORK_ONLY |
| Executors / threads | `GsFileBrowserListAdapter` (static pool, `_loadFolder` → `_recyclerView.post`, 644-779); `HighlightingEditor` pool for highlighting (73, 203-226); delete thread (`GsFileBrowserFragment.java:431-434`); todo sort thread (`TodoTxtActionButtons.java:121-131`) → `setEditorTextAsync` → `runOnUiThread` (`ActionButtonBase.java:624-626`) | ASYNC edges |
| AsyncTask | `FileSearchEngine$QueueSearchFilesTask` (`onPreExecute` 157, `doInBackground` 193, `onProgressUpdate` 263, `onPostExecute` 272, `onCancelled` 287) and a Snackbar callback | Static `isSearchExecuting`/`activity` state survives the activity (`FileSearchEngine.java:47-48`) |
| Handler / debounce | `TextViewUtils.makeDebounced` (745-760) used by the editor watcher (`DocumentEditAndViewFragment.java:207-210`), find bar, search dialogs and highlighting; `GsActivityBase.onPostResume` posts `onActivityFirstTimeVisible` (102-110); `GsFragmentBase` posts `checkRunFirstTimeVisible` (79-82, 152-163); repeat buttons (`ActionButtonBase.java:311-338`); share PDF/image 7 s delay (`DocumentEditAndViewFragment.java:501-523`) | ASYNC edges with delays |
| Text watchers, input filters, spans | `HighlightingEditor` watcher (94-109), `LineNumbersView$LineNumbersDrawer$1/2`, `TextViewUndoRedo$EditTextChangeListener`, `ListHandler`, `AutoTextFormatter` / `TodoTxtAutoTextFormatter` (InputFilter), `GsTextWatcherAdapter`, `NewFileDialog`, `WrRenameDialog`, `TextSearchFragment`, `SearchAndReplaceTextDialog`; spans `SyntaxHighlighterBase$HighlightSpan.updateDrawState`, `TodoTxtSyntaxHighlighter$ParagraphDividerSpan`, `ColorUnderlineSpan`, `WrProportionalHeaderSpanCreator$LargerHeaderSpan`, `GsFontPreferenceCompat$TypefaceObjectSpan` | `setText` and `insert` fire the watchers (FRAMEWORK); spans are called during layout and draw |
| Custom views (framework overrides) | `HighlightingEditor` (`onPreDraw`, `onDraw`, `onSelectionChanged`, `onTextContextMenuItem`, `setText`, `onSaveInstanceState`, …), `LineNumbersView.onDraw`, `DraggableScrollbarScrollView`/`DraggableScrollbarWebView` (touch), `GsHorizontalScrollView`, `GsLinearSplitLayout.addView` (share-into layout), `NewFileDialog$ReselectSpinner.setSelection` | Inflation uses the 2-arg constructors; other constructors are never called |
| ViewTreeObserver | `HighlightingEditor` scroll and global-layout listeners (115-116); window-focus listener (`DocumentEditAndViewFragment.java:222-232`); `AndroidBug5497Workaround$1.onGlobalLayout` (only with "hide status bar") | FRAMEWORK |
| WebView | `DocumentEditAndViewFragment.setupWebViewIfNeeded` (1004-1047): `GsWebViewChromeClient` (`onShowCustomView`/`onHideCustomView`), `MarkorWebViewClient.shouldOverrideUrlLoading` → `DocumentActivity.launch` or browser, `GsWebViewClient.onPageFinished`; long-press copies a link; SearchView `findAllAsync`; `evaluateJavascript` for wrap and line numbers; JS interface "Android" → `webViewJavascriptCallback` (1081-1088) | No bundled JS calls the bridge (grep of assets and Java); only user document content could call it |
| Converters and parser callbacks | `TextConverterBase.convertMarkupShowInWebView` and subclasses; flexmark parser and renderer with `MarkdownTextConverter$LineNumberIdExtension`/`$…Provider*` and `other.com.vladsch.flexmark.ext.katex.*` (library callbacks) | Library → app FRAMEWORK edges |
| Preferences | `GsPreferenceFragmentBase` (`onPreferenceTreeClick`, `onPreferenceStartScreen`, `onDisplayPreferenceDialog`, `onSharedPreferenceChanged`, listener registered in `onResume` 272-279); `GsFontPreferenceCompat`, `GsLanguagePreferenceCompat`; rarepebble `ColorPreference` | Change listeners fire only on a value change (FW-MEMORY) |
| Data layer | SharedPreferences only: "app" (`AppSettings` via `GsSharedPreferencesPropertyBackend`, `SHARED_PREF_APP = "app"`, 62), "cache", "history" (`AppSettings.java:74-75`), `DOCUMENT_MOD_TIMES` (`Document.java:50`), `action_order` (`ActionButtonBase.java:85`), `MARKOR_WIDGET_PREF` (`WrWidgetConfigure.java:31`), default prefs (intro flag, SAF URI); file I/O in `Document.loadContent`/`saveContent` and `GsFileUtils`; Keystore in `PasswordStore` | No SQLite, Room, ContentProvider or LiveData/ViewModel |
| Activity results / pickers / SAF | `GsContextUtils.extractResultFromActivityResult` (1823-1906): camera, gallery `ACTION_PICK`, `RECORD_SOUND`, `OPEN_DOCUMENT_TREE` (2085-2094), storage permission; called from `MainActivity`/`DocumentActivity.onActivityResult` (585-589 / 285-288) | RESULT edges; `sendPathCallback` delivers back to `AttachLinkOrFileDialog` |
| Outgoing intents | `shareText`/`shareStream`/`shareStreamMultiple` (1233-1287), calendar (1289), `viewFileInOtherApp` (1337), APK install (1370-1402), `draftEmail` (1559), browser/Custom Tabs (592), print/PDF (`print` 1445, `printOrCreatePdfFromWebview`) | INTENT edges to S_EXTERNAL |
| Widgets | `WrMarkorWidgetProvider`, `WrFilesWidgetService` → `WrFilesWidgetFactory` (RemoteViewsFactory), `WrWidgetConfigure`; `TodoWidgetProvider`, `TodoWidgetService` → `TodoWidgetRemoteViewsFactory` | Factory methods are called by the launcher host process |
| Shortcuts / launcher components | `ShortcutUtils` (ShortcutManager), `GsContextUtils.createLauncherDesktopShortcut`, `setLauncherActivityEnabled` (1162) | – |
| Libraries with callbacks | AppIntro (`onDonePressed`, `onNextPressed`, `onSlideChanged`, `onSkipPressed`), gene-rate (`MainActivity.lambda$optShowRate$2`), Material BottomNavigation listener (`MainActivity.java:109-114`) | FW-MEMORY behaviour |
| Not present | LiveData, ViewModel, RxJava, WorkManager, JobScheduler, notifications, bound or foreground services, data binding, dynamic BroadcastReceivers in use | `AlarmManager` appears only in the uncalled `GsContextUtils.restartApp` (490-505); the local-broadcast helpers are uncalled (1919-1960) |

---

## 5. Unreachable-code candidates (evidence only, no final verdicts)

Method: a comment- and string-aware search of all 139 compiled source files for call sites (`name(` and `::name`) excluding the declaration line. A name match anywhere counts as a caller, so false negatives are possible (a same-named method elsewhere hides a dead one). Listed methods were also never hit by either tool.

### 5.1 Whole classes with no reference outside their own file (46 methods, all unhit)

- `GsPermissionChecker` (5), `GsNanoProfiler` (8), `GsNetworkUtils` (16; only self-calls), `GsMapPropertyBackend` (17).
- `BuildConfig` (2): generated; never appears in any execution-data segment. Exclude it.

### 5.2 Methods with no call site (118; DEAD candidates)

- SHELL: `MainActivity.getPosTitle:408`; `GsFontPreferenceCompat` get/set FontNames/Values (165-177); `GsLanguagePreferenceCompat` get/set SystemLanguageName/DefaultLanguageCode (184-197).
- FILES: `GsFileBrowserFragment.getOptions:607`; `GsFileBrowserListAdapter.getPathLevel:392`, `toggleSelectionAll:448`, `doAfterChange:606` (so `$1.onLayoutChange` is dead too), `getFsOptions:809`, `isCurrentFolderHome:813`; `WrMarkorSingleton.getNotesLastDirectory:43`, `setNotesLastDirectory:47`, `isDirectoryEmpty:177`.
- EDITOR:
  - `DocumentActivity.isDocumentAlreadyOpen:235`; `DocumentShareIntoFragment$ShareIntoImportOptionsFragment.addDocumentToPrefgroup:593`;
  - `DocumentEditAndViewFragment.webViewJavascriptCallback:1082`: JS-only and not called by any bundled script; a fixture document with inline JS could reach it, and whether the bridge converts a JS array to `String[]` is UNVERIFIED;
  - `DraggableScrollbarScrollView.slowScrollShift/setFastScrollEnabled/isFastScrollEnabled` (30-98); `DraggableScrollbarWebView.setFastScrollEnabled/isFastScrollEnabled/scrollAnimatedToXY` (89-103);
  - `TextViewUtils.isViewVisible:778`; `TextViewUndoRedo.undoRedoPrefKeyForFile:101`, `storePersistentState:221`, `restorePersistentState:249`; `Document.getFileExtension:153`, `filenameFromContent:375`.
- ACTIONS: `MarkorDialogFactory.showColorSelectionModeDialog:485`, `showInsertItemsDialog:593`; `TodoTxtTask$SttTaskSimpleComparator.compareDone:359`; `WikitextActionButtons.createWikitextHeaderAndTitleContents:231`; `WikitextLinkResolver.getNotebookRootDir:182`.
- RENDER: `SyntaxHighlighterBase.getDefaultHighlighter:105`, `getSpannable:274`; `AutoTextFormatter$ListLine.isSiblingLevelOf:117`; `FlexmarkKatexExtension$KatexVisitorExt.VISIT_HANDLERS:239`.
- INFRA:
  - `AppSettings` (14): `isLoadLastDirectoryAtStartup:86`, `isDynamicHighlightingEnabled:183`, `isHighlightingHexColorEnabled:339`, `isEditorStartOnBotttom:367`, `getLastEditScrollY:474`, `setLastViewPosition:482`, `getLastViewPositionX/Y:611/618`, `set/isFileBrowserSortFolderFirst:796/802`, `getNavigationBarColor:806`, `getRating/setRating:889/893`, `getFileBrowserLastBrowsedFolder:995`;
  - `GsSharedPreferencesPropertyBackend` (6): `isKeyEqual:86`, `getDefaultPreferences:123`, `getDefaultPreferencesEditor:127`, `getDefaultPreferencesName:131`, `rstrs:167`, `afterDaysTrue:591`;
  - `GsContextUtils` (39), among them `restartApp:490`, `isConnectedToInternet:465`, `isWifiConnected:1076`, `createPdf:1478`, `sendLocalBroadcastWithStringExtra:1919`, `receiveResultFromLocalBroadcast:1933` (so `$1.onReceive:1940` is dead too), `callTelephoneNumber:2338`, `showSnackBar` ×2, `toggleStatusbarVisibility:2617`, `isInSplitScreenMode:2744`, `removeActivityFromHistory:2806`, `stopBlinking:2930`, `createLauncherDesktopShortcutLegacy:1213`, `getApplicationObject:339`, `isGooglePlayBuild:429`, `isFossBuild:436`;
  - `GsFileUtils` (7): `readTextFile:149`, `readBinaryFile:197`, `fileContains:337`, `hasExtension:371`, `hash:656`, `getPrefix:779`, `isUriOrFilePath:937`;
  - `GsTextUtils` (5); `GsCollectionUtils.listComp:78`, `all:182`; `GsHashMap.limitSizeByRemovingOldest:64`; `GsSimpleMarkdownParser.setHtml:225`; `GsPreferenceFragmentBase.restartActivity:510`.
- Not covered by this search: lambdas and constructors. Check by hand the unused view and preference constructors: the 1-, 3- and 4-arg `GsFontPreferenceCompat`/`GsLanguagePreferenceCompat`, `NewFileDialog$ReselectSpinner` `<init>:408/416`, `DraggableScrollbarScrollView` `<init>:22` and 2 of 3 `DraggableScrollbarWebView` constructors. Inflation calls the (Context, AttributeSet) constructor (FW-MEMORY).

### 5.3 Framework-callback implementations that no known path triggers (100; FRAMEWORK_ONLY or env-gated candidates)

- **`GsMenuItemDummy`** (23) and **`GsMenuItemDummy$Menu`** (13): placeholder `Menu` in `GsFragmentBase._fragmentMenu` (`GsFragmentBase.java:46`); only `<init>`, `findItem` and similar run.
- `GsAndroidSpinnerOnItemSelectedAdapter.onNothingSelected:30` and `FileSearchDialog$1.onNothingSelected:93`; `ReorderCallback.onSwiped:257` (swipe disabled); `GsFileUtils$1.visitFile:1007`.
- The flexmark `KatexDisplayMath`/`KatexInlineMath` node accessors (12) and `KatexOptions.setIn:449` are library-called. Real KaTeX use needs math in a Markdown document with "render math" on.
- Environment-gated rather than dead:
  - `HighlightingEditor$2` ActionMode (4) needs a text selection;
  - `MarkorWebViewClient.shouldOverrideUrlLoading` needs a link tap;
  - `GsWebViewChromeClient.onShowCustomView` needs a full-screen video;
  - the expandable-list child methods (10) need a group expanded;
  - the widget factories and services (12) need a placed widget;
  - `AndroidBug5497Workaround$1.onGlobalLayout` needs "hide status bar";
  - `WrRenameDialog$1` watchers need the rename dialog;
  - `LargerHeaderSpan` (2) needs "bigger headings";
  - `ColorUnderlineSpan.updateDrawState` and `SyntaxHighlighterBase$1.getSize` are highlighting spans;
  - `TextViewUtils$ChunkedEditable` span methods (5), `NewFileDialog$1.onTextChanged`, `FileSearchResultSelectorDialog$1.afterTextChanged` and `GsTextWatcherAdapter$1.beforeTextChanged`.

### 5.4 Build-config, flavor and debug code that is compiled in

- `IS_TEST_BUILD = true`, `IS_GPLAY_BUILD = false`, DEBUG build (read from `BuildConfig.class`). Effects:
  - `MainActivity.IS_DEBUG_ENABLED` is forced true (`MainActivity.java:78`), so "Send debug log" is visible in DocumentActivity edit mode (`DocumentEditAndViewFragment.java:310, 545-549`);
  - special launchers are forced off (`AppSettings.java:254-259`);
  - experimental features default on (`AppSettings.java:921-923`), which shows "Convert & load epub", the UTF-8 BOM checkbox and the experimental settings;
  - keep-screen-on defaults off (262);
  - WebView debugging is enabled (`DocumentEditAndViewFragment.java:1025-1027`).
- `if (BuildConfig.IS_TEST_BUILD && false)` is a dead branch (`MainActivity.java:119-121`).
- `GsContextUtils.isGooglePlayBuild`/`isFossBuild` are uncalled.
- The commented-out "example" classes in `GsSimplePlaylistParser.java:236-268` and `TextViewUndoRedo.java:8-30` are not compiled. `src/test/java` is not in the APK.

### 5.5 API-level gates on the API 27 emulator

- Branches that cannot run: `SDK_INT >= R` in the storage check and request (`GsContextUtils.java:2388-2399, 2423-2425`), `TextViewUtils.java:790`, `HighlightingEditor.java:86` (P), PendingIntent `FLAG_MUTABLE` (S) in both widget providers, and `ShortcutUtils.java:55` (< N_MR1, so it continues on 27).
- `GsPreferenceFragmentBase.lambda$onViewCreated$2` (`GsPreferenceFragmentBase.java:236-251`, `SDK_INT < LOLLIPOP`) is unreachable on API 27. Also `GsContextUtils.java:759, 2212`.

### 5.6 Hardware, network, accounts and other environment

- Camera (`AttachLinkOrFileDialog.insertCameraPhoto` → `IMAGE_CAPTURE`), audio recorder, gallery, calendar, print, mail and browser all need another app.
- The SAF and SD-card paths need a secondary volume.
- No account or network gate exists; INTERNET is only used by the browser and WebView.
- Encryption needs the Keystore password.

---

## 6. Decomposition into 6 areas

Every compiled class (320, excluding JacocoInstrument) is assigned to exactly one area; inner and anonymous classes follow their outer class. **No leftovers.** 37 of these classes contribute no method nodes: 32 interfaces (e.g. `GsCallback$a0…$s5`, `FormatRegistry$TextFormatApplier`, `GsPropertyBackend`, `SyntaxHighlighterBase$StaticSpan`) and 5 synthetic switch-map classes that are not in the JaCoCo report (`ActionButtonSettingsActivity$1`, `MarkdownTextConverter$1`, `TodoTxtFilter$1`, `AttachLinkOrFileDialog$2`, `TextViewUndoRedo$1`).

| Area | Classes it owns (inner classes included) | Classes | Methods | Pages (§3.4) | Main entry edges from other areas |
|---|---|---|---|---|---|
| **SHELL**: start, onboarding, main container, More, Settings, widgets, shortcuts | `ApplicationObject`, `BuildConfig`; `activity.MainActivity`, `IntroActivity`, `StoragePermissionActivity`, `SettingsActivity`, `ActionButtonSettingsActivity`, `MoreFragment`, `MoreInfoFragment`; `activity.openeditor.*`; `widget.*`; `other.writeily.widget.*`; `util.ShortcutUtils`, `util.BackupUtils`; `opoc.util.GsBackupUtils`; `opoc.frontend.settings.*`; `opoc.format.GsSimpleMarkdownParser` | 52 | 282 | 1-36 | All ENTRY edges from S_ENTRY. FILES page S_NB_* → `MainActivity.onOptionsItemSelected` (Settings) and FAB/bottom-nav handlers; EDITOR `DocumentEditAndViewFragment` (628-631), `DocumentShareIntoFragment` (292) and `DocumentActivity.launch` for folders (89) → `MainActivity.launch`/`onNewIntent` |
| **FILES**: notebook, pickers, file operations, file search | `opoc.frontend.filebrowser.*`; `markor.frontend.filebrowser.MarkorFileBrowserFactory`; `frontend.NewFileDialog`, `frontend.FileInfoDialog`; `frontend.filesearch.*`; `other.writeily.ui.WrRenameDialog`, `other.writeily.model.WrMarkorSingleton` | 35 | 313 | 37-55 | SHELL `SectionsPagerAdapter.createFragment` → `GsFileBrowserFragment.newInstance` (`MainActivity.java:521-522`); `getFilesystemFragmentOptions` → `prepareFsViewerOpts` (460-462); `onClickFab` → `NewFileDialog` (359-360); Settings/Backup/WidgetConfigure → `showFolderDialog`/`showFileDialog` (`SettingsActivity.java:253-325`, `WrWidgetConfigure.java:56-77`). EDITOR menu Info → `FileInfoDialog.show` (604-608); epub/share-into pickers. ACTIONS attach → `showFileDialog`; `showSearchFilesDialog` → `FileSearch*` (`MarkorDialogFactory.java:144-160`) |
| **EDITOR**: document screen, editor widget, find/replace, view mode, share-into, document model, encryption | `activity.DocumentActivity`, `DocumentEditAndViewFragment`, `DocumentShareIntoFragment`; `frontend.textview.HighlightingEditor`, `LineNumbersView`, `TextViewUtils`; `frontend.textsearch.*`; `frontend.SearchAndReplaceTextDialog`, `DraggableScrollbarScrollView`; `web.*`; `opoc.web.GsWebViewClient`, `GsWebViewChromeClient`; `opoc.frontend.textview.TextViewUndoRedo`; `opoc.frontend.GsHorizontalScrollView`, `GsLinearSplitLayout`; `model.Document`; `other.de.stanetz.*`; `other.so.*`; `opoc.util.GsCoolExperimentalStuff` | 56 | 577 | 56-78 | SHELL `createFragment` → `DocumentEditAndViewFragment.newInstance` (`MainActivity.java:515-518`); `newItemCallback` / `MainActivity$2.onFsViewerSelected` → `DocumentActivity.launch` (366, 489-491); trampoline (`OpenFromShortcutOrWidgetActivity.java:19`); manifest VIEW/SEND. ACTIONS `onSearch` → `TextSearchFragment` (`ActionButtonBase.java:110-121`); open link → `DocumentActivity.launch` (`ActionButtonBase.java:716`, `MarkdownActionButtons.java:280`, `WikitextActionButtons.java:194`); `showSttSearchDialog`/`showSearchDialog` → `SearchAndReplaceTextDialog` (`MarkorDialogFactory.java:476, 765`) |
| **ACTIONS**: action bar, per-format buttons, dialogs factory, todo.txt model | `format.ActionButtonBase`; `format.*.*ActionButtons` (6); `format.todotxt.TodoTxtTask`, `TodoTxtFilter`; `format.wikitext.WikitextLinkResolver`; `frontend.MarkorDialogFactory`, `DatetimeFormatDialog`, `AttachLinkOrFileDialog`; `opoc.frontend.GsSearchOrCustomTextDialog`; `util.TextCasingUtils` | 40 | 461 | 79-109 | EDITOR `applyTextFormat` → `getActions().setDocument/setUiReferences/recreateActionButtons` (`DocumentEditAndViewFragment.java:649-668, 1057`); `onToolbarClicked` → `runTitleClick` (1090-1094); `onToolbarLongClicked` → `runJumpBottomTopAction` (1097-1102); `onReceiveKeyPress` (342); menu Search → `onSearch` (540-544); Font size → `showFontSizeDialog` (610-626); find-bar filter → `showSearchDialog` (`TextSearchFragment.java:243`). FILES → `showConfirmDialog` (`GsFileBrowserFragment.java:426, 588`), `showFolderSortDialog` (610-628), `showNotebookFilterDialog` (505-515), `showSearchFilesDialog` (499-501); picker new folder → `GsSearchOrCustomTextDialog` (`GsFileBrowserDialog.java:249-266`); `WrMarkorSingleton` → `showCopyMoveConflictDialog` (148); NewFileDialog → `showPopupWindow` (174). SHELL → `showSetPasswordDialog` (`SettingsActivity.java:375`); `ActionButtonSettingsActivity` → `ActionButtonBase` order API |
| **RENDER**: highlighters, auto-format, converters (view-mode HTML), format detection | `format.FormatRegistry`, `TextConverterBase`; every `format.*` class not listed under ACTIONS (all `*SyntaxHighlighter`, `*TextConverter`, `*ReplacePatternGenerator`, `CsvConfig`, `ColorUnderlineSpan`, `plaintext.highlight.*`, `TodoTxtAutoTextFormatter`, `TodoTxtBasicSyntaxHighlighter`); `frontend.textview.SyntaxHighlighterBase`, `AutoTextFormatter`, `ListHandler`, `ReplacePatternGeneratorHelper`; `other.com.vladsch.flexmark.ext.katex.*`; `other.writeily.format.*`; `opoc.format.GsSimplePlaylistParser` | 80 | 398 | none | EDITOR `applyTextFormat` → `FormatRegistry.getFormat` (`DocumentEditAndViewFragment.java:654`); `HighlightingEditor.setHighlighter`/`recomputeHighlighting` (229-241, 184-226); `updateViewModeText` → `convertMarkupShowInWebView` (`DocumentEditAndViewFragment.java:987-997`); share HTML → `convertMarkup` (482-491); `Document.<init>` → `isFileOutOfThisFormat` (`Document.java:73-86`); `DocumentActivity.launch` and `GsFileBrowserFragment.updateMenuItems` → `FormatRegistry.isFileSupported`. ACTIONS buttons → `*ReplacePatternGenerator` |
| **INFRA**: shared infrastructure | `model.AppSettings`; `util.MarkorContextUtils`; `activity.MarkorBaseActivity`, `MarkorBaseFragment`; `opoc.frontend.base.*` (`GsActivityBase`, `GsFragmentBase`, `GsPreferenceFragmentBase`); `opoc.model.*`; `opoc.wrapper.*`; `opoc.util.GsContextUtils`, `GsFileUtils`, `GsCollectionUtils`, `GsNanoProfiler`; `opoc.format.GsTextUtils`; `opoc.web.GsNetworkUtils` | 57 | 824 | none | Called from every area; lifecycle of the base classes |
| **Total** | | **320** | **2855** | 109 | |

**Who owns what**
- **Shared infrastructure** (base classes, the SharedPreferences "database layer" `AppSettings`/`GsSharedPreferencesPropertyBackend`, and the context, file, collection and text utilities) is owned by INFRA.
- **Singletons and static state:**
  - `ApplicationObject._app`/`_appSettings` and `MainActivity.IS_DEBUG_ENABLED`: SHELL;
  - `WrMarkorSingleton` and `FileSearchEngine` statics: FILES;
  - the `FormatRegistry` static converters: RENDER;
  - `GsContextUtils.instance`: INFRA.

**Edge-ownership rules for parallel agents**
1. The area owning a method writes every edge whose `src` is that method, including cross-area CALL edges. Exception: virtual dispatch from an INFRA base-class method to an override (for example `GsActivityBase.onPostResume` → `MainActivity.onActivityFirstTimeVisible`, or `GsFragmentBase.onViewCreated` → `DocumentEditAndViewFragment.onFragmentFirstTimeVisible`) is written by the override's area.
2. The owner of a page writes the GUI and SYSTEM edges from it, even when the callback method belongs to another area. Example: S_NB_BROWSE → `MainActivity.onClickFab`.
3. SHELL writes all ENTRY edges, including those into DocumentActivity and WrWidgetConfigure.
4. The owner of a shared dialog (`GsFileBrowserDialog` and `NewFileDialog` for FILES; `GsSearchOrCustomTextDialog` and `MarkorDialogFactory` for ACTIONS) writes the dialog's internal edges with `@CALLER` variants plus the CALL back into the caller's callback. Callers write the CALL into the `show…` method and tell the owner the callback names.
5. Use per-area edge-id prefixes. Agree on the page names in §3.4 before starting.

---

## 7. Baseline coverage by area and screen

| Area | Methods | Both | Monkey only | APE only | Neither | Monkey % | APE % | Neither: in dead classes (§5.1) | Neither: other no-call-site (§5.2/5.3) |
|---|---|---|---|---|---|---|---|---|---|
| SHELL | 282 | 121 | 9 | 31 | 121 | 46.1 | 53.9 | 5 | 24 |
| FILES | 313 | 115 | 9 | 84 | 105 | 39.6 | 63.6 | 0 | 26 |
| EDITOR | 577 | 241 | 1 | 141 | 194 | 41.9 | 66.2 | 0 | 27 |
| ACTIONS | 461 | 120 | 21 | 90 | 230 | 30.6 | 45.6 | 0 | 5 |
| RENDER | 398 | 126 | 0 | 65 | 207 | 31.7 | 48.0 | 0 | 21 |
| INFRA | 824 | 326 | 6 | 105 | 387 | 40.3 | 52.3 | 41 | 115 |
| **Total** | **2855** | **1049** | **46** | **516** | **1244** | 38.4 | 54.8 | 46 | 218 |

The totals match the brief: Monkey 1095, APE 1565, either 1611.

**Monkey-only methods (46).** They cluster in:
- Settings file pickers (`SettingsFragmentMaster$2/$3/$4`, `AppSettings.setNotebookDirectory`/`setTodoFile`/`setRecreateMainRequired`);
- todo.txt browse-by-key (`TodoTxtFilter.getKeys`, `TodoTxtTask.getContexts`/`getProjects`, `MarkorDialogFactory.showSttKeySearchDialog` and filter lambdas);
- `AttachLinkOrFileDialog.showInsertImageOrLinkDialog` and its picker;
- `GsFileBrowserDialog` new-folder, filter and Back;
- the font-list spans, `GsContextUtils.shareText` and the licence WebView dialog.

**Pages never reached, by area** (page numbers from §3.4, reasons from §2.4):
- SHELL: S_PERMISSION (8, permission pre-granted), S_HOME_WIDGETS/S_LAUNCHER_SHORTCUTS/S_WIDGET_CONFIG (4, 5, 31, outside the package), and Backup/restore inside S_SETTINGS_OTHER (never tapped).
- FILES:
  - S_DLG_RENAME/S_DLG_RENAME_CLASH (45-46);
  - move/copy through S_FSDLG_FOLDER@MOVE/@COPY;
  - import of a picked file;
  - S_DLG_MOUNT_SD (55, no SAF volume).
  - For Monkey also S_NB_SELECT*, S_DLG_NEW_FILE, S_DLG_SEARCH_RESULTS and sort/filter, because the notebook had no rows and the FAB was never tapped.
- EDITOR:
  - S_DOC_EDIT_WIKI and the real plain/CSV/key-value editors (no such files);
  - S_DOC_VIEW_BINARY; S_DOC_SELECT (empty texts);
  - S_DOC_NOT_SUPPORTED and S_DOC_OPEN_WITH (special inputs);
  - S_SHARE_INTO (external intent).
  - For Monkey also every DocumentActivity page and all view-mode pages.
- ACTIONS:
  - todo.txt priority, archive, date, update and save-query (empty todo.txt);
  - snippet (no snippets), table row, AsciiDoc keys, special-file;
  - date/time pickers, copy/move conflict, set password.

---

## 8. Conclusions and recommendations

1. **Graph scope.** Use 2853 method nodes, excluding `BuildConfig` like the Currency graph. Model the 109 pages in §3.4 with the `@CALLER` variants in §3.5. Expect many `needs_state` edges, because Markor's handlers depend heavily on document content:
   - text present: selection, todo.txt actions, headings;
   - a file selected: rename, move, copy;
   - fixtures of a format: wikitext, AsciiDoc, Org, CSV, binary;
   - a password set: encryption.
2. **Verdict starting points.** DEAD candidates: the 4 classes in §5.1 and the methods in §5.2. FRAMEWORK_ONLY candidates: `GsMenuItemDummy*`, the `onNothingSelected` callbacks, `ReorderCallback.onSwiped`, and the non-inflation view/preference constructors. Environment-gated, so reachable: widgets, the JS bridge (document content), the API < 21 lambda (DEAD on API 27), and the API ≥ 28/30 branches.
3. **Dataset fixes (recommendations only; nothing changed here).**
   - Add `Markor-#v2.16.1/app/thirdparty/java/` to `class_files.json` "sourcefiles". Otherwise 178 `other.*` methods have no source in the JaCoCo HTML.
   - Provide the missing `fixtures/Documents`, which must land in `/sdcard/Documents/marder` (lowercase flavor name), as listed in §2.5.
   - Pre-seed the intro flag and the permission so that tools are not scored on the tutorial.
4. **Tool-run hazards worth documenting in the study:**
   - the intro re-opens on every `MainActivity` resume until Done (`MainActivity.java:301`);
   - Settings' full-screen folder picker consumes Back as "folder up" (`GsFileBrowserDialog.java:86-95`) and trapped Monkey for half its budget;
   - More-tab links leave the app;
   - in this build the special launchers are forced off by `MainActivity.onCreate` (`AppSettings.java:254-259`).
5. **Open questions.**
   - Why the intro came back for APE at segment 80: needs the APE event log, or a check of whether the tool clears data on restart.
   - How the permission was granted in both runs.
   - Whether the `_fixtures` files were pushed to `/sdcard/Download` for these runs: class-level coverage cannot tell, and no Wikitext/Org/CSV highlighter ran.
