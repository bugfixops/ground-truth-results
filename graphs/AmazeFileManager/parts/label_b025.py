# ---- Helper batch_025 label part (2026-10-27)

# FileHandler edges
e('MainFragment.showSMBDialog', 'FileHandler.<init>', 'EXPLICIT', 'MainFragment creates FileHandler for CustomFileObserver',
  evidence='SRC MainFragment.java:1194-1195 new CustomFileObserver(CURRENT_PATH, new FileHandler(this, listView, getBoolean(PREFERENCE_SHOW_THUMB)))')

e('CustomFileObserver.sendMessages', 'FileHandler.handleMessage', 'ASYNC', 'CustomFileObserver sends messages to FileHandler',
  evidence='SRC CustomFileObserver.java:134 handler.obtainMessage(NEW_ITEM, pathAdded).sendToTarget()')

# FileListSorter edges
e('LoadFilesListTask.doInBackground', 'FileListSorter.<init>', 'EXPLICIT', 'LoadFilesListTask creates FileListSorter for sorting',
  evidence='SRC LoadFilesListTask.java:215 Collections.sort(list, new FileListSorter(ma.dsort, sortby, asc))')

e('FileListSorter.<init>', 'FileListSorter.compare', 'FRAMEWORK', 'Collections.sort calls Comparator.compare',
  evidence='SRC LoadFilesListTask.java:215 Collections.sort with FileListSorter')

e('FileListSorter.compare', 'FileListSorter.isDirectory', 'CALL', 'compare checks if items are directories',
  evidence='SRC FileListSorter.java:68 if (isDirectory(file1) && !isDirectory(file2))')

e('FileListSorter.compare', 'FileListSorter.getExtension', 'CALL', 'compare gets file extensions for type sorting',
  evidence='SRC FileListSorter.java:108-109 final String ext_a = getExtension(file1.title)')

# FastScroller edges
e('MainFragment.onCreateView', 'FastScroller.<init>', 'FRAMEWORK', 'Fragment inflates FastScroller from XML layout',
  evidence='SRC MainFragment.java:242 fastScroller = rootView.findViewById(R.id.fastscroll)')

e('MainFragment.onCreateView', 'FastScroller.setPressedHandleColor', 'CALL', 'MainFragment sets FastScroller handle color',
  evidence='SRC MainFragment.java:243 fastScroller.setPressedHandleColor(accentColor)')

e('MainFragment.changeSorting', 'FastScroller.setRecyclerView', 'CALL', 'MainFragment sets RecyclerView on FastScroller',
  evidence='SRC MainFragment.java:1150 fastScroller.setRecyclerView(listView, IS_LIST? 1:columns)')

e('MainFragment.changeSorting', 'FastScroller.registerOnTouchListener', 'CALL', 'MainFragment registers touch listener',
  evidence='SRC MainFragment.java:1154 fastScroller.registerOnTouchListener(() -> {')

e('MainFragment.changeSorting', 'FastScroller.updateHandlePosition', 'CALL', 'AppBarLayout listener calls updateHandlePosition',
  evidence='SRC MainFragment.java:1152 fastScroller.updateHandlePosition(verticalOffset, 112)')

e('FastScroller.<init>', 'FastScroller.initialise', 'CALL', 'Constructor calls initialise',
  evidence='SRC FastScroller.java:37,42 initialise(context)')

e('FastScroller.initialise', 'FastScroller.setPressedHandleColor', 'CALL', 'initialise sets default handle color',
  evidence='SRC FastScroller.java:84 setPressedHandleColor(Utils.getColor(getContext(), R.color.accent_blue))')

e('FastScroller.initialise', 'FastScroller.setUpBarBackground', 'CALL', 'initialise sets up bar background',
  evidence='SRC FastScroller.java:84 setUpBarBackground()')

e('FastScroller.setUpBarBackground', 'FastScroller.resolveColor', 'CALL', 'setUpBarBackground resolves color attribute',
  evidence='SRC FastScroller.java:103 int resolveColor = resolveColor(getContext(), R.attr.colorControlNormal)')

e('FastScroller.setRecyclerView', 'FastScroller.invalidateVisibility', 'CALL', 'setRecyclerView calls invalidateVisibility',
  evidence='SRC FastScroller.java:175 invalidateVisibility()')

e('FastScroller.invalidateVisibility', 'FastScroller.isRecyclerViewScrollable', 'CALL', 'invalidateVisibility checks if scrollable',
  evidence='SRC FastScroller.java:132 isRecyclerViewScrollable()')

e('FastScroller.onTouchEvent', 'FastScroller.getRelativeTouchPosition', 'CALL', 'onTouchEvent gets relative touch position',
  evidence='SRC FastScroller.java:123 float relativePos = getRelativeTouchPosition(motionEvent)')

e('FastScroller.onTouchEvent', 'FastScroller.setHandlePosition1', 'CALL', 'onTouchEvent sets handle position',
  evidence='SRC FastScroller.java:124 setHandlePosition1(relativePos)')

e('FastScroller.onTouchEvent', 'FastScroller.setRecyclerViewPosition', 'CALL', 'onTouchEvent sets RecyclerView position',
  evidence='SRC FastScroller.java:125 setRecyclerViewPosition(relativePos)')

e('FastScroller.setHandlePosition1', 'FastScroller.getHeightMinusPadding', 'CALL', 'setHandlePosition1 gets available height',
  evidence='SRC FastScroller.java:97 Utils.clamp(0, getHeightMinusPadding() - handle.getHeight(), ...')

e('FastScroller.computeHandlePosition', 'FastScroller.getHeightMinusPadding', 'CALL', 'computeHandlePosition gets available height',
  evidence='SRC FastScroller.java:62,68 getHeightMinusPadding()')

e('FastScroller.updateHandlePosition', 'FastScroller.setHandlePosition1', 'CALL', 'updateHandlePosition sets handle position',
  evidence='SRC FastScroller.java:191 setHandlePosition1(computeHandlePosition())')

e('FastScroller.updateHandlePosition', 'FastScroller.computeHandlePosition', 'CALL', 'updateHandlePosition computes position',
  evidence='SRC FastScroller.java:191 setHandlePosition1(computeHandlePosition())')

e('FastScroller.setRecyclerView', 'FastScroller$ScrollListener.<init>', 'IMPLICIT', 'ScrollListener created in FastScroller constructor',
  evidence='SRC FastScroller.java:28,36 this.scrollListener = new ScrollListener()')

e('FastScroller.setRecyclerView', 'FastScroller$ScrollListener.onScrolled', 'FRAMEWORK', 'RecyclerView calls onScrolled on scroll',
  evidence='SRC FastScroller.java:174 recyclerView.addOnScrollListener(this.scrollListener)')

e('FastScroller$ScrollListener.onScrolled', 'FastScroller.updateHandlePosition', 'CALL', 'ScrollListener updates handle position',
  evidence='SRC FastScroller.java:34 updateHandlePosition()')

e('FastScroller.setRecyclerView', 'FastScroller$1.<init>', 'IMPLICIT', 'Anonymous OnHierarchyChangeListener created',
  evidence='SRC FastScroller.java:176 recyclerView.setOnHierarchyChangeListener(new OnHierarchyChangeListener() {')

e('FastScroller.setRecyclerView', 'FastScroller$1.onChildViewAdded', 'FRAMEWORK', 'RecyclerView calls onChildViewAdded',
  evidence='SRC FastScroller.java:178 public void onChildViewAdded(View parent, View child) {')

e('FastScroller.setRecyclerView', 'FastScroller$1.onChildViewRemoved', 'FRAMEWORK', 'RecyclerView calls onChildViewRemoved',
  evidence='SRC FastScroller.java:182 public void onChildViewRemoved(View parent, View child) {')

e('FastScroller$1.onChildViewAdded', 'FastScroller.invalidateVisibility', 'CALL', 'onChildViewAdded invalidates visibility',
  evidence='SRC FastScroller.java:179 invalidateVisibility()')

e('FastScroller$1.onChildViewRemoved', 'FastScroller.invalidateVisibility', 'CALL', 'onChildViewRemoved invalidates visibility',
  evidence='SRC FastScroller.java:183 invalidateVisibility()')

# Extractor edges
e('ExtractService.runIntentInService', 'Extractor.extractFiles', 'CALL', 'ExtractService calls extractFiles on Extractor',
  evidence='SRC ExtractService.java:298 extractor.extractFiles(entriesToExtract)')

e('ExtractService.runIntentInService', 'Extractor.extractEverything', 'CALL', 'ExtractService calls extractEverything on Extractor',
  evidence='SRC ExtractService.java:300 extractor.extractEverything()')

e('ExtractService.runIntentInService', 'Extractor.getInvalidArchiveEntries', 'CALL', 'ExtractService gets invalid entries',
  evidence='SRC ExtractService.java:301 extractor.getInvalidArchiveEntries().size()')

e('Extractor.extractFiles', 'Extractor.lambda$extractFiles$0', 'CALL', 'extractFiles creates filter lambda',
  evidence='SRC Extractor.java:54 extractWithFilter((relativePath, isDir) -> {')

e('Extractor.extractEverything', 'Extractor.lambda$extractEverything$1', 'CALL', 'extractEverything creates filter lambda',
  evidence='SRC Extractor.java:72 extractWithFilter((relativePath, isDir) -> true)')

e('TarExtractor.extractWithFilter', 'Extractor.fixEntryName', 'CALL', 'TarExtractor calls fixEntryName',
  evidence='SRC TarExtractor.java:90 File outputFile = new File(outputDir, fixEntryName(entry.getName()))')

