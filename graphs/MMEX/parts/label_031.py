# batch 031 (label_031): com.money.manager.ex.common.CommonSplitCategoryLogic (static utility class, 5 methods) and com.money.manager.ex.common.ExpandableListFragment (21 methods, including the class constructor) with its anonymous listeners $1 and $2 (4 methods). 30 methods in all; rows and printed lines: graphs/MMEX/parts/label_031.md. grep evidence: graphs/MMEX/parts/label_031.grep.txt.
# ExpandableListFragment extends androidx Fragment (ExpandableListFragment.java:48-49). androidx is not in fw_src, so the lifecycle claims are INFERRED (library not read). No app code creates an ExpandableListFragment directly (grep.txt section A). Its subclasses are BaseExpandableListFragment (BaseExpandableListFragment.java:46) and CategoryListFragment (CategoryListFragment.java:73, through Base).
# The list is shown on page S_CATEGORY_LIST (graph_def.py:1214). The page is reused here, not redefined (D9).
# CALL edges come from graphs/MMEX/auto_calls.json (D7) and are not written here. grep.txt section C lists every auto record into this batch. The three e() edges and one gui() edge below have no auto record (checked in grep.txt sections C and D).
# No sup() cut is needed: no auto CALL record enters an UNREACHABLE method of this batch. The auto CALL edges that leave the UNREACHABLE bodies (setSelection, getSelectedId, getSelectedPosition, onContentChanged) point to methods that are also reached from other routes.

# ---- fragment lifecycle (androidx Fragment; library not read: INFERRED)

e('BaseExpandableListFragment.onCreate', 'ExpandableListFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate; BaseExpandableListFragment and CategoryListFragment do not override onCreateView (BaseExpandableListFragment.java:114 is commented out), so the inherited body runs',
  evidence='SRC common/BaseExpandableListFragment.java:61-70, 114; SRC common/ExpandableListFragment.java:98-100; SRC common/CategoryListFragment.java:72-73; grep label_031.grep.txt section A; INFERRED androidx Fragment lifecycle (library not read)')

e('BaseExpandableListFragment.onViewCreated', 'ExpandableListFragment.onDestroyView', 'LIFECYCLE',
  'the framework destroys the view after it was created in onViewCreated, when the fragment leaves the screen (the activity finishes or the fragment is removed); no subclass overrides onDestroyView',
  evidence='SRC common/ExpandableListFragment.java:140-144; SRC common/BaseExpandableListFragment.java:224-236; grep label_031.grep.txt section A (onDestroyView lines); precedent graph_def.py:1299 (BudgetDetailFragment.onViewCreated -> onDestroyView); INFERRED androidx Fragment lifecycle (library not read)')

# ---- framework dispatch of the Handler runnable (android.os.Handler is in fw_src)

e('ExpandableListFragment.ensureList', 'ExpandableListFragment$1.run', 'FRAMEWORK',
  'ensureList posts mRequestFocus to mHandler (created at line 56); the Handler dispatches the message callback on the looper of the thread that created it, which runs the runnable when the message reaches the front of the queue',
  evidence='SRC common/ExpandableListFragment.java:56, 58-62, 329; SRC fw_src/android-8.1.0_r1/core/java/android/os/Handler.java:355 (post), 596 (sendMessageDelayed), 97-99 (dispatchMessage calls handleCallback), 789-790 (handleCallback runs message.callback.run()); SRC fw_src/android-8.1.0_r1/core/java/android/os/Looper.java:164 (msg.target.dispatchMessage); INFERRED the fragment is created on the main thread (androidx lifecycle, library not read)')

# ---- user actions on the category list (page S_CATEGORY_LIST)

gui('S_CATEGORY_LIST', 'ExpandableListFragment$2.onItemClick', 'Tap a row of the category list (plain item click)',
  evidence='SRC common/ExpandableListFragment.java:64-68, 321 (ensureList registers the listener); SRC fw_src/android-8.1.0_r1/core/java/android/widget/AdapterView.java:290, 314-318 (performItemClick calls the listener); SRC common/CategoryListFragment.java:662-665, 681 (child and group listeners set in ACTION_PICK mode); INFERRED ExpandableListView is not in fw_src (ListView.java is), so whether a tap on a group or child row reaches this AdapterView listener is not read')

# ---- UNREACHABLE (grep output: graphs/MMEX/parts/label_031.grep.txt sections A, B, C)

UNREACHABLE['CommonSplitCategoryLogic.<init>'] = (
  'no_trigger_in_app',
  'implicit default constructor of a class that has only static methods (CommonSplitCategoryLogic.java:31, no constructor declared). The class is never instantiated: the references in the app source root are import lines, the class declaration and static calls (grep.txt section A), and no subclass exists. No auto record enters <init> (section C). The constructor never runs',
  'SRC common/CommonSplitCategoryLogic.java:31; grep label_031.grep.txt sections A, C',
  'SOURCE')

UNREACHABLE['ExpandableListFragment.getSelectedId'] = (
  'no_trigger_in_app',
  'public method (lines 187-190), a getter for callers. Its name occurs in the app source root only at the declaration and in its body (ExpandableListFragment.java:187, 189), so no app caller exists (grep.txt section A). No auto record enters it (section C). Its body (mList.getSelectedId()) is never reached. Its only outgoing auto record is a CALL to ensureList (section C, line 188), which is not a reason to run it',
  'SRC common/ExpandableListFragment.java:187-190; grep label_031.grep.txt sections A, C',
  'SOURCE')

UNREACHABLE['ExpandableListFragment.getSelectedPosition'] = (
  'no_trigger_in_app',
  'public method (lines 182-185), a getter for callers. Its name occurs in the app source root only at the declaration and in its body (ExpandableListFragment.java:182, 184), so no app caller exists (grep.txt section A). No auto record enters it (section C). Its body (mList.getSelectedPosition()) is never reached. Its only outgoing auto record is a CALL to ensureList (section C, line 183), which is not a reason to run it',
  'SRC common/ExpandableListFragment.java:182-185; grep label_031.grep.txt sections A, C',
  'SOURCE')

UNREACHABLE['ExpandableListFragment.setSelection'] = (
  'no_trigger_in_app',
  'public method (lines 177-180). In the app source root its name occurs at the declaration and body (ExpandableListFragment.java:177, 179) and in spinner and EditText calls. AbsListFragment.setSelection (core/AbsListFragment.java:124) belongs to another class hierarchy: this fragment extends androidx Fragment (lines 48-49). No caller on an ExpandableListFragment receiver and no auto record enters it (grep.txt sections A, C)',
  'SRC common/ExpandableListFragment.java:48-49, 177-180; SRC core/AbsListFragment.java:124; grep label_031.grep.txt sections A, C',
  'SOURCE')

UNREACHABLE['ExpandableListFragment.onChildClick'] = (
  'no_trigger_in_app',
  'public @Override (lines 344-348) of OnChildClickListener, returns false. The fragment becomes the child listener only in onContentChanged (line 364), and onContentChanged has no caller (grep.txt section A). CategoryListFragment sets its own child listener (anonymous class at CategoryListFragment.java:662-665) in ACTION_PICK mode, and no subclass overrides onChildClick. The body never runs',
  'SRC common/ExpandableListFragment.java:344-348, 354-372; SRC common/CategoryListFragment.java:662-665; grep label_031.grep.txt sections A, C; INFERRED the androidx Fragment does not call onContentChanged (library not read)',
  'INFERRED')

UNREACHABLE['ExpandableListFragment.onGroupExpand'] = (
  'no_trigger_in_app',
  'public @Override (lines 332-336), empty TODO body. The fragment becomes the group-expand listener only in onContentChanged (line 365), and onContentChanged has no caller (grep.txt section A). No other class registers this fragment, and no subclass overrides onGroupExpand (HomeFragment.java:724 is an anonymous listener in another class). The body never runs',
  'SRC common/ExpandableListFragment.java:332-336, 354-372; SRC home/HomeFragment.java:724; grep label_031.grep.txt sections A, C; INFERRED the androidx Fragment does not call onContentChanged (library not read)',
  'INFERRED')

UNREACHABLE['ExpandableListFragment.onGroupCollapse'] = (
  'no_trigger_in_app',
  'public @Override (lines 338-342), empty TODO body. The fragment becomes the group-collapse listener only in onContentChanged (line 366), and onContentChanged has no caller (grep.txt section A). No other class registers this fragment, and no subclass overrides onGroupCollapse (HomeFragment.java:712 is an anonymous listener in another class). The body never runs',
  'SRC common/ExpandableListFragment.java:338-342, 354-372; SRC home/HomeFragment.java:712; grep label_031.grep.txt sections A, C; INFERRED the androidx Fragment does not call onContentChanged (library not read)',
  'INFERRED')

UNREACHABLE['ExpandableListFragment.onContentChanged'] = (
  'no_trigger_in_app',
  'public method without @Override (lines 354-372). The app source root has no caller: its only occurrence is the declaration (grep.txt section A). Its body would register this fragment as the child, group-expand and group-collapse listener (lines 364-366) and reset the adapter (line 369). The superclass androidx Fragment is not read, and it is INFERRED that the framework never calls an app method of this name',
  'SRC common/ExpandableListFragment.java:354-372; grep label_031.grep.txt sections A, C; INFERRED androidx Fragment (library not read)',
  'INFERRED')

UNREACHABLE['ExpandableListFragment.onCreateContextMenu'] = (
  'no_trigger_in_app',
  'public @Override (lines 350-352), empty body. The only registration is registerForContextMenu(getExpandableListView()) in CategoryListFragment (CategoryListFragment.java:130). That makes the fragment the list listener (android.app.Fragment.registerForContextMenu sets view.setOnCreateContextMenuListener(this), fw_src Fragment.java:1937-1938; the androidx version is not read). View dispatches to that listener (View.java:12587-12588), and the receiver is a CategoryListFragment, whose override (CategoryListFragment.java:159-178) does not call super (grep.txt section A: the super.onCreateContextMenu lines are in other classes; section C: no auto record). No ExpandableListFragment instance is created directly (section A), so the base body never runs',
  'SRC common/ExpandableListFragment.java:350-352; SRC common/CategoryListFragment.java:130, 159-178; fw_src/android-8.1.0_r1/core/java/android/app/Fragment.java:1937-1938; fw_src/android-8.1.0_r1/core/java/android/view/View.java:12587-12588; grep label_031.grep.txt sections A, C',
  'SOURCE')
