# batch 040 (label_040): core/UIHelper (19 methods), UIHelper$1 family (8), UIHelper$2 and $3 (4),
# UIHelper_MembersInjector (4), core/bundlers/MoneyBundler (3): 38 methods, 25 REACHABLE, 13 UNREACHABLE, 0 UNRESOLVED.
# Rows and printed lines: graphs/MMEX/parts/label_040.md. Grep output: graphs/MMEX/parts/label_040.grep.txt.
# CALL edges come from auto_calls.json (none written here, D7). Edges written here: 2 FRAMEWORK edges (runOnUiThread runnables)
# and 4 FRAMEWORK edges into MoneyBundler.get and put from the Icepick helpers (D1: this batch owns those destinations).
# sup cuts: 8 auto CALL records whose caller is UNREACHABLE in this batch (D14).
# The icepick library (not in dataset), the generated helpers and Dagger classes (not in source root) are INFERRED (D5, D16).

# ================================================================== FRAMEWORK edges (runOnUiThread runnables)

e('UIHelper.showToast(int,int)', 'UIHelper$2.run', 'FRAMEWORK',
  'showToast(int,int) passes the anonymous Runnable to Activity.runOnUiThread; the framework runs run() on the UI thread',
  evidence='SRC core/UIHelper.java:226-231 (runOnUiThread 226, run 228-230); FW-SRC core/java/android/app/Activity.java:6170-6176 (runOnUiThread hands the action to the UI thread, directly or via mHandler.post)')

e('UIHelper.showToast(String,int)', 'UIHelper$3.run', 'FRAMEWORK',
  'showToast(String,int) passes the anonymous Runnable to Activity.runOnUiThread; the framework runs run() on the UI thread',
  evidence='SRC core/UIHelper.java:240-245 (runOnUiThread 240, run 242-244); FW-SRC core/java/android/app/Activity.java:6170-6176')

# ================================================================== icepick edges into MoneyBundler (INFERRED: icepick library not in dataset)

e('CalculatorActivity$$Icepick.restore', 'MoneyBundler.get', 'FRAMEWORK',
  'Icepick restores the @State field mAmount through the custom bundler: the library calls get(key, bundle) from the generated restore method',
  cls='non_standard', via='icepick library Helper.getWithBundler (library not in dataset); restore is started by MmxBaseFragmentActivity.onCreate:74 (batch 027, label_027.py:127)',
  evidence='SRC core/bundlers/MoneyBundler.java:38-41 (get); SRC common/CalculatorActivity.java:76 (@State(MoneyBundler.class) mAmount); SRC common/MmxBaseFragmentActivity.java:74 (Icepick.restoreInstanceState, no app-side guard); icepick library and CalculatorActivity$$Icepick not in the source root: INFERRED, source not read')

e('CalculatorActivity$$Icepick.save', 'MoneyBundler.put', 'FRAMEWORK',
  'Icepick saves the @State field mAmount through the custom bundler: the library calls put(key, value, bundle) from the generated save method',
  cls='non_standard', via='icepick library Helper.putWithBundler (library not in dataset); save is started by MmxBaseFragmentActivity.onSaveInstanceState:155 (batch 027, label_027.py:132)',
  evidence='SRC core/bundlers/MoneyBundler.java:33-35 (put); SRC common/CalculatorActivity.java:76; SRC common/MmxBaseFragmentActivity.java:151-156 (Icepick.saveInstanceState at 155); icepick library not in the source root: INFERRED, source not read')

e('AmountInputDialog$$Icepick.restore', 'MoneyBundler.get', 'FRAMEWORK',
  'Icepick restores the @State field mAmount through the custom bundler: the library calls get(key, bundle) from the generated restore method',
  cls='non_standard', via='icepick library Helper.getWithBundler (library not in dataset); restore is started by AmountInputDialog.restoreSavedInstanceState (batch 023, label_023.py:77) from Icepick.restoreInstanceState at AmountInputDialog.java:417',
  guard='onCreate received a non-null savedInstanceState (AmountInputDialog.java:148-150), as in batch 023',
  evidence='SRC core/bundlers/MoneyBundler.java:38-41 (get); SRC common/AmountInputDialog.java:122 (@State mAmount), 417 (Icepick.restoreInstanceState); icepick library not in the dataset: INFERRED, source not read')

e('AmountInputDialog$$Icepick.save', 'MoneyBundler.put', 'FRAMEWORK',
  'Icepick saves the @State field mAmount through the custom bundler: the library calls put(key, value, bundle) from the generated save method',
  cls='non_standard', via='icepick library Helper.putWithBundler (library not in dataset); save is started by AmountInputDialog.onSaveInstanceState (batch 023, label_023.py:93) from Icepick.saveInstanceState at AmountInputDialog.java:294',
  evidence='SRC core/bundlers/MoneyBundler.java:33-35 (put); SRC common/AmountInputDialog.java:122 (@State mAmount), 294 (Icepick.saveInstanceState); icepick library not in the dataset: INFERRED, source not read')

# ================================================================== sup cuts (D14): auto CALL records whose caller is UNREACHABLE in this batch

sup(('UIHelper.binaryDialog(int,int)', 'UIHelper.binaryDialog(int,int,int,int)'),
    ('UIHelper.binaryDialog(int,int,int,int)', 'UIHelper$1.<init>'),
    ('UIHelper$1.call', 'UIHelper$1$1.<init>'),
    ('UIHelper$1.call', 'UIHelper$1$2.<init>'),
    ('UIHelper$1.call', 'UIHelper$1$3.<init>'),
    ('UIHelper$1.call', 'UIHelper.getContext'),
    ('UIHelper_MembersInjector.create', 'UIHelper_MembersInjector.<init>'),
    ('UIHelper_MembersInjector.injectMembers', 'UIHelper_MembersInjector.injectAppSettingsLazy'))

# ================================================================== UNREACHABLE (batch 040)

UNREACHABLE['UIHelper.binaryDialog(int,int)'] = ('no_trigger_in_app',
  'Two-argument overload. Its only app caller is SyncPreferenceFragment.checkIfLocalFileExistsAndDownload (line 286). That method runs only from handleFileSelection (line 159), which runs only from onActivityResult (lines 97-98) when requestCode == REQUEST_REMOTE_FILE (1). The only sender of code 1 is the commented-out startActivityForResult at SyncPreferenceFragment.java:202, and grep finds no other use of REQUEST_REMOTE_FILE. The dialog is never shown. The auto CALL to the four-argument overload is cut with sup.',
  'SRC sync/SyncPreferenceFragment.java:63, 97-98, 130, 159, 202, 279, 286; SRC core/UIHelper.java:85-87; label_040.grep.txt sections 1-2. The framework dispatch to onActivityResult is INFERRED; the absence of any active sender is SOURCE.',
  'SOURCE')

UNREACHABLE['UIHelper.binaryDialog(int,int,int,int)'] = ('no_trigger_in_app',
  'Four-argument overload. Callers: binaryDialog(int,int) (UIHelper.java:86, same batch, sup-cut) and SyncPreferenceFragment.handleFileSelection (lines 145-146). handleFileSelection has no live caller (see binaryDialog(int,int)). This method builds the Observable whose OnSubscribe is UIHelper$1.',
  'SRC core/UIHelper.java:85-91; SRC sync/SyncPreferenceFragment.java:130, 145-146, 202; label_040.grep.txt sections 1-2',
  'SOURCE')

UNREACHABLE['UIHelper$1.<init>'] = ('no_trigger_in_app',
  'Anonymous OnSubscribe created only in binaryDialog(int,int,int,int) at UIHelper.java:91. That method has no live caller (see above), so the object is never created.',
  'SRC core/UIHelper.java:91; label_040.grep.txt section 1',
  'SOURCE')

UNREACHABLE['UIHelper$1.call'] = ('no_trigger_in_app',
  'OnSubscribe.call (UIHelper.java:93). It runs only when the rx Observable.create library call subscribes to the Observable from binaryDialog(int,int,int,int), which is never built. Its auto CALLs to getContext (94) and to UIHelper$1$1.<init> (97), UIHelper$1$2.<init> (96) and UIHelper$1$3.<init> (116) are cut with sup.',
  'SRC core/UIHelper.java:91-126; label_040.grep.txt section 1; rx Observable.create is a library call: INFERRED',
  'INFERRED')

UNREACHABLE['UIHelper$1$1.<init>'] = ('no_trigger_in_app',
  'Positive-button OnClickListener created in UIHelper$1.call (UIHelper.java:97). That method is unreachable (see UIHelper$1.call), so the listener is never created.',
  'SRC core/UIHelper.java:97; label_040.grep.txt section 1',
  'INFERRED')

UNREACHABLE['UIHelper$1$1.onClick'] = ('no_trigger_in_app',
  'Positive-button click handler (UIHelper.java:99-102). It runs only for an AlertDialog built in UIHelper$1.call, which never runs.',
  'SRC core/UIHelper.java:97-103; label_040.grep.txt section 1',
  'INFERRED')

UNREACHABLE['UIHelper$1$2.<init>'] = ('no_trigger_in_app',
  'Negative-button OnClickListener created in UIHelper$1.call (UIHelper.java:96). That method is unreachable (see UIHelper$1.call), so the listener is never created.',
  'SRC core/UIHelper.java:96; label_040.grep.txt section 1',
  'INFERRED')

UNREACHABLE['UIHelper$1$2.onClick'] = ('no_trigger_in_app',
  'Negative-button click handler (UIHelper.java:106-109). It runs only for an AlertDialog built in UIHelper$1.call, which never runs.',
  'SRC core/UIHelper.java:104-110; label_040.grep.txt section 1',
  'INFERRED')

UNREACHABLE['UIHelper$1$3.<init>'] = ('no_trigger_in_app',
  'Action0 cleanup object created in UIHelper$1.call (UIHelper.java:116). That method is unreachable (see UIHelper$1.call), so the object is never created.',
  'SRC core/UIHelper.java:116; label_040.grep.txt section 1',
  'INFERRED')

UNREACHABLE['UIHelper$1$3.call'] = ('no_trigger_in_app',
  'Subscription cleanup action that dismisses the dialog (UIHelper.java:118-120). It runs only when the subscription from UIHelper$1.call is unsubscribed, which never happens.',
  'SRC core/UIHelper.java:116-121; label_040.grep.txt section 1',
  'INFERRED')

UNREACHABLE['UIHelper_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger factory method (generated, not in the source root). Its only auto record is create -> <init> (UIHelper_MembersInjector.java:22). No record has create as dst (grep section 6; auto_calls.json method index at line 82242 only). DaggerMmxComponent.injectUIHelper calls the static injectAppSettingsLazy directly (DaggerMmxComponent.java:578), not create. The create -> <init> edge is cut with sup.',
  'label_040.grep.txt sections 6 and 15; auto_calls.json (create -> <init> record); DaggerMmxComponent.java:338, 578',
  'INFERRED')

UNREACHABLE['UIHelper_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Generated constructor (not in the source root). Its only caller is UIHelper_MembersInjector.create (auto record, UIHelper_MembersInjector.java:22), and create has no caller (see above). The create -> <init> edge is cut with sup.',
  'label_040.grep.txt sections 6 and 15; auto_calls.json (create -> <init> record)',
  'INFERRED')

UNREACHABLE['UIHelper_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Instance member injector (generated). No record has it as dst (grep section 6). The component injects UIHelper through the static injectAppSettingsLazy (DaggerMmxComponent.java:578), not through injectMembers. Its auto CALL to injectAppSettingsLazy (UIHelper_MembersInjector.java:27) is cut with sup.',
  'label_040.grep.txt sections 6 and 15; auto_calls.json (injectMembers -> injectAppSettingsLazy record); DaggerMmxComponent.java:578',
  'INFERRED')
