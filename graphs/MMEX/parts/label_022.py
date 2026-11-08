# batch 022 (label_022): com.money.manager.ex.common.AllDataMultiChoiceModeListener (7 methods: <init>, setListener, onPrepareActionMode, onDestroyActionMode, onCreateActionMode, onActionItemClicked, onItemCheckedStateChanged); rows and printed lines: graphs/MMEX/parts/label_022.md.
# The list is shown on page S_ACCOUNT_TRANSACTIONS, defined in label_010.py (AccountTransactionListFragment hosts AllDataListFragment), so no page is defined here and no SCREENS entry is added.
# CALL edges come from auto_calls.json (the constructor and setListener from AllDataListFragment.onActivityCreated, onDestroyActionMode from AllDataListFragment.onDestroy, and the listener's calls back into the fragment), so none are written here.
# ActionMode and the action-bar callbacks are not in fw_src, so the framework steps that go beyond the printed AbsListView code are INFERRED. grep evidence: graphs/MMEX/parts/label_022.grep.txt.

# ---- the selection action mode (the list is a multi-choice modal list: AllDataListFragment.java:154-155)

# long-press a row: in multi-choice modal mode AbsListView takes over the long press, starts the action mode through its wrapper (which forwards onCreateActionMode to this listener), and checks the pressed row
gui('S_ACCOUNT_TRANSACTIONS', 'AllDataMultiChoiceModeListener.onCreateActionMode', 'Long-press a transaction row to start multi-select mode',
  evidence='SRC common/AllDataListFragment.java:154-155 (CHOICE_MODE_MULTIPLE_MODAL and the listener); FW-SRC core/java/android/widget/AbsListView.java:1218-1220 (setChoiceMode makes the list long-clickable), 3226-3229 (performLongPress starts the action mode at 3228), 6454-6458 (wrapper forwards onCreateActionMode to this listener and returns true); the long-press gesture step is INFERRED (source not read)')

# tap a row while the mode is on: performItemClick hands the check change to the wrapper, which forwards it to this listener; the long-press that starts the mode also checks its row through setItemChecked (line 3229)
gui('S_ACCOUNT_TRANSACTIONS', 'AllDataMultiChoiceModeListener.onItemCheckedStateChanged', 'Tap a transaction row while multi-select mode is on (checks or unchecks the row)',
  evidence='FW-SRC core/java/android/widget/AbsListView.java:1130-1132 (performItemClick calls the wrapper while the mode is active), 1068-1071 (setItemChecked calls it), 6489-6491 (wrapper forwards to this listener); SRC common/AllDataListFragment.java:440 (fragment callback that the listener calls at line 104)')

# tap an icon in the action bar of the mode: the framework dispatches the item to this listener; the menu is inflated by the fragment in onMultiChoiceCreated (line 393)
gui('S_ACCOUNT_TRANSACTIONS', 'AllDataMultiChoiceModeListener.onActionItemClicked', 'Tap an icon in the selection action bar (select all, change status, duplicate, delete)',
  evidence='SRC common/AllDataListFragment.java:392-394 (inflates R.menu.menu_all_data_adapter); SRC res/menu/menu_all_data_adapter.xml:23, 29, 35, 41 (the four items); FW-SRC core/java/android/widget/AbsListView.java:6469-6470 (wrapper forwards onActionItemClicked to this listener); INFERRED the action bar dispatches the tap to the callback (ActionMode implementation not in fw_src)')

# ---- batch-internal framework edges (the framework calls the ActionMode callbacks; ActionMode implementation not in fw_src: INFERRED)

e('AllDataMultiChoiceModeListener.onCreateActionMode', 'AllDataMultiChoiceModeListener.onPrepareActionMode', 'FRAMEWORK',
  'after onCreateActionMode returns true the framework prepares the mode, which calls onPrepareActionMode; the mode is invalidated again when the checked count changes (AbsListView line 5510)',
  guard='onCreateActionMode returns true (line 50)',
  evidence='SRC common/AllDataMultiChoiceModeListener.java:48-50; FW-SRC core/java/android/widget/AbsListView.java:6455-6458 (wrapper returns true), 6464-6465 (wrapper forwards prepare), 5509-5510 (invalidate on checked count change); INFERRED ActionMode start and invalidate call the prepare callback (ActionMode implementation not in fw_src)')

e('AllDataMultiChoiceModeListener.onActionItemClicked', 'AllDataMultiChoiceModeListener.onDestroyActionMode', 'FRAMEWORK',
  'a handled item finishes the mode: mode.finish() (line 96) makes the framework call onDestroyActionMode',
  guard='the item was handled: result is true (the cases at lines 71, 75, 79 and 88; menu_select_all keeps the mode open at line 67)',
  evidence='SRC common/AllDataMultiChoiceModeListener.java:95-97; INFERRED ActionMode.finish calls the callback onDestroyActionMode (ActionMode implementation not in fw_src)')

e('AllDataMultiChoiceModeListener.onItemCheckedStateChanged', 'AllDataMultiChoiceModeListener.onDestroyActionMode', 'FRAMEWORK',
  'when the last checked row is unchecked the wrapper finishes the mode, and the framework calls onDestroyActionMode',
  guard='no row is checked after the callback (getCheckedItemCount() is 0, AbsListView line 6494)',
  evidence='FW-SRC core/java/android/widget/AbsListView.java:6491 (wrapper forwards to this listener), 6494-6495 (finish when no row is checked); INFERRED ActionMode.finish calls the callback onDestroyActionMode (ActionMode implementation not in fw_src)')

# ---- auto edge that cannot run: the status case of onActionItemClicked (lines 81-88) needs a menu item with a status id, and menu_all_data_adapter.xml has none (label_022.grep.txt, section C)
sup(('AllDataMultiChoiceModeListener.onActionItemClicked', 'AllDataListFragment.onTransactionStatusClicked'))  # auto_calls.json edge at its record line 37218-37219; batch 020 owns the destination and no other call site exists in the source root (label_022.grep.txt, section B)
