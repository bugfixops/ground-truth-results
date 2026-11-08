import sys
sys.path.insert(0, '/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch')
from r1b_tool import apply, add_gate_entries

# D1: the Dropbox button edge gets its guard (DownloadTabFragment.java:67-69); the AnyMemo edge already has one
apply([
    ("e('DownloadTabFragment.onClick', 'DropboxOauth2AccountActivity.<init>', 'ENTRY', 'v == dropboxButton: startActivity(DropboxOauth2AccountActivity)', evidence='SRC ui/DownloadTabFragment.java:67-69')",
     "e('DownloadTabFragment.onClick', 'DropboxOauth2AccountActivity.<init>', 'ENTRY', 'v == dropboxButton: startActivity(DropboxOauth2AccountActivity)', guard='v == dropboxButton (DownloadTabFragment.java:67-69)', evidence='SRC ui/DownloadTabFragment.java:67-69')"),
], 'D1')

# D2: DropboxOauth2AccountActivity: onCreate calls super.onCreate (line 21); onNewIntent is entered from the browser redirect.
# The onDestroy edge of the old loop is removed here; its replacement is decided in A1.
apply([
    ("for cb in ('onCreate', 'onDestroy', 'onNewIntent'):\n"
     "    e('DropboxOauth2AccountActivity.onCreate', 'Oauth2AccountActivity.' + cb, 'LIFECYCLE', 'Activity lifecycle / framework callback (DropboxOauth2AccountActivity does not override these)', evidence=FW_ACTIVITY + '; SRC downloader/oauth/Oauth2AccountActivity.java:37-63')\n",
     "# Round 1b D2: the old loop (onCreate, onDestroy, onNewIntent as lifecycle steps) is replaced. super.onCreate is a CALL (DropboxOauth2AccountActivity.java:21).\n"
     "# onNewIntent is entered by the browser redirect into the running activity (AndroidManifest.xml:79,86), so its entry comes from the login screen.\n"
     "e('DropboxOauth2AccountActivity.onCreate', 'Oauth2AccountActivity.onCreate', 'CALL', 'super.onCreate(savedInstanceState)', evidence='SRC downloader/dropbox/DropboxOauth2AccountActivity.java:21')\n"
     "e('S_DROPBOX_LOGIN', 'Oauth2AccountActivity.onNewIntent', 'ENTRY', 'browser redirect reaches the running singleTask activity (framework redirect delivery INFERRED)', needs_state=state_text('the Dropbox login page was opened by requestAuth() and this activity is still alive', ('session',)), env=ENV_OAUTH_CALLBACK, evidence='SRC downloader/oauth/Oauth2AccountActivity.java:59-62; AndroidManifest.xml:79,86')\n"),
], 'D2')

# D3: the wrong fetch edge (fetchTokenAndOnAuthenticate -> $2.onComplete) is removed; the fetch success edge to $1.onSuccess exists
apply([
    ("e('Oauth2AccountActivity.fetchTokenAndOnAuthenticate', 'Oauth2AccountActivity$2.onComplete', 'FRAMEWORK', 'fetchAuthTokenFromCallback(uri) (a Single) succeeds on the main thread', env=ENV_OAUTH_CALLBACK, evidence=FW_RX + '; SRC downloader/oauth/Oauth2AccountActivity.java:85-103')\n",
     "# Round 1b D3: removed. The fetch path (fetchTokenAndOnAuthenticate, Oauth2AccountActivity.java:85-103) goes to $1.onSuccess and $1.onError only.\n"),
], 'D3')

# D4(a): fetch success -> onAuthenticated: no saved token on this path, so no needs_state; env is the browser callback
# D4(b): verify success -> onAuthenticated (line 114): needs_state NEED_SAVED_TOKEN, verify env (see the log: ENV_DROPBOX, not ENV_NET)
# D4(c): verify -> $2.onComplete (the verify edge now targets it); duplicate verify -> $2.onComplete removed
# D4(d): verify error path -> requestAuth is renamed to $2.onError (Oauth2AccountActivity.java:118-121)
apply([
    ("e('Oauth2AccountActivity$1.onSuccess', 'DropboxOauth2AccountActivity.onAuthenticated', 'CALL', 'onAuthenticated(token)', needs_state=NEED_SAVED_TOKEN, env=ENV_NET, evidence='SRC downloader/oauth/Oauth2AccountActivity.java:93; downloader/dropbox/DropboxOauth2AccountActivity.java:25-30')",
     "e('Oauth2AccountActivity$1.onSuccess', 'DropboxOauth2AccountActivity.onAuthenticated', 'CALL', 'onAuthenticated(token)', env=ENV_OAUTH_CALLBACK, evidence='SRC downloader/oauth/Oauth2AccountActivity.java:93; downloader/dropbox/DropboxOauth2AccountActivity.java:25-30')"),
    ("e('Oauth2AccountActivity$2.onComplete', 'DropboxOauth2AccountActivity.onAuthenticated', 'CALL', 'onAuthenticated(token)', env=ENV_OAUTH_CALLBACK, evidence='SRC downloader/oauth/Oauth2AccountActivity.java:93')",
     "e('Oauth2AccountActivity$2.onComplete', 'DropboxOauth2AccountActivity.onAuthenticated', 'CALL', 'onAuthenticated(token): the saved token passed the verify call, then the list opens', needs_state=NEED_SAVED_TOKEN, env=ENV_DROPBOX, evidence='SRC downloader/oauth/Oauth2AccountActivity.java:114')"),
    ("e('Oauth2AccountActivity.verifyTokenAndOnAuthenticate', 'Oauth2AccountActivity$1.onSuccess', 'FRAMEWORK', 'verifyAccessToken(token) (a Completable) completes on the main thread', needs_state=NEED_SAVED_TOKEN, env=ENV_NET, evidence=FW_RX + '; SRC downloader/oauth/Oauth2AccountActivity.java:105-123')",
     "e('Oauth2AccountActivity.verifyTokenAndOnAuthenticate', 'Oauth2AccountActivity$2.onComplete', 'FRAMEWORK', 'verifyAccessToken(token) (a Completable) completes on the main thread', needs_state=NEED_SAVED_TOKEN, env=ENV_DROPBOX, evidence=FW_RX + '; SRC downloader/oauth/Oauth2AccountActivity.java:105-123')"),
    ("e('Oauth2AccountActivity.verifyTokenAndOnAuthenticate', 'Oauth2AccountActivity$2.onComplete', 'FRAMEWORK', 'the framework calls onComplete (DisposableCompletableObserver) at downloader/oauth/Oauth2AccountActivity.java:110', evidence=FW_RX + '; SRC downloader/oauth/Oauth2AccountActivity.java:110-123')\n",
     "# Round 1b D4(c): duplicate verify -> $2.onComplete removed (the verify edge above now targets it)\n"),
    ("e('Oauth2AccountActivity$1.onError', 'Oauth2AccountActivity.requestAuth', 'CALL', 'the saved token is no longer valid', needs_state=NEED_SAVED_TOKEN, env=ENV_NET, evidence='SRC downloader/oauth/Oauth2AccountActivity.java:97-101')",
     "e('Oauth2AccountActivity$2.onError', 'Oauth2AccountActivity.requestAuth', 'CALL', 'the saved token is no longer valid (verify error path)', needs_state=NEED_SAVED_TOKEN, env=ENV_DROPBOX, evidence='SRC downloader/oauth/Oauth2AccountActivity.java:118-121')"),
], 'D4 edges')

# D4: GATE env for the fetch path (browser callback). The verify GATE entries stay ENV_DROPBOX (see the log).
apply([
    ("    ('Oauth2AccountActivity.fetchTokenAndOnAuthenticate', 'Oauth2AccountActivity$1.onError'): {'env': ENV_DROPBOX},",
     "    ('Oauth2AccountActivity.fetchTokenAndOnAuthenticate', 'Oauth2AccountActivity$1.onError'): {'env': ENV_OAUTH_CALLBACK},"),
    ("    ('Oauth2AccountActivity.fetchTokenAndOnAuthenticate', 'Oauth2AccountActivity$1.onSuccess'): {'env': ENV_DROPBOX},",
     "    ('Oauth2AccountActivity.fetchTokenAndOnAuthenticate', 'Oauth2AccountActivity$1.onSuccess'): {'env': ENV_OAUTH_CALLBACK},"),
], 'D4 gate')

# D6: rows. The getView edge is drawn once, after addList (shared). RetrieveTask.onPostExecute@X adds the rows (AbstractDownloaderFragment.java:229-230).
# The row click starts from RetrieveTask.onPostExecute@X (the host's rows), not from onCreateView@X.
apply([
    ("    e(DL_AB + '.onCreateView' + hv, DL_AB + '$DownloadListAdapter.getView', 'FRAMEWORK', 'framework calls getView on the object created at downloader/common/AbstractDownloaderFragment.java:158', evidence=FW_VIEW + '; SRC downloader/common/AbstractDownloaderFragment.java:158')\n",
     "    # Round 1b D6: the getView edge is no longer drawn from onCreateView@X; it is drawn once, from addList (below the loop)\n"),
    ("    e(DL_AB + '.onCreateView' + hv, DL_LN + '.onClick' + hv, 'FRAMEWORK', 'tap a row (category, back, or a database)', gui=['Tap a row in the download list'], evidence=FW_VIEW + '; SRC downloader/common/AbstractDownloaderFragment.java:409-438')",
     "    e(DL_RT + '.onPostExecute' + hv, DL_LN + '.onClick' + hv, 'FRAMEWORK', 'tap a row (category, back, or a database) once the list is shown; the row listener is set in getView', env=h_env, gui=['Tap a row in the download list'], evidence=FW_VIEW + '; SRC downloader/common/AbstractDownloaderFragment.java:229-230, 386-411, 409-438')"),
    ("    e(DL_RT + '.onPostExecute' + hv, h_cls + '.hasMore', 'CALL', 'hasMore() decides whether the Load-more footer is shown', evidence='SRC downloader/common/AbstractDownloaderFragment.java:231')\n",
     "    e(DL_RT + '.onPostExecute' + hv, h_cls + '.hasMore', 'CALL', 'hasMore() decides whether the Load-more footer is shown', evidence='SRC downloader/common/AbstractDownloaderFragment.java:231')\n"
     "    e(DL_RT + '.onPostExecute' + hv, DL_AB + '$DownloadListAdapter.addList', 'CALL', 'dlAdapter.addList(downloadItems): the rows of the retrieved list are added', evidence='SRC downloader/common/AbstractDownloaderFragment.java:229-230')\n"),
    ("# therefore appears only on the refresh path. The row listener is registered in the shared getView; the edge is drawn\n"
     "# from onCreateView@X so that each host's rows lead to that host's methods.\n",
     "# therefore appears only on the refresh path. The row listener is registered in the shared getView; the row-click edge is drawn\n"
     "# from RetrieveTask.onPostExecute@X (the host's rows are added there, AbstractDownloaderFragment.java:229-230), not from onCreateView@X.\n"),
    ("# ---- shared leaves: no host-specific callee; each dialog only shows a message\n",
     "# Round 1b D6: rows are laid out by the framework after addList (one shared node; the row listener is set in getView)\n"
     "e(DL_AB + '$DownloadListAdapter.addList', DL_AB + '$DownloadListAdapter.getView', 'FRAMEWORK', 'the ListView lays out the new rows and calls getView (layout timing INFERRED)', evidence=FW_VIEW + '; fw_src android-8.1.0_r1 widget/ArrayAdapter.java:345 (notifyDataSetChanged), BaseAdapter.java:51, AbsListView.java:6406 (onChanged), 1989 (requestLayout), 2348 (obtainView calls getView)')\n"
     "# ---- shared leaves: no host-specific callee; each dialog only shows a message\n"),
], 'D6')

# D7: fetch path: FetchDatabaseTask.onPreExecute becomes per host, then ASYNC to doInBackground; the direct jump is removed.
# RetrieveTask refresh path: the same shape (refreshList -> onPreExecute, and the direct jump to doInBackground).
# The row-click edge into the shared RetrieveTask.onPreExecute stays: that node has no outgoing edge, so it cannot fan out.
apply([
    ("    e(DL_AB + '.startFetchDatabaseTask' + hv, DL_FT + '.onPreExecute', 'ASYNC', 'new FetchDatabaseTask().execute(item): onPreExecute runs on the calling (main) thread first', evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:294-297')\n",
     "    e(DL_AB + '.startFetchDatabaseTask' + hv, DL_FT + '.onPreExecute' + hv, 'ASYNC', 'new FetchDatabaseTask().execute(item): onPreExecute runs on the calling (main) thread first', evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:294-297')\n"
     "    e(DL_FT + '.onPreExecute' + hv, DL_FT + '.doInBackground' + hv, 'ASYNC', 'the worker thread runs doInBackground after onPreExecute', evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:305-316')\n"),
    ("    e(DL_AB + '.startFetchDatabaseTask' + hv, DL_FT + '.doInBackground' + hv, 'ASYNC', 'new FetchDatabaseTask().execute(item): the worker thread runs doInBackground', evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:294-297')\n",
     "    # Round 1b D7: the direct startFetchDatabaseTask -> doInBackground edge is removed (doInBackground follows onPreExecute, see above)\n"),
    ("    e(DL_AB + '.refreshList' + hv, DL_RT + '.onPreExecute', 'ASYNC', 'new RetrieveTask().execute(): onPreExecute runs on the calling (main) thread first', evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:181-187')\n",
     "    e(DL_AB + '.refreshList' + hv, DL_RT + '.onPreExecute' + hv, 'ASYNC', 'new RetrieveTask().execute(): onPreExecute runs on the calling (main) thread first', evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:181-187')\n"
     "    e(DL_RT + '.onPreExecute' + hv, DL_RT + '.doInBackground' + hv, 'ASYNC', 'the worker thread runs doInBackground of RetrieveTask (its Callable is initialRetrieve)', evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:181-187')\n"),
    ("    e(DL_AB + '.refreshList' + hv, DL_RT + '.doInBackground' + hv, 'ASYNC', 'the worker thread runs doInBackground of RetrieveTask (its Callable is initialRetrieve)', evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:181-187')\n",
     "    # Round 1b D7 (RetrieveTask): the direct refreshList -> doInBackground edge is removed (doInBackground follows the host's onPreExecute)\n"),
], 'D7')

# D8: the database branch of the row click (AbstractDownloaderFragment.java:433-435) runs only when the row is neither Category nor Back
apply([
    ("    e(DL_LN + '.onClick' + hv, DL_AB + '.showFetchDatabaseDialog' + hv, 'CALL', 'the row is a database (or a Dropbox file)', evidence='SRC downloader/common/AbstractDownloaderFragment.java:433-435')",
     "    e(DL_LN + '.onClick' + hv, DL_AB + '.showFetchDatabaseDialog' + hv, 'CALL', 'the row is a database (or a Dropbox file)', guard='row is neither Category nor Back (AbstractDownloaderFragment.java:417, 425)', evidence='SRC downloader/common/AbstractDownloaderFragment.java:433-435')"),
], 'D8')

# D9: AnyMemoDownloaderFragment.fetchDatabase has two download branches (lines 79-85). Only the :85 call is automatic,
# so both are written by hand (a hand edge on the pair hides the automatic call, see build_graph.py add_auto_edges).
apply([
    ("e('AnyMemoDownloaderFragment.onCreate', 'S_DOWNLOAD_AM', 'ENTERS',",
     "# Round 1b D9: the two download branches of fetchDatabase (AnyMemoDownloaderFragment.java:79-85), one hand CALL each\n"
     "e('AnyMemoDownloaderFragment.fetchDatabase', 'DownloaderUtils.downloadFile', 'CALL', 'fileName ends with .db: downloadFile(address, filePath), filePath = AMEnv.DEFAULT_ROOT_PATH + fileName', guard='fileName ends with .db (AnyMemoDownloaderFragment.java:79-81)', evidence='SRC downloader/anymemo/AnyMemoDownloaderFragment.java:81')\n"
     "e('AnyMemoDownloaderFragment.fetchDatabase', 'DownloaderUtils.downloadFile', 'CALL', 'fileName ends with .zip: downloadFile(address, zipFilePath), zipFilePath = AMEnv.DEFAULT_TMP_PATH + fileName', guard='fileName ends with .zip (AnyMemoDownloaderFragment.java:83-85)', evidence='SRC downloader/anymemo/AnyMemoDownloaderFragment.java:85')\n"
     "e('AnyMemoDownloaderFragment.onCreate', 'S_DOWNLOAD_AM', 'ENTERS',"),
], 'D9')

# D10: DropboxApiHelper$3.subscribe calls at lines 156, 164, 178, 186. Each call site gets a hand CALL (the pair hides the automatic ones).
apply([
    ("e('DropboxApiHelper.listFiles', 'DropboxApiHelper$3.subscribe', 'FRAMEWORK',",
     "# Round 1b D10: the four helper calls of DropboxApiHelper$3.subscribe (DropboxApiHelper.java:155-186); one hand CALL per site\n"
     "e('DropboxApiHelper$3.subscribe', 'DropboxApiHelper.parseListFolderResponse', 'CALL', 'first list_folder page is parsed', guard='first list_folder response successful (DropboxApiHelper.java:155-158)', evidence='SRC downloader/dropbox/DropboxApiHelper.java:164')\n"
     "e('DropboxApiHelper$3.subscribe', 'DropboxApiHelper.parseListFolderResponse', 'CALL', 'a continuation page is parsed (the has_more loop)', guard='hasMore is true and the continuation response is successful (DropboxApiHelper.java:167, 177-180)', evidence='SRC downloader/dropbox/DropboxApiHelper.java:186')\n"
     "e('DropboxApiHelper$3.subscribe', 'DropboxApiHelper.getResponseErrorString', 'CALL', 'the first list_folder response failed: the error text is built', guard='first response failed (DropboxApiHelper.java:155-158)', evidence='SRC downloader/dropbox/DropboxApiHelper.java:156')\n"
     "e('DropboxApiHelper$3.subscribe', 'DropboxApiHelper.getResponseErrorString', 'CALL', 'a continuation response failed: the error text is built', guard='continuation failed (DropboxApiHelper.java:177-180)', evidence='SRC downloader/dropbox/DropboxApiHelper.java:178')\n"
     "e('DropboxApiHelper.listFiles', 'DropboxApiHelper$3.subscribe', 'FRAMEWORK',"),
], 'D10')

# D11: the inherited Fragment.onCreate cannot be a node (build_graph.py:350 rejects endpoints that are not app methods or screens).
# Fallback: the onAttach -> onCreateView edge keeps its endpoints and its trigger text names the inherited onCreate step.
apply([
    ("e('DownloadTabFragment.onAttach', 'DownloadTabFragment.onCreateView', 'LIFECYCLE', 'Fragment lifecycle callback', evidence=FW_FRAG + '; SRC ui/DownloadTabFragment.java:52-61')",
     "e('DownloadTabFragment.onAttach', 'DownloadTabFragment.onCreateView', 'LIFECYCLE', 'Fragment lifecycle callback; the inherited Fragment.onCreate (not overridden in DownloadTabFragment) runs in between', evidence=FW_FRAG + '; SRC ui/DownloadTabFragment.java:52-61')"),
], 'D11')

# D12: DBX only, the Dropbox list fragment's own onCreate reads the token from the activity extras
apply([
    ("    hv = '@' + h_key\n    for cb in ('onAttach', 'onCreate'):\n",
     "    hv = '@' + h_key\n"
     "    if h_key == 'DBX':\n"
     "        # Round 1b D12: DropboxListFragment.onCreate reads authToken from the arguments (DropboxListFragment.java:49-55)\n"
     "        e(h_page, 'DropboxListFragment.onCreate', 'LIFECYCLE', 'fragment onCreate reads authToken from args', needs_state=state_text('the Dropbox token arrived in the activity extras (DropboxListActivity.java:42-43)', ('session',)), evidence='SRC downloader/dropbox/DropboxListFragment.java:49-55')\n"
     "    for cb in ('onAttach', 'onCreate'):\n"),
], 'D12')

# D13: the guard on the refresh Callable (the one Callable of refreshList, AbstractDownloaderFragment.java:208-212)
apply([
    ("    e(DL_RT + '.doInBackground' + hv, DL_AB + '$1.call' + hv, 'CALL', 'task.call(): runs the Callable, which returns initialRetrieve()', evidence='SRC downloader/common/AbstractDownloaderFragment.java:208-212')",
     "    e(DL_RT + '.doInBackground' + hv, DL_AB + '$1.call' + hv, 'CALL', 'task.call(): runs the Callable, which returns initialRetrieve()', guard='refresh path: the one Callable from refreshList (AbstractDownloaderFragment.java:208-212; for-loop at :210)', evidence='SRC downloader/common/AbstractDownloaderFragment.java:208-212')"),
], 'D13')

# GATE for the Dropbox fetch and verify edges (D3, D4 notes): the GATE above already changed the fetch env. Nothing else here.
print('D script done')
