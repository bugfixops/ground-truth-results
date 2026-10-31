"""Round 1b Group A: onDestroy exits (A1) and rotation of AnyMemo (A2).
All replacements are in one apply() call, so graph_def.py is written only if every anchor matches exactly once."""
import sys
sys.path.insert(0, '/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch')
from r1b_tool import apply

PAIRS = []

# ---- A1 QACardActivity: the direct onCreate -> onDestroy edge is removed (no finish() in the class)
PAIRS.append((
"e('QACardActivity.onCreate', 'QACardActivity.onDestroy', 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACTIVITY + '; SRC ui/QACardActivity.java:488-503')",
"""# A1 (round 1b): the direct onCreate -> onDestroy edge is removed. QACardActivity.java has no finish(), so onCreate does not end
# the activity. Its onDestroy runs only as super.onDestroy() of CardPlayerActivity, StudyActivity and PreviewEditActivity
# (automatic CALL edges from auto_calls.json), so it is reached through those subclass exits (SRC ui/QACardActivity.java:488-503)."""))

# ---- A1 StatisticsScreen: the direct onCreate -> onDestroy edge is replaced by the Back press
PAIRS.append((
"e('StatisticsScreen.onCreate', 'StatisticsScreen.onDestroy', 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACTIVITY + '; SRC ui/StatisticsScreen.java:78-155')",
"""# A1 (round 1b): the direct onCreate -> onDestroy edge is removed. StatisticsScreen.java has no finish() and no onBackPressed.
# Its Up/home item only opens the drawer (StatisticsScreen.java:110-112), so the exit is the default Back press on the chart screen.
e('S_STATISTICS', 'StatisticsScreen.onDestroy', 'SYSTEM', 'press Back on the Statistics screen: the default back press finishes the activity, then onDestroy',
  gui=['Press Back on the Statistics screen'], env=ENV_HW_KEY,
  evidence='FW-SRC core/java/android/app/Activity.java:3001-3010 (onBackPressed -> finishAfterTransition -> finish), :5580-5584, :7203-7208 (performDestroy -> onDestroy); SRC ui/StatisticsScreen.java:108-116 (no onBackPressed, no finish()); common/BaseActivity.java has no onBackPressed')"""))

# ---- A1 ExportAnyMemoDbFragment: the unguarded onCreate -> onDestroy loop is replaced by the three dismiss() paths
PAIRS.append((
"""for cb in ('onDestroy',):
    e('ExportAnyMemoDbFragment.onCreate', 'ExportAnyMemoDbFragment.' + cb, 'LIFECYCLE', 'DialogFragment lifecycle callback', evidence=FW_DIALOGFRAG + '; SRC ui/ExportAnyMemoDbFragment.java:54-60')""",
"""# A1 (round 1b): the loop (onCreate -> onDestroy, no guard) is replaced by the three dismiss() paths. onDestroy follows a dismiss.
e('ExportAnyMemoDbFragment$2.accept', 'ExportAnyMemoDbFragment.onDestroy', 'LIFECYCLE', 'the export succeeded: Toast, then dismiss() removes the dialog and onDestroy follows',
  evidence=FW_DIALOGFRAG + '; SRC ui/ExportAnyMemoDbFragment.java:79-86 (dismiss at :86), :55-60')
e('ExportAnyMemoDbFragment$3.accept', 'ExportAnyMemoDbFragment.onDestroy', 'LIFECYCLE', 'the export throws: Toast, then dismiss() removes the dialog and onDestroy follows',
  evidence=FW_DIALOGFRAG + '; SRC ui/ExportAnyMemoDbFragment.java:88-94 (dismiss at :93), :55-60')
e('ExportAnyMemoDbFragment.onActivityResult', 'ExportAnyMemoDbFragment.onDestroy', 'LIFECYCLE', 'the picker returns with no saved file: super.onActivityResult, then dismiss() removes the dialog and onDestroy follows',
  guard='requestCode == REQUEST_CODE_EXPORT_DB and not (resultCode == RESULT_OK and data.getData() != null) (ExportAnyMemoDbFragment.java:63-64, 96-99)',
  evidence=FW_DIALOGFRAG + '; SRC ui/ExportAnyMemoDbFragment.java:63-64, 96-100 (dismiss at :99), :55-60')"""))

# ---- A1 UploadDropboxActivity: onDestroy leaves the onCreate loop; the exit is the default Back press
PAIRS.append((
"""for cb in ('onStart', 'onStop', 'onDestroy'):
    e('UploadDropboxActivity.onCreate', 'UploadDropboxActivity.' + cb, 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACTIVITY + '; SRC downloader/dropbox/UploadDropboxActivity.java:61-75')""",
"""# A1 (round 1b): onDestroy is no longer looped from onCreate. UploadDropboxActivity.java has no finish(); its progress dialogs are only
# dismissed (:106, :116). Neither the class nor BaseActivity overrides onBackPressed, so the exit is the default Back press.
for cb in ('onStart', 'onStop'):
    e('UploadDropboxActivity.onCreate', 'UploadDropboxActivity.' + cb, 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACTIVITY + '; SRC downloader/dropbox/UploadDropboxActivity.java:61-75')
e('S_DROPBOX_UPLOAD', 'UploadDropboxActivity.onDestroy', 'SYSTEM', 'press Back on the upload page: the default back press finishes the activity, then onDestroy',
  gui=['Press Back on the upload page'], env=ENV_HW_KEY,
  evidence='FW-SRC core/java/android/app/Activity.java:3001-3010, :5580-5584, :7203-7208; SRC downloader/dropbox/UploadDropboxActivity.java:28, 62-65 (no finish(), no onBackPressed); common/BaseActivity.java has no onBackPressed')"""))

# ---- A1 MiscTabFragment: onDestroy leaves the S_MAIN_MISC loop; two real routes replace it
PAIRS.append((
"""for cb in ('onDestroy', 'onSaveInstanceState'):
    e('S_MAIN_MISC', 'MiscTabFragment.' + cb, 'LIFECYCLE', 'Fragment lifecycle callback (the Misc page is left or its state is saved)', evidence=FW_FRAG + '; SRC ui/MiscTabFragment.java:128-222,400-406')""",
"""# A1 (round 1b): onDestroy is no longer looped from S_MAIN_MISC (a page, not a method). Its two real routes follow.
for cb in ('onSaveInstanceState',):
    e('S_MAIN_MISC', 'MiscTabFragment.' + cb, 'LIFECYCLE', 'Fragment lifecycle callback (the Misc page state is saved)', evidence=FW_FRAG + '; SRC ui/MiscTabFragment.java:128-222,400-406')
# Back on the Misc tab: the default back press finishes AnyMemo, and its fragments are destroyed with it (same model as RecentListFragment).
e('S_MAIN_MISC', 'MiscTabFragment.onDestroy', 'FRAMEWORK', 'Back on the Misc tab: the activity finishes and its fragments are destroyed with it',
  gui=['Press Back on the Misc tab'], env=ENV_HW_KEY,
  evidence='INFERRED androidx FragmentActivity destroys its fragments with the activity (androidx source not read); SRC ui/AnyMemo.java:399-411; FW-SRC core/java/android/app/Activity.java:3001-3010, :7203-7208')
# OK on the reset dialog: clear all preferences, then mActivity.finish() (MiscTabFragment.java:361), so the fragment is destroyed with the activity.
e('MiscTabFragment$1.onClick', 'MiscTabFragment.onDestroy', 'LIFECYCLE', 'OK on the reset dialog: clear all preferences, then mActivity.finish() (the host activity and its fragments are destroyed)',
  evidence='SRC ui/MiscTabFragment.java:354-363 (finish at :361); INFERRED androidx destroys the fragments with the host (androidx source not read); FW-SRC core/java/android/app/Activity.java:7203-7208')"""))

# ---- A2 rotation of AnyMemo: a new env text (not ENV_ROTATE), classified 'hardware'
PAIRS.append((
"ENV_HW_KEY = env_text('a hardware or volume key is pressed or released while this screen is in front (key event)', ('hardware',))",
"""ENV_HW_KEY = env_text('a hardware or volume key is pressed or released while this screen is in front (key event)', ('hardware',))
# A2 (round 1b): AnyMemo's manifest entry has no android:configChanges, so a rotation recreates the activity. Kind 'hardware': the
# rotation is a physical movement read by the device sensors. Not ENV_ROTATE, whose text names onConfigurationChanged.
ENV_RECREATE_ROTATE = env_text('the device is rotated: AnyMemo is destroyed and recreated because its manifest entry lists no configChanges', ('hardware',))"""))

PAIRS.append((
"e('AnyMemo.onRequestPermissionsResult', 'AnyMemo.onDestroy', 'LIFECYCLE', 'WRITE_EXTERNAL_STORAGE denied",
"""# A2 (round 1b): the manifest entry of AnyMemo (AndroidManifest.xml:23-46) has no android:configChanges, so a rotation destroys and
# recreates the activity: ActivityThread.handleRelaunchActivity runs handleDestroyActivity (:4675), then handleLaunchActivity (:4699).
for page in ('S_MAIN_RECENT', 'S_MAIN_OPEN', 'S_MAIN_DOWNLOAD', 'S_MAIN_MISC'):
    e(page, 'AnyMemo.onDestroy', 'SYSTEM', 'rotate the device on a main tab: the activity is destroyed and recreated (no configChanges in the manifest)',
      gui=['Rotate the device on a main tab'], env=ENV_RECREATE_ROTATE,
      evidence='FW-SRC core/java/android/app/ActivityThread.java:4553 (handleRelaunchActivity), :4675 (handleDestroyActivity), :4699 (handleLaunchActivity); SRC AndroidManifest.xml:23-46 (no configChanges); INFERRED the system server chooses the relaunch (system server source not read)')
e('AnyMemo.onRequestPermissionsResult', 'AnyMemo.onDestroy', 'LIFECYCLE', 'WRITE_EXTERNAL_STORAGE denied"""))

apply(PAIRS, 'round 1b group A')
