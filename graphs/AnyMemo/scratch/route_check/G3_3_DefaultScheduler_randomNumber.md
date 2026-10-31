# G3-3: DefaultScheduler.randomNumber (checker G3, route 3 of 6)

- Method: DefaultScheduler.randomNumber
- Label: REACHABLE (this route does not support it; the label itself was not re-checked here)
- Steps: 23. Checked: 23 (each step read against its cited lines, guards included).
- Verdict: WRONG (6 wrong steps: 10, 14, 16, 18, 22, 23)

Route (show_route.py --dedupe): S_ENTRY, AnyMemo.<init>, onCreate, loadUiComponents, initDrawer, AnyMemo$2 (@INIT), RecentListFragment.<init>, onAttach, onCreate, onCreateView, RecentListAdapter.onBindViewHolder, adapter $1.onClick, StudyActivity.<init>, QACardActivity.<init>, QACardActivity$6.onClick, StudyActivity.onClickQuestionView, QACardActivity.displayCard@StudyActivity, StudyActivity.onPostDisplayCard, GradeButtonsFragment.setVisibility, GradeButtonsFragment$6.run, setGradeButtonTitle, DefaultScheduler.schedule, calculateIntervalNoise, randomNumber.

## WRONG steps

Step 10. RecentListFragment.onCreateView -> RecentListAdapter.onBindViewHolder (FRAMEWORK, graph_def.py:2309). Same error as G3-2 step 10: the adapter is empty in onCreateView; rows come from onLoadFinished -> setItems (RecentListFragment.java:268-270, 464-467). Fix as in G3-2.

Step 14. QACardActivity.<init> -> QACardActivity$6.onClick (gui edge, graph_def.py:1504). The question card view is built inside displayCard (QACardActivity.java:197-259; the listener is attached at line 259), and displayCard runs first in StudyActivity.onPostInit (StudyActivity.java:297). The route goes from StudyActivity.<init> straight to the tap, so it skips StudyActivity.onCreate and onPostInit, and no card view exists. Fix: give this gui edge needs_state "a question card is on screen (displayCard has run; StudyActivity.onPostInit, StudyActivity.java:297)" (session), or move the edge after displayCard(false).

Step 16. StudyActivity.onClickQuestionView -> QACardActivity.displayCard@StudyActivity (StudyActivity.java:366, graph guard missing). The code guard is `if (!isAnswerShown())` (StudyActivity.java:365). The field starts as isAnswerShown = true (QACardActivity.java:101), so without a prior displayCard(false) the tap does nothing. The route never ran displayCard(false), so the guard fails. Fix: add guard "the answer is hidden (!isAnswerShown())" and needs_state "a question card is on screen" (same STATE as step 14).

Step 18. StudyActivity.onPostDisplayCard -> GradeButtonsFragment.setVisibility (cited StudyActivity.java:313, graph_def edge without guard). Line 313 is in the else branch of `if (isAnswerShown())` (StudyActivity.java:306-314), which needs the answer hidden. displayCard(true) sets isAnswerShown = true (QACardActivity.java:392), so the route takes line 307 (setVisibility(View.VISIBLE)). The target node is the same, but the cited line and guard are wrong. Fix: cite StudyActivity.java:307 with guard isAnswerShown() true; keep line 313 as a second edge with guard !isAnswerShown() and getCardStyle() != DOUBLE_SIDED (StudyActivity.java:310-313).

Step 22. DefaultScheduler.schedule -> DefaultScheduler.calculateIntervalNoise (bytecode DefaultScheduler.java:129). The call at line 129 is in `if (includeNoise && parameters.getEnableNoise())` (DefaultScheduler.java:128). GradeButtonsFragment calls schedule(..., 0..5, false) at GradeButtonsFragment.java:315-320, so includeNoise is false and line 129 is not reached. Fix: add guard "includeNoise is true and noise is enabled in the algorithm settings" (DefaultScheduler.java:128) and make the grade-button callers (GradeButtonsFragment.java:315-320) not feed this edge. Routes to randomNumber must come from a caller that passes true; that is not checked here.

Step 23. DefaultScheduler.calculateIntervalNoise -> DefaultScheduler.randomNumber (bytecode DefaultScheduler.java:208). The call is in the final else of the interval chain (DefaultScheduler.java:199-209): it needs interval > 60.0 (after minimalInterval and the 1.99999 and 10.0 branches). The route is not on a path with includeNoise true (step 22), and no card interval state is recorded. Fix: add guard "interval > 60 days (else branch, DefaultScheduler.java:207-208)" and needs_state data "a card with an interval over 60 days", and fix step 22.

## Steps checked and OK (with notes)

1-9: same as G3-2 steps 1-9 (AnyMemo cold start, loadUiComponents, initDrawer, RecentListFragment lifecycle). OK; see G3-2 for the citations and the FW-SRC line numbers still to add.
11 onBindViewHolder -> $1.onClick (RecentListFragment.java:413): OK; needs_state data holds once step 10 is fixed.
12 $1.onClick -> StudyActivity.<init> (INTENT, RecentListFragment.java:416-422): OK.
13 StudyActivity.<init> -> QACardActivity.<init> (bytecode, StudyActivity.java:63 super call): OK as a call. The route then jumps over StudyActivity.onCreate; charged to step 14.
15 $6.onClick -> StudyActivity.onClickQuestionView (QACardActivity.java:746): OK (virtual dispatch to the override).
17 displayCard@StudyActivity -> onPostDisplayCard (QACardActivity.java:416, unconditional): OK.
19 setVisibility -> GradeButtonsFragment$6.run (handler.post, GradeButtonsFragment.java:245-251): OK, INFERRED (Handler is platform code; FW-SRC not read here).
20 $6.run -> setGradeButtonTitle (GradeButtonsFragment.java:246-248): OK.
21 setGradeButtonTitle -> DefaultScheduler.schedule (GradeButtonsFragment.java:320, inside `if` at line 314): OK. The guard holds in the standard configuration: default button style is ANKI (Option.java:35), and the host is StudyActivity, not QuizActivity. Add the guard text ("the grade button style is not MNEMOSYNE and the host is not QuizActivity", GradeButtonsFragment.java:314).

## Not checked

- Other callers of DefaultScheduler.schedule with includeNoise = true (that is where a correct route to randomNumber would come from).
- Handler.post platform flow; the card-interval STATE values in the algorithm settings.
