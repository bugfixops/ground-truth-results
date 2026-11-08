import csv, glob, json, collections, os

g = json.load(open(glob.glob('graphs/Vanilla-Music/out/*_trigger_graph.json')[0]))
E = {x['id']: x for x in g['edges']}
rows = {r['method']: r for r in csv.DictReader(open('graphs/Vanilla-Music/out/methods.csv', encoding='utf-8'))}

LIBS = ' Steps that run through androidx ViewPager / MediaSessionCompat rest on INFERRED claims (androidx source not read).'

RESUME_SRC = ('ERROR FOUND: LibraryActivity and FullPlaybackActivity both inherit onResume from the same un-overridden method (SlidingPlaybackActivity.onResume); MiniPlaybackActivity and '
              'AudioPickerActivity both inherit it from PlaybackActivity.onResume. A plain (un-suffixed) edge from one shared node to a screen let a route enter through one activity and exit '
              'through another activity\'s screen with no gate (found while reading FolderPickerAdapter$Item.<init>: the route entered LibraryActivity and exited through S_FULL, FullPlaybackActivity\'s '
              'screen). Fixed: each activity\'s onResume got its own context variant (@LibraryActivity / @FullPlaybackActivity / @MiniPlaybackActivity / @AudioPickerActivity); the shared bytecode body '
              '(updateElapsedTime, the super.onResume() call, the PlaybackService lookups) is copied onto each variant automatically, only the screen-specific edges needed separate hand edges.')


def route_edges(m):
    return [E[i] for i in rows[m]['route_edge_ids'].split() if i in E]


def uses_resume_variant(m):
    return any(x['src'].startswith(('SlidingPlaybackActivity.onResume@', 'PlaybackActivity.onResume@')) or
               x['dst'].startswith(('SlidingPlaybackActivity.onResume@', 'PlaybackActivity.onResume@')) for x in route_edges(m))


P = {}


def p(m, res, ref, note):
    P[m] = (res, ref, note)


# ---- the sample of 30 (seed 20261025), in the order verify_sample.py printed them, plus FolderPickerAdapter$Item.<init>
# which was also item 1 of this same sample and is where the onResume bug below was first found and fixed.
p('FolderPickerAdapter$Item.<init>', 'fixed', 'LibraryActivity.java:587-589; PreferencesActivity.java:69-74,185-192; FolderPickerActivity.java:68-93,168; FolderPickerAdapter.java:120,204',
  RESUME_SRC + ' Steps read (final route): launcher -> onResume@LibraryActivity -> S_LIBRARY -> tap the bottom bar overflow -> Settings -> tap "Library" header -> tap "Customize file browser '
  'start" -> FilebrowserStartActivity.onCreate -> setCurrentDir -> FolderPickerAdapter.setCurrentDir -> refresh -> new Item(...).' + LIBS)
p('MediaScanner$MediaScanPlan$Step.<init>', 'correct', 'LibraryActivity.java:176-178; LibraryPagerAdapter.java:407,767,688; MediaAdapter.java:374; QueryTask.java:71; MediaLibrary.java:372,122; MediaScanner.java:151-155,239,377,782',
  'Steps read: launcher -> onCreate -> pager.setAdapter (ViewPager asks for the first pages, INFERRED) -> instantiateItem -> setPrimaryItem -> requeryIfNeeded -> postRunQuery -> handleMessage(MSG_RUN_QUERY) -> adapter.query() -> QueryTask.runQuery -> MediaLibrary.queryLibrary -> getBackend() (lazy init) -> MediaScanner.startQuickScan -> handleMessage(MSG_GUESS_QUICKSCAN) -> guessQuickScanPlan -> addNextStep -> new Step(...). Every step guarded or unconditional as cited.' + LIBS)
p('SongTimeline.removeSongPosition', 'fixed', 'DragSortController.java:243-256,411-420; DragSortListView.java:1177-1178,1206-1209,1800-1850,2882-2920; ShowQueueFragment.java:202; PlaybackService.java:2395',
  'ERROR FOUND: two guard-less bytecode edges on the drag-remove touch chain. (1) DragSortController.onTouch -> DragSortListView.stopDragWithVelocity (DragSortController.java:268) runs only inside '
  '`case ACTION_UP: if (mRemoveEnabled && mIsRemoving) { if (x > removePoint) {...} }` (CS.guard_of confirmed). (2) DragSortListView.onTouchEvent -> onDragTouchEvent (line 1648) runs only while '
  '`mDragState == DRAGGING`, and onDragTouchEvent -> stopDrag(boolean) (line 2179) only in `case ACTION_UP: if (mDragState == DRAGGING)`. Fixed: guard + STATE on all three; the best route (no STATE gate avoided) '
  'now goes through the ordinary drag-to-sort animation instead: onScroll -> startDrag (guarded: ON_DRAG mode, touch slop, sort enabled) -> SmoothAnimator.start/run -> RemoveAnimator.onStop (fraction>=1f) '
  '-> doRemoveItem -> ShowQueueFragment.remove -> PlaybackService.removeSongPosition -> SongTimeline.removeSongPosition; every step on this final route already carried a guard.')
p('CoverCache$BitmapDiskCache.getUsedSpace', 'fixed', 'LibraryPagerAdapter.java:353; MediaAdapter.java:554; Song.java:256,273; CoverCache.java:122,148,348,274',
  'ERROR FOUND: the pre-existing MediaAdapter getView/getCount/getItem/getItemId/hasStableIds and getSections/getPositionForSection/getSectionForPosition framework edges from '
  'LibraryPagerAdapter.instantiateItem all cited "LibraryPagerAdapter.java:895", which is inside onItemClick, not view.setAdapter(adapter) (the real call, at line 353, common code right after the '
  'per-tab switch). Fixed: re-cited to line 353. Steps read: instantiateItem -> MediaAdapter.getView -> row.getCoverView().setCover -> LazyCoverView.handleMessage(MSG_CREATE_COVER) -> '
  'Song.getSmallCover -> getCoverInternal -> CoverCache.getCoverFromSong -> storeCover -> BitmapDiskCache.put -> trim -> getUsedSpace.')
p('ID3v2File.getDecodedString', 'correct', 'MiniPlaybackActivity.java:37-51,54-58; FullPlaybackActivity.java:680,513-515,544; PlaybackService.java:766; BastpUtil.java:63,73; Bastp.java:38,74; ID3v2File.java:106,163,211',
  'Steps read: library content inflates SlidingView -> onLayout -> setExpansionStage(0) -> ViewPropertyAnimator ends -> AnimationListener.onAnimationEnd -> FullPlaybackActivity.onSlideExpansionChanged '
  '-> setExtraInfoVisible -> handleMessage(MSG_LOAD_EXTRA_INFO) -> loadExtraInfo -> PlaybackService.getReplayGainValues -> BastpUtil -> Bastp.getTags -> ID3v2File.getTags -> parse_v3_frames -> '
  'normalizeTaginfo -> getDecodedString. All explicit bytecode calls, cited lines match.' + LIBS)
p('SongTimeline.removeSong', 'correct', 'LibraryActivity.java:587-589,451-456; FullPlaybackActivity.java:383-408,393-400; PlaybackActivity.java:499,579; PlaybackService.java:1743',
  'Steps read: tap the bottom bar -> openPlaybackActivity -> FullPlaybackActivity (onResume@FullPlaybackActivity, the fixed variant) -> overflow menu -> Delete (needs_state: a song is loaded, correct '
  'per FullPlaybackActivity.java:384) -> confirm dialog -> handleMessage(MSG_DELETE) -> PlaybackActivity.delete -> PlaybackService.deleteMedia -> SongTimeline.removeSong.')
p('SongTimeline$FlagComparator.compare', 'correct', 'PlaybackActivity.java:124-127; PlaybackService.java:449,2014; SongTimeline.java:309-322,385',
  'Steps read: onStart starts PlaybackService (guard: hasInstance() false) -> onCreate -> loadState -> SongTimeline.readState -> Collections.sort(songs, new FlagComparator()) (SongTimeline.java:385). '
  'The Collections.sort -> Comparator.compare call is INFERRED standard JDK behavior (libcore source not part of frameworks/base, not fetched).')
p('Limiter.<init>', 'correct', 'SlidingTabLayout.java:217,311-320,313-319; LibraryPagerAdapter.java:333; FileSystemAdapter.java:179,360,350',
  'Steps read: launcher -> onResume@LibraryActivity -> S_LIBRARY -> tap the Files tab title -> ViewPager.setCurrentItem (INFERRED) -> instantiateItem@FILE -> new FileSystemAdapter(...) -> '
  'buildHomeLimiter -> buildLimiter(File) -> new Limiter(...).' + LIBS)
p('MediaLibrary.renamePlaylist', 'correct', 'LibraryPagerAdapter.java:341-343; CoordClickListener.java:60-62,79; LibraryPagerAdapter.java:890; LibraryActivity.java:725,743-845,827-837; '
  'FancyMenu.java:169-190,173-185,178,72-76; PlaylistDialog.java:146-172; PlaylistInputDialog.java:93-98,143-156,150; LibraryActivity.java:771-777,773-776; PlaybackActivity.java:495; Playlist.java:194',
  'Steps read: long-press the play-all header -> onCreateFancyMenu -> FancyMenu.show -> S_FANCY_LIBRARY -> tap "Add to playlist" (always present) -> S_DLG_PLAYLIST -> tap an entry -> '
  '"New playlist..." branch (guard: which == BUTTON_CREATE_PLAYLIST) -> PlaylistInputDialog -> onClick -> LibraryActivity$2.onSuccess (STATE: the rename dialog of a playlist row is open - '
  'the same dialog class is reused for rename, with the matching callback guard) -> handleMessage(MSG_RENAME_PLAYLIST) -> Playlist.renamePlaylist -> MediaLibrary.renamePlaylist.')
p('CoverBitmap.drawText', 'correct', 'LibraryActivity.java:587-589,451-456; FullPlaybackActivity.java:106-185; CoverView.java:280,166-169,249,201-206,256,219,236; CoverBitmap.java:132,295',
  'Steps read: tap the bottom bar -> openPlaybackActivity -> FullPlaybackActivity (onResume@FullPlaybackActivity) -> onCreate inflates CoverView -> onSizeChanged -> querySongs -> '
  'handleMessage(MSG_QUERY_SONGS) -> querySongsInternal -> handleMessage(MSG_SET_BITMAP) (STATE: a song is loaded, guard: the song of this slot changed) -> setSongBitmap -> generateBitmap -> '
  'CoverBitmap.createBitmap -> createSeparatedBitmap -> drawText.')
p('PlaylistActivity.onFancyItemSelected', 'correct', 'MediaAdapter.java:499,610-617; LibraryActivity.java:493-495,732-737; PlaylistActivity.java:102-158,211-225; FancyMenu.java:169-190,173-185,72-76,178',
  'Steps read: tap the expand arrow of a Playlists-tab row (STATE: Playlists tab visible and a playlist exists) -> onItemExpanded@PL (guard: type == TYPE_PLAYLIST) -> editPlaylist -> '
  'PlaylistActivity.onCreate -> S_PLAYLIST -> long-press a song row (STATE: the playlist has a song) -> onItemLongClickWithCoords -> FancyMenu.show@P -> S_FANCY_PLAYLIST -> tap a row -> '
  'PlaylistActivity.onFancyItemSelected (the menu was built with callback=this, guard holds).')
p('ScheduledLibraryUpdate.finalizeScan', 'correct', 'PlaybackActivity.java:124-127; PlaybackService.java:513,441-533; PlaylistObserver.java:143-144,236-238,436; Playlist.java:182; '
  'MediaLibrary.java:438,355-359; ScheduledLibraryUpdate.java:79,139',
  'Steps read: PlaybackService.onCreate -> new PlaylistObserver(...) (constructor sends MSG_FULL_SYNC_SCAN unconditionally) -> fullSyncScan -> Playlist.deletePlaylist -> MediaLibrary.removePlaylist '
  '-> notifyObserver(PLAYLIST,...) -> ScheduledLibraryUpdate$1.onChange (ENV: the job runs, guard: the library update job runs) -> finalizeScan (access$100 bridge, consistent with a private method).')
p('AudioPickerActivity$AudioPickerWorker.getCursorForAnyContent', 'correct', 'AndroidManifest.xml:211-235; AudioPickerActivity.java:93,114,187-191,190,211',
  'Steps read: ACTION_VIEW with an audio URI (ENV other_app) -> onCreate -> mWorker.execute(uri) (ENV permission: the storage check passed, intent has a URI) -> doInBackground -> getSongForUri -> '
  'getCursorForAnyContent. AsyncTask.execute -> doInBackground is the standard AsyncTask dispatch (FW-SRC AsyncTask.java cited).')
p('MiniPlaybackActivity.onClick', 'correct', 'PlaybackService.java:475,2086-2089; MiniPlaybackActivity.java:37-51,47-48,54-58',
  'Steps read: PlaybackService.onCreate -> createNotificationAction (ENV: notification tapped, STATE: notification action = "open mini popup") -> PendingIntent.getActivity(MiniPlaybackActivity) -> '
  'onResume@MiniPlaybackActivity (the fixed variant, distinct from onResume@AudioPickerActivity) -> S_MINI -> tap the cover -> onClick.')
p('AudioSearchActivity.onSearchCompleted', 'correct', 'AndroidManifest.xml:237-244; AudioSearchActivity.java:40-57,70-94,92',
  'Steps read: MEDIA_PLAY_FROM_SEARCH (ENV other_app) -> onCreate -> mWorker.execute(query) (ENV permission) -> doInBackground -> onPostExecute (standard AsyncTask postResult dispatch) -> '
  'onSearchCompleted (access$100 bridge, consistent with a private method).')
p('TrackDetailsDialog$1$1.<init>', 'correct', 'LibraryActivity.java:743-845; TrackDetailsDialog.java:75-117,89-114,99',
  'Steps read: long-press a Songs-tab row (STATE: Songs tab visible, a song row shown; ENV permission for the scan to have populated it) -> onFancyItemSelected@SHOW_DETAILS (guard: type == TYPE_SONG) '
  '-> TrackDetailsDialog.onCreateView -> handler.post(new Runnable(){...}) (TrackDetailsDialog$1.run) -> getActivity().runOnUiThread(new Runnable(){...}) -> TrackDetailsDialog$1$1.<init>.')
p('MediaButtonReceiver.runAction', 'correct', 'AndroidManifest.xml:165-170; MediaButtonReceiver.java:176,109',
  'Steps read: ACTION_MEDIA_BUTTON (ENV hardware/system_event) -> onReceive -> processKey -> runAction. Manifest receiver instantiation + onReceive dispatch is standard (FW-SRC ActivityThread cited).')
p('MediaLibrary.updateSongPlayCounts', 'correct', 'LibraryActivity.java:609-611,610; PlaybackActivity.java:215-217,193; PlaybackService.java:1760,678-693,1609; PlayCountsHelper.java:36',
  'Steps read: tap the bottom bar, swipe up to the controls stage -> tap "next" -> shiftCurrentSong -> PlaybackService.shiftCurrentSong -> preparePlayCountsUpdate -> handleMessage(MSG_UPDATE_PLAYCOUNTS) '
  '(STATE: a song is loaded; guard: isPlaying() and the played-percentage condition) -> PlayCountsHelper.countSong -> MediaLibrary.updateSongPlayCounts.')
p('BottomBarControls.setCover', 'fixed', 'PlaybackService.java:520,1000-1014,1584,1100; PlaybackActivity.java:339,302-312,309; LibraryActivity.java:991,997,964,579',
  'ERROR FOUND: this session\'s own new edge LibraryActivity$1.run -> BottomBarControls.setCover cited LibraryActivity.java:578, which is the `public void run() {` line, not the call itself '
  '(`mBottomBarControls.setCover(cover);`, line 579). Fixed: re-cited to 579. Steps read: PlaybackService.onCreate -> updateState -> handleMessage(MSG_BROADCAST_CHANGE) -> broadcastChange -> '
  'PlaybackActivity.setSong(long,Song) -> setSong(Song) -> runOnUiThread -> PlaybackActivity$2.run -> LibraryActivity.onSongChange (STATE: the code runs for the Library instance) -> '
  'handleMessage(MSG_UPDATE_COVER) (guard: song != null) -> updateCover -> runOnUiThread -> LibraryActivity$1.run -> BottomBarControls.setCover.')
p('TrackDetailsDialog.<init>', 'correct', 'LibraryActivity.java:587-589,451-456; ShowQueueFragment.java:108-130,160; TrackDetailsDialog.java:64,50',
  'Steps read: tap the bottom bar -> openPlaybackActivity -> FullPlaybackActivity (onResume@FullPlaybackActivity) -> swipe up to the queue stage -> long-press a queue row (STATE: queue has a song) -> '
  'ShowQueueFragment.onItemLongClickWithCoords -> FancyMenu.show@Q -> S_FANCY_QUEUE -> tap a row -> ShowQueueFragment.onFancyItemSelected -> TrackDetailsDialog.show -> newInstance -> <init>.')
p('FullPlaybackActivity.updateQueuePosition', 'correct', 'LibraryPagerAdapter.java:344,893-903,861-868,895,901; LibraryActivity.java:472-482,395; PlaybackService.java:2376; SongTimeline.java:657,955; '
  'PlaybackService.java:1936; FullPlaybackActivity.java:288-292,601',
  'Steps read: tap the play-all header row -> onItemClicked@HDR (guard: HEADER_ID, no DATA_EXPANDABLE) -> pickSongs (guard: action != DO_NOTHING, row not expandable) -> '
  'PlaybackService.jumpToQueuePosition -> SongTimeline.setCurrentQueuePosition -> broadcastChangedSongs -> PlaybackService.positionInfoChanged -> FullPlaybackActivity.onPositionInfoChanged -> '
  'handleMessage(MSG_UPDATE_POSITION) (guard: mQueuePosView != null) -> updateQueuePosition.')
p('MediaScanner$MediaScanPlan.clear', 'correct', 'BottomBarControls.java:157-181,106-111,198-203,157-158,120-123; PlaybackActivity.java:403,408-424; PreferencesMediaLibrary.java:191-207,197,377; '
  'MediaLibrary.java:279; MediaScanner.java:162',
  'Steps read: tap the bottom-bar overflow -> popup menu -> Settings -> tap "Media library" header -> tap "Cancel" (scan running) -> cancelButtonPressed -> MediaLibrary.abortLibraryScan -> '
  'MediaScanner.abortScan -> MediaScanPlan.clear.')
p('VanillaMediaPlayer.setDataSource', 'correct', 'PlaybackActivity.java:124-127; PlaybackService.java:521,1326,1922-1923,1604,819,668; SongTimeline.java:724,1052',
  'Steps read: onStart starts PlaybackService -> onCreate -> setCurrentSong(0) -> SongTimeline.shiftCurrentSong -> changed -> PlaybackService.timelineChanged -> handleMessage(MSG_GAPLESS_UPDATE) -> '
  'triggerGaplessUpdate -> prepareMediaPlayer -> VanillaMediaPlayer.setDataSource.')
p('SlidingTabStrip.blendColors', 'correct', 'VanillaTabLayout.java:37,41; SlidingTabLayout.java:100; SlidingTabStrip.java:112',
  'Steps read: library content inflates VanillaTabLayout(Context,AttributeSet) -> (Context,AttributeSet,int) -> super (SlidingTabLayout 3-arg ctor) -> new SlidingTabStrip(context) -> onDraw -> '
  'blendColors. Matches the ctor-chain reasoning used for the UNREACHABLE 1- and 2-argument SlidingTabLayout constructors (section I5).')
p('PlaybackActivity.onStateChange', 'correct', 'PlaybackActivity.java:325-330,676-690,692-702,700; PlaybackActivity.java:256-266,263',
  'Steps read: swipe up to the controls stage -> long-press the shuffle/repeat button -> onCreateContextMenu@LIBRARY -> S_CTX_BUTTON@LIBRARY -> onContextItemSelected -> setState(int) (guard: state '
  'changed) -> runOnUiThread -> PlaybackActivity$1.run -> onStateChange (guard: the activity is Mini/AudioPicker/AudioSearch, the plain-PlaybackActivity override).')
p('PermissionRequestActivity.onRequestPermissionsResult', 'correct', 'LibraryActivity.java:188; PermissionRequestActivity.java:96-105,105,118-126,41-50,60-61',
  'Steps read (this session\'s own new wiring): LibraryActivity.onCreate -> PermissionRequestActivity.showWarning -> tap the warning banner -> $1.onClick -> requestPermissions (guard: still not '
  'granted) -> PermissionRequestActivity.<init> -> onCreate -> onRequestPermissionsResult (standard requestPermissions/onRequestPermissionsResult dispatch, FW-SRC Activity.java cited).')
p('MediaUtils.getCursorForFileQuery', 'correct', 'LibraryPagerAdapter.java:344,893-903,861-868,895,901; LibraryActivity.java:472-482,420; PlaybackService.java:1844-1847,1562,1814; SongTimeline.java:763',
  'Steps read: tap the play-all header -> onItemClicked@HDR -> pickSongs -> PlaybackService.addSongs -> handleMessage(MSG_QUERY) -> runQuery -> SongTimeline.addSongs -> MediaUtils.getCursorForFileQuery.')
p('Song.hashCode', 'correct', 'PlaybackActivity.java:124-127; PlaybackService.java:520,1000-1014,1080; SongTimeline.java:507; Song.java:319',
  'Steps read: onStart starts the service -> onCreate -> updateState -> handleMessage(MSG_PROCESS_STATE) -> processNewState -> SongTimeline.setFinishAction -> Song.equals -> Song.hashCode.')
p('LibraryPagerAdapter.setFilter', 'correct', 'BottomBarControls.java:165-174,106-112; LibraryActivity.java:856,877-879,922-935,184,924',
  'Steps read: tap the bottom-bar overflow -> popup -> tap the search icon (guard: MENU_SEARCH) -> onOptionsItemSelected@SEARCH -> showSearch(true) -> S_LIBRARY_SEARCH -> type in the search field -> '
  'onQueryTextChange -> LibraryPagerAdapter.setFilter.')
p('PlaybackService.getDuration', 'correct', 'PlaybackActivity.java:317-331,221-223,222,207; PlaybackService.java:1774',
  'Steps read: swipe up to the controls stage -> tap "previous" -> rewindCurrentSong -> PlaybackService.rewindCurrentSong -> getDuration (read inside rewindCurrentSong\'s own condition).')

# ---- mark every sampled path whose FINAL route still runs through a RESUME_* context variant as 'fixed' too (per the recipe: a route is only as
# final as the last build; these paths were read AFTER the onResume fix and read correct, but the fix is still the reason their route is right)
for m in list(P):
    if rows.get(m, {}).get('verdict') == 'REACHABLE' and uses_resume_variant(m) and P[m][0] == 'correct':
        res, ref, note = P[m]
        P[m] = ('fixed', ref, RESUME_SRC + ' This path\'s route runs through the fixed variant; read correct once the fix was in place. ' + note)

out = [['type', 'item', 'result', 'confirmed_by', 'ref', 'edges', 'note']]
for m, (res, ref, note) in P.items():
    assert m in rows, m
    out.append(['path', m, res, 'SOURCE', ref, rows[m]['route_edge_ids'], note])

# ---- D7 DEVICE rows: only when a real device run has been committed.
# graphs/Vanilla-Music/device/results.csv (columns route,method,edges,
# reached,script_status,run,script) is written by device/compare.py from
# a committed device/results/<run>/ folder. One DEVICE path row per
# route: correct when reached, else unclear (a not-reached route never
# becomes wrong, and no label changes). When the file does not exist,
# this block adds nothing and the output is byte-identical to before.
device_results = 'graphs/Vanilla-Music/device/results.csv'
if os.path.exists(device_results):
    with open(device_results, encoding='utf-8', newline='') as f:
        for d in csv.DictReader(f):
            assert d['method'] in rows, d
            if d['reached'] == 'yes':
                res, note = 'correct', d['script_status']
            elif d['script_status'] == 'unscriptable':
                res, note = 'unclear', 'unscriptable'
            elif d['script_status'] == 'timeout' or d['script_status'].startswith('failed_at_step'):
                res, note = 'unclear', d['script_status'] + ': script failed'
            else:
                res, note = 'unclear', d['script_status'] + ': not reached'
            out.append(['path', d['method'], res, 'DEVICE',
                        'device run %s/%s' % (d['run'], d['script']),
                        d['edges'], note])

# ---- label rows: every UNREACHABLE method (generic row per the recipe's --callers/--all check), plus the REACHABLE labels of the sample
unre = sorted(m for m, l in g['labels'].items() if l.get('unreachable'))
base = ('call sites of the method name searched with grep over the app and library sources, plus layout XML / manifest / menus; scan_unreachable.py --all and --callers run (3 of %d have a bytecode '
        'caller outside the unreachable set, each explained in its own reason: DragSortListView$LiftAnimator.onStart/onUpdate via the never-constructed LiftAnimator, DragSortListView.removeItem(int) '
        'via the never-configured CLICK_REMOVE mode). Reason: ') % len(unre)
for m in unre:
    l = g['labels'][m]
    u = l['unreachable']
    out.append(['label', m, 'correct', l['confirmed_by'], l['source_ref'], '', base + u['text']])

for m in P:
    if rows[m]['verdict'] != 'REACHABLE':
        continue
    out.append(['label', m, 'correct', g['labels'][m]['confirmed_by'], P[m][1].split(';')[0], '',
                'REACHABLE confirmed: the route to it was read step by step (path row); env=%s state=%s' % (rows[m]['env_kinds'] or '-', rows[m]['state_kinds'] or '-')])

# ---- edge rows: one per corrected edge found this session, plus one per distinct FW-SRC citation read
seen = set()


def edge(i, res, ref, note):
    if i in seen:
        return
    seen.add(i)
    out.append(['edge', i, res, 'SOURCE', ref, '', note])


def find_edge(src, dst):
    for x in g['edges']:
        if x['src'] == src and x['dst'] == dst:
            return x['id']
    raise AssertionError((src, dst))


edge(find_edge('LibraryActivity.<init>', 'SlidingPlaybackActivity.onResume@LibraryActivity'), 'fixed', 'LibraryActivity.java:194-198', RESUME_SRC)
edge(find_edge('FullPlaybackActivity.<init>', 'SlidingPlaybackActivity.onResume@FullPlaybackActivity'), 'fixed', 'FullPlaybackActivity.java:168', RESUME_SRC)
edge(find_edge('MiniPlaybackActivity.<init>', 'PlaybackActivity.onResume@MiniPlaybackActivity'), 'fixed', 'MiniPlaybackActivity.java:37-51', RESUME_SRC)
edge(find_edge('AudioPickerActivity.<init>', 'PlaybackActivity.onResume@AudioPickerActivity'), 'fixed', 'AudioPickerActivity.java:80-115', RESUME_SRC)
edge(find_edge('DragSortController.onTouch', 'DragSortListView.stopDragWithVelocity'), 'fixed', 'DragSortController.java:261-268',
     'ERROR FOUND: guard-less bytecode edge; only taken on ACTION_UP with mRemoveEnabled, mIsRemoving and x > removePoint (CS.guard_of confirmed). Fixed: guard + STATE added, sup() on the bare auto edge.')
edge(find_edge('DragSortListView.onTouchEvent', 'DragSortListView.onDragTouchEvent'), 'fixed', 'DragSortListView.java:1646-1648',
     'ERROR FOUND: guard-less bytecode edge; only taken while mDragState == DRAGGING. Fixed: guard + STATE added.')
edge(find_edge('DragSortListView.onDragTouchEvent', 'DragSortListView.stopDrag(boolean)'), 'fixed', 'DragSortListView.java:2176-2179',
     'ERROR FOUND: guard-less bytecode edge; only taken on ACTION_UP while mDragState == DRAGGING. Fixed: guard + STATE added.')
edge(find_edge('LibraryPagerAdapter.instantiateItem', 'MediaAdapter.getView'), 'fixed', 'LibraryPagerAdapter.java:353',
     'ERROR FOUND: this and the 4 other MediaAdapter row-reading edges, plus the 3 fast-scroll edges (8 edges total, pre-existing from an earlier session), cited LibraryPagerAdapter.java:895, which '
     'is inside onItemClick, not view.setAdapter(adapter) (the real common-code call, line 353). Fixed: all 8 re-cited to line 353.')
edge(find_edge("LibraryActivity$1.run", 'BottomBarControls.setCover'), 'fixed', 'LibraryActivity.java:579',
     'ERROR FOUND: this session\'s own new edge cited line 578 (`public void run() {`); the actual call `mBottomBarControls.setCover(cover);` is on line 579. Fixed.')
edge([x['id'] for x in g['edges'] if x['dst'] == 'ListPreferenceSummary.onDialogClosed'][0], 'fixed', 'ListPreference.java:253-264,277-283',
     'ERROR FOUND (check_citations.py): cited core/java/android/preference/ListPreference.java:331-340,352-356, but that file has only 355 lines and those lines are the unrelated SavedState inner '
     'class. The single-choice AlertDialog + onDialogClosed(true) dispatch is actually at lines 253-264 (onPrepareDialogBuilder) and 277-283 (onDialogClosed). Fixed.')
edge(find_edge('LibraryActivity.onOptionsItemSelected@SORT', 'LibraryActivity.onClick(DialogInterface,int)'), 'correct', 'LibraryActivity.java:902-904',
     'check_bytecode_lines.py false positive, not a wrong citation: this REGISTER edge (builder.setSingleChoiceItems(items, mode, this), line 904) is correct, but the checker\'s callee-name '
     'heuristic looks for the literal text "onClick" near the cited line, which an implicit this-as-listener registration never has. PlaylistDialog.onCreateDialog -> onClick (the same pattern) '
     'already works around this with a line range instead of a single line; applied the same range (902-904) here rather than mis-"fixing" the line number.')
# framework claims read this session (FW-SRC), one row per distinct citation
cites = collections.OrderedDict()
for x in g['edges']:
    for seg in (x['evidence'] or '').split(';'):
        seg = seg.strip()
        if seg.startswith('FW-SRC'):
            cites.setdefault(seg.split('(')[0].strip(), x['id'])
for c, i in cites.items():
    edge(i, 'correct', c.replace('FW-SRC ', '').split(' and ')[0], 'lines read in the Android 8.1.0_r1 source: ' + c.replace('FW-SRC ', ''))

with open('graphs/Vanilla-Music/verification.csv', 'w', encoding='utf-8', newline='') as f:
    csv.writer(f).writerows(out)
print(collections.Counter((r[0], r[2]) for r in out[1:]))
