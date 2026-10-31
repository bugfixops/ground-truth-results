# G5-3 route check: AnyMemoWidgetProvider.updateWidget

- Method: AnyMemoWidgetProvider.updateWidget
- Label: REACHABLE (route from S_ENTRY, cold start)
- Steps: 4. Checked: 4.
- Verdict: WRONG (1 wrong step: step 3)

## Wrong steps

Step 3: AnyMemo.onCreate -> AnyMemo.onDestroy (LIFECYCLE, automatic, from the lc_chain loop at graph_def.py:289-290).
- Graph text: "Activity lifecycle / framework callback"; no guard, env=-, state=-.
- Source: AnyMemo.java:399-411 is onDestroy. It runs only when the activity is destroyed. Nothing in onCreate (AnyMemo.java:115-143) ends the activity. The finish() calls in AnyMemo are at AnyMemo.java:178 (inside onRequestPermissionsResult, storage permission denied) and AnyMemo.java:275 (exit button of the unreadable-storage dialog in prepareStoreage()). AnyMemo has no onBackPressed (grep of AnyMemo.java and BaseActivity.java: no hit), so Back on a main tab runs the default finish, which the graph does not model.
- Why WRONG: the direct onCreate -> onDestroy edge has no trigger. In the app, onDestroy follows a user action (Back on a main tab, the denied permission, the storage dialog exit, or rotation). None of them is in the route, so the route is cheap (no ENV) and looks like it needs no user action. The physical order (onCreate, onStart, onResume, ..., onDestroy) is real, but the trigger is missing.
- Fix (graph_def.py):
  a. Line 289: remove 'onDestroy' from the AnyMemo lc_chain tuple.
  b. Add hand edges, one per real exit, each with a trigger:
     - S_MAIN_RECENT, S_MAIN_OPEN, S_MAIN_DOWNLOAD, S_MAIN_MISC -> AnyMemo.onDestroy (SYSTEM), env=ENV_HW_KEY, text "press Back on a main tab (no onBackPressed override: the default finish() runs, then onDestroy)", evidence FW_ACTIVITY + '; SRC ui/AnyMemo.java:399-411'.
     - AnyMemo.onRequestPermissionsResult -> AnyMemo.onDestroy, guard "WRITE_EXTERNAL_STORAGE was denied (AnyMemo.java:175-178 finish)", env = a new env_text for "the user taps Deny in the system permission dialog" (ENV_PERM_DIALOG_STORAGE at graph_def.py:2757 says Allow, so it does not fit).
     - Optional: the exit button of the unreadable-storage dialog (AnyMemo.java:275, an anonymous listener in prepareStoreage()).
  c. Systemic: the same pattern (onDestroy taken from onCreate with no trigger) is in 10 other lc_chain lists: graph_def.py lines 441, 596, 684, 730, 793, 817, 845, 873, 948, 1243. Those classes need the same check.

## Steps checked (OK)

1. S_ENTRY -> AnyMemo.<init> (ENTRY): OK. AndroidManifest.xml:23-33 (MAIN + LAUNCHER). Cold start.
2. AnyMemo.<init> -> AnyMemo.onCreate (LIFECYCLE): claim OK. Same citation defect as G5-1 step 2 (FW_ACTIVITY, graph_def.py:90, no line numbers).
4. AnyMemo.onDestroy -> AnyMemoWidgetProvider.updateWidget (CALL): OK. AnyMemo.java:405 `AnyMemoWidgetProvider.updateWidget(this);` is in onDestroy with no if/else/catch around it (onDestroy is AnyMemo.java:399-411).

## Not checked

- The target body of AnyMemoWidgetProvider.updateWidget (not a step of this route).
- FW citation lines: FW_ACTIVITY (graph_def.py:90) gives none. I did read the destroy dispatch: ActivityThread.java:4370 (mInstrumentation.callActivityOnDestroy), Instrumentation.java:1232-1249 (callActivityOnDestroy calls activity.performDestroy), Activity.java:7203-7208 (performDestroy calls onDestroy at 7208). Use these in the FW_ACTIVITY fix.
