# G5-4 route check: BaseActivity.onResume

- Method: BaseActivity.onResume
- Label: REACHABLE (route from S_ENTRY, cold start)
- Steps: 4. Checked: 4.
- Verdict: CORRECT (0 wrong steps)

## Steps checked (OK)

1. S_ENTRY -> AnyMemo.<init> (ENTRY): OK. AndroidManifest.xml:23-33 (MAIN + LAUNCHER for .ui.AnyMemo). Cold start, so no earlier visit is needed.
2. AnyMemo.<init> -> AnyMemo.onCreate (LIFECYCLE): claim OK. Citation defect only: FW_ACTIVITY (graph_def.py:90) has no line numbers. Lines I read: ActivityThread.java:2729-2731, Instrumentation.java:1212-1216, Activity.java:6993-6999 (see G5-1 step 2).
3. AnyMemo.onCreate -> AnyMemo.onResume (LIFECYCLE): OK. The route skips onStart, which is an intermediate framework callback with no app code. The resume dispatch is Activity.java:7098-7107 (performResume calls mInstrumentation.callActivityOnResume at line 7107, read). That callActivityOnResume reaches onResume is INFERRED (Instrumentation.java:1353 not printed). AnyMemo.onCreate has no finish() on any path (AnyMemo.java:115-143), so the resume is not cut short. The first-resume state (storage permission, loadUiComponents) is not needed for this target, because the call at step 4 runs before any branch in onResume.
4. AnyMemo.onResume -> BaseActivity.onResume (CALL, bytecode AnyMemo.java:147): OK. AnyMemo.java:146 `public void onResume() {` and line 147 `super.onResume();` is not inside any if/else. The host is AnyMemo, which is the right subclass for this route (BaseActivity.onResume is shared by all subclasses; this route reaches it from AnyMemo only).

## Not checked

- The Instrumentation step from performResume to onResume body (see step 3, INFERRED).
- FW citation defect as in G5-1 step 2.
