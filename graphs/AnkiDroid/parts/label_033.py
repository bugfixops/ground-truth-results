# AnkiDroid batch 033 (LABEL helper). ModelFieldEditor part 1: 40 methods. The full row list is in
# graphs/AnkiDroid/parts/label_033.md. No method in this batch is UNREACHABLE, so there are no UNREACHABLE entries.
#
# Route ownership:
# - CALL edges inside ModelFieldEditor and into its anonymous classes come from auto_calls.json (for example
#   onOptionsItemSelected -> addFieldDialog, renameField -> Models.renameField). They are not written here.
# - The ASYNC launch edges into ModelFieldEditor$8.onPostExecute are written here, because the launch sites are in
#   this batch. The onPreExecute of $8 is not linked from the launch sites (label_019 convention).
# - Edges into methods outside this batch belong to the batch that holds those methods. The page edges from
#   S_MODELFIELDEDITOR and the ENTERS edges from these methods are written here, because their sources are in this batch.
#
# Gate MG272 (batch range MG272-MG281): the sync-required schema branch, which is the catch of
# ConfirmModSchemaException (Collection.modSchema(true) throws only when the schema is not yet marked changed,
# Collection.java:364-373). No predefined STATE kind covers that collection state, so env and needs_state are unset on
# the gated edges. Predefined constant used: STATE_COLLECTION on the page edges. Page node: S_MODELFIELDEDITOR.

# --- Lifecycle callback that starts the collection loader (ModelFieldEditor.onCreate, line 75).
e('ModelFieldEditor.onCreate', 'ModelFieldEditor.onCollectionLoaded', 'ASYNC',
  'the collection loader started by onCreate calls onCollectionLoaded when the collection is ready',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:72-75, 115-120; SRC com/ichi2/anki/AnkiActivity.java:255-262, 283-286',
  note='startLoadingCollection (AnkiActivity.java:255-262) restarts the loader, and AnkiActivity.onLoadFinished (283-286) calls onCollectionLoaded. Same route as the ModelBrowser precedent (label_031.py). No gate.')

# --- Page edges into the editor methods.
e('S_MODELFIELDEDITOR', 'ModelFieldEditor.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu of the field editor screen',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:102-107; FW-SRC core/java/android/app/Activity.java:3386-3388',
  note='The menu is inflated from res/menu/model_editor.xml, which holds the add button action_add_new_model. No gate.')

e('S_MODELFIELDEDITOR', 'ModelFieldEditor.onOptionsItemSelected', 'GUI',
  'tap the home arrow or the add button in the editor toolbar',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['tap the home arrow or the add button in the editor toolbar'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:553-564; RES res/menu/model_editor.xml:4-8; FW-SRC core/java/android/app/Activity.java:3439-3450',
  note='The home arrow (android.R.id.home) calls onBackPressed (line 556). The add button calls addFieldDialog (line 559). STATE_COLLECTION: the collection file exists, so the editor has loaded its note type.')

e('S_MODELFIELDEDITOR', 'ModelFieldEditor.onBackPressed', 'GUI',
  'press the system back key on the field editor screen',
  env=None,
  gui=['press the system back key on the field editor screen'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:584-587; FW-SRC core/java/android/app/Activity.java:2976-2983',
  note='The framework key-up path calls onBackPressed (Activity.java:2976-2983). The screen is the page, so no state or environment gate is set.')

e('S_MODELFIELDEDITOR', 'ModelFieldEditor$1.onItemClick', 'GUI',
  'tap a field name row on the field editor screen',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['tap a field name row on the field editor screen'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:116-120, 135-142; RES res/layout/model_field_editor.xml:12-19',
  note='The list is filled after the collection loads (onCollectionLoaded, line 116-120). STATE_COLLECTION: the collection file exists.')

e('ModelFieldEditor$1.onItemClick', 'S_DLG_MODELEDITOR_CONTEXT', 'ENTERS',
  'the field context menu (rename, reposition, sort, delete) is shown for the tapped row',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:137-141; SRC com/ichi2/anki/dialogs/ModelEditorContextMenu.java:34-38, 43',
  note='showDialogFragment(mContextMenu) at line 139. The menu entries are in ModelEditorContextMenu.java:34-38; their callback (batch 034) selects the field action. No gate.')

e('S_MODELFIELDEDITOR', 'ModelFieldEditor$2.onPositive', 'GUI',
  'tap the add button in the editor toolbar, type a field name and tap OK',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['tap the add button in the editor toolbar, type a field name and tap OK'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:149-163, 183, 186-199, 558-559; RES res/menu/model_editor.xml:4-8',
  note='The dialog is created by addFieldDialog (auto CALL from onOptionsItemSelected). mMod is set by setupLabels (line 151) after the collection loads, so STATE_COLLECTION is needed. The MaterialDialog OK dispatch is library code: INFERRED (source not read).')

e('ModelFieldEditor$2.onPositive', 'ModelFieldEditor$8.onPostExecute', 'ASYNC',
  'the ADD_FIELD task launched from the add-field OK path; DeckTask calls the listener onPostExecute after the task',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:196-199; SRC com/ichi2/async/DeckTask.java:129-134, 324-325, 360-362, 1305-1307',
  note='The destination ModelFieldEditor$8.onPostExecute is batch 034 (mChangeFieldHandler). The edge is owned here because the launch site is in this batch. No gate on this route (modSchema() does not throw on a fresh install).')

e('ModelFieldEditor$2.onPositive', 'S_DLG_CONFIRMATION', 'ENTERS',
  'the sync-required add-field dialog (full sync confirmation) is shown when the schema change needs confirmation',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:200-219; SRC com/ichi2/libanki/Collection.java:364-374; SRC com/ichi2/libanki/Storage.java:317-319; SRC com/ichi2/libanki/sync/Syncer.java:424-429',
  note='MISSING GATE MG272: the catch branch of modSchema() at line 197. A fresh install does not throw (Storage.java:317-319 sets scm = now and ls = 0), so this branch needs a collection whose schema is already marked changed. A sync sets ls (Syncer.java:428). env and needs_state unset.')

e('ModelFieldEditor$2$1.confirm', 'ModelFieldEditor$8.onPostExecute', 'ASYNC',
  'the ADD_FIELD task relaunched after the user confirms the sync-required schema change; DeckTask calls the listener onPostExecute',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:208-209; SRC com/ichi2/async/DeckTask.java:129-134, 324-325, 360-362, 1305-1307',
  note='MISSING GATE MG272: reached only from the catch branch of the add-field OK path. The destination ModelFieldEditor$8.onPostExecute is batch 034. env and needs_state unset.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$2$1.confirm', 'GUI',
  'tap OK on the sync-required add-field dialog (full sync confirmation)',
  env=None,
  gui=['tap OK on the sync-required add-field dialog (full sync confirmation)'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:204-211; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-44',
  note='MISSING GATE MG272: the dialog is shown only from the catch branch (ModelFieldEditor$2.onPositive). The dialog OK dispatch is ConfirmationDialog.onPositive -> confirm() (ConfirmationDialog.java:40-44). env and needs_state unset.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$2$1.cancel', 'GUI',
  'tap Cancel on the sync-required add-field dialog',
  env=None,
  gui=['tap Cancel on the sync-required add-field dialog'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:213-215; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:46-49',
  note='MISSING GATE MG272: the dialog is shown only from the catch branch. ConfirmationDialog.onNegative -> cancel() (ConfirmationDialog.java:46-49). env and needs_state unset.')

# --- Field delete (deleteField): the ASYNC launch of DELETE_FIELD.
e('ModelFieldEditor.deleteField', 'ModelFieldEditor$8.onPostExecute', 'ASYNC',
  'the DELETE_FIELD task launched by deleteField; DeckTask calls the listener onPostExecute after the task',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:280-286; SRC com/ichi2/async/DeckTask.java:129-134, 318-319, 360-362, 1305-1307',
  note='The destination ModelFieldEditor$8.onPostExecute is batch 034 (mChangeFieldHandler). The edge is owned here because the launch site is in this batch. deleteField is called from the delete confirm methods ModelFieldEditor$3.confirm (ungated) and ModelFieldEditor$4.confirm (MISSING GATE MG272). No gate on this edge.')

# --- Field delete dialogs (deleteFieldDialog). The ENTERS edge covers both dialogs.
e('ModelFieldEditor.deleteFieldDialog', 'S_DLG_CONFIRMATION', 'ENTERS',
  'the field delete warning is shown from the field context menu (delete); a second sync-required dialog uses the same page',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:239-256, 273-274',
  note='One ENTERS edge covers both dialogs shown from deleteFieldDialog: the delete warning (line 256, ungated) and the sync-required dialog (line 274, MISSING GATE MG272). The MG272 gate is carried by the S_DLG_CONFIRMATION -> ModelFieldEditor$4 edges below, so the triple is not duplicated. env and needs_state unset.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$3.confirm', 'GUI',
  'tap OK on the field delete warning',
  env=None,
  gui=['tap OK on the field delete warning'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:241-256; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-44',
  note='The delete warning is the ungated branch (modSchema() does not throw on a fresh install). ConfirmationDialog.onPositive -> confirm() (ConfirmationDialog.java:40-44). No gate.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$3.cancel', 'GUI',
  'tap Cancel on the field delete warning',
  env=None,
  gui=['tap Cancel on the field delete warning'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:251-253; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:46-49',
  note='The delete warning is the ungated branch. ConfirmationDialog.onNegative -> cancel() (ConfirmationDialog.java:46-49). No gate.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$4.confirm', 'GUI',
  'tap OK on the sync-required field delete dialog (full sync confirmation)',
  env=None,
  gui=['tap OK on the sync-required field delete dialog (full sync confirmation)'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:259-267; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-44',
  note='MISSING GATE MG272: the dialog is shown only from the catch branch of deleteFieldDialog (line 257). ConfirmationDialog.onPositive -> confirm() (ConfirmationDialog.java:40-44). env and needs_state unset.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$4.cancel', 'GUI',
  'tap Cancel on the sync-required field delete dialog',
  env=None,
  gui=['tap Cancel on the sync-required field delete dialog'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:269-271; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:46-49',
  note='MISSING GATE MG272: the dialog is shown only from the catch branch of deleteFieldDialog. ConfirmationDialog.onNegative -> cancel() (ConfirmationDialog.java:46-49). env and needs_state unset.')

# --- Sort field (sortByField): the ASYNC launch and the sync-required dialog.
e('ModelFieldEditor.sortByField', 'ModelFieldEditor$8.onPostExecute', 'ASYNC',
  'the CHANGE_SORT_FIELD task launched by sortByField; DeckTask calls the listener onPostExecute after the task',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:458-462; SRC com/ichi2/async/DeckTask.java:129-134, 327-328, 360-362, 1305-1307',
  note='The destination ModelFieldEditor$8.onPostExecute is batch 034. The edge is owned here because the launch site is in this batch. The direct launch (line 461) runs when modSchema() does not throw, so no gate on this edge.')

e('ModelFieldEditor.sortByField', 'S_DLG_CONFIRMATION', 'ENTERS',
  'the sync-required sort field dialog is shown when the schema change needs confirmation',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:458-479',
  note='MISSING GATE MG272: the catch branch of sortByField (modSchema() call at line 460, catch at line 463, dialog shown at line 478). The dialog is ModelFieldEditor$7 (batch 034). A fresh install does not throw, so this needs a collection whose schema is already marked changed. env and needs_state unset.')

# --- Rename dialog (renameFieldDialog).
e('S_MODELFIELDEDITOR', 'ModelFieldEditor$5.onPositive', 'GUI',
  'long-press a field row, choose Rename in the context menu, then tap OK in the rename dialog',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['long-press a field row, choose Rename in the context menu, then tap OK in the rename dialog'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:293-304, 116-120, 135-142; SRC com/ichi2/anki/dialogs/ModelEditorContextMenu.java:12-14, 34-38',
  note='The route goes through the field context menu (S_DLG_MODELEDITOR_CONTEXT, selection by ModelFieldEditor$9.onSelection, batch 034, FIELD_RENAME = 2). The rename dialog is shown over this page. STATE_COLLECTION: the field list is loaded.')

e('ModelFieldEditor$5.onPositive', 'S_DLG_CONFIRMATION', 'ENTERS',
  'the sync-required rename dialog is shown when renameField throws ConfirmModSchemaException',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:315-336; SRC com/ichi2/libanki/Collection.java:364-374',
  note='MISSING GATE MG272: the catch branch of renameField at line 316 (renameField calls Models.renameField, which calls mCol.modSchema(true)). The dialog is ModelFieldEditor$5$1. env and needs_state unset.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$5$1.cancel', 'GUI',
  'tap Cancel on the sync-required rename dialog',
  env=None,
  gui=['tap Cancel on the sync-required rename dialog'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:330-332; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:46-49',
  note='MISSING GATE MG272: the dialog is shown only from the catch branch of renameField. ConfirmationDialog.onNegative -> cancel() (ConfirmationDialog.java:46-49). The confirm method ModelFieldEditor$5$1.confirm is outside this batch. env and needs_state unset.')
