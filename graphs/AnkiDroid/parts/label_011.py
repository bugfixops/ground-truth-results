# AnkiDroid batch 011 (LABEL helper). CardBrowser part 3: the second-column spinner listener CardBrowser$6, the card-row
# click and long-click listeners CardBrowser$7 and $8, the search expand/collapse listener CardBrowser$9, the list adapter
# CardBrowser$MultiColumnListAdapter and the scroll listener CardBrowser$RenderOnScroll. 22 methods; the full row list is
# in graphs/AnkiDroid/parts/label_011.md.
#
# Ownership: an edge is written in the part that holds its source method. Written here: the REGISTER edges from the
# <init>s of $7, $8, $9 and RenderOnScroll; the page edges into the batch-011 methods (GUI, FRAMEWORK); INTENT and ENTERS
# from CardBrowser$7.onItemClick; ENTERS from CardBrowser$8.onItemLongClick; ASYNC from RenderOnScroll.onScroll and
# onScrollStateChanged to the CardBrowser$17 callbacks (those callbacks are batch 010 rows and are not labelled here).
# Not written here: CardBrowser$6.<init> (listed in batch_010.txt, not in batch_011; see the report); the auto CALL edges
# from CardBrowser.onCollectionLoaded to the <init>s and from CardBrowser.onCreateOptionsMenu to $9.<init> (batch 009
# methods); the auto CALL edges inside the adapter and from the scroll listeners to DeckTask (auto_calls.json); the
# NoteEditor.<init> label (NoteEditor batch); the CardBrowser$17 callbacks (batch 010); the cancelTask calls in
# CardBrowser.onStop and onDestroy (batch 009).
#
# UNREACHABLE entries: CardBrowser$6.onNothingSelected (framework_never_calls) and
# CardBrowser$MultiColumnListAdapter.getItem (no_trigger_in_app). Constants: none.
# Missing gates are text only, in note= (MG55 to MG57); env and needs_state are not set on those edges.

# ---- CardBrowser$6: second-column spinner (set up in CardBrowser.onCollectionLoaded, CardBrowser.java:439-462) ----

e('S_CARDBROWSER', 'CardBrowser$6.onItemSelected', 'FRAMEWORK',
  'the card browser opens: the framework lays out the second-column spinner and selects position 0, which fires onItemSelected',
  env=None,
  evidence='FW-SRC core/java/android/widget/AdapterView.java:1034-1085, 937-947, 1103-1110; FW-SRC core/java/android/widget/Spinner.java:637-648, 681; SRC com/ichi2/anki/CardBrowser.java:437-457, 482',
  note='Page edge. The default selection (position 0) is set in AbsSpinner, which is not in fw_src: INFERRED for that step. The listener is attached after setAdapter (CardBrowser.java:443, 445). The saved index is read at line 437 and applied with setSelection at line 482, after the listener is attached and before the first layout, so the first callback should report the saved index and not overwrite it (not tested). The GUI edge below is the other route.')

e('S_CARDBROWSER', 'CardBrowser$6.onItemSelected', 'GUI',
  'pick another second column in the card browser column spinner',
  gui=['pick another second column in the card browser column spinner'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:445-457; SRC res/layout/card_browser.xml:32-37',
  note='Page edge. The spinner has no visibility gate: the layout sets none (card_browser.xml:32-37) and the code looks the spinner up only at CardBrowser.java:439.')

UNREACHABLE['CardBrowser$6.onNothingSelected'] = (
    'framework_never_calls',
    "The second-column spinner is filled from ArrayAdapter.createFromResource over R.array.browser_column2_headings (CardBrowser.java:440-443), a static array of six items (res/values/02-strings.xml:60-66). ArrayAdapter does not override isEnabled, so BaseAdapter.isEnabled (BaseAdapter.java:68) makes every item selectable. AdapterView.handleDataChanged pins the position into range and selects a selectable one (AdapterView.java:1040-1085), so the selection is not cleared while the six items stay. fireOnSelected calls onNothingSelected only for a negative selection (AdapterView.java:937-947). Not read: AbsSpinner (not in fw_src), and the other places that set the selection to INVALID_POSITION (not searched), so confirmed_by is INFERRED. Body is '// Do Nothing' (CardBrowser.java:460-462). Same reasoning as CardBrowser$5.onNothingSelected in label_010.py.",
    'SRC com/ichi2/anki/CardBrowser.java:440-443, 460-462; SRC res/values/02-strings.xml:60-66; FW-SRC core/java/android/widget/ArrayAdapter.java:73, 506; FW-SRC core/java/android/widget/BaseAdapter.java:68; FW-SRC core/java/android/widget/AdapterView.java:937-947, 1040-1085',
    'INFERRED')

UNREACHABLE['CardBrowser$MultiColumnListAdapter.getItem'] = (
    'no_trigger_in_app',
    "The card list gets its row data through getView and bindView, which read the card list directly, not through getItem. The framework reaches ListAdapter.getItem only from AdapterView.getSelectedItem (AdapterView.java:590-594) and AdapterView.getItemAtPosition (AdapterView.java:796-798). A search of the widget and view packages of fw_src finds no caller of either method (only their definitions), and CardBrowser.java has no call to getItem on this adapter (the only getItem( in the file is the definition at line 1295). No code in the app or the framework asks this list for an item, so no route reaches the method.",
    'SRC com/ichi2/anki/CardBrowser.java:477, 1295-1297; FW-SRC core/java/android/widget/AdapterView.java:590-594, 796-798',
    'SOURCE')

# ---- CardBrowser$7: card-row click (listener set in CardBrowser.onCollectionLoaded, CardBrowser.java:485-497) ----

e('CardBrowser$7.<init>', 'CardBrowser$7.onItemClick', 'REGISTER',
  'the card-row click listener is set on the card list',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:485-486',
  note='onItemClick is in this part. The builder does not follow REGISTER for reachability; the route is the S_CARDBROWSER -> CardBrowser$7.onItemClick GUI edge below. The <init> is called from CardBrowser.onCollectionLoaded (auto CALL, CardBrowser.java:485).')

e('S_CARDBROWSER', 'CardBrowser$7.onItemClick', 'GUI',
  'tap a card row in the card browser list',
  gui=['tap a card row in the card browser list'],
  needs_state=STATE_CARDS,
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:408, 485-497; FW-SRC core/java/android/widget/AdapterView.java:314-318',
  note='Page edge. The list needs at least one row (STATE_CARDS). The framework calls the listener from AdapterView.performItemClick (line 318).')

e('CardBrowser$7.onItemClick', 'NoteEditor.<init>', 'INTENT',
  'start the note editor for the tapped card: explicit Intent to NoteEditor with the caller and the card id as extras',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:493-496',
  note='INTENT edge (explicit component, app to app; no framework gate). NoteEditor.<init> is labelled in the NoteEditor batch. The result returns through the RESULT edge S_NOTEEDITOR -> CardBrowser.onActivityResult (graph_def.py:1566).')

e('CardBrowser$7.onItemClick', 'S_NOTEEDITOR', 'ENTERS',
  'the note editor screen is shown for the tapped card',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:493-496',
  note='ENTERS edge: method to page, the same pattern as CardBrowser.onOptionsItemSelected -> S_NOTEEDITOR (graph_def.py:1539).')

# ---- CardBrowser$8: card-row long-click (listener set in CardBrowser.onCollectionLoaded, CardBrowser.java:499-512) ----

e('CardBrowser$8.<init>', 'CardBrowser$8.onItemLongClick', 'REGISTER',
  'the card-row long-click listener is set on the card list',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:499-500',
  note='onItemLongClick is in this part. The builder does not follow REGISTER for reachability; the route is the S_CARDBROWSER -> CardBrowser$8.onItemLongClick GUI edge below. The <init> is called from CardBrowser.onCollectionLoaded (auto CALL, CardBrowser.java:499).')

e('S_CARDBROWSER', 'CardBrowser$8.onItemLongClick', 'GUI',
  'long-press a card row in the card browser list',
  gui=['long-press a card row in the card browser list'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:499-511, 1087-1091; FW-SRC core/java/android/widget/AbsListView.java:3223-3237',
  note='Page edge. MISSING GATE MG55: the Q&A render task of the card list (DeckTask.TASK_TYPE_RENDER_BROWSER_QA) is said to block the long-click callback while it runs (comment at CardBrowser.java:1088-1089); no gate kind expresses a running background task. A row must exist.')

e('CardBrowser$8.onItemLongClick', 'S_DLG_CARDBROWSER_CONTEXT', 'ENTERS',
  'the card menu dialog is shown for the long-pressed card',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:501-511',
  note='ENTERS edge: method to page. The dialog listener CardBrowser$1.onSelection is batch 009 (its GUI edge is graph_def.py:1559).')

# ---- CardBrowser$9: search expand and collapse (listener set in CardBrowser.onCreateOptionsMenu, CardBrowser.java:579-594) ----

e('CardBrowser$9.<init>', 'CardBrowser$9.onMenuItemActionExpand', 'REGISTER',
  'the search expand and collapse listener is set on the search menu item',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:579-580',
  note='onMenuItemActionExpand is in this part. The builder does not follow REGISTER for reachability; the route is the S_CARDBROWSER -> CardBrowser$9.onMenuItemActionExpand GUI edge below. The <init> is called from CardBrowser.onCreateOptionsMenu (auto CALL, CardBrowser.java:580; batch 009).')

e('CardBrowser$9.<init>', 'CardBrowser$9.onMenuItemActionCollapse', 'REGISTER',
  'the search expand and collapse listener is set on the search menu item',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:579-580',
  note='onMenuItemActionCollapse is in this part. The builder does not follow REGISTER for reachability; the route is the S_CARDBROWSER -> CardBrowser$9.onMenuItemActionCollapse GUI edge below. The <init> is called from CardBrowser.onCreateOptionsMenu (auto CALL, CardBrowser.java:580; batch 009).')

e('S_CARDBROWSER', 'CardBrowser$9.onMenuItemActionExpand', 'GUI',
  'tap the search icon in the card browser action bar (the search view expands)',
  gui=['tap the search icon in the card browser action bar (the search view expands)'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:579-584; SRC res/menu/card_browser.xml:9-14; FW-SRC core/java/com/android/internal/view/menu/MenuItemImpl.java:749-758',
  note='Page edge. MenuItemImpl.expandActionView calls the listener (lines 754-755) before it expands the view. The step from the tap to expandActionView is INFERRED (the ActionBar and support-library code is not in the dataset).')

e('S_CARDBROWSER', 'CardBrowser$9.onMenuItemActionCollapse', 'GUI',
  'close the expanded search view of the card browser (the search view collapses)',
  gui=['close the expanded search view of the card browser (the search view collapses)'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:587-594; FW-SRC core/java/com/android/internal/view/menu/MenuItemImpl.java:763-773',
  note='Page edge. MenuItemImpl.collapseActionView calls the listener (lines 772-773). Which control calls collapseActionView (the SearchView close control in the support library) is INFERRED. The listener calls searchCards (auto CALL, CardBrowser.java:592; batch 009).')

# ---- CardBrowser$RenderOnScroll: scroll listener (set in CardBrowser.onCollectionLoaded, CardBrowser.java:479) ----

e('CardBrowser$RenderOnScroll.<init>', 'CardBrowser$RenderOnScroll.onScroll', 'REGISTER',
  'the render-on-scroll listener is set on the card list',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:479',
  note='onScroll is in this part. The builder does not follow REGISTER for reachability; the route is the S_CARDBROWSER -> CardBrowser$RenderOnScroll.onScroll GUI edge below. The <init> is called from CardBrowser.onCollectionLoaded (auto CALL, CardBrowser.java:479).')

e('CardBrowser$RenderOnScroll.<init>', 'CardBrowser$RenderOnScroll.onScrollStateChanged', 'REGISTER',
  'the render-on-scroll listener is set on the card list',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:479',
  note='onScrollStateChanged is in this part. The builder does not follow REGISTER for reachability; the route is the S_CARDBROWSER -> CardBrowser$RenderOnScroll.onScrollStateChanged GUI edge below. The <init> is called from CardBrowser.onCollectionLoaded (auto CALL, CardBrowser.java:479).')

e('S_CARDBROWSER', 'CardBrowser$RenderOnScroll.onScroll', 'GUI',
  'scroll the card list: rows whose question and answer are not rendered yet get them rendered',
  gui=['scroll the card list: rows whose question and answer are not rendered yet get them rendered'],
  env=None,
  evidence='FW-SRC core/java/android/widget/AbsListView.java:1471-1477; SRC com/ichi2/anki/CardBrowser.java:1141-1161',
  note='Page edge. MISSING GATE MG56: the render branch needs a visible row whose answer is empty and a list longer than its last visible row (CardBrowser.java:1145-1149; a data state with no kind). MISSING GATE MG57: the render starts only when 300 ms have passed since the last render, or the last visible row is the last row (CardBrowser.java:1153; timing, no kind).')

e('S_CARDBROWSER', 'CardBrowser$RenderOnScroll.onScrollStateChanged', 'GUI',
  'scroll the card list and let it come to rest (the scroll state becomes idle)',
  gui=['scroll the card list and let it come to rest (the scroll state becomes idle)'],
  env=None,
  evidence='FW-SRC core/java/android/widget/AbsListView.java:4548-4555; SRC com/ichi2/anki/CardBrowser.java:1164-1173',
  note='Page edge. The framework reports the idle state through AbsListView.reportScrollStateChange (4548-4555) when a drag or fling ends. Only SCROLL_STATE_IDLE (CardBrowser.java:1167) starts a render; there is no other gate.')

# ASYNC edges from the two launchers to the CardBrowser$17 callbacks (batch 010 rows).

e('CardBrowser$RenderOnScroll.onScroll', 'CardBrowser$17.onPreExecute', 'ASYNC',
  'the render task starts on the UI thread: DeckTask.launchDeckTask executes it',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:1155-1157, 1095-1098; SRC com/ichi2/async/DeckTask.java:129-134, 344-346',
  note='Launch at CardBrowser.java:1156-1157, reached only when MG56 and MG57 hold. The target callback is a batch 010 row (CardBrowser$17.onPreExecute).')

e('CardBrowser$RenderOnScroll.onScroll', 'CardBrowser$17.onProgressUpdate', 'ASYNC',
  'a card is rendered and the progress update reaches the render listener, which redraws the list',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:654-660, 352-354; SRC com/ichi2/anki/CardBrowser.java:1087-1091',
  note='DeckTask publishes progress only for a card it renders (DeckTask.java:659), so the loop must find an empty answer in the requested range. The target is a batch 010 row.')

e('CardBrowser$RenderOnScroll.onScroll', 'CardBrowser$17.onPostExecute', 'ASYNC',
  'the render task finishes without cancellation: the list is redrawn and the progress bar is hidden',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:129-134, 360-362, 639-669; SRC com/ichi2/anki/CardBrowser.java:1101-1110; FW-SRC core/java/android/os/AsyncTask.java:691-696',
  note='The task ends with a non-null TaskData (DeckTask.java:639-669), so the success branch runs. The target is a batch 010 row.')

e('CardBrowser$RenderOnScroll.onScroll', 'CardBrowser$17.onCancelled', 'ASYNC',
  'the render task started before this scroll is cancelled when the user scrolls again',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:1155; SRC com/ichi2/async/DeckTask.java:168-175, 181-186, 368-370; FW-SRC core/java/android/os/AsyncTask.java:525-527, 691-696',
  note='The cancel at CardBrowser.java:1155 cancels the latest DeckTask only when its type is RENDER_BROWSER_QA (DeckTask.java:181-186): it cancels the task launched earlier, not the one this call launches. AsyncTask.finish calls onCancelled instead of onPostExecute (AsyncTask.java:692-695). The target is a batch 010 row.')

e('CardBrowser$RenderOnScroll.onScrollStateChanged', 'CardBrowser$17.onPreExecute', 'ASYNC',
  'the idle-state render task starts on the UI thread',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:1167-1171, 1095-1098; SRC com/ichi2/async/DeckTask.java:129-134, 344-346',
  note='Launch at CardBrowser.java:1170, always under SCROLL_STATE_IDLE. Its cancel is in a later onScroll (edge above), so no onCancelled edge is written from this method. The target is a batch 010 row.')

e('CardBrowser$RenderOnScroll.onScrollStateChanged', 'CardBrowser$17.onProgressUpdate', 'ASYNC',
  'a card is rendered and the progress update reaches the render listener, which redraws the list',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:654-660, 352-354; SRC com/ichi2/anki/CardBrowser.java:1087-1091',
  note='DeckTask publishes progress only for a card it renders (DeckTask.java:659). The target is a batch 010 row.')

e('CardBrowser$RenderOnScroll.onScrollStateChanged', 'CardBrowser$17.onPostExecute', 'ASYNC',
  'the idle-state render task finishes without cancellation: the list is redrawn and the progress bar is hidden',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:129-134, 360-362, 639-669; SRC com/ichi2/anki/CardBrowser.java:1101-1110; FW-SRC core/java/android/os/AsyncTask.java:691-696',
  note='The task ends with a non-null TaskData (DeckTask.java:639-669), so the success branch runs. The target is a batch 010 row.')

# ---- CardBrowser$MultiColumnListAdapter: edges into the adapter from the page (framework calls) ----
# The other adapter methods (bindView, getColor, setFont, setFromMapping, getFromMapping) are reached through auto CALL
# edges from app methods (auto_calls.json) and have no entry here.

e('S_CARDBROWSER', 'CardBrowser$MultiColumnListAdapter.getView', 'FRAMEWORK',
  'the framework draws the card rows: the list asks the adapter for the view of each visible row',
  needs_state=STATE_CARDS,
  env=None,
  evidence='FW-SRC core/java/android/widget/AbsListView.java:2335-2365; SRC com/ichi2/anki/CardBrowser.java:1201-1215',
  note='Page edge. The framework calls getView from AbsListView.obtainView (lines 2348 and 2365). No row is drawn for an empty list (STATE_CARDS). getView calls bindView (auto CALL, CardBrowser.java:1215).')

e('S_CARDBROWSER', 'CardBrowser$MultiColumnListAdapter.getCount', 'FRAMEWORK',
  'the framework reads the row count when the card list is set up and measured',
  env=None,
  evidence='FW-SRC core/java/android/widget/ListView.java:552-575, 1269-1282; SRC com/ichi2/anki/CardBrowser.java:477, 1288-1291',
  note='Page edge. ListView.setAdapter (line 575, called at CardBrowser.java:477) and onMeasure (line 1282) read the count. The count is 0 for an empty list, so there is no state gate.')

e('S_CARDBROWSER', 'CardBrowser$MultiColumnListAdapter.getItemId', 'FRAMEWORK',
  'the framework reads the id of a row when the user taps it or long-presses it',
  needs_state=STATE_CARDS,
  env=None,
  evidence='FW-SRC core/java/android/widget/AbsListView.java:3108-3128, 3133-3149; FW-SRC core/java/android/widget/BaseAdapter.java:35-37; SRC com/ichi2/anki/CardBrowser.java:1300-1303',
  note='Page edge. PerformClick.run calls adapter.getItemId for the tapped row (AbsListView.java:3127) and CheckForLongPress.run for the long-pressed row (AbsListView.java:3149). The body returns the position. Needs at least one row (STATE_CARDS). AbsListView.setItemViewLayoutParams (AbsListView.java:2413-2414) also calls getItemId, but only when the adapter has stable ids; MultiColumnListAdapter inherits hasStableIds() = false (BaseAdapter.java:35-37), so that path is not a route here.')
