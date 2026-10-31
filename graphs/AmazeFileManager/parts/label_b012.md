STATUS: RUNNING 21:40

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| ColorPref.<clinit> | REACHABLE | FRAMEWORK | Class initialization | SRC ColorPref.java:32 |
| ColorPref.<init> | REACHABLE | EXPLICIT | Instantiated from PreferencesActivity.onCreate via loadPrefFragment | SRC PreferencesActivity.java:258, ColorPref.java:32 |
| ColorPref.checkCustomization | UNREACHABLE | branch_never_taken | Only called from loadSection1; conditional execution path never entered in normal flow | SRC ColorPref.java:226-234 |
| ColorPref.colorChangeDialog | REACHABLE | EXPLICIT | Called from onPreferenceClick for skin/accent preferences | SRC ColorPref.java:101, 103 |
| ColorPref.invalidateColorPreference | UNREACHABLE | branch_never_taken | Called from loadSection1 and invalidateEverything, both conditional paths | SRC ColorPref.java:220, 249 |
| ColorPref.invalidateEverything | REACHABLE | EXPLICIT | Called from loadSection1 listener and colorChangeDialog lambda | SRC ColorPref.java:229, 163 |
| ColorPref.lambda$colorChangeDialog$0 | REACHABLE | EXPLICIT | Lambda callback for color adapter selection | SRC ColorPref.java:136-163 |
| ColorPref.lambda$loadSection1$1 | REACHABLE | EXPLICIT | Lambda callback for color picker dialog listener | SRC ColorPref.java:222-230 |
| ColorPref.loadSection0 | REACHABLE | EXPLICIT | Called from onCreate and switchSections | SRC ColorPref.java:57, 202 |
| ColorPref.loadSection1 | REACHABLE | EXPLICIT | Called from switchSections when switching to section 1 | SRC ColorPref.java:205 |
| ColorPref.onBackPressed | REACHABLE | EXPLICIT | Called from PreferencesActivity.onBackPressed when currentFragment is ColorPref | SRC PreferencesActivity.java:107-108 |
| ColorPref.onCreate | REACHABLE | LIFECYCLE | Fragment lifecycle method called by Android framework | SRC ColorPref.java:51-62 |
| ColorPref.onOptionsItemSelected | REACHABLE | EXPLICIT | Fragment callback for menu item selection | SRC ColorPref.java:74-82 |
| ColorPref.onPause | REACHABLE | LIFECYCLE | Fragment lifecycle method | SRC ColorPref.java:66-69 |
| ColorPref.onPreferenceClick | REACHABLE | EXPLICIT | Preference click listener registered in reloadListeners | SRC ColorPref.java:95-105 |
| ColorPref.onRestoreInstanceState | REACHABLE | EXPLICIT | Called from onCreate when savedInstanceState is not null | SRC ColorPref.java:62, 275-284 |
| ColorPref.onSaveInstanceState | REACHABLE | LIFECYCLE | Fragment lifecycle method for saving state | SRC ColorPref.java:270-273 |
| ColorPref.reloadListeners | REACHABLE | EXPLICIT | Called from onCreate and switchSections | SRC ColorPref.java:59, 207 |
| ColorPref.switchSections | REACHABLE | EXPLICIT | Called from onBackPressed and onOptionsItemSelected | SRC ColorPref.java:87, 78 |
| ColorPref$1.<init> | REACHABLE | EXPLICIT | Anonymous ButtonCallback created in colorChangeDialog | SRC ColorPref.java:179 |
| ColorPref$1.onNeutral | REACHABLE | EXPLICIT | Callback method for neutral button in dialog | SRC ColorPref.java:181-186 |
| ColorPreference.<clinit> | REACHABLE | EXPLICIT | Static initialization accessed via availableColors field in colorChangeDialog | SRC ColorPref.java:137, ColorPreference.java:12-24 |
| ColorPreference.<init> | UNREACHABLE | framework_never_calls | ColorPreference only contains static field, never instantiated in application | SRC ColorPreference.java:10-25 |
| ColorUtils.<init> | UNREACHABLE | framework_never_calls | ColorUtils is utility class with only static methods, constructor never called | SRC ColorUtils.java:18-43 |
| ColorUtils.colorizeIcons | REACHABLE | CALL | Called from RecyclerAdapter.bindViewHolderAsFile to colorize file type icons | SRC RecyclerAdapter.java:668, ColorUtils.java:18-43 |

STATUS: DONE 21:41
