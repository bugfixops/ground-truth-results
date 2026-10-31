# Repair Batch 03 Status

STATUS: START 20:24
STATUS: DONE 20:26

## Methods Processed: 37

### REACHABLE: 37
1. TextEditorActivity.afterTextChanged - REACHABLE (TextWatcher callback from EditText, registered in onCreate:210)
2. TextEditorActivity.beforeTextChanged - REACHABLE (TextWatcher callback from EditText, registered in onCreate:210)
3. TextEditorActivity.checkUnsavedChanges - REACHABLE (called from onBackPressed:340 and onOptionsItemSelected:360)
4. TextEditorActivity.cleanSpans - REACHABLE (called from beforeTextChanged:417 and onClick:588)
5. TextEditorActivity.hideSearchView - REACHABLE (called from onOptionsItemSelected:389)
6. TextEditorActivity.lambda$checkUnsavedChanges$0 - REACHABLE (MaterialDialog positive button callback from checkUnsavedChanges:243)
7. TextEditorActivity.lambda$checkUnsavedChanges$1 - REACHABLE (MaterialDialog negative button callback from checkUnsavedChanges:248)
8. TextEditorActivity.lambda$load$4 - REACHABLE (ReadFileTask callback from load:291)
9. TextEditorActivity.lambda$null$3 - REACHABLE (Snackbar action callback from lambda$load$4:308)
10. TextEditorActivity.lambda$saveFile$2 - REACHABLE (WriteFileAbstraction callback from saveFile:263)
11. TextEditorActivity.onBackPressed - REACHABLE (Activity lifecycle callback, framework dispatches)
12. TextEditorActivity.onClick - REACHABLE (View.OnClickListener callback, registered in onCreate:183-185)
13. TextEditorActivity.onCreateOptionsMenu - REACHABLE (Activity lifecycle callback, framework dispatches:344)
14. TextEditorActivity.onDestroy - REACHABLE (Activity lifecycle callback, framework dispatches:399)
15. TextEditorActivity.onOptionsItemSelected - REACHABLE (Activity lifecycle callback, framework dispatches:355)
16. TextEditorActivity.onPrepareOptionsMenu - REACHABLE (Activity lifecycle callback, framework dispatches:349)
17. TextEditorActivity.onSaveInstanceState - REACHABLE (Activity lifecycle callback, framework dispatches:223)
18. TextEditorActivity.onTextChanged - REACHABLE (TextWatcher callback from EditText, registered in onCreate:210,181)
19. TextEditorActivity.revealSearchView - REACHABLE (called from onOptionsItemSelected:390)
20. TextEditorActivity.saveFile - REACHABLE (called from onOptionsItemSelected:364 and lambda$checkUnsavedChanges$0:243)
21. RecyclerAdapter.addItem - REACHABLE (called from MainFragment.addSearchResult:1629)
22. RecyclerAdapter.areAllChecked - REACHABLE (called from MainFragment$3.onActionItemClicked:691)
23. RecyclerAdapter.getCorrectView - REACHABLE (called from RecyclerPreloadSizeProvider.getPreloadSize:56)
24. RecyclerAdapter.getItemId - REACHABLE (RecyclerView.Adapter callback, framework dispatches)
25. RecyclerAdapter.getItemViewType - REACHABLE (RecyclerView.Adapter callback, framework dispatches; also called from MainFragment$2.getSpanSize:345)
26. RecyclerAdapter.lambda$onBindViewHolder$0 - REACHABLE (View.OnClickListener callback from onBindViewHolder:529)
27. RecyclerAdapter.lambda$onBindViewHolder$1 - REACHABLE (View.OnLongClickListener callback from onBindViewHolder:543)
28. RecyclerAdapter.lambda$onBindViewHolder$2 - REACHABLE (View.OnClickListener callback from onBindViewHolder:561)
29. RecyclerAdapter.lambda$onBindViewHolder$3 - REACHABLE (View.OnClickListener callback from onBindViewHolder:570)
30. RecyclerAdapter.lambda$onBindViewHolder$4 - REACHABLE (View.OnClickListener callback from onBindViewHolder:576)
31. RecyclerAdapter.lambda$onBindViewHolder$5 - REACHABLE (View.OnClickListener callback from onBindViewHolder:698-708)
32. RecyclerAdapter.lambda$onBindViewHolder$6 - REACHABLE (View.OnLongClickListener callback from onBindViewHolder:706-714)
33. RecyclerAdapter.lambda$showPopup$7 - REACHABLE (PopupMenu.OnMenuItemClickListener callback from showPopup:771)
34. RecyclerAdapter.onFailedToRecycleView - REACHABLE (RecyclerView.Adapter callback, framework dispatches)
35. RecyclerAdapter.onViewAttachedToWindow - REACHABLE (RecyclerView.Adapter callback, framework dispatches)
36. RecyclerAdapter.onViewDetachedFromWindow - REACHABLE (RecyclerView.Adapter callback, framework dispatches)
37. RecyclerAdapter.toggleChecked(boolean,String) - REACHABLE (called from MainFragment$3.onActionItemClicked:695 and onDestroyActionMode:763)

### UNREACHABLE: 0

### INCOMPLETE: 0

## Evidence Sources
- Source files: TextEditorActivity.java, RecyclerAdapter.java, MainFragment.java, RecyclerPreloadSizeProvider.java
- Bytecode calls: auto_calls.json
- All framework callbacks: INFERRED (Android SDK and androidx source not read)
- All library callbacks: INFERRED (MaterialDialog, Glide, etc. source not read)

## Notes
All 37 methods in this batch are REACHABLE. The batch contains:
- 20 TextEditorActivity methods: all are Activity/View lifecycle callbacks or methods called from those callbacks
- 17 RecyclerAdapter methods: all are RecyclerView.Adapter callbacks, lambda click handlers, or methods called from MainFragment

No methods in this batch are unreachable. All have clear routes from entry points through the framework or direct application calls.
