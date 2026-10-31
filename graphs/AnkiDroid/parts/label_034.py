# AnkiDroid batch 034 (LABEL helper). ModelFieldEditor part 2: 16 methods. Row list: graphs/AnkiDroid/parts/label_034.md.
# Gate used: MISSING GATE MG282 (schema-changed flag; env and needs_state unset). No predefined ENV or STATE kind fits.
# Edges owned: GUI from the S_DLG_CONFIRMATION and S_DLG_MODELEDITOR_CONTEXT pages (owned by the destination),
# the FRAMEWORK edge from $6.<init> to $6.onPositive, and the ASYNC launch edges into the $8 listener from the launch methods.
# UNREACHABLE: ModelFieldEditor$8.onCancelled and ModelFieldEditor$8.onProgressUpdate.

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$5$1.confirm', 'GUI',
  'press OK on the rename field confirmation shown when the schema change needs confirmation',
  gui=['press OK on the rename field confirmation shown when the schema change needs confirmation'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:312-334; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-49; SRC com/ichi2/libanki/Collection.java:364-382; SRC com/ichi2/libanki/Models.java:665-666; SRC com/ichi2/libanki/Storage.java:317-319',
  note='MISSING GATE MG282: the dialog appears only when renameField() throws ConfirmModSchemaException, which needs Collection.schemaChanged() false (mScm <= mLs, Collection.java:380-382) when Models.renameField calls modSchema(true) (Models.java:665-666). A fresh collection (Storage.java:317-319: scm set, ls 0) does not throw. env and needs_state unset. The MaterialDialog OK dispatch to ConfirmationDialog is library code: INFERRED.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$6$1.confirm', 'GUI',
  'press OK on the reposition confirmation shown when the schema change needs confirmation',
  gui=['press OK on the reposition confirmation shown when the schema change needs confirmation'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:375-395; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-49; SRC com/ichi2/libanki/Collection.java:364-382',
  note='MISSING GATE MG282: the dialog is created only when modSchema() throws in $6.onPositive (ModelFieldEditor.java:375, 379-382), which needs Collection.schemaChanged() false (Collection.java:364-371, 380-382). env and needs_state unset. The MaterialDialog OK dispatch to ConfirmationDialog is library code: INFERRED.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$6$1.cancel', 'GUI',
  'press Cancel on the reposition confirmation shown when the schema change needs confirmation',
  gui=['press Cancel on the reposition confirmation shown when the schema change needs confirmation'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:397-399; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-49; SRC com/ichi2/libanki/Collection.java:364-382',
  note='MISSING GATE MG282: same dialog and schema-changed condition as the OK edge (ModelFieldEditor.java:375-382; Collection.java:364-371, 380-382). env and needs_state unset. The MaterialDialog cancel dispatch is library code: INFERRED.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$7.confirm', 'GUI',
  'press OK on the sort-field confirmation shown when the schema change needs confirmation',
  gui=['press OK on the sort-field confirmation shown when the schema change needs confirmation'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:456-471; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-49; SRC com/ichi2/libanki/Collection.java:364-382',
  note='MISSING GATE MG282: the dialog is created only when modSchema() throws in sortByField (ModelFieldEditor.java:460-465), which needs Collection.schemaChanged() false (Collection.java:364-371, 380-382). env and needs_state unset. The MaterialDialog OK dispatch is library code: INFERRED.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$7.cancel', 'GUI',
  'press Cancel on the sort-field confirmation shown when the schema change needs confirmation',
  gui=['press Cancel on the sort-field confirmation shown when the schema change needs confirmation'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:473-475; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-49; SRC com/ichi2/libanki/Collection.java:364-382',
  note='MISSING GATE MG282: same dialog and schema-changed condition as the OK edge (ModelFieldEditor.java:460-465; Collection.java:364-371, 380-382). env and needs_state unset. The MaterialDialog cancel dispatch is library code: INFERRED.')

e('S_DLG_MODELEDITOR_CONTEXT', 'ModelFieldEditor$9.onSelection', 'GUI',
  'tap a row of the field context menu (sort, reposition, delete or rename)',
  gui=['tap a row of the field context menu (sort, reposition, delete or rename)'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:137-139, 592-607; SRC com/ichi2/anki/dialogs/ModelEditorContextMenu.java:40-44',
  note='The menu is created and shown in ModelFieldEditor$1.onItemClick (ModelFieldEditor.java:137-139, batch 033) with itemsCallback(mContextMenuListener) (ModelEditorContextMenu.java:40-44). The ListCallback dispatch is library code: INFERRED. No gate.')

e('ModelFieldEditor$6.<init>', 'ModelFieldEditor$6.onPositive', 'FRAMEWORK',
  'press OK on the reposition dialog (MaterialDialog ButtonCallback)',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:356-360, 376-378',
  note='The ButtonCallback object created by $6.<init> is the one the dialog calls on OK. The library dispatch is not in the dataset (source not read): INFERRED, as label_001 and label_005. No gate: the dialog is shown on each reposition request.')

e('ModelFieldEditor$6.onPositive', 'ModelFieldEditor$8.onPreExecute', 'ASYNC',
  'the reposition task starts: onPreExecute runs on the UI thread inside execute()',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:376-378, 528-533; SRC com/ichi2/async/DeckTask.java:129-134, 344-347, 1296-1302; FW-SRC core/java/android/os/AsyncTask.java:645-650',
  note='launchDeckTask (DeckTask.java:129-134) calls execute(), which calls onPreExecute() before the background work (AsyncTask.java:648). The dispatch to the listener is exact at DeckTask.java:1300. Fresh-collection direct path; the dialog path is the $6$1.confirm edge.')

e('ModelFieldEditor$6.onPositive', 'ModelFieldEditor$8.onPostExecute', 'ASYNC',
  'the reposition task finishes in the background and posts its result to the UI thread',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:376-378, 536-543; SRC com/ichi2/async/DeckTask.java:360-365, 1305-1307; FW-SRC core/java/android/os/AsyncTask.java:691-698, 714-715',
  note='AsyncTask.finish calls onPostExecute (AsyncTask.java:691-698) through the handler (714-715). DeckTask.onPostExecute calls the listener (DeckTask.java:360-365; exact dispatch at 1306). The body closes the activity on a DB error (ModelFieldEditor.java:537-538) and refreshes the list.')

e('ModelFieldEditor$6$1.confirm', 'ModelFieldEditor$8.onPreExecute', 'ASYNC',
  'the reposition task starts after the schema confirmation: onPreExecute runs on the UI thread inside execute()',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:388-390, 528-533; SRC com/ichi2/async/DeckTask.java:129-134, 344-347, 1296-1302; FW-SRC core/java/android/os/AsyncTask.java:645-650',
  note='MISSING GATE MG282 on the route into $6$1.confirm (schema unchanged, see the S_DLG_CONFIRMATION edge). env and needs_state unset. Same dispatch as the $6.onPositive edge (AsyncTask.java:648; DeckTask.java:1300).')

e('ModelFieldEditor$6$1.confirm', 'ModelFieldEditor$8.onPostExecute', 'ASYNC',
  'the reposition task finishes after the schema confirmation and posts its result to the UI thread',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:388-390, 536-543; SRC com/ichi2/async/DeckTask.java:360-365, 1305-1307; FW-SRC core/java/android/os/AsyncTask.java:691-698, 714-715',
  note='MISSING GATE MG282 on the route into $6$1.confirm (schema unchanged). env and needs_state unset. Same finish path as the $6.onPositive edge (AsyncTask.java:691-698; DeckTask.java:1306).')

e('ModelFieldEditor$7.confirm', 'ModelFieldEditor$8.onPreExecute', 'ASYNC',
  'the sort-field task starts after the schema confirmation: onPreExecute runs on the UI thread inside execute()',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:468-469, 528-533; SRC com/ichi2/async/DeckTask.java:129-134, 344-347, 1296-1302; FW-SRC core/java/android/os/AsyncTask.java:645-650',
  note='MISSING GATE MG282 on the route into $7.confirm (schema unchanged, see the S_DLG_CONFIRMATION edge). env and needs_state unset. Same dispatch as the $6.onPositive edge (AsyncTask.java:648; DeckTask.java:1300).')

e('ModelFieldEditor$7.confirm', 'ModelFieldEditor$8.onPostExecute', 'ASYNC',
  'the sort-field task finishes after the schema confirmation and posts its result to the UI thread',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:468-469, 536-543; SRC com/ichi2/async/DeckTask.java:360-365, 1305-1307; FW-SRC core/java/android/os/AsyncTask.java:691-698, 714-715',
  note='MISSING GATE MG282 on the route into $7.confirm (schema unchanged). env and needs_state unset. Same finish path as the $6.onPositive edge (AsyncTask.java:691-698; DeckTask.java:1306).')

UNREACHABLE['ModelFieldEditor$8.onCancelled'] = ('no_trigger_in_app',
  'No in-app event cancels a field task. The four field types 43-46 (DeckTask.java:96-99: DeleteField, RepositionField, AddField, ChangeSortField) all pass mChangeFieldHandler (ModelFieldEditor.java:198, 208, 281, 376, 388, 461, 468) and discard the returned task. DeckTask.cancelTask(int) cancels the latest task only when its mType equals the argument (DeckTask.java:181-184); the only callers pass 30 and 37 (CardBrowser.java:528-529, 796-797, 1155). The no-argument cancelTask() (DeckTask.java:168-178) is called only from line 184. The other cancel(true) calls act on other task objects (TaskOperations.java:33; Connection.java:541; Statistics.java:543, 574, 681, 692). For review: the automatic CALL DeckTask.onCancelled to ModelFieldEditor$8.onCancelled (DeckTask.java:369, cha) makes it look reachable.',
  'SRC com/ichi2/async/DeckTask.java:96-99, 168-184, 368-370; SRC com/ichi2/anki/ModelFieldEditor.java:198, 208, 281, 376, 388, 461, 468; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; SRC com/ichi2/anki/runtimetools/TaskOperations.java:33; SRC com/ichi2/async/Connection.java:541; SRC com/ichi2/anki/Statistics.java:543, 574, 681, 692',
  'SOURCE')

UNREACHABLE['ModelFieldEditor$8.onProgressUpdate'] = ('no_trigger_in_app',
  'Body is empty ("This decktask does not publish updates", ModelFieldEditor.java:546-548). The only route is publishProgress, and none of the four field bodies calls it (DeckTask.java:1144-1227: doInBackGroundDeleteField, RepositionField, AddField, ChangeSortField). The ten publishProgress call sites are at DeckTask.java:380, 420, 422, 457, 565, 601, 633, 659, 809, 859; the AsyncTask.publishProgress definition is FW-SRC AsyncTask.java:684-689. For review: the automatic CALL DeckTask$TaskListener.onProgressUpdate@ModelFieldEditor$8 to ModelFieldEditor$8.onProgressUpdate (DeckTask.java:1312, exact) is in auto_calls.json.',
  'SRC com/ichi2/anki/ModelFieldEditor.java:546-548; SRC com/ichi2/async/DeckTask.java:352-355, 380, 420, 422, 457, 565, 601, 633, 659, 809, 859, 1144-1227, 1296-1314; FW-SRC core/java/android/os/AsyncTask.java:684-689',
  'SOURCE')
