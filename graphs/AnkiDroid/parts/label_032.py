e('S_DLG_CONFIRMATION', 'ModelBrowser$7.confirm', 'GUI',
  'press OK on the first delete note type confirmation (the default path on a fresh collection)',
  env=None,
  gui=['press OK on the delete note type confirmation dialog'],
  evidence='SRC com/ichi2/anki/ModelBrowser.java:448-466, 451-460; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-44; SRC com/ichi2/libanki/Collection.java:364-382; SRC com/ichi2/libanki/Storage.java:317-319',
  note='No gate written: the first dialog is shown when mModelIds.size() > 1 (ModelBrowser.java:448) and col.modSchema() does not throw, which holds while the schema flag is set (a fresh collection has scm > ls = 0). The positive button reaches ConfirmationDialog.onPositive -> confirm() (ConfirmationDialog.java:42-44); the MaterialDialog dispatch is INFERRED (library not in the dataset). The show call (ModelBrowser.java:466) is in deleteModelDialog, outside this batch.')

e('S_DLG_CONFIRMATION', 'ModelBrowser$7.cancel', 'GUI',
  'press Cancel on the first delete note type confirmation',
  env=None,
  gui=['press Cancel on the delete note type confirmation dialog'],
  evidence='SRC com/ichi2/anki/ModelBrowser.java:461-463; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:46-49',
  note='No gate written (same first-dialog path as the confirm edge). The negative button reaches ConfirmationDialog.onNegative -> cancel() (ConfirmationDialog.java:46-49); the MaterialDialog dispatch is INFERRED.')

e('S_DLG_CONFIRMATION', 'ModelBrowser$8.confirm', 'GUI',
  'press OK on the second delete note type confirmation (shown after a sync)',
  env=None,
  gui=['press OK on the full sync confirmation dialog for deleting a note type'],
  evidence='SRC com/ichi2/anki/ModelBrowser.java:467-484; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-44; SRC com/ichi2/libanki/Collection.java:364-382; SRC com/ichi2/libanki/sync/Syncer.java:423-428',
  note='MISSING GATE MG262: the catch branch runs only when col.modSchema() throws, which needs schemaChanged() false (scm <= ls), that is a completed sync since the last schema change. No predefined ENV or STATE kind covers this flag, so env and needs_state are unset. The dialog text is R.string.full_sync_confirmation (ModelBrowser.java:483).')

e('S_DLG_CONFIRMATION', 'ModelBrowser$8.cancel', 'GUI',
  'press Cancel on the second delete note type confirmation (shown after a sync)',
  env=None,
  gui=['press Cancel on the full sync confirmation dialog for deleting a note type'],
  evidence='SRC com/ichi2/anki/ModelBrowser.java:467-484; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:46-49',
  note='MISSING GATE MG262 (same condition as the confirm edge). env and needs_state are unset. The negative button reaches ConfirmationDialog.onNegative -> cancel() (ConfirmationDialog.java:46-49); the MaterialDialog dispatch is INFERRED.')

e('S_MODELBROWSER', 'ModelBrowser$DisplayPairAdapter.getView', 'FRAMEWORK',
  'the note type list draws each visible row through its adapter',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:268-269, 657-673; FW-SRC core/java/android/widget/ListView.java:775-786, 841-847, 1624, 1798, 2037-2052; FW-SRC core/java/android/widget/AbsListView.java:2335-2348, 2365',
  note='No gate: the adapter is set in fillModelList (ModelBrowser.java:268-269) and the list is laid out after that. Route: ListView.layoutChildren (1624) calls fillFromTop (1798) -> fillDown (775, makeAndAddView at 786) -> makeAndAddView (2037, obtainView at 2052) -> AbsListView.obtainView (2335, mAdapter.getView at 2348 and 2365). The framework steps are in fw_src.')

UNREACHABLE['ModelBrowser$DisplayPair.toString'] = ('framework_never_calls', "No app code calls DisplayPair.toString. DisplayPair is referenced only in ModelBrowser.java (grep over src/main/java). No line calls toString() on a DisplayPair (ModelBrowser.java:381, 424, 512 call toString on an EditText and on JSONObjects). DisplayPairAdapter.getView (ModelBrowser.java:657-673) overrides ArrayAdapter.getView and does not call super.getView, so the ArrayAdapter path that calls item.toString() (ArrayAdapter.java:445, inside createViewFromResource, reached from getView at 405-407) is never taken for this adapter. The adapter is set only on the list (ModelBrowser.java:268-269), so the spinner path getDropDownView (ArrayAdapter.java:490-493) is not reached. The filter path (ArrayFilter.performFiltering, value.toString() at ArrayAdapter.java:581) needs getFilter() and a text filter, and neither is set (no setTextFilterEnabled in ModelBrowser.java; no textFilterEnabled in res/layout/model_browser.xml). So no framework path calls toString on a DisplayPair.", "SRC com/ichi2/anki/ModelBrowser.java:268-269, 381, 424, 512, 641-644, 651-674; SRC res/layout/model_browser.xml; FW-SRC core/java/android/widget/ArrayAdapter.java:405-408, 445, 490-493, 550-581", 'SOURCE')
