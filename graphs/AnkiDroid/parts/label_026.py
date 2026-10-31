# AnkiDroid batch 026 (LABEL helper). CardTemplateEditor part 2 of 2: 24 methods. The full row list is in
# graphs/AnkiDroid/parts/label_026.md.
# Edges here: source in batch 026, or page S_CARDTEMPLATEEDITOR with destination in batch 026.
# Not written here (other parts or the builder): OnPageChangeListener.onPageSelected -> updateCss, the DeckTask launch
# edges, the ConfirmationDialog positive dispatch into the confirm() methods, and the automatic CALL edges.
# Gates: no MG id is used. The catch routes of $4 and $5 use the predefined ENV_NETWORK and STATE_ACCOUNT (rows only).

# --- Text watcher $1 (registered on mFront, mCss and mBack in CardTemplateFragment.onCreateView, lines 416-418).
e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$CardTemplateFragment$1.afterTextChanged', 'GUI',
  'type in the front, back or styling text box of a card template',
  env=None,
  gui=['type in the front, back or styling text box of a card template'],
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:398-418; FW-SRC core/java/android/widget/TextView.java:9375-9382, 11935-11939',
  note='Typing reaches the watcher through ChangeWatcher.afterTextChanged (TextView.java:11939) and sendAfterTextChanged (TextView.java:9375-9382). No gate: the editor is open on a note type.')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$CardTemplateFragment$1.beforeTextChanged', 'GUI',
  'type in the front, back or styling text box of a card template',
  env=None,
  gui=['type in the front, back or styling text box of a card template'],
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:398-418; FW-SRC core/java/android/widget/TextView.java:11918, 9309-9316',
  note='Typing reaches the watcher through ChangeWatcher.beforeTextChanged (TextView.java:11918) and sendBeforeTextChanged (TextView.java:9309-9316). The body is empty (CardTemplateEditor.java:412). No gate.')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$CardTemplateFragment$1.onTextChanged', 'GUI',
  'type in the front, back or styling text box of a card template',
  env=None,
  gui=['type in the front, back or styling text box of a card template'],
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:398-418; FW-SRC core/java/android/widget/TextView.java:11921-11926, 9359-9366, 9432-9452',
  note='Typing reaches the watcher through ChangeWatcher.onTextChanged (TextView.java:11926), then handleTextChanged, which calls sendOnTextChanged (TextView.java:9451). The body is empty (CardTemplateEditor.java:414). No gate.')

# --- The same watcher reached from updateCss: setText on the styling box (CardTemplateEditor.java:435) runs the watchers.
e('CardTemplateEditor$CardTemplateFragment.updateCss', 'CardTemplateEditor$CardTemplateFragment$1.afterTextChanged', 'FRAMEWORK',
  'setText of the styling box runs the after-change watcher',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:432-438; FW-SRC core/java/android/widget/TextView.java:5300-5304, 5402-5403, 9375-9382',
  note='updateCss sets the styling box text (CardTemplateEditor.java:435). TextView.setText calls sendAfterTextChanged when the box has listeners (TextView.java:5300-5304, 5402-5403). The watcher is the one registered on mCss (CardTemplateEditor.java:417). Framework dispatch, not an app CALL.')

e('CardTemplateEditor$CardTemplateFragment.updateCss', 'CardTemplateEditor$CardTemplateFragment$1.beforeTextChanged', 'FRAMEWORK',
  'setText of the styling box runs the before-change watcher',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:432-438; FW-SRC core/java/android/widget/TextView.java:5291-5296, 9309-9316',
  note='The same setText call (CardTemplateEditor.java:435) runs sendBeforeTextChanged when notifyBefore is set (TextView.java:5291-5296). The body is empty.')

e('CardTemplateEditor$CardTemplateFragment.updateCss', 'CardTemplateEditor$CardTemplateFragment$1.onTextChanged', 'FRAMEWORK',
  'setText of the styling box runs the on-change watcher',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:432-438; FW-SRC core/java/android/widget/TextView.java:5397, 9359-9366',
  note='The same setText call runs sendOnTextChanged (TextView.java:5397). The body is empty (CardTemplateEditor.java:414).')

# --- Pager adapter entries from the page (ViewPager populates the adapter after setAdapter, CardTemplateEditor.java:213).
# Support library, not in fw_src: INFERRED.
e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$TemplatePagerAdapter.getItem', 'FRAMEWORK',
  'the card template pager creates a page after setAdapter',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:213, 318-320',
  note='INFERRED: the support-library ViewPager and FragmentPagerAdapter call getItem when they create a page after setAdapter (CardTemplateEditor.java:213). getItem returns CardTemplateFragment.newInstance(position, mModelId, mNoteId). No gate.')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$TemplatePagerAdapter.getItemId', 'FRAMEWORK',
  'the card template pager creates a page after setAdapter',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:213, 322-326',
  note='INFERRED: the support-library FragmentPagerAdapter asks for the item id when it builds the fragment tag for a page. The id is baseId plus the position (CardTemplateEditor.java:325). No gate.')

# --- UNREACHABLE entries (no_trigger_in_app). Full argument: see the rows of graphs/AnkiDroid/parts/label_026.md.
UNREACHABLE['CardTemplateEditor$CardTemplateFragment$2.onCancelled'] = (
    'no_trigger_in_app',
    ("DeckTask.onCancelled calls the listener onCancelled (DeckTask.java:367-370) only after the task is cancelled. "
     "The SAVE_MODEL task (TASK_TYPE_SAVE_MODEL = 47, DeckTask.java:100) is never cancelled in the app. "
     "DeckTask.cancelTask(int) (DeckTask.java:181-186) cancels the latest task only when its type equals the argument, "
     "and its only callers pass TASK_TYPE_SEARCH_CARDS and TASK_TYPE_RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155). "
     "The no-argument DeckTask.cancelTask (DeckTask.java:168-178) has no caller except cancelTask(int) (DeckTask.java:184). "
     "The other cancel(true) calls act on other tasks: TaskOperations.stopTaskGracefully (TaskOperations.java:33; its callers "
     "LoadPronounciationActivity.java:474-478 and TranslationActivity.java:405 pass their own tasks), Connection.java:541, "
     "Statistics.java:543, 574, 681, 692. DeckTask.getInstance (DeckTask.java:1548-1549) returns the latest task, and its only caller "
     "(Finder.java:1040) reads isCancelled() and never cancels. So no SAVE_MODEL task is cancelled and onCancelled never runs."),
    ('SRC com/ichi2/async/DeckTask.java:100, 168-186, 367-370; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; '
     'SRC com/ichi2/anki/runtimetools/TaskOperations.java:30-36; SRC com/ichi2/async/Connection.java:541; '
     'SRC com/ichi2/anki/Statistics.java:543, 574, 681, 692; '
     'SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:474-478; '
     'SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:405; SRC com/ichi2/libanki/Finder.java:1040; '
     'SRC com/ichi2/async/DeckTask.java:1548-1549'),
    'SOURCE')

UNREACHABLE['CardTemplateEditor$CardTemplateFragment$2.onProgressUpdate'] = (
    'no_trigger_in_app',
    ("DeckTask.onProgressUpdate (DeckTask.java:352-355) runs only when a DeckTask calls publishProgress. "
     "The publishProgress calls in DeckTask.java are at lines 380, 420, 422, 457, 565, 601, 633, 659, 809, 859 and 1349 "
     "(1349 forwards from ProgressCallback, which exists only from line 750). "
     "None is inside doInBackgroundSaveModel (DeckTask.java:1070-1079), and the ProgressCallback (DeckTask.java:1320-1350) "
     "is built only in doInBackgroundImportAdd (DeckTask.java:750). So a SAVE_MODEL task never publishes progress, "
     "and the listener onProgressUpdate (CardTemplateEditor.java:572-573) never runs."),
    ('SRC com/ichi2/async/DeckTask.java:330-331, 352-355, 750, 1070-1079, 1310-1313, 1320-1350 '
     '(publishProgress at lines 380, 420, 422, 457, 565, 601, 633, 659, 809, 859, 1349); '
     'SRC com/ichi2/anki/CardTemplateEditor.java:572-573'),
    'SOURCE')
