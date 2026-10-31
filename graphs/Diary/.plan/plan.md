# Diary v1.105 trigger graph: implementation plan

Planner output for workflow `wf_6f605575a3f599f3`. The implementer turns this into
`graphs/Diary/graph_def.py`, builds it with the unchanged `tools/build_graph.py`, reviews paths, and writes
`graphs/Diary/out/README.md`. Everything below was read from the files named; framework claims cite the
android-8.1.0_r1 sources downloaded into `.plan/fw_src/` (see section 6).

## 0. Ground rules for this app

- Work from `/Users/darshan/Desktop/yang/work`. Not a git repo: no git, no worktree, no commits.
- Write only inside `graphs/Diary/` and never inside `graphs/Diary/auto/`. Do not modify `tools/`,
  the dataset, Currency's files, `share_example/`, the PDFs or the prompts.
- Paths contain `#`: always quote them, e.g. `"final_java_only/Diary/app/Diary-#v1.105/src/main/java/"`.
- Build command (prefix `diary`):
  `python3 -I tools/build_graph.py graphs/Diary diary`
  It writes `graphs/Diary/out/{diary_trigger_graph.json, methods.csv, diary_trigger_graph.html, build_report.txt}`
  and exits 1 while any error remains. Final state must be `errors: 0` and `0 ... (contradictions)`.
- The workflow loop stops when `graphs/Diary/out/review.json` has `"verdict": "APPROVED"` (written by the reviewer, not the implementer).

## 1. Files read (inventory)

App folder: `final_java_only/Diary/app/Diary-#v1.105/` (upstream billthefarmer/diary@v1.105, commit
07bb05c3b7a8ea90db5efdc8f574b9f334402a71, APK sha256 da19449478bec366f989339ef88b2c6bdd99fece4e24013adbe950a629c4b121,
minSdk 21, targetSdk 28, baseline on API 27).

Read completely (every branch):
- `src/main/AndroidManifest.xml` (137 lines)
- Java (11 files, 6,914 lines): `org/billthefarmer/diary/{Diary.java (3571), FileUtils.java (824), Editor.java (429),
  DiaryWidgetProvider.java (270), DiaryWidgetUpdate.java (263), SettingsFragment.java (209), QueryHandler.java (196),
  Settings.java (119), DatePickerPreference.java (111), AboutPreference.java (99)}`,
  `android/support/v4/content/FileProvider.java (803)`. Excluded: `org/billthefarmer/diary/JacocoInstrument/*` (3 files;
  checked that they reference no app class).
- Layouts: `res/layout/{main.xml, editor.xml, about.xml, save_path.xml, widget.xml}` (no `android:onClick` anywhere).
- Menu: `res/menu/main.xml` (the only menu; 17 items).
- XML: `res/xml/{preferences.xml, widget.xml, filepaths.xml}`.
- Values: `res/values/{strings.xml, arrays.xml, integers.xml, styles.xml, attrs.xml}` (menu titles, theme values 0/1/2).
- Assets: `src/main/assets/styles.css`; `assets/help.md` scanned for links and syntax (links at help.md:15, 203-204;
  event syntax example `@ 10:30 Dentist` at help.md:220).
- `build.gradle` (dependencies: commonmark 0.21.0, CustomCalendarView v1.06, MarkdownView v1.11), `DATASET.txt`,
  `class_files.json`, `final_java_only/MANIFEST.csv` (row Diary: no special setup).
- Not read (no call relations): `res/values-*/strings.xml` translations, `res/anim/*`, `res/drawable*/*`.
- Library sources (version-matched to build.gradle) downloaded to `.plan/fw_src/libs/`:
  CustomCalendarView v1.06 `CustomCalendarDialog.java`, `CustomCalendarView.java`, `DayView.java`; MarkdownView v1.11 `MarkdownView.java`.

## 2. Method universe and the 287 / 286 reconciliation

Commands run (outputs written):
- `python3 -I tools/list_methods.py "final_java_only/Diary/app/Diary-#v1.105/build/intermediates/javac/debug/classes/" --exclude JacocoInstrument --exclude '/R$' --exclude BuildConfig --json graphs/Diary/method_list.json` → **286 methods**
- `python3 -I tools/coverage_methods.py final_java_only/Diary --json graphs/Diary/coverage_baseline.json` → **287 methods**

Reconciliation (checked by set difference on (class, name, descriptor)):
- In the JaCoCo report but not in the graph universe: `BuildConfig.<clinit>()V` (hit by both runs) and `BuildConfig.<init>()V` (not hit). BuildConfig is excluded from the universe (Currency precedent).
- In the graph universe but not in the JaCoCo report: `FileUtils.<init>()V` (private empty constructor, FileUtils.java:102-104; JaCoCo filters it). Keep it in the graph; it is DEAD.
- 286 − 1 + 2 = 287. No R classes exist in the classes dir (the `/R$` exclude matches nothing), the JacocoInstrument package is excluded by both tools.
- Baseline hit counts. Whole report: Monkey 165, APE 187, either 188. Inside the 286-method universe: 285 reported; Monkey 164, APE 186, either 187 (1 Monkey-only: `Diary.lambda$setListeners$4`; 23 APE-only), 98 never hit, 1 not reported.

Per class (universe): Diary 139, FileUtils 30, FileProvider 17, Editor 17, DiaryWidgetUpdate 13, DiaryWidgetProvider 11,
DatePickerPreference 7, QueryHandler 6, SettingsFragment 6, Diary$FindTask 5, Diary$GestureListener 5, Diary$ZipTask 5,
FileProvider$SimplePathStrategy 4, Diary$2 4, Editor$1 4, Diary$1 3, Diary$QueryTextListener 3, Settings 3,
AboutPreference 2, Diary$EntryDecorator 2. The vendored `android/support/v4/content/FileProvider` is app code (short name `FileProvider`).

Exact node names (as `build_graph.method_names` makes them, overloads with `(params)`) with hit flags are in
`.plan/node_names.txt`. Overloaded nodes: `FileProvider.copyOf(Object[],int)`, `copyOf(String[],int)`;
`Diary.addMedia()`, `addMedia(Intent)`, `addMedia(Uri,boolean)`; `Diary.alertDialog(int,int,int,int,OnClickListener)`,
`alertDialog(int,String,int)` (same two in Editor); `Diary.changeDate(long)`, `changeDate(Calendar)`;
`Diary.dateCheck(CharSequence)`, `dateCheck(CharSequence,String)`, `dateCheck(CharSequence,String,Date)`;
`Diary.getEntries()`, `getEntries(Calendar)`; `Diary.getFile()`, `getFile(Calendar)`; `Diary.loadMarkdown()`,
`loadMarkdown(CharSequence)`; `Diary.mediaCheck(Intent)`, `mediaCheck(CharSequence)`;
`Diary.onDateSet(DatePicker,int,int,int)`, `onDateSet(CustomCalendarView,int,int,int)`; `Diary.save()`, `save(CharSequence)`;
`Diary.showToast(int)`, `showToast(String)`; `DiaryWidgetProvider.getFile()`, `getFile(Calendar)`;
`FileUtils.copyFile(Context,Uri,Uri)`, `copyFile(File,File)`; `FileUtils.getMimeType(Context,Uri)`, `getMimeType(File)`;
`FileUtils.getThumbnail(Context,Uri)`, `getThumbnail(Context,Uri,String)`, `getThumbnail(Context,File)`.

Expected verdict breakdown (to confirm after the build): 17 DEAD, 4 FRAMEWORK_ONLY, 265 reachable (REACHABLE plus a
few REACHABLE_AFTER_SETUP). All 21 DEAD/FRAMEWORK_ONLY methods are never hit or unreported, so 0 contradictions are
expected. 78 reachable methods were never hit by the baseline (the TARGETS); they are listed in section 9.

## 3. Planning aids already produced (inside `.plan/`, not deliverables)

- `bytecode_calls.py` / `bytecode_calls.txt`: for every compiled method, its source line range (LineNumberTable) and
  every `invoke*` target with source line; `invokedynamic` resolved to the lambda body. Use it for round A and to
  cite lines. It confirms the lambda numbering (javac numbers a nested lambda before its enclosing one):
  `Diary.lambda$setListeners$4` 932-935 showEdit Runnable; `$5` 941-974 MarkdownView scroll; `$6` 981-985 MarkdownView
  long-press; `$7` 995-1017 Accept tap; `$8` 1023-1026 Accept long-press; `$9` 1050-1059 delayed scroll inside Edit tap;
  `$10` 1036-1062 Edit tap; `$11` 1068-1071 Edit long-press; `$12` 1107-1111 text focus change; `$13` 1117-1142 text tap
  (task-list toggle); `$14` 1148-1152 text long-press; `$15` 1161-1163 showAccept Runnable; `$16` 1169-1203 ScrollView scroll;
  `lambda$cancel$17` 1214-1225; `lambda$addEvents$18` 1869-1876; `lambda$backup$19` 1916-1947;
  `lambda$checkPosition$20` 2468-2477; `lambda$addLink$21` 2819-2844; `lambda$sortFiles$0` 306; `lambda$listYears$1` 315;
  `lambda$listMonths$2` 323; `lambda$listDays$3` 331. Editor: `$0` 175-176 text long-press (static, captures accept),
  `$1` 185-199 Accept tap, `$2` 205-206 Accept long-press, `lambda$onBackPressed$3` 256-271.
  `Diary$1` = the WebViewClient (854-926), `Diary$2` = the TextWatcher (1077-1101).
- `app_callers.txt`: per universe method, every app call site (from bytecode). `access$NNN` accessors appear as callers;
  map them through to the inner class (e.g. `access$700` = `changeDate(Calendar)` called by `Diary$1.shouldOverrideUrlLoading`
  and `Diary$FindTask.lambda$onPostExecute$1`; `access$1900..2200` = `onSwipeRight/Left/Down/Up` from `GestureListener.onFling`;
  `access$1200` = `alertDialog(int,String,int)` from `ZipTask.lambda$doInBackground$0`; `access$2600` = `getDay` from
  `EntryDecorator.decorate`; `access$1100` = `getHome` from FindTask/ZipTask `doInBackground`; `access$500` = `setTitleDate`
  from `onPageFinished`; `access$600` = `diaryEntry`; `access$2400` = `animateEdit` from `onDoubleTap`).
- `node_names.txt`: node name | descriptor | baseline flag (M/A/--/NR).
- `fw_src/android-8.1.0_r1/...`: framework files (Activity, ActivityThread, PhoneWindow, ActionMenuPresenter, MenuBuilder,
  MenuItemImpl, GestureDetector, TextView, SearchView, WebViewClient, AsyncTask, AsyncQueryHandler, ContentProvider, Intent,
  AppWidgetProvider, AppWidgetServiceImpl, ActivityManagerService, BroadcastQueue, Preference, DialogPreference,
  PreferenceFragment, PreferenceScreen, TwoStatePreference, EditTextPreference, ListPreference, SharedPreferencesImpl,
  DatePickerDialog, AbsListView, data/etc/framework-sysconfig.xml, platform.xml). Fetched from
  `https://android.googlesource.com/platform/frameworks/base/+/refs/tags/android-8.1.0_r1/<path>?format=TEXT`.
  More files can be fetched the same way if needed (write them under `.plan/fw_src/`).

## 4. Conventions and decisions (follow exactly)

1. **Template**: same file format as `graphs/Currency/graph_def.py`: header comment, `TITLE = 'Diary v1.105 trigger graph'`,
   ENV/FW constants, `SCREENS`, `DEAD`, `FRAMEWORK_ONLY`, `NOTES`, then `e(...)` calls grouped by section comments. Loops
   and small helper functions are fine (Currency uses them).
2. **Evidence labels**: `SRC <File>:<line>` (app source/res), `FW-SRC <path relative to fw_src/android-8.1.0_r1>:<line>`
   for framework source you actually opened, `FW-SRC lib <CustomCalendarView@v1.06|MarkdownView@v1.11>/<File>:<line>`
   for the two libraries (version-matched to build.gradle), `FW-MEMORY` only for claims not checked (state what is
   recalled), `INFERRED`, `DYN baseline ...` for facts read from the coverage reports, `UNVERIFIED`. Prefer FW-SRC
   for every claim listed in section 6.
3. **Menu ids lack the `action_` prefix** that `build_graph.menu_label` and the viewer regex expect. Keep the standard
   pattern (one GUI edge page → `Diary.onOptionsItemSelected@<CTX>`, then one CALL edge per item with
   `trigger='switch case R.id.<id>'`), and **put the item tap in `gui` of each CALL edge**
   (e.g. `gui=['Tap More options (⋮) -> Share…']`). Then `methods.csv` shows "<GUI step> ; Tap More options (⋮) -> Share…".
   Phrase the GUI edge's `gui[0]` as "Open the action bar menu (icons or More options ⋮)". Exception: the
   `android.R.id.home` CALL edge gets no `gui` (menu_label already turns it into "Up arrow (top-left)"). Mention this in the README.
4. **env constants** (an edge with `env` marks environment-gated code; CSV note "needs environment: ..."):
   - `ENV_NOPERM` = 'storage/calendar runtime permissions not granted yet (fresh install without auto-grant; the baseline had them granted: no onRequestPermissionsResult ran)'
   - `ENV_PERM` = 'storage permission granted' (use on the help-text and read/write success edges only where the branch matters)
   - `ENV_24H` = 'device locale whose SHORT time format is 24-hour without AM/PM (e.g. en-GB, de-DE); in en-US "10:30" fails to parse'
   - `ENV_CAL_ACCOUNT` = 'at least one calendar exists in the Calendar provider (an account with a calendar)'
   - `ENV_CAL_EVENT` = 'the Calendar provider has an event on the shown diary date'
   - `ENV_IO_ERROR` = 'writing the target file fails with an I/O error (e.g. storage full or read-only location)'
   - `ENV_NO_PATH` = 'the picked document has no readable local file path (e.g. a cloud provider), so the URI stays content://'
   Outside-the-app actions (home-screen widget, share sheet, other apps sending intents) are not env: they are normal
   GUI/ENTRY edges whose `gui` says where to tap, and the README explains that APE/Monkey (confined to the package) cannot do them.
5. **Pages vs guards**: preference-dependent behaviour is modelled with `@CONTEXT` page variants reached through Settings
   (section 5), so target paths contain the Settings steps. `needs_state` is used only for genuine "earlier visit" state.
   The complete needs_state list: (a) `Diary.onCreate → Diary.index` (Use index ticked earlier, Diary relaunched);
   (b) base `Diary.onResume → Diary.<init>` recreate (theme changed earlier; the `@THEME` variant has no needs_state);
   (c) `SettingsFragment.onCreate → DatePickerPreference.onSetInitialValue` (a date page was set on an earlier Settings visit);
   (d) `DiaryWidgetProvider.onReceive@APP → onUpdate` (a widget is already placed);
   (e) `DiaryWidgetUpdate.onCreate@X → Diary.onResume` (Diary task alive in the background; hazard 10);
   (f) `Diary.addMedia(Uri,boolean)@COPY → FileUtils.getPathWithoutExtension` (an image with the same name was already copied into
   that month's folder: the rename loop 2772-2779). Data guards (Previous/Next enabled, Up arrow shown) stay guard text.
6. **Accepted page-level approximation**: handlers that modify the text from the menu or from async results (`addTime`,
   `lambda$addEvents$18`, `addMedia(Uri,boolean)`, `lambda$addLink$21`, `addMap`, `addIndexLink`) get two guarded ENTERS
   edges: to `S_DIARY_VIEW_CHANGED` (guard `shown`) and `S_DIARY_EDIT_CHANGED` (guard `!shown`). No method is reachable only
   from one `_CHANGED` page, so this cannot create a wrong method path; state it in the README limits.
7. **S_DIARY_PLAIN** (markdown off) is entered only from the Settings path. Shared navigation handlers do NOT get ENTERS
   edges into S_DIARY_PLAIN (that would create shortcuts from markdown-on pages); the user stays on S_DIARY_PLAIN.
   Write this in the S_DIARY_PLAIN NOTES entry and the README.
8. `REGISTER` edges for every listener (precondition only), as in Currency.

## 5. Pages (window, mode) and @CONTEXT variants

### 5.1 SCREENS (base pages; one-line descriptions to put in SCREENS)

Pseudo pages:
- `S_ENTRY` outside the app: launcher, home screen, another app (search root)
- `S_EXIT` Diary/Editor finished (Back on the root) or crashed; the process may survive (static QueryHandler, FileProvider.sCache kept)
- `S_DIARY_PAUSED` Diary paused/stopped: Home, another activity on top (Settings, Editor, picker, chooser, print, permission dialog, browser), or mid-rotation
- `S_EDITOR_PAUSED` Editor in the background
- `S_SETTINGS_PAUSED` Settings in the background

Diary (markdown on, the default):
- `S_DIARY_VIEW` MarkdownView shown (shown=true), Edit (pencil) button, no unsaved changes; menu main.xml without Cancel; Index/Add link hidden (pref_use_index off)
- `S_DIARY_VIEW_CHANGED` same with unsaved changes (changed=true): Cancel item visible. Entered on the first launch (help text loaded, Diary.java:564-568, readAssetFile sets changed at 2387) and after Add time/events/media/link
- `S_DIARY_EDIT` EditText shown (shown=false), Accept (✓) button, no unsaved changes
- `S_DIARY_EDIT_CHANGED` EditText after typing: Cancel visible, Accept saves
- `S_DIARY_SEARCH` SearchView expanded in the action bar; Find all appears in the overflow (onPrepareOptionsMenu 649-652). Variants `@VIEW` (query searches the MarkdownView, 3337-3338) and `@EDIT` (query highlights in the EditText, 3341-3375)
- `S_DIARY_BROWSE` MarkdownView navigated away from the entry by a link (entry=false): Up arrow shown, Back goes back in WebView history (onBackPressed 744-756)
- `S_DIARY_PLAIN` pref_markdown off: EditText only, no Accept/Edit buttons (setVisibility 1713-1717); Cancel appears after typing (not split; see 4.7)

Dialogs over Diary:
- `S_DLG_CALENDAR` CustomCalendarDialog (pref_custom on): month view with entry days marked, OK/Cancel (lib CustomCalendarDialog.java). Variants by caller (5.2)
- `S_DLG_DATE_PICKER` framework DatePickerDialog (pref_custom off)
- `S_DLG_SAVE_CHANGES` "Save changes?" Save/Discard (cancel(), 1210-1225)
- `S_DLG_BACKUP` Backup dialog: path EditText, Save / Cancel / Storage (saveAsDialog 1951-1973)
- `S_DLG_ADD_LINK` Add link dialog: title EditText, Add link / Cancel (addLinkDialog 2848-2870)
- `S_DLG_FIND_ALL` Find all result list (or empty list) with Cancel (FindTask.onPostExecute 3281-3315)
- `S_DLG_ERROR` alert with an exception message and OK (alertDialog(int,String,int) 2340-2352)

Outside-the-app windows reached from Diary:
- `S_CHOOSER_SHARE` system share sheet for Share…; variants `@IMAGE` (shown: PNG of the MarkdownView) and `@TEXT` (editing: the entry file)
- `S_MEDIA_PICKER` system chooser + picker app for Add media… (GET_CONTENT */*); variants `@PLAIN` and `@COPY` (pref_copy_media on)
- `S_DOC_CREATE` DocumentsUI "save as" for Backup → Storage (ACTION_CREATE_DOCUMENT application/zip)
- `S_PRINT` system print preview (PrintManager.print)
- `S_PERMISSION` runtime permission dialog (GrantPermissionsActivity); variants `@DIARY` and `@EDITOR`; env ENV_NOPERM

Editor:
- `S_EDITOR` Editor activity (monospace EditText, Accept ✓, Up arrow), no unsaved changes; variants `@STYLES` (opened by Edit styles…/Edit script… for result) and `@EXTERNAL` (opened by another app with VIEW/EDIT text/*)
- `S_EDITOR_CHANGED` after typing (Back asks Save/Discard); same two variants
- `S_DLG_EDITOR_SAVE` "Save changes?" Save/Discard in Editor; same two variants

Settings:
- `S_SETTINGS` SettingsActivity + SettingsFragment (preferences.xml); Index page / Index template / Template page rows disabled (dependencies). Variants per changed key (5.2)
- `S_DLG_FOLDER` EditTextPreference dialog "Folder"
- `S_DLG_INDEX_TEMPLATE` EditTextPreference dialog "Index template"
- `S_DLG_DATE_PREF` DatePickerPreference dialog; variants `@INDEX` (pref_index_page) and `@TEMPLATE` (pref_template_page)
- `S_DLG_THEME` ListPreference dialog Light/Dark/System
- `S_DLG_ABOUT` About dialog (AboutPreference, layout about.xml)

Home screen:
- `S_HOME_WIDGET` home screen with a Diary widget (header date, prev/next/today icons, entry text; layout widget.xml)

About 40 base pages (plus variants). Every page must be reachable from S_ENTRY (build_graph checks it).

### 5.2 @CONTEXT variants (the part before @ must be an existing node)

Diary entry contexts (the same onCreate continues differently by launch intent):
- `Diary.<init>` (base, launcher MAIN), `Diary.<init>@WIDGET` (widget body tap: extra ENTRY, data widget://0),
  `@SEND_TEXT` (SEND text/plain: shared text, link or .txt file), `@SEND_IMAGE` (SEND image/* audio/* video/*),
  `@SEND_MULTI` (SEND_MULTIPLE image/*), `@GEO` (VIEW geo:). Matching `Diary.onCreate@X`, `Diary.mediaCheck(Intent)@X`,
  `Diary.goToDate@X`, `Diary.showCustomCalendarDialog@X`, `S_DLG_CALENDAR@X`, `Diary.onDateSet(CustomCalendarView,int,int,int)@X`,
  `Diary.addMedia(Intent)@X` for X in SEND_TEXT/SEND_IMAGE/SEND_MULTI/GEO. The menu path uses `@GOTO`
  (`Diary.goToDate@GOTO` is not needed: use base `Diary.goToDate` → `S_DLG_CALENDAR@GOTO`).
- Self-share: `S_CHOOSER_SHARE@TEXT` → `Diary.<init>@SEND_TEXT`; `S_CHOOSER_SHARE@IMAGE` → `Diary.<init>@SEND_IMAGE`
  (Diary is a SEND target for text/plain and image/*, manifest 60-74). The help text documents the text variant (help.md:205-208).

Menu dispatcher contexts (`Diary.onOptionsItemSelected@CTX`), one GUI edge from each page:
- `@VIEW` (S_DIARY_VIEW, S_DIARY_BROWSE), `@VIEW_CHANGED`, `@EDIT`, `@EDIT_CHANGED`, `@PLAIN`, `@SEARCH` (both S_DIARY_SEARCH variants:
  adds findAll; every other item also collapses the SearchView, 722-724), `@INDEX` (S_DIARY_VIEW@INDEX: adds index and link),
  `@NOCUSTOM` (goToDate → DatePickerDialog), `@COPY` (addMedia() → `Diary.addMedia()@COPY`).
  Cancel CALL edge only from `@VIEW_CHANGED`, `@EDIT_CHANGED` (and `@PLAIN` with guard "after typing").
  `android.R.id.home` CALL edge only where the Up arrow can show (guard: entryStack not empty or WebView history; onPageFinished 861-889).

Preference contexts (Settings → Diary). After toggling a key in Settings, `SettingsFragment.onSharedPreferenceChanged@KEY`
→ ENTERS `S_SETTINGS@KEY`; Up (`Settings.onOptionsItemSelected@KEY`) or Back → SYSTEM `Diary.onResume@KEY` → ENTERS the Diary variant:
- `CUSTOM` (Use custom calendar unticked) → `S_DIARY_VIEW@NOCUSTOM`
- `MARKDOWN` (Use markdown unticked) → `S_DIARY_PLAIN`
- `USE_INDEX` (Use index ticked; also enables the Index page / Index template rows on `S_SETTINGS@USE_INDEX`) → `S_DIARY_VIEW@INDEX`
- `USE_TEMPLATE` (Use template ticked; enables Template page on `S_SETTINGS@USE_TEMPLATE`) → `S_DIARY_VIEW@TEMPLATE`
  (the Edit tap runs template(): `Diary.lambda$setListeners$10@TEMPLATE`)
- `COPY_MEDIA` (Copy images ticked) → `S_DIARY_VIEW@COPY`
- `THEME` (S_DLG_THEME picked a different value) → Settings recreates itself; back in Diary `Diary.onResume@THEME` → SYSTEM `Diary.<init>` (recreate, 547-548)
- `FOLDER`, `INDEX_TEMPLATE`, `INDEX_PAGE`, `TEMPLATE_PAGE`, `EXTENDED`, `EXTERNAL`: listener variants that only update a summary (or
  nothing) and ENTER the same Settings page; no Diary variant needed (their Diary effects are guard text).
  `INDEX_TEMPLATE` additionally matters for the error path: an invalid `<<date X>>` pattern makes addIndexLink show S_DLG_ERROR.

Copy-media chain: `S_DIARY_VIEW@COPY` → `Diary.onOptionsItemSelected@COPY` → `Diary.addMedia()@COPY` → `S_MEDIA_PICKER@COPY`
→ `Diary.onActivityResult@ADD_MEDIA_COPY` → `Diary.addMedia(Uri,boolean)@COPY` → copy branch (2763-2791).
Other onActivityResult contexts: `@ADD_MEDIA` (from S_MEDIA_PICKER@PLAIN), `@EDIT_STYLES` (Editor result), `@CREATE_BACKUP` (S_DOC_CREATE).

Editor contexts: `Editor.<init>@STYLES` / `@EXTERNAL` with matching `onCreate`, `lambda$setListeners$1` (Accept),
`onBackPressed`, `lambda$onBackPressed$3`, `onOptionsItemSelected`, `Editor$1.afterTextChanged@TYPED_<ctx>` → result goes to
`Diary.onActivityResult@EDIT_STYLES` (STYLES) or `S_EXIT` (EXTERNAL: back in the calling app).

Text watcher: `Diary$2.afterTextChanged@TYPED` (and before/onTextChanged) is the GUI typing edge from S_DIARY_EDIT and
S_DIARY_EDIT_CHANGED that ENTERS `S_DIARY_EDIT_CHANGED`. All `setText` consequences go to the base `Diary$2.*` via FRAMEWORK
edges without ENTERS (load() resets changed right after, 2416-2417).

Gesture contexts: `Diary$GestureListener.onFling` (base: one-finger fling; returns at once because multi == false, 3440-3441)
vs `Diary$GestureListener.onFling@MULTI` (a fling right after a touch with ≥2 pointers set multi, 842-843) → onSwipe*.

Widget contexts: `DiaryWidgetProvider.<init>@ADD` (system after the widget is placed), `@APP` (Diary.updateWidgets),
`@BUTTON` (DiaryWidgetUpdate after a prev/next/today tap), `@PERIODIC` (updatePeriodMillis 3600000, xml/widget.xml:27),
`@RESIZE` (APPWIDGET_OPTIONS_CHANGED), `@DELETED`; matching `onReceive@X`. `DiaryWidgetUpdate.<init>@PREV/@NEXT/@TODAY`
with `onCreate@X` (switch on the int extra, DiaryWidgetUpdate.java:75-104).

Permission contexts: `S_PERMISSION@DIARY` → `Diary.onRequestPermissionsResult` (cases REQUEST_WRITE/READ/TEMPLATE, 2216-2244);
`S_PERMISSION@EDITOR` → `Editor.onRequestPermissionsResult` (286-311).

## 6. Framework facts already checked (cite these as FW-SRC)

| claim | target symbol | evidence |
|---|---|---|
| Opening the overflow (⋮) re-runs onPrepareOptionsMenu, so Find all becomes visible while the SearchView is expanded | `Activity.onPrepareOptionsMenu` | `core/java/android/widget/ActionMenuPresenter.java:997-1006` (OpenOverflowRunnable → changeMenuMode) → `core/java/com/android/internal/view/menu/MenuBuilder.java:767-769` → `core/java/com/android/internal/policy/PhoneWindow.java:1242-1265` (reopenMenu → onPreparePanel) → `core/java/android/app/Activity.java:3404-3406` |
| Tapping the Search item dispatches onOptionsItemSelected(R.id.search) (falls to `default`, returns super) and only then expands the action view | `MenuItemImpl.invoke`, `expandActionView` | `MenuBuilder.java:908-913` |
| Expanding the SearchView calls onQueryTextChange("") once (mOldQueryText starts null) | `SearchView.onTextChanged` | `core/java/android/widget/SearchView.java:1358-1365, 1249-1252` |
| Diary.updateWidgets' implicit APPWIDGET_UPDATE is limited to the caller's own package, so it is not an implicit broadcast for the background check and the manifest receiver gets it (explains the DYN hit of DiaryWidgetProvider.onReceive; also explains Currency's open question) | `BroadcastQueue` skip | `services/core/java/com/android/server/am/ActivityManagerService.java:19199-19224` (setPackage(callerPackage)) + `services/core/java/com/android/server/am/BroadcastQueue.java:1252-1278` (skip only when component and package are null) |
| AppWidgetProvider.onReceive calls onUpdate only for a non-empty id list; OPTIONS_CHANGED → onAppWidgetOptionsChanged | `AppWidgetProvider.onReceive` | `core/java/android/appwidget/AppWidgetProvider.java:61-81` |
| OPTIONS_CHANGED (and the system UPDATE/ENABLED/DELETED) are sent with an explicit component, so the manifest filter (UPDATE only) does not block them | `sendOptionsChangedIntentLocked` | `services/appwidget/java/com/android/server/appwidget/AppWidgetServiceImpl.java:2279-2305` |
| Share grants only READ to the target (FLAG_GRANT_READ_URI_PERMISSION), chooser migrates the inner SEND intent | `Intent.migrateExtraStreamToClipData` | `core/java/android/content/Intent.java:9965-10012` |
| insert/update/delete of a provider are only reached after enforceWritePermission passes | `ContentProvider.Transport` | `core/java/android/content/ContentProvider.java:256-265, 333-357` |
| onGetDefaultValue is called only when the preference has android:defaultValue | `Preference.onGetDefaultValue` | `core/java/android/preference/Preference.java:293-294` (only call site in the file) |
| onSetInitialValue(true, null) only when the key is already persisted; (false, default) needs a default value | `dispatchSetInitialValue` | `Preference.java:1547-1561` |
| A tap on an enabled preference row calls the fragment's onPreferenceTreeClick | `Preference.performClick` | `Preference.java:1146` |
| Providers are installed at every process start (before any activity/receiver), attachInfo → onCreate | `ContentProvider.attachInfo` | `core/java/android/app/ActivityThread.java:5722, 6239`; `ContentProvider.java:1917` |
| DatePickerDialog OK → onDateSet | `OnDateSetListener.onDateSet` | `core/java/android/app/DatePickerDialog.java:166-171` |
| CustomCalendarDialog OK → onDateSet(CustomCalendarView,…); Cancel does nothing | `listener.onDateSet` | `FW-SRC lib CustomCalendarView@v1.06/CustomCalendarDialog.java:110-120` |
| decorate() runs for each day cell on refreshCalendar and on a day tap | `DayDecorator.decorate` | `lib CustomCalendarView@v1.06/CustomCalendarView.java:404, 440`; `DayView.java:53-60` |
| MarkdownView.loadMarkdown → loadDataWithBaseURL (then WebViewClient.onPageFinished) | `loadDataWithBaseURL` | `lib MarkdownView@v1.11/MarkdownView.java:280`; onPageFinished itself is FW-MEMORY (Chromium) |
| AsyncTask: onPreExecute on the caller thread, doInBackground on a worker, onPostExecute on main | `AsyncTask.executeOnExecutor` | `core/java/android/os/AsyncTask.java:333-339, 648` |
| AsyncQueryHandler delivers onQueryComplete / onInsertComplete on the handler thread | `AsyncQueryHandler.handleMessage` | `core/java/android/content/AsyncQueryHandler.java:343-348` |
| GestureDetector: onFling is called on ACTION_UP when the fling velocity is above the minimum, also after a second pointer was used | `mListener.onFling` | `core/java/android/view/GestureDetector.java:520-560, 630-656` |

Still FW-MEMORY (label them so): WebView calling the String `shouldOverrideUrlLoading` from the request overload
(WebViewClient.java in fw_src has the default delegation; check and upgrade to FW-SRC if it is there), WebView
loading `content://` image URLs through the ContentResolver (openFile/getType of our FileProvider), Launcher3
behaviour (resize sends options, widget removal), ChooserActivity/receiving apps calling query/getType/openFile,
NEW_TASK trampolines bringing the Diary task to front, onActionModeStarted from text selection, rotation/recreate order,
onSaveInstanceState before onStop on API 27 (Activity.java can upgrade this), the soft keyboard/Enter key behaviour.

## 7. Per-class edge extraction notes (rounds A-G)

Use `.plan/app_callers.txt` / `bytecode_calls.txt` to make sure every app call site becomes a CALL edge (round A);
the notes below say what is not mechanical.

### 7.1 Process start, static init (round D/E)
- `S_ENTRY → FileProvider.<clinit>`, `S_ENTRY → FileProvider.<init>` ENTRY "any start of the app process (launcher, widget
  broadcast, share target, Editor)", then `FileProvider.<init> → attachInfo` LIFECYCLE, `attachInfo → onCreate` FRAMEWORK
  (super.attachInfo, FileProvider.java:366), `attachInfo → getPathStrategy` CALL (376), `getPathStrategy → parsePathStrategy`
  (560, guard sCache miss), `parsePathStrategy → SimplePathStrategy.<init>, buildPath, addRoot` (582-617; filepaths.xml has 3 roots).
- `Diary.<clinit>` (patterns, 157-179): CALL from `Diary.<init>` contexts, `DiaryWidgetProvider.getText` (Diary.read at 193) and
  `DiaryWidgetUpdate.prevYear/...` (Diary.listYears etc.), guard "class not yet initialised in this process".
- `FileUtils.<clinit>` (65-95, creates 3 lambdas never used): CALL from the first FileUtils use: `Diary.mediaCheck(CharSequence)`
  (1390), `Diary.resolveContent`, `Editor.resolveContent`, `Diary.onActivityResult`.
- `QueryHandler.<clinit>`: CALL from `queryEvents` / `insertEvent`.

### 7.2 Diary lifecycle (A, D)
- `S_ENTRY → Diary.<init>` ENTRY launcher (manifest 52-59); `Diary.<init> → onCreate` LIFECYCLE.
- `onCreate` (441-517): CALL getPreferences, setListeners, `Diary$GestureListener.<init>` (493); theme switch; intent branch
  only when `savedInstanceState == null`: `index()` (guard useIndex and ACTION_MAIN; needs_state "Use index was ticked on an
  earlier visit and Diary was relaunched"), `changeDate(long)` (WIDGET context only), `today()` (otherwise), `mediaCheck(Intent)`.
  `onCreate → onRestoreInstanceState` LIFECYCLE guard "recreated with saved state (rotation or theme recreate)";
  `onCreate → onResume` LIFECYCLE.
- `setListeners` (850-1205): CALL `Diary$1.<init>`, `Diary$2.<init>`; REGISTER edges to every lambda $4-$16 and to
  `Diary$1.onPageFinished/shouldOverrideUrlLoading`, `Diary$2.*`. Scroll listeners only on API ≥ 23 (928, 1157): true on API 27.
- `onRestoreInstanceState` (523-533): CALL setDate; restores shown/entry/saved.
- `onResume` (539-571): CALL getPreferences; SYSTEM `Diary.<init>` recreate (guard theme changed and SDK != 23; base onResume
  gets it with needs_state "Theme changed in Settings earlier", and `Diary.onResume@THEME` gets it without needs_state);
  CALL setDate, `getFile()`, load (guard file modified after `saved`), readAssetFile (guard storage permission granted and no
  entries before/after and empty text: first launch), FRAMEWORK `Diary$2.*` (setText at 565), CALL `loadMarkdown()` (guard
  markdown and changed), setVisibility; FRAMEWORK onCreateOptionsMenu/onPrepareOptionsMenu (menu creation after attach).
  ENTERS: `S_DIARY_VIEW_CHANGED` (first launch), `S_DIARY_VIEW` (shown), `S_DIARY_EDIT` (!shown after recreate in edit mode).
- `onSaveInstanceState` (577-590): SYSTEM from Diary pages (Home, rotation, another activity; not on Back).
  `onSaveInstanceState → Diary.<init>` SYSTEM guard rotation.
- `onPause` (596-606): SYSTEM from every Diary page; CALL `save()` (guard changed), `getFile()`; ENTERS S_DIARY_PAUSED;
  `onPause → S_EXIT` guard finishing (Back on root). `S_DIARY_PAUSED → Diary.onResume` SYSTEM.
- `onBackPressed` (731-757): SYSTEM/GUI Back on Diary pages; CALL `changeDate(Calendar)` (entry and stack not empty), super →
  finish (stack empty) → `onPause`/S_EXIT; browse branch: WebView goBack, then `changeDate(Calendar)` when history is empty.

### 7.3 Diary data/navigation helpers (A)
- `setDate` → setTitleDate, getPrevEntry, getNextEntry; FRAMEWORK onCreateOptionsMenu + onPrepareOptionsMenu (invalidateOptionsMenu 2526).
- `getPrevEntry/getNextEntry` → prevDay/prevMonth/prevYear (next*), recursion; `prev/nextDay` → listDays, getMonth, dayValue;
  `prev/nextMonth` → listMonths, getYear, monthValue; `prev/nextYear` → listYears, getHome, yearValue.
  `listDays/listMonths/listYears` → `sortFiles` CALL and FRAMEWORK to their filter lambdas (`File.listFiles(FilenameFilter)` calls
  accept per entry; guard directory exists and is not empty); `sortFiles` → FRAMEWORK `lambda$sortFiles$0` (Arrays.sort comparator,
  guard ≥ 2 files).
- `getFile()` → `getFile(Calendar)` → getDay → getMonth → getYear → getHome.
- `changeDate(Calendar)` (2563-2582) → `save()` (changed), setDate, load, animateAccept (markdown and !shown). `changeDate(long)` → `changeDate(Calendar)`.
- `prevEntry/nextEntry/today/index` → changeDate; `today` → template (guard useTemplate and !markdown).
- `load` (2398-2424) → permission request (env ENV_NOPERM → ENTERS S_PERMISSION@DIARY), `read`, `getFile()`, FRAMEWORK `Diary$2.*`
  (setText 2416), FRAMEWORK onCreateOptionsMenu/onPrepareOptionsMenu (2418), `loadMarkdown()` (markdown), `checkPosition`.
- `checkPosition` → ASYNC `lambda$checkPosition$20` (postDelayed 2465).
- `loadMarkdown()` → `loadMarkdown(CharSequence)` → markdownCheck, getBaseUrl, getStyles, getScript; FRAMEWORK `Diary$1.onPageFinished`
  (lib MarkdownView.java:280). `markdownCheck` → `dateCheck(CharSequence)`, mapCheck, `mediaCheck(CharSequence)`;
  `dateCheck(CharSequence)` → getDay; `mediaCheck(CharSequence)` → `FileUtils.getMimeType(File)` → getExtension.
- `getBaseUrl` → getCurrent → getMonth; `getStyles/getScript` → getHome.
- `save()` (2248-2284) → permission request (ENV_NOPERM), eventCheck, mapCheck, positionCheck, `save(CharSequence)`, updateWidgets.
  `eventCheck` → `QueryHandler.insertEvent` (guard a line `@ HH:MM title`, env ENV_24H; help.md:220 shows the syntax).
  `save(CharSequence)` → getFile; → `alertDialog(int,String,int)` (env ENV_IO_ERROR) → ENTERS S_DLG_ERROR.
- `updateWidgets` → INTENT `DiaryWidgetProvider.<init>@APP` (evidence: FW-SRC AMS.java:19199-19224 + BroadcastQueue.java:1252-1278 + DYN baseline onReceive hit, onUpdate never).
- `diaryEntry` → getHome. `setVisibility`, `animateAccept`, `animateEdit`, `startAnimation` are plain CALL targets.

### 7.4 Diary gestures and listeners (B, F)
Pages S_DIARY_VIEW/_CHANGED: Edit tap → `lambda$setListeners$10` → animateEdit, template (guard useTemplate; in base guard
says "only on S_DIARY_VIEW@TEMPLATE"), ASYNC `lambda$setListeners$9`; ENTERS S_DIARY_EDIT. Edit long-press → `$11`.
MarkdownView long-press → `$6` (also starts WebView text selection → FRAMEWORK `onActionModeStarted`, no effect while shown).
MarkdownView scroll → `$5` → startAnimation, ASYNC `$4` (postDelayed showEdit 957, guard scrolling down).
Tap a link → `Diary$1.shouldOverrideUrlLoading` (help text has links: help.md:15 https, 203-204 file:///android_asset/help.md)
→ diaryEntry; changeDate (diary link: file under the diary folder or a `date:` link converted by dateCheck); ENTERS S_DIARY_BROWSE
(file/asset link, or http(s) with pref_external off); external `startActivity` → S_DIARY_PAUSED (pref_external on or mailto).
Double-tap → `Diary$GestureListener.onDoubleTap` → animateEdit, ASYNC `lambda$onDoubleTap$0`; ENTERS S_DIARY_EDIT (guard shown).
Pages S_DIARY_EDIT/_CHANGED/PLAIN: type → `Diary$2.afterTextChanged@TYPED` (+ before/onTextChanged) → FRAMEWORK menu rebuild,
ENTERS S_DIARY_EDIT_CHANGED. Tap a task-list line `- [ ] x` → `$13` (editable.replace → FRAMEWORK `Diary$2.*`, ENTERS
S_DIARY_EDIT_CHANGED, guard tapped line matches CHECK_PATTERN). Tap/leave the text → `$12` focus change. Long-press text → `$14`
(+ FRAMEWORK `onActionModeStarted` with the extended-selection branch, guard pref_extended and !shown). Scroll the editor → `$16`
→ ASYNC `$15`. Accept tap → `$7` → save, loadMarkdown (guard changed), FRAMEWORK menu rebuild, animateAccept; ENTERS S_DIARY_VIEW.
Accept long-press → `$8`.
All Diary pages: any touch → `Diary.dispatchTouchEvent` → FRAMEWORK `GestureListener.onDown`; one-finger fling → FRAMEWORK
`GestureListener.onFling` (returns, multi false); two-finger fling or a pinch followed by a fling → `onFling@MULTI` → onSwipeLeft
(fling left: next day), onSwipeRight (previous day), onSwipeUp (next month), onSwipeDown (previous month) (3447-3480;
thresholds 256 px and 256 px/s) → getNext/PrevCalendarDay/Month, changeDate, animateSwipeLeft/Right (markdown and shown); ENTERS S_DIARY_VIEW.
Rotation, Home, Back as in 7.2.

### 7.5 Diary menus (C) — main.xml items and handlers (onOptionsItemSelected 661-726)
| id | title | handler | visible/enabled (onPrepareOptionsMenu 622-654) |
|---|---|---|---|
| cancel | Cancel (✕ icon) | cancel | visible iff changed |
| prevEntry | Previous (◀) | prevEntry | enabled iff prevEntry != null |
| nextEntry | Next (▶) | nextEntry | enabled iff nextEntry != null |
| today | Today | today | enabled iff the shown date is not today |
| goToDate | Go to date… | goToDate(currEntry) | always |
| index | Index | index | visible iff pref_use_index |
| link | Add link (overflow) | addIndexLink | visible iff pref_use_index |
| search | Search… (SearchView) | default → super; SearchView expands → S_DIARY_SEARCH | always |
| findAll | Find all… (overflow) | findAll | visible iff SearchView expanded (needs overflow open while expanded) |
| print | Print… | print | overflow |
| share | Share… | share | overflow |
| addTime | Add time | addTime | overflow |
| addEvents | Add events | addEvents | overflow |
| addMedia | Add media… | addMedia() | overflow |
| editStyles | Edit styles… | editStyles | overflow |
| editScript | Edit script… | editScript | overflow |
| backup | Backup… | backup | overflow |
| settings | Settings | settings | overflow |
| android.R.id.home | Up arrow | onBackPressed | only while the Up arrow is shown |
Also: `S_DIARY_* → Diary.onPrepareOptionsMenu` GUI "Open More options (⋮)" (section 6), and
`onPrepareOptionsMenu → Diary$QueryTextListener.<init>` CALL + REGISTER onQueryTextChange/onQueryTextSubmit (645).

Handlers:
- `cancel` → `alertDialog(int,int,int,int,OnClickListener)` → ENTERS S_DLG_SAVE_CHANGES; `S_DLG_SAVE_CHANGES → lambda$cancel$17`
  GUI Save/Discard → save + load (Save) or load (Discard); ENTERS S_DIARY_VIEW (shown) / S_DIARY_EDIT; Back cancels the dialog.
  `cancel → load` guard !changed (unreachable branch, NOTES).
- `goToDate` → showCustomCalendarDialog (pref_custom, ENTERS S_DLG_CALENDAR@GOTO; → `EntryDecorator.<init>`; FRAMEWORK
  `EntryDecorator.decorate` per day cell) / showDatePickerDialog (only from `Diary.onOptionsItemSelected@NOCUSTOM` →
  `Diary.goToDate@NOCUSTOM` → ENTERS S_DLG_DATE_PICKER). Dialog OK → `onDateSet(...)` → changeDate (push entryStack),
  `addMedia(Intent)` only in SEND/GEO contexts (haveMedia); ENTERS S_DIARY_VIEW. Calendar month arrows/day taps → decorate.
- `findAll` → `FindTask.<init>`, ASYNC `FindTask.doInBackground` → listEntries, getHome, read, parseTime; ASYNC `onPostExecute`
  → ENTERS S_DLG_FIND_ALL; `S_DLG_FIND_ALL → FindTask.lambda$onPostExecute$1` GUI tap a result (guard non-empty) → changeDate,
  ASYNC `lambda$onPostExecute$0` (setQuery → FRAMEWORK onQueryTextChange); ENTERS S_DIARY_VIEW.
- `print` → ENTERS S_PRINT; `S_PRINT → Diary.onResume` SYSTEM Back/print.
- `share` → `FileProvider.getUriForFile` → getPathStrategy, `SimplePathStrategy.getUriForFile` (interface call 401);
  ENTERS S_CHOOSER_SHARE@IMAGE (shown) / @TEXT (!shown).
- `addTime` → FRAMEWORK `Diary$2.*` (editable.insert), loadMarkdown; ENTERS _CHANGED (4.6).
- `addEvents` → `QueryHandler.queryEvents` → `QueryHandler.<init>` (first call); ASYNC `QueryHandler.onQueryComplete` (INSTANCE_LISTEN)
  → `lambda$addEvents$18` (guard rows, env ENV_CAL_EVENT) → loadMarkdown; ENTERS _CHANGED.
- `addMedia()` → ENTERS S_MEDIA_PICKER@PLAIN (or `@COPY` from the COPY context). `S_MEDIA_PICKER@X → Diary.onActivityResult@ADD_MEDIA[_COPY]`
  RESULT (pick an image/audio/video, or another file); Back → onActivityResult (RESULT_CANCELED returns at 765).
  `onActivityResult@ADD_MEDIA` → `resolveContent` (content URI) → `FileUtils.getPath` → isExternalStorageDocument /
  isDownloadsDocument / isMediaDocument / getDataColumn / isGooglePhotosUri / fileProviderPath (guards per picker root);
  → `FileUtils.getDisplayName` (env ENV_NO_PATH), `FileUtils.getMimeType(Context,Uri)` (file URI), → `addMedia(Uri,boolean)`
  (image/audio/video) or `addLink` (other or unknown type). Fixtures: `_fixtures/Pictures`, `Music`, `Download/*.pdf|.txt|.md`.
- `editStyles/editScript` → getHome; INTENT `Editor.<init>@STYLES` (startActivityForResult EDIT_STYLES; both use code 2).
- `backup` → getHome, saveAsDialog → ENTERS S_DLG_BACKUP; `lambda$backup$19`: Save (non-empty path) → `ZipTask.<init>` → FRAMEWORK
  `ZipTask.onPreExecute` → `showToast(int)` → `showToast(String)`; ASYNC `doInBackground` → getHome, listFiles (recursive);
  ASYNC `lambda$doInBackground$0` (runOnUiThread on exception, e.g. a path in a missing folder) → `alertDialog(int,String,int)`
  → S_DLG_ERROR; ASYNC `onPostExecute` → showToast(int). Storage → ENTERS S_DOC_CREATE → `Diary.onActivityResult@CREATE_BACKUP`
  → ZipTask chain. Cancel → nothing.
- `settings` → INTENT `Settings.<init>`.
- `index` → changeDate. `addIndexLink` (only via `@INDEX`) → index, `dateCheck(CharSequence,String,Date)` → `alertDialog(int,String,int)`
  (guard invalid pattern in pref_index_template, e.g. `<<date q>>`), loadMarkdown; ENTERS S_DIARY_VIEW_CHANGED.
- Search page: type → `QueryTextListener.onQueryTextChange`; submit (keyboard Go or the arrow) → `onQueryTextSubmit`; Back
  collapses → ENTERS base page.

### 7.6 External entries into Diary (E)
For each context X (5.2): `S_ENTRY → Diary.<init>@X` ENTRY with the concrete outside action:
SEND_TEXT "In another app share text or a link (e.g. select text and Share, or share a .txt from Files), pick Diary";
SEND_IMAGE "Share an image/audio/video file from Files or Gallery, pick Diary"; SEND_MULTI "Select several images in Files, Share, pick Diary";
GEO "Open a geo: link (e.g. a map link in Browser) and pick Diary"; WIDGET from S_HOME_WIDGET (GUI, 7.10).
Then `Diary.<init>@X → onCreate@X` → today, `mediaCheck(Intent)@X` (1290-1300) → `goToDate@X` → `showCustomCalendarDialog@X`
→ ENTERS `S_DLG_CALENDAR@X` → GUI OK → `onDateSet(CustomCalendarView,int,int,int)@X` → changeDate, `addMedia(Intent)@X` →
- TEXT: http(s) text → `addLink` (1577); plain text → append + loadMarkdown; EXTRA_STREAM → `resolveContent`, `addLink` (1600)
- IMAGE (SEND): `resolveContent`, `addMedia(Uri,boolean)` (1611-1636)
- MULTI: `resolveContent`, `addMedia(Uri,boolean)` per URI (1641-1650)
- GEO: `addMap` (1557-1558)
`addLink` → `addLinkDialog` → ENTERS S_DLG_ADD_LINK → GUI Add link → `lambda$addLink$21` → loadMarkdown → ENTERS _CHANGED.
Self-share from S_CHOOSER_SHARE reaches the in-process provider: `resolveContent → FileUtils.getPath → getDataColumn` queries
`content://org.billthefarmer.diary.fileprovider/...` → FRAMEWORK `FileProvider.query` → `SimplePathStrategy.getFileForUri`,
`copyOf(String[],int)`, `copyOf(Object[],int)`; then `fileProviderPath` (FileUtils.java:288-339). For the IMAGE self-share,
the inserted `![Diary.png](content://...)` is rendered by the WebView, which reads it through the provider
(`FileProvider.openFile` → `modeToMode`, `getType`; INFERRED/FW-MEMORY). External share targets reading the stream give the
same three callbacks (GUI from S_CHOOSER_SHARE "pick an app that opens the shared file, e.g. Messaging").
Also `S_CHOOSER_SHARE@X → Diary.onResume` SYSTEM (Back or after the target app returns).

### 7.7 Settings (B, C, D)
- `Diary.settings → Settings.<init>` INTENT; `<init> → onCreate` LIFECYCLE (theme switch 57-90) → `SettingsFragment.<init>` CALL (94).
- `SettingsFragment.<init> → onCreate` LIFECYCLE (FW-MEMORY fragment transaction); `onCreate` → FRAMEWORK `AboutPreference.<init>`,
  `DatePickerPreference.<init>` (preference inflater, preferences.xml:92,121,172), FRAMEWORK `DatePickerPreference.onSetInitialValue`
  (FW-SRC Preference.java:1547-1561; guard key already persisted; needs_state "Index page or Template page was set with OK on an earlier
  Settings visit"), CALL `DatePickerPreference.getValue` (71, 90). `onCreate → onResume` LIFECYCLE; `onResume` REGISTER
  `onSharedPreferenceChanged` (111-112); ENTERS S_SETTINGS.
- `S_SETTINGS → SettingsFragment.onPreferenceTreeClick` GUI tap any enabled row (FW-SRC Preference.java:1146).
- `S_SETTINGS → SettingsFragment.onSharedPreferenceChanged@<KEY>` GUI tap the checkbox row (value always changes) for
  CUSTOM, MARKDOWN, EXTENDED, USE_INDEX, USE_TEMPLATE, EXTERNAL, COPY_MEDIA; each ENTERS `S_SETTINGS@<KEY>` (Settings stays shown).
- Dialog rows: Folder → ENTERS S_DLG_FOLDER → OK with a different value → `onSharedPreferenceChanged@FOLDER` (148-159);
  Theme → S_DLG_THEME → `@THEME` → SYSTEM `Settings.<init>` (recreate 205-206, guard SDK != 23); About → GUI
  `AboutPreference.onBindDialogView` → ENTERS S_DLG_ABOUT; on `S_SETTINGS@USE_INDEX`: Index page → GUI
  `DatePickerPreference.onCreateDialogView@INDEX` → ENTERS S_DLG_DATE_PREF@INDEX; Index template → S_DLG_INDEX_TEMPLATE →
  `@INDEX_TEMPLATE`; on `S_SETTINGS@USE_TEMPLATE`: Template page → `onCreateDialogView@TEMPLATE` → S_DLG_DATE_PREF@TEMPLATE.
  In S_DLG_DATE_PREF@X: change the date → `DatePickerPreference.lambda$onCreateDialogView$0`; OK/Cancel →
  `DatePickerPreference.onDialogClosed` → (positive and value changed) `onSharedPreferenceChanged@INDEX_PAGE|TEMPLATE_PAGE`
  (FW-SRC SharedPreferencesImpl notifies only on change). Dialog Cancel/Back → ENTERS the Settings page.
- Up: `S_SETTINGS[@KEY] → Settings.onOptionsItemSelected[@KEY]` GUI → SYSTEM `Diary.onResume[@KEY]` (finish 113).
  Back: SYSTEM `S_SETTINGS[@KEY] → Diary.onResume[@KEY]`. Home: `S_SETTINGS → SettingsFragment.onPause` → S_SETTINGS_PAUSED → onResume.
- `Diary.onResume@KEY` → ENTERS the Diary variant (5.2). Keep these variants minimal: the ENTERS edge plus a note
  "other calls as Diary.onResume".

### 7.8 Editor (B, D, E)
- INTENT `Diary.editStyles/editScript → Editor.<init>@STYLES`; ENTRY `S_ENTRY → Editor.<init>@EXTERNAL` "Open a text file
  (e.g. _fixtures Download/todo.txt) from Files with 'Open with' → Diary's Editor" (manifest 85-98, VIEW/EDIT text/*).
- `onCreate@X` (72-136): theme switch, Up enabled (110); `resolveContent` (content URI, EXTERNAL only) → `FileUtils.getPath`;
  `read` (guard savedInstanceState == null) → permission request (ENV_NOPERM → S_PERMISSION@EDITOR); setText before the watcher
  is registered (no watcher call); `setListeners` → `Editor$1.<init>`, REGISTER `Editor$1.*`, `lambda$0`, `lambda$1`, `lambda$2`;
  ENTERS `S_EDITOR@X`.
- `S_EDITOR@X`: type → `Editor$1.afterTextChanged@TYPED` (+ before/on) → ENTERS `S_EDITOR_CHANGED@X`; long-press text → `lambda$setListeners$0`;
  Accept → `lambda$setListeners$1@X` → `write` (guard changed) → `alertDialog(int,String,int)` (ENV_IO_ERROR) / permission request;
  RESULT_OK + finish → `Diary.onActivityResult@EDIT_STYLES` (STYLES; then markdownView.reload, then LIFECYCLE Diary.onResume) or
  ENTERS S_EXIT (EXTERNAL). Accept long-press → `lambda$2`. Up → `onOptionsItemSelected@X` → `onBackPressed@X`. Back →
  `onBackPressed@X`: unchanged → RESULT_CANCELED finish (STYLES: `Diary.onActivityResult` returns early, then Diary.onResume);
  changed → `alertDialog(int,int,int,int,OnClickListener)` → ENTERS S_DLG_EDITOR_SAVE@X → `lambda$onBackPressed$3@X` (Save → write, RESULT_OK; Discard → RESULT_CANCELED).
- Rotation: `S_EDITOR*@X → Editor.onSaveInstanceState` SYSTEM → `Editor.<init>@X` → onCreate (no read) → LIFECYCLE
  `Editor.onRestoreInstanceState` (215-217). Home → onSaveInstanceState → S_EDITOR_PAUSED.
- Permission: `S_PERMISSION@EDITOR → Editor.onRequestPermissionsResult` → read (REQUEST_READ) / write (REQUEST_WRITE).

### 7.9 QueryHandler (E)
`queryEvents` (76-96) and `insertEvent` (99-117) create the static handler and call startQuery; ASYNC `onQueryComplete`
(FW-SRC AsyncQueryHandler.java:343-344): INSTANCE_LISTEN → listener.onEvent = `Diary.lambda$addEvents$18` (env ENV_CAL_EVENT);
EVENT_INSERT → startInsert → ASYNC `onInsertComplete` (env ENV_CAL_ACCOUNT, ENV_24H) → EVENT_REMIND → second startInsert →
`onInsertComplete` again (EVENT_DONE, no-op). Empty or null cursor returns at once (124-125).

### 7.10 Widget (E)
- `S_ENTRY → DiaryWidgetProvider.<init>@ADD` ENTRY "Home screen: long-press → Widgets → drag Diary onto the screen" (manifest
  108-117; no configure activity). `<init>@X → onReceive@X` LIFECYCLE for every context; `onReceive` (75-96) writes
  `pref:pref_widget_entry`, FRAMEWORK super → `onUpdate` (guard non-empty id list) or `onAppWidgetOptionsChanged` (RESIZE).
  `@ADD` also sends OPTIONS_CHANGED (Launcher3 sets the size: FW-MEMORY).
- `onUpdate` (117-186) → getText → `Diary.read` (+ `Diary.<clinit>` guard), `getFile(Calendar)` → getDay → getMonth → getYear → getHome;
  ENTERS S_HOME_WIDGET.
- `S_HOME_WIDGET` GUI: tap the entry text/body → `Diary.<init>@WIDGET` (PendingIntent with ENTRY extra) → `onCreate@WIDGET` →
  `changeDate(long)` (508-509) → ENTERS S_DIARY_VIEW; tap ◀ / ▶ / today icon → `DiaryWidgetUpdate.<init>@PREV|NEXT|TODAY` →
  `onCreate@X` → PREV: getPrevEntry chain (prevDay/prevMonth/prevYear → Diary.listDays/... static), NEXT: getNextEntry chain,
  TODAY: nothing; then sendBroadcast (setPackage-limited, see 6) → INTENT `DiaryWidgetProvider.<init>@BUTTON`; ENTERS S_HOME_WIDGET
  (finish 123). Resize → `<init>@RESIZE`. Wait an hour → SYSTEM `<init>@PERIODIC`. Remove → GUI `<init>@DELETED` → onReceive only
  → ENTERS S_ENTRY.
- `onReceive@APP → onUpdate` with needs_state "a Diary widget is already on the home screen".
- Hazard candidate (FW-MEMORY, UNVERIFIED): the NoDisplay trampoline started with NEW_TASK joins an existing Diary task, so
  tapping ◀/▶ while Diary is in the background may bring Diary to the front. Model as `DiaryWidgetUpdate.onCreate@X → Diary.onResume`
  SYSTEM with needs_state "Diary task alive in the background" and evidence FW-MEMORY.

## 8. Round G: DEAD and FRAMEWORK_ONLY (with the search scope each verdict needs)

Search scope for every DEAD verdict: all 11 app source files (grep), the bytecode `invoke*`/`invokedynamic` scan of all 23
non-instrumentation classes (`.plan/app_callers.txt`), res/ XML (no `android:onClick`, no class names besides
AboutPreference/DatePickerPreference in preferences.xml), and reflection (grep for `forName|getMethod|getDeclared|newInstance|getIdentifier|addJavascriptInterface`: no hits).
The 3 JacocoInstrument classes reference no app class. Put the scope sentence in each DEAD reason.

DEAD (17):
1. `Diary.getEntries()` — no caller (Diary.java:2152-2156)
2. `Diary.getEntries(Calendar)` — only caller is the dead `getEntries()` (2155)
3. `DiaryWidgetProvider.getFile()` — no caller (265-269)
4. `FileUtils.<init>` — private constructor never called (102-104); also not in the JaCoCo report
5. `FileUtils.copyFile(Context,Uri,Uri)` — no caller
6. `FileUtils.createGetContentIntent` — no caller (Diary.addMedia() builds its own intent, 1880-1886)
7. `FileUtils.getPathWithoutFilename` — no caller
8. `FileUtils.getReadableFileSize` — no caller
9. `FileUtils.getSize` — no caller
10. `FileUtils.getThumbnail(Context,Uri)` — no caller
11. `FileUtils.getThumbnail(Context,File)` — no caller
12. `FileUtils.getThumbnail(Context,Uri,String)` — only callers are the two dead overloads (732, 746)
13. `FileUtils.getUri` — only caller is dead `getThumbnail(Context,File)` (732)
14. `FileUtils.isMediaUri` — only caller is dead `getThumbnail(Context,Uri,String)` (765)
15-17. `FileUtils.lambda$static$0`, `lambda$static$1`, `lambda$static$2` — function objects created in `<clinit>` (65-100) and
   stored in `sComparator`, `sFileFilter`, `sDirFilter`; no code reads those fields (grep of all sources), so compare/accept never run.

FRAMEWORK_ONLY (4):
1. `DatePickerPreference.onGetDefaultValue` — the framework calls it only for an `android:defaultValue` attribute
   (FW-SRC Preference.java:293-294, the only call site in Preference.java); neither DatePickerPreference in preferences.xml
   (92-97, 121-126) has one; the app never calls it.
2-4. `FileProvider.insert`, `FileProvider.update`, `FileProvider.delete` — the app never calls insert/update/delete on its own
   authority (all sources: the only ContentResolver writes are QueryHandler.startInsert on Calendar URIs); the provider is not
   exported (manifest 122) and Diary grants only read access when sharing (FW-SRC Intent.java:10001-10012); ContentProvider.Transport
   reaches these methods only after enforceWritePermission (ContentProvider.java:256-265, 333-357). (insert/update would throw anyway.)

Not dead although never hit (check you do not mark them): `FileProvider.query/getType/openFile/modeToMode/copyOf*` and
`SimplePathStrategy.getFileForUri` (share target or self-share, 7.6), `DiaryWidgetProvider.onAppWidgetOptionsChanged` (widget resize),
`Editor.onRestoreInstanceState` (rotate in Editor), `Diary.onRequestPermissionsResult`/`Editor.onRequestPermissionsResult` (ENV_NOPERM),
`QueryHandler.onInsertComplete` (ENV_24H + ENV_CAL_ACCOUNT), `DatePickerPreference.onSetInitialValue` (hit by APE).

## 9. TARGETS (78 reachable, never hit by the baseline) and why the baseline missed them

Group them like this in the README (counts must match the build report; re-derive after the build):
- Home-screen widget (22): `DiaryWidgetProvider.{onUpdate, onAppWidgetOptionsChanged, getText, getFile(Calendar), getDay, getMonth, getYear, getHome}`,
  `DiaryWidgetUpdate.{<init>, onCreate, getPrevEntry, getNextEntry, prevDay, prevMonth, prevYear, nextDay, nextMonth, nextYear, getHome, getYear, getMonth}`,
  `Diary.changeDate(long)` (widget body tap). Outside the package.
- Share target / incoming intents / pickers outside the app (28): `Diary.{addMedia(Intent), addMedia(Uri,boolean), addMap, addLink,
  addLinkDialog, lambda$addLink$21, resolveContent}`, `FileProvider.{query, getType, openFile, modeToMode, copyOf(String[],int), copyOf(Object[],int)}`,
  `FileProvider$SimplePathStrategy.getFileForUri`, `FileUtils.{getPath, getDataColumn, fileProviderPath, getDisplayName, getMimeType(Context,Uri),
  isExternalStorageDocument, isDownloadsDocument, isMediaDocument, isGooglePhotosUri}`, `Editor.resolveContent`;
  copy-media chain `FileUtils.{getFile, isLocal, copyFile(File,File), getPathWithoutExtension}` (needs Copy images on + a picked image).
  The system chooser/picker belongs to another package, which Monkey's package restriction blocks.
- Two-finger swipe (10): `Diary.{onSwipeLeft, onSwipeRight, onSwipeUp, onSwipeDown, getNextCalendarDay, getPrevCalendarDay,
  getNextCalendarMonth, getPrevCalendarMonth, animateSwipeLeft, animateSwipeRight}` (a fling right after a multi-pointer touch).
- Find all (8): `Diary.{findAll, listEntries, parseTime}`, `Diary$FindTask.{<init>, doInBackground, onPostExecute, lambda$onPostExecute$1, lambda$onPostExecute$0}`
  (open Search, then the overflow, then Find all).
- Template on an empty entry (1): `Diary.dateCheck(CharSequence,String)` (Use template + Edit on an empty entry).
- Error dialogs (3): `Diary.alertDialog(int,String,int)` (invalid `<<date …>>` pattern, write error, backup error),
  `Diary$ZipTask.lambda$doInBackground$0` (backup to a missing folder), `Editor.alertDialog(int,String,int)` (ENV_IO_ERROR).
- Environment-gated (5): `Diary.onRequestPermissionsResult`, `Editor.onRequestPermissionsResult` (ENV_NOPERM),
  `Diary.lambda$addEvents$18` (ENV_CAL_EVENT), `QueryHandler.insertEvent` (ENV_24H), `QueryHandler.onInsertComplete` (ENV_24H + ENV_CAL_ACCOUNT).
- Rotation in Editor (1): `Editor.onRestoreInstanceState`.
(Exact per-group counts: recount from methods.csv; the list above has 78 names.)

## 10. NOTES (branch-level, put in NOTES)

- `Diary.cancel`: the `else load()` branch (1227-1228) is unreachable from the menu: Cancel is visible only while changed (632).
- `Diary.onOptionsItemSelected`: R.id.search and unknown ids fall to `default` (717-718) and skip the collapse at 722.
- `Diary.addMap`: the `else` branch after `if (true)` (2878-2886) is dead code.
- `Diary.mediaCheck(CharSequence)`: the non-geo `type == null` branch (1426-1428) and the image branch (1430-1433) do nothing.
- `Diary.onResume`: on the first launch the help text sets changed (2387), so onPause saves it as today's entry (598-600).
- `Diary.eventCheck` / `QueryHandler.insertEvent`: event lines parse only in 24-hour locales (ENV_24H).
- `DatePickerPreference.onSetInitialValue`: the `restorePersistedValue == false` branch (87-92) is unreachable (no default value, Preference.java:1555-1557).
- `SettingsFragment.onPreferenceTreeClick`: the PreferenceScreen branch (133-138) is unreachable (no nested screen in preferences.xml).
- `Settings.onOptionsItemSelected`: `return false` (117) unreachable (no menu besides Up). `Editor.onOptionsItemSelected`: super branch unreachable.
- `QueryHandler.onInsertComplete`: EVENT_DONE does nothing (185-186).
- `DiaryWidgetProvider.onUpdate`: line 164 sets the data of `intent` instead of `today` (typo); no visible effect (the PendingIntents still differ).
- `Diary$GestureListener.onFling`: returns at once unless a multi-pointer touch came first (multi, 3440).
- `S_DIARY_PLAIN` handling per 4.7 (state it on `Diary.setVisibility` or `Diary.onResume`).

## 11. Hazard candidates (from reading; not reproduced; README section "Hazard candidates")

1. `Diary.addMedia(Intent)`: SEND of image/audio/video without EXTRA_STREAM dereferences `media` before the null check
   (Diary.java:1615 vs 1618) → NullPointerException; SEND_MULTIPLE without a stream list → NPE at 1643. Triggered by another app's intent.
2. `Diary.share()` with shown == true in a Diary instance that never displayed the MarkdownView (pref_markdown off from the
   start: ViewSwitcher keeps child 1 GONE, setVisibility 1713-1717) → `getDrawingCache()` likely null → `Bitmap.createBitmap(null)`
   NPE at 1817 (INFERRED).
3. First launch silently saves the help text as today's entry (2387 + 598-600).
4. Events (`@ 10:30 Title`, help.md:220) are never added to the calendar in en-US: SHORT time format "h:mm a" cannot parse "10:30" (1307-1323).
5. With markdown off, `shown` stays true, so Search looks in the hidden MarkdownView (3337-3338): nothing is highlighted.
6. `haveMedia` stays true when the date dialog for received media is cancelled; the next Go to date + OK inserts the media again (823-824, 1655).
7. Editor opened with a content URI that FileUtils.getPath cannot map keeps `file == null`; Accept/Save then drop the edits silently
   and still return RESULT_OK (Editor.java:125-126, 411).
8. `FileUtils.getPath` on an external-storage root document id like `primary:` would throw ArrayIndexOutOfBounds (split[1], 501-503); unlikely from a file picker.
9. `QueryHandler.onQueryComplete` never closes the cursor (leak).
10. Widget ◀/▶ may bring a background Diary task to the front (7.10; UNVERIFIED).

## 12. Implementation plan (ordered checklist)

All verification uses the real build: `python3 -I tools/build_graph.py graphs/Diary diary` (from `/Users/darshan/Desktop/yang/work`),
then read `graphs/Diary/out/build_report.txt`. Until step 9 the build exits 1 with "method has no path" / "page not reachable"
errors for parts not yet written; at every step there must be **no** `unknown ... node`, `bad kind`, `GUI edge must go`,
`ENTERS edge must end`, `missing/invalid evidence` or `verdict for unknown method` errors.

- [ ] 1. Create `graphs/Diary/graph_def.py` skeleton: header comment (version, commit, files read, label policy), `TITLE`, the ENV
      constants of 4.4, FW citation constants (one per row of section 6, e.g. `FW_OVERFLOW_PREPARE`, `FW_WIDGET_PKG`), the full
      `SCREENS` dict with the base pages of 5.1 only (variants such as `S_DLG_CALENDAR@GOTO` are written only in edges;
      build_graph resolves `S_X@CTX` to its base `S_X`, which must be in SCREENS), `DEAD` (the 17 of section 8, each with
      the scope sentence), `FRAMEWORK_ONLY` (the 4 of section 8), `NOTES` (section 10).
      Files: graphs/Diary/graph_def.py
      Verify: build runs; report shows 286 methods and ~40 pages; only "no path"/"page not reachable" errors.

- [ ] 2. Process start and Diary core: sections 7.1, 7.2, 7.3 (lifecycle, helpers, load/save/markdown chain, widget broadcast
      INTENT to `DiaryWidgetProvider.<init>@APP`, permission ENTERS with ENV_NOPERM).
      Files: graph_def.py
      Verify: build; FileProvider start-up methods, Diary.onCreate/onResume/load/save chains and all navigation helpers no longer
      appear in "method has no path" errors.

- [ ] 3. Diary pages, gestures and menus: 7.4 and 7.5 with the dispatcher contexts of 5.2 (write a helper that emits the GUI edge
      + one CALL per visible item with `gui=['Tap …']`, per 4.3), dialogs S_DLG_CALENDAR@GOTO, S_DLG_DATE_PICKER, S_DLG_SAVE_CHANGES,
      S_DLG_BACKUP, S_DLG_FIND_ALL, S_DLG_ERROR, S_PRINT, S_CHOOSER_SHARE, S_MEDIA_PICKER, S_DOC_CREATE, S_PERMISSION@DIARY, the
      ZipTask/FindTask/QueryHandler chains (7.9), onActivityResult contexts.
      Files: graph_def.py
      Verify: build; every Diary-only page is reachable; remaining "no path" errors only for Settings-context, Editor, widget,
      SEND/GEO and FileUtils/FileProvider-on-demand methods.

- [ ] 4. External entries and the content-URI chains: 7.6 (SEND_TEXT/SEND_IMAGE/SEND_MULTI/GEO/WIDGET contexts, self-share,
      FileProvider query/getType/openFile, FileUtils.getPath family, addLink dialog).
      Files: graph_def.py
      Verify: build; `FileProvider.query`, `FileUtils.getPath`, `Diary.addMap`, `Diary.addMedia(Intent)` have paths that start with the
      intended ENTRY (check their `shortest_path` in out/methods.csv).

- [ ] 5. Settings and preference contexts: 7.7 including `S_SETTINGS@KEY`, `Diary.onResume@KEY` and the Diary variant pages
      (@INDEX, @NOCUSTOM, @TEMPLATE, @COPY, S_DIARY_PLAIN, THEME recreate), the copy-media chain.
      Files: graph_def.py
      Verify: build; `Diary.index`, `Diary.addIndexLink`, `Diary.showDatePickerDialog`, `Diary.dateCheck(CharSequence,String)`,
      `FileUtils.copyFile(File,File)` paths go through Settings (read their shortest_path).

- [ ] 6. Editor: 7.8 (both contexts, permission page @EDITOR, rotation).
      Files: graph_def.py
      Verify: build; no Editor method left in "no path" errors; `Editor.resolveContent` path starts at `Editor.<init>@EXTERNAL`.

- [ ] 7. Widget: 7.10.
      Files: graph_def.py
      Verify: build; S_HOME_WIDGET reachable; all 21 widget methods have paths starting with `DiaryWidgetProvider.<init>@ADD`.

- [ ] 8. Remaining gaps: run the build and resolve every remaining "method has no path" error by adding the missing edge (never by
      adding a verdict unless section 8 lists it). Confirm every DEAD/FRAMEWORK_ONLY method has no non-REGISTER incoming edge (warnings list).
      Files: graph_def.py
      Verify: `errors: 0`, `0 DEAD/FRAMEWORK_ONLY but hit (contradictions)`, `not in the JaCoCo report: FileUtils.<init>`,
      verdicts 17 DEAD + 4 FRAMEWORK_ONLY, warnings explained or fixed.

- [ ] 9. Path review (GRAPH_PROMPT step 4): read the `shortest_path` and `gui_steps_on_shortest_path` columns in out/methods.csv for at least
      these 36 methods and fix shortcuts with variants/needs_state/removing a wrong ENTERS: `Diary.findAll`, `Diary$FindTask.lambda$onPostExecute$0`,
      `Diary.onSwipeUp`, `Diary.changeDate(long)`, `Diary.dateCheck(CharSequence,String)`, `Diary.addMap`, `Diary.addMedia(Uri,boolean)`,
      `FileUtils.copyFile(File,File)`, `FileUtils.getDisplayName`, `FileProvider.query`, `FileProvider.openFile`, `FileProvider$SimplePathStrategy.getFileForUri`,
      `Diary.alertDialog(int,String,int)`, `Diary$ZipTask.lambda$doInBackground$0`, `Diary.lambda$addEvents$18`, `QueryHandler.onInsertComplete`,
      `DiaryWidgetUpdate.prevYear`, `DiaryWidgetProvider.onAppWidgetOptionsChanged`, `Editor.onRestoreInstanceState`, `Editor.resolveContent`,
      `Editor.alertDialog(int,String,int)`, `Diary.onRequestPermissionsResult`, `DatePickerPreference.onSetInitialValue`,
      `DatePickerPreference.lambda$onCreateDialogView$0`, `Diary.onDateSet(DatePicker,int,int,int)`, `Diary.index`, `Diary.addIndexLink`,
      `Diary.template`, `Diary.lambda$cancel$17`, `Diary.onActionModeStarted`, `Diary$GestureListener.lambda$onDoubleTap$0`,
      `Diary.lambda$setListeners$4`, `Diary.onRestoreInstanceState`, `Diary$1.shouldOverrideUrlLoading`, `Diary.share`, `AboutPreference.onBindDialogView`.
      Check especially: no path reaches a SEND/GEO-only method from the launcher context; no path uses a Settings-only Diary variant
      without the Settings steps; no path reaches Find all without opening Search; swipe paths use `onFling@MULTI`; the menu rows show
      the item tap. Record each fix (method, wrong path, fix) for the README.
      Files: graph_def.py
      Verify: build `errors: 0`; re-read the fixed paths.

- [ ] 10. Write `graphs/Diary/out/README.md` with the structure of `graphs/Currency/out/README.md`: what is in the folder (prefix diary),
      numbers (methods/pages/edges/verdicts from build_report.txt), the 287 vs 286 reconciliation (section 2, stated exactly), comparison
      with the baseline (hit counts inside the universe 164/186/187, 0 contradictions, the target groups of section 9 with counts,
      FileUtils.<init> not in the report), how much to trust it (evidence label counts from the report; FW-SRC sources in `.plan/fw_src`;
      not checked on a device; the paths fixed in step 9), the resolved implicit-broadcast question (section 6 row 4), hazard candidates
      (section 11), limits (4.3 menu-label workaround, 4.6 and 4.7 approximations, pages modelled by hand, guards ignored by the shortest path),
      JSON shape.
      Files: graphs/Diary/out/README.md
      Verify: rebuild once more so out/ matches graph_def.py; every number in the README equals build_report.txt.

## 13. Open questions (keep as UNVERIFIED in the graph, list in the README)

- Whether Monkey/APE could reach the share sheet target list at all (the chooser is in package `android`); the README should say "outside the package" without claiming the exact Monkey filter rule.
- Launcher3 behaviour for widget add/resize/remove (FW-MEMORY).
- WebView loading `content://` images via our FileProvider (openFile/getType) — INFERRED.
- Widget trampoline bringing Diary to the front (hazard 10).
