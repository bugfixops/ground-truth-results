# ---- Repair batch 03 (2024-10-28 20:24)
# TextEditorActivity callbacks and RecyclerAdapter methods

# TextEditorActivity lifecycle and callbacks - all reachable through activity lifecycle

# TextEditorActivity implements TextWatcher, registered in onCreate
e('TextEditorActivity.onCreate', 'TextEditorActivity.afterTextChanged', 'FRAMEWORK',
  'TextWatcher.afterTextChanged callback dispatched by EditText when text changes',
  evidence='SRC activities/TextEditorActivity.java:210 mInput.addTextChangedListener(this); ' +
  'INFERRED EditText dispatches to registered TextWatcher (Android SDK source not read)')

e('TextEditorActivity.onCreate', 'TextEditorActivity.beforeTextChanged', 'FRAMEWORK',
  'TextWatcher.beforeTextChanged callback dispatched by EditText before text changes',
  evidence='SRC activities/TextEditorActivity.java:210 mInput.addTextChangedListener(this); ' +
  'INFERRED EditText dispatches to registered TextWatcher (Android SDK source not read)')

e('TextEditorActivity.onCreate', 'TextEditorActivity.onTextChanged', 'FRAMEWORK',
  'TextWatcher.onTextChanged callback dispatched by EditText when text is changing',
  evidence='SRC activities/TextEditorActivity.java:210,181 searchEditText.addTextChangedListener(this); ' +
  'INFERRED EditText dispatches to registered TextWatcher (Android SDK source not read)')

# onBackPressed is Activity lifecycle callback
e('TextEditorActivity.onCreate', 'TextEditorActivity.onBackPressed', 'FRAMEWORK',
  'Activity.onBackPressed called by framework when back button pressed',
  evidence='SRC activities/TextEditorActivity.java:340; ' +
  'INFERRED Activity framework dispatches back button events (Android SDK source not read)')

# onClick is View.OnClickListener callback, registered in onCreate for buttons
e('TextEditorActivity.onCreate', 'TextEditorActivity.onClick', 'FRAMEWORK',
  'View.OnClickListener.onClick callback when search buttons clicked',
  evidence='SRC activities/TextEditorActivity.java:183-185 upButton/downButton/closeButton.setOnClickListener(this); ' +
  'INFERRED View dispatches click events to registered OnClickListener (Android SDK source not read)')

# Options menu callbacks
e('TextEditorActivity.onCreate', 'TextEditorActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'Activity.onCreateOptionsMenu called by framework to create options menu',
  evidence='SRC activities/TextEditorActivity.java:344; ' +
  'INFERRED Activity framework calls onCreateOptionsMenu (Android SDK source not read)')

e('TextEditorActivity.onCreate', 'TextEditorActivity.onPrepareOptionsMenu', 'FRAMEWORK',
  'Activity.onPrepareOptionsMenu called by framework before showing menu',
  evidence='SRC activities/TextEditorActivity.java:349; ' +
  'INFERRED Activity framework calls onPrepareOptionsMenu (Android SDK source not read)')

e('TextEditorActivity.onCreate', 'TextEditorActivity.onOptionsItemSelected', 'FRAMEWORK',
  'Activity.onOptionsItemSelected called by framework when menu item selected',
  evidence='SRC activities/TextEditorActivity.java:355; ' +
  'INFERRED Activity framework calls onOptionsItemSelected (Android SDK source not read)')

# onSaveInstanceState and onDestroy are Activity lifecycle
e('TextEditorActivity.onCreate', 'TextEditorActivity.onSaveInstanceState', 'FRAMEWORK',
  'Activity.onSaveInstanceState called by framework to save state',
  evidence='SRC activities/TextEditorActivity.java:223; ' +
  'INFERRED Activity framework calls onSaveInstanceState before destroying activity (Android SDK source not read)')

e('TextEditorActivity.onCreate', 'TextEditorActivity.onDestroy', 'FRAMEWORK',
  'Activity.onDestroy called by framework when activity is destroyed',
  evidence='SRC activities/TextEditorActivity.java:399; ' +
  'INFERRED Activity framework calls onDestroy (Android SDK source not read)')

# checkUnsavedChanges called from onBackPressed and onOptionsItemSelected
e('TextEditorActivity.onBackPressed', 'TextEditorActivity.checkUnsavedChanges', 'DIRECT',
  'onBackPressed calls checkUnsavedChanges to prompt user if unsaved',
  evidence='SRC activities/TextEditorActivity.java:340')

e('TextEditorActivity.onOptionsItemSelected', 'TextEditorActivity.checkUnsavedChanges', 'DIRECT',
  'onOptionsItemSelected calls checkUnsavedChanges when home button pressed',
  evidence='SRC activities/TextEditorActivity.java:360 case android.R.id.home')

# cleanSpans called from beforeTextChanged and onClick
e('TextEditorActivity.beforeTextChanged', 'TextEditorActivity.cleanSpans', 'DIRECT',
  'beforeTextChanged calls cleanSpans to clear search highlights',
  evidence='SRC activities/TextEditorActivity.java:417')

e('TextEditorActivity.onClick', 'TextEditorActivity.cleanSpans', 'DIRECT',
  'onClick calls cleanSpans when close button pressed',
  evidence='SRC activities/TextEditorActivity.java:588 case R.id.close')

# hideSearchView and revealSearchView called from onOptionsItemSelected
e('TextEditorActivity.onOptionsItemSelected', 'TextEditorActivity.hideSearchView', 'DIRECT',
  'onOptionsItemSelected calls hideSearchView if search is shown',
  evidence='SRC activities/TextEditorActivity.java:389 case R.id.find')

e('TextEditorActivity.onOptionsItemSelected', 'TextEditorActivity.revealSearchView', 'DIRECT',
  'onOptionsItemSelected calls revealSearchView if search is hidden',
  evidence='SRC activities/TextEditorActivity.java:390 case R.id.find')

# saveFile called from onOptionsItemSelected and lambda
e('TextEditorActivity.onOptionsItemSelected', 'TextEditorActivity.saveFile', 'DIRECT',
  'onOptionsItemSelected calls saveFile when save menu item selected',
  evidence='SRC activities/TextEditorActivity.java:364 case R.id.save')

# Lambda callbacks from MaterialDialog in checkUnsavedChanges
e('TextEditorActivity.checkUnsavedChanges', 'TextEditorActivity.lambda$checkUnsavedChanges$0', 'FRAMEWORK',
  'MaterialDialog positive button callback lambda',
  evidence='SRC activities/TextEditorActivity.java:243 .onPositive((dialog, which) -> {...}); ' +
  'INFERRED MaterialDialog dispatches button callbacks (library source not read)')

e('TextEditorActivity.checkUnsavedChanges', 'TextEditorActivity.lambda$checkUnsavedChanges$1', 'FRAMEWORK',
  'MaterialDialog negative button callback lambda',
  evidence='SRC activities/TextEditorActivity.java:248 .onNegative((dialog, which) -> finish()); ' +
  'INFERRED MaterialDialog dispatches button callbacks (library source not read)')

e('TextEditorActivity.lambda$checkUnsavedChanges$0', 'TextEditorActivity.saveFile', 'DIRECT',
  'Positive dialog button lambda calls saveFile then finish',
  evidence='SRC activities/TextEditorActivity.java:243-244')

# Lambda from load method (ReadFileTask callback)
e('TextEditorActivity.load', 'TextEditorActivity.lambda$load$4', 'FRAMEWORK',
  'ReadFileTask result callback lambda',
  evidence='SRC activities/TextEditorActivity.java:291-292 new ReadFileTask(..., (data) -> {...}); ' +
  'INFERRED AsyncTask-like callback pattern (ReadFileTask implementation dispatches callback)')

# Lambda from lambda$load$4 (Snackbar action callback)
e('TextEditorActivity.lambda$load$4', 'TextEditorActivity.lambda$null$3', 'FRAMEWORK',
  'Snackbar action button callback lambda',
  evidence='SRC activities/TextEditorActivity.java:308 snackbar.setAction(..., v -> snackbar.dismiss()); ' +
  'INFERRED Snackbar dispatches action callbacks (Material Components source not read)')

# Lambda from saveFile (WriteFileAbstraction callback)
e('TextEditorActivity.saveFile', 'TextEditorActivity.lambda$saveFile$2', 'FRAMEWORK',
  'WriteFileAbstraction result callback lambda',
  evidence='SRC activities/TextEditorActivity.java:263-264 new WriteFileAbstraction(..., (errorCode) -> {...}); ' +
  'INFERRED AsyncTask-like callback pattern (WriteFileAbstraction implementation dispatches callback)')

# RecyclerAdapter methods

# addItem called from MainFragment.addSearchResult
e('MainFragment.addSearchResult', 'RecyclerAdapter.addItem', 'DIRECT',
  'MainFragment calls addItem to add search result to adapter',
  evidence='SRC fragments/MainFragment.java:1629')

# areAllChecked called from MainFragment$3.onActionItemClicked
e('MainFragment$3.onActionItemClicked', 'RecyclerAdapter.areAllChecked', 'DIRECT',
  'Action mode callback checks if all items with path are checked',
  evidence='SRC fragments/MainFragment.java:691')

# getCorrectView called from RecyclerPreloadSizeProvider
e('RecyclerPreloadSizeProvider.getPreloadSize', 'RecyclerAdapter.getCorrectView', 'DIRECT',
  'Glide preload size provider calls getCorrectView to determine which view type',
  evidence='SRC adapters/glide/RecyclerPreloadSizeProvider.java:56')

# getItemId is RecyclerView.Adapter callback
e('RecyclerAdapter.onCreateViewHolder', 'RecyclerAdapter.getItemId', 'FRAMEWORK',
  'RecyclerView.Adapter.getItemId called by RecyclerView framework',
  evidence='INFERRED RecyclerView framework calls getItemId for stable IDs (androidx source not read)')

# getItemViewType is RecyclerView.Adapter callback, also called from MainFragment$2
e('RecyclerAdapter.onCreateViewHolder', 'RecyclerAdapter.getItemViewType', 'FRAMEWORK',
  'RecyclerView.Adapter.getItemViewType called by RecyclerView framework',
  evidence='INFERRED RecyclerView framework calls getItemViewType (androidx source not read)')

e('MainFragment$2.getSpanSize', 'RecyclerAdapter.getItemViewType', 'DIRECT',
  'GridLayoutManager.SpanSizeLookup calls getItemViewType',
  evidence='SRC fragments/MainFragment.java:345')

# onFailedToRecycleView is RecyclerView.Adapter callback
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.onFailedToRecycleView', 'FRAMEWORK',
  'RecyclerView.Adapter.onFailedToRecycleView called when view recycling fails',
  evidence='INFERRED RecyclerView framework calls onFailedToRecycleView (androidx source not read)')

# onViewAttachedToWindow is RecyclerView.Adapter callback
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.onViewAttachedToWindow', 'FRAMEWORK',
  'RecyclerView.Adapter.onViewAttachedToWindow called when view attached',
  evidence='INFERRED RecyclerView framework calls onViewAttachedToWindow (androidx source not read)')

# onViewDetachedFromWindow is RecyclerView.Adapter callback
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.onViewDetachedFromWindow', 'FRAMEWORK',
  'RecyclerView.Adapter.onViewDetachedFromWindow called when view detached',
  evidence='INFERRED RecyclerView framework calls onViewDetachedFromWindow (androidx source not read)')

# toggleChecked(boolean,String) called from MainFragment$3
e('MainFragment$3.onActionItemClicked', 'RecyclerAdapter.toggleChecked(boolean,String)', 'DIRECT',
  'Action mode callback toggles checked state for items with path',
  evidence='SRC fragments/MainFragment.java:695')

e('MainFragment$3.onDestroyActionMode', 'RecyclerAdapter.toggleChecked(boolean,String)', 'DIRECT',
  'Action mode destroy callback unchecks all items with path',
  evidence='SRC fragments/MainFragment.java:763')

# RecyclerAdapter lambda callbacks from onBindViewHolder

# lambda$onBindViewHolder$0 is View.OnClickListener from onBindViewHolder
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.lambda$onBindViewHolder$0', 'FRAMEWORK',
  'View.OnClickListener callback for row click',
  evidence='SRC adapters/RecyclerAdapter.java:529 holder.rl.setOnClickListener(v -> {...}); ' +
  'INFERRED View dispatches click events (Android SDK source not read)')

# lambda$onBindViewHolder$1 is View.OnLongClickListener
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.lambda$onBindViewHolder$1', 'FRAMEWORK',
  'View.OnLongClickListener callback for row long click',
  evidence='SRC adapters/RecyclerAdapter.java:543 holder.rl.setOnLongClickListener(p1 -> {...}); ' +
  'INFERRED View dispatches long click events (Android SDK source not read)')

# lambda$onBindViewHolder$2 is View.OnClickListener for genericIcon
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.lambda$onBindViewHolder$2', 'FRAMEWORK',
  'View.OnClickListener callback for generic icon click',
  evidence='SRC adapters/RecyclerAdapter.java:561 holder.genericIcon.setOnClickListener(v -> {...}); ' +
  'INFERRED View dispatches click events (Android SDK source not read)')

# lambda$onBindViewHolder$3 is View.OnClickListener for pictureIcon
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.lambda$onBindViewHolder$3', 'FRAMEWORK',
  'View.OnClickListener callback for picture icon click',
  evidence='SRC adapters/RecyclerAdapter.java:570 holder.pictureIcon.setOnClickListener(view -> {...}); ' +
  'INFERRED View dispatches click events (Android SDK source not read)')

# lambda$onBindViewHolder$4 is View.OnClickListener for apkIcon
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.lambda$onBindViewHolder$4', 'FRAMEWORK',
  'View.OnClickListener callback for apk icon click',
  evidence='SRC adapters/RecyclerAdapter.java:576 holder.apkIcon.setOnClickListener(view -> {...}); ' +
  'INFERRED View dispatches click events (Android SDK source not read)')

# lambda$onBindViewHolder$5 is View.OnClickListener for about button (shows popup)
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.lambda$onBindViewHolder$5', 'FRAMEWORK',
  'View.OnClickListener callback lambda for about button in grid mode',
  evidence='SRC adapters/RecyclerAdapter.java:698-708 about.setOnClickListener(view -> {...}); ' +
  'INFERRED View dispatches click events (Android SDK source not read)')

# lambda$onBindViewHolder$6 is View.OnLongClickListener for grid mode
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.lambda$onBindViewHolder$6', 'FRAMEWORK',
  'View.OnLongClickListener callback lambda for item long click in grid mode',
  evidence='SRC adapters/RecyclerAdapter.java:706-714 imageView.setOnLongClickListener(...); ' +
  'INFERRED View dispatches long click events (Android SDK source not read)')

# lambda$showPopup$7 is PopupMenu.OnMenuItemClickListener
e('RecyclerAdapter.showPopup', 'RecyclerAdapter.lambda$showPopup$7', 'FRAMEWORK',
  'PopupMenu.OnMenuItemClickListener callback lambda',
  evidence='SRC adapters/RecyclerAdapter.java:771 popupMenu.setOnMenuItemClickListener((item) -> {...}); ' +
  'INFERRED PopupMenu dispatches menu item click callbacks (Android SDK source not read)')

# Lambdas call toggleChecked
e('RecyclerAdapter.lambda$onBindViewHolder$1', 'RecyclerAdapter.toggleChecked(int,ImageView)', 'DIRECT',
  'Long click lambda calls toggleChecked',
  evidence='SRC adapters/RecyclerAdapter.java:546')

e('RecyclerAdapter.lambda$onBindViewHolder$2', 'RecyclerAdapter.toggleChecked(int,ImageView)', 'DIRECT',
  'Generic icon click lambda calls toggleChecked',
  evidence='SRC adapters/RecyclerAdapter.java:564')

e('RecyclerAdapter.lambda$onBindViewHolder$3', 'RecyclerAdapter.toggleChecked(int,ImageView)', 'DIRECT',
  'Picture icon click lambda calls toggleChecked',
  evidence='SRC adapters/RecyclerAdapter.java:571')

e('RecyclerAdapter.lambda$onBindViewHolder$4', 'RecyclerAdapter.toggleChecked(int,ImageView)', 'DIRECT',
  'Apk icon click lambda calls toggleChecked',
  evidence='SRC adapters/RecyclerAdapter.java:577')

e('RecyclerAdapter.lambda$onBindViewHolder$6', 'RecyclerAdapter.toggleChecked(int,ImageView)', 'DIRECT',
  'Grid mode long click lambda calls toggleChecked',
  evidence='SRC adapters/RecyclerAdapter.java:707')

# UNREACHABLE dictionary for batch 03
UNREACHABLE = {}

