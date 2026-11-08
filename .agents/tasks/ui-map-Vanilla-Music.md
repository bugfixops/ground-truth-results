# Vanilla-Music 1.3.2: UI map and modeling plan (read-only investigation)

## Summary

- Vanilla-Music is a single-task music player with **no onboarding, login, account, vault or network gate**. The launcher opens `LibraryActivity` (a ViewPager of library tabs plus a sliding "now playing / queue" panel). The only real setup gates are the **storage runtime permission** (READ+WRITE_EXTERNAL_STORAGE on API 27) and **songs indexed by Android's MediaStore**. Both were met in the baselines: `PermissionRequestActivity.onCreate` never ran, and the scanner parsed ID3 tags in both runs.
- Scope: **1468 JaCoCo methods** in 209 classes. There are 247 compiled classes without JacocoInstrument; the other 38 are interfaces, constant holders and synthetic classes with no methods. The bytecode has 1603 methods with code; the 135 extra are 80 `access$`, 30 bridge, 6 synthetic constructors, 6 enum `values/valueOf`, 10 trivial constructors and 3 switch-map `<clinit>`. There are **no lambdas**.
- Entry points: 13 activities (4 reachable from outside: launcher, VIEW audio, MEDIA_PLAY_FROM_SEARCH, launcher shortcuts and widgets through a non-exported pseudo activity), an exported `PlaybackService`, a JobService, `MediaButtonReceiver`, 6 home-screen widgets and a FileProvider. There is no Application class and no `configChanges`, so rotation recreates every activity.
- Proposed **97 pages** in 4 modeling areas: LIBRARY (373 methods, 40 pages), PLAYBACK (510, 25), SETTINGS_DATA (370, 30), DSLV drag-sort library (215, 0 pages); plus 2 shared pseudo pages.
- Monkey missed 566 methods. My rough classification:
  - 154 DEAD candidates: unused DSLV cursor adapters and API, `FancyMenuItem` MenuItem stubs, unused tab-layout API, utility constructors.
  - 18 FRAMEWORK_ONLY candidates.
  - 75 that need an external entry point or system event: VIEW/search intents, widgets, shortcuts, MEDIA_BUTTON, JobScheduler, audio focus, service destroy, revoked permission.
  - 64 that need fixtures, preferences or the environment: non-MP3 formats, cover images, plugins, M3U sync, readahead.
  - 255 reachable through the UI, 189 of which APE hit.
- **The largest Monkey gap is long-press.** Every `FancyMenu` context menu (library rows, queue rows, playlist rows), the shuffle/repeat context menus, cover long-press and every dialog behind them were hit only by APE.
- Baseline caveats:
  - The Monkey run apparently started with existing app data, or it lost the probes of the first process. The DB `onCreate` methods were hit only by APE, `ScheduledLibraryUpdate.jobsEqual` only by Monkey, and Monkey crashed the app twice.
  - APE deleted fixture songs mid-run.

## 0. Conventions

- `SRC` = `/Users/darshan/Desktop/yang/work/final_java_only/Vanilla-Music/app/Vanilla-Music-#1.3.2/app/src/main`. `MAN` = `SRC/AndroidManifest.xml`. `V/` = `SRC/java/ch/blinkenlights/android/vanilla/`, `ML/` = `SRC/java/ch/blinkenlights/android/medialibrary/`, `BP/` = `SRC/java/ch/blinkenlights/bastp/`, `DS/` = `SRC/java/com/mobeta/android/dslv/`, `TB/` = `SRC/java/android/support/iosched/tabs/`, `RES/` = `SRC/res/`.
- `JM` / `JA` = `final_java_only/Vanilla-Music/monkey/report/report.xml` / `.../ape/report/report.xml`. "M+ / A+" = the method (or line) was covered by Monkey / APE. Line-level claims ("line N executed") come from the `<sourcefile><line ci=..>` entries of these XML files.
- Labels: `SRC` (read in app source), `FW-MEMORY` (Android behaviour recalled, not checked), `INFERRED`, `UNVERIFIED`. No framework source was available, so there is no `FW-SRC`.
- No merged manifest exists: `app/build/intermediates` only contains `javac/debug/classes`. I decoded the binary `AndroidManifest.xml` inside `Vanilla-Music-#1.3.2-rebuilt.apk` with a small read-only Python AXML parser; it matches `MAN` and only adds the library provider `androidx.startup.InitializationProvider`. There are no build flavors (`app/build.gradle:18-27`: release/debug only; debug has `testCoverageEnabled`).
- Joining JaCoCo to source: the JaCoCo `line` attribute is the first line with code, which for constructors can be a field initializer. Example: `MediaMetadataExtractor.<init>(String,boolean)` is reported at line 224 but declared at `ML/MediaMetadataExtractor.java:245`. Join on name+descriptor, not on line.
- Other environment facts:
  - minSdk 26, targetSdk 34, compileSdk 34 (`Vanilla-Music-#1.3.2/build.gradle:16-20`); the baseline device is API 27.
  - No JDK runtime is installed (`javap` unavailable), so the bytecode method list above came from a Python class-file parser.

## 1. Entry points

No `android:name` on `<application>` (`MAN:49-54`, same in the APK manifest), so the app uses the default `android.app.Application`. `allowBackup="true"`, `resizeableActivity="true"`, `requestLegacyExternalStorage="true"` (`MAN:50-54`). No component declares `configChanges` or `screenOrientation` (grep of `MAN`). `<queries>` asks for `ch.blinkenlights.android.vanilla.action.REQUEST_PLUGIN_PARAMS` (`MAN:43-47`).

| Component | Kind | exported | Intent filters / meta-data | launchMode, theme | Notes |
|---|---|---|---|---|---|
| `LibraryActivity` | activity | **true** (`MAN:76`) | MAIN + `android.intent.action.MUSIC_PLAYER`; categories LAUNCHER, APP_MUSIC, DEFAULT (`MAN:78-84`); meta `android.app.shortcuts` → `RES/xml/shortcuts.xml` (`MAN:86-88`) | singleTask (`MAN:77`); `@style/Library` = no action bar (`RES/values-v21/theme-standard_light.xml:43-46`) | Launcher activity. Static shortcuts "Play" (`TOGGLE_PLAYBACK`) and "Random" (`RANDOM_MIX_AUTOPLAY`) both target `ShortcutPseudoActivity` (`RES/xml/shortcuts.xml:4-28`) |
| `FullPlaybackActivity` | activity | false (no filter) | – | singleTask (`MAN:70-72`); runtime theme `Playback` (action bar with `homeAsUp`, `RES/values-v21/theme.xml:21-24`) via `ThemeHelper.setTheme` (`V/FullPlaybackActivity.java:109`) | Now-playing screen |
| `PlaylistActivity` | activity | false | – | singleTask (`MAN:91-93`); runtime `BackActionBar` | Playlist editor |
| `MiniPlaybackActivity` | activity | false | – | singleInstance, excludeFromRecents, `@style/PopupDialog` (`MAN:94-98`; dialog look, parent `Theme.Material.Light.Dialog.MinWidth`, `RES/values-v21/theme-standard_light.xml:48`) | Only target: notification content intent when pref `notification_action`=1 (`V/PlaybackService.java:2086-2088`) |
| `PreferencesActivity` | activity | false | – | standard (`MAN:188-189`); runtime `BackActionBar` | `PreferenceActivity` with 12 headers (`RES/xml/preference_headers.xml:23-60`) |
| `TabOrderActivity`, `FilebrowserStartActivity`, `PlaylistObserverDirActivity`, `MediaFoldersSelectionActivity` | activities | false | – | standard (`MAN:190-197`); runtime `BackActionBar` | Reached only from preference screens |
| `PermissionRequestActivity` | activity | false | – | `@android:style/Theme.Translucent.NoTitleBar` (`MAN:198-200`) | Requests permissions, then kills the process (`V/PermissionRequestActivity.java:64-90`) |
| `ShortcutPseudoActivity` | activity | **false (explicit)** (`MAN:205`) | MAIN action (`MAN:206-208`) | Translucent.NoTitleBar | No UI. Forwards 13 actions to `PlaybackService` and throws `IllegalArgumentException` on unknown actions (`V/ShortcutPseudoActivity.java:44-81`). Started by launcher shortcuts, pinned shortcuts and widget PendingIntents. The shell cannot start it (not exported) unless root (FW-MEMORY) |
| `AudioPickerActivity` | activity | **true** (`MAN:214`) | VIEW + DEFAULT, scheme `file` or `content`, mime `audio/*`, `application/ogg`, `application/x-ogg`, `application/x-flac`, `application/itunes` (`MAN:215-234`) | PopupDialog, excludeFromRecents (`MAN:211-213`) | "Open with" for audio files |
| `AudioSearchActivity` | activity | **true** (`MAN:238`) | `android.media.action.MEDIA_PLAY_FROM_SEARCH` + DEFAULT (`MAN:240-243`) | PopupDialog, excludeFromRecents | No content view. AsyncTask plays the search result, then finishes (`V/AudioSearchActivity.java:37-94`) |
| `PlaybackService` | service | **true** (`MAN:173`) | actions `...action.PLAY`, `PAUSE`, `TOGGLE_PLAYBACK`, `NEXT_SONG`, `PREVIOUS_SONG` (`MAN:174-180`) | `foregroundServiceType=mediaPlayback` (`MAN:172`) | Started service. `onStartCommand` handles 13 actions (`V/PlaybackService.java:536-606`); `onBind` returns null (`:1708-1711`) |
| `ScheduledLibraryUpdate` | JobService | true, `BIND_JOB_SERVICE` (`MAN:183-186`) | – | – | Periodic job id 9 requiring charging + idle, every 32 h (`V/ScheduledLibraryUpdate.java:39, 51-73`) |
| `MediaButtonReceiver` | receiver | **true** (`MAN:166`) | MEDIA_BUTTON, priority 999 (`MAN:167-169`) | – | `onReceive` → `processKey` (`V/MediaButtonReceiver.java:172-180`) |
| `OneCellWidget`, `FourLongWidget`, `FourWhiteWidget`, `WidgetE`, `FourSquareWidget`, `WidgetD` | AppWidgetProvider | false (`MAN:99-164`) | APPWIDGET_UPDATE; meta `android.appwidget.provider` → `RES/xml/{one_cell_widget,four_long_widget,four_white_widget,widget_e,four_square_widget,widget_d}.xml` | – | Buttons → `ShortcutPseudoActivity` actions; cover/title → `LibraryActivity` (`V/FourLongWidget.java:129-140`, `V/WidgetD.java:126-148`, …) |
| `JacocoInstrument.SMSInstrumentedReceiver` | receiver | true | `edu.gatech.m3.emma.COLLECT_COVERAGE` (`MAN:252-257`) | – | Coverage harness, out of scope. Dumps with `reset=true` (`V/JacocoInstrument/JacocoInstrumentation.java:59-61`) |
| `androidx.core.content.FileProvider` | provider | false, grantUriPermissions (`MAN:60-68`) | `root-path "."` (`RES/xml/provider_paths.xml:2-4`) | – | Used by `MediaUtils.shareMedia` (`V/MediaUtils.java:369-393`) |
| `androidx.startup.InitializationProvider` | provider (merged from libraries) | false | emoji2 + lifecycle initializers | – | APK manifest only. Library code, outside the class dirs |

Permissions: WAKE_LOCK, FOREGROUND_SERVICE(+_MEDIA_PLAYBACK), READ/WRITE_EXTERNAL_STORAGE, MODIFY_AUDIO_SETTINGS, READ_MEDIA_IMAGES/AUDIO, INSTALL_SHORTCUT, POST_NOTIFICATIONS (`MAN:30-41`).

## 2. First-run flow and setup gates

### 2.1 Cold start (first launch from the launcher)

1. `LibraryActivity.onCreate` (`V/LibraryActivity.java:159-207`):
   - `ThemeHelper.setTheme(Library)`.
   - `PlaybackActivity.onCreate` registers the activity as a `TimelineCallback` and starts a worker `HandlerThread` (`V/PlaybackActivity.java:95-108`).
   - `checkForLaunch` opens `FullPlaybackActivity` only if pref `playback_on_startup` and the action is MAIN (`:242-248`; default false, `V/PrefDefaults.java:56`).
   - `setContentView(library_content)`, then `LibraryPagerAdapter`.
   - `BottomBarControls.enableOptionsMenu`, which calls `onCreateOptionsMenu` on a PopupMenu (`V/BottomBarControls.java:153-195`).
   - **Permission check** (`:187-189`).
   - `loadTabOrder`, restore the last page from pref `library_page` (`:194-198`), `loadLimiterIntent`, `bindControlButtons`.
2. `onStart` → `PlaybackActivity.onStart` starts `PlaybackService` if it is not running (`V/PlaybackActivity.java:120-127`), then `LibraryActivity.loadPreferences/loadTabOrder/updateHeaders` (`V/LibraryActivity.java:211-218`).
3. `PlaybackService.onCreate` (`V/PlaybackService.java:442-533`):
   - Restores the queue state file (`loadState`, `:2004-2027`).
   - Creates the 2 MediaPlayers, reads prefs, registers the NOISY/SCREEN_ON receiver (`:497-501`) and the library observer (`:503`).
   - Creates `MediaSessionTracker` (`:508`) and `PlaylistObserver` (`:513`), which creates `playlist_observer.db` and a FileObserver on `/sdcard/Playlists` (`V/PlaylistObserver.java:115-145`).
   - Runs `initWidgets` (`:518`) and `setCurrentSong(0)` (`:521`).
   - `setCurrentSong(0)` → `MediaUtils.isSongAvailable` → `MediaLibrary.getLibrarySize` → `getBackend`, which creates `media-library.db`, a `MediaScanner` and **`startQuickScan(50)`** (`ML/MediaLibrary.java:115-127`).
   - Calls `ScheduledLibraryUpdate.scheduleUpdate` (`:532`).
4. The quick scan runs on "MediaScannerThread". It queries Android's MediaStore (`IS_MUSIC != 0`) and inspects each listed file (`ML/MediaScanner.java:349-386, 389-420, 481-…`). Inserted songs notify observers. `PlaybackService.mObserver` → `LibraryActivity.onMediaChange` → requery (`V/PlaybackService.java:1941-1952, 1478-1490`; `V/LibraryActivity.java:975-979`).
5. First-run queue is empty: `setCurrentSong` sets `FLAG_EMPTY_QUEUE` when no song is current but songs exist (`V/PlaybackService.java:1326-1333`).
   - `play()` with an empty queue switches to random mode (`:1211-1213`).
   - `FullPlaybackActivity` shows an "empty queue" overlay; tapping it enables random mode (`V/FullPlaybackActivity.java:229-236, 642-643`).

### 2.2 Setup gates

| Gate | Enforcing code | Effect when not met | Baseline |
|---|---|---|---|
| Storage permission. On API 27: READ_ + WRITE_EXTERNAL_STORAGE (`V/PermissionRequestActivity.java:146-154`) | `havePermissions` (`:137-144`)<br>`LibraryActivity` injects a clickable banner `permission_request` (`V/LibraryActivity.java:187-189`, `V/PermissionRequestActivity.java:98-112`)<br>`AudioPickerActivity`/`AudioSearchActivity` redirect to the permission request (`V/AudioPickerActivity.java:80`, `V/AudioSearchActivity.java:47`) | MediaStore queries throw SecurityException (caught), so the library stays empty (`ML/MediaScanner.java:354-358`).<br>Tapping the banner opens `PermissionRequestActivity` and the system dialog. If all needed permissions are granted: `finish`, restart the callback intent with NEW_TASK\|CLEAR_TASK, then `killProcess` (`:64-90`). If denied, only `finish` | **Not a gate in either run.** `showWarning`, `onCreate` and `onRequestPermissionsResult` never ran; `LibraryActivity.java:188` was never executed. INFERRED: the APK was installed with permissions pre-granted |
| Songs present and indexed by MediaStore | Quick scan depends on MediaStore (`ML/MediaScanner.java:349-420`) | No songs: tabs empty, `FLAG_NO_MEDIA`, FullPlayback "no songs" overlay (`V/FullPlaybackActivity.java:230-231`).<br>Workaround inside the app: Settings › Media library › "Full scan" › Start walks the media folders directly (`ML/MediaScanner.java:135-145, 444-466`) | Met. `MediaScanner.rpcInspectFile` and `ID3v2File.*` hit by both. Setup note "push fixtures/Music + media scan" (`final_java_only/MANIFEST.csv:14`) |
| Non-empty queue (soft gate) | `FLAG_EMPTY_QUEUE` (`V/PlaybackService.java:1318-1340`) | Queue panel empty; FullPlayback overlay; Clear/Empty/Save-queue are no-ops | Any row tap fills the queue |
| POST_NOTIFICATIONS | `getOptionalPermissions`, API 33+ only (`V/PermissionRequestActivity.java:156-161`) | n/a on API 27 | n/a |
| Anything else (intro, login, vault, account, network)? | **None.** The only network use is the "clone check" DNS lookup in `SlidingPlaybackActivity.adjustSpines` (`V/SlidingPlaybackActivity.java:295-307`). It shows a toast only if `<pkg>.spx.eqmx.net.` resolves | – | Toast lines `:298-302` never ran in either run (lookup failed) |

### 2.3 Screens the baseline never reached and the likely gate

| Screen / feature (classes) | Monkey | APE | Most likely reason |
|---|---|---|---|
| `AudioPickerActivity` (+Worker), `AudioSearchActivity` (+Worker) | – | – | External entry point only (VIEW audio / MEDIA_PLAY_FROM_SEARCH intents). Both tools start the app only through the launcher (`monkey/status.json` command `monkey -p …`) |
| `ShortcutPseudoActivity`, launcher shortcuts, widget buttons, all 6 widget `onUpdate/onEnabled/onDisabled` | – | – | Home-screen widgets and launcher shortcuts live outside the package; the activity is not exported |
| `MiniPlaybackActivity` | – | – | Needs pref notification_action = mini player (APE did set it: `V/PlaybackService.java:2087-2088` A+) **and** a tap on the notification in the shade |
| `MediaFoldersSelectionActivity` (and `FolderPickerActivity` tristate spinner, long-press dialog, `setFolderState`) | – | – | Settings › Media library › Edit opens a confirm dialog; APE only pressed Cancel (`PreferencesMediaLibrary$4.onClick` A+, `$5.onClick` never) |
| `PermissionRequestActivity`, permission banner | – | – | Permissions were pre-granted (§2.2) |
| `ScheduledLibraryUpdate.onStartJob/onStopJob` | – | – | JobScheduler needs charging + device idle (`V/ScheduledLibraryUpdate.java:56-58`) |
| `MediaButtonReceiver.onReceive`, `DelayedClickCounter`, `MediaSessionTracker$1.onSkipToNext/Previous/onSeekTo` | – | – | Hardware headset or external media controller. Media keys sent to the activity go through `PlaybackActivity.onKeyDown` instead (`V/PlaybackActivity.java:163-174`) |
| Every `FancyMenu` context menu: library rows, Files rows, queue rows, playlist rows. Also PlaylistDialog / PlaylistInputDialog / TrackDetailsDialog, delete confirmations, rename, "add to home screen", shuffle/repeat context menus, cover long-press | – | A+ | **Long-press.** `CoordClickListener.onItemLongClick`, `PlaybackActivity.onCreateContextMenu`, `FullPlaybackActivity.onLongClick` and `DragSortController.onLongPress` have 0 Monkey hits. Monkey's random touches are short down/up pairs (FW-MEMORY) |
| `TabOrderActivity`, `FilebrowserStartActivity`, `PlaylistObserverDirActivity`, Prefs › Library and Prefs › Notifications fragments | – | A+ | Depth: random navigation reached them only in APE |
| FullPlayback "empty queue" overlay, "Enqueue current ›" submenu, Share, Add to playlist, delete confirm, JumpToTime OK | – | A+ | INFERRED: Monkey's queue was never empty while FullPlayback was visible (possibly a restored queue, §2.4), and Monkey rarely went 2 menu levels deep |
| Library "Album artists"/"Composers" tabs | – | – | Hidden by default (`V/LibraryPagerAdapter.java:78`). Neither run enabled them: `LibraryPagerAdapter.java:301-309` never executed |
| Wide (≥600dp) library layout with the queue always visible | – | A+ | Rotation to landscape picks `RES/layout-w600dp/library_content.xml:59-68` (`slider_always_expanded`). `SlidingView.java:198` executed only in APE (INFERRED: APE rotated) |
| Queue menu items "Dequeue rest", "Empty the queue", "Save as playlist"; Library "Go home"; Files sort by size/time/extension | – | – | Mode-gated menu items. Visible only with the queue fully expanded (`V/SlidingPlaybackActivity.java:315-342`) or on the Files tab (`V/LibraryActivity.java:863-871`); `FileSystemAdapter.java:136-145` never executed |

### 2.4 Baseline anomalies that matter for target selection

1. **Coverage is collected in ~30 s deltas.** `getExecutionData(true)` resets after each dump (`V/JacocoInstrument/JacocoInstrumentation.java:59-61`), there are 120 snapshots per run (`monkey/coverage/*.json`), and `merged.ec` unions them. Probes executed after the last dump of a process that dies are lost. **Monkey crashed the app 2 times** (`final_java_only/combined_ape_monkey_api27.csv`, `monkey_app_crashes=2`); APE had 0 crashes (`summary_ape_api27.csv`).
2. **Monkey looks like it started with existing app data, or it lost the first process.**
   - First-run-only code was hit only by APE: `MediaLibraryBackend.onCreate`, `MediaSchema.createDatabaseSchema`, `PlaylistObserver.onCreate`, `MediaLibrary.discoverDefaultMediaPaths/discoverDefaultBlacklistedPaths`, `MediaLibrary$Preferences.<init>`.
   - `ScheduledLibraryUpdate.jobsEqual` runs only when a job is already pending (`V/ScheduledLibraryUpdate.java:60-65`). It was hit only by Monkey; APE never executed line 62.
   - `CoverCache$BitmapDiskCache.onCreate` was hit by both, which weakens the "old data" explanation.
   - UNVERIFIED. Resolving it needs the run logs or the snapshot contents.
   - These first-run methods are reachable; Monkey just did not record them.
3. **APE deleted fixture files mid-run.** `PlaybackService.deleteMedia` lines `:1740-1744` (`File.delete()` succeeded) and `MediaLibrary.removeSong` were A+. Library contents therefore changed during the APE run. `Delete` on a Files-tab folder deletes recursively (`V/MediaUtils.java:467-477`).
4. Monkey probably used the notification shade. `PlaybackService.java:560` (`ACTION_NEXT_SONG`) was executed only by Monkey, and that plain action is sent only by the notification "next" button, widgets and shortcuts (`:2120-2142`) (INFERRED).

### 2.5 What a harness must prepare

- **Install and permissions:** grant READ/WRITE_EXTERNAL_STORAGE (`adb install -g` or `pm grant`), or revoke them on purpose to reach `PermissionRequestActivity` (banner, system dialog, process restart). Clear app data (`pm clear`) before each run so first-run code is observable.
- **Media:**
  - Push `_fixtures/Music` (12 ID3v2.3 MP3 with title/artist/album-artist/album/track/genre/year tags, 3 WAV; read with a Python ID3 reader) and trigger the MediaStore scan **before** first launch.
  - The fixtures have **no** composer tags (Composers tab stays empty), **no** embedded art and **no** ReplayGain tags.
  - Re-push after every run: deletes are destructive (§2.4).
- **Extra fixtures to unlock fixture-gated code:**
  - One each of FLAC, Ogg Vorbis, Opus, M4A, MIDI, ADTS-AAC and a raw MP3 without ID3 (`BP/Bastp.java:49-110`).
  - Files with REPLAYGAIN_* or R128_* tags (`V/BastpUtil.java:72-110`).
  - Any `*.jpg`/`*.png` (ideally `cover.jpg`) inside the music folder for covers (`V/CoverCache.java:212-216, 406-509`).
  - A corrupt or unplayable audio file (`V/PlaybackService.java:1400-1413`).
  - More than about 4 screens of songs, so the fast scroller appears (`RES/layout/listview.xml:29`; FW-MEMORY: min 4 pages).
  - An image or text file under the Files-tab start folder (`V/FileUtils.java:185-227`). `_fixtures/Pictures/*.jpg` and `_fixtures/Download/todo.txt` exist but are not pushed by the current setup.
  - An `.m3u` in `/sdcard/Playlists` plus pref `playlist_sync_mode`=1 or 255 (`V/PlaylistObserver.java:300-360`; `V/PrefDefaults.java:80-81`).
- **Preferences:** seed `shared_prefs` or flip them in the UI to reach:
  - Shake actions (`enable_shake`); idle timeout (`use_idle_timeout`); readahead.
  - Auto playlist (`playcounts_autoplaylist`>0); notification_action (mini / full / next).
  - display_mode 0/1; swipe/cover actions; double_tap (widgets); playback_on_startup.
  - Tab order (Album artists/Composers); playlist sync; replay gain; headset_only.
- **External apps and events:**
  - A dummy "plugin" APK with a receiver for `ch.blinkenlights.android.vanilla.action.REQUEST_PLUGIN_PARAMS` (`V/PluginUtils.java:65-78`).
  - Optionally a package `ch.blinkenlights.android.vanillaplug` (`V/PreferencesActivity.java:62, 277-294`).
  - `am start -a android.intent.action.VIEW -d file:///sdcard/Music/x.mp3 -t audio/mpeg` (AudioPicker).
  - `am start -a android.media.action.MEDIA_PLAY_FROM_SEARCH --es query …` (AudioSearch).
  - `cmd jobscheduler run -f ch.blinkenlights.android.vanilla 9` (job; FW-MEMORY).
  - Power key off/on → `SCREEN_ON` broadcast.
  - Another app taking audio focus.
  - Headset-hook double/triple press (`input keyevent 79`).
  - Placing widgets and pinning shortcuts in Launcher3.
  - Tapping notification actions (`cmd statusbar expand-notifications`; FW-MEMORY).
  - Rotation to landscape for the w600dp layout and for recreate paths.

## 3. Screens and navigation

### 3.1 Window inventory

- **Activities (13):** see §1. Six have UI pages: Library, FullPlayback, Mini, Playlist, Preferences (many instances), TabOrder. There are also 3 folder pickers sharing one base class, and AudioPicker. `ShortcutPseudoActivity`, `AudioSearchActivity` and `PermissionRequestActivity` have no own UI.
- **Fragments.** All are framework `android.app` fragments, managed through `getFragmentManager()`.
  - `ShowQueueFragment` is declared statically in `RES/layout/library_content.xml:74-76`, `RES/layout-w600dp/library_content.xml:82-84`, `RES/layout/full_playback.xml:53-56` and `RES/layout/full_playback_alt.xml:75`.
  - `PreferenceFragment`s: `AudioFragment`, `PlaybackFragment`, `LibraryFragment`, `NotificationsFragment`, `ShakeFragment`, `CoverArtFragment`, `MiscFragment`, `PlaylistFragment`, `ReplayGainFragment` (opened from Audio), `PreferencesTheme` (`V/PreferencesActivity.java:102-236`, `V/PreferencesTheme.java:33-66`).
  - Fragments without own UI: `EqualizerFragment`, which starts the audio-effect panel and calls `popBackStack` (`V/PreferencesActivity.java:147-170`); `HelpFragment`, which opens the wiki URL and finishes (`:239-250`); `HeadsetLaunchFragment`, which launches VanillaPlug or shows a dialog (`:270-310`).
  - `AboutFragment` is a WebViewFragment (`:254-266`).
  - `PreferencesMediaLibrary` is a plain Fragment with `RES/layout/medialibrary_preferences.xml`.
  - DialogFragments: `PlaylistDialog`, `PlaylistInputDialog`, `JumpToTimeDialog`, `TrackDetailsDialog`.
- **AlertDialogs:**
  - Sort (`V/LibraryActivity.java:887-911`).
  - Delete confirm in Library (`:781-797`) and in FullPlayback (`V/FullPlaybackActivity.java:383-407`).
  - Delete playlist (`V/PlaylistActivity.java:183-191`).
  - Plugin chooser (`V/PlaybackActivity.java:708-737`).
  - Media-library "change preferences?" confirmation (`V/PreferencesMediaLibrary.java:254-269, 392-404`).
  - Headset-launch "install helper?" (`V/PreferencesActivity.java:287-309`).
  - Folder state include/exclude/neutral (`V/FolderPickerActivity.java:274-291`).
  - DialogPreference dialogs: `ListPreferenceSummary` (11 keys), `SeekBarPreference` (5 keys), `IdlePreference` (1).
- **Menus and popups:**
  - Library options menu: a `PopupMenu` anchored on the bottom-bar "⋮" button. Invisible items that have an icon (Search) become bar buttons (`V/BottomBarControls.java:153-203`). The MENU key is intercepted (`V/LibraryActivity.java:333-336`).
  - FullPlayback: action-bar overflow menu with 3 submenus (Enqueue current ›, More from current ›, Add to playlist, which has no children) and an "Add to favorites" star (`V/FullPlaybackActivity.java:295-327`).
  - `FancyMenu`: a Material `BottomSheetDialog` listing `FancyMenuItem`s, used as the long-press context menu (`V/ui/FancyMenu.java:169-196`).
  - Activity context menus on the shuffle and repeat buttons (`V/PlaybackActivity.java:327, 330, 677-702`).
  - Spinner dropdown in the tristate folder picker (`V/FolderPickerActivity.java:79-88, 215-229`).
  - Action-bar Up on FullPlayback, Playlist, TabOrder, folder pickers and Preferences screens (`displayOptions homeAsUp`, `RES/values-v21/theme.xml:21-24`).
- **Tabs and pager:** `ViewPager R.id.pager` + `VanillaTabLayout R.id.sliding_tabs` (`RES/layout/library_content.xml:31-41`). Default visible tabs are Artists, Albums, Songs, Playlists, Genres, Files; Album artists and Composers are hidden (`V/LibraryPagerAdapter.java:72-78`).
- **Panel:** `SlidingView` (`V/SlidingView.java`), a drag-up bottom panel. In Library its stages are bottom bar → seek bar → controls → queue (`RES/layout/library_content.xml:54-77`). In FullPlayback they are controls → queue (`RES/layout/full_playback.xml:32-57`).
- **Not used:** ActionMode/CAB, NavigationDrawer, Navigation component, RecyclerView, BottomNavigation (grep of `SRC/java`).

### 3.2 Navigation between windows

| From (gesture) | Handler chain | To | Evidence |
|---|---|---|---|
| Library: tap bottom bar, or menu "Playback view" | `BottomBarControls.onClick` → `LibraryActivity.onClick` → `openPlaybackActivity` | FullPlayback (`startActivity`) | `V/BottomBarControls.java:107-118`; `V/LibraryActivity.java:585-588, 451-456, 880-882` |
| Any playback activity: menu "Settings" | `PlaybackActivity.onOptionsItemSelected` MENU_PREFS | PreferencesActivity | `V/PlaybackActivity.java:411-413` |
| Library: tap a playlist row (default action 9 expands) or its arrow | `LibraryPagerAdapter.onItemClick` / `MediaAdapter.onClick` → `onItemClicked` / `onItemExpanded` → `editPlaylist` | PlaylistActivity | `V/LibraryPagerAdapter.java:894-904`; `V/MediaAdapter.java:611-617`; `V/LibraryActivity.java:463-498, 732-738` |
| Library: tap artist/album/genre row or arrow | `expand` → `LibraryPagerAdapter.setLimiter` → switch tab | same activity, limited tab | `V/LibraryActivity.java:435-445`; `V/LibraryPagerAdapter.java:517-607` |
| Library: tap song or file row, or header "Play all" | `pickSongs` → `PlaybackService.addSongs` (worker) | stays; queue filled | `V/LibraryActivity.java:383-425` |
| Library: tap image/text file | `FileSystemAdapter.onItemClicked` → `FileUtils.dispatchIntent` | external viewer (`ACTION_VIEW file://`) | `V/FileSystemAdapter.java:440-453`; `V/FileUtils.java:185-227` |
| Long-press a row (Library, Files, queue, playlist) | `CoordClickListener.onItemLongClick` → `…onItemLongClickWithCoords` → `FancyMenu.show` | bottom sheet | `V/ext/CoordClickListener.java:69-91`; `V/LibraryPagerAdapter.java:883-891`; `V/ShowQueueFragment.java:104-136`; `V/PlaylistActivity.java:204-227` |
| FullPlayback: Up / More from › / tap info table / SEARCH key | `PlaybackActivity.openLibrary` (CLEAR_TOP + extras type/id/folder); SEARCH key starts Library with extra `launch_search` | Library: `onNewIntent` → `loadLimiterIntent` | `V/FullPlaybackActivity.java:336-350, 442-446, 646-647`; `V/PlaybackActivity.java:625-654`; `V/LibraryActivity.java:254-287` |
| MiniPlayback: tap cover | `MiniPlaybackActivity.onClick` | FullPlayback + finish | `V/MiniPlaybackActivity.java:54-63` |
| Notification: tap content | PendingIntent per pref `notification_action`: 0 Library (default), 1 Mini, 2 Full, 3 service NEXT_AUTOPLAY | activity / service | `V/PlaybackService.java:2078-2105` |
| Notification: prev / play-pause / next | `PendingIntent.getService` → `onStartCommand` | service | `V/PlaybackService.java:2120-2142` |
| Widget buttons, launcher shortcuts, pinned shortcuts | `ShortcutPseudoActivity.onCreate` → `startService` | service (no UI) | `V/ShortcutPseudoActivity.java:44-81`; `V/SystemUtils.java:43-94` |
| Double tap within 400 ms on widget (pref `double_tap`) | `onStartCommand` `ACTION_*_DELAYED` | LibraryActivity (NEW_TASK) | `V/PlaybackService.java:549-572` |
| Preferences: header tap | single-pane PreferenceActivity starts a new `PreferencesActivity` with the header fragment (FW-MEMORY) | sub-screen | `RES/xml/preference_headers.xml:24-59` |
| Prefs › Library › Tabs / Filebrowser start; Prefs › Playlists › sync folder | `<intent>` in a PreferenceScreen | TabOrder / FilebrowserStart / PlaylistObserverDir | `RES/xml/preference_library.xml:26-32, 60-66`; `RES/xml/preference_playlist.xml:44-51` |
| Prefs › Media library › Edit › Yes | `editButtonPressed` → `startMediaFoldersSelection` | MediaFoldersSelection | `V/PreferencesMediaLibrary.java:385-412` |
| Prefs › Help; About links | `HelpFragment` (ACTION_VIEW wiki + finish); WebView links (no WebViewClient, FW-MEMORY: opens browser) | browser | `V/PreferencesActivity.java:239-266`; `SRC/assets/about.html` (7 hrefs) |
| Permission banner tap | `PermissionRequestActivity$1.onClick` → `requestPermissions` → `PermissionRequestActivity` → system dialog → `onRequestPermissionsResult` | callback intent in a new task + `killProcess` | `V/PermissionRequestActivity.java:98-129, 64-90` |

- **Back:**
  - Library: hide the slide if shrinkable → close search → pop the limiter (album → artist, artist/genre → clear, folder → parent) → `finish` (`V/LibraryActivity.java:290-332`).
  - FullPlayback: hide the slide if shrinkable (`V/FullPlaybackActivity.java:462-467`), otherwise default `finish`.
  - Others: default.
- **Up:**
  - Calls `finish` in TabOrder (`V/TabOrderActivity.java:70-78`), FolderPicker (`V/FolderPickerActivity.java:201-209`) and Playlist (`V/PlaylistActivity.java:308-316`).
  - Calls `openLibrary(null)` in FullPlayback.
  - PreferencesActivity has no Up handler; whether Up does anything there is UNVERIFIED.
- **Rotation (no `configChanges`):**
  - Every activity is recreated. `LibraryActivity.onCreate(state≠null)` skips `checkForLaunch` (`:164-166`).
  - Limiters survive through `LibraryPagerAdapter.saveState/restoreState` (`V/LibraryPagerAdapter.java:415-449`).
  - Search is closed by `BottomBarControls.onSaveInstanceState` (`:126-130`).
  - `ShowQueueFragment.onResume` repopulates the queue (`V/ShowQueueFragment.java:77-88`).
  - Landscape with ≥600 dp width switches Library to the two-pane w600dp layout.
- **Recreate on theme or display-mode change:**
  - `PlaybackService.loadPreference` calls `recreate()` on every registered TimelineCallback (`V/PlaybackService.java:938-943`).
  - `PreferencesActivity.onSharedPreferenceChanged` recreates the preference screens (`V/PreferencesActivity.java:94-100`).
  - `FullPlaybackActivity.onStart` restarts itself when the display mode changed (`V/FullPlaybackActivity.java:173-181`).

### 3.3 Modes per window

| Window | Mode variables that change active handlers / items | Evidence |
|---|---|---|
| `LibraryActivity` | (a) **current tab type**: adapter, header row (Artist/AlbArtist/Composer/Album/Song/Files only), row-tap meaning, context-menu item set, "Go home" item (Files only)<br>(b) **limiter set**: breadcrumb `ArrowedText` views clickable, Back pops the limiter, sort key `sort_<type>_<limiterType>`<br>(c) **search visible**: `onQueryTextChange/Submit`, Back closes it<br>(d) **SlidingView stage**: 0 = bar only; partial = seek bar/controls usable; fully expanded = queue usable, menu shows Hide queue / Dequeue rest / Empty / Save as playlist and hides Sort and Show queue; always-expanded (w600dp) = queue always visible, Sort plus queue items visible<br>(e) **permission missing**: banner<br>(f) prefs `default_action_int` (default 9 = expand-or-play-all), `tab_order`, `jump_to_enqueued_on_play`<br>(g) plugins installed: "Plugins" item<br>(h) library empty vs non-empty | `V/LibraryPagerAdapter.java:283-367`; `V/LibraryActivity.java:463-485, 503-569, 585-612, 675-729, 863-871`; `V/SlidingPlaybackActivity.java:315-342`; `V/SlidingView.java:169-216, 389-403`; `V/PrefDefaults.java:38` |
| `FullPlaybackActivity` | (a) **display_mode**: 2 (default) = `full_playback_alt` with info table (tap → library album, long-press → extra info); 0/1 = `full_playback` with info drawn on the cover<br>(b) **controls hidden** (DPAD-center/Enter or ToggleControls action): SlidingView GONE<br>(c) **queue expanded**: menu toggles, Back hides the slide<br>(d) **overlay** for EMPTY_QUEUE (tap → random mode) or NO_MEDIA (eats touches)<br>(e) extra-info visible<br>(f) favorite state of the star<br>(g) plugins installed<br>(h) prefs `cover_press_action`, `cover_longpress_action`, `swipe_up/down_action` (all default Nothing) | `V/FullPlaybackActivity.java:107-170, 186-236, 295-327, 454-519, 625-683`; `V/CoverView.java:355-482`; `V/PrefDefaults.java:36-37, 46, 61-62` |
| `MiniPlaybackActivity` | none besides playback state | `V/MiniPlaybackActivity.java:38-63` |
| `PlaylistActivity` | `mEditing` (drag/fling enabled, dragger visible, Delete hidden, row tap ignored); empty playlist | `V/PlaylistActivity.java:166-174, 287-295`; `V/PlaylistAdapter.java:96-121` |
| `PreferencesMediaLibrary` | scan running: Start/Edit/checkboxes disabled, Cancel visible; `mFullScanPending` skips the confirm dialog | `V/PreferencesMediaLibrary.java:313-346, 246-252, 385-390` |
| Preference screens | dependencies: Shake (`enable_shake`), Misc (`use_idle_timeout`), Playlists (`playlist_sync_mode`); ReplayGain bump sliders enabled only when RG is on | `RES/xml/preference_shake.xml:38,48`; `RES/xml/preference_misc.xml:46`; `RES/xml/preference_playlist.xml:45,54`; `V/PreferencesActivity.java:140-145` |
| `FolderPickerActivity` | tristate mode (MediaFolders only): spinner + long-press active, button "Save" vs "Select"; current path is a directory: Save/spinner enabled | `V/FolderPickerActivity.java:142-158, 166-191`; `V/MediaFoldersSelectionActivity.java:34-47` |
| `AudioPickerActivity` | loading (only Cancel) vs resolved (Play; Enqueue only if the service is running) | `V/AudioPickerActivity.java:71-115, 157-182` |
| `PlaylistInputDialog` | text equals the initial text: positive disabled; name exists: label "Overwrite" | `V/PlaylistInputDialog.java:108-141` |
| `PlaylistDialog` | song known: ☐/☑ markers | `V/PlaylistDialog.java:109-149` |

### 3.4 Candidate page list (97 pages)

Owner: L = LIBRARY, P = PLAYBACK, S = SETTINGS_DATA, ★ = shared/coordinator (see §6). The predicate uses field names from the code. Variants (`X@CTX`) are suggested where the same page or method serves several callers.

**Pseudo pages (6)**

| Page | Description | Window | Mode predicate | Owner |
|---|---|---|---|---|
| S_ENTRY | outside the app (launcher/home); search root | – | – | ★ |
| S_EXIT | app finished/crashed; process may survive with `PlaybackService.sInstance`, `MediaLibrary.sBackend`, `MediaUtils` caches | – | – | ★ |
| S_LIB_PAUSED | LibraryActivity stopped under Full/Playlist/Prefs/external, or Home | LibraryActivity | paused | L |
| S_PLAYLIST_PAUSED | PlaylistActivity stopped (Home, external, rotation) | PlaylistActivity | paused | L |
| S_FULL_PAUSED | FullPlaybackActivity stopped: Prefs, share chooser or another external activity on top, Home, or Library started above it while Library was not already below it in the task (otherwise CLEAR_TOP/singleTask destroys Full; FW-MEMORY) | FullPlaybackActivity | paused | P |
| S_PREFS_PAUSED | a PreferencesActivity instance under a sub-screen, TabOrder, folder picker or external app | PreferencesActivity | paused | S |

**Outside the app (11)**

| Page | Description | Window | Mode predicate | Owner |
|---|---|---|---|---|
| S_HOME_WIDGET | home screen with a Vanilla widget (1x1, 4x1 A/B/White, 2x2 A/B) | launcher | `sEnabled` of that provider | P |
| S_LAUNCHER_SHORTCUTS | long-press on the app icon: static "Play" and "Random" shortcuts, plus pinned shortcuts | launcher | – | P |
| S_NOTIFICATION_SHADE | shade with the playback notification (prev / play-pause / next / content tap) | SystemUI | notification visible (`VISIBILITY_WHEN_PLAYING` default) | P |
| S_SYS_PERMISSION_DIALOG | runtime permission dialog over translucent PermissionRequestActivity | system | permissions not granted | S |
| S_SYS_PIN_SHORTCUT | launcher "add to home screen" confirmation | launcher | `isRequestPinShortcutSupported()` | L |
| S_EXT_SHARE | share chooser for the current song (FileProvider URI) | ResolverActivity | – | P |
| S_EXT_VIEWER | external viewer for an image/text file from the Files tab | external | an activity resolves | L |
| S_EXT_BROWSER | browser (Help wiki, About links) | external | – | S |
| S_EXT_EQUALIZER | audio-effect control panel | external | an activity resolves (else exception swallowed) | S |
| S_EXT_MARKET | `market://` for VanillaPlug | external | market app installed (else toast) | S |
| S_EXT_PLUGIN | plugin activity (`LAUNCH_PLUGIN`) or the VanillaPlug launcher activity | external | plugin / VanillaPlug installed | P |

**LibraryActivity and its popups and dialogs (L, 36)**

Library tab pages (predicate fragments `stage0 = mSlidingView.mCurrentStage==0`, `!search = search view GONE`):

| Page | Description | Window | Mode predicate |
|---|---|---|---|
| S_LIB_ARTISTS | Artists tab, "Play all" header; tap = expand to albums | LibraryActivity | tab type ARTIST, limiter null, !search, stage0 |
| S_LIB_ALBUMS | Albums tab; tap = expand to songs | LibraryActivity | ALBUM, limiter null, … |
| S_LIB_SONGS | Songs tab; tap = play all from this row | LibraryActivity | SONG, limiter null, … |
| S_LIB_PLAYLISTS | Playlists tab, no header; tap = open PlaylistActivity; empty until a playlist exists | LibraryActivity | PLAYLIST |
| S_LIB_GENRES | Genres tab, no header; tap = expand | LibraryActivity | GENRE |
| S_LIB_FILES | Files tab at the browse start (default external storage root); folder tap = enter; audio = play; image/text = viewer | LibraryActivity | FILE, limiter = home |
| S_LIB_ALBUMARTISTS | hidden tab; needs tab order | LibraryActivity | ALBARTIST visible in `tab_order` |
| S_LIB_COMPOSERS | hidden tab; needs tab order; empty with the fixtures (no composer tags) | LibraryActivity | COMPOSER visible |
| S_LIB_ARTISTS_LIMITED | artists (or album artists/composers) of one genre; breadcrumbs | LibraryActivity | ARTIST\|ALBARTIST\|COMPOSER, limiter type GENRE |
| S_LIB_ALBUMS_LIMITED | albums of an artist/album artist/composer/genre; breadcrumbs | LibraryActivity | ALBUM, limiter ≠ null |
| S_LIB_SONGS_LIMITED | songs of an album/artist/genre; breadcrumbs | LibraryActivity | SONG, limiter ≠ null |
| S_LIB_FILES_SUBDIR | Files tab inside a folder: ".." row, path breadcrumbs, FileObserver active | LibraryActivity | FILE, limiter ≠ home |

Other Library modes:

| Page | Description | Window | Mode predicate |
|---|---|---|---|
| S_LIB_SEARCH | search box open (bar icon, SEARCH key); typing filters every tab | LibraryActivity | `mSearchView` VISIBLE |
| S_LIB_NO_PERMISSION | permission banner injected; lists empty | LibraryActivity | `!havePermissions` |
| S_LIB_CONTROLS | panel partially raised: seek bar and prev/play/next/shuffle/repeat usable | LibraryActivity | 0 < stage < last |
| S_LIB_QUEUE | panel fully raised: queue list (tap = jump, drag = move, fling handle = remove, long-press = menu) | LibraryActivity | stage == last (OVERLAY_EXPANDED) |
| S_LIB_WIDE | two-pane ≥600 dp layout: library left, queue always visible right | LibraryActivity | `mSliderAlwaysExpanded` |
| S_LIB_MENU | bottom-bar PopupMenu, slide not fully expanded: Playback view, Settings, Sort by, Show queue, Jump to time, Go home (Files only) | PopupMenu | expansion PARTIAL |
| S_LIB_MENU_QUEUE | PopupMenu when expanded/wide: Hide queue (expanded only), Dequeue rest, Empty the queue, Save as playlist, Jump to time, Settings, Playback view (+Sort in wide) | PopupMenu | expansion OVERLAY_EXPANDED or ALWAYS_EXPANDED |

Library context menus (FancyMenu bottom sheets), all from `LibraryActivity.onCreateFancyMenu` (`V/LibraryActivity.java:675-729`). Suggested variant: `LibraryActivity.onFancyItemSelected@<ROW>`.

| Page | Items | Window | Mode predicate |
|---|---|---|---|
| S_LIB_CTX_HEADER | "All songs": Add to playlist, Play all, Enqueue all | FancyMenu$Sheet | id == HEADER_ID |
| S_LIB_CTX_SONG | Add to playlist, Add to homescreen, Play, Play all, Enqueue as next, Enqueue, More from artist, More from album, Details, (Plugins), Delete | FancyMenu$Sheet | type SONG |
| S_LIB_CTX_ALBUM | … Play all, Expand, More from artist, Delete | FancyMenu$Sheet | type ALBUM |
| S_LIB_CTX_ARTIST | … Play all, Expand, Delete | FancyMenu$Sheet | type ARTIST |
| S_LIB_CTX_GROUP | album artist / composer / genre: no Play all; Expand if expandable | FancyMenu$Sheet | type ALBARTIST\|COMPOSER\|GENRE |
| S_LIB_CTX_PLAYLIST | … Rename, Delete (no Play all, no Expand) | FancyMenu$Sheet | type PLAYLIST |
| S_LIB_CTX_FILE | Open (image/text only), Play, Play all, Enqueue as next, Enqueue, Add to playlist, Delete (no homescreen) | FancyMenu$Sheet | type FILE, not a directory, not ".." |
| S_LIB_CTX_FOLDER | folder: Play, Play all, Enqueue…, Expand, Add to playlist, Delete (recursive) | FancyMenu$Sheet | type FILE, directory |

Library-owned dialogs and PlaylistActivity:

| Page | Description | Window | Mode predicate |
|---|---|---|---|
| S_DLG_SORT | sort-by single choice + Reverse checkbox + Done; dismiss applies | AlertDialog (LibraryActivity) | – |
| S_LIB_DLG_DELETE | "Delete <title>?" Delete/Cancel | AlertDialog | – |
| S_DLG_PLAYLIST_PICK | "Add to playlist": New playlist… + playlists (☐/☑ when song known). Variants @LIB_ROW @LIB_HEADER @FULL @QUEUE_ROW @QUEUE_SAVE | PlaylistDialog | `Playlist.queryPlaylists ≠ null` |
| S_DLG_PLAYLIST_NAME | name input; Create/Rename/Overwrite; Cancel. Variants @CREATE @RENAME | PlaylistInputDialog | – |
| S_DLG_TRACK_DETAILS | read-only song details, filled asynchronously | TrackDetailsDialog | – |
| S_PLAYLIST | playlist view: Edit/Delete header; tap = default playlist action (3 = play all from row); long-press = menu | PlaylistActivity | `!mEditing` |
| S_PLAYLIST_EDIT | edit mode: drag handle reorder, fling remove; Delete hidden | PlaylistActivity | `mEditing` |
| S_PLAYLIST_CTX | Play, Play all, Enqueue as next, Enqueue, Enqueue all, Details, Remove | FancyMenu$Sheet | – |
| S_PLAYLIST_DLG_DELETE | "Delete playlist?" | AlertDialog | – |

**FullPlaybackActivity, Mini, AudioPicker and playback popups (P, 19)**

| Page | Description | Window | Mode predicate |
|---|---|---|---|
| S_FULL | now playing, default layout with info table, controls visible, slide partial | FullPlaybackActivity | `mDisplayMode==2 && mControlsVisible && stage0 && !overlay` |
| S_FULL_COVERINFO | display mode 0 (overlap) or 1 (below): no info table; cover rendered with text | FullPlaybackActivity | `mDisplayMode ∈ {0,1}` |
| S_FULL_CONTROLS_HIDDEN | controls and seek bar hidden (DPAD-center/Enter, or ToggleControls action) | FullPlaybackActivity | `!mControlsVisible` |
| S_FULL_QUEUE | queue panel expanded; Back hides it | FullPlaybackActivity | expansion OVERLAY_EXPANDED |
| S_FULL_EMPTY_QUEUE | "empty queue" overlay; tap = random mode | FullPlaybackActivity | `FLAG_EMPTY_QUEUE` |
| S_FULL_NO_MEDIA | "no songs" overlay; touches eaten | FullPlaybackActivity | `FLAG_NO_MEDIA` |
| S_FULL_MENU | overflow: Show queue, Jump to time, Settings, Delete, Enqueue current ›, More from current ›, Add to playlist, Share; star = favorites; (Plugins) | action-bar menu | expansion PARTIAL |
| S_FULL_MENU_QUEUE | overflow with queue items (Hide queue, Dequeue rest, Empty, Save as playlist, Jump to time, Settings); Delete/Enqueue/More/Add/Share hidden | action-bar menu | OVERLAY_EXPANDED |
| S_FULL_SUBMENU_ENQUEUE | Album / Artist / Genre | SubMenu | – |
| S_FULL_SUBMENU_MORE | Album / Artist / Genre / Folder: opens Library limited | SubMenu | – |
| S_FULL_DLG_DELETE | "Delete file <title>?" | AlertDialog | `mCurrentSong ≠ null` |
| S_CTX_SHUFFLE | No shuffle / Shuffle songs / Shuffle albums. Variants @LIB @FULL @MINI | ContextMenu | long-press on the shuffle button |
| S_CTX_REPEAT | No repeat / Repeat / Repeat current / Stop current / Random. Variants @LIB @FULL @MINI | ContextMenu | long-press on the repeat button |
| S_QUEUE_CTX | queue row menu: Play, Enqueue album/artist/genre, Add to playlist, Move to top/bottom, Details, Remove. Variants @LIB @FULL | FancyMenu$Sheet | – |
| S_DLG_JUMP_TO_TIME | hh:mm:ss input; OK = seek. Variants @LIB @FULL | JumpToTimeDialog | – |
| S_DLG_PLUGINS | plugin chooser. Variants @LIB @FULL | AlertDialog | plugins installed |
| S_MINI | dialog mini player: cover tap → Full; controls | MiniPlaybackActivity | – |
| S_AUDIO_PICKER_LOADING | resolving the URI; only Cancel | AudioPickerActivity | worker running |
| S_AUDIO_PICKER_READY | Play enabled; Enqueue enabled only if the service already exists | AudioPickerActivity | `mSong ≠ null` |

**Settings, folder pickers, permission (S, 25)**

| Page | Description | Window | Mode predicate |
|---|---|---|---|
| S_PREFS | header list (12 headers) | PreferencesActivity | no `:android:show_fragment` extra (FW-MEMORY) |
| S_PREFS_AUDIO | Equalizer, ReplayGain ›, Volume during ducking, gapless, headset only, headset pause, Headset launch | PreferencesActivity + AudioFragment | – |
| S_PREFS_REPLAYGAIN | track/album RG checkboxes, bump and untagged sliders (enabled iff RG on) | ReplayGainFragment | – |
| S_PREFS_PLAYBACK | startup, display mode, swipe and cover actions | PlaybackFragment | – |
| S_PREFS_LIBRARY | Tabs ›, default action, playlist action, scroll-to-song ×2, jump to enqueued, Filebrowser start › | LibraryFragment | – |
| S_PREFS_NOTIFICATIONS | visibility, action | NotificationsFragment | – |
| S_PREFS_SHAKE | enable, action, threshold | ShakeFragment | – |
| S_PREFS_COVERART | 5 checkboxes | CoverArtFragment | – |
| S_PREFS_MISC | lockscreen, screen on, idle timeout, double tap, scrobble, stock broadcast, readahead | MiscFragment | – |
| S_PREFS_MEDIALIB | Start, Edit, group albums, force bastp, full scan, drop DB; stats | PreferencesMediaLibrary | `!progress.isRunning` |
| S_PREFS_MEDIALIB_SCANNING | scan running: Cancel visible, other controls disabled, progress updates | PreferencesMediaLibrary | `progress.isRunning` |
| S_PREFS_MEDIALIB_MENU | overflow: Dump database, Force M3U import | options menu | – |
| S_PREFS_PLAYLISTS | auto playlist slider, sync mode, sync folder ›, relative paths | PlaylistFragment | – |
| S_PREFS_THEME | 12 theme rows (`RES/values-v21/themes-list.xml`); tap = set theme, which recreates | PreferencesTheme | – |
| S_PREFS_ABOUT | WebView with `about.html` (JS toggles, external links) | AboutFragment | – |
| S_PREFS_BLANK | empty preferences screen left after the Equalizer or HeadsetLaunch fragment pops (UNVERIFIED; single-pane behaviour) | PreferencesActivity | – |
| S_DLG_LISTPREF | single-choice dialog. Variants @default_action_int @default_playlist_action @display_mode @swipe_up_action @swipe_down_action @cover_press_action @cover_longpress_action @notification_visibility @notification_action @shake_action @playlist_sync_mode | ListPreferenceSummary | – |
| S_DLG_SEEKBARPREF | slider dialog. Variants @volume_during_ducking (+ ignore-focus checkbox) @replaygain_bump @replaygain_untagged_debump @shake_threshold @playcounts_autoplaylist | SeekBarPreference | – |
| S_DLG_IDLEPREF | idle-timeout slider dialog | IdlePreference | `use_idle_timeout` |
| S_DLG_MEDIALIB_CONFIRM | "rescan required" Yes/Cancel. Variants @CHECKBOX @EDIT | AlertDialog | `!mFullScanPending` |
| S_DLG_HEADSET_LAUNCH | "helper app missing, install?" Yes/Cancel | AlertDialog | VanillaPlug not installed |
| S_TAB_ORDER | checkbox list with drag handles; Done, Restore default, Up | TabOrderActivity | – |
| S_FOLDER_PICKER | path field, folder list, Select. Variants @FILEBROWSER_START @PLAYLIST_DIR | FilebrowserStart/PlaylistObserverDir | tristate off |
| S_MEDIA_FOLDERS | tristate picker: spinner Include/Exclude/Neutral, long-press row, Save | MediaFoldersSelectionActivity | tristate on |
| S_DLG_FOLDER_STATE | long-press dialog Include/Exclude/Neutral | AlertDialog | tristate on, row ≠ ".." |

Other suggested variants:
- Shared button handlers: `PlaybackActivity.onClick@LIB|@FULL|@MINI`.
- Options-menu dispatch: `LibraryActivity.onOptionsItemSelected@MENU|@MENU_QUEUE`, `FullPlaybackActivity.onOptionsItemSelected@MENU|@MENU_QUEUE|@SUB_ENQUEUE|@SUB_MORE`.
- Shared dialog callback: `SlidingPlaybackActivity.updatePlaylistFromPlaylistDialog@<caller>`. `sourceIntent==null` means "save queue" → `MSG_ADD_QUEUE_TO_PLAYLIST` (`V/SlidingPlaybackActivity.java:168-185`).
- Folder picker: `FolderPickerActivity.*@FILEBROWSER_START|@PLAYLIST_DIR|@MEDIA_FOLDERS`.
- Service action dispatch: `PlaybackService.onStartCommand@<ACTION>`, `PlaybackService.performAction@<Action>` (callers: swipes, cover tap/long-press, shake).
- Media keys: `MediaButtonReceiver.processKey@ACTIVITY|@SESSION|@RECEIVER`.

## 4. Framework mechanisms that need FRAMEWORK / ASYNC / LIFECYCLE edges

| Mechanism | App classes and wiring | Notes for edges |
|---|---|---|
| ViewPager + PagerAdapter + tabs | `LibraryPagerAdapter`: `instantiateItem`, `setPrimaryItem`, `getItemPosition`, `saveState`/`restoreState`, `onPageSelected` (`V/LibraryPagerAdapter.java:283-449, 846-858`).<br>`SlidingTabLayout$InternalViewPagerListener` forwards page events to `LibraryPagerAdapter` (registered by `V/LibraryActivity.java:192`; `TB/SlidingTabLayout.java:134-142, 262-309`).<br>Tab tap: `SlidingTabLayout$TabClickListener.onClick` → `setCurrentItem` (`TB/SlidingTabLayout.java:311-323`) | `setPrimaryItem` → `LibraryActivity.onPageChanged` → MSG_SAVE_PAGE on the worker → `adjustSpines` (DNS) (`V/LibraryActivity.java:1028-1040, 950-955`).<br>`getItemPosition` runs only after `notifyDataSetChanged` from a tab-order change (FW-MEMORY) |
| ListView adapters | `MediaAdapter` (SortableAdapter/BaseAdapter + SectionIndexer for `fastScrollEnabled`, `RES/layout/listview.xml:29`)<br>`FileSystemAdapter`, `ShowQueueAdapter`, `PlaylistAdapter` (CursorAdapter), `TabOrderAdapter`, `FolderPickerAdapter` (ArrayAdapter), `FancyMenu$Adapter` (ArrayAdapter)<br>`FastScrollGuardedListView.onInterceptTouchEvent` (`V/FastScrollGuardedListView.java:65-77`) | `getCount/getView/getItemId/hasStableIds` run on layout/data change. `getItem` of MediaAdapter/FileSystemAdapter/TabOrderAdapter never ran (FRAMEWORK_ONLY candidates).<br>Section index `toString` only when the fast-scroll preview shows (FW-MEMORY: list ≥ 4 pages) |
| Handler/HandlerThread (main ASYNC mechanism; no executors) | `PlaybackActivity.mHandler` (per-activity worker) and `mUiHandler` (`V/PlaybackActivity.java:65-108`)<br>`LibraryPagerAdapter` worker/UI handlers (MSG_RUN_QUERY → MSG_COMMIT_QUERY, `:681-715`)<br>`PlaybackService` "PlaybackService" thread (`handleMessage` 14 messages, `V/PlaybackService.java:1544-1640`)<br>`MediaScanner` "MediaScannerThread" (`ML/MediaScanner.java:101-119, 205-301`)<br>`PlaylistObserver` thread (`V/PlaylistObserver.java:115-145, 212-243`)<br>`ReadaheadThread`, `CoverView`, `LazyCoverView` (static "LazyCoverRpc" thread, `V/LazyCoverView.java:97-170`), `TrackDetailsDialog`, `PlaylistActivity`/`PlaylistAdapter`<br>`MediaButtonReceiver` `Handler.postDelayed` (`V/MediaButtonReceiver.java:78-80`) | Model each message `what` as an `ASYNC` edge. Delays:<br>seek 150 ms (`V/SlidingPlaybackActivity.java:276-284`); SAVE_STATE 5 s; ENTER_SLEEP 60 s; IDLE_TIMEOUT pref; FADE_OUT 50 ms steps (`V/PlaybackService.java:211-223, 1564-1577`)<br>quick-scan coalesce 3.5 s (`ML/MediaScanner.java:98`); M3U coalesce 2.345 s (`V/PlaylistObserver.java:62`); media-key double click 600 ms |
| AsyncTask | `AudioPickerActivity$AudioPickerWorker`, `AudioSearchActivity$AudioSearchWorker` | `doInBackground` → `onPostExecute` on the main thread |
| runOnUiThread | `PlaybackActivity.setState/setSong` ($1/$2), `showToast` ($3); `LibraryActivity.updateCover` ($1); `PreferencesMediaLibrary$1$1`; `ShowQueueFragment$1`; `TrackDetailsDialog$1$1` | |
| In-app observer lists | `PlaybackService.sCallbacks` (TimelineCallback): `setState`, `setSong`, `replaceSong`, `onMediaChange`, `onTimelineChanged`, `onPositionInfoChanged`, `recreate` for every live PlaybackActivity and ShowQueueFragment (`V/PlaybackService.java:1089-1110, 1478-1490, 1716-1724, 1914-1939, 938-943`)<br>`MediaLibrary.sLibraryObservers`: `PlaybackService.mObserver`, `PlaylistObserver.mLibraryObserver`, `PreferencesMediaLibrary.mLibraryObserver`, `ScheduledLibraryUpdate.mObserver` (`ML/MediaLibrary.java:328-360`)<br>`SongTimeline.Callback` → `PlaybackService.activeSongReplaced/timelineChanged/positionInfoChanged` | `FRAMEWORK`-like CALL edges. Guards depend on which activities are alive (`needs_state`) |
| SharedPreferences listeners | `PlaybackService.onSharedPreferenceChanged` → `loadPreference` (29 keys; `coverloader_inline` is not handled, `V/PlaybackService.java:868-948, 1494`); `PreferencesActivity.onSharedPreferenceChanged` (`V/PreferencesActivity.java:94-100`) | Fire only on a value change (FW-MEMORY). `BackupManager.dataChanged` on every change (`:947`) |
| Started foreground service | `PlaybackService`: `startService` from `PlaybackActivity.onStart`; `startForeground` in `processNewState` and in `onStartCommand` with `EXTRA_EARLY_NOTIFICATION`; `START_NOT_STICKY`; never bound; never stops itself (no `stopSelf`) | `onDestroy` only if the system stops the service (FW-MEMORY: background limits on API 26+ after the app idles) or on `am stopservice` |
| JobScheduler | `ScheduledLibraryUpdate` | System → `onStartJob`; `onStopJob` when constraints are lost |
| Broadcast receivers | dynamic `PlaybackService$Receiver`: AUDIO_BECOMING_NOISY → pause if `headset_pause`; SCREEN_ON → `userActionTriggered` (`V/PlaybackService.java:1462-1476`)<br>manifest `MediaButtonReceiver`; 6 `AppWidgetProvider`s<br>outgoing: `com.android.music.playstatechanged` (pref `stock_broadcast`, default **true**), `net.jjc1138...MUSIC_STATUS` (pref `scrobble`, default false) (`:1147-1176`; `V/PrefDefaults.java:57, 60`) | |
| ContentObserver / FileObserver | `MediaScanner$1` on `MediaStore.Audio.Media.EXTERNAL_CONTENT_URI` → `startQuickScan(3500)` (`ML/MediaScanner.java:112-118`)<br>`FileSystemAdapter$Observer` on the browsed folder → requery (`V/FileSystemAdapter.java:382-394`)<br>`PlaylistObserver$2` on the playlist folder → import/full sync (`V/PlaylistObserver.java:614-649`) | External file system changes trigger these |
| Media playback | `VanillaMediaPlayer` ×2 with gapless `setNextMediaPlayer`; `onCompletion`/`onError` (`V/PlaybackService.java:657-663, 1420-1444`); audio focus `requestAudioFocus` / `onAudioFocusChange` (`:1035, 2160-2203`); accelerometer when shake is enabled (`:855-866, 2206-2231`) | `onError` is hit only by APE |
| MediaSession / remote | `MediaSessionTracker` (MediaSessionCompat callbacks → `MediaButtonReceiver.processKey`, `V/MediaSessionTracker.java:47-78`); `RemoteControlImplLp` is all no-ops | Media keys not consumed by an activity reach the session (FW-MEMORY) |
| Notifications | `NotificationHelper` channel; playback notification MediaStyle with 3 service actions plus the content intent (`V/PlaybackService.java:2078-2158`); scanner progress notification without actions (`ML/MediaScanner.java:317-345`) | Outside the package; only Monkey seems to have used it (§2.4) |
| Home-screen widgets and shortcuts | 6 providers updated from `PlaybackService.updateWidgets` (`V/PlaybackService.java:1119-1145`); static shortcuts (`RES/xml/shortcuts.xml`); pinned shortcuts (`V/SystemUtils.java:80-94`) | Need a launcher host |
| Database / storage layer | SQLiteOpenHelpers: `MediaLibraryBackend` (`media-library.db`, `ML/MediaLibraryBackend.java:42-96`), `CoverCache$BitmapDiskCache` (`covercache.db`, `V/CoverCache.java:200-260`), `PlaylistObserver` (`playlist_observer.db`)<br>default SharedPreferences (`V/SharedPrefHelper.java:42-47`); object-stream `_prefs-v1.obj` (`ML/MediaLibrary.java:135-160, 240-253`); queue state file `state` (`V/PlaybackService.java:2004-2050`)<br>MediaStore queries (scanner, `CoverCache` album art, `MediaUtils.getAndroidMediaIds`, `AudioPicker`) | `onUpgrade` ×3 only on a schema-version bump (FRAMEWORK_ONLY in a fresh install) |
| WebView | `AboutFragment`: JS enabled, `file:///android_asset/about.html`, no JS bridge (no `addJavascriptInterface`), no WebViewClient (`V/PreferencesActivity.java:254-266`) | No app callbacks from JS |
| SAF / file pickers | **none** (no OPEN_DOCUMENT/GET_CONTENT). Custom `FolderPickerActivity`; `AudioPickerActivity` copies any `content://` URI into the cache (`V/AudioPickerActivity.java:257-290`) | |
| Animations | `SlidingView` ViewPropertyAnimator → `AnimationListener.onAnimationEnd` → `onSlideExpansionChanged` (`V/SlidingView.java:193-216, 389-403`); `CoverView` Scroller driven from `onDraw` (`V/CoverView.java:309-353`); DSLV animators | Page changes of the panel arrive through `onAnimationEnd` (FRAMEWORK) |
| Absent | LiveData/ViewModel, RxJava, WorkManager, AlarmManager, data binding, Executors, Kotlin (grep of `SRC/java`) | |

## 5. Unreachable-code candidates (evidence only; no final verdicts)

All methods below were hit by **neither** baseline. The full per-area lists are in Appendix A.

### 5.1 DEAD candidates (no caller, or the caller cannot pass its guard)

| Candidate | Evidence |
|---|---|
| `ThemeHelper.usesDarkTheme` | private, no call site (grep of `SRC/java`); `V/ThemeHelper.java:80` |
| `SongTimeline.reshuffleTimeline` | private, no call site; `V/SongTimeline.java:547` |
| `MediaScanner$MediaScanPlan.addOptionalStep`, `addChainedStep` | no call sites; `ML/MediaScanner.java:793, 805` |
| `FancyMenu.add(int,int,int,CharSequence)` | every caller passes a string resource id; `V/ui/FancyMenu.java:109` |
| 34 `FancyMenuItem` methods: `MenuItem` interface stubs (`getActionProvider` … `setShowAsAction`), `setIcon(Drawable)`, `setTitle(int)`, `getGroupId` | items are only rendered by `FancyMenu$Adapter` and passed to `onFancyItemSelected`. `LibraryActivity.onFancyItemSelected`'s default branch → `super.onContextItemSelected(item)` → `getGroupId` is unreachable because every id added has a case and spacers are filtered (`V/ui/FancyMenu.java:175-182`; `V/LibraryActivity.java:741-849`). Interface stubs: `V/ui/FancyMenuItem.java:115-273` |
| `SlidingTabLayout.setCustomTabColorizer/setCustomTabView/setContentDescription(int,String)`, `SlidingTabStrip.setCustomTabColorizer` | no app callers (`TB/SlidingTabLayout.java:111, 144, 230`; `TB/SlidingTabStrip.java:76`) |
| `SlidingTabStrip.blendColors` | only when 2 neighbouring indicator colours differ (`TB/SlidingTabStrip.java:107-112`); `VanillaTabLayout` sets a single colour (`TB/VanillaTabLayout.java:42`) |
| Unused constructors: `VanillaTabLayout(Context)`, `SlidingTabLayout(Context)` and `(Context,AttributeSet)`, `SlidingView(Context)`, `FastScrollGuardedListView` 1/3/4-arg, `VanillaImageButton(Context)`, 3 short `DragSortController` constructors | XML inflation uses the 2-arg constructors, and `VanillaTabLayout` chains to the 3-arg super (`TB/VanillaTabLayout.java:33-44`; `V/FastScrollGuardedListView.java:47-58`; `V/SlidingView.java:110-117`). DSLV uses only the 6-arg controller constructor (`DS/DragSortListView.java:525-527`) |
| Implicit constructors of static helpers: `MediaLibrary`, `MediaSchema`, `MediaMigrations`, `MediaUtils`, `Playlist`, `PlayCountsHelper`, `SystemUtils`, `ThemeHelper`, `CoverBitmap`, `LibraryObserver$Value`; `BuildConfig.<init>/<clinit>` | never instantiated. `BuildConfig` constants are inlined at compile time, so the class is never loaded (INFERRED) |
| `LibraryObserver.onChange` (base no-op) | all 4 registered observers override it (§4) |
| Debug-only code: `MediaLibraryBackend.debugQuery`, `Mp4File.printDebugAtomPath`, `Common.debug` | guarded by `DEBUG=false` (`ML/MediaLibraryBackend.java:34, 306-307`) and `PRINT_DEBUG=false` (`BP/Mp4File.java:87, 176`); `Common.debug` has no caller (`BP/Common.java:75`, callers commented out). `PlaylistObserver.XT` runs, but its body is dead (`V/PlaylistObserver.java:52, 651-658`) |
| `SystemUtils.installShortcutLegacy` | API-gated: only if `SDK_INT < N_MR1` (25), but minSdk is 26 (`V/SystemUtils.java:63-67`) |
| DSLV cursor adapters `DragSortCursorAdapter` (19), `ResourceDragSortCursorAdapter` (7), `SimpleDragSortCursorAdapter` (15) | never instantiated or subclassed by the app (grep) |
| `DragSortListView$DragSortTracker` (5) | only when attr `track_drag_sort` is set (`DS/DragSortListView.java:457-461`); no layout sets it |
| DSLV API without callers | `setFloatAlpha`, `getFloatAlpha`, `setMaxScrollSpeed`, `printPosData`, `invalidateFloatView`, `setFloatViewManager`, `setDragSortListener`, `setDragScrollProfile`, `moveItem` → `getInputAdapter` → `AdapterWrapper.getAdapter`<br>`setDragListener`: only if the adapter implements `DragListener`; none does (`DS/DragSortListView.java:622-632`)<br>`removeItem(int)`: only from click-remove mode (`DS/DragSortController.java:452-456`); layouts use `flingRemove`<br>`DragSortController` getters/setters (`getDragInitMode`, `isSortEnabled`, `getRemoveMode`, `isRemoveEnabled`, `setDragHandleId`, `setFlingHandleId`, `setClickRemoveId`); `DragSortItemView.getGravity`<br>`moveCheckState`/`removeCheckState` have no callers (only Javadoc mentions), so their helpers `buildRunList`, `rotate`, `findFirstSetIndex`, `insertionIndexForKey` are dead too (`DS/DragSortListView.java:2624-2795`)<br>`LiftAnimator` (3 methods): its construction is commented out (`DS/DragSortListView.java:546`)<br>`SmoothAnimator` base `cancel/onStart/onUpdate/onStop`: `cancel()` has no caller, and all subclasses override the callbacks (`DS/DragSortListView.java:1160-1196, 1218-1316`)<br>`SimpleFloatViewManager.onDragFloatView/setSecondaryOnTouchListener`: the only instance is the `DragSortController` subclass, which overrides both without calling `super` (`DS/DragSortController.java:22, 284, 296`; `DS/SimpleFloatViewManager.java:72, 89`) |

Dead **branches** inside reachable methods (useful as notes):
- `LibraryActivity.onCreate` reads `state.getBoolean("launch_search")` from the saved-instance Bundle, but the flag is only ever put into an Intent (`V/FullPlaybackActivity.java:444`). Line `V/LibraryActivity.java:204` never ran in either run.
- `onFancyItemSelected` default branch (above).
- `ShowQueueFragment.onFancyItemSelected` default throw (`V/ShowQueueFragment.java:176-177`).
- `adjustSpines` toast (§2.2).
- `PermissionRequestActivity` TIRAMISU/R branches on API 27.
- `MediaLibrary.discoverDefaultMediaPaths` Q branch on API 27 (`ML/MediaLibrary.java:168-190`).

### 5.2 FRAMEWORK_ONLY candidates

| Candidate | Why |
|---|---|
| `PlaybackService.onBind` | nobody calls `bindService` (grep); returns null (`V/PlaybackService.java:1708-1711`) |
| `MediaAdapter.getItem`, `FileSystemAdapter.getItem`, `TabOrderAdapter.getItem`, `DragSortListView$AdapterWrapper.getItem/isEmpty` | plain ListView does not call `getItem` (FW-MEMORY); app code uses `getItemId`/`createData` |
| `DraggableRow.isChecked/toggle`, `DragSortItemViewCheckable.isChecked/toggle` | ListView choice mode calls `setChecked` (A+) but, as far as I recall, not `isChecked`/`toggle` (FW-MEMORY) |
| `CoverCache$CoverKey.toString` | no string conversion in app code |
| `FullPlaybackActivity.onSearchRequested` | `KEYCODE_SEARCH` is consumed in `onKeyDown` (`V/FullPlaybackActivity.java:442-446`), so the default path that calls `onSearchRequested` does not run (FW-MEMORY) |
| `MediaLibraryBackend.onUpgrade` → `MediaSchema.upgradeDatabaseSchema` → `MediaMigrations.migrate_to_20180416`; `CoverCache$BitmapDiskCache.onUpgrade`; `PlaylistObserver.onUpgrade` | only with an older-schema database, e.g. after upgrading from an older APK (`needs_state`) |
| `PlaybackService.onAccuracyChanged` | sensor accuracy change while shake is enabled (`onSensorChanged` itself ran in Monkey) |

### 5.3 Reachable only with an external entry point, a system event, hardware, accounts or the network

- External intents:
  - `AudioPickerActivity*` (VIEW audio), `AudioSearchActivity*` (MEDIA_PLAY_FROM_SEARCH).
  - `ShortcutPseudoActivity` (launcher shortcuts, widgets).
  - `MiniPlaybackActivity` (notification + pref).
- Widgets ×6 (`onEnabled/onDisabled/onUpdate/<init>`). The `checkEnabled`/`updateWidget` statics run from the service but return early when no widget is placed (`V/OneCellWidget.java:73-90`).
- System callbacks:
  - `MediaButtonReceiver.onReceive/<init>`, `MediaButtonReceiver$DelayedClickCounter` (double/triple press within 600 ms).
  - `MediaSessionTracker$1.onSkipToNext/onSkipToPrevious/onSeekTo`.
  - `PlaybackService$Receiver.onReceive` (headset unplug / screen on).
  - `onAudioFocusChange`, `VanillaMediaPlayer.setIsDucking` (transient focus loss "can duck").
  - Service teardown: `onDestroy`, `VanillaMediaPlayer.release`, `MediaSessionTracker.release`, `RemoteControlImplLp.unregisterRemote`.
  - `MediaScanner$1.onChange` (MediaStore change while running).
  - `ScheduledLibraryUpdate.*` (job).
  - `PermissionRequestActivity.*` (permission revoked).
- Hardware: accelerometer (shake); wired/Bluetooth headset for `isSpeakerOn` / `headset_only` (`V/PlaybackService.java:975-992`).
- Network: only the DNS lookup in `adjustSpines` and external browser/market intents. No accounts.

### 5.4 Fixture-, preference- or environment-gated

- **Formats:** `FlacFile`, `OggFile`, `OpusFile`, `Mp4File`, `Atom`, `RawFile` (MIDI/ADTS), `PageInfo`, `Common.parse_vorbis_comment/raf2le32/b2le16/xdie`, `LameHeader.getTags/parseV1Header` (MP3 without ID3) (`BP/Bastp.java:49-110`).
- **ReplayGain tags:** `BastpUtil.getFloatFromString` (`V/BastpUtil.java:72-110`).
- **Covers:** `CoverCache.storeCover`, `BitmapDiskCache.put/getSampleSize/isExpired/getUnixTime`. They need an image in the song's folder, a `Music/.vanilla/<artist>/<album>.jpg`, MediaStore album art or embedded art (`V/CoverCache.java:116-128, 406-509`).
- **Unplayable file:** `PlaybackService.getErrorMessage` and the IOException branch of `processSong` (`V/PlaybackService.java:1400-1413`).
- **Plugins:** `PluginUtils.getPluginMap`, `PlaybackActivity.showPluginMenu` + `$4` (`V/PluginUtils.java:65-96`).
- **Files tab:** `FileUtils.dispatchIntent` needs an image/text file (`V/FileUtils.java:185-227`).
- **M3U sync:** `PlaylistObserver.importM3uPlaylist/getHash/fromM3u/asM3u/getFileForName/updatePlaylistMetadata/deletePlaylistMetadata`, and `FileUtils.resolve/normalizeDirectorySeparators/relativize/traversePathUpwards`. They need pref `playlist_sync_mode`, `.m3u` files, and the relative-paths pref for export (`V/PlaylistObserver.java:300-405`).
- **Auto playlist:** `PlayCountsHelper.getTopSongs` needs pref `playcounts_autoplaylist`>0 plus `Math.random()>0.8` (`V/PlaybackService.java:1606-1618`).
- **Fast scroller:** `MediaAdapter$SectionIndex.toString` needs a long list.
- **Readahead:** `ReadaheadThread.*` and `triggerReadAhead` need pref `enable_readahead` (APE turned it on).

## 6. Decomposition into 4 modeling areas

**Rule.** A page belongs to the area that owns its window class (§3.4). An edge into a method is written by the area that owns the method, using the page names published by the page owner. The coordinator owns `S_ENTRY`/`S_EXIT` and merges the parts. Every one of the 247 in-scope compiled classes is assigned exactly once; JacocoInstrument (3 classes) is excluded.

| Area | Classes (inner classes included) | JaCoCo methods | Pages | Entry edges from other areas |
|---|---|---|---|---|
| **L — LIBRARY** (browse UI) | **vanilla:** `LibraryActivity`($1-$4), `LibraryPagerAdapter`($AdaperPositionLruCache), `MediaAdapter`($SectionIndex), `FileSystemAdapter`($1,$2,$Observer), `SortableAdapter`, `Limiter`, `DraggableRow`, `LazyCoverView`($BitmapLruCache,$CoverMsg), `FastScrollGuardedListView`, `ViewHolder`, `BottomBarControls`, `PlaylistActivity`, `PlaylistAdapter`, `PlaylistDialog`($1,$Data), `PlaylistInputDialog`, `TrackDetailsDialog`($1,$1$1), `SystemUtils`, `PluginUtils`, `FileUtils`<br>**vanilla.ui:** `ArrowedText`, `FancyMenu`($1,$Adapter,$Sheet), `FancyMenuItem`<br>**vanilla.ext:** `CoordClickListener`<br>**android.support.iosched.tabs:** `SlidingTabLayout`($InternalViewPagerListener,$TabClickListener), `SlidingTabStrip`($SimpleTabColorizer), `VanillaTabLayout`<br>**no-method types:** `LibraryAdapter`, `PlaylistDialog$Callback`, `PlaylistInputDialog$Callback`, `FancyMenu$Callback`, `CoordClickListener$Callback`, `SlidingTabLayout$TabColorizer`, synthetic `SlidingTabLayout$1`, `SlidingTabStrip$1` (47 + 8 classes) | 373 | 40: all `S_LIB_*` (19 + 8 ctx), `S_DLG_SORT`, `S_LIB_DLG_DELETE`, `S_DLG_PLAYLIST_PICK`, `S_DLG_PLAYLIST_NAME`, `S_DLG_TRACK_DETAILS`, `S_PLAYLIST*` (4), `S_LIB_PAUSED`, `S_PLAYLIST_PAUSED`, `S_SYS_PIN_SHORTCUT`, `S_EXT_VIEWER` | **ENTRY** launcher → `LibraryActivity` (`MAN:78-84`).<br>**P →** `PlaybackActivity.openLibrary` (`V/PlaybackActivity.java:625-654`); FullPlayback SEARCH key (`V/FullPlaybackActivity.java:442-446`); `performAction(Library)` (`V/PlaybackService.java:2247-2251`); `*_DELAYED` double tap (`:549-572`); notification content (`:2093-2096`); widget cover/title; `TimelineCallback` → `LibraryActivity.onSongChange/onStateChange/onMediaChange`; `recreate`; `PlaylistDialog`/`TrackDetailsDialog` shown from FullPlayback and the queue.<br>**S →** permission restart (`V/PermissionRequestActivity.java:79-83`); `TabOrderActivity` pref → `LibraryActivity.onStart` → `loadTabOrder`; library observer chain.<br>**D →** `PlaylistActivity.drop/remove` |
| **P — PLAYBACK** (service, now playing, queue, external control) | `PlaybackActivity`($1-$4), `SlidingPlaybackActivity`, `FullPlaybackActivity`($1,$2), `MiniPlaybackActivity`, `AudioPickerActivity`($AudioPickerWorker), `AudioSearchActivity`($AudioSearchWorker), `ShortcutPseudoActivity`, `ShowQueueFragment`($1), `ShowQueueAdapter`, `SlidingView`($AnimationListener,$GestureListener), `CoverView`($BitmapBucket,$CoverScroller), `CoverBitmap`, `CoverCache`($BitmapDiskCache,$CoverKey), `JumpToTimeDialog`($1), `VanillaImageButton`, `PlaybackService`($1,$Receiver), `SongTimeline`($FlagComparator,$IdComparator), `Song`, `QueryTask`, `PlaylistTask`, `Action`, `TimestampedObject`, `MediaUtils`, `VanillaMediaPlayer`, `ReadaheadThread`, `BastpUtil`($GainValues,$RGLruCache), `MediaSessionTracker`($1), `RemoteControl`, `RemoteControlImplLp`, `NotificationHelper`, `MediaButtonReceiver`($DelayedClickCounter), `OneCellWidget`, `FourLongWidget`, `FourSquareWidget`, `FourWhiteWidget`, `WidgetD`, `WidgetE`, `ThemeHelper`, `SharedPrefHelper`, `PrefDefaults`, `BuildConfig`<br>**no-method types:** `TimelineCallback`, `CoverView$Callback`, `SlidingView$Callback`, `SongTimeline$Callback`, `JumpToTimeDialog$OnPositionSubmitListener`, `RemoteControl$Client`, `PrefKeys`, synthetic `PlaybackService$2`, `FullPlaybackActivity$3` (switch maps), `AudioPickerActivity$1`, `AudioSearchActivity$1` (65 + 11 classes) | 510 | 25: `S_FULL*` (11), `S_CTX_SHUFFLE`, `S_CTX_REPEAT`, `S_QUEUE_CTX`, `S_DLG_JUMP_TO_TIME`, `S_DLG_PLUGINS`, `S_MINI`, `S_AUDIO_PICKER_*` (2), `S_FULL_PAUSED`, `S_HOME_WIDGET`, `S_LAUNCHER_SHORTCUTS`, `S_NOTIFICATION_SHADE`, `S_EXT_SHARE`, `S_EXT_PLUGIN` | **ENTRY:** VIEW/search intents, exported service actions, MEDIA_BUTTON, widgets, shortcuts, notification, media session.<br>**L →** `openPlaybackActivity` (`V/LibraryActivity.java:451-456`); `pickSongs` → `addSongs` (`:383-425`); control buttons, menus and queue panel inside the Library window (`PlaybackActivity.onClick`, `SlidingPlaybackActivity.onOptionsItemSelected`, `ShowQueueFragment.*`); `PlaylistActivity.performAction` → `addSongs` (`V/PlaylistActivity.java:256-284`); `MSG_SAVE_PAGE` → `adjustSpines`.<br>**S →** SharedPreferences → `PlaybackService.loadPreference`; `MediaLibrary` observers → `PlaybackService.mObserver`; `EqualizerFragment` → `getAudioSession` (`V/PreferencesActivity.java:153-157`).<br>**D →** `ShowQueueFragment.drop/remove` |
| **S — SETTINGS_DATA** (preferences, folder pickers, permission, job, media DB and tag parsing) | `PreferencesActivity` and all inner fragments ($AboutFragment, $AudioFragment, $CoverArtFragment, $EqualizerFragment, $HeadsetLaunchFragment($1,$2), $HelpFragment, $LibraryFragment, $MiscFragment, $NotificationsFragment, $PlaybackFragment, $PlaylistFragment, $ReplayGainFragment($1), $ShakeFragment); `PreferencesMediaLibrary`($1,$1$1,$2-$5), `PreferencesTheme`, `SeekBarPreference`, `IdlePreference`, `ListPreferenceSummary`, `TabOrderActivity`, `TabOrderAdapter`, `FolderPickerActivity`($1,$2,$3,$FolderState), `FolderPickerAdapter`($Item), `MediaFoldersSelectionActivity`, `FilebrowserStartActivity`, `PlaylistObserverDirActivity`, `PermissionRequestActivity`($1), `ScheduledLibraryUpdate`($1), `PlaylistObserver`($1,$2,$Database), `Playlist`, `PlayCountsHelper`<br>**medialibrary:** `LibraryObserver`($Type,$Value), `MediaLibrary`($Preferences,$ScanProgress), `MediaLibraryBackend`, `MediaMetadataExtractor`, `MediaMigrations`, `MediaScanner`($1,$MediaScanPlan,$MediaScanPlan$Statistics,$MediaScanPlan$Step), `MediaSchema`<br>**bastp:** `Atom`, `Bastp`, `Common`, `FlacFile`, `ID3v2File`($TagItem), `LameHeader`, `Mp4File`, `OggFile`, `OpusFile`, `PageInfo`, `RawFile`<br>**no-method types:** `MediaLibrary$AlbumColumns`, `$ContributorColumns`, `$ContributorSongColumns`, `$GenreColumns`, `$GenreSongColumns`, `$PlaylistColumns`, `$PlaylistSongColumns`, `$PreferenceColumns`, `$SongColumns`, synthetic `FolderPickerActivity$4`, `PageInfo$PageParser` (77 + 11 classes) | 370 | 30: `S_PREFS*` (16), `S_DLG_LISTPREF`, `S_DLG_SEEKBARPREF`, `S_DLG_IDLEPREF`, `S_DLG_MEDIALIB_CONFIRM`, `S_DLG_HEADSET_LAUNCH`, `S_TAB_ORDER`, `S_FOLDER_PICKER`, `S_MEDIA_FOLDERS`, `S_DLG_FOLDER_STATE`, `S_PREFS_PAUSED`, `S_SYS_PERMISSION_DIALOG`, `S_EXT_BROWSER`, `S_EXT_EQUALIZER`, `S_EXT_MARKET` | **ENTRY:** JobScheduler → `ScheduledLibraryUpdate`; MediaStore change → `MediaScanner$1`.<br>**P/L →** menu Settings (`V/PlaybackActivity.java:411-413`); permission banner/requests (`V/LibraryActivity.java:187-189`, `V/AudioPickerActivity.java:80`, `V/AudioSearchActivity.java:47`); `PlaybackService.onCreate` → `scheduleUpdate`, `new PlaylistObserver`, `MediaLibrary.registerLibraryObserver` (`V/PlaybackService.java:503, 513, 532`); every `QueryTask.runQuery` → `MediaLibrary.queryLibrary` (`V/QueryTask.java:70-73`); `Playlist.*` from Library, FullPlayback, PlaylistDialog and the worker; `MediaMetadataExtractor` from FullPlayback, TrackDetails and `MediaUtils`; `PlayCountsHelper.countSong` from the service.<br>**D →** `TabOrderActivity.drop` |
| **D — DSLV** (bundled drag-sort ListView, modified to chain a secondary touch listener) | `DragSortController`($1), `DragSortCursorAdapter`, `DragSortItemView`, `DragSortItemViewCheckable`, `DragSortListView`($1,$2,$AdapterWrapper,$AdapterWrapper$1,$DragScroller,$DragSortTracker,$DropAnimator,$HeightCache,$LiftAnimator,$RemoveAnimator,$SmoothAnimator), `ResourceDragSortCursorAdapter`, `SimpleDragSortCursorAdapter`, `SimpleFloatViewManager`<br>**no-method types:** `DragSortListView$DragListener`, `$DragScrollProfile`, `$DragSortListener`, `$DropListener`, `$FloatViewManager`, `$RemoveListener`, `SimpleDragSortCursorAdapter$CursorToStringConverter`, `$ViewBinder` (20 + 8 classes) | 215 | none. Provides gesture semantics on `S_LIB_QUEUE`, `S_LIB_WIDE`, `S_FULL_QUEUE`, `S_PLAYLIST_EDIT`, `S_TAB_ORDER`, `S_FOLDER_PICKER`, `S_MEDIA_FOLDERS` | Inflated from `RES/layout/showqueue_listview.xml`, `playlist_activity.xml`, `tab_order.xml`, `folderpicker_content.xml`.<br>App calls: `setAdapter`, `setDropListener`, `setRemoveListener`, `setDragEnabled` (`V/PlaylistActivity.java:166-174`), `setOnTouchListener` (chained through `DS/DragSortListView.java:580-584`), `setOnItemClickListener`.<br>Outgoing callbacks: `DropListener.drop`, `RemoveListener.remove` |

- **Shared infrastructure owners:**
  - **P** owns the base classes `PlaybackActivity`/`SlidingPlaybackActivity` (superclasses of Library, Full, Mini, AudioPicker, AudioSearch), the singleton `PlaybackService` (`sInstance`, `get()` blocks until `onCreate`, `V/PlaybackService.java:1956-1975`), the queue (`SongTimeline`), and the core helpers `Song`, `QueryTask`, `MediaUtils`, `ThemeHelper`, `SharedPrefHelper`, `PrefDefaults`/`PrefKeys`, `Action`.
  - **S** owns the database layer (`ML/*`, `Playlist`, `PlayCountsHelper`, `PlaylistObserver`) and tag parsing (`BP/*`, `MediaMetadataExtractor`).
  - **L** owns the reusable UI widgets that other areas also use: `FancyMenu`/`FancyMenuItem`, `CoordClickListener`, `DraggableRow`, `LazyCoverView`, `ViewHolder`, and the playlist/details dialogs.
- **Methods split across areas by inheritance.** `LibraryActivity` overrides `onCreateOptionsMenu/onOptionsItemSelected/handleMessage/onClick/onKeyUp`, and the overridden super chain is in P. L writes the edges for its overrides and the CALL edges to `super.*`; P writes the rest.
- **Leftovers:**
  - 3 JacocoInstrument classes (excluded).
  - R classes and library code: not in the class directory.
  - Nothing else is unassigned (47+65+77+20 = 209 classes with JaCoCo methods + 38 no-method types = 247).
  - (JaCoCo lists 211 classes with methods; the 2 extra are `JacocoInstrumentation` and `SMSInstrumentedReceiver`. The per-area method totals 373+510+370+215 = 1468 are exact.)
- **Size balance.** P is the largest, but `PlaybackService` and `SongTimeline` are mostly straight-line CALL chains.
- **Option.** Move the external-control cluster (`AudioPicker*`, `AudioSearch*`, `ShortcutPseudoActivity`, widgets, `MediaButtonReceiver`, `MediaSessionTracker`; about 75 methods) from P to D to balance the work. I recommend keeping it in P because those classes only call `PlaybackService`.

## 7. Baseline coverage by area and screen

### 7.1 Method hits per area (JaCoCo METHOD counter, JacocoInstrument excluded)

| Area | Methods | Both | Monkey only | APE only | Neither | Monkey hit | APE hit | Either |
|---|---|---|---|---|---|---|---|---|
| L LIBRARY | 373 | 241 | 0 | 67 | 65 | 241 | 308 | 308 |
| P PLAYBACK | 510 | 374 | 4 | 38 | 94 | 378 | 412 | 416 |
| S SETTINGS_DATA | 370 | 172 | 5 | 91 | 102 | 177 | 263 | 268 |
| D DSLV | 215 | 71 | 35 | 3 | 106 | 106 | 74 | 109 |
| **Total** | **1468** | **858** | **44** | **199** | **367** | **902** | **1057** | **1101** |

The totals match the brief. Monkey-only methods are almost all drag-and-drop (35 DSLV drag/drop/scroll methods plus `ShowQueueFragment.drop`, `SlidingView$GestureListener.onFling`), media keys (`MediaSessionTracker$1.onPlay/onStop`), the idle-timeout dialog (4 `IdlePreference` methods) and `ScheduledLibraryUpdate.jobsEqual`.

### 7.2 Monkey-missed methods (566) by rough reachability class

This is my heuristic classification from source reading (rules in Appendix A). It is not a verdict.

| Area | Monkey-missed | DEAD cand. | FRAMEWORK_ONLY cand. | External entry / system event | Fixture / pref / env | UI-reachable | …of which APE hit |
|---|---|---|---|---|---|---|---|
| L | 132 | 48 | 4 | 0 | 7 | 73 | 67 |
| P | 132 | 9 | 5 | 60 | 15 | 43 | 33 (+5 pref-gated) |
| S | 193 | 12 | 5 | 15 | 42 | 119 | 86 (+5 pref-gated) |
| D | 109 | 85 | 4 | 0 | 0 | 20 | 3 |
| **Total** | **566** | **154** | **18** | **75** | **64** | **255** | **189 (+10)** |

So roughly 255 Monkey-missed methods are reachable through the app UI alone, and about another 139 are reachable after harness setup or an external trigger.

### 7.3 Screens per area: reached or not, and why

| Area | Never reached by either | Reached only by APE (Monkey gap) | Reason |
|---|---|---|---|
| L | `S_LIB_ALBUMARTISTS`, `S_LIB_COMPOSERS` (`V/LibraryPagerAdapter.java:301-309` never ran)<br>`S_LIB_NO_PERMISSION`<br>`S_EXT_VIEWER` (`FileUtils.dispatchIntent`)<br>`S_LIB_MENU_QUEUE` items Dequeue/Empty/Save (`PlaybackService.clearQueue/emptyQueue`, `PlaylistDialog.newInstance(3-arg)`)<br>"Go home" (`V/LibraryActivity.java:884-886`)<br>Files sort by size/time/ext (`V/FileSystemAdapter.java:136-145`)<br>`PlaylistActivity` drop/remove in edit mode<br>Rename-playlist confirm (`LibraryActivity$2.onSuccess`) | all `S_LIB_CTX_*` (`LibraryActivity.onCreateFancyMenu` A+, every branch except Plugins: `:679-726`); `S_DLG_PLAYLIST_PICK`, `S_DLG_PLAYLIST_NAME`, `S_DLG_TRACK_DETAILS`, `S_LIB_DLG_DELETE`, `S_SYS_PIN_SHORTCUT`, `S_PLAYLIST_CTX`, `S_PLAYLIST_DLG_DELETE`, `S_LIB_WIDE` | Tab order never changed; permission pre-granted; no image/text files pushed; deep, mode-gated menu items; precise drag gestures; long-press (Monkey) |
| P | `S_MINI`, `S_AUDIO_PICKER_*`, `S_HOME_WIDGET`, `S_LAUNCHER_SHORTCUTS`, `S_DLG_PLUGINS`, `S_EXT_PLUGIN`, `S_FULL_NO_MEDIA` (`V/FullPlaybackActivity.java:231` never ran)<br>`S_FULL_COVERINFO` with display mode 0 (`CoverBitmap.createOverlappingBitmap`)<br>ToggleControls and SeekForward/Backward/NextAlbum/PreviousAlbum/Shuffle/PlayPause/Library/ClearQueue actions (`V/PlaybackService.java:2248-2325` mostly unexecuted)<br>Back-hides-queue in Full (`:464-465`) | `S_FULL_EMPTY_QUEUE`, `S_FULL_SUBMENU_ENQUEUE`, `S_CTX_SHUFFLE`, `S_CTX_REPEAT`, `S_QUEUE_CTX`, `S_EXT_SHARE`, `S_DLG_JUMP_TO_TIME` OK button, display mode 1 (`createSeparatedBitmap`), cover long-press | External entry points and outside-package UI; no plugin installed; library never empty; preferences for actions never set to those values; long-press; possibly a restored non-empty queue in the Monkey run (INFERRED, §2.4) |
| S | `S_MEDIA_FOLDERS`, `S_DLG_FOLDER_STATE`, `S_SYS_PERMISSION_DIALOG`<br>Dump database (`MediaLibrary.createDebugDump`); Cancel scan; full scan / drop DB<br>Seek-bar drags in preference dialogs (`SeekBarPreference/IdlePreference.onStart/StopTrackingTouch`)<br>Job run; M3U import | `S_TAB_ORDER`, `S_FOLDER_PICKER@FILEBROWSER_START`, `@PLAYLIST_DIR`, `S_PREFS_LIBRARY`, `S_PREFS_NOTIFICATIONS`, `S_PREFS_MEDIALIB_SCANNING`, `S_PREFS_MEDIALIB_MENU` (Force M3U only), `S_DLG_MEDIALIB_CONFIRM@EDIT`, `S_DLG_HEADSET_LAUNCH`, `S_EXT_MARKET` | Confirm dialogs answered "Cancel"; checkbox+Start combinations never chosen; drag gestures; job constraints; no M3U fixture |
| D | `DragSortListView` remove/fling animations (`RemoveAnimator`, `doRemoveItem`, `removeItem(int,float)`, `stopDragWithVelocity`), `DragScroller.run/startScrolling` (auto-scroll while dragging near an edge), `adjustScroll`, `adjustItem`, `drawDivider`, `cancelDrag` (data change or cancel during a drag). (`LiftAnimator` and the check-state helpers are DEAD, §5.1) | `DragSortController.onLongPress/onShowPress` | Fling-to-remove and long drags were never completed by either tool. APE never completed a drag-and-drop (all 35 drop/drag methods are Monkey-only) |

## Conclusions and recommendations

1. **Page modeling.** Use the 97-page list in §3.4.
   - Most of the behaviour is mode-driven, not window-driven. The keys are LibraryActivity's tab, limiter, search and slide stage; FullPlayback's display mode, controls, overlay and queue; and Playlist edit mode.
   - Model the `SlidingView` stage change as a FRAMEWORK edge `SlidingView$AnimationListener.onAnimationEnd` → `onSlideExpansionChanged` and an ENTERS edge to `S_LIB_QUEUE`/`S_FULL_QUEUE`. Do not use the menu rebuild as a page change.
2. **Method set.** Use JaCoCo's 1468 methods as the node set so that verdicts can be compared with the baseline. If `javap` becomes available, record the 19 extra bytecode methods (enum `values/valueOf`, trivial constructors, switch-map `<clinit>`) as excluded rather than as targets.
3. **Long-press is the main Monkey blind spot.** For the study, the 199 APE-only methods are proven reachable (APE ran them) but were missed by Monkey. Most hang off long-press → bottom sheet → dialog → worker message, which is a deep but deterministic chain and so a good tool target.
4. **Harness changes** (§2.5) would move many fixture/environment-gated methods from "unreachable in practice" to REACHABLE_AFTER_SETUP:
   - Clear data per run; re-push fixtures because deletes are destructive.
   - Push 1 image + 1 text file, 1 cover image in Music, 1 FLAC/OGG/OPUS/M4A each, 1 corrupt file, 1 `.m3u`.
   - Install a dummy plugin APK.
5. **Record environment conditions as `guard`/`needs_state`:** `playlist_sync_mode`, `enable_shake`, `use_idle_timeout`, `enable_readahead`, `notification_action`, `display_mode`, tab order, plugins installed, service running (Enqueue in AudioPicker), queue non-empty, library non-empty.
6. **Open questions:**
   - Single-pane PreferenceActivity behaviour (new activity per header; the blank screen left after Equalizer/HeadsetLaunch) is FW-MEMORY/UNVERIFIED.
   - Whether Up does anything in PreferencesActivity is UNVERIFIED.
   - Whether Monkey started with stale app data is UNVERIFIED (needs logs).
   - Which exact control produced each Monkey/APE line hit (notification vs widget) is INFERRED.
   - FW-MEMORY claims about ListView `getItem`/`isChecked`, fast-scroller thresholds and Monkey's lack of long-press should be checked against AOSP 8.1 sources if available.

## Appendix A. Monkey-missed methods by area and category

Rules:
- DEAD = explicit list from §5.1, and only if APE also missed the method.
- FRAMEWORK_ONLY = §5.2.
- EXTERNAL = §5.3.
- FIXTURE/PREF/ENV = §5.4.
- Everything else = UI-reachable.
- `[A]` marks methods APE hit.
- Duplicate names are overloads.
- DSLV: `removeItem` appears once as DEAD (the 1-arg overload) and once as UI-reachable (the 2-arg fling path).

**L LIBRARY (132 Monkey-missed)**
- *DEAD candidates* (48): `FancyMenu.add` (CharSequence overload), `FancyMenuItem.collapseActionView`, `expandActionView`, `getActionProvider`, `getActionView`, `getAlphabeticShortcut`, `getGroupId`, `getMenuInfo`, `getNumericShortcut`, `getOrder`, `getSubMenu`, `getTitleCondensed`, `hasSubMenu`, `isActionViewExpanded`, `isCheckable`, `isChecked`, `isEnabled`, `isVisible`, `setActionProvider`, `setActionView` ×2, `setAlphabeticShortcut`, `setCheckable`, `setChecked`, `setEnabled`, `setIcon` (Drawable), `setNumericShortcut`, `setOnActionExpandListener`, `setOnMenuItemClickListener`, `setShortcut`, `setShowAsAction`, `setShowAsActionFlags`, `setTitle` (int), `setTitleCondensed`, `setVisible`; `FastScrollGuardedListView.<init>` ×3; `SlidingTabLayout.<init>` ×2, `SlidingTabLayout.setContentDescription`, `setCustomTabColorizer`, `setCustomTabView`; `SlidingTabStrip.blendColors`, `SlidingTabStrip.setCustomTabColorizer`; `SystemUtils.<init>`, `SystemUtils.installShortcutLegacy`; `VanillaTabLayout.<init>` (1-arg)
- *FRAMEWORK_ONLY candidates* (4): `DraggableRow.isChecked`, `DraggableRow.toggle`, `FileSystemAdapter.getItem`, `MediaAdapter.getItem`
- *Fixture / pref / env* (7): `FileUtils.dispatchIntent`, `FileUtils.normalizeDirectorySeparators`, `FileUtils.relativize`, `FileUtils.resolve`, `FileUtils.traversePathUpwards`, `MediaAdapter$SectionIndex.toString`, `PluginUtils.getPluginMap`
- *UI-reachable* (73):
  - Long-press menus: `CoordClickListener.onItemLongClick` [A]; `FancyMenu.<init>`, `add` (int), `addInternal`, `addSpacer`, `assembleAdapter`, `setHeaderTitle`, `show` [A]; `FancyMenu$1.<init>`, `onItemClick` [A]; `FancyMenu$Adapter.<init>`, `getView` [A]; `FancyMenu$Sheet.<init>` [A]; `FancyMenuItem.<init>`, `getIcon`, `getIntent`, `getItemId`, `getTitle`, `isSpacer`, `setIcon` (int), `setIntent`, `setIsSpacer`, `setTitle` (CharSequence) [A]; `FileSystemAdapter.onCreateFancyMenu` [A]; `LibraryActivity.onCreateFancyMenu`, `onFancyItemSelected` [A]; `LibraryPagerAdapter.onItemLongClickWithCoords` [A]
  - Rename and delete dialogs: `LibraryActivity$2.<init>` [A], `LibraryActivity$2.onSuccess`; `LibraryActivity$3.<init>`, `onClick` [A]; `LibraryActivity$4.<init>`, `onClick` [A]
  - Tabs and rows: `DraggableRow.setChecked` [A]; `FileUtils.getFileExtension`; `LibraryPagerAdapter.getItemPosition` [A]
  - Playlist editor: `PlaylistActivity.drop`, `remove`; `PlaylistActivity.onClick` (dialog), `onFancyItemSelected`, `onItemLongClickWithCoords`, `onOptionsItemSelected` [A]; `PlaylistAdapter.moveItem`; `PlaylistAdapter.removeItem` [A]
  - Playlist dialogs: `PlaylistDialog.<init>`, `newInstance` (4-arg), `onClick`, `onCreateDialog` [A]; `PlaylistDialog.newInstance` (3-arg, "Save as playlist"); `PlaylistDialog$1.<init>`, `onSuccess` [A]; `PlaylistDialog$Data.<init>` [A]; `PlaylistInputDialog.<init>`, `newInstance`, `onCreateDialog`, `onStart`, `afterTextChanged`, `beforeTextChanged`, `onTextChanged`, `onClick` [A]
  - Shortcuts: `SystemUtils.installLauncherShortcut`, `installShortcut` [A]
  - Track details: `TrackDetailsDialog.<clinit>`, `<init>`, `newInstance`, `show`, `onCreate`, `onCreateView`, `onDestroy` [A]; `TrackDetailsDialog$1.<init>`, `run` [A]; `TrackDetailsDialog$1$1.<init>`, `run` [A]

**P PLAYBACK (132 Monkey-missed)**
- *DEAD candidates* (9): `BuildConfig.<clinit>`, `BuildConfig.<init>`, `CoverBitmap.<init>`, `MediaUtils.<init>`, `SlidingView.<init>` (1-arg), `SongTimeline.reshuffleTimeline`, `ThemeHelper.<init>`, `ThemeHelper.usesDarkTheme`, `VanillaImageButton.<init>` (1-arg)
- *FRAMEWORK_ONLY candidates* (5): `CoverCache$BitmapDiskCache.onUpgrade`, `CoverCache$CoverKey.toString`, `FullPlaybackActivity.onSearchRequested`, `PlaybackService.onAccuracyChanged`, `PlaybackService.onBind`
- *External entry / system event* (60):
  - Audio intents: `AudioPickerActivity.<init>`, `onCreate`, `onClick`, `onSongResolved`; `AudioPickerActivity$AudioPickerWorker.<init>`, `doInBackground`, `onPostExecute`, `getSongForUri`, `getCursorForMediaContent`, `getCursorForAnyContent`; `AudioSearchActivity.<init>`, `onCreate`, `onSearchCompleted`; `AudioSearchActivity$AudioSearchWorker.<init>`, `doInBackground`, `onPostExecute`
  - Widgets: `OneCellWidget`, `FourLongWidget`, `FourSquareWidget`, `FourWhiteWidget`, `WidgetD`, `WidgetE` × {`<init>`, `onEnabled`, `onDisabled`, `onUpdate`} (24)
  - Media buttons and session: `MediaButtonReceiver.<init>`, `onReceive`; `MediaButtonReceiver$DelayedClickCounter.<init>`, `run`; `MediaSessionTracker$1.onSkipToNext`, `onSkipToPrevious`, `onSeekTo`; `MediaSessionTracker.release`
  - Notification and shortcuts: `MiniPlaybackActivity.<init>`, `onCreate`, `onClick`; `ShortcutPseudoActivity.<init>`, `getIntent`, `onCreate`
  - Service and audio system: `PlaybackService$Receiver.onReceive`; `PlaybackService.onAudioFocusChange`, `onDestroy`; `RemoteControlImplLp.unregisterRemote`; `VanillaMediaPlayer.release`, `setIsDucking`
- *Fixture / pref / env* (15): `BastpUtil.getFloatFromString`; `CoverCache.storeCover`; `CoverCache$BitmapDiskCache.put`, `getSampleSize`, `isExpired`, `getUnixTime`; `PlaybackActivity.showPluginMenu`, `PlaybackActivity$4.<init>`, `onClick`; `PlaybackService.getErrorMessage`; `PlaybackService.onError` [A]; `PlaybackService.triggerReadAhead` [A]; `ReadaheadThread.handleMessage`, `pause`, `setSong` [A]
- *UI-reachable* (43):
  - Covers and cover view: `CoverBitmap.createOverlappingBitmap`; `CoverBitmap.createSeparatedBitmap`, `drawText`, `loadTextSizes` [A]; `CoverView$BitmapBucket.abortScroll`; `CoverView$CoverScroller.abortAnimation`
  - Now playing: `FullPlaybackActivity$2.onClick` [A]; `FullPlaybackActivity.hideMessageOverlay`, `showOverlayMessage`, `loadExtraInfo`, `onLongClick` [A]; `JumpToTimeDialog.onClick`, `parseInteger` [A]
  - Media utilities: `MediaUtils.addFileToCursor`, `queryGenreForSong`, `shareMedia` [A]; `MediaUtils.deleteFile`
  - Context menus, delete and playlists: `PlaybackActivity.delete`, `onContextItemSelected`, `onCreateContextMenu`, `removeFromPlaylist` [A]
  - Queue operations: `PlaybackService.clearQueue`, `emptyQueue`, `showToast(int,int)`; `PlaybackService.deleteMedia`, `enqueueFromSong`, `getQueuePositionForSongId`, `moveSongPosition`, `removeSongPosition` [A]; `ShowQueueFragment.onFancyItemSelected`, `onItemLongClickWithCoords`, `remove` [A]
  - Panel and dialog callbacks: `SlidingPlaybackActivity.onPositionSubmit`, `updatePlaylistFromPlaylistDialog` [A]; `SlidingView.isFullyExpanded`
  - Timeline: `Song.getTrackAndDiscNumber`, `isRandom` [A]; `SongTimeline.clearQueue`, `emptyQueue`; `SongTimeline.getQueuePositionForSongId`, `moveSongPosition`, `removeSong`, `removeSongPosition` [A]

**S SETTINGS_DATA (193 Monkey-missed)**
- *DEAD candidates* (12): `Common.debug`, `LibraryObserver$Value.<init>`, `LibraryObserver.onChange`, `MediaLibrary.<init>`, `MediaLibraryBackend.debugQuery`, `MediaMigrations.<init>`, `MediaScanner$MediaScanPlan.addChainedStep`, `MediaScanner$MediaScanPlan.addOptionalStep`, `MediaSchema.<init>`, `Mp4File.printDebugAtomPath`, `PlayCountsHelper.<init>`, `Playlist.<init>`
- *FRAMEWORK_ONLY candidates* (5): `MediaLibraryBackend.onUpgrade`, `MediaMigrations.migrate_to_20180416`, `MediaSchema.upgradeDatabaseSchema`, `PlaylistObserver.onUpgrade`, `TabOrderAdapter.getItem`
- *External entry / system event* (15): `MediaScanner$1.onChange`; `PermissionRequestActivity.<init>`, `onCreate`, `onRequestPermissionsResult`, `requestPermissions`, `showWarning`, `getOptionalPermissions`; `PermissionRequestActivity$1.<init>`, `onClick`; `ScheduledLibraryUpdate.<init>`, `onStartJob`, `onStopJob`, `finalizeScan`; `ScheduledLibraryUpdate$1.<init>`, `onChange`
- *Fixture / pref / env* (42):
  - Tag parsers: `Atom.<init>`; `Common.b2le16`, `parse_vorbis_comment`, `raf2le32`, `xdie`; `FlacFile.<init>`, `getTags`, `parse_stream_page`, `parse_streaminfo_block`; `LameHeader.getTags`, `parseV1Header`; `Mp4File.<clinit>`, `<init>`, `getTags`, `readIntoBuffer`; `OggFile.<init>`, `getTags`, `parse_ogg_vorbis_comment`, `parse_ogg_vorbis_identification`, `parse_stream_page`; `OpusFile.<clinit>`, `<init>`, `calculate_gain`, `getTags`, `parse_opus_head`, `parse_opus_vorbis_comment`; `PageInfo.<init>`; `RawFile.<init>`, `getTags`
  - Auto playlist: `PlayCountsHelper.getTopSongs`
  - M3U sync: `PlaylistObserver$2.onEvent` [A]; `PlaylistObserver.dumpAllAsM3uPlaylist`, `dumpAsM3uPlaylist`, `forceM3uImport`, `isM3uFilename` [A]; `PlaylistObserver.asM3u`, `deletePlaylistMetadata`, `fromM3u`, `getFileForName`, `getHash`, `importM3uPlaylist`, `updatePlaylistMetadata`
- *UI-reachable* (119):
  - Folder pickers: `FilebrowserStartActivity.<init>`, `onCreate`, `onFolderPicked` [A]; `FolderPickerActivity.<init>`, `onCreate`, `onCreateOptionsMenu`, `onOptionsItemSelected`, `onItemClick`, `setCurrentDir`, `enableTritasticSelect`, `enableTritasticSpinner` [A]; `FolderPickerActivity$1.<init>`, `onClick` [A]; `FolderPickerActivity$2.<init>`, `afterTextChanged`, `beforeTextChanged`, `onTextChanged` [A]; `FolderPickerActivity.onItemLongClick`, `onItemSelected`, `onNothingSelected`, `setFolderState`; `FolderPickerActivity$3.<init>`, `onClick`; `FolderPickerActivity$FolderState.<clinit>`; `FolderPickerAdapter.<init>`, `getView`, `getCurrentDir`, `setCurrentDir`, `getIncludedDirs`, `getExcludedDirs`, `refresh` [A]; `FolderPickerAdapter$Item.<init>` [A]; `FolderPickerAdapter.setIncludedDirs`, `setExcludedDirs`, `verifyDirs`; `MediaFoldersSelectionActivity.<init>`, `onCreate`, `onFolderPicked`; `PlaylistObserverDirActivity.<init>`, `onCreate`, `onFolderPicked` [A]
  - Preference dialogs: `IdlePreference.onStartTrackingTouch`, `onStopTrackingTouch`; `SeekBarPreference.onStartTrackingTouch`, `onStopTrackingTouch`; `SeekBarPreference.saveCheckBoxPreference` [A]
  - Media library and database: `MediaLibrary$Preferences.<init>` [A]; `MediaLibrary.discoverDefaultBlacklistedPaths`, `discoverDefaultMediaPaths`, `removeFromPlaylist`, `removePlaylist`, `removeSong`, `startLibraryScan` [A]; `MediaLibrary.abortLibraryScan`, `createDebugDump`, `movePlaylistItem`, `renamePlaylist`; `MediaLibraryBackend.onCreate`, `delete`, `update`, `cleanOrphanedEntries` [A]; `MediaLibraryBackend.setPendingDeletion`; `MediaMetadataExtractor.<init>` (1-arg), `addFiltered`, `decodeMimeType`, `getFormat`, `populateSelf` [A]; `MediaScanner.startNormalScan`, `rpcLibraryVerify`, `isUnset` [A]; `MediaScanner.startFullScan`, `abortScan`, `flushDatabase`, `rpcReadDirectory`; `MediaScanner$MediaScanPlan.clear`; `MediaSchema.createDatabaseSchema` [A]; `Playlist.addToPlaylist`, `deletePlaylist`, `getPlaylist`, `queryPlaylists`, `removeFromPlaylist` [A]; `Playlist.renamePlaylist`; `PlaylistObserver.onCreate` [A]
  - Preference screens: `PreferencesActivity$HeadsetLaunchFragment$1.onClick`, `$2.onClick` [A]; `PreferencesActivity$LibraryFragment.<init>`, `onCreate` [A]; `PreferencesActivity$NotificationsFragment.<init>`, `onCreate` [A]; `PreferencesMediaLibrary.startButtonPressed`, `editButtonPressed`, `onOptionsItemSelected` [A]; `PreferencesMediaLibrary.cancelButtonPressed`, `startMediaFoldersSelection`; `PreferencesMediaLibrary$1.onChange`, `$1$1.<init>`, `$1$1.run`, `$2.onClick`, `$4.<init>`, `$4.onClick`, `$5.<init>` [A]; `PreferencesMediaLibrary$3.onClick`, `$5.onClick`
  - Tab order: `TabOrderActivity.<init>`, `onCreate`, `onOptionsItemSelected`, `onClick`, `restoreDefault`, `save`, `load`, `onItemClick` [A]; `TabOrderActivity.drop`; `TabOrderAdapter.<init>`, `setTabIds`, `getTabIds`, `getCount`, `getItemId`, `getView`, `hasStableIds` [A]

**D DSLV (109 Monkey-missed)**
- *DEAD candidates* (85):
  - `DragSortController.<init>` ×3 (short); `DragSortController.getDragInitMode`, `getRemoveMode`, `isRemoveEnabled`, `isSortEnabled`, `setClickRemoveId`, `setDragHandleId`, `setFlingHandleId`
  - `DragSortCursorAdapter` (all 19), `ResourceDragSortCursorAdapter` (all 7), `SimpleDragSortCursorAdapter` (all 15)
  - `DragSortItemView.getGravity`; `DragSortListView$AdapterWrapper.getAdapter`; `DragSortListView$DragSortTracker` (all 5)
  - `DragSortListView.getFloatAlpha`, `setFloatAlpha`, `getInputAdapter`, `invalidateFloatView`, `moveItem`, `printPosData`, `removeItem(int)`, `setDragListener`, `setDragScrollProfile`, `setDragSortListener`, `setFloatViewManager`, `setMaxScrollSpeed`
  - `DragSortListView.moveCheckState`, `removeCheckState`, `buildRunList`, `rotate`, `findFirstSetIndex`, `insertionIndexForKey`
  - `DragSortListView$LiftAnimator.<init>`, `onStart`, `onUpdate`; `DragSortListView$SmoothAnimator.cancel`, `onStart`, `onUpdate`, `onStop`
  - `SimpleFloatViewManager.onDragFloatView`, `setSecondaryOnTouchListener`
- *FRAMEWORK_ONLY candidates* (4): `DragSortItemViewCheckable.isChecked`, `DragSortItemViewCheckable.toggle`, `DragSortListView$AdapterWrapper.getItem`, `DragSortListView$AdapterWrapper.isEmpty`
- *UI-reachable* (20):
  - Long-press and checkboxes: `DragSortController.onLongPress`, `onShowPress` [A]; `DragSortItemViewCheckable.setChecked` [A]
  - Drag and auto-scroll: `DragSortItemView.setGravity`; `DragSortListView$1.getSpeed`; `DragSortListView$DragScroller.run`, `startScrolling`; `DragSortListView$HeightCache.add`, `get`; `DragSortListView.adjustItem`, `adjustScroll`, `cancelDrag`, `drawDivider`
  - Fling-remove: `DragSortListView$RemoveAnimator.onStart`, `onUpdate`, `onStop`; `DragSortListView.doRemoveItem` ×2, `removeItem(int,float)`, `stopDragWithVelocity`



