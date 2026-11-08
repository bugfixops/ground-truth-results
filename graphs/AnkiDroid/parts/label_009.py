# AnkiDroid batch 009 (LABEL helper). CardBrowser part 1: 40 methods, all REACHABLE, so there are no UNREACHABLE entries.
# The rows and reasons are in graphs/AnkiDroid/parts/label_009.md.
#
# Route notes:
# - The entry S_DECKPICKER -> CardBrowser.<clinit> (INTENT) skips the DeckPicker.openCardBrowser node (batch 003).
# - DeckDropDownAdapter.getView belongs to another batch. The edge into it is written here because its source is in batch 009.
# - No env or needs_state gate is set. The card browser is opened from the deck picker with the collection loaded.
# - The closeCardBrowser(int) route (RESULT_DB_ERROR) always throws NullPointerException (bug finding; no MG number assigned).

e('S_DECKPICKER', 'CardBrowser.<clinit>', 'INTENT',
  'open the card browser from the deck picker',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1708-1713; FW-SRC core/java/android/app/Instrumentation.java:1170-1174',
  note='Entry edge into batch 009. It skips the DeckPicker.openCardBrowser node (batch 003), which has no INTENT edge into CardBrowser in its part.')

e('CardBrowser.<clinit>', 'CardBrowser.<init>', 'FRAMEWORK',
  'newInstance constructs the instance after the class is initialized',
  env=None,
  evidence='FW-SRC core/java/android/app/Instrumentation.java:1170-1174; SRC com/ichi2/anki/CardBrowser.java:121, 134-135',
  note='Java class initialization runs before the first constructor call (not cited).')

e('S_CARDBROWSER', 'CardBrowser.onOptionsItemSelected', 'GUI',
  'tap a menu item in the card browser action bar',
  gui=['tap a menu item in the card browser action bar'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:624-628',
  note='Page edge. lc_chain skips onOptionsItemSelected (graph_def.py LC_NO_TRIGGER), so this edge is the route in.')

e('CardBrowser.onCreate', 'CardBrowser.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu after onCreate (onCreatePanelMenu calls onCreateOptionsMenu)',
  env=None,
  evidence='FW-SRC core/java/android/app/Activity.java:3386-3388; SRC com/ichi2/anki/CardBrowser.java:572-573',
  note='Follows the label_002.py precedent (DeckPicker.onCreate -> onCreateOptionsMenu). The timing of the panel build is not modelled.')

e('CardBrowser.onCreate', 'CardBrowser.onCollectionLoaded', 'ASYNC',
  'the collection loader delivers onLoadFinished after startLoadingCollection',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:348; SRC com/ichi2/anki/AnkiActivity.java:255-262, 282-290',
  note='The loader is restarted in AnkiActivity.startLoadingCollection (261) and the result reaches onCollectionLoaded through AnkiActivity.onLoadFinished (286). The library delivery step is not in the tree.')

e('CardBrowser.onCollectionLoaded', 'DeckDropDownAdapter.getView', 'FRAMEWORK',
  'the spinner draws its rows with the adapter set in onCollectionLoaded',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:367, 373; SRC com/ichi2/anki/widgets/DeckDropDownAdapter.java:90',
  note='Cross-batch: DeckDropDownAdapter.getView belongs to another batch. The getView -> getSubtitleText edge is automatic (CHA, DeckDropDownAdapter.java:90).')

e('S_CARDBROWSER', 'CardBrowser.onBackPressed', 'GUI',
  'press the back key with the navigation drawer closed',
  gui=['press the back key with the navigation drawer closed'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:548-561; FW-SRC core/java/android/app/Activity.java:3001',
  note='Page edge. The framework calls onBackPressed on the back key (not cited).')

e('S_CARDBROWSER', 'CardBrowser$10.onQueryTextChange', 'GUI',
  'type in the search view',
  gui=['type in the search view'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:597-602',
  note='Page edge. The SearchView dispatch is library behaviour (not cited).')

e('CardBrowser.onOptionsItemSelected', 'S_NOTEEDITOR', 'ENTERS',
  'the add-card menu item starts the note editor (ADD_NOTE)',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:630-634',
  note='ENTERS edge: method to page. The result returns through the RESULT edge S_NOTEEDITOR -> CardBrowser.onActivityResult.')

e('S_CARDBROWSER', 'CardBrowser$10.onQueryTextSubmit', 'GUI',
  'submit a query in the search view',
  gui=['submit a query in the search view'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:605-610',
  note='Page edge. The SearchView dispatch is library behaviour (not cited).')

e('S_CARDBROWSER', 'CardBrowser$11.onClick', 'GUI',
  'tap the search view (search click)',
  gui=['tap the search view (search click)'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:612-617',
  note='Page edge. The View click dispatch is library behaviour (not cited).')

e('S_DLG_CARDBROWSER_CONTEXT', 'CardBrowser$1.onSelection', 'GUI',
  'tap an item in the card context menu',
  gui=['tap an item in the card context menu'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:159-161; SRC com/ichi2/anki/dialogs/CardBrowserContextMenu.java:58-62',
  note='Page edge. The MaterialDialog list dispatch is library behaviour (not cited).')

e('S_NOTEEDITOR', 'CardBrowser.onActivityResult', 'RESULT',
  'the note editor returns to the card browser (ADD_NOTE or EDIT_CARD result, or RESULT_DB_ERROR)',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:686-693; SRC com/ichi2/anki/NoteEditor.java:271, 1021-1022',
  note='RESULT edge: page to method. The framework delivers the result (not cited). The RESULT_DB_ERROR branch leads to the closeCardBrowser NullPointerException (bug finding).')

e('S_DLG_CARDBROWSER_CONTEXT', 'CardBrowser$1$1.onClick', 'GUI',
  'tap DELETE in the context menu, then OK in the delete confirmation',
  gui=['tap DELETE in the context menu, then OK in the delete confirmation'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:185-197',
  note='Page edge. The delete confirmation is built in CardBrowser$1.onSelection (187-203). The MaterialDialog button dispatch is library behaviour (not cited).')

e('S_DLG_TAGS', 'CardBrowser$12.onPositive', 'GUI',
  'pick tags in the tag dialog and confirm',
  gui=['pick tags in the tag dialog and confirm'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:732-734; SRC com/ichi2/anki/dialogs/TagsDialog.java:162-167',
  note='Page edge. Also an automatic CHA CALL edge from TagsDialog$2.onPositive (TagsDialog.java:166).')

e('CardBrowser.onCreate', 'S_CARDBROWSER', 'ENTERS',
  'the card browser screen is shown after onCreate sets the content view',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:343-349',
  note='ENTERS edge: method to page.')

e('CardBrowser.showTagsDialog', 'S_DLG_TAGS', 'ENTERS',
  'showTagsDialog shows the TagsDialog fragment',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:729-731, 768',
  note='ENTERS edge: method to page.')

e('CardBrowser.onOptionsItemSelected', 'S_DLG_CARDBROWSER_SEARCHES', 'ENTERS',
  'the save-search and list-my-searches items show CardBrowserMySearchesDialog',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:636-640, 642-654',
  note='ENTERS edge: method to page.')

e('CardBrowser.onOptionsItemSelected', 'S_DLG_CARDBROWSER_ORDER', 'ENTERS',
  'the sort item shows CardBrowserOrderDialog',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:655-658',
  note='ENTERS edge: method to page.')

e('CardBrowser.closeCardBrowser(int,Intent)', 'CardBrowser.onDestroy', 'FRAMEWORK',
  'finishWithAnimation leads the framework to destroy the activity',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:1124-1134; SRC com/ichi2/anki/AnkiActivity.java:206-209; FW-SRC core/java/android/app/Activity.java:5526-5528, 7204-7208',
  note='Follows the label_002.py precedent (finishWithAnimation -> onDestroy). Only the non-null Intent route (back key) reaches it; the closeCardBrowser(int) route throws first (bug finding).')
