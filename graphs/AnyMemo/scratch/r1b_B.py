import sys
sys.path.insert(0, '/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch')
from r1b_tool import GD, add_gate_entries


def line_op(text, prefix, new=None, sub=None, pre=None):
    """Find the single line that starts with prefix.
    sub = (old, new) text replacement inside that line (old must occur once in the line).
    pre = lines to insert before it.
    new = list of lines that replace it ([] deletes it); None keeps it (after sub)."""
    lines = text.split('\n')
    idx = [i for i, l in enumerate(lines) if l.startswith(prefix)]
    if len(idx) != 1:
        sys.exit('FAIL prefix matched %d lines: %r' % (len(idx), prefix[:90]))
    i = idx[0]
    line = lines[i]
    if sub is not None:
        old, rep = sub
        if line.count(old) != 1:
            sys.exit('FAIL sub text found %d times in line: %r' % (line.count(old), old[:90]))
        line = line.replace(old, rep)
    block = list(pre or [])
    if new is None:
        block.append(line)
    else:
        block += list(new)
    lines[i:i + 1] = block
    return '\n'.join(lines)


def exact(text, old, new):
    n = text.count(old)
    if n != 1:
        sys.exit('FAIL exact anchor found %d times: %r' % (n, old[:90]))
    return text.replace(old, new, 1)


text = open(GD, encoding='utf-8').read()

# B1: the action sheet is entered from its own onCreateView (the view is built there); df.show is in RecentListFragment.java:450
text = line_op(text, "e('RecentListFragment$RecentListAdapter$3.onClick', 'S_DLG_OPEN_ACTIONS', 'ENTERS'", new=[
    "# Round 1b B1: the action sheet is entered from its own onCreateView (its view is built there); df.show(...) is at RecentListFragment.java:450",
    "e('OpenActionsFragment.onCreateView', 'S_DLG_OPEN_ACTIONS', 'ENTERS', 'the action sheet is shown (df.show(...) runs in RecentListFragment.java:450; its view is built here)', evidence='SRC ui/OpenActionsFragment.java:85-117; ui/RecentListFragment.java:450')",
])

# B2: drop the ENTERS shortcut from the Open-actions list button; drop NEED_CARD from the list setup runnable
text = line_op(text, "e('OpenActionsFragment$1.onClick', 'S_CARD_LIST', 'ENTERS'", new=[])
text = line_op(text, "e('CardListActivity$11.run', 'S_CARD_LIST', 'ENTERS'",
               sub=("needs_state=NEED_CARD, evidence=", "evidence="),
               pre=["# Round 1b B2: the list setup (adapter, selection, listeners, sort) needs no card; the card need stays on the long-press edge (CardListActivity.java:437-446)"])

# B3: the quiz launcher is entered from its own onCreateDialog (df.show is at OpenActionsFragment.java:152)
text = line_op(text, "e('OpenActionsFragment$1.onClick', 'S_DLG_QUIZ_LAUNCHER', 'ENTERS'", new=[
    "# Round 1b B3: the quiz launcher is entered from its own onCreateDialog; df.show(...) is at OpenActionsFragment.java:152",
    "e('QuizLauncherDialogFragment.onCreateDialog', 'S_DLG_QUIZ_LAUNCHER', 'ENTERS', 'the launcher is shown (df.show(...) runs in OpenActionsFragment.java:152; the dialog is built in onCreateDialog)', evidence='SRC ui/QuizLauncherDialogFragment.java:145-205; ui/OpenActionsFragment.java:152')",
])

# B4: category picker entered from CategoryEditorFragment.onCreateView; category result sent by the OK handler
text = line_op(text, "e('QuizLauncherDialogFragment.showCategoriesDialog', 'S_DLG_CATEGORY_QUIZ', 'ENTERS'", new=[
    "# Round 1b B4: the picker is entered from CategoryEditorFragment.onCreateView (the construction CALL and the onAttach/onCreate chain already exist as automatic edges)",
    "e('CategoryEditorFragment.onCreateView', 'S_DLG_CATEGORY_QUIZ', 'ENTERS', 'df.show(...) in showCategoriesDialog: the category picker is shown with the view built in onCreateView', needs_state=NEED_CATEGORY, evidence='SRC ui/CategoryEditorFragment.java:72-86; ui/QuizLauncherDialogFragment.java:508-516')",
])
text = line_op(text, "e('S_DLG_CATEGORY_QUIZ', 'QuizLauncherDialogFragment$10.onReceiveCategory', 'CALL'", new=[
    "# Round 1b B4: the category result is sent by the OK button handler (CategoryEditorFragment.java:96-107), not by the screen node",
    "e('CategoryEditorFragment$1.onClick', 'QuizLauncherDialogFragment$10.onReceiveCategory', 'CALL', 'a category is picked: OK tapped, resultListener.onReceiveCategory(selectedCategory)', guard='v == okButton (CategoryEditorFragment.java:96)', needs_state=NEED_CATEGORY, evidence='SRC ui/QuizLauncherDialogFragment.java:520-531; ui/CategoryEditorFragment.java:94-109')",
])

# B6: drop the ENTERS shortcut to S_CARD_PLAYER; guard the cardPlayerItem ENTRY
text = line_op(text, "e('OpenActionsFragment$1.onClick', 'S_CARD_PLAYER', 'ENTERS'", new=[])
text = line_op(text, "e('OpenActionsFragment$1.onClick', 'CardPlayerActivity.<init>', 'ENTRY'",
               sub=("evidence='SRC ui/OpenActionsFragment.java:192-197')",
                    "guard='v == cardPlayerItem (OpenActionsFragment.java:192-197)', evidence='SRC ui/OpenActionsFragment.java:192-197')"))

# B7: CardPlayerFragment lifecycle chain instead of the star from onCreate; the settings menu item is in onOptionsItemSelected
text = exact(text,
    "for cb in ('onResume', 'onPause', 'onCreateView', 'onDestroyView', 'onCreateOptionsMenu', 'onOptionsItemSelected'):\n"
    "    e('CardPlayerFragment.onCreate', 'CardPlayerFragment.' + cb, 'LIFECYCLE', 'Fragment lifecycle / framework callback', evidence=FW_FRAG + '; SRC ui/CardPlayerFragment.java:78-146')",
    "# Round 1b B7: the fragment lifecycle is a chain (CardPlayerFragment.java:68-130), not a star from onCreate.\n"
    "# onOptionsItemSelected is a menu callback (FRAMEWORK edge below), not a lifecycle step.\n"
    "for cb_from, cb_to in (('onCreate', 'onCreateView'), ('onCreateView', 'onResume'), ('onResume', 'onPause'), ('onPause', 'onDestroyView')):\n"
    "    e('CardPlayerFragment.' + cb_from, 'CardPlayerFragment.' + cb_to, 'LIFECYCLE', 'Fragment lifecycle callback', evidence=FW_FRAG + '; SRC ui/CardPlayerFragment.java:68-130')\n"
    "e('CardPlayerFragment.onCreate', 'CardPlayerFragment.onCreateOptionsMenu', 'LIFECYCLE', 'Fragment lifecycle / framework callback', evidence=FW_FRAG + '; SRC ui/CardPlayerFragment.java:68-72,132-135')\n"
    "e('S_CARD_PLAYER', 'CardPlayerFragment.onOptionsItemSelected', 'FRAMEWORK', 'tap the Card Player menu item (card_player_settings)', evidence=FW_MENU + '; SRC ui/CardPlayerFragment.java:137-146')")
text = line_op(text, "e('CardPlayerFragment$1.onClick', 'CardPlayerFragment.displaySettingsDialog', 'CALL'",
               sub=("e('CardPlayerFragment$1.onClick', 'CardPlayerFragment.displaySettingsDialog', 'CALL', 'card_player_settings menu item'",
                    "e('CardPlayerFragment.onOptionsItemSelected', 'CardPlayerFragment.displaySettingsDialog', 'CALL', 'itemId == card_player_settings: displaySettingsDialog()'"),
               pre=["# Round 1b B7: the settings item is handled in onOptionsItemSelected (CardPlayerFragment.java:140-141), not in the button listener"])

# B8: menu_context_gotoprev starts PreviewEditActivity (ENTRY), not a screen ENTERS
text = line_op(text, "e('StudyActivity.onOptionsItemSelected', 'S_PREVIEW_EDIT', 'ENTERS', 'menu_context_gotoprev", new=[
    "# Round 1b B8: menu_context_gotoprev starts PreviewEditActivity (gotoPreviewEdit, StudyActivity.java:701-710)",
    "e('StudyActivity.onOptionsItemSelected', 'PreviewEditActivity.<init>', 'ENTRY', 'menu_context_gotoprev: startActivity(PreviewEditActivity) via gotoPreviewEdit()', guard='itemId == menu_context_gotoprev (StudyActivity.java:175-177)', evidence='SRC ui/StudyActivity.java:175-177,701-710')",
])

# B9: detail ENTRY from PreviewEditActivity and from Study (keep NEED_CARD on Study)
text = line_op(text, "e('PreviewEditActivity.onOptionsItemSelected', 'S_DETAIL', 'ENTERS', 'editmenu_detail_id'", new=[
    "# Round 1b B9: editmenu_detail_id starts DetailScreen (startActivityForResult, PreviewEditActivity.java:277-283)",
    "e('PreviewEditActivity.onOptionsItemSelected', 'DetailScreen.<init>', 'ENTRY', 'editmenu_detail_id: startActivityForResult(DetailScreen)', guard='getCurrentCard() != null (PreviewEditActivity.java:278)', evidence='SRC ui/PreviewEditActivity.java:277-283')",
])
text = line_op(text, "e('StudyActivity.onOptionsItemSelected', 'S_DETAIL', 'ENTERS', 'menudetail", new=[
    "e('StudyActivity.onOptionsItemSelected', 'DetailScreen.<init>', 'ENTRY', 'menudetail: startActivityForResult(DetailScreen)', guard='itemId == menudetail (StudyActivity.java:157-159)', needs_state=NEED_CARD, evidence='SRC ui/StudyActivity.java:157-159,712-717')",
])

# B10: typeface pickers are entered after the picker's lifecycle; the Q/A checkbox and field taps are modelled
text = line_op(text, "e('SettingsScreen$10.onClick', 'S_DLG_TYPEFACE_Q', 'ENTERS'", new=[
    "# Round 1b B10: the .ttf picker is entered after its fragment lifecycle (onCreate, onCreateView, onResume browses the folder)",
    "e('FileBrowserFragment.onResume@SETTINGS_Q', 'S_DLG_TYPEFACE_Q', 'ENTERS', 'the question-typeface .ttf picker is on screen (df.show at SettingsScreen.java:720; onResume lists the folder)', evidence='SRC ui/SettingsScreen.java:712-721; ui/FileBrowserFragment.java:209-212')",
])
text = line_op(text, "e('SettingsScreen$10.onClick', 'S_DLG_TYPEFACE_A', 'ENTERS'", new=[
    "e('FileBrowserFragment.onResume@SETTINGS_A', 'S_DLG_TYPEFACE_A', 'ENTERS', 'the answer-typeface .ttf picker is on screen (df.show at SettingsScreen.java:731; onResume lists the folder)', evidence='SRC ui/SettingsScreen.java:723-732; ui/FileBrowserFragment.java:209-212')",
    "NEED_TYPEFACE_Q_VISIBLE = state_text('the question typeface field is VISIBLE: its checkbox is ticked (a question font is saved, SettingsScreen.java:467-472, or the box was ticked, :659-660)', ('settings',))",
    "NEED_TYPEFACE_A_VISIBLE = state_text('the answer typeface field is VISIBLE: its checkbox is ticked (an answer font is saved, SettingsScreen.java:475-480, or the box was ticked, :669-670)', ('settings',))",
    "gui('S_SETTINGS', 'SettingsScreen$10.onClick', 'Tap the question-font checkbox', evidence=FW_VIEW + '; SRC ui/SettingsScreen.java:658-661')",
    "gui('S_SETTINGS', 'SettingsScreen$10.onClick', 'Tap the question-font field (opens the .ttf picker when visible)', needs_state=NEED_TYPEFACE_Q_VISIBLE, evidence=FW_VIEW + '; SRC ui/SettingsScreen.java:712-721')",
    "gui('S_SETTINGS', 'SettingsScreen$10.onClick', 'Tap the answer-font checkbox', evidence=FW_VIEW + '; SRC ui/SettingsScreen.java:667-674')",
    "gui('S_SETTINGS', 'SettingsScreen$10.onClick', 'Tap the answer-font field (opens the .ttf picker when visible)', needs_state=NEED_TYPEFACE_A_VISIBLE, evidence=FW_VIEW + '; SRC ui/SettingsScreen.java:723-732')",
])

# B11: the Open tab's sheet ENTERS with NEED_DECK is removed (the sheet comes from B1); the state moves to the row tap (GATE below)
text = line_op(text, "e('OpenTabFragment$1.onFileBrowserFileClick', 'S_DLG_OPEN_ACTIONS', 'ENTERS'", new=[])

# Sanity: every new edge text is present exactly once
for needle in [
    "e('OpenActionsFragment.onCreateView', 'S_DLG_OPEN_ACTIONS', 'ENTERS'",
    "e('QuizLauncherDialogFragment.onCreateDialog', 'S_DLG_QUIZ_LAUNCHER', 'ENTERS'",
    "e('CategoryEditorFragment.onCreateView', 'S_DLG_CATEGORY_QUIZ', 'ENTERS'",
    "e('CategoryEditorFragment$1.onClick', 'QuizLauncherDialogFragment$10.onReceiveCategory'",
    "e('StudyActivity.onOptionsItemSelected', 'PreviewEditActivity.<init>', 'ENTRY'",
    "e('PreviewEditActivity.onOptionsItemSelected', 'DetailScreen.<init>', 'ENTRY'",
    "e('StudyActivity.onOptionsItemSelected', 'DetailScreen.<init>', 'ENTRY'",
    "e('FileBrowserFragment.onResume@SETTINGS_Q', 'S_DLG_TYPEFACE_Q', 'ENTERS'",
    "e('FileBrowserFragment.onResume@SETTINGS_A', 'S_DLG_TYPEFACE_A', 'ENTERS'",
    "e('S_CARD_PLAYER', 'CardPlayerFragment.onOptionsItemSelected', 'FRAMEWORK'",
]:
    if text.count(needle) != 1:
        sys.exit('FAIL sanity: %d copies of %r' % (text.count(needle), needle))

# Removed edges must be gone
for gone in [
    "'RecentListFragment$RecentListAdapter$3.onClick', 'S_DLG_OPEN_ACTIONS'",
    "'OpenActionsFragment$1.onClick', 'S_CARD_LIST', 'ENTERS'",
    "'OpenActionsFragment$1.onClick', 'S_DLG_QUIZ_LAUNCHER', 'ENTERS'",
    "'OpenActionsFragment$1.onClick', 'S_CARD_PLAYER', 'ENTERS'",
    "'StudyActivity.onOptionsItemSelected', 'S_PREVIEW_EDIT', 'ENTERS', 'menu_context_gotoprev'",
    "'PreviewEditActivity.onOptionsItemSelected', 'S_DETAIL', 'ENTERS', 'editmenu_detail_id'",
    "'StudyActivity.onOptionsItemSelected', 'S_DETAIL', 'ENTERS', 'menudetail'",
    "'SettingsScreen$10.onClick', 'S_DLG_TYPEFACE_Q', 'ENTERS'",
    "'SettingsScreen$10.onClick', 'S_DLG_TYPEFACE_A', 'ENTERS'",
    "'OpenTabFragment$1.onFileBrowserFileClick', 'S_DLG_OPEN_ACTIONS', 'ENTERS'",
]:
    if text.count(gone) != 0:
        sys.exit('FAIL: removed edge still present: %r' % gone)

open(GD, 'w', encoding='utf-8').write(text)
print('OK (B line edits written)')

# GATE entries: B5 (refill with a category filter) and B11 (the Open tab row tap needs a .db file)
for key in ["('QuizQueueManager$Builder.build', 'QuizQueueManager.refill(Category)')",
            "('FileBrowserFragment$FileBrowserAdapter$1.onClick@OPEN', 'FileBrowserFragment.openFile@OPEN')"]:
    if open(GD, encoding='utf-8').read().count(key) != 0:
        sys.exit('FAIL: GATE key already present: %r' % key)

add_gate_entries([
    "    # Round 1b B5: refill(Category) runs only when a category filter is set (QuizQueueManager.java:199-202); the category must exist (QuizActivity.java:264-268)",
    "    ('QuizQueueManager$Builder.build', 'QuizQueueManager.refill(Category)'): {'guard': 'filterCategory != null (QuizQueueManager.java:199-202)', 'needs_state': state_text('the category id from EXTRA_CATEGORY_ID exists in the category table (QuizActivity.java:264-268)', ('data',))},",
    "    # Round 1b B11: the Open tab row tap needs a .db file in the folder (FileBrowserFragment.java:516-517; the sheet is entered from OpenActionsFragment.onCreateView, B1)",
    "    ('FileBrowserFragment$FileBrowserAdapter$1.onClick@OPEN', 'FileBrowserFragment.openFile@OPEN'): {'needs_state': state_text('the Open tab folder holds at least one .db file', ('data',))},",
], 'B5 B11')
