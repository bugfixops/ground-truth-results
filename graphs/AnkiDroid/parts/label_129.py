# AnkiDroid batch 129 (LABEL helper). CompatHelper, the Compat implementations on the API 27 path, the DeckTask launch
# and listener, and the Custom Tabs helpers. 37 methods: 30 REACHABLE, 7 UNREACHABLE (closed_by_api_level).
# The full row list is in graphs/AnkiDroid/parts/label_129.md.
#
# Route ownership:
# - The CALL edges out of CompatHelper, the Compat* constructors, AnkiActivity, DeckPicker, DB, Storage and the widget
#   code come from auto_calls.json and are not written here. Among them, the CHA targets on CompatV10 and the branch
#   edges of the CompatHelper constructor that API 27 never takes are named in the final answer for suppression.
# - Written here: the AsyncTask hops out of DeckTask.launchDeckTask (execute, then onPreExecute on the calling thread,
#   then doInBackground on the worker thread), because the source method is in this batch.
# - No gate constant is used by these two edges (env=None). Browser and widget gates are named in the row reasons.

e('DeckTask.launchDeckTask', 'DeckTask.doInBackground', 'ASYNC',
  'AsyncTask.execute hands the task to the worker thread, which calls DeckTask.doInBackground (the task body)',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-595, 632-651, 326-333',
  note='executeOnExecutor (AsyncTask.java:632-651) hands mWorker to exec.execute at line 651; the worker call at line 333 runs doInBackground.')

e('DeckTask.launchDeckTask', 'DeckTask.onPreExecute', 'FRAMEWORK',
  'AsyncTask.executeOnExecutor calls onPreExecute on the calling UI thread before the worker starts; DeckTask.onPreExecute forwards to the listener',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:129-134, 344-347; FW-SRC core/java/android/os/AsyncTask.java:594-595, 632-648, 412-413',
  note='Runs synchronously inside execute() on the thread that called launchDeckTask.')

UNREACHABLE['CompatV10.disableDatabaseWriteAheadLogging'] = ('closed_by_api_level', 'Overridden by CompatV16.disableDatabaseWriteAheadLogging, and no override calls super. On API 27 CompatHelper selects CompatV21, and the nearest override up its superclass chain is CompatV16, so this empty body never runs.', 'com/ichi2/compat/CompatV10.java:69-71; com/ichi2/compat/CompatV16.java:29-32; com/ichi2/compat/CompatHelper.java:35-36; com/ichi2/compat/CompatV21.java:13', 'SOURCE')

UNREACHABLE['CompatV10.enableCookiesForFileSchemePages'] = ('closed_by_api_level', 'Overridden by CompatV12.enableCookiesForFileSchemePages. CompatV15 to CompatV21 do not override it and no override calls super, so on API 27 the CompatV12 body runs (AnkiDroidApp.onCreate:177) and this Timber.w body never does.', 'com/ichi2/compat/CompatV10.java:74-77; com/ichi2/compat/CompatV12.java:14-21; com/ichi2/compat/CompatV15.java:11; com/ichi2/anki/AnkiDroidApp.java:177', 'SOURCE')

UNREACHABLE['CompatV10.prepareWebViewCookies'] = ('closed_by_api_level', 'Overridden by CompatV21.prepareWebViewCookies (empty body). API 27 selects CompatV21, so the CompatV10 CookieSyncManager body never runs (AnkiDroidApp.onCreate:180 dispatches to CompatV21).', 'com/ichi2/compat/CompatV10.java:79-83; com/ichi2/compat/CompatV21.java:23-27; com/ichi2/anki/AnkiDroidApp.java:180', 'SOURCE')

UNREACHABLE['CompatV10.updateWidgetDimensions'] = ('closed_by_api_level', 'Overridden by CompatV16.updateWidgetDimensions. API 27 selects CompatV21, whose chain reaches CompatV16 first, so this empty body never runs; the automatic CHA edges to it (AnkiDroidWidgetSmall.java:72, 171) name a target that does not run on API 27.', 'com/ichi2/compat/CompatV10.java:97-100; com/ichi2/compat/CompatV16.java:42-43; com/ichi2/widget/AnkiDroidWidgetSmall.java:171', 'SOURCE')

UNREACHABLE['CompatV11.disableDatabaseWriteAheadLogging'] = ('closed_by_api_level', 'Shadowed by the CompatV16 override (db.disableWriteAheadLogging), which is the nearest override above CompatV21 and does not call super. On API 27 the rawQuery PRAGMA body never runs.', 'com/ichi2/compat/CompatV11.java:34-38; com/ichi2/compat/CompatV16.java:29-32; com/ichi2/compat/CompatHelper.java:35-36', 'SOURCE')

UNREACHABLE['CompatV15NookHdOrHdPlus.<init>'] = ('closed_by_api_level', 'Created only when isNookHdOrHdPlus() is true and getSdkVersion() == 15 (CompatHelper.java:33-34). API 27 fails the SDK test, so this constructor never runs. The automatic exact edge CompatHelper.<init> -> CompatV15NookHdOrHdPlus.<init> is a suppression candidate.', 'com/ichi2/compat/CompatHelper.java:33-34; com/ichi2/compat/CompatV15NookHdOrHdPlus.java:14', 'SOURCE')

UNREACHABLE['CompatV15NookHdOrHdPlus.disableDatabaseWriteAheadLogging'] = ('closed_by_api_level', 'Only reachable through a CompatV15NookHdOrHdPlus instance, which API 27 never creates (the instance needs SDK 15, CompatHelper.java:33-34). The method is not on the API 21+ superclass chain of CompatV21.', 'com/ichi2/compat/CompatV15NookHdOrHdPlus.java:16-19; com/ichi2/compat/CompatHelper.java:33-34', 'SOURCE')
