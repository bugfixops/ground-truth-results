# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 86 part (ExpansionHeader tail, custom views, BlankFragment, DetailTorrentActivity head). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b086_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.

e('ExpansionHeader.setExpanded(boolean,boolean)', 'ExpansionHeader.createRotateAnimator', 'CALL', 'Animated expand rotates the arrow', cls='explicit', evidence='SRC ui/customviews/ExpansionHeader.java:97-115; SRC ui/customviews/ExpansionHeader.java:117-124')
e('ExpansionHeader.<init>(Context,AttributeSet)', 'ExpansionHeader.init', 'CALL', 'Header constructor initializes the header view', cls='explicit', evidence='SRC ui/customviews/ExpansionHeader.java:63-67; SRC ui/customviews/ExpansionHeader.java:126-152')
e('ExpansionHeader.<init>(Context,AttributeSet)', 'ExpansionHeader.onRestoreInstanceState', 'CALL', 'Inflated header restores its expanded state', cls='non_standard', via='Framework state-restore dispatch after inflation', evidence='INFERRED framework dispatch; SRC ui/customviews/ExpansionHeader.java:63-67; SRC ui/customviews/ExpansionHeader.java:175-185')
e('ExpansionHeader.<init>(Context,AttributeSet)', 'ExpansionHeader.onSaveInstanceState', 'CALL', 'Inflated header saves its expanded state', cls='non_standard', via='Framework state-save dispatch after inflation', evidence='INFERRED framework dispatch; SRC ui/customviews/ExpansionHeader.java:63-67; SRC ui/customviews/ExpansionHeader.java:164-173')
e('MainActivity.initDrawer', 'ExpansionHeader.setExpanded(boolean)', 'CALL', 'Drawer setup restores the tags group expansion', cls='explicit', evidence='SRC ui/main/MainActivity.java:230-290; SRC ui/customviews/ExpansionHeader.java:82-84')
e('DrawerExpandableAdapter$GroupViewHolder.bind', 'ExpansionHeader.setExpanded(boolean,boolean)', 'CALL', 'Group binding applies the group expand state', cls='explicit', evidence='SRC ui/main/drawer/DrawerExpandableAdapter.java:200-212; SRC ui/customviews/ExpansionHeader.java:97-115')
e('DrawerExpandableAdapter$GroupViewHolder.bind', 'ExpansionHeader.setText(CharSequence)', 'CALL', 'Group binding sets the group header text', cls='explicit', evidence='SRC ui/main/drawer/DrawerExpandableAdapter.java:200-212; SRC ui/customviews/ExpansionHeader.java:87-89')
e('ExpansionHeader.init', 'ExpansionHeader.setTextAppearance', 'CALL', 'Header init applies the text appearance', cls='explicit', evidence='SRC ui/customviews/ExpansionHeader.java:126-152; SRC ui/customviews/ExpansionHeader.java:154-160')
e('MainActivity.initDrawer', 'ExpansionHeader.toggleExpand', 'CALL', 'Drawer header click toggles the tags group', cls='non_standard', via='Framework click-listener dispatch', evidence='INFERRED framework dispatch; SRC ui/main/MainActivity.java:282-284; SRC ui/customviews/ExpansionHeader.java:77-79')
e('CreateTorrentDialog.onCreateDialog', 'FixHintTextInputEditText.<init>(Context,AttributeSet)', 'CALL', 'Create-torrent layout inflation constructs the fix-hint fields', cls='non_standard', via='LayoutInflater 2-arg constructor dispatch', evidence='INFERRED inflater dispatch; SRC ui/createtorrent/CreateTorrentDialog.java:172-192; SRC ui/customviews/FixHintTextInputEditText.java:39-41')
e('FixHintTextInputEditText.<init>(Context,AttributeSet)', 'FixHintTextInputEditText.getAutofillType', 'CALL', 'Inflated fix-hint field answers autofill queries', cls='non_standard', via='Framework autofill dispatch after inflation', evidence='INFERRED framework dispatch; SRC ui/customviews/FixHintTextInputEditText.java:39-41; SRC ui/customviews/FixHintTextInputEditText.java:52-58')
e('MainFragment.onViewCreated', 'RecyclerViewDividerDecoration.<init>(Drawable)', 'CALL', 'Main fragment decorates the torrent list', cls='explicit', evidence='SRC ui/main/MainFragment.java:125-167; SRC ui/customviews/RecyclerViewDividerDecoration.java:39-42')
e('MainFragment.onViewCreated', 'RecyclerViewDividerDecoration.onDrawOver', 'CALL', 'List decoration draws over the torrent list', cls='non_standard', via='RecyclerView ItemDecoration dispatch after addItemDecoration', evidence='INFERRED framework dispatch; SRC ui/main/MainFragment.java:125-167; SRC ui/customviews/RecyclerViewDividerDecoration.java:50-66')
e('SwitchBarPreference.onBindViewHolder', 'SwitchBar.<init>(Context,AttributeSet)', 'CALL', 'Preference view inflation constructs the switch bar', cls='non_standard', via='LayoutInflater 2-arg constructor dispatch for the preference layout', evidence='INFERRED inflater dispatch; SRC ui/settings/customprefs/SwitchBarPreference.java:64-71; SRC ui/customviews/SwitchBar.java:44-49')
e('SwitchBar.<init>(Context,AttributeSet)', 'SwitchBar.init', 'CALL', 'Switch bar constructor initializes the switch', cls='explicit', evidence='SRC ui/customviews/SwitchBar.java:44-49; SRC ui/customviews/SwitchBar.java:58-67')
e('SwitchBarPreference.onBindViewHolder', 'SwitchBar.setChecked', 'CALL', 'Preference binding applies the checked state', cls='explicit', evidence='SRC ui/settings/customprefs/SwitchBarPreference.java:64-71; SRC ui/customviews/SwitchBar.java:69-74')
e('MainFragment.onCreateView', 'ThemedSpeedDialView.<init>(Context,AttributeSet)', 'CALL', 'Main layout inflation constructs the speed-dial button', cls='non_standard', via='LayoutInflater 2-arg constructor dispatch', evidence='INFERRED inflater dispatch; SRC ui/main/MainFragment.java:115-122; SRC ui/customviews/ThemedSpeedDialView.java:40-44')
e('MainFragment.initFabSpeedDial', 'ThemedSpeedDialView.addActionItem', 'CALL', 'Main fragment adds the speed-dial actions', cls='explicit', evidence='SRC ui/main/MainFragment.java:414-451; SRC ui/customviews/ThemedSpeedDialView.java:55-83')
e('FeedFragment.onCreateView', 'ThemedSwipeRefreshLayout.<init>', 'CALL', 'Feed layout inflation constructs the swipe container', cls='non_standard', via='LayoutInflater 2-arg constructor dispatch', evidence='INFERRED inflater dispatch; SRC ui/feeds/FeedFragment.java:95-102; SRC ui/customviews/ThemedSwipeRefreshLayout.java:32-43')
e('BlankFragment.newInstance', 'BlankFragment.<init>', 'CALL', 'Blank fragment factory constructs the fragment', cls='explicit', evidence='SRC ui/detailtorrent/BlankFragment.java:36-43; SRC ui/detailtorrent/BlankFragment.java:33-54')
e('MainActivity.showBlankFragment', 'BlankFragment.newInstance', 'CALL', 'Two-pane main shows the blank fragment', cls='explicit', evidence='SRC ui/main/MainActivity.java:677-685; SRC ui/detailtorrent/BlankFragment.java:36-43')
e('MainActivity.showBlankFragment', 'BlankFragment.onCreateView', 'CALL', 'Blank fragment transaction creates its view', cls='non_standard', via='FragmentManager transaction and lifecycle dispatch', evidence='INFERRED framework dispatch; SRC ui/main/MainActivity.java:677-685; SRC ui/detailtorrent/BlankFragment.java:47-54')
e('DetailTorrentFragment.onViewCreated', 'DetailPagerAdapter.<init>', 'CALL', 'Detail fragment builds its pager adapter', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:156-222; SRC ui/detailtorrent/DetailPagerAdapter.java:47-49')
e('DetailTorrentFragment.onViewCreated', 'DetailPagerAdapter.createFragment', 'CALL', 'Detail pager creates its page fragments', cls='non_standard', via='ViewPager2 dispatch after setAdapter', evidence='INFERRED framework dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:156-222; SRC ui/detailtorrent/DetailPagerAdapter.java:53-71')
e('DetailTorrentFragment.onViewCreated', 'DetailPagerAdapter.getItemCount', 'CALL', 'Detail pager reports its page count', cls='non_standard', via='ViewPager2 dispatch after setAdapter', evidence='INFERRED framework dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:156-222; SRC ui/detailtorrent/DetailPagerAdapter.java:73-75')
e('MainActivity.showDetailTorrent', 'DetailTorrentActivity.<clinit>', 'CALL', 'Detail intent construction loads the activity class', cls='non_standard', via='JVM class-load dispatch on Intent construction', evidence='INFERRED class-load dispatch; SRC ui/main/MainActivity.java:656-672; SRC ui/detailtorrent/DetailTorrentActivity.java:43-46')
e('MainActivity.showDetailTorrent', 'DetailTorrentActivity.<init>', 'CALL', 'Detail activity starts from the torrent list', cls='non_standard', via='Framework activity instantiation on startActivity', evidence='INFERRED framework dispatch; SRC ui/main/MainActivity.java:656-672; SRC ui/detailtorrent/DetailTorrentActivity.java:40-46')
e('DetailTorrentActivity.subscribeTorrentDeleted', 'DetailTorrentActivity.lambda$subscribeTorrentDeleted$0', 'CALL', 'Deleted-torrent subscription checks the shown torrent', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/detailtorrent/DetailTorrentActivity.java:95-105')
e('MainActivity.showDetailTorrent', 'DetailTorrentActivity.onCreate', 'CALL', 'Detail activity starts from the torrent list', cls='non_standard', via='Framework lifecycle dispatch after startActivity', evidence='INFERRED framework dispatch; SRC ui/main/MainActivity.java:656-672; SRC ui/detailtorrent/DetailTorrentActivity.java:53-78')
e('DetailTorrentFragment.finish', 'DetailTorrentActivity.onFragmentFinished', 'CALL', 'Detail fragment finish reports through the host callback', cls='non_standard', via='FragmentCallback interface dispatch', evidence='INFERRED interface dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:827-831; SRC ui/detailtorrent/DetailTorrentActivity.java:108-122')
e('DetailTorrentActivity.onCreate', 'DetailTorrentActivity.onStart', 'CALL', 'Detail activity starts and subscribes deletions', cls='non_standard', via='Framework lifecycle dispatch', evidence='INFERRED framework dispatch; SRC ui/detailtorrent/DetailTorrentActivity.java:53-78; SRC ui/detailtorrent/DetailTorrentActivity.java:88-93')
e('DetailTorrentActivity.onStart', 'DetailTorrentActivity.onStop', 'CALL', 'Detail activity stops and clears its disposables', cls='non_standard', via='Framework lifecycle dispatch', evidence='INFERRED framework dispatch; SRC ui/detailtorrent/DetailTorrentActivity.java:88-93; SRC ui/detailtorrent/DetailTorrentActivity.java:80-86')
e('DetailTorrentActivity.onStart', 'DetailTorrentActivity.subscribeTorrentDeleted', 'CALL', 'Detail activity start subscribes torrent deletions', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentActivity.java:88-93; SRC ui/detailtorrent/DetailTorrentActivity.java:95-105')
e('DetailTorrentActivity.onCreate', 'DetailTorrentFragment.<clinit>', 'CALL', 'Detail layout inflation loads the fragment class', cls='non_standard', via='JVM class-load dispatch on FragmentManager lookup', evidence='INFERRED class-load dispatch; SRC ui/detailtorrent/DetailTorrentActivity.java:53-78; SRC ui/detailtorrent/DetailTorrentFragment.java:92-100')
e('DetailTorrentActivity.onCreate', 'DetailTorrentFragment.<init>', 'CALL', 'Detail layout inflation instantiates the fragment', cls='non_standard', via='FragmentManager instantiation on layout inflation', evidence='INFERRED framework dispatch; SRC ui/detailtorrent/DetailTorrentActivity.java:53-78; SRC ui/detailtorrent/DetailTorrentFragment.java:90-113')
e('DetailTorrentFragment.lambda$subscribeAlertDialog$9', 'DetailTorrentFragment.addTrackers', 'CALL', 'Add-trackers dialog event runs add-trackers', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:297-352; SRC ui/detailtorrent/DetailTorrentFragment.java:689-736')

# Four UNREACHABLE rows in this batch.
UNREACHABLE.update({
    'ExpansionHeader.setText(int)': ('no_trigger_in_app',
        'Only two ExpansionHeader receivers exist in the tree and the sole setText call passes a String (CharSequence overload); init writes textView.setText directly.',
        'SRC ui/customviews/ExpansionHeader.java:92-94',
        'INFERRED'),
    'FixHintTextInputEditText.<init>(Context,AttributeSet,int)': ('no_trigger_in_app',
        'LayoutInflater looks up only the 2-arg ctor; the 2-arg ctor calls super only, never this(...,int); saved 252-file grep found 0 constructions, 0 extends, 0 reflection lookups.',
        'SRC ui/customviews/FixHintTextInputEditText.java:43-49',
        'INFERRED'),
    'SwitchBar.<init>(Context,AttributeSet,int)': ('no_trigger_in_app',
        'LayoutInflater looks up only the 2-arg ctor; the 2-arg ctor calls super only, never this(...,int); saved 252-file grep found 0 constructions, 0 extends, 0 reflection lookups.',
        'SRC ui/customviews/SwitchBar.java:51-56',
        'INFERRED'),
    'ThemedSpeedDialView.<init>(Context,AttributeSet,int)': ('no_trigger_in_app',
        'LayoutInflater looks up only the 2-arg ctor; the 2-arg ctor calls super only, never this(...,int); saved 252-file grep found 0 constructions, 0 extends, 0 reflection lookups.',
        'SRC ui/customviews/ThemedSpeedDialView.java:46-51',
        'INFERRED'),
})

# No auto edge points at this batch's UNREACHABLE overloads: the
# overload-aware auto_calls recompute found zero calls into
# setText(int) or any 3-arg ctor (the one setText hit is the
# CharSequence overload), and no REACHABLE method in this group
# calls them in bytecode, so no SUPPRESS entries apply here.
SUPPRESS.update(set())
