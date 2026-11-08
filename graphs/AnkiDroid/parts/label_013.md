STATUS: RUNNING 02:33

Batch 013: NoteEditor part 2, 40 methods (NoteEditor.updateCards, updateDeckPosition, updateField, updateFieldsFromMap, updateTags, and the anonymous classes NoteEditor$1 to $13 with their callbacks). Source root: final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/java. Gates used: MG75 to MG81; MG82 to MG84 not used. Edges follow the ownership rule (source part, or destination part for S_* pages). Dependencies: batch_012 (the callers saveNote, showTagsDialog, showCardTemplateEditor, onOptionsItemSelected, startMultimediaFieldEditor, onCollectionLoaded, registerExternalStorageListener and changeNoteTypeWithErrorHandling) and batch_014 (NoteEditor$EditNoteTypeListener, which calls updateFieldsFromMap at NoteEditor.java:1625). Two methods are UNREACHABLE; the rest are REACHABLE through the edges listed below.

| item | label | kind | reason | source |
| --- | --- | --- | --- | --- |
| NoteEditor.updateCards | REACHABLE | - | Sets the Cards button text from the note type templates; called from setNote(Note) and onActivityResult. | com/ichi2/anki/NoteEditor.java:1404-1429, 1379, 1063 |
| NoteEditor.updateDeckPosition | REACHABLE | - | Selects the current deck in the deck spinner; called from setNote(Note). | com/ichi2/anki/NoteEditor.java:1384-1391, 1377 |
| NoteEditor.updateField | REACHABLE | - | Copies one field's text into the note; called from saveNote and duplicateCheck. | com/ichi2/anki/NoteEditor.java:1432-1439, 665, 722, 1301 |
| NoteEditor.updateFieldsFromMap | REACHABLE | - | Rebuilds the field rows from the new note type mapping; called from the remap popup and from the change-note-type listener (batch_014). | com/ichi2/anki/NoteEditor.java:1468-1499, 1225, 1625 |
| NoteEditor.updateTags | REACHABLE | - | Sets the Tags button text; called from setNote(Note) and the tags dialog listener. | com/ichi2/anki/NoteEditor.java:1394-1400, 1378, 995 |
| NoteEditor$1.onCancelled | UNREACHABLE | no_trigger_in_app | The add-note task is never cancelled: the only DeckTask cancel is inside cancelTask(), which is reached only from cancelTask(int) with CardBrowser's search and browser-QA types. The body is empty. | com/ichi2/async/DeckTask.java:172, 181-186, 243-244; com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; com/ichi2/anki/NoteEditor.java:276-278; FW-SRC core/java/android/os/AsyncTask.java:525-528, 691-698 |
| NoteEditor$1.onPostExecute | REACHABLE | - | Result handler of the add-note task, dispatched by AsyncTask.finish; the editor is closed with RESULT_DB_ERROR at line 271. | com/ichi2/anki/NoteEditor.java:250-273; FW-SRC core/java/android/os/AsyncTask.java:691-698 |
| NoteEditor$1.onPreExecute | REACHABLE | - | Shows the saving progress dialog; dispatched by AsyncTask at the start of the add-note task. | com/ichi2/anki/NoteEditor.java:190-194; FW-SRC core/java/android/os/AsyncTask.java:646-648 |
| NoteEditor$1.onProgressUpdate | REACHABLE | - | Handles progress from the add-note task (setNote and sticky-field restore); dispatched by AsyncTask.publishProgress. | com/ichi2/anki/NoteEditor.java:198-246; FW-SRC core/java/android/os/AsyncTask.java:684-689, 714-715 |
| NoteEditor$10.<init> | REACHABLE | - | Constructs the tags dialog listener in showTagsDialog. | com/ichi2/anki/NoteEditor.java:989-997 |
| NoteEditor$10.onPositive | REACHABLE | - | Tags dialog OK: stores the selected tags and refreshes the Tags button. | com/ichi2/anki/NoteEditor.java:993-996; com/ichi2/anki/dialogs/TagsDialog.java:164-166 |
| NoteEditor$11.<init> | REACHABLE | - | Constructs the media button listener in setMMButtonListener. | com/ichi2/anki/NoteEditor.java:1129-1131 |
| NoteEditor$11.onClick | REACHABLE | - | Media button tap: starts the field editor for a non-empty field, otherwise shows the media popup. | com/ichi2/anki/NoteEditor.java:1132-1146 |
| NoteEditor$11$1.<init> | REACHABLE | - | Constructs the media popup listener. | com/ichi2/anki/NoteEditor.java:1148-1150 |
| NoteEditor$11$1.onMenuItemClick | REACHABLE | - | Popup choice (audio, image or text); the audio branch starts the field editor. | com/ichi2/anki/NoteEditor.java:1150-1160 |
| NoteEditor$12.<init> | REACHABLE | - | Constructs the remap button listener in setRemapButtonListener. | com/ichi2/anki/NoteEditor.java:1186-1189 |
| NoteEditor$12.onClick | REACHABLE | - | Remap button tap: builds and shows the old-field popup. | com/ichi2/anki/NoteEditor.java:1189-1198, 1229 |
| NoteEditor$12$1.<init> | REACHABLE | - | Constructs the old-field popup listener. | com/ichi2/anki/NoteEditor.java:1199-1201 |
| NoteEditor$12$1.onMenuItemClick | REACHABLE | - | Picks the old field for the new field, then reloads the fields through updateFieldsFromMap. | com/ichi2/anki/NoteEditor.java:1201-1227 |
| NoteEditor$13.<init> | REACHABLE | - | Constructs the field text watcher, added in initFieldEditText after init. | com/ichi2/anki/NoteEditor.java:1247-1253 |
| NoteEditor$13.afterTextChanged | REACHABLE | - | Sets mFieldEdited and runs the duplicate check for field 0. | com/ichi2/anki/NoteEditor.java:1255-1260 |
| NoteEditor$13.beforeTextChanged | REACHABLE | - | Empty body; reached through the TextView dispatch. | com/ichi2/anki/NoteEditor.java:1264-1265; FW-SRC core/java/android/widget/TextView.java:9309-9314 |
| NoteEditor$13.onTextChanged | REACHABLE | - | Empty body; reached through the TextView dispatch. | com/ichi2/anki/NoteEditor.java:1269-1270; FW-SRC core/java/android/widget/TextView.java:9359-9364 |
| NoteEditor$2.<init> | REACHABLE | - | Constructs the Cards button listener in onCollectionLoaded. | com/ichi2/anki/NoteEditor.java:353-359 |
| NoteEditor$2.onClick | REACHABLE | - | Cards button tap: opens the template editor (showCardTemplateEditor, batch_012). | com/ichi2/anki/NoteEditor.java:355-358, 1001-1002 |
| NoteEditor$3.<init> | REACHABLE | - | Constructs the deck spinner listener in onCollectionLoaded. | com/ichi2/anki/NoteEditor.java:471-482 |
| NoteEditor$3.onItemSelected | REACHABLE | - | Sets mCurrentDid from the selected deck position. | com/ichi2/anki/NoteEditor.java:473-476 |
| NoteEditor$3.onNothingSelected | UNREACHABLE | framework_never_calls | The spinner adapter is set once and never changed; both setSelection calls use a valid index; AdapterView fires onNothingSelected only for a negative selection, which this path never reaches. Framework read from source, not run: INFERRED. | com/ichi2/anki/NoteEditor.java:468-469, 479-481, 1385-1387; FW-SRC core/java/android/widget/AdapterView.java:941-947, 1103-1108 |
| NoteEditor$4.<init> | REACHABLE | - | Constructs the Tags button listener in onCollectionLoaded. | com/ichi2/anki/NoteEditor.java:526-531 |
| NoteEditor$4.onClick | REACHABLE | - | Tags button tap: opens the tags dialog (showTagsDialog, batch_012). | com/ichi2/anki/NoteEditor.java:528-531 |
| NoteEditor$5.<init> | REACHABLE | - | Constructs the map-cards-to-nothing confirmation in saveNote. | com/ichi2/anki/NoteEditor.java:690-698 |
| NoteEditor$5.confirm | REACHABLE | - | Confirmed: runs changeNoteTypeWithErrorHandling without the check. | com/ichi2/anki/NoteEditor.java:692-695; com/ichi2/anki/dialogs/ConfirmationDialog.java:40-43 |
| NoteEditor$6.<init> | REACHABLE | - | Constructs the schema-change confirmation in changeNoteTypeWithErrorHandling. | com/ichi2/anki/NoteEditor.java:751-763 |
| NoteEditor$6.confirm | REACHABLE | - | Confirmed: runs modSchemaNoCheck, then changeNoteType. | com/ichi2/anki/NoteEditor.java:753-761; com/ichi2/libanki/Collection.java:364-371 |
| NoteEditor$7.<init> | REACHABLE | - | Constructs the reset-card-progress confirmation in onOptionsItemSelected. | com/ichi2/anki/NoteEditor.java:851-864 |
| NoteEditor$7.confirm | REACHABLE | - | Confirmed: forgets the current card's progress, resets the collection and sets mReloadRequired. | com/ichi2/anki/NoteEditor.java:855-863 |
| NoteEditor$8.<init> | REACHABLE | - | Constructs the SD-card eject receiver in registerExternalStorageListener. | com/ichi2/anki/NoteEditor.java:892-899 |
| NoteEditor$8.onReceive | REACHABLE | - | On the eject broadcast, finishes the editor without animation. | com/ichi2/anki/NoteEditor.java:894-898; com/ichi2/anki/receiver/SdCardReceiver.java:42-47 |
| NoteEditor$9.<init> | REACHABLE | - | Constructs the discard-changes callback in showDiscardChangesDialog. | com/ichi2/anki/NoteEditor.java:921-927 |
| NoteEditor$9.onPositive | REACHABLE | - | Discard OK: calls closeNoteEditor(). | com/ichi2/anki/NoteEditor.java:923-926 |
| NoteEditor$2.<init> -> NoteEditor$2.onClick (REGISTER) | EDGE | REGISTER | Cards button listener set in onCollectionLoaded. | com/ichi2/anki/NoteEditor.java:353-359 |
| S_NOTEEDITOR -> NoteEditor$2.onClick (GUI) | EDGE | GUI | Tap the Cards text to open the template editor. No gate: the view has no visibility attribute. | com/ichi2/anki/NoteEditor.java:353-359; res/layout/note_editor.xml:116-122 |
| NoteEditor$3.<init> -> NoteEditor$3.onItemSelected (REGISTER) | EDGE | REGISTER | Deck spinner listener set in onCollectionLoaded. | com/ichi2/anki/NoteEditor.java:471-482 |
| S_NOTEEDITOR -> NoteEditor$3.onItemSelected (FRAMEWORK) | EDGE | FRAMEWORK | The first selection fires onItemSelected when the spinner is laid out. The AbsSpinner step is not in fw_src (INFERRED). | com/ichi2/anki/NoteEditor.java:452-469, 471-476; FW-SRC core/java/android/widget/AdapterView.java:937-947; FW-SRC core/java/android/widget/Spinner.java:637-648, 681 |
| S_NOTEEDITOR -> NoteEditor$3.onItemSelected (GUI) | EDGE | GUI | Pick another deck in the drop-down. MISSING GATE MG80: needs two or more decks in the list. | com/ichi2/anki/NoteEditor.java:452-462, 471-476 |
| NoteEditor$4.<init> -> NoteEditor$4.onClick (REGISTER) | EDGE | REGISTER | Tags button listener set in onCollectionLoaded. | com/ichi2/anki/NoteEditor.java:526-531 |
| S_NOTEEDITOR -> NoteEditor$4.onClick (GUI) | EDGE | GUI | Tap the Tags button to open the tags dialog. No gate: the view has no visibility attribute. | com/ichi2/anki/NoteEditor.java:526-531, 983-999; res/layout/note_editor.xml:85-90 |
| NoteEditor$8.<init> -> NoteEditor$8.onReceive (REGISTER) | EDGE | REGISTER | SD-card eject receiver registered in registerExternalStorageListener (called from onCollectionLoaded, batch_012). | com/ichi2/anki/NoteEditor.java:892-902, 340 |
| S_NOTEEDITOR -> NoteEditor$8.onReceive (SYSTEM) | EDGE | SYSTEM | SD card ejected while the editor is open (ENV_SDCARD_EVENT). The system delivery hop is INFERRED. | com/ichi2/anki/NoteEditor.java:895-896; com/ichi2/anki/receiver/SdCardReceiver.java:42-47 |
| NoteEditor$9.<init> -> NoteEditor$9.onPositive (REGISTER) | EDGE | REGISTER | Discard-changes callback built in showDiscardChangesDialog. | com/ichi2/anki/NoteEditor.java:921-927 |
| S_NOTEEDITOR -> NoteEditor$9.onPositive (GUI) | EDGE | GUI | Close with unsaved changes, then OK on the discard dialog. MISSING GATE MG79: hasUnsavedChanges must be true. | com/ichi2/anki/NoteEditor.java:625-627, 907-911, 921-927 |
| NoteEditor$10.<init> -> NoteEditor$10.onPositive (REGISTER) | EDGE | REGISTER | Tags dialog listener set in showTagsDialog. | com/ichi2/anki/NoteEditor.java:989-997; com/ichi2/anki/dialogs/TagsDialog.java:162-167 |
| S_DLG_TAGS -> NoteEditor$10.onPositive (GUI) | EDGE | GUI | In the tags dialog, select tags and tap OK. The MaterialDialog dispatch is library code (INFERRED). | com/ichi2/anki/dialogs/TagsDialog.java:162-167 |
| NoteEditor$11.<init> -> NoteEditor$11.onClick (REGISTER) | EDGE | REGISTER | Media button listener set when not in change-note-type mode. | com/ichi2/anki/NoteEditor.java:1116-1122, 1129-1131 |
| S_NOTEEDITOR -> NoteEditor$11.onClick (GUI) | EDGE | GUI | Tap the media button (not in change-note-type mode). MISSING GATE MG77: setMMButtonListener runs only when editModelMode is false. | com/ichi2/anki/NoteEditor.java:1116-1122, 1132-1146 |
| NoteEditor$11$1.<init> -> NoteEditor$11$1.onMenuItemClick (REGISTER) | EDGE | REGISTER | Popup listener set on the media popup of an empty field. | com/ichi2/anki/NoteEditor.java:1142-1148 |
| S_NOTEEDITOR -> NoteEditor$11$1.onMenuItemClick (GUI) | EDGE | GUI | Tap the media button of an empty field, then choose audio, image or text. MISSING GATE MG77 applies. The popup dispatch is library code (INFERRED). | com/ichi2/anki/NoteEditor.java:1135-1160 |
| NoteEditor$12.<init> -> NoteEditor$12.onClick (REGISTER) | EDGE | REGISTER | Remap button listener set in setRemapButtonListener (edit mode, more than two fields). | com/ichi2/anki/NoteEditor.java:1112-1115, 1186-1189 |
| S_NOTEEDITOR -> NoteEditor$12.onClick (GUI) | EDGE | GUI | Change the note type to one with more than two fields, then tap a remap button. MISSING GATE MG78. | com/ichi2/anki/NoteEditor.java:1112-1115, 1186-1198, 1507 |
| NoteEditor$12$1.<init> -> NoteEditor$12$1.onMenuItemClick (REGISTER) | EDGE | REGISTER | Old-field popup listener set in setRemapButtonListener. | com/ichi2/anki/NoteEditor.java:1192-1201 |
| S_NOTEEDITOR -> NoteEditor$12$1.onMenuItemClick (GUI) | EDGE | GUI | Pick an old field (or None) after a remap tap. MISSING GATE MG78 applies. | com/ichi2/anki/NoteEditor.java:1199-1201, 1225-1229 |
| NoteEditor$13.<init> -> NoteEditor$13.afterTextChanged (REGISTER) | EDGE | REGISTER | Text watcher added in initFieldEditText, after editText.init. | com/ichi2/anki/NoteEditor.java:1247, 1253 |
| NoteEditor$13.<init> -> NoteEditor$13.beforeTextChanged (REGISTER) | EDGE | REGISTER | Same text watcher. | com/ichi2/anki/NoteEditor.java:1247, 1253-1265 |
| NoteEditor$13.<init> -> NoteEditor$13.onTextChanged (REGISTER) | EDGE | REGISTER | Same text watcher. | com/ichi2/anki/NoteEditor.java:1247, 1253-1270 |
| S_NOTEEDITOR -> NoteEditor$13.afterTextChanged (FRAMEWORK) | EDGE | FRAMEWORK | Typing in an enabled field. MISSING GATE MG81: the field is enabled only when editModelMode is false. | com/ichi2/anki/NoteEditor.java:1102, 1255-1260, 1272; FW-SRC core/java/android/widget/TextView.java:9375-9380 |
| S_NOTEEDITOR -> NoteEditor$13.beforeTextChanged (FRAMEWORK) | EDGE | FRAMEWORK | Typing in an enabled field. MISSING GATE MG81 applies. Empty body. | com/ichi2/anki/NoteEditor.java:1264-1265; FW-SRC core/java/android/widget/TextView.java:9309-9314 |
| S_NOTEEDITOR -> NoteEditor$13.onTextChanged (FRAMEWORK) | EDGE | FRAMEWORK | Typing in an enabled field. MISSING GATE MG81 applies. Empty body. | com/ichi2/anki/NoteEditor.java:1269-1270; FW-SRC core/java/android/widget/TextView.java:9359-9364 |
| S_DLG_CONFIRMATION -> NoteEditor$5.confirm (GUI) | EDGE | GUI | OK on the map-cards-to-nothing confirmation raised in saveNote (batch_012). MISSING GATE MG76: the change needs an edited note in change-note-type mode. | com/ichi2/anki/NoteEditor.java:688-698; com/ichi2/anki/dialogs/ConfirmationDialog.java:40-43 |
| S_DLG_CONFIRMATION -> NoteEditor$6.confirm (GUI) | EDGE | GUI | OK on the schema-change confirmation raised in changeNoteTypeWithErrorHandling (batch_012). MISSING GATE MG76 and the libanki check. | com/ichi2/anki/NoteEditor.java:751-763; com/ichi2/libanki/Collection.java:364-371; com/ichi2/anki/dialogs/ConfirmationDialog.java:40-43 |
| S_DLG_CONFIRMATION -> NoteEditor$7.confirm (GUI) | EDGE | GUI | Reset card progress from the menu, then OK. MISSING GATE MG75: the menu item is hidden in add mode. | com/ichi2/anki/NoteEditor.java:800-810, 851-864; res/menu/note_editor.xml:17-20; com/ichi2/anki/dialogs/ConfirmationDialog.java:40-43 |

STATUS: DONE 02:36
