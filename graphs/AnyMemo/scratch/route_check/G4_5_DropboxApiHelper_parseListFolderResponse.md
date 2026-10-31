# G4-5: DropboxApiHelper.parseListFolderResponse

- Method: DropboxApiHelper.parseListFolderResponse. Call sites: DropboxApiHelper.java:164 (first page) and :186 (later pages, inside `while (hasMore)` at :167), both in the Observable.create subscribe body (:143-190).
- Label: REACHABLE (cold start -> Download tab -> Dropbox button -> DropboxOauth2AccountActivity -> login -> redirect into Oauth2AccountActivity.onNewIntent -> token fetch -> DropboxListActivity -> DropboxListFragment -> listFiles). Needs a first-time login and a Dropbox account.
- Steps: 28 (show_route.py --dedupe). Checked: 28.
- Verdict: WRONG (7 wrong steps: 10, 14, 16, 17, 21, 24, 28)

## Wrong steps

Step 10: DownloadTabFragment.onAttach -> DownloadTabFragment.onCreateView (LIFECYCLE), graph_def.py:1370.
- Wrong: skips the inherited onCreate (order is onAttach -> onCreate -> onCreateView). No state effect, since DownloadTabFragment has no onCreate override. The base is androidx Fragment (common/BaseFragment.java:3, :9). No androidx source is in the tree, so the order is INFERRED.
- Fix: insert an inherited onCreate node between the two edges.

Step 14: DropboxOauth2AccountActivity.onCreate -> Oauth2AccountActivity.onNewIntent (LIFECYCLE), loop at graph_def.py:1163-1164.
- Wrong: onNewIntent is not called from onCreate. Oauth2AccountActivity.onCreate (:37-50) calls requestAuth() when no token is saved (:44-48), which opens the login page (:127-131). onNewIntent (:59-62) runs only when the browser redirects back into the singleTask activity (AndroidManifest.xml:77-88, scheme anymemo-dropbox).
- Fix: in the loop keep only 'onCreate', as a CALL (super.onCreate, DropboxOauth2AccountActivity.java:21), and drop onDestroy and onNewIntent. Route instead: onCreate -> requestAuth (guard 'no saved token', :44-48; edges at :1165-1166 exist) -> S_DROPBOX_LOGIN -> onNewIntent (new edge, env ENV_OAUTH_CALLBACK).

Step 16: Oauth2AccountActivity.fetchTokenAndOnAuthenticate -> Oauth2AccountActivity$2.onComplete (FRAMEWORK), graph_def.py:1172.
- Wrong: the fetch uses DisposableSingleObserver (Oauth2AccountActivity.java:89), whose callback is onSuccess (:91). That is class $1 (constant pool: onSuccess, onError, saveToken, onAuthenticated). $2 is the saved-token verify observer (DisposableCompletableObserver, verifyTokenAndOnAuthenticate :105-120, onComplete :112).
- Fix: delete the edge at :1172. The correct edge to Oauth2AccountActivity$1.onSuccess already exists at :1496.

Step 17: Oauth2AccountActivity$2.onComplete -> DropboxOauth2AccountActivity.onAuthenticated (CALL), graph_def.py:1173; the call is at Oauth2AccountActivity.java:114.
- Wrong: the call is on the saved-token path, entered only when savedToken != null (:44-46). The route reached it from the fetch path with no state. The env ENV_OAUTH_CALLBACK is also wrong: the verify runs from onCreate, not from the redirect.
- Fix: at :1173 add needs_state=NEED_SAVED_TOKEN (text at graph_def.py:166) and env=ENV_NET, reached from onCreate's verify branch. The states are swapped: :1169 ($1.onSuccess -> onAuthenticated) carries NEED_SAVED_TOKEN, but the first-login fetch path needs no saved token. Remove it there.

Step 21: S_DROPBOX_LIST -> AbstractDownloaderFragment.onViewCreated@DBX (LIFECYCLE), loop at graph_def.py:1119.
- Wrong: skips DropboxListFragment.onCreate (DropboxListFragment.java:49-55, sets authToken at :54), plus onAttach (AbstractDownloaderFragment.java:128), onCreate (:134) and onCreateView (:140). listFiles(authToken, ...) at DropboxListFragment.java:60 would then run with authToken unset. Missing state: the token from the activity extras (DropboxListActivity.java:49-50; set at DropboxOauth2AccountActivity.java:27).
- Fix: at :1119 chain DropboxListFragment.onCreate (already a CALL target at :1177) -> AbstractDownloaderFragment.onCreateView (:140) -> onViewCreated (:170). Add needs_state for the token.

Step 24: AbstractDownloaderFragment$RetrieveTask.doInBackground -> AbstractDownloaderFragment$1.call (CALL), graph_def.py:1143.
- Wrong: the for loop at AbstractDownloaderFragment.java:210 (`for (Callable ... task : tasks)`) has no guard in the graph. It always runs once (refreshList passes one Callable, :182), but the guard must be shown.
- Fix: guard='for each Callable in tasks (AbstractDownloaderFragment.java:210); always one task from :182' on the edge at :1143.

Step 28: DropboxApiHelper$3.subscribe -> DropboxApiHelper.parseListFolderResponse (CALL, auto edge; evidence DropboxApiHelper.java:186).
- Wrong: the route takes the continuation call at :186, inside `while (hasMore)` (:167) and after the continuation early return (:177-180). It has no guard and needs a folder with more than one page. The first-page call at :164 needs only the early return at :155-158. The auto edge keeps one call site per caller/callee pair: graphs/AnyMemo/auto_calls.json has one record for this pair (line 186), so :164 is lost.
- Fix: hand edges for both call sites (a hand edge for the pair suppresses the auto edge, build_graph.py:223-224). :164: guard='first list_folder response is successful (:155-158)'. :186: guard='hasMore (:167) and continuation response successful (:177-180)', needs_state='folder has more than one page'.

## Steps checked and OK (21)

- 1 ENTRY: AndroidManifest.xml:23-46 OK.
- 2 AnyMemo.<init> -> onCreate: AnyMemo.java:116 OK. Citation fix: Activity.java:6989-6999 (not counted).
- 3 guard AnyMemo.java:124-134 OK. 4 AnyMemo.java:187 OK. 5 AnyMemo.java:263 OK (library dispatch INFERRED). 6 guard :240-241 OK. 7 tap listener :234-261 OK (dispatch INFERRED).
- 8 guard :247-248, commit :253-257 OK. The `if (fragment != null)` guard is always true on this route.
- 9 S_MAIN_DOWNLOAD -> DownloadTabFragment.onAttach (:46-50) OK.
- 11 onCreateView -> onClick listener (:58-59) OK.
- 12 guard v == dropboxButton and startActivity (:67-68) OK. The guard is in the trigger text, not a guard= field (not counted).
- 13 DropboxOauth2AccountActivity.onCreate (:19-21) OK. Citation fix as step 2 (not counted).
- 15 onNewIntent -> fetch (Oauth2AccountActivity.java:59-62) OK. The edge is right; its entry is wrong (step 14).
- 18 onAuthenticated -> DropboxListActivity (DropboxOauth2AccountActivity.java:25-30) OK.
- 19 DropboxListActivity.onCreate (:36) OK (citation fix as step 2, not counted). 20 commit to S_DROPBOX_LIST (:49-56) OK.
- 22 onViewCreated -> refreshList (:173) OK. 23 refreshList -> doInBackground, ASYNC (:181-187) OK (AsyncTask INFERRED).
- 25 $1.call -> initialRetrieve (:184-186) OK (class $1 holds call and initialRetrieve).
- 26 initialRetrieve -> listFiles (DropboxListFragment.java:60) OK.
- 27 listFiles -> $3.subscribe (:143; $3 holds subscribe and parseListFolderResponse) OK.

## Not checked

- No source in the tree (INFERRED): androidx Fragment order (steps 10, 21), RxJava, AsyncTask, Material, Custom Tabs. The auto_calls.json generator was not located.
