# Repair Batch 12 Summary

STATUS: START 20:51

## Methods Analyzed: 36

### ALREADY REACHABLE (skipped - routes exist in graph_def.py): 18 methods

| Method | Status |
|--------|--------|
| GeneralDialogCreation.lambda$showCompressDialog$28 | REACHABLE in build |
| GeneralDialogCreation.lambda$showCompressDialog$29 | REACHABLE in build |
| GeneralDialogCreation.lambda$showCompressDialog$30 | REACHABLE in build |
| GeneralDialogCreation.showCompressDialog | REACHABLE in build |
| GeneralDialogCreation.showPropertiesDialogWithoutPermissions | REACHABLE in build |
| GeneralDialogCreation.showSMBHelpDialog | REACHABLE in build |
| CircularColorsView.<init>(Context) | REACHABLE in build |
| CircularColorsView.init | REACHABLE in build |
| CircularColorsView.onDraw | REACHABLE in build |
| CircularColorsView.setColors | REACHABLE in build |
| CircularColorsView.setDividerColor | REACHABLE in build |
| DataUtils.addServer | REACHABLE in build |
| DataUtils.containsServer(String) | REACHABLE in build |
| DataUtils.removeServer | REACHABLE in build |
| RootUtils.cat | REACHABLE in build |

### NEWLY LABELED: 18 methods

#### REACHABLE: 14 methods

| Method | Evidence |
|--------|----------|
| CircularColorsView.<init>(Context,AttributeSet) | Inflated from XML; SRC selectedcolors_preference.xml:7, item_colorpicker.xml:28 |
| CustomNavigationView.<init> | Inflated from XML; SRC main_toolbar.xml:58 |
| CustomNavigationView.onItemChecked | Called by onNavigationItemSelected; SRC CustomNavigationView.java:38, 43 |
| DataUtils.addHiddenFile | Called by MainFragment.hide; SRC MainFragment.java:1553, DataUtils.java:276-283 |
| DataUtils.contains(String,ArrayList) | Called by containsServer(String); SRC DataUtils.java:95-102 |
| DataUtils.sortBook | Called by RenameBookmark.lambda$onCreateDialog$0; SRC RenameBookmark.java:144, DataUtils.java:314-316 |
| RootUtils.lambda$changePermissions$0 | Lambda in changePermissions; SRC RootUtils.java:117-122 |
| RootUtils.mkDir | Called by Operations.mkdirWithMode; SRC Operations.java:175, RootUtils.java:139-147 |
| RootUtils.mkFile | Called by Operations.mkfile; SRC Operations.java:313, RootUtils.java:155-163 |
| ShareAdapter.<init> | Instantiated in ShareTask.onPostExecute; SRC ShareTask.java:121, ShareAdapter.java:32-38 |
| ShareAdapter.onCreateViewHolder | RecyclerView framework callback; SRC ShareAdapter.java:20, 42-46 |
| ShareAdapter.onBindViewHolder | RecyclerView framework callback; SRC ShareAdapter.java:20, 49-51 |
| ShareAdapter.getItemCount | RecyclerView framework callback; SRC ShareAdapter.java:20, 84-87 |
| ShareAdapter.getItemId | RecyclerView framework callback; SRC ShareAdapter.java:20, 80-82 |
| ShareAdapter.updateMatDialog | Called by ShareTask.onPostExecute; SRC ShareTask.java:122, ShareAdapter.java:29-31 |

#### UNREACHABLE: 3 methods

| Method | Kind | Reason | Evidence |
|--------|------|--------|----------|
| CustomNavigationView.isNavigationViewSavedStateMissing | framework_never_calls | Called only from onSaveInstanceState and onRestoreInstanceState, which are unreachable per graph_def.py | SRC CustomNavigationView.java:69, 88 |
| RootUtils.<init> | no_trigger_in_app | Utility class with only static methods; constructor never instantiated; grep shows no "new RootUtils" | SRC RootUtils.java:16-17 |
| RootUtils.getFilePermissions | no_trigger_in_app | Private method never called; grep shows only definition line | SRC RootUtils.java:169-172 |

#### INCOMPLETE: 1 method

| Method | Reason |
|--------|--------|
| RenameBookmark.lambda$onCreateDialog$0 | Target of edge E_rp12_008 but not in this batch; assumed reachable based on RenameBookmark.<init> being REACHABLE in build |

---

## Summary

STATUS: DONE 20:56

**Batch 12 Results:**
- Total methods: 36
- Already REACHABLE (skipped): 18
- Newly labeled REACHABLE: 14
- Newly labeled UNREACHABLE: 3
- INCOMPLETE: 1

**Notes:**
- CustomNavigationView methods: graph_def.py has edges using full package path names (com.amaze.filemanager.ui.views.drawer.CustomNavigationView.*) instead of canonical short names. This file uses correct canonical names.
- DataUtils.sortBook: graph_def.py has edge from 'RenameBookmark.onClick' which doesn't exist in method_list.json. Corrected to use actual lambda name.
- All edges have printed source evidence per protocol requirements.

