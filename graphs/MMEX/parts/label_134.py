# ================================================================== batch 134 (label_134): SplitCategoriesAdapter (with its $1-$4 listeners), SplitItemFactory, SplitItemTouchCallback, SplitItemViewHolder, SplitItemViewHolder_ViewBinding (35 methods)
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_134.md (31 REACHABLE, 4 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence: graphs/MMEX/parts/label_134.grep.txt.
# This file writes 13 e() edges (12 FRAMEWORK, 1 CALL non_standard), 0 gui() edges, 4 UNREACHABLE entries and 1 sup pair.
# Edges are written only for destinations owned by this batch (D1). Every other route is a CALL edge from auto_calls.json (USE_AUTO, D7) and is not written here.
# The route into SplitCategoriesActivity.initRecyclerView (onCreate, batch 133, not merged) is interim (D8); the RecyclerView and touch-helper edges start from initRecyclerView.
# RecyclerView and ItemTouchHelper dispatch is INFERRED: androidx is not in fw_src (label_134.grep.txt Q20, Q27), so those edges cite the setter and attach lines only.
# Listener registrations inside this batch get a FRAMEWORK edge from the registering method to the listener callback (label_131 convention). View.performClick and TextView dispatch are cited from fw_src/android-8.1.0_r1 (Q21, Q22).
# ButterKnife: the generated SplitItemViewHolder_ViewBinding.<init> is built by ButterKnife.bind(this, itemView) by reflection, so one CALL edge with cls='non_standard' is written (label_008 convention).
# onMove and onItemMove are INCOMPLETE and have no edge here: their only route is the androidx ItemTouchHelper drag path, which is not in the repo (Q20, Q27).
# Evidence labels: SRC = printed line of the source tree; FW-SRC = printed line of fw_src/android-8.1.0_r1; INFERRED = a step whose source was not read.

# ---- RecyclerView setup in SplitCategoriesActivity.initRecyclerView (lines 254-274; setAdapter 259, ItemTouchHelper 271-273)

e('SplitCategoriesActivity.initRecyclerView', 'SplitCategoriesAdapter.onCreateViewHolder', 'FRAMEWORK',
  'after setAdapter the RecyclerView asks the adapter to create each row holder through onCreateViewHolder',
  evidence='SRC transactions/SplitCategoriesActivity.java:259 (mRecyclerView.setAdapter(mAdapter)); INFERRED: androidx RecyclerView dispatches onCreateViewHolder (library not in fw_src or the source root, label_134.grep.txt Q20, Q27)')

e('SplitCategoriesActivity.initRecyclerView', 'SplitCategoriesAdapter.onBindViewHolder', 'FRAMEWORK',
  'after setAdapter the RecyclerView binds each visible row through onBindViewHolder',
  evidence='SRC transactions/SplitCategoriesActivity.java:259 (mRecyclerView.setAdapter(mAdapter)); INFERRED: androidx RecyclerView dispatches onBindViewHolder (library not in fw_src or the source root, label_134.grep.txt Q20, Q27)')

e('SplitCategoriesActivity.initRecyclerView', 'SplitCategoriesAdapter.getItemCount', 'FRAMEWORK',
  'after setAdapter the RecyclerView asks the adapter for its row count through getItemCount',
  evidence='SRC transactions/SplitCategoriesActivity.java:259 (mRecyclerView.setAdapter(mAdapter)); INFERRED: androidx RecyclerView calls getItemCount (library not in fw_src or the source root, label_134.grep.txt Q20, Q27)')

e('SplitCategoriesActivity.initRecyclerView', 'SplitItemTouchCallback.getMovementFlags', 'FRAMEWORK',
  'the ItemTouchHelper attached at line 273 asks the callback for the movement flags of a touched row through getMovementFlags',
  evidence='SRC transactions/SplitCategoriesActivity.java:271-273 (new SplitItemTouchCallback, new ItemTouchHelper, attachToRecyclerView); INFERRED: androidx ItemTouchHelper calls Callback.getMovementFlags (library not in fw_src or the source root, label_134.grep.txt Q17, Q20, Q27)')

e('SplitCategoriesActivity.initRecyclerView', 'SplitItemTouchCallback.isItemViewSwipeEnabled', 'FRAMEWORK',
  'the ItemTouchHelper asks the callback whether swipe is enabled for a touched row through isItemViewSwipeEnabled',
  evidence='SRC transactions/SplitCategoriesActivity.java:271-273 (new SplitItemTouchCallback, new ItemTouchHelper, attachToRecyclerView); INFERRED: androidx ItemTouchHelper calls Callback.isItemViewSwipeEnabled (library not in fw_src or the source root, label_134.grep.txt Q17, Q20, Q27)')

e('SplitCategoriesActivity.initRecyclerView', 'SplitItemTouchCallback.onSwiped', 'FRAMEWORK',
  'the ItemTouchHelper calls onSwiped when a swipe to START or END completes',
  evidence='SRC transactions/SplitCategoriesActivity.java:271-273 (new SplitItemTouchCallback, new ItemTouchHelper, attachToRecyclerView); SRC transactions/SplitItemTouchCallback.java:45-47 (swipe flags START | END); INFERRED: androidx ItemTouchHelper calls Callback.onSwiped (library not in fw_src or the source root, label_134.grep.txt Q17, Q20, Q24, Q27)')

# ---- listeners registered in SplitCategoriesAdapter (creation and setter lines in the source; dispatch in fw_src)

e('SplitCategoriesAdapter.initAmountControl', 'SplitCategoriesAdapter$1.onClick', 'FRAMEWORK',
  'a tap on the amount view calls onClick: View.performClick calls the OnClickListener',
  evidence='SRC transactions/SplitCategoriesAdapter.java:161 (viewHolder.txtAmount.setOnClickListener), 161-176 (onClick body); FW-SRC core/java/android/view/View.java:6289-6294 (performClick calls li.mOnClickListener.onClick(this) at 6294); INFERRED: the touch path to performClick is not read (label_134.grep.txt Q21, Q23)')

e('SplitCategoriesAdapter.initCategorySelector', 'SplitCategoriesAdapter$2.onClick', 'FRAMEWORK',
  'a tap on the category view calls onClick: View.performClick calls the OnClickListener',
  evidence='SRC transactions/SplitCategoriesAdapter.java:180 (listener set on the category view), 180-187 (onClick body); FW-SRC core/java/android/view/View.java:6289-6294 (performClick calls the listener at 6294); INFERRED: the touch path to performClick is not read (label_134.grep.txt Q21, Q23)')

e('SplitCategoriesAdapter.initTransactionTypeButton', 'SplitCategoriesAdapter$3.onClick', 'FRAMEWORK',
  'a tap on the transaction type button calls onClick: View.performClick calls the OnClickListener',
  evidence='SRC transactions/SplitCategoriesAdapter.java:191 (listener set on the type button), 191-206 (onClick body; setTransactionType 203; notifyItemChanged 204); FW-SRC core/java/android/view/View.java:6289-6294 (performClick calls the listener at 6294); INFERRED: the touch path to performClick is not read (label_134.grep.txt Q21, Q23)')

e('SplitCategoriesAdapter.initNotesControls', 'SplitCategoriesAdapter$4.beforeTextChanged', 'FRAMEWORK',
  'the framework calls beforeTextChanged before the notes text changes: TextView.sendBeforeTextChanged calls every TextWatcher',
  evidence='SRC transactions/SplitCategoriesAdapter.java:210 (addTextChangedListener), 210-214 (empty beforeTextChanged body); FW-SRC core/java/android/widget/TextView.java:9309-9316 (sendBeforeTextChanged calls list.get(i).beforeTextChanged at 9314); INFERRED: the path from a text change to sendBeforeTextChanged is not read (label_134.grep.txt Q22, Q23)')

e('SplitCategoriesAdapter.initNotesControls', 'SplitCategoriesAdapter$4.onTextChanged', 'FRAMEWORK',
  'the framework calls onTextChanged when the notes text changes: TextView.sendOnTextChanged calls every TextWatcher',
  evidence='SRC transactions/SplitCategoriesAdapter.java:210 (addTextChangedListener), 216-219 (empty onTextChanged body); FW-SRC core/java/android/widget/TextView.java:9359-9366 (sendOnTextChanged calls the watcher at 9364); INFERRED: the path from a text change to sendOnTextChanged is not read (label_134.grep.txt Q22, Q23)')

e('SplitCategoriesAdapter.initNotesControls', 'SplitCategoriesAdapter$4.afterTextChanged', 'FRAMEWORK',
  'the framework calls afterTextChanged after the notes text changes (typing, or setText in bindNotes): TextView.sendAfterTextChanged calls every TextWatcher',
  evidence='SRC transactions/SplitCategoriesAdapter.java:210 (addTextChangedListener), 221-228 (afterTextChanged body; split.setNotes at 226), 131 (setText in bindNotes); FW-SRC core/java/android/widget/TextView.java:9375-9382 (sendAfterTextChanged calls the watcher at 9380); INFERRED: the path from a text change to sendAfterTextChanged is not read (label_134.grep.txt Q22, Q23)')

# ---- generated binding built by ButterKnife (label_008 convention; cls non_standard)

e('SplitItemViewHolder.<init>', 'SplitItemViewHolder_ViewBinding.<init>', 'CALL',
  'ButterKnife.bind(this, itemView) constructs the generated binding for this holder',
  cls='non_standard', via='ButterKnife.bind(this, itemView) (library): the generated SplitItemViewHolder_ViewBinding is constructed by reflection (INFERRED, library and generated source not read)',
  evidence='SRC transactions/SplitItemViewHolder.java:49 (ButterKnife.bind(this, itemView)); label_134.grep.txt Q16 (ButterKnife.bind grep), Q26 E4 (decoded constructor bytecode: invokestatic ButterKnife.bind, then the result is popped); method_list entry SplitItemViewHolder_ViewBinding.<init> (label_134.grep.txt Q14); INFERRED generated class not in the source root')

# ================================================================== UNREACHABLE (batch 134)

UNREACHABLE['SplitItemFactory.<init>'] = ('no_trigger_in_app',
  'SplitItemFactory declares no constructor, so the compiler adds an implicit public no-argument constructor; the class has only the static create method, and nothing creates an instance: no new SplitItemFactory in the source root, and no class file has a Methodref to SplitItemFactory.<init> (label_134.grep.txt Q6, Q7, Q8, Q26 E1)',
  'SRC transactions/SplitItemFactory.java:30-46 (public class, no constructor; static create at 32); label_134.grep.txt Q6, Q7, Q8, Q26 E1',
  'SOURCE')

UNREACHABLE['SplitItemViewHolder_ViewBinding.unbind'] = ('no_trigger_in_app',
  'the Unbinder returned by ButterKnife.bind(this, itemView) is discarded (the decoded bytecode of SplitItemViewHolder.<init> pops it at offset 10, label_134.grep.txt Q26 E4), no app code names unbind (label_134.grep.txt Q15), and no class file has a Methodref to unbind (Q26 E3); the generated class has no outgoing auto_calls.json records (Q1). ButterKnife calling unbind is library behaviour, not read, so this is INFERRED',
  'SRC transactions/SplitItemViewHolder.java:42-50; label_134.grep.txt Q15, Q26 E3, E4, Q1',
  'INFERRED')

UNREACHABLE['SplitItemTouchCallback.onMove'] = ('framework_never_calls',
  'the androidx ItemTouchHelper calls Callback.onMove only while a drag is in progress (INFERRED, library not read); getMovementFlags returns dragFlags = 0, so no drag direction is offered, and no auto_calls.json record reaches onMove (0 incoming)',
  'SRC transactions/SplitItemTouchCallback.java:43 (dragFlags = 0), 47 (swipe flags only), 60-71 (onMove body); label_134.grep.txt Q1, Q17, Q18, Q20, Q27',
  'INFERRED')

UNREACHABLE['SplitCategoriesAdapter.onItemMove'] = ('framework_never_calls',
  'its only caller is SplitItemTouchCallback.onMove (auto CALL record at SplitItemTouchCallback.java:69), which is UNREACHABLE; the body has no statement (every line commented out)',
  'SRC transactions/SplitCategoriesAdapter.java:236-249 (body commented out); transactions/SplitItemTouchCallback.java:69; label_134.grep.txt Q1',
  'INFERRED')

sup(('SplitItemTouchCallback.onMove', 'SplitCategoriesAdapter.onItemMove'))  # D14a: caller UNREACHABLE; auto CALL record at SplitItemTouchCallback.java:69
