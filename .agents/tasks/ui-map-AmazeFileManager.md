# AmazeFileManager 3.4.2 (#1837): UI map and modeling plan

Read-only investigation for the method-level trigger graph (recipe: `/Users/darshan/Desktop/yang/GRAPH_PROMPT.md`). Nothing outside this report was written.

## Summary

- **One hub activity.** `MainActivity` (singleInstance) hosts almost every screen as a fragment in `R.id.content_frame`: the 2-tab browser (`TabFragment` with 2 `MainFragment`s), the archive viewer, the app manager, the FTP server and the process viewer. On top of that sit about 45 MaterialDialogs, 4 DialogFragments, 1 bottom sheet, 2 popup menus and 2 action modes. The other 4 activities are Settings (5 preference fragments), About, the text editor and the database viewer.
- **No onboarding, login or vault.** The only first-run gate is the Android 6+ storage permission (`MainActivity.java:436-484`, `PermissionsActivity.java:53-95`). Both baseline runs had it granted before start: line 439 never ran.
- **Method universe.** 2982 methods in JaCoCo (JacocoInstrument excluded). That includes 177 Glide-generated methods and 254 methods in the separate 7z module (`commons_compress_7z`). Union coverage is 1133 (38.0%): APE 1124, Monkey 761, Monkey-only 9.
- **What the baseline never reached:**
  - Settings and About, the app manager and the FTP server. Their only in-app entries are the last 3 rows of a 16-row drawer, and the dispatch line `Drawer.java:597` never ran.
  - The process viewer, which opens only from a notification or an intent extra.
  - The archive viewer and extraction (6.4% of that area). The archive dialog was shown in both runs, but neither of its buttons was ever pressed.
  - Search, DB table view, encryption, and everything that needs a network (SMB, SFTP, FTP, cloud) or root.
- **Gates, in order of impact:**
  1. Drawer rows below the fold.
  2. Dialogs that need typed input: search needs the IME *search* action plus text; New folder needs a name; encryption needs two matching passwords.
  3. Missing fixtures: no `.apk`, `.db`, `.7z`, `.rar`, `.tar*`, `.aze` file.
  4. Missing environment: no SMB or SSH server, no cloud plugin app, no root, no USB OTG.
  5. System UI outside the `-p` package: notifications, the Quick Settings tile, launcher shortcuts, the SAF picker.
- **Proposal.** 115 candidate pages (section 3.4) and 6 areas (section 6):

  | Area | Methods |
  |---|---|
  | A1 Shell and infrastructure | 852 |
  | A2 File list and dialog hub | 353 |
  | A3 File operations, filesystem and services | 649 |
  | A4 Archives (including the 7z module) | 486 |
  | A5 Network and remote | 382 |
  | A6 Secondary screens | 260 |

  Every class belongs to exactly one area.

## 0. Sources, conventions, limits

Path prefixes used below:

| Prefix | Full path |
|---|---|
| `APP/` | `/Users/darshan/Desktop/yang/work/final_java_only/AmazeFileManager/app/` |
| `M` | `APP/AmazeFileManager-#1837/app/src/main/AndroidManifest.xml` |
| `J/` | `APP/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/` |
| `F/` | `APP/AmazeFileManager-#1837/app/src/fdroid/java/com/amaze/filemanager/` (built flavor; only `AboutActivity.java`) |
| `R/` | `APP/AmazeFileManager-#1837/app/src/main/res/` |
| `Z/` | `APP/AmazeFileManager-#1837/commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/` |

- **APK-M** is the merged manifest. No merged manifest exists under `build/intermediates` (only `javac/` is there). I decoded the binary `AndroidManifest.xml` inside `APP/AmazeFileManager-3.4.2-#1837-rebuilt.apk` with a read-only Python AXML reader. It has no line numbers, so it is cited as "APK-M, <component>".
- **Coverage.** `.../AmazeFileManager/monkey/report/report.xml` and `.../ape/report/report.xml`. "M"/"A"/"MA"/"--" means hit by Monkey, by APE, by both, by neither. `L<n>` is the method's first line as JaCoCo reports it. "Line N covered/not covered" refers to `<line ci>` in the same XML.
- **Method list.** There is no JRE on this machine (`javap` fails with "Unable to locate a Java Runtime"). Use the JaCoCo XML as the method list. It already excludes compiler bridges and `access$` methods and includes lambdas, inner classes and constructors. Its totals match the brief: 2982 / 761 / 1124 / 1133.
- **What I read.**
  - In full: `M`; APK-M; `MainActivity`, `Drawer`, `TabFragment`, `PreferencesActivity`, `PrefFrag`, `ColorPref`, the activity superclasses, the `application` package and the fdroid `AboutActivity`.
  - Most of: `MainFragment`, `MainActivityHelper`, `GeneralDialogCreation`, `RecyclerAdapter`, `ItemPopupMenu`, `FileUtils`, `LoadFilesListTask`, `CompressedExplorerFragment`, `TextEditorActivity`, `DatabaseViewerActivity`, `ServiceWatcherUtil`, `EncryptDecryptUtils`, `BottomBar`, `SearchView`, `CloudSheetFragment`, `FtpServerFragment`, `AppsAdapter`.
  - At grep level only: the services, ssh, cloud, sevenz and streamer code, and the remaining dialogs. A graph agent must still read those files completely (GRAPH_PROMPT rule 1).
- **Evidence labels.** `FW-MEMORY` means Android behaviour I recall but did not check (no framework source is available here). `UNVERIFIED` means not confirmed.

## 1. Entry points

**Application:** `J/utils/application/AppConfig.java:48`, chain `AppConfig → GlideApplication (GlideApplication.java:11) → LeakCanaryApplication (LeakCanaryApplication.java:10) → MultiDexApplication`.
- `AppConfig.onCreate` (`AppConfig.java:70-87`) starts the `app_background` HandlerThread used by `runInBackground` (`:100-104`), builds `UtilitiesProvider` and `UtilsHandler`, and resets the StrictMode VM policy.
- `GlideApplication.onCreate` sets the Glide memory category (`GlideApplication.java:13-16`).
- `LeakCanary.install` is commented out (`LeakCanaryApplication.java:15-21`).

Manifest facts: `package="com.amaze.filemanager"` (`M:22-24`); the APK id is `com.amaze.filemanager.debug`; minSdk 14, targetSdk 28, `debuggable=true` (APK-M). No `activity-alias`, no `configChanges` anywhere (`M` and APK-M), no widget providers, no searchable metadata, no static shortcuts. Dynamic pinned shortcuts are created in code (`J/fragments/MainFragment.java:1573-1600`).

| Component | Type | Exported | Intent filters / how it starts | launchMode, theme, other | Handling code |
|---|---|---|---|---|---|
| `activities.MainActivity` | Activity | yes (has filters) | MAIN/LAUNCHER + LEANBACK_LAUNCHER `M:61-65`; GET_CONTENT `*/*` OPENABLE `M:67-72`; RINGTONE_PICKER `M:74-77`; VIEW zip/rar/gzip/bzip2/xz/7z MIME `M:79-90`; QS_TILE_PREFERENCES `M:92-94`; VIEW scheme `com.amaze.filemanager` BROWSABLE (cloud OAuth redirect) `M:96-101`; VIEW `resource/folder` + that scheme `M:103-108`; SEND/SEND_MULTIPLE `*/*` ("Save as") `M:110-115`. Explicit extras: `path` (`MainActivity.java:308`, from pinned shortcuts), `openprocesses` (`:309`, from notifications), `failedOps` (`:313-318`) | `singleInstance` `M:57`; theme `appCompatLight` `M:59` (re-themed at run time by `ThemedActivity.setTheme`, `ThemedActivity.java:42-220`) | `onCreate` `MainActivity.java:277-434`; `checkForExternalIntent` `:486-548`; `onNewIntent` `:1568-1606` (with singleInstance, re-launches arrive here: FW-MEMORY) |
| `activities.PreferencesActivity` | Activity | yes (has filter) | APPLICATION_PREFERENCES `M:123-126` | `uiOptions=splitActionBarWhenNarrow` `M:119`, `appCompatLight` | `onCreate` `PreferencesActivity.java:78-96`; optional extra `current_frag_open` |
| `activities.TextEditorActivity` | Activity | yes | VIEW text/*, application/javascript, application/json, application/xml `M:133-142` | `appCompatLight` | reads `getIntent().getData()`; no data → toast and finish (`TextEditorActivity.java:190-197`) |
| `activities.DatabaseViewerActivity` | Activity | yes | VIEW `db/*` `M:150-156` | `screenOrientation=locked` `M:149` | needs the explicit extra `path` (`DatabaseViewerActivity.java:128-129`). An external VIEW intent has none → `new File(null)` → likely NullPointerException (hazard, UNVERIFIED on device) |
| `activities.AboutActivity` (fdroid source) | Activity | no (no filter) | only `PrefFrag.java:203-205` | theme `aboutLight` `M:160-163`; 10 XML `android:onClick="onClick"` handlers in `R/layout/activity_about.xml:89-614` | `F/activities/AboutActivity.java:58-235` |
| `ExtractService`, `ZipService`, `CopyService`, `EncryptService`, `DecryptService` | started + bound Services | no | started by `ServiceWatcherUtil.runService` (`J/utils/ServiceWatcherUtil.java:162-185`); bound with flags 0 by `ProcessViewerFragment.onResume` (`ProcessViewerFragment.java:155-172`) and `CompressedExplorerFragment.onResume` (ExtractService, `:367-373`) | each calls `startForeground` (e.g. `CopyService.java:149`) | `M:165-187` |
| `asynchronous.services.ftp.FtpService` | Service | **yes**, permission `CONTROL_FTP_SERVER` | started by `FtpReceiver` | declares `protectionLevel=dangerous` `M:26-27`; the app does not `uses-permission` it | `M:189-193`; `FtpService.java:122-145` |
| `asynchronous.services.ftp.FtpTileService` | TileService (API 24+) | yes (QS_TILE filter) | Quick Settings tile | permission BIND_QUICK_SETTINGS_TILE `M:195-203` | `FtpTileService.java:32-73` |
| `asynchronous.services.ftp.FtpReceiver` | manifest receiver | **yes**, permission `CONTROL_FTP_SERVER` | actions `...FTPReceiver.ACTION_START_FTPSERVER` / `..._STOP_FTPSERVER` `M:205-213` | sent by `FtpServerFragment.java:375-385`, `FtpTileService.java:45-60`, the FTP notification Stop action (`FtpNotification.java:47-55`) | `FtpReceiver.java:16-31`; exceptions caught and logged |
| `androidx.core.content.FileProvider` | provider | no, `grantUriPermissions` | authority `com.amaze.filemanager` `M:215-223`; paths `R/xml/provider_paths.xml` | the code uses the same literal authority (`FileUtils.java:97, 398`) | used by share/open (`FileUtils.java:358, 532`; `Utils.java:220`) |
| `JacocoInstrument.SMSInstrumentedReceiver` | receiver | yes | `edu.gatech.m3.emma.COLLECT_COVERAGE` `M:225-229` | coverage harness, out of scope | |
| LeakCanary `HeapAnalyzerService`, `DisplayLeakService`, `DisplayLeakActivity` (MAIN/LAUNCHER), `RequestStoragePermissionActivity` | library | `enabled=false`, process `:leakcanary` | APK-M only | stay disabled: install is commented out (FW-MEMORY that LeakCanary enables them only after `install()`) | no app code |
| aboutlibraries `LibsActivity`; CloudRail `AuthenticationActivity` | library activities | no filters | APK-M only | `LibsActivity` is started from About › Licenses (`F/activities/AboutActivity.java:177-201`) | no app code |

Permissions: WRITE_EXTERNAL_STORAGE, INSTALL_SHORTCUT, INTERNET, ACCESS_WIFI/NETWORK_STATE, USE_FINGERPRINT, REQUEST_INSTALL_PACKAGES, REQUEST_DELETE_PACKAGES, FOREGROUND_SERVICE, and the cloud plugin's `com.amaze.cloud.permission.ACCESS_PROVIDER` (`M:29-38`). The merger adds READ_EXTERNAL_STORAGE (APK-M).

Cold-start behaviour of the external intents (`MainActivity.checkForExternalIntent`, `:486-548`):

| Intent | Effect |
|---|---|
| GET_CONTENT, RINGTONE_PICKER | Set `mReturnIntent` (plus `mRingtonePickerIntent`) and disable rotation (`:491-509`) |
| VIEW with type `resource/folder` | Opens `uri.getPath()` (`:512-521`) |
| Any other VIEW, including the BROWSABLE OAuth scheme | Treated as an archive: `openzip=true`, `zippath=uri.toString()` (`:522-526`); `goToMain` then opens `CompressedExplorerFragment` (`:796-799`). A `content://` URI or the OAuth URI most likely ends in the "unsupported or corrupt" toast (`CompressedExplorerFragment.java:506-509`) (UNVERIFIED) |
| SEND / SEND_MULTIPLE | Turn the FAB into a save button (`initFabToSave`, `:555-585`) |

On `onNewIntent`, a BROWSABLE category goes to `CloudRail.setAuthenticationResponse` (`:1585-1587`).

## 2. First-run flow and setup gates

### 2.1 What a new user goes through (code order)

1. `AppConfig.onCreate` (no UI).
2. `MainActivity.onCreate` (`MainActivity.java:277-434`):
   - opens a root shell only if pref `rootmode` is set (`:592-611`, `PreferenceActivity.java:49-51`);
   - calls `CustomSshJConfig.init()`;
   - builds AppBar, Drawer and FAB (`:286-301`);
   - starts the cloud loader only if the cloud plugin is installed (`:303-305`);
   - on first launch (`books_added` false) adds the bookmarks DCIM, Download, Movies, Music and Pictures (`:358-361` → `UtilsHandler.java:225-239`).
3. **Storage permission (API 23+), the only interactive gate** (`checkForExternalPermission`, `:436-484`):
   - `requestStoragePermission` builds a non-cancelable rationale dialog; its Cancel button calls `finish()` (`PermissionsActivity.java:53-61`);
   - if `shouldShowRequestPermissionRationale` is true, the dialog is shown first and Grant asks the system; otherwise the system dialog appears directly (`:82-95`);
   - on denial: toast and ask again (`:31-34`), so the app loops until granted or Cancel;
   - on grant: the drawer is refreshed and, when `needtosethome` is set, the tabs DB is reset (`MainActivity.java:438-483`).
4. `runInParallel` loads hidden files, history, grid/list paths, bookmarks and servers from SQLite, then refreshes the drawer and calls `goToMain` (`:365-433`).
5. `TabFragment.onCreateView`, first time (empty tabs DB): tab 1 = first storage, tab 2 = second or first (`TabFragment.java:111-127`). If no storage is found at all, it **silently enables root mode** and opens `/` (`:115-119`).
6. No intro, tutorial, changelog, rating prompt, login, account, vault or data import. A grep for intro/onboard/tutorial/changelog/first-run patterns found nothing.

### 2.2 Feature gates beyond first run

| Gate | Enforced by | Unlocks |
|---|---|---|
| Root mode pref `rootmode` + a working `su` | `PreferenceActivity.java:49-51`; shell `MainActivity.java:592-611`; `HybridFile.java:111`; `DeleteTask.java:61-66` | `S_MAIN_ROOT`, the permissions editor in Properties (`GeneralDialogCreation.java:530`), `RootUtils`, system-app uninstall (`AppsAdapter.java:191-224`) |
| Amaze Cloud Plugin app `com.filemanager.amazecloud` | `CloudContract.java:9`; `CloudSheetFragment.java:89-98` (cloud rows hidden otherwise, `:66-73`); `CloudHandler.java:85-86` throws → toast `MainActivity.java:1815-1819` | Every cloud path: `CloudLoaderAsyncTask`, `CloudUtil`, `CloudStreamer`/`Server`, `S_MAIN_CLOUD` |
| Reachable SMB server | `LoadFilesListTask.java:105-124` (null on failure) | `S_MAIN_SMB`, `StreamServer`/`Streamer`, re-auth (`MainFragment.java:1345-1356`) |
| Reachable SSH server + credentials or key | `SftpConnectDialog.java:160-230` (host-key task) | `S_MAIN_SFTP`, `SshClientUtils`, `SshAuthenticationTask` |
| Wi-Fi, LAN or hotspot | `FtpServerFragment.java:132-147, 406-418`; `FtpService.java:271-305` | Starting the FTP server |
| Encryption: API 18+; fingerprint needs hardware, an enrolled finger and a secure keyguard | `RecyclerAdapter.java:974-978`; `PrefFrag.java:95-136` | Encrypt/decrypt services, `CryptUtil`, `FingerprintHandler` |
| Settings toggles | `goBack_checkbox` → ".." row (`MainFragment.java:1087-1090`); `typeablepaths` → path dialog (`BottomBar.java:150-155`); `showPermissions` (`RecyclerAdapter.java:678, 823`); `crypt_remember` skips the warning (`ItemPopupMenu.java:179-193`); `showHidden`; `texteditor_newstack`; About easter egg `studio` → audio countdown (`F/activities/AboutActivity.java:151-167`, `FileUtils.java:761-790`) | The matching code paths |
| Typed input | The positive button is disabled while input is invalid (`WarnableTextInputValidator.java:32, 68-84`). New folder starts empty and its validator rejects empty input (`MainActivityHelper.java:136-153`). New file is prefilled ".txt" (warning state, enabled; `:162-191`). Compress is prefilled ".zip" (`GeneralDialogCreation.java:952-956`). Search runs only on `IME_ACTION_SEARCH` (`SearchView.java:54-60`) and only with non-empty text (`MainActivity.java:290-294`) | Create folder, search, password dialogs |
| Pin-shortcut support in the launcher | `MainFragment.java:1578-1583` | `ShortcutManagerCompat.requestPinShortcut` |

### 2.3 What the baseline shows

- **Permission was pre-granted.** `MainActivity.java:439` is not covered in either run, and every `PermissionsActivity` method except `<init>` and `checkStoragePermission` has 0 hits. The permission must have been granted before launch, probably by `install -g` (UNVERIFIED).
- **APE started from fresh data, Monkey did not.** The first-run bookmark lines `MainActivity.java:359-360` are covered by APE only. Monkey began with existing preferences (cause UNVERIFIED). Recommend `pm clear` before each run.
- **Only internal storage was present.** The OTG and SD-card branches `Drawer.java:262-264, 273-281` are not covered, and `TabFragment.java:124` is not covered.
- **APE saved an SMB connection.** The positive lambda `SmbConnectDialog.lambda$onCreateDialog$2` (registered at `SmbConnectDialog.java:220`) and the servers loop `Drawer.java:296-299` are covered by APE only.

### 2.4 Screens the baseline never reached

| Screen | Evidence (JaCoCo, union) | Most likely gate |
|---|---|---|
| Settings (`PreferencesActivity`, `PrefFrag`, `ColorPref`, `FoldersPref`, `AdvancedSearchPref`, `ColorPickerDialog`, preference views) | 0 hits in all of them; `QuickAccessPref` only `<clinit>` (static fields read by Drawer) | The only in-app entry is the last drawer row "Settings" (`Drawer.java:435-442`). `ITEM_INTENT` dispatch `Drawer.java:597` is not covered in either run. The rows are appended after ~13 storage, bookmark and quick-access rows (`Drawer.java:252-454`), so they are probably below the fold (UNVERIFIED: screen size not known). The external APPLICATION_PREFERENCES entry is outside `-p` |
| About, LibsActivity | `AboutActivity` 0/9 | only via Settings |
| App manager (`AppsListFragment`, `AppsAdapter`, `AppListLoader`) | 0 | drawer row "Apps" (`Drawer.java:418-433`) never selected |
| FTP server (`FtpServerFragment` 0/38, `FtpService`, `FtpReceiver`, `FtpTileService`, `FtpNotification`) | 0 | drawer row "FTP" (`Drawer.java:402-416`) never selected; the QS tile is system UI |
| Process viewer (`ProcessViewerFragment` 0/19) | 0 | only through the progress-notification content intent (`CopyService.java:121-124` and similar in the other services) or the `openprocesses` extra (`MainActivity.java:388-397, 1588-1596`). The notification shade is outside `-p` (FW-MEMORY: Monkey/APE block other packages) |
| Archive viewer and extraction (`CompressedExplorerFragment` 0/35, `CompressedExplorerAdapter`, all `*Decompressor`/`*HelperTask`/`*Extractor`, `ExtractService` 0/32, the whole 7z module) | 0 | `showArchiveDialog` ran to `b.show()` in both runs (`GeneralDialogCreation.java:944` covered), but neither button lambda ran: Extract L935, View L936 (`lambda$showArchiveDialog$26/27` 0 hits). No `.rar`/`.7z`/`.tar*`/`.apk` fixtures |
| Search results (`SearchWorkerFragment` 0/4, `SearchAsyncTask` 0/15, `MainFragment.onSearch*`) | 0 | APE fired the search field's editor action, but not with `IME_ACTION_SEARCH`: `SearchView.java:55` and `:60` covered, `:56-58` not (probably a hardware Enter key, GRAPH_PROMPT step 3.6) |
| DB table view (`DbViewerFragment` 0/4, `DbViewerTask` 0/8) | `DatabaseViewerActivity` opened in both runs through Open as › Database (`FileUtils.java:612-615` covered) | no SQLite fixture: `openDatabase` threw and the activity finished (`DatabaseViewerActivity.java:181-183` covered, `:177-180` not) |
| Encrypt / decrypt (`EncryptService` 0/21, `DecryptService` 0/22, `CryptUtil` 0/24) | APE reached the warning and password dialogs (`showEncryptAuthenticateDialog` lambdas 14, 15, 17-19) | needs two equal typed passwords: the positive `lambda$...$16` has 0 hits. Decrypt needs an `.aze` file plus a `CryptHandler` row |
| SMB / SFTP / cloud browsing, streamers | 0 | needs servers, the cloud plugin, accounts |
| Text-editor save | `saveFile` 0; Monkey showed the unsaved-changes dialog (`TextEditorActivity.java:235-247` covered) | neither button pressed; the toolbar Save item was never tapped |
| Package installer dialog | `showPackageDialog` 0 | no `.apk` fixture (`FileUtils.java:752-753`) |
| OTG, root permission editor | `OTGUtil` 1/6, `RootUtils` 0/15 | no USB device; root mode off |

### 2.5 What a harness should prepare

- **Files** under `/sdcard/Download` or a new `/sdcard/Documents` (the dataset's Documents folder is missing):
  - archives: `.zip` (present), a password-protected `.zip`, `.rar`, `.7z` (one encrypted), `.tar`, `.tar.gz`/`.tgz`, `.tar.bz2`, `.tar.xz`, `.tar.lzma`;
  - a small signed `.apk`;
  - a SQLite `.db` with at least one table;
  - dot-files and folders for "hidden";
  - a nested folder tree and two folders sharing a file name (copy-conflict dialog `PrepareCopyTask.java:178-219`);
  - a file of tens of MB, so copy/extract services run long enough to show their notification and progress;
  - optionally an audio file (Music fixtures exist) and a video.
- **Rescan media** after pushing. The quick-access lists query MediaStore (`LoadFilesListTask.java:257-447`).
- **Preferences.** The build is debuggable, so `run-as` can write `shared_prefs`. Alternatively start the screens directly: `am start -a android.intent.action.APPLICATION_PREFERENCES -p com.amaze.filemanager.debug`; FTP fragment via `-a android.service.quicksettings.action.QS_TILE_PREFERENCES -n com.amaze.filemanager.debug/com.amaze.filemanager.activities.MainActivity`; process viewer via `--ez openprocesses true`. Useful toggles: `goBack_checkbox`, `typeablepaths`, `showHidden`, `showPermissions`, `crypt_password`, `view`.
- **Intents** for the external entry points:
  - GET_CONTENT `*/*`, RINGTONE_PICKER;
  - SEND / SEND_MULTIPLE with a `content://` stream;
  - VIEW on a zip;
  - VIEW `resource/folder` with `com.amaze.filemanager:/sdcard/Download`;
  - VIEW `text/plain` on a file URI (TextEditorActivity);
  - DatabaseViewerActivity with `--es path /sdcard/Download/x.db`.
- **Network:**
  - an SMB share and an SSH server reachable from the emulator (host 10.0.2.2 by FW-MEMORY), with known credentials;
  - Wi-Fi up for FTP (FW-MEMORY: API 25+ emulator images provide a virtual Wi-Fi network);
  - cloud needs the plugin app plus real accounts, so treat it as `REACHABLE_AFTER_SETUP` or infeasible offline.
- **Device features:** a rooted image where the app can get `su`, for root mode; fingerprint enrolment (`adb -e emu finger touch`) plus a lock screen (FW-MEMORY); USB OTG is not possible on the emulator (UNVERIFIED).
- **Tool scope.** Allow DocumentsUI and SystemUI packages, or drive notifications and SAF by script. Under Monkey/APE `-p`, blocked SAF launches come back canceled. APE hit `Drawer.onActivityResult` without data; that is consistent with this (FW-MEMORY).

## 3. Screens and navigation

### 3.1 Window inventory

- **Activities (5 app plus libraries):** `MainActivity`, `PreferencesActivity`, `TextEditorActivity`, `DatabaseViewerActivity`, `AboutActivity`; plus `LibsActivity` and the system pickers/choosers.
- **Fragments in MainActivity's `R.id.content_frame`** (`R/layout/main_toolbar.xml:34`):
  - `TabFragment`: replace with back stack `tabt1` (`MainActivity.java:781-800`). It hosts a `DisablableViewPager` with a `FragmentStatePagerAdapter` of 2 `MainFragment`s (`TabFragment.java:319-367`).
  - `CompressedExplorerFragment`: **added** on top (`MainActivity.java:1240-1250`).
  - `AppsListFragment` (ListFragment) and `FtpServerFragment`: replace, committed when the drawer closes (`Drawer.java:402-433, 530-534`).
  - `ProcessViewerFragment`: replace (`MainActivity.java:388-397, 1588-1596`).
  - `SearchWorkerFragment`: headless, retained, tag `async_helper` (`MainActivityHelper.java:627-641`).
- **PreferencesActivity** loads framework `PreferenceFragment`s into `R.id.prefsfragment` (`PreferencesActivity.java:251-275`): `PrefFrag` (`R/xml/preferences.xml`), `ColorPref` (two sections: `color_prefs.xml` / `conficolor_prefs.xml`, `ColorPref.java:193-238`), `FoldersPref`, `QuickAccessPref`, `AdvancedSearchPref`.
- **DatabaseViewerActivity:** a ListView of tables; `DbViewerFragment` (WebView) is added with back stack (`DatabaseViewerActivity.java:133-142`).
- **Bottom sheets:** `CloudSheetFragment` (from the FAB, `MainActivity.java:1952-1956`). `PropertiesSheet` is never instantiated (section 5).
- **DialogFragments** (`android.app`, shown with `getFragmentManager()`): `SmbSearchDialog`, `SmbConnectDialog`, `SftpConnectDialog`, `RenameBookmark`.
- **MaterialDialogs:** `GeneralDialogCreation` (about 22 builders), `MainActivityHelper` (name, LEXA, failed ops), `MainActivity` (directory sort `:974-992`, set home `:945-960`), `PermissionsActivity`, `FileUtils.openWith` (`:588-633`), `PrepareCopyTask.showDialog`, `ShareTask.onPostExecute`, `TextEditorActivity.checkUnsavedChanges`, `PrefFrag`, `ColorPref`, `FoldersPref`, `FtpServerFragment`, `AppsAdapter`, `SftpConnectDialog` (host key: AlertDialog lambdas).
- **Preference dialogs:** `ColorPickerDialog` (DialogPreference, `ColorPickerDialog.java:40`) and two `EditTextPreference`s (`preferences.xml:110-120`, framework dialogs).
- **Popups:** `ItemPopupMenu` (`R/menu/item_extras.xml`, `RecyclerAdapter.java:948-984`); the AppsAdapter `PopupMenu` (`app_options.xml`, `AppsAdapter.java:167-266`).
- **Options menus:** `activity_extra.xml` (MainActivity, with the Sort submenu at lines 37-49); `ftp_server_menu.xml` (`FtpServerFragment.java:317-319`); `text.xml` (TextEditorActivity).
- **Action modes:** `MainFragment.mActionModeCallback` (`contextual.xml`, `MainFragment.java:461-772`); `CompressedExplorerFragment.mActionModeCallback` (same menu with most items hidden, `:247-352`). Both start through `startSupportActionMode` (`RecyclerAdapter.java:192`, and the archive adapter).
- **Drawer:** `Drawer` + `CustomNavigationView`, menu built in code (`Drawer.java:252-458`), header long-press (`:141-155`). On w720dp layouts it is locked open (`Drawer.java:203-209`, `R/layout-w720dp/main_toolbar.xml`).
- **FAB:** `SpeedDialView` with 3 actions, overlay `fabs_overlay_layout` (`MainActivity.java:1496-1536, 1930-1962`).
- **App bar:** `AppBar`, `SearchView` (circular reveal), `BottomBar` (path text; tap shows breadcrumb buttons for 5 s; long-press opens the path dialog).
- **System UI:** progress notifications with a Cancel action, the failed-ops notification (`AbstractProgressiveService.java:232-259`), the FTP notification with a Stop action (`FtpNotification.java:27-60`), the QS tile, pinned shortcuts.

### 3.2 How the user moves (main transitions)

| From | Gesture | Callback chain | To |
|---|---|---|---|
| Launcher | tap icon | `MainActivity.onCreate` → `runInParallel.onPostExecute` → `goToMain` → `TabFragment.onCreateView` → `MainFragment.onActivityCreated` → `loadlist` → `LoadFilesListTask` (ASYNC) → `setListElements` (`MainFragment.java:1016-1077`) | `S_MAIN_LIST` / `S_MAIN_GRID` / `S_MAIN_EMPTY` |
| Main list | tap folder row | `RecyclerAdapter` lambda (`:530-533`; grid `:700-703`) → `MainFragment.onListItemClicked` (`:851-948`) → `loadlist` | Main list of the new folder |
| Main list | tap file row | `onListItemClicked` → `FileUtils.openFile` (`FileUtils.java:746-800`): `.apk` → `S_DLG_PACKAGE`; archive while Amaze is the default handler → `S_DLG_ARCHIVE`; `.db` → DatabaseViewerActivity; audio → external player; else `openunknown` (`:420-454`): VIEW intent (text types → TextEditorActivity) or `S_DLG_OPEN_AS` when the MIME type is unknown. `.aze` → decrypt flow (`MainFragment.java:896-907`). Picker mode → `returnIntentResults` (`:976-1008`) | various |
| Main list | long-press row, or tap its icon | `toggleChecked` (`RecyclerAdapter.java:162-206`) → `startSupportActionMode` | `S_MAIN_SELECT` |
| Main list | tap the row's "⋮" | `showPopup` (`RecyclerAdapter.java:948-984`) | `S_POPUP_ITEM` |
| Main list | pull down | SwipeRefresh lambda (`MainFragment.java:261`; empty view `:1037-1053`) → `loadlist` | same page |
| Main list | swipe horizontally | ViewPager → `TabFragment.onPageSelected` (`:289-316`) | other tab (same page set) |
| Main list | tap path bar / long-press it | `BottomBar` GestureDetector `onSingleTapConfirmed` (`:130-148`), `onLongPress` (`:150-155`, needs `typeablepaths`) | `S_MAIN_PATHBAR` / `S_DLG_CHANGE_PATH` |
| Main list | toolbar Search | `onOptionsItemSelected` R.id.search (`MainActivity.java:1040-1042`) → `SearchView.revealSearchView` | `S_MAIN_SEARCH_BAR`; IME search → `MainActivityHelper.search` (`:585-641`) → `SearchWorkerFragment` → `SearchAsyncTask` → `MainActivity.onPreExecute`/`onProgressUpdate`/`onPostExecute` (`:1771-1792`) → `S_MAIN_SEARCH_RESULTS` |
| Main list | overflow items | `MainActivity.onOptionsItemSelected` (`:928-1044`), items visible per `onPrepareOptionsMenu` (`:834-903`): home `:937`, history `:941` → `S_DLG_HISTORY`, set home `:945`, exit `:961`, sort `:964` (submenu) → sortby `:970` / dsort `:974`, hidden files `:993`, list/grid toggle `:996`, paste `:1025`, extract `:1034`, search `:1040` | dialogs / grid / exit |
| Main list | hamburger or edge swipe | `ActionBarDrawerToggle` (`Drawer.java:217-240`) | `S_DRAWER` |
| Drawer | tap storage, bookmark or quick access | `onNavigationItemSelected` (`:558-602`) → `pendingPath` → `onDrawerClosed` (`:530-556`) → `loadlist` or `goToMain` | Main list (`S_MAIN_CUSTOM` for quick access) |
| Drawer | tap FTP / Apps / Settings | `meta.onClickListener.onClick()` (`:597`) → `lambda$refreshDrawer$1/2/3` | `S_FTP_*` / `S_APPS_LIST` / PreferencesActivity (MainActivity **finishes**, `:437-440`) |
| Drawer | tap a row's action icon | `onNavigationItemActionClick` (`:604-637`): storage → storage properties; bookmark → RenameBookmark; `smb:`/`ssh:` server → edit dialog; cloud → account dialog | dialogs |
| Drawer | long-press header | OPEN_DOCUMENT `image/*`, request 31 (`:141-155`) → RESULT `MainActivity.onActivityResult` (`:1306-1309`) → `Drawer.onActivityResult` (`:498-509`) | system picker, back to drawer |
| Main list | tap FAB, then an action | `FabActionListener.onActionSelected` (`MainActivity.java:1943-1962`): new folder `:1946` → `MainActivityHelper.mkdir`; new file `:1949` → `mkfile`; cloud `:1952` → `CloudSheetFragment` | `S_DLG_NEW_FOLDER` / `S_DLG_NEW_FILE` / `S_CLOUD_SHEET` |
| Any MainActivity page | Back | `MainActivity.onBackPressed` (`:703-756`): close drawer (`:704`) › hide search (`:710`) › close FAB or `MainFragment.goBack` (`:713-718`; `goBack` at home/root → `exit()` "press again" with a 2 s window, `:765-779`) › archive: finish action mode, go up a level, finish if `openzip`, else remove the fragment (`:719-737`) › FTP → `goToMain(path)` (`:738-751`) › other → `goToMain(null)` (`:752-754`) | previous page / `S_EXIT` |
| Notification | tap | content intent with `openprocesses` (`CopyService.java:121-124`) → `MainActivity.onNewIntent` (`:1588-1596`) | `S_PROCESS_VIEWER` |
| Notification | Cancel | broadcast → `CopyService` receiver3 (`:525-533`), `ExtractService` receiver1 (`:379-385`), `ZipService` receiver1 (`:305-311`), Encrypt/Decrypt `cancelReceiver` | service stops |
| PreferencesActivity | Back / Up at root | `onBackPressed` (`PreferencesActivity.java:106-123`) / `onOptionsItemSelected` (`:125-150`) → start MainActivity + `finish` | Main list |
| TextEditor / DBViewer / About | Back / Up | `checkUnsavedChanges` (`TextEditorActivity.java:233-251`) / `super.onBackPressed` | `S_MAIN_PAUSED` → resume |

### 3.3 Modes that change active handlers

| Window | Mode variables (where read) |
|---|---|
| MainActivity | fragment at frame (`onPrepareOptionsMenu` `:834-903`): TabFragment, CompressedExplorer, Apps, ProcessViewer or FTP; `pasteHelper != null` (`:758-764`); `mReturnIntent` / `mRingtonePickerIntent` (picker); save mode (`initFabToSave`); `openzip`; drawer open or locked (tablet); SearchView shown; FAB open; `backPressedToExitOnce` (2 s window) |
| MainFragment | `selection` / `mActionMode`; `results` (search results; `openparent` only then, `:579-616`); `IS_LIST` vs grid (different bind lambdas, `RecyclerAdapter.java:514-828`); empty (`nofilesview`, `:1093-1101`); `openMode` (FILE, ROOT, CUSTOM, SMB, SFTP, OTG, cloud: back rules `:1265-1342`, click routing `:913-936`, action-mode menu `:530-534`); `goBack_checkbox` (".." row → `goBackItemClick` `:1359-1391`); `mRetainSearchTask` (Back after opening a result re-runs the search, `:1306-1333`); `isEncryptOpen` |
| Action mode (MainFragment) | item count, file vs folder, picker mode (`onPrepareActionMode` `:520-620`) |
| ItemPopupMenu | folder: no open-with/share, `return_select` only in picker mode; file: no bookmark; archive suffix → Extract; `.aze` → Decrypt else Encrypt, API ≥ 18 only (`RecyclerAdapter.java:952-979`) |
| CompressedExplorerFragment | `selection`; root vs sub-folder (`canGoBack`); `openzip` (Back finishes); `gobackitem` pref |
| AppsListFragment | system vs user app, and root mode, decide the uninstall branch (`AppsAdapter.java:187-224`) |
| FtpServerFragment | no network / stopped / running (`updateStatus` `:406-463`); password set → eye button |
| PreferencesActivity | `selectedItem`; `restartActivity` (Back restarts, `:110-111`); ColorPref section 0/1; customization enabled only when the color config is CUSTOM (`ColorPref.java:240-248`) |
| TextEditorActivity | load OK or failed; `mModified` (Save visible, `:350-355`; Back → dialog); find bar shown; read-only cache file (`:303-317`) |
| DatabaseViewerActivity | table list vs table fragment |

### 3.4 Candidate page list (115 pages)

Owner = proposed area (section 6). `@CONTEXT` variants to plan for:

- `MainActivity.onOptionsItemSelected@TAB/@ARCHIVE/@APPS/@FTP/@PROCESS` and `onBackPressed@...`;
- `RecyclerAdapter` list vs grid lambdas;
- `GeneralDialogCreation.showNameDialog@NEW_FOLDER/@NEW_FILE/@RENAME`;
- `HiddenAdapter@HISTORY/@HIDDEN`;
- `AbstractProgressiveService.*@COPY/@ZIP/@EXTRACT/@ENCRYPT/@DECRYPT`;
- `MainFragment.*@TAB1/@TAB2` if paths diverge.

| Page | Window class | Mode predicate | Description | Owner |
|---|---|---|---|---|
| S_ENTRY | — | outside app | launcher, external sender apps | A1 |
| S_EXIT | — | finished/crashed | process may survive (statics: `MainActivity.currentTab`, `DataUtils` singleton, `MainActivityHelper.SEARCH_TEXT`, `ServiceWatcherUtil.*`) | A1 |
| S_MAIN_PAUSED | MainActivity | stopped/paused | Home, another activity, system UI on top | A1 |
| S_PREFS_PAUSED / S_EDITOR_PAUSED / S_DBVIEWER_PAUSED / S_ABOUT_PAUSED | each activity | paused | back-stack pseudo pages (4 pages) | A6 |
| S_SYS_PERMISSION | system | storage permission prompt | runtime permission dialog | A1 |
| S_SYS_DOC_PICKER | DocumentsUI | SAF/GET_CONTENT open | tree (SD write, OTG), image (drawer header), PEM key (SFTP) | A1 |
| S_SYS_CHOOSER | system/other app | chooser or target app | open with, share target, market, browser, app details, (un)install confirm | A1 |
| S_HOME_SHORTCUT | launcher | pinned shortcut exists | tap → MainActivity with `path` | A1 |
| S_NOTIF_PROGRESS | SystemUI | a progressive service running | tap → process viewer; Cancel action | A3 |
| S_NOTIF_FAILED | SystemUI | failed ops | tap → failed-ops dialog | A3 |
| S_NOTIF_FTP | SystemUI | FTP running | tap → MainActivity; Stop action | A5 |
| S_QS_TILE | SystemUI | tile added | tap toggles the server; long-press → FTP page | A5 |
| S_DLG_STORAGE_RATIONALE | MaterialDialog | `shouldShowRequestPermissionRationale` | Grant / Cancel (finish) | A1 |
| S_DLG_INSTALL_RATIONALE | MaterialDialog | API 26+, cannot install | install-permission rationale (`FileUtils.java:388-392`) | A1 |
| S_DRAWER | Drawer | open, not locked | storage, server, cloud, bookmark, quick rows; FTP/Apps/Settings; action icons; header | A1 |
| S_FAB_OPEN | SpeedDialView | expanded | New folder / New file / Cloud connection; overlay | A1 |
| S_MAIN_SEARCH_BAR | SearchView | revealed | edit text, clear, back | A1 |
| S_MAIN_PATHBAR | BottomBar | breadcrumbs visible (5 s) | root, storage, folder buttons → `changePath` | A1 |
| S_MAIN_SORT_SUBMENU | options submenu | Sort tapped (TabFragment) | Sort by / Directory sort | A1 |
| S_DLG_DIRSORT | MaterialDialog | — | directory-sort single choice (`MainActivity.java:974-992`) | A1 |
| S_DLG_SET_HOME | MaterialDialog | FILE or ROOT mode | set current folder as tab home | A1 |
| S_DLG_RENAME_BOOKMARK | RenameBookmark | bookmark action icon | rename / delete bookmark | A1 |
| S_DLG_OTG_SAF | MaterialDialog | OTG row, no root URI | explanation → OPEN_DOCUMENT_TREE (`Drawer.java:580-590`) | A1 |
| S_MAIN_SAVE | MainActivity/MainFragment | SEND / SEND_MULTIPLE | FAB = save here, then finish | A1 |
| S_MAIN_LIST | MainFragment (TabFragment) | FILE mode, list, non-empty, no selection, no results, no paste | normal browser | A2 |
| S_MAIN_GRID | MainFragment | `IS_LIST == false` | grid browser (different bind lambdas) | A2 |
| S_MAIN_EMPTY | MainFragment | list empty, not results | "no files" view with its own refresh | A2 |
| S_MAIN_PASTE | MainFragment | `pasteHelper != null` | Paste visible in the toolbar | A2 |
| S_MAIN_SELECT | MainFragment + ActionMode | `selection && !results` | contextual menu (copy, cut, delete, all, share, compress, open with, hide, add shortcut, extract, `openmulti` in picker mode) | A2 |
| S_MAIN_SEARCH_RESULTS | MainFragment | `results == true` | streamed search results | A2 |
| S_MAIN_SELECT_RESULTS | MainFragment + ActionMode | `selection && results` | also "open parent" | A2 |
| S_MAIN_CUSTOM | MainFragment | `openMode == CUSTOM` | Quick / Recent / Images / Videos / Audio / Documents / APKs | A2 |
| S_MAIN_PICKER | MainFragment | `mReturnIntent` | tap a file returns a result and finishes | A2 |
| S_POPUP_ITEM | ItemPopupMenu | — | open with, cut, copy, delete, rename, encrypt/decrypt, properties, share, extract, bookmark, select | A2 |
| S_DLG_RENAME | showNameDialog | — | rename (prefilled, valid) | A2 |
| S_DLG_DELETE | MaterialDialog | — | delete confirmation with summary task | A2 |
| S_DLG_PROPERTIES | MaterialDialog | file or folder | properties, hashes, chart, `.nomedia` checkbox | A2 |
| S_DLG_PROPERTIES_ROOT | MaterialDialog | root && permissions length > 6 | permission table + Set | A2 |
| S_DLG_PROPERTIES_STORAGE | MaterialDialog | storage action icon | used/free pie chart | A2 |
| S_DLG_COMPRESS | MaterialDialog | — | zip name (prefilled ".zip") | A2 |
| S_DLG_SORT | MaterialDialog | MainFragment | sort type, "only this folder", Asc/Desc | A2 |
| S_DLG_HISTORY | MaterialDialog + HiddenAdapter | — | history list, Clear | A2 |
| S_DLG_HIDDEN | MaterialDialog + HiddenAdapter | — | hidden list, un-hide buttons | A2 |
| S_DLG_ARCHIVE | MaterialDialog | archive tapped | Extract / View / Cancel (View disabled if not extractable) | A2 |
| S_DLG_PACKAGE | MaterialDialog | `.apk` tapped | Install / View / Cancel | A2 |
| S_DLG_ENCRYPT_WARNING | MaterialDialog | `!crypt_remember` | warning, "remember" checkbox | A2 |
| S_DLG_ENCRYPT_PASSWORD | MaterialDialog | no master password or fingerprint | password, confirm, file name | A2 |
| S_DLG_ENCRYPT_SAVEAS | MaterialDialog | master password or fingerprint set | file-name-only dialog | A2 |
| S_DLG_DECRYPT_PASSWORD | MaterialDialog | entry password is not the fingerprint sentinel | password check | A2 |
| S_DLG_DECRYPT_FINGERPRINT | MaterialDialog + FingerprintHandler | API 23+, fingerprint entry | fingerprint prompt | A2 |
| S_DLG_CHANGE_PATH | MaterialDialog | `typeablepaths` | typed path, Go | A2 |
| S_DLG_CLOUD_ACCOUNT | MaterialDialog | cloud action icon | delete account | A2 |
| S_DLG_NEW_FOLDER | showNameDialog | — | name; Create disabled while empty | A3 |
| S_DLG_NEW_FILE | showNameDialog | — | name prefilled ".txt" | A3 |
| S_DLG_SAF_GUIDE | MaterialDialog | target on external SD, not writable | "needs access" → OPEN_DOCUMENT_TREE, request 3 | A3 |
| S_DLG_FAILED_OPS | MaterialDialog | failed-ops intent or broadcast | list of failures | A3 |
| S_DLG_COPY_CONFLICT | MaterialDialog | name clash on paste | Skip / Overwrite / Cancel, apply-to-all | A3 |
| S_DLG_SHARE | MaterialDialog + ShareAdapter | share | in-app share-target list | A3 |
| S_DLG_OPEN_AS | MaterialDialog | unknown MIME or "open with" | Text, Image, Video, Audio, Database, Other | A3 |
| S_PROCESS_VIEWER | ProcessViewerFragment | — | progress cards, cancel buttons, charts | A3 |
| S_MAIN_ROOT | MainFragment | `openMode == ROOT` | root browsing | A3 |
| S_MAIN_OTG | MainFragment | `openMode == OTG` | USB browsing via DocumentFile | A3 |
| S_ARCHIVE_LIST | CompressedExplorerFragment | no selection | archive browsing; toolbar Extract | A4 |
| S_ARCHIVE_SELECT | ActionMode | selection | Select all / Extract | A4 |
| S_DLG_ARCHIVE_PASSWORD | showPasswordDialog | encrypted zip/7z | password (`ExtractService.java:330-340`, `SevenZipHelperTask.java:103-114`) | A4 |
| S_CLOUD_SHEET | CloudSheetFragment | plugin present / absent | SMB, SFTP, (Box, Dropbox, GDrive, OneDrive) or "get plugin" | A5 |
| S_DLG_SMB_SEARCH | SmbSearchDialog | scanning | LAN hosts, Enter manually / Cancel | A5 |
| S_DLG_SMB_CONNECT / S_DLG_SMB_EDIT | SmbConnectDialog | edit flag | new / edit (delete) SMB connection | A5 |
| S_DLG_SMB_HELP | MaterialDialog | — | SMB instructions | A5 |
| S_DLG_SFTP_CONNECT / S_DLG_SFTP_EDIT | SftpConnectDialog | edit flag | new / edit (delete) SFTP; PEM picker | A5 |
| S_DLG_SFTP_HOSTKEY | AlertDialog | host-key fetched | accept host fingerprint | A5 |
| S_MAIN_SMB / S_MAIN_SFTP / S_MAIN_CLOUD | MainFragment | `openMode` SMB / SFTP / cloud | remote listings (tap streams, launches or downloads) | A5 |
| S_FTP_NO_NETWORK / S_FTP_STOPPED / S_FTP_RUNNING | FtpServerFragment | network and `isRunning` | start/stop button state | A5 |
| S_DLG_FTP_PORT / _PATH / _LOGIN / _TIMEOUT | MaterialDialog | menu item | FTP settings (4 pages) | A5 |
| S_APPS_LIST | AppsListFragment | — | installed apps; menu Sort | A6 |
| S_POPUP_APP | PopupMenu | — | open, backup, uninstall, properties, Play, share | A6 |
| S_DLG_APPS_SORT | MaterialDialog | — | app sort | A6 |
| S_DLG_UNINSTALL_SYSTEM | MaterialDialog | system app && root | confirm root uninstall | A6 |
| S_PREFS_MAIN | PrefFrag | `selectedItem == 0` | main settings | A6 |
| S_DLG_PREF_COLUMNS / _THEME / _MASTER_PASSWORD | MaterialDialog | — | 3 settings dialogs | A6 |
| S_DLG_PREF_EXTRACT_PATH / _ZIP_PATH | EditTextPreference | — | framework dialogs (2 pages) | A6 |
| S_PREFS_COLORS / S_PREFS_COLORS_CUSTOM | ColorPref | section 0 / 1 | color settings | A6 |
| S_DLG_COLOR_PRESETS | ColorPickerDialog | — | presets, custom, random | A6 |
| S_DLG_COLOR_CHOOSER | MaterialDialog + ColorAdapter | customization enabled | color grid, Default | A6 |
| S_PREFS_FOLDERS | FoldersPref | — | sidebar bookmarks | A6 |
| S_DLG_FOLDER_ADD / _EDIT / _DELETE | MaterialDialog | — | bookmark dialogs (3 pages) | A6 |
| S_PREFS_QUICKACCESS / S_PREFS_ADVSEARCH | Quick/AdvancedSearch pref | — | switches | A6 |
| S_ABOUT / S_ABOUT_LIBS | AboutActivity / LibsActivity | — | links, easter egg, licenses | A6 |
| S_EDITOR_VIEW | TextEditorActivity | loaded, `!mModified` | read/edit text | A6 |
| S_EDITOR_MODIFIED | TextEditorActivity | `mModified` | Save visible; Back → dialog | A6 |
| S_EDITOR_FIND | TextEditorActivity | find bar shown | prev / next / close | A6 |
| S_EDITOR_READONLY | TextEditorActivity | file in app cache | read-only snackbar | A6 |
| S_DLG_EDITOR_UNSAVED | MaterialDialog | modified + Back | Yes (save) / No | A6 |
| S_DBVIEWER_TABLES / S_DBVIEWER_TABLE | DatabaseViewerActivity / DbViewerFragment | — | table list / WebView of a table | A6 |

Rows that cover several pages (for example `S_FTP_*`, `S_DLG_FTP_*`) count each page separately: 115 in total. Pages per owner: A1 19, A2 28, A3 12, A4 3, A5 20, A6 33.

Not proposed as pages:
- loading states: the list keeps its handlers, so model loading as ASYNC edges;
- tablet locked-drawer layout: phone emulator assumed;
- the `backPressedToExitOnce` window: use `needs_state` on the second Back edge.

## 4. Framework mechanisms

| Mechanism | App classes, with the registration site |
|---|---|
| RecyclerView adapters | `RecyclerAdapter` (`MainFragment.java:1106-1111`); `CompressedExplorerAdapter`; `HiddenAdapter` and `ShareAdapter` (inside MaterialDialogs, `GeneralDialogCreation.java:1097-1102, 1120-1124`; `ShareTask.java:118-127`); `SmbSearchDialog$ListViewAdapter`. Bind-time listeners are lambdas in `onBindViewHolder` (`RecyclerAdapter.java:491-828`) |
| AdapterView adapters | `AppsAdapter` (ArrayAdapter in a ListFragment); `ColorAdapter` (GridView, `ColorPref.java:131-168`); framework ArrayAdapter in DatabaseViewerActivity (`:179-187`) |
| ViewPager | `TabFragment.ScreenSlidePagerAdapter` (`FragmentStatePagerAdapter`, `:319-345`); `onPageScrolled`/`onPageSelected` (`:279-316`); `DisablableViewPager`; `Indicator` |
| Glide | `AmazeFileManagerModule` (AppGlideModule, registers `ApkImageModelLoaderFactory` and `CloudIconModelFactory`, `AmazeFileManagerModule.java:17-23`); generated `GlideApp`, `GlideRequest(s)`, `GlideOptions`, `GeneratedAppGlideModuleImpl` (found by Glide reflection: FW-MEMORY); RecyclerView preloaders `RecyclerPreload*`, `AppsAdapterPreloadModel` |
| Loaders | `AppListLoader` (AsyncTaskLoader + `PackageReceiver`, `AppsListFragment.java:108, 162-185`); a `CursorLoader` on the cloud plugin's provider `content://com.amaze.cloud.provider/keys.db/secret_keys` (`MainActivity.java:1832-1929`) |
| AsyncTask | `LoadFilesListTask`, `SearchAsyncTask`, `PrepareCopyTask`, `MoveFiles`, `DeleteTask`, `CountItemsOrAndSizeTask`, `GenerateHashesTask`, `LoadFolderSpaceDataTask`, `ReadFileTask`, `WriteFileAbstraction`, `SearchTextTask`, `DbViewerTask`, `CloudLoaderAsyncTask`, `ShareTask`, 9 `*HelperTask`s, ssh tasks, the service workers (`CopyService$DoInBackground`, `ZipService$CompressAsyncTask`, `ExtractService$DoWork`, `Encrypt/DecryptService$BackgroundTask`), `FileUtils$3`, `MainFragment$6`, `AppConfig.runInParallel` (`AppConfig.java:110-133`) |
| Handler / threads / timers | `AppConfig.runInBackground` HandlerThread; MainActivity root-shell HandlerThread (`:592-611`); `ServiceWatcherUtil` HandlerThreads (`:58-66, 188-230`); `FileHandler` (Handler for FileObserver messages); raw Threads in `DatabaseViewerActivity.load` (`:157`), `MainFragment.launchSMB` (`:1658`), `HiddenAdapter` (`:102`), `SshClientUtils` (`:240`), `CloudUtil` (`:137`), `SubnetScanner` (60-thread pool, `:80, 143`), streamers; properties dialog executor (`GeneralDialogCreation.java:374`); `CountDownTimer` in `BottomBar` (`:113-121`) and `FileUtils` (`:769-790`); `Timer` in `TextEditorActivity.onTextChanged` (`:422-443`) |
| FileObserver | `CustomFileObserver` (started in `MainFragment.startFileObserver`, `:1177-1202`; polling variant only on API 23, `CustomFileObserver.java:64-82`) |
| Services | 5 foreground progressive services (`AbstractProgressiveService` base; `ServiceWatcherUtil` progress watcher; `ObtainableServiceBinder` for binding); `FtpService` (foreground; `onTaskRemoved` schedules a restart with **AlarmManager**, `FtpService.java:254-265`); `FtpTileService`. No JobScheduler or WorkManager |
| Broadcast receivers | manifest: `FtpReceiver`. Dynamic: `MainActivityHelper.mNotificationReceiver` (MEDIA_MOUNTED/UNMOUNTED, `MainActivity.java:1114-1119`); `MainActivity.receiver2` (`general_communications`, `:1120`); `mOtgReceiver` (USB attach/detach, `:1160-1165`); `MainFragment.receiver2` (`loadlist`, `:1421`); `decryptReceiver` (`:1427`); service cancel receivers (`CopyService.java:100`, `ZipService.java:86`, `ExtractService.java:92`, `EncryptService.java:68`, `DecryptService.java:69`); `FtpServerFragment.mWifiReceiver` (`:392`); `PackageReceiver` (`:29-34`) |
| EventBus (greenrobot) | `FtpService` posts `FtpReceiverActions` (`:227-248`); `@Subscribe` in `FtpServerFragment.onFtpReceiveActions` (`:342-372`) and `FtpTileService` (`:26-29`) |
| Content providers | own FileProvider (share, open); MediaStore queries (`LoadFilesListTask.java:257-447`, `FileUtils.fileToContentUri` `:517-586`, `MediaStoreHack`); the external cloud-plugin provider |
| Database layer | SQLiteOpenHelpers `UtilsHandler` (`utilities.db`, `:40-41`), `TabHandler`/`SortHandler`/`CryptHandler`/`CloudHandler` (`explorer.db`, `TabHandler.java:40-41`); cached in the `DataUtils` singleton with `DataChangeListener` callbacks into MainActivity (`:1731-1769`) |
| WebView | `DbViewerFragment` + `DbViewerTask` (`loadData` HTML, `DbViewerTask.java:96`); no JS bridge |
| SAF and pickers | OPEN_DOCUMENT_TREE request 3 (SD write, `MainActivityHelper.java:255-258` → `MainActivity.onActivityResult` `:1310-1398`); REQUEST_CODE_SAF 223 (OTG, `Drawer.java:584-588` → `:1399-1410`); OPEN_DOCUMENT image 31 (drawer header); GET_CONTENT PEM (`SftpConnectDialog.java:141-147`, `onActivityResult` L304); `DocumentFile` for OTG (`OTGUtil`) |
| Notifications | progress notifications with custom RemoteViews, a content intent to MainActivity and a Cancel PendingIntent broadcast (`CopyService.java:118-149` and similar); failed-ops notification (`AbstractProgressiveService.java:232-259`); FTP notification with Stop (`FtpNotification.java:27-60`); channels in `NotificationConstants` |
| Other | pinned shortcuts (`ShortcutManagerCompat`); Quick Settings tile; Volley `ImageLoader` for the drawer header (`AppConfig.java:217-226`, `Drawer.java:652-671`); libsuperuser root shell (`RootHelper`, `RootUtils`); local HTTP streamers (`utils/SmbStreamer/StreamServer`, `utils/cloud/CloudStreamServer`); FingerprintManager (`FingerprintHandler`); `MediaScannerConnection` (`MainFragment.java:776-825`); MPAndroidChart (properties pie, process line chart); Palette (About); clipboard. **No** LiveData, ViewModel, RxJava, data binding, WorkManager, JobScheduler, JS bridge or app widgets (grep counts 0) |

## 5. Unreachable-code candidates (evidence only; verdicts left to the graph build)

**Classes with no reference in compiled sources or resources** (comments stripped):

| Class | Evidence |
|---|---|
| `fragments/PropertiesSheet` | 8 methods; only referenced inside a comment in `ItemPopupMenu.java:70-78` |
| `ui/views/ScrimInsetsRelativeLayout` | 9; no layout uses it |
| `adapters/holders/DonationViewHolder` | 1; used only by the play-flavor `Billing.java`, which is not compiled |
| `utils/test/DummyFileGenerator` | 2; `@VisibleForTesting` helper in the main source set |
| `Z/CLI` (+`$Mode*`) | 12; command-line `main` (`CLI.java:116`) |
| `Z/SevenZOutputFile` (+inner) | 44; writer, mentioned only in a comment (`SevenZFile.java:92`) |
| Glide-generated API surface | `GlideOptions` 68/73 unhit, `GlideRequest` 50/63, `GlideRequests` 16/21, `GlideApp` 11/12. These are generated overrides: some may be called by Glide internals (FW-MEMORY), the rest have no caller |

**Methods with no call site** (heuristic scan of all compiled sources, then checked by grep):
- `MainActivity.getFAB` (`:1294`), `getPaste` (`:1558`)
- `TabFragment.parsePathForName` (`:243`) and `parseSmbPath` (`:238`, called only from it)
- `FtpNotification.removeNotification` (`:94`, private)
- `Utils.isDeviceInLandScape` (`:183`; its only call is commented out at `Drawer.java:161`); `Drawer.setNavViewDimension` (`:243`, call commented out)
- `DataUtils.containsAccounts(OpenMode)` (`:118`), `setAccounts` (`:328`)
- `MainActivityHelper.isNewDirectoryRecursive` (`:644`), `ScreenUtils.getScreeHeightInDb` (`:41`), `SubnetScanner.getResults` (`:197`)
- `CloudStreamServer.encodeUri` (`:866`), `RandomAccessStream.availableExact` (`:37`; only commented calls)
- `Operations.isFileSystemFAT` (`:549`), `FileUtil.getTempFile` (`:476`), `FileUtil.copyDummyFiles` (`:971`), `RootHelper.runNonRootShellCommand` (`:93`), `RootUtils.getFilePermissions` (`:169`), `MimeTypes.mimeTypeMatch` (`:173`)
- `PrepareCopyTask$CopyNode.getFilesToCopy` / `getConflictingFiles`
- 7z library getters and setters (`SevenZArchiveEntry.get/setCrc`, `get/setCompressedCrc`, `SevenZFile.getStatisticsForCurrentEntry`)

**Branches that cannot run inside reachable methods:**
- `MainFragment.mActionModeCallback.onActionItemClicked`: the cases `R.id.about` (`:652`) and `R.id.rename` (`:701`) have no item in `R/menu/contextual.xml` (which lists openmulti, cpy, delete, openparent, cut, all, share, compress, openwith, hide, addshortcut, ex).
- `LoadFilesListTask.listDocs`: `Arrays.asList(types).contains(path)` compares a full path with extensions (`:346`), so the inner block and the sort lambda (`lambda$listDocs$5`) never run. Documents is always empty.
- `ServiceWatcherUtil.runService`: case 0 starts the service without queueing (`:163-166`), so `pendingIntents` never grows. `postWaiting` (`:188-230`) and `ServiceWatcherUtil$2` are dead.
- `CustomFileObserver.stopWatching` calls `super.startWatching()` on non-API-23 devices (`:73-82`): a quirk, not dead code.

**API-gated on the API 27 baseline** (unreachable there):
- pre-Lollipop circle indicators `TabFragment.updateIndicator` (`:380`) and `ColorCircleDrawable`;
- KitKat/JB branches: `SystemBarTintManager` at `MainActivity.java:1449, 1487`, `PreferencesActivity.java:203`, `DatabaseViewerActivity.java:111`; many `SDK_INT == KITKAT` branches in `FileUtil`, `GenericCopyUtil` and `Operations`;
- `Drawer.java:143-147` (pre-KitKat GET_CONTENT);
- API-23-only polling `CustomFileObserver.startPollingSystem` / `FileTimerTask`.

API-gated but available on 27: the QS tile (24+), fingerprint (23+), install-permission check (26+).

**Flavor, debug and build config:** play sources (`Billing`, play `AboutActivity`) are not compiled. `BuildConfig.IS_VERSION_FDROID` is never read. `BuildConfig.DEBUG` guards a duplicate-id check (`Drawer.java:461, 480`). The LeakCanary install is commented out. 7z `BuildConfig` has 2 methods.

**Framework-only candidates** (callbacks the framework may never call in practice):
- `MainActivity.onConfigurationChanged` (`:1067-1071`) and its only callee `Drawer.onConfigurationChanged`: no `configChanges` is declared, so rotation recreates the activity instead (FW-MEMORY). 0 hits.
- `AppConfig.onTerminate` (`:89-93`; FW-MEMORY: never called on devices).
- `RecyclerAdapter.onFailedToRecycleView`.
- `MainActivity.onLoaderReset` (empty; needs the cloud plugin).
- `AbstractProgressiveService.progressResumed` (needs a stalled-then-resumed transfer).

`onServiceDisconnected` in `CompressedExplorerFragment` (`:388-401`, opens a file extracted from an archive) and in `ProcessViewerFragment` should be reachable: FW-MEMORY says `ActiveServices.bringDownServiceLocked` notifies bound clients when the service stops. Verify on a device.

**Environment-gated:** root (`RootUtils`, root branches), SMB (`StreamServer`, `Streamer`, `StreamSource`, `SmbUtil`), SFTP (ssh package and tasks), cloud (`utils/cloud`, `CloudLoaderAsyncTask`, `CloudIconDataFetcher`), FTP (Wi-Fi), OTG (`OTGUtil`, `UsbOtgRepresentation`, `SingletonUsbOtg.set*`), fingerprint, external SD card + SAF (`FileUtil.isWritableNormalOrSaf`, the LEXA dialog), launcher pin support, other apps (open with, share, market, email).

**Hazards noticed** (not reproduced):
- DatabaseViewerActivity crashes on an external VIEW `db/*` intent (`:128-129`).
- Any external VIEW intent without type `resource/folder` is treated as an archive (`MainActivity.java:522-526`).
- `FtpReceiver.startService` from the background on targetSdk 28: background-start limits apply (FW-MEMORY). The exception is caught (`FtpReceiver.java:19-30`), so the tile may silently fail when the app is not in the foreground (UNVERIFIED).

## 6. Decomposition into parallel areas

**Rule for overlap:**
- An edge belongs to the area that owns its `src`: GUI edges belong to the page owner, CALL/ASYNC/FRAMEWORK edges to the owner of the source method.
- Every top-level class (with all its inner, anonymous and lambda members) belongs to exactly one area.
- Counts are JaCoCo methods.

| Area | Owns (packages / classes) | Methods | Pages owned | Entry edges from other areas |
|---|---|---|---|---|
| **A1 Shell & infrastructure** | `MainActivity` (89), `activities/superclasses/*`, `TabFragment`, `ui/views/**` except `preference` and the color pickers (`appbar` AppBar/BottomBar/SearchView, `drawer`, FastScroller, Indicator, Warnable*, Themed*, RoundedImageView, Divider, DisablableViewPager, CircleGradientDrawable, ScrimInsetsRelativeLayout), `ui/dialogs/RenameBookmark`, `ui/ColorCircleDrawable`, `ui/colors/{ColorPreferenceHelper,ColorUtils,UserColorPreferences}`, `database/{UtilsHandler,TabHandler,SortHandler}` + models `OperationData,Sort,Tab`, `utils/{DataUtils,Utils,OpenMode,PreferenceUtils,TinyDB,ScreenUtils,AnimUtils,BookSorter,SimpleTextWatcher,EditTextColorStateUtil,LruBitmapCache,GlideConstants}`, `utils/application/*`, `utils/provider/UtilitiesProvider`, `utils/theme/*`, `asynchronous/asynctasks/AsyncTaskResult`, Glide infra (`AmazeFileManagerModule`, `adapters/glide/apkimage/*`, `utils/glide/*`, generated `GlideApp/GlideOptions/GlideRequest/GlideRequests`, `com/bumptech/glide/Generated*`), root `BuildConfig`, `Manifest` | 852 (177 generated, 4 BuildConfig/Manifest) | 19: entry/exit/system pseudo pages, drawer, FAB, search bar, path bar, sort submenu, dir sort, set home, rename bookmark, OTG SAF, permission rationales, save mode | from A6: `PreferencesActivity` Back → MainActivity intent; from A3/A4/A5: services' content and failed-ops intents → `onNewIntent`/`receiver2`; `SmbConnectDialog` → `MainActivity.addConnection` (`:1679`); `RenameBookmark` → `modify`/`delete` callbacks (`:1757-1769`) |
| **A2 File list & dialog hub** | `MainFragment` (85), `SearchWorkerFragment`, `PropertiesSheet`, `adapters/{RecyclerAdapter,HiddenAdapter}`, `adapters/data/{LayoutElementParcelable,IconDataParcelable}`, `adapters/glide/RecyclerPreload*`, `adapters/holders/{Item,Special,Empty,Hidden,Donation}ViewHolder`, `asynchronous/asynctasks/{LoadFilesListTask,SearchAsyncTask}`, `asynchronous/handlers/FileHandler`, `filesystem/CustomFileObserver`, `ui/ItemPopupMenu`, `ui/dialogs/GeneralDialogCreation` (80), `ui/icons/*`, `utils/files/FileListSorter` | 353 | 28: all `S_MAIN_*` list pages except remote/root/OTG/save, item popup, the `GeneralDialogCreation` dialogs | A1: `TabFragment.addTab` creates MainFragment (`:351-367`); `onOptionsItemSelected` → `home`, `switchView`, `updateList`, `showHistoryDialog`, `showSortDialog`, `showHiddenDialog` (`:937-1024`); `Drawer.onDrawerClosed` → `loadlist`; A3: `Operations` callbacks / `KEY_INTENT_LOAD_LIST` broadcast → `updateList`; `MainActivityHelper.search` → `addSearchFragment`; A6: `TextEditorActivity` Details → `showPropertiesDialogWithoutPermissions`; MainActivity sort with Apps → `showSortDialog(AppsListFragment)` |
| **A3 File operations, filesystem & services** | `filesystem/{HybridFile,HybridFileParcelable,Operations,FileUtil,RootHelper,PasteHelper,MediaStoreHack}`, `filesystem/usb/*`, `utils/files/*` except FileListSorter (`FileUtils`, `GenericCopyUtil`, `CryptUtil`, `EncryptDecryptUtils`), `utils/{MainActivityHelper,ServiceWatcherUtil,ProgressHandler,DatapointParcelable,ObtainableServiceBinder,FingerprintHandler,RootUtils,OTGUtil}`, `utils/share/*`, `utils/test/*`, `asynchronous/asynctasks/{DeleteTask,PrepareCopyTask,MoveFiles,CountItemsOrAndSizeTask,GenerateHashesTask,LoadFolderSpaceDataTask}`, `asynchronous/services/{AbstractProgressiveService,CopyService,EncryptService,DecryptService}`, `fragments/ProcessViewerFragment`, `ui/notifications/NotificationConstants`, `database/CryptHandler`, `database/models/EncryptedEntry`, `exceptions/ShellNotRunningException` | 649 | 12: new folder/file, SAF guide, failed ops, copy conflict, share, open-as, process viewer, progress and failed notifications, root and OTG lists | A1: FAB → `mkdir`/`mkfile`; paste → `PrepareCopyTask` (`:1025-1033`); `onActivityResult` SAF replays (`:1332-1398`); A2: popup and action mode → `PasteHelper`, `rename`, `deleteFilesDialog` → `deleteFiles`, `FileUtils.openFile`/`openWith`/`shareFiles`, `EncryptDecryptUtils`; A5: `HybridFile` SMB/SFTP methods call A5 helpers |
| **A4 Archives** | `fragments/CompressedExplorerFragment`, `adapters/CompressedExplorerAdapter`, `adapters/data/CompressedObjectParcelable`, `adapters/holders/CompressedItemViewHolder`, `filesystem/compressed/**`, `asynchronous/asynctasks/compress/*`, `asynchronous/services/{ExtractService,ZipService}`, the whole `commons_compress_7z` module (254) | 486 | 3: archive list, archive select, archive password | A1: `openCompressed` (`:1240`) from A2's archive/package dialogs and VIEW intents; `onOptionsItemSelected` extract (`:1034-1039`); `onBackPressed` (`:719-737`); A3: `MainActivityHelper.extractFile` (`:522-531`) / `compressFiles` (`:375-388`) → `Decompressor.decompress` / ZipService; A2: popup/action-mode Extract |
| **A5 Network & remote** | `ui/dialogs/{SmbSearchDialog,SmbConnectDialog,SftpConnectDialog}`, `utils/{SubnetScanner,ComputerParcelable,SmbUtil,OneCharacterCharSequence}`, `utils/SmbStreamer/*`, `utils/streams/*`, `exceptions/{StreamNotFoundException,CloudPluginException}`, `filesystem/ssh/*`, `asynchronous/asynctasks/ssh/*`, `fragments/{FtpServerFragment,CloudSheetFragment}`, `asynchronous/services/ftp/*`, `ui/notifications/FtpNotification`, `asynchronous/asynctasks/CloudLoaderAsyncTask`, `utils/cloud/*`, `database/{CloudHandler,CloudContract}`, `database/models/CloudEntry` | 382 | 20: cloud sheet, SMB/SFTP dialogs, remote lists, FTP pages and dialogs, FTP notification, QS tile | A1: FAB cloud (`:1952`); drawer FTP row; drawer server icons → `showSMBDialog`/`showSftpDialog` (`:1622-1669`); `CustomSshJConfig.init` in `onCreate`; cloud loader (`:1902-1924`); A2: `onListItemClicked` → `launchSMB`, `SshClientUtils.launchSftp`, `CloudUtil.launchCloud` (`:913-936`); A3: `HybridFile` and `LoadFilesListTask` SMB/SFTP branches |
| **A6 Secondary screens** | `activities/{PreferencesActivity,TextEditorActivity,DatabaseViewerActivity}`, F/`AboutActivity`, `fragments/preference_fragments/*` (incl. `PreferencesConstants`), `ui/views/preference/*`, `ui/dialogs/ColorPickerDialog`, `adapters/ColorAdapter`, `ui/views/{CircularColorsView,CheckableCircleView}`, `ui/colors/ColorPreference`, `asynchronous/asynctasks/{ReadFileTask,WriteFileAbstraction,SearchTextTask,DbViewerTask}`, `utils/{MapEntry,ImmutableEntry,InterestingConfigChange}`, `filesystem/EditableFileAbstraction`, `fragments/{AppsListFragment,DbViewerFragment}`, `adapters/{AppsAdapter}`, `adapters/data/AppDataParcelable`, `adapters/holders/AppHolder`, `adapters/glide/AppsAdapterPreloadModel`, `asynchronous/loaders/*`, `utils/broadcast_receiver/*` | 260 | 33: settings, about, editor, DB viewer, app manager, their dialogs and paused pages | A1: drawer Apps and Settings rows; A3: `FileUtils.openFile`/`openWith`/`openunknown` → DatabaseViewerActivity (explicit) and TextEditorActivity (implicit VIEW); manifest entries |

- **Shared infrastructure.** A1 owns the base activities, Application, `UtilitiesProvider`/theme, `DataUtils`, `UtilsHandler`/`TabHandler`/`SortHandler`, the generic views and Glide. A3 owns the filesystem layer and the progressive-service framework that A4's `ExtractService` and `ZipService` extend. `PreferencesConstants` (1 method) sits in A6 but is read everywhere.
- **Leftovers** (classes placed by the catch-all rule rather than a feature rule; all in A1): the generated Glide classes, root `BuildConfig` and `Manifest`, `AsyncTaskResult`, `GlideConstants`, `LruBitmapCache`, `EditTextColorStateUtil`, `ScrimInsetsRelativeLayout`. JacocoInstrument (3 classes) is excluded. No class is unassigned: the script assigned all 2982 methods.

## 7. Baseline coverage by area and screen

| Area | Methods | Monkey only | APE only | Both | Neither | Union |
|---|---|---|---|---|---|---|
| A1 Shell | 852 | 2 | 65 | 441 | 344 (145 are generated Glide) | 508 (59.6%) |
| A2 File list | 353 | 2 | 59 | 161 | 131 | 222 (62.9%) |
| A3 File ops | 649 | 0 | 197 | 76 | 376 | 273 (42.1%) |
| A4 Archives | 486 | 0 | 20 | 11 | 455 | 31 (6.4%) |
| A5 Network | 382 | 5 | 22 | 35 | 320 | 62 (16.2%) |
| A6 Secondary | 260 | 0 | 9 | 28 | 223 | 37 (14.2%) |
| **Total** | 2982 | 9 | 372 | 752 | 1849 | 1133 (38.0%) |

Monkey-only methods (9): `LoadFilesListTask.listVideos`, `MainFragment.changePath`, `BottomBar.lambda$showButtons$1/2` (breadcrumb taps), `SftpConnectDialog.<init>/onCreate/onCreateDialog/$1.<init>`, `SmbSearchDialog$1.searchFinished`.

Never reached, by area, with the likely reason:

- **A1.** Zero-hit classes: `ScrimInsetsRelativeLayout`, `ColorCircleDrawable` (pre-L), the Glide data fetchers for APK and cloud icons, `Sort`.
  - Settings/FTP/Apps rows: `Drawer.java:597` never executed (section 2.4).
  - Save mode (`initFabToSave` 0) and picker mode (`returnIntentResults` 0): no external intents were sent.
  - The OTG drawer path: no device.
  - The storage permission flow: pre-granted.
- **A2.**
  - Search results: no `IME_ACTION_SEARCH` with text.
  - ".." row (`goBackItemClick` 0): pref off.
  - Package dialog: no `.apk`.
  - Archive dialog buttons: never pressed.
  - Change-path dialog: pref off.
  - Decrypt dialogs: no `.aze` file.
  - Properties permission table: root.
  - `PropertiesSheet`: dead.
- **A3.**
  - Process viewer: notification or intent only.
  - Encrypt/decrypt services and `CryptUtil`: password input.
  - `RootUtils`: root.
  - `MediaStoreHack`: only on KitKat SD writes and ringtone results.
  - SAF guide: no external SD.
  - Copy conflict: no clash produced (UNVERIFIED).
  - New folder positive (`lambda$mkdir$0` 0): empty name keeps Create disabled.
  - APE did copy, move, delete, compress and share (APE-only 197).
- **A4.**
  - Archive viewer and extraction: dialog buttons never pressed; no non-zip archives.
  - The 7z module (254): no `.7z` file.
  - `ArchivePasswordCache`: no protected archive.
  - Only `CompressedHelper` (11, both runs) and ZipService (APE, via Compress) ran.
- **A5.**
  - FTP pages and service: drawer row never selected; QS tile is system UI.
  - SSH/SFTP: no server; Monkey only opened the connect dialog.
  - SMB browse/stream: no server (APE saved a connection that cannot list).
  - Cloud: plugin missing (`isCloudProviderAvailable` false).
- **A6.**
  - Settings, About, App manager: drawer rows.
  - DB table view: no SQLite fixture.
  - Editor save/unsaved buttons and find navigation: buttons not pressed or text not typed. The find bar was opened by APE (`revealSearchView` A, `onClick` A), but `hideSearchView` was never hit.

## Conclusions and recommendations

1. **Model `MainActivity` as a multi-mode hub.** Use variants keyed by the fragment at `content_frame` for `onPrepareOptionsMenu`, `onOptionsItemSelected` and `onBackPressed` (`MainActivity.java:703-1044`). Use list vs grid variants for the `RecyclerAdapter` lambdas.
2. **Use the JaCoCo XML as the method list**, since `javap` is unavailable. Mark the generated Glide surface (145 unhit methods) separately, so it does not swamp the DEAD or target counts.
3. **The best tool targets are cheap to reach but were missed:** the Settings tree plus About (≈140 methods), App manager, FTP UI, archive View/Extract, search, New folder, editor save, and encrypt with typed passwords. All of these need either one scroll in the drawer or typed text. No environment setup is required.
4. **Mark these as REACHABLE_AFTER_SETUP, not DEAD:** SMB, SFTP, cloud, root, OTG, fingerprint and the process viewer. Record the setup in `env`.
5. **Verify on a device before freezing verdicts:** the `onServiceDisconnected` paths, `onConfigurationChanged` (no `configChanges`), the singleInstance + `onNewIntent` paths, and the background-start behaviour of the FTP receiver and tile.
6. **Harness improvements for the next baseline:** reset app data before each run; push the richer fixtures in 2.5; allow DocumentsUI and SystemUI, or script the notification and SAF steps; optionally pre-set the preferences in 2.2.
