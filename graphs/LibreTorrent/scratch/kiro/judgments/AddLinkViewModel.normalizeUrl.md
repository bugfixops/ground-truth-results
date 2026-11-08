# Judgment: AddLinkViewModel.normalizeUrl

Route print: graphs/LibreTorrent/scratch/route_print/AddLinkViewModel.normalizeUrl.txt (18 steps). Judged by Kiro (lead), 2026-11-03, by Appendix D.

Steps 1-17: same nodes and edges as first-draw row 13 (AddLinkDialog.checkUrlField, CORRECT: the link field is two-way bound to viewModel.link); re-read in this print. Graded TRUE on that judged prefix.

| step | edge | from -> to | action true? | condition true? | grade | printed file:lines / note |
|---|---|---|---|---|---|---|
| 1 | Ef4711e98 | S_ENTRY -> MainActivity.onCreate | yes | yes | TRUE | judged prefix; SRC AndroidManifest.xml:43-59; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215 |
| 2 | Ed8e7f5f9 | MainActivity.onCreate -> MainFragment.<init> | yes | yes | TRUE | judged prefix; SRC ui/main/MainActivity.java:182-185; res/values/layouts.xml:1-4; notouch/layouts.xml:1-4; res/layout/activity_main_drawer.xml:22-28; res/layout/activity_main_two_pane.xml:26-32; ui/main/MainFragment |
| 3 | Ee453d286 | MainFragment.<init> -> MainFragment.onAttach | yes | yes | TRUE | judged prefix; SRC ui/main/MainFragment.java:85-87,223-230 |
| 4 | E28c54333 | MainFragment.onAttach -> MainFragment.onCreateView | yes | yes | TRUE | judged prefix; SRC ui/main/MainFragment.java:223-230,113-122 |
| 5 | E2e46bfdf | MainFragment.onCreateView -> MainFragment.onViewCreated | yes | yes | TRUE | judged prefix; SRC ui/main/MainFragment.java:115-127 |
| 6 | E17916b8d | MainFragment.onViewCreated -> MainFragment.initFabSpeedDial | yes | yes | TRUE | judged prefix; SRC ui/main/MainFragment.java:157-208 |
| 7 | Ed7e1785e | MainFragment.initFabSpeedDial -> MainFragment.lambda$initFabSpeedDial$11 | yes | yes | TRUE | judged prefix; SRC ui/main/MainFragment.java:414-431 |
| 8 | E53bc255d | MainFragment.lambda$initFabSpeedDial$11 -> MainFragment.addLinkDialog | yes | yes | TRUE | judged prefix; SRC ui/main/MainFragment.java:416-430; ui/main/MainFragment.java:523-526 |
| 9 | Edb99c793 | MainFragment.addLinkDialog -> AddLinkActivity.onCreate | yes | yes | TRUE | judged prefix; SRC ui/main/MainFragment.java:523-526; AndroidManifest.xml:235-238; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215 |
| 10 | E0884fdcf | AddLinkActivity.onCreate -> AddLinkDialog.newInstance | yes | yes | TRUE | judged prefix; SRC ui/addlink/AddLinkActivity.java:21-37; ui/addlink/AddLinkDialog.java:73-81 |
| 11 | E67270a38 | AddLinkDialog.newInstance -> AddLinkDialog.onAttach | yes | yes | TRUE | judged prefix; SRC ui/addlink/AddLinkDialog.java:73-90 |
| 12 | E0be419ef | AddLinkDialog.onAttach -> AddLinkDialog.onCreateDialog | yes | yes | TRUE | judged prefix; SRC ui/addlink/AddLinkDialog.java:169-192 |
| 13 | E05f42392 | AddLinkDialog.onCreateDialog -> AddLinkDialog.initLayoutView | yes | yes | TRUE | judged prefix; SRC ui/addlink/AddLinkDialog.java:171-191,202-226 |
| 14 | E0bdc65f2 | AddLinkDialog.initLayoutView -> AddLinkDialog.initAlertDialog | yes | yes | TRUE | judged prefix; SRC ui/addlink/AddLinkDialog.java:221-226,228-246 |
| 15 | Eb00ec938 | AddLinkDialog.initAlertDialog -> AddLinkDialog.lambda$initAlertDialog$6 | yes | yes | TRUE | judged prefix; SRC ui/addlink/AddLinkDialog.java:238-245 |
| 16 | Ea674eaf3 | AddLinkDialog.lambda$initAlertDialog$6 -> AddLinkDialog.lambda$initAlertDialog$4 | yes | yes | TRUE | judged prefix; SRC ui/addlink/AddLinkDialog.java:238-241 |
| 17 | E130d2f8c | AddLinkDialog.lambda$initAlertDialog$4 -> AddLinkDialog.addLink | yes | yes | TRUE | judged prefix; SRC ui/addlink/AddLinkDialog.java:238-241,260-288 |
| 18 | E23a4ea72 | AddLinkDialog.addLink -> AddLinkViewModel.normalizeUrl | yes | yes | TRUE | addLink: non-empty link (:266-268), checkUrlField true for non-empty field text (AddLinkDialog.java:290-304), then viewModel.normalizeUrl(s) at :273. Prints: judge_addlink.txt |

**Route verdict: CORRECT.** Premise: the user types a non-empty link before tapping Add (same as first-draw row 13).
