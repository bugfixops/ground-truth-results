# AnkiDroid batch 035 (LABEL helper). MyAccount login activity: 22 methods. The full row list is in
# graphs/AnkiDroid/parts/label_035.md.
#
# Route ownership:
# - CALL edges inside MyAccount (onCreate, initAllContentViews, the $1-$4 constructors and click callbacks, login,
#   logout, resetPassword, saveUserInformation, switchToState, onKeyDown), and the Connection-to-$5 chain
#   (Connection.onPreExecute/onPostExecute/onProgressUpdate/launchConnectionTask), come from auto_calls.json.
#   They are not written here.
# - The INTENT edge DeckPicker.loginToSyncServer -> MyAccount.<init> and the LIFECYCLE chain are already in
#   graph_def.py (lines 1259 and 194-195). They are not written here.
# - Gates: MG292 (logged-out state, login view), MG293 (device offline, $5.onDisconnected, row only),
#   MG294 (request or reply of at least 1024 bytes before the progress callback). Batch range MG292-MG301.

# --- Login view (shown when no hkey is stored; MyAccount.java:92-95).
e('S_MYACCOUNT', 'MyAccount$1.onClick', 'GUI',
  'tap the login button in the login view (both fields filled in)',
  gui=['tap the login button in the login view (both fields filled in)'],
  evidence='SRC com/ichi2/anki/MyAccount.java:177-184, 139-142; SRC com/ichi2/anki/MyAccount.java:92-95',
  note='MISSING GATE MG292: the login view is shown only when no hkey is stored (logged out). No STATE constant covers the logged-out state (STATE_ACCOUNT is logged in). env and needs_state unset. login runs only when both fields are non-empty (MyAccount.java:139-140).')

e('S_MYACCOUNT', 'MyAccount$2.onClick', 'GUI',
  'tap the reset password button in the login view',
  gui=['tap the reset password button in the login view'],
  evidence='SRC com/ichi2/anki/MyAccount.java:187-193, 92-95',
  note='MISSING GATE MG292: the login view is shown only when no hkey is stored (logged out). env and needs_state unset. The handler calls resetPassword (auto CALL, MyAccount.java:191).')

e('S_MYACCOUNT', 'MyAccount$3.onClick', 'GUI',
  'tap the sign up button in the login view (opens the registration page in an external browser)',
  gui=['tap the sign up button in the login view (opens the registration page in an external browser)'],
  evidence='SRC com/ichi2/anki/MyAccount.java:196-202, 92-95',
  note='MISSING GATE MG292: the login view is shown only when no hkey is stored (logged out). env and needs_state unset. The handler calls openUrl (auto CALL, MyAccount.java:199).')

# --- Back key on the MyAccount screen (framework dispatch; no state gate).
e('S_MYACCOUNT', 'MyAccount.onKeyDown', 'GUI',
  'press the back key on the MyAccount screen',
  env=None,
  gui=['press the back key on the MyAccount screen'],
  evidence='SRC com/ichi2/anki/MyAccount.java:221-285; FW-SRC core/java/android/view/KeyEvent.java:2684-2691; FW-SRC core/java/android/app/Activity.java:3255-3272',
  note='Framework route: Activity.dispatchKeyEvent -> KeyEvent.dispatch -> receiver.onKeyDown. The handler finishes the activity with a fade when the key is BACK and the repeat count is 0 (finishWithAnimation, auto CALL).')

# --- Login listener $5 (Connection.TaskListener) on the login task started by MyAccount.login.
e('MyAccount.login', 'MyAccount$5.onPreExecute', 'ASYNC',
  'the login task starts; the listener shows the progress dialog before the background login runs',
  env=ENV_NETWORK,
  evidence='FW-SRC core/java/android/os/AsyncTask.java:632-651; SRC com/ichi2/async/Connection.java:81-87, 124-131; SRC com/ichi2/anki/MyAccount.java:221-285',
  note='Edge from the launcher to the listener callback (label_019 convention). AsyncTask calls onPreExecute on the caller thread (AsyncTask.java:648). Connection.onPreExecute forwards to the listener (auto CALL, Connection.java:129). The task is launched only when isOnline is true (Connection.java:83), so env is ENV_NETWORK.')

e('MyAccount.login', 'MyAccount$5.onPostExecute', 'ASYNC',
  'the background login finishes; the listener saves the account and finishes, or shows an error snackbar',
  env=ENV_NETWORK,
  evidence='FW-SRC core/java/android/os/AsyncTask.java:327-341, 691-697; SRC com/ichi2/async/Connection.java:138-145; SRC com/ichi2/anki/MyAccount.java:221-285',
  note='Edge from the launcher to the listener callback (label_019 convention). AsyncTask.finish calls onPostExecute on the UI thread (AsyncTask.java:695). The success path needs a 200 reply with a key (Connection.java:221-225). Its CALLs (saveUserInformation, finishWithAnimation, snackbars) are in auto_calls.json.')

e('MyAccount.login', 'MyAccount$5.onProgressUpdate', 'ASYNC',
  'the login reply is read and progress is published; the listener body is empty',
  env=ENV_NETWORK,
  evidence='SRC com/ichi2/libanki/sync/HttpSyncer.java:291-319, 393-402; SRC com/ichi2/async/Connection.java:196-225, 471-472; FW-SRC core/java/android/os/AsyncTask.java:684-689, 706-718; SRC com/ichi2/anki/MyAccount.java:221-226',
  note='MISSING GATE MG294: the progress publish runs only when bytesReceived or bytesSent reaches 1024 (HttpSyncer.java:93-94, 312; the request-body writer calls publishProgress at HttpSyncer.java:400), so a login whose request and reply are both under 1024 bytes never reaches this callback. The network part of the route is ENV_NETWORK. Route after publish: Connection.publishProgress (Connection.java:471-472), AsyncTask.publishProgress (AsyncTask.java:684-689), InternalHandler (AsyncTask.java:715), Connection.onProgressUpdate (auto CALL, Connection.java:155).')

# --- UNREACHABLE: the logged-in view is never shown in a standard run (no hkey at launch; notLoggedIn always set).
UNREACHABLE['MyAccount.logout'] = ('branch_never_taken',
  "The only caller is MyAccount$4.onClick (auto CALL, MyAccount.java:211, via access$200). A grep of logout() over the source root shows no other caller. "
  "The logged-in view is shown only by switchToState(STATE_LOGGED_IN): from onCreate when hkey is stored (MyAccount.java:92-93), or from the success path when the notLoggedIn extra is absent (MyAccount.java:250-256). "
  "A standard launch has no hkey (DeckPicker.java:1278-1282, 1422-1430) and always sends notLoggedIn=true (DeckPicker.java:1571-1573), so the success path finishes (MyAccount.java:251-252) and neither branch runs.",
  'SRC com/ichi2/anki/MyAccount.java:147-161, 211, 92-95, 250-256; SRC com/ichi2/anki/DeckPicker.java:1278-1282, 1422-1430, 1569-1574',
  'SOURCE')

UNREACHABLE['MyAccount$4.onClick'] = ('branch_never_taken',
  "Logout button of the logged-in view. That view is shown only through switchToState(STATE_LOGGED_IN), which a standard run never reaches: hkey is empty at launch (DeckPicker.java:1278-1282, 1422-1430) and the launch always sends notLoggedIn=true (DeckPicker.java:1571-1573), so the success path finishes instead (MyAccount.java:251-252). "
  "The only route to this onClick goes through that view, so the branch is never taken. Its CALL to MyAccount.logout (MyAccount.java:211) is in auto_calls.json.",
  'SRC com/ichi2/anki/MyAccount.java:207-214, 92-95, 250-256; SRC com/ichi2/anki/DeckPicker.java:1278-1282, 1422-1430, 1571-1573',
  'SOURCE')
