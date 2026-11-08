# AnkiDroid batch 028 (LABEL helper). DeckOptions part 2 of 2: 13 methods (scratch/batches/batch_028.txt).
# The full row list is in graphs/AnkiDroid/parts/label_028.md.
#
# Route ownership:
# - E1 and E4 have a page source (S_DECKOPTIONS) and a destination in this batch, so they belong to this part.
# - E2 and E3 have their source in this batch (remConf launches the conf-remove DeckTask at DeckOptions.java:403-405).
# - Automatic CALL edges from graphs/AnkiDroid/auto_calls.json are not re-added: Editor.commit -> remConf (line 28447),
#   Editor$1.onPositive -> remConf (line 22223), Editor.commit -> Editor$1.<init> (line 28439), Editor.<init> ->
#   Editor$2.<init> (line 28343), buildLists -> JSONNameComparator.<init> (lines 27330-27331).
# - Gates: MG222 (the schema is unchanged since the last upload; stored state, no predefined constant) and MG223 (a
#   second options group exists; no predefined constant). env and needs_state are left unset on every edge below.
# - Lead for the orchestrator (not suppressed here): the automatic CALL edges DeckTask$TaskListener.onProgressUpdate ->
#   Editor$2.onProgressUpdate (auto_calls.json lines 2092-2093) and DeckTask.onCancelled -> Editor$2.onCancelled
#   (lines 3324-3325) point into the two UNREACHABLE methods below. They are generic dispatch edges.

e('S_DECKOPTIONS', 'DeckOptions$DeckPreferenceHack$Editor.putString', 'GUI',
  'tap OK in the confAdd or confRename text dialog (EditTextPreference), which persists the value',
  gui=['tap OK in the confAdd or confRename text dialog (EditTextPreference), which persists the value'],
  evidence='SRC com/ichi2/anki/DeckOptions.java:338-341, 488-495; SRC res/xml/deck_options.xml:29-30, 43-44; FW-SRC core/java/android/preference/EditTextPreference.java:142-150, 88-100; FW-SRC core/java/android/preference/Preference.java:1609-1629, 1587-1598',
  note='EditTextPreference.onDialogClosed calls setText (EditTextPreference.java:148), which calls persistString (line 94), which calls putString (Preference.java:1625). The editor is DeckPreferenceHack.edit() because DeckOptions.getSharedPreferences returns mPref (DeckOptions.java:491-495). Editor.apply (DeckOptions.java:352-354) runs commit, which handles the confRename and confAdd keys (DeckOptions.java:218-242). No gate on a fresh install.')

e('DeckOptions$DeckPreferenceHack$Editor.remConf', 'DeckOptions$DeckPreferenceHack$Editor$2.onPreExecute', 'ASYNC',
  'the conf-remove DeckTask starts and calls its listener onPreExecute (shows the reordering dialog)',
  evidence='SRC com/ichi2/anki/DeckOptions.java:363-369, 399-410; SRC com/ichi2/async/DeckTask.java:129-134, 344-347, 1298-1301; FW-SRC core/java/android/os/AsyncTask.java:644-650',
  note='MISSING GATE MG223: a second options group must exist (id != 1), because remConf runs only for a non-default group (DeckOptions.java:243-251). env and needs_state unset. DeckTask.launchDeckTask (DeckOptions.java:403-405) runs AsyncTask.execute, which calls onPreExecute (AsyncTask.java:648); DeckTask.onPreExecute forwards to the listener (DeckTask.java:344-347); the TaskListener default calls the no-argument onPreExecute, which is this method (DeckTask.java:1298-1301).')

e('DeckOptions$DeckPreferenceHack$Editor.remConf', 'DeckOptions$DeckPreferenceHack$Editor$2.onPostExecute', 'ASYNC',
  'the conf-remove DeckTask finishes and calls its listener onPostExecute (rebuild the lists and restart the activity)',
  evidence='SRC com/ichi2/anki/DeckOptions.java:378-386, 399-410; SRC com/ichi2/async/DeckTask.java:129-134, 358-365, 1298-1313; FW-SRC core/java/android/os/AsyncTask.java:691-698',
  note='MISSING GATE MG223: a second options group must exist (id != 1), because remConf runs only for a non-default group (DeckOptions.java:243-251). env and needs_state unset. AsyncTask.finish calls onPostExecute (AsyncTask.java:691-698); DeckTask.onPostExecute forwards to the listener (DeckTask.java:358-365); the TaskListener default forwards to this method (DeckTask.java:1298-1313). Body: cacheValues, buildLists, updateSummaries, dismiss, restartActivity (DeckOptions.java:378-386).')

e('S_DECKOPTIONS', 'DeckOptions$DeckPreferenceHack$Editor$1.onPositive', 'GUI',
  'tap OK on the full-sync confirmation dialog shown after removing an options group that needs a full sync',
  gui=['tap OK on the full-sync confirmation dialog shown after removing an options group that needs a full sync'],
  evidence='SRC com/ichi2/anki/DeckOptions.java:243-271; SRC com/ichi2/libanki/Collection.java:337-344, 364-376, 395-407; SRC com/ichi2/libanki/Decks.java:708-712; SRC com/ichi2/libanki/sync/FullSyncer.java:154; SRC com/ichi2/libanki/Storage.java:317-319',
  note='MISSING GATE MG222: the confirmation dialog appears only when the schema marker is unchanged since the last full upload (Collection.modSchema throws when schemaChanged() is false, Collection.java:364-376; Collection.beforeUpload sets mLs = mScm at line 407, and FullSyncer calls it at line 154; a fresh collection has ls = 0, Storage.java:317-319). MISSING GATE MG223: a second options group must exist (DeckOptions.java:243-251). env and needs_state unset. The route continues with mCol.modSchemaNoCheck (Collection.java:337-344) and then remConf (automatic CALL, auto_calls.json line 22223).')

UNREACHABLE['DeckOptions$DeckPreferenceHack$Editor.putStringSet'] = ('framework_never_calls',
  'The only framework caller of putStringSet is Preference.persistStringSet (Preference.java:1662-1682, putStringSet at 1678). No code in this app calls persistStringSet, and res/xml/deck_options.xml has no MultiSelectListPreference (the XML uses EditTextPreference, ListPreference, CheckBoxPreference, CustomDialogPreference, StepsPreference, NumberRangePreference and Preference). MultiSelectListPreference is not in fw_src. The method is a TODO stub that returns null.',
  'SRC com/ichi2/anki/DeckOptions.java:358-361; FW-SRC core/java/android/preference/Preference.java:1662-1682; SRC res/xml/deck_options.xml:18-186; grep of com/ichi2 and res/xml finds no persistStringSet or MultiSelect use',
  'SOURCE')

UNREACHABLE['DeckOptions$DeckPreferenceHack$Editor.remove'] = ('no_trigger_in_app',
  'Editor.remove only removes the key from mUpdate. Nothing calls it: the framework preference package has no editor remove call, and the app preference classes in com/ichi2/preferences have no remove call (grep of both finds none). The only Editor.remove is the definition itself.',
  'SRC com/ichi2/anki/DeckOptions.java:345-349; grep of FW-SRC core/java/android/preference and SRC com/ichi2/preferences finds no editor remove call',
  'SOURCE')

UNREACHABLE['DeckOptions$DeckPreferenceHack$Editor$2.onCancelled'] = ('no_trigger_in_app',
  'DeckTask.onCancelled runs only after AsyncTask.cancel(true); AsyncTask.finish calls onCancelled only when isCancelled() is true. In-app DeckTask cancels go through DeckTask.cancelTask(int), which cancels only when the latest task has the given type. Every in-app caller passes SEARCH_CARDS or RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155). cancelTask() has no caller except cancelTask(int) (DeckTask.java:184). TaskOperations.stopTaskGracefully cancels a generic AsyncTask, not a DeckTask. So the conf-remove task is never cancelled. The automatic CALL DeckTask.onCancelled -> Editor$2.onCancelled (auto_calls.json lines 3324-3325) is a generic over-approximation.',
  'SRC com/ichi2/async/DeckTask.java:168-184, 368-370; FW-SRC core/java/android/os/AsyncTask.java:691-698; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; SRC com/ichi2/anki/runtimetools/TaskOperations.java:30-36; SRC com/ichi2/anki/DeckOptions.java:388-392',
  'SOURCE')

UNREACHABLE['DeckOptions$DeckPreferenceHack$Editor$2.onProgressUpdate'] = ('framework_never_calls',
  'AsyncTask calls onProgressUpdate only after publishProgress (AsyncTask.java:430-436). DeckTask.onProgressUpdate forwards only that call (DeckTask.java:350-355). The conf-remove body (DeckTask.java:961-982) contains no publishProgress (grep over lines 961-1000 finds none), and Sched.resortConf (Sched.java:2273-2286) does not publish. No conf task publishes progress, so the framework never calls this callback for this listener.',
  'SRC com/ichi2/anki/DeckOptions.java:373-374; SRC com/ichi2/async/DeckTask.java:350-355, 961-982; SRC com/ichi2/libanki/Sched.java:2273-2286; FW-SRC core/java/android/os/AsyncTask.java:430-436',
  'SOURCE')
