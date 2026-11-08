# AnkiDroid batch 040 (LABEL helper). ConfirmationDialog (8 methods) and CustomStudyDialog (27 methods).
# The full row list is in graphs/AnkiDroid/parts/label_040.md.
# Gates: MG342 (an empty card exists, empty-cards confirmation), MG343 (custom study session launch).
# Predefined constant: STATE_DECK (non-dynamic deck, custom study menu).
# Automatic CALL pairs NOT written here, to be suppressed (named in the final report):
#   DeckTask.onCancelled -> CustomStudyDialog$4.onCancelled (DeckTask.java:369)
#   DeckTask$TaskListener.onProgressUpdate -> CustomStudyDialog$4.onProgressUpdate
# Lifecycle edges for onCreateDialog of both dialogs already come from lc_chain in graph_def; none written here.

# --- ConfirmationDialog: empty-cards confirmation (DeckPicker.handleEmptyCards).
e('S_DLG_CONFIRMATION', 'ConfirmationDialog$1.onNegative', 'GUI',
  'tap Cancel in the empty-cards confirmation dialog',
  gui=['tap Cancel in the empty-cards confirmation dialog'],
  evidence='SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:46-49; SRC com/ichi2/anki/DeckPicker.java:2180-2195',
  note='MISSING GATE MG342: an empty card exists (the find-empty-cards task returns at least one card, DeckPicker.java:2182-2195). The MaterialDialog callback dispatch is not in the dataset: INFERRED. env and needs_state unset.')

e('S_DLG_CONFIRMATION', 'ConfirmationDialog$1.onPositive', 'GUI',
  'tap OK in the empty-cards confirmation dialog',
  gui=['tap OK in the empty-cards confirmation dialog'],
  evidence='SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-44; SRC com/ichi2/anki/DeckPicker.java:2180-2195',
  note='MISSING GATE MG342: same gate as the cancel edge (an empty card exists). The callback calls confirm() (ConfirmationDialog.java:43), overridden at DeckPicker.java:2186-2193. The MaterialDialog callback dispatch is INFERRED. env and needs_state unset.')

# --- CustomStudyDialog: custom study menu (deck long-press route) and number dialogs.
e('S_DLG_CUSTOM_STUDY', 'CustomStudyDialog$1.onSelection', 'GUI',
  'tap one row of the custom study context menu',
  env=None,
  needs_state=STATE_DECK,
  gui=['tap one row of the custom study context menu'],
  evidence='SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:119-122, 124-189; SRC com/ichi2/anki/dialogs/DeckPickerContextMenu.java:105-107, 132-137',
  note='The menu opens from the deck long-press only for a non-dynamic deck (DeckPickerContextMenu.java:105-107). The ListCallback dispatch is not in the dataset: INFERRED.')

e('S_DLG_TAGS', 'CustomStudyDialog$1$1.onPositive', 'GUI',
  'tap OK in the tag selection dialog opened from the custom study menu',
  env=None,
  needs_state=STATE_DECK,
  gui=['tap OK in the tag selection dialog opened from the custom study menu'],
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:162-167; SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:139-151, 175-179',
  note='The TagsDialog positive callback calls mTagsDialogListener.onPositive (TagsDialog.java:165-166). The tags item is the CUSTOM_STUDY_TAGS case (CustomStudyDialog.java:139). The dialog opens only through the custom study menu. The button dispatch is INFERRED.')

e('S_DLG_CUSTOM_STUDY', 'CustomStudyDialog$2.onPositive', 'GUI',
  'tap OK in the custom study number dialog (a number is typed)',
  env=None,
  needs_state=STATE_DECK,
  gui=['tap OK in the custom study number dialog (a number is typed)'],
  evidence='SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:226-231, 233-282, 291-301',
  note='The OK button is enabled only when the number field is not empty (CustomStudyDialog.java:291-301). The dialog opens from the custom study menu default branch (CustomStudyDialog.java:182-187). The button dispatch is INFERRED.')

e('S_DLG_CUSTOM_STUDY', 'CustomStudyDialog$2.onNegative', 'GUI',
  'tap Cancel in the custom study number dialog',
  env=None,
  needs_state=STATE_DECK,
  gui=['tap Cancel in the custom study number dialog'],
  evidence='SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:286-288',
  note='The negative callback dismisses all dialog fragments (CustomStudyDialog.java:287). The button dispatch is INFERRED.')

e('S_DLG_CUSTOM_STUDY', 'CustomStudyDialog$3.onKey', 'FRAMEWORK',
  'type or delete text in the custom study number field (the key event reaches the attached listener)',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:291-301; FW-SRC core/java/android/view/View.java:11705-11709',
  note='The OnKeyListener is set on the number field (CustomStudyDialog.java:291). View.dispatchKeyEvent calls the attached listener first (View.java:11707-11709). The key events reach the view through the window: INFERRED (not read).')

e('CustomStudyDialog.createCustomStudySession', 'CustomStudyDialog$4.onPreExecute', 'FRAMEWORK',
  'the rebuild task starts (DeckTask.launchDeckTask executes it); AsyncTask calls onPreExecute on the UI thread',
  evidence='SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:454, 460-462; SRC com/ichi2/async/DeckTask.java:129-134; FW-SRC core/java/android/os/AsyncTask.java:648',
  note='MISSING GATE MG343: the launch is reached only when the custom study deck name is free or names a dynamic deck (CustomStudyDialog.java:423-431). env and needs_state unset. The DeckTask delegation to the listener onPreExecute is automatic (DeckTask.java:344-347).')

e('CustomStudyDialog.createCustomStudySession', 'CustomStudyDialog$4.onPostExecute', 'ASYNC',
  'the rebuild task finishes in the background and the result is posted to the UI thread',
  evidence='SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:454, 465-468; SRC com/ichi2/async/DeckTask.java:359-365; FW-SRC core/java/android/os/AsyncTask.java:691-698',
  note='MISSING GATE MG343: same launch gate as the onPreExecute edge. finish calls onPostExecute when the task is not cancelled (AsyncTask.java:695). The DeckTask delegation at DeckTask.java:359-365 is automatic. env and needs_state unset.')

# --- UNREACHABLE: the REBUILD_CRAM listener methods onCancelled and onProgressUpdate.
UNREACHABLE['CustomStudyDialog$4.onCancelled'] = (
    'no_trigger_in_app',
    "no_trigger_in_app: the REBUILD_CRAM task is never cancelled, so DeckTask.onCancelled (DeckTask.java:367-370) never runs for it. "
    "In-app cancels go through DeckTask.cancelTask(int) (DeckTask.java:181-186), which cancels only when the latest task type equals the argument. "
    "Its callers pass TASK_TYPE_SEARCH_CARDS or TASK_TYPE_RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155), and none passes REBUILD_CRAM. "
    "The no-argument cancelTask (DeckTask.java:168-178) is called only from cancelTask(int) (line 184). "
    "The other cancel(true) calls act on non-DeckTask tasks (TaskOperations.java:33, Connection.java:541, Statistics.java:543, 574, 681, 692). "
    "A grep for 'extends DeckTask' finds no subclass. "
    "The automatic CALL DeckTask.onCancelled -> CustomStudyDialog$4.onCancelled (DeckTask.java:369) must be suppressed.",
    "SRC com/ichi2/async/DeckTask.java:168-186, 367-370; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; "
    "SRC com/ichi2/anki/runtimetools/TaskOperations.java:33; SRC com/ichi2/async/Connection.java:541; "
    "SRC com/ichi2/anki/Statistics.java:543, 574, 681, 692",
    'SOURCE')

UNREACHABLE['CustomStudyDialog$4.onProgressUpdate'] = (
    'no_trigger_in_app',
    "no_trigger_in_app: the REBUILD_CRAM body never publishes progress. doInBackgroundRebuildCram (DeckTask.java:728-733) calls the scheduler rebuild "
    "and doInBackgroundUpdateValuesFromDeck only, and no publishProgress call lies in that range. "
    "The only new ProgressCallback in the source root is at DeckTask.java:750 (the import body). "
    "So the DeckTask.onProgressUpdate delegation (DeckTask.java:351-355) never runs for this listener. "
    "The automatic CALL DeckTask$TaskListener.onProgressUpdate -> CustomStudyDialog$4.onProgressUpdate must be suppressed.",
    "SRC com/ichi2/async/DeckTask.java:351-355, 728-733, 750; "
    "SRC com/ichi2/async/DeckTask.java:380, 420, 422, 457, 565, 601, 633, 659, 809, 859",
    'SOURCE')
