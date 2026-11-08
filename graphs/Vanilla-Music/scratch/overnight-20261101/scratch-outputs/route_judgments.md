# Route judgments — Vanilla-Music sample 30 (seed 20261025), re-read against the rebuilt graph
Method: every step printed by scratch/print_routes.py from graphs/Vanilla-Music/out/methods.csv +
vanilla_trigger_graph.json, app lines read from the connector-reconstructed source tree.
FW-SRC steps are listed with their citations; framework lines themselves are read only
once fw_src is fetched (batch6) — see check_citations.py result. Chain check by the printer:
0 BREAKs, 0 NOT FOUNDs over all 30 routes. Judgments below are this run's re-reads;
the branch's verification.csv convention (a route through the onResume fix logs 'fixed')
is preserved in the regenerated verification.csv — see DECISIONS.md D3.

- Route 1 FolderPickerAdapter$Item.<init> — CORRECT (re-verified). Chain continuous 20 steps.
  Launcher -> onResume@LibraryActivity (the fixed context variant, not the bare shared node)
  -> S_LIBRARY -> bottom-bar overflow -> Settings -> Library header -> file-browser-start
  -> setCurrentDir -> refresh -> new Item. Cited lines match: manifest LibraryActivity entry,
  BottomBarControls 110 openMenu() / 198-203 show(), PlaybackActivity 403 MENU_PREFS /
  408-424 switch case -> 412 startActivity PreferencesActivity, PreferencesActivity 69-74 /
  185-192, FilebrowserStartActivity 35, FolderPickerActivity 168, FolderPickerAdapter 120 / 204.
  Logged 'fixed' in verification.csv under the branch convention (route runs through the
  onResume fix); no new error found this run.
- Route 2 SongTimeline.removeSongPosition — CORRECT (re-verified) with a recorded caveat.
  Chain continuous 18 steps at method level; cited lines match (library_content.xml:74-76
  <fragment ShowQueueFragment>, DragSortListView 525-534 controller registration,
  DragSortController 411-415 startDrag guard, DragSortListView 2230 / 2314 / 1178 / 1207 /
  1411 / 1534 / 1547, ShowQueueFragment 202, PlaybackService 2395).
  CAVEAT (instance-level, not a label error): step 11 enters SmoothAnimator.start via
  startDrag's mLiftAnimator.start() (line 2314, guarded by `if (mLiftAnimator != null)` at
  2313, and the LiftAnimator assignment at line 546 is commented out, so that call never
  fires), while step 13's RemoveAnimator.onStop belongs to the RemoveAnimator instance
  started at lines 1457-1458. At method level — the graph's stated route semantics, which
  ignore guards and model virtual dispatch per method — the path is valid, and a coherent
  execution path to the endpoint exists through mRemoveAnimator.start; the REACHABLE label
  is therefore correct. No fix applied: re-deriving the best route through stopDrag would
  change route costs, not the verdict. Logged 'fixed' in verification.csv (drag-guard fix).
- Route 3 MediaScanner$MediaScanPlan$Step.<init> — CORRECT (re-verified). 15 steps, chain
  continuous. Launcher -> onCreate -> ViewPager setAdapter (INFERRED, LibraryActivity
  176-178) -> setPrimaryItem -> requeryIfNeeded (407) -> postRunQuery (767; 750-755
  sendMessage confirmed, middle line 755) -> handleMessage -> MediaAdapter.query (688
  adapter.query()) -> QueryTask.runQuery (MediaAdapter 374; QueryTask 71) ->
  MediaLibrary.queryLibrary -> getBackend (372) -> startQuickScan (MediaLibrary 122;
  MediaScanner 151-155, middle line 153 sendMessageDelayed confirmed by direct read) ->
  handleMessage -> guessQuickScanPlan (239) -> addNextStep (377) -> new Step (782).
  INFERRED label stands (ViewPager dispatch not read).
- Route 4 CoverCache$BitmapDiskCache.getUsedSpace — CORRECT (re-verified). 13 steps.
  onCreate -> instantiateItem (ViewPager INFERRED) -> MediaAdapter.getView via the fixed
  citation LibraryPagerAdapter.java:353 view.setAdapter(adapter) -> getView 554 setCover ->
  handleMessage (LazyCoverView 174-180 sendMessage) -> Song.getSmallCover (142) ->
  getCoverInternal (256) -> getCoverFromSong (273) -> storeCover (122) -> put (148) ->
  trim (348) -> getUsedSpace (274). Every bytecode line matches exactly. Logged 'fixed'
  in verification.csv (the 353 re-citation); no new error.
- Route 5 ID3v2File.getDecodedString — CORRECT (re-verified). 19 steps. SlidingView
  onLayout -> setExpansionStage(0) (301) -> AnimationListener.onAnimationEnd (205-210,
  389-400) -> onSlideExpansionChanged (398) -> setExtraInfoVisible (680) ->
  handleMessage@MSG_LOAD_EXTRA_INFO (513-515, guard visible && !pending) -> loadExtraInfo
  (588) -> getReplayGainValues (544; PlaybackService 766) -> BastpUtil (63, 73) -> Bastp
  (38, 74) -> ID3v2File.getTags -> parse_v3_frames (106) -> normalizeTaginfo (163) ->
  getDecodedString (211). All lines match.
- Route 6 SongTimeline.removeSong — CORRECT (re-verified). 17 steps. Bottom-bar tap
  (BottomBarControls 135-138 / 113-116) -> LibraryActivity.onClick@BAR (587-589
  openPlaybackActivity) -> FullPlaybackActivity via its own onResume@FullPlaybackActivity
  variant (the fix: no cross-activity exit) -> S_FULL -> overflow menu -> DELETE case
  (383-408) -> confirm dialog (393-400 sendMessage MSG_DELETE) -> handleMessage@MSG_DELETE
  -> delete (499) -> deleteMedia (579) -> removeSong (1743). STATE session (song loaded)
  is stated on the menu step and consistent with the dialog path. Logged 'fixed'
  (resume variant); no new error.
- Route 7 SongTimeline$FlagComparator.compare — CORRECT (re-verified). 8 steps.
  onStart -> super.onStart (211) -> startService guarded by hasInstance()==false
  (124-127) -> onCreate (441-533) -> loadState (449) -> readState (2014) ->
  Collections.sort(songs, new FlagComparator()) (385; comparator at 309-322). The
  sort->compare dispatch is INFERRED JDK behaviour, as labelled.
- Route 8 Limiter.<init> — CORRECT (re-verified). 9 steps. Tab tap (SlidingTabLayout
  217 listener registration, 311-320 listener) -> setCurrentItem -> instantiateItem@FILE
  (INFERRED ViewPager) -> new FileSystemAdapter (LibraryPagerAdapter 333) ->
  buildHomeLimiter (179) -> buildLimiter(File) (360) -> new Limiter (350).
- Route 9 MediaLibrary.renamePlaylist — CORRECT (re-verified) with a recorded caveat.
  18 steps. Long-press (LibraryPagerAdapter 341-343; CoordClickListener 79) ->
  onCreateFancyMenu (890) -> FancyMenu.show (725; 169-190 sheet.show()) -> item click
  (173-185) -> onFancyItemSelected@ADD_TO_PLAYLIST (743-845) -> playlist dialog
  (827-837) -> PlaylistDialog.onClick (146-149, 152-172) -> CREATE branch (155-165) ->
  PlaylistInputDialog.onClick (93-98, 143-156) -> LibraryActivity$2.onSuccess (150) ->
  MSG_RENAME_PLAYLIST (773-776) -> Playlist.renamePlaylist (495) ->
  MediaLibrary.renamePlaylist (194). CAVEAT (same method-level class as route 2): the
  printed entry into PlaylistInputDialog is the create-playlist flow, while the exit
  callback is the rename callback; a coherent rename execution path exists (playlist-row
  Rename -> same dialog with the LibraryActivity$2 callback -> onSuccess), so the label
  is correct and no fix is applied.
- Route 10 CoverBitmap.drawText — CORRECT (re-verified). 19 steps. Bottom-bar tap ->
  openPlaybackActivity (588; 451-456) -> FullPlaybackActivity onCreate -> CoverView
  inflate -> onSizeChanged -> querySongs (280) -> MSG_QUERY_SONGS (166-169) ->
  querySongsInternal (249) -> MSG_SET_BITMAP (201-206, guard song changed, STATE song
  loaded) -> setSongBitmap (256) -> generateBitmap (219) -> createBitmap (236) ->
  createSeparatedBitmap (132) -> drawText (295). All lines match. Logged 'fixed'
  (resume variant); no new error.
- Route 11 PlaylistActivity.onFancyItemSelected — CORRECT (re-verified). 15 steps.
  Expand arrow (MediaAdapter 499, 610-617) -> onItemExpanded@PL (615-616) ->
  editPlaylist guarded TYPE_PLAYLIST (493-495) -> PlaylistActivity (732-737) ->
  onCreate (102-158) -> song long-press (CoordClickListener 69-72, 77-80) ->
  FancyMenu.show@P (211-225, menu built with callback=this) -> menu tap (173-185) ->
  onFancyItemSelected (FancyMenu 178). Callback guard holds. Logged 'fixed'
  (resume variant); no new error.
- Route 12 ScheduledLibraryUpdate.finalizeScan — CORRECT (re-verified). 13 steps.
  onStart -> PlaybackService start (124-127) -> onCreate (441-533) ->
  PlaylistObserver ctor (513) -> MSG_FULL_SYNC_SCAN (143-144) -> fullSyncScan
  (236-238) -> deletePlaylist (436) -> removePlaylist (182) -> notifyObserver
  (438; 355-359 observer iteration) -> ScheduledLibraryUpdate$1.onChange (ENV: job
  runs, charging+idle+periodic) -> finalizeScan (139). ENV hardware;time consistent.
- Route 13 AudioPickerActivity$AudioPickerWorker.getCursorForAnyContent — CORRECT
  (re-verified). 5 steps. Manifest ACTION_VIEW entry (211-235) -> onCreate ->
  worker execute (93, 114; 187-191) -> getSongForUri (190) -> getCursorForAnyContent
  (211). ENV other_app + permission consistent with the entry.
- Route 14 MiniPlaybackActivity.onClick — CORRECT (re-verified). 10 steps. Service
  onCreate -> createNotificationAction (475) -> notification PendingIntent for
  MiniPlaybackActivity (2086-2089, ENV other_app, STATE notification-action setting) ->
  onResume@MiniPlaybackActivity variant (the fix) -> S_MINI (37-51) -> onClick
  (47-48 listener, 54-58 cover case). Logged 'fixed' (resume variant); no new error.
- Route 15 AudioSearchActivity.onSearchCompleted — CORRECT (re-verified). 5 steps.
  Manifest MEDIA_PLAY_FROM_SEARCH entry (237-244) -> onCreate (40-57 execute, guard
  action + permission) -> doInBackground (70-77) -> onPostExecute (70-94) ->
  onSearchCompleted (92). ENV other_app + permission consistent.
- Route 16 TrackDetailsDialog$1$1.<init> — CORRECT (re-verified). 13 steps. Long-press
  -> fancy menu -> SHOW_DETAILS (guard TYPE_SONG, ENV permission, STATE Songs tab) ->
  TrackDetailsDialog.onCreateView (75-117) -> handler.post Runnable (89-114) ->
  runOnUiThread new Runnable at line 99 (the $1$1 ctor). All lines match.
- Route 17 MediaButtonReceiver.runAction — CORRECT (re-verified). 4 steps. Manifest
  receiver entry (165-170) -> onReceive -> processKey (176) -> runAction (109).
  ENV hardware + system_event consistent.
- Route 18 MediaLibrary.updateSongPlayCounts — CORRECT (re-verified). 14 steps.
  Launcher -> resume@Library (fix) -> S_LIBRARY -> swipe bottom bar (SlidingView
  235-251, 313-379) -> S_SLIDE_LIBRARY -> tap next (bindControlButtons 317-331,
  LibraryActivity 609-611, super.onClick 610, onClick@next 215-217) ->
  shiftCurrentSong (216, 193) -> preparePlayCountsUpdate (1760) ->
  MSG_UPDATE_PLAYCOUNTS (678-693, guard isPlaying) -> countSong (1609) ->
  updateSongPlayCounts (PlayCountsHelper 36). Logged 'fixed' (resume variant);
  no new error.
- Route 19 BottomBarControls.setCover — CORRECT (re-verified). 16 steps. Launcher ->
  onStart chain -> service onCreate -> updateState (520) -> MSG_BROADCAST_CHANGE
  (1000-1014, guard state change) -> broadcastChange (1584) -> setSong(long,Song)
  (1100) -> setSong(Song) (339) -> $2.run (302-312) -> onSongChange (309) ->
  MSG_UPDATE_COVER (997) -> updateCover (964) -> $1.run (575-581) -> setCover (579).
- Route 20 TrackDetailsDialog.<init> — CORRECT (re-verified). 14 steps. Launcher ->
  resume@Library (fix) -> S_LIBRARY -> swipe to queue stage (SlidingView 331-343) ->
  queue long-press (CoordClickListener 69-72, 77-80) -> ShowQueueFragment
  .onItemLongClickWithCoords (guard: listener created with ShowQueueFragment) ->
  FancyMenu.show@Q (108-130) -> S_FANCY_QUEUE -> menu tap -> onFancyItemSelected
  (FancyMenu 72-76, 178; ShowQueueFragment 111) -> TrackDetailsDialog.show (160) ->
  newInstance (64) -> <init> (50). Logged 'fixed' (resume variant); no new error.
- Route 21 FullPlaybackActivity.updateQueuePosition — CORRECT (re-verified). 13 steps.
  Launcher -> resume@Library (fix) -> S_LIBRARY -> tap play-all header
  (LibraryPagerAdapter 344, 893-903) -> onItemClicked@HDR (861-868, 895, 901) ->
  pickSongs (472-482) -> jumpToQueuePosition (395) -> setCurrentQueuePosition (2376)
  -> broadcastChangedSongs (657) -> positionInfoChanged (955) ->
  FullPlaybackActivity.onPositionInfoChanged (1936, virtual dispatch) ->
  MSG_UPDATE_POSITION (288-292, guard mQueuePosView != null) -> updateQueuePosition
  (601). Logged 'fixed' (resume variant); no new error.
- Route 22 MediaScanner$MediaScanPlan.clear — CORRECT (re-verified). 19 steps.
  Launcher -> resume@Library (fix) -> S_LIBRARY -> overflow menu (BottomBarControls
  157-181, 106-111) -> openMenu (110) -> S_LIBRARY_MENU (198-203) ->
  onMenuItemClick (157-158, 120-123) -> onOptionsItemSelected@PREFS (403, 408-424) ->
  PreferencesActivity (412) -> onCreate (68-80) -> S_PREFS (69-74) ->
  PreferencesMediaLibrary.<init> via header (preference_headers.xml) -> onViewCreated
  (122-188) -> S_PREFS_MEDIALIB (128-153, 313-341) -> onClick (191-207) ->
  cancelButtonPressed (197) -> abortLibraryScan (377) -> abortScan (279) -> clear
  (162). Logged 'fixed' (resume variant); no new error.
- Route 23 VanillaMediaPlayer.setDataSource — CORRECT (re-verified). 13 steps.
  Launcher -> onStart chain -> service onCreate -> setCurrentSong (521) ->
  shiftCurrentSong (1326) -> changed (724) -> timelineChanged (1052) ->
  MSG_GAPLESS_UPDATE (1922-1923) -> triggerGaplessUpdate (1604) ->
  prepareMediaPlayer (819) -> setDataSource (668).
- Route 24 SlidingTabStrip.blendColors — CORRECT (re-verified). 8 steps. Launcher ->
  onCreate (158-216) -> inflate VanillaTabLayout (library_content.xml) -> ctors
  (37, 41, 100) -> onDraw (FW View) -> blendColors (112).
- Route 25 PlaybackActivity.onStateChange — CORRECT (re-verified). 11 steps. Launcher
  -> resume@Library (fix) -> S_LIBRARY -> swipe -> S_SLIDE_LIBRARY -> context menu
  on shuffle/repeat (325-330, 676-690) -> S_CTX_BUTTON -> onContextItemSelected
  (692-702) -> setState(int) (700) -> $1.run (256-266, guard state changed) ->
  onStateChange (263). Logged 'fixed' (resume variant); no new error.
- Route 26 PermissionRequestActivity.onRequestPermissionsResult — CORRECT
  (re-verified). 8 steps. Launcher -> onCreate (158-216) -> showWarning (188) ->
  $1.onClick (96-105, banner tap -> requestPermissions 105) -> requestPermissions
  (118-126, guard havePermissions false -> startActivity PermissionRequestActivity) ->
  onCreate (41-50, requestPermissions(allPerms, 0)) -> onRequestPermissionsResult
  (FW Activity dispatch 4371-4384, 7270, 7412-7419).
- Route 27 MediaUtils.getCursorForFileQuery — CORRECT (re-verified). 11 steps.
  Launcher -> resume@Library (fix) -> S_LIBRARY -> tap play-all header (344,
  893-903) -> onItemClicked@HDR -> pickSongs (472-482) -> addSongs (420) ->
  MSG_QUERY (1844-1847) -> runQuery (1562) -> addSongs (1814) ->
  getCursorForFileQuery (763). Logged 'fixed' (resume variant); no new error.
- Route 28 Song.hashCode — CORRECT (re-verified). 11 steps. Launcher -> onStart
  chain -> service onCreate -> updateState (520) -> MSG_PROCESS_STATE (1000-1014)
  -> processNewState (1580) -> setFinishAction (1080) -> Song.equals (507) ->
  hashCode (319).
- Route 29 LibraryPagerAdapter.setFilter — CORRECT (re-verified). 8 steps. Launcher
  -> resume@Library (fix) -> S_LIBRARY -> search icon (BottomBarControls 165-174,
  106-112) -> onOptionsItemSelected@SEARCH (856, 877-879) -> S_LIBRARY_SEARCH
  (877-879, BottomBarControls 211-221) -> onQueryTextChange (184, 922-935) ->
  setFilter (924). Logged 'fixed' (resume variant); no new error.
- Route 30 PlaybackService.getDuration — CORRECT (re-verified). 11 steps. Launcher
  -> resume@Library (fix) -> S_LIBRARY -> swipe -> S_SLIDE_LIBRARY -> tap previous
  (317-331, 609-611, super.onClick 610, onClick@previous 221-223) ->
  rewindCurrentSong (222, 207) -> getDuration (1774). Logged 'fixed' (resume
  variant); no new error.

CONVENTION NOTE: routes running through the systemic onResume fix log 'fixed'
under the branch convention even though they read correct after the fix. Route 16
also runs through the resume variant (step 2) and so logs 'fixed' too, although
its judgment above does not carry the note. The authoritative fixed/correct
split for the regenerated verification.csv comes from make_verification.py's
printed Counter, to be recorded when that step runs — not from hand-counting
these notes.
