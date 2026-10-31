# batch 025 (label_025): com.money.manager.ex.common.BaseExpandableListFragment (abstract; 26 methods: the class, its anonymous listeners $1 and $2); rows and printed lines: graphs/MMEX/parts/label_025.md.
# The only subclass is CategoryListFragment (CategoryListFragment.java:72-73). The list is shown on page S_CATEGORY_LIST, defined at graph_def.py:1214 and only reused here. Its ENTERS edge is written by batches 028, 029, 030 and 080, so no ENTERS edge is written here.
# CALL edges come from auto_calls.json (the super calls of CategoryListFragment, the calls inside this class, and the receiver-variant records "...@CategoryListFragment"), so none are written here. The edges that cannot run are cut with sup below.
# androidx Fragment, SearchView and the options-menu dispatch are not in fw_src: those claims are INFERRED (library source not read). grep evidence: graphs/MMEX/parts/label_025.grep.txt.

# ---- fragment lifecycle (androidx Fragment; library source not read: INFERRED). CategoryListFragment overrides none of onCreate, onCreateView, onViewCreated, onStart, onCreateOptionsMenu or onOptionsItemSelected (grep of CategoryListFragment.java), so the framework calls these inherited bodies on a CategoryListFragment instance.

e('CategoryListFragment.<init>', 'BaseExpandableListFragment.onCreate', 'LIFECYCLE',
  'the framework creates the fragment (CategoryListActivity creates it at line 43) and calls onCreate; CategoryListFragment does not override onCreate, so the inherited body runs',
  evidence='SRC common/CategoryListFragment.java:72-73 (class declaration, no onCreate); SRC common/CategoryListActivity.java:43; SRC common/BaseExpandableListFragment.java:61-70; INFERRED androidx Fragment lifecycle (library not read)')

e('ExpandableListFragment.onCreateView', 'BaseExpandableListFragment.onViewCreated', 'LIFECYCLE',
  'the framework calls onViewCreated after the view is created by the inherited onCreateView (ExpandableListFragment inflates expandable_list_fragment)',
  evidence='SRC common/ExpandableListFragment.java:99 (onCreateView inflates the layout), 133-135; SRC common/BaseExpandableListFragment.java:224-236; INFERRED androidx Fragment lifecycle (library not read)')

e('CategoryListFragment.onActivityCreated', 'BaseExpandableListFragment.onStart', 'LIFECYCLE',
  'the framework calls onStart after onActivityCreated',
  evidence='SRC common/CategoryListFragment.java:97-98; SRC common/BaseExpandableListFragment.java:95-111; INFERRED androidx Fragment lifecycle (library not read)')

e('CategoryListFragment.onActivityCreated', 'BaseExpandableListFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'CategoryListFragment.onActivityCreated calls setHasOptionsMenu(true) (line 113); the activity then builds its options menu and the fragment adds its own items in onCreateOptionsMenu',
  evidence='SRC common/CategoryListFragment.java:113; SRC common/BaseExpandableListFragment.java:120-155; INFERRED androidx FragmentManager dispatches onCreateOptionsMenu to fragments that have an options menu (library not read)')

# ---- user actions on the category list (page S_CATEGORY_LIST). The items of the fragment's options menu: menu_query_mode (search, line 123) and the Up arrow (android.R.id.home, line 160).

gui('S_CATEGORY_LIST', 'BaseExpandableListFragment.onOptionsItemSelected', 'Tap the Up arrow in the action bar',
  evidence='SRC common/BaseExpandableListFragment.java:158-164 (home: setResultAndFinish, unless hosted by MainActivity); SRC common/CategoryListFragment.java:113; INFERRED androidx FragmentManager dispatches the selected item to the fragment (library not read)')

gui('S_CATEGORY_LIST', 'BaseExpandableListFragment$1.onQueryTextChange', 'Type in the search box',
  evidence='SRC common/BaseExpandableListFragment.java:129-143 (SearchView created and listener set at 131); INFERRED androidx SearchView calls the listener on each text change (SearchView not in fw_src)')

gui('S_CATEGORY_LIST', 'BaseExpandableListFragment$1.onQueryTextSubmit', 'Submit the search text (search key on the keyboard)',
  evidence='SRC common/BaseExpandableListFragment.java:131-135; INFERRED androidx SearchView calls onQueryTextSubmit on submit (SearchView not in fw_src)')

gui('S_CATEGORY_LIST', 'BaseExpandableListFragment$2.onClick', 'Tap the + button (floating action button) on the category list',
  evidence='SRC common/BaseExpandableListFragment.java:224-232 (fab found by R.id.fab at 225, listener at 227-232); SRC res/layout/expandable_list_fragment.xml:66-67 (@+id/fab); SRC common/CategoryListFragment.java:140-141 (fab made visible and attached); INFERRED the view dispatches the click to the listener (View not read)')

# ---- auto edges that cannot run

# menu_query_mode on API 27: the branch at line 167 (SDK_INT < HONEYCOMB) is false, so onMenuItemSearchClick is never called from here; the plain edge (line 168) and its receiver variant are both cut
sup(('BaseExpandableListFragment.onOptionsItemSelected', 'BaseExpandableListFragment.onMenuItemSearchClick'),  # line 168
    ('BaseExpandableListFragment.onOptionsItemSelected@CategoryListFragment', 'BaseExpandableListFragment.onMenuItemSearchClick@CategoryListFragment'))  # the receiver variant of the same call (line 168)

# CategoryListFragment.onQueryTextChange (line 230) overrides the base method and does not call super, so the base body never runs; the receiver edge to the override (auto record, line 210) stays
sup(('BaseExpandableListFragment.onPreQueryTextChange', 'BaseExpandableListFragment.onQueryTextChange'))  # line 210

# CategoryListFragment.setResult (line 313) overrides the base method and does not call super; the receiver edge to the override (setResultAndFinish@CategoryListFragment -> CategoryListFragment.setResult, line 262) stays
sup(('BaseExpandableListFragment.setResultAndFinish', 'BaseExpandableListFragment.setResult'))  # line 262

# CategoryListFragment.onFloatingActionButtonClickListener (line 367) overrides the base method and does not call super; the cha edge to the override (auto record, line 230) stays
sup(('BaseExpandableListFragment$2.onClick', 'BaseExpandableListFragment.onFloatingActionButtonClickListener'))  # line 230

# ---- UNREACHABLE (grep output: graphs/MMEX/parts/label_025.grep.txt)

UNREACHABLE['BaseExpandableListFragment.onMenuItemSearchClick'] = (
  'closed_by_api_level',
  'protected method called only from the menu_query_mode case of onOptionsItemSelected, under if (Build.VERSION.SDK_INT < Build.VERSION_CODES.HONEYCOMB) (lines 166-168). The standard configuration is API 27 (handoff/SCHEMA_V2.md:38), so the condition is false and the call never runs. The HONEYCOMB constant is not printed from fw_src (Build.java is not in fw_src); its value (11) is INFERRED from the public Android API levels. The name occurs only at its declaration (line 175) and at line 168 (label_025.grep.txt, section A). Both auto edges into it (line 168, plain and receiver variant) are cut by sup',
  'SRC common/BaseExpandableListFragment.java:158-173, 175; handoff/SCHEMA_V2.md:38; grep label_025.grep.txt sections A, G',
  'INFERRED')

UNREACHABLE['BaseExpandableListFragment.onFloatingActionButtonClickListener'] = (
  'no_trigger_in_app',
  'public method with an empty body (lines 293-294). Its only subclass, CategoryListFragment, overrides it (lines 367-369) without calling super, so every call on a CategoryListFragment receiver runs the override and this body never runs. The FAB listener (BaseExpandableListFragment$2.onClick, line 230) reaches the override through the cha edge, which stays; the exact edge to this body is cut by sup. The name occurs in this file at lines 230 and 293 only (label_025.grep.txt, section B)',
  'SRC common/BaseExpandableListFragment.java:227-231, 293-294; SRC common/CategoryListFragment.java:367-369; grep label_025.grep.txt sections B, G',
  'SOURCE')

UNREACHABLE['BaseExpandableListFragment.onQueryTextChange'] = (
  'no_trigger_in_app',
  'protected method whose base body returns true (lines 213-215). Its only subclass, CategoryListFragment, overrides it (lines 230-237) without calling super. The call in onPreQueryTextChange (line 210) runs on a CategoryListFragment receiver, so it dispatches to the override. The plain edge to this body (line 210) is cut by sup; the receiver edge to the override stays. In this file the name also appears in the SearchView listener method at line 138, which is a different method (label_025.grep.txt, section D)',
  'SRC common/BaseExpandableListFragment.java:206-215; SRC common/CategoryListFragment.java:230-237; grep label_025.grep.txt sections D, G',
  'SOURCE')

UNREACHABLE['BaseExpandableListFragment.setResult'] = (
  'no_trigger_in_app',
  'protected method with an empty body (lines 257-258). Its only caller in this class is setResultAndFinish (line 262), which runs on a CategoryListFragment receiver, and the only subclass CategoryListFragment overrides setResult (line 313) without calling super. So the override runs and this body never does. The plain edge from setResultAndFinish to this body (line 262) is cut by sup; the receiver edge to the override stays. The other setResult() declarations in the source root belong to BaseListFragment, PayeeListFragment, AccountListFragment and CurrencyListFragment, which are not subclasses of this class (label_025.grep.txt, sections C, C2, E)',
  'SRC common/BaseExpandableListFragment.java:257-265; SRC common/CategoryListFragment.java:313; grep label_025.grep.txt sections C, C2, E, G',
  'SOURCE')
