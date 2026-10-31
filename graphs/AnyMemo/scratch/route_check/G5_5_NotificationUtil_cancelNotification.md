# G5-5 route check: NotificationUtil.cancelNotification

- Method: NotificationUtil.cancelNotification
- Label: REACHABLE (route from S_ENTRY, cold start)
- Steps: 4. Checked: 4.
- Verdict: WRONG (1 wrong step: step 3)

## Wrong steps

Step 3: AnyMemo.onCreate -> AnyMemo.onDestroy (LIFECYCLE, automatic, from the lc_chain loop at graph_def.py:289-290).
- Graph text: "Activity lifecycle / framework callback"; no guard, env=-, state=-.
- Why WRONG: the same error as G5-3 step 3. onDestroy (AnyMemo.java:399-411) runs only after the activity is destroyed by a user action (Back on a main tab, which has no onBackPressed override in AnyMemo or BaseActivity; the permission denied at AnyMemo.java:175-178; the storage dialog exit at AnyMemo.java:275; or rotation). The direct onCreate -> onDestroy edge has no trigger, so the route looks free of user action.
- Fix (graph_def.py): remove 'onDestroy' from the AnyMemo lc_chain tuple at line 289, and add the real exits as hand edges with their triggers (Back key on S_MAIN_RECENT / S_MAIN_OPEN / S_MAIN_DOWNLOAD / S_MAIN_MISC with env=ENV_HW_KEY; the permission-denied path from AnyMemo.onRequestPermissionsResult with a guard). Full text in G5-3.
- Systemic: the same pattern is in 10 other lc_chain lists (graph_def.py lines 441, 596, 684, 730, 793, 817, 845, 873, 948, 1243). See G5-3.

## Steps checked (OK)

1. S_ENTRY -> AnyMemo.<init> (ENTRY): OK. AndroidManifest.xml:23-33 (MAIN + LAUNCHER). Cold start.
2. AnyMemo.<init> -> AnyMemo.onCreate (LIFECYCLE): claim OK. Same citation defect as G5-1 step 2.
4. AnyMemo.onDestroy -> NotificationUtil.cancelNotification (CALL, bytecode AnyMemo.java:406): OK. AnyMemo.java:406 `notificationUtil.cancelNotification();` is in onDestroy after super.onDestroy() (403) and AnyMemoWidgetProvider.updateWidget(this) (405). No if/else/catch around it.

## Not checked

- The body of NotificationUtil.cancelNotification (the route target, not a step).
- FW citation defect as in G5-1 step 2 and G5-3 (the destroy dispatch lines are in G5-3).
