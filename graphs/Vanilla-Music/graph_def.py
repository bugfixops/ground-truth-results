# Vanilla Music 1.3.2 (ch.blinkenlights.android.vanilla, vanilla-music/vanilla@1.3.2 commit 2e7ef1c, single flavor, instrumented debug build) trigger graph definition.
# Hand-written (schema 2): entry points, lifecycle, pages and GUI handlers, framework callbacks (Handler messages, adapters, menus, preferences,
# dialogs, services, receivers, widgets), gates, UNREACHABLE reasons. Direct app->app calls come from tools/extract_calls.py (bytecode, USE_AUTO).
# Every label, edge and gate below comes from reading the sources under final_java_only/Vanilla-Music/app/Vanilla-Music-#1.3.2/app/src/main/.
# The generated draft of the first pass is kept as generated_draft_graph_def.py.txt (inventory only; nothing is taken over from it).
#
# Section index (search for "# ====="):
#  A  helpers, framework citations, gates
#  B  entry points of the manifest, process start, component lifecycle
#  C  LibraryActivity: start, tabs, rows, search, menus, sliding panel
#  D  PlaybackActivity base: controls, handler messages, menus, seek bar
#  E  FullPlaybackActivity, MiniPlaybackActivity, AudioPicker / AudioSearch / ShortcutPseudoActivity
#  F  PlaybackService, widgets, receivers, job service, timeline callbacks
#  G  preferences, folder pickers, tab order, playlist activity, dialogs
#  H  media library: scanner, backend, tag readers, covers, drag-sort list, small adapters
#  I  verdicts (UNREACHABLE), gate kinds, EDIT, CLASSIFY

TITLE = 'Vanilla Music 1.3.2 trigger graph'
USE_AUTO = True
STRICT = True

import re
import sys
sys.path.insert(0, TOOLS)
import cases
CS = cases.Cases('Vanilla-Music')

# ===================================================================== A. helpers, framework citations, gates
ENV_KINDS_OF, STATE_KINDS_OF = {}, {}


def env_text(text, *kinds):
    ENV_KINDS_OF[text] = list(kinds)
    return text


def state_text(text, *kinds):
    STATE_KINDS_OF[text] = list(kinds)
    return text


# ---- ENV gates (outside the app; the kinds are in the second argument list)
ENV_LAUNCHER = env_text('outside package: the user starts the app from the launcher icon (MAIN / LAUNCHER intent filter of LibraryActivity)', 'other_app')
ENV_SHORTCUT = env_text('outside package: the launcher starts a static app shortcut (res/xml/shortcuts.xml: "play" or "random") or a pinned shortcut', 'other_app')
ENV_WIDGET = env_text('outside package: a Vanilla Music widget is placed on the launcher home screen (the system then calls the AppWidgetProvider receiver)', 'other_app')
ENV_WIDGET_TAP = env_text('outside package: a Vanilla Music widget is placed on the home screen and the user taps one of its buttons (the launcher fires the PendingIntent)', 'other_app')
ENV_MEDIAKEY = env_text('outside package: a media button event (headset button, Bluetooth, media key) is delivered by the system as ACTION_MEDIA_BUTTON', 'hardware', 'system_event')
ENV_SERVICE_EXT = env_text('outside package: another app sends an intent to the exported PlaybackService (action PLAY, PAUSE, TOGGLE_PLAYBACK, NEXT_SONG or PREVIOUS_SONG)', 'other_app')
ENV_NOTIF = env_text('outside package: the user taps a button of the playback notification (the notification shade fires the PendingIntent)', 'other_app')
ENV_VIEW_AUDIO = env_text('outside package: another app sends ACTION_VIEW with an audio file:// or content:// URI (intent filters of AudioPickerActivity)', 'other_app')
ENV_SEARCH = env_text('outside package: another app (voice search, assistant) sends android.media.action.MEDIA_PLAY_FROM_SEARCH', 'other_app')
ENV_JOB = env_text('time passes and the device is idle and charging: JobScheduler runs job 9 (setRequiresCharging, setRequiresDeviceIdle, setPeriodic 32 hours)', 'time', 'hardware')
ENV_PERM = env_text('the storage permission is granted: READ_EXTERNAL_STORAGE and WRITE_EXTERNAL_STORAGE on API 27 (PermissionRequestActivity.getNeededPermissions) are denied after a fresh install, so the media library stays empty until the permission dialog is answered with Allow and the scan has read the fixtures in /sdcard/Music', 'permission')
ENV_PERM_DIALOG = env_text('outside package: the system runtime-permission dialog is answered (PermissionRequestActivity asks for READ and WRITE_EXTERNAL_STORAGE)', 'permission')
ENV_PLUGIN = env_text('outside package: a Vanilla Music plugin app is installed (PluginUtils.checkPlugins finds a receiver for the REQUEST_PLUGIN_PARAMS action)', 'other_app')
ENV_SHARE = env_text('outside package: the Android share chooser or another app is driven (ACTION_SEND for the audio file)', 'other_app')
ENV_EXT_VIEW = env_text('outside package: another app opens the image or text file (ACTION_VIEW)', 'other_app')
ENV_MARKET = env_text('outside package: the Play Store / market app is driven (market://details?id=ch.blinkenlights.android.vanillaplug)', 'other_app')
ENV_VPLUG = env_text('outside package: the Vanilla Headset Launch app (ch.blinkenlights.android.vanillaplug) is installed', 'other_app')
ENV_EQ = env_text('outside package: an audio-effects control panel app answers ACTION_DISPLAY_AUDIO_EFFECT_CONTROL_PANEL', 'other_app')
ENV_WEB = env_text('outside package: a browser is driven (the help page https://github.com/vanilla-music/vanilla-music.github.io/wiki)', 'other_app')
ENV_FOCUS = env_text('outside package: another app takes or gives back audio focus (AudioManager focus change)', 'other_app', 'system_event')
ENV_NOISY = env_text('outside package: the audio output changes (headphones unplugged, AUDIO_BECOMING_NOISY) or the screen turns on (SCREEN_ON)', 'hardware', 'system_event')
ENV_SENSOR = env_text('the accelerometer reports a shake (a sensor event arrives while shake actions are enabled)', 'hardware')
ENV_MEDIASESSION = env_text('outside package: a media controller (system media controls, Bluetooth, another app) calls the MediaSession callback', 'other_app', 'system_event')
ENV_MEDIASTORE = env_text('outside package: the Android MediaStore changes (a file was added, removed or modified: the system media scanner notifies the ContentObserver)', 'system_event')
ENV_FILESYS = env_text('outside package: files are created, deleted or moved in the watched folder (FileObserver event)', 'other')
ENV_OLDDB = env_text('an older media-library.db is on disk (the app was updated from an older build with data); a fresh install creates the database with onCreate', 'other')
ENV_KILL = env_text('time passes with the app in the background and nothing playing: the system stops the idle background PlaybackService (background service limits of API 26+)', 'time', 'system_event')
ENV_ROTATE = env_text('the device is rotated or another configuration changes (the activities declare no configChanges, so the activity is recreated)', 'hardware')
ENV_EXC = env_text('an I/O error or other runtime exception is thrown by the call (missing file, unreadable media, failed query)', 'other')
ENV_FS_NOSCAN = env_text('outside package: the file system allows the app to list the folder (the storage permission is granted)', 'permission')

# ---- STATE gates (earlier in-app action or in-memory / stored state)
NEED_SONGS = state_text('The media library holds songs (needs the storage permission: the scan of /sdcard/Music found the fixture files)', 'data', 'file')
NEED_QUEUE = state_text('The queue holds at least one song (a song was played or enqueued, or the saved queue was restored)', 'data')
NEED_PLAYING = state_text('A song is loaded in the media player (a queue exists and the current song could be prepared)', 'session')
NEED_PLAYLIST = state_text('A playlist exists (Add to playlist > New playlist, or an imported m3u file)', 'data')
NEED_TAB_FILES = state_text('The Files tab is the visible library tab (tap its title)', 'session')
NEED_TAB_PLAYLISTS = state_text('The Playlists tab is the visible library tab (tap its title)', 'session')
NEED_TAB_SONGS = state_text('The Songs tab is the visible library tab (tap its title)', 'session')
NEED_TAB_ALBUMS = state_text('The Albums tab is the visible library tab (tap its title)', 'session')
NEED_LIMITER = state_text('A limiter is set on the current library tab (a row was expanded, "More from artist/album" was chosen, or a folder was opened)', 'session')
NEED_SEARCH = state_text('The search field of the bottom bar is open (Search in the overflow menu, or the search key)', 'session')
NEED_SLIDE = state_text('The sliding panel is pulled up (swipe up on the bottom bar) so the controls and the queue are visible', 'session')
NEED_SLIDE_QUEUE = state_text('The queue list is shown: the sliding panel is pulled fully up (Show queue, or swipe up to the last stage)', 'session')
NEED_PREF_CHANGED = state_text('A preference value was changed while the app runs (Settings screen, or a menu action that writes a preference)', 'settings')
NEED_STATE_FILE = state_text('A previous run saved a non-empty queue (the state file in the app files directory)', 'file')
NEED_OLD_STATE = state_text('A state file written by an earlier run of the service exists in the app files directory', 'file')
NEED_FAV = state_text('The favourites playlist exists (the star in the playback menu was used before)', 'data')
NEED_HIDDEN_TAB = state_text('The Album artists or Composers tab is enabled (Settings > Library > Tabs: tabs hidden by default)', 'settings')
NEED_SYNC_IMPORT = state_text('Settings > Playlists > Synchronization is set to import or to synchronize all (default: disabled)', 'settings')
NEED_SYNC_EXPORT = state_text('Settings > Playlists > Synchronization is set to export or to synchronize all (default: disabled)', 'settings')
NEED_SYNC_PURGE = state_text('Settings > Playlists > Synchronization is set to synchronize all (the purge bit is set; default: disabled)', 'settings')
NEED_M3U_FILE = state_text('A .m3u playlist file exists in the playlist sync folder (default /sdcard/Playlists)', 'file')
NEED_FMT_FLAC = state_text('A FLAC file (magic "fLaC") is in a media folder: the fixtures hold only mp3 and wav files', 'file')
NEED_FMT_OGG = state_text('An Ogg Vorbis or Opus file (magic "OggS") is in a media folder: the fixtures hold only mp3 and wav files', 'file')
NEED_FMT_MP4 = state_text('An MP4 / M4A file (ftyp box) is in a media folder: the fixtures hold only mp3 and wav files', 'file')
NEED_FMT_MIDI = state_text('A MIDI or raw ADTS file is in a media folder: the fixtures hold only mp3 and wav files', 'file')
NEED_FMT_ID3 = state_text('A music file with an ID3v2 tag is in a media folder (the fixture mp3 files)', 'file')
NEED_FMT_MP3 = state_text('An mp3 file whose first bytes are an MPEG frame header (0xFFFB) is in a media folder', 'file')
NEED_COVER_FILE = state_text('A cover image (cover.jpg, folder.png, ...) is in the song folder, or the file carries embedded art, or MediaStore has album art', 'file')
NEED_OPEN_TWICE = state_text('The activity was started before in this process or an earlier run (second start: saved page, saved preferences)', 'session')

# ---- framework citations (AOSP android-8.1.0_r1, lines printed and read) ----
FW_ACT_CREATE = ('FW-SRC core/java/android/app/ActivityThread.java:2669, 2729-2731, 2741 and core/java/android/app/Instrumentation.java:1212-1214, 1333-1334 and core/java/android/app/Activity.java:6993-7000, 7014-7019 '
                 '(performLaunchActivity creates the activity, callActivityOnCreate calls performCreate which calls onCreate, then performStart runs callActivityOnStart which calls onStart)')
FW_ACT_RESUME = ('FW-SRC core/java/android/app/ActivityThread.java:3556 and core/java/android/app/Instrumentation.java:1353-1355 and core/java/android/app/Activity.java:7098-7107 '
                 '(performResumeActivity calls Activity.performResume, which calls callActivityOnResume and so onResume)')
FW_ACT_PAUSE = ('FW-SRC core/java/android/app/ActivityThread.java:3812-3826 and core/java/android/app/Instrumentation.java:1407-1408 and core/java/android/app/Activity.java:7139-7143 '
                '(handlePauseActivity calls performPauseActivity; callActivityOnPause calls performPause, which calls onPause)')
FW_ACT_STOP = ('FW-SRC core/java/android/app/Instrumentation.java:1374-1376 and core/java/android/app/Activity.java:7159-7181 '
               '(performStop calls callActivityOnStop, which calls onStop)')
FW_ACT_DESTROY = ('FW-SRC core/java/android/app/Instrumentation.java:1232, 1249 and core/java/android/app/Activity.java:7204-7208 '
                  '(callActivityOnDestroy calls performDestroy, which calls onDestroy)')
FW_ACT_NEWINTENT = ('FW-SRC core/java/android/app/ActivityThread.java:2936-2952 and core/java/android/app/Instrumentation.java:1308-1309 and core/java/android/app/Activity.java:7009-7012 '
                    '(performNewIntents delivers a new intent to a running activity, pausing and resuming it around the delivery; callActivityOnNewIntent calls performNewIntent, which calls onNewIntent)')
FW_ACT_KEY = ('FW-SRC core/java/android/app/Activity.java:3255-3273 and core/java/android/view/KeyEvent.java:2684-2715 '
              '(Activity.dispatchKeyEvent calls event.dispatch(this ...); KeyEvent.dispatch calls the receiver onKeyDown on ACTION_DOWN and onKeyUp on ACTION_UP)')
FW_ACT_MENU = ('FW-SRC core/java/android/app/Activity.java:3386-3388, 3404-3406, 3439-3450 '
               '(the window panel callbacks call onCreateOptionsMenu, onPrepareOptionsMenu and, for a selected item, onOptionsItemSelected)')
FW_HANDLER = ('FW-SRC core/java/android/os/Handler.java:97-108, 355-358, 596-602, 623-631 and core/java/android/os/Looper.java:164 '
              '(sendMessage / post queue the message on the handler looper; Looper.loop calls msg.target.dispatchMessage, which runs the Runnable callback or calls mCallback.handleMessage; '
              'the looper thread of a HandlerThread is started by HandlerThread.run, core/java/android/os/HandlerThread.java:60-65)')
FW_INFLATE = ('FW-SRC core/java/android/view/LayoutInflater.java:615-617, 645-647 '
              '(createView looks up the (Context, AttributeSet) constructor of the view class named in the XML and calls newInstance)')



# every call site of every bytecode edge (tools/extract_calls.py keeps only the last line of a caller/callee pair; calls_all.json is the same scan with all lines,
# written by a copy of that script that adds the field "lines"; the edge set is identical to auto_calls.json)
import json
ALL_CALLS = json.load(open(GDIR + '/calls_all.json'))['calls']
CALLS_OF = {}
for _c in ALL_CALLS:
    CALLS_OF.setdefault(_c['src'], []).append(_c)


def calls_in(src, a, b):
    """[(callee, line, file, dispatch)] of the bytecode calls of node `src` whose source line lies in [a, b]; one entry per callee (first line in the range)."""
    out, seen = [], set()
    for c in CALLS_OF.get(src, []):
        ls = sorted(l for l in c['lines'] if a <= l <= b)
        if ls and c['dst'] not in seen:
            seen.add(c['dst'])
            out.append((c['dst'], ls[0], c['file'], c['dispatch']))
    return out



def switch_branches(fname, mname, which=0, nth=0, params=None, any_depth=False):
    """Branches [(label, first_line, last_line)] of the `which`-th switch anywhere inside method `mname` (cases.branches only reads the first top-level construct)."""
    lines, text = CS._load(fname)
    starts = CS._offsets(text)
    a, b = CS.method_lines(fname, mname, nth, params, any_depth)
    o0 = starts[a - 1]
    o1 = starts[b]
    body = text[o0:o1]
    idx = [m.start() for m in re.finditer(r'\bswitch\s*\(', body)]
    i = idx[which]
    p = body.index('(', i)
    pe = CS._match(body, p, '(', ')')
    ob = body.index('{', pe)
    cb = CS._match(body, ob)
    inner = body[ob + 1:cb]
    ibase = o0 + ob + 1
    labels, d, j = [], 0, 0
    while j < len(inner):
        c = inner[j]
        if c == '{':
            d += 1
        elif c == '}':
            d -= 1
        elif d == 0:
            mm = re.match(r'(case\s+[^:]+?|default)\s*:(?!:)', inner[j:])
            if mm and (j == 0 or not (inner[j - 1].isalnum() or inner[j - 1] == '_')):
                labels.append((re.sub(r'^case\s+', '', mm.group(1)).strip(), j, j + mm.end()))
                j += mm.end()
                continue
        j += 1
    out, pending = [], []
    for k, (lab, s0, s1) in enumerate(labels):
        nxt = labels[k + 1][1] if k + 1 < len(labels) else len(inner)
        stmt = inner[s1:nxt]
        pending.append(lab)
        if stmt.strip() == '':
            continue
        la = CS._line_of(starts, ibase + s0)
        last = inner[:nxt].rstrip()
        lb = CS._line_of(starts, ibase + len(last) - 1)
        for l_ in pending:
            out.append((l_, la, lb))
        pending = []
    return out

def variants_of(src, fname, mname, nth=0, params=None, bounds=None, names=None, only=None, skip=(), text=None, **gate):
    """Context variants of `src`: one node `src@LABEL` per branch (first switch / if-chain, tools/cases.py) holding the bytecode calls of that branch.
    names maps a label to a short variant name; `gate` may give per-label gates: {label: dict(guard=..., needs_state=..., env=...)}.
    Returns {label or short name: variant node}. The plain node keeps only the calls outside every branch."""
    br = bounds if bounds is not None else CS.branches(fname, mname, nth, params)
    out = {}
    gates = gate.get('gates', {})
    for label, a, b in br:
        if label in skip or (only is not None and label not in only):
            continue
        nm = (names or {}).get(label, label)
        var = '%s@%s' % (src, nm)
        out[label] = var
        out[nm] = var          # the result can be indexed by the label of the source or by the short name
        for dst, line, fn, disp in calls_in(src, a, b):
            call(var, dst, text or ('call made in the branch %s of %s' % (nm, src.split('.', 1)[1])), 'SRC %s:%d (bytecode)' % (fn, line))
    return out

def gui(src, dst, text, kind='GUI', **kw):
    e(src, dst, kind, text, gui=[text], **kw)


def sup(*items):
    for it in items:
        SUPPRESS.add(it)


def call(src, dst, text, ev, kind='CALL', **kw):
    """A hand-written call edge (the bytecode scan cannot see it, or it needs a variant node); kind CALL unless the framework makes the call."""
    e(src, dst, kind, text, evidence=ev, **kw)

# ---- more framework citations (lines printed and read)
FW_VIEW_CLICK = ('FW-SRC core/java/android/view/View.java:6289-6296, 6370-6376, 11768-11774 '
                 '(performClick calls the OnClickListener set with setOnClickListener, performLongClick calls the OnLongClickListener, the touch dispatch calls the OnTouchListener)')
FW_VIEW_DRAW = ('FW-SRC core/java/android/view/View.java:17445, 19659, 19792, 22071, 19192 '
                '(the view system calls onAttachedToWindow when the view is attached, onMeasure from measure, onLayout from layout, onSizeChanged when the frame size changes and onDraw from draw)')
FW_INFLATE_FINISH = ('FW-SRC core/java/android/view/LayoutInflater.java:876 '
                     '(rInflate calls parent.onFinishInflate() after the children of the inflated ViewGroup were created)')
FW_FRAG_XML = ('FW-SRC core/java/android/app/FragmentManager.java:3491-3496, 3527-3528, 3536-3537 and core/java/android/app/Fragment.java:508-520 '
               '(the layout inflater hands the <fragment> tag to FragmentManager.onCreateView, which instantiates the class named by the class attribute through Fragment.instantiate (reflection) and adds it)')
FW_FRAG_LIFE = ('FW-SRC core/java/android/app/FragmentManager.java:1237, 1279, 1299, 1315, 1322 and core/java/android/app/Fragment.java:2489, 2502-2508, 2511-2517, 2527-2534, 2547-2554 '
                '(moveToState calls performCreate, performCreateView, performActivityCreated, performStart and performResume, which call the fragment onCreate, onCreateView, onActivityCreated, onStart and onResume)')
FW_RUNUI = ('FW-SRC core/java/android/app/Activity.java:6170-6176 '
            '(runOnUiThread runs the action directly on the UI thread, else posts it to the activity handler)')
FW_VIEWPAGER = 'INFERRED androidx.viewpager.widget.ViewPager calls the PagerAdapter methods (setAdapter, setCurrentItem, populate) and the OnPageChangeListener (androidx source not read)'
FW_MEDIAPLAYER = 'INFERRED android.media.MediaPlayer reports completion and errors through the listeners set with setOnCompletionListener / setOnErrorListener (MediaPlayer source: see the cited lines where read)'

# ===================================================================== B. entry points, process start, component lifecycle
SCREENS = {
    'S_ENTRY': 'Outside the app: launcher icon or shortcut, widget, notification, media button, another app, the system scheduler or adb',
    'S_EXIT': 'The activity task ended (Back from the library with nothing to undo)',
    'S_LIBRARY': 'LibraryActivity: tab strip (Artists, Albums, Songs, Playlists, Genres, Files), list of the current tab with a play-all header row, bottom bar with the current song and the overflow menu button',
    'S_LIBRARY_SEARCH': 'LibraryActivity with the search field of the bottom bar open (keyboard shown)',
    'S_LIBRARY_MENU': 'Overflow menu (PopupMenu) of the bottom bar: Settings, Playback view, Go home (Files tab), Sort by, Show queue / Hide queue, Dequeue rest, Empty the queue, Save as playlist, Jump to time',
    'S_SLIDE_LIBRARY': 'LibraryActivity with the sliding panel pulled up: seek bar and the shuffle / previous / play-pause / next / repeat buttons',
    'S_SLIDE_LIBRARY_QUEUE': 'LibraryActivity with the sliding panel fully up: the queue list (ShowQueueFragment) is visible',
    'S_FANCY_LIBRARY': 'Bottom sheet context menu (FancyMenu) of a library row',
    'S_DLG_SORT': 'Sort dialog: single-choice list of sort modes and the "reverse sort" check box',
    'S_DLG_DELETE_MEDIA': 'Confirm dialog "Delete" for the selected library item (positive button deletes the files)',
}


def lifecycle(cls, cbs, cite, text='Activity lifecycle callback', src=None, **kw):
    """Edges `<init>` -> the node that runs for an instance of `cls` for each callback name in cbs (impl() resolves inherited implementations)."""
    for cb in cbs:
        try:
            node = impl(cls, cb)
        except KeyError:
            continue
        e(src or (cls + '.<init>'), node, 'LIFECYCLE', text, evidence=cite, **kw)


# ---- B1. entry points (manifest)
e('S_ENTRY', 'LibraryActivity.<init>', 'ENTRY', 'MAIN / LAUNCHER intent starts LibraryActivity', gui=['Home screen: tap the Vanilla Music icon'],
  evidence='SRC AndroidManifest.xml:73-90; ' + FW_ACT_CREATE)
e('S_ENTRY', 'ShortcutPseudoActivity.<init>', 'ENTRY', 'a static app shortcut (play / random mix) starts ShortcutPseudoActivity with the action of the shortcut', env=ENV_SHORTCUT,
  gui=['Long-press the launcher icon and tap the "Play" or "Random" shortcut'], evidence='SRC AndroidManifest.xml:86-88, 202-209; res/xml/shortcuts.xml:3-26')
e('S_ENTRY', 'AudioPickerActivity.<init>', 'ENTRY', 'another app opens an audio file with ACTION_VIEW (file:// or content:// data)', env=ENV_VIEW_AUDIO,
  gui=['In a file manager open an audio file and choose Vanilla Music'], evidence='SRC AndroidManifest.xml:211-235')
e('S_ENTRY', 'AudioSearchActivity.<init>', 'ENTRY', 'another app sends MEDIA_PLAY_FROM_SEARCH', env=ENV_SEARCH, gui=['Ask the voice assistant to play a song'], evidence='SRC AndroidManifest.xml:237-244')
e('S_ENTRY', 'MediaButtonReceiver.<init>', 'ENTRY', 'the system delivers ACTION_MEDIA_BUTTON to the exported receiver', env=ENV_MEDIAKEY, gui=['Press the headset / media button'],
  evidence='SRC AndroidManifest.xml:165-170; FW-SRC core/java/android/app/ActivityThread.java:3141-3190 (handleReceiver instantiates the manifest receiver class and calls onReceive)')
e('MediaButtonReceiver.<init>', 'MediaButtonReceiver.onReceive', 'LIFECYCLE', 'BroadcastReceiver.onReceive is called with the intent',
  evidence='SRC AndroidManifest.xml:165-170; FW-SRC core/java/android/app/ActivityThread.java:3141-3190 (handleReceiver instantiates the manifest receiver class and calls onReceive)')
e('S_ENTRY', 'PlaybackService.<init>', 'ENTRY', 'another app starts the exported PlaybackService with one of its five actions', env=ENV_SERVICE_EXT,
  gui=['Send the PLAY / PAUSE / TOGGLE_PLAYBACK / NEXT_SONG / PREVIOUS_SONG intent to the service'], evidence='SRC AndroidManifest.xml:171-181')
e('S_ENTRY', 'ScheduledLibraryUpdate.<init>', 'ENTRY', 'JobScheduler starts the scheduled library update job', env=ENV_JOB,
  evidence='SRC AndroidManifest.xml:183-186; ScheduledLibraryUpdate.java:51-73 (job 9: charging, idle, every ~32 hours)')
for w in ('OneCellWidget', 'FourLongWidget', 'FourSquareWidget', 'FourWhiteWidget', 'WidgetD', 'WidgetE'):
    e('S_ENTRY', w + '.<init>', 'ENTRY', 'the system sends APPWIDGET_UPDATE / ENABLED / DISABLED to the widget provider receiver', env=ENV_WIDGET,
      gui=['Long-press the home screen, open Widgets and add the Vanilla Music widget'], evidence='SRC AndroidManifest.xml:99-164 (receiver of ' + w + ', action APPWIDGET_UPDATE, android.appwidget.provider meta-data)')
    for cb in ('onEnabled', 'onUpdate', 'onDisabled'):
        e(w + '.<init>', w + '.' + cb, 'LIFECYCLE', 'AppWidgetProvider.onReceive calls %s for the widget broadcast' % cb,
          evidence='FW-SRC core/java/android/appwidget/AppWidgetProvider.java:57-67, 84-87 (onReceive calls onUpdate for APPWIDGET_UPDATE and onEnabled / onDisabled for the enable / disable actions) and '
                   'core/java/android/app/ActivityThread.java:3141-3190 (handleReceiver instantiates the manifest receiver class and calls onReceive); SRC AndroidManifest.xml:99-164', env=ENV_WIDGET)

# the library activity is started by many app-internal intents; singleTask: a running instance gets onNewIntent, otherwise a new one is created
LIB_NEW = 'the library task does not exist yet: a new LibraryActivity is created (launchMode singleTask)'
LIB_RUN = 'LibraryActivity runs already in the back stack (launchMode singleTask): the system delivers the intent with onNewIntent'
PBA_CLASSES = ('LibraryActivity', 'FullPlaybackActivity', 'MiniPlaybackActivity', 'AudioPickerActivity', 'AudioSearchActivity')

# ---- B2. lifecycle of the activities
e('LibraryActivity.<init>', 'LibraryActivity.<clinit>', 'LIFECYCLE', 'class initialisation (static array modeForAction)',
  evidence='SRC LibraryActivity.java:124-127; INFERRED the JVM runs the static initialiser before the first use of the class (Java language rule, not read from a source)')
lifecycle('LibraryActivity', ('onCreate', 'onStart'), FW_ACT_CREATE, 'Activity lifecycle callback; SRC LibraryActivity.java:158-216 (the callbacks of the class and its superclasses)')
# LibraryActivity does not override onResume: impl('LibraryActivity', 'onResume') resolves to the single shared method SlidingPlaybackActivity.onResume,
# which FullPlaybackActivity (also no override of its own) resolves to as well. A plain (un-suffixed) edge from that one shared node to a screen would let
# the builder enter LibraryActivity and exit through FullPlaybackActivity's screen (or vice versa) with no gate - a wrong route found while reading this
# sample. Context variants (@LibraryActivity / @FullPlaybackActivity, see RESUME_FP below) keep the two activities' resumes apart; the automatic bytecode
# edges of the shared body (updateElapsedTime, the super.onResume() call) are copied onto each variant by the builder (variants_of's rule), so only the
# screen-specific edges need to be written twice.
RESUME_LA = 'SlidingPlaybackActivity.onResume@LibraryActivity'
e('LibraryActivity.<init>', RESUME_LA, 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACT_RESUME)
e(RESUME_LA, 'S_LIBRARY', 'ENTERS', 'LibraryActivity is resumed and shown (default tab Artists: library_page = 0)', guard='no saved page (library_page = 0, the default)',
  evidence='SRC LibraryActivity.java:194-198; SlidingPlaybackActivity.java:91-96; PrefDefaults.java:52')

FW_PERM = ('FW-SRC core/java/android/app/Activity.java:4371-4384, 7270, 7412-7419 '
           '(requestPermissions starts the system permission screen with startActivityForResult; when its result returns, dispatchRequestPermissionsResult calls onRequestPermissionsResult)')
FW_ITEMCLICK = ('FW-SRC core/java/android/widget/AdapterView.java:314-319 and core/java/android/widget/AbsListView.java:3223-3238 '
                '(performItemClick calls the OnItemClickListener; performLongPress calls the OnItemLongClickListener registered with setOnItemLongClickListener)')
FW_GETVIEW = ('FW-SRC core/java/android/widget/AbsListView.java:2348-2365 '
              '(obtainView calls mAdapter.getView for each visible row of the list)')
FW_SAVESTATE = ('FW-SRC core/java/android/app/Activity.java:1565-1566 and core/java/android/view/View.java:17611-17614 '
                '(Activity.onSaveInstanceState saves the window hierarchy; dispatchSaveInstanceState calls the onSaveInstanceState of each view with an id)')

# ---- C0. layout inflation: the classes named in the XML layouts are built by the LayoutInflater (non_standard)
def inflate(src, classes, layout, cite=FW_INFLATE):
    for c in classes:
        node = c if '(' in c or c.endswith('.<init>') else c + '.<init>'
        e(src, node, 'FRAMEWORK', 'setContentView / inflate builds the view or fragment <%s> of %s' % (c.split('.')[0], layout), evidence='SRC res/layout/' + layout + '; ' + cite)


def finish_inflate(cls, cb='onFinishInflate'):
    e(cls + '.<init>' if cls + '.<init>' in METHODS else cls + '.<init>(Context,AttributeSet)', cls + '.' + cb, 'FRAMEWORK', 'the inflater calls onFinishInflate after the children were created',
      evidence=FW_INFLATE_FINISH)


# ===================================================================== C. LibraryActivity
OC = 'LibraryActivity.onCreate'
inflate(OC, ['BottomBarControls', 'SlidingView.<init>(Context,AttributeSet)', 'VanillaTabLayout.<init>(Context,AttributeSet)', 'VanillaImageButton.<init>(Context,AttributeSet)'], 'library_content.xml, bottombar_controls.xml, controls.xml')
e(OC, 'ShowQueueFragment.<init>', 'FRAMEWORK', 'setContentView inflates the <fragment class=ShowQueueFragment> of library_content.xml', evidence='SRC res/layout/library_content.xml:74-76; ' + FW_FRAG_XML,
  cls='non_standard', via='the <fragment> XML tag; FragmentManager.onCreateView instantiates the named class through reflection (Fragment.instantiate)')
finish_inflate('BottomBarControls')
finish_inflate('SlidingView')
# mPlayPauseButton/mEndButton/mShuffleButton are declared as the platform ImageButton type, so the virtual call is not resolved by the bytecode scan to the app's override (same gap as other base-typed-field dispatch in this app)
e('PlaybackActivity.onStateChange', 'VanillaImageButton.setImageResource', 'CALL', 'mPlayPauseButton/mEndButton/mShuffleButton.setImageResource(...): virtual call on an ImageButton-typed field whose runtime class is VanillaImageButton',
  guard='the button field holds a VanillaImageButton instance (inflated from controls.xml)', evidence='SRC PlaybackActivity.java:239-248 (bytecode); res/layout/controls.xml')
for cb in ('onCreateView',):
    e('ShowQueueFragment.<init>', 'ShowQueueFragment.' + cb, 'LIFECYCLE', 'Fragment lifecycle callback', evidence=FW_FRAG_LIFE + '; SRC ShowQueueFragment.java:49-68')
e('ShowQueueFragment.<init>', 'ShowQueueFragment.onResume', 'LIFECYCLE', 'Fragment lifecycle callback', evidence=FW_FRAG_LIFE + '; SRC ShowQueueFragment.java:76-87')
e('ShowQueueFragment.<init>', 'ShowQueueFragment.onDestroyView', 'LIFECYCLE', 'the fragment view is destroyed when the activity is destroyed', env=ENV_ROTATE,
  evidence='FW-SRC core/java/android/app/FragmentManager.java:1356 and core/java/android/app/Fragment.java:2744-2750 (moveToState calls performDestroyView, which calls onDestroyView); SRC ShowQueueFragment.java:70-74')
# ViewPager (androidx): adapter callbacks after setAdapter / setCurrentItem
for cb in ('getCount', 'isViewFromObject', 'getItemPosition', 'setPrimaryItem', 'destroyItem'):
    e(OC, 'LibraryPagerAdapter.' + cb, 'FRAMEWORK', 'pager.setAdapter(...): the ViewPager calls PagerAdapter.' + cb, evidence=FW_VIEWPAGER + '; SRC LibraryActivity.java:176-178', cls='non_standard', via='androidx ViewPager calls the PagerAdapter')
# cold start: page 0 (Artists) and its neighbour (Albums) are instantiated, in the default tab order
e(OC, 'LibraryPagerAdapter.instantiateItem', 'FRAMEWORK', 'pager.setAdapter(...): the ViewPager asks the adapter for the first pages', guard='the pager starts on page 0 and keeps one page on each side',
  evidence=FW_VIEWPAGER + '; SRC LibraryActivity.java:176-178; LibraryPagerAdapter.java:72-78', cls='non_standard', via='androidx ViewPager calls the PagerAdapter')
# the overflow menu is built by the app: BottomBarControls calls the owner activity (typed Activity, so the scan sees no edge)
for cb, line in (('onCreateOptionsMenu', 161), ('onPrepareOptionsMenu', 201)):
    src = 'BottomBarControls.enableOptionsMenu' if cb == 'onCreateOptionsMenu' else 'BottomBarControls.openMenu'
    e(src, impl('LibraryActivity', cb), 'CALL', 'mParentMenuConsumer.%s(...) calls the owner LibraryActivity override' % cb,
      guard='the receiver is the LibraryActivity registered with enableOptionsMenu(this) (its only caller)', evidence='SRC BottomBarControls.java:%d; LibraryActivity.java:185' % line)
e('BottomBarControls.onMenuItemClick', impl('LibraryActivity', 'onOptionsItemSelected'), 'CALL', 'mParentMenuConsumer.onOptionsItemSelected(item) calls the owner LibraryActivity override',
  evidence='SRC BottomBarControls.java:122; LibraryActivity.java:185')


def send(site, handler, variants, label, text, ev, kind='ASYNC', plain=True, **kw):
    """A Handler.sendMessage from `site`: the looper thread then calls handleMessage of `handler`. Both the method (plain node) and the branch of the message are reached."""
    if plain:
        e(site, handler, kind, 'Handler.dispatchMessage calls %s.handleMessage with %s' % (handler.split('.')[0], text), evidence=ev + '; ' + FW_HANDLER, **kw)
    e(site, variants[label], kind, 'the branch of %s that handles %s runs' % (handler.split('.')[0], text), evidence=ev + '; ' + FW_HANDLER, **kw)


def branch(src, variants, gates, ev_file, bounds=None, kind='CALL'):
    """Edges plain node -> variant (the user or the data selects the branch); gates: {label: dict(guard=, needs_state=, env=)}."""
    rng = {l: (a, b) for l, a, b in (bounds or [])}
    for label, var in variants.items():
        if '.' in label and label.split('.')[0] in ('MediaUtils', 'R', 'KeyEvent', 'PrefKeys') and False:
            continue
        g = dict(gates.get(label, {}))
        ab = rng.get(label)
        ev = 'SRC %s:%s' % (ev_file, ('%d-%d' % ab) if ab else '?') if ab else 'SRC ' + ev_file
        e(src, var, kind, g.pop('text', 'branch %s of %s' % (var.split('@')[1], src.split('.', 1)[1])), evidence=g.pop('evidence', ev), **g)


# ---- C1. tabs and the pager (androidx ViewPager is INFERRED; the platform lifecycle is cited)
LP = 'LibraryPagerAdapter'
IT_BOUNDS = switch_branches('LibraryPagerAdapter.java', 'instantiateItem')
IT_NAMES = {'MediaUtils.TYPE_ARTIST': 'ARTIST', 'MediaUtils.TYPE_ALBARTIST': 'ALBARTIST', 'MediaUtils.TYPE_COMPOSER': 'COMPOSER', 'MediaUtils.TYPE_ALBUM': 'ALBUM', 'MediaUtils.TYPE_SONG': 'SONG',
            'MediaUtils.TYPE_PLAYLIST': 'PLAYLIST', 'MediaUtils.TYPE_GENRE': 'GENRE', 'MediaUtils.TYPE_FILE': 'FILE', 'default': 'DEFAULT'}
IT = variants_of('LibraryPagerAdapter.instantiateItem', 'LibraryPagerAdapter.java', 'instantiateItem', bounds=IT_BOUNDS, names=IT_NAMES, text='the page of this tab type is built')
# default tab order (TAB_ORDER preference not set): Artists, Albums, Songs, Playlists, Genres, Files; Album artists and Composers are hidden
for lab, ev in (('MediaUtils.TYPE_ARTIST', 'page 0'), ('MediaUtils.TYPE_ALBUM', 'page 1, next to the first page')):
    e(OC, IT[lab], 'FRAMEWORK', 'pager.setAdapter(...): the ViewPager instantiates the %s of the default tab order' % ev, guard='default tab order (preference tab_order not set)',
      evidence=FW_VIEWPAGER + '; SRC LibraryActivity.java:176-178; LibraryPagerAdapter.java:72-78, 241-246', cls='non_standard', via='androidx ViewPager calls the PagerAdapter')
TABS = [('MediaUtils.TYPE_ARTIST', None), ('MediaUtils.TYPE_ALBUM', None), ('MediaUtils.TYPE_SONG', None), ('MediaUtils.TYPE_PLAYLIST', None), ('MediaUtils.TYPE_GENRE', None), ('MediaUtils.TYPE_FILE', None),
        ('MediaUtils.TYPE_ALBARTIST', NEED_HIDDEN_TAB), ('MediaUtils.TYPE_COMPOSER', NEED_HIDDEN_TAB)]
TC = 'SlidingTabLayout$TabClickListener.onClick'
gui('S_LIBRARY', TC, 'Tap a tab title of the tab strip', evidence='SRC SlidingTabLayout.java:217, 311-320; ' + FW_VIEW_CLICK)
for lab, st in TABS:
    e(TC, IT[lab], 'FRAMEWORK', 'mViewPager.setCurrentItem(i): the ViewPager creates the page of the tapped tab (and its neighbours)', needs_state=st,
      guard='the tapped tab is of type %s' % lab.split('.')[1], evidence=FW_VIEWPAGER + '; SRC SlidingTabLayout.java:313-319', cls='non_standard', via='androidx ViewPager calls the PagerAdapter')
for cb in ('onPageScrolled', 'onPageSelected', 'onPageScrollStateChanged'):
    e(TC, 'SlidingTabLayout$InternalViewPagerListener.' + cb, 'FRAMEWORK', 'mViewPager.setCurrentItem(i): the ViewPager calls the page change listener (' + cb + ')',
      evidence=FW_VIEWPAGER + '; SRC SlidingTabLayout.java:158, 262-309', cls='non_standard', via='androidx ViewPager calls the OnPageChangeListener')
    e('SlidingTabLayout$InternalViewPagerListener.' + cb, LP + '.' + cb, 'CALL', 'the internal listener forwards to the listener registered with setOnPageChangeListener (the LibraryPagerAdapter)',
      guard='mViewPagerPageChangeListener != null: LibraryActivity.onCreate registers the LibraryPagerAdapter', evidence='SRC SlidingTabLayout.java:%d; LibraryActivity.java:192' % {'onPageScrolled': 281, 'onPageSelected': 305, 'onPageScrollStateChanged': 291}[cb])
e(TC, 'S_LIBRARY', 'ENTERS', 'the tab is selected and its list is shown', evidence='SRC SlidingTabLayout.java:313-319')
# the tab strip is filled from the adapter (typed PagerAdapter, so the scan sees no edge)
for cb in ('getCount', 'getPageTitle'):
    e('SlidingTabLayout.populateTabStrip', LP + '.' + cb, 'CALL', 'adapter.%s(...) on the ViewPager adapter (a LibraryPagerAdapter)' % cb, guard='the ViewPager adapter is the LibraryPagerAdapter set by LibraryActivity.onCreate',
      evidence='SRC SlidingTabLayout.java:%d; LibraryActivity.java:177' % {'getCount': 191, 'getPageTitle': 216}[cb])
e('SlidingTabLayout.setViewPager', 'SlidingTabLayout$InternalViewPagerListener.<init>', 'CALL', 'viewPager.setOnPageChangeListener(new InternalViewPagerListener())', evidence='SRC SlidingTabLayout.java:158 (bytecode)')
e('SlidingTabLayout.populateTabStrip', 'VanillaTabLayout.createDefaultTabView', 'CALL', 'createDefaultTabView(getContext()) (virtual call; the only SlidingTabLayout subclass the app ever instantiates is VanillaTabLayout, which overrides this method)',
  guard='mTabViewLayoutId == 0 (setCustomTabView was never called, so no custom tab layout id is set)', evidence='SRC SlidingTabLayout.java:187, 201-203 (bytecode: invokevirtual SlidingTabLayout.createDefaultTabView); VanillaTabLayout.java:44-54')
# view classes built from XML
for cls in ('VanillaTabLayout',):
    e(cls + '.<init>(Context,AttributeSet)', 'SlidingTabLayout.onAttachedToWindow', 'FRAMEWORK', 'the view is attached to the window', evidence=FW_VIEW_DRAW)
e('SlidingTabStrip.<init>(Context)', 'SlidingTabStrip.onDraw', 'FRAMEWORK', 'the strip is drawn', evidence=FW_VIEW_DRAW)
# BottomBarControls and SlidingView callbacks
e('SlidingView.<init>(Context,AttributeSet)', 'SlidingView.onLayout', 'FRAMEWORK', 'the sliding view is laid out', evidence=FW_VIEW_DRAW)
e('SlidingView.<init>(Context,AttributeSet)', 'SlidingView.onWindowVisibilityChanged', 'FRAMEWORK', 'the window visibility changes (the window is shown)',
  evidence='INFERRED View.dispatchWindowVisibilityChanged calls onWindowVisibilityChanged when the window becomes visible (View source line not read)')


# ---- C2. rows of the library lists: tap -> LibraryPagerAdapter.onItemClick (the header "play all" row exists in 5 of the 6 default tabs; rows need the scanned library)
NEED_PL_ROW = state_text('The Playlists tab is the visible library tab and a playlist exists (tap its title; Add to playlist > New playlist)', 'session', 'data')
NEED_FILES_ADAPTER = state_text('The Files tab page exists: FileSystemAdapter was created when the Files tab (or its neighbour) was brought into view', 'session')
NEED_EXPANDABLE_SONGROW = state_text('The Songs tab is the visible library tab and a song row is shown', 'session', 'data')
LA = 'LibraryActivity'
LPA_CLICK = 'LibraryPagerAdapter.onItemClick'
gui('S_LIBRARY', LPA_CLICK, 'Tap the play-all header row at the top of the list, or a row (song, album, artist, genre, playlist, folder or file)',
    evidence='SRC LibraryPagerAdapter.java:344, 893-903; ' + FW_ITEMCLICK)
sup(LA + '.onItemClicked', LA + '.onItemExpanded')
OIC = {v: LA + '.onItemClicked@' + v for v in ('HDR', 'EXP', 'EXPPL', 'PLAY')}
OIE = {v: LA + '.onItemExpanded@' + v for v in ('PL', 'MEDIA')}
call(OIC['EXP'], OIE['MEDIA'], 'onItemExpanded(rowData): the default action (expand or play all) expands a row that can be expanded', 'SRC LibraryActivity.java:469-471', guard='tryExpand && rowData has DATA_EXPANDABLE')
call(OIC['EXPPL'], OIE['PL'], 'onItemExpanded(rowData): the playlist row can be expanded', 'SRC LibraryActivity.java:469-471', guard='tryExpand && rowData has DATA_EXPANDABLE (playlist rows always)')
for v in ('HDR', 'PLAY'):
    call(OIC[v], LA + '.pickSongs', 'pickSongs(rowData, action): the row cannot be expanded (the header, a song, a file), so it is played', 'SRC LibraryActivity.java:472-482',
         guard='action != ACTION_DO_NOTHING and the row is not expandable (the play-all header, a song or a file)')
e(LA + '.onItemExpanded@PL', LA + '.editPlaylist', 'CALL', 'type == TYPE_PLAYLIST: editPlaylist(rowData)', guard='type == MediaUtils.TYPE_PLAYLIST', evidence='SRC LibraryActivity.java:493-495')
e(LA + '.onItemExpanded@MEDIA', LA + '.expand', 'CALL', 'type is not a playlist: expand(rowData)', guard='type != MediaUtils.TYPE_PLAYLIST', evidence='SRC LibraryActivity.java:493-497')
for v in OIC:
    e(LPA_CLICK, LA + '.onItemClicked', 'CALL', 'mActivity.onItemClicked(intent) for a row of a media tab', evidence='SRC LibraryPagerAdapter.java:901', guard='type != TYPE_FILE')
e(LPA_CLICK, OIC['HDR'], 'CALL', 'the play-all header row: onItemClicked(createHeaderIntent(view))', guard='id == LibraryAdapter.HEADER_ID: the intent has no DATA_EXPANDABLE extra, so the row is not expandable',
  evidence='SRC LibraryPagerAdapter.java:861-868, 895, 901')
e(LPA_CLICK, OIC['EXP'], 'CALL', 'a row of the Artists / Albums / Genres tab: onItemClicked(createData(view))', env=ENV_PERM, guard='type != TYPE_FILE; the row is expandable (an adapter whose target tab is visible: Artists and Albums by default)',
  evidence='SRC LibraryPagerAdapter.java:895, 901; MediaAdapter.java:596-605; LibraryPagerAdapter.java:263-280')
e(LPA_CLICK, OIC['EXPPL'], 'CALL', 'a row of the Playlists tab: onItemClicked(createData(view))', needs_state=NEED_PL_ROW, guard='type == TYPE_PLAYLIST; playlist rows are always expandable (MediaAdapter.java:229)',
  evidence='SRC LibraryPagerAdapter.java:895, 901; MediaAdapter.java:222-230')
e(LPA_CLICK, OIC['PLAY'], 'CALL', 'a row of the Songs tab: onItemClicked(createData(view))', env=ENV_PERM, needs_state=NEED_TAB_SONGS, guard='type == TYPE_SONG: song rows are never expandable',
  evidence='SRC LibraryPagerAdapter.java:895, 901; MediaAdapter.java:202-221, 596-605')
e(LPA_CLICK, 'FileSystemAdapter.onItemClicked', 'CALL', 'a row of the Files tab: mFilesAdapter.onItemClicked(intent)', needs_state=NEED_TAB_FILES, guard='type == TYPE_FILE', evidence='SRC LibraryPagerAdapter.java:895-899')
# FileSystemAdapter.onItemClicked: a folder is expanded, an image or text file is opened by another app, anything else is played
sup(('FileSystemAdapter.onItemClicked', LA + '.onItemExpanded'), ('FileSystemAdapter.onItemClicked', LA + '.onItemClicked'))
call('FileSystemAdapter.onItemClicked', OIE['MEDIA'], 'a folder row: mActivity.onItemExpanded(intent)', 'SRC FileSystemAdapter.java:448-449', guard='isFolder (DATA_EXPANDABLE) and the row was not dispatched to another app')
call('FileSystemAdapter.onItemClicked', OIC['PLAY'], 'a file row: mActivity.onItemClicked(intent)', 'SRC FileSystemAdapter.java:451', guard='not a folder, and not an image or text file that another app opened')
# arrow of a row (MediaAdapter is the OnClickListener of the dragger arrow)
gui('S_LIBRARY', 'MediaAdapter.onClick', 'Tap the arrow at the right end of an expandable row', evidence='SRC MediaAdapter.java:499, 610-617; DraggableRow.java:168-174; ' + FW_VIEW_CLICK)
sup(('MediaAdapter.onClick', LA + '.onItemExpanded'))
e('MediaAdapter.onClick', OIE['MEDIA'], 'CALL', 'mActivity.onItemExpanded(createData(parent)) for the arrow of a non-playlist row', env=ENV_PERM, guard='the row is of the Artists, Albums or Genres tab',
  evidence='SRC MediaAdapter.java:615-616')
e('MediaAdapter.onClick', OIE['PL'], 'CALL', 'mActivity.onItemExpanded(createData(parent)) for the arrow of a playlist row', needs_state=NEED_PL_ROW, guard='the row is of the Playlists tab',
  evidence='SRC MediaAdapter.java:615-616')
# expand: the limiter is set and the next tab is shown; the playlist editor is another activity
e(LA + '.expand', 'S_LIBRARY', 'ENTERS', 'the limiter is set and the library shows the next tab (Albums after Artists, Songs after Albums, Artists after Genres; the folder content in Files)', evidence='SRC LibraryActivity.java:435-445')
e(LA + '.expand', 'LibraryPagerAdapter.instantiateItem', 'FRAMEWORK', 'mViewPager.setCurrentItem(tab): the ViewPager shows the target tab (its page may be created)', guard='tab != -1 and tab != the current item',
  evidence=FW_VIEWPAGER + '; SRC LibraryActivity.java:441-444', cls='non_standard', via='androidx ViewPager calls the PagerAdapter')
for lab in ('MediaUtils.TYPE_ALBUM', 'MediaUtils.TYPE_SONG', 'MediaUtils.TYPE_ARTIST', 'MediaUtils.TYPE_FILE'):
    e(LA + '.expand', IT[lab], 'FRAMEWORK', 'mViewPager.setCurrentItem(tab): the target page of the expansion is built', guard='the target tab (Albums for an artist, Songs for an album, Artists for a genre, Files for a folder) is visible',
      evidence=FW_VIEWPAGER + '; SRC LibraryActivity.java:440-444', cls='non_standard', via='androidx ViewPager calls the PagerAdapter')
e(LA + '.editPlaylist', 'PlaylistActivity.<init>', 'INTENT', 'startActivity(new Intent(this, PlaylistActivity.class)) with the playlist id and title', evidence='SRC LibraryActivity.java:732-737; AndroidManifest.xml:91-93; ' + FW_ACT_CREATE)
# limiter breadcrumbs (ArrowedText views built by updateLimiterViews, clicks go to the activity)
e('ArrowedText.<init>', 'ArrowedText.onDraw', 'FRAMEWORK', 'the view system draws the limiter breadcrumb (added to mLimiterViews)', evidence=FW_VIEW_DRAW)


FW_SEEKBAR = ('FW-SRC core/java/android/widget/SeekBar.java:90-95, 112-115, 120-123 and core/java/android/widget/AbsSeekBar.java:796, 825 '
              '(onProgressRefresh calls OnSeekBarChangeListener.onProgressChanged; a touch gesture on the bar calls onStartTrackingTouch and onStopTrackingTouch)')
FW_DLG_BUTTON = ('FW-SRC core/java/com/android/internal/app/AlertController.java:125-147, 159-167 and core/java/android/app/Dialog.java:1350-1370 '
                 '(a tap on a dialog button sends the stored message; its handler calls the DialogInterface.OnClickListener registered with setPositiveButton / setNegativeButton, then the dialog is dismissed)')
FW_DLG_ITEM = ('FW-SRC core/java/com/android/internal/app/AlertController.java:1138-1145 '
               '(a tap on an item of setItems / setSingleChoiceItems calls the DialogInterface.OnClickListener)')
FW_DIALOGFRAG = ('FW-SRC core/java/android/app/DialogFragment.java:225-231, 406, 498-503 '
                 '(show adds the fragment in a transaction; the fragment lifecycle calls onGetLayoutInflater, which calls onCreateDialog, and onStart shows the dialog)')
FW_FASTSCROLL = ('FW-SRC core/java/android/widget/FastScroller.java:285, 954-974, 1000, 1119, 1288-1295 and core/java/android/widget/AbsListView.java:2169-2170, 6404-6418 '
                 '(a list with fastScrollEnabled asks an adapter that implements SectionIndexer for getSections when the list is laid out or its data changes, for getPositionForSection and '
                 'getSectionForPosition while the thumb is dragged, and uses section.toString() as preview text)')


def gui2(page, plain, variant, text, ev, **kw):
    """The gesture calls the method (plain node) and runs the branch of the variant node."""
    gui(page, plain, text, evidence=ev, **kw)
    gui(page, variant, text, evidence=ev, **kw)


# ---- C3. long-press on a row: CoordClickListener (registered per list; owners: library pager L, playlist activity P, queue fragment Q) -> FancyMenu bottom sheet
CCL = 'CoordClickListener.onItemLongClick'
sup(CCL, 'FancyMenu$1.onItemClick', ('LibraryActivity.onCreateFancyMenu', 'FancyMenu.show'), ('FileSystemAdapter.onCreateFancyMenu', LA + '.onCreateFancyMenu'))
for own, tgt in (('L', 'LibraryPagerAdapter.onItemLongClickWithCoords'), ('P', 'PlaylistActivity.onItemLongClickWithCoords'), ('Q', 'ShowQueueFragment.onItemLongClickWithCoords')):
    call(CCL + '@' + own, tgt, 'mCallback.onItemLongClickWithCoords(...) with the callback of this list', 'SRC CoordClickListener.java:60-62, 79',
         guard='the listener was created with the owner of this list (%s)' % {'L': 'LibraryPagerAdapter.instantiateItem:341', 'P': 'PlaylistActivity.onCreate:113', 'Q': 'ShowQueueFragment.onCreateView:63'}[own])
gui2('S_LIBRARY', CCL, CCL + '@L', 'Long-press the play-all header row or a row of the list', 'SRC LibraryPagerAdapter.java:341-343; CoordClickListener.java:69-72, 77-80; ' + FW_ITEMCLICK)
gui('S_LIBRARY', 'CoordClickListener.onTouch', 'Touch the list (the listener only records the touch position)', evidence='SRC CoordClickListener.java:71, 85-91; ' + FW_VIEW_CLICK)
LPA_LONG = 'LibraryPagerAdapter.onItemLongClickWithCoords'
sup((LPA_LONG, 'FileSystemAdapter.onCreateFancyMenu'), (LPA_LONG, LA + '.onCreateFancyMenu'))
e(LPA_LONG, LA + '.onCreateFancyMenu', 'CALL', 'mActivity.onCreateFancyMenu(intent, view, x, y) for a row of a media tab or the play-all header', guard='type != TYPE_FILE', evidence='SRC LibraryPagerAdapter.java:890')
e(LPA_LONG, 'FileSystemAdapter.onCreateFancyMenu', 'CALL', 'mFilesAdapter.onCreateFancyMenu(intent, view, x, y) for a row of the Files tab', needs_state=NEED_TAB_FILES, guard='type == TYPE_FILE', evidence='SRC LibraryPagerAdapter.java:887-888')
e('FileSystemAdapter.onCreateFancyMenu', LA + '.onCreateFancyMenu', 'CALL', 'the row is not the ".." parent row: mActivity.onCreateFancyMenu(...)', guard='!isParentRow', evidence='SRC FileSystemAdapter.java:467-468')
FM_SHOW = {o: 'FancyMenu.show@' + o for o in 'LPQ'}
e(LA + '.onCreateFancyMenu', 'FancyMenu.show', 'CALL', 'fm.show(view, x, y)', evidence='SRC LibraryActivity.java:725 (bytecode)')
e(LA + '.onCreateFancyMenu', FM_SHOW['L'], 'CALL', 'fm.show(view, x, y): the bottom sheet of the library opens', evidence='SRC LibraryActivity.java:725 (bytecode)')
e(FM_SHOW['L'], 'S_FANCY_LIBRARY', 'ENTERS', 'the BottomSheetDialog with the menu rows is shown', evidence='SRC FancyMenu.java:169-190; ' + FW_DIALOGFRAG.split(' (')[0] + ' (see FancyMenu.Sheet: a BottomSheetDialog, shown by sheet.show())')
e('FancyMenu.show', 'FancyMenu$Adapter.getView', 'FRAMEWORK', 'list.setAdapter(adapter): the ListView of the sheet calls getView for each menu row', evidence='SRC FancyMenu.java:184-185, 211-226; ' + FW_GETVIEW)
for o in 'LPQ':
    e(FM_SHOW[o], 'FancyMenu$Adapter.getView', 'FRAMEWORK', 'list.setAdapter(adapter): the ListView of the sheet calls getView for each menu row', evidence='SRC FancyMenu.java:184-185, 211-226; ' + FW_GETVIEW)
# tap on an item of the sheet
FMC = 'FancyMenu$1.onItemClick'
gui2('S_FANCY_LIBRARY', FMC, FMC + '@L', 'Tap a row of the context menu', 'SRC FancyMenu.java:173-185; ' + FW_ITEMCLICK)
FIS = LA + '.onFancyItemSelected'
FIS_B = CS.branches('LibraryActivity.java', 'onFancyItemSelected')
FIS_N = {l: l.replace('CTX_MENU_', '') for l, a, b in FIS_B}
FIS_V = variants_of(FIS, 'LibraryActivity.java', 'onFancyItemSelected', bounds=FIS_B, names=FIS_N, text='call made in the menu item branch')
call(FMC + '@L', FIS, 'mCallback.onFancyItemSelected(item) with the callback of this menu (the LibraryActivity)', 'SRC FancyMenu.java:72-76, 178', guard='the menu was created by the LibraryActivity (FancyMenu(this, this))')
RS = 'a row of a media tab is selected in the context menu'
GATE_FIS = {
    'CTX_MENU_EXPAND': dict(env=ENV_PERM, guard='item "Expand": rowData has DATA_EXPANDABLE and the type is not a playlist'),
    'CTX_MENU_ENQUEUE': dict(env=ENV_PERM, guard='item "Enqueue" (rows only)'),
    'CTX_MENU_PLAY': dict(env=ENV_PERM, guard='item "Play" (rows only)'),
    'CTX_MENU_PLAY_ALL': dict(guard='item "Play all": the header row, or a row of type artist / album / song / file'),
    'CTX_MENU_ENQUEUE_ALL': dict(guard='item "Enqueue all": the header row only'),
    'CTX_MENU_ENQUEUE_AS_NEXT': dict(env=ENV_PERM, guard='item "Enqueue as next" (rows only)'),
    'CTX_MENU_RENAME_PLAYLIST': dict(needs_state=NEED_PL_ROW, guard='item "Rename": type == TYPE_PLAYLIST'),
    'CTX_MENU_DELETE': dict(env=ENV_PERM, guard='item "Delete" (rows only)'),
    'CTX_MENU_OPEN_EXTERNAL': dict(needs_state=NEED_TAB_FILES, guard='item "Open": FileUtils.canDispatchIntent (an image or text file of the Files tab)'),
    'CTX_MENU_SHOW_DETAILS': dict(needs_state=NEED_EXPANDABLE_SONGROW, env=ENV_PERM, guard='item "Details": type == TYPE_SONG'),
    'CTX_MENU_PLUGINS': dict(needs_state=NEED_EXPANDABLE_SONGROW, env=ENV_PLUGIN, guard='item "Plugins": type == TYPE_SONG and PluginUtils.checkPlugins'),
    'CTX_MENU_MORE_FROM_ARTIST': dict(needs_state=NEED_TAB_ALBUMS, env=ENV_PERM, guard='item "More from artist": type == TYPE_SONG or TYPE_ALBUM'),
    'CTX_MENU_MORE_FROM_ALBUM': dict(needs_state=NEED_EXPANDABLE_SONGROW, env=ENV_PERM, guard='item "More from album": type == TYPE_SONG'),
    'CTX_MENU_ADD_TO_PLAYLIST': dict(guard='item "Add to playlist": always present (also on the header row)'),
    'CTX_MENU_ADD_TO_HOMESCREEN': dict(env=ENV_PERM, guard='item "Add to home screen": every row except Files tab rows'),
}
for lab, var in FIS_V.items():
    g = GATE_FIS.get(lab)
    if g is None:
        continue          # CTX_MENU_NOOP (id -1) and the default branch are never selected: see UNREACHABLE reasons
    e(FMC + '@L', var, 'CALL', 'item %s of the context menu was tapped' % FIS_N[lab], evidence='SRC LibraryActivity.java:743-845; FancyMenu.java:176-178', **g)
for lab in ('CTX_MENU_EXPAND', 'CTX_MENU_ENQUEUE', 'CTX_MENU_PLAY', 'CTX_MENU_PLAY_ALL', 'CTX_MENU_ENQUEUE_ALL', 'CTX_MENU_ENQUEUE_AS_NEXT', 'CTX_MENU_MORE_FROM_ARTIST', 'CTX_MENU_MORE_FROM_ALBUM',
            'CTX_MENU_OPEN_EXTERNAL', 'CTX_MENU_ADD_TO_HOMESCREEN'):
    e(FIS_V[lab], 'S_LIBRARY', 'ENTERS', 'the sheet closes and the library is shown (sheet.dismiss())', evidence='SRC FancyMenu.java:180')
e(FIS_V['CTX_MENU_DELETE'], 'S_DLG_DELETE_MEDIA', 'ENTERS', 'the confirm dialog "Delete" is shown', evidence='SRC LibraryActivity.java:781-797; ' + FW_DLG_BUTTON.split(' (')[0])

FW_SEARCHVIEW = ('FW-SRC core/java/android/widget/SearchView.java:500, 1249-1250, 1258-1259 '
                 '(setOnQueryTextListener stores the listener; typing calls onQueryTextChange and the submit action calls onQueryTextSubmit)')
FW_POPUPMENU = ('FW-SRC core/java/android/widget/PopupMenu.java:101-105, 226-227 '
                '(PopupMenu.show opens the popup; a selected item reaches the MenuBuilder.Callback, which calls mMenuItemClickListener.onMenuItemClick)')
FW_TEXTWATCHER = ('FW-SRC core/java/android/widget/TextView.java:5294-5296, 5397-5403, 9309-9314, 9359-9366, 9375-9382 '
                  '(setText and typing call sendBeforeTextChanged, sendOnTextChanged and sendAfterTextChanged, which call every TextWatcher added with addTextChangedListener)')
SCREENS.update({
    'S_DLG_PLAYLIST': 'Dialog "Add to playlist": list with "New playlist..." and the existing playlists (PlaylistDialog)',
    'S_DLG_PLAYLIST_INPUT': 'Dialog "Choose playlist name" (PlaylistInputDialog); variant RENAME renames a playlist (positive button "Rename"), variant CREATE makes a new playlist (positive button "Create")',
    'S_DLG_TRACK_DETAILS': 'Dialog with the tag details of a song (TrackDetailsDialog)',
    'S_DLG_PLUGINS': 'Dialog that lists the installed Vanilla Music plugins',
    'S_DLG_JUMP_TO_TIME': 'Dialog "Jump to time" with hours, minutes and seconds fields (JumpToTimeDialog)',
    'S_PLAYLIST': 'PlaylistActivity: songs of one playlist with the Edit and Delete buttons',
    'S_PLAYLIST_EDIT': 'PlaylistActivity in edit mode: drag handles shown, rows can be moved and removed',
    'S_DLG_PLAYLIST_DELETE': 'Dialog "Delete playlist" (confirm)',
    'S_FANCY_PLAYLIST': 'Bottom sheet context menu (FancyMenu) of a row of the playlist activity',
    'S_FANCY_QUEUE': 'Bottom sheet context menu (FancyMenu) of a row of the queue list',
})

# ---- C4. dialogs opened from the library context menu
OIS = LA + '.onFancyItemSelected@'
e(FIS_V['CTX_MENU_RENAME_PLAYLIST'], 'PlaylistInputDialog.onCreateDialog', 'FRAMEWORK', 'dialog.show(getFragmentManager(), ...): the fragment builds its dialog', evidence='SRC LibraryActivity.java:778; ' + FW_DIALOGFRAG)
e(FIS_V['CTX_MENU_RENAME_PLAYLIST'], 'PlaylistInputDialog.onStart', 'FRAMEWORK', 'the fragment is started: the dialog is shown', evidence='SRC LibraryActivity.java:778; PlaylistInputDialog.java:107-113; ' + FW_FRAG_LIFE)
e(FIS_V['CTX_MENU_RENAME_PLAYLIST'], 'S_DLG_PLAYLIST_INPUT@RENAME', 'ENTERS', 'the rename dialog is shown', evidence='SRC LibraryActivity.java:768-780')
e(FIS_V['CTX_MENU_ADD_TO_PLAYLIST'], 'PlaylistDialog.onCreateDialog', 'FRAMEWORK', 'plDialog.show(getFragmentManager(), "PlaylistDialog"): the fragment builds its dialog', evidence='SRC LibraryActivity.java:834-835; ' + FW_DIALOGFRAG)
e(FIS_V['CTX_MENU_ADD_TO_PLAYLIST'], 'S_DLG_PLAYLIST', 'ENTERS', 'the playlist chooser dialog is shown', evidence='SRC LibraryActivity.java:827-837')
e(FIS_V['CTX_MENU_SHOW_DETAILS'], 'TrackDetailsDialog.onCreate', 'FRAMEWORK', 'TrackDetailsDialog.show(getFragmentManager(), songId): the fragment starts', evidence='SRC LibraryActivity.java:802-806; TrackDetailsDialog.java:63-73; ' + FW_DIALOGFRAG)
e(FIS_V['CTX_MENU_SHOW_DETAILS'], 'TrackDetailsDialog.onCreateView', 'FRAMEWORK', 'the fragment builds its view (the dialog window shows it)', evidence='SRC TrackDetailsDialog.java:75-117; ' + FW_FRAG_LIFE)
e(FIS_V['CTX_MENU_SHOW_DETAILS'], 'S_DLG_TRACK_DETAILS', 'ENTERS', 'the details dialog is shown', evidence='SRC LibraryActivity.java:802-806')
e(FIS_V['CTX_MENU_PLUGINS'], 'S_DLG_PLUGINS', 'ENTERS', 'the plugin list dialog is shown (AlertDialog with setItems)', evidence='SRC PlaybackActivity.java:708-735')
e(FIS_V['CTX_MENU_PLUGINS'], 'PlaybackActivity$4.<init>', 'CALL', 'new DialogInterface.OnClickListener for the plugin items', evidence='SRC PlaybackActivity.java:713 (bytecode)')
e(FIS_V['CTX_MENU_ADD_TO_HOMESCREEN'], 'S_ENTRY', 'ENTERS', 'the launcher asks the user to pin the shortcut (ShortcutManager.requestPinShortcut) and later starts it', env=ENV_SHORTCUT,
  evidence='SRC SystemUtils.java:63-64, 80-93')
# the dialogs of the library context menu
gui('S_DLG_DELETE_MEDIA', LA + '$3.onClick', 'Tap "Delete" in the confirm dialog', evidence='SRC LibraryActivity.java:787-791; ' + FW_DLG_BUTTON)
gui('S_DLG_DELETE_MEDIA', LA + '$4.onClick', 'Tap "Cancel" in the confirm dialog', evidence='SRC LibraryActivity.java:792-795; ' + FW_DLG_BUTTON)
e(LA + '$3.onClick', 'S_LIBRARY', 'ENTERS', 'the dialog closes after the positive button', evidence='SRC LibraryActivity.java:787-791; ' + FW_DLG_BUTTON.split(' (')[0])
e(LA + '$4.onClick', 'S_LIBRARY', 'ENTERS', 'the dialog closes after the negative button', evidence='SRC LibraryActivity.java:792-795; ' + FW_DLG_BUTTON.split(' (')[0])
# LibraryActivity$2.onSuccess is the PlaylistInputDialog callback for a rename
gui('S_DLG_PLAYLIST_INPUT@RENAME', 'PlaylistInputDialog.onClick', 'Tap "Rename" in the dialog (the name must differ from the old one)', evidence='SRC PlaylistInputDialog.java:93-98, 143-156; ' + FW_DLG_BUTTON)
gui('S_DLG_PLAYLIST_INPUT@CREATE', 'PlaylistInputDialog.onClick', 'Tap "Create" (or "Overwrite") in the dialog, or Cancel', evidence='SRC PlaylistInputDialog.java:93-98, 143-156; ' + FW_DLG_BUTTON)
for pg in ('S_DLG_PLAYLIST_INPUT@RENAME', 'S_DLG_PLAYLIST_INPUT@CREATE'):
    for cb in ('onTextChanged', 'beforeTextChanged', 'afterTextChanged'):
        gui(pg, 'PlaylistInputDialog.' + cb, 'Type in the name field', evidence='SRC PlaylistInputDialog.java:91, 118-141; ' + FW_TEXTWATCHER)
sup(('PlaylistInputDialog.onClick', LA + '$2.onSuccess'), ('PlaylistInputDialog.onClick', 'PlaylistDialog$1.onSuccess'))
call('PlaylistInputDialog.onClick', LA + '$2.onSuccess', 'mCallback.onSuccess(text) for the rename dialog of the library', 'SRC PlaylistInputDialog.java:150; LibraryActivity.java:771-777',
     guard='positive button and the callback is the one given by LibraryActivity (rename)', needs_state=state_text('The rename dialog of a playlist is open (context menu of a playlist row > Rename)', 'session'))
call('PlaylistInputDialog.onClick', 'PlaylistDialog$1.onSuccess', 'mCallback.onSuccess(text) for the new-playlist dialog of PlaylistDialog', 'SRC PlaylistInputDialog.java:150; PlaylistDialog.java:156-163',
     guard='positive button and the callback is the one given by PlaylistDialog (new playlist)', needs_state=state_text('The new-playlist dialog is open (Add to playlist > New playlist...)', 'session'))
for pg in ('S_DLG_PLAYLIST_INPUT@RENAME', 'S_DLG_PLAYLIST_INPUT@CREATE'):
    e('PlaylistInputDialog.onClick', 'S_LIBRARY' if pg.endswith('RENAME') else 'S_LIBRARY', 'ENTERS', 'the dialog is dismissed (dialog.dismiss())', evidence='SRC PlaylistInputDialog.java:155')
# PlaylistDialog (add to playlist): chooser
e('PlaylistDialog.onCreateDialog', 'PlaylistDialog.onClick', 'REGISTER', 'builder.setItems(displayItem, this)', evidence='SRC PlaylistDialog.java:147-148 (bytecode)')
gui('S_DLG_PLAYLIST', 'PlaylistDialog.onClick', 'Tap an entry of the list ("New playlist..." or an existing playlist)', evidence='SRC PlaylistDialog.java:146-149, 152-172; ' + FW_DLG_ITEM)
sup(('PlaylistDialog.onClick', 'PlaylistInputDialog.newInstance'), ('PlaylistDialog.onClick', 'PlaylistDialog$1.<init>'), ('PlaylistDialog.onClick', 'SlidingPlaybackActivity.updatePlaylistFromPlaylistDialog'))
e('PlaylistDialog.onClick', 'PlaylistDialog$1.<init>', 'CALL', 'new PlaylistInputDialog.Callback() for "New playlist..."', guard='which == BUTTON_CREATE_PLAYLIST (index 0)', evidence='SRC PlaylistDialog.java:155-163 (bytecode)')
e('PlaylistDialog.onClick', 'PlaylistInputDialog.newInstance', 'CALL', 'PlaylistInputDialog.newInstance(callback, "", R.string.create)', guard='which == BUTTON_CREATE_PLAYLIST (index 0)', evidence='SRC PlaylistDialog.java:156-163 (bytecode)')
e('PlaylistDialog.onClick', 'PlaylistInputDialog.onCreateDialog', 'FRAMEWORK', 'newDialog.show(getFragmentManager(), ...): the fragment builds its dialog', guard='which == BUTTON_CREATE_PLAYLIST', evidence='SRC PlaylistDialog.java:164; ' + FW_DIALOGFRAG)
e('PlaylistDialog.onClick', 'PlaylistInputDialog.onStart', 'FRAMEWORK', 'the fragment is started: the dialog is shown', guard='which == BUTTON_CREATE_PLAYLIST', evidence='SRC PlaylistDialog.java:164; ' + FW_FRAG_LIFE)
e('PlaylistDialog.onClick', 'S_DLG_PLAYLIST_INPUT@CREATE', 'ENTERS', 'the new-playlist name dialog is shown', guard='which == BUTTON_CREATE_PLAYLIST', evidence='SRC PlaylistDialog.java:155-165')
e('PlaylistDialog.onClick', 'S_LIBRARY', 'ENTERS', 'an existing playlist was picked: the dialog closes and the songs are added', guard='which != BUTTON_CREATE_PLAYLIST', evidence='SRC PlaylistDialog.java:166-171')
e('PlaylistDialog.onClick', 'SlidingPlaybackActivity.updatePlaylistFromPlaylistDialog', 'CALL', 'mCallback.updatePlaylistFromPlaylistDialog(mData) for an existing playlist', guard='which != BUTTON_CREATE_PLAYLIST; needs a playlist in the list',
  needs_state=NEED_PLAYLIST, evidence='SRC PlaylistDialog.java:166-169')
e('PlaylistDialog$1.onSuccess', 'SlidingPlaybackActivity.updatePlaylistFromPlaylistDialog', 'CALL', 'mCallback.updatePlaylistFromPlaylistDialog(mData) after the name was typed', evidence='SRC PlaylistDialog.java:158-162 (bytecode)')
# delete from the dialog and the other plugin/dialog callbacks
gui('S_DLG_PLUGINS', 'PlaybackActivity$4.onClick', 'Tap a plugin in the list', evidence='SRC PlaybackActivity.java:712-733; ' + FW_DLG_ITEM)
e('PlaybackActivity$4.onClick', 'S_ENTRY', 'ENTERS', 'the plugin app is started with ACTION_LAUNCH_PLUGIN', env=ENV_PLUGIN, guard='the plugin activity resolves (request.resolveActivity != null)', evidence='SRC PlaybackActivity.java:726-728')
# the track details dialog works on a background thread and posts the result to the UI thread
e('TrackDetailsDialog.onCreateView', 'TrackDetailsDialog$1.run', 'ASYNC', 'handler.post(new Runnable(){...}) on the HandlerThread of the dialog', evidence='SRC TrackDetailsDialog.java:89-114; ' + FW_HANDLER)
e('TrackDetailsDialog$1.run', 'TrackDetailsDialog$1$1.run', 'ASYNC', 'getActivity().runOnUiThread(...) fills the text views', evidence='SRC TrackDetailsDialog.java:99-112; ' + FW_RUNUI)
e('TrackDetailsDialog.onCreate', 'TrackDetailsDialog.onDestroy', 'LIFECYCLE', 'the dialog fragment is destroyed when it is dismissed', evidence='SRC TrackDetailsDialog.java:119-123; ' + FW_FRAG_LIFE.split(' (')[0] + ' (moveToState calls performDestroy)')


# ---- C5. bottom bar: overflow menu, search icon, tap on the bar; sliding panel; keys
NEED_SERVICE_UP = state_text('The PlaybackService instance exists (an earlier activity start in this process created it)', 'session')
BBC = 'BottomBarControls.onClick'
BB_B = CS.branches('BottomBarControls.java', 'onClick')
BB_V = variants_of(BBC, 'BottomBarControls.java', 'onClick', bounds=BB_B, names={BB_B[0][0]: 'POPUP', BB_B[1][0]: 'MENUITEM', BB_B[2][0]: 'CONTENT'}, text='call made in the click branch')
gui2('S_LIBRARY', BBC, BB_V[BB_B[0][0]], 'Tap the overflow (three dots) button at the right end of the bottom bar', 'SRC BottomBarControls.java:157-181, 106-111; ' + FW_VIEW_CLICK)
gui2('S_LIBRARY', BBC, BB_V[BB_B[1][0]], 'Tap the search (magnifier) icon of the bottom bar', 'SRC BottomBarControls.java:165-174, 106-112; LibraryActivity.java:856; ' + FW_VIEW_CLICK)
gui2('S_LIBRARY', BBC, BB_V[BB_B[2][0]], 'Tap the bottom bar (current song)', 'SRC BottomBarControls.java:135-138, 113-116; ' + FW_VIEW_CLICK)
sup((BBC, 'BottomBarControls.openMenu'))
e('BottomBarControls.openMenu', 'S_LIBRARY_MENU', 'ENTERS', 'mPopupMenu.show(): the overflow menu is open', evidence='SRC BottomBarControls.java:198-203; ' + FW_POPUPMENU)
e(BB_V[BB_B[0][0]], 'BottomBarControls.openMenu', 'CALL', 'openMenu()', evidence='SRC BottomBarControls.java:110 (bytecode)')
e(BB_V[BB_B[2][0]], LA + '.onClick(View)', 'CALL', 'mParentClickConsumer.onClick(this): the registered click consumer is the LibraryActivity', guard='mParentClickConsumer != null (LibraryActivity.onCreate calls setOnClickListener(this))',
  evidence='SRC BottomBarControls.java:113-116; LibraryActivity.java:183')
# LibraryActivity.onClick(View): the bar, a limiter breadcrumb, or one of the control buttons (super)
OC_B = CS.branches('LibraryActivity.java', 'onClick', params='View')
OC_V = variants_of(LA + '.onClick(View)', 'LibraryActivity.java', 'onClick', params='View', bounds=OC_B, names={OC_B[0][0]: 'BAR', OC_B[1][0]: 'LIMITER', OC_B[2][0]: 'BUTTON'}, text='call made in the click branch')
e(BB_V[BB_B[2][0]], OC_V[OC_B[0][0]], 'CALL', 'the click comes from the bottom bar itself', guard='view == mBottomBarControls', evidence='SRC LibraryActivity.java:587-589')
gui2('S_LIBRARY', LA + '.onClick(View)', OC_V[OC_B[1][0]], 'Tap a limiter breadcrumb above the bottom bar', 'SRC LibraryActivity.java:545, 551, 589-608; ' + FW_VIEW_CLICK, needs_state=NEED_LIMITER)
for pg in ('S_SLIDE_LIBRARY', 'S_SLIDE_LIBRARY_QUEUE'):
    gui2(pg, LA + '.onClick(View)', OC_V[OC_B[2][0]], 'Tap one of the control buttons (previous, play / pause, next, shuffle, repeat)', 'SRC PlaybackActivity.java:317-331; LibraryActivity.java:609-611; ' + FW_VIEW_CLICK)
e(OC_V[OC_B[1][0]], 'S_LIBRARY', 'ENTERS', 'the limiter was changed or removed and the breadcrumbs are rebuilt', evidence='SRC LibraryActivity.java:593-608')
e(LA + '.openPlaybackActivity', 'FullPlaybackActivity.<init>', 'INTENT', 'startActivity(new Intent(this, FullPlaybackActivity.class))', evidence='SRC LibraryActivity.java:451-456; AndroidManifest.xml:70-72; ' + FW_ACT_CREATE)


# ---- C6. overflow menu items (Library, Sliding and Playback levels of onOptionsItemSelected)
OOI = LA + '.onOptionsItemSelected'
OOI_B = CS.branches('LibraryActivity.java', 'onOptionsItemSelected')
OOI_V = variants_of(OOI, 'LibraryActivity.java', 'onOptionsItemSelected', bounds=OOI_B, names={l: l.replace('MENU_', '') for l, a, b in OOI_B}, skip=('default',), text='call made in the menu item branch')
SOI = 'SlidingPlaybackActivity.onOptionsItemSelected'
SOI_B = CS.branches('SlidingPlaybackActivity.java', 'onOptionsItemSelected')
SOI_V = variants_of(SOI, 'SlidingPlaybackActivity.java', 'onOptionsItemSelected', bounds=SOI_B, names={l: l.replace('MENU_', '') for l, a, b in SOI_B}, skip=('default',), text='call made in the menu item branch')
POI = 'PlaybackActivity.onOptionsItemSelected'
POI_B = CS.branches('PlaybackActivity.java', 'onOptionsItemSelected')
POI_V = variants_of(POI, 'PlaybackActivity.java', 'onOptionsItemSelected', bounds=POI_B, names={l: l.replace('MENU_', '') for l, a, b in POI_B}, skip=('default',), text='call made in the menu item branch')
OMI = 'BottomBarControls.onMenuItemClick'
gui('S_LIBRARY_MENU', OMI, 'Tap an entry of the overflow menu', evidence='SRC BottomBarControls.java:157-158, 120-123; ' + FW_POPUPMENU)
e(OMI, OOI, 'CALL', 'mParentMenuConsumer.onOptionsItemSelected(item) calls the owner LibraryActivity override', evidence='SRC BottomBarControls.java:122; LibraryActivity.java:185')
call(OOI, SOI, 'default branch: super.onOptionsItemSelected(item)', 'SRC LibraryActivity.java:913-914 (bytecode)', guard='the item is not one of the library items')
call(SOI, POI, 'default branch: super.onOptionsItemSelected(item)', 'SRC SlidingPlaybackActivity.java:155-156 (bytecode)', guard='the item is not one of the queue items')
LIB_ITEMS = {'MENU_PLAYBACK': dict(), 'MENU_GO_HOME': dict(needs_state=NEED_TAB_FILES), 'MENU_SORT': dict()}
for lab, g in LIB_ITEMS.items():
    e(OMI, OOI_V[lab], 'CALL', 'the item %s of the overflow menu was tapped' % lab, guard='item id == %s' % lab, evidence='SRC LibraryActivity.java:855-858, 874-917', **g)
e(BB_V[BB_B[1][0]], OOI, 'CALL', 'mParentMenuConsumer.onOptionsItemSelected(tag) calls the owner LibraryActivity override', evidence='SRC BottomBarControls.java:112; LibraryActivity.java:185')
e(BB_V[BB_B[1][0]], OOI_V['MENU_SEARCH'], 'CALL', 'the search icon was tapped (menu item MENU_SEARCH, hidden in the popup, shown as an icon)', guard='item id == MENU_SEARCH', evidence='SRC LibraryActivity.java:856, 877-879')
SLIDE_ITEMS = {'MENU_SHOW_QUEUE': dict(), 'MENU_HIDE_QUEUE': dict(needs_state=NEED_SLIDE_QUEUE), 'MENU_SAVE_QUEUE': dict(needs_state=NEED_SLIDE), 'MENU_JUMP_TO_TIME': dict()}
for lab, g in SLIDE_ITEMS.items():
    e(OMI, SOI_V[lab], 'CALL', 'the item %s of the overflow menu was tapped' % lab, guard='item id == %s' % lab, evidence='SRC SlidingPlaybackActivity.java:126-131, 140-159', **g)
PB_ITEMS = {'MENU_PREFS': dict(), 'MENU_CLEAR_QUEUE': dict(needs_state=NEED_SLIDE), 'MENU_EMPTY_QUEUE': dict(needs_state=NEED_SLIDE)}
for lab, g in PB_ITEMS.items():
    e(OMI, POI_V[lab], 'CALL', 'the item %s of the overflow menu was tapped' % lab, guard='item id == %s' % lab, evidence='SRC PlaybackActivity.java:403, 408-424; SlidingPlaybackActivity.java:126-131', **g)
# where the items lead
e(OOI_V['MENU_SEARCH'], 'S_LIBRARY_SEARCH', 'ENTERS', 'the search field is open', evidence='SRC LibraryActivity.java:877-879; BottomBarControls.java:211-221')
e(OOI_V['MENU_GO_HOME'], 'S_LIBRARY', 'ENTERS', 'the Files tab shows the home folder', evidence='SRC LibraryActivity.java:883-886')
e(OOI_V['MENU_SORT'], 'S_DLG_SORT', 'ENTERS', 'the sort dialog is shown (AlertDialog.show())', evidence='SRC LibraryActivity.java:887-911')
e(SOI_V['MENU_SHOW_QUEUE'], 'S_SLIDE_LIBRARY_QUEUE', 'ENTERS', 'the sliding panel expands over the library: the queue is shown', evidence='SRC SlidingPlaybackActivity.java:142-144; SlidingView.java:146-148')
e(SOI_V['MENU_HIDE_QUEUE'], 'S_LIBRARY', 'ENTERS', 'the panel is minimized', evidence='SRC SlidingPlaybackActivity.java:145-147; SlidingView.java:153-156')
e(SOI_V['MENU_SAVE_QUEUE'], 'S_DLG_PLAYLIST', 'ENTERS', 'the playlist chooser dialog is shown (PlaylistDialog.newInstance(this, null, null).show(...))', evidence='SRC SlidingPlaybackActivity.java:148-151')
e(SOI_V['MENU_SAVE_QUEUE'], 'PlaylistDialog.onCreateDialog', 'FRAMEWORK', 'dialog.show(getFragmentManager(), "PlaylistDialog"): the fragment builds its dialog', evidence='SRC SlidingPlaybackActivity.java:150; ' + FW_DIALOGFRAG)
e(SOI_V['MENU_JUMP_TO_TIME'], 'JumpToTimeDialog.onCreateDialog', 'FRAMEWORK', 'JumpToTimeDialog.show(getFragmentManager()): the fragment builds its dialog', evidence='SRC SlidingPlaybackActivity.java:152-154; JumpToTimeDialog.java:60-62; ' + FW_DIALOGFRAG)
e(SOI_V['MENU_JUMP_TO_TIME'], 'S_DLG_JUMP_TO_TIME', 'ENTERS', 'the jump-to-time dialog is shown', evidence='SRC SlidingPlaybackActivity.java:152-154')
for _cb in ('beforeTextChanged', 'onTextChanged', 'afterTextChanged'):
    e('JumpToTimeDialog.onCreateDialog', 'JumpToTimeDialog$1.' + _cb, 'FRAMEWORK', 'editText.addTextChangedListener(textWatcher): edit the hours/minutes/seconds field', gui=['Type in the hours, minutes or seconds field'],
      evidence=FW_TEXTWATCHER + '; SRC JumpToTimeDialog.java:66-92')
gui('S_DLG_JUMP_TO_TIME', 'JumpToTimeDialog.onClick', 'Tap OK', evidence=FW_DLG_BUTTON + '; SRC JumpToTimeDialog.java:95-109, 106-116')
e(POI_V['MENU_PREFS'], 'PreferencesActivity.<init>', 'INTENT', 'startActivity(new Intent(this, PreferencesActivity.class))', evidence='SRC PlaybackActivity.java:412; AndroidManifest.xml:188-189; ' + FW_ACT_CREATE)
e(POI_V['MENU_CLEAR_QUEUE'], 'S_SLIDE_LIBRARY', 'ENTERS', 'the queue after the current song was dropped; the panel stays pulled up', evidence='SRC PlaybackActivity.java:414-416')
e(POI_V['MENU_EMPTY_QUEUE'], 'S_SLIDE_LIBRARY', 'ENTERS', 'the queue was emptied; the panel stays pulled up', evidence='SRC PlaybackActivity.java:417-419')
e(OOI_V['MENU_PLAYBACK'], 'FullPlaybackActivity.<init>', 'INTENT', 'openPlaybackActivity() opens the playback screen', evidence='SRC LibraryActivity.java:880-882, 451-456; ' + FW_ACT_CREATE)
# the sort dialog: choose a mode (single choice list, the button "Done" only closes)
e(OOI_V['MENU_SORT'], LA + '.onClick(DialogInterface,int)', 'REGISTER', 'builder.setSingleChoiceItems(items, mode, this)', evidence='SRC LibraryActivity.java:902-904 (bytecode)')
gui('S_DLG_SORT', LA + '.onClick(DialogInterface,int)', 'Tap a sort mode in the list', evidence='SRC LibraryActivity.java:902-910, 1002-1006; ' + FW_DLG_ITEM)
gui('S_DLG_SORT', LA + '.onDismiss', 'Tap "Done" or Back: the dialog is dismissed and the sort mode is applied', evidence='SRC LibraryActivity.java:905-909, 1008-1020; FW-SRC core/java/android/app/Dialog.java:1350-1362 (a dismissed dialog sends the dismiss message to the OnDismissListener)')
e(LA + '.onClick(DialogInterface,int)', LA + '.onDismiss', 'FRAMEWORK', 'dialog.dismiss() sends the dismiss message to the OnDismissListener set with setOnDismissListener(this)',
  evidence='SRC LibraryActivity.java:1005, 909; FW-SRC core/java/android/app/Dialog.java:1350-1362 (the ListenersHandler calls OnDismissListener.onDismiss)')
e(LA + '.onDismiss', 'S_LIBRARY', 'ENTERS', 'the list is shown in the chosen order', evidence='SRC LibraryActivity.java:1008-1020')
# search
for cb in ('onQueryTextChange', 'onQueryTextSubmit'):
    gui('S_LIBRARY_SEARCH', LA + '.' + cb, 'Type in the search field' if cb == 'onQueryTextChange' else 'Submit the search (keyboard search key)', evidence='SRC LibraryActivity.java:184, 922-935; ' + FW_SEARCHVIEW)
    e(LA + '.' + cb, 'S_LIBRARY_SEARCH', 'ENTERS', 'the lists are filtered; the search field stays open', evidence='SRC LibraryActivity.java:923-926')
e('BottomBarControls.showSearch', 'S_LIBRARY', 'ENTERS', 'setVisibility(GONE): the search field closes', needs_state=NEED_SEARCH, guard='visible == false and the field was visible', evidence='SRC BottomBarControls.java:211-221')


# ---- C7. keys of the library
KU = LA + '.onKeyUp'
KU_BOUNDS = [('BACK_SLIDE', 296, 299), ('BACK_SEARCH', 301, 303), ('BACK_LIMITER', 305, 328), ('BACK_EXIT', 329, 331), ('MENU', 333, 336), ('SEARCH', 337, 339)]
KU_V = variants_of(KU, 'LibraryActivity.java', 'onKeyUp', bounds=KU_BOUNDS, text='call made in the key branch')
gui('S_LIBRARY', KU, 'Press Back, Menu or Search (hardware or on-screen key)', evidence='SRC LibraryActivity.java:289-345; ' + FW_ACT_KEY)
gui('S_LIBRARY_SEARCH', KU, 'Press Back (closes the search field)', evidence='SRC LibraryActivity.java:289-345; ' + FW_ACT_KEY)
for pg in ('S_SLIDE_LIBRARY', 'S_SLIDE_LIBRARY_QUEUE'):
    gui(pg, KU, 'Press Back (pushes the sliding panel down)', evidence='SRC LibraryActivity.java:289-345; ' + FW_ACT_KEY)
for lab, g, pg in (('BACK_SLIDE', dict(needs_state=NEED_SLIDE, guard='KEYCODE_BACK and mSlidingView.isShrinkable() (the panel is pulled up)'), 'S_LIBRARY'),
                   ('BACK_SEARCH', dict(needs_state=NEED_SEARCH, guard='KEYCODE_BACK, the panel is down and the search field was open (showSearch(false) returned true)'), 'S_LIBRARY'),
                   ('BACK_LIMITER', dict(needs_state=NEED_LIMITER, guard='KEYCODE_BACK, the panel is down, no search field, and the current tab has a limiter'), 'S_LIBRARY'),
                   ('BACK_EXIT', dict(guard='KEYCODE_BACK, the panel is down, no search field and no limiter: finish()'), 'S_EXIT'),
                   ('MENU', dict(guard='KEYCODE_MENU: the activity-default menu is swallowed and the overflow popup opens'), 'S_LIBRARY_MENU'),
                   ('SEARCH', dict(guard='KEYCODE_SEARCH: showSearch(true)'), 'S_LIBRARY_SEARCH')):
    e(KU, KU_V[lab], 'CALL', 'branch %s of onKeyUp' % lab, evidence='SRC LibraryActivity.java:%d-%d' % dict((a, (b, c)) for a, b, c in KU_BOUNDS)[lab], **g)
    e(KU_V[lab], pg, 'ENTERS', {'BACK_SLIDE': 'the panel slides down', 'BACK_SEARCH': 'the search field closes', 'BACK_LIMITER': 'the limiter is removed or the parent folder is shown',
                                'BACK_EXIT': 'the activity finishes and the task ends', 'MENU': 'the overflow popup opens', 'SEARCH': 'the search field opens'}[lab], evidence='SRC LibraryActivity.java:289-345')
KD = LA + '.onKeyDown'
for pg in ('S_LIBRARY', 'S_LIBRARY_SEARCH', 'S_SLIDE_LIBRARY', 'S_SLIDE_LIBRARY_QUEUE'):
    gui(pg, KD, 'Press a key (media keys are passed to MediaButtonReceiver, DEL is swallowed)', evidence='SRC LibraryActivity.java:347-360; ' + FW_ACT_KEY)
# ---- C8. the sliding panel (touch on the bottom bar or the control strip)
ST = 'SlidingView.onTouch'
ST_L, ST_F = ST + '@LIBRARY', ST + '@FULL'
gui2('S_LIBRARY', ST, ST_L, 'Swipe up on the bottom bar (the sliding panel follows the finger and snaps to a stage)', 'SRC SlidingView.java:235-251, 313-379; ' + FW_VIEW_CLICK)
for pg in ('S_SLIDE_LIBRARY', 'S_SLIDE_LIBRARY_QUEUE'):
    gui2(pg, ST, ST_L, 'Swipe on the bottom bar or on the control strip (the panel snaps to another stage)', 'SRC SlidingView.java:235-251, 313-379; ' + FW_VIEW_CLICK)
e(ST_L, 'S_SLIDE_LIBRARY', 'ENTERS', 'the panel snaps to the stage with the controls (ACTION_UP after a scroll)', guard='mDidScroll and the target stage shows the control buttons', evidence='SRC SlidingView.java:331-343')
e(ST_L, 'S_SLIDE_LIBRARY_QUEUE', 'ENTERS', 'the panel snaps to the last stage: the queue is shown', guard='mDidScroll and the target stage is the last one', evidence='SRC SlidingView.java:331-343')
e(ST_L, 'S_LIBRARY', 'ENTERS', 'the panel snaps back to the first stage', guard='mDidScroll and the target stage is 0', evidence='SRC SlidingView.java:331-343')
call(ST, 'SlidingView$GestureListener.onFling', 'mDetector.onTouchEvent(fakeEvent): the GestureDetector reports a fling', 'SRC SlidingView.java:122, 321; FW-SRC core/java/android/view/GestureDetector.java:490, 655 (onTouchEvent calls mListener.onFling when the velocity is high enough)',
     kind='FRAMEWORK', guard='the touch is a fling (velocity above the minimum fling velocity)')
for v in (ST_L, ST_F):
    call(v, 'SlidingView$GestureListener.onFling', 'mDetector.onTouchEvent(fakeEvent): the GestureDetector reports a fling', 'SRC SlidingView.java:122, 321; FW-SRC core/java/android/view/GestureDetector.java:490, 655 (onTouchEvent calls mListener.onFling when the velocity is high enough)',
         kind='FRAMEWORK', guard='the touch is a fling (velocity above the minimum fling velocity)')
e('SlidingView.setExpansionStage', 'SlidingView$AnimationListener.<init>', 'CALL', 'new AnimationListener() is set on the view animator', evidence='SRC SlidingView.java:209 (bytecode)')
e('SlidingView.setExpansionStage', 'SlidingView$AnimationListener.onAnimationEnd', 'FRAMEWORK', 'the ViewPropertyAnimator ends: onAnimationEnd is called', evidence='SRC SlidingView.java:205-210, 389-400; INFERRED ViewPropertyAnimator calls AnimatorListener.onAnimationEnd when the animation ends or is cancelled (animator source not read)')
e('SlidingView.setExpansionStage', 'SlidingView$AnimationListener.onAnimationCancel', 'FRAMEWORK', 'a running animation is replaced by a new one: onAnimationCancel is called', guard='setExpansionStage is called while an animation runs',
  evidence='SRC SlidingView.java:401-404; INFERRED ViewPropertyAnimator cancels the running animation when a new one starts and calls onAnimationCancel (animator source not read)')
# lifecycle edges of the library page
e('S_LIBRARY', impl('LibraryActivity', 'onPause'), 'SYSTEM', 'Press Home or open another app', gui=['Press Home'], evidence=FW_ACT_PAUSE + '; SRC SlidingPlaybackActivity.java:98-102')
e(impl('LibraryActivity', 'onPause'), 'BottomBarControls.onSaveInstanceState', 'SYSTEM', 'the stopping activity saves its view state (BottomBarControls closes the search field first)', evidence=FW_SAVESTATE + '; SRC BottomBarControls.java:125-130')
e(impl('LibraryActivity', 'onPause'), LP + '.saveState', 'SYSTEM', 'the ViewPager saves the state of its adapter while the view state is saved', evidence=FW_SAVESTATE + '; ' + FW_VIEWPAGER, cls='non_standard', via='androidx ViewPager.onSaveInstanceState calls PagerAdapter.saveState')
e(impl('LibraryActivity', 'onPause'), 'S_LIBRARY_PAUSED', 'ENTERS', 'LibraryActivity is stopped', evidence=FW_ACT_STOP + '; SRC SlidingPlaybackActivity.java:98-102')
e('S_LIBRARY_PAUSED', LA + '.onStart', 'SYSTEM', 'Return to the app from the recent apps list or the launcher (the stopped activity is started again)', gui=['Return to the app'], evidence=FW_ACT_CREATE.split(' and core/java/android/app/Activity.java')[0] + ' (Activity.performStart / performRestart calls onStart again)')
e('S_LIBRARY_PAUSED', RESUME_LA, 'SYSTEM', 'Return to the app: onResume', gui=['Return to the app'], evidence=FW_ACT_RESUME)
e('S_LIBRARY', impl('LibraryActivity', 'onDestroy'), 'SYSTEM', 'The activity is destroyed (rotation, finish, system)', env=ENV_ROTATE, gui=['Rotate the device'], evidence=FW_ACT_DESTROY + '; SRC PlaybackActivity.java:111-117')
e(impl('LibraryActivity', 'onDestroy'), 'S_EXIT', 'ENTERS', 'the activity is gone', evidence=FW_ACT_DESTROY + '; SRC PlaybackActivity.java:111-117')
e('S_LIBRARY_PAUSED', impl('LibraryActivity', 'onDestroy'), 'SYSTEM', 'The stopped activity is destroyed by the system (or the user swipes it away)', env=ENV_KILL, evidence=FW_ACT_DESTROY + '; SRC PlaybackActivity.java:111-117')
SCREENS['S_LIBRARY_PAUSED'] = 'LibraryActivity is stopped: Home key, another activity or app on top'
# restoring the pager after a rotation
e(LA + '.onCreate', LP + '.restoreState', 'FRAMEWORK', 'the activity is recreated with a saved state: the ViewPager restores the adapter state', env=ENV_ROTATE, evidence=FW_VIEWPAGER + '; SRC LibraryPagerAdapter.java:414-424',
  cls='non_standard', via='androidx ViewPager.onRestoreInstanceState calls PagerAdapter.restoreState')
# new intents (singleTask): notification, widget, double-tap, "more from" menu, Library action of the swipe
e(LA + '.onNewIntent', LA + '.checkForLaunch', 'CALL', 'checkForLaunch(intent)', evidence='SRC LibraryActivity.java:285 (bytecode)')
LI = LA + '.loadLimiterIntent'
LI_V = variants_of(LI, 'LibraryActivity.java', 'loadLimiterIntent', bounds=[('LIMIT', 262, 276)], text='call made when the intent carries a limiter')
ONI_LIMIT = LA + '.onNewIntent@LIMIT'
call(ONI_LIMIT, LI_V['LIMIT'], 'loadLimiterIntent(intent) with an intent that carries type, id and folder extras', 'SRC LibraryActivity.java:286, 254-276', guard='the intent has extras type / id / folder (PlaybackActivity.openLibrary)')
call(ONI_LIMIT, LA + '.checkForLaunch', 'checkForLaunch(intent)', 'SRC LibraryActivity.java:285 (bytecode)')
call(ONI_LIMIT, LI, 'loadLimiterIntent(intent)', 'SRC LibraryActivity.java:286 (bytecode)')


# ===================================================================== D. PlaybackActivity base (Handler messages, controls, menus)
NEED_FULL_OPEN = state_text('FullPlaybackActivity is the open playback screen (the code runs for the Full instance)', 'session')
NEED_LIB_OPEN = state_text('LibraryActivity is open (the code runs for the Library instance)', 'session')


def hv(cls_src, fname, mname, nth=0, params=None, skip=('default',)):
    b = CS.branches(fname, mname, nth, params)
    return variants_of(cls_src + '.handleMessage', fname, mname, nth, params, bounds=b, names={l: l for l, a, b_ in b}, skip=skip, text='call made in the message branch')


PBA_H = hv('PlaybackActivity', 'PlaybackActivity.java', 'handleMessage')
SPA_H = hv('SlidingPlaybackActivity', 'SlidingPlaybackActivity.java', 'handleMessage')
LA_H = hv('LibraryActivity', 'LibraryActivity.java', 'handleMessage')
FPA_H = hv('FullPlaybackActivity', 'FullPlaybackActivity.java', 'handleMessage')
LA_TOP, FPA_TOP = impl('LibraryActivity', 'handleMessage'), impl('FullPlaybackActivity', 'handleMessage')
PBA_TOP = 'PlaybackActivity.handleMessage'


def send_act(site, variants, label, text, ev, tops=('L', 'F'), gate_full=True, **kw):
    """Handler message from base-class code: it runs for a Library or Full instance; the message reaches the top handleMessage of that instance and the branch of the class that handles it."""
    for t in tops:
        top = LA_TOP if t == 'L' else FPA_TOP
        kk = dict(kw)
        if t == 'F' and gate_full and 'needs_state' not in kk:
            kk['needs_state'] = NEED_FULL_OPEN
        e(site, top, 'ASYNC', 'Handler.dispatchMessage calls %s with %s' % (top, text), evidence=ev + '; ' + FW_HANDLER, **kk)
    kk = dict(kw)
    e(site, variants[label], 'ASYNC', 'the branch that handles %s runs' % text, evidence=ev + '; ' + FW_HANDLER, **kk)


# Library level
send(LA + '.onPageChanged', LA_TOP, LA_H, 'MSG_SAVE_PAGE', 'MSG_SAVE_PAGE', 'SRC LibraryActivity.java:1037-1038', guard='adapter != null and (the adapter has no limiter or it is the Files adapter)')
send(LA + '.onSongChange', LA_TOP, LA_H, 'MSG_UPDATE_COVER', 'MSG_UPDATE_COVER', 'SRC LibraryActivity.java:997', guard='song != null')
e(LA + '.updateCover', LA + '$1.run', 'ASYNC', 'runOnUiThread(new Runnable(){...}): the cover bitmap is set on the UI thread', evidence=FW_RUNUI + '; SRC LibraryActivity.java:575-581')
e(LA + '$1.run', 'BottomBarControls.setCover', 'CALL', 'mBottomBarControls.setCover(cover)', evidence='SRC LibraryActivity.java:579 (bytecode)')
send(LA + '$2.onSuccess', LA_TOP, PBA_H, 'MSG_RENAME_PLAYLIST', 'MSG_RENAME_PLAYLIST', 'SRC LibraryActivity.java:773-776')
send(LA + '$3.onClick', LA_TOP, PBA_H, 'MSG_DELETE', 'MSG_DELETE', 'SRC LibraryActivity.java:787-791')
for lab in ('MSG_SAVE_PAGE', 'MSG_UPDATE_COVER'):
    pass
call(LA_H['MSG_SAVE_PAGE'], 'SlidingPlaybackActivity.adjustSpines', 'super.adjustSpines()', 'SRC LibraryActivity.java:954 (bytecode)')
# base-class level (runs for Library or Full instances)
for site, lab, ln, g in (('PlaybackActivity.addToPlaylist', 'MSG_NOTIFY_PLAYLIST_CHANGED', 531, {}), ('PlaybackActivity.removeFromPlaylist', 'MSG_NOTIFY_PLAYLIST_CHANGED', 553, {})):
    e(site, LA_TOP, 'ASYNC', 'Handler.dispatchMessage calls %s with MSG_NOTIFY_PLAYLIST_CHANGED' % LA_TOP, evidence='SRC PlaybackActivity.java:%d; ' % ln + FW_HANDLER)
    e(site, PBA_H[lab], 'ASYNC', 'the branch of PlaybackActivity.handleMessage that ignores MSG_NOTIFY_PLAYLIST_CHANGED runs', evidence='SRC PlaybackActivity.java:%d, 502-505; ' % ln + FW_HANDLER)
    e(site, FPA_TOP, 'ASYNC', 'Handler.dispatchMessage calls %s with MSG_NOTIFY_PLAYLIST_CHANGED' % FPA_TOP, needs_state=NEED_FULL_OPEN, evidence='SRC PlaybackActivity.java:%d; ' % ln + FW_HANDLER)
    e(site, FPA_H['MSG_NOTIFY_PLAYLIST_CHANGED'], 'ASYNC', 'the FullPlaybackActivity branch refreshes the favourite star', needs_state=NEED_FULL_OPEN, evidence='SRC PlaybackActivity.java:%d; FullPlaybackActivity.java:603-609; ' % ln + FW_HANDLER)
UPD = 'SlidingPlaybackActivity.updatePlaylistFromPlaylistDialog'
send_act(UPD, PBA_H, 'MSG_CREATE_PLAYLIST', 'MSG_CREATE_PLAYLIST', 'SRC SlidingPlaybackActivity.java:179-181', guard='data.id < 0 (a new playlist)')
send_act(UPD, PBA_H, 'MSG_ADD_QUEUE_TO_PLAYLIST', 'MSG_ADD_QUEUE_TO_PLAYLIST', 'SRC SlidingPlaybackActivity.java:172-174, 182-183', guard='data.id >= 0 and data.sourceIntent == null (the queue is saved)')
send_act(UPD, PBA_H, 'MSG_ADD_TO_PLAYLIST', 'MSG_ADD_TO_PLAYLIST', 'SRC SlidingPlaybackActivity.java:175-178, 182-183', guard='data.id >= 0 and data.sourceIntent != null (library rows are added)')
e(PBA_H['MSG_CREATE_PLAYLIST'], PBA_H['MSG_ADD_TO_PLAYLIST'], 'ASYNC', 'mHandler.sendMessage(obtainMessage(nextAction, playlistTask)) with MSG_ADD_TO_PLAYLIST', guard='nextAction == MSG_ADD_TO_PLAYLIST', evidence='SRC PlaybackActivity.java:466; ' + FW_HANDLER)
e(PBA_H['MSG_CREATE_PLAYLIST'], PBA_H['MSG_ADD_QUEUE_TO_PLAYLIST'], 'ASYNC', 'mHandler.sendMessage(obtainMessage(nextAction, playlistTask)) with MSG_ADD_QUEUE_TO_PLAYLIST', guard='nextAction == MSG_ADD_QUEUE_TO_PLAYLIST', evidence='SRC PlaybackActivity.java:466; ' + FW_HANDLER)
e(PBA_H['MSG_CREATE_PLAYLIST'], LA_TOP, 'ASYNC', 'Handler.dispatchMessage calls the top handleMessage with the follow-up message', evidence='SRC PlaybackActivity.java:466; ' + FW_HANDLER)
UEL = 'SlidingPlaybackActivity.updateElapsedTime'
send_act(UEL, SPA_H, 'MSG_UPDATE_PROGRESS', 'MSG_UPDATE_PROGRESS (delayed 1 s)', 'SRC SlidingPlaybackActivity.java:267-271', guard='!mPaused and the state has FLAG_PLAYING', needs_state=NEED_PLAYING)
send_act('SlidingPlaybackActivity.onProgressChanged', SPA_H, 'MSG_SEEK_TO_PROGRESS', 'MSG_SEEK_TO_PROGRESS (delayed 150 ms)', 'SRC SlidingPlaybackActivity.java:276-282', guard='fromUser (the user drags the seek bar)')
# seek bar and the other listeners registered in bindControlButtons (SlidingPlaybackActivity)
for pg in ('S_SLIDE_LIBRARY', 'S_SLIDE_LIBRARY_QUEUE'):
    for cb, txt in (('onProgressChanged', 'Drag the seek bar'), ('onStartTrackingTouch', 'Put the finger on the seek bar'), ('onStopTrackingTouch', 'Lift the finger from the seek bar')):
        gui(pg, 'SlidingPlaybackActivity.' + cb, txt, evidence='SRC SlidingPlaybackActivity.java:85-87, 275-293; ' + FW_SEEKBAR, needs_state=NEED_PLAYING if cb == 'onProgressChanged' else None)

FW_CTXMENU = ('FW-SRC core/java/android/app/Activity.java:3466-3470, 3769-3770 and core/java/android/view/View.java:12578-12589 '
              '(registerForContextMenu makes the activity the context-menu listener of the view; a long press builds the menu through createContextMenu, which calls the activity onCreateContextMenu; '
              'a chosen item reaches Activity.onMenuItemSelected, which calls onContextItemSelected)')
ENV_KEYS = env_text('a media key (headset hook, play/pause, next, previous) is pressed on a keyboard or headset attached to the device', 'hardware')
SCREENS.update({
    'S_CTX_BUTTON': 'Context menu of the shuffle button (no shuffle / shuffle songs / shuffle albums) or the repeat button (no repeat / repeat / repeat current song / stop after current song / random)',
})

# ---- D2. lifecycle and controls of PlaybackActivity (shared by the Library, Full, Mini, AudioPicker and AudioSearch activities)
PBA = 'PlaybackActivity'
sup((PBA + '.onStart', PBA + '.onServiceReady'), (PBA + '.onResume', 'PlaybackService.userActionTriggered'), (PBA + '.onResume', 'PlaybackService.get'))
e(PBA + '.onStart', PBA + '.onServiceReady', 'CALL', 'PlaybackService.hasInstance(): onServiceReady()', guard='PlaybackService.hasInstance() is true', needs_state=NEED_SERVICE_UP, evidence='SRC PlaybackActivity.java:124-125')
e(PBA + '.onStart', 'PlaybackService.<init>', 'INTENT', 'startService(new Intent(this, PlaybackService.class)): the service is created and started', guard='PlaybackService.hasInstance() is false (the service does not run yet)',
  evidence='SRC PlaybackActivity.java:124-127; AndroidManifest.xml:171-181; FW-SRC core/java/android/app/ActivityThread.java:3311, 3464 (handleCreateService / handleServiceArgs create the service and call its onCreate / onStartCommand)')
e(PBA + '.onResume', 'PlaybackService.userActionTriggered', 'CALL', 'service.userActionTriggered()', guard='PlaybackService.hasInstance()', needs_state=NEED_SERVICE_UP, evidence='SRC PlaybackActivity.java:155-157 (bytecode)')
e(PBA + '.onResume', 'PlaybackService.get', 'CALL', 'PlaybackService.get(this)', guard='PlaybackService.hasInstance()', needs_state=NEED_SERVICE_UP, evidence='SRC PlaybackActivity.java:156 (bytecode)')
# runOnUiThread posts the runnables of setState / setSong / showToast
e(PBA + '.setState(int)', PBA + '$1.run', 'FRAMEWORK', 'runOnUiThread(new Runnable(){...}) runs onStateChange(state, toggled) on the UI thread', guard='the state changed (mState != state)', evidence='SRC PlaybackActivity.java:256-266; ' + FW_RUNUI)
e(PBA + '.setSong(Song)', PBA + '$2.run', 'FRAMEWORK', 'runOnUiThread(new Runnable(){...}) runs onSongChange(song) on the UI thread', evidence='SRC PlaybackActivity.java:302-312; ' + FW_RUNUI)
e(PBA + '.showToast', PBA + '$3.run', 'FRAMEWORK', 'runOnUiThread(new Runnable(){...}) shows the toast on the UI thread', evidence='SRC PlaybackActivity.java:593-600; ' + FW_RUNUI)
sup((PBA + '$1.run', 'FullPlaybackActivity.onStateChange'), (PBA + '$1.run', 'LibraryActivity.onStateChange'), (PBA + '$1.run', 'SlidingPlaybackActivity.onStateChange'),
    (PBA + '$2.run', 'FullPlaybackActivity.onSongChange'), (PBA + '$2.run', 'LibraryActivity.onSongChange'), (PBA + '$2.run', 'SlidingPlaybackActivity.onSongChange'))
for fn, nm in (('onStateChange', '$1.run'), ('onSongChange', '$2.run')):
    e(PBA + nm, PBA + '.' + fn, 'CALL', '%s(...) of the instance that runs the code (the plain PlaybackActivity version: Mini, AudioPicker, AudioSearch)' % fn, guard='the activity is a MiniPlaybackActivity, AudioPickerActivity or AudioSearchActivity', evidence='SRC PlaybackActivity.java:%d (bytecode)' % (263 if fn == 'onStateChange' else 309))
    e(PBA + nm, LA + '.' + fn, 'CALL', '%s(...) of the LibraryActivity instance' % fn, needs_state=NEED_LIB_OPEN, evidence='SRC PlaybackActivity.java:%d (bytecode); LibraryActivity.java:%d' % (263 if fn == 'onStateChange' else 309, 982 if fn == 'onStateChange' else 991))
    e(PBA + nm, 'FullPlaybackActivity.' + fn, 'CALL', '%s(...) of the FullPlaybackActivity instance' % fn, needs_state=NEED_FULL_OPEN, evidence='SRC PlaybackActivity.java:%d (bytecode); FullPlaybackActivity.java:%d' % (263 if fn == 'onStateChange' else 309, 225 if fn == 'onStateChange' else 244))
# the control buttons call the service through the activity
PB_B = CS.branches('PlaybackActivity.java', 'onClick')
PB_V = variants_of(PBA + '.onClick', 'PlaybackActivity.java', 'onClick', bounds=PB_B, names={l: l.replace('R.id.', '') for l, a, b in PB_B}, text='call made for this button')
for lab, a_, b_ in PB_B:
    e(PBA + '.onClick', PB_V[lab], 'CALL', 'the button %s was tapped' % lab.replace('R.id.', ''), guard='view.getId() == ' + lab, evidence='SRC PlaybackActivity.java:%d-%d' % (a_, b_))
# keys and the context menus of the shuffle / repeat buttons
e(PBA + '.onKeyDown', 'MediaButtonReceiver.processKey', 'CALL', 'media key codes are handled by MediaButtonReceiver.processKey(this, event)', env=ENV_KEYS, guard='keyCode is HEADSETHOOK, MEDIA_PLAY_PAUSE, MEDIA_NEXT or MEDIA_PREVIOUS', evidence='SRC PlaybackActivity.java:165-171 (bytecode)')
e(PBA + '.onKeyUp', 'MediaButtonReceiver.processKey', 'CALL', 'media key codes are handled by MediaButtonReceiver.processKey(this, event)', env=ENV_KEYS, guard='keyCode is HEADSETHOOK, MEDIA_PLAY_PAUSE, MEDIA_NEXT or MEDIA_PREVIOUS', evidence='SRC PlaybackActivity.java:179-184 (bytecode)')
for ctx, pg_from, pg_back in (('LIBRARY', ('S_SLIDE_LIBRARY', 'S_SLIDE_LIBRARY_QUEUE'), 'S_SLIDE_LIBRARY'),):
    for pg in pg_from:
        gui2(pg, PBA + '.onCreateContextMenu', PBA + '.onCreateContextMenu@' + ctx, 'Long-press the shuffle or the repeat button', 'SRC PlaybackActivity.java:325-330, 676-690; ' + FW_CTXMENU)
    e(PBA + '.onCreateContextMenu@' + ctx, 'S_CTX_BUTTON@' + ctx, 'ENTERS', 'the context menu of the button is shown', evidence='SRC PlaybackActivity.java:676-690')
    gui2('S_CTX_BUTTON@' + ctx, PBA + '.onContextItemSelected', PBA + '.onContextItemSelected@' + ctx, 'Tap an entry of the shuffle / repeat context menu', 'SRC PlaybackActivity.java:692-702; ' + FW_CTXMENU)
    e(PBA + '.onContextItemSelected@' + ctx, pg_back, 'ENTERS', 'the menu closes and the state of the button changes', evidence='SRC PlaybackActivity.java:692-702')


# ===================================================================== E. FullPlaybackActivity, MiniPlaybackActivity, AudioPicker, AudioSearch, ShortcutPseudoActivity, PermissionRequestActivity
FW_SEARCHKEY = ('FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:2035-2046, 3130-3148 and core/java/android/app/Activity.java:3255-3273, 4086, 4096 '
                '(the window handles the search key in onKeyUp by launchDefaultSearch, which calls onSearchRequested of the activity window callback)')
ENV_SEARCHKEY = env_text('the search key of a hardware keyboard or navigation pad is pressed (KEYCODE_SEARCH reaches the window)', 'hardware')
NEED_ACTION_PREF = state_text('A gesture action preference (cover press, cover long press, swipe up, swipe down or shake) is set to an action other than "do nothing" (Settings > Playback or Settings > Shake; default: do nothing)', 'settings')
NEED_DISPLAY_MODE = state_text('Settings > Playback > Display mode is set to "info on cover" or "info below cover" (default: fixed info)', 'settings')
NEED_EXTRA_INFO = state_text('The extra info table is shown (long-press the info table; visible_extra_info is true)', 'session')
NEED_FAV_STAR = state_text('The playback menu was created and a song is loaded (the favourite star shows its state)', 'session')
SCREENS.update({
    'S_FULL': 'FullPlaybackActivity: cover, info table (title, artist, album; extra rows after a long press), seek bar and the control buttons, action bar with the playback menu',
    'S_FULL_QUEUE': 'FullPlaybackActivity with the sliding panel pulled fully up: the queue list is visible',
    'S_FULL_MENU': 'Action bar overflow menu of FullPlaybackActivity (Delete, Enqueue, More from, Add to playlist, Share, Plugins, Settings, queue entries, Jump to time)',
    'S_MINI': 'MiniPlaybackActivity: popup dialog with the cover and the control buttons',
    'S_PICKER': 'AudioPickerActivity: popup dialog with the file name, a progress bar and the buttons Cancel, Enqueue and Play',
    'S_DLG_DELETE_FULL': 'Confirm dialog "Delete" for the playing song (FullPlaybackActivity)',
})
FP = 'FullPlaybackActivity'
e(FP + '.<init>', FP + '.<clinit>', 'LIFECYCLE', 'class initialisation of the switch map used by performAction', evidence='SRC FullPlaybackActivity.java:626; INFERRED the JVM runs the static initialiser of the generated switch-map class before first use (Java language rule, not read from a source)') if (FP + '.<clinit>') in METHODS else None
lifecycle(FP, ('onCreate', 'onStart'), FW_ACT_CREATE, 'Activity lifecycle callback; SRC FullPlaybackActivity.java:106-185')
# RESUME_FP: see the comment at RESUME_LA (section B2) - FullPlaybackActivity also does not override onResume, so impl(FP, 'onResume') is the SAME shared
# node as LibraryActivity's (SlidingPlaybackActivity.onResume); a plain edge from it to S_FULL would let a route enter through LibraryActivity and exit
# through FullPlaybackActivity's screen with no gate. Use the @FullPlaybackActivity variant instead (the shared bytecode body is copied onto it automatically).
RESUME_FP = 'SlidingPlaybackActivity.onResume@FullPlaybackActivity'
e(FP + '.<init>', RESUME_FP, 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACT_RESUME)
e(RESUME_FP, 'S_FULL', 'ENTERS', 'FullPlaybackActivity is resumed and shown (controls visible by default)', evidence='SRC FullPlaybackActivity.java:168; PrefDefaults.java:65')
inflate(FP + '.onCreate', ['CoverView.<init>', 'SlidingView.<init>(Context,AttributeSet)', 'VanillaImageButton.<init>(Context,AttributeSet)'], 'full_playback_alt.xml, controls.xml, seek_bar.xml')
e(FP + '.onCreate', 'ShowQueueFragment.<init>', 'FRAMEWORK', 'setContentView inflates the <fragment class=ShowQueueFragment> of full_playback_alt.xml', evidence='SRC res/layout/full_playback_alt.xml:47-50; ' + FW_FRAG_XML,
  cls='non_standard', via='the <fragment> XML tag; FragmentManager.onCreateView instantiates the named class through reflection (Fragment.instantiate)')
for cb in ('onSizeChanged', 'onMeasure', 'onDraw'):
    e('CoverView.<init>', 'CoverView.' + cb, 'FRAMEWORK', 'the cover view is measured, sized and drawn', evidence=FW_VIEW_DRAW)
for pg in ('S_FULL', 'S_FULL_QUEUE'):
    gui2(pg, ST, ST_F, 'Swipe on the control strip (the sliding panel snaps to another stage)', 'SRC SlidingView.java:235-251, 313-379; ' + FW_VIEW_CLICK)
e(ST_F, 'S_FULL', 'ENTERS', 'the panel snaps to the first stage (seek bar and controls)', guard='mDidScroll and the target stage is 0', evidence='SRC SlidingView.java:331-343')
e(ST_F, 'S_FULL_QUEUE', 'ENTERS', 'the panel snaps to the last stage: the queue is shown', guard='mDidScroll and the target stage is the last one', evidence='SRC SlidingView.java:331-343')
# touch on the cover: CoverView.onTouchEvent (tap, long-press, swipe)
for pg in ('S_FULL', 'S_MINI'):
    gui(pg, 'CoverView.onTouchEvent', 'Touch the cover (tap, long-press or swipe)', evidence='SRC CoverView.java:354-479; FW-SRC core/java/android/view/View.java:11768-11774 (the touch dispatch calls onTouchEvent of the view)')
# CoverView: the callback is the PlaybackActivity (CHA edges are replaced by edges per instance type)
sup(('CoverView.onTouchEvent', 'PlaybackActivity.downSwipe'), ('CoverView.onTouchEvent', 'PlaybackActivity.upSwipe'), ('CoverView.handleMessage', 'PlaybackActivity.shiftCurrentSong'))
for fn in ('downSwipe', 'upSwipe'):
    e('CoverView.onTouchEvent', 'PlaybackActivity.%s@FullPlaybackActivity' % fn, 'CALL', 'mCallback.%s() of the FullPlaybackActivity (vertical fling on the cover)' % fn, guard='mvy > mvx and the speed is above the snap velocity; the cover belongs to FullPlaybackActivity',
      needs_state=NEED_FULL_OPEN, evidence='SRC CoverView.java:446-452 (bytecode)')
    e('CoverView.onTouchEvent', 'PlaybackActivity.' + fn, 'CALL', 'mCallback.%s() of the activity that owns the cover (vertical fling on the cover)' % fn, guard='mvy > mvx and the speed is above the snap velocity', evidence='SRC CoverView.java:446-452 (bytecode)')
e('CoverView.handleMessage', 'PlaybackActivity.shiftCurrentSong', 'CALL', 'mCallback.shiftCurrentSong(arg1) after a horizontal swipe on the cover', guard='message.what == MSG_SHIFT_SONG', evidence='SRC CoverView.java:251-254 (bytecode)')
# CoverView messages
CV_H = hv('CoverView', 'CoverView.java', 'handleMessage', skip=('default',))
send('CoverView.querySongs', 'CoverView.handleMessage', CV_H, 'MSG_QUERY_SONGS', 'MSG_QUERY_SONGS', 'SRC CoverView.java:166-169', guard='called by setSong / replaceSong / onSizeChanged')
send('CoverView.querySongsInternal', 'CoverView.handleMessage', CV_H, 'MSG_SET_BITMAP', 'MSG_SET_BITMAP', 'SRC CoverView.java:201-206', guard='the song of this slot changed (mBitmapBucket.getSong(i) != song)', needs_state=NEED_PLAYING)
send('CoverView.advanceScroll', 'CoverView.handleMessage', CV_H, 'MSG_SHIFT_SONG', 'MSG_SHIFT_SONG', 'SRC CoverView.java:341-343', guard='the scroll finished with a non-zero coverIntent (ASYNC_SWITCH < 0 is a constant true)', needs_state=NEED_PLAYING)
send('CoverView.onTouchEvent', 'CoverView.handleMessage', CV_H, 'MSG_SHIFT_SONG', 'MSG_SHIFT_SONG', 'SRC CoverView.java:375-390', guard='a touch interrupted a running scroll that was about to change the song', needs_state=NEED_PLAYING)
send('CoverView.onTouchEvent', 'CoverView.handleMessage', CV_H, 'MSG_UI_LONG_CLICK', 'MSG_UI_LONG_CLICK (delayed by twice the long-press timeout)', 'SRC CoverView.java:369-370', guard='ACTION_DOWN while the scroller is finished')


# ---- E2. FullPlaybackActivity: taps, long presses, keys, menu
FC = FP + '.onClick'
FC_B = CS.branches('FullPlaybackActivity.java', 'onClick')
FC_N = {FC_B[0][0]: 'OVERLAY', FC_B[1][0]: 'COVER', FC_B[2][0]: 'INFO', FC_B[3][0]: 'BUTTON'}
FC_V = variants_of(FC, 'FullPlaybackActivity.java', 'onClick', bounds=FC_B, names=FC_N, text='call made in the click branch')
gui2('S_FULL', FC, FC_V[FC_B[1][0]], 'Tap the cover (the CoverView calls performClick)', 'SRC FullPlaybackActivity.java:139-143, 644-646; CoverView.java:439-443; ' + FW_VIEW_CLICK)
gui2('S_FULL', FC, FC_V[FC_B[2][0]], 'Tap the info table (title, artist, album)', 'SRC FullPlaybackActivity.java:145-150, 646-648; ' + FW_VIEW_CLICK, needs_state=NEED_PLAYING)
gui2('S_FULL', FC, FC_V[FC_B[3][0]], 'Tap one of the control buttons (previous, play / pause, next, shuffle, repeat)', 'SRC PlaybackActivity.java:317-331; FullPlaybackActivity.java:648-650; ' + FW_VIEW_CLICK)
gui2('S_FULL_QUEUE', FC, FC_V[FC_B[3][0]], 'Tap one of the control buttons (previous, play / pause, next, shuffle, repeat)', 'SRC PlaybackActivity.java:317-331; FullPlaybackActivity.java:648-650; ' + FW_VIEW_CLICK)
gui2('S_FULL', FC, FC_V[FC_B[0][0]], 'Tap the "no songs / empty queue" message that covers the screen', 'SRC FullPlaybackActivity.java:201-222, 642-644; ' + FW_VIEW_CLICK,
     needs_state=state_text('The message overlay is shown: the service has no media (FLAG_NO_MEDIA) or an empty queue (FLAG_EMPTY_QUEUE)', 'session'))
e(FC_V[FC_B[0][0]], 'S_FULL', 'ENTERS', 'random mode starts and the overlay disappears', evidence='SRC FullPlaybackActivity.java:642-644')
e(FC_V[FC_B[1][0]], 'S_FULL', 'ENTERS', 'the cover press action runs', evidence='SRC FullPlaybackActivity.java:644-646')
e(FC_V[FC_B[3][0]], 'S_FULL', 'ENTERS', 'the control state changed', evidence='SRC FullPlaybackActivity.java:648-650')
e(FP + '.onClick@INFO', 'LibraryActivity.<init>', 'INTENT', 'openLibrary(mCurrentSong, TYPE_ALBUM): startActivity(LibraryActivity with the album limiter)', guard='the library task does not exist yet', evidence='SRC FullPlaybackActivity.java:646-648; PlaybackActivity.java:625-654')
OLONG = FP + '.onLongClick'
FL_B = CS.branches('FullPlaybackActivity.java', 'onLongClick')
FL_V = variants_of(OLONG, 'FullPlaybackActivity.java', 'onLongClick', bounds=FL_B, names={l: l.replace('R.id.', '') for l, a, b in FL_B}, skip=('default',), text='call made in the long-click branch')
gui2('S_FULL', OLONG, FL_V['R.id.cover_view'], 'Long-press the cover', 'SRC FullPlaybackActivity.java:142, 657-659; CoverView.java:258-265; ' + FW_VIEW_CLICK)
gui2('S_FULL', OLONG, FL_V['R.id.info_table'], 'Long-press the info table (shows or hides the extra rows)', 'SRC FullPlaybackActivity.java:148, 660-663; ' + FW_VIEW_CLICK)
e(FL_V['R.id.cover_view'], 'S_FULL', 'ENTERS', 'the cover long-press action runs', evidence='SRC FullPlaybackActivity.java:657-659')
e(FL_V['R.id.info_table'], 'S_FULL', 'ENTERS', 'the extra info rows are toggled', evidence='SRC FullPlaybackActivity.java:660-663')
# performAction of the Full activity: only ToggleControls and ShowQueue are handled here
FPA_A = FP + '.performAction'
FPA_AB = CS.branches('FullPlaybackActivity.java', 'performAction')
FPA_AV = variants_of(FPA_A, 'FullPlaybackActivity.java', 'performAction', bounds=FPA_AB, names={l: l for l, a, b in FPA_AB}, skip=('default',), text='call made for this action')
for lab, a_, b_ in FPA_AB:
    if lab == 'default':
        continue
    e(FPA_A, FPA_AV[lab], 'CALL', 'the action %s was configured' % lab, needs_state=NEED_ACTION_PREF, guard='action == ' + lab, evidence='SRC FullPlaybackActivity.java:626-633')
e(FPA_AV['ToggleControls'], 'S_FULL', 'ENTERS', 'the controls are shown or hidden', evidence='SRC FullPlaybackActivity.java:627-630')
e(FPA_AV['ShowQueue'], 'S_FULL_QUEUE', 'ENTERS', 'the queue slides up', evidence='SRC FullPlaybackActivity.java:631-633')
# keys
FKD = FP + '.onKeyDown'
FKD_B = CS.branches('FullPlaybackActivity.java', 'onKeyDown')
FKD_V = variants_of(FKD, 'FullPlaybackActivity.java', 'onKeyDown', bounds=FKD_B, names={l: l.replace('KeyEvent.KEYCODE_', '') for l, a, b in FKD_B}, skip=('default',), text='call made in the key branch')
FKU = FP + '.onKeyUp'
FKU_B = CS.branches('FullPlaybackActivity.java', 'onKeyUp')
FKU_V = variants_of(FKU, 'FullPlaybackActivity.java', 'onKeyUp', bounds=FKU_B, names={l: l.replace('KeyEvent.KEYCODE_', '') for l, a, b in FKU_B}, skip=('KeyEvent.KEYCODE_ENTER',), text='call made in the key branch')
for pg in ('S_FULL', 'S_FULL_QUEUE'):
    gui(pg, FKD, 'Press a key (D-pad left / right change the song, the search key opens the library search)', evidence='SRC FullPlaybackActivity.java:430-451; ' + FW_ACT_KEY)
    gui(pg, FKU, 'Press Back, or D-pad centre / Enter (toggles the controls)', evidence='SRC FullPlaybackActivity.java:453-470; ' + FW_ACT_KEY)
for lab in ('KEYCODE_DPAD_RIGHT', 'KEYCODE_DPAD_LEFT'):
    e(FKD, FKD_V['KeyEvent.' + lab], 'CALL', 'key %s' % lab, env=env_text('a D-pad or keyboard arrow key is pressed on a hardware keyboard or navigation pad', 'hardware'), needs_state=NEED_PLAYING, evidence='SRC FullPlaybackActivity.java:434-441')
e(FKD, FKD_V['KeyEvent.KEYCODE_SEARCH'], 'CALL', 'the search key opens the library with the search field', env=ENV_SEARCHKEY, guard='keyCode == KEYCODE_SEARCH reaches the activity (onKeyDown)', evidence='SRC FullPlaybackActivity.java:442-446')
e(FKD_V['KeyEvent.KEYCODE_SEARCH'], 'LibraryActivity.<init>', 'INTENT', 'startActivity(new Intent(this, LibraryActivity.class) with launch_search = true)', guard='the library task does not exist yet', evidence='SRC FullPlaybackActivity.java:442-446')
e(FKU, FKU_V['KeyEvent.KEYCODE_DPAD_CENTER'], 'CALL', 'key DPAD_CENTER / ENTER toggles the controls', env=env_text('a D-pad centre or Enter key is pressed on a hardware keyboard or navigation pad', 'hardware'), evidence='SRC FullPlaybackActivity.java:457-461')
e(FKU, FKU_V['KeyEvent.KEYCODE_BACK'], 'CALL', 'Back while the sliding panel is pulled up pushes it down', needs_state=NEED_SLIDE_QUEUE, guard='mSlidingView.isShrinkable()', evidence='SRC FullPlaybackActivity.java:462-466')
e(FKU_V['KeyEvent.KEYCODE_BACK'], 'S_FULL', 'ENTERS', 'the panel slides down', evidence='SRC FullPlaybackActivity.java:462-466')
e(FKU_V['KeyEvent.KEYCODE_DPAD_CENTER'], 'S_FULL', 'ENTERS', 'the controls are shown or hidden', evidence='SRC FullPlaybackActivity.java:457-461')
e(FKD_V['KeyEvent.KEYCODE_DPAD_RIGHT'], 'S_FULL', 'ENTERS', 'the song changes', evidence='SRC FullPlaybackActivity.java:434-437')
e(FKD_V['KeyEvent.KEYCODE_DPAD_LEFT'], 'S_FULL', 'ENTERS', 'the song changes', evidence='SRC FullPlaybackActivity.java:438-441')
e(FKD_V['KeyEvent.KEYCODE_SEARCH'], 'S_ENTRY', 'ENTERS', 'the library is started (another activity of this app)', evidence='SRC FullPlaybackActivity.java:442-446')
gui('S_FULL', FP + '.onSearchRequested', 'Press the search key (the window launches the default search)', env=ENV_SEARCHKEY, evidence='SRC FullPlaybackActivity.java:423-428; ' + FW_SEARCHKEY)
e(FP + '.onSearchRequested', 'LibraryActivity.<init>', 'INTENT', 'openLibrary(null, -1) starts the library', guard='the library task does not exist yet', evidence='SRC FullPlaybackActivity.java:423-428; PlaybackActivity.java:625-654')
# restart when the display mode changed and the menu / sliding callbacks
e(FP + '.onStart', FP + '.<init>', 'INTENT', 'the display mode preference changed: finish() and startActivity(new Intent(this, FullPlaybackActivity.class))', needs_state=NEED_DISPLAY_MODE,
  guard='mDisplayMode != the stored display mode', evidence='SRC FullPlaybackActivity.java:177-181; ' + FW_ACT_CREATE)


# ---- E3. FullPlaybackActivity: action bar menu, delete dialog, handler messages
FOI = FP + '.onOptionsItemSelected'
FOI_B = CS.branches('FullPlaybackActivity.java', 'onOptionsItemSelected')
FOI_N = {l: ('HOME' if l == 'android.R.id.home' else l.replace('MENU_', '')) for l, a, b in FOI_B}
FOI_V = variants_of(FOI, 'FullPlaybackActivity.java', 'onOptionsItemSelected', bounds=FOI_B, names=FOI_N, skip=('default',), text='call made in the menu item branch')
e(RESUME_FP, FP + '.onCreateOptionsMenu', 'FRAMEWORK', 'the window builds the options menu of the action bar (Playback theme with an action bar)',
  evidence='FW-SRC core/java/android/app/Activity.java:3386-3388 (onCreatePanelMenu calls onCreateOptionsMenu); INFERRED the decor view / action bar asks for the options menu when the window is set up (PhoneWindow panel code not read); SRC FullPlaybackActivity.java:294-328')
e(FP + '.onCreateOptionsMenu', FPA_TOP, 'ASYNC', 'Handler.dispatchMessage calls FullPlaybackActivity.handleMessage with MSG_LOAD_FAVOURITE_INFO', evidence='SRC FullPlaybackActivity.java:326; ' + FW_HANDLER)
e(FP + '.onCreateOptionsMenu', FPA_H['MSG_LOAD_FAVOURITE_INFO'], 'ASYNC', 'the branch that loads the favourite state runs', evidence='SRC FullPlaybackActivity.java:326; ' + FW_HANDLER)
gui('S_FULL', FP + '.onOptionsItemSelected', 'Open the overflow menu of the action bar and tap an entry, or tap an action icon (favourite star, plugins), or the app icon', evidence='SRC FullPlaybackActivity.java:330-421; ' + FW_ACT_MENU)
OVERFLOW_GUI = 'Open the overflow menu of the action bar (three dots)'
e('S_FULL', 'S_FULL_MENU', 'ENTERS', 'the overflow menu of the action bar opens', gui=[OVERFLOW_GUI], evidence='SRC FullPlaybackActivity.java:294-328; INFERRED the action bar shows the overflow popup (ActionMenuPresenter source not read; core/java/android/widget/ActionMenuPresenter.java is held but the popup path was not read)')
FULL_ITEMS = [
    ('HOME', 'Tap the app icon at the left end of the action bar', 'S_FULL', 'S_FULL', {}),
    ('MORE_ALBUM', 'Tap "More from current" > "Album"', 'S_FULL_MENU', 'S_ENTRY', dict(needs_state=NEED_PLAYING)),
    ('MORE_ARTIST', 'Tap "More from current" > "Artist"', 'S_FULL_MENU', 'S_ENTRY', dict(needs_state=NEED_PLAYING)),
    ('MORE_GENRE', 'Tap "More from current" > "Genre"', 'S_FULL_MENU', 'S_ENTRY', dict(needs_state=NEED_PLAYING)),
    ('MORE_FOLDER', 'Tap "More from current" > "Folder"', 'S_FULL_MENU', 'S_ENTRY', dict(needs_state=NEED_PLAYING)),
    ('ENQUEUE_ALBUM', 'Tap "Enqueue current" > "Album"', 'S_FULL_MENU', 'S_FULL', dict(needs_state=NEED_PLAYING)),
    ('ENQUEUE_ARTIST', 'Tap "Enqueue current" > "Artist"', 'S_FULL_MENU', 'S_FULL', dict(needs_state=NEED_PLAYING)),
    ('ENQUEUE_GENRE', 'Tap "Enqueue current" > "Genre"', 'S_FULL_MENU', 'S_FULL', dict(needs_state=NEED_PLAYING)),
    ('SONG_FAVORITE', 'Tap the favourite star in the action bar', 'S_FULL', 'S_FULL', dict(needs_state=NEED_PLAYING)),
    ('ADD_TO_PLAYLIST', 'Tap "Add to playlist"', 'S_FULL_MENU', 'S_DLG_PLAYLIST', dict(needs_state=NEED_PLAYING)),
    ('SHARE', 'Tap "Share"', 'S_FULL_MENU', 'S_ENTRY', dict(needs_state=NEED_PLAYING, env=ENV_SHARE)),
    ('DELETE', 'Tap "Delete"', 'S_FULL_MENU', 'S_DLG_DELETE_FULL', dict(needs_state=NEED_PLAYING)),
    ('PLUGINS', 'Tap the plugins icon in the action bar', 'S_FULL', 'S_DLG_PLUGINS', dict(needs_state=NEED_PLAYING, env=ENV_PLUGIN)),
]
for nm, txt, frm, to, g in FULL_ITEMS:
    lab = [l for l, n in FOI_N.items() if n == nm][0]
    ab_ = [(a, b) for l, a, b in FOI_B if l == lab][0]
    gui(frm, FOI_V[lab], txt, evidence='SRC FullPlaybackActivity.java:%d-%d; ' % ab_ + FW_ACT_MENU, **g)
    if to == 'S_ENTRY':
        pass
    else:
        e(FOI_V[lab], to, 'ENTERS', 'the item %s finished' % nm, evidence='SRC FullPlaybackActivity.java:330-421')
# the entries the Full menu passes on to the Sliding / Playback levels
for lab, g in (('MENU_SHOW_QUEUE', {}), ('MENU_HIDE_QUEUE', dict(needs_state=NEED_SLIDE_QUEUE)), ('MENU_SAVE_QUEUE', dict(needs_state=NEED_SLIDE)), ('MENU_JUMP_TO_TIME', {})):
    gui('S_FULL_MENU', SOI_V[lab], 'Tap the menu entry of the queue / time group', evidence='SRC SlidingPlaybackActivity.java:126-131, 140-159; ' + FW_ACT_MENU, **g)
for lab, g in (('MENU_PREFS', {}), ('MENU_CLEAR_QUEUE', dict(needs_state=NEED_SLIDE)), ('MENU_EMPTY_QUEUE', dict(needs_state=NEED_SLIDE))):
    gui('S_FULL_MENU', POI_V[lab], 'Tap the menu entry "Settings", "Dequeue rest" or "Empty the queue"', evidence='SRC PlaybackActivity.java:403, 408-424; ' + FW_ACT_MENU, **g)
call(FOI, SOI, 'default branch: super.onOptionsItemSelected(item)', 'SRC FullPlaybackActivity.java:416-417 (bytecode)', guard='the item is not one of the Full items')
e(FOI_V['MENU_MORE_ALBUM'], 'LibraryActivity.<init>', 'INTENT', 'openLibrary(song, TYPE_ALBUM): startActivity(LibraryActivity with the album limiter)', guard='the library task does not exist yet', evidence='SRC FullPlaybackActivity.java:339-341; PlaybackActivity.java:625-654')
e(SOI_V['MENU_SHOW_QUEUE'], 'S_FULL_QUEUE', 'ENTERS', 'the sliding panel expands (Full activity): the queue is shown', guard='the activity is the FullPlaybackActivity', needs_state=NEED_FULL_OPEN, evidence='SRC SlidingPlaybackActivity.java:142-144')
e(SOI_V['MENU_HIDE_QUEUE'], 'S_FULL', 'ENTERS', 'the panel is minimized (Full activity)', guard='the activity is the FullPlaybackActivity', needs_state=NEED_FULL_OPEN, evidence='SRC SlidingPlaybackActivity.java:145-147')
for lab in ('MENU_CLEAR_QUEUE', 'MENU_EMPTY_QUEUE'):
    e(POI_V[lab], 'S_FULL_QUEUE', 'ENTERS', 'the queue changed (Full activity)', guard='the activity is the FullPlaybackActivity', needs_state=NEED_FULL_OPEN, evidence='SRC PlaybackActivity.java:414-419')
# delete dialog of the Full activity
gui('S_DLG_DELETE_FULL', FP + '$1.onClick', 'Tap "Delete" in the confirm dialog', evidence='SRC FullPlaybackActivity.java:393-400; ' + FW_DLG_BUTTON)
gui('S_DLG_DELETE_FULL', FP + '$2.onClick', 'Tap "Cancel" in the confirm dialog', evidence='SRC FullPlaybackActivity.java:402-405; ' + FW_DLG_BUTTON)
for nm in ('$1', '$2'):
    e(FP + nm + '.onClick', 'S_FULL', 'ENTERS', 'the dialog closes', evidence='SRC FullPlaybackActivity.java:393-405; ' + FW_DLG_BUTTON.split(' (')[0])
send(FP + '$1.onClick', FPA_TOP, PBA_H, 'MSG_DELETE', 'MSG_DELETE', 'SRC FullPlaybackActivity.java:395-399')
# the favourite star sends add / remove messages; extra info and controls
send(FP + '.onSongChange', FPA_TOP, FPA_H, 'MSG_LOAD_FAVOURITE_INFO', 'MSG_LOAD_FAVOURITE_INFO', 'SRC FullPlaybackActivity.java:260')
send(FP + '.onSongChange', FPA_TOP, FPA_H, 'MSG_LOAD_EXTRA_INFO', 'MSG_LOAD_EXTRA_INFO', 'SRC FullPlaybackActivity.java:264-266', guard='mExtraInfoVisible', needs_state=NEED_EXTRA_INFO, plain=False)
send(FP + '.onPositionInfoChanged', FPA_TOP, FPA_H, 'MSG_UPDATE_POSITION', 'MSG_UPDATE_POSITION', 'SRC FullPlaybackActivity.java:288-292', guard='mQueuePosView != null')
send(FP + '.onKeyUp', FPA_TOP, FPA_H, 'MSG_SAVE_CONTROLS', 'MSG_SAVE_CONTROLS', 'SRC FullPlaybackActivity.java:457-461', env=env_text('a D-pad centre or Enter key is pressed on a hardware keyboard or navigation pad', 'hardware'))
send(FP + '.setExtraInfoVisible', FPA_TOP, FPA_H, 'MSG_LOAD_EXTRA_INFO', 'MSG_LOAD_EXTRA_INFO', 'SRC FullPlaybackActivity.java:513-515', guard='visible && no MSG_LOAD_EXTRA_INFO pending', plain=False)
send(FP + '.loadExtraInfo', FPA_TOP, FPA_H, 'MSG_COMMIT_INFO', 'MSG_COMMIT_INFO', 'SRC FullPlaybackActivity.java:548', plain=False)
send(FP + '.performAction', FPA_TOP, FPA_H, 'MSG_SAVE_CONTROLS', 'MSG_SAVE_CONTROLS', 'SRC FullPlaybackActivity.java:627-630', needs_state=NEED_ACTION_PREF)
send(FP + '.onLongClick', FPA_TOP, FPA_H, 'MSG_SAVE_CONTROLS', 'MSG_SAVE_CONTROLS', 'SRC FullPlaybackActivity.java:660-663')
e(FPA_H['MSG_LOAD_FAVOURITE_INFO'], FPA_H['MSG_COMMIT_FAVOURITE_INFO'], 'ASYNC', 'mUiHandler.sendMessage(obtainMessage(MSG_COMMIT_FAVOURITE_INFO, found))', guard='mCurrentSong != null', evidence='SRC FullPlaybackActivity.java:604-609; ' + FW_HANDLER)
e(FPA_H['MSG_NOTIFY_PLAYLIST_CHANGED'], FPA_H['MSG_COMMIT_FAVOURITE_INFO'], 'ASYNC', 'mUiHandler.sendMessage(obtainMessage(MSG_COMMIT_FAVOURITE_INFO, found))', guard='mCurrentSong != null', evidence='SRC FullPlaybackActivity.java:603-609; ' + FW_HANDLER)
send(FOI_V['MENU_SONG_FAVORITE'], FPA_TOP, PBA_H, 'MSG_ADD_TO_PLAYLIST', 'MSG_ADD_TO_PLAYLIST', 'SRC FullPlaybackActivity.java:366-368', guard='the song is not in the favourites yet', needs_state=NEED_PLAYING)
send(FOI_V['MENU_SONG_FAVORITE'], FPA_TOP, PBA_H, 'MSG_REMOVE_FROM_PLAYLIST', 'MSG_REMOVE_FROM_PLAYLIST', 'SRC FullPlaybackActivity.java:366-368', guard='the song is in the favourites', needs_state=NEED_FAV)
# the queue slider of the Full activity: seek bar callbacks
for pg in ('S_FULL', 'S_FULL_QUEUE'):
    for cb, txt in (('onProgressChanged', 'Drag the seek bar'), ('onStartTrackingTouch', 'Put the finger on the seek bar'), ('onStopTrackingTouch', 'Lift the finger from the seek bar')):
        gui(pg, 'SlidingPlaybackActivity.' + cb, txt, evidence='SRC SlidingPlaybackActivity.java:85-87, 275-293; ' + FW_SEEKBAR, needs_state=NEED_PLAYING if cb == 'onProgressChanged' else None)


# ---- E4. MiniPlaybackActivity, AudioPickerActivity, AudioSearchActivity, ShortcutPseudoActivity, PermissionRequestActivity
FW_ASYNC = ('FW-SRC core/java/android/os/AsyncTask.java:219-224, 237-260, 594-596, 632-650, 326-334, 369-374, 691-697, 705-713 '
            '(execute uses the serial executor, which hands each task to THREAD_POOL_EXECUTOR; the worker runnable calls doInBackground; postResult sends the result to a main-looper handler whose handleMessage calls finish, which calls onPostExecute)')
NEED_NOTIF_ACTION_MINI = state_text('Settings > Notifications > "Notification action" is set to "open mini popup" (default: open main activity)', 'settings')
NEED_NOTIF_ACTION_FULL = state_text('Settings > Notifications > "Notification action" is set to "open full player" (default: open main activity)', 'settings')
NEED_NOTIF_ACTION_NEXT = state_text('Settings > Notifications > "Notification action" is set to "skip to next song" (default: open main activity)', 'settings')
NEED_NOTIFICATION = state_text('The playback notification is shown (a song was played; the service created the notification with its buttons)', 'session')
MP = 'MiniPlaybackActivity'
lifecycle(MP, ('onCreate', 'onStart'), FW_ACT_CREATE, 'Activity lifecycle callback; SRC MiniPlaybackActivity.java:37-51')
# RESUME_MINI: MiniPlaybackActivity extends PlaybackActivity directly and does not override onResume, so impl(MP, 'onResume') is the shared
# PlaybackActivity.onResume node; AudioPickerActivity (below) also inherits the same one. A plain edge to S_MINI would let a route enter through
# AudioPickerActivity and exit through MiniPlaybackActivity's screen (or vice versa) with no gate - same class of bug as RESUME_LA/RESUME_FP above.
RESUME_MINI = 'PlaybackActivity.onResume@MiniPlaybackActivity'
e(MP + '.<init>', RESUME_MINI, 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACT_RESUME)
e(RESUME_MINI, 'S_MINI', 'ENTERS', 'MiniPlaybackActivity is resumed and shown', evidence='SRC MiniPlaybackActivity.java:37-51')
inflate(MP + '.onCreate', ['CoverView.<init>', 'VanillaImageButton.<init>(Context,AttributeSet)'], 'mini_playback.xml, controls.xml')
MC = MP + '.onClick'
MC_B = CS.branches('MiniPlaybackActivity.java', 'onClick')
MC_V = variants_of(MC, 'MiniPlaybackActivity.java', 'onClick', bounds=MC_B, names={l: ('COVER' if 'cover_view' in l else 'BUTTON') for l, a, b in MC_B}, text='call made in the click branch')
gui2('S_MINI', MC, MC_V[MC_B[0][0]], 'Tap the cover (the CoverView calls performClick)', 'SRC MiniPlaybackActivity.java:47-48, 54-58; CoverView.java:439-443; ' + FW_VIEW_CLICK)
gui2('S_MINI', MC, MC_V[MC_B[1][0]], 'Tap one of the control buttons (previous, play / pause, next, shuffle, repeat)', 'SRC PlaybackActivity.java:317-331; MiniPlaybackActivity.java:59-61; ' + FW_VIEW_CLICK)
e(MC_V[MC_B[0][0]], 'FullPlaybackActivity.<init>', 'INTENT', 'startActivity(new Intent(this, FullPlaybackActivity.class)); finish()', evidence='SRC MiniPlaybackActivity.java:56-58; ' + FW_ACT_CREATE)
e(MC_V[MC_B[0][0]], 'S_ENTRY', 'ENTERS', 'the mini popup finishes and the full player starts', evidence='SRC MiniPlaybackActivity.java:56-58')
e(MC_V[MC_B[1][0]], 'S_MINI', 'ENTERS', 'the control state changed', evidence='SRC MiniPlaybackActivity.java:59-61')
for fn, kw in (('onKeyDown', {}), ('onKeyUp', {})):
    gui('S_MINI', PBA + '.' + fn, 'Press a key (media keys are passed to MediaButtonReceiver)', evidence='SRC PlaybackActivity.java:162-188; ' + FW_ACT_KEY)
gui2('S_MINI', PBA + '.onCreateContextMenu', PBA + '.onCreateContextMenu@MINI', 'Long-press the shuffle or the repeat button', 'SRC PlaybackActivity.java:325-330, 676-690; ' + FW_CTXMENU)
e(PBA + '.onCreateContextMenu@MINI', 'S_CTX_BUTTON@MINI', 'ENTERS', 'the context menu of the button is shown', evidence='SRC PlaybackActivity.java:676-690')
gui2('S_CTX_BUTTON@MINI', PBA + '.onContextItemSelected', PBA + '.onContextItemSelected@MINI', 'Tap an entry of the shuffle / repeat context menu', 'SRC PlaybackActivity.java:692-702; ' + FW_CTXMENU)
e(PBA + '.onContextItemSelected@MINI', 'S_MINI', 'ENTERS', 'the menu closes and the state of the button changes', evidence='SRC PlaybackActivity.java:692-702')
gui2('S_FULL', PBA + '.onCreateContextMenu', PBA + '.onCreateContextMenu@FULL', 'Long-press the shuffle or the repeat button', 'SRC PlaybackActivity.java:325-330, 676-690; ' + FW_CTXMENU)
gui2('S_FULL_QUEUE', PBA + '.onCreateContextMenu', PBA + '.onCreateContextMenu@FULL', 'Long-press the shuffle or the repeat button', 'SRC PlaybackActivity.java:325-330, 676-690; ' + FW_CTXMENU)
e(PBA + '.onCreateContextMenu@FULL', 'S_CTX_BUTTON@FULL', 'ENTERS', 'the context menu of the button is shown', evidence='SRC PlaybackActivity.java:676-690')
gui2('S_CTX_BUTTON@FULL', PBA + '.onContextItemSelected', PBA + '.onContextItemSelected@FULL', 'Tap an entry of the shuffle / repeat context menu', 'SRC PlaybackActivity.java:692-702; ' + FW_CTXMENU)
e(PBA + '.onContextItemSelected@FULL', 'S_FULL', 'ENTERS', 'the menu closes and the state of the button changes', evidence='SRC PlaybackActivity.java:692-702')
# swipes on the cover of the mini popup (the plain PlaybackActivity versions)
# AudioPickerActivity: the work after the permission check needs the storage permission
AP = 'AudioPickerActivity'
lifecycle(AP, ('onCreate', 'onStart'), FW_ACT_CREATE, 'Activity lifecycle callback; SRC AudioPickerActivity.java:70-115')
# RESUME_PICKER: see the comment at RESUME_MINI above (same shared-node issue, PlaybackActivity.onResume).
RESUME_PICKER = 'PlaybackActivity.onResume@AudioPickerActivity'
e(AP + '.<init>', RESUME_PICKER, 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACT_RESUME)
e(RESUME_PICKER, 'S_PICKER', 'ENTERS', 'AudioPickerActivity is resumed and shown (a popup dialog)', needs_state=state_text('The picker was set up: the intent has a URI and the storage permission is granted, so onCreate went past the permission check', 'session'),
  evidence='SRC AudioPickerActivity.java:80-115')
e(AP + '.onCreate', AP + '$AudioPickerWorker.doInBackground', 'ASYNC', 'mWorker.execute(uri): the task runs doInBackground on a pool thread', env=ENV_PERM, guard='the permission check passed and the intent has a URI', evidence='SRC AudioPickerActivity.java:93, 114, 187-191; ' + FW_ASYNC)
e(AP + '$AudioPickerWorker.doInBackground', AP + '$AudioPickerWorker.onPostExecute', 'ASYNC', 'the result is delivered on the main thread', evidence='SRC AudioPickerActivity.java:187-195; ' + FW_ASYNC)
AP_B = CS.branches('AudioPickerActivity.java', 'onClick')
AP_V = variants_of(AP + '.onClick', 'AudioPickerActivity.java', 'onClick', bounds=[('PLAY', 124, 126), ('ENQUEUE', 127, 129), ('CANCEL', 130, 133)], text='call made in the button branch')
gui2('S_PICKER', AP + '.onClick', AP_V['PLAY'], 'Tap "Play" (enabled after the file was recognised)', 'SRC AudioPickerActivity.java:107-108, 118-148; ' + FW_VIEW_CLICK, needs_state=state_text('The picker resolved the song (mSong is filled)', 'session'))
gui2('S_PICKER', AP + '.onClick', AP_V['ENQUEUE'], 'Tap "Enqueue" (enabled when the service already runs)', 'SRC AudioPickerActivity.java:104-105, 118-148, 165-168; ' + FW_VIEW_CLICK, needs_state=state_text('The picker resolved the song and the PlaybackService runs', 'session'))
gui2('S_PICKER', AP + '.onClick', AP_V['CANCEL'], 'Tap "Cancel"', 'SRC AudioPickerActivity.java:100-102, 130-133; ' + FW_VIEW_CLICK)
for v in ('PLAY', 'ENQUEUE', 'CANCEL'):
    e(AP_V[v], 'S_EXIT', 'ENTERS', 'the picker activity finishes', evidence='SRC AudioPickerActivity.java:118-148')
AS = 'AudioSearchActivity'
lifecycle(AS, ('onCreate', 'onStart'), FW_ACT_CREATE, 'Activity lifecycle callback; SRC AudioSearchActivity.java:36-58')
e(AS + '.onCreate', AS + '$AudioSearchWorker.doInBackground', 'ASYNC', 'mWorker.execute(query): the task runs doInBackground on a pool thread', env=ENV_PERM, guard='the action is MEDIA_PLAY_FROM_SEARCH and the permission check passed', evidence='SRC AudioSearchActivity.java:40-57, 70-77; ' + FW_ASYNC)
e(AS + '$AudioSearchWorker.doInBackground', AS + '$AudioSearchWorker.onPostExecute', 'ASYNC', 'the result is delivered on the main thread', evidence='SRC AudioSearchActivity.java:70-94; ' + FW_ASYNC)
e(AS + '$AudioSearchWorker.onPostExecute', 'S_EXIT', 'ENTERS', 'onSearchCompleted() finishes the activity', evidence='SRC AudioSearchActivity.java:60-65, 90-93')
# ShortcutPseudoActivity: one startService per action; the actions are variants of the service start
SP = 'ShortcutPseudoActivity'
lifecycle(SP, ('onCreate',), FW_ACT_CREATE, 'Activity lifecycle callback; SRC ShortcutPseudoActivity.java:44-82')
e(SP + '.<init>', SP + '.<clinit>', 'LIFECYCLE', 'class initialisation (INTENT_FLAGS constant)', evidence='SRC ShortcutPseudoActivity.java:27-28; INFERRED the JVM runs the static initialiser before first use (Java language rule)') if (SP + '.<clinit>') in METHODS else None
e(SP + '.onCreate', 'S_EXIT', 'ENTERS', 'finish(): the translucent activity ends at once', evidence='SRC ShortcutPseudoActivity.java:58')
# the widgets build the intents of ShortcutPseudoActivity (PendingIntent); the launcher fires them on a tap
e('ShortcutPseudoActivity.getIntent', SP + '.<init>', 'INTENT', 'new Intent(context, ShortcutPseudoActivity.class) is wrapped in a PendingIntent for the widget buttons; the launcher starts it on a tap', env=ENV_WIDGET_TAP,
  evidence='SRC ShortcutPseudoActivity.java:15-20; OneCellWidget.java:105-111; FourLongWidget.java:134-140; WidgetD.java:130-148; WidgetE.java:121-139')

# ---- E5. PermissionRequestActivity (storage permission flow): LibraryActivity.onCreate shows a warning banner when the permission is missing; tapping it starts this activity
PRA = 'PermissionRequestActivity'
lifecycle(PRA, ('onCreate',), FW_ACT_CREATE, 'Activity lifecycle callback; SRC PermissionRequestActivity.java:41-50')
e('PermissionRequestActivity.showWarning', PRA + '$1.onClick', 'FRAMEWORK', 'view.setOnClickListener(...): tap the storage-permission warning banner injected into the library layout', gui=['Tap the storage permission warning banner'],
  evidence=FW_VIEW_CLICK + '; SRC PermissionRequestActivity.java:96-105')
e(PRA + '.requestPermissions', PRA + '.<init>', 'INTENT', 'havePermissions is false: activity.startActivity(new Intent(activity, PermissionRequestActivity.class))', guard='havePermissions(activity) is false (the permission is still not granted)',
  evidence='SRC PermissionRequestActivity.java:118-126; ' + FW_ACT_CREATE)
e(PRA + '.onCreate', PRA + '.onRequestPermissionsResult', 'FRAMEWORK', 'requestPermissions(allPerms, 0): the system permission dialog result is delivered', evidence=FW_PERM + '; SRC PermissionRequestActivity.java:41-50, 60-61')


# ===================================================================== F. PlaybackService, widgets, receivers, job service, timeline callbacks
FW_SERVICE = ('FW-SRC core/java/android/app/ActivityThread.java:3321, 3339, 3474, 3504, 3366 '
              '(handleCreateService instantiates the service class and calls onCreate; handleServiceArgs calls onStartCommand; handleStopService calls onDestroy; handleBindService calls onBind)')
FW_SERVICE_STOP = ('FW-SRC services/core/java/com/android/server/am/ActivityManagerService.java:22975 and services/core/java/com/android/server/am/ActiveServices.java:562-580, 615-651, 2547 and core/java/android/app/ActivityThread.java:3504 '
                   '(when an app becomes idle in the background the system stops its started services (stopInBackgroundLocked) when its start mode is not normal, which schedules handleStopService, which calls onDestroy)')
FW_MP_EVENT = ('FW-SRC media/java/android/media/MediaPlayer.java:3235-3240, 3294-3306 '
               '(the EventHandler calls the OnCompletionListener for MEDIA_PLAYBACK_COMPLETE and the OnErrorListener for MEDIA_ERROR)')
FW_FOCUS = ('FW-SRC media/java/android/media/AudioManager.java:2136-2144 '
            '(the focus event handler calls OnAudioFocusChangeListener.onAudioFocusChange of the listener given to requestAudioFocus)')
FW_SENSOR = ('FW-SRC core/java/android/hardware/SystemSensorManager.java:826-830 '
             '(dispatchSensorEvent calls onAccuracyChanged and onSensorChanged of the SensorEventListener registered with registerListener)')
FW_PREF_LISTENER = ('FW-SRC core/java/android/app/SharedPreferencesImpl.java:551-561 '
                    '(after an edit is committed, notifyListeners calls onSharedPreferenceChanged(prefs, key) of every registered listener for each modified key)')
FW_DYNRECV = ('FW-SRC core/java/android/app/LoadedApk.java:1313 '
              '(the ReceiverDispatcher calls receiver.onReceive for a receiver registered with registerReceiver)')
FW_CONTENTOBS = ('FW-SRC core/java/android/database/ContentObserver.java:129-130, 194-199, 227-232 '
                 '(the content service calls Transport.onChange, which dispatches onChange(selfChange, uri, userId) and then onChange(selfChange) of the observer registered with registerContentObserver)')
FW_FILEOBS = ('FW-SRC core/java/android/os/FileObserver.java:106-123, 178 '
              '(after startWatching the observer thread calls onEvent of the FileObserver for each event of the watched path)')
ENV_BIND = env_text('outside package: another app binds the exported PlaybackService with bindService', 'other_app')
NEED_SHAKE_ON = state_text('Settings > Shake > "Enable shake" is on (default off) and an action is chosen', 'settings')
NEED_MEDIASESSION = state_text('The media session of the service is active (the service ran updateSession at least once)', 'session')
SV = 'PlaybackService'
sup(SV + '.onStartCommand', SV + '.handleMessage')
e(SV + '.<init>', SV + '.<clinit>', 'LIFECYCLE', 'class initialisation (static callback list and lock)', evidence='SRC PlaybackService.java:285-293; INFERRED the JVM runs the static initialiser before first use (Java language rule, not read from a source)')
e(SV + '.<init>', SV + '.onCreate', 'LIFECYCLE', 'the system creates the service and calls onCreate', evidence=FW_SERVICE + '; SRC PlaybackService.java:441-533')
e(SV + '.<init>', SV + '.onStartCommand', 'LIFECYCLE', 'the start request is delivered with onStartCommand', evidence=FW_SERVICE + '; SRC PlaybackService.java:535-606')
e('S_LIBRARY_PAUSED', SV + '.onDestroy', 'SYSTEM', 'time passes with the app in the background: the system stops the idle service', env=ENV_KILL, evidence=FW_SERVICE_STOP + '; SRC PlaybackService.java:608-654')
e(SV + '.<init>', SV + '.onDestroy', 'LIFECYCLE', 'the idle background service is stopped by the system', env=ENV_KILL, evidence=FW_SERVICE_STOP + '; SRC PlaybackService.java:608-654')
e(SV + '.<init>', SV + '.onBind', 'LIFECYCLE', 'another app binds the exported service', env=ENV_BIND, evidence=FW_SERVICE + '; SRC AndroidManifest.xml:171-181; PlaybackService.java:1707-1711')
e(SV + '.get', SV + '.<init>', 'INTENT', 'context.startService(new Intent(context, PlaybackService.class)) when sInstance == null; the caller waits until the service is created', guard='sInstance == null',
  evidence='SRC PlaybackService.java:1956-1971; AndroidManifest.xml:171-181; ' + FW_SERVICE)
# onCreate: callbacks registered by the service
e(SV + '.onCreate', SV + '.onSharedPreferenceChanged', 'FRAMEWORK', 'settings.registerOnSharedPreferenceChangeListener(this): a preference value changes while the service runs (another screen of the app writes a preference)',
  needs_state=NEED_PREF_CHANGED, evidence=FW_PREF_LISTENER + '; SRC PlaybackService.java:462-463')
e(SV + '.onCreate', SV + '$Receiver.<init>', 'CALL', 'mReceiver = new Receiver()', evidence='SRC PlaybackService.java:497 (bytecode)')
e(SV + '.onCreate', SV + '$Receiver.onReceive', 'FRAMEWORK', 'registerReceiver(mReceiver, filter): AUDIO_BECOMING_NOISY and SCREEN_ON broadcasts call onReceive', env=ENV_NOISY, evidence='SRC PlaybackService.java:497-501; ' + FW_DYNRECV)
e(SV + '.onCreate', 'MediaSessionTracker$1.onPlay', 'FRAMEWORK', 'new MediaSessionTracker(this) registers the MediaSession callback; a media controller command calls it', env=ENV_MEDIASESSION, evidence='SRC PlaybackService.java:508; MediaSessionTracker.java:47-76; INFERRED androidx MediaSessionCompat calls MediaSessionCompat.Callback for controller commands (androidx source not read)', cls='non_standard', via='androidx MediaSessionCompat calls the Callback')
for cb in ('onPause', 'onSkipToNext', 'onSkipToPrevious', 'onStop', 'onSeekTo'):
    e(SV + '.onCreate', 'MediaSessionTracker$1.' + cb, 'FRAMEWORK', 'a media controller command calls MediaSessionCompat.Callback.' + cb, env=ENV_MEDIASESSION, evidence='SRC MediaSessionTracker.java:47-76; INFERRED androidx MediaSessionCompat calls MediaSessionCompat.Callback for controller commands (androidx source not read)', cls='non_standard', via='androidx MediaSessionCompat calls the Callback')
e(SV + '.getNewMediaPlayer', SV + '.onCompletion', 'FRAMEWORK', 'mp.setOnCompletionListener(this): the song reached its end', needs_state=NEED_PLAYING, evidence='SRC PlaybackService.java:659-665; ' + FW_MP_EVENT)
e(SV + '.getNewMediaPlayer', SV + '.onError', 'FRAMEWORK', 'mp.setOnErrorListener(this): the media player reports an error', needs_state=NEED_PLAYING, env=ENV_EXC, evidence='SRC PlaybackService.java:659-665; ' + FW_MP_EVENT)
e(SV + '.processNewState', SV + '.onAudioFocusChange', 'FRAMEWORK', 'mAudioManager.requestAudioFocus(this, ...): focus changes call onAudioFocusChange', env=ENV_FOCUS, evidence='SRC PlaybackService.java:1035-1038; ' + FW_FOCUS)
e(SV + '.setupSensor', SV + '.onSensorChanged', 'FRAMEWORK', 'registerListener(this, accelerometer, SENSOR_DELAY_UI): sensor events call onSensorChanged', env=ENV_SENSOR, needs_state=NEED_SHAKE_ON, guard='mShakeAction != Action.Nothing', evidence='SRC PlaybackService.java:855-865; ' + FW_SENSOR)
e(SV + '.setupSensor', SV + '.onAccuracyChanged', 'FRAMEWORK', 'registerListener(this, ...): the sensor reports an accuracy change', env=ENV_SENSOR, needs_state=NEED_SHAKE_ON, guard='mShakeAction != Action.Nothing', evidence='SRC PlaybackService.java:855-865, 2228-2231; ' + FW_SENSOR)
# the service handler: messages sent by the service code
SV_B = [b for b in CS.branches('PlaybackService.java', 'handleMessage') if b[0] != 'MSG_CALL_GO'] + [('MSG_CALL_GO_PLAY', 1548, 1549), ('MSG_CALL_GO_SHIFT', 1550, 1551)]   # arg1 == 0: playPause; else setCurrentSong(arg1)
SV_H = variants_of(SV + '.handleMessage', 'PlaybackService.java', 'handleMessage', bounds=SV_B, names={l: l for l, a, b in SV_B}, skip=('default',), text='call made in the message branch')
SVH = SV + '.handleMessage'
SV_SENDS = [
    (SV + '.preparePlayCountsUpdate', 'MSG_UPDATE_PLAYCOUNTS', 'SRC PlaybackService.java:678-693', dict(guard='isPlaying() and (SHIFT_KEEP_SONG with 80% played, or SHIFT_NEXT_SONG with at most 50% played)', needs_state=NEED_PLAYING)),
    (SV + '.updateState', 'MSG_PROCESS_STATE', 'SRC PlaybackService.java:1000-1014', dict(guard='state != oldState')),
    (SV + '.updateState', 'MSG_BROADCAST_CHANGE', 'SRC PlaybackService.java:1000-1014', dict(guard='state != oldState')),
    (SV + '.processNewState', 'MSG_ENTER_SLEEP_STATE', 'SRC PlaybackService.java:1047-1064', dict(guard='FLAG_PLAYING was cleared and a song is loaded: the sleep state is entered after 60 s', needs_state=NEED_PLAYING)),
    (SV + '.showToast(int,int)', 'MSG_SHOW_TOAST', 'SRC PlaybackService.java:1195-1197', {}),
    (SV + '.showToast(CharSequence,int)', 'MSG_SHOW_TOAST', 'SRC PlaybackService.java:1199-1201', {}),
    (SV + '.setCurrentSong', 'MSG_PROCESS_SONG', 'SRC PlaybackService.java:1342-1353', dict(guard='mTimeline.shiftCurrentSong returned a song (song != null)', needs_state=NEED_QUEUE)),
    (SV + '.setCurrentSong', 'MSG_BROADCAST_CHANGE', 'SRC PlaybackService.java:1352', dict(guard='song != null', needs_state=NEED_QUEUE)),
    (SV + '.processSong', 'MSG_GAPLESS_UPDATE', 'SRC PlaybackService.java:1378-1382', dict(guard='the song was prepared (no IOException)', needs_state=NEED_PLAYING)),
    (SV + '.processSong', 'MSG_SKIP_BROKEN_SONG', 'SRC PlaybackService.java:1400-1412', dict(guard='IOException while preparing, not at the end of the queue and (playing or a broken song was skipped already)', env=ENV_EXC, needs_state=NEED_QUEUE)),
    (SV + '.onCompletion', 'MSG_UPDATE_PLAYCOUNTS', 'SRC PlaybackService.java:1419-1424', dict(needs_state=NEED_PLAYING)),
    (SV + '.seekToPosition', 'MSG_BROADCAST_SEEK', 'SRC PlaybackService.java:1699-1705', dict(guard='mMediaPlayerInitialized', needs_state=NEED_PLAYING)),
    (SV + '.userActionTriggered', 'MSG_IDLE_TIMEOUT', 'SRC PlaybackService.java:1787-1792', dict(guard='mIdleTimeout != 0', needs_state=state_text('Settings > Misc > "Idle timeout" is on (use_idle_timeout; default off)', 'settings'))),
    (SV + '.addSongs', 'MSG_QUERY', 'SRC PlaybackService.java:1844-1847', {}),
    (SV + '.timelineChanged', 'MSG_SAVE_STATE', 'SRC PlaybackService.java:1913-1917', {}),
    (SV + '.timelineChanged', 'MSG_GAPLESS_UPDATE', 'SRC PlaybackService.java:1922-1923', {}),
]
for i, (site, lab, ev, g) in enumerate(SV_SENDS):
    send(site, SVH, SV_H, lab, lab, ev, plain=(i == 0 or site not in [s[0] for s in SV_SENDS[:i]] or True), **g)
send(SV_H['MSG_IDLE_TIMEOUT'], SVH, SV_H, 'MSG_FADE_OUT', 'MSG_FADE_OUT', 'SRC PlaybackService.java:1564-1568', guard='(mState & FLAG_PLAYING) != 0', needs_state=NEED_PLAYING)
send(SV_H['MSG_FADE_OUT'], SVH, SV_H, 'MSG_FADE_OUT', 'MSG_FADE_OUT (delayed 50 ms)', 'SRC PlaybackService.java:1569-1578', guard='mFadeOut > 0')

# ---- F2. onStartCommand: one variant per action (the intent action is data carried by the start request)
OSC = SV + '.onStartCommand'
OSC_B = [('EARLY', 542, 545), ('TOGGLE_PLAYBACK', 547, 548), ('TOGGLE_PLAYBACK_DELAYED', 549, 558), ('NEXT_SONG', 559, 560), ('NEXT_SONG_AUTOPLAY', 561, 563), ('NEXT_SONG_DELAYED', 564, 573),
         ('PREVIOUS_SONG', 574, 575), ('PREVIOUS_SONG_AUTOPLAY', 576, 578), ('PLAY', 579, 580), ('PAUSE', 581, 582), ('CYCLE_REPEAT', 583, 584), ('CYCLE_SHUFFLE', 585, 586),
         ('RANDOM_MIX_AUTOPLAY', 587, 594), ('FROM_TYPE_ID_AUTOPLAY', 595, 602)]
OSC_V = variants_of(OSC, 'PlaybackService.java', 'onStartCommand', bounds=OSC_B, text='call made for this start action')
OSC_EV = 'SRC PlaybackService.java:536-606'
for lab in ('TOGGLE_PLAYBACK_DELAYED', 'NEXT_SONG_DELAYED'):
    pass
e(OSC_V['TOGGLE_PLAYBACK_DELAYED'], 'LibraryActivity.<init>', 'INTENT', 'a second TOGGLE_PLAYBACK_DELAYED within 400 ms: startActivity(LibraryActivity, ACTION_MAIN, NEW_TASK)', guard='mHandler.hasMessages(MSG_CALL_GO, 0) (the first tap is still pending)', evidence='SRC PlaybackService.java:549-556; ' + FW_ACT_CREATE)
e(OSC_V['NEXT_SONG_DELAYED'], 'LibraryActivity.<init>', 'INTENT', 'a second NEXT_SONG_DELAYED within 400 ms: startActivity(LibraryActivity, ACTION_MAIN, NEW_TASK)', guard='mHandler.hasMessages(MSG_CALL_GO, 1) (the first tap is still pending)', evidence='SRC PlaybackService.java:564-571; ' + FW_ACT_CREATE)
for lab in ('TOGGLE_PLAYBACK_DELAYED', 'NEXT_SONG_DELAYED'):
    e(OSC_V[lab], LA + '.onNewIntent', 'INTENT', 'the library task exists: onNewIntent with the ACTION_MAIN intent', needs_state=state_text('LibraryActivity runs in the back stack (launchMode singleTask)', 'session'), evidence='SRC PlaybackService.java:549-571; AndroidManifest.xml:73-77; ' + FW_ACT_NEWINTENT)
send(OSC_V['TOGGLE_PLAYBACK_DELAYED'], SVH, SV_H, 'MSG_CALL_GO_PLAY', 'MSG_CALL_GO with arg1 = 0 (delayed 400 ms)', 'SRC PlaybackService.java:556-558', guard='no pending first tap')
send(OSC_V['NEXT_SONG_DELAYED'], SVH, SV_H, 'MSG_CALL_GO_SHIFT', 'MSG_CALL_GO with arg1 = 1 (delayed 400 ms)', 'SRC PlaybackService.java:571-573', guard='no pending first tap')
send(OSC_V['RANDOM_MIX_AUTOPLAY'], SVH, SV_H, 'MSG_CALL_GO_PLAY', 'MSG_CALL_GO with arg1 = 0', 'SRC PlaybackService.java:587-594')
send(SV_H['MSG_SKIP_BROKEN_SONG'], SVH, SV_H, 'MSG_CALL_GO_PLAY', 'MSG_CALL_GO with arg1 = 0', 'SRC PlaybackService.java:1601', plain=False)
# callers of onStartCommand
START_NOTE = 'startService / startForegroundService / PendingIntent.getService delivers the intent with onStartCommand'
e(SV + '.<init>', OSC_V['EARLY'], 'CALL', 'the start intent has EXTRA_EARLY_NOTIFICATION (MediaButtonReceiver.runAction): a foreground notification is created at once', guard='intent.hasExtra(EXTRA_EARLY_NOTIFICATION)', env=ENV_MEDIAKEY, evidence=OSC_EV)
for act, who in (('TOGGLE_PLAYBACK', 'notification play/pause button, widget buttons, media button'), ('NEXT_SONG', 'notification next button, widget next button, external intent'), ('PREVIOUS_SONG', 'notification previous button, widget previous button, external intent')):
    e(SV + '.createNotification', OSC_V[act], 'INTENT', 'PendingIntent.getService: the notification button (%s) starts the service with ACTION_%s' % (act.lower(), act), env=ENV_NOTIF, needs_state=NEED_NOTIFICATION, evidence='SRC PlaybackService.java:2113-2146; ' + FW_SERVICE)
for act in ('PLAY', 'PAUSE', 'TOGGLE_PLAYBACK', 'NEXT_SONG', 'PREVIOUS_SONG'):
    e(SV + '.<init>', OSC_V[act], 'LIFECYCLE', 'another app started the exported service with ACTION_' + act, env=ENV_SERVICE_EXT, evidence='SRC AndroidManifest.xml:171-181; PlaybackService.java:535-606; ' + FW_SERVICE)
for act, ev_ in (('TOGGLE_PLAYBACK', 'MediaButtonReceiver.java:50-63'), ('NEXT_SONG_AUTOPLAY', 'MediaButtonReceiver.java:65-68'), ('PREVIOUS_SONG_AUTOPLAY', 'MediaButtonReceiver.java:69-72'), ('PLAY', 'MediaButtonReceiver.java:73-76'), ('PAUSE', 'MediaButtonReceiver.java:77-82')):
    e('MediaButtonReceiver.runAction', OSC_V[act], 'INTENT', 'context.startForegroundService(intent with action ACTION_%s, EXTRA_FORCE_NOTIFICATION and EXTRA_EARLY_NOTIFICATION)' % act, env=ENV_MEDIAKEY, guard='the key code maps to this action', evidence='SRC MediaButtonReceiver.java:98-107; ' + ev_ + '; ' + FW_SERVICE)
e('MediaButtonReceiver.runAction', SV + '.<init>', 'INTENT', 'context.startForegroundService(intent) creates the service when it does not run', env=ENV_MEDIAKEY, guard='PlaybackService does not run', evidence='SRC MediaButtonReceiver.java:98-107; ' + FW_SERVICE)
e('MediaButtonReceiver.runAction', OSC, 'INTENT', 'onStartCommand(intent) of the running service', env=ENV_MEDIAKEY, evidence='SRC MediaButtonReceiver.java:98-107; ' + FW_SERVICE)
e(SV + '.createNotificationAction', OSC_V['NEXT_SONG_AUTOPLAY'], 'INTENT', 'notification action "skip to next song": PendingIntent.getService with ACTION_NEXT_SONG_AUTOPLAY', env=ENV_NOTIF, needs_state=NEED_NOTIF_ACTION_NEXT, evidence='SRC PlaybackService.java:2080-2085; ' + FW_SERVICE)
e(SV + '.createNotificationAction', MP + '.<init>', 'INTENT', 'notification action "open mini popup": PendingIntent.getActivity(MiniPlaybackActivity)', env=ENV_NOTIF, needs_state=NEED_NOTIF_ACTION_MINI, evidence='SRC PlaybackService.java:2086-2089; ' + FW_ACT_CREATE)
e(SV + '.createNotificationAction', FP + '.<init>', 'INTENT', 'notification action "open full player": PendingIntent.getActivity(FullPlaybackActivity, ACTION_MAIN)', env=ENV_NOTIF, needs_state=NEED_NOTIF_ACTION_FULL, evidence='SRC PlaybackService.java:2098-2101; ' + FW_ACT_CREATE)
e(SV + '.createNotificationAction', LA + '.<init>', 'INTENT', 'default notification action: PendingIntent.getActivity(LibraryActivity, ACTION_MAIN)', env=ENV_NOTIF, needs_state=NEED_NOTIFICATION, evidence='SRC PlaybackService.java:2090-2097; PrefDefaults.java:53; ' + FW_ACT_CREATE)
e(SV + '.createNotificationAction', LA + '.onNewIntent', 'INTENT', 'default notification action: the library task exists, onNewIntent with ACTION_MAIN', env=ENV_NOTIF, needs_state=NEED_NOTIFICATION, evidence='SRC PlaybackService.java:2090-2097; ' + FW_ACT_NEWINTENT)
# the shortcut activity starts the service with the action of its own intent (static shortcuts, widget buttons, pinned shortcuts)
for act, why in (('TOGGLE_PLAYBACK', 'shortcut "play", widget buttons'), ('TOGGLE_PLAYBACK_DELAYED', 'widget with double tap enabled'), ('RANDOM_MIX_AUTOPLAY', 'shortcut "random"'), ('NEXT_SONG', 'widget next button'),
                 ('NEXT_SONG_DELAYED', 'widget with double tap enabled'), ('PREVIOUS_SONG', 'widget previous button'), ('CYCLE_SHUFFLE', 'widget shuffle button'), ('CYCLE_REPEAT', 'widget repeat button'),
                 ('FROM_TYPE_ID_AUTOPLAY', 'pinned shortcut of a library row')):
    # cls='standard' (checked, not a REVIEW false positive): the Intent names the target component explicitly (PlaybackService.class); the action string is read only by this app's own
    # onStartCommand switch (not used by the OS to resolve the target), so this is an explicit-component intent, not an action-resolved one.
    e(SP + '.onCreate', OSC_V[act], 'INTENT', 'startService(new Intent(this, PlaybackService.class).setAction(ACTION_%s)) (%s)' % (act, why), env=ENV_SHORTCUT if act in ('RANDOM_MIX_AUTOPLAY', 'FROM_TYPE_ID_AUTOPLAY') else ENV_WIDGET_TAP,
      guard='the intent action of ShortcutPseudoActivity is ACTION_' + act, evidence='SRC ShortcutPseudoActivity.java:44-82; res/xml/shortcuts.xml:3-26; ' + FW_SERVICE, cls='standard')
e(SP + '.onCreate', SV + '.<init>', 'INTENT', 'startService(...) creates the service when it does not run', env=ENV_SHORTCUT, guard='PlaybackService does not run', evidence='SRC ShortcutPseudoActivity.java:44-82; ' + FW_SERVICE)
e(SP + '.onCreate', OSC, 'INTENT', 'startService(...): onStartCommand of the running service', env=ENV_SHORTCUT, evidence='SRC ShortcutPseudoActivity.java:44-82; ' + FW_SERVICE)


# ---- F3. performAction (gesture actions), preferences, timeline callbacks
SCREENS.update({
    'S_PREFS': 'PreferencesActivity: list of the settings sections (Audio, Playback, Library, Notifications, Shake, Cover art, Misc, Media library, Playlists, Theme, Help, About)',
    'S_PREFS_AUDIO': 'Settings > Audio: Equalizer, Replay gain, volume while ducking, gapless playback, headset only, pause on headset unplug, headset launch',
    'S_PREFS_REPLAYGAIN': 'Settings > Audio > Replay gain: track gain, album gain, bump and untagged de-bump',
    'S_PREFS_PLAYBACK': 'Settings > Playback: playback on startup, display mode, swipe up / down action, cover press / long-press action',
    'S_PREFS_LIBRARY': 'Settings > Library: tabs, default action, default playlist action, scroll to song, jump to enqueued song, file browser start folder',
    'S_PREFS_NOTIFICATIONS': 'Settings > Notifications: notification visibility, notification action',
    'S_PREFS_SHAKE': 'Settings > Accelerometer shake: enable, action, threshold',
    'S_PREFS_COVERART': 'Settings > Cover art: cover loaders (Vanilla, shadow, Android, inline) and cover on the lock screen',
    'S_PREFS_MISC': 'Settings > Misc features: lock screen, keep screen on, idle timeout, double tap on widgets, scrobbling, stock broadcast, readahead',
    'S_PREFS_MEDIALIB': 'Settings > Media library: scan buttons, statistics, options, media folders (PreferencesMediaLibrary)',
    'S_PREFS_PLAYLIST': 'Settings > Playlists: auto playlist, synchronization mode, sync folder, relative paths',
    'S_PREFS_THEME': 'Settings > Theme: list of themes with a colour preview',
    'S_PREFS_ABOUT': 'Settings > About: web view of about.html',
})
SPA = SV + '.performAction'
SPA_B = CS.branches('PlaybackService.java', 'performAction')
SPA_V = variants_of(SPA, 'PlaybackService.java', 'performAction', bounds=SPA_B, names={l: l for l, a, b in SPA_B}, skip=('default',), text='call made for this action')
e(SPA_V['Library'], 'LibraryActivity.<init>', 'INTENT', 'startActivity(LibraryActivity, CLEAR_TOP | NEW_TASK)', guard='no library task exists', evidence='SRC PlaybackService.java:2247-2251; ' + FW_ACT_CREATE)
e(SPA_V['Library'], LA + '.onNewIntent', 'INTENT', 'startActivity(LibraryActivity, CLEAR_TOP | NEW_TASK): the running library gets onNewIntent', needs_state=state_text('LibraryActivity runs in the back stack (launchMode singleTask)', 'session'), evidence='SRC PlaybackService.java:2247-2251; ' + FW_ACT_NEWINTENT)
sup((PBA + '.performAction', SPA))
call(PBA + '.performAction', SPA, 'PlaybackService.get(this).performAction(action, this)', 'SRC PlaybackActivity.java:668-671 (bytecode)')
for lab, a_, b_ in SPA_B:
    if lab == 'default':
        continue
    g = {} if lab == 'Nothing' else dict(needs_state=NEED_ACTION_PREF)
    call(PBA + '.performAction', SPA_V[lab], 'the configured gesture action is %s' % lab, 'SRC PlaybackService.java:%d-%d; PlaybackActivity.java:656-671' % (a_, b_), guard='the action preference (swipe up / down, cover press / long press) is ' + lab, **g)
    call(SV + '.onSensorChanged', SPA_V[lab], 'the shake action is %s' % lab, 'SRC PlaybackService.java:2219-2224, %d-%d' % (a_, b_), guard='the shake action is ' + lab, env=ENV_SENSOR, needs_state=NEED_SHAKE_ON)
sup((SV + '.onSensorChanged', SPA))
call(SV + '.onSensorChanged', SPA, 'performAction(mShakeAction, null) after a shake', 'SRC PlaybackService.java:2219-2224 (bytecode)', env=ENV_SENSOR, needs_state=NEED_SHAKE_ON, guard='filtered acceleration above the threshold and 500 ms since the last shake')
# preferences: the SharedPreferences listener of the service calls loadPreference (one variant per key)
LP_B = CS.branches('PlaybackService.java', 'loadPreference')
LP_N = {}
for l, a_, b_ in LP_B:
    ks = re.findall(r'PrefKeys\.([A-Z_]+)', l)
    LP_N[l] = ks[0] if len(ks) == 1 else '_OR_'.join(ks)
LPV = variants_of(SV + '.loadPreference', 'PlaybackService.java', 'loadPreference', bounds=LP_B, names=LP_N, text='call made for this preference key')
LPV_BYKEY = {}
for l, a_, b_ in LP_B:
    for k in re.findall(r'PrefKeys\.([A-Z_]+)', l):
        LPV_BYKEY[k] = LPV[l]
PREF_SCREENS = {
    'AUDIO': ('S_PREFS_AUDIO', ['VOLUME_DURING_DUCKING', 'IGNORE_AUDIOFOCUS_LOSS', 'DISABLE_GAPLESS_PLAYBACK', 'HEADSET_ONLY', 'HEADSET_PAUSE']),
    'REPLAYGAIN': ('S_PREFS_REPLAYGAIN', ['ENABLE_TRACK_REPLAYGAIN', 'ENABLE_ALBUM_REPLAYGAIN', 'REPLAYGAIN_BUMP', 'REPLAYGAIN_UNTAGGED_DEBUMP']),
    'PLAYBACK': ('S_PREFS_PLAYBACK', ['DISPLAY_MODE']),
    'NOTIFICATIONS': ('S_PREFS_NOTIFICATIONS', ['NOTIFICATION_VISIBILITY', 'NOTIFICATION_ACTION']),
    'SHAKE': ('S_PREFS_SHAKE', ['ENABLE_SHAKE', 'SHAKE_ACTION', 'SHAKE_THRESHOLD']),
    'COVERART': ('S_PREFS_COVERART', ['COVERLOADER_ANDROID', 'COVERLOADER_VANILLA', 'COVERLOADER_SHADOW', 'COVER_ON_LOCKSCREEN']),
    'MISC': ('S_PREFS_MISC', ['USE_IDLE_TIMEOUT', 'IDLE_TIMEOUT', 'SCROBBLE', 'STOCK_BROADCAST', 'ENABLE_READAHEAD']),
    'PLAYLIST': ('S_PREFS_PLAYLIST', ['AUTOPLAYLIST_PLAYCOUNTS', 'PLAYLIST_SYNC_MODE', 'PLAYLIST_SYNC_FOLDER', 'PLAYLIST_EXPORT_RELATIVE_PATHS']),
    'THEME': ('S_PREFS_THEME', ['SELECTED_THEME']),
}
OSPC = SV + '.onSharedPreferenceChanged'
sup((OSPC, SV + '.loadPreference'))
e(OSPC, SV + '.loadPreference', 'CALL', 'loadPreference(key)', evidence='SRC PlaybackService.java:1494-1497 (bytecode)')
OSPC_V = {}
for nm, (pg, keys) in PREF_SCREENS.items():
    OSPC_V[nm] = OSPC + '@' + nm
    e(pg, OSPC_V[nm], 'FRAMEWORK', 'a preference of this settings screen changes while the service runs (settings.registerOnSharedPreferenceChangeListener(this))',
      needs_state=NEED_PREF_CHANGED, evidence=FW_PREF_LISTENER + '; SRC PlaybackService.java:462-463, 868-945')
    call(OSPC_V[nm], SV + '.loadPreference', 'loadPreference(key)', 'SRC PlaybackService.java:1494-1497 (bytecode)')
    for k in keys:
        e(OSPC_V[nm], LPV_BYKEY[k], 'CALL', 'the changed preference is %s' % k, guard='key equals PrefKeys.' + k, evidence='SRC PlaybackService.java:868-945')


# ---- F4. widgets, media button receiver, job service, library observers
FW_JOB = ('FW-SRC core/java/android/app/job/JobService.java:66-80 and core/java/android/app/job/JobServiceEngine.java:77, 86, 103-118 '
          '(the JobScheduler binds the service; the JobServiceEngine posts MSG_EXECUTE_JOB / MSG_STOP_JOB, whose handler calls onStartJob / onStopJob of the service)')
ENV_JOB_STOP = env_text('time passes and the job constraints stop holding (the device is used or unplugged): JobScheduler stops job 9', 'time', 'hardware')
WIDGETS = ('OneCellWidget', 'FourLongWidget', 'FourSquareWidget', 'FourWhiteWidget', 'WidgetD', 'WidgetE')
for w, ev_ in (('FourLongWidget', 'FourLongWidget.java:129-132'), ('FourSquareWidget', 'FourSquareWidget.java:131-134'), ('FourWhiteWidget', 'FourWhiteWidget.java:137-140'), ('WidgetD', 'WidgetD.java:126-128'), ('WidgetE', 'WidgetE.java:116-119')):
    e(w + '.updateWidget', LA + '.<init>', 'INTENT', 'PendingIntent.getActivity(LibraryActivity, ACTION_MAIN) on the cover / text of the widget: a tap starts the library', env=ENV_WIDGET_TAP, guard='sEnabled (a widget of this type is placed)', evidence='SRC ' + ev_ + '; ' + FW_ACT_CREATE)
    e(w + '.updateWidget', LA + '.onNewIntent', 'INTENT', 'the library task exists: onNewIntent with ACTION_MAIN', env=ENV_WIDGET_TAP, needs_state=state_text('LibraryActivity runs in the back stack (launchMode singleTask)', 'session'), guard='sEnabled', evidence='SRC ' + ev_ + '; ' + FW_ACT_NEWINTENT)
# media button
MBR = 'MediaButtonReceiver'
e(MBR + '.processKey', MBR + '$DelayedClickCounter.<init>', 'CALL', 'new DelayedClickCounter(context, time) for a second play / pause key within 600 ms', guard='action == ACTION_DOWN and time - sLastClickTime < DOUBLE_CLICK_DELAY',
  needs_state=state_text('A play / pause key press happened less than 600 ms ago (double click on the headset button)', 'session'), evidence='SRC MediaButtonReceiver.java:72-80 (bytecode)')
e(MBR + '.processKey', MBR + '$DelayedClickCounter.run', 'ASYNC', 'handler.postDelayed(dcc, 600): the click counter runs on the main looper', guard='double click',
  needs_state=state_text('A play / pause key press happened less than 600 ms ago (double click on the headset button)', 'session'), evidence='SRC MediaButtonReceiver.java:72-80; ' + FW_HANDLER)
# the job service
SL = 'ScheduledLibraryUpdate'
e(SL + '.<init>', SL + '.onStartJob', 'LIFECYCLE', 'the JobScheduler starts the job: onStartJob', env=ENV_JOB, evidence=FW_JOB + '; SRC ScheduledLibraryUpdate.java:71-83')
e(SL + '.<init>', SL + '.onStopJob', 'LIFECYCLE', 'the JobScheduler stops the running job: onStopJob', env=ENV_JOB_STOP, evidence=FW_JOB + '; SRC ScheduledLibraryUpdate.java:91-95')
e(SL + '.<init>', SL + '$1.<init>', 'CALL', 'the service builds its LibraryObserver field', env=ENV_JOB, evidence='SRC ScheduledLibraryUpdate.java:112-120 (bytecode)')
# library observers: MediaLibrary.notifyObserver reaches the registered observers only
LO = 'MediaLibrary.notifyObserver'
sup((LO, 'PlaybackService$1.onChange'), (LO, 'PlaylistObserver$1.onChange'), (LO, 'PreferencesMediaLibrary$1.onChange'), (LO, 'ScheduledLibraryUpdate$1.onChange'))
OBS_REG = state_text('The observer is registered: MediaLibrary.registerLibraryObserver was called and not yet undone', 'session')
e(LO, 'PlaybackService$1.onChange', 'CALL', 'list.get(i).onChange(type, id, ongoing) for the observer of the service (registered in PlaybackService.onCreate)', guard='the PlaybackService runs', needs_state=NEED_SERVICE_UP, evidence='SRC MediaLibrary.java:355-359; PlaybackService.java:503')
e(LO, 'PlaylistObserver$1.onChange', 'CALL', 'list.get(i).onChange(type, id, ongoing) for the observer of the playlist synchronisation (registered in the PlaylistObserver constructor)', guard='the PlaybackService runs', needs_state=NEED_SERVICE_UP, evidence='SRC MediaLibrary.java:355-359; PlaylistObserver.java:138')
e(LO, 'PreferencesMediaLibrary$1.onChange', 'CALL', 'list.get(i).onChange(type, id, ongoing) for the observer of the media library settings screen (registered in onResume)', guard='PreferencesMediaLibrary is resumed',
  needs_state=state_text('The media library settings screen is open (PreferencesMediaLibrary is resumed)', 'session'), evidence='SRC MediaLibrary.java:355-359; PreferencesMediaLibrary.java:156-175')
e(LO, 'ScheduledLibraryUpdate$1.onChange', 'CALL', 'list.get(i).onChange(type, id, ongoing) for the observer of the running job (registered in onStartJob)', guard='the library update job runs', env=ENV_JOB, evidence='SRC MediaLibrary.java:355-359; ScheduledLibraryUpdate.java:79')
e('PreferencesMediaLibrary$1.onChange', 'PreferencesMediaLibrary$1$1.run', 'ASYNC', 'getActivity().runOnUiThread(runnable): updateProgress() runs on the UI thread', guard='type == LibraryObserver.Type.SCAN_PROGRESS',
  evidence=FW_RUNUI + '; SRC PreferencesMediaLibrary.java:110-118')
e('ReadaheadThread.setSong', 'ReadaheadThread.handleMessage', 'ASYNC', 'pause() cancels pending messages, then mHandler.sendMessageDelayed(mHandler.obtainMessage(MSG_SET_SONG, song), 1000)', evidence=FW_HANDLER + '; SRC ReadaheadThread.java:75-78')


# ===================================================================== G. preferences, folder pickers, tab order, playlist activity, dialogs
# ---- G1. PlaylistActivity (opened from LibraryActivity.editPlaylist, the Playlists tab)
PA = 'PlaylistActivity'
lifecycle(PA, ('onCreate', 'onStart', 'onDestroy'), FW_ACT_CREATE, 'Activity lifecycle callback; SRC PlaylistActivity.java:102-147')
e(PA + '.<init>', PA + '.<clinit>', 'LIFECYCLE', 'class initialisation (static array MODE_FOR_ACTION)',
  evidence='SRC PlaylistActivity.java:64-67; INFERRED the JVM runs the static initialiser before the first use of the class (Java language rule, not read from a source)')
e(PA + '.onCreate', 'S_PLAYLIST', 'ENTERS', 'the playlist songs are shown (cold start: onNewIntent(getIntent()) sets the title and the adapter query)', evidence='SRC PlaylistActivity.java:102-158')
inflate(PA + '.onCreate', ['DragSortListView.<init>'], 'playlist_activity.xml')
inflate('PlaylistAdapter.newView', ['DraggableRow', 'LazyCoverView'], 'draggable_row.xml')
gui('S_PLAYLIST', PA + '.onOptionsItemSelected', 'Tap the Up/Back arrow of the action bar', evidence=FW_ACT_MENU + '; SRC PlaylistActivity.java:307-314')
# LazyCoverView: a 'song-aware' ImageView inflated as a child of every DraggableRow (draggable_row.xml); setCover is called by every adapter that binds a row (PlaylistAdapter, ShowQueueAdapter, MediaAdapter, FileSystemAdapter)
e('DragSortListView$AdapterWrapper.getView', 'LazyCoverView.setCover', 'CALL', 'row.getCoverView().setCover(type, id, title): the row cover is requested after the row view is bound', evidence='SRC PlaylistAdapter.java:122-124; ShowQueueAdapter.java:136; MediaAdapter.java:554 (bytecode)')
e('LazyCoverView.setCover', 'LazyCoverView.handleMessage', 'ASYNC', 'cache miss: sHandler.sendMessage(sHandler.obtainMessage(MSG_CREATE_COVER, payload)): the worker handler thread builds the cover', evidence=FW_HANDLER + '; SRC LazyCoverView.java:174-180')
e('LazyCoverView.handleMessage', 'LazyCoverView.handleMessage', 'ASYNC', 'MSG_CREATE_COVER: sUiHandler.sendMessage(sUiHandler.obtainMessage(MSG_DRAW_COVER, payload)): the cover is drawn on the UI thread', guard='message.what == MSG_CREATE_COVER and payload.isRecent()',
  evidence=FW_HANDLER + '; SRC LazyCoverView.java:124-156')
NEED_PLAYLIST_SONGS = state_text('The open playlist has at least one song (Add to playlist was used on a song of the library)', 'data')
gui('S_PLAYLIST', PA + '.onClick(View)', 'Tap "Edit" in the header', evidence='SRC PlaylistActivity.java:121-125, 176-193; ' + FW_VIEW_CLICK)
gui('S_PLAYLIST_EDIT', PA + '.onClick(View)', 'Tap "Done" or "Delete" in the header', evidence='SRC PlaylistActivity.java:121-125, 176-193; ' + FW_VIEW_CLICK)
e(PA + '.onClick(View)', 'S_DLG_PLAYLIST_DELETE', 'ENTERS', 'tap "Delete": the confirm AlertDialog is shown', guard='view.getId() == R.id.delete', evidence='SRC PlaylistActivity.java:183-190')
gui('S_DLG_PLAYLIST_DELETE', PA + '.onClick(DialogInterface,int)', 'Tap "Delete" or "Cancel" in the confirm dialog', evidence='SRC PlaylistActivity.java:184-188, 297-305; ' + FW_DLG_BUTTON)
e(PA + '.setEditing', 'S_PLAYLIST_EDIT', 'ENTERS', 'editing becomes true: drag handles show, the delete button hides', guard='editing == true (tap "Edit" while not editing)', evidence='SRC PlaylistActivity.java:166-174')
e(PA + '.setEditing', 'S_PLAYLIST', 'ENTERS', 'editing becomes false (tap "Done" while editing)', guard='editing == false', evidence='SRC PlaylistActivity.java:166-174')
e('S_PLAYLIST', PA + '.onItemClick', 'FRAMEWORK', 'tap a song row (not in edit mode)', gui=['Tap a song row'], guard='mEditing is false and the default playlist action is not "do nothing"',
  needs_state=NEED_PLAYLIST_SONGS, evidence=FW_ITEMCLICK + '; SRC PlaylistActivity.java:286-295')
gui2('S_PLAYLIST', CCL, CCL + '@P', 'Long-press a song row', 'SRC CoordClickListener.java:69-72, 77-80; ' + FW_ITEMCLICK, needs_state=NEED_PLAYLIST_SONGS)
e(PA + '.onItemLongClickWithCoords', FM_SHOW['P'], 'CALL', 'fm.show(view, x, y): the bottom sheet of the playlist activity opens', needs_state=NEED_PLAYLIST_SONGS, evidence='SRC PlaylistActivity.java:211-225 (bytecode)')
e(FM_SHOW['P'], 'S_FANCY_PLAYLIST', 'ENTERS', 'the BottomSheetDialog with the menu rows is shown', evidence='SRC FancyMenu.java:169-190; ' + FW_DIALOGFRAG.split(' (')[0])
gui2('S_FANCY_PLAYLIST', FMC, FMC + '@P', 'Tap a row of the context menu', 'SRC FancyMenu.java:173-185; ' + FW_ITEMCLICK)
call(FMC + '@P', PA + '.onFancyItemSelected', 'mCallback.onFancyItemSelected(item) with the callback of this menu (PlaylistActivity: new FancyMenu(this, this))', 'SRC FancyMenu.java:72-76, 178; PlaylistActivity.java:211',
     guard='the menu was created by PlaylistActivity')

# ---- G2. PreferencesActivity (opened from the library overflow menu: POI_V['MENU_PREFS'] -> PreferencesActivity.<init>)
PREF = 'PreferencesActivity'
FW_PREF_HEADER = ('FW-SRC core/java/android/preference/PreferenceActivity.java:1100-1102, 1246-1254, 1249 '
                  '(onHeaderClick calls switchToHeader, which checks isValidFragment and instantiates the fragment named by the header through Fragment.instantiate, reflection) and '
                  'core/java/android/preference/PreferenceFragment.java:333-341 and core/java/android/preference/PreferenceActivity.java:1393-1409, 1431-1436 '
                  '(a nested PreferenceScreen with a fragment attribute: onPreferenceTreeClick calls onPreferenceStartFragment, which calls startPreferencePanel, instantiating the fragment through Fragment.instantiate)')
FW_PREF_INTENT = 'FW-SRC core/java/android/preference/Preference.java:1129-1154 (performClick starts the Intent of a Preference / PreferenceScreen that has an <intent> tag and no fragment)'
FW_PREF_CLICK = 'FW-SRC core/java/android/preference/Preference.java:1135-1139 (performClick calls the registered OnPreferenceClickListener)'
FW_DLGPREF = ('FW-SRC core/java/android/preference/DialogPreference.java:274-309, 386-395 '
              '(Preference.onClick calls DialogPreference.onClick, which calls showDialog: onCreateDialogView and onPrepareDialogBuilder build the AlertDialog, which is then shown; '
              'a dialog button calls DialogPreference.onClick(DialogInterface,int), which calls onDialogClosed)')
lifecycle(PREF, ('onCreate', 'onDestroy'), FW_ACT_CREATE, 'Activity lifecycle callback; SRC PreferencesActivity.java:68-80')
e(PREF + '.onCreate', PREF + '.isValidFragment', 'FRAMEWORK', 'the fragment name is validated before any header or nested fragment is instantiated', evidence='FW-SRC core/java/android/preference/PreferenceActivity.java:1249; SRC PreferencesActivity.java:312-315')
e(PREF + '.onCreate', PREF + '.onBuildHeaders', 'FRAMEWORK', 'the activity builds the list of settings sections from preference_headers.xml', evidence='FW-SRC core/java/android/preference/PreferenceActivity.java:599-613, 816; SRC PreferencesActivity.java:82-91')
e(PREF + '.onCreate', 'S_PREFS', 'ENTERS', 'the list of settings headers is shown', evidence='SRC PreferencesActivity.java:69-74; ' + FW_PREF_HEADER.split(' and ')[0])
gui('S_PREFS', PREF + '.onSharedPreferenceChanged', 'a preference value changes while a settings screen is open', needs_state=NEED_PREF_CHANGED, evidence='SRC PreferencesActivity.java:73, 94-100; ' + FW_VIEW_CLICK)
e(PREF + '.onSharedPreferenceChanged', PREF + '.<init>', 'CALL', 'the selected theme changed: recreate()', guard="key equals PrefKeys.SELECTED_THEME", evidence='SRC PreferencesActivity.java:95-99')
HEADERS = {
    'AudioFragment': ('S_PREFS_AUDIO', '102-109'),
    'PlaybackFragment': ('S_PREFS_PLAYBACK', '176-183'),
    'LibraryFragment': ('S_PREFS_LIBRARY', '185-192'),
    'NotificationsFragment': ('S_PREFS_NOTIFICATIONS', '194-201'),
    'ShakeFragment': ('S_PREFS_SHAKE', '203-210'),
    'CoverArtFragment': ('S_PREFS_COVERART', '212-219'),
    'MiscFragment': ('S_PREFS_MISC', '221-228'),
    'PlaylistFragment': ('S_PREFS_PLAYLIST', '230-237'),
}
for cls, (pg, lines) in HEADERS.items():
    node = PREF + '$' + cls
    gui('S_PREFS', node + '.<init>', 'Tap the "%s" header' % pg.replace('S_PREFS_', '').title(), evidence='SRC res/xml/preference_headers.xml; ' + FW_PREF_HEADER,
        cls='non_standard', via='the PreferenceActivity header list; the fragment named in res/xml/preference_headers.xml is instantiated through reflection (Fragment.instantiate)')
    lifecycle(node, ('onCreate',), FW_FRAG_LIFE, 'Fragment lifecycle callback; SRC PreferencesActivity.java:' + lines)
    e(node + '.onCreate', pg, 'ENTERS', 'addPreferencesFromResource: the settings rows of this section are shown', evidence='SRC PreferencesActivity.java:' + lines)
# ---- help / about (no settings rows: an external action, then the fragment finishes itself)
gui('S_PREFS', PREF + '$HelpFragment.<init>', 'Tap the "Help" header', evidence='SRC res/xml/preference_headers.xml; ' + FW_PREF_HEADER, cls='non_standard', via='the PreferenceActivity header list; the fragment named in res/xml/preference_headers.xml is instantiated through reflection (Fragment.instantiate)')
lifecycle(PREF + '$HelpFragment', ('onCreate',), FW_FRAG_LIFE, 'Fragment lifecycle callback; SRC PreferencesActivity.java:239-252')
e(PREF + '$HelpFragment.onCreate', 'S_ENTRY', 'INTENT', 'startActivity(ACTION_VIEW, the wiki URL); the fragment then calls activity.finish()', env=ENV_WEB, evidence='SRC PreferencesActivity.java:246-250')
gui('S_PREFS', PREF + '$AboutFragment.<init>', 'Tap the "About" header', evidence='SRC res/xml/preference_headers.xml; ' + FW_PREF_HEADER, cls='non_standard', via='the PreferenceActivity header list; the fragment named in res/xml/preference_headers.xml is instantiated through reflection (Fragment.instantiate)')
e(PREF + '$AboutFragment.<init>', PREF + '$AboutFragment.onCreateView', 'LIFECYCLE', 'Fragment lifecycle callback (onCreateView of the WebViewFragment base)', evidence=FW_FRAG_LIFE + '; SRC PreferencesActivity.java:254-268')
e(PREF + '$AboutFragment.onCreateView', 'S_PREFS_ABOUT', 'ENTERS', 'the about.html page is loaded in the WebView', evidence='SRC PreferencesActivity.java:258-266')
# ---- nested fragments opened from a PreferenceScreen row of S_PREFS_AUDIO
gui('S_PREFS_AUDIO', PREF + '$EqualizerFragment.<init>', 'Tap "Equalizer"', evidence='SRC res/xml/preference_audio.xml; ' + FW_PREF_HEADER, cls='non_standard', via='the nested PreferenceScreen fragment attribute (res/xml/preference_audio.xml); the fragment is instantiated through reflection (Fragment.instantiate, onPreferenceStartFragment)')
lifecycle(PREF + '$EqualizerFragment', ('onCreate',), FW_FRAG_LIFE, 'Fragment lifecycle callback; SRC PreferencesActivity.java:147-174')
e(PREF + '$EqualizerFragment.onCreate', 'S_ENTRY', 'INTENT', 'startActivityForResult(ACTION_DISPLAY_AUDIO_EFFECT_CONTROL_PANEL, 0); the fragment then pops the back stack', env=ENV_EQ, evidence='SRC PreferencesActivity.java:160-172')
gui('S_PREFS_AUDIO', PREF + '$ReplayGainFragment.<init>', 'Tap "Replay gain"', evidence='SRC res/xml/preference_audio.xml; ' + FW_PREF_HEADER, cls='non_standard', via='the nested PreferenceScreen fragment attribute (res/xml/preference_audio.xml); the fragment is instantiated through reflection (Fragment.instantiate, onPreferenceStartFragment)')
lifecycle(PREF + '$ReplayGainFragment', ('onCreate',), FW_FRAG_LIFE, 'Fragment lifecycle callback; SRC PreferencesActivity.java:111-138')
e(PREF + '$ReplayGainFragment.onCreate', 'S_PREFS_REPLAYGAIN', 'ENTERS', 'addPreferencesFromResource(preference_replaygain): track/album gain switches and the bump/de-bump sliders are shown', evidence='SRC PreferencesActivity.java:117-137')
e('S_PREFS_REPLAYGAIN', PREF + '$ReplayGainFragment$1.onPreferenceClick', 'FRAMEWORK', 'tap the track or album replay-gain switch', gui=['Tap the "Track replay gain" or "Album replay gain" switch'], evidence=FW_PREF_CLICK + '; SRC PreferencesActivity.java:128-136')
gui('S_PREFS_AUDIO', PREF + '$HeadsetLaunchFragment.<init>', 'Tap "Headset launch"', evidence='SRC res/xml/preference_audio.xml; ' + FW_PREF_HEADER, cls='non_standard', via='the nested PreferenceScreen fragment attribute (res/xml/preference_audio.xml); the fragment is instantiated through reflection (Fragment.instantiate, onPreferenceStartFragment)')
lifecycle(PREF + '$HeadsetLaunchFragment', ('onCreate',), FW_FRAG_LIFE, 'Fragment lifecycle callback; SRC PreferencesActivity.java:270-310')
e(PREF + '$HeadsetLaunchFragment.onCreate', 'S_ENTRY', 'INTENT', 'the launcher intent of the Vanilla Headset Launch plugin app is started', env=ENV_VPLUG, guard='getLaunchIntentForPackage(...) is not null (the plugin app is installed)', evidence='SRC PreferencesActivity.java:276-284')
e(PREF + '$HeadsetLaunchFragment.onCreate', 'S_DLG_PLUGINS', 'ENTERS', 'the plugin app is not installed: a dialog offers to open the market', guard='getLaunchIntentForPackage(...) is null', evidence='SRC PreferencesActivity.java:285-307')
gui('S_DLG_PLUGINS', PREF + '$HeadsetLaunchFragment$1.onClick', 'Tap "Yes" (open the market)', evidence='SRC PreferencesActivity.java:290-301; ' + FW_DLG_BUTTON)
e(PREF + '$HeadsetLaunchFragment$1.onClick', 'S_ENTRY', 'INTENT', 'startActivity(ACTION_VIEW, market://details?id=...vanillaplug)', env=ENV_MARKET, evidence='SRC PreferencesActivity.java:293-295')
gui('S_DLG_PLUGINS', PREF + '$HeadsetLaunchFragment$2.onClick', 'Tap "Cancel"', evidence='SRC PreferencesActivity.java:302-306; ' + FW_DLG_BUTTON)

# ---- G2b. PreferencesTheme (header fragment; theme list built at runtime)
PT = 'PreferencesTheme'
gui('S_PREFS', PT + '.<init>', 'Tap the "Theme" header', evidence='SRC res/xml/preference_headers.xml; ' + FW_PREF_HEADER, cls='non_standard', via='the PreferenceActivity header list; the fragment named in res/xml/preference_headers.xml is instantiated through reflection (Fragment.instantiate)')
lifecycle(PT, ('onCreate',), FW_FRAG_LIFE, 'Fragment lifecycle callback; SRC PreferencesTheme.java:38-64')
e(PT + '.onCreate', 'S_PREFS_THEME', 'ENTERS', 'a Preference row is added for each theme (decodeValue / generateThemePreview build the colour preview icon)', evidence='SRC PreferencesTheme.java:44-63')
e('S_PREFS_THEME', PT + '.onPreferenceClick', 'FRAMEWORK', 'tap a theme row', gui=['Tap a theme in the list'], evidence=FW_PREF_CLICK + '; SRC PreferencesTheme.java:57, 66-72')

# ---- G2c. custom DialogPreference widgets (SeekBarPreference, IdlePreference, ListPreferenceSummary): the same framework dialog flow on every settings page that uses them
e('S_PREFS_SHAKE', 'SeekBarPreference.onCreateDialogView', 'FRAMEWORK', 'tap the shake threshold row: the dialog with its seek bar is built', gui=['Tap the shake threshold row'], evidence=FW_DLGPREF + '; SRC res/xml/preference_shake.xml; SeekBarPreference.java:168-190')
e('SeekBarPreference.onCreateDialogView', 'SeekBarPreference.onProgressChanged', 'FRAMEWORK', 'drag the seek bar', gui=['Drag the seek bar'], evidence=FW_SEEKBAR + '; SRC SeekBarPreference.java:180, 206-213')
e('SeekBarPreference.onCreateDialogView', 'SeekBarPreference.onDialogClosed', 'FRAMEWORK', 'tap OK or Cancel on the dialog', gui=['Tap OK or Cancel'], evidence=FW_DLGPREF + '; SRC SeekBarPreference.java:192-203')
e('S_PREFS_MISC', 'IdlePreference.onCreateDialogView', 'FRAMEWORK', 'tap the idle timeout row: the dialog with its seek bar is built', gui=['Tap the idle timeout row'], evidence=FW_DLGPREF + '; SRC res/xml/preference_misc.xml; IdlePreference.java:67-84')
e('IdlePreference.onCreateDialogView', 'IdlePreference.onProgressChanged', 'FRAMEWORK', 'drag the seek bar', gui=['Drag the seek bar'], evidence=FW_SEEKBAR + '; SRC IdlePreference.java:79, 130-141')
e('IdlePreference.onCreateDialogView', 'IdlePreference.onDialogClosed', 'FRAMEWORK', 'tap OK or Cancel on the dialog', gui=['Tap OK or Cancel'], evidence=FW_DLGPREF + '; SRC IdlePreference.java:121-128')
e('S_PREFS_PLAYBACK', 'ListPreferenceSummary.onDialogClosed', 'FRAMEWORK', 'tap a row (ListPreference, e.g. "Playback on startup") and choose a value', gui=['Tap the preference row and choose a value'],
  evidence='FW-SRC core/java/android/preference/ListPreference.java:253-264, 277-283 (onPrepareDialogBuilder builds a single-choice AlertDialog from the entries; a tap commits the value, simulates the positive button and dismisses the dialog, which calls onDialogClosed(true)); SRC res/xml/preference_playback.xml; ListPreferenceSummary.java:54-60')
# ---- G2e. construction and value-binding of the three custom Preference subclasses (a PreferenceFragment inflates its XML with GenericInflater, which builds every row through reflection)
FW_PREF_CTOR = 'FW-SRC core/java/android/preference/GenericInflater.java:368-385 (createItem builds the (Context, AttributeSet) constructor of the class named in the XML tag through reflection, newInstance)'
FW_PREF_DEFAULT = 'FW-SRC core/java/android/preference/Preference.java:294, 382-384 (the Preference constructor reads the android:defaultValue XML attribute and calls onGetDefaultValue to parse it)'
FW_PREF_INITIAL = 'FW-SRC core/java/android/preference/Preference.java:1546-1560, 1584 (dispatchSetInitialValue, called once the preference is attached to its PreferenceScreen, calls onSetInitialValue with the persisted or default value)'
FW_PREF_SUMMARY = 'FW-SRC core/java/android/preference/Preference.java:625, 1944, 802 (the preference row view binds its summary text view to getSummary())'
for _cls, _pg, _xml in (('SeekBarPreference', 'S_PREFS_SHAKE', 'preference_shake.xml'), ('IdlePreference', 'S_PREFS_MISC', 'preference_misc.xml'), ('ListPreferenceSummary', 'S_PREFS_PLAYBACK', 'preference_playback.xml')):
    e(_pg, _cls + '.<init>', 'FRAMEWORK', 'the settings screen inflates the custom Preference row named in res/xml/' + _xml, evidence=FW_PREF_CTOR + '; SRC res/xml/' + _xml,
      cls='non_standard', via='the XML tag of the custom Preference row (res/xml/' + _xml + '); GenericInflater.createItem instantiates it through reflection (newInstance)')
    # only SeekBarPreference overrides onGetDefaultValue/onSetInitialValue (SeekBarPreference.java:135, 141); IdlePreference and ListPreferenceSummary do not
    # override them, so the framework calls the inherited Preference/ListPreference implementation directly (not an app method, no node for it)
    if _cls == 'SeekBarPreference':
        e(_cls + '.<init>', _cls + '.onGetDefaultValue', 'FRAMEWORK', 'the Preference constructor parses android:defaultValue', evidence=FW_PREF_DEFAULT)
        e(_cls + '.<init>', _cls + '.onSetInitialValue', 'FRAMEWORK', 'the preference is attached to its screen', evidence=FW_PREF_INITIAL)
    _gs = _cls + '.getSummary()' if _cls == 'SeekBarPreference' else _cls + '.getSummary'
    e(_pg, _gs, 'FRAMEWORK', 'the row view is bound and shows its summary text', evidence=FW_PREF_SUMMARY)
e('SeekBarPreference.getSummary()', 'SeekBarPreference.getSummary(int)', 'CALL', 'getSummary(mValue)', evidence='SRC SeekBarPreference.java:131 (bytecode)')
e('SeekBarPreference.<init>', 'SeekBarPreference.initDefaults', 'CALL', 'the constructor reads the vanilla: styled attributes', evidence='SRC SeekBarPreference.java:97-102 (bytecode)')
e('SeekBarPreference.onCreateDialogView', 'SeekBarPreference.onStartTrackingTouch', 'FRAMEWORK', 'start dragging the seek bar', gui=['Start dragging the seek bar'], evidence=FW_SEEKBAR + '; SRC SeekBarPreference.java:180')
e('SeekBarPreference.onCreateDialogView', 'SeekBarPreference.onStopTrackingTouch', 'FRAMEWORK', 'release the seek bar', gui=['Release the seek bar'], evidence=FW_SEEKBAR + '; SRC SeekBarPreference.java:180')
e('IdlePreference.onCreateDialogView', 'IdlePreference.onStartTrackingTouch', 'FRAMEWORK', 'start dragging the seek bar', gui=['Start dragging the seek bar'], evidence=FW_SEEKBAR + '; SRC IdlePreference.java:79')
e('IdlePreference.onCreateDialogView', 'IdlePreference.onStopTrackingTouch', 'FRAMEWORK', 'release the seek bar', gui=['Release the seek bar'], evidence=FW_SEEKBAR + '; SRC IdlePreference.java:79')

# ---- G2d. TabOrderActivity (opened from a PreferenceScreen row of S_PREFS_LIBRARY with an <intent> to this activity)
e('S_PREFS_LIBRARY', 'TabOrderActivity.<init>', 'INTENT', 'tap "Customize tab order": performClick starts the Intent of the PreferenceScreen', gui=['Tap "Customize tab order"'],
  evidence=FW_PREF_INTENT + '; SRC res/xml/preference_library.xml; AndroidManifest.xml:190-191')
lifecycle('TabOrderActivity', ('onCreate',), FW_ACT_CREATE)
e('TabOrderActivity.onCreate', 'S_TAB_ORDER', 'ENTERS', 'the draggable list of tabs is shown (load() reads the saved order, or restoreDefault() if none is saved)', evidence='SRC TabOrderActivity.java:49-67, 127-155')
inflate('TabOrderActivity.onCreate', ['DragSortListView.<init>'], 'tab_order.xml')
SCREENS.update({'S_TAB_ORDER': 'TabOrderActivity: draggable, checkable list of the library tabs, with Done and "Restore default" buttons'})
e('TabOrderActivity.onCreate', 'TabOrderAdapter.getCount', 'FRAMEWORK', 'list.setAdapter(mAdapter): the ListView reads the rows', evidence=FW_GETVIEW + '; SRC TabOrderActivity.java:57-59')
for cb in ('getView', 'getItemId', 'getItem', 'hasStableIds'):
    e('TabOrderActivity.onCreate', 'TabOrderAdapter.' + cb, 'FRAMEWORK', 'the ListView binds the tab rows', evidence=FW_GETVIEW + '; SRC TabOrderActivity.java:57-59')
inflate('TabOrderAdapter.getView', ['DraggableRow'], 'draggable_row.xml')
gui('S_TAB_ORDER', 'TabOrderActivity.onClick', 'Tap "Done" or "Restore default"', evidence='SRC TabOrderActivity.java:65-66, 80-91; ' + FW_VIEW_CLICK)
gui('S_TAB_ORDER', 'TabOrderActivity.onItemClick', 'Tap the check box of a tab row', evidence=FW_ITEMCLICK + '; SRC TabOrderActivity.java:60, 157-161')
gui('S_TAB_ORDER', 'TabOrderActivity.onOptionsItemSelected', 'Tap the Up/Back arrow of the action bar', evidence=FW_ACT_MENU + '; SRC TabOrderActivity.java:69-78')
# list.setItemChecked(...) (cold start: default visibility; TabOrderActivity.onItemClick: tap a row) updates the check mark of the visible row view (DragSortItemViewCheckable, since
# TabOrderAdapter's rows, DraggableRow, implement Checkable), which forwards to the wrapped DraggableRow
FW_CHECKABLE_ROW = ('FW-SRC core/java/android/widget/AbsListView.java:1033-1102 (setItemChecked records the check state and requests a layout) and '
                     'core/java/android/widget/ListView.java:2076-2114 (setupChild, called while binding/laying out each visible row, calls Checkable.setChecked on a row view that implements Checkable)')
e('TabOrderActivity.onCreate', 'DragSortItemViewCheckable.setChecked', 'FRAMEWORK', 'list.setItemChecked(i, ...): the ListView updates the check mark of the visible tab row (tab_order.xml sets android:choiceMode="multipleChoice")',
  evidence=FW_CHECKABLE_ROW + '; SRC TabOrderActivity.java:57-59, 101, 147, 157-161; res/layout/tab_order.xml')
e('DragSortItemViewCheckable.setChecked', 'DraggableRow.setChecked', 'CALL', '((Checkable) child).setChecked(checked): the wrapped row view forwards the call (child is a DraggableRow, built by TabOrderAdapter.getView)',
  guard='the wrapped child view is Checkable (DraggableRow)', evidence='SRC com/mobeta/android/dslv/DragSortItemViewCheckable.java:43-47 (bytecode: invokeinterface Checkable.setChecked, not resolved to DraggableRow by the scan)')
for _cb in ('onLayout', 'onMeasure'):
    e('DragSortItemView.<init>', 'DragSortItemView.' + _cb, 'FRAMEWORK', 'the view system lays out and measures the item view wrapper', evidence=FW_VIEW_DRAW)

# ---- G3. PreferencesMediaLibrary (header fragment: scan controls, stats, media folders)
PML = 'PreferencesMediaLibrary'
gui('S_PREFS', PML + '.<init>', 'Tap the "Media library" header', evidence='SRC res/xml/preference_headers.xml; ' + FW_PREF_HEADER, cls='non_standard', via='the PreferenceActivity header list; the fragment named in res/xml/preference_headers.xml is instantiated through reflection (Fragment.instantiate)')
lifecycle(PML, ('onCreateView', 'onViewCreated', 'onResume', 'onPause'), FW_FRAG_LIFE, 'Fragment lifecycle callback; SRC PreferencesMediaLibrary.java:122-188')
e(PML + '.onViewCreated', 'S_PREFS_MEDIALIB', 'ENTERS', 'the scan controls and statistics are shown', evidence='SRC PreferencesMediaLibrary.java:128-153, 313-341')
gui('S_PREFS_MEDIALIB', PML + '.onClick', 'Tap "Start", "Cancel", "Edit" or a checkbox', evidence='SRC PreferencesMediaLibrary.java:191-207; ' + FW_VIEW_CLICK)
gui('S_PREFS_MEDIALIB', PML + '.onCreateOptionsMenu', 'the overflow menu is inflated (setHasOptionsMenu(true))', evidence='FW-SRC core/java/android/app/Fragment.java:2489 (performCreate leads to the options-menu callbacks of a fragment that called setHasOptionsMenu); SRC PreferencesMediaLibrary.java:152, 212-217')
gui('S_PREFS_MEDIALIB', PML + '.onOptionsItemSelected', 'Tap "Dump database" or "Force m3u import" in the overflow menu', evidence=FW_ACT_MENU + '; SRC PreferencesMediaLibrary.java:220-239')
e(PML + '.onClick', 'S_DLG_MEDIALIB_CONFIRM', 'ENTERS', 'tap the "group albums by folder" or "force bastp" checkbox (no scan pending yet): a confirm dialog is shown', guard='view.getId() is media_scan_group_albums or media_scan_force_bastp, and mFullScanPending is false',
  evidence='SRC PreferencesMediaLibrary.java:202-204, 246-270')
gui('S_DLG_MEDIALIB_CONFIRM', PML + '$2.onClick', 'Tap "Yes"', evidence='SRC PreferencesMediaLibrary.java:257-262; ' + FW_DLG_BUTTON)
gui('S_DLG_MEDIALIB_CONFIRM', PML + '$3.onClick', 'Tap "Cancel"', evidence='SRC PreferencesMediaLibrary.java:263-268; ' + FW_DLG_BUTTON)
e(PML + '.editButtonPressed', 'S_DLG_MEDIALIB_CONFIRM', 'ENTERS', 'tap "Edit" (no scan pending yet): a confirm dialog is shown', guard='mFullScanPending is false', evidence='SRC PreferencesMediaLibrary.java:385-404')
gui('S_DLG_MEDIALIB_CONFIRM', PML + '$4.onClick', 'Tap "Yes"', evidence='SRC PreferencesMediaLibrary.java:395-399; ' + FW_DLG_BUTTON)
gui('S_DLG_MEDIALIB_CONFIRM', PML + '$5.onClick', 'Tap "Cancel"', evidence='SRC PreferencesMediaLibrary.java:400-402; ' + FW_DLG_BUTTON)
SCREENS.update({
    'S_DLG_MEDIALIB_CONFIRM': 'Confirm dialog "This will delete your cached results..." (shared text for the checkbox change and the Edit button)',
    'S_FOLDERPICKER': 'FolderPickerActivity (base of MediaFoldersSelectionActivity and FilebrowserStartActivity): a folder tree browser with a path field and a Save/Select button',
})

# ---- G4. FolderPickerActivity (abstract) and its two concrete activities
e(PML + '$4.onClick', 'MediaFoldersSelectionActivity.<init>', 'CALL', 'startMediaFoldersSelection(): startActivity(new Intent(this, MediaFoldersSelectionActivity.class))', evidence='SRC PreferencesMediaLibrary.java:396, 409-411; ' + FW_ACT_CREATE)
e(PML + '.editButtonPressed', 'MediaFoldersSelectionActivity.<init>', 'CALL', 'mFullScanPending is true: startMediaFoldersSelection() runs directly', guard='mFullScanPending is true', evidence='SRC PreferencesMediaLibrary.java:386-389, 409-411; ' + FW_ACT_CREATE)
e('S_PREFS_LIBRARY', 'FilebrowserStartActivity.<init>', 'INTENT', 'tap "Customize file browser start": performClick starts the Intent of the PreferenceScreen', gui=['Tap "Customize file browser start folder"'],
  evidence=FW_PREF_INTENT + '; SRC res/xml/preference_library.xml; AndroidManifest.xml:192-193')
lifecycle('FilebrowserStartActivity', ('onCreate',), FW_ACT_CREATE, 'Activity lifecycle callback; SRC FilebrowserStartActivity.java')
lifecycle('MediaFoldersSelectionActivity', ('onCreate',), FW_ACT_CREATE, 'Activity lifecycle callback; SRC MediaFoldersSelectionActivity.java:33-46')
e('FilebrowserStartActivity.onCreate', 'S_FOLDERPICKER', 'ENTERS', 'the folder browser opens at the saved filesystem-browse-start folder', evidence='SRC FilebrowserStartActivity.java:9-16; FolderPickerActivity.java:68-93')
e('MediaFoldersSelectionActivity.onCreate', 'S_FOLDERPICKER', 'ENTERS', 'the folder browser opens with tritastic include/exclude selection enabled', evidence='SRC MediaFoldersSelectionActivity.java:33-46; FolderPickerActivity.java:68-93')
inflate('FolderPickerActivity.onCreate', ['DragSortListView.<init>'], 'folderpicker_content.xml')
e('FolderPickerActivity.onCreate', 'FolderPickerAdapter.getView', 'FRAMEWORK', 'mListView.setAdapter(mListAdapter): the ListView reads the folder rows', evidence=FW_GETVIEW + '; SRC FolderPickerActivity.java:75-81')
gui('S_FOLDERPICKER', 'FolderPickerActivity.onItemClick', 'Tap a folder row (or "..")', evidence=FW_ITEMCLICK + '; SRC FolderPickerActivity.java:239-255')
gui('S_FOLDERPICKER', 'FolderPickerActivity$2.afterTextChanged', 'Edit the path field directly', evidence=FW_TEXTWATCHER + '; SRC FolderPickerActivity.java:84, 109-114')
for _cb, _ln in (('beforeTextChanged', '114-116'), ('onTextChanged', '118-120')):
    gui('S_FOLDERPICKER', 'FolderPickerActivity$2.' + _cb, 'Edit the path field directly', evidence=FW_TEXTWATCHER + '; SRC FolderPickerActivity.java:84, ' + _ln)
gui('S_FOLDERPICKER', 'FolderPickerActivity.onCreateOptionsMenu', 'the overflow menu is inflated', evidence=FW_ACT_MENU + '; SRC FolderPickerActivity.java:196-199')
gui('S_FOLDERPICKER', 'FolderPickerActivity$1.onClick', 'Tap "Save" / "Select"', evidence='SRC FolderPickerActivity.java:85, 98-104; ' + FW_VIEW_CLICK)
e('FolderPickerActivity$1.onClick', 'MediaFoldersSelectionActivity.onFolderPicked', 'CALL', 'onFolderPicked(dir, included, excluded)', guard='the activity is MediaFoldersSelectionActivity', evidence='SRC FolderPickerActivity.java:100-103 (bytecode)')
e('FolderPickerActivity$1.onClick', 'FilebrowserStartActivity.onFolderPicked', 'CALL', 'onFolderPicked(dir, included, excluded)', guard='the activity is FilebrowserStartActivity', evidence='SRC FolderPickerActivity.java:100-103 (bytecode)')
gui('S_FOLDERPICKER', 'FolderPickerActivity.onOptionsItemSelected', 'Tap the Up/Back arrow of the action bar', evidence=FW_ACT_MENU + '; SRC FolderPickerActivity.java:200-209')
# the tritastic controls (long-press menu, spinner) are wired only by MediaFoldersSelectionActivity (enableTritasticSelect/Spinner(true, ...)); FilebrowserStartActivity leaves them disabled
gui('S_FOLDERPICKER', 'FolderPickerActivity.onItemLongClick', 'Long-press a folder row (media-folders editor only)', needs_state=state_text('The folder browser was opened from Settings > Media library > Edit (tritastic include/exclude is enabled)', 'session'),
    evidence=FW_ITEMCLICK + '; SRC FolderPickerActivity.java:142, 148, 260-293')
gui('S_FOLDERPICKER', 'FolderPickerActivity$3.onClick', 'Tap "Include" / "Exclude" / "Neutral" in the long-press menu', needs_state=state_text('The folder browser was opened from Settings > Media library > Edit (tritastic include/exclude is enabled)', 'session'),
    evidence='SRC FolderPickerActivity.java:276-290; ' + FW_DLG_ITEM)
gui('S_FOLDERPICKER', 'FolderPickerActivity.onItemSelected', 'Change the include/exclude/neutral spinner (media-folders editor only)', needs_state=state_text('The folder browser was opened from Settings > Media library > Edit (tritastic include/exclude is enabled)', 'session'),
    evidence='FW-SRC core/java/android/widget/AdapterView.java:908, 933, 937-945 (fireOnSelected calls the OnItemSelectedListener registered with setOnItemSelectedListener); SRC FolderPickerActivity.java:79, 88, 214-226')
gui('S_FOLDERPICKER', 'FolderPickerActivity.onNothingSelected', 'Dismiss the include/exclude/neutral spinner without choosing a value (media-folders editor only)',
    needs_state=state_text('The folder browser was opened from Settings > Media library > Edit (tritastic include/exclude is enabled)', 'session'),
    evidence='FW-SRC core/java/android/widget/AdapterView.java:908, 947 (fireOnNothingSelected calls the OnItemSelectedListener registered with setOnItemSelectedListener when the selection is cleared); SRC FolderPickerActivity.java:79, 88, 231-235')

# ===================================================================== H. media library: drag-sort list, covers, scanner, backend, tag readers, small adapters
# ---- H1. com.mobeta.android.dslv.DragSortListView / DragSortController (vendored library, bundled as app source; used by PlaylistActivity, TabOrderActivity, FolderPickerActivity and ShowQueueFragment)
FW_GESTURE = ('FW-SRC core/java/android/view/GestureDetector.java:593, 611-624, 640, 655, 778, 289 '
              '(onTouchEvent calls the registered OnGestureListener: onDown, onScroll, onSingleTapUp, onFling, onLongPress, onShowPress)')
inflate('ShowQueueFragment.onCreateView', ['DragSortListView.<init>'], 'showqueue_listview.xml')
FW_TOUCH_DISPATCH = ('FW-SRC core/java/android/view/ViewGroup.java:2480, 2511 (dispatchTouchEvent calls onInterceptTouchEvent first, before any child view sees the event) and '
                     'core/java/android/view/View.java:11741, 11770-11776 (dispatchTouchEvent then calls the OnTouchListener registered with setOnTouchListener, and calls onTouchEvent when the listener does not consume the event)')
e('DragSortListView.<init>', 'DragSortController.onTouch', 'FRAMEWORK', 'the touch dispatch calls the OnTouchListener registered in the constructor (super.setOnTouchListener(controller), the default DragSortController)',
  evidence=FW_VIEW_CLICK + '; SRC DragSortListView.java:525-534')
e('DragSortListView.<init>', 'DragSortListView.onInterceptTouchEvent', 'FRAMEWORK', 'the ViewGroup touch dispatch calls onInterceptTouchEvent before any child row sees the event', evidence=FW_TOUCH_DISPATCH)
e('DragSortListView.<init>', 'DragSortListView.onTouchEvent', 'FRAMEWORK', 'the touch dispatch calls onTouchEvent (DragSortController.onTouch, the registered OnTouchListener, always returns false and never consumes the event)',
  evidence=FW_TOUCH_DISPATCH + '; SRC DragSortController.java:277 (onTouch always returns false)')
for cb in ('onMeasure', 'onSizeChanged', 'onDraw', 'dispatchDraw'):
    e('DragSortListView.<init>', 'DragSortListView.' + cb, 'FRAMEWORK', 'the view system lays out and draws the list', evidence=FW_VIEW_DRAW)
e('DragSortController.onTouch', 'DragSortController.onDown', 'FRAMEWORK', 'the GestureDetector created in the constructor dispatches every touch event', guard='isDragEnabled() is true (set in the layout attr dslv:drag_enabled, or toggled by PlaylistActivity.setEditing)',
  evidence=FW_GESTURE + '; SRC DragSortController.java:120, 243-256')
for cb in ('onScroll', 'onLongPress', 'onSingleTapUp', 'onShowPress', 'onFling'):
    e('DragSortController.onTouch', 'DragSortController.' + cb, 'FRAMEWORK', 'the GestureDetector dispatches the next touch event of the same gesture', guard='isDragEnabled() is true',
      evidence=FW_GESTURE + '; SRC DragSortController.java:120, 243-256')
e('DragSortController.onTouch', 'DragSortController$1.onFling', 'FRAMEWORK', 'mFlingRemoveDetector.onTouchEvent(ev): the second GestureDetector (fling-to-remove) dispatches a fling while a drag is in progress',
  guard='isDragEnabled() is true', needs_state=state_text('A drag is in progress, removal is enabled and remove_mode is flingRemove (ShowQueueFragment, PlaylistActivity after Edit)', 'session'),
  evidence=FW_GESTURE + '; SRC DragSortController.java:120-122, 253-255')
# drag_start_mode is "onMove" (ON_DRAG) in every layout that uses this controller (playlist_activity.xml, tab_order.xml, showqueue_listview.xml): the ON_DOWN and ON_LONG_PRESS branches of startDrag are never taken
sup(('DragSortController.onDown', 'DragSortController.startDrag'), ('DragSortController.onLongPress', 'DragSortController.startDrag'), ('DragSortController.onDown', 'DragSortController.viewIdHitPosition'))
# guard-less bytecode edge found while reading the verify_sample route of SongTimeline.removeSongPosition: onTouch's ACTION_UP case only calls stopDragWithVelocity
# when a fling-to-remove drag is in progress and crossed the removal threshold (CS.guard_of confirms: case ACTION_UP / mRemoveEnabled && mIsRemoving / x > removePoint)
sup(('DragSortController.onTouch', 'DragSortListView.stopDragWithVelocity'))
call('DragSortController.onTouch', 'DragSortListView.stopDragWithVelocity', 'mDslv.stopDragWithVelocity(true, 0): the finger lifts past the removal threshold while a fling-to-remove drag is in progress',
     'SRC DragSortController.java:261-268 (bytecode)', guard='action == ACTION_UP and mRemoveEnabled and mIsRemoving and x > removePoint (the floating view crossed half the list width)',
     needs_state=state_text('A drag is in progress, removal is enabled and remove_mode is flingRemove, and a fling-to-remove gesture was already detected (mIsRemoving) earlier in the same touch sequence', 'session'))
# two more guard-less bytecode edges of the same onTouch(Event) dispatch chain, found while re-reading this route after the fix above picked the plain
# (non-remove) drop path instead: onTouchEvent only forwards to onDragTouchEvent while a drag is active, and onDragTouchEvent's ACTION_UP case only calls
# stopDrag(false) while still DRAGGING (CS.guard_of confirms both).
NEED_DRAGGING = state_text('A drag is in progress (DragSortController.startDrag was called earlier in the same touch sequence)', 'session')
sup(('DragSortListView.onTouchEvent', 'DragSortListView.onDragTouchEvent'), ('DragSortListView.onDragTouchEvent', 'DragSortListView.stopDrag(boolean)'))
call('DragSortListView.onTouchEvent', 'DragSortListView.onDragTouchEvent', 'mDragState == DRAGGING: the touch event belongs to an active drag', 'SRC DragSortListView.java:1646-1648 (bytecode)',
     guard='mDragState == DRAGGING', needs_state=NEED_DRAGGING)
call('DragSortListView.onDragTouchEvent', 'DragSortListView.stopDrag(boolean)', 'ACTION_UP while still dragging: stopDrag(false) (not a fling-to-remove; the plain drop path)', 'SRC DragSortListView.java:2176-2179 (bytecode)',
     guard='action == ACTION_UP and mDragState == DRAGGING', needs_state=NEED_DRAGGING)
e('DragSortController.onScroll', 'DragSortController.startDrag', 'CALL', 'the vertical drag exceeds the touch slop while the drag handle is held and sorting is enabled (drag_start_mode=onMove, sort_enabled default true)',
  guard='mDragInitMode == ON_DRAG and abs(y2-y1) > touchSlop and mSortEnabled', evidence='SRC DragSortController.java:411-415 (bytecode)')
e('DragSortController.onScroll', 'DragSortController.startDrag', 'CALL', 'the horizontal drag exceeds the touch slop while removal is enabled (fling-to-remove: ShowQueueFragment, PlaylistActivity after Edit)',
  guard='mDragInitMode != ON_DOWN and abs(x2-x1) > touchSlop and mRemoveEnabled', needs_state=state_text('Removal is enabled for this list (ShowQueueFragment and PlaylistActivity after Edit; not TabOrderActivity or FolderPickerActivity)', 'session'),
  evidence='SRC DragSortController.java:416-420 (bytecode)')
# onSingleTapUp's click-to-remove branch needs remove_mode=clickRemove, never configured (every layout uses the flingRemove default or leaves remove disabled)
sup(('DragSortController.onSingleTapUp', 'DragSortListView.removeItem(int)'))
finish_inflate('DraggableRow')
# ---- H1c. DragSortListView$AdapterWrapper: the real adapter is wrapped (its type is the android.widget.ListAdapter interface, so the bytecode scan cannot resolve the delegated call)
AW = 'DragSortListView$AdapterWrapper'
FW_CURSORADAPTER = 'FW-SRC core/java/android/widget/CursorAdapter.java:276-289, 319, 340 (getView calls newView the first time a row is created (convertView is null), then always calls bindView)'
for cb in ('getView', 'getCount', 'getItem', 'getItemId', 'hasStableIds', 'isEmpty', 'isEnabled', 'areAllItemsEnabled', 'getItemViewType', 'getViewTypeCount', 'getAdapter'):
    e('DragSortListView.<init>', AW + '.' + cb, 'FRAMEWORK', 'the ListView reads the wrapped adapter', evidence=FW_GETVIEW + '; SRC DragSortListView.java:656-700 (bytecode)')
e(AW + '.<init>', AW + '$1.<init>', 'CALL', 'the DataSetObserver field of the wrapper is created', evidence='SRC DragSortListView.java (bytecode)')
e(AW + '$1.onChanged', AW + '.getCount', 'CALL', 'notifyDataSetChanged on the wrapped adapter is forwarded', evidence='INFERRED android.database.Observable.notifyChanged calls each registered DataSetObserver.onChanged (android.widget.BaseAdapter / CursorAdapter source not read for this call)')
e('DragSortListView.<init>', AW + '$1.onChanged', 'FRAMEWORK', 'the wrapped adapter notifies a data change', evidence='INFERRED android.database.Observable.notifyChanged calls each registered DataSetObserver.onChanged (source not read)')
e('DragSortListView.<init>', AW + '$1.onInvalidated', 'FRAMEWORK', 'the wrapped adapter notifies invalidation', evidence='INFERRED android.database.Observable.notifyInvalidated calls each registered DataSetObserver.onInvalidated (source not read)')
# TabOrderAdapter (own BaseAdapter overrides) is the cheapest reachable wrapped adapter (TabOrderActivity needs no gate beyond S_PREFS_LIBRARY)
for cb in ('getView', 'getCount', 'getItem', 'getItemId', 'hasStableIds'):
    e(AW + '.' + cb, 'TabOrderAdapter.' + cb, 'CALL', 'mAdapter.%s(...): the wrapped adapter of TabOrderActivity' % cb, guard='the wrapped adapter is TabOrderAdapter (DragSortListView.setAdapter in TabOrderActivity.onCreate)',
      evidence='SRC DragSortListView.java:656-700 (interface-typed field, not resolved by the bytecode scan); TabOrderActivity.java:57-59')
# PlaylistAdapter (a CursorAdapter: getView is not overridden, CursorAdapter.getView mediates to newView / bindView)
e(AW + '.getView', 'PlaylistAdapter.newView', 'CALL', 'mAdapter.getView(...): the wrapped adapter is PlaylistAdapter (a CursorAdapter); the row is created the first time (convertView is null)',
  guard='the wrapped adapter is PlaylistAdapter and convertView is null', evidence=FW_CURSORADAPTER + '; SRC PlaylistActivity.java:129')
e(AW + '.getView', 'PlaylistAdapter.bindView', 'CALL', 'mAdapter.getView(...): the wrapped adapter is PlaylistAdapter (a CursorAdapter); the row is bound to the cursor', guard='the wrapped adapter is PlaylistAdapter',
  evidence=FW_CURSORADAPTER + '; SRC PlaylistActivity.java:129')
e('PlaylistAdapter.setPlaylistId', 'PlaylistAdapter.handleMessage', 'ASYNC', 'mWorkerHandler.sendEmptyMessage(MSG_RUN_QUERY)', evidence=FW_HANDLER + '; SRC PlaylistAdapter.java:84-88')
e('PlaylistAdapter.handleMessage', 'PlaylistAdapter.handleMessage', 'ASYNC', 'MSG_RUN_QUERY: the worker thread runs the query, then mUiHandler.sendMessage(MSG_UPDATE_CURSOR) delivers the cursor to the UI thread',
  guard='message.what == MSG_RUN_QUERY', evidence=FW_HANDLER + '; SRC PlaylistAdapter.java:148-153')
# ShowQueueAdapter (a BaseAdapter, own overrides)
e(AW + '.getView', 'ShowQueueAdapter.getView', 'CALL', 'mAdapter.getView(...): the wrapped adapter is ShowQueueAdapter', guard='the wrapped adapter is ShowQueueAdapter', evidence='SRC ShowQueueFragment.java:55-56; DragSortListView.java:656-700')
for cb in ('getCount', 'getItem', 'getItemId', 'hasStableIds'):
    e(AW + '.' + cb, 'ShowQueueAdapter.' + cb, 'CALL', 'mAdapter.%s(...): the wrapped adapter is ShowQueueAdapter' % cb, guard='the wrapped adapter is ShowQueueAdapter', evidence='SRC ShowQueueFragment.java:55-56; DragSortListView.java:656-700')
e('ShowQueueFragment.refreshSongQueueList', 'ShowQueueFragment$1.run', 'ASYNC', 'getActivity().runOnUiThread(runnable)', evidence=FW_RUNUI + '; SRC ShowQueueFragment.java:220-232')

# ---- H2. LibraryPagerAdapter's two-Handler query pipeline (worker thread query, UI thread commit); MediaAdapter; the media library backend and scanner (first triggered by this query)
e('LibraryPagerAdapter.postRunQuery', 'LibraryPagerAdapter.handleMessage', 'ASYNC', 'mWorkerHandler.sendMessage(MSG_RUN_QUERY, adapter): the query runs on the worker thread', evidence=FW_HANDLER + '; SRC LibraryPagerAdapter.java:750-755')
e('LibraryPagerAdapter.handleMessage', 'LibraryPagerAdapter.handleMessage', 'ASYNC', 'MSG_RUN_QUERY: mUiHandler.sendMessage(MSG_COMMIT_QUERY, index, 0, adapter.query()) delivers the cursor to the UI thread', guard='message.what == MSG_RUN_QUERY', evidence=FW_HANDLER + '; SRC LibraryPagerAdapter.java:684-690')
# fixed while reading the verify_sample route of CoverCache$BitmapDiskCache.getUsedSpace this session: these cited LibraryPagerAdapter.java:895, which is
# inside onItemClick, not the setAdapter call; the real call (view.setAdapter(adapter)) is at line 353 (common code after the per-tab switch of instantiateItem).
for cb in ('getView', 'getCount', 'getItem', 'getItemId', 'hasStableIds'):
    e('LibraryPagerAdapter.instantiateItem', 'MediaAdapter.' + cb, 'FRAMEWORK', 'the tab\'s ListView reads the rows (list.setAdapter(adapter))', evidence=FW_GETVIEW + '; SRC LibraryPagerAdapter.java:353')
for cb in ('getSections', 'getPositionForSection', 'getSectionForPosition'):
    e('LibraryPagerAdapter.instantiateItem', 'MediaAdapter.' + cb, 'FRAMEWORK', 'the fast scroll thumb of the tab\'s ListView is dragged', evidence=FW_FASTSCROLL + '; SRC LibraryPagerAdapter.java:353')
e('MediaAdapter.getSections', 'MediaAdapter$SectionIndex.toString', 'CALL', 'the fast scroll thumb shows the section preview text (section.toString())', evidence=FW_FASTSCROLL + '; SRC MediaAdapter.java (bytecode)')

# ---- H2a. the ListView itself (listview.xml, common code of instantiateItem after the per-tab switch) and FileSystemAdapter's own framework wiring (the Files tab)
inflate('LibraryPagerAdapter.instantiateItem', ['FastScrollGuardedListView.<init>(Context,AttributeSet)'], 'listview.xml')
e('FastScrollGuardedListView.<init>(Context,AttributeSet)', 'FastScrollGuardedListView.onInterceptTouchEvent', 'FRAMEWORK', 'the ViewGroup touch dispatch calls onInterceptTouchEvent before any child row sees the event', evidence=FW_TOUCH_DISPATCH)
for cb, line in (('getView', '353'), ('getCount', '353'), ('getItem', '353'), ('getItemId', '353')):
    e('LibraryPagerAdapter.instantiateItem', 'FileSystemAdapter.' + cb, 'FRAMEWORK', 'the tab\'s ListView reads the rows (list.setAdapter(adapter), the Files tab)', evidence=FW_GETVIEW + '; SRC LibraryPagerAdapter.java:' + line)
FW_FILE_LISTFILTER = 'INFERRED java.io.File.listFiles(FilenameFilter) calls the given filter\'s accept(File dir, String name) for each directory entry (standard Java library behavior; libcore is not part of frameworks/base, source not fetched)'
FW_JDK_SORT = 'INFERRED java.util.Collections.sort(list, comparator) calls the given Comparator\'s compare(a,b) to order the list (standard Java library behavior; libcore is not part of frameworks/base, source not fetched)'
e('FileSystemAdapter.query', 'FileSystemAdapter$1.accept', 'FRAMEWORK', 'file.listFiles(mFileFilter): the directory is listed', evidence=FW_FILE_LISTFILTER + '; SRC FileSystemAdapter.java:106-121, 195')
e('FileSystemAdapter.query', 'FileSystemAdapter$2.compare', 'FRAMEWORK', 'Collections.sort(files, mFileComparator): the listed entries are sorted', evidence=FW_JDK_SORT + '; SRC FileSystemAdapter.java:125-158, 202')
e('FileSystemAdapter.query', 'FileSystemAdapter$Observer.onEvent', 'FRAMEWORK', 'mFileObserver = new Observer(...); the constructor calls startWatching(): a file system event in the current directory fires', env=ENV_FILESYS,
  evidence=FW_FILEOBS + '; SRC FileSystemAdapter.java:190-192, 382-394')

# ---- H2b. CoverCache$BitmapDiskCache (SQLiteOpenHelper), CoverKey (hashCode-only key: equals/toString are never called), LazyCoverView (in-memory LRU cover cache, inflated as part of draggable_row.xml)
_FW_SQLITE_EARLY = 'FW-SRC core/java/android/database/sqlite/SQLiteOpenHelper.java:333, 338 (getWritableDatabase / getReadableDatabase call onCreate the first time the database file does not exist, and onUpgrade when the stored version is older than the requested one)'
e('CoverCache$BitmapDiskCache.<init>', 'CoverCache$BitmapDiskCache.onCreate', 'FRAMEWORK', 'the first access to covercache.db creates it (a fresh install)', evidence=_FW_SQLITE_EARLY + '; SRC CoverCache.java:236-239, 244-248')
e('CoverCache$BitmapDiskCache.<init>', 'CoverCache$BitmapDiskCache.onUpgrade', 'FRAMEWORK', 'an older covercache.db from an earlier install is on disk', env=ENV_OLDDB, evidence=_FW_SQLITE_EARLY + '; SRC CoverCache.java:236-239, 253-255')
e('LazyCoverView$BitmapLruCache.<init>', 'LazyCoverView$BitmapLruCache.sizeOf', 'FRAMEWORK', 'LruCache.put calls safeSizeOf, which calls sizeOf to track the entry size', evidence='FW-SRC core/java/android/util/LruCache.java:164-183, 285-299 (put calls safeSizeOf, which calls the overridden sizeOf); SRC LazyCoverView.java:217-233')
e('SongTimeline.readState', 'SongTimeline$IdComparator.compare', 'FRAMEWORK', 'Collections.sort(songs, new IdComparator()): the saved songs are sorted by id (the order the restore query returns them in)', evidence=FW_JDK_SORT + '; SRC SongTimeline.java:294-307, 350')
e('SongTimeline.readState', 'SongTimeline$FlagComparator.compare', 'FRAMEWORK', 'Collections.sort(songs, new FlagComparator()): the songs are restored to the order they were saved in', evidence=FW_JDK_SORT + '; SRC SongTimeline.java:309-322, 385')

FW_CONTENTOBS = ('FW-SRC core/java/android/database/ContentObserver.java:106-114, 144-154 '
                 '(dispatchChange calls onChange on the handler thread the observer was registered with); INFERRED the MediaStore scanner (or another app writing media) notifies the registered URI when a file changes (platform media provider source not read)')
e('MediaLibrary.getBackend', 'MediaScanner$1.onChange', 'FRAMEWORK', 'the system MediaStore content observer fires (a file was scanned by the platform media scanner)', env=ENV_MEDIASTORE, evidence=FW_CONTENTOBS + '; SRC MediaScanner.java:112-118')
_FW_SQLITE_EARLY = 'FW-SRC core/java/android/database/sqlite/SQLiteOpenHelper.java:333, 338 (getWritableDatabase / getReadableDatabase call onCreate the first time the database file does not exist, and onUpgrade when the stored version is older than the requested one)'
e('MediaLibraryBackend.<init>', 'MediaLibraryBackend.onCreate', 'FRAMEWORK', 'the first access to media-library.db creates it (a fresh install)', evidence=_FW_SQLITE_EARLY + '; SRC MediaLibraryBackend.java:69-71, 80-82')
e('MediaLibraryBackend.<init>', 'MediaLibraryBackend.onUpgrade', 'FRAMEWORK', 'an older media-library.db from an earlier install is on disk', env=ENV_OLDDB, evidence=_FW_SQLITE_EARLY + '; SRC MediaLibraryBackend.java:69-71, 93-95')
e('MediaScanner.startQuickScan', 'MediaScanner.handleMessage', 'ASYNC', 'mHandler.sendMessageDelayed(MSG_GUESS_QUICKSCAN, delay)', evidence=FW_HANDLER + '; SRC MediaScanner.java:151-155')
sup(('MediaLibraryBackend.query', 'MediaLibraryBackend.debugQuery'))  # DEBUG = false (constant, MediaLibraryBackend.java:33): the call at line 306-307 is never taken

# ---- H1d. the SmoothAnimator family (LiftAnimator, DropAnimator, RemoveAnimator): a Runnable-based animation loop driven by View.post, not a bytecode-visible call
FW_VIEWPOST = 'FW-SRC core/java/android/view/View.java:15777-15781 (post adds the Runnable to the queue of the handler attached to the view, which calls its run() on the main thread)'
SA = 'DragSortListView$SmoothAnimator'
e(SA + '.start', SA + '.run', 'FRAMEWORK', 'post(this): the animation loop runs', evidence=FW_VIEWPOST + '; SRC DragSortListView.java:1178')
e(SA + '.run', SA + '.transform', 'CALL', 'each frame computes its eased fraction', evidence='SRC DragSortListView.java:1209 (bytecode)')
for sub in ('DropAnimator', 'RemoveAnimator'):  # LiftAnimator is never instantiated (its construction is commented out, DragSortListView.java:546): see UNREACHABLE
    node = 'DragSortListView$' + sub
    e(SA + '.start', node + '.onStart', 'CALL', 'onStart() (virtual call on the concrete animator instance; the bytecode scan resolved only the receiver type SmoothAnimator)', evidence='SRC DragSortListView.java:1177 (bytecode: invokevirtual SmoothAnimator.onStart)')
    e(SA + '.run', node + '.onUpdate', 'CALL', 'onUpdate(frac, smoothFrac) (virtual call, same as onStart)', evidence='SRC DragSortListView.java:1206, 1209 (bytecode: invokevirtual SmoothAnimator.onUpdate)')
    e(SA + '.run', node + '.onStop', 'CALL', 'the animation reached its end (virtual call, same as onStart)', guard='fraction >= 1f', evidence='SRC DragSortListView.java:1207 (bytecode: invokevirtual SmoothAnimator.onStop)')
# the default DragScrollProfile (DragSortListView$1) is used by DragScroller
e('DragSortListView.continueDrag', 'DragSortListView$DragScroller.startScrolling', 'CALL', 'the floating view enters the scroll-shuffle edge', evidence='SRC DragSortListView.java:1800-1850 (bytecode)')
e('DragSortListView$DragScroller.startScrolling', 'DragSortListView$DragScroller.run', 'FRAMEWORK', 'the auto-scroll loop reposts itself with post(this)', evidence=FW_VIEWPOST)
e('DragSortListView$DragScroller.run', 'DragSortListView$1.getSpeed', 'CALL', 'mScrollProfile.getSpeed(...): the default profile (no custom one was set)', evidence='SRC DragSortListView.java:2882-2920 (bytecode)')
# the cancel-on-change DataSetObserver registered once on the DragSortListView itself (mObserver, field initialiser of the constructor)
e('DragSortListView.<init>', 'DragSortListView$2.onChanged', 'FRAMEWORK', 'the adapter notifies a data change while dragging', needs_state=state_text('A drag is in progress when the adapter data changes', 'session'),
  evidence='INFERRED android.database.Observable.notifyChanged calls each registered DataSetObserver.onChanged (source not read); SRC DragSortListView.java:555-571')
e('DragSortListView.<init>', 'DragSortListView$2.onInvalidated', 'FRAMEWORK', 'the adapter notifies invalidation while dragging', needs_state=state_text('A drag is in progress when the adapter data is invalidated', 'session'),
  evidence='INFERRED android.database.Observable.notifyInvalidated calls each registered DataSetObserver.onInvalidated (source not read); SRC DragSortListView.java:555-571')
e('DragSortListView$2.onChanged', 'DragSortListView$2.cancel', 'CALL', 'cancel() stops the drag if one is in progress', guard='mDragState == DRAGGING', evidence='SRC DragSortListView.java:556-560 (bytecode)')

# ---- H1a2. PlaylistObserver (playlist file sync; constructed unconditionally in PlaybackService.onCreate, gated internally by the sync-mode bits)
PO = 'PlaylistObserver'
FW_SQLITE = 'FW-SRC core/java/android/database/sqlite/SQLiteOpenHelper.java:333, 338 (getWritableDatabase / getReadableDatabase call onCreate the first time the database file does not exist, and onUpgrade when the stored version is older than the requested one)'
e(PO + '.<init>', PO + '$1.<init>', 'CALL', 'the LibraryObserver field initialiser runs as part of the constructor', evidence='SRC PlaylistObserver.java:584-612 (bytecode)')
e(PO + '.<init>', PO + '$2.<init>', 'CALL', 'getFileObserver(mPlaylists) builds the FileObserver field', evidence='SRC PlaylistObserver.java:140, 614-649 (bytecode)')
e(PO + '.<init>', PO + '.onCreate', 'FRAMEWORK', 'the first access to the playlist_observer.db creates it', evidence=FW_SQLITE + '; SRC PlaylistObserver.java:116, 184-191')
e(PO + '.<init>', PO + '.onUpgrade', 'FRAMEWORK', 'an older playlist_observer.db from an earlier install is on disk', env=ENV_OLDDB, evidence=FW_SQLITE + '; SRC PlaylistObserver.java:116, 196-199')
e(PO + '.<init>', PO + '$2.onEvent', 'FRAMEWORK', 'mFileObserver.startWatching() (called by the FileObserver anonymous subclass\'s own constructor): a file system event in the watched playlist folder fires', env=ENV_FILESYS,
  evidence=FW_FILEOBS + '; SRC PlaylistObserver.java:140-141, 614-649')
e(PO + '.<init>', PO + '.handleMessage', 'ASYNC', 'sendUniqueMessage(MSG_FULL_SYNC_SCAN, 0): the handler thread runs the message', evidence=FW_HANDLER + '; SRC PlaylistObserver.java:143-144')
e(PO + '.handleMessage', PO + '.fullSyncScan', 'CALL', 'MSG_FULL_SYNC_SCAN', guard='message.what == MSG_FULL_SYNC_SCAN', evidence='SRC PlaylistObserver.java:236-238 (bytecode)')
e(PO + '.fullSyncScan', PO + '.getFileForName', 'CALL', 'a playlist exists in the library (the cursor over playlist_observer.db has a row)', needs_state=NEED_PLAYLIST, evidence='SRC PlaylistObserver.java:414-420 (bytecode)')
e(PO + '.fullSyncScan', PO + '.isM3uFilename', 'CALL', 'a .m3u file is listed in the sync folder', needs_state=NEED_M3U_FILE, evidence='SRC PlaylistObserver.java:449-453 (bytecode)')
e(PO + '.isM3uFilename', PO + '.fromM3u', 'CALL', 'the file matches *.m3u and has no known metadata row', needs_state=NEED_M3U_FILE, evidence='SRC PlaylistObserver.java:453-456 (bytecode)')
e(PO + '.fromM3u', PO + '.handleMessage', 'ASYNC', 'sendUniqueMessage(MSG_IMPORT_M3U, f)', needs_state=NEED_M3U_FILE, evidence=FW_HANDLER + '; SRC PlaylistObserver.java:456')
e(PO + '.handleMessage', PO + '.importM3uPlaylist', 'CALL', 'MSG_IMPORT_M3U', guard='message.what == MSG_IMPORT_M3U', needs_state=NEED_M3U_FILE, evidence='SRC PlaylistObserver.java:229-231 (bytecode)')
e(PO + '.importM3uPlaylist', PO + '.getHash', 'CALL', 'the sync mode includes import (the body returns at once otherwise)', needs_state=NEED_SYNC_IMPORT, evidence='SRC PlaylistObserver.java:303-309 (bytecode)')
e(PO + '.getHash', PO + '.updatePlaylistMetadata', 'CALL', 'the m3u is new or its hash changed: it is imported and its metadata recorded', needs_state=NEED_SYNC_IMPORT, evidence='SRC PlaylistObserver.java:333-348 (bytecode)')
e(PO + '.fullSyncScan', PO + '.dumpAsM3uPlaylist', 'CALL', 'the sync mode includes purge and the playlist still exists but its m3u file does not', needs_state=NEED_SYNC_PURGE, evidence='SRC PlaylistObserver.java:430-434 (bytecode)')
e(PO + '.fullSyncScan', PO + '.deletePlaylistMetadata', 'CALL', 'the native playlist was removed, or purge removed it: the metadata row is dropped', needs_state=NEED_SYNC_PURGE, evidence='SRC PlaylistObserver.java:423-428, 437 (bytecode)')
e(PO + '.handleMessage', PO + '.dumpAllAsM3uPlaylist', 'CALL', 'MSG_DUMP_ALL_M3U (forceM3uImport, or the "Force m3u import" overflow item of Settings > Media library)', needs_state=NEED_SYNC_EXPORT, guard='message.what == MSG_DUMP_ALL_M3U', evidence='SRC PlaylistObserver.java:226-227 (bytecode)')
e(PO + '.dumpAllAsM3uPlaylist', PO + '.handleMessage', 'ASYNC', 'a playlist exists: sendUniqueMessage(MSG_DUMP_M3U, id) for each row', needs_state=NEED_PLAYLIST, evidence=FW_HANDLER + '; SRC PlaylistObserver.java:268-274')
e(PO + '.handleMessage', PO + '.dumpAsM3uPlaylist', 'CALL', 'MSG_DUMP_M3U, the playlist still exists', guard='message.what == MSG_DUMP_M3U', needs_state=NEED_PLAYLIST, evidence='SRC PlaylistObserver.java:216-220 (bytecode)')
e(PO + '.handleMessage', PO + '.forceM3uImport', 'CALL', 'MSG_FORCE_M3U_IMPORT ("Force m3u import" overflow item of Settings > Media library)', guard='message.what == MSG_FORCE_M3U_IMPORT', evidence='SRC PlaylistObserver.java:233-234 (bytecode)')
e('PreferencesMediaLibrary.onOptionsItemSelected', PO + '.handleMessage', 'ASYNC', 'MENU_FORCE_M3U_IMPORT: notifyObserver(PLAYLIST, OUTDATED, false) reaches the PlaybackService observer, which sends MSG_FORCE_M3U_IMPORT', guard='item.getItemId() == MENU_FORCE_M3U_IMPORT',
  needs_state=NEED_SERVICE_UP, evidence='SRC PreferencesMediaLibrary.java:230-233; PlaybackService.java (LibraryObserver.onChange routes LibraryObserver.Type.PLAYLIST to PlaylistObserver); ' + FW_HANDLER)
e(PO + '$2.onEvent', PO + '.handleMessage', 'ASYNC', 'a file change is seen in the watched sync folder (FileObserver CREATE/DELETE/MOVED/MODIFY): sendUniqueMessage(MSG_FULL_SYNC_SCAN, 0)', env=ENV_FILESYS,
  evidence=FW_FILEOBS + '; SRC PlaylistObserver.java:626-649')

# ---- H1a3. PlaylistObserverDirActivity (opened from a PreferenceScreen row of S_PREFS_PLAYLIST, dependent on the sync-mode preference)
NEED_SYNC_ON = state_text('Settings > Playlists > Synchronization is not "Off" (the dependent "Synchronize to" row is enabled)', 'settings')
e('S_PREFS_PLAYLIST', 'PlaylistObserverDirActivity.<init>', 'INTENT', 'tap "Synchronize to": performClick starts the Intent of the PreferenceScreen', gui=['Tap "Synchronize to"'], needs_state=NEED_SYNC_ON,
  evidence=FW_PREF_INTENT + '; SRC res/xml/preference_playlist.xml:41-51; AndroidManifest.xml:194-195')
lifecycle('PlaylistObserverDirActivity', ('onCreate',), FW_ACT_CREATE, 'Activity lifecycle callback; SRC PlaylistObserverDirActivity.java:28-36')
e('PlaylistObserverDirActivity.onCreate', 'S_FOLDERPICKER', 'ENTERS', 'the folder browser opens at the configured sync folder', evidence='SRC PlaylistObserverDirActivity.java:28-36; FolderPickerActivity.java:68-93')
e('FolderPickerActivity$1.onClick', 'PlaylistObserverDirActivity.onFolderPicked', 'CALL', 'onFolderPicked(dir, included, excluded)', guard='the activity is PlaylistObserverDirActivity', evidence='SRC FolderPickerActivity.java:100-103 (bytecode)')

# ---- H1b. ShowQueueFragment long-press menu (owner Q of CoordClickListener and FancyMenu; mirrors C3's L and G1's P)
NEED_QUEUE_ROW = state_text('The queue holds at least one song (needed for a row to long-press)', 'data')
gui2('S_SLIDE_LIBRARY_QUEUE', CCL, CCL + '@Q', 'Long-press a song row of the queue', 'SRC CoordClickListener.java:69-72, 77-80; ' + FW_ITEMCLICK, needs_state=NEED_QUEUE_ROW)
e('ShowQueueFragment.onItemLongClickWithCoords', FM_SHOW['Q'], 'CALL', 'fm.show(view, x, y): the bottom sheet of the queue opens', needs_state=NEED_QUEUE_ROW, evidence='SRC ShowQueueFragment.java:108-130 (bytecode)')
e(FM_SHOW['Q'], 'S_FANCY_QUEUE', 'ENTERS', 'the BottomSheetDialog with the menu rows is shown', evidence='SRC FancyMenu.java:169-190; ' + FW_DIALOGFRAG.split(' (')[0])
gui2('S_FANCY_QUEUE', FMC, FMC + '@Q', 'Tap a row of the context menu', 'SRC FancyMenu.java:173-185; ' + FW_ITEMCLICK)
call(FMC + '@Q', 'ShowQueueFragment.onFancyItemSelected', 'mCallback.onFancyItemSelected(item) with the callback of this menu (ShowQueueFragment: new FancyMenu(getActivity(), this))', 'SRC FancyMenu.java:72-76, 178; ShowQueueFragment.java:111',
     guard='the menu was created by ShowQueueFragment')
gui('S_SLIDE_LIBRARY_QUEUE', 'ShowQueueFragment.onItemClick', 'Tap a song row of the queue', needs_state=NEED_QUEUE_ROW, evidence=FW_ITEMCLICK + '; SRC ShowQueueFragment.java:208-215 (bytecode)')


# ===================================================================== I. verdicts (UNREACHABLE), gate kinds, EDIT, CLASSIFY
_NOCALL = 'grep -rn over the app and library sources found no caller'
UNREACHABLE = {}

# ---- I1. FancyMenuItem: a custom android.view.MenuItem implementation; the app only ever calls getItemId/getIntent/setIntent on it
_FM_REASON = ('SRC ui/FancyMenuItem.java implements the full android.view.MenuItem interface, but every call site in the app '
              '(LibraryActivity, PlaylistActivity, ShowQueueFragment: FancyMenu.add(...).setIntent(intent), item.getItemId(), item.getIntent()) uses only getItemId, getIntent and setIntent; '
              + _NOCALL + ' of any other MenuItem method on a FancyMenuItem (no action view, submenu, checkable or shortcut feature is used by the bottom-sheet menu)')
for _m in ('collapseActionView', 'expandActionView', 'getActionProvider', 'getActionView', 'getAlphabeticShortcut', 'getGroupId', 'getMenuInfo', 'getNumericShortcut', 'getOrder', 'getSubMenu',
           'getTitleCondensed', 'hasSubMenu', 'isActionViewExpanded', 'isCheckable', 'isChecked', 'isEnabled', 'isVisible', 'setActionProvider', 'setActionView(int)', 'setActionView(View)',
           'setAlphabeticShortcut', 'setCheckable', 'setChecked', 'setEnabled', 'setIcon(Drawable)', 'setNumericShortcut', 'setOnActionExpandListener', 'setOnMenuItemClickListener', 'setShortcut',
           'setShowAsAction', 'setShowAsActionFlags', 'setTitle(int)', 'setTitleCondensed', 'setVisible'):
    UNREACHABLE['FancyMenuItem.' + _m] = ('no_trigger_in_app', _FM_REASON, 'SRC ui/FancyMenuItem.java', 'SOURCE')
UNREACHABLE['FancyMenu.add(int,int,int,CharSequence)'] = ('no_trigger_in_app',
    'SRC ui/FancyMenu.java declares add(int,int,int,CharSequence) and add(int,int,int,int) (drawable + string resource id); every call site (LibraryActivity, PlaylistActivity, ShowQueueFragment) uses the '
    'four-int overload with a string resource id, never a CharSequence; ' + _NOCALL + ' of the CharSequence overload', 'SRC ui/FancyMenu.java', 'SOURCE')

# ---- I2. com.mobeta.android.dslv dead classes/methods: DragSortCursorAdapter family is never subclassed by an app adapter (PlaylistAdapter extends
# android.widget.CursorAdapter directly, TabOrderAdapter/ShowQueueAdapter extend BaseAdapter, FolderPickerAdapter extends ArrayAdapter); confirmed by
# `grep -rln "SimpleDragSortCursorAdapter\|ResourceDragSortCursorAdapter\|DragSortCursorAdapter\b\|SimpleFloatViewManager" java/ch/blinkenlights/android/vanilla` = no results.
_DSCA_REASON = ('SRC com/mobeta/android/dslv/DragSortCursorAdapter.java (and its subclasses ResourceDragSortCursorAdapter, SimpleDragSortCursorAdapter): no class under ch.blinkenlights.android.vanilla '
                'extends DragSortCursorAdapter (PlaylistAdapter extends android.widget.CursorAdapter directly, TabOrderAdapter and ShowQueueAdapter extend BaseAdapter, FolderPickerAdapter extends ArrayAdapter); '
                + _NOCALL + ' of this class or its constructors anywhere in the app sources')
for _m in ('<init>(Context,Cursor)', '<init>(Context,Cursor,int)', '<init>(Context,Cursor,boolean)', 'changeCursor', 'getCursorPosition', 'getCursorPositions', 'getDropDownView', 'getItem', 'getItemId',
           'getListPosition', 'getView', 'reset', 'resetMappings', 'swapCursor'):
    UNREACHABLE['DragSortCursorAdapter.' + _m] = ('no_trigger_in_app', _DSCA_REASON, 'SRC com/mobeta/android/dslv/DragSortCursorAdapter.java', 'SOURCE')
for _m in ('<init>(Context,int,Cursor)', '<init>(Context,int,Cursor,int)', '<init>(Context,int,Cursor,boolean)', 'newDropDownView', 'newView', 'setDropDownViewResource', 'setViewResource'):
    UNREACHABLE['ResourceDragSortCursorAdapter.' + _m] = ('no_trigger_in_app', _DSCA_REASON, 'SRC com/mobeta/android/dslv/ResourceDragSortCursorAdapter.java', 'SOURCE')
for _m in ('<init>(Context,int,Cursor,String[],int[])', '<init>(Context,int,Cursor,String[],int[],int)', 'bindView', 'changeCursorAndColumns', 'convertToString', 'findColumns', 'getCursorToStringConverter',
           'getStringConversionColumn', 'getViewBinder', 'setCursorToStringConverter', 'setStringConversionColumn', 'setViewBinder', 'setViewImage', 'setViewText', 'swapCursor'):
    UNREACHABLE['SimpleDragSortCursorAdapter.' + _m] = ('no_trigger_in_app', _DSCA_REASON, 'SRC com/mobeta/android/dslv/SimpleDragSortCursorAdapter.java', 'SOURCE')
UNREACHABLE['SimpleFloatViewManager.setSecondaryOnTouchListener'] = ('branch_never_taken',
    'SRC com/mobeta/android/dslv/DragSortController.java:296-298 overrides setSecondaryOnTouchListener; the only FloatViewManager instance the app ever constructs is a DragSortController '
    '(DragSortListView.java:525-532: `new DragSortController(...)`, never `new SimpleFloatViewManager(...)`), so virtual dispatch on mFloatViewManager.setSecondaryOnTouchListener(...) always resolves to the '
    'DragSortController override, never to the SimpleFloatViewManager implementation (unlike onCreateFloatView/onDestroyFloatView, which DragSortController does not override and which do run)', 'SRC com/mobeta/android/dslv/DragSortController.java:296-298', 'SOURCE')

# ---- I3. DragSortController / DragSortListView: unused public convenience constructors and unused public getters/setters (the app always uses the one
# 6-argument DragSortController constructor and never reads these values back); confirmed with grep over ch.blinkenlights.android.vanilla.
_DSC_CTOR_REASON = ('SRC com/mobeta/android/dslv/DragSortController.java:97-107: the convenience constructors each call the next one with default arguments, ending at the 6-argument constructor; '
                    'DragSortListView.java:525-527 always calls the 6-argument constructor directly with explicit values read from the layout XML attributes; ' + _NOCALL + ' of the other constructor overloads')
for _m in ('<init>(DragSortListView)', '<init>(DragSortListView,int,int,int)', '<init>(DragSortListView,int,int,int,int)'):
    UNREACHABLE['DragSortController.' + _m] = ('no_trigger_in_app', _DSC_CTOR_REASON, 'SRC com/mobeta/android/dslv/DragSortController.java:97-107', 'SOURCE')
_DSC_API_REASON = 'SRC com/mobeta/android/dslv/DragSortController.java: unused public getter/setter of the library API; ' + _NOCALL + ' in the app sources'
for _m in ('getDragInitMode', 'getRemoveMode', 'isRemoveEnabled', 'isSortEnabled', 'setClickRemoveId', 'setDragHandleId', 'setFlingHandleId', 'setSecondaryOnTouchListener'):
    UNREACHABLE['DragSortController.' + _m] = ('no_trigger_in_app', _DSC_API_REASON, 'SRC com/mobeta/android/dslv/DragSortController.java', 'SOURCE')
UNREACHABLE['DragSortListView$LiftAnimator.<init>'] = ('no_trigger_in_app',
    'SRC com/mobeta/android/dslv/DragSortListView.java:546: `// mLiftAnimator = new LiftAnimator(smoothness, 100);` is commented out; ' + _NOCALL + ' of `new LiftAnimator(` anywhere else', 'SRC DragSortListView.java:546', 'SOURCE')
for _m in ('onStart', 'onUpdate'):
    UNREACHABLE['DragSortListView$LiftAnimator.' + _m] = ('no_trigger_in_app',
        'SRC com/mobeta/android/dslv/DragSortListView.java:546: mLiftAnimator is never constructed (the line is commented out), so its instance methods are never called', 'SRC DragSortListView.java:546, 1218-1249', 'SOURCE')
_DSLV_API_REASON = 'SRC com/mobeta/android/dslv/DragSortListView.java: unused public method of the library API, or a private helper called only from one (' + _NOCALL + ' of any caller in the app sources)'
UNREACHABLE['DragSortListView.moveItem'] = ('no_trigger_in_app',
    'SRC com/mobeta/android/dslv/DragSortListView.java:1474-1487 (public moveItem(from,to), calls the registered DropListener directly); the app never calls mListView.moveItem(...) - reordering instead goes '
    'through the internal drag machinery (dropFloatView), which calls the same DropListener; ' + _NOCALL + ' of moveItem(', 'SRC DragSortListView.java:1474-1487', 'SOURCE')
UNREACHABLE['DragSortListView.removeItem(int)'] = ('branch_never_taken',
    'SRC com/mobeta/android/dslv/DragSortController.java:452-458 (onSingleTapUp): removeItem(int) (the 1-argument overload) is called only when mRemoveMode == CLICK_REMOVE; every layout that uses this '
    'controller leaves remove_mode at its default (flingRemove) or does not set it; the other overload, removeItem(int,float), is the one the fling-to-remove path (stopDrag) actually calls', 'SRC DragSortController.java:166-172, 452-458', 'SOURCE')
for _m in ('adjustItem(int)', 'buildRunList', 'findFirstSetIndex', 'getFloatAlpha', 'getInputAdapter', 'insertionIndexForKey', 'invalidateFloatView', 'moveCheckState', 'printPosData', 'removeCheckState',
           'rotate', 'setDragScrollProfile', 'setDragSortListener', 'setFloatAlpha', 'setFloatViewManager', 'setMaxScrollSpeed', 'setOnTouchListener'):
    UNREACHABLE['DragSortListView.' + _m] = ('no_trigger_in_app', _DSLV_API_REASON, 'SRC com/mobeta/android/dslv/DragSortListView.java', 'SOURCE')

# ---- I4. static-only utility / constant classes: the implicit public constructor is never called (the class is used only through its static members)
for _m in ('PrefKeys.<init>', 'PrefDefaults.<init>', 'MediaLibrary.<init>', 'MediaSchema.<init>', 'MediaMigrations.<init>', 'FileUtils.<init>', 'PluginUtils.<init>', 'PlayCountsHelper.<init>',
           'SharedPrefHelper.<init>', 'SystemUtils.<init>', 'ThemeHelper.<init>', 'MediaUtils.<init>', 'Playlist.<init>', 'LibraryObserver$Value.<init>'):
    UNREACHABLE[_m] = ('no_trigger_in_app', 'The class is used only through its static members (field constants / static methods); ' + _NOCALL + ' of `new ' + _m.split('.')[0].split('$')[0] + '(` anywhere in the app sources',
                        'SRC ' + _m.split('.')[0].split('$')[0] + '.java', 'SOURCE')
UNREACHABLE['MediaLibraryBackend.debugQuery'] = ('branch_never_taken',
    'SRC ch/blinkenlights/android/medialibrary/MediaLibraryBackend.java:33 (`private static final boolean DEBUG = false;`) and :306-307 (`if (DEBUG) debugQuery(...)`): DEBUG is a false compile-time constant, so the call is never taken', 'SRC MediaLibraryBackend.java:33, 306-307', 'SOURCE')

# ---- I5. singles found this session (219 "no path" methods in the fresh build): each read at its own call site, see AGENT_NOTES.md for the triage log
UNREACHABLE['MediaScanner$MediaScanPlan.addOptionalStep'] = ('no_trigger_in_app',
    'SRC ch/blinkenlights/android/medialibrary/MediaScanner.java:793-795 declares addOptionalStep; every real caller of the MediaScanPlan (guessQuickScanPlan:371-377, rpcNativeVerify, rpcLibraryVerify) uses only addNextStep; '
    + _NOCALL + ' of addOptionalStep( or addChainedStep( anywhere in the app sources', 'SRC MediaScanner.java:793-795', 'SOURCE')
UNREACHABLE['MediaScanner$MediaScanPlan.addChainedStep'] = ('no_trigger_in_app',
    'SRC ch/blinkenlights/android/medialibrary/MediaScanner.java:805-807 declares addChainedStep; ' + _NOCALL + ' of addChainedStep( anywhere in the app sources (only addNextStep is ever called)', 'SRC MediaScanner.java:805-807', 'SOURCE')
UNREACHABLE['CoverBitmap.<init>'] = ('no_trigger_in_app', 'SRC CoverBitmap.java:46 (`public final class CoverBitmap`): every member used by the app (createBitmap, generateDefaultCover, generatePlaceholderCover, STYLE_* constants) is static; '
    + _NOCALL + ' of `new CoverBitmap(` anywhere in the app sources', 'SRC CoverBitmap.java', 'SOURCE')
UNREACHABLE['ThemeHelper.usesDarkTheme'] = ('no_trigger_in_app', 'SRC ThemeHelper.java:80-86 (private static method); ' + _NOCALL + ' of usesDarkTheme( anywhere in the app sources (dead private helper)', 'SRC ThemeHelper.java:80', 'SOURCE')
UNREACHABLE['Common.debug'] = ('no_trigger_in_app', 'SRC ch/blinkenlights/bastp/Common.java:75-77 (public instance method, prints to stdout); ' + _NOCALL + ' of .debug( on a Common/Mp4File/Id3Tag instance anywhere in the bastp or app sources', 'SRC Common.java:75-77', 'SOURCE')
UNREACHABLE['Mp4File.printDebugAtomPath'] = ('branch_never_taken',
    'SRC ch/blinkenlights/bastp/Mp4File.java:87 (`final static boolean PRINT_DEBUG = false;`) and :176 (`if (PRINT_DEBUG) { printDebugAtomPath(...); }`): PRINT_DEBUG is a false compile-time constant, so the call is never taken (same pattern as MediaLibraryBackend.DEBUG)',
    'SRC Mp4File.java:87, 176', 'SOURCE')
UNREACHABLE['Song.compareTo'] = ('no_trigger_in_app', 'SRC Song.java:36 (`implements Comparable<Song>`) and :290-296 (compareTo); ' + _NOCALL + ' of .compareTo( on a Song, Collections.sort(songList) (natural order) or Arrays.sort on an array of Song anywhere in the app sources '
    '(SongTimeline sorts with the explicit IdComparator / FlagComparator instead)', 'SRC Song.java:290-296', 'SOURCE')
UNREACHABLE['Song.toString'] = ('no_trigger_in_app', 'SRC Song.java:281-287 (toString); ' + _NOCALL + ' of .toString() on a Song or an implicit string conversion (string concatenation, log call) of a Song anywhere in the app sources', 'SRC Song.java:281-287', 'SOURCE')
UNREACHABLE['SlidingView.<init>(Context)'] = ('no_trigger_in_app',
    'SRC SlidingView.java:110-113 (1-argument convenience constructor, calls this(context, null)); the only place SlidingView is built is XML inflation of library_content.xml / full_playback_alt.xml, which calls the (Context, AttributeSet) constructor directly through reflection; '
    + _NOCALL + ' of `new SlidingView(` in the app sources', 'SRC SlidingView.java:110-113', 'SOURCE')
UNREACHABLE['DraggableRow.isChecked'] = ('no_trigger_in_app',
    'SRC DraggableRow.java:35 (`implements Checkable`) and :111-113 (isChecked); FW-SRC core/java/android/widget/ListView.java:2109-2114 and core/java/android/widget/AbsListView.java:1169-1179 (the framework\'s row check-state update calls only Checkable.setChecked on a bound row view, never isChecked); '
    + _NOCALL + ' of row.isChecked() / getCoverView-style access to a DraggableRow\'s isChecked() in the app sources', 'SRC DraggableRow.java:111-113', 'SOURCE')
UNREACHABLE['DraggableRow.toggle'] = ('no_trigger_in_app',
    'SRC DraggableRow.java:122-124 (toggle calls setChecked(!mChecked)); same reasoning as isChecked: the framework only calls setChecked on a Checkable row view, never toggle, and ' + _NOCALL + ' of row.toggle() in the app sources', 'SRC DraggableRow.java:122-124', 'SOURCE')
UNREACHABLE['DragSortItemViewCheckable.isChecked'] = ('no_trigger_in_app',
    'SRC com/mobeta/android/dslv/DragSortItemViewCheckable.java:34-39 (isChecked, delegates to the wrapped child); same reasoning as DraggableRow.isChecked: FW-SRC ListView.java:2109-2114 / AbsListView.java:1169-1179 call only Checkable.setChecked on the row view the ListView itself owns, never isChecked',
    'SRC com/mobeta/android/dslv/DragSortItemViewCheckable.java:34-39', 'SOURCE')
UNREACHABLE['DragSortItemViewCheckable.toggle'] = ('no_trigger_in_app',
    'SRC com/mobeta/android/dslv/DragSortItemViewCheckable.java:50-54 (toggle, delegates to the wrapped child); same reasoning: the framework never calls toggle() on a ListView row view', 'SRC com/mobeta/android/dslv/DragSortItemViewCheckable.java:50-54', 'SOURCE')
UNREACHABLE['DragSortItemView.getGravity'] = ('no_trigger_in_app',
    'SRC com/mobeta/android/dslv/DragSortItemView.java:45-47 (public getter); only setGravity is ever called (DragSortListView.java:1917, 1919, from the drop/lift animation); ' + _NOCALL + ' of .getGravity() on a DragSortItemView anywhere in the dslv or app sources',
    'SRC com/mobeta/android/dslv/DragSortItemView.java:45-47', 'SOURCE')
# CoverCache$CoverKey.equals is reached: LazyCoverView$CoverMsg.isRecent() calls `this.key.equals(this.view.mExpectedKey)` (LazyCoverView.java:88), found by the bytecode scan once isRecent's
# caller (LazyCoverView.handleMessage) was wired above; no UNREACHABLE entry needed, BitmapDiskCache.put/get keying by hashCode() alone does not make equals() itself unreachable.
UNREACHABLE['CoverCache$CoverKey.toString'] = ('no_trigger_in_app',
    'SRC CoverCache.java:193-195 (toString); ' + _NOCALL + ' of .toString() on a CoverKey or an implicit string conversion of one anywhere in the app sources', 'SRC CoverCache.java:193-195', 'SOURCE')
UNREACHABLE['SlidingTabLayout.<init>(Context)'] = ('no_trigger_in_app',
    'SRC SlidingTabLayout.java:82-85 (1-argument convenience constructor, calls this(context, null)); the only SlidingTabLayout subclass the app uses, VanillaTabLayout, calls this(context, attrs) from its own 1-argument constructor, which never reaches SlidingTabLayout\'s own 1- or 2-argument '
    'constructors (VanillaTabLayout always ends at the shared 3-argument super(context, attrs, defStyle)); XML inflation of library_content.xml also calls the (Context, AttributeSet) constructor of VanillaTabLayout directly', 'SRC SlidingTabLayout.java:82-85; VanillaTabLayout.java:31-39', 'SOURCE')
UNREACHABLE['SlidingTabLayout.<init>(Context,AttributeSet)'] = ('no_trigger_in_app',
    'SRC SlidingTabLayout.java:86-89 (2-argument convenience constructor); same reasoning as the 1-argument constructor: VanillaTabLayout\'s own constructor chain and XML inflation both go straight to the 3-argument constructor', 'SRC SlidingTabLayout.java:86-89; VanillaTabLayout.java:31-39', 'SOURCE')
UNREACHABLE['SlidingTabLayout.setContentDescription'] = ('no_trigger_in_app',
    'SRC SlidingTabLayout.java:230-232 (public setter, used by populateTabStrip only if mContentDescriptions holds a value for the tab); mContentDescriptions is never populated (no caller of setContentDescription); ' + _NOCALL + ' of .setContentDescription(int,String) anywhere in the app sources',
    'SRC SlidingTabLayout.java:230-232', 'SOURCE')
UNREACHABLE['SlidingTabLayout.setCustomTabColorizer'] = ('no_trigger_in_app',
    'SRC SlidingTabLayout.java:111-113 (public setter, forwards to SlidingTabStrip.setCustomTabColorizer); VanillaTabLayout only calls setSelectedIndicatorColors / setDistributeEvenly from its own constructor; ' + _NOCALL + ' of .setCustomTabColorizer( anywhere in the app sources',
    'SRC SlidingTabLayout.java:111-113', 'SOURCE')
UNREACHABLE['SlidingTabLayout.setCustomTabView'] = ('no_trigger_in_app',
    'SRC SlidingTabLayout.java:144-147 (public setter, sets mTabViewLayoutId/mTabViewTextViewId, read by populateTabStrip); never called, so populateTabStrip always builds the default tab view (createDefaultTabView); ' + _NOCALL + ' of .setCustomTabView( anywhere in the app sources',
    'SRC SlidingTabLayout.java:144-147, 201-203', 'SOURCE')
UNREACHABLE['SlidingTabStrip.setCustomTabColorizer'] = ('no_trigger_in_app',
    'SRC SlidingTabStrip.java:76-79: the only caller is SlidingTabLayout.setCustomTabColorizer (SlidingTabLayout.java:112), itself unreachable (never called by the app); ' + _NOCALL + ' of a second caller', 'SRC SlidingTabStrip.java:76-79', 'SOURCE')
# dead-cluster-internal bytecode edges: the caller of each is itself UNREACHABLE (no app trigger reaches it), so these are not real incoming edges
sup(('SlidingTabLayout.<init>(Context)', 'SlidingTabLayout.<init>(Context,AttributeSet)'), ('SlidingTabLayout.setCustomTabColorizer', 'SlidingTabStrip.setCustomTabColorizer'))
UNREACHABLE['VanillaTabLayout.<init>(Context)'] = ('no_trigger_in_app',
    'SRC VanillaTabLayout.java:31-33 (1-argument convenience constructor, calls this(context, null)); the only place VanillaTabLayout is built is XML inflation of library_content.xml, which calls the (Context, AttributeSet) constructor directly through reflection; '
    + _NOCALL + ' of `new VanillaTabLayout(` with one argument in the app sources', 'SRC VanillaTabLayout.java:31-33', 'SOURCE')
_FSGLV_REASON = 'SRC FastScrollGuardedListView.java: unused convenience constructor; XML inflation of listview.xml always calls the (Context, AttributeSet) constructor directly through reflection; ' + _NOCALL + ' of this overload in the app sources'
for _m, _ln in (('<init>(Context)', '47-49'), ('<init>(Context,AttributeSet,int)', '53-55'), ('<init>(Context,AttributeSet,int,int)', '56-58')):
    UNREACHABLE['FastScrollGuardedListView.' + _m] = ('no_trigger_in_app', _FSGLV_REASON, 'SRC FastScrollGuardedListView.java:' + _ln, 'SOURCE')
UNREACHABLE['VanillaImageButton.<init>(Context)'] = ('no_trigger_in_app',
    'SRC VanillaImageButton.java:37-39 (1-argument convenience constructor, calls this(context, null)); every place VanillaImageButton is built is XML inflation (controls.xml), which calls the (Context, AttributeSet) constructor directly through reflection; '
    + _NOCALL + ' of `new VanillaImageButton(` with one argument in the app sources', 'SRC VanillaImageButton.java:37-39', 'SOURCE')
UNREACHABLE['PlaylistObserver$Database.<init>'] = ('no_trigger_in_app',
    'SRC PlaylistObserver.java:102-117 (`private static class Database`, only static final fields: TABLE_NAME, _ID, NAME, HASH, FILLED_PROJECTION); every use (onCreate, onUpgrade, getHash, updatePlaylistMetadata, deletePlaylistMetadata, getFileForName, ...) '
    'reads a static field (Database.TABLE_NAME etc.); ' + _NOCALL + ' of `new Database(` anywhere in PlaylistObserver.java', 'SRC PlaylistObserver.java:102-117', 'SOURCE')
UNREACHABLE['SongTimeline.reshuffleTimeline'] = ('no_trigger_in_app',
    'SRC SongTimeline.java:547-556 (private method, shuffles the timeline but keeps the current queue position); ' + _NOCALL + ' of reshuffleTimeline( anywhere in SongTimeline.java or the app sources (dead private helper, no menu action or preference change calls it)',
    'SRC SongTimeline.java:547-556', 'SOURCE')

# ---- I6. dead-cluster-internal bytecode edges: each caller below is itself UNREACHABLE (part of the same dead library cluster: unused DragSortController/DragSortListView
# convenience ctors and setters, the whole DragSortCursorAdapter family, LiftAnimator), so these "incoming edges" never actually run; sup() them (same pattern as openlauncher's UNREACHABLE cluster)
sup(
    ('DragSortController.<init>(DragSortListView)', 'DragSortController.<init>(DragSortListView,int,int,int)'),
    ('DragSortController.<init>(DragSortListView,int,int,int)', 'DragSortController.<init>(DragSortListView,int,int,int,int)'),
    ('DragSortListView.setOnTouchListener', 'DragSortController.setSecondaryOnTouchListener'),
    ('DragSortListView.setOnTouchListener', 'SimpleFloatViewManager.setSecondaryOnTouchListener'),
    ('ResourceDragSortCursorAdapter.<init>(Context,int,Cursor)', 'DragSortCursorAdapter.<init>(Context,Cursor)'),
    ('ResourceDragSortCursorAdapter.<init>(Context,int,Cursor,int)', 'DragSortCursorAdapter.<init>(Context,Cursor,int)'),
    ('ResourceDragSortCursorAdapter.<init>(Context,int,Cursor,boolean)', 'DragSortCursorAdapter.<init>(Context,Cursor,boolean)'),
    ('SimpleDragSortCursorAdapter.changeCursorAndColumns', 'DragSortCursorAdapter.changeCursor'),
    ('DragSortCursorAdapter.swapCursor', 'DragSortCursorAdapter.resetMappings'),
    ('DragSortCursorAdapter.changeCursor', 'DragSortCursorAdapter.resetMappings'),
    ('DragSortCursorAdapter.reset', 'DragSortCursorAdapter.resetMappings'),
    ('SimpleDragSortCursorAdapter.swapCursor', 'DragSortCursorAdapter.swapCursor'),
    ('DragSortListView.moveCheckState', 'DragSortListView.buildRunList'),
    ('DragSortListView.removeCheckState', 'DragSortListView.buildRunList'),
    ('DragSortListView.buildRunList', 'DragSortListView.findFirstSetIndex'),
    ('DragSortListView.moveItem', 'DragSortListView.getInputAdapter'),
    ('DragSortListView.findFirstSetIndex', 'DragSortListView.insertionIndexForKey'),
    ('DragSortListView.moveCheckState', 'DragSortListView.rotate'),
    ('DragSortListView.removeCheckState', 'DragSortListView.rotate'),
    ('DragSortListView$SmoothAnimator.start@DragSortListView$LiftAnimator', 'DragSortListView$LiftAnimator.onStart'),
    ('DragSortListView$SmoothAnimator.run@DragSortListView$LiftAnimator', 'DragSortListView$LiftAnimator.onUpdate'),
    ('SimpleDragSortCursorAdapter.<init>(Context,int,Cursor,String[],int[])', 'ResourceDragSortCursorAdapter.<init>(Context,int,Cursor)'),
    ('SimpleDragSortCursorAdapter.<init>(Context,int,Cursor,String[],int[],int)', 'ResourceDragSortCursorAdapter.<init>(Context,int,Cursor,int)'),
    ('SimpleDragSortCursorAdapter.<init>(Context,int,Cursor,String[],int[])', 'SimpleDragSortCursorAdapter.findColumns'),
    ('SimpleDragSortCursorAdapter.<init>(Context,int,Cursor,String[],int[],int)', 'SimpleDragSortCursorAdapter.findColumns'),
    ('SimpleDragSortCursorAdapter.swapCursor', 'SimpleDragSortCursorAdapter.findColumns'),
    ('SimpleDragSortCursorAdapter.changeCursorAndColumns', 'SimpleDragSortCursorAdapter.findColumns'),
    ('SimpleDragSortCursorAdapter.bindView', 'SimpleDragSortCursorAdapter.setViewImage'),
    ('SimpleDragSortCursorAdapter.bindView', 'SimpleDragSortCursorAdapter.setViewText'),
)
