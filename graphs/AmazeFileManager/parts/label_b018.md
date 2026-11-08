STATUS: RUNNING 22:51

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| CustomNavigationView.<init> | REACHABLE | | Layout inflation from MainActivity.setContentView | SRC main_toolbar.xml:58; CustomNavigationView.java:22-24 |
| CustomNavigationView.setNavigationItemSelectedListener | REACHABLE | | Called from constructor line 24 and Drawer constructor | SRC CustomNavigationView.java:24,27-29; Drawer.java:162 |
| CustomNavigationView.onNavigationItemSelected | REACHABLE | | GUI callback when user clicks drawer item | SRC CustomNavigationView.java:33-44 implements OnNavigationItemSelectedListener |
| CustomNavigationView.onItemChecked | REACHABLE | | Called from onNavigationItemSelected | SRC CustomNavigationView.java:38,42,47-49 |
| CustomNavigationView.getSelected | REACHABLE | | Called from Drawer.refreshDrawer | SRC Drawer.java:451; CustomNavigationView.java:62-65 |
| CustomNavigationView.setCheckedItem | REACHABLE | | Called from Drawer.selectCorrectDrawerItemForPath | SRC Drawer.java:678; CustomNavigationView.java:56-59 |
| CustomNavigationView.deselectItems | REACHABLE | | Called from Drawer.deselectEverything | SRC Drawer.java:715; CustomNavigationView.java:61-63 |
| CustomNavigationView.onSaveInstanceState | UNREACHABLE | framework_never_calls | API 27 target; isNavigationViewSavedStateMissing returns true for API 23-28, skips SavedState | SRC CustomNavigationView.java:67-69,117 guard blocks SavedState usage |
| CustomNavigationView.onRestoreInstanceState | UNREACHABLE | framework_never_calls | API 27 target; isNavigationViewSavedStateMissing returns true for API 23-28, skips SavedState | SRC CustomNavigationView.java:84-87,117 guard blocks SavedState usage |
| CustomNavigationView.isNavigationViewSavedStateMissing | UNREACHABLE | no_trigger_in_app | Only called from unreachable onSaveInstanceState/onRestoreInstanceState | SRC CustomNavigationView.java:67,84,117 |
| CustomNavigationView$SavedState.<clinit> | UNREACHABLE | framework_never_calls | SavedState not used on API 27 due to isNavigationViewSavedStateMissing | SRC CustomNavigationView.java:120,117 |
| CustomNavigationView$SavedState.<init> | UNREACHABLE | framework_never_calls | SavedState(Parcelable) not instantiated on API 27 | SRC CustomNavigationView.java:123-125,67-69 |
| CustomNavigationView$SavedState.<init> | UNREACHABLE | framework_never_calls | SavedState(Parcel) not used on API 27 | SRC CustomNavigationView.java:127-130,84-87 |
| CustomNavigationView$SavedState.writeToParcel | UNREACHABLE | framework_never_calls | SavedState.writeToParcel not called since SavedState not created | SRC CustomNavigationView.java:132-135 |
| CustomNavigationView$SavedState$1.<init> | UNREACHABLE | framework_never_calls | CREATOR not instantiated since SavedState not parceled | SRC CustomNavigationView.java:138-145 |
| CustomNavigationView$SavedState$1.createFromParcel | UNREACHABLE | framework_never_calls | CREATOR.createFromParcel not called on API 27 | SRC CustomNavigationView.java:139-141,84-87 |
| CustomNavigationView$SavedState$1.newArray | UNREACHABLE | framework_never_calls | CREATOR.newArray not called on API 27 | SRC CustomNavigationView.java:142-144,117 |
| CustomSshJConfig.<init> | REACHABLE | | Instantiated when creating SSH clients | SRC SshAuthenticationTask.java:119; GetSshHostFingerprintTask.java:84 |
| CustomSshJConfig.init | REACHABLE | | Called from MainActivity.onCreate | SRC MainActivity.java:286; CustomSshJConfig.java:44-49 |
| CustomSshJConfig.initSignatureFactories | UNREACHABLE | framework_never_calls | Protected override not invoked by DefaultConfig; INFERRED source not read | SRC CustomSshJConfig.java:53-55; INFERRED DefaultConfig not read |
| CustomSshJConfig.initRandomFactory | UNREACHABLE | framework_never_calls | Protected override not invoked by DefaultConfig; INFERRED source not read | SRC CustomSshJConfig.java:57-60; INFERRED DefaultConfig not read |

STATUS: DONE 22:55
