# Conflicts for batch 006 (DeckPicker listeners $5 to $9$1)

Written by the LABEL helper for batch_006. Part: graphs/AnkiDroid/parts/label_006.py and label_006.md.

## 1. ASYNC edges owned by batch_002 (not written here)

The launchers are in DeckPicker.java and belong to batch_002. No label_002.py exists yet, so the ASYNC edges to these callbacks must be written by the launcher's part:

| launcher (DeckPicker.java) | ASYNC edges to write | callers |
|---|---|---|
| importAdd (1579-1582) | DeckPicker$5.onPreExecute; DeckPicker$5.onProgressUpdate (progress route, see below) | ImportDialog.java:134 |
| importReplace (1587-1589) | DeckPicker$6.onPreExecute; DeckPicker$6.onPostExecute; DeckPicker$6.onProgressUpdate | ImportDialog.java:148; DeckPicker.java:1249 |
| exportApkg (1593-1623, launch at 1623) | DeckPicker$7.onPreExecute; DeckPicker$7.onPostExecute | ExportDialog.java:100 |

$5.onPostExecute and $5.onCancelled are in batch_005 (same launcher importAdd).

Progress route for $5.onProgressUpdate and $6.onProgressUpdate (for the part that writes the ASYNC edge): DeckTask.java:750-751 (importAdd: setProgressCallback, run); AnkiPackageImporter.java:50 (publishProgress); Anki2Importer.java:759-762 (forwards to mProgress); DeckTask.java:1340-1350 (ProgressCallback to doProgress); DeckTask.java:352-355 and 1311-1313 (onProgressUpdate to the listener). For import-replace the publish points are DeckTask.java:809 and 859.

Label decision: these callbacks are labelled REACHABLE in label_006.md, with "confirmed_by INFERRED" in the reason. The checker (scratch/c1_check.py) rejects any label value other than REACHABLE, UNREACHABLE or EDGE, so INFERRED cannot be a label.

## 2. $8 (fallback FAB branch) is closed on the standard config, but auto edges reach it

- UNREACHABLE closed_by_api_level for DeckPicker$8.<init> and DeckPicker$8.onClick. Reason: on API 27 the layout-v14 variant of floating_add_button.xml is selected and declares add_content_menu (line 7), so DeckPicker.java:391 is non-null and the else branch (394-405) does not run. minSdkVersion is 10 (build.gradle line 12), so the branch is live on API 10 to 13.
- Overriding auto edge: graphs/AnkiDroid/auto_calls.json has DeckPicker.onCreate -> DeckPicker$8.<init> (line 399). That edge is an over-approximation of bytecode and ignores the layout guard. The integrator must decide how the build resolves an UNREACHABLE key that has an auto CALL edge into it. The builder was not run.
- No REGISTER edge was written from DeckPicker$8.<init> to $8.onClick, because the <init> is closed.

## 3. Auto cha edges into $6/$7 onCancelled and $7 onProgressUpdate

- auto_calls.json has DeckTask$TaskListener.on* -> every listener (cha and exact variants), so DeckTask.onCancelled -> DeckPicker$6/$7.onCancelled (line 369) and the listener progress dispatch reach these methods.
- These are over-approximations. The cancel callers in the app are CardBrowser only (DeckTask.cancelTask(int)); no code cancels an import or export DeckTask. $7.onProgressUpdate has no publishProgress in doInBackgroundExportApkg (DeckTask.java:881-909).
- Labelled UNREACHABLE with no_trigger_in_app or framework_never_calls, the same pattern as label_004 for $13 to $16. The integrator must decide how the auto edges are handled, as in section 2.

## 4. node_names.tsv declaration lines (scratch/node_names.tsv)

- DeckPicker$8.onClick and DeckPicker$9.onClick show decl_line 183. That is wrong. In DeckPicker.java, $8 is created at line 399 with onClick at 401, and $9 is created at 461 with onClick at 463 (body 463-486). 183 belongs to the $1 expander listener area.
- Only these two rows were checked. The other rows of node_names.tsv were not checked. Not edited here (scratch file).

## 5. REGISTER edges written here

- DeckPicker$9.<init> -> DeckPicker$9.onClick (REGISTER) and DeckPicker$9$1.<init> -> DeckPicker$9$1.onPositive (REGISTER). Both <init>s are in this batch, so this part writes them (same convention as label_003 for $1 and $10).
- No REGISTER for $6 or $7: those listeners are passed to launchDeckTask (ASYNC route), not registered on a view.

## 6. Other edges and small mismatches

- GUI edges written here: S_DECKPICKER -> DeckPicker$9.onClick and S_DECKPICKER -> DeckPicker$9$1.onPositive. label_004 wrote no edges for $9 or $9$1, so there is no duplicate.
- Line mismatch (minor): auto_calls.json gives DeckPicker$9$1.<init> at line 474. The source line of the MaterialDialog callback is 475, and the report cites 471-475.
- Shared constant: no ENV_* or STATE_* gate is set on the GUI edges (the add-deck flow needs no storage or network gate).

## 7. Checks

- python3 -I -m py_compile graphs/AnkiDroid/parts/label_006.py: passes.
- python3 -I scratch/c1_check.py on label_006.py and label_006.md: see the final report line (entries 9, rows 22).
- Build (tools/build_graph.py) was not run, as required by the brief.
