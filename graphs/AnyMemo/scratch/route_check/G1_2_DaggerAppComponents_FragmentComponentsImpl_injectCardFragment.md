# G1-2 DaggerAppComponents$FragmentComponentsImpl.injectCardFragment (checker G1)

- Label: REACHABLE
- Steps: 25 (show_route.py --dedupe, freeDebug build); checked: 25
- Verdict: WRONG (5 wrong steps: 10, 12, 14, 16, 17)

## WRONG steps

**Step 10.** RecentListFragment.onCreateView -> RecentListFragment$RecentListAdapter.onBindViewHolder (FRAMEWORK, non_standard)
- Wrong: onCreateView only calls setAdapter (RecentListFragment.java:182). The RecyclerView binds a row only when the adapter holds items. The items come later: onResume restarts loader 1 (:216-218), the loader's onLoadFinished calls recentListAdapter.setItems(ril) when the version matches (:268-271), and setItems calls notifyDataSetChanged (:464-468). The route binds rows with no data loaded (the first-resume shortcut).
- Fix: graph_def.py:2309 remove onBindViewHolder from the tuple (keep getItemCount and onCreateViewHolder on onCreateView). Add two edges: RecentListFragment$RecentListLoaderCallbacks.onLoadFinished -> RecentListFragment$RecentListAdapter.setItems (CALL, guard='recentListVersion.get() == loadedVersion (RecentListFragment.java:269)'), and RecentListFragment$RecentListAdapter.setItems -> RecentListFragment$RecentListAdapter.onBindViewHolder (FRAMEWORK, cls non_standard, needs_state=NEED_RECENT, evidence SRC RecentListFragment.java:464-468).

**Step 12.** RecentListFragment$RecentListAdapter$1.onClick -> StudyActivity.<init> (INTENT)
- Wrong: the condition `getSelectedItemCount() == 0` (RecentListFragment.java:416) is only in the edge text; the edge has no guard=.
- Also the intent carries EXTRA_DBPATH (:420), which startInit reads (QACardActivity.java:147-150). The route then skips StudyActivity.onCreate.
- Fix: graph_def.py:594 add guard='getSelectedItemCount() == 0: no row selected (RecentListFragment.java:416-422)'.

**Step 14.** QACardActivity.<init> -> QACardActivity$6.onClick (FRAMEWORK, gui)
- Wrong source. The listener object is created in the field initializer (QACardActivity.java:742-748), but it is attached to a view only inside displayCard: `.setCardOnClickListener(onQuestionViewClickListener)` at :259 (the other three listeners are set at :258, :270-271, :282, :303). displayCard reads getCurrentCard() (:255), so before it runs there is no card to tap. This is the constructor-to-tap shortcut: StudyActivity.onCreate, startInit, the loaders and onPostInit are all skipped.
- Fix: graph_def.py:1502-1505 change the source from QACardActivity.<init> to QACardActivity.displayCard (the same pattern as line 1500 for $1), with a needs_state session text: "a card is on screen (displayCard ran in this activity)".

**Step 16.** QACardActivity.onClickQuestionView -> QACardActivity.displayCard (CALL)
- Wrong: the call at QACardActivity.java:548-549 is inside `if (setting.getCardStyle() == Setting.CardStyle.DOUBLE_SIDED)`; the return false otherwise (:552). No guard= on the edge.
- Fix: EDIT guard dict (graph_def.py ~2771-2800, key (src, dst)): ('QACardActivity.onClickQuestionView', 'QACardActivity.displayCard'): {'guard': 'the card style is DOUBLE_SIDED (QACardActivity.java:548-549)'}.

**Step 17.** QACardActivity.displayCard -> FlipableCardFragment.<init> (CALL)
- Wrong: the new FlipableCardFragment() at QACardActivity.java:372 is in the else-if at :371 (`setting.getCardStyle() == DOUBLE_SIDED`), after the SINGLE_SIDED branch at :321. No guard= on the edge.
- Fix: EDIT guard dict key ('QACardActivity.displayCard', 'FlipableCardFragment.<init>'): {'guard': 'the card style is DOUBLE_SIDED (QACardActivity.java:371-372, else-if of :321)'}.

## Steps checked OK
- 1-9: ENTRY, LIFECYCLE, CALL chain (AndroidManifest.xml:23-46; AnyMemo.java:115-141 with the API <= 29 permission guard (ENV kept); :187; :263; :240-241 itemId guard; RecentListFragment lifecycle :127-226). Step 5 (BottomNavigationView library) is INFERRED, which is correct.
- 11: FRAMEWORK row tap, needs_state NEED_RECENT, RecentListFragment.java:413-428. OK (the bind that feeds it is fixed in step 10).
- 13: StudyActivity.<init> -> QACardActivity.<init> is the implicit super() (StudyActivity.java:63). The edge is real; the skipped StudyActivity.onCreate is covered by the step 14 fix.
- 18-19, 23: androidx fragment lifecycle, INFERRED (correct).
- 20: FlipableCardFragment.onCreateView -> $1.getItem, FRAMEWORK, FlipableCardFragment.java:79-90. The class FlipableCardFragment$1 exists in the freeDebug classes and holds FragmentStatePagerAdapter. OK.
- 21: $1.getItem -> CardFragment$Builder.build, FlipableCardFragment.java:83. OK.
- 22: Builder.build -> CardFragment.<init>, CardFragment.java:325-326. OK.
- 24: CardFragment.onCreate -> inject, CardFragment.java:102, unconditional. OK.
- 25: DaggerAppComponents$FragmentComponentsImpl.inject -> injectCardFragment. The class file in build/intermediates/javac/freeDebug/.../modules/ contains the injectCardFragment string. OK (non_standard, Dagger).

## Could not check / INFERRED
- androidx (LoaderManager, RecyclerView, ViewPager, fragment manager) and Material: not read; INFERRED is the correct label.
- Anonymous-class numbers QACardActivity$4-$7 follow source order (javap not available); consistent with the graph's $1 and $3.
