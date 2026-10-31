# ---- Helper batch_022 label part (2024-12-27)
# Drawer class - Navigation backbone for AmazeFileManager

# Drawer.<clinit> - static initializer
# REACHABLE via class loading when MainActivity creates Drawer instance

e('MainActivity.initialiseViews', 'Drawer.<init>', 'CALL', 'MainActivity creates Drawer in initialiseViews',
  evidence='SRC Drawer.java:133 shows constructor, MainActivity.java:1425 shows new Drawer(this)')

e('Drawer.<init>', 'Drawer.lock', 'CALL', 'Constructor calls lock for tablet mode',
  evidence='SRC Drawer.java:204 shows lock(DrawerLayout.LOCK_MODE_LOCKED_OPEN) in tablet branch')

e('Drawer.<init>', 'Drawer.open', 'CALL', 'Constructor calls open for tablet mode',
  evidence='SRC Drawer.java:205 shows open() call in tablet branch')

e('Drawer.<init>', 'Drawer.unlockIfNotOnTablet', 'CALL', 'Constructor calls unlockIfNotOnTablet for phone mode',
  evidence='SRC Drawer.java:209 shows unlockIfNotOnTablet() in else branch')

e('Drawer.<init>', 'Drawer.close', 'CALL', 'Constructor calls close for phone mode',
  evidence='SRC Drawer.java:210 shows close() call in else branch')

# Framework callback from NavigationView
e('FRAMEWORK', 'Drawer.onNavigationItemSelected', 'FRAMEWORK', 'NavigationView.OnNavigationItemSelectedListener callback',
  evidence='SRC Drawer.java:97 implements NavigationView.OnNavigationItemSelectedListener, line 164 sets listener')

e('Drawer.onNavigationItemSelected', 'Drawer.closeIfNotLocked', 'CALL', 'Closes drawer after navigation',
  evidence='SRC Drawer.java:594 shows closeIfNotLocked() call in ITEM_ENTRY case')

e('Drawer.onNavigationItemSelected', 'Drawer.onDrawerClosed', 'CALL', 'Handles locked drawer navigation',
  evidence='SRC Drawer.java:595 shows if (isLocked()) { onDrawerClosed(); }')

e('Drawer.onNavigationItemSelected', 'Drawer.lambda$onNavigationItemSelected$6', 'CALL', 'Lambda for SAF dialog callback',
  evidence='SRC Drawer.java:587 shows lambda (v) -> ... in dialog.getActionButton')

# refreshDrawer edges
e('MainActivity.onResume', 'Drawer.refreshDrawer', 'CALL', 'Refresh drawer on activity resume',
  evidence='SRC MainActivity.java:1112 shows drawer.refreshDrawer()')

e('Drawer.refreshDrawer', 'Drawer.addNewItem', 'CALL', 'Adds menu items for storages',
  evidence='SRC Drawer.java:282 shows addNewItem(menu, STORAGES_GROUP, ...) calls')

e('Drawer.refreshDrawer', 'Drawer.lambda$refreshDrawer$1', 'CALL', 'Lambda for FTP menu item',
  evidence='SRC Drawer.java:404 shows new MenuMetadata(() -> { ... }) for FTP')

e('Drawer.refreshDrawer', 'Drawer.lambda$refreshDrawer$2', 'CALL', 'Lambda for Apps menu item',
  evidence='SRC Drawer.java:420 shows new MenuMetadata(() -> { ... }) for Apps')

e('Drawer.refreshDrawer', 'Drawer.lambda$refreshDrawer$3', 'CALL', 'Lambda for Settings menu item',
  evidence='SRC Drawer.java:433 shows new MenuMetadata(() -> { ... }) for Settings')

# Lambda edges to fragments
e('Drawer.lambda$refreshDrawer$1', 'Drawer.close', 'CALL', 'Close drawer after FTP selection',
  evidence='SRC Drawer.java:413 shows if (!isDrawerLocked) close()')

e('Drawer.lambda$refreshDrawer$1', 'Drawer.onDrawerClosed', 'CALL', 'Handle locked drawer FTP selection',
  evidence='SRC Drawer.java:414 shows else onDrawerClosed()')

e('Drawer.lambda$refreshDrawer$2', 'Drawer.close', 'CALL', 'Close drawer after Apps selection',
  evidence='SRC Drawer.java:429 shows if (!isDrawerLocked) close()')

e('Drawer.lambda$refreshDrawer$2', 'Drawer.onDrawerClosed', 'CALL', 'Handle locked drawer Apps selection',
  evidence='SRC Drawer.java:430 shows else onDrawerClosed()')

e('Drawer.lambda$refreshDrawer$2', 'AppsListFragment.<init>', 'CALL', 'Creates AppsListFragment',
  evidence='SRC Drawer.java:421 shows new AppsListFragment()')

# addNewItem edges
e('Drawer.addNewItem', 'Drawer.lambda$addNewItem$4', 'CALL', 'Lambda for action view click listener',
  evidence='SRC Drawer.java:462 shows (view) -> onNavigationItemActionClick(item)')

e('Drawer.lambda$addNewItem$4', 'Drawer.onNavigationItemActionClick', 'CALL', 'Delegates to action click handler',
  evidence='SRC Drawer.java:462 shows lambda calling onNavigationItemActionClick(item)')

# onDrawerClosed edges
e('Drawer.onDrawerClosed', 'MainActivity.goToMain', 'CALL', 'Navigate to path when no main fragment',
  evidence='SRC Drawer.java:551 shows mainActivity.goToMain(pendingPath)')

# Getters called from MainActivity
e('MainActivity.onResume', 'Drawer.deselectEverything', 'CALL', 'Deselect drawer items on resume',
  evidence='SRC MainActivity.java:1113 shows drawer.deselectEverything()')

# Action view manager delegation
e('Drawer.onNavigationItemSelected', 'ActionViewStateManager.deselectCurrentActionView', 'CALL', 'Deselect previous item',
  evidence='SRC Drawer.java:559 shows actionViewStateManager.deselectCurrentActionView()')

e('Drawer.onNavigationItemSelected', 'ActionViewStateManager.selectActionView', 'CALL', 'Select current item',
  evidence='SRC Drawer.java:560 shows actionViewStateManager.selectActionView(item)')

e('Drawer.deselectEverything', 'ActionViewStateManager.deselectCurrentActionView', 'CALL', 'Deselect all action views',
  evidence='SRC Drawer.java:712 shows actionViewStateManager.deselectCurrentActionView()')

e('Drawer.refreshDrawer', 'ActionViewStateManager.deselectCurrentActionView', 'CALL', 'Clear selection on refresh',
  evidence='SRC Drawer.java:254 shows actionViewStateManager.deselectCurrentActionView()')

e('Drawer.selectCorrectDrawerItemForPath', 'ActionViewStateManager.selectActionView', 'CALL', 'Select item for path',
  evidence='SRC Drawer.java:679 shows actionViewStateManager.selectActionView(item)')

e('Drawer.selectCorrectDrawerItemForPath', 'Drawer.deselectEverything', 'CALL', 'Deselect when no match',
  evidence='SRC Drawer.java:675 shows if(id == null) deselectEverything()')

# Drawer toggle callbacks (anonymous inner class methods in ActionBarDrawerToggle)
e('FRAMEWORK', 'Drawer$1.onDrawerClosed', 'FRAMEWORK', 'ActionBarDrawerToggle callback when drawer closes',
  evidence='SRC Drawer.java:224 shows onDrawerClosed override in ActionBarDrawerToggle anonymous class')

e('Drawer$1.onDrawerClosed', 'Drawer.onDrawerClosed', 'CALL', 'Delegates to outer class method',
  evidence='SRC Drawer.java:225 shows Drawer.this.onDrawerClosed()')

e('FRAMEWORK', 'Drawer$1.onDrawerOpened', 'FRAMEWORK', 'ActionBarDrawerToggle callback when drawer opens',
  evidence='SRC Drawer.java:228 shows onDrawerOpened override in ActionBarDrawerToggle anonymous class')

# Additional MainActivity calls
e('MainActivity.onCreate', 'MainActivity.initialiseViews', 'CALL', 'Initialize views in onCreate',
  evidence='SRC MainActivity.java:295 shows initialiseViews() call in onCreate')

# Additional edges for lifecycle and framework integration
e('MainActivity.onPostCreate', 'Drawer.syncState', 'LIFECYCLE', 'Sync drawer toggle state after restore',
  evidence='SRC MainActivity.java:1063 shows drawer.syncState() in onPostCreate')

e('MainActivity.onConfigurationChanged', 'Drawer.onConfigurationChanged', 'LIFECYCLE', 'Pass config changes to drawer',
  evidence='SRC MainActivity.java:1070 shows drawer.onConfigurationChanged(newConfig)')

e('MainActivity.onOptionsItemSelected', 'Drawer.onOptionsItemSelected', 'CALL', 'Handle options menu via drawer toggle',
  evidence='SRC MainActivity.java:931 shows if (drawer.onOptionsItemSelected(item)) return true')

e('MainActivity.onCreate', 'Drawer.setDrawerIndicatorEnabled', 'CALL', 'Enable drawer indicator in onCreate',
  evidence='SRC MainActivity.java:348 shows drawer.setDrawerIndicatorEnabled()')

e('MainActivity.onBackPressed', 'Drawer.isLocked', 'CALL', 'Check drawer state on back press',
  evidence='SRC MainActivity.java:704 shows if (!drawer.isLocked() && drawer.isOpen())')

e('MainActivity.onBackPressed', 'Drawer.isOpen', 'CALL', 'Check if drawer is open on back press',
  evidence='SRC MainActivity.java:704 shows drawer.isOpen() check')

e('MainActivity.onBackPressed', 'Drawer.close', 'CALL', 'Close drawer on back press',
  evidence='SRC MainActivity.java:705 shows drawer.close()')

e('MainActivity.onActivityResult', 'Drawer.onActivityResult', 'RESULT', 'Handle activity result for drawer header',
  evidence='SRC MainActivity.java:1309 shows drawer.onActivityResult(requestCode, responseCode, intent)')

e('MainActivity.onSaveInstanceState', 'Drawer.isSomethingSelected', 'CALL', 'Save drawer selection state',
  evidence='SRC MainActivity.java:1076 shows outState.putBoolean(KEY_DRAWER_SELECTED, drawer.isSomethingSelected())')

e('MainActivity.onCreate', 'Drawer.setSomethingSelected', 'CALL', 'Restore drawer selection from saved state',
  evidence='SRC MainActivity.java:322 shows drawer.setSomethingSelected(savedInstanceState.getBoolean(...))')

e('MainActivity.onCreate', 'Drawer.getPhoneStorageCount', 'CALL', 'Get storage count for tab setup',
  evidence='SRC MainActivity.java:447 shows if (drawer.getPhoneStorageCount() > 1)')

e('MainActivity.onCreate', 'Drawer.getFirstPath', 'CALL', 'Get first storage path for tab setup',
  evidence='SRC MainActivity.java:453 shows if (drawer.getFirstPath() != null)')

e('MainActivity.onCreate', 'Drawer.getSecondPath', 'CALL', 'Get second storage path for tab setup',
  evidence='SRC MainActivity.java:448,457 shows drawer.getSecondPath() for tabs')

e('MainActivity.initialiseViews', 'Drawer.setDrawerHeaderBackground', 'CALL', 'Set header background in initialization',
  evidence='SRC MainActivity.java:1445 shows drawer.setDrawerHeaderBackground()')

e('MainActivity.updatePathColor', 'Drawer.setBackgroundColor', 'CALL', 'Update drawer background color',
  evidence='SRC MainActivity.java:1479 shows drawer.setBackgroundColor(colorDrawable.getColor())')

e('MainFragment.onTabChanged', 'Drawer.selectCorrectDrawerItemForPath', 'CALL', 'Select drawer item when tab changes',
  evidence='SRC MainFragment.java:1423 shows getMainActivity().getDrawer().selectCorrectDrawerItemForPath(getPath())')

e('TabFragment.onPageSelected', 'Drawer.selectCorrectDrawerItemForPath', 'CALL', 'Select drawer item on page selection',
  evidence='SRC TabFragment.java:224 shows mainActivity.getDrawer().selectCorrectDrawerItemForPath(...)')

e('MainFragment.actionModeFinish', 'Drawer.lockIfNotOnTablet', 'CALL', 'Lock drawer during action mode',
  evidence='SRC MainFragment.java:509 shows getMainActivity().getDrawer().lockIfNotOnTablet(...)')

e('MainFragment.handleSearchResult', 'Drawer.unlockIfNotOnTablet', 'CALL', 'Unlock drawer after action mode',
  evidence='SRC MainFragment.java:771 shows getMainActivity().getDrawer().unlockIfNotOnTablet()')

# Lambda method edges
e('Drawer.<init>', 'Drawer.lambda$new$0', 'CALL', 'Long click listener lambda for header',
  evidence='SRC Drawer.java:141 shows drawerHeaderView.setOnLongClickListener(v -> ...)')

e('Drawer.<init>', 'Drawer$1.<init>', 'CALL', 'Anonymous ActionBarDrawerToggle created in constructor',
  evidence='SRC Drawer.java:214-232 new ActionBarDrawerToggle(...) { ... } anonymous class')

e('Drawer.setDrawerHeaderBackground', 'Drawer$2.<init>', 'CALL', 'Anonymous ImageListener for header background',
  evidence='SRC Drawer.java:657 shows new ImageLoader.ImageListener() { ... }')

e('Drawer$1.<init>', 'Drawer$1.onDrawerClosed', 'CALL', 'Method defined in anonymous class',
  evidence='SRC Drawer.java:224 onDrawerClosed method definition in Drawer$1')

e('Drawer$1.<init>', 'Drawer$1.onDrawerOpened', 'CALL', 'Method defined in anonymous class',
  evidence='SRC Drawer.java:228 onDrawerOpened method definition in Drawer$1')

e('Drawer$2.<init>', 'Drawer$2.onResponse', 'CALL', 'Method defined in anonymous ImageListener',
  evidence='SRC Drawer.java:659 onResponse method definition in Drawer$2')

e('Drawer$2.<init>', 'Drawer$2.onErrorResponse', 'CALL', 'Method defined in anonymous ImageListener',
  evidence='SRC Drawer.java:665 onErrorResponse method definition in Drawer$2')

# Static initializer
e('JVM', 'Drawer.<clinit>', 'SYSTEM', 'Static initialization when class loads',
  evidence='SRC Drawer.java:1 class declaration, static fields initialized when MainActivity creates Drawer')

# UNREACHABLE methods
UNREACHABLE['Drawer.setNavViewDimension'] = (
  'no_trigger_in_app',
  'Method is commented out in constructor at the only call site',
  'SRC Drawer.java:160-163 shows /* commented out setNavViewDimension call */',
  'SOURCE'
)

