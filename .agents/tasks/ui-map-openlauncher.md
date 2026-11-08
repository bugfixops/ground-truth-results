# openlauncher 0.3.1 (#67): UI map and modeling plan (read-only investigation)

## Summary

- OpenLauncher is a home-screen app. It has **two entry activities**: `Init` (MAIN/LAUNCHER: the app icon; it shows a 3-page onboarding intro on the first run, then always forwards to `Home`) and `Home` (MAIN/HOME/DEFAULT, singleTask, portrait-locked). Being the **default home app is not needed** to reach the UI, because `Init` starts `Home` with an explicit intent. There is no Application class, no service, no login, no database in use, no network feature.
- Almost all UI lives in **one Activity (`Home`)** that stacks overlays: desktop pager, dock, an app drawer (Paged by default, Vertical after a setting change), a left "minibar" drawer, a folder popup, a drag-target bar and a desktop edit mode. The other screens are `SettingsActivity` (7 categories built with the in-APK library `MaterialPrefFragment`), `AboutActivity`, `HideAppsActivity`, `MinibarEditActivity`, plus about 15 dialogs.
- Proposed graph: **53 base pages** plus `@` variants (§3.4). Method universe: **901 methods in JaCoCo** (899 without `BuildConfig`); `tools/list_methods.py` yields **934** (35 extra compiler-generated enum/switch-map methods JaCoCo filters).
- Setup gates: the intro (one tap), a silent and always-denied `READ_CALL_LOG` request (the permission is not declared, so the quick-contacts code can never run), `READ_EXTERNAL_STORAGE` for backup/icon packs, and several **environment gates**: the system widget picker (outside the package), an installed icon pack, an `INSTALL_SHORTCUT` broadcast, device-admin activation, package install/remove events, and settings that must be changed and then trigger a `Home` restart (Vertical drawer, gestures, Show-All-Apps).
- Baseline: Monkey hit 351, APE 485, either 520 of 901. **Monkey never long-presses**, so it missed desktop edit mode, every drag-and-drop, folders and the Hide-apps screen (APE reached them). **APE never opened the minibar** (an edge swipe), so it missed `MinibarEditActivity`. Neither run placed a widget or shortcut, created a 2nd desktop page, opened the Vertical drawer, the minibar popups, or the wallpaper / RAM / lock / volume actions.
- Of the 381 methods neither run hit: ~139 are dead-code candidates, 25 are blocked by the undeclared permission, 13 look framework-only, 4 need a hardware configuration change, ~67 need an environment setup, and ~133 are reachable through the GUI but were missed. Estimated tool targets (reachable, missed by Monkey) ≈ **370** (169 APE-only + ~200 never hit).
- Decomposition: 3 areas. **A** Shell + shared infrastructure (417 methods, of which ~100 are trivially dead), **B** Desktop surface / drag-and-drop / folders / widgets (335), **C** Settings and secondary activities (149). Rule: an edge is written by the area that owns its destination method (ENTERS edges by the owner of the source method); pages are global and defined in §3.4.

## Conventions

- `APP` = `/Users/darshan/Desktop/yang/work/final_java_only/openlauncher/app/openlauncher-#67/app`. Java files are cited relative to `APP/src/main/java/com/benny/openlauncher/` (for example `activity/Home.java:202`); the vendored gesture library as `sfg/SimpleFingerGestures.java:68` (= `APP/src/main/java/in/championswimmer/sfg/lib/...`); `AndroidManifest.xml:NN` = `APP/src/main/AndroidManifest.xml`; `res/...` = `APP/src/main/res/...`; library sources as `libs/materialpreffragment/.../MaterialPrefFragment.java:NN`.
- `APK-MANIFEST` = the compiled manifest of `openlauncher-0.3.1-#67-rebuilt.apk`, decoded read-only with `/opt/homebrew/bin/apkutils manifest`. `DEX-XREF` = call sites found in the APK's dex with `apkutils xref` (library code that is not in the class directory).
- Coverage flags: `MA` hit by Monkey and APE, `M-` Monkey only, `-A` APE only, `--` neither. Method level from `monkey|ape/report/report.xml` (METHOD counter); line level from the same XML's `<sourcefile><line ci>` data, cited as `Lnnn MA`.
- Evidence labels as in `GRAPH_PROMPT.md`: `SRC` (read), `FW-MEMORY` (Android/library behaviour recalled, not checked), `INFERRED`, `UNVERIFIED`. No framework source was available, so nothing is `FW-SRC`.
- Method names follow `tools/list_methods.py` short names (`Home$CallLogObserver.onChange(boolean,Uri)`).

## 1. Entry points

No merged manifest exists under `APP/build/intermediates` (only `javac/` classes). The table uses `AndroidManifest.xml` (the only flavor built is `flavorDefault`, see `class_files.json` and `APP/build.gradle:27-33`; no `src/flavor*` source sets exist) and was cross-checked against `APK-MANIFEST`, which adds library entries (marked *merged*).

### 1.1 Components

| Component | Kind | Exported | Intent filters / protection | Launch / window attributes | Theme | Notes |
|---|---|---|---|---|---|---|
| *(application)* | — | — | — | `taskAffinity=""` (all activities), `stateNotNeeded=true`, `launchMode=singleTask` on `<application>` (not a valid application attribute, ignored: FW-MEMORY); merged: `debuggable=true`, `supportsRtl=true` (`AndroidManifest.xml:15-24`, APK-MANIFEST) | `Home.Light` (AppCompat Light NoActionBar, shows wallpaper, transparent background, `res/values/styles.xml:3-17`) | **No `android:name` → no custom Application class.** `meta-data android.max_aspect=2.1` (`:26`) |
| `activity.Init` | Activity | yes (has filter) | MAIN + LAUNCHER (`:28-36`) | `clearTaskOnLaunch` (`:30`) | app theme | Extends AndroidOnboarder `OnboarderActivity` (library). Listed in the app drawer as **"OLSettings"** (`util/AppManager.java:267-268`) |
| `activity.Home` | Activity | yes | MAIN + HOME + DEFAULT (`:48-53`) | `singleTask`, `clearTaskOnLaunch`, `stateNotNeeded`, `taskAffinity=""`, `screenOrientation=portrait`, `configChanges=orientation\|keyboard\|screenSize`, `windowSoftInputMode=adjustNothing` (`:38-47`) | app theme | The launcher itself |
| `activity.AutoFinishActivity` | Activity | no | none | — | `@android:style/Theme.Translucent.NoTitleBar.Fullscreen` (`:63-65`) | Calls `finish()` in `onCreate` (`activity/AutoFinishActivity.java:10-13`); only started by the provider below |
| `activity.MinibarEditActivity` | Activity | no | none | `parentActivityName=Home` (`:66-70`) | `NormalActivity.Light` | label "Edit Item" |
| `activity.SettingsActivity` | Activity | no | none | `configChanges=orientation\|keyboard\|screenSize` (`:71-75`) | `NormalActivity.Light` | label "Settings" |
| `activity.HideAppsActivity` | Activity | no | none | `enabled=true` (`:77-81`) | `NormalActivity.Light` | rotation allowed (no configChanges) |
| `activity.AboutActivity` | Activity | no | none | — | `AppTheme.MaterialAboutActivity` (`:100-103`) | Extends material-about-library `MaterialAboutActivity` |
| `cat.ereza.customactivityoncrash.activity.DefaultErrorActivity` | Activity (*merged*, library) | no | none | `process=":error_activity"` (APK-MANIFEST) | library | Shown after an uncaught exception once `Home.onCreate` installed the handler (`activity/Home.java:184-187`). Library code, out of scope |
| `util.FiveSecsDelayContentProvider` | ContentProvider | **yes** (`:56-61`) | authority `com.benny.openlauncher.util.FiveSecsDelayContentProvider`, `grantUriPermissions` | — | — | For Kustom apps: `delete(.../reset5secs)` starts `AutoFinishActivity` only if the caller is `org.kustom.wallpaper` or `org.kustom.widget` (`util/FiveSecsDelayContentProvider.java:49-62, 79-86`); `query/insert/update` throw `UnsupportedOperationException` |
| `android.support.v4.content.FileProvider` | ContentProvider (library class) | no (`:105-113`) | authority `com.benny.openlauncher.provider`, `res/xml/file_paths.xml` | — | — | No app code uses it (no `getUriForFile`/`FileProvider` reference in `src/main/java`) |
| `util.DeviceAdminReceiver` | Receiver | yes, but `permission=BIND_DEVICE_ADMIN` (`:84-93`) | `DEVICE_ADMIN_ENABLED`; meta-data `res/xml/device_admin.xml` (`force-lock`) | — | — | Extends plain `BroadcastReceiver`; `onReceive` is empty (`util/DeviceAdminReceiver.java:9-11`) |
| `util.ShortcutReceiver` | Receiver | **yes** (`:95-98`) | **no filter** (only explicit broadcasts reach the manifest instance) | — | — | Same class is also registered at runtime for `INSTALL_SHORTCUT` (§1.2). Dereferences `Home.launcher` without a null check (`util/ShortcutReceiver.java:48-64`) |
| `JacocoInstrument.SMSInstrumentedReceiver` | Receiver | yes | `edu.gatech.m3.emma.COLLECT_COVERAGE` (`:115-119`) | — | — | Coverage harness, **excluded**. The baseline broadcasts it at t=0 (`monkey/coverage/00000.json`), which starts the process before the tool runs |

Permissions (`AndroidManifest.xml:10-13`, APK-MANIFEST): `SET_WALLPAPER`, `KILL_BACKGROUND_PROCESSES`, `READ_EXTERNAL_STORAGE`, `WRITE_EXTERNAL_STORAGE`; merged adds `INTERNET` (from a library). `CALL_PHONE`, `READ_CONTACTS`, `READ_CALL_LOG` are **commented out** (`AndroidManifest.xml:4-8`). minSdk 16, targetSdk 25 (`APP/build.gradle:16-17`), so runtime permissions apply on the API 27 emulator.

Not present: services, VIEW/deep-link/SEND/file-type filters, search, app shortcuts XML, app-widget providers (the app is a widget *host*), notifications, dialog-themed activities.

### 1.2 Entry points registered in code (only while a `Home` instance is alive)

| Receiver | Registered | Actions | Handler | Unregistered |
|---|---|---|---|---|
| `Home$1` (anonymous) | `activity/Home.java:641` in `registerBroadcastReceiver` (called from `init`, `:257`) | `TIME_TICK`, `TIMEZONE_CHANGED`, `TIME_CHANGED` (`:164-168`) | `Home$1.onReceive` → `updateDesktopClock` only for TIME/TIMEZONE changes (`:155-160`); TIME_TICK arrives every minute and does nothing else | **never** (leak; `onDestroy` unregisters only the other two, `:691-692`) |
| `AppUpdateReceiver` | `:640` | `PACKAGE_ADDED/REMOVED/CHANGED`, scheme `package` (`:170-174`) | `AppUpdateReceiver.onReceive` → `AppManager.onReceive` → `getAllApps` (`util/AppUpdateReceiver.java:9-11`, `util/AppManager.java:155-157`) | `:691` |
| `ShortcutReceiver` | `:642` | `com.android.launcher.action.INSTALL_SHORTCUT` (`:176-177`) | `ShortcutReceiver.onReceive` (`util/ShortcutReceiver.java:24-65`) | `:692` |

Other callbacks the system drives: `ContentObserver` `Home$CallLogObserver` (never registered in practice, §5.2), `AppWidgetHost` (`viewutil/WidgetHost.java`), `DrawerLayout.DrawerListener` (`Home` implements it, `activity/Home.java:235, 846-877`).

### 1.3 How S_ENTRY should work for a launcher

1. **Launcher icon / `monkey -p` / `am start -n .../.activity.Init`** → `Init.onCreate`. If `SharedPreferences("quickSettings").firstStart` is true (default) it builds the 3-page onboarding (`activity/Init.java:20-51`) → page `S_INTRO`. Skip or Finish (library buttons; DEX-XREF: both `onSkipButtonPressed` and `onFinishButtonPressed` are called from `OnboarderActivity.onClick`) → `Init.RockIt` writes `firstStart=false`, starts `Home` with `FLAG_ACTIVITY_NO_ANIMATION` and finishes `Init` (`:55-76`). On every later launch `Init.onCreate` calls `RockIt` immediately (`:20-23`), so `Init` never shows a UI again.
2. **HOME intent** (HOME key, boot, or the system restarting home after a crash or `System.exit`) → `Home` directly, skipping `Init` and the intro. This needs OpenLauncher to be the **default home app**. With Launcher3 and OpenLauncher installed and no preference set, Android shows the "Select a home app" chooser (ResolverActivity, Just once / Always) (FW-MEMORY). `Home` is `singleTask`: if it already exists the HOME intent is delivered as pause → `onNewIntent` (not overridden) → `onResume`, which runs `handleLauncherPause()` (FW-MEMORY for the callback order; `activity/Home.java:744-765` for what it does). A singleTask start also destroys activities above `Home` in its task (e.g. `SettingsActivity`, whose `onDestroy` may then recreate `Home`, `activity/SettingsActivity.java:296-299`) (FW-MEMORY).
3. **First `Home` creation in a process** shows the loading splash while `LauncherSettings.readSettings` runs in an `AsyncTask` (`activity/Home.java:202-228`): page `S_HOME_LOADING`. Later creations in the same process (`recreate()` from Settings/Hide apps/icon pack, or a second launch) skip it because `LauncherSettings.init` is already true (`util/LauncherSettings.java:130`; `activity/Home.java:202-204`).
4. **Back never leaves `Home`**: `onBackPressed` only closes drawers and calls `handleLauncherPause()` (`activity/Home.java:738-741`). If OpenLauncher is not the default home, HOME takes the user to the other launcher (`S_HOME_PAUSED`).
5. Under the baseline tools (`-p com.benny.openlauncher`), Monkey's activity controller **refuses to start activities of other packages** and the caller receives `RESULT_CANCELED` with no data (FW-MEMORY, Monkey `ActivityController.activityStarting`). Coverage supports this: `Home.onActivityResult` ran only its cancel branch with `data == null` (`activity/Home.java:708 -A`, `714 -A`, `715-718 --`), although a user cancelling the system widget picker returns data with the widget id (FW-MEMORY) (INFERRED). So everything behind the widget picker, the permission dialog, the wallpaper chooser, system Settings, app info and uninstall screens is invisible to Monkey/APE.

### 1.4 Proposed edges out of S_ENTRY

| Edge | Kind | Trigger | Guard / needs_state | Evidence |
|---|---|---|---|---|
| S_ENTRY → `Init.<init>`, `Init.onCreate` | ENTRY | tap the OpenLauncher icon in another launcher, or `monkey -p`, or `am start` | then branch on `pref:quickSettings.firstStart` | SRC `AndroidManifest.xml:28-36`, `activity/Init.java:17-53` |
| S_ENTRY → `Home.<init>`, `Home.onCreate@FIRST` | ENTRY | HOME key / boot / system restart of home | needs_state "OpenLauncher is the default home app" | SRC `AndroidManifest.xml:38-53`; FW-MEMORY |
| S_ENTRY → `FiveSecsDelayContentProvider.<init>`, `.onCreate` | ENTRY | process start (providers are created before any component, FW-MEMORY); both runs hit them (MA) | none | SRC `util/FiveSecsDelayContentProvider.java:20-23` |
| S_ENTRY → `FiveSecsDelayContentProvider.query/insert/update/getType/delete` | ENTRY | another app or `adb shell content ...` on the exported authority | `delete` → `AutoFinishActivity` only if caller package is `org.kustom.wallpaper/widget`, else `SecurityException` (`:79-86`) | SRC; UNVERIFIED whether `content gettype` exists on API 27 |
| S_ENTRY → `ShortcutReceiver.<init>`, `.onReceive@EXPLICIT` | ENTRY | explicit broadcast to the exported manifest receiver | returns at `:25` if no extras; NPE crash at `:48` if `Home.launcher == null` | SRC `AndroidManifest.xml:95-98` |
| S_ENTRY → `DeviceAdminReceiver.<init>`, `.onReceive` | ENTRY | system sends `DEVICE_ADMIN_ENABLED` after the user activates the admin in system Settings (or `adb shell dpm set-active-admin com.benny.openlauncher/.util.DeviceAdminReceiver`, FW-MEMORY) | protected by `BIND_DEVICE_ADMIN` | SRC `AndroidManifest.xml:84-93` |
| any Home page → `Home$1.onReceive`, `AppUpdateReceiver.onReceive`, `ShortcutReceiver.onReceive@DYNAMIC` | SYSTEM | minute tick / time or timezone change; any app installed, removed, changed; an `INSTALL_SHORTCUT` broadcast | `Home` alive (registered in `init`) | SRC §1.2 |
| any page → `S_CRASH` | SYSTEM | uncaught exception after `CustomActivityOnCrash.install` (`activity/Home.java:184-187`; DEX-XREF: `install` is called only from `Home.onCreate`) | `setEnableAppRestart(false)`, `setShowErrorDetails(true)` | SRC; library behaviour FW-MEMORY |

## 2. First-run flow and setup gates

### 2.1 Startup sequence (first run, launched from the icon)

1. Process start → `FiveSecsDelayContentProvider.<init>/onCreate` (MA).
2. `Init.onCreate` → onboarding (3 pages: "OpenLauncher", "Minibar", "Settings", `res/values/strings.xml:27-36`) → Skip / Finish → `RockIt` → `Home` (`activity/Init.java:17-76`). Monkey only pressed Skip (`Init.onSkipButtonPressed MA`, `onFinishButtonPressed -A`).
3. `Home.onCreate`: installs the crash handler, sets `Home.resources` and `Home.launcher` (static), clears `AppManager` listeners, inflates `activity_home`, `ButterKnife.bind(this)` (reflection loads `Home$$ViewBinder`; the dex strings of `ButterKnife.findViewBinderForClass`, read with `apkutils mtds`, include `"$$ViewBinder"` and "Loaded view binder class"), shows the splash and starts `Home$2` (`activity/Home.java:181-231`).
4. `Home$2.doInBackground` → `LauncherSettings.readSettings` reads `files/generalSettings.json`, `dockData.json`, `desktopData.json` with Gson (missing files are fine) (`util/LauncherSettings.java:126-156`). `onPostExecute` → `init()`; if a JSON type error occurred, an alert "Some settings can't be read" (`activity/Home.java:223-226`, `--` in both runs).
5. `Home.init` (`:234-295`): drawer listener, `WidgetHost` + `startListening`, `initViews` (minibar adapter, quick-center RecyclerView, edge drag zones, clock, app drawer, desktop pager, dock, drag bar, drawer callbacks), system-bar padding, registers the 3 receivers, adds `AppManager` listeners, `AppManager.init()` (starts `AsyncGetApps`), `initSettings()`.
6. `initQuickCenter` requests `READ_CALL_LOG` every time (`:617-624`) → the request is auto-denied because the permission is not declared (FW-MEMORY) → `Home.onRequestPermissionsResult` runs but its branch needs `callLogObserver != null`, which is never true (`:628-637`; `L629 MA`, `L631-634 --`).
7. `AppManager$AsyncGetApps` loads all launcher activities sorted by label, filters `hiddenList`, applies an icon pack if one is set and installed (`util/AppManager.java:159-252`). `onPostExecute` calls `Home$3.onAppUpdated`: on the very first launch (`generalSettings.firstLauncher`, Normal mode) it puts the round **"All Apps" button** at dock x=2, then fills desktop and dock (`activity/Home.java:260-277`, `L265-270 MA`). `AppDrawer_Paged$1.onAppUpdated` builds the drawer pages (`widget/AppDrawer_Paged.java:102-111`).
8. The user is now on `S_HOME_DESKTOP`: empty desktop page, dock with the All Apps button, clock text at the top. On every `onStop` the settings are written back (`activity/Home.java:731-735` → `util/LauncherSettings.java:231-268`).

### 2.2 Gates

| # | Gate | Enforced by | What it blocks | Harness action |
|---|---|---|---|---|
| G1 | Onboarding intro | `activity/Init.java:20-51` (`quickSettings.firstStart`) | `Home` on the icon path until Skip/Finish | tap Skip once, or pre-set the pref via `run-as` (APK is debuggable, APK-MANIFEST) |
| G2 | Async settings + app-list load | `activity/Home.java:202-228`; `util/AppManager.java:101-108, 220-251` | desktop, dock and drawer contents appear only after two `AsyncTask`s | wait ~1-2 s after launch |
| G3 | `READ_CALL_LOG` not declared | `AndroidManifest.xml:4-8` vs `activity/Home.java:617-624` | `Home$CallLogObserver`, quick contacts, `RoundDrawable`, `Tool.fetchThumbnail*` | none possible (cannot be granted to an undeclared permission, FW-MEMORY) |
| G4 | `READ_EXTERNAL_STORAGE` runtime permission | `activity/SettingsActivity.java:368-374`; `util/AppManager.java:138-146` | Backup/Restore dialog, choosing an icon pack | `adb install -g` or `pm grant ... READ_EXTERNAL_STORAGE` and `WRITE_EXTERNAL_STORAGE` (backup writes to `/sdcard/OpenLauncher/`, `util/DialogUtils.java:147-158`). The APE run evidently had it granted: `SettingsActivity L370 -A`, request branch `L372 --` (INFERRED: installed with grants) |
| G5 | Settings must be changed, then `Home` recreated | `activity/SettingsActivity.java:291-299, 325-330` (`requireLauncherRestart` → `Home.recreate()`); `widget/AppDrawerController.java:172-205` reads `drawerMode` only at init | Vertical drawer + search (`drawerMode`, `drawerSearchBar`), Show-All-Apps desktop, label/grid/fullscreen changes | choose in Settings and press Back to leave Settings, or pre-write `generalSettings.json` |
| G6 | Gesture actions default to "None" | `util/LauncherSettings.java:283-289` (`swipe=false`, `singleClick..swipeUp=0`) | desktop tap / double-tap / pinch / swipe actions do nothing; swipe-up does not open the drawer | Settings › Gestures, or `generalSettings.json` |
| G7 | System widget picker is another package | `activity/Home.java:647-652, 707-721` | widget items, resize handles, widget drag | allow leaving the package / UI automation of the system picker (and of configure activities) |
| G8 | Icon pack app installed | `util/AppManager.java:111-117` (category `com.anddoes.launcher.THEME`), `:213-215` | `AppManager$2`, `IconPackHelper` | install any ADW/Nova-style icon pack APK |
| G9 | Shortcut broadcast | `activity/Home.java:176-177, 642`; `util/ShortcutReceiver.java:24-65` | shortcut items and their handlers | a helper app sending `INSTALL_SHORTCUT` with a Parcelable `EXTRA_SHORTCUT_INTENT` (`am broadcast` cannot pass an Intent extra; without it `newShortcutItem` NPEs, `widget/Desktop.java:719-731`) (FW-MEMORY) |
| G10 | Device admin | `util/LauncherAction.java:73-82` | real lock screen; `DeviceAdminReceiver` | `dpm set-active-admin` (FW-MEMORY). Then `LockScreen` really locks the device: the harness must unlock |
| G11 | Default home app | §1.3 | HOME-key returns to `Home`, system restart of `Home` after `System.exit`/crash | `cmd package set-home-activity com.benny.openlauncher/.activity.Home` (FW-MEMORY, UNVERIFIED on API 27) or the chooser's "Always" |
| G12 | Process restart with saved data | `util/LauncherSettings.java:45-111` run only on the first `Home` creation of a process | Gson read path (`Desktop$SimpleItem.<init>()`, `Desktop$Item.<init>(SimpleItem)`, `getActionsFromString`, `Tool.split` for folders) | kill/restart the app after a change (Monkey never did: `Desktop$SimpleItem.<init>() -A`) |
| G13 | Corrupt settings file | `util/LauncherSettings.java:134-142` | `S_DLG_SETTINGS_ERROR` (`Tool$DialogHelper.alert --`) | write e.g. `{"iconSize":"x"}` into `files/generalSettings.json` (a JSON type error is caught and reported; a malformed array may instead crash, UNVERIFIED) |

There is **no** login, account, password, vault, database creation or data import. `_fixtures/` files are not needed (no file, media or contacts access); `Pictures/*.jpg` can be used by the system wallpaper picker reached from "Set Wallpaper".

### 2.3 Screens the baseline never reached (details and per-method evidence in §7.3)

| Screen | Monkey | APE | Most likely gate |
|---|---|---|---|
| Desktop edit mode, edit-panel buttons, Action popup, all drag-and-drop pages, folders, rename dialog | no | yes | Monkey sends no long-press (each touch gesture is injected as DOWN…UP without a hold, FW-MEMORY) |
| Minibar (left drawer), `MinibarEditActivity` | yes | no | APE never performed the left-edge swipe (`Home.onDrawerStateChanged M-`) |
| Settings › Colors / Icons / Other, Hide apps, icon-pack dialog, backup dialog | no | yes | Monkey only opened the first 4 categories (`SettingsActivity L58-109 MA`, `L111-134 -A`) |
| Vertical drawer and its search | no | no | G5 (needs the setting plus a `Home` recreation) |
| Minibar popups (RAM info, volume sliders) | no | no | needs a horizontal fling on a minibar row (`SwipeListView$1.onFling --`) |
| Wallpaper dialog; ClearRam, LockScreen, DeviceSettings, Volume actions | no | no | only reachable from the minibar or from configured gestures (G6); Monkey's minibar taps executed only EditMinBar and OpenAppDrawer (`LauncherAction L44-46 M-`, `L134 M-`, all other cases `--`) |
| Widget on the desktop, widget resize/drag | no | no | G7 (picker blocked; `WidgetHost.onCreateView --`) |
| Shortcut items | no | no | G9 |
| 2nd desktop page, "Remove page" body | no | no | pages are only added by holding a dragged item at the screen edge for 1 s (`viewutil/DragNavigationControl.java:16-35`, `$1/$2.run --`) |
| Drop on Remove / App info / Uninstall | no | no | drop on the top bar never happened (`widget/DragOptionView.java:101, 125-133, 162-163 --`) |
| Settings-error alert, Restore (`System.exit`), Settings › Restart | no | no | G13; `DialogUtils$9.onSelection --`; `SettingsActivity L326-330 --` |
| `AutoFinishActivity`, device admin, package/shortcut receivers | no | no | external events only (§1.4) |

### 2.4 What a harness should prepare

1. Install with runtime permissions granted (`adb install -g`); `READ_CALL_LOG` cannot be granted.
2. Either keep a fresh install (to exercise `S_INTRO`) or pre-set `quickSettings.firstStart=false`.
3. Decide about the default home (G11). Making OpenLauncher default lets HOME presses and process restarts land back in `Home` instead of Launcher3.
4. Let tools/UI automation operate system activities: widget picker and widget configure screens, permission dialog, wallpaper chooser, Settings, app info, uninstall dialog, device-admin settings, browser.
5. Install: one icon pack; 1-2 extra launchable apps (more drawer pages; an app to uninstall for `PACKAGE_REMOVED` → `AppUpdateReceiver`, `Home$4.onAppDeleted`); a helper that can send `INSTALL_SHORTCUT`, and optionally a helper with package name `org.kustom.widget` that calls `ContentResolver.delete(content://com.benny.openlauncher.util.FiveSecsDelayContentProvider/reset5secs)`. Which widget providers ship on the API 27 image is UNVERIFIED (the dataset machine was not inspected).
6. Optional presets through files (via `run-as`, or by placing `desktopData.json`, `dockData.json`, `generalSettings.json` in `/sdcard/OpenLauncher/` and using Settings › Other › Backup › Restore, which calls `System.exit(1)`, `util/DialogUtils.java:163-180`): `drawerMode:"Vertical"`, `desktopMode:"ShowAllApps"`, gesture values 1-8 (`res/values/arrays.xml:7-28`), `swipe:true`, desktop data with a GROUP/SHORTCUT item (shortcut icons live in `files/iconCache/<id>`, `util/Tool.java:229-277`).

## 3. Screens and navigation

### 3.1 Window inventory

**Activities (6 app + 1 library).** `Init` (onboarding), `Home` (everything below), `SettingsActivity`, `AboutActivity`, `HideAppsActivity`, `MinibarEditActivity`, `AutoFinishActivity` (invisible, finishes at once); library `DefaultErrorActivity` (crash screen).

**Fragments.** Live: `HideAppsFragment` (single page of `HideAppsActivity`'s `ViewPager`, `activity/HideAppsActivity.java:50-54`); library `MaterialPrefFragment` instances for the Settings root and 7 categories (`activity/SettingsActivity.java:41-51, 54-138`). Dead: `fragment/SettingsFragment.java` (`@Deprecated`, its only use is commented out at `activity/SettingsActivity.java:39`), `fragment/MinibarEditFragment.java` (never referenced).

**Overlays inside `Home`** (all in `res/layout/activity_home.xml` / `view_home.xml`):

| Overlay | Class | Shown when | Code |
|---|---|---|---|
| Loading splash | `FrameLayout loadingSplash` + library `LauncherLoadingIcon` | first `Home` creation per process | `activity/Home.java:202-228` |
| Desktop pager | `widget.Desktop` (extends library `SmoothViewPager`), pages are `CellContainer`s | always (hidden while the drawer is open, `Home$5.onEnd`) | `widget/Desktop.java:76-86, 335-541` |
| Dock | `widget.Dock` (a `CellContainer`) | always | `widget/Dock.java` |
| Page indicators | `widget.PagerIndicator` (desktop, drawer) | `showIndicator` / `drawerShowIndicator` | `activity/Home.java:318-319, 546-548` |
| Desktop edit panel | `LinearLayout desktopEditOptionPanel` (Remove, Home, Widget, Action, Settings) | `Desktop.inEditMode` | `res/layout/view_desktop_edit_option.xml`; `activity/Home.java:416-459` |
| App drawer | `widget.AppDrawerController` (circular reveal) containing `AppDrawer_Paged` (pager of `CellContainer` pages) or `AppDrawer_Vertical` (RecyclerView grid + `DragScrollBar`) and, in Vertical mode, a search card with `widget.SearchBar` | `openAppDrawer` / `closeAppDrawer` | `widget/AppDrawerController.java:63-205`; `activity/Home.java:771-810` |
| Drag target bar | `widget.DragOptionView` (Remove, Info, Uninstall) | during any drag | `widget/DragOptionView.java:78-310` |
| Edge drag zones | two `View`s `left`/`right` with `DragNavigationControl` listeners | during any drag | `viewutil/DragNavigationControl.java:14-119`; `res/layout/view_home.xml:50-68` |
| Folder popup | `widget.GroupPopupView` | tap on a folder item | `widget/GroupPopupView.java:96-258` |
| Minibar | `DrawerLayout` start drawer with `widget.SwipeListView minBar` | left-edge swipe, `minBarEnable` | `res/layout/activity_home.xml:5-34`; `activity/Home.java:544, 551-606` |
| Minibar popup / quick center | `RelativeLayout shortcutLayout` with `widget.MiniPopupView` and the (always empty) quick-contacts RecyclerView | visible only while the minibar is open and idle | `activity/Home.java:858-876`; `widget/MiniPopupView.java:52-127` |
| Action popup | `android.support.v7.widget.PopupMenu` with `res/menu/launcher_action.xml` (one item "AppDrawer") | edit panel › Action | `activity/Home.java:491-501` |

**Dialogs** (all `com.afollestad.materialdialogs.MaterialDialog` unless noted): settings-error alert (`activity/Home.java:225`), wallpaper list (`util/LauncherAction.java:47-72`), folder rename input (`widget/GroupPopupView.java:187-200` → `util/Tool.java:463-479`), icon-pack list (`util/AppManager.java:110-153`), desktop style, drawer style, 6 gesture pickers, backup/restore (`util/DialogUtils.java:19-184`), library NUMPref seek-bar dialog (`libs/materialpreffragment/.../MaterialPrefFragment.java:278-300`), library `ColorChooserDialog` (a DialogFragment, `:324-337`), library Snackbar in Hide apps (`fragment/HideAppsFragment.java:137-148`). Toasts are not pages.

**Pagers / tabs.** Desktop pager, Paged drawer, HideApps `ViewPager` with one page and no tab strip, the onboarding pager (library). No TabLayout, no BottomSheet, no action mode, no context menu, no options menu in `Home` (no `onCreateOptionsMenu`; theme without action bar), no navigation graph.

### 3.2 Navigation

| From | Gesture / event | To | Code |
|---|---|---|---|
| S_INTRO | Skip, or Finish on the last page | S_HOME_LOADING | `activity/Init.java:55-76` |
| S_HOME_LOADING | settings + app list loaded | S_HOME_DESKTOP (or S_DLG_SETTINGS_ERROR) | `activity/Home.java:214-227` |
| S_HOME_DESKTOP | long-press empty desktop area | S_HOME_EDIT | `widget/Desktop.java:520-535` |
| S_HOME_DESKTOP | tap the All Apps item | S_HOME_DRAWER_PAGED / _VERTICAL | `widget/AppItemView.java:285-293` → `activity/Home.java:775-805` |
| S_HOME_DESKTOP | swipe up on desktop or dock (only if `swipe=true`); a gesture or minibar entry mapped to "Open App Drawer" | drawer | `widget/Desktop.java:473-496`; `widget/Dock.java:78-94`; `util/LauncherAction.java:133-135` |
| S_HOME_DESKTOP | tap a folder | S_HOME_GROUP_POPUP | `viewutil/ItemViewFactory.java:224-231` |
| S_HOME_DESKTOP | long-press an item (app, folder, shortcut, All Apps button) | S_HOME_DRAG_ITEM@type | `widget/AppItemView.java:319-345`; `viewutil/ItemViewFactory.java:44-54, 66-77, 185-197, 202-213` |
| S_HOME_DESKTOP | hold-and-move a widget > 500 ms | S_HOME_DRAG_WIDGET | `widget/WidgetView.java:34-50`; `viewutil/ItemViewFactory.java:122-133` |
| S_HOME_DESKTOP | swipe from the left edge (`minBarEnable`) | S_HOME_MINIBAR | `activity/Home.java:544, 858-876` |
| S_HOME_DESKTOP | tap an app | S_EXTERNAL@APP; **OpenLauncher's own entry ("OLSettings") → S_SETTINGS_ROOT** | `widget/AppItemView.java:299-312`; `util/Tool.java:336-349` |
| S_HOME_DESKTOP | tap a shortcut | S_EXTERNAL@SHORTCUT | `widget/AppItemView.java:367-383` |
| S_HOME_EDIT | tap a page / Back / HOME | S_HOME_DESKTOP | `widget/CellContainer.java:144-163`; `activity/Home.java:738-765` |
| S_HOME_EDIT | Remove (page count > 1), Home (set home page) | S_HOME_EDIT | `activity/Home.java:473-478`; `widget/Desktop.java:136-157` |
| S_HOME_EDIT | Widget | S_WIDGET_PICKER → (S_WIDGET_CONFIG) → S_HOME_EDIT with the widget | `activity/Home.java:479-481, 647-685, 707-721` |
| S_HOME_EDIT | Action | S_HOME_ACTION_MENU → "AppDrawer" adds an All Apps button | `activity/Home.java:482-484, 491-512` |
| S_HOME_EDIT | Settings | S_SETTINGS_ROOT | `activity/Home.java:485-487` |
| S_HOME_DRAWER_* | tap app / long-press app (Normal mode only) / Back or HOME | S_EXTERNAL@APP or S_SETTINGS_ROOT / S_HOME_DRAG_DRAWER_APP (drawer closes) / S_HOME_DESKTOP | `widget/AppDrawer_Paged.java:128-153`; `widget/AppDrawer_Vertical.java:198-219`; `activity/Home.java:751-765` |
| S_HOME_DRAWER_VERTICAL | tap the search field | S_HOME_DRAWER_SEARCH; Back (IME) clears and leaves | `widget/SearchBar.java:46-64` |
| S_HOME_DRAG_* | release over a desktop cell / dock cell / an app (makes a folder) / Remove / hold at an edge 1 s / release elsewhere | S_HOME_DESKTOP (item placed, folder made, item removed, page switched/added, or reverted) | `widget/Desktop.java:160-231, 543-569`; `widget/Dock.java:96-150`; `widget/DragOptionView.java:143-170, 221-310`; `viewutil/DragNavigationControl.java:37-118` |
| S_HOME_DRAG_DRAWER_APP / _ITEM@APP | release over Info / Uninstall | S_EXTERNAL@APPINFO / S_EXTERNAL@UNINSTALL | `widget/DragOptionView.java:88-140, 181-195` |
| S_HOME_GROUP_POPUP | tap app / long-press app / tap title / tap outside, Back, HOME | S_EXTERNAL@APP / S_HOME_DRAG_ITEM@APP or @SHORTCUT / S_DLG_RENAME_GROUP / S_HOME_DESKTOP | `widget/GroupPopupView.java:67-76, 128-185, 187-201`; `activity/Home.java:762-764` |
| S_HOME_MINIBAR | tap a row | EditMinBar → S_MINIBAR_EDIT; SetWallpaper → S_DLG_WALLPAPER; LockScreen → device locks (admin) or toast + S_EXTERNAL@DEVICEADMIN; ClearRam → toast; DeviceSettings → S_EXTERNAL@SETTINGS; LauncherSettings → S_SETTINGS_ROOT; VolumeDialog → system volume panel; OpenAppDrawer → drawer. The drawer closes except for EditMinBar/LauncherSettings/DeviceSettings | `activity/Home.java:591-605`; `util/LauncherAction.java:41-137` |
| S_HOME_MINIBAR | fling right on the ClearRam / VolumeDialog row (other rows clear the popup) | S_MINIBAR_POPUP_CLEARRAM / _VOLUME | `widget/SwipeListView.java:42-69`; `activity/Home.java:585-590`; `widget/MiniPopupView.java:52-92` |
| S_MINIBAR_POPUP_* | tap outside the window | S_HOME_MINIBAR | `widget/MiniPopupView.java:41-50, 94-101` |
| S_DLG_WALLPAPER | Set / Blur | S_EXTERNAL@WALLPAPER (chooser) / back to caller (wallpaper replaced) | `util/LauncherAction.java:53-70` |
| S_SETTINGS_ROOT | tap a category / Info / Up or Back | S_SETTINGS_<CAT> (fragment replace, back-stack "notMenu") / S_ABOUT / previous page (Home recreated if a restart-needing pref changed) | `activity/SettingsActivity.java:137, 147-159, 296-324, 379-382` |
| S_SETTINGS_<CAT> | Back / Up | S_SETTINGS_ROOT | `activity/SettingsActivity.java:137, 155, 379-382` |
| S_SETTINGS_DESKTOP | Minibar / Desktop style / Desktop size / switches | S_MINIBAR_EDIT / S_DLG_DESKTOP_STYLE / S_DLG_NUMPREF@DESKTOP_GRID / same page | `activity/SettingsActivity.java:58-73, 331-344` |
| S_SETTINGS_DOCK | Dock size / switch | S_DLG_NUMPREF@DOCK_GRID / same | `:74-82` |
| S_SETTINGS_DRAWER | Drawer style / Drawer size / switches | S_DLG_DRAWER_STYLE / S_DLG_NUMPREF@DRAWER_GRID / same | `:83-97, 337-340` |
| S_SETTINGS_INPUT | swipe switch / 6 gesture buttons | same / S_DLG_GESTURE@kind | `:98-109, 345-362` |
| S_SETTINGS_COLORS | 5 color buttons | S_DLG_COLOR@pref | `:110-119`; `libs/.../MaterialPrefFragment.java:324-337`; `libs/.../BaseSettingsActivity.java:18-21` |
| S_SETTINGS_ICONS | Icon size / Icon pack / Hide apps | S_DLG_NUMPREF@ICON_SIZE / S_DLG_ICONPACK / S_HIDEAPPS_LOADING | `:120-127, 334-336, 363-367` |
| S_SETTINGS_OTHER | Backup / Restart | S_DLG_BACKUP (permission granted) or S_PERMISSION_DIALOG / `Home.recreate()` + finish → Home | `:128-134, 325-330, 368-374` |
| S_DLG_BACKUP | Backup / Restore / Cancel | toast, same page / `System.exit(1)` → S_EXIT / close | `util/DialogUtils.java:131-184` |
| S_DLG_ICONPACK | Default / a pack | `Home` recreated after reload (S_HOME_DESKTOP behind Settings) / same, or S_PERMISSION_DIALOG | `util/AppManager.java:123-150, 244-248` |
| S_HIDEAPPS_LOADING | list loaded | S_HIDEAPPS_LIST | `fragment/HideAppsFragment.java:108-115` |
| S_HIDEAPPS_LIST | tap row / FAB / Up, Back | toggle (same) / finish (≥1 selected) or S_HIDEAPPS_SNACKBAR / S_SETTINGS_ICONS. `onDestroy` reloads apps and recreates `Home` | `fragment/HideAppsFragment.java:59-64, 123-159, 186-207`; `activity/HideAppsActivity.java:44-64` |
| S_MINIBAR_EDIT | switch / row checkbox / long-press-drag row / Up or Back | same / same / same / parent `Home` (Up via `parentActivityName`, FW-MEMORY) or the caller | `activity/MinibarEditActivity.java:78-117, 155-168`; `AndroidManifest.xml:69` |
| S_ABOUT | Up / Back / list items | caller / caller / S_EXTERNAL@BROWSER (library) | `activity/AboutActivity.java:80-85` |
| any external page | Back | the app page that launched it (`onResume`); HOME → `Home` if default home | FW-MEMORY |

**Back/HOME normalisation.** Every return to `Home` runs `handleLauncherPause()` from `onResume` (`activity/Home.java:744-765`): in edit mode it exits edit mode; else if the drawer is visible it closes it; else (no folder open) it jumps to the configured home page; then it dismisses the folder popup. So `onResume` of `Home` always enters `S_HOME_DESKTOP` (the minibar can stay open: `onResume` does not call `closeDrawers`).

### 3.3 Modes that change active handlers

| Window | Mode variable (code) | Effect |
|---|---|---|
| `Init` | onboarding page index (library) | Finish button on the last page, Skip before it (library, FW-MEMORY/UNVERIFIED) |
| `Home` | `LauncherSettings.init` (`util/LauncherSettings.java:34, 130`) | loading splash and no listeners yet vs ready |
| `Home` | `Desktop.inEditMode` + `CellContainer.blockTouch` (`widget/Desktop.java:515, 528-532`; `widget/CellContainer.java:150-168`) | edit panel visible; touches on pages are intercepted (no item clicks, no gestures, no long-press), a quick tap exits |
| `Home` | drawer child visibility (`activity/Home.java:754`) and `drawerMode` (`widget/AppDrawerController.java:174-205`) | drawer page active; Paged vs Vertical classes; search card only with Vertical + `drawerSearchBar` |
| `Home` | `drawerLayout.isDrawerOpen` (`activity/Home.java:871`), `minBarEnable` lock (`:544`) | minibar rows and fling active; `shortcutLayout` overlay visible |
| `Home` | `MiniPopupView.haveWidowDisplayed` (`widget/MiniPopupView.java:41-50, 120`) | popup window; next tap closes it |
| `Home` | `GroupPopupView.isShowing` (`widget/GroupPopupView.java:96-101`) | folder content handlers; blocks the home-page jump in `handleLauncherPause` |
| `Home` | `DragOptionView.dragging` and the `DragAction.Action` of the drag (`widget/DragOptionView.java:221-310`) | which drop targets are shown and accept: Info/Uninstall only for APP and APP_DRAWER, Remove for all except APP_DRAWER (and APP in Show-All-Apps), dock rejects WIDGET (`widget/Dock.java:97-107`) |
| `Home` | `generalSettings.desktopMode` (Normal / ShowAllApps) | Show-All-Apps fills the desktop with all apps (`util/LauncherSettings.java:204-228`), disables dragging from the drawer (`widget/AppDrawer_Paged.java:144-147`), hides Remove for apps, page removal needs an empty page (`widget/Desktop.java:138-140`); treat as a guard, not a page |
| `Home` | desktop content: page count, presence of APP/GROUP/SHORTCUT/WIDGET/ACTION items | which item handlers exist; treat as `needs_state` |
| `Home` | widget resize handles visible (scale 1 for 2 s after the widget view is created or resized, `viewutil/ItemViewFactory.java:97-174`) | handle taps act only while visible (`if (view.getScaleX() < 1) return;`) |
| `SettingsActivity` | fragment back stack (root vs category) | which prefs exist; the title; Back pops the category |
| `SettingsActivity` | `requireLauncherRestart` (`activity/SettingsActivity.java:291-299`) | finishing Settings recreates `Home` |
| `HideAppsActivity` | `ViewSwitcher` child (loading/list), number of selected apps (`fragment/HideAppsFragment.java:108-155`) | list handlers; snackbar when none selected |
| `MinibarEditActivity` | `minBarEnable` switch | locks/unlocks the minibar drawer in `Home` (`activity/MinibarEditActivity.java:78-89`) |

### 3.4 Candidate page list (53 base pages plus `@` variants; owner = area of §6)

Pseudo and external pages

| Page | Description | Window | Mode predicate | Owner |
|---|---|---|---|---|
| `S_ENTRY` | outside the app (other launcher, system, adb) | — | — | A |
| `S_EXIT` | process ended (`System.exit(1)` after Restore, or killed); statics `Home.launcher`, `LauncherSettings`, `AppManager` singletons gone | — | — | A |
| `S_CRASH` | CustomActivityOnCrash error screen ("Close app"; restart disabled) | library `DefaultErrorActivity` (`:error_activity`) | after an uncaught exception | A |
| `S_EXTERNAL` | another app or system screen on top; variants `@APP`, `@SHORTCUT`, `@SETTINGS`, `@APPINFO`, `@UNINSTALL`, `@WALLPAPER`, `@DEVICEADMIN`, `@BROWSER` | foreign activity | started by `Tool.startApp`, `LauncherAction.RunAction`, `DragOptionView`, About links | A |
| `S_WIDGET_PICKER` | system "choose widget" list (`ACTION_APPWIDGET_PICK`) | system activity (FW-MEMORY: Settings `AppWidgetPickActivity`) | after `Home.pickWidget` | A |
| `S_WIDGET_CONFIG` | provider's configure activity (`ACTION_APPWIDGET_CONFIGURE`) | foreign activity | `appWidgetInfo.configure != null` (`activity/Home.java:654-666`) | A |
| `S_PERMISSION_DIALOG` | runtime dialog for `READ_EXTERNAL_STORAGE`, requested on `Home.launcher` | system GrantPermissionsActivity | from Settings › Backup or an icon-pack row without permission | A |

`Init`

| Page | Description | Mode predicate | Owner |
|---|---|---|---|
| `S_INTRO` | onboarding, pages 1-2 (Skip, next) | `quickSettings.firstStart == true` | A |
| `S_INTRO_LAST` | onboarding, page 3 (Finish "Let's start.") | last page (button visibility per page is library behaviour, UNVERIFIED; merge with `S_INTRO` if it cannot be confirmed) | A |
| `S_INTRO_PAUSED` | `Init` in background | — | A |

`Home` (one Activity; all pages are overlays/modes of it)

| Page | Description | Mode predicate | Main handlers on this page | Owner |
|---|---|---|---|---|
| `S_HOME_LOADING` | splash with spinning icon | `!LauncherSettings.init` at `onCreate` until `Home$2.onPostExecute` | none (Back/HOME only) | A |
| `S_DLG_SETTINGS_ERROR` | alert "Some settings can't be read" + OK | `readSettings()==false` | dialog OK (library) | A |
| `S_HOME_DESKTOP` | desktop pager + dock + clock; nothing open | `!inEditMode`, drawer hidden, minibar closed, no folder, no drag | `Desktop$DesktopAdapter$3.onTouch`, `$4.onClick`, `$5.onLongClick`, `CellContainer.onTouchEvent` → `SimpleFingerGestures.onTouch` → `Desktop$DesktopAdapter$1.*`, `AppItemView$Builder$1/$2/$3/$4`, `ItemViewFactory$12.onClick`, `Tool$2.onTouch`, `Dock.dispatchTouchEvent`, `WidgetView.onInterceptTouchEvent`, page swipe (`Desktop.onPageScrolled`, `PagerIndicator.on*`), edge swipe (DrawerLayout → `Home.onDrawer*`), Back (`Home.onBackPressed`) | B |
| `S_HOME_WIDGET_RESIZE` | desktop with a widget whose 4 resize handles are visible | ≤2 s after the widget view was created or last resized | `ItemViewFactory$6..$9.onClick` → `scaleWidget` | B |
| `S_HOME_EDIT` | pages scaled to 85 %, edit panel visible | `Desktop.inEditMode == true` | `CellContainer.onTouchEvent` (tap → `performClick` → `Desktop$DesktopAdapter$4.onClick`), `Home$$ViewBinder$1..$5.doClick` (Remove, Home, Widget, Action, Settings: order INFERRED from the constant pool of `Home$$ViewBinder.class`), `Tool$1.onTouch` | B |
| `S_HOME_ACTION_MENU` | PopupMenu with "AppDrawer" | shown from S_HOME_EDIT | `Home$9.onMenuItemClick` → `Home.onOptionsItemSelected` | B |
| `S_HOME_DRAWER_PAGED` | app drawer, pages of icons | drawer visible, `drawerMode == Paged` (default) | `AppItemView$Builder$2.onClick`, `$3.onLongClick` → `AppDrawer_Paged$Adapter$1.readyForDrag/afterDrag`, drawer page swipe, Back/HOME → `closeAppDrawer` | A |
| `S_HOME_DRAWER_VERTICAL` | app drawer as a scrolling grid with alphabet scrollbar (+ search card if `drawerSearchBar`) | drawer visible, `drawerMode == Vertical` | `AppItemView$Builder$2/$3` via `AppDrawer_Vertical$AppItem.bindView`, `AppDrawer_Vertical$AppItem$1`, `GridAppDrawerAdapter.getCharacterForElement` (scrollbar), `SearchBar.onClick` | A |
| `S_HOME_DRAWER_SEARCH` | Vertical drawer, search field focused, IME up | after `SearchBar.onClick` | typing → `AppDrawerController.before/on/afterTextChanged` → filter (`GridAppDrawerAdapter$1.filter`, background thread); IME Back → `SearchBar.onKeyPreIme`; IME action → `SearchBar.onEditorAction` | A |
| `S_HOME_DRAG_DRAWER_APP` | dragging an app from the drawer; top bar shows Info + Uninstall | `DragAction.ACTION_APP_DRAWER` | `Desktop.onDrag@*`, `Dock.onDrag@*`, `DragOptionView$1/$2.onDrag@DROP`, `DragNavigationControl$3/$4.onDrag`, `CellContainer.peekItemAndSwap` | B |
| `S_HOME_DRAG_ITEM` | dragging a desktop/dock/folder item; variants `@APP` (Remove+Info+Uninstall), `@GROUP`, `@SHORTCUT`, `@ACTION` (Remove only) | `ACTION_APP/GROUP/SHORTCUT/LAUNCHER` | as above plus `DragOptionView$3.onDrag@DROP` (Remove) | B |
| `S_HOME_DRAG_WIDGET` | dragging a widget; Remove only; dock refuses | `ACTION_WIDGET` | `Desktop.onDrag@*`, `DragOptionView$3.onDrag`, edges | B |
| `S_HOME_GROUP_POPUP` | folder popup over the desktop | `GroupPopupView.isShowing` | `GroupPopupView$2.onClick` (outside), `$3.onLongClick`, `$4.onClick`, `$5.onClick`, `$6.onClick` (title) | B |
| `S_DLG_RENAME_GROUP` | input dialog "Rename" | from folder title | `Tool$DialogHelper$1.onInput` → `GroupPopupView$6$1.hereIsTheText` | B |
| `S_HOME_MINIBAR` | left drawer with action icons | `drawerLayout.isDrawerOpen(LEFT)` | `Home$11.onItemClick`, `SwipeListView.dispatchTouchEvent` → `SwipeListView$1.onFling` → `Home$10.onSwipe`, `Home.onDrawerStateChanged`, Back | A |
| `S_MINIBAR_POPUP_CLEARRAM` | window with free RAM and storage | `haveWidowDisplayed`, action ClearRam | `MiniPopupView.onTouchEvent` | A |
| `S_MINIBAR_POPUP_VOLUME` | window with 4 volume sliders | `haveWidowDisplayed`, action VolumeDialog | `MiniPopupView$VolumeDialogViewHolder$1.onProgressChanged/onStart/StopTrackingTouch`, `MiniPopupView.onTouchEvent` | A |
| `S_DLG_WALLPAPER` | list "Set Wallpaper / Blur Wallpaper" | from `LauncherAction.RunAction(SetWallpaper)` | `LauncherAction$1.onSelection` | A |
| `S_HOME_PAUSED` | `Home` stopped (another activity on top or app in background) | — | `onPause/onStop`; return via `onStart/onResume` | A |

`SettingsActivity` (+ library dialogs)

| Page | Description | Mode predicate | Owner |
|---|---|---|---|
| `S_SETTINGS_ROOT` | 7 category buttons, Info action, Up | back stack empty | C |
| `S_SETTINGS_DESKTOP` | Minibar, Desktop style, Desktop size, Search bar, Fullscreen, Indicator, Labels | category 0 | C |
| `S_SETTINGS_DOCK` | Dock size, Labels | category 1 | C |
| `S_SETTINGS_DRAWER` | Drawer style, Drawer size, Card, Search bar, Search icon, Remember page, Indicator | category 2 | C |
| `S_SETTINGS_INPUT` | Swipe switch, Single/Double click, Pinch, Unpinch, Swipe down/up | category 3 | C |
| `S_SETTINGS_COLORS` | 5 colour buttons | category 4 | C |
| `S_SETTINGS_ICONS` | Icon size, Icon pack, Hide apps | category 5 | C |
| `S_SETTINGS_OTHER` | Backup, Restart | category 6 | C |
| `S_DLG_NUMPREF` | seek-bar dialog (OK/Cancel); variants `@DESKTOP_GRID`, `@DOCK_GRID`, `@DRAWER_GRID`, `@ICON_SIZE` | library dialog | C |
| `S_DLG_COLOR` | colour chooser; variants `@DOCK`, `@DRAWER`, `@CARD`, `@FOLDER`, `@LABEL` | library `ColorChooserDialog` | C |
| `S_DLG_DESKTOP_STYLE` | single choice Normal / Show All Apps | `DialogUtils.desktopStylePicker` | C |
| `S_DLG_DRAWER_STYLE` | single choice Paged / Vertical | `DialogUtils.appDrawerStylePicker` | C |
| `S_DLG_GESTURE` | single choice of 9 actions; variants `@SINGLE_CLICK`, `@DOUBLE_CLICK`, `@PINCH`, `@UNPINCH`, `@SWIPE_DOWN`, `@SWIPE_UP` (separate callback classes `DialogUtils$3..$8`) | `DialogUtils.start*Picker` | C |
| `S_DLG_ICONPACK` | list "Default" + installed icon packs | `AppManager.startPickIconPackIntent` | A (built and handled in `AppManager`) |
| `S_DLG_BACKUP` | list Backup / Restore + Cancel | permission granted | C |
| `S_SETTINGS_PAUSED` | Settings in background | — | C |

Other activities

| Page | Description | Mode predicate | Owner |
|---|---|---|---|
| `S_ABOUT` | material-about cards (version, GitHub, libraries, rate, team) | — | C |
| `S_ABOUT_PAUSED` | About in background | — | C |
| `S_HIDEAPPS_LOADING` | "please wait" + progress | `AsyncWorkerList` running | C |
| `S_HIDEAPPS_LIST` | list of all apps with check marks, FAB | after `onPostExecute` | C |
| `S_HIDEAPPS_SNACKBAR` | indefinite Snackbar "No apps selected. Show all apps in drawer?" + OK | FAB with 0 selected | C |
| `S_HIDEAPPS_PAUSED` | Hide apps in background (triggers `HideAppsFragment.onSaveInstanceState`) | — | C |
| `S_MINIBAR_EDIT` | enable switch + reorderable list with check boxes | — | C |
| `S_MINIBAR_EDIT_PAUSED` | Minibar edit in background (`onPause` saves, `onStop` rebuilds the minibar) | — | C |

### 3.5 Modeling notes

- **Variants worth using.** `LauncherAction.RunAction@MINIBAR / @GESTURE / @EDITPANEL / @SETTINGS / @OLSETTINGS` (the same dispatcher is reached from the minibar `activity/Home.java:595`, desktop gestures `widget/Desktop.java:395-443, 501-503`, the edit panel `activity/Home.java:486`, Settings `activity/SettingsActivity.java:332`, and `Tool.startApp` for OpenLauncher's own icon `util/Tool.java:337-338`; dialogs open over the caller). `Desktop.onDrag@STARTED/@LOCATION/@DROP/@ENDED`, same for `Dock.onDrag`, `DragOptionView.onDragEvent`, `DragOptionView$1..$3.onDrag`, `DragNavigationControl$3/$4.onDrag`. `SettingsActivity.onPrefClicked@<id>` and `onPrefChanged@<id>` (one big switch each). `Home.onCreate@FIRST` (splash) vs `@RECREATE`. `Tool.startApp@SELF` vs `@OTHER`.
- **Library-mediated callbacks** (library code is outside the class directory, so these are FRAMEWORK edges): `MaterialPrefFragment.onClick` → `SettingsActivity.onPrefClicked` for ButtonPrefs **and** for switch taps (`libs/.../MaterialPrefFragment.java:114-118, 161, 370`); switch `onCheckedChanged` → `onPrefChanged` (`:164-173`); NUMPref dialog OK → `NUMPrefItem.save` → `onPrefChanged` (`:263-268, 292-297`); ColorChooserDialog → `BaseSettingsActivity.onColorSelection` → `onPrefChanged` (`libs/.../BaseSettingsActivity.java:18-21`; DEX-XREF: `ColorCallback.onColorSelection` is called from `ColorChooserDialog$4.onClick`). Consequence: `onPrefChanged` cases `singleClick`/`doubleClick` (`activity/SettingsActivity.java:183-188`) can never run, because those are ButtonPrefs. Material-dialogs single-choice callbacks run when an item is tapped, since these dialogs have no positive button (FW-MEMORY; DEX-XREF: `ListCallbackSingleChoice.onSelection` is called only from `MaterialDialog.sendSingleChoiceCallback`). `AboutActivity.getMaterialAboutList` runs on a background thread (DEX-XREF: called from `MaterialAboutActivity$ListTask.doInBackground`) → ASYNC edge; `getActivityTitle` from `MaterialAboutActivity.onCreate`. FastAdapter items: `bindView/getFactory/getType/getLayoutRes/ItemFactory.create` are called by the adapter on layout (DEX-XREF `FastAdapter$OnBindViewHolderListenerImpl.onBindViewHolder`, `AbstractItem.getViewHolder`). `SimpleDragCallback.onMove` → `itemTouchOnMove` (DEX-XREF).
- **Drag-and-drop** goes through the framework: `View.startDrag` → `GoodDragShadowBuilder.onProvideShadowMetrics/onDrawShadow`, `Desktop$Item.writeToParcel` (ClipData is parcelled); `ACTION_DRAG_STARTED/ENDED` are delivered to every listening view, `LOCATION/ENTERED/EXITED/DROP` to the view under the finger; `Desktop$Item$1.createFromParcel` runs at `getParcelableExtra` on DROP (FW-MEMORY; all of these were hit by APE).
- **Timers.** `Tool.createScaleInScaleOutAnim` delays every icon launch by 160 ms via two `Handler.postDelayed` (`util/Tool.java:490-502`): model `AppItemView$Builder$2.onClick` → ASYNC `Tool$3.run` → ASYNC `Tool$3$1.run` → `AppItemView$Builder$2$1.run` → `Tool.startApp`. Edge-zone page flipping repeats every 1 s while hovering (`viewutil/DragNavigationControl.java:16-35`).
- **`Home$$ViewBinder`** is instantiated by reflection from `ButterKnife.bind(this)` (`activity/Home.java:197`): FRAMEWORK edge to `Home$$ViewBinder.<init>`, `.bind`, `.createUnbinder`, `Home$$ViewBinder$1..$5.<init>`, `Home$$ViewBinder$InnerUnbinder.<init>`; same for `MinibarEditActivity$$ViewBinder` (`activity/MinibarEditActivity.java:51`) and the two `MiniPopupView` holders (`widget/MiniPopupView.java:135, 170`).
- **Static initialisers.** `LauncherAction.<clinit>` reads `Home.resources` (`util/LauncherAction.java:23, 29-39`), set only in `Home.onCreate` (`activity/Home.java:189`); first use is `Home.initMinBar`. If any other entry (e.g. `MinibarEditActivity` restored after process death) touched `LauncherAction` first, class init would throw (INFERRED hazard, UNVERIFIED that the system restores such a task).

## 4. Framework mechanisms needing FRAMEWORK / ASYNC / LIFECYCLE edges

| Mechanism | App classes (code) | Edge notes |
|---|---|---|
| `AsyncTask` | `Home$2` settings load (`activity/Home.java:207-228`); `AppManager$AsyncGetApps` app list (`util/AppManager.java:101-108, 159-252`); `LauncherAction$2` Clear RAM (`util/LauncherAction.java:90-121`); `HideAppsFragment$AsyncWorkerList` (`fragment/HideAppsFragment.java:79-116`); library `MaterialAboutActivity$ListTask` → `AboutActivity.getMaterialAboutList` (DEX-XREF) | ASYNC `execute` → `onPreExecute` (main) → `doInBackground` → `onPostExecute`. `AsyncGetApps.onCancelled` only when `getAllApps` runs while a task is RUNNING (`util/AppManager.java:104-107`): timing-dependent |
| Plain `Thread` | `HideAppsFragment$2` (`fragment/HideAppsFragment.java:124-158`) builds a Snackbar and calls `finish()` off the main thread | ASYNC; Snackbar callbacks posted to main (FW-MEMORY) |
| `Handler` / `postDelayed` / `View.post` | `Tool$3`, `Tool$3$1` (`util/Tool.java:490-502`); `DragNavigationControl$1/$2` (1 s repeat, `viewutil/DragNavigationControl.java:15-35`); `GroupPopupView$1` (2 s, `widget/GroupPopupView.java:59-65`); `ItemViewFactory$3` (`View.post`), `$4` (2 s) (`viewutil/ItemViewFactory.java:87-121`); `Home$7`, `Home$8` (100 ms, `activity/Home.java:425-458`) | ASYNC with delay |
| Animator / ViewPropertyAnimator end actions | `AppDrawerController$1/$2` (reveal listeners; `onAnimationEnd` calls `Home$5/$6.onEnd`), `$3/$4` (`widget/AppDrawerController.java:69-170`); `Home$2$1`, `Home$6$1`, `Home$12`; `DragOptionView$4/$5` | ASYNC after ~60-300 ms. `onAnimationCancel/Repeat` never triggered by app code (§5.3) |
| `ViewTreeObserver.OnGlobalLayoutListener` | `AppDrawer_Vertical$1` (builds the whole Vertical drawer on first layout, `widget/AppDrawer_Vertical.java:63-81`); `MiniPopupView$1` (`widget/MiniPopupView.java:104-119`) | FRAMEWORK after layout |
| Pager adapters (library `SmoothViewPager`/`SmoothPagerAdapter`, a ViewPager fork) | `Desktop$DesktopAdapter` (`widget/Desktop.java:335-541`), `AppDrawer_Paged$Adapter` (`widget/AppDrawer_Paged.java:126-214`); listeners `PagerIndicator` (`widget/PagerIndicator.java:64-98`), override `Desktop.onPageScrolled` (`widget/Desktop.java:317-323`) | `getCount/instantiateItem/isViewFromObject` on layout; `destroyItem` when pages leave the offscreen window or on `setAdapter(null)`; `getItemPosition` only after `notifyDataSetChanged` (`libs/smoothviewpager/.../SmoothViewPager.java:911-923, 2954-2962`), which only `Desktop$DesktopAdapter.addPage*/removePage` call |
| Support `FragmentPagerAdapter` | `HideAppsActivity$ViewPagerAdapter` (`activity/HideAppsActivity.java:66-94`) | `getItem/getCount` FRAMEWORK; `getPageTitle` needs a tab strip (none) |
| `ListView` adapters | `IconListAdapter` (minibar, `viewutil/IconListAdapter.java`), `HideAppsFragment$AppAdapter` (`fragment/HideAppsFragment.java:210-257`) | `getCount/getView/getItemId` FRAMEWORK; `IconListAdapter.getItem` not called (§5.3) |
| RecyclerView + FastAdapter | `MinibarEditActivity$Item`, `IconLabelItem`, `AppDrawer_Vertical$AppItem` + `GridAppDrawerAdapter` (also `INameableAdapter` for the scrollbar, DEX-XREF `AlphabetIndicator.getTextElement`), `QuickCenterItem.*` (dead), `MinibarEditFragment$AppItem` (dead); `ItemTouchHelper` + `SimpleDragCallback` → `itemTouchOnMove` | FRAMEWORK on bind; filter predicate runs on the `Filter` worker thread (DEX-XREF `ItemAdapter$ItemFilter.performFiltering`) |
| Drag and drop | sources: `AppItemView$Builder$3.onLongClick`, `ItemViewFactory$5.onLongClick`, `GroupPopupView$3.onLongClick`; targets: `Desktop`, `Dock`, `DragOptionView` (+`$1..$3`, `dispatchDragEvent`, `onDragEvent`), `DragNavigationControl$3/$4`, `SearchBar.onDragEvent`; shadow `GoodDragShadowBuilder`; payload `Desktop$Item` Parcelable | see §3.5 |
| Custom touch pipeline | `CellContainer.onTouchEvent/onInterceptTouchEvent` → `SimpleFingerGestures.onTouch` → `GestureAnalyser` → `doCallBack` (`widget/CellContainer.java:144-169`; `sfg/SimpleFingerGestures.java:68-181`); `Dock.dispatchTouchEvent`; `SwipeListView.dispatchTouchEvent` + `GestureDetector` (`widget/SwipeListView.java:42-75`); `WidgetView.onInterceptTouchEvent` fakes the long-click (`widget/WidgetView.java:34-50`); `MiniPopupView.onTouchEvent`; `SearchBar.onKeyPreIme`; `Tool$1/$2` OnTouchListeners | FRAMEWORK/GUI. Pinch/unpinch need 2 fingers |
| Custom drawing / Drawable callbacks | `AppItemView.onMeasure/onLayout/onDraw/invalidateDrawable/refreshDrawableState`; `CellContainer.onLayout/onDraw`; `PagerIndicator.onLayout/onDraw`; `GroupIconDrawable.draw` (+`popUp/popBack`); `RoundDrawable` (dead) | FRAMEWORK on layout/invalidate |
| `View.onConfigurationChanged` | `AppDrawer_Paged`, `AppDrawer_Vertical` | `Home` handles orientation, keyboard and screenSize changes itself but is portrait-locked, so only a keyboard/screen-size change reaches them (§5.3) |
| `DrawerLayout.DrawerListener` | `Home.onDrawerSlide/Opened/Closed/StateChanged` (`activity/Home.java:235, 846-877`) | FRAMEWORK while the minibar moves |
| Activity results / permissions | `Home.onActivityResult` (widget pick/config, `:707-721`); `Home.onRequestPermissionsResult` (`:628-637`) for requests made on `Home.launcher` from `Home`, `SettingsActivity`, `AppManager$2`, `QuickCenterItem$ContactItem$1` | RESULT; delivered before `Home.onResume` (FW-MEMORY) |
| `Activity.recreate()` of `Home` | `SettingsActivity.onDestroy` / `onPrefClicked("restart")` (`activity/SettingsActivity.java:296-299, 325-330`); `AppManager$AsyncGetApps.onPostExecute` when `recreateAfterGettingApps` (`util/AppManager.java:244-248`; set by icon-pack choice and `HideAppsActivity.onDestroy`) | LIFECYCLE chain pause→stop→destroy→create(`@RECREATE`)→start→resume. Note `AppManager.context` keeps the **first** `Home` instance (`util/AppManager.java:53-60`), so a later `recreate()` targets a destroyed activity (INFERRED: probably a no-op) |
| Broadcast receivers | §1.2, plus manifest `ShortcutReceiver`, `DeviceAdminReceiver` | SYSTEM |
| Content provider / observer | `FiveSecsDelayContentProvider` (exported); `Home$CallLogObserver` (never registered) | ENTRY / FRAMEWORK |
| App widgets (host side) | `viewutil/WidgetHost.java` (`onCreateView` → `WidgetView`); `Home.appWidgetHost.startListening/stopListening` in `init/onStart/onResume/onDestroy` (`activity/Home.java:239, 689, 726, 746`); `ItemViewFactory` WIDGET branch (`viewutil/ItemViewFactory.java:82-177`); `AppWidgetManager.updateAppWidgetOptions` | FRAMEWORK (`AppWidgetHost.createView` → `onCreateView`, FW-MEMORY) |
| Persistence | Gson JSON in `files/` (`desktopData.json`, `dockData.json`, `desktopData2.json`, `dockData2.json` for Show-All-Apps, `generalSettings.json`) via `Tool.writeToFile/getStringFromFile` (`util/LauncherSettings.java:21-25, 45-111, 126-156, 231-268`); icon cache PNGs in `files/iconCache/` (`util/Tool.java:209-277`); SharedPreferences `quickSettings` (`Init`), `LauncherSettings` (opened, never used, `util/LauncherSettings.java:128`), `materialpref` (library switch/seek states, `libs/.../MaterialPrefFragment.java:86`); external `/sdcard/OpenLauncher/` backup | Gson creates `GeneralSettings` and `Desktop$SimpleItem` by reflection (no-arg constructors) and calls enum `values()` reflectively (FW-MEMORY) |
| Database layer | `util/DatabaseHelper.java` (SQLite `launcher.db`) | **unused**: all call sites are commented out (`util/LauncherSettings.java:48-50, 79-81, 236-238`) |
| Reflection | ButterKnife `$$ViewBinder` lookup (§3.5); Gson | FRAMEWORK |
| System services | `WallpaperManager` (offsets, tap command, `setBitmap` blur), `DevicePolicyManager.lockNow`, `ActivityManager` (memory info, `killBackgroundProcesses`), `AudioManager` (`FLAG_SHOW_UI` volume panel, stream volumes), `InputMethodManager` (`SearchBar`), haptics | side effects only |
| Crash handler | library CustomActivityOnCrash (`activity/Home.java:184-187`) | SYSTEM edge to `S_CRASH` |
| Not used | LiveData/ViewModel, RxJava, data binding, WorkManager/JobScheduler/AlarmManager, services, notifications, WebView/JS bridges, Storage Access Framework, file pickers, network code | — |

## 5. Unreachable-code candidates (evidence only; verdicts are for the graph builders)

All candidates below are `--` in both baseline runs (no contradiction). Reference searches were run over `APP/src/main/java` (all app sources) and `APP/src/main/res` (layouts have **no** `android:onClick`).

### 5.1 No caller found (DEAD candidates, 139 methods)

| Methods | Count | Evidence |
|---|---|---|
| `fragment.SettingsFragment` and `$1..$7` | 18 | class `@Deprecated` (`fragment/SettingsFragment.java:14-15`); only use commented out (`activity/SettingsActivity.java:39`); Settings uses library `MaterialPrefFragment` instead |
| `fragment.MinibarEditFragment` and all inner classes incl. `$$ViewBinder` | 26 | no reference anywhere; duplicate of `MinibarEditActivity`; even if used it binds the *activity* (`fragment/MinibarEditFragment.java:53`), so its own binder would stay unused |
| `util.DatabaseHelper` (all) | 16 | only commented-out callers (`util/LauncherSettings.java:49, 80, 237`); unused import in `widget/Desktop.java:22` |
| `QuickCenterItem.<init>`, `$NoteItem*`, `$NoteContent*`, `$SearchHeader*` | 21 | class `@Deprecated` "concept idea" (`viewutil/QuickCenterItem.java:27-28`); no constructor call for these nested classes |
| ButterKnife `InnerUnbinder.unbind()` / `unbind(T)` for `Home`, `MinibarEditActivity`, both `MiniPopupView` holders | 8 | the app never keeps or calls the returned `Unbinder` (`activity/Home.java:197`, `activity/MinibarEditActivity.java:51`, `widget/MiniPopupView.java:135, 170`) |
| `BuildConfig.<init>`, `<clinit>` | 2 | `BuildConfig` is never referenced (`IS_TEST_BUILD`, `IS_GPLAY_BUILD` unused); the Currency recipe excludes it from the method list anyway |
| Default constructors of static-only classes: `DialogUtils`, `IconPackHelper`, `LauncherAction`, `Tool$DialogHelper`, `DragNavigationControl`, `ItemViewFactory`, `GroupPopupView$GroupDef` | 7 | never instantiated (all members static) |
| `Home.onSearch`, `Home.onVoiceSearch` | 2 | comments say the search bar was removed (`activity/Home.java:812-843`); no caller, no XML `onClick` |
| `LauncherAction$Theme.names` | 1 | no caller (`util/LauncherAction.java:163`); `theme` is "Not used" (`util/LauncherSettings.java:319-320`) |
| `Tool.getContactIDFromNumber`, `Tool.openPhoto`, `Tool.setHomeTheme`, `Tool.wrapColorTag` | 4 | `openPhoto` has no caller and is the only caller of `getContactIDFromNumber` (`util/Tool.java:123-198`); the others have none |
| `AppItemView.getBgColor/getHeightPadding/getIconPadding/getIconSizeSmall/isRoundBg` | 5 | getters without callers (`widget/AppItemView.java:79-143`) |
| `PagerIndicator.setColor/setFillPaint/setOutlinePaint` | 3 | no callers (`widget/PagerIndicator.java:47-61`) |
| `SimpleFingerGestures.<init>(int,int,int)`, `getConsumeTouchEvents`, `setConsumeTouchEvents`, `setDebug`; `GestureAnalyser.getOngoingGesture` | 5 | vendored library API unused by the app (`sfg/SimpleFingerGestures.java:18-28, 47-49`; `sfg/GestureAnalyser.java:119-128`) |
| `CellContainer.cellPositionToLayoutPrams(int,int,int,int)`, `positionToLayoutPrams(Point,int,int)`, `CellContainer$LayoutParams.<init>(int,int)` and `(int,int,int,int)` | 4 | no callers; the used siblings are `cellPositionToLayoutPrams(int,int,int,int,LayoutParams)` (widgets only), `positionToLayoutPrams(int,int,int,int)` and the 6-int `LayoutParams` constructor (`widget/CellContainer.java:373-493, 576-600`; `widget/AppDrawer_Paged.java:174`) |
| `Desktop$Item.fromGroupItem` | 1 | no caller (`widget/Desktop.java:752-759`) |
| View constructors never used: `(Context)` of `AppDrawerController`, `AppDrawer_Paged`, `AppDrawer_Vertical`, `Desktop`, `Dock`, `DragOptionView`, `GroupPopupView`, `MiniPopupView`, `PagerIndicator`, `SearchBar`, `SwipeListView`; `(Context,AttributeSet,int)` of `AppDrawerController`, `AppDrawer_Vertical`, `MiniPopupView`, `SwipeListView`; `WidgetView(Context,int,int)` | 16 | XML inflation uses the `(Context, AttributeSet)` constructor (FW-MEMORY); no `new X(context)` for these (`new` is used only for `AppItemView`, `CellContainer`, `WidgetView(Context)`: `widget/AppItemView.java:249`, `widget/Desktop.java:457`, `viewutil/WidgetHost.java:18`) |

### 5.2 Blocked by an undeclared permission (25 methods)

`Home$CallLogObserver` (5), `Tool.fetchThumbnail`, `Tool.fetchThumbnailId` (2), `QuickCenterItem$ContactItem*` (10), `QuickCenterItem$ContactContent*` (2), `RoundDrawable` (6). The only creation of a `CallLogObserver` is behind `checkSelfPermission(READ_CALL_LOG) == GRANTED` (`activity/Home.java:617-621`) or behind `callLogObserver != null` (`:629-634`, a bug that makes the branch need an observer that only the first branch creates). `READ_CALL_LOG` is commented out in the manifest (`AndroidManifest.xml:4-8`) and absent from APK-MANIFEST, so it can never be granted (FW-MEMORY: runtime grants and `pm grant` require a manifest declaration). `ContactItem`/`ContactContent` are only created in `logCallLog` (`activity/Home.java:913-916`); `RoundDrawable` only in `ContactItem.bindView` (`viewutil/QuickCenterItem.java:130-131`). Recommend `DEAD` with this reason (or `FRAMEWORK_ONLY` for `onChange`).

### 5.3 Framework-only candidates (13) and configuration-change code (4)

| Method | Why no known path triggers it |
|---|---|
| `IconListAdapter.getItem` | `ListView` layout and clicks do not call `getItem` (FW-MEMORY); app never calls it |
| `HideAppsActivity$ViewPagerAdapter.getPageTitle` | only tab strips / title strips call it; `res/layout/activity_appskip.xml` has none |
| `AppDrawer_Paged$Adapter.getItemPosition` | `SmoothViewPager` calls it only from `dataSetChanged()` after `notifyDataSetChanged()` (`libs/smoothviewpager/.../SmoothViewPager.java:911-923, 2954-2962`); nobody notifies the drawer adapter |
| `GroupIconDrawable.getOpacity/setAlpha/setColorFilter` | the drawable is drawn by `AppItemView.onDraw` (`icon.draw(canvas)`), not by an ImageView that would set alpha/filters (FW-MEMORY) |
| `Desktop$Item.describeContents`, `Desktop$Item$1.newArray` | Parcelable plumbing; `describeContents` is used by `Bundle.hasFileDescriptors` paths, `newArray` for typed arrays (FW-MEMORY); neither applies to the drag ClipData |
| `AppDrawerController$1/$2.onAnimationCancel/onAnimationRepeat` | the reveal animator is never cancelled or repeated by app code |
| `Home.onLowMemory` | needs a system low-memory callback (FW-MEMORY: hard to trigger on demand) |
| `AppDrawer_Paged.onConfigurationChanged`, `setLandscapeValue`; `AppDrawer_Vertical.onConfigurationChanged`, `setLandscapeValue` | `Home` is portrait-locked and handles orientation, keyboard and screenSize changes itself (`AndroidManifest.xml:41, 44`), so views get `onConfigurationChanged` only on a hardware-keyboard or screen-size change, and the orientation is never LANDSCAPE: `setLandscapeValue` looks unreachable on a phone emulator (FW-MEMORY/UNVERIFIED) |

### 5.4 Environment- or setup-gated (67 methods; REACHABLE_AFTER_SETUP candidates)

| Gate | Methods |
|---|---|
| Widget placed via the system picker (G7) | `Home.configureWidget`, `Home.createWidget`, `Desktop$Item.newWidgetItem`, `WidgetHost.onCreateView`, `WidgetView.<init>(Context)`, `.onInterceptTouchEvent`, `.onTouchEvent`, `.setOnLongClickListener`, `ItemViewFactory.scaleWidget`, `.updateWidgetOption`, `ItemViewFactory$3..$9` (14), `CellContainer.cellPositionToLayoutPrams(int,int,int,int,LayoutParams)` (25) |
| Shortcut via `INSTALL_SHORTCUT` (G9) | `ShortcutReceiver.onReceive`, `Desktop$Item.newShortcutItem` ×2, `Tool.saveIconAndReturnID`, `Tool.getIconFromID`, `AppItemView$Builder.setShortcutItem`, `AppItemView$Builder$4`, `$4$1` (4), `ItemViewFactory$10` (3), `GroupPopupView$5`, `$5$1` (4) (17) |
| Icon pack installed (G8) | `AppManager$2` (2), `IconPackHelper` except `<init>` (6), `Tool.isPackageInstalled`, `AppManager.getPackageManager` (10) |
| Kustom caller / adb `content` on the exported provider | `FiveSecsDelayContentProvider.query/insert/update/getType/delete/checkCallingPackage` (6), `AutoFinishActivity.<init>/onCreate/start` (3; needs caller `org.kustom.*`) (9) |
| Package added/removed/changed while `Home` runs | `AppUpdateReceiver.onReceive`, `AppManager.onReceive`, `AppManager$AsyncGetApps.onCancelled` (also timing: a second refresh while one runs) (3) |
| Device admin enabled (G10) | `DeviceAdminReceiver.<init>`, `.onReceive` (2) |
| Corrupt settings file (G13) | `Tool$DialogHelper.alert` (1) |

### 5.5 Flavor, debug, API-level and hardware gates

- Flavors: only `flavorDefault` is built (`class_files.json`); `flavorTest`/`flavorGplay` differ only in `BuildConfig` flags and resources (`APP/build.gradle:27-51`), and no flavor source sets exist. Debug-only code: `HideAppsFragment.DEBUG = true` logging (`fragment/HideAppsFragment.java:46`), `Tool.print` logging everywhere, the `JacocoInstrument` package (excluded).
- API checks are all `>= LOLLIPOP`/`KITKAT` (`activity/Home.java:199, 244`; `activity/HideAppsActivity.java:29`; `widget/DragOptionView.java:72`; `util/FiveSecsDelayContentProvider.java:81`): true on API 27, so only their else-branches are dead (branch level, not method level).
- Hardware: pinch/unpinch need two fingers (`sfg/GestureAnalyser.java:152-170`; `Desktop$DesktopAdapter$1.onPinch/onUnpinch --`); `LockScreen` needs device admin; widget sizes need real providers.

### 5.6 Methods JaCoCo does not report (35)

`tools/list_methods.py --exclude JacocoInstrument --exclude '/R$' --exclude BuildConfig` prints **934** methods: the 899 JaCoCo methods plus 35 JaCoCo filters (blank baseline flags): `values()`, `valueOf(String)` and the private `<init>(String,int)` of the 7 enums (`DragAction$Action`, `LauncherAction$Action`, `LauncherAction$Theme`, `AppDrawerController$DrawerMode`, `CellContainer$PeekDirection`, `Desktop$DesktopMode`, `Desktop$Item$Type`; 21), 13 synthetic switch-map classes' `<clinit>` (`Home$13`, `DatabaseHelper$1`, `LauncherAction$3`, `LauncherSettings$1`, `AppDrawerController$5`, `MiniPopupView$2`, `DragNavigationControl$5`, `ItemViewFactory$13`, `AppItemView$1`, `CellContainer$1`, `Desktop$1`, `Dock$1`, `DragOptionView$6`), and `Tool.<init>` (private, never called: DEAD). Most enum methods are reachable: `LauncherAction$Action.valueOf` (`activity/Home.java:588, 594`), `DrawerMode.values/valueOf` (`util/DialogUtils.java:33-49`), `DesktopMode.values` (`util/LauncherSettings.java:183`), `Desktop$Item$Type.valueOf` (`widget/Desktop.java:763`), switch-map `<clinit>` on the first `switch` over an enum, and Gson's enum adapters (FW-MEMORY).

### 5.7 Crash hazards that change paths (from reading, not reproduced)

- `SettingsActivity.onPrefChanged("desktopSearchBar")` dereferences `Home.launcher` without a null check (`activity/SettingsActivity.java:171, 173`); `ShortcutReceiver.onReceive` likewise (`util/ShortcutReceiver.java:48-64`); `LauncherAction.RunAction(OpenAppDrawer)` too (`util/LauncherAction.java:134`).
- `LockScreen` without admin starts `com.android.settings/.DeviceAdminSettings` inside the `catch` (`util/LauncherAction.java:76-81`); if that component is missing or not exported on API 27 the `ActivityNotFoundException`/`SecurityException` is uncaught → `S_CRASH` (UNVERIFIED).
- `GroupPopupView.removeItem` calls `currentItem.actions[0].getComponent().getPackageName()` when one entry is left (`widget/GroupPopupView.java:268`); if that last entry is a shortcut intent without a component this NPEs (INFERRED).
- `DialogUtils` Restore kills the process (`util/DialogUtils.java:179`) → `S_EXIT`.

## 6. Decomposition into 3 areas

Three agents can work in parallel. The split follows the code's own seams: `Home` + utilities (A), the desktop widgets that render and move items (B), the separate Settings-type activities (C). Each outer class goes to exactly one area **with all its inner, anonymous and synthetic classes**.

### 6.1 Areas

| Area | Theme | Outer classes | Class files | JaCoCo methods | `list_methods` methods | Of which DEAD / no-permission / framework-only candidates (§5) | Pages owned |
|---|---|---|---|---|---|---|---|
| **A** Shell & shared infrastructure | entry, lifecycle, settings/app-list model, app drawer, minibar, system integration, receivers/provider | 24 | 114 | 417 (415 without `BuildConfig`) | 431 | 65 / 25 / 7 (+4 config) | 21 |
| **B** Desktop surface | desktop pager, dock, cells, item views, drag-and-drop, folders, widgets, gestures | 18 | 84 | 335 | 354 | 27 / 0 / 5 | 9 |
| **C** Settings & secondary activities | Settings + dialogs, About, Hide apps, Minibar edit | 9 | 49 | 149 | 149 | 47 / 0 / 1 | 23 |
| *Leftover* | `JacocoInstrument` (excluded) | 3 | 3 | 10 | — | — | — |

A is the largest, but about 100 of its methods need only a verdict (dead `QuickCenterItem`, `DatabaseHelper`, call-log code). C is small and could also take the minibar if A runs late (moving `SwipeListView`, `MiniPopupView`, `IconListAdapter` would shift 41 methods), at the cost of more cross-area edges through `Home$10/$11`.

### 6.2 Class lists (JaCoCo method count in brackets)

**A — Shell.** `activity.Home` incl. `Home$1..$13`, `$2$1`, `$6$1`, `$CallLogObserver`, `$$ViewBinder`, `$$ViewBinder$1..$5`, `$$ViewBinder$InnerUnbinder` [91]; `activity.Init` [5]; `activity.AutoFinishActivity` [3]; `widget.AppDrawerController` + `$1..$5`, `$CallBack`, `$DrawerMode` [29]; `widget.AppDrawer_Paged` + `$1`, `$Adapter`, `$Adapter$1` [21]; `widget.AppDrawer_Vertical` + 8 inner [27]; `widget.SearchBar` [7]; `widget.SwipeListView` + `$1`, `$OnSwipeRight` [8]; `widget.MiniPopupView` + `$1`, `$2`, both view holders and their binders [28]; `viewutil.IconListAdapter` [5]; `viewutil.IconLabelItem` + 2 inner (rows of the icon-pack dialog built by `AppManager`) [9]; `viewutil.QuickCenterItem` + 13 inner [33]; `viewutil.RoundDrawable` [6]; `util.AppManager` + `$1`, `$2`, `$App`, `$AppDeletedListener`, `$AppUpdatedListener`, `$AsyncGetApps`, `$AsyncGetApps$1` [30]; `util.LauncherSettings` + `$1`, `$GeneralSettings` [15]; `util.LauncherAction` + `$1..$3`, `$Action`, `$ActionItem`, `$Theme` [14]; `util.Tool` + `$1`, `$2`, `$3`, `$3$1`, `$DialogHelper`, `$DialogHelper$1`, `$DialogHelper$OnTextResultListener` [47]; `util.AppUpdateReceiver` [2]; `util.ShortcutReceiver` [2]; `util.DeviceAdminReceiver` [2]; `util.FiveSecsDelayContentProvider` [8]; `util.IconPackHelper` [7]; `util.DatabaseHelper` + `$1` [16]; `BuildConfig` [2].

**B — Desktop surface.** `widget.Desktop` + `$1`, `$DesktopAdapter`, `$DesktopAdapter$1..$5`, `$DesktopMode`, `$Item`, `$Item$1`, `$Item$Type`, `$OnDesktopEditListener`, `$SimpleItem` [75]; `widget.CellContainer` + `$1`, `$LayoutParams`, `$OnItemRearrangeListener`, `$PeekDirection` [35]; `widget.Dock` + `$1` [15]; `widget.DragOptionView` + `$1..$6` [22]; `widget.GroupPopupView` + `$1..$8`, `$4$1`, `$5$1`, `$6$1`, `$GroupDef` [33]; `widget.AppItemView` + `$1`, `$Builder`, `$Builder$1..$4`, `$Builder$2$1`, `$Builder$4$1`, `$Builder$LongPressCallBack` [52]; `widget.PagerIndicator` [12]; `widget.WidgetView` [5]; `viewutil.ItemViewFactory` + `$1..$13` [33]; `viewutil.GroupIconDrawable` [8]; `viewutil.GoodDragShadowBuilder` [3]; `viewutil.DragNavigationControl` + `$1..$5` [11]; `viewutil.WidgetHost` [2]; `viewutil.DesktopCallBack` [0]; `util.DragAction` + `$Action` [2]; `util.RevertibleAction` [0]; `in.championswimmer.sfg.lib.SimpleFingerGestures` + `$OnFingerGestureListener` [10]; `in.championswimmer.sfg.lib.GestureAnalyser` + `$GestureType` [17].

**C — Settings & secondary.** `activity.SettingsActivity` [10]; `activity.AboutActivity` [4]; `activity.HideAppsActivity` + `$1` (synthetic), `$ViewPagerAdapter` [10]; `activity.MinibarEditActivity` + `$$ViewBinder`, `$$ViewBinder$InnerUnbinder`, `$1`, `$Item`, `$Item$1`, `$Item$ItemFactory`, `$Item$ViewHolder` [24]; `fragment.HideAppsFragment` + 7 inner [22]; `fragment.MinibarEditFragment` + 7 inner [26]; `fragment.SettingsFragment` + 8 inner [18]; `model.AppInfo` [6]; `util.DialogUtils` + `$1..$9` [29].

Classes with no method nodes (assigned with their outer class): 14 synthetic classes (`HideAppsActivity$1` and the 13 switch maps of §5.6) and 11 interfaces (`DesktopCallBack`, `RevertibleAction`, `Desktop$OnDesktopEditListener`, `CellContainer$OnItemRearrangeListener`, `AppItemView$Builder$LongPressCallBack`, `SimpleFingerGestures$OnFingerGestureListener`, `AppDrawerController$CallBack`, `SwipeListView$OnSwipeRight`, `AppManager$AppDeletedListener`, `Tool$DialogHelper$OnTextResultListener`, `SettingsFragment$OnSettingsSelectedInterface`). Library modules `launcheranim`, `materialpreffragment`, `smoothviewpager` are in the APK but **not** in the class directory, so they are not method nodes; treat them like framework code.

### 6.3 Pages per area (from §3.4)

- **A (21):** `S_ENTRY`, `S_EXIT`, `S_CRASH`, `S_EXTERNAL`, `S_WIDGET_PICKER`, `S_WIDGET_CONFIG`, `S_PERMISSION_DIALOG`, `S_INTRO`, `S_INTRO_LAST`, `S_INTRO_PAUSED`, `S_HOME_LOADING`, `S_DLG_SETTINGS_ERROR`, `S_HOME_DRAWER_PAGED`, `S_HOME_DRAWER_VERTICAL`, `S_HOME_DRAWER_SEARCH`, `S_HOME_MINIBAR`, `S_MINIBAR_POPUP_CLEARRAM`, `S_MINIBAR_POPUP_VOLUME`, `S_DLG_WALLPAPER`, `S_DLG_ICONPACK`, `S_HOME_PAUSED`.
- **B (9):** `S_HOME_DESKTOP`, `S_HOME_WIDGET_RESIZE`, `S_HOME_EDIT`, `S_HOME_ACTION_MENU`, `S_HOME_DRAG_DRAWER_APP`, `S_HOME_DRAG_ITEM`, `S_HOME_DRAG_WIDGET`, `S_HOME_GROUP_POPUP`, `S_DLG_RENAME_GROUP`.
- **C (23):** the 8 `S_SETTINGS_*` pages, `S_DLG_NUMPREF`, `S_DLG_COLOR`, `S_DLG_DESKTOP_STYLE`, `S_DLG_DRAWER_STYLE`, `S_DLG_GESTURE`, `S_DLG_BACKUP`, `S_SETTINGS_PAUSED`, `S_ABOUT`, `S_ABOUT_PAUSED`, `S_HIDEAPPS_LOADING`, `S_HIDEAPPS_LIST`, `S_HIDEAPPS_SNACKBAR`, `S_HIDEAPPS_PAUSED`, `S_MINIBAR_EDIT`, `S_MINIBAR_EDIT_PAUSED`.

### 6.4 Cross-area edges (the contract between agents)

| From → to | Calls / transitions (code) |
|---|---|
| A → B | `Home.initViews` → `Desktop.init`, `Desktop.setDesktopEditListener`, `Desktop.setPageIndicator`, `PagerIndicator.setViewPager`, `DragOptionView.setHome/setAutoHideView`, `DragNavigationControl.init` (`activity/Home.java:298-394`); `Home.initDock` → `Dock.init` (`:404-414`); `Home$3.onAppUpdated`, `Home$4.onAppDeleted` → `Desktop$Item.newAppDrawerBtn`, `Desktop.initDesktopItem`, `Dock.initDockItem` (`:260-285`); `Home.onViewClicked` → `Desktop.removeCurrentPage` (`:473-475`); `Home.onOptionsItemSelected` → `Desktop.getCurrentPage`, `CellContainer.findFreeSpace`, `Desktop.addItemToPosition` (`:504-512`); `Home.createWidget` → `Desktop$Item.newWidgetItem`, `Desktop.addItemToPagePosition` (`:668-684`); `Home.handleLauncherPause` → `GroupPopupView.dismissPopup`, page `performClick` → `Desktop$DesktopAdapter$4.onClick` (`:751-765`); `Home.openAppDrawer(View,int,int)` → `AppItemView.isNoLabel/getIconSize` (`:779-805`); `AppDrawer_Paged$Adapter.getItemView`, `AppDrawer_Vertical$AppItem.bindView` → `AppItemView$Builder.*` (`widget/AppDrawer_Paged.java:128-153`, `widget/AppDrawer_Vertical.java:198-219`); `ShortcutReceiver.onReceive` → `Desktop$Item.newShortcutItem`, `CellContainer.findFreeSpace`, `Desktop.addItemToPagePosition`; `LauncherSettings.readDockData/readDesktopData/writeSettings/switchDesktopMode` → `Desktop$SimpleItem.<init>`, `Desktop$Item.<init>(SimpleItem)`, `getActionsAsString`, `newAppItem` (`util/LauncherSettings.java:45-268`) |
| B → A | `Desktop$DesktopAdapter$1.on*`, `$4.onClick` → `LauncherAction.RunAction@GESTURE` (`widget/Desktop.java:395-443, 501-503`); `Desktop$DesktopAdapter$3.onTouch`, `Dock.detectSwipe` → `Tool.convertPoint`, `Home.openAppDrawer(View,int,int)` (`widget/Desktop.java:486-491`; `widget/Dock.java:84-91`); `Desktop$DesktopAdapter$5.onLongClick` → `Home.onDesktopEdit`, `$4.onClick` → `Home.onFinishDesktopEdit` (`widget/Desktop.java:516-534`); `AppItemView$Builder$1.onClick` → `Home.openAppDrawer(View)`; `AppItemView$Builder$2$1.run`, `GroupPopupView$4$1.run` → `Tool.startApp`; `AppItemView$Builder$2.onClick` etc. → `Tool.createScaleInScaleOutAnim`; `GroupPopupView$6.onClick` → `Tool$DialogHelper.promptInputText`; utilities everywhere (`LauncherSettings.getInstance`, `AppManager.findApp`, `Tool.dp2px/print/...`) |
| A → C | `LauncherAction.RunAction` → INTENT `MinibarEditActivity` (`util/LauncherAction.java:43-46`), `SettingsActivity` (`:126-128`); reached from the minibar, gestures, the edit panel (`activity/Home.java:485-487`) and `Tool.startApp` for "OLSettings" (`util/Tool.java:337-338`) |
| C → A | `SettingsActivity.onPrefClicked` → `LauncherAction.RunAction@SETTINGS(EditMinBar)`, `AppManager.startPickIconPackIntent`, `ActivityCompat.requestPermissions(Home.launcher)` → RESULT `Home.onRequestPermissionsResult`, `Home.recreate` (`activity/SettingsActivity.java:325-336, 368-374`); `onPrefChanged` → `AppDrawerController.reloadDrawerCardTheme` (`:249, 257, 266, 274`); `onDestroy` → `Home.recreate` (`:297`); `DialogUtils$1..$8.onSelection` → `LauncherSettings.switchDesktopMode` / `set*Gesture` (`util/DialogUtils.java:25-127`); `HideAppsActivity.onDestroy` → `AppManager.init` (`activity/HideAppsActivity.java:44-48`); `HideAppsFragment.prepareData` → `AppManager.getNonFilteredApps`; `MinibarEditActivity.onCreate/onStop` → `LauncherAction.getActionItemFromString`, `Home.initMinBar` (`activity/MinibarEditActivity.java:66-71, 106-111`); `Tool.setTheme` from both activities |
| C → B | none (Settings changes `Home`'s views only through framework setters, e.g. `desktopDock.setBackgroundColor`, `activity/SettingsActivity.java:232`) |

### 6.5 Shared infrastructure and working rules

- **A owns** the singletons and utilities used by everyone: `LauncherSettings` (+`GeneralSettings`), `AppManager`, `Tool`, `LauncherAction`, plus the dead `DatabaseHelper` and `BuildConfig`. **B owns** the item data model `Desktop$Item`/`$SimpleItem`/`$Item$Type` and `DragAction`, which A's persistence uses. There are no app base classes (activities extend library/support classes directly).
- **Edge authorship:** an edge is written by the area that owns its **destination method** (GUI, CALL, INTENT, RESULT, ASYNC, FRAMEWORK, LIFECYCLE, SYSTEM, REGISTER), and `ENTERS` edges by the owner of the **source method**. `ENTRY` edges by A. Example: the 5 edit-panel buttons are GUI edges `S_HOME_EDIT → Home$$ViewBinder$N.doClick`, written by A although B owns the page.
- **Pages are global:** use the names and predicates of §3.4 unchanged; a new page or variant is added to a shared list first.
- **Order:** A first defines the bootstrap path `S_ENTRY → … → S_HOME_DESKTOP` (B and C need it for reachability); B and C can then work in parallel; a short merge step runs `tools/build_graph.py` on the union and fixes dangling names.
- Method universe: `tools/list_methods.py <classes> --exclude JacocoInstrument --exclude '/R$' --exclude BuildConfig --json` (934); baseline flags: `tools/coverage_methods.py final_java_only/openlauncher --json`.

### 6.6 Leftovers

Only `com.benny.openlauncher.JacocoInstrument` (`FinishListener`, `JacocoInstrumentation`, `SMSInstrumentedReceiver`; 10 methods, coverage harness) is unassigned, by design. No compiled class is unassigned otherwise (checked by script: 114 + 84 + 49 + 3 = 250 class files).

## 7. Baseline coverage by area and screen

### 7.1 Per area (JaCoCo METHOD counter, 901 methods without `JacocoInstrument`)

| Area | Methods | Both | Monkey only | APE only | Neither | Monkey total | APE total | Either |
|---|---|---|---|---|---|---|---|---|
| A Shell | 417 | 156 | 10 | 44 | 207 | 166 | 200 | 210 |
| B Desktop surface | 335 | 144 | 4 | 83 | 104 | 148 | 227 | 231 |
| C Settings & secondary | 149 | 16 | 21 | 42 | 70 | 37 | 58 | 79 |
| **Total** | **901** | **316** | **35** | **169** | **381** | **351** | **485** | **520** |

The totals match the brief (351 / 485 / 520). The 35 Monkey-only methods are the minibar path (A: `Home.onDrawerSlide/Opened/Closed/StateChanged`, `Home$11.onItemClick`, `Home$12` ×2, `Home.openAppDrawer()`, `SwipeListView.dispatchTouchEvent`, `MiniPopupView.onTouchEvent`), `MinibarEditActivity*` (C: 19) plus `DialogUtils.startSwipeDownPicker` and `$7.<init>` (C), and gesture details (B: `Desktop$DesktopAdapter$1.onDoubleTap/onSwipeLeft`, `GestureAnalyser.initialFingDist/finalFingDist`).

### 7.2 What the 381 never-hit methods are (classification of §5)

| Area | DEAD cand. | No permission | Framework-only | Config change | Environment-gated | GUI-reachable, missed | Sum |
|---|---|---|---|---|---|---|---|
| A | 65 | 25 | 7 | 4 | 30 (icon pack 10, provider 9, pkg events 3, widget 2, shortcut 3, device admin 2, corrupt file 1) | 76 | 207 |
| B | 27 | 0 | 5 | 0 | 37 (widget 23, shortcut 14) | 35 | 104 |
| C | 47 | 0 | 1 | 0 | 0 | 22 | 70 |
| All | 139 | 25 | 13 | 4 | 67 | 133 | 381 |

**Estimated tool targets** (reachable but not hit by Monkey) = APE-only + environment-gated + GUI-missed ≈ A 150, B 155, C 64, **≈ 370 in total** (+4 config-change methods if counted). This is an estimate from reading; the graph's verdicts decide.

GUI-reachable but missed by both, by feature: Vertical drawer + search (A: `AppDrawer_Vertical*` 27, `SearchBar` 6, `AppDrawerController` text watcher 3 + `$4` 2, `Home$6$1` 2); minibar popups (A: `MiniPopupView*` 22, `SwipeListView$1.onFling`, `Home$10.onSwipe`, `Tool.getFreeRAM/getFreeMemory`); wallpaper and RAM actions (A: `LauncherAction$1` 2, `$2` 4, `Tool.toast` ×2); gestures (A: `LauncherSettings.setSingle/Double/Pinch/SwipeDown*`, `Tool.convertPoint`; C: `DialogUtils.startSingle/Double/PinchPicker`, `$3/$4/$5`, `$7.onSelection`); app hidden or removed (A: `Home$4.onAppDeleted`, `AppManager$App.equals`; B: `Desktop$Item.invalidate`); multi-page desktop (B: `DragNavigationControl$1/$2.run`, `Desktop.addPage*`, `Desktop$DesktopAdapter.addPage*/removePage/destroyItem/getItemPosition`); rearranging while dragging (B: `CellContainer.findFreeSpace(int,int,PeekDirection)`, `isValid`, `onItemRearrange`, `Desktop$DesktopAdapter$2`, `getItemFromCoordinate`); folders (B: `GroupPopupView.removeItem`, `$3.onLongClick`, `$4`, `$4$1`, `$8`, `Desktop$Item.removeActions`, `ItemViewFactory$11` drag, `Dock.addItemToSettings`); uninstall drop (B: `DragOptionView.startDeletePackageDialog`); pinch (B: `onPinch/onUnpinch`); Hide apps confirm (C: `HideAppsFragment.confirmSelection`, `$1.onClick`, `$2`, `$2$1`, `onSaveInstanceState`); minibar edit toggles (C: `MinibarEditActivity.itemTouchOnMove`, `$1`, `$Item$1`); backup/restore (C: `DialogUtils.copy`, `$9.onSelection`); folder load after restart (A: `Tool.split`).

### 7.3 Per screen

| Page | Indicator (code / coverage) | Monkey | APE | Likely reason if missed |
|---|---|---|---|---|
| S_INTRO / S_INTRO_LAST | `Init.onCreate` first-run branch `L25-51 MA`; `onSkipButtonPressed MA`; `onFinishButtonPressed -A` | yes / Finish never pressed | yes / yes | Monkey always hit Skip first |
| S_HOME_LOADING | `Home$2.doInBackground MA` | yes | yes | — |
| S_DLG_SETTINGS_ERROR | `Tool$DialogHelper.alert --`, `Home.java L224-225 --` | no | no | needs a corrupt settings file (G13) |
| S_HOME_DESKTOP | `Desktop$DesktopAdapter$3.onTouch MA`, `$4.onClick MA` | yes | yes | — |
| S_HOME_EDIT | `Desktop$DesktopAdapter$5.onLongClick -A`, `Home.onDesktopEdit -A`, `Home$$ViewBinder$1..$5.doClick -A` | no | yes | Monkey: no long-press |
| S_HOME_ACTION_MENU | `Home$9.onMenuItemClick -A` | no | yes | long-press |
| S_WIDGET_PICKER / S_WIDGET_CONFIG | `Home.pickWidget -A`; `configureWidget --`, `createWidget --`; `onActivityResult` only `RESULT_CANCELED`, null data (`L714 -A`, `L715 --`) | no | start attempted, aborted | external package blocked by the tool (INFERRED) |
| S_HOME_WIDGET_RESIZE, S_HOME_DRAG_WIDGET | `WidgetHost.onCreateView --`, `ItemViewFactory$5..$9 --` | no | no | no widget ever placed |
| S_HOME_DRAWER_PAGED | `AppDrawerController.open MA`, `AppDrawer_Paged$Adapter.instantiateItem MA`, `AppItemView$Builder$1.onClick MA` | yes | yes | — |
| S_HOME_DRAWER_VERTICAL / _SEARCH | `AppDrawer_Vertical$AppItem.bindView --`, `SearchBar.onClick --` | no | no | G5: APE picked a drawer style (`DialogUtils$2.onSelection -A`) but `AppDrawer_Vertical` was never constructed, so `Home` never restarted in Vertical mode (which item APE chose is UNVERIFIED) |
| S_HOME_DRAG_DRAWER_APP | `AppDrawer_Paged$Adapter$1.afterDrag -A`; drop on desktop `Desktop.java L201-204 -A`; on dock `Dock.java L118-121 -A` | no | yes | long-press |
| S_HOME_DRAG_ITEM @APP / @ACTION / @GROUP / @SHORTCUT | `ItemViewFactory$2.afterDrag -A` / `$1.afterDrag -A` / `$11.afterDrag --` / `$10 --`; folder creation `Desktop.java L547-564 -A`; drop on Remove/Info/Uninstall `DragOptionView.java L101, L125-133, L162-163 --`; edges `DragNavigationControl$1/$2.run --` | no | APP, ACTION only | long-press; APE never long-pressed a folder; no shortcuts; never released over the top bar or held at an edge 1 s |
| S_HOME_GROUP_POPUP | `GroupPopupView.showWindowV -A`, `$2.onClick -A`; `$3/$4 --` | no | yes (open, close) | Monkey had no folders |
| S_DLG_RENAME_GROUP | `GroupPopupView$6.onClick -A`, `$6$1.hereIsTheText -A` | no | yes | — |
| S_HOME_MINIBAR | `Home.onDrawerStateChanged M-`, `Home$11.onItemClick M-` (EditMinBar `LauncherAction L44 M-`, OpenAppDrawer `L134 M-`) | yes | no | APE did not do the left-edge swipe |
| S_MINIBAR_POPUP_CLEARRAM / _VOLUME | `MiniPopupView.showActionWindow --` | no | no | needs a right fling on a minibar row |
| S_DLG_WALLPAPER | `LauncherAction$1.<init> --` (`L48-71 --`) | no | no | only from the minibar/gestures; Monkey tapped other rows |
| S_DLG_ICONPACK | `AppManager.startPickIconPackIntent -A`, `$1.onClick -A`; pack rows `L134-148 --` | no | yes (Default only) | no icon pack installed (G8) |
| S_PERMISSION_DIALOG | `SettingsActivity L372 --`, `AppManager$2 --` | no | no | permission already granted in the APE run (`L370 -A`) |
| S_SETTINGS_ROOT | `SettingsActivity.onCreate MA`, `onOptionsItemSelected MA` | yes | yes | — |
| S_SETTINGS_DESKTOP / DOCK / DRAWER / INPUT | `onSettingsSelected L58-109 MA` | yes | yes | — |
| S_SETTINGS_COLORS / ICONS / OTHER | `L111-134 -A` | no | yes | Monkey never tapped the lower 3 entries |
| S_DLG_NUMPREF | `onPrefChanged`: dock grid `L226 -A`, drawer grid `L198-202 -A`, icon size `L194 -A`, desktop grid `L218-224 --` | no | yes (3 of 4 variants) | — |
| S_DLG_COLOR | dock `L230-232 -A`, drawer `L238-241 -A`; card/folder/label `L255-279 --` | no | 2 of 5 | — |
| S_DLG_DESKTOP_STYLE | `DialogUtils.desktopStylePicker -A`, `$1.onSelection -A` | no | yes | — |
| S_DLG_DRAWER_STYLE | `appDrawerStylePicker MA`, `$2.onSelection -A` | shown | yes | Monkey dismissed it |
| S_DLG_GESTURE | single/double/pinch `--`; unpinch `-A` (+selection); swipe down `M-` (no selection); swipe up `-A` (+selection) | 1 of 6 shown | 2 of 6 | — |
| S_DLG_BACKUP | `DialogUtils.backupDialog -A`, `$9.onSelection --`, `copy --` | no | shown only | APE never chose Backup/Restore |
| S_ABOUT | `AboutActivity.getMaterialAboutList MA` | yes | yes | — |
| S_HIDEAPPS_LOADING / _LIST | `HideAppsFragment$AsyncWorkerList.* -A`, `populateView -A`, `$3.onItemClick -A` | no | yes | Monkey never reached Settings › Icons |
| S_HIDEAPPS_SNACKBAR | `HideAppsFragment$1.onClick --`, `$2.run --` | no | no | the FAB was never pressed |
| S_MINIBAR_EDIT | `MinibarEditActivity.onCreate M-`; switch/checkbox/drag `--` | yes | no | reached only from the minibar (APE never opened it); Settings › Desktop › Minibar was never tapped (`SettingsActivity L332 --`) |
| S_EXTERNAL@* | `Tool.startApp MA` (the start itself is refused under `-p`, FW-MEMORY) | call only | call only | external packages blocked |
| S_EXIT via Restore, Settings › Restart | `DialogUtils$9.onSelection --`; `SettingsActivity L326-330 --` | no | no | — |
| S_CRASH | library code, not measurable | ? | ? | UNVERIFIED |

### 7.4 Reading of the baseline

- **Monkey vs APE.** Monkey injects each touch as a quick DOWN-(MOVE)-UP sequence (FW-MEMORY), so `onLongClick` never fires: no edit mode, no drag-and-drop, no folders (`Desktop$DesktopAdapter$5`, `AppItemView$Builder$3`, `GroupPopupView.showWindowV` are all `-A`). Its random edge swipes opened the minibar, which APE (widget-targeted actions) never did. APE also explored the lower Settings categories and Hide apps.
- **Neither** reached code that needs (1) another package's activity (widget picker, permission dialog, system Settings: blocked by `-p`), (2) a settings change followed by a `Home` restart (Vertical drawer), (3) precise multi-step gestures (fling right on a minibar row, holding a drag at the screen edge for 1 s, dropping on the top bar, two-finger pinch), (4) external events (package changes, shortcut broadcast, device admin, Kustom provider), or (5) a process restart with saved data (Monkey never restarted the process: `Desktop$SimpleItem.<init>() -A`).
- **No baseline hit contradicts a candidate verdict of §5**: every DEAD, no-permission and framework-only candidate is `--` in both runs.

## Conclusions and recommendations

1. Model OpenLauncher as one big `Home` window with overlay modes (§3.4); keep `desktopMode`, gesture mappings and desktop contents as guards/`needs_state` rather than pages.
2. Put two ENTRY edges on `S_ENTRY` (icon → `Init`, HOME intent → `Home` with `needs_state` "default home"), plus the process-start provider edge and the external receiver/provider edges of §1.4. Make `Home.onResume` always enter `S_HOME_DESKTOP` (it normalises the state).
3. Treat every library callback (MaterialPrefFragment, material-dialogs, FastAdapter, AndroidOnboarder, material-about, ButterKnife, SmoothViewPager) as FRAMEWORK; several call sites were confirmed with `apkutils xref` on the APK and can be cited as such.
4. Give `DEAD` to the 139 + 25 methods of §5.1-5.2 with the listed reasons, `FRAMEWORK_ONLY` to the 13 of §5.3, and `REACHABLE_AFTER_SETUP` (with `env`) to the 67 of §5.4. Re-check the 4 configuration-change methods if a keyboard toggle is possible on the target emulator.
5. Split the work into areas A, B, C (§6) with the edge-authorship rule of §6.5; let A deliver the bootstrap path first.
6. For any later device check, prepare the harness of §2.4 (grants, icon pack, shortcut sender, default home, system-UI access); without it ~67 methods stay out of reach for every tool.

## Appendix: files read and commands used

- Read completely: 51 of the 53 Java files under `APP/src/main/java` (all except `JacocoInstrument/FinishListener.java` and `JacocoInstrumentation.java`, which belong to the excluded harness; `SMSInstrumentedReceiver.java` was read); libraries `BaseSettingsActivity.java`, `MaterialPrefFragment.java`; `AndroidManifest.xml` (source and APK-MANIFEST); `res/menu/*.xml` (2), `res/values/arrays.xml`, `ids.xml`, `styles.xml`, parts of `strings.xml`; `res/xml/device_admin.xml`, `file_paths.xml`; layouts `activity_home`, `view_home`, `view_search_bar_nougat`, `view_searchbar_app`, `view_desktop_edit_option`, `activity_appskip`, `request`, `activity_minbaredit` (others scanned for ids and `onClick`); `settings.gradle`, root/app/library `build.gradle`, `gradle.properties`; `class_files.json`, `DATASET.txt`, `MANIFEST.csv`, `monkey|ape/status.json`, `coverage/00000.json`.
- Skimmed: `SmoothPagerAdapter.java` (header) and `SmoothViewPager.java` (callback dispatch sites only); `LauncherLoadingIcon.java` not read (only `setLoading` is used).
- Read-only commands: `apkutils manifest|packages|xref|mtds` on the APK; small Python scripts parsing the class files (method/flag inventory, constant pool of `Home$$ViewBinder.class`) and the two JaCoCo XML reports (method and line coverage); `tools/list_methods.py` printed to stdout only (`tools/coverage_methods.py` was read, not run); `grep` over sources and resources. No file other than this report was written (a temporary class-inventory JSON in `/tmp` was deleted).

