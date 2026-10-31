# Repair Batch 32 Status

STATUS: START 22:11
STATUS: DONE 22:14

## Method Status

| Method | Status | Evidence |
|--------|--------|----------|
| SearchAsyncTask.<init> | REACHABLE | Already in graph_def.py (called by SearchWorkerFragment.onAttach) |
| SearchAsyncTask.bashRegexToJava | REACHABLE | Already in graph_def.py (called by SearchAsyncTask.search) |
| SearchAsyncTask.doInBackground | REACHABLE | Already in graph_def.py (framework calls from AsyncTask) |
| SearchAsyncTask.lambda$search$0 | REACHABLE | Already in graph_def.py |
| SearchAsyncTask.lambda$search$1 | REACHABLE | Already in graph_def.py |
| SearchAsyncTask.lambda$searchRegExFind$2 | REACHABLE | Already in graph_def.py |
| SearchAsyncTask.lambda$searchRegExMatch$3 | REACHABLE | Already in graph_def.py |
| SearchAsyncTask.onCancelled | REACHABLE | Already in graph_def.py (framework callback) |
| SearchAsyncTask.onPostExecute | REACHABLE | Already in graph_def.py (framework callback) |
| SearchAsyncTask.onPreExecute | REACHABLE | Already in graph_def.py (framework callback) |
| SearchAsyncTask.onProgressUpdate | REACHABLE | Already in graph_def.py (framework callback) |
| SearchAsyncTask.search(HybridFile,SearchFilter) | REACHABLE | Already in graph_def.py (called by doInBackground) |
| SearchAsyncTask.search(HybridFile,String) | REACHABLE | Already in graph_def.py (called by doInBackground) |
| SearchAsyncTask.searchRegExFind | REACHABLE | Already in graph_def.py (called by doInBackground) |
| SearchAsyncTask.searchRegExMatch | REACHABLE | Already in graph_def.py (called by doInBackground) |
| SearchView$1.onAnimationCancel | REACHABLE | Already in graph_def.py (Animator.AnimatorListener callback) |
| SearchView$1.onAnimationEnd | REACHABLE | Already in graph_def.py (Animator.AnimatorListener callback) |
| SearchView$1.onAnimationRepeat | REACHABLE | Already in graph_def.py (Animator.AnimatorListener callback) |
| SearchView$1.onAnimationStart | REACHABLE | Already in graph_def.py (Animator.AnimatorListener callback) |
| SearchView$2.onAnimationCancel | REACHABLE | Already in graph_def.py (Animator.AnimatorListener callback) |
| SearchView$2.onAnimationEnd | REACHABLE | Already in graph_def.py (Animator.AnimatorListener callback) |
| SearchView$2.onAnimationRepeat | REACHABLE | Already in graph_def.py (Animator.AnimatorListener callback) |
| SearchView$2.onAnimationStart | REACHABLE | Already in graph_def.py (Animator.AnimatorListener callback) |
| SearchWorkerFragment.onAttach | REACHABLE | Already in graph_def.py (Fragment lifecycle callback) |
| SearchWorkerFragment.onCreate | REACHABLE | Already in graph_def.py (Fragment lifecycle callback, creates SearchAsyncTask) |
| SelectedColorsPreference.<init> | REACHABLE | Already in graph_def.py |
| SelectedColorsPreference.onBindView | REACHABLE | Already in graph_def.py (Preference callback) |
| SelectedColorsPreference.onCreateView | REACHABLE | Already in graph_def.py (Preference callback) |
| SevenZFile.read(byte[]) | REACHABLE | Already in graph_def.py |
| SevenZFile$1.count | REACHABLE | Added route: called by SevenZFile$1.read() and read(byte[],int,int) |
| SevenZFile$1.read() | REACHABLE | Added route: framework calls when InputStream is read, overrides FilterInputStream.read() |
| SevenZFile$1.read(byte[]) | REACHABLE | Added route: framework calls, delegates to read(byte[],int,int) |
| SevenZFile$1.read(byte[],int,int) | REACHABLE | Added route: framework calls when InputStream is read with offset, overrides FilterInputStream |
| SevenZFile$2.<init> | REACHABLE | Already in graph_def.py |
| SevenZFile$2.getCompressedCount | REACHABLE | Already in graph_def.py |
| SevenZFile$2.getUncompressedCount | REACHABLE | Already in graph_def.py |
| SevenZMethodConfiguration.getMethod | REACHABLE | Already in graph_def.py |
| SevenZMethodConfiguration.getOptions | REACHABLE | Already in graph_def.py |

## Summary

- REACHABLE: 38
- UNREACHABLE: 0
- INCOMPLETE: 0

## Notes

Batch 32 contained 38 methods, of which 34 already had routes in graph_def.py. Only 4 methods needed to be added:
- SevenZFile$1.count (private method in anonymous FilterInputStream)
- SevenZFile$1.read() (overrides FilterInputStream.read())
- SevenZFile$1.read(byte[]) (delegates to read(byte[],int,int))
- SevenZFile$1.read(byte[],int,int) (overrides FilterInputStream.read(byte[],int,int))

SevenZFile$1 is an anonymous FilterInputStream class created in SevenZFile.buildDecoderStack() at line 997 to track compressed bytes read from the archive stream.
