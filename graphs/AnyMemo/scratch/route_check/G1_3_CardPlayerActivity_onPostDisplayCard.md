# G1-3 CardPlayerActivity.onPostDisplayCard (checker G1)

- Label: REACHABLE
- Steps: 25 (show_route.py --dedupe); checked: 25
- Verdict: WRONG (7 wrong steps: 10, 14, 16, 17, 19, 21, 24)

## WRONG steps

**Step 10** RecentListFragment.onCreateView -> RecentListAdapter.onBindViewHolder (FRAMEWORK)
- Same error as G1-2 step 10: rows are bound before any recent-deck data is loaded (onResume loader, RecentListFragment.java:216-218, 268-271; setItems :464-468).
- Fix: graph_def.py:2309 as in G1-2.

**Step 14** OpenActionsFragment$1.onClick -> S_CARD_PLAYER (ENTERS, graph_def.py:1366)
- Wrong: the page is entered without the activity start. The page and the fragment are added only from CardPlayerActivity.onPostInit (CardPlayerActivity.java:112-117; setupControlButtons :116, :123-127). That runs after onCreate/startInit (:62-71) and the loader, and it needs a current card (:112). The route skips all of it.
- The guard `v == cardPlayerItem` (OpenActionsFragment.java:192-197) is only in the edge text; no guard=.
- Fix: delete graph_def.py:1366 (page shortcut). Keep the intent edge at :1245 (OpenActionsFragment$1.onClick -> CardPlayerActivity.<init>) and add guard='v == cardPlayerItem (OpenActionsFragment.java:192-197)'. The page then follows onPostInit -> S_CARD_PLAYER (:1249-1251, needs NEED_CARD).

**Step 16** CardPlayerFragment.onCreate -> CardPlayerFragment.onDestroyView (LIFECYCLE)
- Wrong: graph_def.py:1254-1255 is a star loop, so onCreate reaches onResume, onPause, onCreateView and onDestroyView directly. The route skips onResume. onResume (CardPlayerFragment.java:79-85) registers serviceEventListener, the receiver used in step 20; onPause (:88-90) unregisters it.
- Fix: replace the star loop with a chain (onCreate -> onCreateView -> onResume -> onPause -> onDestroyView), as lc_chain is used at graph_def.py:441 for RecentListFragment. Check the output after the change.

**Step 17** CardPlayerFragment.onDestroyView -> CardPlayerService.stopPlaying (CALL, graph_def.py:1283)
- Wrong: the call at CardPlayerFragment.java:205 is inside `if (activity != null && activity.getCardPlayerService() != null)` (:204). No guard= on the edge.
- Fix: guard='activity is not null and the service is bound (CardPlayerFragment.java:203-205)'.

**Step 19** CardPlayerState$1.transition -> CardPlayerService$1.onPlayCard (CALL)
- Wrong: onPlayCard is called only in the STOPPED state's GO_TO_NEXT case (CardPlayerState.java:43-52) and GO_TO_PREV case (:54-60). STOP_PLAYING in STOPPED goes to default (:62-64) and does nothing. So the stop path (steps 17-18) never sends ACTION_GO_TO_CARD.
- Fix: EDIT guard for this (src, dst): guard='message is GO_TO_NEXT or GO_TO_PREV and the next/prev card exists (CardPlayerState.java:43-61)'. The route to this step must use the Prev/Next button: CardPlayerFragment$1.onClick -> CardPlayerService.skipToPrev (graph_def.py:1260; CardPlayerFragment.java:165-166).

**Step 21** CardPlayerFragment$2.onReceive -> CardPlayerActivity.gotoCardId (CALL, graph_def.py:1267)
- Partial guard. The code (CardPlayerFragment.java:233-239) also returns if activity is null (:234-237) and requires `currentCardId != activity.getCurrentCard().getId()` (:238). The graph guard lists only isActivityForeground().
- Fix: graph_def.py:1267 guard='activity is not null and activity.isActivityForeground() and currentCardId != activity.getCurrentCard().getId() (CardPlayerFragment.java:233-238)'.

**Step 24** CardPlayerActivity.updateCardFrontSide -> QACardActivity.displayCard@CardPlayerActivity (CALL)
- Wrong: displayCard(true) at CardPlayerActivity.java:205 is the else branch of `if (setting.getCardStyle() == DOUBLE_SIDED)` (:200-206), inside `if (getCurrentCard() != null)` (:199). No guard= on the edge. (The DOUBLE_SIDED branch is displayCard(false), :202.)
- Fix: EDIT guard for this (src, dst): guard='a current card exists and the card style is not DOUBLE_SIDED (CardPlayerActivity.java:199-205)'.

## Steps checked OK
- 1-9: same chain as G1-2 (AndroidManifest.xml:23-46; AnyMemo.java:115-141 with the API <= 29 guard, ENV kept; RecentListFragment lifecycle).
- 11: row "more" listener, needs NEED_RECENT (RecentListFragment.java:442-452). OK.
- 12: "more" -> df.show(...) (RecentListFragment.java:444-450), unconditional. OK.
- 13: OK in the graph. show_route --dedupe printed 'Tap "study" in the action sheet', the first of six identical S_DLG_OPEN_ACTIONS -> OpenActionsFragment$1.onClick gui edges (graph_def.py:1348-1354; the cardPlayer edge has its own text). Display bug in the tool (dedupe keeps the first text), not a graph error.
- 15: S_CARD_PLAYER -> CardPlayerFragment.onCreate is a valid fragment lifecycle edge once step 14 is fixed.
- 18: CardPlayerService.stopPlaying -> CardPlayerState$1.transition (CardPlayerService.java:157-160), virtual call. OK.
- 20: CardPlayerService$1.onPlayCard -> CardPlayerFragment$2.onReceive (sendBroadcast, CardPlayerService.java:229-235). Receiver only while registered (onResume, step 16 fix). The action check (CardPlayerFragment.java:224) is always true for this sender; no guard needed for the route.
- 22: gotoCardId -> gotoCard (CardPlayerActivity.java:190), unconditional; needs cardDao from onPostInit (:97), covered by step 14.
- 23: gotoCard -> updateCardFrontSide (:175), unconditional. OK.
- 25: displayCard -> onPostDisplayCard (QACardActivity.java:416). No return between :197 and :416, so it is reached. Dispatch to CardPlayerActivity.onPostDisplayCard (:131). OK.

## Could not check / INFERRED
- androidx fragment and loader callbacks, and the Material bottom nav (not read; INFERRED is correct).
- Anonymous numbers (CardPlayerFragment$2, CardPlayerState$1) follow source order; javap is not available.
