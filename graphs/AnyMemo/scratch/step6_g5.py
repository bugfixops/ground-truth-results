# Step 6, Back-key group, part 2: fix the opener texts and the CardEditor Open-tab return (not an opener).
P = 'graphs/AnyMemo/graph_def.py'
L = open(P, encoding='utf-8').read().split('\n')

def block(first, last, new):
    # first/last: (line_no, expected_prefix_or_suffix) asserting the 1-based block bounds
    a, pa = first
    b, pb = last
    assert L[a-1].startswith(pa), (a, L[a-1][:80])
    assert L[b-1].rstrip().endswith(pb), (b, L[b-1][-80:])
    L[a-1:b] = new

GUARD_EDITOR = "guard='isEditNew, or the fields did not change (CardEditor.java:131)',"
# CardEditor: lines 713-718 (Preview/Edit, Study, Open tab -> card list)
block((713, "e('CardEditor.onBackPressed', 'S_PREVIEW_EDIT'"), (718, "evidence='SRC ui/CardEditor.java:153-158')"), [
 "e('CardEditor.onBackPressed', 'S_PREVIEW_EDIT', 'ENTERS', 'isEditNew, or nothing changed: setResult(RESULT_CANCELED); finish()', " + GUARD_EDITOR,
 "  needs_state=state_text('CardEditor was started from Preview/Edit (PreviewEditActivity newButtonListener or editButtonListener onClick, PreviewEditActivity.java:608-625) in this process', ('session',)), evidence='SRC ui/CardEditor.java:153-158')",
 "e('CardEditor.onBackPressed', 'S_STUDY', 'ENTERS', 'isEditNew, or nothing changed: setResult(RESULT_CANCELED); finish() (the Study caller restarts in StudyActivity.onActivityResult)', " + GUARD_EDITOR,
 "  needs_state=state_text('CardEditor was started from Study (StudyActivity.showEditDialog, StudyActivity.java:662-667) in this process', ('session',)), evidence='SRC ui/CardEditor.java:153-158')",
 "e('CardEditor.onBackPressed', 'S_CARD_LIST', 'ENTERS', 'isEditNew, or nothing changed: setResult(RESULT_CANCELED); finish() (back to the card list)', " + GUARD_EDITOR,
 "  needs_state=state_text('CardEditor was started from the card list row popup (CardListActivity.gotoCardEditorActivity, startActivity, CardListActivity.java:236-241) in this process', ('session',)), evidence='SRC ui/CardEditor.java:153-158; SRC ui/CardListActivity.java:236-241')",
])
# SettingsScreen: lines 891-898 (Preview/Edit, Study, Open tab, Misc tab)
G_SET = "guard='settingsChanged is false (SettingsScreen.java:196, 216-221)',"
block((891, "e('SettingsScreen.onBackPressed', 'S_PREVIEW_EDIT'"), (898, "evidence='SRC ui/SettingsScreen.java:216-221')"), [
 "e('SettingsScreen.onBackPressed', 'S_PREVIEW_EDIT', 'ENTERS', 'settingsChanged is false: setResult(RESULT_CANCELED); finish()', " + G_SET,
 "  needs_state=state_text('SettingsScreen was started from Preview/Edit (PreviewEditActivity.onOptionsItemSelected, editmenu_settings_id, PreviewEditActivity.java:269-272) in this process', ('session',)), evidence='SRC ui/SettingsScreen.java:216-221')",
 "e('SettingsScreen.onBackPressed', 'S_STUDY', 'ENTERS', 'settingsChanged is false: setResult(RESULT_CANCELED); finish() (the Study caller restarts)', " + G_SET,
 "  needs_state=state_text('SettingsScreen was started from Study (StudyActivity.onOptionsItemSelected, menusettings, gotoSettings at StudyActivity.java:155 and 719-723) in this process', ('session',)), evidence='SRC ui/SettingsScreen.java:216-221')",
 "e('SettingsScreen.onBackPressed', 'S_MAIN_OPEN', 'ENTERS', 'settingsChanged is false: setResult(RESULT_CANCELED); finish() (back to the Open tab)', " + G_SET,
 "  needs_state=state_text('SettingsScreen was started from the Open tab actions (OpenActionsFragment buttonClickListener onClick, settingsItem, OpenActionsFragment.java:156-161) in this process', ('session',)), evidence='SRC ui/SettingsScreen.java:216-221')",
 "e('SettingsScreen.onBackPressed', 'S_MAIN_MISC', 'ENTERS', 'settingsChanged is false: setResult(RESULT_CANCELED); finish() (back to the Misc tab)', " + G_SET,
 "  needs_state=state_text('SettingsScreen was started from the Misc tab (MiscTabFragment.onClick, defaultSettingsButton, MiscTabFragment.java:339-345) in this process', ('session',)), evidence='SRC ui/SettingsScreen.java:216-221')",
])
# CardPlayerActivity: lines 1161-1164 (Preview/Edit, Open tab)
block((1161, "e('CardPlayerActivity.onBackPressed', 'S_PREVIEW_EDIT'"), (1164, "evidence='SRC ui/CardPlayerActivity.java:180-185')"), [
 "e('CardPlayerActivity.onBackPressed', 'S_PREVIEW_EDIT', 'ENTERS', 'setResult(RESULT_OK) with the current card id; finish() (the Preview/Edit caller restarts)',",
 "  needs_state=state_text('CardPlayerActivity was started from Preview/Edit (PreviewEditActivity.onOptionsItemSelected, menu_card_player, PreviewEditActivity.java:307-314) in this process', ('session',)), evidence='SRC ui/CardPlayerActivity.java:180-185')",
 "e('CardPlayerActivity.onBackPressed', 'S_MAIN_OPEN', 'ENTERS', 'setResult(RESULT_OK) with the current card id; finish() (back to the Open tab)',",
 "  needs_state=state_text('CardPlayerActivity was started from the Open tab actions (OpenActionsFragment buttonClickListener onClick, cardPlayerItem, OpenActionsFragment.java:192-196) in this process', ('session',)), evidence='SRC ui/CardPlayerActivity.java:180-185')",
])
open(P, 'w', encoding='utf-8').write('\n'.join(L))
print('ok')
