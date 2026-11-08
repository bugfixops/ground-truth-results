# Aegis v3.4.2 (`com.beemdevelopment.aegis.debug`): UI map and modeling plan

Read-only investigation that prepares the method-level trigger graph. Nothing in the dataset was modified; all scripts only read files (the APK, class files, JaCoCo XML and `.ec` segments were parsed in memory).

## Summary

- **Entry points**: 14 app activities (2 without UI) plus 1 merged library activity, 2 exported quick-settings tile services, 2 non-exported receivers (+ the exported JaCoCo harness receiver), a FileProvider and a backup agent. External triggers: launcher → `MainActivity`; `otpauth://` VIEW deep link; SEND / SEND_MULTIPLE of `image/*` or `text/plain`; a dynamic launcher shortcut (`action=scan`); two QS tiles; a Guardian-Project panic intent (signer-checked). No widgets, search, notifications (disabled, issue #1047), WorkManager or RxJava.
- **Why the baseline stalled**: a fresh install starts in a 4-slide intro that must create the vault. Both tools finished it once, each time with security **None**, and **never created a single entry**. With an empty vault the entry list is hidden, so the entry/selection/edit/transfer/OTP side never ran: 0 of 106 `otp` + `crypto/otp` methods, 0/71 `EditEntryActivity`, 0/42 `EntryHolder`, 0/27 `AuthActivity` (the vault was never encrypted).
- **APE lost its vault** at t≈3.1 min (a restart with the exact fresh-install coverage signature, so app data was cleared, INFERRED) and then looped in the intro for the remaining ~57 min. Monkey stayed in one process, reached the main screen at t≈5.6 min and then explored Settings/About.
- **Out-of-package screens** (DocumentsUI, gallery chooser, browser, date settings) are blocked for `monkey -p`/APE (FW-MEMORY), so every file import/export/icon-pack/backup-location path only received `RESULT_CANCELED`.
- **Harness**: the APK is `debuggable`, so `run-as` can seed `files/aegis.json`. A plaintext vault with entries (`app/src/androidTest/resources/.../aegis_plain.json` or the grouped `app/src/test/resources/.../vault/aegis_plain_grouped_v2.json`) skips the intro entirely, because `isVaultInitNeeded()` only checks that file. Add an encrypted variant (password `test`), importer samples from the unit-test resources, QR-code images (none in `_fixtures`), an icon-pack ZIP (none available), camera permission and an enrolled emulator fingerprint.
- **Model proposal**: 114 candidate pages (incl. 12 paused and 6 outside-the-app pseudo pages) and 6 areas: CORE 1020 methods (327 generated), SECURITY 324, MAIN 477, EDIT/ICONS 522 (196 generated), SETTINGS 190, IMPORT/EXPORT 424.
- **Data caveats**: `RootShellTask`, `RawSlot` and `BuildConfig` are not instrumented in the APK (no `$jacocoInit`), so they can never show as hit, although `RootShellTask` demonstrably ran in Monkey; JaCoCo filters 145 methods that `tools/list_methods.py` keeps; the 30-s coverage broadcast itself starts the process.

## 0. Sources, abbreviations, evidence labels

| Abbreviation | Path |
|---|---|
| `APP/` | `/Users/darshan/Desktop/yang/work/final_java_only/Aegis/app/Aegis-#v3.4.2/app/` |
| `SRC/` | `APP/src/main/java/com/beemdevelopment/aegis/` |
| `RES/` | `APP/src/main/res/` |
| `MAN` | `APP/src/main/AndroidManifest.xml` |
| `APKMAN` | binary `AndroidManifest.xml` inside `Aegis-#v3.4.2-rebuilt.apk`, decoded in memory (this **is** the merged manifest; no merged manifest exists under `APP/build/intermediates`, which only holds `classes/`) |
| `CLS/` | `APP/build/intermediates/classes/debug/transformDebugClassesWithAsm/dirs/` (the only class dir in `class_files.json`) |
| `JM`, `JA` | `final_java_only/Aegis/monkey/report/report.xml`, `.../ape/report/report.xml` |
| `SEG-M/n`, `SEG-A/n` | `final_java_only/Aegis/{monkey,ape}/coverage/0000n.ec/.json` (120 segments each, ~30 s apart, dumped with reset, so each segment is incremental: `SRC/JacocoInstrument/JacocoInstrumentation.java:56-62`) |
| `TEST/`, `ATEST/` | `APP/src/test/`, `APP/src/androidTest/` (not in the APK) |

Evidence labels: `SRC` = read in app source/resources (file:line); `BYTECODE` = class-file constant-pool scan of `CLS/` (references/annotations/superclasses); `DATA` = JaCoCo XML or `.ec` segments; `FW-MEMORY` = Android/tool behaviour recalled, not checked; `INFERRED`; `UNVERIFIED`.

Read completely: manifest, all activities, all fragments, slides/intro, `Dialogs`, `IconPickerDialog`, `SimpleWebViewDialog`, `EntryListView`, `EntryAdapter`, `EntryHolder`, `IconAdapter`, `DropdownCheckBoxes`, `SwitchPreference`, `NoAutofillEditText`, `VaultManager`, start of `VaultRepository`/`VaultBackupManager`/`IconPackManager`, `DatabaseImporter`, `AuditLogRepository`, `AppDatabase`, `AegisModule`, `AegisApplicationBase`, `AegisBackupAgent`, receivers, services, tasks `ProgressDialogTask`/`RootShellTask`, helpers used by the UI, the JaCoCo harness, all menus and preference XML. Scanned only (grep/bytecode): the 24 importer files, `otp/*`, `crypto/*`, the rest of `vault/*`, `util/*`, `TextDrawable`, `info.guardianproject.*`, the other task classes, remaining view holders/adapters and layouts.

## 1. Entry points

All components from `APKMAN` (merged), cross-checked with `MAN`. Activities without an intent filter are not exported (FW-MEMORY: default for `targetSdk` 35). App theme `Theme.Aegis.Launch` (`MAN:33`) is replaced at runtime by `ThemeHelper` in every `AegisActivity` (`SRC/ui/AegisActivity.java:61-68,116-118`) and in `LicensesActivity` (`SRC/ui/LicensesActivity.java:29-31`); no activity uses a dialog theme.

| Component | Kind | Exported | Filters / trigger | Flags | Evidence |
|---|---|---|---|---|---|
| `AegisApplication` (`@HiltAndroidApp`, superclass `Hilt_AegisApplication` → `AegisApplicationBase`) | Application | – | any process start (also the coverage broadcast) | `debuggable=true`, `allowBackup`, `fullBackupOnly`, `backupAgent=.AegisBackupAgent`, `appComponentFactory=CoreComponentFactory` | `MAN:21-34`; APKMAN; BYTECODE superclass |
| `ui.MainActivity` | activity | **true** | MAIN/LAUNCHER; VIEW + DEFAULT + BROWSABLE, scheme `otpauth`; SEND + SEND_MULTIPLE + DEFAULT, mime `image/*` and `text/plain` | label `${title}` = `AegisDev` (debug placeholder) | `MAN:43-67`; `APP/build.gradle` debug `manifestPlaceholders` |
| `ui.PanicResponderActivity` | activity, no UI | **true** | `info.guardianproject.panic.action.TRIGGER` + DEFAULT | `singleInstance`, `noHistory`, `@android:style/Theme.NoDisplay` | `MAN:91-101` |
| `ui.ScannerActivity` | activity | false | internal | portrait; `configChanges=keyboardHidden/orientation/screenSize` | `MAN:68-72` |
| `ui.IntroActivity` | activity | false | internal | portrait | `MAN:76-78` |
| `ui.TransferEntriesActivity`, `AboutActivity`, `ImportEntriesActivity`, `EditEntryActivity`, `AuthActivity`, `PreferencesActivity`, `GroupManagerActivity`, `AssignIconsActivity`, `LicensesActivity`, `ExitActivity` | activities | false | internal intents only | defaults; `ExitActivity` extends plain `Activity` (no Hilt, no theme helper) | `MAN:35-42,73-90,102`; BYTECODE |
| `com.mikepenz.aboutlibraries.ui.LibsActivity` | activity (library, merged) | false | never started directly; `LicensesActivity` extends it | – | APKMAN; BYTECODE |
| `services.LaunchAppTileService`, `services.LaunchScannerTileService` | `TileService` | **true**, permission `BIND_QUICK_SETTINGS_TILE` | `android.service.quicksettings.action.QS_TILE`, `ACTIVE_TILE=true` | bound by SystemUI | `MAN:108-132` |
| `services.NotificationService` | service | **not declared** (commented out, issue #1047) | – | – | `MAN:104-106` |
| `receivers.VaultLockReceiver` (Hilt) | receiver | false | `com.beemdevelopment.aegis.debug.LOCK_VAULT`; also registered dynamically for `SCREEN_OFF` | – | `MAN:134-138`; APKMAN; `SRC/AegisApplicationBase.java:50-51` |
| `receivers.QsTileRefreshReceiver` | receiver | false | `BOOT_COMPLETED`, `USER_UNLOCKED` | – | `MAN:140-147` |
| `JacocoInstrument.SMSInstrumentedReceiver` | receiver (harness, out of scope) | true | `edu.gatech.m3.emma.COLLECT_COVERAGE` | – | `MAN:161-166` |
| `androidx.core.content.FileProvider` | provider | false, grants URI permissions | authority `com.beemdevelopment.aegis.debug.fileprovider` | – | `MAN:149-158`; APKMAN |
| `androidx.startup.InitializationProvider` | provider (library) | false | EmojiCompat, ProcessLifecycle, ProfileInstaller initializers | – | APKMAN |
| `androidx.room.MultiInstanceInvalidationService`; `androidx.camera.core.impl.MetadataHolderService` (`enabled=false`); `androidx.profileinstaller.ProfileInstallReceiver` (exported, permission `DUMP`) | library components | see left | – | – | APKMAN |
| Dynamic shortcut `shortcut_new` | `ShortcutManager` | – | long-press the launcher icon → `MainActivity`, action MAIN, extra `action=scan`, NEW_TASK + CLEAR_TASK | API ≥ 25 | `SRC/AegisApplicationBase.java:59-61,70-89`; consumed by `SRC/ui/MainActivity.java:837-851` |
| `AegisBackupAgent` | `BackupAgent` | – | Android backup/restore (bmgr, cloud, device-to-device) | `fullBackupOnly` | `MAN:23-27`; `SRC/AegisBackupAgent.java:33-128` |

Permissions: `CAMERA`, `USE_BIOMETRIC`, `VIBRATE`, `RECEIVE_BOOT_COMPLETED` (`MAN:5-8`), merged `USE_FINGERPRINT` and `…DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION` (APKMAN); `POST_NOTIFICATIONS` is commented out (`MAN:10-12`). `<queries>` lists the 10 authenticator packages used by "Import from app" (`MAN:169-180`). No static shortcuts, no app widgets, no searchable, no file-type VIEW filters.

How each external intent is consumed (all only when the vault is loaded): VIEW `otpauth://` → `GoogleAuthInfo.parseUri` → `EditEntryActivity` (prefilled) or an error dialog (`SRC/ui/MainActivity.java:853-882`); SEND `EXTRA_STREAM` → QR decode of the image (`884-895`); SEND `EXTRA_TEXT` → parse URI (`896-911`); SEND_MULTIPLE → decode all images (`913-926`); extra `action=scan` → scanner (`837-851`). Tile services: `onStartListening` sets the tile inactive, `onClick` starts `MainActivity` (scanner tile adds `action=scan`) via `startActivityAndCollapse`; the API 34 `PendingIntent` branch is dead on API 27 (`SRC/services/LaunchAppTileService.java:18-43`, `LaunchScannerTileService.java:18-44`). Panic: ignored unless `pref_panic_trigger` is on; with `BuildConfig.TEST == false` the intent must come from a Guardian-Project-signed sender (`TrustedIntents`), then the vault file is deleted, the vault locked and the app exits (`SRC/ui/PanicResponderActivity.java:19-52`).

## 2. First-run flow and setup gates

### 2.1 Gate chain (in the order a new user meets it)

| Gate | What the user must do | Enforcing code |
|---|---|---|
| G0 process start | – | `AegisApplicationBase.onCreate`: early-entry-point `VaultManager`, dynamic `SCREEN_OFF` receiver, `ProcessLifecycleOwner` observer, cache clearing, dynamic shortcut (`SRC/AegisApplicationBase.java:45-67`) |
| G1 vault creation (intro) | no file `files/aegis.json` → intro is forced | `MainActivity.onStart` → `isVaultInitNeeded()` → `startIntroActivity()` (`SRC/ui/MainActivity.java:942-947,603-609`); `isVaultInitNeeded = !isVaultLoaded() && !VaultRepository.fileExists()` (`SRC/vault/VaultManager.java:226-228`, `SRC/vault/VaultRepository.java:52-59`) |
| G1a Welcome slide | Next, or "Import Aegis vault" (ACTION_GET_CONTENT, external picker) | `SRC/ui/slides/WelcomeSlide.java:43-47`; import path `57-109` (`ImportFileTask`, `AegisImporter`, password prompt if encrypted, writes the vault file, sets `imported` → skip to Done: `SRC/ui/IntroActivity.java:57-62`) |
| G1b security picker | choose None / Password (pre-checked) / Biometrics (enabled only if a strong biometric is enrolled) | `RES/layout/fragment_security_picker_slide.xml:55-58`; `SRC/ui/slides/SecurityPickerSlide.java:48-60,73-88`; `SRC/helpers/BiometricsHelper.java:13-29`; None skips the setup slide (`SRC/ui/IntroActivity.java:50-55`) |
| G1c security setup (Password/Biometrics) | type the same non-empty password twice, press Next (scrypt derivation with a progress dialog); biometrics additionally needs a successful BiometricPrompt | `SRC/helpers/EditTextHelper.java:19-23`; `SRC/ui/slides/SecuritySetupSlide.java:109-114,117-147,153-191`; `SRC/ui/intro/IntroBaseActivity.java:80-93` |
| G1d Done | press the check button | `SRC/ui/IntroActivity.java:86-130` (`VaultManager.initNew`, `pref_intro=true`, `RESULT_OK`) → `MainActivity.onIntroResult` → `loadEntries` (`SRC/ui/MainActivity.java:142-148,752-754`) |
| (trap) | Back never leaves the intro: on the first and last slide it does nothing; the pager cannot be swiped | `SRC/ui/intro/IntroBaseActivity.java:39,53,96-101,190-199` |
| G2 unlock (only if encrypted) | type the password (or biometrics) on every cold start and after each lock | plaintext vaults load silently (`SRC/ui/MainActivity.java:951-973`); otherwise `startAuthActivity` (`976-977,1146-1153`) → `AuthActivity` (`SRC/ui/AuthActivity.java:167-178,295-311`); Back = `finishAffinity` (exit, `329-341`); re-lock via menu Lock (`MainActivity.java:1093-1094`), Back with auto-lock (`999-1001,1417-1428`), screen off (`SRC/receivers/VaultLockReceiver.java:24-34`), minimize if enabled (`SRC/AegisApplicationBase.java:105-114`); default auto-lock = Back + device lock (`SRC/Preferences.java:188-195`), effective only for encrypted vaults (`SRC/vault/VaultManager.java:192-196`) |
| G3 content | create or import at least one entry | empty vault → RecyclerView `GONE`, empty-state view shown (`SRC/ui/views/EntryListView.java:539-548`); group chips hidden while no groups (`SRC/ui/MainActivity.java:268`); ways to add: FAB → Enter manually (valid Base32 secret required: `SRC/ui/EditEntryActivity.java:717-834,845-869`), FAB → Scan QR (camera + QR, `MainActivity.java:803-810`), FAB → Scan image (external picker + QR image, `812-824`), deep link/share (`853-930`), Settings → Import & Export |
| G4 feature gates | icon pack installed; encryption on; root + installed source app; biometrics; custom sort; ≥2 entries | Assign-icons item (`MainActivity.java:1270-1273`), icon picker vs. plain image chooser (`EditEntryActivity.java:585-606`), `AssignIconsActivity` throws without packs (`SRC/ui/AssignIconsActivity.java:101`); backups enabled only when encrypted (`SRC/ui/fragments/preferences/BackupsPreferencesFragment.java:196-219`), security items hidden when plain (`SecurityPreferencesFragment.java:258-288`); direct import (`SRC/ui/ImportEntriesActivity.java:143-174`, `SRC/importers/DatabaseImporter.java:64-67`); drag only with custom sort and no filter (`SRC/ui/views/EntryAdapter.java:751-753`) |
| G5 permissions | grant CAMERA once | `SRC/ui/MainActivity.java:803-806,430-441`; `SRC/helpers/PermissionHelper.java:21-36` |

### 2.2 What the baseline did (per-class JaCoCo plus the 30-s segments)

- Both runs start on fresh data with the app already launched: segment 0 of both runs has the same size (57,845 bytes) and its app classes are Application/DI, `Preferences`, Room, `MainActivity`, `EntryListView`, `IntroActivity`, `WelcomeSlide` and the helpers they use; no vault class is loaded yet (DATA `SEG-M/00000`, `SEG-A/00000`).
- Both completed the intro **only with None**: `IntroActivity.java:53-54` (skip to Done) is covered in both; `SecurityPickerSlide.java:77-80` (None and Password branches) covered, `81-82` (Biometrics) missed; `SecuritySetupSlide.deriveKey`, both listeners and `onSaveIntroState` never ran, while `isFinished`/`onNotFinishedError` did, so the two password fields were never equal (DATA JM/JA line counters). Biometrics stayed disabled (`SecurityPickerSlide.java:54,58` missed: no enrolled biometric).
- **Monkey**: one process for the whole hour (Application probes only in segments 0-1); vault created at t≈5.6 min (`SEG-M/00011`); then Settings from t≈6.1, `ImportEntriesActivity` via "Import from app" at t≈16.7 (root check failed: `lambda$startImportApp$5` executed 16 of 50 instructions), About at t≈22.8, Licenses, `GroupManagerActivity` from t≈55.7. It never opened the Backups page, never tapped a FAB menu item (`FabMenuHelper.lambda$setupClickListeners$2` not hit; random taps land on the scrim, which closes the menu) and never confirmed the export dialog.
- **APE**: vault at t≈0.5 min (`SEG-A/00001`); `ScannerActivity` at t≈1.5 (camera bound, frames analysed, no QR: `QrCodeAnalyzer.analyze` hit, `ScannerActivity.onQrCodeDetected` not); CAMERA was already granted (`onRequestPermissionsResult` never ran but the scanner opened; INFERRED `install -g`); a restart that reloaded the plaintext vault at t≈2.0 (`Vault.fromJson`, `VaultManager.loadFrom` APE-only); then at t≈3.1 (`SEG-A/00006`) a restart with the **fresh-install signature** (same probe counts as segment 0: `VaultRepository` 5, `VaultManager` 11, `MainActivity` 82, `EntryListView` 55; intro active). No app code deleted the file (`VaultRepository.deleteFile` is only called by `PanicResponderActivity`, which never ran), so app data was cleared by the tool or harness (INFERRED; mechanism UNVERIFIED). After that ≈25 restarts, each back in the intro, which was never completed again (`Vault` idle after segment 4). `summary_ape_api27.csv` reports 2 app crashes; their cause is UNVERIFIED (no logcat in the dataset).
- Neither tool ever executed `VaultRepository.addEntry`, any `otp/*` or `crypto/otp/*` method, `EntryAdapter.onCreateViewHolder/onBindViewHolder`, `MainActivity.onLongEntryClick` or any `ActionModeCallbacks` method (DATA).

Screens reached / not reached (method counts include inner classes; DATA JM/JA):

| Window | methods | Monkey | APE | Reached? |
|---|---|---|---|---|
| `MainActivity` | 124 | 42 | 49 | yes, empty-vault mode only; search submit APE only |
| `IntroActivity` + `IntroBaseActivity` + 4 slides | 66 | 47 | 47 | yes (None path only) |
| `PreferencesActivity` + `MainPreferencesFragment` | 11 | 11 | 8 | both |
| Appearance / Behavior / Security / Import&Export / AuditLog / IconPacks fragments | 17/9/39/49/6/16 | 14/8/10/16/4/8 | 0 each | Monkey only (Security in plain mode only) |
| `BackupsPreferencesFragment` | 27 | 0 | 0 | never |
| `AboutActivity` / `LicensesActivity` | 20 / 2 | 16 / 2 | 5 / 2 | both (dialogs Monkey only) |
| `GroupManagerActivity` | 22 | 10 | 0 | Monkey, empty list |
| `ImportEntriesActivity` | 38 | 8 | 0 | Monkey, root failure → finish |
| `ScannerActivity` | 16 | 0 | 8 | APE, no QR |
| `AuthActivity`, `EditEntryActivity`, `TransferEntriesActivity`, `AssignIconsActivity`, `PanicResponderActivity`, `ExitActivity` | 27/71/12/24/3/3 | 0 | 0 | never |
| `EntryHolder`, `IconPickerDialog` | 42 / 16 | 0 | 0 | never |

### 2.3 Which gate stopped the baseline

1. **G3 (empty vault)** blocks the largest part: MAIN list/selection modes, EDIT, Transfer, Assign icons, OTP generation, group filters, error cards. The cheapest entry creation (FAB → Enter manually → type a Base32 secret → Save) needs 4-5 precise actions plus valid text; neither random tool achieved it.
2. **Out-of-package activities**: every file-based feature goes through `VaultManager.fireIntentLauncher` or a chooser (`SRC/vault/VaultManager.java:243-277`). Monkey's activity controller rejects starts into other packages and the caller gets `RESULT_CANCELED` (FW-MEMORY; consistent with DATA: `WelcomeSlide.lambda$new$0` and `ImportExportPreferencesFragment.lambda$new$0` ran, their follow-up methods never did).
3. **G1 for APE** (data wipe on restart) and **G1c for both** (no password ever set, so `AuthActivity`, encrypted Security/Backups modes and all slot/crypto code stayed unreachable).
4. Environment: no QR content for the camera or images, no icon pack, no root, no enrolled biometric, no other authenticator apps installed.

### 2.4 What a test harness has to prepare

Concrete, but not tried on a device (UNVERIFIED):

1. **Skip the intro with content** (plaintext): put a vault file at `files/aegis.json` before the first start, e.g. `adb push aegis_plain_grouped_v2.json /data/local/tmp/` then `adb shell run-as com.beemdevelopment.aegis.debug sh -c 'mkdir -p files && cp /data/local/tmp/aegis_plain_grouped_v2.json files/aegis.json'` (`run-as` works because `debuggable=true` in APKMAN; FW-MEMORY for `run-as`). `MainActivity.onStart` then loads it without any dialog (`SRC/ui/MainActivity.java:951-973`). No preference is required (`pref_intro` only toggles a toast, `943-945`). Candidates: `ATEST/resources/com/beemdevelopment/aegis/aegis_plain.json` (7 entries: TOTP, HOTP, Steam; no groups) and `TEST/resources/com/beemdevelopment/aegis/vault/aegis_plain_grouped_v2.json` (same entries with v2 `group` fields → migrated into groups, which exercises group chips and the migration save path).
2. **Encrypted variant**: `ATEST/resources/com/beemdevelopment/aegis/aegis_encrypted.json`, password `test` (`ATEST/java/com/beemdevelopment/aegis/AegisTest.java:46`, used in `IntroTest.java:161-170`). Needed for `AuthActivity`, lock/auto-lock, encrypted Security page, Backups, backup password.
3. **Files for pickers** in `/sdcard/Download`: importer samples from `TEST/resources/com/beemdevelopment/aegis/importers/` (40 files: `aegis_plain.json`, `andotp_plain.json`, `2fas_authenticator_plain*.2fas`, `freeotp_plus.json`, `bitwarden.csv/.json`, `steam.json`, `stratum_plain.json`, `plain.txt`, `proton_authenticator.json`, `ente_auth.txt`, `duo.json`, `authy_plain.xml`, … plus encrypted ones whose password is `test`, `TEST/java/com/beemdevelopment/aegis/importers/DatabaseImporterTest.java:67`); QR images with `otpauth://` and `otpauth-migration://` payloads (**missing**: the `_fixtures` images are plain gradients, checked `Download/image_1.png`, `image_4.png`, `Pictures/photo_1.jpg`); any PNG/JPG (fixtures work) or an SVG for custom icons; an Aegis icon-pack ZIP with `pack.json` (**missing**; alternatively pre-extract into `files/icons/`, read by `SRC/icons/IconPackManager.java:30-34`).
4. **Let the tool operate DocumentsUI / gallery / ChooserActivity**, or deliver results by intent (`adb shell am start -a android.intent.action.SEND -t image/png --eu android.intent.extra.STREAM …`, `am start -a android.intent.action.VIEW -d 'otpauth://totp/…'`).
5. **Device state**: CAMERA granted (`install -g`) and a QR in the emulator camera scene (FW-MEMORY); an enrolled fingerprint (`adb -e emu finger touch 1`, FW-MEMORY) for biometric slides/unlock/enrolment; `settings put global auto_time 0` for the time-sync dialog (`MainActivity.java:756-764`); an `otpauth://` URI in the clipboard for the clipboard-import dialog (`474-500`); screen off (`input keyevent 26`) for `VaultLockReceiver`; `bmgr backupnow com.beemdevelopment.aegis.debug` for the backup agent (only does work if `pref_android_backups` is on, `SRC/AegisBackupAgent.java:43-71`); root plus an installed source app for "Import from app" (likely infeasible → treat as environment-gated); a trusted panic sender (practically unavailable).
6. **Never clear app data on tool restarts**, or re-seed the vault after each restart (APE lost its vault this way).

## 3. Screens and navigation

### 3.1 Window inventory

- **Activities**: `MainActivity` (host of fragment `EntryListView`, `RES/layout/activity_main.xml:54-56`), `IntroActivity` (ViewPager2 with `WelcomeSlide`, `SecurityPickerSlide`, `SecuritySetupSlide`, `DoneSlide`: `SRC/ui/IntroActivity.java:35-42`), `AuthActivity`, `EditEntryActivity`, `ScannerActivity`, `TransferEntriesActivity`, `PreferencesActivity` (container `R.id.content` with back stack: `SRC/ui/PreferencesActivity.java:41-50,80-98`), `GroupManagerActivity`, `AssignIconsActivity`, `ImportEntriesActivity`, `AboutActivity`, `LicensesActivity` (library UI), `PanicResponderActivity` and `ExitActivity` (no UI).
- **Preference fragments** (`RES/xml/preferences.xml:7-47`): Appearance, Behavior, Icon packs (`IconPacksManagerFragment`, a plain Fragment), Security, Backups, Import & Export, Audit log (plain Fragment).
- **DialogFragments**: `LicenseDialog`, `ChangelogDialog` (`SimpleWebViewDialog`, `SRC/ui/dialogs/SimpleWebViewDialog.java:42-65`).
- **Bottom sheets**: group selection and duplicate entry in `EditEntryActivity` (`384-438`, `871-942`); `IconPickerDialog` (`SRC/ui/dialogs/IconPickerDialog.java:42-156`).
- **AlertDialogs**: shared ones in `Dialogs` (`SRC/ui/dialogs/Dialogs.java`: delete 71, discard 111, set password 121, text/password input 194-272, checkbox 274, number pickers 305/323, error 355-418, backup error 420, multi error 427-487, time sync 489, importers 515, partial Google-Auth import 542, backup strategy 583) plus inline ones in `MainActivity`, `EditEntryActivity`, `AuthActivity`, preference fragments, `GroupManagerActivity`, `ImportEntriesActivity`, `IconPacksManagerFragment`, importers; `ProgressDialogTask` modal progress dialogs (`SRC/ui/tasks/ProgressDialogTask.java:26-50`).
- **Popups and transient UI**: Sort submenu (`RES/menu/menu_main.xml:15-48`), overflow menus, `PopupMenu` icon-pack switch (`IconPickerDialog.java:130-154`), non-focusable `PopupWindow` password hint (`SRC/ui/AuthActivity.java:248-268`), AutoCompleteTextView dropdowns (OTP type/algorithm `EditEntryActivity.java:217-221,323-362`, assign-group `MainActivity.java:544-559`, export format and `DropdownCheckBoxes` in the export dialog), Snackbar with Undo (`SRC/ui/ImportEntriesActivity.java:361-394`), toasts.
- **Action mode**: `MainActivity` selection (`RES/menu/menu_action_mode.xml:4-54`, `SRC/ui/MainActivity.java:1303-1308,1456-1540`). **SearchView**: `menu_main.xml:5-9`. **FAB menu** overlay with scrim (`RES/layout/fab_menu.xml:23,59,95,133`; `SRC/helpers/FabMenuHelper.java:54-134`).
- None: navigation graph, drawer, tabs (the intro pager is not user-swipeable), widgets.

### 3.2 Navigation (how the user moves)

| From | Gesture | Callback chain | To |
|---|---|---|---|
| launcher | tap icon | `MainActivity.onCreate/onStart` (`193`, `939`) | intro (G1), auth (G2) or main |
| intro slide | Next / Previous / Back | `IntroBaseActivity` lambdas `45,47` → `goToNextSlide` (`80-93`: `isFinished` else `onNotFinishedError`) / `goToPreviousSlide` (`96-101`) → `setPagerPosition` → `IntroActivity.onBeforeSlideChanged` (skips) | next slide; last slide Next → `onDonePressed` → main (`RESULT` to `MainActivity.java:142-148`) |
| main | overflow → Settings / About; Lock; Sort item | `MainActivity.onOptionsItemSelected` (`1086-1124`) | `PreferencesActivity` (for result, `826-835`; result → `recreate()` `467-472`), `AboutActivity`, lock → `onLocked(true)` → `AuthActivity` (`1348-1367`) |
| main | FAB, then item | `FabMenuHelper` lambdas (`54-66`) → `startScanActivity` (`803`) / `startScanImageActivity` (`812`) / `startEditEntryActivity()` (`474`) | scanner; external chooser; clipboard dialog or `EditEntryActivity` |
| main list | long-press row | `EntryAdapter$2.onLongClick` (`SRC/ui/views/EntryAdapter.java:522-535`) → `EntryListView.onLongEntryClick` (`326`) → `MainActivity.onLongEntryClick` (`1293-1301`) → `startActionMode` | selection mode |
| selection | action items | `ActionModeCallbacks.onActionItemClicked` (`1470-1531`) | copy (stay), `EditEntryActivity` (edit), `TransferEntriesActivity` (`1493-1505`), delete dialog, assign-group dialog, `AssignIconsActivity` (`522-531`) |
| main row | tap | `EntryAdapter$1.onClick` (`466-516`) → copy/reveal or toggle selection → `MainActivity.onEntryClick` (`1243-1252`) | same page (or selection change) |
| prefs main | tap section | `PreferencesActivity.onPreferenceStartFragment` (`80-89`, FragmentFactory by class name) → `showFragment` (`91-98`, back stack) | section page; Back/Up pops (`69-77`) |
| Appearance | "Groups" | lambda `SRC/ui/fragments/preferences/AppearancePreferencesFragment.java:33-37` | `GroupManagerActivity` |
| Import & Export | Import from file / app, Export, GA-style export | `ImportExportPreferencesFragment.java:106-136` | importers dialog → external picker or `ImportEntriesActivity`; export dialog; `TransferEntriesActivity` (`350-391`) |
| Icon packs | FAB | `IconPacksManagerFragment.java:71,172-176` | external picker |
| About | buttons | `SRC/ui/AboutActivity.java:53-98` | license/changelog dialogs, `LicensesActivity`, browser/mail (external) |
| `EditEntryActivity` | Save / Up / Back / menu | `onOptionsItemSelected` (`535-566`), `onSave` (`845-869`), `discardAndFinish` (`505-533`) | result to main (`169-183` launchers in `MainActivity`), discard dialog, duplicate sheet |
| `ImportEntriesActivity` | FAB | lambda `93-100` → `saveAndFinish` (`262-342`) | back to Import & Export; optional assign-icons dialog → `AssignIconsActivity` |
| any non-main `AegisActivity` | process recreated without a loaded vault | `abortIfOrphan` (`SRC/ui/AegisActivity.java:154-164,243-248`) | `MainActivity` (NEW_TASK + CLEAR_TASK) |

### 3.3 Modes per window (what changes the active handlers)

- **MainActivity**: vault loaded/encrypted (Lock item visible only if encrypted, `1155-1161`); shown entries 0 vs >0 (`EntryListView.java:539-548`); action mode with 1 vs >1 selected (Edit/Copy hidden for >1 and drag disabled, `1264-1268`; Assign icons only with an icon pack `1270-1273`; favorite title `1275-1290`); search expanded vs submitted (`1019-1083`, Back handler `1398-1415`); FAB menu open (`FabMenuHelper.java:76-134`, Back closes `1443-1454`); groups present (chips `268`, Save chip after a change `373-377`); error card variant (`1163-1197`); sort = Custom enables drag (`EntryAdapter.java:751-753`); preference-driven tap behaviour (copy single/double tap, tap-to-reveal, highlight: `EntryAdapter.java:469-500`); HOTP rows show a refresh button (`EntryHolder.java:153`, handler `EntryAdapter.java:549-566`); Back callbacks are stacked FAB > action mode > search > lock (added in that reverse order, `211-217`; FW-MEMORY: last added enabled callback wins).
- **IntroActivity**: slide index 0-3, Previous only on 1-2 (`IntroBaseActivity.java:154-166`); crypt type and `imported` drive skips (`IntroActivity.java:50-62`); biometrics option enabled or not (`SecurityPickerSlide.java:48-60`).
- **AuthActivity**: PIN-keyboard layout vs standard (`82-91`); biometric slot with valid key (button + auto prompt, `132-165,211-224`) vs invalidated key (info box); password reminder due (`181-195,237-241`); ≥3 failures switch the input type (`324-326`).
- **EditEntryActivity**: new manual vs new prefilled vs existing (`189-197,224-245`; Delete hidden for new `658-660`; Default icon only with a custom icon `661-663`); advanced section collapsed/expanded (`249,485-499`); OTP type (PIN field for Yandex/mOTP, advanced fields disabled for Steam/Yandex/mOTP: `471-483`); icon crop mode (`616-654`, Back handler `989-998`); unsaved changes (Back → discard dialog, `966-987`); icon packs present (picker vs chooser, `585-606`).
- **ScannerActivity**: camera provider ready (menu inert before, `108`); 2 lenses → switch item visible (`134-150`); analysis bound vs unbound after an error dialog (`175-200`); Google-Auth export batch in progress (`209-234`).
- **TransferEntriesActivity**: one vs several QR codes (`81-108`); copy button only for `GoogleAuthInfo` (`110-131`); brightness toggled (`154-162`).
- **PreferencesActivity**: which fragment is on top; Security encrypted vs plain (`SecurityPreferencesFragment.java:258-288`); Backups disabled/off/on (`BackupsPreferencesFragment.java:196-219`); Icon packs empty vs list (`IconPacksManagerFragment.java:178-186`); Audit log empty vs list (LiveData, `AuditLogPreferencesFragment.java:75-90`); export dialog encrypt checked vs not, groups present (`ImportExportPreferencesFragment.java:168-333`); dynamic colors disabled below API 31 and language hidden at API ≤ 23 (`AppearancePreferencesFragment.java:73,80`).
- **GroupManagerActivity**: empty vs list (`210-218`), dirty (Back → discard dialog, `177-186,220-229`).
- **ImportEntriesActivity**: file vs app import (`107-129`), before vs after results, vault empty vs not and wipe toggle (`93-100,404-416`), icon pack present after import (`320-340`).
- **IconPickerDialog**: query empty (categories, collapsible) vs query (flat list) (`SRC/ui/views/IconAdapter.java:92-101,123-129`); "Custom" icon only when opened from `EditEntryActivity` (`showAddCustom`).

### 3.4 Candidate page list (114 pages)

Variant naming for shared windows: `S_DLG_ERROR@SCANNER`, `S_DLG_TEXT_INPUT@RENAME_GROUP`, `S_DLG_SET_PASSWORD@ENABLE_ENCRYPTION`, `S_DLG_PROGRESS@KEY_DERIVATION`, `S_BIOMETRIC_PROMPT@AUTH`, `S_ICON_PICKER@ASSIGN`, `S_DLG_DELETE_ENTRIES@EDIT`, `S_DLG_DISCARD@GROUPS`, …

**CORE (pseudo pages and shared dialogs, 15)**

| Page | Window class | Mode predicate / handlers |
|---|---|---|
| `S_ENTRY` | outside the app | launcher, adb/am, other apps (deep link, share), system events (boot, screen off, backup), QS tiles, coverage broadcast |
| `S_EXIT` | – | task finished (`finish`, `finishAndRemoveTask`, `finishAffinity`, `AegisActivity.onLocked` private `finish(2)`) or crash; process and the `@Singleton VaultManager` (unlocked vault) may survive (`SRC/AegisModule.java:37-41`) |
| `S_EXT_PICKER` | external DocumentsUI / gallery / ChooserActivity | started for a result; returns `RESULT_OK` + Uri or `RESULT_CANCELED` |
| `S_EXT_APP` | browser, mail chooser, date settings, share chooser | no result consumed; Back returns |
| `S_SYS_PERMISSION` | system permission dialog | CAMERA not yet granted; Allow/Deny → `MainActivity.onRequestPermissionsResult` |
| `S_QS_PANEL` | SystemUI quick settings | Aegis tiles added; tap → tile `onClick` |
| `S_DLG_ERROR` | `Dialogs.showErrorDialog` (non-cancelable) | OK → caller listener; Details reveals, then Copy |
| `S_DLG_MULTI_ERROR` | `Dialogs.showMultiErrorDialog` | OK, Details |
| `S_DLG_MULTI_ERROR_DETAILS` | `Dialogs.showDetailedMultiErrorDialog` | OK, Copy |
| `S_DLG_TEXT_INPUT` | `Dialogs.showTextInputDialog` (text or password) | OK disabled while empty; outside tap cancels → optional cancel listener |
| `S_DLG_SET_PASSWORD` | `Dialogs.showSetPasswordDialog` | OK enabled only when both fields equal and non-empty → `KeyDerivationTask` |
| `S_DLG_DISCARD` | `Dialogs.showDiscardDialog` | Save / Discard |
| `S_DLG_CHECKBOX` | `Dialogs.showCheckboxDialog` | Yes enabled only when the box is checked; No |
| `S_DLG_NUMBER_PICKER` | tap-to-reveal timeout / backup versions picker | OK |
| `S_DLG_PROGRESS` | `ProgressDialogTask` dialog | task running, non-cancelable; closes in `onPostExecute` (or `ON_PAUSE` observer) |

**SECURITY (18)**

| Page | Window class | Mode predicate / handlers |
|---|---|---|
| `S_INTRO_WELCOME` | `IntroActivity` + `WelcomeSlide` | pager position 0: Next, Import Aegis vault; Previous invisible; Back no-op |
| `S_INTRO_PICKER` | `SecurityPickerSlide` | position 1: radio None / Password / Biometrics (iff available); Next, Previous, Back = previous |
| `S_INTRO_SETUP_PASSWORD` | `SecuritySetupSlide` | position 2, `cryptType == PASS`: two fields, show-password box, strength meter; Next → toast or key derivation |
| `S_INTRO_SETUP_BIOMETRIC` | `SecuritySetupSlide` | position 2, `cryptType == BIOMETRIC`: Next → biometric enrolment prompt, then derivation |
| `S_INTRO_DONE` | `DoneSlide` | last position: check button → `onDonePressed`; Back no-op |
| `S_INTRO_PAUSED` | – | intro under an external picker, error dialog or Home |
| `S_AUTH_PASSWORD` | `AuthActivity` | no usable biometric key, or reminder due: password field (standard or PIN layout), Unlock, IME Done/Enter, Back = exit |
| `S_AUTH_BIOMETRIC` | `AuthActivity` | biometric slot with valid key: + Biometrics button, prompt auto-shown on resume unless inhibited |
| `S_AUTH_PAUSED` | – | under the biometric prompt / Home |
| `S_BIOMETRIC_PROMPT` | androidx `BiometricPrompt` | @INTRO, @AUTH, @SECURITY: authenticate, cancel, error |
| `S_DLG_UNLOCK_FAILED` | inline AlertDialog (`AuthActivity.java:313-327`) | OK → select password |
| `S_DLG_PASSWORD_REMINDER` | inline AlertDialog (`AuthActivity.java:181-192`) | OK → biometric prompt |
| `S_PREF_SECURITY_PLAIN` | `SecurityPreferencesFragment` | vault not encrypted: encryption switch, secure screen, tap-to-reveal (+time), panic switch |
| `S_PREF_SECURITY_ENCRYPTED` | same | encrypted: + change password, biometrics, reminder frequency (iff bio slot), auto-lock, PIN keyboard, backup password (+change) |
| `S_DLG_DISABLE_ENCRYPTION` | inline AlertDialog | Yes / No |
| `S_DLG_AUTO_LOCK` | multi-choice AlertDialog | OK / Cancel |
| `S_DLG_REMINDER_FREQ` | single-choice AlertDialog | item tap |
| `S_DLG_PIN_KEYBOARD_ERROR` | inline AlertDialogs (not digits / wrong password) | OK |

**MAIN (21)**

| Page | Window class | Mode predicate / handlers |
|---|---|---|
| `S_MAIN_EMPTY` | `MainActivity` + `EntryListView` | vault loaded, 0 shown entries, no action mode, search collapsed: empty view, Search, Sort, Lock (iff encrypted), overflow Settings/About, FAB |
| `S_MAIN_LIST` | same | ≥1 shown entry, nothing selected: row tap, long-press, HOTP refresh, chips (iff groups), error card (iff reminder/backup error/plaintext warning), drag |
| `S_MAIN_SELECT_ONE` | `MainActivity` action mode | `_actionMode != null`, 1 selected: Favorite, Copy, Edit, Transfer, Delete, overflow Select all / Assign icons (iff pack) / Assign to group; row taps toggle |
| `S_MAIN_SELECT_MULTI` | same | >1 selected: Copy and Edit hidden, no drag |
| `S_MAIN_SEARCH` | SearchView expanded | not iconified, nothing submitted: typing filters live; IME search submits; Back collapses |
| `S_MAIN_SEARCH_RESULT` | `MainActivity` | `_submittedSearchQuery != null`: title "Search" + subtitle; Back clears; search icon reopens with query |
| `S_MAIN_FAB_OPEN` | FAB overlay | `FabMenuHelper.isOpen()`: Scan QR code, Scan image, Enter manually; scrim tap or Back closes |
| `S_MAIN_SORT_MENU` | Sort submenu | 7 single-choice items → `onOptionsItemSelected` (group `action_sort_category`) |
| `S_MAIN_PAUSED` | – | under any child activity, dialog activity or Home |
| `S_DLG_CLIPBOARD_IMPORT` | inline AlertDialog (`MainActivity.java:486-492`) | clipboard holds a valid otpauth URI: Yes → editor prefilled, No → editor manual |
| `S_DLG_ASSIGN_GROUP` | inline AlertDialog + dropdown (`533-601`) | dropdown (New group shows a name field), OK validates, Cancel |
| `S_DLG_DELETE_ENTRIES` | `Dialogs.showDeleteEntriesDialog` | @MAIN / @EDIT: Yes / No |
| `S_DLG_TIME_SYNC` | `Dialogs.showTimeSyncWarningDialog` | first load with `AUTO_TIME == 0` and warning enabled: Yes → date settings, No, checkbox |
| `S_DLG_BACKUP_REMINDER` | inline AlertDialog (error card) | Yes → Backups page, Cancel |
| `S_DLG_PLAINTEXT_WARNING` | inline AlertDialog (`1199-1227`) | OK (+checkbox), Cancel |
| `S_DLG_PARTIAL_GA_IMPORT` | `Dialogs.showPartialGoogleAuthImportWarningDialog` | incomplete Google-Auth batch from images: Import anyway, Cancel, Show details |
| `S_SCANNER` | `ScannerActivity` | camera bound: switch camera (iff 2 lenses), QR detection, Back |
| `S_SCANNER_PAUSED` | – | under an error dialog or Home |
| `S_TRANSFER_SINGLE` | `TransferEntriesActivity` | one QR: tap QR toggles brightness, Copy URI (iff `GoogleAuthInfo`), Up |
| `S_TRANSFER_MULTI` | same | several QRs: Next/Previous (Next becomes Done on the last), brightness, Up |
| `S_TRANSFER_PAUSED` | – | Home |

**EDIT / ICONS (19)**

| Page | Window class | Mode predicate / handlers |
|---|---|---|
| `S_EDIT_NEW_MANUAL` | `EditEntryActivity` | `_isNew && _isManual`: all fields, Secret in basic section; Save, Edit icon, Reset usage; Delete hidden |
| `S_EDIT_NEW_PREFILLED` | same | `_isNew && !_isManual` (QR, URI, clipboard, share): advanced section disabled |
| `S_EDIT_EXISTING` | same | `!_isNew`: + Delete, usage count and last-used shown |
| `S_EDIT_ICON_CROP` | same, KropView visible | after picking a bitmap: save-image button; Back cancels the crop |
| `S_EDIT_GROUP_SHEET` | BottomSheetDialog | chips, Add group (→ `S_DLG_TEXT_INPUT@ADD_GROUP`), Clear, Save |
| `S_EDIT_DUPLICATE_SHEET` | BottomSheetDialog (non-cancelable) | new entry duplicates name+issuer: Overwrite, Add suffix, Cancel |
| `S_DLG_OVERWRITE_DUPLICATES` | inline AlertDialog | Delete / No |
| `S_DLG_RESET_USAGE` | inline AlertDialog | Yes / No |
| `S_DLG_SAVE_ERROR` | inline AlertDialog (`836-843`) | OK |
| `S_ICON_PICKER` | `IconPickerDialog` | ≥1 icon pack, empty query: category headers, icons, Custom (@EDIT only), search field, pack button |
| `S_ICON_PICKER_SEARCH` | same | query non-empty: flat suggested list |
| `S_ICON_PACK_MENU` | PopupMenu | pack names |
| `S_ASSIGN_ICONS` | `AssignIconsActivity` | icon pack present: row tap → picker, per-row reset, Save, Up → discard dialog; Back simply finishes (its back callback is never enabled) |
| `S_PREF_ICON_PACKS_EMPTY` | `IconPacksManagerFragment` | no pack: help link, FAB import |
| `S_PREF_ICON_PACKS_LIST` | same | ≥1 pack: delete per pack, FAB |
| `S_DLG_REMOVE_ICON_PACK` | inline AlertDialog | Yes / No |
| `S_DLG_ICON_PACK_EXISTS` | inline AlertDialog | Yes replaces, No |
| `S_EDIT_PAUSED`, `S_ASSIGN_ICONS_PAUSED` | – | under picker/dialog/Home |

**SETTINGS (29)**

| Page | Window class | Mode predicate / handlers |
|---|---|---|
| `S_PREFS_MAIN` | `PreferencesActivity` + `MainPreferencesFragment` | 7 section entries, Up |
| `S_PREF_APPEARANCE` | `AppearancePreferencesFragment` | theme, dynamic colors (disabled on API 27), language, view mode, icon/next-code/expiration switches, code grouping, name position, shared-issuer switch, Groups, reset usage counts |
| `S_DLG_THEME`, `S_DLG_LANGUAGE`, `S_DLG_VIEW_MODE`, `S_DLG_CODE_GROUPING`, `S_DLG_NAME_POSITION`, `S_DLG_RESET_ALL_USAGE` | inline single-choice / confirm dialogs | theme and language → `recreate()` |
| `S_PREF_BEHAVIOR` | `BehaviorPreferencesFragment` | focus search, search behavior, minimize on copy, copy behavior, haptics, multi-select groups, highlight (enables pause), pause |
| `S_DLG_SEARCH_BEHAVIOR`, `S_DLG_COPY_BEHAVIOR` | inline multi-/single-choice | OK disabled when no search field is checked |
| `S_PREF_BACKUPS_DISABLED` | `BackupsPreferencesFragment` | vault plain: backup switches disabled, reminder switch active |
| `S_PREF_BACKUPS_OFF` | same | encrypted, built-in backups off |
| `S_PREF_BACKUPS_ON` | same | encrypted and `pref_backups`: strategy, location, trigger, versions, status |
| `S_DLG_VERSIONING_STRATEGY` | `Dialogs.showBackupsVersioningStrategy` | keep-X vs single (+risk box) |
| `S_PREF_AUDIT_LOG_EMPTY`, `S_PREF_AUDIT_LOG_LIST` | `AuditLogPreferencesFragment` | events of the last 30 days (`SRC/database/AuditLogDao.java:16`); rows have no handlers |
| `S_GROUPS_EMPTY`, `S_GROUPS_LIST` | `GroupManagerActivity` | menu Remove unused, Save; list: rename, delete, drag |
| `S_DLG_REMOVE_GROUP`, `S_DLG_REMOVE_UNUSED_GROUPS` | inline AlertDialogs | Yes / No |
| `S_ABOUT` | `AboutActivity` | license, third-party licenses, version copy, links, mail, changelog |
| `S_DLG_LICENSE`, `S_DLG_CHANGELOG` | `SimpleWebViewDialog` subclasses | OK |
| `S_LICENSES` | `LicensesActivity` (library UI) | library list with search |
| `S_PREFS_PAUSED`, `S_GROUPS_PAUSED`, `S_ABOUT_PAUSED`, `S_LICENSES_PAUSED` | – | under a child activity, external app or Home |

**IMPORT / EXPORT (12)**

| Page | Window class | Mode predicate / handlers |
|---|---|---|
| `S_PREF_IMPORT_EXPORT` | `ImportExportPreferencesFragment` | Import from file, Import from app, Export, Google-Authenticator-style export |
| `S_DLG_IMPORTERS_FILE` | `Dialogs.showImportersDialog(isDirect=false)` | 19 importers (Aegis preselected): row tap updates help, OK → external picker |
| `S_DLG_IMPORTERS_APP` | same, `isDirect=true` | 10 direct importers: OK → `ImportEntriesActivity` without file |
| `S_DLG_EXPORT_ENCRYPTED` | inline export dialog | format Aegis with encrypt checked: format dropdown, encrypt box, export-all-groups box (iff groups), OK, Share, Cancel |
| `S_DLG_EXPORT_PLAIN` | same | encrypt unchecked or HTML/URI format: risk box must be checked before OK/Share |
| `S_EXPORT_GROUPS_DROPDOWN` | `DropdownCheckBoxes` popup | groups exist and export-all unchecked |
| `S_IMPORT_ENTRIES_LOADING` | `ImportEntriesActivity` | before results: root shell / read / importer prompts |
| `S_IMPORT_ENTRIES_LIST` | same | results shown: row tap toggles, FAB import (wipe dialog iff vault non-empty and toggle on), menu toggle all / wipe vault, Undo snackbar for duplicates, Up |
| `S_DLG_APP_VERSION_WARNING` | inline AlertDialog | unsupported installed app version (e.g. Google Authenticator not installed): Yes / No |
| `S_DLG_IMPORTER_CHOICE` | importer pre-dialogs (andOTP format, FreeOTP warning, TOTP Authenticator) | `SRC/importers/AndOtpImporter.java:185-198`, `FreeOtpImporter.java:175-196`, `TotpAuthenticatorImporter.java:155-167` |
| `S_DLG_IMPORT_ASSIGN_ICONS` | inline AlertDialog | after import with an icon pack: Yes → `AssignIconsActivity`, No |
| `S_IMPORT_ENTRIES_PAUSED` | – | under prompts/Home |

## 4. Framework mechanisms that need FRAMEWORK / ASYNC / LIFECYCLE edges

| Mechanism | App classes (evidence) | Modelling note |
|---|---|---|
| Activity Result API | `MainActivity` 8 launchers (`134-191`), `WelcomeSlide` (`32-38`), `EditEntryActivity` (`141-162`), `ImportExportPreferencesFragment` 5 launchers (`73-95`), `BackupsPreferencesFragment` (`41-48`), `IconPacksManagerFragment` (`56-62`); external launches through `VaultManager.fireIntentLauncher` (blocks auto-lock; ActivityNotFound → error dialog, `243-277`) | `RESULT` edges into the launcher lambdas; results arrive before the caller's `onStart/onResume` (FW-MEMORY) |
| RecyclerView adapters / holders | `EntryAdapter` (+`EntryHolder`, `ErrorCardHolder`, `FooterView`, `DiffCallback` via `DiffUtil.dispatchUpdatesTo`, `EntryAdapter.java:285-296`), `GroupAdapter`, `IconAdapter` (+ holders, `notifyItemRange*`), `IconPackAdapter`, `ImportEntriesAdapter`, `AssignIconAdapter`, `AuditLogAdapter`; `GridLayoutManager.SpanSizeLookup` (`EntryListView$2`, `IconPickerDialog$3`); item decorations; `ItemTouchHelper` (`SimpleItemTouchHelperCallback`, anonymous `GroupManagerActivity$1`) | create/bind only when the RecyclerView is visible (empty vault → none ran); drag needs `isLongPressDragEnabled` |
| AdapterViews | `ArrayAdapter` ListView (importers dialog `Dialogs.java:515-540`); AutoCompleteTextView dropdowns (`DropdownHelper`, `DropdownCheckBoxes$CheckboxAdapter` + `Filter`) | `getItem/getItemId` of the checkbox adapter are FRAMEWORK_ONLY candidates |
| ViewPager2 + `FragmentStateAdapter` | `IntroBaseActivity$ScreenSlidePagerAdapter` (reflection `newInstance`, `212`), `SlideSkipBlocker` page callback (`224-232`) | fragments created by the adapter; `SlideFragment.onResume` sets the current slide (`SRC/ui/intro/SlideFragment.java:29-32`) |
| Fragments by reflection | `PreferencesActivity.onPreferenceStartFragment` (`81`), `getRequestedFragment` (`107`), `DatabaseImporter.create` (`SRC/importers/DatabaseImporter.java:90-97`, all 19 importer `<init>(Context)`) | edges from the reflective call site, guarded by the chosen preference / importer |
| Lifecycle / LiveData | `ProcessLifecycleOwner` observer (`SRC/AegisApplicationBase.java:54,105-114`); Room `LiveData` observed in `AuditLogPreferencesFragment` (`75-90`); `ProgressDialogTask$Observer` `@OnLifecycleEvent(ON_PAUSE)` (reflection via androidx Lifecycling, FW-MEMORY) | the observer only exists when a task is started with `execute(Lifecycle, …)` |
| AsyncTask | 10 subclasses of `ProgressDialogTask`: `KeyDerivationTask`, `PasswordSlotDecryptTask`, `PBKDFTask`, `Argon2Task`, `ImportFileTask`, `ExportTask`, `IconOptimizationTask`, `ImportIconPackTask`, `QrDecodeTask`, `RootShellTask` | `ASYNC`: `doInBackground` on a worker, `onPreExecute/onPostExecute/onProgressUpdate` on main |
| Executors / Handlers | `AuditLogRepository` single thread (`17,61`), `VaultBackupManager` single thread (`53,58`), CameraX analysis executor (`ScannerActivity.java:65,164`) → `QrCodeAnalyzer.analyze` → main-thread `Handler.post` (`176`); `UiRefresher` TOTP refresh loop (`SRC/helpers/UiRefresher.java:21-43`); `EntryAdapter` dim/double-tap handlers; `EntryHolder` copy/expiration handlers; `FabMenuHelper` delayed hide (`125`); `AuthActivity` popup dismiss (`258-267`); `UiThreadExecutor` for biometric callbacks | timers fire only with entries shown (TOTP period) |
| Biometrics / KeyStore | `AuthActivity$BiometricPromptListener` (`366-401`), `BiometricSlotInitializer` (`SRC/helpers/BiometricSlotInitializer.java:29-131`), `KeyStoreHandle` | on API 27 androidx.biometric 1.1.0 uses the fingerprint dialog (FW-MEMORY) |
| Broadcast receivers | `VaultLockReceiver` (dynamic `SCREEN_OFF`; manifest `LOCK_VAULT` whose only sender is the disabled notification); `QsTileRefreshReceiver` (boot / user unlocked) | `SYSTEM` edges from `S_ENTRY` or from any page (screen off) |
| Services | two `TileService`s (bound by SystemUI); `NotificationService` undeclared | tiles: `S_QS_PANEL` → `onClick` → `INTENT MainActivity` |
| Content providers | androidx `FileProvider` for "Share" export (`ImportExportPreferencesFragment.java:320-326`); `InitializationProvider` (library) | library only |
| Database | Room `AppDatabase` (`SRC/AegisModule.java:50-55`), generated `AppDatabase_Impl`, `AuditLogDao_Impl`, `AuditLogRepository` | inserts are async; queries via LiveData |
| Vault persistence | `AtomicFile files/aegis.json` (`SRC/vault/VaultRepository.java:52-90`); `cacheDir/export`, `cacheDir/backup`, `files/icons` | plain direct calls |
| Dependency injection | Hilt bytecode transform: `AegisActivity`→`Hilt_AegisActivity`, `PreferencesFragment`/`AuditLogPreferencesFragment`/`IconPacksManagerFragment`→`Hilt_*`, `VaultLockReceiver`→`Hilt_VaultLockReceiver`, `AegisApplication`→`Hilt_AegisApplication` (BYTECODE superclasses); `EarlyEntryPoints` in `AegisApplicationBase.java:47`, `AegisActivity.java:64`, `LicensesActivity.java:29` | injection happens in `Hilt_*` `onContextAvailable`/`onAttach`/`onReceive` (FRAMEWORK) |
| WebView | `SimpleWebViewDialog.loadData` of `changelog.html` / `license.html` assets (`63`, `ChangelogDialog.java:18`, `LicenseDialog.java:18-19`); no JS bridge | – |
| Storage Access Framework / pickers | `ACTION_GET_CONTENT` (`WelcomeSlide.java:44`, `ImportExportPreferencesFragment.java:110-112`, `IconPacksManagerFragment.java:172-176`), `ACTION_PICK`+`GET_CONTENT` choosers (`MainActivity.java:812-824`, `EditEntryActivity.java:568-578`), `ACTION_CREATE_DOCUMENT` (export `ImportExportPreferencesFragment.java:270-277`, single backup `BackupsPreferencesFragment.java:255-261`), `ACTION_OPEN_DOCUMENT_TREE` + persistable permission (`263-271`, `179-194`), `DocumentFile` in `VaultBackupManager` | all leave the package (`S_EXT_PICKER`) |
| Camera / QR | CameraX (`ScannerActivity`), zxing (`QrCodeAnalyzer`, `QrCodeHelper`, `QrDecodeTask`) | needs QR content |
| Clipboard | read: `ClipboardUtils.readText` (`MainActivity.java:475`); write: `copyEntryCode` (`1377-1396`), Transfer copy, About version, error-dialog copy | – |
| Backup | `AegisBackupAgent` (full backup only), `BackupManager.dataChanged` (`VaultManager.java:187-190`) | `bmgr` or cloud backup |
| Root | libsu `Shell` in `RootShellTask`, `SuFile` in importers | environment-gated |
| Glide | `AegisGlideModule` → generated `GeneratedAppGlideModuleImpl` registers `VaultEntryIconLoader` and SVG decoders/transcoder; `GlideHelper`; `RecyclerViewPreloader` + `PreloadModelProvider`s | `Glide.with()` returns the generated `GlideRequests`, so generated `GlideRequest` overrides are reached by virtual dispatch from library code (INFERRED) |
| Shortcuts / tiles / panic | `ShortcutManager` dynamic shortcut; QS tiles; `TrustedIntents` | outside the package |
| Not present | data binding, RxJava, WorkManager, JobScheduler, AlarmManager, Navigation component, app widgets, notifications (disabled) | `APP/build.gradle` dependencies; grep of `SRC/` |

## 5. Unreachable-code candidates (evidence only, no verdicts)

Method-level reference scan of all class files in `CLS/` (BYTECODE: no `Methodref`/`InterfaceMethodref` from any app class to the method, its overridden app supertype method, or a subclass-qualified reference). Framework callbacks were removed from this list by hand.

**No caller anywhere in the APK code (DEAD candidates)**
- Disabled notification feature: `AegisApplicationBase.initNotificationChannels` (call commented out, `SRC/AegisApplicationBase.java:63-66,91-103`), `VaultManager.getNotificationServiceIntent` (callers commented out, `SRC/vault/VaultManager.java:279-293`), all of `NotificationService` (not declared, `MAN:104-106`).
- Unused helpers/getters: `AboutActivity.getThemeColorAsHex` (`143`), `Preferences.getTimeout` (`360`), `Preferences.isAutoLockEnabled()` (`211`), `Preferences.setFocusSearch` (`430`), `Preferences.setIsPanicTriggerEnabled` (`111`, used only by `ATEST`), `EventType.fromInteger`, `VaultEntry.isDefault`, `Slot.getEncryptedMasterKey` (test only), `YandexInfo.setPin`, `GoogleAuthInfo.parseExportUri(String)` (the `Uri` overload is used), `IconPack.getDirectory`, `VaultBackupManager$FileInfo.getExtension/getFilename`, `VaultGroupModel.getGroup`, `EntryHolder.isHidden`, `AuditLogAdapter.addReferencedEntry`, `DatabaseImporterEntryException.getText`, `ImportFileTask$Result.getUri`, `QrDecodeTask$Result.getUri`, `PasswordSlotDecryptTask$Result.<init>(MasterKey,PasswordSlot)`, `BiometricSlotInitializer.cancelAuthentication` and its `(FragmentActivity, Listener)` constructor (both callers pass a Fragment: `SecuritySetupSlide.java:101`, `SecurityPreferencesFragment.java:117`), `SlideFragment.goToPreviousSlide/skipToSlide` (`SRC/ui/intro/SlideFragment.java:64-72`), `Dialogs.showErrorDialog(Context,String,Exception)` (`359`), `Dialogs.showPasswordInputDialog(Context,TextInputListener)` (`254`) and `(Context,int,TextInputListener)` (`262`).
- Test-only overloads in main code: `TOTP.generateOTP(byte[],String,int,long)`, `MOTP.generateOTP(…5 args)`, `YAOTP.generateOTP(…5 args)`, `OTP.getCode/getDigits`; importer `decrypt(char[])` helpers in `AegisImporter$EncryptedState`, `FreeOtpImporter$EncryptedState`, `StratumImporter$EncryptedState`, `StratumImporter$LegacyEncryptedState`, and `AndOtpImporter$EncryptedState.decryptNewFormat` (used by `TEST/.../DatabaseImporterTest.java`).
- `getAppPath()` of the 9 non-direct importers (AegisImporter, AndOtp, AuthenticatorPlus, Bitwarden, EnteAuth, GoogleAuthUri, ProtonAuthenticator, TwoFAS, WinAuth) only throws `UnsupportedOperationException` (e.g. `SRC/importers/AegisImporter.java:40-42`) and is reachable only through `readFromApp`, which is only offered for `supportsDirect` importers (`DatabaseImporter.java:33-51,99-105`).
- `GroupAdapter.onItemDismiss/onItemDrop` (the group touch callback calls only `onItemMove`, `SRC/ui/GroupManagerActivity.java:70-81`).
- Third-party sources compiled in: `ColorGenerator.getRandomColor`, 8 `TextDrawable$Builder` config methods, `TrustedIntents` API not used by `PanicResponderActivity` (`startActivity`, `isReceiverTrusted×3`, `isTrustedSigner`, `removeTrustedSigner`, `removeAllTrustedSigners`, `checkTrustedSigner`) and `ApkSignaturePin` fingerprint getters.

**FRAMEWORK_ONLY candidates** (callback exists, but no known path makes the framework call it)
- `SimpleItemTouchHelperCallback.onSwiped` and therefore `EntryAdapter.onItemDismiss`: swipe disabled (`isItemViewSwipeEnabled` returns false and swipe flags are 0, `SRC/helpers/SimpleItemTouchHelperCallback.java:46-48,69-77`); same for `GroupManagerActivity$1.onSwiped` (`63-81`).
- `AssignIconsActivity$BackPressHandler.handleOnBackPressed`: the callback is created disabled and never enabled (`SRC/ui/AssignIconsActivity.java:77-78,212-215`; no `setEnabled` call in the file).
- `AegisBackupAgent.onBackup/onRestore`: key-value API, empty bodies; with `fullBackupOnly=true` the framework uses full backup (FW-MEMORY).
- `DropdownCheckBoxes$CheckboxAdapter.getItem/getItemId` (FW-MEMORY: AutoCompleteTextView only calls `getItem` on item click; clicks go to the checkbox).
- `TextDrawable.getOpacity/setAlpha/setColorFilter`, `CenterVerticalSpan.update*` (only when tap-to-reveal draws dots), `EditEntryActivity$2.onLoadCleared`: framework callbacks with narrow triggers; check each.

**Generated code in bulk** (decide a policy once)
- `GoogleAuthProtos*` (187 methods, protoc-lite from `APP/src/main/proto/google_auth.proto`): only the `MigrationPayload.parseFrom(byte[])`/getters path (`GoogleAuthInfo.parseExportUri(Uri)`) and the builder path (`GoogleAuthInfo$Export.getUri`, `SRC/otp/GoogleAuthInfo.java:195-205,399-452`) are used; the other `parseFrom` overloads, `parseDelimitedFrom`, `clear*`, `*Bytes` getters etc. have no caller. `dynamicMethod` is called by the protobuf runtime (library FRAMEWORK edge).
- Glide generated API: `GlideApp` (14 methods, no caller: the app uses `Glide.with`), 26 static factories of `GlideOptions`; but `GlideRequests`/`GlideRequest`/`GlideOptions` instance overrides are reachable by virtual dispatch (see §4).
- Hilt/Dagger: marker classes with only a constructor that nothing instantiates (`hilt_aggregated_deps/*` ×10, `dagger/hilt/internal/*/codegen/*` ×2, `dagger/hilt/android/internal/earlyentrypoint/codegen/*` ×4, `AegisApplication_ComponentTreeDeps`); never-built components `…$ServiceC*`, `…$ViewC*`, `…$ViewModelC*`, `…$ViewWithFragmentC*` (no `@AndroidEntryPoint` service/view and no `@HiltViewModel`; all 0 hits, DATA). Room `_Impl` methods are reachable through the Room runtime.

**Debug-only, build-config and flavor facts**
- Only the `debug` build type is compiled; no product flavors (`APP/build.gradle` `buildTypes`). `BuildConfig`: `APPLICATION_ID=com.beemdevelopment.aegis.debug`, `DEBUG=true`, `GIT_HASH=780393bf5`, `GIT_BRANCH=main`, `TEST=new AtomicBoolean(false)` (BYTECODE strings of `CLS/com/beemdevelopment/aegis/BuildConfig.class`). Note: `GIT_HASH` differs from `DATASET.txt` `source_commit 619c1ab…` (cause UNVERIFIED).
- `DEBUG` branches: version string format (`SRC/ui/AboutActivity.java:111-117`), secure screen off by default (`SRC/Preferences.java:115-118`; `FLAG_SECURE` only if enabled, `AegisActivity.java:72-74` — turning it on blanks screenshots), verbose libsu logging (`AegisApplicationBase.java:39-42`).
- `BuildConfig.TEST` is set only by instrumentation tests (`ATEST`), so the `getIntent()` branch of `PanicResponderActivity` (`29-37`) is dead in the APK.

**API-level, hardware, environment gates (API 27 emulator)**
- Dead branches on API 27: tile `PendingIntent` (API 34+), dynamic colors (API 31+, preference disabled), `AegisBackupAgent` transport flags (API 28+), `NoAutofillEditText.getAutofillType` else-branch (< API 26); taken on API 27: SVG software layer (`SRC/ui/glide/GlideHelper.java:75-82`), shortcuts (≥ 25), language preference (> 23).
- Hardware/environment: camera + QR (scanner), enrolled biometric (biometric slides, unlock, enrolment), root + installed source app (direct import; `MAN:169-180`), Guardian-Project-signed sender (panic), SystemUI (tiles), reboot (boot receiver), backup transport. No network or account use anywhere.

**JaCoCo blind spots (affect the cross-check)**
- Not instrumented in the APK (no `$jacocoInit` in the dex; BYTECODE scan of `classes*.dex`): `BuildConfig` (2), `RootShellTask` (3), `RawSlot` (3). `RootShellTask` ran in Monkey (its callback `ImportEntriesActivity.lambda$startImportApp$5` and `ProgressDialogTask.<init>/onPreExecute/onPostExecute` are hit, DATA) but shows 0.
- JaCoCo reports 2,957 methods; `tools/list_methods.py` yields 3,102 (excluding `JacocoInstrument`). The 145 missing ones: enum `values/valueOf` (34), enum constructors (12), private empty constructors (40), `@DaggerGenerated` classes `AegisModule_*Factory` (20), `*_MembersInjector` (26) and `DaggerAegisApplication_HiltComponents_SingletonC.builder` (BYTECODE: the classes carry `Ldagger/internal/DaggerGenerated;`; JaCoCo's "Generated" annotation filter is FW-MEMORY), synthetic switch-map `<clinit>` (12). Their hit flag must stay blank.

## 6. Decomposition (6 areas)

Every class file in `CLS/` (544) is assigned to exactly one area by the rules below; counts are JaCoCo methods (2,957 total).

| Area | Owns (classes) | Methods (generated) | Pages | Entry edges from other areas |
|---|---|---|---|---|
| **1 CORE** (shared infrastructure owner) | Application + DI (`AegisApplication*`, `Hilt_AegisApplication*`, `AegisApplication_HiltComponents*`, `DaggerAegisApplication_HiltComponents_SingletonC*`, `AegisModule*`, `hilt_aggregated_deps`, `dagger/hilt/**`, `BuildConfig`, `HiltWrapper_*`); `ui/AegisActivity` + `Hilt_AegisActivity`; `Preferences` + enums (`AccountNamePosition`, `CopyBehavior`, `EventType`, `GroupPlaceholderType`, `PassReminderFreq`, `SortCategory`, `Theme`, `ThemeMap`, `ViewMode`, `VibrationPatterns`, `BackupsVersioningStrategy`); `vault/*` except `slots/` (incl. `VaultManager`, `VaultRepository`, `VaultBackupManager`, `VaultHtmlExporter`); `otp/*`, `crypto/otp/*`, `encoding/*`, `GoogleAuthProtos*`; `database/*`; `util/*`; `receivers/*`, `services/*`, `AegisBackupAgent`; `ui/dialogs/Dialogs`, `ui/tasks/ProgressDialogTask`, `ui/tasks/ImportFileTask`, `ui/components/NoAutofillEditText`; generic helpers (`AnimationsHelper`, `ContextHelper`, `DropdownHelper`, `EditTextHelper`, `MetricsHelper`, `PermissionHelper`, `SafHelper`, `SimpleAnimationEndListener`, `SimpleTextWatcher`, `ThemeHelper`, `UiThreadExecutor`, `ViewHelper`) | **1020** (327): Application+DI 113, `AegisActivity` 28, Preferences+enums 137, protos 187, otp/encoding 116, vault model ~198, database 46, util 33, Dialogs+progress 79, helpers 35, receivers/services/agent 32, `ImportFileTask`+`NoAutofillEditText` 16 | 15 (`S_ENTRY`, `S_EXIT`, `S_EXT_*`, `S_SYS_PERMISSION`, `S_QS_PANEL`, shared `S_DLG_*`, `S_DLG_PROGRESS`) | every `AegisActivity` subclass (`LIFECYCLE` via `super`, `onLocked` via `VaultManager.lock`); all areas `CALL` vault/prefs/otp/Dialogs; tiles `INTENT` to MAIN |
| **2 SECURITY** (onboarding, unlock, security settings) | `IntroActivity`, `ui/intro/*`, `ui/slides/*`, `AuthActivity`, `PanicResponderActivity`, `ExitActivity`, `SecurityPreferencesFragment`, `ui/preferences/SwitchPreference`, tasks `KeyDerivationTask`, `PasswordSlotDecryptTask`, helpers `BiometricSlotInitializer`, `BiometricsHelper`, `PasswordStrengthHelper`, `vault/slots/*`, `crypto/{CryptoUtils, CryptParameters, CryptResult, KeyStoreHandle(+Exception), MasterKey(+Exception), SCryptParameters, bc/*, pins/*}`, `info/guardianproject/**` | **324** (0) | 18 (`S_INTRO_*`, `S_AUTH_*`, `S_BIOMETRIC_PROMPT`, `S_PREF_SECURITY_*` and its dialogs) | MAIN `startIntroActivity`/`startAuthActivity`/`onLocked(true)` (`MainActivity.java:603-609,1146-1153,1348-1367`) and `RESULT` back (`134-148`); SETTINGS `onPreferenceStartFragment`; CORE `Dialogs.showSetPasswordDialog` → `KeyDerivationTask`; IMPORT `AegisImporter` → `PasswordSlotDecryptTask`; `S_ENTRY` panic intent |
| **3 MAIN** (entry list, search, selection, scan, transfer) | `MainActivity` (+inner), `ui/views/Entry*` (`EntryListView`, `EntryAdapter`, `EntryHolder` + inner), `ErrorCardHolder`, `TotpProgressBar`, `ui/models/{ErrorCardInfo, VaultGroupModel}`, helpers `FabMenuHelper`, `FabScrollHelper`, `SimpleItemTouchHelperCallback`, `ItemTouchHelperAdapter`, `UiRefresher`, `VibrationHelper`, `CenterVerticalSpan`, `QrCodeAnalyzer`, `QrCodeHelper`, `comparators/*`; `ScannerActivity`, `TransferEntriesActivity`, `QrDecodeTask` | **477** (0) | 21 (`S_MAIN_*`, main dialogs, `S_SCANNER*`, `S_TRANSFER_*`) | `S_ENTRY` (launcher, deep link, share, shortcut, tiles); SECURITY results; EDIT results (`169-183`); SETTINGS result → `recreate` (`467-472`); IMPORT → `TransferEntriesActivity` (`ImportExportPreferencesFragment.java:350-391`) |
| **4 EDIT / ICONS** | `EditEntryActivity` (+inner), `AssignIconsActivity` (+inner), `IconPickerDialog` (+inner), `ui/views/Icon*`, `ui/views/AssignIcon*`, `ui/models/AssignIconEntry`, `icons/*`, `IconPacksManagerFragment` + `Hilt_IconPacksManagerFragment`, tasks `ImportIconPackTask`, `IconOptimizationTask`, `ui/glide/*`, `com/bumptech/glide/Generated*`, `com/amulyakhare/**`, helpers `BitmapHelper`, `TextDrawableHelper` | **522** (196 Glide generated) | 19 (`S_EDIT_*`, `S_ICON_*`, `S_ASSIGN_ICONS*`, `S_PREF_ICON_PACKS_*`) | MAIN → editor (`MainActivity.java:502-520`), → assign icons (`522-531`), → `IconOptimizationTask` (`766-781`); SETTINGS → icon packs page; IMPORT → `AssignIconsActivity` (`ImportEntriesActivity.java:320-340`); entry rows → `GlideHelper.loadEntryIcon` |
| **5 SETTINGS** | `PreferencesActivity` (+inner), `PreferencesFragment` + `Hilt_PreferencesFragment`, `MainPreferencesFragment`, `AppearancePreferencesFragment`, `BehaviorPreferencesFragment`, `BackupsPreferencesFragment`, `AuditLogPreferencesFragment` + Hilt base, `GroupManagerActivity` (+inner), `ui/views/Group*`, `ui/views/AuditLog*`, `ui/models/AuditLogEntryModel`, `AboutActivity`, `LicensesActivity`, `ChangelogDialog`, `LicenseDialog`, `SimpleWebViewDialog` | **190** (23 Hilt) | 29 (`S_PREFS_*`, appearance/behavior/backups/audit/groups/about pages and dialogs) | MAIN overflow Settings/About (`1086-1092`), error-card dialogs → Backups (`1163-1197`) |
| **6 IMPORT / EXPORT** | `importers/*` (all 24 files), `ImportEntriesActivity` (+inner), `ImportExportPreferencesFragment` (+inner), `ui/views/ImportEntr*`, `ui/models/ImportEntry`, `ui/components/DropdownCheckBoxes`, tasks `ExportTask`, `RootShellTask`, `Argon2Task`, `PBKDFTask` | **424** (0) | 12 (`S_PREF_IMPORT_EXPORT`, importer/export dialogs, `S_IMPORT_ENTRIES_*`) | SETTINGS section entry; SECURITY `WelcomeSlide` → `AegisImporter` (`WelcomeSlide.java:57-96`) |

Ownership rules: CORE owns shared infrastructure (base classes, singletons `VaultManager`/`IconPackManager` providers, `Preferences`, Room, utilities, `Dialogs`, progress tasks) and the shared dialog pages; other areas model calls into CORE as `CALL` edges and add `@CONTEXT` variants of the shared pages for their own callers. A page's owner writes its `ENTERS` and GUI edges; the area that launches it writes the `INTENT`/`CALL` edge into it.

Leftovers (assigned but contributing 0 JaCoCo methods): `JacocoInstrument` (3 classes, out of scope); interfaces and listener types (e.g. `Dialogs$*Listener`, `EntryAdapter$Listener`, `IntroActivityInterface`, `ItemTouchHelperAdapter`, `Transferable`, task `Callback`s); `@DaggerGenerated` classes (5 `AegisModule_*Factory`, 5 `*_MembersInjector`, `DaggerAegisApplication_HiltComponents_SingletonC`); `*_GeneratedInjector`/`HiltWrapper_*`/component `Builder`/`BuilderModule` interfaces; 12 synthetic switch-map classes (`EventType$1`, `GoogleAuthProtos$1`, `GroupPlaceholderType$1`, `PassReminderFreq$1`, `SortCategory$1`, `ViewMode$1`, `AuditLogDao_Impl$2`, `IconType$1`, `GoogleAuthInfo$1`, `AuditLogHolder$1`, `EntryAdapter$5`, `EntryHolder$2`). CORE is the largest area, but about a third is generated and most of the rest is model code with direct `CALL` edges; if a seventh agent is available, split CORE into CORE-UI (app/DI, base activity, prefs, dialogs, helpers, receivers/services/agent, `ImportFileTask`, `NoAutofillEditText`: 440) and CORE-MODEL (vault, otp, protos, encoding, util, database: 580).

## 7. Baseline coverage by area and screen

| Area | Methods | Monkey only | APE only | Both | Neither | Screens never reached (likely reason) |
|---|---|---|---|---|---|---|
| 1 CORE | 1020 | 45 | 18 | 210 | 747 | `S_SYS_PERMISSION` for Monkey, `S_QS_PANEL`, backup agent, receivers' `onReceive` (no screen-off/boot/backup); shared dialogs mostly unused because the features calling them were unreached; otp/encoding/protos 0/303 (no entries) |
| 2 SECURITY | 324 | 13 | 0 | 69 | 242 | `S_INTRO_SETUP_*` beyond the toast (passwords never equal), `S_INTRO_SETUP_BIOMETRIC` (no enrolled biometric), Welcome import (picker blocked), all `S_AUTH_*` (never encrypted), `S_PREF_SECURITY_ENCRYPTED`, panic (needs trusted sender); APE: data wipe kept it in the intro |
| 3 MAIN | 477 | 0 | 26 | 174 | 277 | `S_MAIN_LIST`, both selection modes, all entry dialogs, `S_TRANSFER_*` (empty vault); `S_DLG_CLIPBOARD_IMPORT` (Enter manually never tapped); scanner without QR; Monkey never tapped a FAB item or submitted a search |
| 4 EDIT / ICONS | 522 | 21 | 0 | 17 | 484 | all `S_EDIT_*` (FAB item never tapped, no entries to edit), `S_ICON_PICKER*`, `S_ASSIGN_ICONS` (no icon pack, no entries); icon packs page empty only (Monkey; import picker blocked) |
| 5 SETTINGS | 190 | 80 | 0 | 28 | 82 | all `S_PREF_BACKUPS_*` (never opened; most items need encryption), `S_GROUPS_LIST` (no groups), `S_PREF_AUDIT_LOG_LIST` (no events); APE never left `S_PREFS_MAIN` |
| 6 IMPORT / EXPORT | 424 | 50 | 0 | 0 | 374 | `S_IMPORT_ENTRIES_LIST`, importer prompts, `S_DLG_IMPORT_ASSIGN_ICONS` (file picker blocked; root missing for app import), export completion (dialog opened, OK/Share never pressed; GA-style export → "no data" toast with an empty vault) |
| **Total** | **2957** | **209** | **44** | **498** | **2206** | Monkey 707, APE 542, either 751 (matches the brief) |

Per-package totals (methods / Monkey / APE, DATA): `aegis` root 433/133/120, `crypto` 42/3/3, `crypto/bc` 11/0/0, `crypto/otp` 18/0/0, `database` 46/19/13, `encoding` 10/0/0, `helpers` 122/57/62, `helpers/comparators` 10/1/5, `icons` 41/3/2, `importers` 271/15/0, `otp` 88/0/0, `receivers` 8/3/3, `services` 12/0/0, `ui` 404/113/94, `ui/components` 23/9/0, `ui/dialogs` 99/23/0, `ui/fragments/preferences` 207/97/15, `ui/glide` 213/8/8, `ui/intro` 40/32/32, `ui/models` 26/4/4, `ui/preferences` 7/3/0, `ui/slides` 37/21/21, `ui/tasks` 91/3/0, `ui/views` 341/106/99, `util` 33/6/5, `vault` 198/40/48, `vault/slots` 42/1/1, textdrawable 33/0/0, Glide generated 8/7/7, Hilt markers 16/0/0, guardianproject 26/0/0.

Generated classes JaCoCo does report (and their hits): `Hilt_AegisApplication(+$1)` 7/7, `Hilt_AegisActivity(+$1)` 13 → 11 hit, `Hilt_PreferencesFragment` 11 → 10, `Hilt_AuditLogPreferencesFragment` and `Hilt_IconPacksManagerFragment` 12 → 10 (Monkey only), `Hilt_VaultLockReceiver` 3 → 1, `AegisApplication_HiltComponents$*C` constructors (Activity/ActivityRetained/Fragment/Singleton hit; Service/View/ViewModel/ViewWithFragment not), 18 nested `DaggerAegisApplication_HiltComponents_SingletonC$*` classes (65 methods; Service/View/ViewModel builders and impls 0), `AegisApplication_ComponentTreeDeps` and all `hilt_aggregated_deps`/`dagger/hilt/**` markers 0, Room `AppDatabase_Impl(+$1)`, `AuditLogDao_Impl(+$1)` partly, Glide `GlideApp` 0/14, `GlideOptions` 5/73, `GlideRequest` 0/67, `GlideRequests` 2/22, `GeneratedAppGlideModuleImpl` 5/6, `GeneratedRequestManagerFactory` 2/2, `GoogleAuthProtos*` 0/187.

## 8. Conclusions and recommendations

1. **For the graph agents**: start CORE and SECURITY first (they define `S_ENTRY`, lifecycle, the shared dialog pages and the intro/auth gate), then run MAIN, EDIT, SETTINGS and IMPORT in parallel. Model the intro and unlock as `needs_state`-free first paths, and everything that requires an entry, an encrypted vault, an icon pack or a picker result with explicit guards/`needs_state` (e.g. "vault holds ≥1 entry", "vault encrypted", "icon pack installed", "picker returned a file"), so that the reachable-but-missed targets are not mistaken for dead code.
2. Use the JaCoCo universe (2,957) as the method list and keep the 145 filtered methods with blank hit flags; mark `RootShellTask`, `RawSlot`, `BuildConfig` as "not observable" instead of "missed".
3. **For the study harness**: seed the vault (plaintext, with groups) and keep app data across tool restarts; provide QR images, importer samples, an icon pack and an encrypted-vault configuration; allow the tools to leave the package for DocumentsUI, or the file-based features (intro import, import from file, export, backups, icon packs, custom icons, scan image) stay unreachable for every tool. Report APE's data wipe and Monkey's single-process run when comparing against the baseline.
4. **Code oddities seen while reading (hazard candidates, not reproduced)**: `SwitchPreference.setChecked(boolean)` ignores its argument and always checks the switch (`SRC/ui/preferences/SwitchPreference.java:34-36`); `AssignIconsActivity` throws if started without icon packs (`SRC/ui/AssignIconsActivity.java:101`, e.g. after a pack is removed and the activity is recreated); `SecuritySetupSlide.onResume` and `IntroActivity.onDonePressed` throw on inconsistent intro state (`SecuritySetupSlide.java:93-95`, `IntroActivity.java:92-97`); `EditEntryActivity` throws for an unknown OTP type (`EditEntryActivity.java:271,357,785`).
5. Open questions (UNVERIFIED): what cleared APE's app data at t≈3.1 min; the cause of APE's 2 crashes; why three classes were left uninstrumented; whether the emulator image grants CAMERA at install and offers a QR in the virtual camera scene.
