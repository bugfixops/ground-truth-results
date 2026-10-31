# G2-3 route check: AMDateUtil.<init>

- Method: AMDateUtil.<init> (`@Inject public AMDateUtil(@ForApplication Context)`, utils/AMDateUtil.java:38-39)
- Label: REACHABLE
- Steps: 23; checked: 23 (every step read in the source; steps 1-5 are the cold-start edges already checked in G2-1)
- Verdict: CORRECT (0 wrong steps)

Rule used: a step is WRONG only if the transition cannot happen or its guard or STATE is false. Kind labels, skipped hops and citation gaps are listed below but do not count as wrong.

## Wrong steps
None.

## Steps checked as OK (short)
- 6 guard itemId == recent_tab_menu (AnyMemo.java:240-241, 263). 7 RecentListFragment.<init> -> onAttach (RecentListFragment.java:134-141, two LocalBroadcastManager receivers).
- 8 onAttach -> onCreate (127-132, inject at 130). 9 onCreate -> onCreateView (169).
- 10 onCreateView -> RecentListAdapter.onBindViewHolder via setAdapter (182) and RecyclerView (non_standard).
- 11 onBindViewHolder sets the row click listener (413). STATE holds: a row is bound only when an entry exists.
- 12 onClick -> StudyActivity.<init>, guard getSelectedItemCount() == 0 (416-422).
- 13 cold dispatch: ActivityThread.java:2669 newActivity, 2729 callActivityOnCreate -> Instrumentation.java:1212-1214 -> Activity.performCreate -> onCreate.
- 15 onCreateLoader -> dbLoadInBackground: forceLoad (StudyActivity.java:435) -> DBLoader.loadInBackground (DBLoader.java:42-46) -> dbLoadInBackground (StudyActivity.java:475).
- 16 dbLoadInBackground -> onLoadFinished (440-443).
- 18 onPostInit -> setupGradeButtons. STATE matches StudyActivity.java:292-296 (returns early when there is no current card).
- 19 setupGradeButtons -> GradeButtonsFragment.<init> (533). 20 <init> -> onCreate after ft.commit (538-540; onCreate at 99-102).
- 21 onCreate -> DaggerAppComponents inject: bytecode record, GradeButtonsFragment.java:101 (cha).
- 22 inject -> injectGradeButtonsFragment: bytecode record, DaggerAppComponents.java:254 (generated file, not in the tree).
- 23 the field `@Inject AMDateUtil amDateUtil` is at GradeButtonsFragment.java:83, as the step says.

## Compressed or mislabelled steps (not counted as wrong)
- Step 14 (StudyActivity.onCreate -> onCreateLoader, FRAMEWORK; graph_def.py:598). The real chain is onCreate (StudyActivity.java:121) -> startInit (QACardActivity.java:147-168) -> MultipleLoaderManager.startLoading (79-98; initLoader at 93) -> onCreateLoader. The outcome is right; two hops are skipped.
- Step 17 (onLoadFinished -> onPostInit, labelled CALL/explicit; graph_def.py:426). The code posts a runnable: checkAllLoadersCompleted (MultipleLoaderManager.java:104-114) -> handler.post at line 112 -> onPostInitRunnable.run (QACardActivity.java:658-662) -> onPostInit. The kind should be ASYNC (posted to the main looper), and two hops are missing. The STATE "every loader reported" matches 104-108.
- Step 13 citation is "Activity.java, no line numbers". It should name Instrumentation.java:1212-1214 and ActivityThread.java:2729.
- Step 23 (injectGradeButtonsFragment -> AMDateUtil.<init>, CALL; hand edge at graph_def.py:2107). The bytecode extract has no record from injectGradeButtonsFragment to the constructor. Its only recorded callee is Provider.get, and AMDateUtil_Factory has no methods in the extract. The edge skips the generated Provider.get -> AMDateUtil_Factory.get hop. The @ForApplication Context comes from the Dagger provider. The outcome is right. The evidence text "bytecode line 254" belongs to step 22, not 23.

## Not checked
- androidx LoaderManager, RecyclerView and FragmentManager source not read (INFERRED reasons kept for steps 9, 10, 14, 15, 16, 20).
- DaggerAppComponents generated code is not in the tree; checked only through the bytecode extract.
- Steps 1-5 not re-read in this pass (G2-1 covers them).
