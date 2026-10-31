# Conflicts and open items: part 005 (LABEL helper, batch_005)

Files: graphs/AnkiDroid/parts/label_005.py, graphs/AnkiDroid/parts/label_005.md.
Checker result after relabel: `entries 20, rows 51, problems 0`. Labels: REACHABLE 31, UNREACHABLE 9, EDGE 11, INFERRED 0. The 17 rows that were INFERRED are now REACHABLE with `confirmed_by INFERRED` in the reason column, as the coordinator asked. No method was removed.

## 1. ASYNC edges missing from graph_def.py (owner = part containing the starter method)

graph_def.py has only three ASYNC edges: line 510 `DeckPicker.updateDeckList -> DeckPicker$22.onPostExecute`, line 516 `DeckPicker.undo -> DeckPicker$13.onPostExecute`, line 522 `DeckPicker.sync(String) -> DeckPicker$17.onPostExecute`.

Missing for batch_005 listeners. Each is listed in label_005.md with its route, and the starter's part writes the edge. None is written here.
- `DeckPicker.updateDeckList -> DeckPicker$22.onPreExecute`. Owner: batch_003 (updateDeckList).
- `DeckPicker.deleteDeck -> DeckPicker$24.onPreExecute` and `-> DeckPicker$24.onPostExecute`. Owner: batch_002 (deleteDeck).
- `DeckPicker.rebuildFiltered -> DeckPicker$25.onPreExecute` and `-> DeckPicker$25.onPostExecute`. Owner: batch_003 (rebuildFiltered).
- `DeckPicker.emptyFiltered -> DeckPicker$25.onPreExecute` and `-> DeckPicker$25.onPostExecute`. Owner: batch_002 (emptyFiltered).
- `DeckPicker.handleEmptyCards -> DeckPicker$27.onPreExecute` and `-> DeckPicker$27.onPostExecute`. Owner: batch_002 (handleEmptyCards).
- `DeckPicker.importAdd -> DeckPicker$5.onPostExecute`. Owner: batch_002 (importAdd).

## 2. Unsupported ASYNC claims in parts/label_004.md (not my file; not edited)

label_004.md marks these rows "ASYNC edge owned by DeckPicker part". No such edge is in graph_def.py:
$13.onPreExecute, $13.onProgressUpdate, $14.onPreExecute, $14.onPostExecute, $15.onPreExecute, $15.onPostExecute, $16.onPreExecute, $16.onPostExecute, $17.onCancelled, $17.onDisconnected, $17.onPreExecute, $17.onProgressUpdate.
The edges that do exist are $13.onPostExecute (line 516) and $17.onPostExecute (line 522). The check covered the first 34 lines of label_004.md, so there may be more rows.

## 3. c1_check INFERRED conflict (resolved by relabel)

c1_check.py (line 90) accepts only REACHABLE, UNREACHABLE and EDGE. The 17 rows that had INFERRED as their label now use REACHABLE, with the route named in the kind-or-route column and `confirmed_by INFERRED` at the start of the reason column. The checker reports `problems 0`. c1_check.py was not edited.
Note for the coordinator: `confirmed_by INFERRED` marks a route whose last step is a library callback with no source in the dataset (Snackbar.Callback, MaterialDialog.ButtonCallback, MaterialDialog.ListCallback). The source route up to that callback is cited in each row. The 17 rows are DeckPicker$22.onPreExecute; $23.<init>, $23.onNegative, $23.onPositive; $24.<init>, $24.onPostExecute, $24.onPreExecute; $25.onPostExecute, $25.onPreExecute; $26.onDismissed, $26.onShown; $27.<init>, $27.onPostExecute, $27.onPreExecute; $27$1.<init>, $27$1.confirm; $5.onPostExecute.
No entries were in label_005.py for these 17 rows (REACHABLE rows need no py entry), so only the py header comment changed.

## 4. parts/label_004.py defect (not my file; not edited)

Line 7 is `UNREACHABLE = {}`. The brief forbids assigning a global UNREACHABLE. The file also has `UNREACHABLE['...']` subscript entries from line 9 onward.

## 5. Page edges and routes (no edges written for other batches)

Each route below is named in its label_005.md row. The page edge that starts it is owned by the part containing its destination, not by this part:
- `S_DECKPICKER -> DeckPicker.handleEmptyCards`: route is the options menu action_empty_cards (DeckPicker.java:605-608, inside onOptionsItemSelected). onOptionsItemSelected is in LC_NO_TRIGGER (graph_def.py:37) and has no edge. batch_002 writes the page edge if it chooses.
- `S_DECKPICKER -> DeckPicker$1.onClick` (batch_003 writes it; label_003.py line 65): the expander route DeckPicker.java:183-187 reaches updateDeckList at line 187 for $22.<init> and $22.onPreExecute. Gate: deck has subdecks.
- Rename dialog ($23): route is S_DECKPICKER -> DeckPicker$4.onLongClick -> DeckPickerContextMenu rename item (DeckPickerContextMenu.java:140-142) -> renameDeckDialog(). The other caller, StudyOptionsFragment.java:329 (batch_038), is not merged.
- deleteDeck ($24): route is DeckPicker$4.onLongClick -> DeckPickerContextMenu delete item (122-124) -> confirmDeckDeletion() -> confirmDeckDeletion(long) with cnt==0 (DeckPicker.java:1995). Decks with cards go through DeckPickerConfirmDeleteDeckDialog.java:34-37 and deleteContextMenuDeck (DeckPicker.java:2014). The other caller, StudyOptionsFragment.java:332 (batch_038), is not merged.
- rebuildFiltered and emptyFiltered ($25): route is DeckPicker$4.onLongClick -> DeckPickerContextMenu items at 158-160 and 164-166. Those dispatch through a ListCallback (library).
- importAdd ($5.onPostExecute): route is onOptionsItemSelected action_import (DeckPicker.java:561-563) -> showImportDialog(int) (1088-1089) -> ImportDialog positive button (ImportDialog.java:131-134).

## 6. Library dispatch with no source in the dataset

Snackbar.Callback (DeckPicker$26.onDismissed and onShown), MaterialDialog.ButtonCallback (DeckPicker$23.onNegative and onPositive, ImportDialog positive, ConfirmationDialog positive), and MaterialDialog.ListCallback (DeckPickerContextMenu item dispatch). No Snackbar or MaterialDialog source is in final_java_only or fw_src. Each dependent row is REACHABLE with `confirmed_by INFERRED` (see item 3).

## 7. node_names.tsv decl_line values

decl_line is unreliable for anonymous classes (wrong line numbers for DeckPicker$N). All citations in this part come from reading DeckPicker.java and DeckTask.java directly.

## 8. Batch membership note

batch_005.txt contains $5.<init>, $5.onCancelled and $5.onPostExecute. $5.onPreExecute and $5.onProgressUpdate are in batch_006.txt (lines 1-2), and $6 is at batch_006.txt lines 3-7. They are not labeled here.

## 9. Overlap risk at merge

batch_002 (background agent aadd164203afd1638, still running when this was written) owns handleDeckSelection and may write S_DECKPICKER edges to DeckPicker$2, $3, $4, $20, $21. The two GUI edges and two REGISTER edges here may duplicate it. Check for duplicate keys before merging.

## 10. Other notes

- $20 Uri: helpUrl is computed in handleDeckSelection (DeckPicker.java:1771), and the snackbar action $20.onClick calls openUrl(helpUrl) at 1776. The row is REACHABLE.
- Missing gates MG6 (empty deck) and MG7 (no cards due, not filtered) are described in label_005.md only. graph_def.py has no constants for them.
- The STATUS RUNNING time (22:21) is the time label_005.py was written. The run start was not logged.
- cancel analysis: DeckTask.cancelTask(int) is called only from CardBrowser (528-529, 796-797, 1155). So every DeckPicker onCancelled is no_trigger_in_app.
- progress analysis: LoadDeckCounts, DeleteDeck, RebuildCram, EmptyCram and FindEmptyCards call no publishProgress, so their onProgressUpdate bodies are framework_never_calls.
