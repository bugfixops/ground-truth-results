# G1-1 DropboxApiHelper$4.call (checker G1)

- Label: REACHABLE
- Steps: 30 (show_route.py --dedupe on the group 12 build); checked: 30
- Verdict: WRONG (6 wrong steps: 12, 14, 16, 17, 22, 23)

## WRONG steps

**Step 12.** DownloadTabFragment.onClick -> DropboxOauth2AccountActivity.<init> (ENTRY)
- Graph text: "v == dropboxButton: startActivity(...)", but the edge has no guard=.
- Source DownloadTabFragment.java:67-68: `if (v == dropboxButton){ startActivity(new Intent(mActivity, DropboxOauth2AccountActivity.class)); }`
- Fix: add guard='v == dropboxButton (the Dropbox source button was tapped; DownloadTabFragment.java:67-68)'. Same gap on the AnyMemo edge (guard `v == amButton`, lines 64-66).
- graph_def.py: line 1373 (and 1372).

**Step 14.** DropboxOauth2AccountActivity.onCreate -> Oauth2AccountActivity.onNewIntent (LIFECYCLE)
- Wrong: onNewIntent is never called right after onCreate. requestAuth() (Oauth2AccountActivity.java:127-131) opens a Custom Tab; onNewIntent (59-62) runs only when the browser redirect delivers the anymemo-dropbox:// intent to the already-running singleTask instance (AndroidManifest.xml:78-86: launchMode="singleTask", scheme anymemo-dropbox).
- Fix: in the loop, use ('onCreate', 'onDestroy') and drop 'onNewIntent' (onDestroy after onCreate is the same kind of shortcut, not used by this route). Add a hand edge S_DROPBOX_LOGIN -> Oauth2AccountActivity.onNewIntent, env=ENV_OAUTH_CALLBACK, needs_state = a session text "the Dropbox login page was opened by requestAuth() and this activity instance is still alive".
- graph_def.py: line 1163 (loop; creates the wrong edge at 1164). requestAuth -> S_DROPBOX_LOGIN is line 1166.

**Step 16.** Oauth2AccountActivity.fetchTokenAndOnAuthenticate -> Oauth2AccountActivity$2.onComplete (FRAMEWORK)
- Wrong observer. The Single observer of fetchTokenAndOnAuthenticate (Oauth2AccountActivity.java:89, onSuccess at 91) is class $1 (DisposableSingleObserver: onSuccess, onError; checked in the freeDebug class file constant pool). $2 is DisposableCompletableObserver (onComplete at 112, used by verifyTokenAndOnAuthenticate).
- Fix: change the target to Oauth2AccountActivity$1.onSuccess (ENV_OAUTH_CALLBACK kept). The correct FRAMEWORK edge already exists at line 1496.
- graph_def.py: line 1172 (replace).

**Step 17.** Oauth2AccountActivity$2.onComplete -> DropboxOauth2AccountActivity.onAuthenticated (CALL)
- Wrong caller. The call at Oauth2AccountActivity.java:93 (`onAuthenticated(token);`) is inside $1.onSuccess (lines 90-94), not in the Completable's onComplete.
- Fix: source becomes Oauth2AccountActivity$1.onSuccess; target and env unchanged.
- graph_def.py: line 1173.
- Same class mix-up on the verify path, lines 1168-1170 (not on this route): they name $1.onSuccess / $1.onError but cite the verify code's lines 110-121 only through $2. Verify observer is $2: onComplete (112-115) -> onAuthenticated (114); onError (118-121) -> requestAuth (121). Rename those three edges to $2.

**Step 22.** AbstractDownloaderFragment.onCreateView@DBX -> DownloadListAdapter$1.onClick@DBX (FRAMEWORK, "tap a row")
- Wrong: the row listener is registered inside getView (AbstractDownloaderFragment.java:386-411), and getView only runs once the adapter holds rows. Rows come from onViewCreated (170-174) -> refreshList (179-188) -> RetrieveTask.doInBackground (initialRetrieve = Dropbox folder listing, network) -> onPostExecute -> dlAdapter.addList (229-230). The route skips that listing and carries no ENV or STATE.
- Fix: draw the getView and row-click edges from RetrieveTask.onPostExecute@DBX (DL_RT + '.onPostExecute' + hv) with env=ENV_DROPBOX, or keep the source and add needs_state "the Dropbox folder listing loaded (initialRetrieve returned)" plus env=ENV_DROPBOX. The comment at graph_def.py:1095-1100 needs the same change.
- graph_def.py: lines 1121 (getView) and 1122 (row click).

**Step 23.** AbstractDownloaderFragment$DownloadListAdapter$1.onClick@DBX -> showFetchDatabaseDialog@DBX (CALL)
- Missing guard. The call at AbstractDownloaderFragment.java:433-434 is the else branch of `getType()==Category` (417) and `getType()==Back` (425), and only runs when di != null (413-416 return). The edge has only description text, no guard=.
- Fix: guard='row is neither a category nor the back row (else of AbstractDownloaderFragment.java:417 and 425; di != null)'.
- graph_def.py: line 1130.

## Could not check / INFERRED
- Step 5: BottomNavigationView.setSelectedItemId calls the listener (material library, not read). Correct as INFERRED.
- Steps 9-11, 21, 24: androidx fragment callbacks and dialogs (not read). INFERRED is correct.
- Steps 14-15: singleTask onNewIntent delivery is framework behaviour; fw_src not read for it, so INFERRED.
- Step 3: `!isUiLoaded` is always true on a cold start (new instance), so it is not a graph gap.
- Steps 16-17 correction depends on javac numbering; checked from the class-file constant pool, not javap (no JRE installed).
