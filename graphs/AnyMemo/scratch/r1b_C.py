import sys
sys.path.insert(0, '/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch')
from r1b_tool import apply, add_gate_entries

# C1: the four listener gui edges start at CardFragment.onCreateView (CardFragment.java:114-201).
# Text listeners ($4, $5) are attached at CardFragment.java:135-140; card view listeners ($6, $7) at 127-128.
apply([
    ("gui('QACardActivity.<init>', 'QACardActivity$4.onClick'",
     "gui('CardFragment.onCreateView', 'QACardActivity$4.onClick'"),
    ("evidence=FW_VIEW + '; SRC ui/QACardActivity.java:726-732')",
     "evidence=FW_VIEW + '; SRC ui/QACardActivity.java:726-732; ui/CardFragment.java:135-140')"),
    ("gui('QACardActivity.<init>', 'QACardActivity$5.onClick'",
     "gui('CardFragment.onCreateView', 'QACardActivity$5.onClick'"),
    ("evidence=FW_VIEW + '; SRC ui/QACardActivity.java:734-740')",
     "evidence=FW_VIEW + '; SRC ui/QACardActivity.java:734-740; ui/CardFragment.java:135-140')"),
    ("gui('QACardActivity.<init>', 'QACardActivity$6.onClick'",
     "gui('CardFragment.onCreateView', 'QACardActivity$6.onClick'"),
    ("evidence=FW_VIEW + '; SRC ui/QACardActivity.java:742-748')",
     "evidence=FW_VIEW + '; SRC ui/QACardActivity.java:742-748; ui/CardFragment.java:127-128')"),
    ("gui('QACardActivity.<init>', 'QACardActivity$7.onClick'",
     "gui('CardFragment.onCreateView', 'QACardActivity$7.onClick'"),
    ("evidence=FW_VIEW + '; SRC ui/QACardActivity.java:749-755')",
     "evidence=FW_VIEW + '; SRC ui/QACardActivity.java:749-755; ui/CardFragment.java:127-128')"),
], 'C1')

# C4: stopPlaying from onDestroyView needs the activity and the bound service (CardPlayerFragment.java:204-205)
apply([
    ("e('CardPlayerFragment.onDestroyView', 'CardPlayerService.stopPlaying', 'CALL', 'stopPlaying() (make sure playback stops if the fragment is killed)', evidence='SRC ui/CardPlayerFragment.java:125-130,201-207')",
     "e('CardPlayerFragment.onDestroyView', 'CardPlayerService.stopPlaying', 'CALL', 'stopPlaying() (make sure playback stops if the fragment is killed)', guard='activity and bound CardPlayerService are non-null (CardPlayerFragment.java:204-205)', evidence='SRC ui/CardPlayerFragment.java:125-130,201-207')"),
], 'C4')

# C6: replace the guard on the onReceive -> gotoCardId edge (CardPlayerFragment.java:234-238)
apply([
    ("guard='activity.isActivityForeground()', evidence='SRC ui/CardPlayerFragment.java:238-239')",
     "guard='activity is not null, activity.isActivityForeground(), and currentCardId != activity.getCurrentCard().getId() (CardPlayerFragment.java:234-238)', evidence='SRC ui/CardPlayerFragment.java:234-239')"),
], 'C6')

# C9 (needs_state on the bind ENTRY) and C7 (two CALL edges for the two branches of updateCardFrontSide)
apply([
    ("e('CardPlayerActivity.onPostInit', 'CardPlayerService.onCreate', 'ENTRY', 'bindCardPlayerService(): bindService(Context.BIND_AUTO_CREATE)', evidence='SRC ui/CardPlayerActivity.java:111,210-215')\n",
     "e('CardPlayerActivity.onPostInit', 'CardPlayerService.onCreate', 'ENTRY', 'bindCardPlayerService(): bindService(Context.BIND_AUTO_CREATE)', needs_state=NEED_CARD, evidence='SRC ui/CardPlayerActivity.java:111,210-215')\n"
     "# Round 1b C7: updateCardFrontSide has one CALL per branch (CardPlayerActivity.java:199-205); the automatic edge is replaced by these two\n"
     "e('CardPlayerActivity.updateCardFrontSide', 'QACardActivity.displayCard@CardPlayerActivity', 'CALL', 'DOUBLE_SIDED: displayCard(false) shows the front side', guard='current card not null and DOUBLE_SIDED (CardPlayerActivity.java:199-202)', evidence='SRC ui/CardPlayerActivity.java:198-208')\n"
     "e('CardPlayerActivity.updateCardFrontSide', 'QACardActivity.displayCard@CardPlayerActivity', 'CALL', 'displayCard(true) otherwise: single sided, question and answer shown', guard='current card not null and not DOUBLE_SIDED (CardPlayerActivity.java:199-205)', evidence='SRC ui/CardPlayerActivity.java:198-208')\n"),
], 'C7 C9')

# C11: three CALL edges for the three branches of StudyActivity.onPostDisplayCard (StudyActivity.java:306-313)
apply([
    ("'handler.post(...) runs once the fragment view is attached', evidence=FW_HANDLER + '; SRC ui/GradeButtonsFragment.java:245-251')\n",
     "'handler.post(...) runs once the fragment view is attached', evidence=FW_HANDLER + '; SRC ui/GradeButtonsFragment.java:245-251')\n"
     "# Round 1b C11: onPostDisplayCard sets the grade buttons three ways (StudyActivity.java:306-313); the automatic edge is replaced by these three\n"
     "e('StudyActivity.onPostDisplayCard', 'GradeButtonsFragment.setVisibility', 'CALL', 'setVisibility(VISIBLE): the answer is shown', guard='isAnswerShown() is true (StudyActivity.java:306-307)', evidence='SRC ui/StudyActivity.java:306-313')\n"
     "e('StudyActivity.onPostDisplayCard', 'GradeButtonsFragment.setVisibility', 'CALL', 'setVisibility(GONE): the answer is hidden on a double sided card', guard='answer not shown and DOUBLE_SIDED (StudyActivity.java:310-311)', evidence='SRC ui/StudyActivity.java:306-313')\n"
     "e('StudyActivity.onPostDisplayCard', 'GradeButtonsFragment.setVisibility', 'CALL', 'setVisibility(INVISIBLE): the answer is hidden on a single sided card', guard='answer not shown and not DOUBLE_SIDED (StudyActivity.java:312-313)', evidence='SRC ui/StudyActivity.java:306-313')\n"),
], 'C11')

# GATE entries: C2, C3, C5, C8, C10, C12, C13
gate = []
gate.append("    # Round 1b C2: the DOUBLE_SIDED check in onClickQuestionView (QACardActivity.java:548-549), one key per variant")
for v in ['', '@CardPlayerActivity', '@PreviewEditActivity', '@QuizActivity', '@StudyActivity']:
    gate.append("    ('QACardActivity.onClickQuestionView%s', 'QACardActivity.displayCard%s'): {'guard': 'card style is DOUBLE_SIDED (QACardActivity.java:548-549)'}," % (v, v))
gate.append("    # Round 1b C3: the card style picks the card fragment (QACardActivity.java:321-322 single sided, 371-372 double sided)")
for v in ['', '@CardPlayerActivity', '@PreviewEditActivity', '@QuizActivity', '@StudyActivity']:
    gate.append("    ('QACardActivity.displayCard%s', 'FlipableCardFragment.<init>'): {'guard': 'card style is DOUBLE_SIDED (QACardActivity.java:371-372)'}," % v)
    gate.append("    ('QACardActivity.displayCard%s', 'TwoFieldsCardFragment.<init>'): {'guard': 'card style is SINGLE_SIDED (QACardActivity.java:321-322)'}," % v)
gate.append("    # Round 1b C5: the STOPPED state moves to the next or previous card and calls the event handler (CardPlayerState.java:43-61)")
gate.append("    ('CardPlayerState$1.transition', 'CardPlayerService$1.onPlayCard'): {'guard': 'state is STOPPED, message is GO_TO_NEXT or GO_TO_PREV, and a next/previous card is found (CardPlayerState.java:43-61)'},")
gate.append("    # Round 1b C8: the registered onPostInit runnable runs on the host activity (QACardActivity.java:167)")
for x in ['CardPlayerActivity', 'StudyActivity', 'QuizActivity', 'PreviewEditActivity']:
    gate.append("    ('QACardActivity$2.run', '%s.onPostInit'): {'guard': 'the registering activity is %s (QACardActivity.java:167)'}," % (x, x))
gate.append("    # Round 1b C10: the question view tap only displays the answer when it is not shown yet (StudyActivity.java:365)")
gate.append("    ('StudyActivity.onClickQuestionView', 'QACardActivity.displayCard@StudyActivity'): {'guard': 'answer not yet shown (StudyActivity.java:365)', 'needs_state': NEED_CARD},")
gate.append("    # Round 1b C12: the noise is added only when the schedule asks for it (DefaultScheduler.java:128)")
gate.append("    ('DefaultScheduler.schedule', 'DefaultScheduler.calculateIntervalNoise'): {'guard': 'includeNoise is true and noise is enabled (DefaultScheduler.java:128)'},")
gate.append("    # Round 1b C13: the minimal-interval branch sets noise to 0 and never calls randomNumber (DefaultScheduler.java:199-200)")
gate.append("    ('DefaultScheduler.calculateIntervalNoise', 'DefaultScheduler.randomNumber'): {'guard': 'interval is above the minimal interval so noise is not forced to 0 (DefaultScheduler.java:199-200)'},")
add_gate_entries(gate, 'C2 C3 C5 C8 C10 C12 C13')
