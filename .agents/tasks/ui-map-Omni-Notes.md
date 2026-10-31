# Omni-Notes 6.1.0 (#745, playDebug): UI map and modeling plan

## Summary

- **No first-run gate in this build.** The intro tour is switched off because the APK is a debug build (`IntroActivity.mustRun()` returns false when `BuildConfig.BUILD_TYPE` is "debug"). The app needs no login, account, vault or import, asks for no permission at start, and creates its database on first access. The list screen (`MainActivity` with `ListFragment`) is usable at once. The only real gate is an optional password ("Request password on access"), which is off by default.
- **What actually limits exploration is missing data plus actions outside the package.** Many screens need notes in a particular state: archived, trashed, with a reminder, with a `#tag`, locked, with an image or video attachment, or with a category. Others need backups, or a password that neither tool ever set. Every external activity (camera, file picker, ringtone picker, share chooser, browser) is blocked under `monkey -p` (FW-MEMORY). The home screen, notification shade and system settings are outside the package too, so widgets, shortcuts, notifications, boot and notification access were never exercised.
- **Monkey produced no long-press at all.** All 6 long-click handlers have 0 Monkey hits, so it never entered multi-select. It never opened Settings either. APE did both. APE never reached Trash, Reminders, the Gallery, tags or any password flow.
- **Proposed decomposition: 4 areas, 97 pages.** A = shell, list and drawer (441 methods). B = note editor and attachments (334). C = settings, security, backup, stats, about, intro (218). D = core data layer, utilities and background/external components (433). Together that is 1426 methods and 234 classes (the 3 `JacocoInstrument` classes are excluded).
- **About 110 methods have no caller in the bytecode.** Examples: the whole `UpdaterTask` + `PlayStoreMetadataFetcherResult`, `VerticalSeekBar`, `ImageAndTextItem`, `LoadingDialog`, `Display.*`, several `DbHelper` queries, and the `GeocodeHelper` instance callbacks. Further code is unreachable through the UI or the build config: the intro, "Add shortcut" (menu item never made visible), the widget-colours preference listener, and the Places autocomplete (empty API key).
- **Mechanisms the graph must model:** greenrobot EventBus 2.4 (17 handlers), a reflection-based note loader (`NoteLoaderTask` calls `DbHelper` methods by name), DB upgrade via reflection, ButterKnife `_ViewBinding` classes, ~10 AsyncTasks, RxJava 1, AlarmManager, an IntentService, a JobIntentService, widgets with a RemoteViewsService, and a NotificationListenerService.

Conventions:
- `J/` = `/Users/darshan/Desktop/yang/work/final_java_only/Omni-Notes/app/Omni-Notes-#745/omniNotes/src/main/java/it/feio/android/omninotes/`. Java citations without a prefix are relative to `J/`.
- `res/` and `AndroidManifest.xml` are under `.../omniNotes/src/main/`.
- "JaCoCo" means `.../Omni-Notes/{monkey,ape}/report/report.xml`. M = Monkey hit, A = APE hit.
- `FW-MEMORY` = Android/library behaviour I recalled but did not check in framework source. `UNVERIFIED` = not confirmed. `INFERRED` = deduced from code and coverage data.
- Method lists come from the JaCoCo XML (java/javap are not usable on this machine). A small read-only Python parser of the compiled classes in `build/intermediates/javac/playDebug/classes/` supplied the bytecode call references used in section 5.

---

## 1. Entry points

There is no merged manifest: `omniNotes/build/intermediates` only contains `javac/`. The table below is `src/main/AndroidManifest.xml`; the play flavor has no manifest of its own. Library components that would be merged (LeakCanary's DisplayLeakActivity/services, ACRA senders, the RxPermissions shadow activity) are UNVERIFIED and contain no in-scope code.

Application class: `OmniNotes` (`AndroidManifest.xml:47-55`), a `MultiDexApplication`.
- `attachBaseContext` initialises ACRA (`OmniNotes.java:75-76`).
- `onCreate` installs LeakCanary (`OmniNotes.java:83,106`), enables StrictMode in debug builds (`OmniNotes.java:90,96-97`) and creates notification channels (`OmniNotes.java:92`; channels are only created when `SDK_INT > O`, i.e. on API 27+, `NotificationsHelper.java:56`).
- `onConfigurationChanged` re-applies the language (`OmniNotes.java:113-117`).
- Manifest attributes: `allowBackup=true`, `largeHeap`. The theme is `OmniNotesTheme.ApiSpec.Branded`.

| Component | exported | Intent filters / triggers | launchMode, theme, other | Cite |
|---|---|---|---|---|
| `MainActivity` | true (explicit) | MAIN/LAUNCHER; SEARCH (+ `res/xml/searchable.xml`, voice search); `com.google.android.gm.action.AUTO_SEND` `*/*`; SEND `*/*`; SEND_MULTIPLE `*/*`; VIEW + BROWSABLE, scheme `hashtag`. Being exported, it also accepts explicit custom actions handled in `handleIntents`: `action_restart_app`, `action_send_and_exit`, `action_shortcut`, `action_notification_click`, `action_widget`, `action_widget_take_photo`, `action_widget_show_list`, `action_shortcut_widget`, `action_merge`, `action_fab_take_photo` (`MainActivity.java:345-392`, `utils/ConstantsBase.java:59-76`) | singleTop; app theme; no configChanges (rotation recreates it) | `AndroidManifest.xml:65-114` |
| `GalleryActivity` | false (no filter) | started from the editor | `configChanges=orientation\|keyboardHidden\|screenSize`, fullscreen theme | `:117-120` |
| `CategoryActivity` | false | for-result from list/editor | `Theme.AppCompat.Light.Dialog` (dialog window), parent MainActivity | `:122-131` |
| `SettingsActivity` | false | from the drawer | PreferencesTheme, parent MainActivity | `:133-142` |
| `PasswordActivity` | false | from Settings and from editor "Lock" | `OmniNotesTheme.ApiSpec.Dialog` (floating, translucent, `styles.xml:66-74`), `windowSoftInputMode=stateHidden\|adjustResize` | `:144-147` |
| `AboutActivity` | false | preference intent `targetClass` (`res/xml/settings.xml:119-125`) | singleTop | `:150-153` |
| `intro.IntroActivity` | false | only from `MainActivity.onCreate`, guarded by `mustRun()` | PreferencesTheme | `:156-159` |
| `SnoozeActivity` | false | PendingIntents from reminder notifications; list "Add reminder" | singleInstance, noHistory, excludeFromRecents, `OmniNotesTheme.NoDisplay` (`windowNoDisplay=true`, `styles.xml:57-64`) | `:162-167` |
| `ShortcutActivity` | true (has filter) | CREATE_SHORTCUT (launcher "add shortcut") | — | `:170-179` |
| `StatsActivity` | false | preference intent `targetClass` (`settings.xml:111-117`) | dialog theme | `:181-183` |
| `NoteInfosActivity` | false | editor "Info" | dialog theme | `:184-186` |
| `widget.WidgetConfigurationActivity` | true | APPWIDGET_CONFIGURE (referenced by `res/xml/appwidget_list.xml` `android:configure`) | dialog theme | `:222-229` |
| `receiver.AlarmReceiver` | false | explicit PendingIntent from AlarmManager (`ReminderHelper.java:52-57`) | — | `:189` |
| `receiver.BootCompleteReceiver` | false (explicit) | BOOT_COMPLETED; permission RECEIVE_BOOT_COMPLETED | system broadcast still delivered (FW-MEMORY) | `:192-201` |
| `async.AlarmRestoreOnRebootService` | false | JobIntentService; permission BIND_JOB_SERVICE | `enqueueWork` on O+ (`AlarmRestoreOnRebootService.java:41-46`) | `:204-206` |
| `services.NotificationListener` | true | NotificationListenerService; permission BIND_NOTIFICATION_LISTENER_SERVICE | only bound if the user grants notification access | `:209-217` |
| `async.DataBackupIntentService` | false | IntentService started from Settings | — | `:219` |
| `widget.SimpleWidgetProvider` | true | APPWIDGET_UPDATE, `res/xml/appwidget_simple.xml` (no configure) | — | `:231-243` |
| `widget.ListWidgetProvider` | true | APPWIDGET_UPDATE, `res/xml/appwidget_list.xml` (configure = WidgetConfigurationActivity, resizable) | — | `:245-257` |
| `widget.ListWidgetService` | false | RemoteViewsService; permission BIND_REMOTEVIEWS | bound by the launcher | `:259-261` |
| `extensions.ONDashClockExtension` | true | DashClock Extension; permission READ_EXTENSION_DATA | needs the DashClock app | `:264-286` |
| `extensions.PushBulletExtension` | true | Pushbullet MessagingExtension | needs the Pushbullet app | `:288-297` |
| `androidx.core.content.FileProvider` | false | authority `${applicationId}.authority`, grantUriPermissions, `res/xml/file_provider_paths.xml` (external-path ".") | library class | `:299-307` |
| `JacocoInstrument.SMSInstrumentedReceiver` | (harness, ignore) | `edu.gatech.m3.emma.COLLECT_COVERAGE` | — | `:309-313` |

Not present: no content provider of the app's own, no deep-link host other than `hashtag:`, no static shortcuts XML, no file-type VIEW filters (shares of any MIME type go through SEND).

Implicit entries from outside the app:
- Reminder notification taps and actions → `SnoozeActivity` (`receiver/AlarmReceiver.java:85-113`).
- Widget buttons → `MainActivity` with `action_widget`, `action_widget_show_list`, `action_widget_take_photo` (`widget/WidgetProvider.java:74-90`); list-widget rows → `action_widget` (`widget/ListWidgetProvider.java:73-78`).
- Launcher shortcut created by `ShortcutActivity` → `action_shortcut_widget` (`ShortcutActivity.java:33-34`).
- DashClock tile → ACTION_MAIN (`extensions/ONDashClockExtension.java:99-107`).
- Backup-import notification → `action_restart_app` (`async/DataBackupIntentService.java:176-188`).

---

## 2. First-run flow and setup gates

### 2.1 What happens on a fresh install

1. `OmniNotes.attachBaseContext`/`onCreate` run (see section 1).
2. `MainActivity.onCreate` (`MainActivity.java:93-109`):
   - `BaseActivity.attachBaseContext` calls `LanguageHelper.updateLanguage`, which on first run stores the device locale into pref `settings_language` (`BaseActivity.java:72-75`, `helpers/LanguageHelper.java:45-61`).
   - `BaseActivity.onCreate` uses reflection on `ViewConfiguration.sHasPermanentMenuKey` (`BaseActivity.java:77-92`).
   - `setContentView` inflates the static `NavigationDrawerFragment` (`res/layout/activity_main.xml:54-61`).
   - The activity registers with EventBus (`MainActivity.java:98`) and registers the prefs listener.
   - **Intro gate (disabled):** `if (IntroActivity.mustRun()) startActivity(IntroActivity)` (`MainActivity.java:103-105`). `mustRun()` returns `!OmniNotes.isDebugBuild() && !pref_tour_complete` (`intro/IntroActivity.java:48-51`), and `isDebugBuild()` compares `BuildConfig.BUILD_TYPE` with "debug" (`OmniNotes.java:55-57`). The compiled `BuildConfig.class` contains the constants "debug" and "play" (read from the class file), and the module builds variant playDebug (`class_files.json`). So the intro never starts. JaCoCo agrees: only `IntroActivity.mustRun` ran (M and A); `init`, `onDonePressed` and all slides never ran.
3. `MainActivity.onResume`: `isPasswordAccepted` is a static field, false on first run, so `checkPassword()` runs (`MainActivity.java:111-118`).
   - **Password gate:** active only if pref `password` != null **and** `settings_password_access` == true (`MainActivity.java:138-156`). Both are unset by default, so `init()` runs directly.
   - When the gate is active, `PasswordHelper.requestPassword` shows a dialog. SUCCEED → `init()`; FAIL (cancel) → `finish()`; RESTORE → `resetPassword` (`utils/PasswordHelper.java:49-139`).
4. `init()` adds `ListFragment` (`MainActivity.java:165-184`); the drawer-creation branch at `:172-176` is dead because the fragment is static in the layout.
5. `ListFragment.init` → `initNotesList` → `NoteLoaderTask("getAllNotes")` (`ListFragment.java:250-261,1051-1121`). The first `DbHelper.getWritableDatabase/getReadableDatabase` creates the DB through `DbHelper.onCreate` → `assets/sql/create.sql` via `SqlParser` (`db/DbHelper.java:180-188,274-284`).
6. With no notes, the result is the empty list with the "Mr. Jingles" empty view (`ListFragment.java:1227-1229,325-338`). That page is usable.
7. **Permissions:** none are requested at start. Location, RECORD_AUDIO, READ/WRITE_EXTERNAL_STORAGE are requested lazily through `PermissionsHelper.requestPermission`:
   - `DetailFragment.java:734` (location), `:1808` (audio), `:2157` (storage);
   - `SettingsFragment.java:150,162,174,510` (storage).
   - Baseline evidence: `PermissionsHelper.requestPermission` ran in APE, but `requestPermissionExecute` and its lambdas never ran in either run. Whenever a permission was checked it was already granted, so the baseline emulators had runtime permissions pre-granted (for example `adb install -g`; the mechanism is UNVERIFIED).

**Answer:** a new user does nothing before the main UI is usable: no intro (debug build), no login, account, vault or import, and no permission prompt.

### 2.2 Gates that keep parts of the app out of reach

| Gate | Code that enforces it | Effect |
|---|---|---|
| Debug build disables intro | `intro/IntroActivity.java:48-51`, `OmniNotes.java:55-57` | IntroActivity and slides are unreachable. "Show tour again" (`SettingsFragment.java:521-535`) only clears `pref_tour_complete` and exits the process. |
| Password not set | `DetailFragment.java:1684-1688` (lock opens PasswordActivity), `:1708-1713`; `PasswordActivity.java:92-126,155-197`; `BaseActivity.java:115-134` | Locked notes, the password dialog, password reset, removal and the access gate need pref `password` (MD5). Setting one needs 5 consistent fields (`PasswordActivity.checkData`, `:203-239`). Neither tool managed it: the Rx chain lambdas of `updatePassword` (`:168-195`) have 0 hits; all 14 `PasswordHelper` methods have 0 hits. |
| Dynamic drawer | `async/MainMenuTask.java:120-152` with `models/misc/DynamicNavigationLookupTable.java:53-72` | Archive, Reminders and Trash appear only when such notes exist (pref `settings_dynamic_menu`, default true). Uncategorized also needs `settings_show_uncategorized=true` (`:134-139`). |
| Categories exist | `async/CategoryMenuTask.java:120-142`; `widget/WidgetConfigurationActivity.java:107-110` | Category navigation, category edit (long-press), and widget category filter. |
| Tags exist (`#word` in a note) | `db/DbHelper.java:677-710`; `ListFragment.java:1560-1570,1801-1808`; `DetailFragment.java:2046-2054` | All tag dialogs and tag search show "no tags". `Tag.<init>` was never hit in either run. |
| Attachments of a given MIME | `DetailFragment.java:757-827` | Gallery needs image/sketch/video; playback needs audio; the long-press actions dialog needs any attachment. |
| Long-press | `ListFragment.java:507-516`; `CategoryMenuTask.java:144-157`; `DetailFragment.java:663-675,715-730,809-827`; `models/views/Fab.java:69-76` | Multi-select (CAB), category edit, reminder/location removal, attachment actions. Monkey hit **none** of the 6 long-click handlers (JaCoCo: `ListFragment.lambda$initListView$3`, `CategoryMenuTask.lambda$buildCategoryMenuLongClickEvent$2`, `DetailFragment.lambda$initViewReminder$4`, `lambda$initViewLocation$6`, `lambda$initViewAttachments$10`, `Fab.lambda$init$1` all have M=0). |
| External activities | `DetailFragment.java:1317-1358,2147-2154`; `SettingsFragment.java:240-255,413-439`; `MainActivity.java:509-510` | Camera, video capture, document picker, ringtone picker, share chooser, browser/maps. Under `monkey -p <pkg>` the ActivityController refuses starts of other packages and the caller gets RESULT_CANCELED (FW-MEMORY; consistent with `DetailFragment.onActivityResult` running in both runs while `onActivityResultManageReceivedFiles`, `AttachmentTask` and every image attachment path never ran). |
| Outside the app window | widgets, shortcut, notification shade, boot, system settings | All widget, shortcut, boot, NotificationListener, DashClock and Pushbullet code has 0 hits. |
| Build config | `utils/GeocodeHelper.java:174-177` with `gradle.properties` `MAPS_API_KEY=` (empty); `MainActivity.java:107` (`UpdaterTask` commented out) | Places autocomplete never calls the network; the updater is dead. |
| Theme.NoDisplay activity | `SnoozeActivity` "postpone" branch (`SnoozeActivity.java:88-92,104-105,116-119`) does not `finish()` before `onResume` | FW-MEMORY: on API 23+ with targetSdk 28 this throws IllegalStateException "did not call finish() prior to onResume() completing". APE ran `SnoozeActivity.onCreate` and `postpone` but never `onReminderPicked` or `onRecurrenceReminderPicked`. Hazard candidate, UNVERIFIED. |

### 2.3 Screens the baseline never reached

Per-class JaCoCo data; sizes include inner classes and `_ViewBinding`.

| Window | methods | Monkey | APE | Likely blocking gate |
|---|---|---|---|---|
| SettingsActivity / SettingsFragment (8 screens) | 16 / 47 | 0 / 0 | 9 / 28 | Monkey: the Settings entry is a footer TextView at the bottom of the drawer (`CategoryMenuTask.java:124-133`, `res/layout/fragment_navigation_drawer.xml:77`). Monkey opened the drawer (`NavigationDrawerFragment$1.onDrawerOpened` M=1) and tapped nav items (`MainMenuTask.lambda$onPostExecute$0` M=1) but never the footer (random-event odds; UNVERIFIED). |
| StatsActivity, AboutActivity | 7, 6 | 0, 0 | 7, 6 | Only reachable through Settings. |
| ListFragment CAB (ModeCallback) | 6 | 0 | 6 | No long-press in Monkey. |
| CategoryActivity | 20 | 0 | 14 | Needs categorize dialog "Add category" or drawer long-press. Monkey never ran `DetailFragment.categorizeNote`. |
| SketchFragment + SketchView | 50 | 0 | 38 | Needs the attachment popup (`DetailFragment.showAttachmentsPopup` M=0). APE never drew: `SketchView.onTouch` A=0. SketchView is not marked clickable, and APE targets clickable widgets (FW-MEMORY). |
| GalleryActivity | 19 | 0 | 0 | Needs an image, sketch or video attachment. Camera and picker results are blocked by `-p`; no sketch was ever drawn. |
| PasswordActivity | 24 | 11 | 11 | Reached via the editor "Lock" item; password never set. |
| Password dialog (PasswordHelper) | 14 | 0 | 0 | Needs a password. |
| SnoozeActivity | 10 | 0 | 4 | Only APE's list "Add reminder" (postpone). Notification actions are outside the app. |
| AlarmReceiver | 7 | 0 | 7 | APE set a near-future reminder that fired. |
| Intro (activity + fragment + 6 slides) | 22 | 1 | 1 | Debug build (`mustRun` false). |
| ShortcutActivity, WidgetConfigurationActivity, widgets | 2, 4, 23 | 0 | 0 | Launcher / home screen. |
| BootCompleteReceiver + AlarmRestoreOnRebootService | 5 | 0 | 0 | Reboot. |
| NotificationListener | 7 | 0 | 1 (`isRunning`, static) | Notification access never granted; the preference that opened the system screen is removed (`SettingsFragment.java:456-459`). |
| DataBackupIntentService + BackupHelper | 32 | 0 | 10 | APE exported a backup; it opened the import list but never confirmed a restore (`SettingsFragment.lambda$null$28` A=0). |
| SpringImportHelper | 4 | 0 | 0 | Needs a Springpad export zip. No fixture qualifies (`_fixtures/Download/archive.zip` holds a.txt, b.txt, sub/c.txt). |
| DashClock + Pushbullet | 11 | 0 | 0 | Host apps not installed. |

Other observations:
- **Monkey run started with an existing database (INFERRED):** `DbHelper.onCreate` and `SqlParser.*` ran in APE but not in Monkey, although Monkey used the DB heavily. The harness should state the starting state explicitly.
- **Monkey tapped collapsed FAB mini-buttons (UNVERIFIED library behaviour):** `Fab$2.onClick` and `ListFragment.lambda$initFab$0` ran (M=1, giving FAB camera → `DetailFragment.takePhoto` M=1), yet the main "+" button lambda `Fab.lambda$init$0` and `Fab.performToggle` never ran in Monkey.

### 2.4 What a harness must prepare to reach the rest

Recommendations, not executed. Package `it.feio.android.omninotes`, prefs file `it.feio.android.omninotes_preferences.xml` (`utils/Constants.java` (play):24), DB name `omni-notes` (`ConstantsBase.java:21`).

1. **Seed data.** The debug APK should allow `run-as` (FW-MEMORY: the debug buildType is debuggable). Alternatively import a prepared backup through the UI.
   - Backup format: folder `/sdcard/Omni Notes/<name>/` (`StorageHelper.java:287-304`) containing one `<13-digit>.json` file per note (`BackupHelper.java:145-151`), an attachments sub-folder named like the app's external files dir, and optionally the prefs XML (`BackupHelper.java:198-200,265-277`). Import path: Settings → Data → Sync → Import (`SettingsFragment.java:539-622`).
   - Notes to include, each covering one gate:
     - plain text containing a URL, an e-mail and `#tags`;
     - a checklist with checked and unchecked items (`DbHelper.getNotesByUncompleteChecklist`, `:761-764`);
     - an archived note; a trashed note;
     - a future and a past reminder, plus a recurrence rule;
     - a note with latitude, longitude and address;
     - attachments of every MIME: `image/jpeg`, `video/mp4`, `audio/amr`, `image/png` (sketch), `file/*` (`ConstantsBase.java:106-110`);
     - at least 2 categories; at least 1 locked note (needs a password);
     - enough notes to scroll (`AbsListViewScrollDetector` and FAB hide/show never ran).
2. **Preferences.**
   - `password` = md5(pw), `password_question`, `password_answer` = md5(ans) (`PasswordActivity.java:172-176`, `ConstantsBase.java:82-84`).
   - `settings_password_access=true` only for a dedicated run, because it gates app launch.
   - `settings_show_uncategorized=true`; `settings_dynamic_menu=false` (always shows Archive/Reminders/Trash); `settings_fab_expansion_behavior`, `settings_instant_search`, `settings_swipe_to_trash`, `settings_attachments_on_bottom`, `settings_auto_location` to flip modes.
   - `settings_language=ja_JP` or `zh_CN` for `IdeogramsWordCounter` (`helpers/count/CountFactory.java:28-44`).
3. **Files.** Push `_fixtures/Pictures` (6 jpg; `MANIFEST.csv` says "push fixtures/Pictures") and `Download/*` so the document picker has content. Prepare one backup folder and one legacy folder containing a file named `omni-notes` for "Import legacy" (`BackupHelper.java:308-315`). No Springpad zip exists in the fixtures.
4. **External activities.** A tool must be allowed to drive camera, DocumentsUI, the ringtone picker, ChooserActivity and the browser/maps, or those `RESULT` edges stay untested.
5. **Environment.**
   - Location fix (`adb emu geo fix`) and network for the Geocoder.
   - A reminder due within a minute, then use of the notification shade (tap / Snooze / Add reminder).
   - Simple and List widgets placed on the launcher, list widget configured, a widget resized.
   - The "Add note" launcher shortcut added (CREATE_SHORTCUT).
   - A BOOT_COMPLETED broadcast (needs root/reboot).
   - Notification access granted to `.services.NotificationListener`.
   - Intents via `adb shell am start -n it.feio.android.omninotes/.MainActivity`:
     - SEND / SEND_MULTIPLE with `android.intent.extra.TEXT` / `SUBJECT` / `STREAM`;
     - VIEW `hashtag://work` with category BROWSABLE;
     - the custom actions in section 1, with extras `note_id`, `note`, `widget_id` (`ConstantsBase.java:48-55`).
   - DashClock/Pushbullet code stays unreachable unless those apps are installed.

---

## 3. Screens and navigation

### 3.1 Window inventory

**Activities (12):** MainActivity, GalleryActivity, CategoryActivity, SettingsActivity, PasswordActivity, AboutActivity, IntroActivity, SnoozeActivity, ShortcutActivity (no UI, finishes in onCreate, `ShortcutActivity.java:30-45`), StatsActivity, NoteInfosActivity, WidgetConfigurationActivity.

**Fragments:**
- in MainActivity: `ListFragment`, `DetailFragment`, `SketchFragment` (all in `R.id.fragment_container`), `NavigationDrawerFragment` (static, `activity_main.xml:54-61`);
- `SettingsFragment` (one instance per preference XML);
- `IntroFragment` + `IntroSlide1..6` (AppIntro2 pager);
- `SublimePickerFragment` (DialogFragment, `utils/date/SublimePickerFragment.java:36`).

**Library dialog fragments:** `ColorChooserDialog` (`CategoryActivity.java:93-100`), `FolderChooserDialog` (`SettingsFragment.java:174-179`, callback `SettingsActivity.onFolderSelection`).

**MaterialDialogs (app callbacks):**
- List: empty trash `ListFragment.java:1018-1043`; delete notes `:1352-1364`; categorize `:1473-1497`; tag notes `:1560-1583`; filter by tags `:1801-1835`.
- Editor: link `DetailFragment.java:273-322`; remove reminder `:663-675`; remove location `:715-730`; attachment actions `:819-825`; delete all attachments `:853-859`; remove checklist `:1169-1191`; categorize `:1242-1277`; attachment popup `:1279-1315`; discard `:1471-1497`; delete note `:1535-1545`; tags `:2046-2072`; location search `:2210-2254`.
- Sketch: erase `SketchFragment.java:160-165`.
- Category: delete `CategoryActivity.java:162-188`.
- Settings: legacy import confirm `SettingsActivity.java:98-112`; import list, restore confirm, delete confirm `SettingsFragment.java:539-622`; export `:625-669`; changelog `:469-472`; reset `:487-499`; tour `:524-532`.
- Password: remove `PasswordActivity.java:161-164`; request `PasswordHelper.java:49-102`; reset `:105-139`.
- androidx preference dialogs: ListPreference `settings_language`, `settings_colors_app`, `settings_checked_items_behavior`; EditTextPreference `settings_max_video_size`, `settings_notification_snooze_delay`.

**Popups:** `PopupWindow` for sketch stroke and eraser (`SketchFragment.java:231-287`); overflow menus; the sort submenu (`ListFragment.java:587-602`, `res/menu/menu_list.xml:139-147`).

**Action mode:** `ListFragment.ModeCallback` started by `startSupportActionMode` (`ListFragment.java:401-465,512`), overlaying the toolbar (`styles.xml:27`).

**Preference screens (8):** `res/xml/settings.xml` (root), `settings_data.xml`, `settings_sync_import_export.xml`, `settings_interface.xml`, `settings_navigation.xml`, `settings_behaviors.xml`, `settings_notifications.xml`, `settings_privacy.xml`.

**Drawer:** `DrawerLayout` with nav list (`drawer_nav_list`), category list (`drawer_tag_list`) and Settings footer (`res/layout/fragment_navigation_drawer.xml:66-80`).

**Pager:** `GalleryViewPager` (`GalleryActivity.java:149-183`); AppIntro2 (intro).

**Others:**
- Snackbar with an "OK" action (permission rationale, `helpers/PermissionsHelper.java:42-45`); Crouton/Toast messages carry no handlers except the Crouton `onRemoved` → `onBackPressed` in `PasswordActivity.java:138-150,181-192`.
- Notifications: reminder with Snooze and Add-reminder actions (`AlarmReceiver.java:85-136`); backup progress and completion (`DataBackupIntentService.java:71-72,172-199`).
- Home-screen widgets.

**Not present:** context menus, PopupMenu, bottom sheets, tabs, the Navigation component, LiveData/ViewModel, data binding.

### 3.2 Navigation

- **Fragment back stack in MainActivity:**
  - ListFragment is added without a back stack entry (`MainActivity.java:178-181`).
  - `switchToDetail` replaces it with DetailFragment, back stack name "fragment_list"; if a detail is already shown it first does `popBackStackImmediate` (`MainActivity.java:439-459`).
  - `DetailFragment.takeSketch` replaces the detail with SketchFragment (`DetailFragment.java:1360-1384`).
  - An edge swipe in the detail replaces it with a new DetailFragment (`DetailFragment.java:1903-1953`; edges under 30 px, move over 100 px, `ConstantsBase.java:33-34`).
  - `switchToList` (hashtag VIEW) replaces with a new ListFragment on the back stack (`MainActivity.java:425-437`).
- **Back** (`MainActivity.onBackPressed`, `:255-298`):
  - from Sketch: `SketchFragment.save()` then popBackStack;
  - from Detail: `saveAndExit` → `SaveNoteTask` → `onNoteSaved` → `goHome` (popBackStack, or `finish()` when started by widget, shortcut, share or notification: `afterSavedReturnsToList=false`, `DetailFragment.java:513-585,1040-1071`);
  - from List: opens or closes the drawer depending on `settings_navdrawer_on_exit`, collapses the FAB, or exits and resets `isPasswordAccepted`.
- **Toolbar navigation icon:**
  - List: ActionBarDrawerToggle (`NavigationDrawerFragment.java:172-196`).
  - Detail: replaced by `navigateUp` (`DetailFragment.java:366`).
  - Sketch: `onBackPressed` (`SketchFragment.java:107`).
  - The `android.R.id.home` case in `ListFragment.performAction` (`:806-812`) is therefore probably never dispatched, because the toggle owns toolbar clicks (FW-MEMORY).
- **Drawer:**
  - A nav item tap → `BaseActivity.updateNavigation` writes pref `navigation` → `NavigationUpdatedEvent` → drawer closes → after 400 ms `NavigationUpdatedNavDrawerClosedEvent` → `ListFragment.initNotesList` (`MainMenuTask.java:73-84`, `NavigationDrawerFragment.java:143-156`, `ListFragment.java:1155-1160`).
  - Category tap: the same path (`CategoryMenuTask.java:159-173`). Category long-press → `MainActivity.editTag` → `CategoryActivity` (for result).
  - Settings footer → `SettingsActivity`.
- **Intents between activities:**
  - List → CategoryActivity (for result codes 1 and 2), List → SnoozeActivity (for result 3, with NEW_TASK, so RESULT_CANCELED comes back at once; FW-MEMORY).
  - Detail → Gallery, NoteInfos, CategoryActivity (5), PasswordActivity (3), external camera (1, 2), document picker (7).
  - Settings → PasswordActivity (no result), Stats, About, ringtone picker (100), Springpad picker (0), browser (beta/manual links `settings.xml:68-91`).
  - Results: `ListFragment.onActivityResult` (`:955-993`), `DetailFragment.onActivityResult` (`:1408-1451`), `SettingsFragment.onActivityResult` (`:680-703`).
- **Search:** expanding the SearchView with search item visible (`ListFragment.java:669-736`). On submit, `onQueryTextSubmit` returns the `settings_instant_search` value; when false, SearchView sends ACTION_SEARCH to MainActivity (singleTop → `onNewIntent` then `onResume`, FW-MEMORY) → `ListFragment.onResume` → `initNotesList` (`:390-398`). Instant search reloads on each keystroke (`:719-731`).
- **Process exits:** `SystemHelper.restartApp` only calls `System.exit(0)` (`utils/SystemHelper.java:34-44`). Callers: language change, reset data, tour again (`SettingsFragment.java:356,498,531`) and `action_restart_app` (`MainActivity.java:352-354`). These lead to S_EXIT; the system then relaunches the task's remaining activity in a new process (FW-MEMORY).

### 3.3 Modes that change active handlers

- **ListFragment.**
  - Navigation (`utils/Navigation.java:49-67`, pref `navigation`) changes the menu (`setActionItemsVisibility`, `ListFragment.java:739-776`), whether the FAB is allowed (`:1848-1863`), the swipe action (`:1176-1223`: TRASH → restore; CATEGORY → remove category; ARCHIVE or swipe-to-trash → trash; otherwise archive; UNCATEGORIZED or swipe disabled → no swipe), the CAB menu (`:611-648`) and archive behaviour (`:1406-1414`).
  - Empty vs non-empty (`:1227-1229`).
  - SearchView focused (`:686`; shows uncompleted-checklists and tags filters).
  - Search label active (`:1124-1152`).
  - Action mode with 1 vs many selected (`:623-638`), in Trash or not.
  - FAB expanded (`models/views/Fab.java:113-125`), with the click/long-click roles swapped by `settings_fab_expansion_behavior` (`Fab.java:62-76`).
  - Undo pending (`ListFragment.java:1301-1307,1688-1718`).
  - Drawer open (hides search, filters and sort, `:741-772`).
- **DetailFragment.**
  - New (`_id == null`), archived or trashed changes the menu (`DetailFragment.java:1011-1037`).
  - Checklist vs text (`:1021-1022,887-902,1152-1237`).
  - Locked and not yet checked: password dialog before the views are built (`:461-498`).
  - Has attachments (grid handlers `:757-827`); audio playing (`:1739-1758`); recording (`:2277-2288,2319-2321`); location shown (`:689-730`); reminder set (`:656-683`).
  - Options-item debounce of 1 s (`BaseFragment.java:43-49`).
- **Duplicate menus (INFERRED from code):** `BaseActivity.onCreateOptionsMenu` inflates `menu_list` into MainActivity's menu (`BaseActivity.java:64-69`) in addition to the fragment's menu (`ListFragment.java:579-584` inflates `menu_list` again; `DetailFragment.java:1005-1008` inflates `menu_detail`).
  - So every list id exists twice, and `menu_category`, `menu_share`, `menu_archive`, `menu_unarchive`, `menu_trash`, `menu_untrash` exist in both menus while in the detail. `menu_delete` is only in `menu_list`.
  - `findItem` returns the first match, but dispatch is by id, so the handlers do not change.
- **Hidden menu items:** `menu_add_shortcut` is never made visible (`res/menu/menu_detail.xml:73-78`; the line that showed it is commented out at `DetailFragment.java:1032`). `menu_synchronize` has no handler (`menu_list.xml:160-165`, `ListFragment.java:881-883` commented).
- **CategoryActivity:** delete button visible only when editing an existing category (`CategoryActivity.java:128`).
- **PasswordActivity:** password set vs not changes whether Confirm and Remove first ask for the current password (`PasswordActivity.java:91-126`).
- **SettingsFragment:** the XML comes from the `xmlName` argument (`SettingsFragment.java:93-101`). `settings_password_access` is enabled only when a password exists (`:330-346`).
- **WidgetConfigurationActivity:** radio group and spinner hidden when there are no categories (`widget/WidgetConfigurationActivity.java:107-110`).

### 3.4 Candidate page list (97 pages)

The "Base" column shows which baseline run reached the page (M, A, both, or "—" for neither), inferred from method hits. Variants follow `GRAPH_PROMPT.md` section 3 Step 1.

| Page | Description (window, mode) | Mode predicate / guard | Area | Base |
|---|---|---|---|---|
| S_ENTRY | outside the app (launcher, other apps, adb) | — | A | — |
| S_EXIT | process finished or `System.exit` | — | A | — |
| S_MAIN_PAUSED | MainActivity paused or stopped under another activity or Home | — | A | M A |
| S_LIST_NOTES_EMPTY | ListFragment, navigation Notes, no notes; empty view tap → jingles | `notes.size()==0` | A | M A |
| S_LIST_NOTES | ListFragment, Notes, rows; menu search/sort/view; FAB; swipe → archive (or trash) | `navigation==NOTES`, no action mode | A | M A |
| S_LIST_ARCHIVE | Archive navigation; no FAB; swipe → trash | `ARCHIVE` | A | A |
| S_LIST_REMINDERS | Reminders; filter-past toggle; no sort; no FAB | `REMINDERS` | A | — |
| S_LIST_TRASH | Trash; "Empty trash"; swipe → restore; no FAB | `TRASH` | A | M |
| S_LIST_UNCATEGORIZED | Uncategorized; swipe disabled | `UNCATEGORIZED` (needs pref) | A | A |
| S_LIST_CATEGORY | a category; filter-archived toggle; swipe → remove category | `CATEGORY` | A | A |
| S_LIST_SEARCH_EDIT | SearchView expanded with focus; uncompleted-checklist and tags icons | `searchViewHasFocus` | A | A |
| S_LIST_SEARCH_RESULT | results with search label bar and cancel (X) (query, tag, checklist, hashtag link) | `searchLabelActive` | A | A |
| S_LIST_FAB_OPEN | FAB menu expanded (note, camera, checklist) | `fab.isExpanded()` | A | A |
| S_LIST_SELECT_ONE | CAB, 1 selected: share, category, tags, reminder, (un)archive, trash, select all | actionMode, count==1, not Trash | A | A |
| S_LIST_SELECT_MANY | CAB, 2 or more: merge instead of share | count>1, not Trash | A | A? (UNVERIFIED) |
| S_LIST_SELECT_TRASH | CAB in Trash: untrash, delete, select all | actionMode, TRASH | A | — |
| S_LIST_UNDO | undo bar after archive, trash or uncategorize; any touch commits | `undoTrash\|\|undoArchive\|\|undoCategorize` | A | A |
| S_DRAWER | drawer open: nav items, categories (tap, long-press), Settings | `isDrawerOpen(START)` | A | M A |
| S_SORT_MENU | sort submenu (title, creation, modification, reminder) | — | A | A |
| S_DLG_EMPTY_TRASH | confirm empty trash | — | A | — |
| S_DLG_DELETE_NOTES | confirm permanent delete (CAB) | — | A | — |
| S_DLG_CATEGORIZE_LIST | category list + Add + Remove (CAB) | — | A | A |
| S_DLG_TAG_NOTES | multi-choice tags for selection | tags exist | A | — |
| S_DLG_FILTER_TAGS | multi-choice tags filter (from SearchView) | tags exist | A | — |
| S_CATEGORY_NEW | CategoryActivity new (delete invisible); variants @LIST_CAB (req 2), @DETAIL (req 5) | `category.getName()` empty | A | A |
| S_CATEGORY_EDIT | CategoryActivity edit existing (delete visible), from drawer long-press (req 1) | name not empty | A | A |
| S_DLG_COLOR_CHOOSER | ColorChooserDialog over CategoryActivity | — | A | A |
| S_DLG_DELETE_CATEGORY | confirm delete category | — | A | — |
| S_DETAIL_NEW | DetailFragment new note; archive and trash hidden; keyboard | `noteTmp.get_id()==null` | B | M A |
| S_DETAIL_EDIT | existing, not archived or trashed (text mode) | id set, `!archived`, `!trashed` | B | M A |
| S_DETAIL_ARCHIVED | existing archived note (unarchive) | `isArchived()` | B | UNVERIFIED |
| S_DETAIL_TRASHED | trashed note (untrash, delete) | `isTrashed()` | B | UNVERIFIED (delete: —) |
| S_DETAIL_CHECKLIST | detail in checklist mode (CheckListView items) | `noteTmp.isChecklist()` | B | M A |
| S_DLG_ATTACH | attachment popup (camera, video, files, recording, sketch, location, timestamp, pushbullet) | — | B | A |
| S_DLG_ATTACH_RECORDING | same popup while recording ("Stop"; not dismissed) | `isRecording` | B | A |
| S_DLG_CATEGORIZE_DETAIL | category list + Add + Remove (detail) | — | B | A |
| S_DLG_TAGS_DETAIL | tags multi-choice (detail) | tags exist | B | — |
| S_DLG_DISCARD | confirm discard changes | — | B | M A (confirm A) |
| S_DLG_DELETE_NOTE | confirm delete (trashed note) | — | B | — |
| S_DLG_REMOVE_CHECKLIST | keep-checked and keep-checkmarks options | checked items > 0 | B | — |
| S_DLG_ATTACHMENT_ACTIONS | long-press attachment: share, delete, delete all, edit (sketch) | attachments, no playback | B | — |
| S_DLG_DELETE_ALL_ATTACHMENTS | confirm | — | B | — |
| S_DLG_REMOVE_REMINDER | long-press reminder → confirm | — | B | A |
| S_DLG_REMOVE_LOCATION | long-press location → confirm | location shown | B | A (confirm —) |
| S_DLG_LOCATION | location search dialog (autocomplete, use current location) | location fix and network | B | A |
| S_DLG_LINK | link in title or content: open, copy | text has a link | B | — |
| S_REMINDER_PICKER | SublimePicker (date, time, recurrence); variants @DETAIL, @SNOOZE | — | B | M A |
| S_SKETCH | SketchFragment (stroke, eraser, undo, redo, erase, canvas) | — | B | A |
| S_SKETCH_STROKE_POPUP | stroke PopupWindow (seekbar, colour picker) | stroke mode already active | B | A |
| S_SKETCH_ERASER_POPUP | eraser PopupWindow (seekbar) | eraser mode already active | B | A? |
| S_DLG_ERASE_SKETCH | confirm erase | — | B | A |
| S_GALLERY | GalleryActivity pager (share, open externally, Up; tap on video opens viewer) | image, sketch or video attachment | B | — |
| S_GALLERY_PAUSED | Gallery under an external viewer or share | — | B | — |
| S_NOTE_INFO | NoteInfosActivity (dialog; read-only) | — | B | M A |
| S_EXT_CAMERA | external camera or video capture (RESULT codes 1, 2) | camera app allowed | B | M A (start only) |
| S_EXT_PICKER | external document picker; variants @FILES (detail, req 7), @SPRINGPAD (settings, req 0) | — | B | A (start only) |
| S_EXT_APP | other external app without result (chooser, browser, maps, viewer, Play, Facebook) | — | B | (blocked) |
| S_SETTINGS | root: sub-screens, beta, manual, tour, changelog, stats, about | `xmlName` null | C | A |
| S_SETTINGS_DATA | sync screen, password, password access, reset all data | `settings_data` | C | A |
| S_SETTINGS_SYNC | export, import, legacy import, Springpad | `settings_sync_import_export` | C | A |
| S_SETTINGS_INTERFACE | language, colours, FAB behaviour, attachments on bottom, dates | `settings_interface` | C | A |
| S_SETTINGS_NAVIGATION | dynamic menu, category count, uncategorized, drawer on exit | `settings_navigation` | C | A |
| S_SETTINGS_BEHAVIORS | checked items, instant search, swipe, swipe to trash, auto location, max video | `settings_behaviors` | C | A |
| S_SETTINGS_NOTIFICATIONS | vibration, ringtone, snooze delay | `settings_notifications` | C | A |
| S_SETTINGS_PRIVACY | ACRA, analytics, file logging | `settings_privacy` | C | A |
| S_SETTINGS_PAUSED | SettingsActivity under Password, Stats, About or a picker | — | C | A |
| S_DLG_EXPORT | backup name dialog | — | C | A |
| S_DLG_IMPORT | backup list (tap → restore; long-press → delete) | backups exist | C | A |
| S_DLG_IMPORT_CONFIRM | confirm restore | — | C | — |
| S_DLG_BACKUP_DELETE | confirm backup deletion | — | C | — |
| S_DLG_FOLDER_CHOOSER | FolderChooserDialog (legacy import) | — | C | — |
| S_DLG_LEGACY_IMPORT_CONFIRM | confirm legacy import | — | C | — |
| S_DLG_RESET_DATA | confirm reset (→ S_EXIT) | — | C | A (confirm —) |
| S_DLG_CHANGELOG | changelog dialog | — | C | — |
| S_DLG_TOUR_AGAIN | confirm show tour (→ S_EXIT; intro still off) | — | C | A (confirm —) |
| S_DLG_LANGUAGE | ListPreference language (→ S_EXIT on change) | — | C | — (change) |
| S_DLG_COLORS_APP | ListPreference colours | — | C | A |
| S_DLG_CHECKED_ITEMS | ListPreference checked-item behaviour | — | C | A |
| S_DLG_MAX_VIDEO_SIZE | EditTextPreference | — | C | — (change) |
| S_DLG_SNOOZE_DELAY | EditTextPreference | — | C | A |
| S_EXT_RINGTONE | system ringtone picker (RESULT 100) | — | C | A (start only) |
| S_PASSWORD_UNSET | PasswordActivity, no password stored; variants @SETTINGS, @DETAIL (result 3) | `prefs.password == null` | C | M A |
| S_PASSWORD_SET | PasswordActivity, password stored | `!= null` | C | — |
| S_DLG_REMOVE_PASSWORD | "unlock all notes" confirm | — | C | — |
| S_DLG_PASSWORD | PasswordHelper request dialog; variants @APP_ACCESS, @OPEN_NOTE, @CAB, @SWIPE, @EMPTY_TRASH, @DELETE_NOTES, @DETAIL_OPEN, @DETAIL_LOCK, @PWD_CONFIRM, @PWD_REMOVE, @PWD_ACCESS | password set | C | — |
| S_DLG_PASSWORD_RESET | security-question dialog | password set | C | — |
| S_STATS | StatsActivity (dialog; async load) | — | C | A |
| S_ABOUT | AboutActivity (WebView `about.html`, Up) | — | C | A |
| S_INTRO | IntroActivity pager (unreachable in this build; keep only for verdicts) | `mustRun()` | C | — |
| S_NOTIF_REMINDER | notification shade with a reminder (tap, Snooze, Add reminder) | alarm fired | D | A (posted only) |
| S_NOTIF_BACKUP | shade with a backup or import notification | — | D | A (posted only) |
| S_HOME_WIDGET_SIMPLE | home screen with simple widget (add, list, camera) | widget placed | D | — |
| S_HOME_WIDGET_LIST | home screen with list widget (rows + buttons) | widget placed | D | — |
| S_WIDGET_CONFIG | WidgetConfigurationActivity (radio, spinner, checkboxes, OK) | — | D | — |
| S_HOME_SHORTCUT | home screen with the "Add note" shortcut | shortcut added | D | — |
| S_PERMISSION_RATIONALE | Snackbar rationale (OK) | permission previously denied | D | — |
| S_SYS_PERMISSION | system runtime-permission dialog | permission not granted | D | — |

### 3.5 Shared windows and how to model them

- **S_DLG_PASSWORD (owned by C).** Each caller's PasswordValidator lambda lives in the caller's class:
  - `MainActivity.lambda$checkPassword$0`;
  - `ListFragment.lambda$editNote$7`, `$ModeCallback.lambda$onActionItemClicked$0`, `lambda$null$9` (swipe), `ListFragment$3.lambda$onClick$0`, `lambda$null$11`;
  - `DetailFragment.lambda$checkNoteLock$1`, `lambda$lockNote$20`;
  - `PasswordActivity.lambda$null$0`, `lambda$null$2`;
  - `SettingsFragment.lambda$null$11`.
  Use one page variant per caller.
- **S_REMINDER_PICKER (owned by B).** D adds the @SNOOZE edges. The callback object (`ReminderPickers$1`) forwards to `DetailFragment.onReminderPicked` or `SnoozeActivity.onReminderPicked` (`utils/date/ReminderPickers.java:53-69`).
- **Exact lambda names and lines** come from the JaCoCo `<method name=... line=...>` attributes; use them for node names.

---

## 4. Framework mechanisms needing framework, async or lifecycle edges

- **EventBus (greenrobot 2.4).** Handler naming decides the thread (FW-MEMORY): `onEvent` runs on the posting thread, `onEventMainThread` on main, `onEventAsync` on a background thread. Priority 1 registration: `ListFragment.java:210`, `PasswordActivity.java:72`. Subscribers:
  - `NavigationDrawerFragment`: DynamicNavigationReady, CategoriesUpdated, NotesUpdated (async), NotesLoaded, SwitchFragment, NavigationUpdated (`NavigationDrawerFragment.java:101-156`).
  - `ListFragment`: NavigationUpdatedNavDrawerClosed, CategoriesUpdated, NotesLoaded, PasswordRemoved, NotesMerge (async) (`ListFragment.java:1155-1246,1745`).
  - `MainActivity` and `PasswordActivity`: PasswordRemoved (`MainActivity.java:159`, `PasswordActivity.java:130`).
  - `DetailFragment`: PushbulletReply (`DetailFragment.java:2162`).
  - `DynamicNavigationLookupTable.onEventAsync(NotesUpdated)` (`:75`); `UpdateWidgetsTask$WidgetUpdateSubscriber.onEvent(NotesUpdated)` (`UpdateWidgetsTask.java:46`); `NotificationListener.onEventAsync(NotificationRemoved)` (`:60`).
  - Posts are listed with `grep EventBus.getDefault().post`, for example `NoteLoaderTask.java:87`, `NoteProcessor.java:67`, `DetailFragment.java:334,1065,1615`, `PasswordHelper.java:158`, `DynamicNavigationLookupTable.java:69`.
  - Registration windows matter (`needs_state`): MainActivity registers in `onCreate` but unregisters in `onStop` (`MainActivity.java:98,124`), so after its first stop it misses PasswordRemovedEvent. DetailFragment is registered only while resumed (`:347,421`).
- **AsyncTask:**
  - `NoteLoaderTask` is a singleton (`getInstance` reuses a PENDING task or cancels a RUNNING one, `NoteLoaderTask.java:40-52`). It calls `DbHelper` **by reflection** with the method-name strings `getAllNotes`, `getNotesByPattern`, `getNotesByTag`, `getNotesByUncompleteChecklist`, `getNotesByCategory` (`:58-79`; call sites `ListFragment.java:725,1078,1084,1091,1111,1114,1118`).
  - `NoteProcessor$NotesProcessorTask` with subclasses Archive, Categorize, Delete, Trash (`async/notes/*.java`); `SaveNoteTask`; `MainMenuTask`; `CategoryMenuTask` (runs `runOnUiThread` from `doInBackground`, `CategoryMenuTask.java:129-139`); `TextWorkerTask` (per list row); `UpdateWidgetsTask`; `AttachmentTask`; `StatsActivity$1StatsTask`; `UpdaterTask` (dead).
- **RxJava 1:**
  - `PasswordActivity.updatePassword` (`:168-195`) and `PasswordHelper.removePassword` (`:142-161`): newThread then main thread.
  - `DetailFragment.categorizeNote` and `DbHelper.getNotesByTag`: blocking.
  - `GeocodeHelper.getLocation`: SmartLocation observable with a 2 s timeout (`GeocodeHelper.java:86-110`).
  - `PermissionsHelper`: RxPermissions (`:56-68`).
- **Handler posts:**
  - `NavigationDrawerFragment.java:153` (400 ms); `ListFragment.java:1262` (150 ms), `1748`.
  - `DetailFragment.java:317`; `PasswordHelper.java:101,138`; `ReminderHelper.java:88`; `MainActivity.java:226` (dead method).
- **AlarmManager:** `ReminderHelper.addReminder` → `setExact(RTC_WAKEUP)` → `AlarmReceiver.onReceive` (`ReminderHelper.java:50-58`, `AlarmReceiver.java:53-65`). Callers: `SaveNoteTask.java:58-65`, `NoteProcessorTrash.java:41-46`, `SnoozeActivity.java:71-78`, `DataBackupIntentService.java:205-210`, `AlarmRestoreOnRebootService.java:56-60`, `DetailFragment.java:1530`.
- **Services:**
  - `DataBackupIntentService` (export, import, legacy, Springpad, delete; `:67-84`).
  - `AlarmRestoreOnRebootService` (JobIntentService, `enqueueWork` on O+).
  - `ListWidgetService` (bound by the launcher).
  - `NotificationListener` (bound by the system).
  - DashClock/Pushbullet extensions (bound by host apps).
  - No foreground service.
- **Broadcasts:**
  - Receivers: AlarmReceiver, BootCompleteReceiver, widget providers (APPWIDGET_UPDATE, options-changed), `ONDashClockExtension$DashClockUpdateReceiver` (LocalBroadcastManager, registered in `onInitialize`, `:51-60`; sent by `BaseActivity.notifyAppWidgets`, `BaseActivity.java:171`).
  - Sent: launcher INSTALL/UNINSTALL_SHORTCUT broadcasts (`ShortcutHelper.java:62-64,100-101`).
- **Widgets:** `WidgetProvider.onUpdate/onAppWidgetOptionsChanged` → `setLayout` → `getRemoteViews` (`WidgetProvider.java:49-111`). `ListWidgetService.onGetViewFactory` → `ListRemoteViewsFactory` (onCreate, onDataSetChanged, getViewAt, …), called by the widget host (FW-MEMORY). Data refresh comes from `BaseActivity.notifyAppWidgets` → `notifyAppWidgetViewDataChanged` (`BaseActivity.java:163-172`). Configuration: `WidgetConfigurationActivity` → `ListRemoteViewsFactory.updateConfiguration` (`:95-96`).
- **Database:** `DbHelper` is a `SQLiteOpenHelper` singleton, version 560 (`DbHelper.java:73,129-148`).
  - `onCreate` runs `create.sql`.
  - `onUpgrade` runs `UpgradeProcessor.process`, which **reflectively** invokes `onUpgradeTo476/480/482/501` (`UpgradeProcessor.java:68-95`), then `upgrade-*.sql` via `AssetUtils.list` (`DbHelper.java:191-214`). It only fires with an older DB on disk.
  - Notes are encrypted with `Security.encrypt` when locked (`DbHelper.java:220-222`).
- **SharedPreferences:** `MainActivity.onSharedPreferenceChanged` sets `prefsChanged`, which makes `ListFragment.onResume` re-run `init()` (`MainActivity.java:538-540`, `ListFragment.java:392-394`). Preference change listeners only fire when the value changes (FW-MEMORY).
- **Adapters:**
  - `NoteAdapter` (ArrayAdapter on listviewanimations `DynamicListView` with swipe-to-dismiss, `ListFragment.java:1171-1224`; `NoteAdapter.add(int,Object)` implements `Insertable` and is called by the library from `list.insert` at `ListFragment.java:1662`, FW-MEMORY/UNVERIFIED).
  - `NavDrawerAdapter`; `CategoryBaseAdapter` (drawer and widget spinner); `CategoryRecyclerViewAdapter` with `RecyclerViewItemClickSupport` (categorize dialogs); `AttachmentAdapter` (GridView with Glide); `PlacesAutoCompleteAdapter` (Filter on a worker thread); library `GalleryPagerAdapter`.
- **ButterKnife:** `X_ViewBinding.<init>(X, View)` is invoked reflectively from `ButterKnife.bind` at `MainActivity.java:97`, `ListFragment.java:233`, `DetailFragment.java:353` and others; `@OnClick` in `CategoryActivity.java:93,135,162` is dispatched through `CategoryActivity_ViewBinding$1..$3.doClick`. JaCoCo: only the 2-arg constructors ever ran.
- **Other libraries with callbacks:**
  - ChecklistView (`ChecklistManager`, `DetailFragment.java:1204-1237`; callbacks `onCheckListChanged`, TextWatcher).
  - SublimePicker, MaterialDialogs (positive, negative, neutral, item and multi-choice callbacks, show and cancel listeners), Crouton `LifecycleCallback`.
  - SmartLocation + Geocoder.
  - `MediaRecorder` and `MediaPlayer.setOnCompletionListener` (`DetailFragment.java:1772-1856`).
  - `ActionBarDrawerToggle` `onDrawerOpened/Closed` (`NavigationDrawerFragment.java:172-187`).
  - SearchView expand/collapse and query listeners (`ListFragment$2`, `$2$1`).
  - `AnimatorListenerAdapter.onAnimationEnd` opens the note after the zoom animation (`ListFragment.java:561-568`).
- **Storage Access Framework and pickers:** `ACTION_GET_CONTENT` (`DetailFragment.java:2147-2154`, multiple, `*/*`; `SettingsFragment.java:240-255`, `application/zip`); `RingtoneManager.ACTION_RINGTONE_PICKER` (`:413-439`); camera `ACTION_IMAGE_CAPTURE` / `ACTION_VIDEO_CAPTURE` with FileProvider output (`DetailFragment.java:1317-1358`); share via `Intent.createChooser` (`MainActivity.java:462-511`).
- **Notifications:** `NotificationsHelper` with `NotificationChannels` (Backups, Reminders); reminder actions are PendingIntents to `SnoozeActivity` with ACTION_SNOOZE, ACTION_POSTPONE and `action_notification_click<timestamp>` (`AlarmReceiver.java:85-136`).
- **WebView:** `AboutActivity` loads `file:///android_asset/html/about.html` with no JS bridge (`AboutActivity.java:30-31`).
- **Other app infrastructure:** ACRA, LeakCanary (`BaseFragment.java:40`), analytics (`OmniNotes.getAnalyticsHelper`; empty params probably fall back to `MockAnalyticsHelper`, `OmniNotes.java:119-131`, UNVERIFIED).
- **Not used:** LiveData/ViewModel, WorkManager, data binding, content providers of the app's own.

---

## 5. Unreachable-code candidates (evidence only; not final verdicts)

Method: a bytecode scan of every compiled class (invoke* instructions plus invokedynamic bootstrap method handles), with class-hierarchy resolution, combined with source and resource grep and the JaCoCo hits. All methods below have **0 hits in both runs** unless stated.

### 5.1 No caller anywhere in the compiled code (DEAD candidates)

- **Updater, never instantiated:** `async/UpdaterTask` (12 methods incl. `$1`; the only start site is commented at `MainActivity.java:107`). Also dead through it: `models/misc/PlayStoreMetadataFetcherResult` (13), `AppVersionHelper.isAppUpdated/getAppVersionFromPreferences/updateAppVersionInPreferences/getCurrentAppVersion` (`helpers/AppVersionHelper.java:37-59`, callers only in UpdaterTask `:134,138`), `MiscUtils.isGooglePlayAvailable` (UpdaterTask `:112`).
- **Classes never instantiated and absent from layouts:** `models/views/VerticalSeekBar` (9; sketch popups use a plain `SeekBar`, `res/layout/popup_sketch_stroke.xml:47-48`), `models/holders/ImageAndTextItem` (5), `utils/LoadingDialog` (2), `models/PushBulletMessage` (1).
- **`GeocodeHelper` instance part:** `<init>` and `LocationListener` callbacks `onLocationChanged/onStatusChanged/onProviderEnabled/onProviderDisabled` (`utils/GeocodeHelper.java:56-83`); there is no `new GeocodeHelper`. `GeocodeHelper.getAddressFromCoordinates(Context,double,double)` (`:121-133`) is used only by androidTest.
- **Play-flavor code compiled in but unused:** `helpers/GeocodeProviderFactory.getProvider` (`src/play/.../GeocodeProviderFactory.java:30-32`); `GeocodeHelper` statically imports the *base* factory (`GeocodeHelper.java:21`). `GeocodeProviderBaseFactory.<init>` is also never called.
- **DbHelper:** `emptyTrash` (`:542-546`; the list's empty-trash uses `NoteProcessorDelete`), `getCategorizedCount` (`:936`), `getChecklists` (`:640`), `getMasked` (`:646`), `getNotesWithLocation` (`:382`), `getTodayReminders` (`:624`), `getDatabaseName` override (`:158`; FW-MEMORY: the framework uses its own field, not this getter).
- **Helpers and utils:**
  - `BaseActivity.getStringResourceByName` (`:153-157`); `MainActivity.getSearchMenuItem` (`:205-212`) → `ListFragment.getSearchMenuItem` (`:1838`); `MainActivity.initNotesList` + `lambda$initNotesList$1` (`:223-231`).
  - `BackupHelper.deleteNote(File)`, `deleteNoteBackup`, `exportAttachments(File)`, `importAttachments(File)`, `importAttachments(Note,File)`, `integrityCheck` + `addIntegrityCheckError` (`integrityCheck` is used by androidTest `AutoBackupTest` only).
  - `LanguageHelper.getLocalizedString` (`:83`, used by androidTest only); `DateHelper.getSortableDate/getTimeShort(x2)/onDateSet/onTimeSet` (static helpers, `helpers/date/DateHelper.java:37-65,82-100`); `RecurrenceHelper.nextReminderFromRecurrenceRule(long,long,String)` reachable only through the other overload. Some test-only uses are confirmed: `ReminderHelper.checkReminder` (`ReminderHelperTest`), `DateUtils.prettyTime` (`DateUtilsTest`).
  - `NavigationItem.setArrayIndex/setIcon/setIconSelected/setText`; `Stats.getUsageTime/setUsageTime`; `UndoBarController.isVisible/onSaveInstanceState/onRestoreInstanceState` (not a View; never called, `ListFragment.java:253-1712` only calls show and hide).
  - `NoteAdapter.colorNote(Note,View)`, `getNotes`; `AttachmentAdapter.getAttachmentsList`; `ExpandableHeightGridView.getItemHeight`; `Fab.setOverlay(x2)` + lambdas; `SketchView.getStrokeSize/getUndonePaths/setPaths/setUndonePaths`; `SquareImageView.getAsyncTask/setAsyncTask`; `AbsListViewScrollDetector.setListView/setScrollThreshold`; `RecyclerViewItemClickSupport.removeFrom` + `detach`.
  - `utils/Display` (7: `getActionbarHeight`, `getNavigationBarHeight`, `getNavigationBarHeightStandard`, `getRootView`, `getSoftButtonsBarHeight`, `getStatusBarHeight`, `getVisibleSize`, `orientationLandscape`); `ColorsUtil.getContrastedColor` (+ `calculateColorLuminance`); `IntentChecker.resolveActivityPackage`; `KeyboardUtils.hideKeyboard(MainActivity)`; `StorageHelper.getDbSyncDir/getRealPathFromURI/getStorageDir/copyDirectory/createNewAttachmentFile(Context)`; `SystemHelper.copyToClipboard`; `FileHelper.getFileExtension(File)/getFilePrefix(File)`; `DateUtils.getDateFromString/getLongFromDateTime/getString(long,String)/prettyTime(String)`; `NotificationsHelper.cancel(int)/setIcon`; `AssetUtils.exists`.
- **Implicit public constructors of static-only classes:** `TextHelper`, `StorageHelper`, `SystemHelper`, `TagsHelper`, `DateUtils`, `PasswordHelper`, `ResourcesUtils`, `NotesHelper`, `NotificationChannels`, `SqlParser`, `BuildConfig`. All are in JaCoCo with 0 hits.

### 5.2 Present but unreachable through UI or build configuration

- **Intro (22 methods):** debug build (section 2.1).
- **"Add shortcut":** menu item never visible (`menu_detail.xml:73-78`, `DetailFragment.java:1032`), so `DetailFragment.addShortcut` (`:1896-1899`) and `ShortcutHelper.addShortcut` (`:47-83`) are unreachable. On API 27 the latter would take the `ShortcutManager` branch (`:65-82`).
- **`SettingsFragment.lambda$onResume$16`:** listener for preference `settings_colors_widget`, which exists in no preference XML (grep of `res/xml`), so `findPreference` returns null (`SettingsFragment.java:396-410`).
- **`SettingsActivity.replaceFragment`:** called only when `backStack` is non-empty (`SettingsActivity.java:71-84`), and nothing ever adds to `backStack`.
- **Notification listener:** in-app access is removed (`SettingsFragment.java:456-459`); `NotificationListener` runs only after a manual system grant.
- **`GeocodeHelper.autocomplete`:** network part unreachable because `MAPS_API_KEY` is empty (`GeocodeHelper.java:175-177`, `gradle.properties`); `SystemHelper.closeCloseable` is then reached only from dead code.
- **Debug-only branches:** `ListFragment.animateListView` fade branch (`ListFragment.java:1249-1251`, never taken in debug); `OmniNotes.enableStrictMode` and LeakCanary run only in debug (`OmniNotes.java:96-97,104-110`, `BaseFragment.java:40`).
- **`MainActivity.init` drawer-creation branch** (`:172-176`): dead because the drawer fragment is static in `activity_main.xml:54-61`.
- **Home button cases with a toolbar listener:** `ListFragment.performAction` case `android.R.id.home` (`:806-812`) and `SketchFragment.onOptionsItemSelected` (`:198-205`) are probably never dispatched because the toolbar listener consumes the click (FW-MEMORY). `SettingsFragment.onOptionsItemSelected` (`:127-134`): no `setHasOptionsMenu(true)` in SettingsFragment, so it is never called (FW-MEMORY).
- **`DetailFragment.onConfigurationChanged`** (`:437-442`): MainActivity declares no `configChanges`, so fragments do not receive configuration callbacks (FW-MEMORY).
- **`DbHelper.onUpgrade` + `UpgradeProcessor` (7) + `AssetUtils.list`:** only with an older DB file (install an old DB, then upgrade).

### 5.3 Reached only by reflection or by the framework (not dead; model them explicitly)

- **Reflection:** `DbHelper.getAllNotes`, `getNotesByPattern`, `getNotesByTag(String)`, `getNotesByUncompleteChecklist`, `getNotesByCategory` (via `NoteLoaderTask`); `UpgradeProcessor.onUpgradeToNNN` (reflection on DB upgrade); `X_ViewBinding.<init>(X,View)` (ButterKnife).
- **EventBus `onEvent*` handlers** (section 4).
- **FRAMEWORK_ONLY candidates:**
  - 1-arg and 3-arg constructors of custom views (inflation uses the 2-arg one, FW-MEMORY; JaCoCo shows only the 2-arg constructors ran).
  - `_ViewBinding.<init>(Target)` (activities) and all `unbind()` methods (the app never calls `Unbinder.unbind`).
  - Parcelable `describeContents` and `CREATOR.newArray` for Note, Attachment, Category, Tag.
  - `CategoryActivity/SettingsActivity.onPointerCaptureChanged`.
  - `DetailFragment$4.onAnimationRepeat`, `AnimationsHelper$1.onAnimationRepeat`.
  - `Fab$3.onAnimationCancel` and `RecyclerViewItemClickSupport$3.onChildViewDetachedFromWindow` (possible but unlikely; UNVERIFIED).
  - `DetailFragment.lambda$initViewTitle$12` (title `OnDragListener`; needs a text drag-and-drop).
  - `ListRemoteViewsFactory.getLoadingView/getViewTypeCount/hasStableIds/getItemId` (widget host).
  - `WidgetProvider.onAppWidgetOptionsChanged` (needs a resize).

### 5.4 Environment-gated

| Gate | Code affected |
|---|---|
| Reboot | BootCompleteReceiver, AlarmRestoreOnRebootService (+ `DbHelper.getNotesWithReminderNotFired`) |
| Notification access | NotificationListener (+ `DbHelper.setReminderFired`) |
| Host apps | DashClock and Pushbullet extensions (+ `DetailFragment.onEventMainThread(PushbulletReplyEvent)`; the attachment-popup "pushbullet" item calls the library `MessagingExtension.mirrorMessage`) |
| Launcher | widgets, ShortcutActivity |
| Camera feature | `IntentChecker.isAvailable(..., FEATURE_CAMERA)` (`DetailFragment.java:1320,1339`; also oddly required for opening links, `:294-298`) |
| Microphone | `MediaRecorder` |
| Location fix and Geocoder (network) | location paths |
| CJK locale | `IdeogramsWordCounter` (4 methods, `CountFactory.java:33-44`) |
| API level | `AlarmRestoreOnRebootService.enqueueWork` (O+ branch), `ShortcutHelper.addShortcut` (<26 vs ≥26), `LanguageHelper.getCurrentLocale` (N+), `NotificationsHelper.initNotificationChannels` (>O), `DetailFragment.onActivityResultManageReceivedFiles` (>16, ClipData) |

---

## 6. Decomposition into 4 areas

Method counts are JaCoCo methods (the 1426 total excludes JacocoInstrument). Every compiled class except the 3 `JacocoInstrument` classes is assigned exactly once (70 + 47 + 29 + 88 = 234). Classes with no JaCoCo methods (interfaces, constant interfaces, and the switch-map classes `MainActivity$1`, `DetailFragment$5`) are listed with their area.

| Area | Owns (classes) | Methods | Pages owned | Entry edges from other areas |
|---|---|---|---|---|
| **A – Shell, notes list, drawer, categories** | 70 classes, listed below | 441 | S_ENTRY, S_EXIT, S_MAIN_PAUSED, S_LIST_* (14), S_DRAWER, S_SORT_MENU, S_DLG_EMPTY_TRASH, S_DLG_DELETE_NOTES, S_DLG_CATEGORIZE_LIST, S_DLG_TAG_NOTES, S_DLG_FILTER_TAGS, S_CATEGORY_NEW, S_CATEGORY_EDIT, S_DLG_COLOR_CHOOSER, S_DLG_DELETE_CATEGORY (28) | B→A: editor "Add category" → CategoryActivity (`DetailFragment.java:1259-1263`); back from the editor via `goHome` popBackStack (`:1058-1067`). D→A: widget, shortcut, notification, DashClock and backup notification → `MainActivity` intents (section 1). C→A: process exit and relaunch → MainActivity. |
| **B – Note editor and attachments** | 47 classes | 334 | S_DETAIL_* (5), editor dialogs (13), S_REMINDER_PICKER, S_SKETCH*, S_DLG_ERASE_SKETCH, S_GALLERY, S_GALLERY_PAUSED, S_NOTE_INFO, S_EXT_CAMERA, S_EXT_PICKER, S_EXT_APP (29) | A→B: `MainActivity.switchToDetail` (`:439-459`) from `ListFragment.editNote2` (`:928-950`), merge (`:1745-1766`), FAB camera (`:275-279` → `DetailFragment.java:557-559`), `handleIntents` (`MainActivity.java:358-371,385-388`); `MainActivity.onBackPressed` → `SketchFragment.save` and `DetailFragment.saveAndExit` (`:259-275`). D→B: `SnoozeActivity` → picker @SNOOZE. |
| **C – Settings, password and security, backup and import, stats, about, intro** | 29 classes | 218 | S_SETTINGS* (8), S_SETTINGS_PAUSED, settings dialogs (14), S_EXT_RINGTONE, S_PASSWORD_UNSET/SET, S_DLG_REMOVE_PASSWORD, S_DLG_PASSWORD (+ variants), S_DLG_PASSWORD_RESET, S_STATS, S_ABOUT, S_INTRO (32) | A→C: drawer Settings (`CategoryMenuTask.java:130-133`); `MainActivity.checkPassword` and `BaseActivity.requestPassword` → `PasswordHelper` (`MainActivity.java:138-156`, `BaseActivity.java:115-134`). B→C: `DetailFragment.lockNote` → PasswordActivity (`:1684-1687`) and `PasswordHelper` (`:477,1697`). |
| **D – Core data and platform + background and external** | 88 classes | 433 | S_NOTIF_REMINDER, S_NOTIF_BACKUP, S_HOME_WIDGET_SIMPLE, S_HOME_WIDGET_LIST, S_WIDGET_CONFIG, S_HOME_SHORTCUT, S_PERMISSION_RATIONALE, S_SYS_PERMISSION, plus picker variant @SNOOZE (8 pages + variant) | A→D: `ListFragment.addReminders` → SnoozeActivity (`:893-899`); everybody → `DbHelper`, models, utils (CALL). B→D: `SaveNoteTask` → `ReminderHelper` → AlarmManager → `AlarmReceiver`; `PermissionsHelper`. C→D: `DataBackupIntentService` → `NotificationsHelper`, `SystemHelper.restartApp`. |

**Shared infrastructure owner:** D owns the database layer (`DbHelper`, `SqlParser`), the data models (`Note`, `Attachment`, `Category`, `Tag`, `ONStyle`), all EventBus event classes, exceptions (except `BackupException`), and the generic utils and helpers. A owns the app start (`OmniNotes`, `BaseActivity`, `BaseFragment`, `BuildConfig`) and the list-side helpers (`NoteLoaderTask`, `NoteProcessor*`, `Navigation`, `TagsHelper`, `NotesHelper`, adapters). Callers create CALL edges into D; the D agent models what happens inside the callee and decides the verdicts.

**Class lists** (`{...}` = inner and ViewBinding classes of the same outer class):

- **A (70):** BaseActivity; BaseFragment; BuildConfig; OmniNotes; MainActivity{$1,_ViewBinding}; ListFragment{$1,$2,$2$1,$3,$ModeCallback,_ViewBinding}; NavigationDrawerFragment{$1}; CategoryActivity{_ViewBinding,_ViewBinding$1,$2,$3}; async/CategoryMenuTask; async/MainMenuTask{_ViewBinding}; async/TextWorkerTask; async/UpdateWidgetsTask{$WidgetUpdateSubscriber}; async/notes/NoteLoaderTask, NoteProcessor{$NotesProcessorTask}, NoteProcessorArchive, NoteProcessorCategorize, NoteProcessorDelete, NoteProcessorTrash; helpers/NotesHelper; models/NavigationItem; models/UndoBarController{$1,$2,$UndoListener}; models/adapters/CategoryBaseAdapter, CategoryRecyclerViewAdapter, NavDrawerAdapter, NoteAdapter, NoteDrawerAdapterViewHolder, category/CategoryViewHolder{_ViewBinding}; models/holders/NoteViewHolder{_ViewBinding}; models/listeners/AbsListViewScrollDetector, OnCABItemClickedListener, OnFabItemClickedListener, OnViewTouchedListener, RecyclerViewItemClickSupport{$1,$2,$3,$OnItemClickListener,$OnItemLongClickListener}; models/misc/DynamicNavigationLookupTable; models/views/Fab{$1,$2,$3}, InterceptorLinearLayout, NonScrollableListView; utils/AnimationsHelper{$1}; utils/Navigation; utils/TagsHelper.
- **B (47):** DetailFragment{$1,$2,$3,$4,$5,$AttachmentOnClickListener,$OnGeoUtilResultListenerImpl,$OnGeoUtilResultListenerImpl$1,_ViewBinding}; GalleryActivity{$1,$2,_ViewBinding}; NoteInfosActivity{_ViewBinding}; SketchFragment{$1,$2,_ViewBinding}; async/AttachmentTask; async/notes/SaveNoteTask; helpers/AttachmentsHelper, GeocodeProviderBaseFactory, GeocodeProviderFactory (play); models/StatsSingleNote; models/adapters/AttachmentAdapter{$AttachmentHolder}, PlacesAutoCompleteAdapter{$1}; models/listeners/OnAttachingFileListener, OnDrawChangedListener, OnGeoUtilResultListener, OnNoteSaved, OnReminderPickedListener; models/views/ExpandableHeightGridView, InterceptorFrameLayout, SketchView, SquareImageView, VerticalSeekBar; utils/GeocodeHelper{$1}; utils/date/ReminderPickers{$1}, SublimePickerFragment{$1,$Callback}.
- **C (29):** AboutActivity; PasswordActivity{$1,$2}; SettingsActivity{_ViewBinding}; SettingsFragment{$1}; StatsActivity{$1StatsTask}; async/DataBackupIntentService; exceptions/BackupException; helpers/AppVersionHelper, BackupHelper, SpringImportHelper; intro/IntroActivity, IntroFragment{_ViewBinding}, IntroSlide1..6; models/PasswordValidator{$Result}; models/Stats; utils/PasswordHelper; utils/Security.
- **D (88):** ShortcutActivity; SnoozeActivity; async/AlarmRestoreOnRebootService; async/UpdaterTask{$1}; async/upgrade/UpgradeProcessor; async/bus/* (13 event classes incl. SwitchFragmentEvent$Direction); db/DbHelper, SqlParser; exceptions/DatabaseException, GenericException, NotesLoadingException; extensions/ONDashClockExtension{$Counters,$DashClockUpdateReceiver}, PushBulletExtension; factory/MediaStoreFactory; helpers/LanguageHelper, LogDelegate, PermissionsHelper, count/CountFactory, DefaultWordCounter, IdeogramsWordCounter, WordCounter, date/DateHelper, date/RecurrenceHelper; models/Attachment{$1}, Category{$1}, Note{$1}, ONStyle, PushBulletMessage, Tag{$1}, holders/ImageAndTextItem, listeners/OnPermissionRequestedListener, misc/PlayStoreMetadataFetcherResult; receiver/AlarmReceiver, BootCompleteReceiver; services/NotificationListener; utils/AlphaManager, AssetUtils, BitmapHelper, ColorsUtil, ConnectionManager, Constants (play), ConstantsBase, Display, FileHelper, FileProviderHelper, IntentChecker, KeyboardUtils, LoadingDialog, MiscUtils, ParcelableUtil, ReminderHelper, ResourcesUtils{$ResourceIdentifiers}, ShortcutHelper, StorageHelper, SystemHelper, TextHelper, date/DateUtils, notifications/NotificationChannel, NotificationChannels{$1,$NotificationChannelNames}, NotificationsHelper; widget/ListRemoteViewsFactory, ListWidgetProvider, ListWidgetService, SimpleWidgetProvider, WidgetConfigurationActivity, WidgetProvider.
- **Leftovers (excluded):** `JacocoInstrument/FinishListener`, `JacocoInstrument/JacocoInstrumentation`, `JacocoInstrument/SMSInstrumentedReceiver` (coverage harness).

**Overlap rules for the parallel agents:**
1. Page variants of shared dialogs (S_DLG_PASSWORD@X, S_REMINDER_PICKER@X, S_CATEGORY_NEW@X, S_PASSWORD_UNSET@DETAIL, S_EXT_PICKER@SPRINGPAD) are created by the area that owns the **caller's** continuation.
2. `MainActivity.onBackPressed` and `switchToDetail` belong to A; B adds the `ENTERS` edges back to the S_LIST_* pages after `goHome`.
3. Agree on edge-id prefixes (A###, B###, …) and on the method-name convention (JaCoCo names, overloads as `Class.m(Type,Type)`).

---

## 7. Baseline coverage by area and screen

### 7.1 By area

| Area | methods | both | Monkey only | APE only | neither | Monkey total | APE total |
|---|---|---|---|---|---|---|---|
| A | 441 | 224 | 0 | 110 | 107 | 224 | 334 |
| B | 334 | 110 | 0 | 109 | 115 | 110 | 219 |
| C | 218 | 12 | 0 | 96 | 110 | 12 | 108 |
| D | 433 | 88 | 1 (`DbHelper.getNotesTrashed`) | 98 | 246 | 89 | 186 |
| **Total** | **1426** | 434 | 1 | 413 | 578 | **435** | **847** (either 848) |

The totals match the brief.

Largest never-hit sets (never-hit / class methods):
- A: ListFragment 24/94, TagsHelper 11/13, MainActivity 9/38, NoteAdapter 5/21, NotesHelper 5/8 (merge path), NoteProcessorDelete 4/4.
- B: DetailFragment 26/118, GeocodeHelper 9/15, VerticalSeekBar 9/9, GalleryActivity 9/9 (+7 in inner classes and ViewBinding), SketchView 8/23, AttachmentTask 5/5.
- C: SettingsFragment 16/43, BackupHelper 15/22, PasswordHelper 14/14, DataBackupIntentService 7/10, PasswordActivity 7/18, SpringImportHelper 4/4, intro 21/22.
- D: DbHelper 24/56, StorageHelper 19/31, ListRemoteViewsFactory 13/13, PlayStoreMetadataFetcherResult 13/13, FileHelper 10/10, UpdaterTask 10/10, Display 9/12, DateUtils 8/17, Tag 7/7, UpgradeProcessor 7/7, NotificationsHelper 7/23, NotificationListener 6/7, SnoozeActivity 6/10.

### 7.2 By screen (methods hit, Monkey / APE)

| Window | methods | M | A | Note |
|---|---|---|---|---|
| MainActivity | 41 | 29 | 30 | |
| ListFragment (+inner) | 113 | 46 | 85 | Monkey: no CAB, search, sort, undo or FAB toggle |
| Drawer + MainMenuTask + CategoryMenuTask | 46 | 41 | 44 | |
| DetailFragment (+inner) | 146 | 60 | 108 | |
| SketchFragment + SketchView | 50 | 0 | 38 | |
| GalleryActivity | 19 | 0 | 0 | |
| NoteInfosActivity | 8 | 6 | 6 | |
| CategoryActivity | 20 | 0 | 14 | |
| SettingsActivity / SettingsFragment | 16 / 47 | 0 / 0 | 9 / 28 | |
| PasswordActivity / PasswordHelper | 24 / 14 | 11 / 0 | 11 / 0 | |
| StatsActivity / AboutActivity | 7 / 6 | 0 / 0 | 7 / 6 | |
| Intro | 22 | 1 | 1 | |
| SnoozeActivity | 10 | 0 | 4 | |
| Shortcut, widget config, widgets | 2, 4, 23 | 0 | 0 | |
| AlarmReceiver / Boot + restore service / NotificationListener | 7 / 5 / 7 | 0 / 0 / 0 | 7 / 0 / 1 | |
| Backup service + BackupHelper / Springpad | 32 / 4 | 0 / 0 | 10 / 0 | |
| Extensions / UpdaterTask + metadata / UpgradeProcessor / Tag + TagsHelper | 11 / 25 / 7 / 23 | 0 / 0 / 0 / 2 | 0 / 0 / 0 / 2 | |

### 7.3 Pages never reached and the likely reason

- **Neither run:**
  - S_LIST_REMINDERS (the drawer item was never tapped; `DbHelper.getNotesWithReminder` 0 hits).
  - S_LIST_SELECT_TRASH, S_DLG_EMPTY_TRASH, S_DLG_DELETE_NOTES (APE never in Trash; Monkey never long-pressed).
  - All tag pages (no `#tag` in any note).
  - All password pages (password never set).
  - S_DLG_DELETE_CATEGORY; S_GALLERY; S_DLG_LINK (no links in note text).
  - S_DLG_ATTACHMENT_ACTIONS / S_DLG_DELETE_ALL_ATTACHMENTS (long-press on an attachment); S_DLG_REMOVE_CHECKLIST (needs checked items); S_DLG_DELETE_NOTE.
  - Results from S_EXT_* (blocked by `-p`).
  - S_DLG_IMPORT_CONFIRM, S_DLG_BACKUP_DELETE, S_DLG_FOLDER_CHOOSER, S_DLG_CHANGELOG; the confirm steps of reset and tour.
  - S_INTRO (debug build).
  - All D pages except notifications being posted (home screen, shade, boot and system settings are outside the package).
- **Monkey only missed:** everything in C; CAB and undo (no long-press); search, sort and FAB toggle; CategoryActivity; Sketch; the attachment popup; S_LIST_ARCHIVE, S_LIST_CATEGORY, S_LIST_UNCATEGORIZED. One page was reached by Monkey but not by APE: S_LIST_TRASH.

---

## Conclusions and recommendations

1. **Modeling order.** Start with A (app start → empty list → list modes → detail switch), then B and C in parallel, and D last (mostly CALL edges and verdicts).
2. **Edges that are easy to miss:**
   - The `NoteLoaderTask` reflection targets (CALL edges with evidence `SRC NoteLoaderTask.java:63/74` plus the call-site string).
   - EventBus delivery (FRAMEWORK edges) with the registration windows as `needs_state`.
   - The 400 ms drawer-close event chain.
   - The immediate RESULT_CANCELED to `ListFragment.onActivityResult` for "Add reminder" (FW-MEMORY).
   - `goHome` choosing `finish()` vs popBackStack depending on how the detail was opened.
   - `System.exit` → S_EXIT for language change, reset and tour.
3. **Targets for the tools.** Reachable-but-unhit methods cluster in:
   - list multi-select (A);
   - attachments and gallery (B; needs an image attachment);
   - password, lock and backup restore (C; needs a password and backups);
   - reminders, notifications and widgets (D; outside the package).

   Verdict-wise, about 110 methods are DEAD candidates (section 5.1) and about 60 are framework-only or environment-gated.
4. **Harness setup.** Seed data through a prepared backup folder imported via Settings, or by writing the DB and prefs with `run-as`. Pre-set the password prefs in a separate configuration. Allow external packages or script the camera and picker steps. Use adb intents for SEND, `hashtag://` and the custom actions. Place the widgets and the shortcut through the launcher.
5. **Hazard candidates** (not reproduced; for awareness):
   - `SnoozeActivity` postpone with `Theme.NoDisplay` and no `finish()` before `onResume` (FW-MEMORY IllegalStateException on API 23+).
   - `NotificationListener.onEventAsync` parses the notification tag as a note id (`NotificationListener.java:61-64`). Backup notifications use tag "0" or no tag (`NotificationsHelper.java:155,162`), so with the listener enabled, dismissing one could lead to `getNote(0)` → null → NPE, or `Long.parseLong(null)` (INFERRED).
6. **Not verified.**
   - Every FW-MEMORY claim, most importantly: toolbar navigation clicks owned by ActionBarDrawerToggle; Monkey's ActivityController blocking other packages; the NoDisplay check; fragment `onConfigurationChanged`; LayoutInflater constructor choice.
   - The cause of Monkey's starting DB state.
   - Whether `S_LIST_SELECT_MANY`, `S_DETAIL_ARCHIVED` and `S_DETAIL_TRASHED` were reached (method-level data cannot separate them).
   - All of these could be resolved by a short device session with per-action coverage resets.
