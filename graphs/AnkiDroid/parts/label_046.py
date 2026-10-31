# AnkiDroid batch 046 (LABEL helper). TagsDialog: 36 methods. The full row list is in graphs/AnkiDroid/parts/label_046.md.
#
# Route ownership:
# - The DialogFragment lifecycle edges from TagsDialog.<init> to onCreate and onCreateDialog are in graph_def.py (lines 278-279). Not written here.
# - The callers of newInstance, setTagsDialogListener and the showTagsDialog methods are in other batches. Their automatic CALL edges
#   into this batch (the <init> methods, adjustToolbar, addTag, sortData, getFilter) come from auto_calls.json. Not written here.
# - The listener dispatch to CardBrowser$12, NoteEditor$10 and CustomStudyDialog$1$1 is the existing S_DLG_TAGS page edges and the
#   automatic CHA CALL edge from TagsDialog$2.onPositive. Not written here.
# - Page node: S_DLG_TAGS (graph_def.py line 102). A page edge belongs to the part that contains its destination, so the page edges
#   into this batch are written here.
#
# Gates (MG402-MG406): MG402 at least one tag is listed; MG403 the dialog type is TYPE_ADD_TAG; MG404 the dialog type is not
# TYPE_ADD_TAG; MG405 at least two tags are listed; MG406 the add item opens the input dialog (search view not expanded with a
# non-empty query). None of the predefined ENV or STATE constants fits, so env and needs_state are unset.

# --- Page edges from S_DLG_TAGS (the dialog is entered by CardBrowser.showTagsDialog, NoteEditor.showTagsDialog or CustomStudyDialog).

e('S_DLG_TAGS', 'TagsDialog$2.onPositive', 'GUI',
  'tap the positive button of the tags dialog (OK or Select)',
  env=None,
  gui=['tap the positive button of the tags dialog (OK or Select)'],
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:158-168',
  note='The button callback is the MaterialDialog ButtonCallback (TagsDialog.java:162). The library dispatch from the button to onPositive is not in the dataset: INFERRED (source not read). The call to the listener at TagsDialog.java:165-166 is an automatic CHA CALL edge and is not repeated here.')

e('S_DLG_TAGS', 'TagsDialog$1.onCheckedChanged', 'GUI',
  'choose one of the three options (all cards, new cards, due cards) in the options radio group',
  env=None,
  gui=['choose one of the three options (all cards, new cards, due cards) in the options radio group'],
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:138-143, 146-148; res/layout/tags_dialog.xml:18-36',
  note='MISSING GATE MG404: the options group is hidden for TYPE_ADD_TAG (TagsDialog.java:148), so the radio options exist only for the filter and custom study types. The RadioGroup dispatch to the listener is android.widget code, not in fw_src: INFERRED (source not read).')

e('S_DLG_TAGS', 'TagsDialog$4.onMenuItemClick', 'GUI',
  'tap the add (+) item in the tags dialog toolbar',
  env=None,
  gui=['tap the add (+) item in the tags dialog toolbar'],
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:193-196, 268-274; res/menu/tags_dialog_menu.xml:12-16',
  note='MISSING GATE MG403: the add item is set invisible for every type other than TYPE_ADD_TAG (TagsDialog.java:272-273). The toolbar item click dispatch is support library code, not in the dataset: INFERRED (source not read).')

e('S_DLG_TAGS', 'TagsDialog$6.onMenuItemClick', 'GUI',
  'tap the select-all item in the tags dialog toolbar',
  env=None,
  gui=['tap the select-all item in the tags dialog toolbar'],
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:244-266; res/menu/tags_dialog_menu.xml:18-22',
  note='No gate: the select-all item is not hidden for any dialog type (TagsDialog.java:268-274 changes only the add item). The toolbar dispatch is support library code: INFERRED (source not read).')

e('S_DLG_TAGS', 'TagsDialog$5.onQueryTextChange', 'GUI',
  'type in the filter search field of the toolbar (the SearchView is expanded)',
  env=None,
  gui=['type in the filter search field of the toolbar (the SearchView is expanded)'],
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:229, 237-240; res/menu/tags_dialog_menu.xml:5-10',
  note='No gate. The SearchView text listener is set at TagsDialog.java:229. The SearchView dispatch is support library code, not in the dataset: INFERRED (source not read).')

e('S_DLG_TAGS', 'TagsDialog$5.onQueryTextSubmit', 'GUI',
  'submit the query in the filter search field (search key)',
  env=None,
  gui=['submit the query in the filter search field (search key)'],
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:229-234',
  note='No gate. The body clears the focus of the SearchView and returns true. The dispatch is support library code: INFERRED (source not read).')

e('S_DLG_TAGS', 'TagsDialog$3.filter', 'FRAMEWORK',
  'type a character into the filter search field (the InputFilter rejects a space)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:181-192, 226',
  note='No gate. The InputFilter is set on the search EditText at TagsDialog.java:226. The EditText dispatch to InputFilter.filter is android.text code, not in fw_src: INFERRED (source not read).')

e('S_DLG_TAGS', 'TagsDialog$TagsArrayAdapter$2.onClick', 'GUI',
  'tap a tag row to check or uncheck the tag',
  env=None,
  gui=['tap a tag row to check or uncheck the tag'],
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:340-353',
  note='MISSING GATE MG402: a row exists only when at least one tag is listed (TagsDialog.java:359-361, 366-367). The row click listener is set in onCreateViewHolder (TagsDialog.java:341). The View click dispatch is framework code whose source was not read: INFERRED.')

e('S_DLG_TAGS', 'TagsDialog$TagsArrayAdapter.onCreateViewHolder', 'FRAMEWORK',
  'the RecyclerView creates a row for a tag',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:124-125, 335-340',
  note='MISSING GATE MG402: no row is created while the tag list is empty. The RecyclerView dispatch is support library code, not in the dataset: INFERRED (source not read).')

e('S_DLG_TAGS', 'TagsDialog$TagsArrayAdapter.onBindViewHolder', 'FRAMEWORK',
  'the RecyclerView binds a tag name and its checked state to a row',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:124-125, 358-362',
  note='MISSING GATE MG402: no row is bound while the tag list is empty. The RecyclerView dispatch is support library code: INFERRED (source not read).')

e('S_DLG_TAGS', 'TagsDialog$TagsArrayAdapter.getItemCount', 'FRAMEWORK',
  'the RecyclerView asks how many rows the tag list has',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:124-125, 365-367',
  note='No gate: getItemCount is asked on every layout and returns 0 for an empty list. The RecyclerView dispatch is support library code: INFERRED (source not read).')

# --- Edges inside the dialog's own methods.

e('TagsDialog$4.onMenuItemClick', 'TagsDialog$4$1.onInput', 'FRAMEWORK',
  'confirm the add-tag input dialog with OK; the input dialog calls onInput with the typed text',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:197-216',
  note='MISSING GATE MG406: the input dialog opens only when the search view is not expanded with a non-empty query (TagsDialog.java:197-201). The add item is visible only for TYPE_ADD_TAG (MG403). The MaterialDialog InputCallback dispatch is library code, not in the dataset: INFERRED (source not read). The call to addTag at TagsDialog.java:210 is an automatic CALL edge.')

e('TagsDialog$4.onMenuItemClick', 'TagsDialog$3.filter', 'FRAMEWORK',
  'type a character into the add-tag input dialog (the InputFilter rejects a space)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:181-192, 215-216',
  note='MISSING GATE MG406: the input dialog opens only when the search view is not expanded with a non-empty query (TagsDialog.java:197-201), and the add item needs MG403. The EditText dispatch to InputFilter.filter is android.text code, not in fw_src: INFERRED (source not read).')

e('TagsDialog$5.onQueryTextChange', 'TagsDialog$TagsArrayAdapter$TagsFilter.performFiltering', 'ASYNC',
  'the search text changes: Filter.filter posts the constraint and performFiltering runs on the filter worker thread',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:237-240, 383; FW-SRC core/java/android/widget/Filter.java:101-126, 227-234',
  note='No gate: an empty constraint still runs performFiltering. The getFilter call at TagsDialog.java:238 is an automatic CALL edge. The posting and the RequestHandler path are in Filter.java (fw_src), read only at the lines cited.')

e('TagsDialog$TagsArrayAdapter$TagsFilter.performFiltering', 'TagsDialog$TagsArrayAdapter$TagsFilter.publishResults', 'ASYNC',
  'the filter results are posted back and publishResults runs on the UI thread',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:383-408; FW-SRC core/java/android/widget/Filter.java:239-241, 279-282',
  note='No gate. The result post is Filter.java:239-241, and ResultsHandler.handleMessage calls publishResults at Filter.java:282.')

e('TagsDialog$TagsArrayAdapter.sortData', 'TagsDialog$TagsArrayAdapter$1.compare', 'FRAMEWORK',
  'Collections.sort calls the Comparator to order the tag list (checked tags first)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:322-331',
  note='MISSING GATE MG405: the comparator runs only when the list has at least two tags. java.util.Collections.sort is not in the dataset: INFERRED (source not read).')
