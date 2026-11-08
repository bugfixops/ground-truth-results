STATUS: RUNNING 21:45

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| Drawer.<clinit> | REACHABLE | SYSTEM | Static initialization when class loads | SRC Drawer.java:1 class declaration with static fields |
| Drawer.<init> | REACHABLE | CALL | Called from MainActivity.initialiseViews | SRC MainActivity.java:1425 new Drawer(this) |
| Drawer.addNewItem | REACHABLE | CALL | Called from refreshDrawer for menu items | SRC Drawer.java:282+ multiple addNewItem calls in refreshDrawer |
| Drawer.close | REACHABLE | CALL | Called from constructor, lambdas, MainActivity | SRC Drawer.java:211,212,413,429; MainActivity.java:705 |
| Drawer.closeIfNotLocked | REACHABLE | CALL | Called from onNavigationItemSelected | SRC Drawer.java:594 closeIfNotLocked() in navigation handler |
| Drawer.deselectEverything | REACHABLE | CALL | Called from MainActivity.onResume, selectCorrectDrawerItemForPath | SRC MainActivity.java:1113; Drawer.java:675 |
| Drawer.getFirstPath | REACHABLE | CALL | Called from MainActivity onCreate for tab setup | SRC MainActivity.java:453-454 drawer.getFirstPath() |
| Drawer.getPhoneStorageCount | REACHABLE | CALL | Called from MainActivity onCreate for tab setup | SRC MainActivity.java:447 drawer.getPhoneStorageCount() > 1 |
| Drawer.getSecondPath | REACHABLE | CALL | Called from MainActivity onCreate for tab setup | SRC MainActivity.java:448,457 drawer.getSecondPath() |
| Drawer.isLocked | REACHABLE | CALL | Called from MainActivity.onBackPressed, onNavigationItemSelected | SRC MainActivity.java:704; Drawer.java:595 |
| Drawer.isOpen | REACHABLE | CALL | Called from MainActivity.onBackPressed | SRC MainActivity.java:704 drawer.isOpen() |
| Drawer.isSomethingSelected | REACHABLE | CALL | Called from MainActivity.onSaveInstanceState | SRC MainActivity.java:1076 drawer.isSomethingSelected() |
| Drawer.lambda$addNewItem$4 | REACHABLE | CALL | Lambda for action view click from addNewItem | SRC Drawer.java:462 (view) -> onNavigationItemActionClick |
| Drawer.lambda$addNewItem$5 | REACHABLE | CALL | Lambda for action view click from addNewItem overload | SRC Drawer.java:475+ second addNewItem overload with lambda |
| Drawer.lambda$new$0 | REACHABLE | CALL | Long click listener lambda from constructor | SRC Drawer.java:141-152 drawerHeaderView.setOnLongClickListener |
| Drawer.lambda$onNavigationItemSelected$6 | REACHABLE | CALL | Lambda for SAF dialog from onNavigationItemSelected | SRC Drawer.java:587 dialog.getActionButton().setOnClickListener |
| Drawer.lambda$refreshDrawer$1 | REACHABLE | CALL | Lambda for FTP menu item from refreshDrawer | SRC Drawer.java:404-415 new MenuMetadata for FTP |
| Drawer.lambda$refreshDrawer$2 | REACHABLE | CALL | Lambda for Apps menu item from refreshDrawer | SRC Drawer.java:418-431 new MenuMetadata for Apps |
| Drawer.lambda$refreshDrawer$3 | REACHABLE | CALL | Lambda for Settings menu item from refreshDrawer | SRC Drawer.java:433-439 new MenuMetadata for Settings |
| Drawer.lock | REACHABLE | CALL | Called from constructor for tablet mode | SRC Drawer.java:204 lock(DrawerLayout.LOCK_MODE_LOCKED_OPEN) |
| Drawer.lockIfNotOnTablet | REACHABLE | CALL | Called from MainFragment action mode | SRC MainFragment.java:509 getMainActivity().getDrawer().lockIfNotOnTablet |
| Drawer.onActivityResult | REACHABLE | RESULT | Called from MainActivity.onActivityResult | SRC MainActivity.java:1309 drawer.onActivityResult |
| Drawer.onConfigurationChanged | REACHABLE | LIFECYCLE | Called from MainActivity.onConfigurationChanged | SRC MainActivity.java:1070 drawer.onConfigurationChanged |
| Drawer.onDrawerClosed | REACHABLE | CALL | Called from onNavigationItemSelected, lambdas, ActionBarDrawerToggle | SRC Drawer.java:225,414,430,595 |
| Drawer.onNavigationItemActionClick | REACHABLE | CALL | Called from lambda$addNewItem$4 and $5 | SRC Drawer.java:462 lambda calling onNavigationItemActionClick |
| Drawer.onNavigationItemSelected | REACHABLE | FRAMEWORK | NavigationView.OnNavigationItemSelectedListener callback | SRC Drawer.java:97 implements interface, 164 setListener |
| Drawer.onOptionsItemSelected | REACHABLE | CALL | Called from MainActivity.onOptionsItemSelected | SRC MainActivity.java:931 drawer.onOptionsItemSelected |
| Drawer.open | REACHABLE | CALL | Called from constructor for tablet mode | SRC Drawer.java:205,208 open() calls in constructor |
| Drawer.refreshDrawer | REACHABLE | CALL | Called from MainActivity.onResume and many other lifecycle points | SRC MainActivity.java:1112,385,440+ multiple calls |
| Drawer.resetPendingPath | REACHABLE | CALL | Called from MainActivity when OTG access denied | SRC MainActivity.java:1407 drawer.resetPendingPath() |
| Drawer.selectCorrectDrawerItemForPath | REACHABLE | CALL | Called from MainFragment, TabFragment on navigation | SRC MainFragment.java:1423; TabFragment.java:224,304 |
| Drawer.setBackgroundColor | REACHABLE | CALL | Called from MainActivity.updatePathColor | SRC MainActivity.java:1479 drawer.setBackgroundColor |
| Drawer.setDrawerHeaderBackground | REACHABLE | CALL | Called from MainActivity.initialiseViews | SRC MainActivity.java:1445 drawer.setDrawerHeaderBackground() |
| Drawer.setDrawerIndicatorEnabled | REACHABLE | CALL | Called from MainActivity.onCreate | SRC MainActivity.java:348 drawer.setDrawerIndicatorEnabled() |
| Drawer.setNavViewDimension | UNREACHABLE | no_trigger_in_app | Method call is commented out in constructor | SRC Drawer.java:160-163 shows commented call site |
| Drawer.setSomethingSelected | REACHABLE | CALL | Called from MainActivity onCreate and navigation actions | SRC MainActivity.java:322,392,406,792,1592 |
| Drawer.syncState | REACHABLE | LIFECYCLE | Called from MainActivity.onPostCreate | SRC MainActivity.java:1063 drawer.syncState() |
| Drawer.unlockIfNotOnTablet | REACHABLE | CALL | Called from constructor and MainFragment | SRC Drawer.java:209; MainFragment.java:771 |
| Drawer$1.<init> | REACHABLE | CALL | Anonymous ActionBarDrawerToggle created in constructor | SRC Drawer.java:214-232 new ActionBarDrawerToggle anonymous class |
| Drawer$1.onDrawerClosed | REACHABLE | FRAMEWORK | ActionBarDrawerToggle callback when drawer closes | SRC Drawer.java:224-225 override in anonymous class |
| Drawer$1.onDrawerOpened | REACHABLE | FRAMEWORK | ActionBarDrawerToggle callback when drawer opens | SRC Drawer.java:228-230 override in anonymous class |
| Drawer$2.<init> | REACHABLE | CALL | Anonymous ImageListener created in setDrawerHeaderBackground | SRC Drawer.java:657 new ImageLoader.ImageListener |
| Drawer$2.onResponse | REACHABLE | FRAMEWORK | ImageLoader callback on successful load | SRC Drawer.java:659-662 override in ImageListener |
| Drawer$2.onErrorResponse | REACHABLE | FRAMEWORK | ImageLoader callback on error | SRC Drawer.java:665 override in ImageListener |

STATUS: DONE 21:49
