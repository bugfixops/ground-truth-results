# G5-1 route check: BaseActivity$1.<init>

- Method: BaseActivity$1.<init>
- Label: REACHABLE (route from S_ENTRY, cold start)
- Steps: 5. Checked: 5.
- Verdict: WRONG (1 wrong step: step 4)

## Wrong steps

Step 4: BaseActivity.onCreate -> BaseActivity.enableImmersiveMode (CALL, explicit, bytecode BaseActivity.java:37).
- Graph text: guard "the fullscreen mode preference is on (common/BaseActivity.java:36-37)"; env=-, state=- (no needs_state).
- Source: BaseActivity.java:36-37 `if(settings.getBoolean(AMPrefKeys.FULLSCREEN_MODE_KEY, false)) {` then `enableImmersiveMode();`. The guard text matches the code.
- Why WRONG: the key is a Settings checkbox (res/xml/option_screen.xml:66-69, android:defaultValue="false"). No fixture sets it (grep of final_java_only/_fixtures for "fullscreen": no hit). On a fresh install the branch never runs. It needs an earlier action (ticking Fullscreen mode in Settings and saving it), which is a STATE (settings), not a guard. The route says state=- and so claims no earlier action.
- Fix (graph_def.py): in the GATE dict, entry ('BaseActivity.onCreate', 'BaseActivity.enableImmersiveMode') at line 2773, add 'needs_state': NEED_FULLSCREEN. Define NEED_FULLSCREEN = state_text('The Fullscreen mode box in Settings was ticked and saved before (SharedPreferences fullscreen_mode = true; option_screen.xml:66-69), so the flag is on when this activity is created', ('settings',)) next to NEED_PREF_SAVED (graph_def.py:1708). Keep the guard text. Rebuild and check the route stays REACHABLE with a settings state.

## Steps checked (OK)

1. S_ENTRY -> AnyMemo.<init> (ENTRY): OK. AndroidManifest.xml:23-33 has the MAIN + LAUNCHER filter for .ui.AnyMemo. Cold start.
2. AnyMemo.<init> -> AnyMemo.onCreate (LIFECYCLE): claim OK. Citation defect only: FW_ACTIVITY (graph_def.py:90) has no line numbers. Lines I read in fw_src: ActivityThread.java:2729-2731 (mInstrumentation.callActivityOnCreate), Instrumentation.java:1212-1216 (callActivityOnCreate calls activity.performCreate), Activity.java:6993-6999 (performCreate calls onCreate). Fix: give FW_ACTIVITY these lines.
3. AnyMemo.onCreate -> BaseActivity.onCreate (CALL): OK. AnyMemo.java:118 `super.onCreate(savedInstanceState);` is not inside any if/else (onCreate is AnyMemo.java:115-143).
4. WRONG (see above).
5. BaseActivity.enableImmersiveMode -> BaseActivity$1.<init> (CALL): OK. BaseActivity.java:159 `getWindow().getDecorView().setOnSystemUiVisibilityChangeListener(new View.OnSystemUiVisibilityChangeListener() {` is in enableImmersiveMode (declared at line 145). Lines 145-159 have no if/else/catch/loop. The listener object is created by the `new` at line 159.

## Not checked

- Nothing else. The BaseActivity$1 body is not part of this route (its <init> is the target).
