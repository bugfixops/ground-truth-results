# AnkiDroid batch 147 (LABEL helper, 2026-10-30). 40 methods in 20 classes, 2 each: BasicTextFieldController$3$1, CardTemplateEditor$3,
# ColorWrap, CompatV19$1, CompatV19$2, CustomTabActivityHelper, DeckOptions$DeckPreferenceHack$Editor$1, DeckPicker$26,
# DeckPickerExportCompleteDialog$1, DeckTask, Decks, LanguageListerBase$1, LoadPronounciationActivity$1, Lookup$1, ModelFieldEditor$2,
# ModelFieldEditor$5, ModelFieldEditor$6, MyAccount$1, MyAccount$2, MyAccount$3. Row list: graphs/AnkiDroid/parts/label_147.md.
#
# Labels: each of the 40 methods already has a row in another part (exact name match), so no label is repeated here.
# No UNREACHABLE entry is written: no method is provably never entered.
#
# Route gaps: out/methods.csv marks 7 batch methods UNRESOLVED. The six edges below close six of them:
#   CompatV19$2.onAnimationEnd (part 073 has a REGISTER edge only, which gives no path),
#   DeckPicker$26.onDismissed and DeckPicker$26.onShown (part 005 names the route in text but writes no edge),
#   DeckTask.onCancelled (part 070 names the route in text but writes no edge),
#   CustomTabActivityHelper.onServiceConnected and CustomTabActivityHelper.onServiceDisconnected (part 073 relies on the
#   ServiceConnection wrapper methods, which have no inbound edge; these two edges skip the wrapper, see the notes).
# DeckTask.waitToFinish() is the seventh UNRESOLVED method. It has a conflict with part 070 (see label_147.md), so no edge is written.
# CompatV19$1.onSystemUiVisibilityChange is already REACHABLE through the part 144 edge (CompatV19.setFullScreen), not written here.

e('CompatV19.hideViewWithAnimation', 'CompatV19$2.onAnimationEnd', 'FRAMEWORK',
  'the animator calls the end listener that hideViewWithAnimation sets, when the fade-out ends',
  env=None,
  evidence='SRC com/ichi2/compat/CompatV19.java:78-88; FW-SRC core/java/android/view/ViewPropertyAnimator.java:375-377, 1111-1123',
  note='hideViewWithAnimation sets the listener at CompatV19.java:82 and starts the fade. ViewPropertyAnimator stores the listener in setListener (375-377). Its inner listener onAnimationEnd (1111-1112) calls mListener.onAnimationEnd (1122). The library makes this call, so the kind is FRAMEWORK. Route to the source: CompatV19$1.onSystemUiVisibilityChange calls hideViewWithAnimation (automatic CALL, CompatV19.java:62, 64-65), and part 144 reaches that listener from CompatV19.setFullScreen. MISSING GATE MG672 applies to the chain start, as in parts 073 and 144. The toolbar call at line 62 has no preference gate; the fullscreenMode preference (CompatV19.java:39) gates only lines 63-65. No constant fits, so env is unset.')

e('DeckPicker.handleDeckSelection', 'DeckPicker$26.onDismissed', 'FRAMEWORK',
  'the snackbar that handleDeckSelection shows calls the show/hide callback when it is dismissed',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1746-1754, 1773-1778, 1786-1794, 2151-2168; SRC com/ichi2/anki/UIUtils.java:56-60, 64-80; INFERRED Snackbar.Callback dispatch (support library, no source in the dataset)',
  note='handleDeckSelection (DeckPicker.java:1717) passes mSnackbarShowHideCallback to UIUtils.showSnackbar in three branches: 1746-1754 (study limit reached), 1773-1778 (empty deck) and 1786-1794 (empty schedule). The int overload at UIUtils.java:56-60 delegates to the String overload, which calls sb.setCallback at lines 79-80. The Snackbar dispatch is library code and INFERRED. The empty-deck branch carries MISSING GATE MG6 (label_005.md). handleDeckSelection is REACHABLE in out/methods.csv. No preference or constant gate.')

e('DeckPicker.handleDeckSelection', 'DeckPicker$26.onShown', 'FRAMEWORK',
  'the snackbar that handleDeckSelection shows calls the show/hide callback when it is shown',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1746-1754, 1773-1778, 1786-1794, 2151-2168; SRC com/ichi2/anki/UIUtils.java:56-60, 64-80; INFERRED Snackbar.Callback dispatch (support library, no source in the dataset)',
  note='Same three snackbar branches and the same callback as the onDismissed edge (see that note). The onShown body disables the add-note button (DeckPicker.java:2162-2168). No preference or constant gate.')

e('DeckTask.cancelTask()', 'DeckTask.onCancelled', 'ASYNC',
  'cancel(true) on the running DeckTask makes the framework call the task listener onCancelled',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:168-178 (cancel(true) at 172), 181-186 (cancelTask(int) calls cancelTask() at 184), 367-370; FW-SRC core/java/android/os/AsyncTask.java:525-528, 345-350, 369-376, 691-698, 712, 462-464, 479-480',
  note='cancel(true) sets mCancelled and cancels the future (AsyncTask.java:525-528). The future calls done(), which posts a result through postResultIfNotInvoked (345-350; the CancellationException catch branch is not reprinted in this run). postResult sends MESSAGE_POST_RESULT (369-376), and the handler calls finish (712). finish calls onCancelled(result) when isCancelled (691-693), which calls onCancelled() (462-464). DeckTask.java:368-370 overrides that method and calls mListener.onCancelled() (369). cancelTask() runs only when the latest task is still running (DeckTask.java:171), and cancelTask(int) allows it only for the matching task type (183). Callers: out/methods.csv marks cancelTask() REACHABLE through cancelTask(int). The auto CALL edges out of DeckTask.onCancelled to the listeners whose tasks are never cancelled are suppressed by sup tuples in graph_def.py. CardBrowser$16.onCancelled (search listener, CardBrowser.java:1051, 1080) and CardBrowser$17.onCancelled (render listener, CardBrowser.java:1085, 1114) are not suppressed. Their tasks are cancelled in the app (CardBrowser.java:528-529, 796-797, 1155-1156), so they become live by design. The mapping is inferred from javac anonymous-class order: $13-$15 match the named handlers at 900, 1000 and 1028 by the same count.')

e('CustomTabActivityHelper.bindCustomTabsService', 'CustomTabActivityHelper.onServiceConnected', 'FRAMEWORK',
  'the Custom Tabs service connects after the bind, and the framework calls back into the helper',
  env=None,
  evidence='SRC com/ichi2/compat/customtabs/CustomTabActivityHelper.java:96-104, 120-125; SRC com/ichi2/compat/customtabs/ServiceConnection.java:31-39; INFERRED CustomTabsClient.bindCustomTabsService (support library, no source in the dataset)',
  note='bindCustomTabsService creates ServiceConnection(this) (CustomTabActivityHelper.java:102) and binds it (line 103). The framework calls the ServiceConnection wrapper, which calls the helper callback (ServiceConnection.java:36-38). This edge skips the wrapper because the wrapper methods are outside batch 147. ServiceConnection.onCustomTabsServiceConnected is UNRESOLVED with 0 incoming in out/methods.csv; its owner needs a FRAMEWORK edge from bindCustomTabsService into it. The wrapper-to-helper CALL edge is automatic and stays in place. Gates: bindCustomTabsService returns at line 97 when mClient is already set and at line 100 when no browser package is found (MG673, label_073.md). No constant fits, so env is unset. bindCustomTabsService is REACHABLE in out/methods.csv from AnkiActivity.onStart (AnkiActivity.java:67).')

e('CustomTabActivityHelper.bindCustomTabsService', 'CustomTabActivityHelper.onServiceDisconnected', 'FRAMEWORK',
  'the Custom Tabs service disconnects, and the framework calls back into the helper',
  env=None,
  evidence='SRC com/ichi2/compat/customtabs/CustomTabActivityHelper.java:96-104, 127-131; SRC com/ichi2/compat/customtabs/ServiceConnection.java:41-45; INFERRED CustomTabsClient.bindCustomTabsService (support library, no source in the dataset)',
  note='Same shortcut as the connect edge. The framework calls the wrapper onServiceDisconnected (ServiceConnection.java:41-44), which calls the helper callback at line 44. ServiceConnection.onServiceDisconnected is UNRESOLVED with 0 incoming in out/methods.csv and is outside batch 147; its owner needs the FRAMEWORK edge from bindCustomTabsService. MG673 (label_073.md) applies as on the connect edge.')
