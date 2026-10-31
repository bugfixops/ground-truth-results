# G2-6 route check: AudioRecorderFragment$2.<init>

- Method: AudioRecorderFragment$2.<init> = the anonymous OnCompletionListener built in startPlaying (ui/AudioRecorderFragment.java:143). Naming by javac source order: the `new` sites in the file are 44 (View.OnClickListener, $1), 114 (AlertDialog.Builder, not anonymous), 142 (MediaPlayer), 143 ($2), 169 (MediaRecorder).
- Label: REACHABLE
- Steps: 23; checked: 23 (steps 12-23 read in the source in this pass; steps 1-11 taken from G2-3 and earlier reads)
- Verdict: CORRECT (0 wrong steps)

Rule used: a step is WRONG if the transition cannot happen, or if its guard or STATE is false or missing. Kind labels, skipped hops and citation gaps are not counted.

## Wrong steps
None.

## Steps checked as OK (short)
- 1-11 cold start, Recent tab and row click, as in G2-1 and G2-3 (steps 6-11 match route 3).
- 12 ENTERS S_STUDY, guard getSelectedItemCount() == 0 (RecentListFragment.java:416-422, per G2-3).
- 13 FRAMEWORK S_STUDY -> StudyActivity.onOptionsItemSelected. The study menu is inflated in StudyActivity.onCreateOptionsMenu (StudyActivity.java:138-140).
- 14 ENTERS S_CARD_EDITOR. StudyActivity.java:166-168 (menu_context_edit) -> showEditDialog (662-668). The item is in study_activity_menu.xml:25-28 with showAsAction="ifRoom", so it is shown by default. STATE "deck has at least one card" holds: showEditDialog calls getCurrentCard().getId() (665).
- 15 FRAMEWORK S_CARD_EDITOR -> CardEditor.onOptionsItemSelected. CardEditor.onCreateOptionsMenu inflates card_editor_menu (CardEditor.java:162-164). add_new_audio is at card_editor_menu.xml:18-19.
- 16 CALL onOptionsItemSelected -> addNewAudio, guard isViewEligibleToEditAudio (CardEditor.java:192-194). The guard holds when focus is questionEdit or answerEdit (224-231). A tap on the question or answer field makes it true.
- 17 CALL addNewAudio -> startAudioRecorderWithPermissionCheck, guard audioPreviouslyExists() false. The call is in the else branch (273). The true branch (264-271) shows a confirm dialog and then makes the same call, so the route's false branch is valid. Not counted.
- 18 CALL startAudioRecorderWithPermissionCheck -> startAudioRecorder, guard RECORD_AUDIO granted (CardEditor.java:299-305).
- 19 ENTERS startAudioRecorder -> S_DLG_AUDIO_RECORDER, guard focus is questionEdit or answerEdit (315-321; `else return` at 320). The add is at 336-338.
- 20 FRAMEWORK S_DLG_AUDIO_RECORDER -> AudioRecorderFragment$1.onClick (buttonListener, AudioRecorderFragment.java:44-81). Listeners are set at 100, 104 and 108 in onCreateDialog.
- 21 CALL $1.onClick -> AudioRecorderFragment.onPlay, guard v == mPlayButton (61-63). STATE "record tapped, then tapped again to stop" holds: the play button is disabled at creation (103) and enabled only after the record toggle goes false (56-57).
- 22 CALL onPlay -> startPlaying, guard start is true (133-135). The first play tap sets mStartPlaying to true (62).
- 23 CALL startPlaying -> AudioRecorderFragment$2.<init>, "Direct call" (143). It is the statement right after `new MediaPlayer()` (142), outside any if, so it runs on every startPlaying.

## Compressed or citation notes (not counted)
- Step 20: the DialogFragment dispatch to onCreateDialog is not read in the source (INFERRED). The listeners are set in onCreateDialog (97-108), so the edge holds.
- Step 13: the framework dispatch of onOptionsItemSelected is not read in fw_src. The menu-item switch is StudyActivity.java:144-194.
- menu_context_edit also appears in memoscreen_context_menu.xml, the Recent list menu. This route uses the study menu, so that copy is not used.

## Not checked
- Steps 1-11 not re-read in this pass (G2-3 covers 6-11; G2-1 covers 1-5).
- android.media.MediaPlayer and the platform OnCompletionListener are not read (INFERRED).
- Recorder layout ids (R.layout.recorder, record_button, play_button, save_button) are not checked in the XML.
- Runtime: the file at mFileName must exist for playback to succeed. MediaPlayer.setDataSource is inside a try that catches IOException (158). The $2 constructor runs before that call, so the edge does not depend on the file.
- Not run on a device; RECORD_AUDIO permission is assumed granted by the route's ENV.
