# ================================================================== batch 142 (label_142): com.money.manager.ex.view.recycler (ContextMenuRecyclerView, CursorRecyclerViewAdapter, DividerItemDecoration, RecyclerViewContextMenuInfo; 26 methods)
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_142.md (0 REACHABLE, 26 UNREACHABLE, 0 INCOMPLETE).
# Grep, query and printed-line evidence: graphs/MMEX/parts/label_142.grep.txt (sections S1, S3, S4, S5, S6, S7).
# This file writes 0 e() edges, 0 gui() edges, 26 UNREACHABLE entries and 6 sup pairs.
# Edges are written only for destinations owned by this batch (D1). The batch has no REACHABLE route, so no e() edge is needed.
# The sup pairs cut the six auto CALL records from UNREACHABLE batch-142 callers into UNREACHABLE batch-142 targets (D14(a)). The two batch-050 records into DividerItemDecoration are already cut in graph_def.py:4057 and 4060 and are not repeated here.
# Library and framework dispatch (androidx RecyclerView.Adapter and ItemDecoration callbacks, android.database.DataSetObserver) was not read; no label relies on it, and each such row says so.
# Evidence labels: SRC = printed line of the source tree; FW-SRC = printed line of fw_src/android-8.1.0_r1; INFERRED = a step whose source was not read.

# ---- ContextMenuRecyclerView (never constructed: its only XML use is in a fragment that is never created)

UNREACHABLE['ContextMenuRecyclerView.<init>(Context)'] = (
  'no_trigger_in_app',
  'No new ContextMenuRecyclerView( in app/src. LayoutInflater looks up the (Context,AttributeSet) constructor for the XML tag, not this one. The tag is inflated only by CurrencyRecyclerListFragment.onCreateView, which never runs because the fragment is never created (CurrencyRecyclerListActivity is never started).',
  'label_142.grep.txt S1 (no new ContextMenuRecyclerView); S4 ContextMenuRecyclerView.java:44-46; S4 layout fragment_currency_recycler_list.xml:28; S4 CurrencyRecyclerListFragment.java:99; S4 CurrencyRecyclerListActivity.java:41; S4 AndroidManifest.xml:359 (no intent-filter); S4 MainActivity.java:644 (commented out); S3 FW-SRC LayoutInflater.java:90-91, 615',
  'SOURCE')

UNREACHABLE['ContextMenuRecyclerView.<init>(Context,AttributeSet)'] = (
  'no_trigger_in_app',
  'LayoutInflater calls this constructor for XML tag fragment_currency_recycler_list.xml:28. That XML is inflated only in CurrencyRecyclerListFragment.onCreateView (line 99), which never runs because the fragment is never created (the activity is never started).',
  'label_142.grep.txt S4 ContextMenuRecyclerView.java:40-42; S4 layout xml:28; S4 CurrencyRecyclerListFragment.java:99; S4 CurrencyRecyclerListActivity.java:41; S4 AndroidManifest.xml:359; S4 MainActivity.java:644; S3 FW-SRC LayoutInflater.java:90-91, 615',
  'SOURCE')

UNREACHABLE['ContextMenuRecyclerView.<init>(Context,AttributeSet,int)'] = (
  'no_trigger_in_app',
  'No caller at all. No new site in app/src, and LayoutInflater looks up only the (Context,AttributeSet) constructor. The class is only used from the XML tag, which is never inflated.',
  'label_142.grep.txt S1 (no new ContextMenuRecyclerView); S4 ContextMenuRecyclerView.java:36-38; S3 FW-SRC LayoutInflater.java:90-91, 615; activity and fragment chain as in the first entry',
  'SOURCE')

UNREACHABLE['ContextMenuRecyclerView.getContextMenuInfo'] = (
  'no_trigger_in_app',
  'Overrides View.getContextMenuInfo (FW-SRC View.java:12610), which View.createContextMenu calls at 12579. No ContextMenuRecyclerView instance exists (the fragment chain above), so no context menu is built on it.',
  'label_142.grep.txt S4 ContextMenuRecyclerView.java:48-50; S3 FW-SRC View.java:12578-12579, 12610; S4 CurrencyRecyclerListFragment.java:99; S4 CurrencyRecyclerListActivity.java:41',
  'SOURCE')

UNREACHABLE['ContextMenuRecyclerView.showContextMenuForChild'] = (
  'no_trigger_in_app',
  'Overrides ViewGroup.showContextMenuForChild(View) (FW-SRC ViewGroup.java:860, parent recursion at 866). No ContextMenuRecyclerView instance exists (the fragment chain above). Its auto CALL to RecyclerViewContextMenuInfo.<init> (line 58) is internal to batch 142 and is cut by a sup below.',
  'label_142.grep.txt S4 ContextMenuRecyclerView.java:53-61 (new RecyclerViewContextMenuInfo at 58); S3 FW-SRC ViewGroup.java:859-860, 866; S5 record ContextMenuRecyclerView.java:58 exact',
  'SOURCE')

# ---- CursorRecyclerViewAdapter (abstract; no subclass and no instance in app/src)

UNREACHABLE['CursorRecyclerViewAdapter.<init>'] = (
  'no_trigger_in_app',
  'The class is abstract, has no subclass, and has no new site in app/src. No file outside its own names the type or wildcard-imports the package, so no adapter instance is built. Its auto CALL to NotifyingDataSetObserver.<init> (line 40) is internal and cut by a sup below.',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:27-28, 36-44; S1; S5 record CursorRecyclerViewAdapter.java:40 exact; S6 (package listing and no outside mention)',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter.changeCursor'] = (
  'no_trigger_in_app',
  'Public method of an abstract class with no instance. The in-tree changeCursor calls are on other adapter types in other packages, which cannot be CursorRecyclerViewAdapter because no file outside its own names it. Its auto CALL to swapCursor (line 100) is internal and cut by a sup below.',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:99-104; S5 record line 100 exact; S6 (changeCursor call sites and package check)',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter.getContext'] = (
  'no_trigger_in_app',
  'No adapter instance exists (see CursorRecyclerViewAdapter.<init>). mContext is set only in onCreateViewHolder (line 79), which never runs.',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:46-48, 79; S1; S6',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter.getCursor'] = (
  'no_trigger_in_app',
  'No adapter instance exists (see CursorRecyclerViewAdapter.<init>).',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:50-52; S1; S6',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter.getItemCount'] = (
  'no_trigger_in_app',
  'Overrides RecyclerView.Adapter.getItemCount (androidx source not read; not relied on). No adapter instance exists (see CursorRecyclerViewAdapter.<init>).',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:54-60; S5 framework_calls (Cursor.getCount); S1; S6',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter.getItemId'] = (
  'no_trigger_in_app',
  'Overrides RecyclerView.Adapter.getItemId (androidx source not read; not relied on). No adapter instance exists (see CursorRecyclerViewAdapter.<init>).',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:62-68; S5 framework_calls (Cursor.moveToPosition, Cursor.getLong); S1; S6',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter.onBindViewHolder'] = (
  'no_trigger_in_app',
  'Overrides RecyclerView.Adapter.onBindViewHolder (androidx source not read; not relied on). No adapter instance exists (see CursorRecyclerViewAdapter.<init>). Its call at line 92 goes to the abstract onBindViewHolder(VH,Cursor), which has no code (line 75).',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:75, 84-93; S5 framework_calls (Cursor.moveToPosition); S1; S6',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter.onCreateViewHolder'] = (
  'no_trigger_in_app',
  'Overrides RecyclerView.Adapter.onCreateViewHolder (androidx source not read; not relied on). No adapter instance exists (see CursorRecyclerViewAdapter.<init>). The body (lines 79-81) would only set mContext and return null.',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:77-82; S5 framework_calls (ViewGroup.getContext); S1; S6',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter.setHasStableIds'] = (
  'no_trigger_in_app',
  'No adapter instance exists (see CursorRecyclerViewAdapter.<init>). The body ignores its argument and passes true to super (line 72).',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:70-73; S5 framework_calls (RecyclerView$Adapter.setHasStableIds); S1; S6',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter.swapCursor'] = (
  'no_trigger_in_app',
  'Called in-tree only from changeCursor (line 100), which is itself unreached. No adapter instance exists (see CursorRecyclerViewAdapter.<init>). The auto record from changeCursor is cut by a sup below.',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:111-134 (registerDataSetObserver at 122; notifyDataSetChanged at 126 and 130); S5 record line 100 exact; S6',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter$NotifyingDataSetObserver.<init>'] = (
  'no_trigger_in_app',
  'Implicit constructor of a private inner class (no declared constructor). Its only construction is in the outer constructor at line 40, which never runs (no adapter instance). Its auto CALL from line 40 is cut by a sup below.',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:36-44 (new at 40), 136-137; S5 record line 40 exact; S6',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter$NotifyingDataSetObserver.onChanged'] = (
  'no_trigger_in_app',
  'No observer is ever registered. Observers are registered only at lines 42 and 122, on an adapter that is never built. Overrides android.database.DataSetObserver.onChanged, whose source is not in fw_src (source not read; not relied on).',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:139-144 (method at 140), 42, 122; S3 (DataSetObserver.java not present in fw_src); S5 framework_calls',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter$NotifyingDataSetObserver.onInvalidated'] = (
  'no_trigger_in_app',
  'Same as onChanged: no observer is ever registered, because the adapter is never built. DataSetObserver source not read; not relied on.',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:146-152 (method at 147), 42, 122; S3; S5 framework_calls',
  'SOURCE')

# ---- DividerItemDecoration (constructed only in CurrencyRecyclerListFragment.java:366, which never runs)

UNREACHABLE['DividerItemDecoration.<clinit>'] = (
  'no_trigger_in_app',
  'The class is initialized on first active use (JVM class initialization). Its only use in app/src is new DividerItemDecoration at CurrencyRecyclerListFragment.java:366, in code that never runs. The batch 050 auto CALL from initializeList is cut in graph_def.py:4057.',
  'label_142.grep.txt S4 DividerItemDecoration.java:31-36; S4 CurrencyRecyclerListFragment.java:366; S1; S5 record (batch 050 caller, cut at graph_def.py:4057); S4 CurrencyRecyclerListActivity.java:41',
  'SOURCE')

UNREACHABLE['DividerItemDecoration.<init>'] = (
  'no_trigger_in_app',
  'The only construction is CurrencyRecyclerListFragment.java:366, in unreached code. Its auto CALL to setOrientation (line 44) is cut by a sup below. The batch 050 CALL from initializeList is cut in graph_def.py:4060.',
  'label_142.grep.txt S4 DividerItemDecoration.java:40-45; S4 CurrencyRecyclerListFragment.java:366; S1; S5 records (line 44 and batch 050 caller); graph_def.py:4060',
  'SOURCE')

UNREACHABLE['DividerItemDecoration.drawHorizontal'] = (
  'no_trigger_in_app',
  'Called in-app only from onDraw (line 57). onDraw has no instance behind it (see DividerItemDecoration.onDraw). The auto CALL from onDraw is cut by a sup below.',
  'label_142.grep.txt S4 DividerItemDecoration.java:53-59, 74-87; S5 record line 57 exact',
  'SOURCE')

UNREACHABLE['DividerItemDecoration.drawVertical'] = (
  'no_trigger_in_app',
  'Called in-app only from onDraw (line 55). onDraw has no instance behind it (see DividerItemDecoration.onDraw). The auto CALL from onDraw is cut by a sup below.',
  'label_142.grep.txt S4 DividerItemDecoration.java:53-59, 60-73; S5 record line 55 exact',
  'SOURCE')

UNREACHABLE['DividerItemDecoration.getItemOffsets'] = (
  'no_trigger_in_app',
  'Overrides RecyclerView.ItemDecoration.getItemOffsets (androidx source not read; not relied on). The only DividerItemDecoration instance would come from the unreached fragment code at CurrencyRecyclerListFragment.java:366.',
  'label_142.grep.txt S4 DividerItemDecoration.java:88-95 (@Override at 88, method 89-95); S4 CurrencyRecyclerListFragment.java:366; S5 framework_calls (Rect.set)',
  'SOURCE')

UNREACHABLE['DividerItemDecoration.onDraw'] = (
  'no_trigger_in_app',
  'Overrides RecyclerView.ItemDecoration.onDraw (androidx source not read; not relied on). No instance exists (see DividerItemDecoration.<init>). Its auto CALLs to drawVertical (line 55) and drawHorizontal (line 57) are internal and cut by sups below.',
  'label_142.grep.txt S4 DividerItemDecoration.java:52-59; S5 records lines 55 and 57 exact',
  'SOURCE')

UNREACHABLE['DividerItemDecoration.setOrientation'] = (
  'no_trigger_in_app',
  'Called in-app only from the constructor (line 44), which is unreached (see DividerItemDecoration.<init>). The auto CALL from line 44 is cut by a sup below. The other setOrientation call in app/src is DateDisplay.java:56 on a LinearLayout, not this class.',
  'label_142.grep.txt S4 DividerItemDecoration.java:46-51, 44; S5 record line 44 exact; S7 (setOrientation call sites)',
  'SOURCE')

# ---- RecyclerViewContextMenuInfo (constructed only by ContextMenuRecyclerView.showContextMenuForChild, which has no instance)

UNREACHABLE['RecyclerViewContextMenuInfo.<init>'] = (
  'no_trigger_in_app',
  'The only construction is ContextMenuRecyclerView.java:58 (auto CALL, internal to batch 142, cut by a sup below). That method has no instance behind it (see ContextMenuRecyclerView.showContextMenuForChild). The casts at CurrencyRecyclerListFragment.java:150 and :163 do not construct the class.',
  'label_142.grep.txt S4 RecyclerViewContextMenuInfo.java:25-31; S4 ContextMenuRecyclerView.java:58; S1 (fragment lines 150 and 163 are casts); S5 record line 58 exact',
  'SOURCE')

# ================================================================== sup cuts (D14a): auto CALL records from UNREACHABLE batch-142 callers into UNREACHABLE batch-142 targets

sup(('ContextMenuRecyclerView.showContextMenuForChild', 'RecyclerViewContextMenuInfo.<init>'),
    ('CursorRecyclerViewAdapter.<init>', 'CursorRecyclerViewAdapter$NotifyingDataSetObserver.<init>'),
    ('CursorRecyclerViewAdapter.changeCursor', 'CursorRecyclerViewAdapter.swapCursor'),
    ('DividerItemDecoration.<init>', 'DividerItemDecoration.setOrientation'),
    ('DividerItemDecoration.onDraw', 'DividerItemDecoration.drawHorizontal'),
    ('DividerItemDecoration.onDraw', 'DividerItemDecoration.drawVertical'))
