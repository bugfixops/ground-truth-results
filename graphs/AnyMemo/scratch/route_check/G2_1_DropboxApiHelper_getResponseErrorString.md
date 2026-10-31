# G2-1 route check: DropboxApiHelper.getResponseErrorString

- Method: DropboxApiHelper.getResponseErrorString
- Label: REACHABLE
- Steps: 20; checked: 20 (every step read in the source)
- Verdict: WRONG (3 wrong steps: 12, 13, 20; step 16 has a wrong citation reason but a correct edge)

## Wrong steps

**Step 12. FileBrowserFragment.openFile@OPEN -> FileBrowserFragment.notifyFileClick (CALL)**
- Source FileBrowserFragment.java:412-415: `if (onFileClickListener != null) { onFileClickListener.onFileBrowserFileClick(clickedFile); } else { notifyFileClick(clickedFile); }`.
- The Open tab's OpenTabFragment sets that listener in onAttach (OpenTabFragment.java:38). So the call at line 415 never runs on the OPEN host. The graph edge exists only because `clone_auto` copies the bytecode edge openFile -> notifyFileClick onto every variant, and `FileBrowserFragment.notifyFileClick` is not in its exclude set.
- Fix: graph_def.py:526, add `'FileBrowserFragment.notifyFileClick'` to the exclude set (`set(FB_TARGET.values()) | {...}`). The hand edge for UPLOADDROPBOX at graph_def.py:528 stays. After the fix, the OPEN route goes openFile@OPEN -> OpenTabFragment$1.onFileBrowserFileClick (graph_def.py:531) -> OpenActionsFragment dialog.

**Step 13. FileBrowserFragment.notifyFileClick -> UploadDropboxActivity.onFileBrowserFileClick (CALL)**
- The edge itself is right for one host only: UploadDropboxActivity hosts a plain FileBrowserFragment (UploadDropboxActivity.java:55-57, no listener set). In this route the click came from the Open tab (AnyMemo host), so this edge cannot follow step 12. The route must enter the upload host instead.
- Guard text (graph_def.py:532, duplicate at 1190) covers only the second branch of FileBrowserFragment.java:435-438. The first branch, `getParentFragment() instanceof OnFileClickListener` (line 435), is not in the text; it is false on the activity host, so the guard should say so.
- Fix: no change to this edge after the step 12 fix. The rebuilt route should enter the upload host: S_DROPBOX_UPLOAD (DropboxListActivity.openUploadDropbox -> UploadDropboxActivity.<init>, graph_def.py:1181) -> FileBrowserFragment.onCreateView@UPLOADDROPBOX (FB_PAGES, graph_def.py:537-542). The rebuilt route will carry ENV_DROPBOX on the way. Optional: extend the guard text at graph_def.py:532 with the first-branch condition.

**Step 20. DropboxApiHelper$5.call -> DropboxApiHelper.getResponseErrorString (CALL, auto edge, no graph_def line)**
- Source DropboxApiHelper.java:248-251: `Response response = okHttpClient.newCall(request).execute(); if (!response.isSuccessful()) { throw new IOException(getResponseErrorString(request, response)); }`. The graph says "Direct call" with no guard.
- Missing guard: `!response.isSuccessful()` (the upload server answered with an error status). The call also needs `fileToUpload.exists()` (lines 236-238 throw before the request, so the path to line 250 requires the file to exist).
- Fix: add a GATE entry in graph_def.py (GATE dict starts at line 2769; the Dropbox GATE entries are at 2830-2833), key `('DropboxApiHelper$5.call', 'DropboxApiHelper.getResponseErrorString')`, guard text `'!response.isSuccessful() (DropboxApiHelper.java:249-250); the file to upload exists (236-238)'`. The error response is an outside condition; set env= only if the build has an ENV kind for it. ENV_DROPBOX is already on the upstream edge (graph_def.py:2833).

## Non-route issue (edge correct, citation wrong)

**Step 16. S_DLG_DROPBOX_UPLOAD_CONFIRM -> UploadDropboxActivity$1.onClick (GUI)**
- The INFERRED reason says "androidx.fragment.app.DialogFragment shows an android.app.Dialog". UploadDropboxActivity.java:77-87 uses `new AlertDialog.Builder(this)...show()` inside the Activity; there is no DialogFragment. The edge is still right. Fix the evidence text of the gui() call at graph_def.py:1193 (it uses FW_DIALOGFRAG) to name android.app.AlertDialog and give the reason.

## Steps checked as OK (short)
1 manifest MAIN/LAUNCHER (AndroidManifest.xml:23-36); 2 AnyMemo.<init> -> onCreate (lifecycle); 3 onCreate -> loadUiComponents, guard matches AnyMemo.java:124-135 (SDK <= Q, permission granted, !isUiLoaded at cold start); 4 loadUiComponents -> initDrawer unconditional (AnyMemo.java:187); 5 initDrawer -> setSelectedItemId at 263, unconditional; 6 and 8 guards match 240-246; 7 GUI tap; 9 OpenTabFragment inherits FileBrowserFragment.onCreateView; 10 row click set in onBindViewHolder at 514, after the empty-name return at 483-485; 11 onClick -> openFile at 517; 14 onFileBrowserFileClick -> showUploadDialog (UploadDropboxActivity.java:123-124); 15 dialog ENTERS (77-87); 17 OK tap -> uploadToDropbox (84); 18 uploadToDropbox -> uploadDropbox at line 99; 19 uploadDropbox -> $5.call via Rx (233).

## Not checked
- RxJava and androidx source not read (INFERRED reasons kept for steps 5, 7, 9, 10, 16, 19).
- The anonymous class number DropboxApiHelper$5 was not confirmed with javap (bytecode checker covers it).
- The AlertDialog button dispatch in fw_src was not read.
