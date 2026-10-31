# AnkiDroid batch 104 (LABEL helper): libanki hooks (Hook, Hooks, Leech, ChessFilter, HebrewFixFilter, ExternalHookLoader,
# AdvancedStatistics inner classes), and the AnkiPackageExporter ZipFile class. 32 methods.
# The row list is in graphs/AnkiDroid/parts/label_104.md. Automatic bytecode CALL edges are not written here.
# Two e() edges are written (the registry dispatch into the leech hook, and the UI-thread post of its toast).
# 19 methods are UNREACHABLE (18 no_trigger_in_app, 1 branch_never_taken). The rest are REACHABLE and need no entry here.

e('Hooks.runHook', 'Leech$LeechHook.runHook', 'CALL',
  'a review answer makes a card a leech: Hooks.runHook loops over the hooks registered under the key leech and calls runHook on each, which is LeechHook.runHook',
  cls='non_standard',
  via=['hook registry dispatch (Hooks.runHook loops over the Hook objects registered under the key leech and calls func.runHook; the only registrant is Leech.LeechHook, installed by the Hooks constructor)'],
  evidence='SRC com/ichi2/libanki/hooks/Hooks.java:52, 114-128; com/ichi2/libanki/hooks/Leech.java:33-37, 60-62; com/ichi2/libanki/Sched.java:1721-1723',
  note='MISSING GATE MG982: the card must reach the leech threshold of its deck on a lapse answer (Sched.java:1697-1702 and 1365). No predefined STATE constant covers this, so env and needs_state are unset. The call at Sched.java:1723 also needs mContextReference to be set (Reviewer.java:115), otherwise the block at Sched.java:1721 is skipped.')

e('Leech$LeechHook.runHook', 'Leech$LeechHook$1.run', 'ASYNC',
  'the leech hook posts the toast Runnable to the UI thread, because the answer runs on the background DeckTask thread',
  cls='non_standard',
  via=['Handler message dispatch (Activity.runOnUiThread posts the Runnable to the UI-thread Handler when called off the UI thread; the Handler runs Message.callback.run)'],
  evidence='SRC com/ichi2/libanki/hooks/Leech.java:38, 46-51; FW-SRC core/java/android/app/Activity.java:6170-6176; FW-SRC core/java/android/os/Handler.java:355-358, 789-791',
  note='MISSING GATE MG983: the Activity passed to the hook must be non-null (Leech.java:38). It is the Reviewer, held by the WeakReference set at Reviewer.java:115 and still alive. No predefined constant covers this, so env and needs_state are unset. runOnUiThread posts only when the current thread is not the UI thread (Activity.java:6171-6172).')

UNREACHABLE['AdvancedStatistics$ArrayUtils.createIntMatrix'] = ('no_trigger_in_app',
  'Declared in the private inner class ArrayUtils. The field ArrayUtils (AdvancedStatistics.java:136) is used for transposeMatrix, stringToLongArray, formatMatrix, createDoubleMatrix and toIntMatrix only. Nothing in the source root calls createIntMatrix.',
  'com/ichi2/libanki/hooks/AdvancedStatistics.java:136, 1119-1129', 'SOURCE')

UNREACHABLE['AdvancedStatistics$ArrayUtils.append'] = ('no_trigger_in_app',
  'The only calls to ArrayUtils.append are in commented-out lines (AdvancedStatistics.java:340 and 393). No live caller exists in the source root.',
  'com/ichi2/libanki/hooks/AdvancedStatistics.java:339-340, 393, 1162-1169', 'SOURCE')

UNREACHABLE['AdvancedStatistics$ArrayUtils.nCols'] = ('no_trigger_in_app',
  'The only calls to ArrayUtils.nCols are in the commented-out lines 339-340. No live caller exists in the source root.',
  'com/ichi2/libanki/hooks/AdvancedStatistics.java:339-340, 1175-1179', 'SOURCE')

UNREACHABLE['AdvancedStatistics$ArrayUtils.nRows'] = ('no_trigger_in_app',
  'No call to nRows exists anywhere in the source root (grep finds only the declaration at line 1171).',
  'com/ichi2/libanki/hooks/AdvancedStatistics.java:1171-1173', 'SOURCE')

UNREACHABLE['AdvancedStatistics$Card.getId'] = ('no_trigger_in_app',
  'Declared in the private inner class Card. No call to getId() exists in AdvancedStatistics.java (grep finds only the declaration), and the class is private, so no other file can call it.',
  'com/ichi2/libanki/hooks/AdvancedStatistics.java:399, 442-444', 'SOURCE')

UNREACHABLE['AdvancedStatistics$Card.setDue'] = ('no_trigger_in_app',
  'Declared in the private inner class Card. No call to setDue exists in AdvancedStatistics.java (grep finds only the declaration). The class is private, so no other file can call it.',
  'com/ichi2/libanki/hooks/AdvancedStatistics.java:399, 466-468', 'SOURCE')

UNREACHABLE['AdvancedStatistics$Card.setFactor'] = ('no_trigger_in_app',
  'Declared in the private inner class Card. The only call is the commented-out line 836 (c.setFactor(factor)). No live caller exists.',
  'com/ichi2/libanki/hooks/AdvancedStatistics.java:399, 458-460, 836', 'SOURCE')

UNREACHABLE['AdvancedStatistics$Card.toString'] = ('no_trigger_in_app',
  'Declared in the private inner class Card. The implicit calls come only from string concatenation in ReviewOutcome.toString (line 1499) and in Review.writeLog (lines 1715-1716). Both are unreachable (see the rows for those methods), so nothing reaches Card.toString.',
  'com/ichi2/libanki/hooks/AdvancedStatistics.java:399, 409-412, 1497-1499, 1710-1716', 'SOURCE')

UNREACHABLE['AdvancedStatistics$Review.writeLog'] = ('no_trigger_in_app',
  'Private method of the inner class Review. Its only call is commented out (AdvancedStatistics.java:1685, //writeLog(newCard, outcomeProb)). No live caller exists.',
  'com/ichi2/libanki/hooks/AdvancedStatistics.java:1685, 1710-1714', 'SOURCE')

UNREACHABLE['AdvancedStatistics$ReviewOutcome.toString'] = ('no_trigger_in_app',
  'Declared in the private inner class ReviewOutcome. The only mention in a call position is the commented-out Timber line at 1680. ReviewOutcome has no live string concatenation in the source root.',
  'com/ichi2/libanki/hooks/AdvancedStatistics.java:1474, 1497-1500, 1680', 'SOURCE')

UNREACHABLE['ExternalHookLoader.<init>'] = ('no_trigger_in_app',
  'The class ExternalHookLoader has no construction site in the source root (grep for ExternalHookLoader outside its own file finds nothing). Without an instance, its constructor never runs.',
  'com/ichi2/libanki/hooks/ExternalHookLoader.java:16, 31-34', 'SOURCE')

UNREACHABLE['ExternalHookLoader.importExternalHook'] = ('no_trigger_in_app',
  'Public method of ExternalHookLoader. The class is never instantiated and the method has no caller in the source root (grep finds no reference outside the file).',
  'com/ichi2/libanki/hooks/ExternalHookLoader.java:43-77', 'SOURCE')

UNREACHABLE['ExternalHookLoader.prepareDex'] = ('no_trigger_in_app',
  'Private method. Its only caller is PrepareDexTask.doInBackground (line 130), which is created only in importExternalHook (line 52). importExternalHook has no caller, so prepareDex never runs.',
  'com/ichi2/libanki/hooks/ExternalHookLoader.java:80-112, 128-130, 52', 'SOURCE')

UNREACHABLE['ExternalHookLoader$PrepareDexTask.<init>'] = ('no_trigger_in_app',
  'Implicit constructor of the private inner class PrepareDexTask. The only creation site is line 52, inside importExternalHook, which has no caller.',
  'com/ichi2/libanki/hooks/ExternalHookLoader.java:52, 114', 'SOURCE')

UNREACHABLE['ExternalHookLoader$PrepareDexTask.doInBackground'] = ('no_trigger_in_app',
  'AsyncTask calls doInBackground only after execute() on a PrepareDexTask. The only execute() call is at line 52, inside importExternalHook, which has no caller.',
  'com/ichi2/libanki/hooks/ExternalHookLoader.java:52, 128-132', 'SOURCE')

UNREACHABLE['ExternalHookLoader$PrepareDexTask.onCancelled'] = ('no_trigger_in_app',
  'AsyncTask calls onCancelled only for a task that was started by execute(). The only execute() call is at line 52, inside importExternalHook, which has no caller.',
  'com/ichi2/libanki/hooks/ExternalHookLoader.java:52, 116-120', 'SOURCE')

UNREACHABLE['ExternalHookLoader$PrepareDexTask.onPostExecute'] = ('no_trigger_in_app',
  'AsyncTask calls onPostExecute only for a task that was started by execute(). The only execute() call is at line 52, inside importExternalHook, which has no caller.',
  'com/ichi2/libanki/hooks/ExternalHookLoader.java:52, 122-126', 'SOURCE')

UNREACHABLE['Hook.hashCode'] = ('no_trigger_in_app',
  'Hooks keeps Hook objects in an ArrayList (Hooks.java:75, 85, 100) and compares them with equals (Hooks.java:79, 99). The Map key is a String (Hooks.java:36). No HashSet or HashMap keyed by a Hook exists in the source root, so nothing calls Hook.hashCode.',
  'com/ichi2/libanki/hooks/Hook.java:34-40; com/ichi2/libanki/hooks/Hooks.java:36, 73-87, 96-105', 'SOURCE')

UNREACHABLE['Hook.runHook'] = ('branch_never_taken',
  'The base body is empty (Hook.java:64-66). Hooks.runHook calls func.runHook (Hooks.java:121), but the only key dispatched through runHook is leech (Sched.java:1723), and its only registrant is LeechHook, which overrides runHook (Leech.java:35). So the base body never runs.',
  'com/ichi2/libanki/hooks/Hook.java:64-66; com/ichi2/libanki/hooks/Hooks.java:114-128; com/ichi2/libanki/hooks/Leech.java:33-37, 61; com/ichi2/libanki/Sched.java:1723', 'SOURCE')
