# AnkiDroid batch 025 (LABEL helper). CardTemplateEditor part 1: 40 methods. The full row list is in
# graphs/AnkiDroid/parts/label_025.md.
#
# Route ownership:
# - Automatic CALL edges (graphs/AnkiDroid/auto_calls.json) are not written here. They cover the direct calls inside
#   CardTemplateEditor, $1, $3 and the fragment, the AnkiActivity virtual dispatches into showProgressBar,
#   hideProgressBar and onCollectionLoaded, and the DeckTask listener defaults into $1.
# - Edges into batch 026 methods (updateCss, the fragment $2 save listener, the fragment $3, $4 and $5 confirm methods,
#   TemplatePagerAdapter) are not written here.
# - Page edges (S_CARDTEMPLATEEDITOR, S_PREVIEWER) are written here only when the destination is in this batch.
# - Launch edges into $1 (ASYNC) are written from addNewTemplate and deleteTemplate, as label_031 does for ModelBrowser.
#
# Gates: MG192 (model changed), MG193 (two or more templates), MG194 (framework saves state), MG195 (one template at add),
# MG196 (no note card for the position), MG198 (schema not yet modified). MG197 and MG199 to MG201 are not used.
# No STATE or ENV constant fits these gates, so env and needs_state are unset.

# --- Activity: collection load, save state, Up arrow, pager listener, discard dialog.

e('CardTemplateEditor.onCreate', 'CardTemplateEditor.onCollectionLoaded', 'ASYNC',
  'the collection loader delivers onLoadFinished after startLoadingCollection',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:157, 205-206; SRC com/ichi2/anki/AnkiActivity.java:255-262, 283-290',
  note='Precedent label_009 (CardBrowser.onCreate -> onCollectionLoaded). The restart is in AnkiActivity.startLoadingCollection (AnkiActivity.java:261); the result reaches onCollectionLoaded through AnkiActivity.onLoadFinished (AnkiActivity.java:286, automatic CALL). The library delivery step is not in the tree.')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor.onSaveInstanceState', 'FRAMEWORK',
  'the framework saves the editor state when the activity is stopped and not finishing',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:161-168; FW-SRC core/java/android/app/ActivityThread.java:4020-4027',
  note='Page edge, destination in this part. MISSING GATE MG194: the not-finishing and saveState conditions are framework state with no STATE kind, so env and needs_state are unset. Precedent: DeckPicker.onPause -> onSaveInstanceState (label_003).')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor.onOptionsItemSelected', 'GUI',
  'tap the Up (home) arrow in the toolbar of the template editor',
  env=None,
  gui=['tap the Up (home) arrow in the toolbar of the template editor'],
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:171-184; FW-SRC core/java/android/app/Activity.java:3439-3450',
  note='Page edge, destination in this part. Activity.onMenuItemSelected calls onOptionsItemSelected (Activity.java:3450). The discard dialog branch needs MISSING GATE MG192 (the model was edited); otherwise the editor finishes.')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$2.onPageScrolled', 'FRAMEWORK',
  'the support-library ViewPager dispatches a scroll step to the page-change listener while the user swipes between templates',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:214, 216-217',
  note='Page edge, destination in this part. INFERRED: ViewPager dispatch, source not read. The body is empty. MISSING GATE MG193: a swipe needs two or more templates.')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$2.onPageScrollStateChanged', 'FRAMEWORK',
  'the support-library ViewPager dispatches a scroll-state change to the page-change listener while the user swipes',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:214, 228-229',
  note='Page edge, destination in this part. INFERRED: ViewPager dispatch, source not read. The body is empty. MISSING GATE MG193: a swipe needs two or more templates.')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$2.onPageSelected', 'FRAMEWORK',
  'the support-library ViewPager dispatches the selected page to the page-change listener',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:214, 220-225, 290',
  note='Page edge, destination in this part. INFERRED: ViewPager dispatch, source not read. Also reached from selectTemplate (setCurrentItem at CardTemplateEditor.java:290). The body calls instantiateItem and fragment.updateCss (automatic CALL, line 223).')

e('CardTemplateEditor$3.<init>', 'CardTemplateEditor$3.onPositive', 'FRAMEWORK',
  'the discard dialog calls onPositive when its positive button is tapped (MaterialDialog.ButtonCallback)',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:255-260, 262-268',
  note='Library dispatch (MaterialDialog, INFERRED, source not read). The dialog is shown after $3.<init> is constructed in showDiscardChangesDialog (automatic CALL, CardTemplateEditor.java:259). MISSING GATE MG192: the dialog needs an edited model. Precedent: DeckPicker$23.<init> -> onPositive (label_005).')

# --- Template task listener $1: launch edges from the add and delete methods of the fragment.

e('CardTemplateEditor$CardTemplateFragment.addNewTemplate', 'CardTemplateEditor$1.onPreExecute', 'ASYNC',
  'the ADD_TEMPLATE task starts and runs the pre-execute callback of the editor listener',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:718-719, 86-88; SRC com/ichi2/async/DeckTask.java:344-347, 1298-1300',
  note='Launch link, as in label_031 (ModelBrowser launch edges). DeckTask.onPreExecute calls mListener.onPreExecute(this) (DeckTask.java:346), which the TaskListener default (DeckTask.java:1298-1300) forwards to the no-argument onPreExecute that $1 overrides.')

e('CardTemplateEditor$CardTemplateFragment.addNewTemplate', 'CardTemplateEditor$1.onPostExecute', 'ASYNC',
  'the ADD_TEMPLATE task finishes and delivers its result to the editor listener',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:718-719, 95-113; SRC com/ichi2/async/DeckTask.java:360-365, 1304-1306',
  note='DeckTask.onPostExecute delegates to the listener (DeckTask.java:362); the success branch calls selectTemplate (automatic CALL, CardTemplateEditor.java:100).')

e('CardTemplateEditor$CardTemplateFragment.deleteTemplate', 'CardTemplateEditor$1.onPreExecute', 'ASYNC',
  'the REMOVE_TEMPLATE task starts and runs the pre-execute callback of the editor listener',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:664-665, 86-88; SRC com/ichi2/async/DeckTask.java:344-347, 1298-1300',
  note='Launch link, as in label_031 (ModelBrowser launch edges). DeckTask.onPreExecute calls mListener.onPreExecute(this) (DeckTask.java:346), which the TaskListener default (DeckTask.java:1298-1300) forwards to the no-argument onPreExecute that $1 overrides.')

e('CardTemplateEditor$CardTemplateFragment.deleteTemplate', 'CardTemplateEditor$1.onPostExecute', 'ASYNC',
  'the REMOVE_TEMPLATE task finishes and delivers its result to the editor listener',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:664-665, 95-113; SRC com/ichi2/async/DeckTask.java:360-365, 1304-1306',
  note='DeckTask.onPostExecute delegates to the listener (DeckTask.java:362); the success branch calls selectTemplate (automatic CALL, CardTemplateEditor.java:100). The "removeTemplateFailed" branch shows a toast (CardTemplateEditor.java:104-107).')

# --- Fragment: preview result, menu, add and delete routes.

e('S_PREVIEWER', 'CardTemplateEditor$CardTemplateFragment.onActivityResult', 'RESULT',
  'the preview returns to the template editor, which hands the result to the fragment',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:503-504, 557-560',
  note='Page edge, destination in this part. Launched by startActivityForResult(i, REQUEST_PREVIEWER) (CardTemplateEditor.java:504). The hand-off to the fragment is support-library FragmentActivity dispatch (INFERRED, source not read). Precedent: S_CARDTEMPLATEEDITOR -> NoteEditor.onActivityResult (label_012).')

e('CardTemplateEditor$CardTemplateFragment.onOptionsItemSelected', 'Previewer.<init>', 'INTENT',
  'open the previewer for the template being edited (explicit Intent to Previewer, card id extra)',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:485, 488-491, 503-504',
  note='Explicit component (Previewer.class) started for a result. The card is the note card when noteId is set and the position exists; otherwise the dummy card path (MISSING GATE MG196). The source is in this part, so the edge is written here; label_036 has no edge into Previewer.<init>.')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$CardTemplateFragment.onOptionsItemSelected', 'GUI',
  'tap an action in the template editor toolbar menu (add, delete, preview, done)',
  env=None,
  gui=['tap an action in the template editor toolbar menu (add, delete, preview, done)'],
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:442-446, 449-521',
  note='Page edge, destination in this part. The fragment inflates the menu (CardTemplateEditor.java:444). The dispatch from the activity menu to the fragment is support-library code (INFERRED, source not read).')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$CardTemplateFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'the options menu is built and the fragment inflates its menu',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:420, 442-446',
  note='Page edge, destination in this part. INFERRED: support-library FragmentActivity dispatches onCreateOptionsMenu to fragments that called setHasOptionsMenu(true) (CardTemplateEditor.java:420). Source not read.')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$CardTemplateFragment.onCreateView', 'FRAMEWORK',
  'the pager creates each template page and the fragment inflates its view',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:213, 318-320, 380-425',
  note='Page edge, destination in this part. INFERRED: support-library ViewPager and FragmentPagerAdapter create the page after setAdapter (CardTemplateEditor.java:213) through TemplatePagerAdapter.getItem (batch 026 edge). Source not read.')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$CardTemplateFragment.onResume', 'FRAMEWORK',
  'the editor resumes and the attached fragment receives onResume',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:427-430',
  note='Page edge, destination in this part. INFERRED: support-library dispatch of onResume to attached fragments (source not read). The body calls super only.')

# --- UNREACHABLE entries (text inline; no module-level names).

UNREACHABLE['CardTemplateEditor$1.onCancelled'] = (
    'no_trigger_in_app',
    ("DeckTask.onCancelled calls the listener onCancelled (DeckTask.java:367-370) only after a DeckTask is cancelled. "
     "The ADD_TEMPLATE and REMOVE_TEMPLATE tasks (TASK_TYPE_ADD_TEMPLATE = 39, TASK_TYPE_REMOVE_TEMPLATE = 40, DeckTask.java:92-93) "
     "are never cancelled in the app. DeckTask.cancelTask(int) (DeckTask.java:181-186) cancels the latest task only when its type "
     "equals the argument, and its only callers pass TASK_TYPE_SEARCH_CARDS and TASK_TYPE_RENDER_BROWSER_QA "
     "(CardBrowser.java:528-529, 796-797, 1155). The no-argument DeckTask.cancelTask (DeckTask.java:168-178) has no caller except "
     "cancelTask(int) (DeckTask.java:184). The other cancel(true) calls act on other tasks: TaskOperations.stopTaskGracefully "
     "(TaskOperations.java:33; its callers pass pronunciation and translation tasks), Connection.java:541, Statistics.java:543, 574, "
     "681, 692. So no template task is cancelled and onCancelled never runs. Suppress candidate: the automatic CALL "
     "DeckTask.onCancelled -> CardTemplateEditor$1.onCancelled (DeckTask.java:369, cha) would reach this method."),
    ('SRC com/ichi2/async/DeckTask.java:92-93, 168-186, 367-370, 1028-1065; '
     'SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; '
     'SRC com/ichi2/anki/runtimetools/TaskOperations.java:30-33; '
     'SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:474-478; '
     'SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:405; '
     'SRC com/ichi2/async/Connection.java:541; '
     'SRC com/ichi2/anki/Statistics.java:543, 574, 681, 692; SRC com/ichi2/anki/CardTemplateEditor.java:84, 116-118'),
    'SOURCE')

UNREACHABLE['CardTemplateEditor$1.onProgressUpdate'] = (
    'no_trigger_in_app',
    ("DeckTask.onProgressUpdate (DeckTask.java:352-355) runs only when a DeckTask calls publishProgress. The ADD_TEMPLATE and "
     "REMOVE_TEMPLATE bodies (DeckTask.java:1028-1065) never call it. The publishProgress calls (DeckTask.java:380, 420, 422, "
     "457, 565, 601, 633, 659, 809, 859) are inside other task bodies. The only ProgressCallback is built for the import task "
     "(DeckTask.java:750) and its class is at DeckTask.java:1320-1325. So the template listener never receives progress. "
     "Suppress candidate: the automatic CALL DeckTask$TaskListener.onProgressUpdate -> CardTemplateEditor$1.onProgressUpdate "
     "(DeckTask.java:1312, cha), and its specialized copy DeckTask$TaskListener.onProgressUpdate@CardTemplateEditor$1, would reach this method."),
    ('SRC com/ichi2/async/DeckTask.java:352-355, 380, 420, 422, 457, 565, 601, 633, 659, 750, 809, 859, 1028-1065, 1312, 1320-1325; '
     'SRC com/ichi2/anki/CardTemplateEditor.java:91-92'),
    'SOURCE')
