STATUS: START 22:11

| Method | Label | Kind | Reason | Evidence |
|--------|-------|------|--------|----------|
| ProgressHandler.<init>(int,long) | UNREACHABLE | no_trigger_in_app | two-argument constructor never called; all call sites use no-argument constructor | SRC ProgressHandler.java:48-51, grep output showing all callers use no-arg constructor |
| RecyclerPreloadModelProvider.getPreloadItems | REACHABLE | FRAMEWORK | Glide RecyclerViewPreloader calls via ListPreloader.PreloadModelProvider interface | SRC RecyclerAdapter.java:388-389, RecyclerPreloadModelProvider.java:23,35-38 |
| RootHelper.<init> | UNREACHABLE | no_trigger_in_app | utility class with only static methods, constructor never called | SRC RootHelper.java:36, grep -rn "new RootHelper" shows no matches |
| RootHelper.generateBaseFile(DocumentFile) | UNREACHABLE | no_trigger_in_app | DocumentFile overload never called; all call sites use File parameter overload | SRC RootHelper.java:151-158, grep shows all callers use File parameter |
| RootHelper.lambda$runShellCommandToList$0 | REACHABLE | ASYNC | lambda desugared from runShellCommandToList callback | SRC RootHelper.java:50 |
| RootHelper.runNonRootShellCommand | UNREACHABLE | no_trigger_in_app | deprecated method never called | SRC RootHelper.java:83-94, grep shows only definition |
| RootUtils.<init> | UNREACHABLE | no_trigger_in_app | utility class with only static methods, constructor never called | SRC RootUtils.java:15, grep -rn "new RootUtils" shows no matches |
| RootUtils.getFilePermissions | UNREACHABLE | no_trigger_in_app | private method never called within class | SRC RootUtils.java:163-166, grep shows only definition |
| RootUtils.lambda$changePermissions$0 | REACHABLE | ASYNC | lambda desugared from changePermissions callback | SRC RootUtils.java:117-121 |
| ScrimInsetsRelativeLayout.draw | UNREACHABLE | no_trigger_in_app | custom view never instantiated in any XML layout or Java code | SRC ScrimInsetsRelativeLayout.java:75-100, grep in XML/Java shows no usage |
| ScrimInsetsRelativeLayout.fitSystemWindows | UNREACHABLE | no_trigger_in_app | custom view never instantiated in any XML layout or Java code | SRC ScrimInsetsRelativeLayout.java:66-74, grep in XML/Java shows no usage |
| ScrimInsetsRelativeLayout.init | UNREACHABLE | no_trigger_in_app | custom view never instantiated in any XML layout or Java code | SRC ScrimInsetsRelativeLayout.java:57-65, grep in XML/Java shows no usage |
| ScrimInsetsRelativeLayout.onAttachedToWindow | UNREACHABLE | no_trigger_in_app | custom view never instantiated in any XML layout or Java code | SRC ScrimInsetsRelativeLayout.java:102-108, grep in XML/Java shows no usage |
| ScrimInsetsRelativeLayout.onDetachedFromWindow | UNREACHABLE | no_trigger_in_app | custom view never instantiated in any XML layout or Java code | SRC ScrimInsetsRelativeLayout.java:110-116, grep in XML/Java shows no usage |
| ScrimInsetsRelativeLayout.setOnInsetsCallback | UNREACHABLE | no_trigger_in_app | custom view never instantiated in any XML layout or Java code | SRC ScrimInsetsRelativeLayout.java:123-125, grep in XML/Java shows no usage |

STATUS: DONE 22:14
