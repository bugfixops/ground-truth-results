# G4-6: NotificationChannelUtil.createConversationNotificationChannel

- Method: NotificationChannelUtil.createConversationNotificationChannel (utils/NotificationChannelUtil.java:70-75, private, @RequiresApi(O)). Its only call site is createNotificationChannels at :43, inside `if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O)` (:36-49).
- Label: REACHABLE (process start -> AMApplication.<init> -> attachBaseContext -> AMApplication.onCreate -> createNotificationChannels -> createConversationNotificationChannel). Needs API 26+ (true on API 27).
- Steps: 5 (show_route.py --dedupe). Checked: 5.
- Verdict: WRONG (1 wrong step: 5)

## Wrong steps

Step 5: NotificationChannelUtil.createNotificationChannels -> createConversationNotificationChannel (CALL, auto edge, evidence NotificationChannelUtil.java:43). The graph has no hand edge for this pair.
- Wrong: the call sits inside `if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O)` (:36). cases.guard_of(utils/NotificationChannelUtil.java, 43) returns exactly this condition. The route shows no guard, so the graph says the call runs on every API level. On API below 26 it never runs. The auto edge has no guard field.
- Fix: add a hand edge for the pair (a hand edge for the same pair suppresses the auto edge, build_graph.py:223-224): e('NotificationChannelUtil.createNotificationChannels', 'NotificationChannelUtil.createConversationNotificationChannel', 'CALL', 'Direct call', guard='Build.VERSION.SDK_INT >= Build.VERSION_CODES.O (API 26+; always true on API 27) (NotificationChannelUtil.java:36)', evidence='SRC utils/NotificationChannelUtil.java:36-43'). Same guard style as the AnyMemo.onCreate edge at graph_def.py:1533.

## Steps checked and OK (4)

- 1 ENTRY S_ENTRY -> AMApplication.<init>: AndroidManifest.xml:20 (android:name=".common.AMApplication") OK. The Application.java citation is not in the tree, so the process-start claim is INFERRED.
- 2 AMApplication.<init> -> attachBaseContext (LIFECYCLE): AMApplication.java:56-60 OK. The order (attach before onCreate) is INFERRED: Application.attach is not in the tree. Replace the Application.java evidence with "INFERRED (framework Application.attach not in tree)". Not counted.
- 3 attachBaseContext -> onCreate (LIFECYCLE): AMApplication.java:62-73 OK. The claim "after every ContentProvider in the manifest" is confirmed by ActivityThread.java:5722 (installContentProviders in handleBindApplication) before :5740 (callApplicationOnCreate). Citation fix: use ActivityThread.java:5722-5740 instead of Application.java (not counted).
- 4 AMApplication.onCreate -> createNotificationChannels (CALL, auto edge): AMApplication.java:72 OK. No guard (guard_of at :72 is empty). notificationChannelUtil is injected at :71 (Dagger, INFERRED).

## Not checked

- Application.java / Application.attach / Instrumentation.newApplication: not in fw_src (only ActivityThread.java and LoadedApk.java are there). Steps 1-2 stay INFERRED.
- DaggerAppComponents (the injection at :71): generated code, no source, INFERRED.
- What the channel does on API 26+ (notification behaviour): out of scope for the route.
