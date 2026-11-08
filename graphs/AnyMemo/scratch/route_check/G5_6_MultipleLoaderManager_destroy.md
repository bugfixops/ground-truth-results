# G5-6 route check: MultipleLoaderManager.destroy

- Method: MultipleLoaderManager.destroy
- Label: REACHABLE (route from S_ENTRY, cold start)
- Steps: 4. Checked: 4.
- Verdict: WRONG (2 wrong steps: step 3 and step 4)

## Wrong steps

Step 3: AnyMemo.onCreate -> AnyMemo.onDestroy (LIFECYCLE, automatic, lc_chain at graph_def.py:289-290).
- Same error as G5-3 step 3 (no trigger for the destroy). Fix: see G5-3 (remove 'onDestroy' from the line-289 tuple; add the real exits with their triggers).

Step 4: AnyMemo.onDestroy -> MultipleLoaderManager.destroy (CALL, bytecode AnyMemo.java:409).
- Graph text: no guard, env=-, state=-.
- Source: AnyMemo.java:408 `if (multipleLoaderManager != null) {`, line 409 `multipleLoaderManager.destroy();`. The guard is in the code and not in the graph (rule b).
- Note: the field is `@Inject MultipleLoaderManager multipleLoaderManager;` (AnyMemo.java:98), so it is set by injection and the guard is always true in practice. It still has to be in the graph.
- Fix (graph_def.py): add to the GATE dict (starts at line 2769; this edge is automatic, so the GATE key is enough): ('AnyMemo.onDestroy', 'MultipleLoaderManager.destroy'): {'guard': 'multipleLoaderManager != null (AnyMemo.java:408)'}.

## Steps checked (OK)

1. S_ENTRY -> AnyMemo.<init> (ENTRY): OK. AndroidManifest.xml:23-33 (MAIN + LAUNCHER). Cold start.
2. AnyMemo.<init> -> AnyMemo.onCreate (LIFECYCLE): claim OK. Same citation defect as G5-1 step 2.

## Not checked

- The body of MultipleLoaderManager.destroy (route target, not a step).
- FW citation defect (as in G5-3; the destroy dispatch lines are ActivityThread.java:4370, Instrumentation.java:1232-1249, Activity.java:7203-7208).
