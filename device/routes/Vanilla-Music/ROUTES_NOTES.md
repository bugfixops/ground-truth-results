# Vanilla-Music — ROUTES notes

Scope: one row per `path` row in
`graphs/Vanilla-Music/verification.csv`, in that file's order (30 rows,
route_01 … route_30). `method`, `edges`, and `source` are copied
verbatim from the verification row (`item`, `edges`, `ref`);
`env_kinds` / `state_kinds` are copied verbatim from
`graphs/Vanilla-Music/out/methods.csv` for that method. Nothing was
invented: every route edge id was checked against
`graphs/Vanilla-Music/out/vanilla_trigger_graph.json` (all 30 routes'
edges resolve; no missing edge id), and every permission below was
checked against the manifest (see below). No row was marked
unscriptable for difficulty alone.

## Permissions

Manifest:
`final_java_only/Vanilla-Music/app/Vanilla-Music-#1.3.2/app/src/main/AndroidManifest.xml`
declares, among others:

- `android.permission.READ_EXTERNAL_STORAGE`
- `android.permission.WRITE_EXTERNAL_STORAGE`
- `android.permission.READ_MEDIA_IMAGES`
- `android.permission.READ_MEDIA_AUDIO`
- `android.permission.POST_NOTIFICATIONS`

All five are dangerous runtime permissions and all five are declared,
so any of them could legally be listed. The normal install-time
permissions in the manifest (WAKE_LOCK, FOREGROUND_SERVICE,
FOREGROUND_SERVICE_MEDIA_PLAYBACK, MODIFY_AUDIO_SETTINGS,
INSTALL_SHORTCUT) are never listed, per the task rule.

Non-empty permissions on exactly 4 rows (13, 15, 16, 26), each listing
`android.permission.READ_EXTERNAL_STORAGE;android.permission.WRITE_EXTERNAL_STORAGE`:

- Routes 13, 15, 16: a route edge's ENV prose names both permissions
  explicitly — edge E05fcb9f9 (route_13), E43c53a39 (route_15),
  E5ea28138 (route_16): "the storage permission is granted:
  READ_EXTERNAL_STORAGE and WRITE_EXTERNAL_STORAGE on API 27
  (PermissionRequestActivity.getNeededPermissions) are denied after a
  fresh install, so the media library stays empty until the permission
  dialog is answered with Allow and the scan has read the fixtures in
  /sdcard/Music". The script must answer Allow (or pre-grant via
  `pm grant`) before the gated step, and must start from a state where
  the scan has actually populated the library from the setup-pushed
  Music fixtures; a granted permission with an empty library does not
  satisfy the gate.
- Route_26: the route IS the permission-dialog result
  (PermissionRequestActivity.onRequestPermissionsResult). Its edges
  name no permission literally — they say "storage-permission warning
  banner" (E1adb6602) and "requestPermissions(allPerms, 0)"
  (E10cdb1ad) with guard "havePermissions(activity) is false". The
  two permissions listed are the request set on the graph's API-27
  framing, read from handler source
  (PermissionRequestActivity.java:146-153, `getNeededPermissions`):
  pre-R returns READ_EXTERNAL_STORAGE + WRITE_EXTERNAL_STORAGE.
  API caveat for the device lead (see below): on API 30-32 the needed
  set is READ_EXTERNAL_STORAGE alone, and on API 33+ (TIRAMISU) it is
  READ_MEDIA_AUDIO + READ_MEDIA_IMAGES, with POST_NOTIFICATIONS as an
  optional extra — all declared in the manifest. The script must
  revoke (or start ungranted) whatever the replay image's needed set
  is, tap the banner, and answer the dialog; either answer reaches
  onRequestPermissionsResult, only the granted set differs downstream.

Empty permissions on the other 26 rows is deliberate, not an omission:
a full-field scan of every edge on every route found no other edge
whose env/guard prose names a permission. In particular:

- Routes 01-12, 17-25, 27-30 run inside the app after launch (or, for
  route_17, via a system broadcast) with no permission gate on the
  route. Their need for a populated media library is covered by the
  setup step (push Music fixtures + media scan, with storage granted
  during setup), not by a per-route permission gate, so no permission
  is listed for them.
- Route_14 (notification tap) is not given POST_NOTIFICATIONS: no
  route edge names it. On API 33+ images the harness must still grant
  it during setup or no notification exists to tap — that is a setup
  precondition, noted here, not a route gate.

## Fixtures: empty on all 30 rows (nothing omitted)

Only STATE file gates take a fixtures value. Vanilla-Music has no
`file` state_kind in these 30 routes: the state_kinds present are
`session` (a song loaded / a dialog open / LibraryActivity open),
`data` (a playlist exists, a playlist has a song, the queue holds a
song, a song row is shown), and `settings` (route_14's notification
action preference). Every one of those states is created through the
app itself (play a song, create a playlist via Add to playlist, set a
preference) from the library that the setup step builds by pushing
`fixtures/Music` and running a media scan. No route names a specific
pushed file as its gate, and inventing one (e.g. naming a single
Music track for "a song is loaded") would misrepresent the route, so
fixtures stays empty and no route is marked "fixture missing".

Two related points the device lead still needs:

- The setup push covers the whole `Music/` directory (12 mp3 files,
  `01 Morning Light.mp3` … `12 Lullaby.mp3`, plus three wav tones),
  all verified present under `work-emulator/fixtures/Music/`. Any
  song-dependent script step may use any of them; none is singled out
  in the CSV because the gate is "a song", not "that file".
- Route_13's ACTION_VIEW intent needs an audio URI: use any
  setup-pushed Music file as the URI target. That is an ENV other_app
  intent, not a STATE file gate, so it also takes no fixtures value
  under the column rule — but the script cannot run route_13 without
  it, so it is called out here explicitly.

## Setup: identical on every row

`push fixtures/Music + media scan` — the Vanilla-Music row's `setup`
cell in `work-emulator/ci/apps.csv`, copied verbatim onto all 30 rows
as instructed. It is a setup condition, not a per-route verdict. Note
the ordering consequence: the scan must complete before any
song/playlist/queue-dependent route runs, and routes needing an
ungranted permission (route_26) or a fresh-install permission dialog
must run before setup grants storage, or after a revoke / `pm clear`.

## Status summary

30 rows, 30 scripted, 0 unscriptable (0%, below the 10% flag
threshold). No route meets the unscriptable test: no time, network,
or hardware condition that adb cannot create on an AOSP emulator, and
no missing fixture blocks any route. The two closest calls were both
judged scripted, with the script approach stated so the device lead
can confirm it on the replay image:

- Route_12 (ENV `hardware;time`): the gate is JobScheduler job 9
  (setRequiresCharging, setRequiresDeviceIdle, setPeriodic 32 hours),
  edge Ea27ba51e. This is NOT a "wait 32 hours" route: the job is
  scheduled by the app itself (PlaybackService.java:532 calls
  `ScheduledLibraryUpdate.scheduleUpdate`), and adb can force-run it
  (`cmd jobscheduler run -f <package> 9`) and/or set the
  charging/idle state, instead of waiting for the periodic window.
  Ordering caveat: the job's observer is registered in onStartJob, so
  the notifying library change must happen while the job is running —
  force the job after first launch, then cause a library change (e.g.
  delete a playlist), rather than relying on the first-launch
  fullSyncScan, which precedes job start. If `run -f` does not
  register the observer on the replay image, that is a harness finding
  to report, not a reason to have marked the route unscriptable here,
  since a forced run is the standard adb mechanism for this gate.
- Route_17 (ENV `hardware;system_event`): a media-button event. No
  headset or Bluetooth hardware is needed: adb can deliver the event
  (`input keyevent` media keys, or an ordered MEDIA_BUTTON broadcast
  to the exported MediaButtonReceiver). That is the standard
  adb-creatable substitute, unlike a missing backend service, so the
  route is scripted. If the emulator's media-session routing swallows
  the keyevent, the fallback is a direct broadcast to the receiver
  component; the device lead should confirm which delivery fires
  runAction on the replay image.

## Per-route judgments

- route_01 FolderPickerAdapter$Item.<init> — no env/state gates.
  Launcher -> bottom-bar overflow -> Settings -> "Library" header ->
  "Customize file browser start" -> folder picker refresh creates an
  Item. Scripted.
- route_02 MediaScanner$MediaScanPlan$Step.<init> — no env/state
  gates. Launch triggers the library pager query and a quick scan;
  the scan plan gains a step. Needs the setup scan path to be live,
  not a specific file. Scripted.
- route_03 SongTimeline.removeSongPosition — no env/state gates.
  Queue drag-to-sort animation to completion (RemoveAnimator
  fraction >= 1) removes a song position. Requires a queue with at
  least two songs; drag via input swipe, not a tap. Scripted.
- route_04 CoverCache$BitmapDiskCache.getUsedSpace — no env/state
  gates. Library list rendering loads a cover, stores it in the disk
  cache, trims, and reads used space. Needs at least one scanned song
  with cover handling; any Music fixture song qualifies. Scripted.
- route_05 ID3v2File.getDecodedString — no env/state gates. Open the
  full playback screen and let the extra-info load read ID3 tags from
  the playing song. Scripted.
- route_06 SongTimeline.removeSong — STATE `session`: a song is
  loaded. Full playback overflow menu -> Delete -> confirm dialog ->
  deleteMedia -> removeSong. The song must be playing/loaded first.
  Scripted.
- route_07 SongTimeline$FlagComparator.compare — no env/state gates.
  App start with a saved timeline state sorts songs with the
  comparator. Runs on ordinary launch after a previous session saved
  state. Scripted.
- route_08 Limiter.<init> — no env/state gates. Library -> Files tab
  -> FileSystemAdapter builds the home limiter. Scripted.
- route_09 MediaLibrary.renamePlaylist — STATE `session`: the rename
  dialog of a playlist is open. Long-press a playlist row -> Rename
  (the same input dialog class is reused for rename, with the
  matching callback guard) -> confirm -> renamePlaylist. Requires a
  playlist to exist first (create via Add to playlist if needed).
  Scripted.
- route_10 CoverBitmap.drawText — STATE `session`: a song is loaded.
  Full playback CoverView bitmap generation draws fallback text.
  Scripted.
- route_11 PlaylistActivity.onFancyItemSelected — STATE
  `data;session`: Playlists tab visible with a playlist existing, and
  the open playlist having at least one song. Expand a playlist row
  -> open it -> long-press a song -> fancy menu item. Create the
  playlist and add a song first if the library is fresh. Scripted.
- route_12 ScheduledLibraryUpdate.finalizeScan — ENV
  `hardware;time`. See the force-job discussion in Status summary.
  Scripted.
- route_13 AudioPickerActivity$AudioPickerWorker.getCursorForAnyContent
  — ENV `other_app;permission`. Send ACTION_VIEW with an audio URI
  (any setup-pushed Music file) from another context, with storage
  granted (permissions column) so the worker's permission check
  passes and the cursor query runs. Scripted.
- route_14 MiniPlaybackActivity.onClick — ENV `other_app`, STATE
  `settings`: notification action set to "open mini popup". Set
  Settings > Notifications > notification action to that value
  (non-default), play a song so the notification exists, pull the
  shade, tap a notification button. On API 33+ grant
  POST_NOTIFICATIONS during setup (see Permissions). Scripted.
- route_15 AudioSearchActivity.onSearchCompleted — ENV
  `other_app;permission`. Send MEDIA_PLAY_FROM_SEARCH (e.g. via
  `am start` with that action) with storage granted, so the search
  worker runs to onSearchCompleted. The sender need not be a real
  assistant app: the route's guards are the action and the permission
  check, both satisfiable from adb. Scripted, with that sender
  caveat for the device lead to confirm.
- route_16 TrackDetailsDialog$1$1.<init> — ENV `permission`, STATE
  `data;session`. Storage granted (permissions column) so the scan
  populated the library; Songs tab visible with a song row shown;
  long-press the row -> Details -> dialog view posts the runnable
  whose anonymous class is the target. Scripted.
- route_17 MediaButtonReceiver.runAction — ENV
  `hardware;system_event`. See the media-key discussion in Status
  summary. Scripted.
- route_18 MediaLibrary.updateSongPlayCounts — STATE `session`: a
  song is loaded. Play past the play-count threshold (80% played with
  SHIFT_KEEP_SONG, or at most 50% with SHIFT_NEXT_SONG, per the edge
  guard) so the play-count update message fires. The script must
  control playback position, not just start playback. Scripted.
- route_19 BottomBarControls.setCover — STATE `session`:
  LibraryActivity is open. Playback state broadcast reaches the
  Library instance and updates the bottom-bar cover. Keep the Library
  activity in front while a song plays/changes. Scripted.
- route_20 TrackDetailsDialog.<init> — STATE `data`: the queue holds
  at least one song. Full playback -> swipe up to the queue stage ->
  long-press a queue row -> Details dialog. Scripted.
- route_21 FullPlaybackActivity.updateQueuePosition — no env/state
  gates. Play-all header row -> pickSongs -> jump to a queue
  position. Scripted.
- route_22 MediaScanner$MediaScanPlan.clear — no env/state gates.
  Settings -> Media library -> Cancel while a scan is running ->
  abort scan -> clear the plan. The script must start a scan and
  cancel it mid-run (timing-sensitive, but ordinary UI automation).
  Scripted.
- route_23 VanillaMediaPlayer.setDataSource — no env/state gates.
  App start prepares the media player for the first queue song
  (gapless update path). Scripted.
- route_24 SlidingTabStrip.blendColors — no env/state gates. Library
  content inflation draws the tab strip. Runs on ordinary launch.
  Scripted.
- route_25 PlaybackActivity.onStateChange — no env/state gates.
  Swipe up to the controls stage -> long-press shuffle/repeat ->
  context menu -> set a state different from the current one, so the
  state-change runnable runs. Scripted.
- route_26 PermissionRequestActivity.onRequestPermissionsResult — no
  env/state gates in methods.csv; the route itself is the permission
  flow. Start ungranted (fresh install or revoke), launch, tap the
  storage-permission warning banner, answer the system dialog. See
  the API-conditional permission set in Permissions. Scripted.
- route_27 MediaUtils.getCursorForFileQuery — no env/state gates.
  Play-all header -> pickSongs -> addSongs -> query -> file cursor.
  Scripted.
- route_28 Song.hashCode — no env/state gates. App start processes a
  new playback state and the finish-action path calls Song.equals /
  hashCode. Runs on ordinary launch with a saved state. Scripted.
- route_29 LibraryPagerAdapter.setFilter — no env/state gates.
  Bottom-bar overflow -> search icon -> type in the search field ->
  query text change sets the filter. Scripted.
- route_30 PlaybackService.getDuration — no env/state gates. Controls
  stage -> Previous button -> rewindCurrentSong reads the duration.
  Scripted.

## Ambiguities the device lead must resolve at script time

1. Replay API level (routes 13, 15, 16, 26): the graph's permission
   prose is framed for API 27 (READ + WRITE_EXTERNAL_STORAGE), but
   `getNeededPermissions` returns a different needed set on API 30+
   and API 33+ (see Permissions). Scripts must grant/revoke the set
   for the actual replay image, not blindly the CSV's API-27 pair;
   the CSV pair is correct for the graph's framing and both members
   are declared, but on newer images the media permissions are the
   ones that matter.
2. Job forcing (route_12): confirm `cmd jobscheduler run -f` for job
   9 registers the library observer on the replay image, and confirm
   the ordering (job running before the notifying change).
3. Media-button delivery (route_17): confirm whether `input keyevent`
   media keys reach MediaButtonReceiver on the replay image, or
   whether a direct broadcast to the receiver is needed.
4. Other-app senders (routes 13, 15): both are scripted from adb
   (`am start` with the stated action), but the device lead should
   confirm the receiver/dispatch accepts a shell-sent intent with
   those actions on the replay image.
5. First-launch ordering (route_26 vs the rest): route_26 needs
   permissions ungranted; every song-dependent route needs them
   granted and the library scanned. Run route_26 first on a fresh
   install, or revoke / clear data before it, and do not let a
   once-per-install setup grant silently satisfy its guard.

## Blocked items

None. All inputs were present and readable: verification.csv (30 path
rows), methods.csv (all 30 methods found, env/state copied exactly),
trigger graph (every route edge id resolved), AndroidManifest.xml
(both listed permissions declared, plus the API 33+ media and
notification permissions also declared), the Vanilla-Music row of
apps.csv (setup cell non-empty), and the fixtures directory (Music
fixtures present for the setup push). No permission named in a gate
prose is absent from the manifest, and no STATE file gate lacks a
fixture — because no route in this app has a STATE file gate.
