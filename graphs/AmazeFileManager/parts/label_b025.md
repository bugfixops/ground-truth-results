STATUS: RUNNING 22:59

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| FileHandler.<init> | REACHABLE | | Constructor called from MainFragment | SRC MainFragment.java:1194-1195 |
| FileHandler.handleMessage | REACHABLE | | Handler callback from CustomFileObserver | SRC CustomFileObserver.java:104,134,141 |
| FileListSorter.<init> | REACHABLE | | Constructor called from LoadFilesListTask and MainFragment | SRC LoadFilesListTask.java:215; MainFragment.java:1643 |
| FileListSorter.compare | REACHABLE | | Comparator interface method called by Collections.sort | SRC FileListSorter.java:48 |
| FileListSorter.isDirectory | REACHABLE | | Called from compare | SRC FileListSorter.java:68,72,76,79 |
| FileListSorter.getExtension | REACHABLE | | Called from compare | SRC FileListSorter.java:108-109 |
| FastScroller.<init> | REACHABLE | | Constructor called via XML inflation from fragments | SRC MainFragment.java:242; CompressedExplorerFragment.java:478 |
| FastScroller.<init> | REACHABLE | | Second constructor overload | SRC FastScroller.java:41-44 |
| FastScroller.setPressedHandleColor | REACHABLE | | Called from MainFragment and CompressedExplorerFragment | SRC MainFragment.java:243; CompressedExplorerFragment.java:480 |
| FastScroller.setRecyclerView | REACHABLE | | Called from MainFragment and CompressedExplorerFragment | SRC MainFragment.java:1150; CompressedExplorerFragment.java:479 |
| FastScroller.registerOnTouchListener | REACHABLE | | Called from MainFragment | SRC MainFragment.java:1154 |
| FastScroller.updateHandlePosition | REACHABLE | | Called from AppBarLayout offset listener | SRC MainFragment.java:1152; CompressedExplorerFragment.java:481 |
| FastScroller.updateHandlePosition | REACHABLE | | No-arg overload called from ScrollListener | SRC FastScroller.java:190-191 |
| FastScroller.onTouchEvent | REACHABLE | | View touch event framework callback | SRC FastScroller.java:116 |
| FastScroller.initialise | REACHABLE | | Called from constructors | SRC FastScroller.java:37,42 |
| FastScroller.resolveColor | REACHABLE | | Called from setUpBarBackground | SRC FastScroller.java:103 |
| FastScroller.setUpBarBackground | REACHABLE | | Called from initialise | SRC FastScroller.java:84 |
| FastScroller.getHeightMinusPadding | REACHABLE | | Called from computeHandlePosition and others | SRC FastScroller.java:62,68,136,145 |
| FastScroller.computeHandlePosition | REACHABLE | | Called from updateHandlePosition and setHandlePosition1 | SRC FastScroller.java:191,197 |
| FastScroller.setHandlePosition1 | REACHABLE | | Called from onTouchEvent and updateHandlePosition | SRC FastScroller.java:124,191,197 |
| FastScroller.getRelativeTouchPosition | REACHABLE | | Called from onTouchEvent | SRC FastScroller.java:123 |
| FastScroller.setRecyclerViewPosition | REACHABLE | | Called from onTouchEvent | SRC FastScroller.java:125 |
| FastScroller.invalidateVisibility | REACHABLE | | Called from setRecyclerView and inner class | SRC FastScroller.java:175,179,183 |
| FastScroller.isRecyclerViewScrollable | REACHABLE | | Called from invalidateVisibility | SRC FastScroller.java:132 |
| FastScroller$ScrollListener.<init> | REACHABLE | | Inner class constructor | SRC FastScroller.java:28,36 |
| FastScroller$ScrollListener.onScrolled | REACHABLE | | RecyclerView.OnScrollListener callback | SRC FastScroller.java:32 |
| FastScroller$1.<init> | REACHABLE | | Anonymous class constructor | SRC FastScroller.java:176 |
| FastScroller$1.onChildViewAdded | REACHABLE | | OnHierarchyChangeListener callback | SRC FastScroller.java:178 |
| FastScroller$1.onChildViewRemoved | REACHABLE | | OnHierarchyChangeListener callback | SRC FastScroller.java:182 |
| Extractor.<init> | REACHABLE | | Abstract class constructor called via subclasses | SRC Extractor.java:43-49 |
| Extractor.extractFiles | REACHABLE | | Called from ExtractService | SRC ExtractService.java:298 |
| Extractor.extractEverything | REACHABLE | | Called from ExtractService | SRC ExtractService.java:300 |
| Extractor.getInvalidArchiveEntries | REACHABLE | | Called from ExtractService | SRC ExtractService.java:301 |
| Extractor.fixEntryName | REACHABLE | | Protected method called by subclasses | SRC TarExtractor.java:90; RarExtractor.java:86; GzipExtractor.java:92; ZipExtractor.java:100 |
| Extractor.lambda$extractFiles$0 | REACHABLE | | Lambda from extractFiles | SRC Extractor.java:54-67 |
| Extractor.lambda$extractEverything$1 | REACHABLE | | Lambda from extractEverything | SRC Extractor.java:72 |

STATUS: DONE 23:04
