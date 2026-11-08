import sys

P = '/Users/darshan/Desktop/yang/work/graphs/AnyMemo/graph_def.py'
src = open(P, encoding='utf-8').read()


def rep(old, new):
    global src
    n = src.count(old)
    assert n == 1, (n, old[:90])
    src = src.replace(old, new)


# 1. cold-start LIFECYCLE shortcuts to onActivityResult removed (a result needs an earlier start)
rep("'onRequestPermissionsResult', 'onActivityResult', 'onOptionsItemSelected'",
    "'onRequestPermissionsResult', 'onOptionsItemSelected'")
rep("'onCreateContextMenu', 'onActivityResult', 'onDestroy', 'onResume'",
    "'onCreateContextMenu', 'onDestroy', 'onResume'")
rep("'onRequestPermissionsResult', 'onActivityResult', 'onConfigurationChanged'",
    "'onRequestPermissionsResult', 'onConfigurationChanged'")
rep("lc_chain('CardListActivity', ('onCreate', 'onDestroy', 'onActivityResult', 'onCreateOptionsMenu', 'onOptionsItemSelected'))",
    "lc_chain('CardListActivity', ('onCreate', 'onDestroy', 'onCreateOptionsMenu', 'onOptionsItemSelected'))")
rep("'onOptionsItemSelected', 'onActivityResult'))",
    "'onOptionsItemSelected'))")
rep("lc_chain('DatabaseMerger', ('onCreate', 'onActivityResult'))",
    "lc_chain('DatabaseMerger', ('onCreate',))")
rep("for cb in ('onActivityResult', 'onCreateOptionsMenu', 'onOptionsItemSelected'):",
    "for cb in ('onCreateOptionsMenu', 'onOptionsItemSelected'):")
rep("DropboxListActivity.java:36-91", "DropboxListActivity.java:65-82")

# 2. wrong CardEditor RESULT edge (destination was InitTask.onPostExecute): replaced in block E2 below
rep("e('CardEditor.onOptionsItemSelected', 'CardEditor$InitTask.onPostExecute', 'RESULT', 'save: startActivityForResult(FileBrowserActivity) for an image returns', env=ENV_PICKER,\n"
    "  guard='the focused field is question/answer/note', evidence=FW_RESULT + '; SRC ui/CardEditor.java:180-186,361-388')\n",
    "# group 6: the image-picker RESULT edge is in block E2 (it returns to CardEditor.onActivityResult).\n")

# 3. CardListActivity hand edges removed (the method is UNREACHABLE now, see UNREACHABLE below)
rep("e('CardListActivity.onActivityResult', 'CardListActivity.restartActivity', 'CALL', 'RESULT_OK: refresh the list', evidence='SRC ui/CardListActivity.java:167-173')\n"
    "e('CardListActivity.restartActivity', 'S_CARD_LIST', 'ENTERS', 'finish(); startActivity(CardListActivity)', evidence='SRC ui/CardListActivity.java:158-164')\n",
    "# group 6: CardListActivity.onActivityResult and CardListActivity.restartActivity are UNREACHABLE (see UNREACHABLE).\n")

# 4. Dropbox citations that did not match the source (read in group 6)
rep("e('DropboxListActivity.openUploadDropbox', 'UploadDropboxActivity.<init>', 'ENTRY', 'startActivityForResult(UploadDropboxActivity)', evidence='SRC downloader/dropbox/DropboxListActivity.java:95-99')",
    "e('DropboxListActivity.openUploadDropbox', 'UploadDropboxActivity.<init>', 'ENTRY', 'startActivityForResult(UploadDropboxActivity)', evidence='SRC downloader/dropbox/DropboxListActivity.java:100-104')")
rep("e('S_DROPBOX_LIST', 'DropboxListActivity$1.onClick', 'FRAMEWORK', 'tap the upload FAB', gui=['Tap the upload FAB'], evidence=FW_VIEW + '; SRC downloader/dropbox/DropboxListActivity.java:58-63')",
    "e('S_DROPBOX_LIST', 'DropboxListActivity$1.onClick', 'FRAMEWORK', 'tap the upload FAB', gui=['Tap the upload FAB'], evidence=FW_VIEW + '; SRC downloader/dropbox/DropboxListActivity.java:56-61')")
rep("e('DropboxListActivity$1.onClick', 'DropboxListActivity.openUploadDropbox', 'CALL', 'openUploadDropbox()', evidence='SRC downloader/dropbox/DropboxListActivity.java:61')",
    "e('DropboxListActivity$1.onClick', 'DropboxListActivity.openUploadDropbox', 'CALL', 'openUploadDropbox()', evidence='SRC downloader/dropbox/DropboxListActivity.java:59')")
rep("e('DropboxListActivity.onOptionsItemSelected', 'S_EXIT', 'ENTERS', 'logout: invalidateSavedToken(); finish()', evidence='SRC downloader/dropbox/DropboxListActivity.java:78-85')",
    "e('DropboxListActivity.onOptionsItemSelected', 'S_EXIT', 'ENTERS', 'logout: invalidateSavedToken(); finish()', evidence='SRC downloader/dropbox/DropboxListActivity.java:75-78')")
rep("e('DropboxListActivity.onActivityResult', 'DropboxListActivity.refreshList', 'CALL', 'the upload activity returns RESULT_OK', evidence='SRC downloader/dropbox/DropboxListActivity.java:70-74')",
    "e('DropboxListActivity.onActivityResult', 'DropboxListActivity.refreshList', 'CALL', 'the upload activity returns RESULT_OK', guard='requestCode == OPEN_UPLOAD_DROPBOX_REQUEST_CODE and resultCode == RESULT_OK', evidence='SRC downloader/dropbox/DropboxListActivity.java:85-90')")

# 5. UNREACHABLE entries (read: CardListActivity.java:158-173, CardEditor.java:116, grep of restartActivity() callers)
rep("UNREACHABLE = {}\n", """UNREACHABLE = {}
UNREACHABLE['CardListActivity.onActivityResult'] = ('no_trigger_in_app', 'CardListActivity starts no child with startActivityForResult (every start in ui/CardListActivity.java is startActivity: lines 163, 240, 247, 254; no setResult either), so the framework never delivers a result to it; the list is started for a result by PreviewEditActivity (ui/PreviewEditActivity.java:285-294), and that result goes to PreviewEditActivity.onActivityResult', 'SRC ui/CardListActivity.java:167-173', 'SOURCE')
UNREACHABLE['CardListActivity.restartActivity'] = ('no_trigger_in_app', 'its only call in the app is in CardListActivity.onActivityResult (ui/CardListActivity.java:172), which is UNREACHABLE; the BaseActivity-typed mActivity.restartActivity() calls in GestureSelectionDialogFragment.onDismiss and OpenActionsFragment$1$1.onClick reach it only by class-hierarchy analysis: the gesture dialog is shown only by PreviewEditActivity (ui/PreviewEditActivity.java:578) and StudyActivity (ui/StudyActivity.java:651), and OpenActionsFragment only from AnyMemo (ui/AnyMemo.java:241, 243, via RecentListFragment and OpenTabFragment), so the runtime receiver is never a CardListActivity', 'SRC ui/CardListActivity.java:158-164', 'SOURCE')
UNREACHABLE['CardEditor.restartActivity'] = ('no_trigger_in_app', 'no call of CardEditor.restartActivity in the app (grep of restartActivity() in ui: only the declaration at ui/CardEditor.java:116); the mActivity.restartActivity() calls in GestureSelectionDialogFragment and OpenActionsFragment reach it only by class-hierarchy analysis, and their hosts are never a CardEditor', 'SRC ui/CardEditor.java:116', 'SOURCE')
""")

# 6. block E2: RESULT edges for the starters the old list did not cover (2026-10-26)
E2 = r'''# ---- E2. group 6 (2026-10-26): RESULT edges for the starters that section E does not list.
# FW_RESULT: the framework delivers a result to the activity that made the start, so each RESULT edge goes to the
# onActivityResult of the STARTER's own class (the cold-start LIFECYCLE shortcut to onActivityResult was removed).
e('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity.onActivityResult', 'RESULT',
  'editmenu_settings_id: startActivityForResult(SettingsScreen) returns',
  evidence=FW_RESULT + '; SRC ui/PreviewEditActivity.java:269-273')
e('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity.onActivityResult', 'RESULT',
  'editmenu_detail_id: startActivityForResult(DetailScreen) returns', guard='getCurrentCard() != null',
  evidence=FW_RESULT + '; SRC ui/PreviewEditActivity.java:277-284')
e('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity.onActivityResult', 'RESULT',
  'editmenu_list_id: startActivityForResult(CardListActivity) returns',
  evidence=FW_RESULT + '; SRC ui/PreviewEditActivity.java:285-294')
e('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity.onActivityResult', 'RESULT',
  'menu_card_player: startActivityForResult(CardPlayerActivity) returns', guard='getCurrentCard() != null',
  evidence=FW_RESULT + '; SRC ui/PreviewEditActivity.java:307-316')
e('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity.onActivityResult', 'RESULT',
  'menu_context_merge_db: startActivityForResult(DatabaseMerger) returns',
  evidence=FW_RESULT + '; SRC ui/PreviewEditActivity.java:400-404')
e('PreviewEditActivity$9.onClick', 'PreviewEditActivity.onActivityResult', 'RESULT',
  'newButtonListener: startActivityForResult(CardEditor, isEditNew=true) returns',
  evidence=FW_RESULT + '; SRC ui/PreviewEditActivity.java:606-616')
e('PreviewEditActivity$10.onClick', 'PreviewEditActivity.onActivityResult', 'RESULT',
  'editButtonListener: startActivityForResult(CardEditor, isEditNew=false) returns', guard='getCurrentCard() != null',
  needs_state=NEED_CARD, evidence=FW_RESULT + '; SRC ui/PreviewEditActivity.java:618-628')
e('StudyActivity.gotoSettings', 'StudyActivity.onActivityResult', 'RESULT',
  'menusettings: startActivityForResult(SettingsScreen) returns',
  evidence=FW_RESULT + '; SRC ui/StudyActivity.java:719-723')
e('StudyActivity.gotoDetail', 'StudyActivity.onActivityResult', 'RESULT',
  'menudetail: startActivityForResult(DetailScreen) returns', needs_state=NEED_CARD,
  evidence=FW_RESULT + '; SRC ui/StudyActivity.java:712-717')
e('StudyActivity.showEditDialog', 'StudyActivity.onActivityResult', 'RESULT',
  'menu_context_edit: startActivityForResult(CardEditor, isEditNew=false) returns', needs_state=NEED_CARD,
  evidence=FW_RESULT + '; SRC ui/StudyActivity.java:662-668')
e('CardEditor.onOptionsItemSelected', 'CardEditor.onActivityResult', 'RESULT',
  'editor_menu_image: startActivityForResult(FileBrowserActivity, image extensions) returns the picked image',
  env=ENV_PICKER, guard='the focused field is question/answer/note',
  evidence=FW_RESULT + '; SRC ui/CardEditor.java:180-186,361-388')
e('CardEditor.startAudioBrowser', 'CardEditor.onActivityResult', 'RESULT',
  'add_existing_audio: startActivityForResult(FileBrowserActivity, audio extensions) returns the picked audio',
  env=ENV_PICKER, guard='isViewEligibleToEditAudio() is true (add_existing_audio branch)',
  evidence=FW_RESULT + '; SRC ui/CardEditor.java:187-191,290-295,389')
e('DatabaseMerger.onClick', 'DatabaseMerger.onActivityResult', 'RESULT',
  'v == targetEdit: startActivityForResult(FileBrowserActivity, .db) returns the picked path', env=ENV_PICKER,
  guard='v == targetEdit', evidence=FW_RESULT + '; SRC ui/DatabaseMerger.java:100-106,74-97')
e('DatabaseMerger.onClick', 'DatabaseMerger.onActivityResult', 'RESULT',
  'v == sourceEdit: startActivityForResult(FileBrowserActivity, .db) returns the picked path', env=ENV_PICKER,
  guard='v == sourceEdit', evidence=FW_RESULT + '; SRC ui/DatabaseMerger.java:108-113,74-97')
e('DropboxListActivity.openUploadDropbox', 'DropboxListActivity.onActivityResult', 'RESULT',
  'startActivityForResult(UploadDropboxActivity) returns', evidence=FW_RESULT + '; SRC downloader/dropbox/DropboxListActivity.java:100-104,85-90')

# ---- E3. group 6: CHA over-approximations of the BaseActivity-typed mActivity.restartActivity() calls.
# The gesture dialog's host is PreviewEditActivity or StudyActivity (both override restartActivity), so the CHA edges to
# CardEditor, CardListActivity and BaseActivity never run; OpenActionsFragment's host is AnyMemo (no override), so only
# BaseActivity.restartActivity runs there (kept).
sup(('GestureSelectionDialogFragment.onDismiss', 'CardEditor.restartActivity'),
    ('GestureSelectionDialogFragment.onDismiss', 'CardListActivity.restartActivity'),
    ('GestureSelectionDialogFragment.onDismiss', 'BaseActivity.restartActivity'),
    ('OpenActionsFragment$1$1.onClick', 'PreviewEditActivity.restartActivity'),
    ('OpenActionsFragment$1$1.onClick', 'CardEditor.restartActivity'),
    ('OpenActionsFragment$1$1.onClick', 'StudyActivity.restartActivity'),
    ('OpenActionsFragment$1$1.onClick', 'CardListActivity.restartActivity'),
    ('CardListActivity.onActivityResult', 'CardListActivity.restartActivity'))

# ---- F. layout <fragment> tag, loader, service and widget creation by the framework ----'''
rep("# ---- F. layout <fragment> tag, loader, service and widget creation by the framework ----", E2)

open(P, 'w', encoding='utf-8').write(src)
print('written', len(src))
