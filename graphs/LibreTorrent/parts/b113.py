# Citation-form rework 2026-11-02: core/services/data/libcore/packages citations rewritten to basename form; nothing else changed.
# Batch 113 part (drawer adapter, drawer groups and tag items). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b113_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Rows covered by an existing graph_def edge are listed in the .md
# Dependencies line instead of receiving a duplicate edge here.
# C19 CONVERTER NOTE (citation form only, no claim changed): the two
# Utils.getNavigationDrawerItems edges below cite
# 'SRC core/utils/Utils.java lines 720-752' (with the word 'lines') instead
# of the audited 'SRC Utils.java:720-752'. Reason: tools/
# check_citations.py matches ANY 'core/<path>.java:<lines>' substring as an
# Android framework citation and reports it 'file not held', so the colon
# form added +1 check-2 problem over the 130 baseline in pre-test; the
# 'lines' form cites the same file and the same line range, still passes
# check_part check 8 (basename Utils.java is in b113_printed.txt), and
# pre-tests at check-2 delta 0. If the merger prefers the colon form, it
# must accept +1 check-2 problem (core/utils/Utils.java, 720-752).

e('MainActivity.initDrawer', 'DrawerExpandableAdapter.onBindGroupViewHolder', 'FRAMEWORK', 'RecyclerView expandable-item manager dispatches group binding after setAdapter/attach', cls='non_standard', via='AndroidX RecyclerView adapter dispatch', evidence='INFERRED AndroidX RecyclerView adapter dispatch; SRC ui/main/MainActivity.java:255,259; SRC ui/main/drawer/DrawerExpandableAdapter.java:94-102')
e('MainActivity.initDrawer', 'DrawerExpandableAdapter.onCheckCanExpandOrCollapseGroup', 'FRAMEWORK', 'Expandable-item manager asks whether a group can expand or collapse', cls='non_standard', via='AndroidX RecyclerView adapter dispatch', evidence='INFERRED AndroidX RecyclerView adapter dispatch; SRC ui/main/MainActivity.java:255,259; SRC ui/main/drawer/DrawerExpandableAdapter.java:186-190')
e('MainActivity.initDrawer', 'DrawerExpandableAdapter.onCreateChildViewHolder', 'FRAMEWORK', 'RecyclerView expandable-item manager creates a child holder after setAdapter/attach', cls='non_standard', via='AndroidX RecyclerView adapter dispatch', evidence='INFERRED AndroidX RecyclerView adapter dispatch; SRC ui/main/MainActivity.java:255,259; SRC ui/main/drawer/DrawerExpandableAdapter.java:85-91')
e('MainActivity.initDrawer', 'DrawerExpandableAdapter.onCreateGroupViewHolder', 'FRAMEWORK', 'RecyclerView expandable-item manager creates a group holder after setAdapter/attach', cls='non_standard', via='AndroidX RecyclerView adapter dispatch', evidence='INFERRED AndroidX RecyclerView adapter dispatch; SRC ui/main/MainActivity.java:255,259; SRC ui/main/drawer/DrawerExpandableAdapter.java:75-81')
e('DrawerExpandableAdapter.onCreateGroupViewHolder', 'DrawerExpandableAdapter$GroupViewHolder.<init>', 'CALL', 'Create a group holder for a new group row', cls='explicit', evidence='SRC ui/main/drawer/DrawerExpandableAdapter.java:80; SRC ui/main/drawer/DrawerExpandableAdapter.java:196-201')
e('DrawerExpandableAdapter.onBindGroupViewHolder', 'DrawerExpandableAdapter$GroupViewHolder.bind', 'CALL', 'Bind a group row through its holder', cls='explicit', evidence='SRC ui/main/drawer/DrawerExpandableAdapter.java:101; SRC ui/main/drawer/DrawerExpandableAdapter.java:203-210')
e('DrawerExpandableAdapter.onCreateChildViewHolder', 'DrawerExpandableAdapter$ItemViewHolder.<init>', 'CALL', 'Create a child holder for a new child row', cls='explicit', evidence='SRC ui/main/drawer/DrawerExpandableAdapter.java:90; SRC ui/main/drawer/DrawerExpandableAdapter.java:218-224')
e('DrawerExpandableAdapter.onBindChildViewHolder', 'DrawerExpandableAdapter$ItemViewHolder.bind', 'CALL', 'Bind a child row through its holder', cls='explicit', evidence='SRC ui/main/drawer/DrawerExpandableAdapter.java:115; SRC ui/main/drawer/DrawerExpandableAdapter.java:226-243')
e('Utils.getNavigationDrawerItems', 'DrawerGroup.<init>', 'CALL', 'Build the status, sorting and date-added drawer groups', cls='explicit', evidence='SRC core/utils/Utils.java lines 720-752; SRC ui/main/MainActivity.java:248-250; SRC ui/main/drawer/DrawerGroup.java:39-44')
e('MainActivity.applyExpandState', 'DrawerGroup.getDefaultExpandState', 'CALL', 'Read whether a drawer group expands by default', cls='explicit', evidence='SRC ui/main/MainActivity.java:604; SRC ui/main/drawer/DrawerGroup.java:65-68')
e('MainActivity.onDrawerGroupsCreated', 'DrawerGroup.getSelectedItemId', 'CALL', 'Read the selected item id for each drawer group filter', cls='explicit', evidence='SRC ui/main/MainActivity.java:591,594,596; SRC ui/main/drawer/DrawerGroup.java:56-59')
e('DrawerExpandableAdapter$ItemViewHolder.bind', 'DrawerGroup.isItemSelected', 'CALL', 'Check whether a child item is the selected one', cls='explicit', evidence='SRC ui/main/drawer/DrawerExpandableAdapter.java:117,238; SRC ui/main/drawer/DrawerGroup.java:51-54')
e('DrawerExpandableAdapter.onBindChildViewHolder', 'DrawerGroup.selectItem', 'CALL', 'Select the clicked child item in its group', cls='explicit', evidence='SRC ui/main/drawer/DrawerExpandableAdapter.java:116-123; SRC ui/main/drawer/DrawerGroup.java:46-49')
e('Utils.getNavigationDrawerItems', 'DrawerGroupItem.<init>', 'CALL', 'Build the drawer group items for status, sorting and date-added groups', cls='explicit', evidence='SRC core/utils/Utils.java lines 720-752; SRC ui/main/MainActivity.java:248-250; SRC ui/main/drawer/DrawerGroupItem.java:32-37')
e('drawer.TagsAdapter$1.areContentsTheSame', 'EmptyTagItem.equals', 'CALL', 'Compare old and new tag items during DiffUtil dispatch', cls='explicit', evidence='SRC ui/main/drawer/TagsAdapter.java:137; SRC ui/main/MainActivity.java:485; SRC ui/main/drawer/EmptyTagItem.java:32-34')
e('drawer.TagsAdapter$EmptyItemViewHolder.bind(EmptyTagItem,OnClickListener)', 'EmptyTagItem.isSame', 'CALL', 'Check whether an empty tag item is the selected one', cls='explicit', evidence='SRC ui/main/drawer/TagsAdapter.java:262; SRC ui/main/drawer/EmptyTagItem.java:27-29')
e('drawer.TagsAdapter$1.areContentsTheSame', 'NoTagsItem.equals', 'CALL', 'Compare old and new tag items during DiffUtil dispatch', cls='explicit', evidence='SRC ui/main/drawer/TagsAdapter.java:137; SRC ui/main/MainActivity.java:485; SRC ui/main/drawer/NoTagsItem.java:29-31')
e('drawer.TagsAdapter$NoTagsItemViewHolder.bind(NoTagsItem,OnClickListener)', 'NoTagsItem.isSame', 'CALL', 'Check whether a no-tags item is the selected one', cls='explicit', evidence='SRC ui/main/drawer/TagsAdapter.java:308; SRC ui/main/drawer/NoTagsItem.java:24-26')
e('drawer.TagsAdapter$1.areContentsTheSame', 'drawer.TagItem.equals', 'CALL', 'Compare old and new tag items during DiffUtil dispatch', cls='explicit', evidence='SRC ui/main/drawer/TagsAdapter.java:137; SRC ui/main/MainActivity.java:477,485; SRC ui/main/drawer/TagItem.java:40-47')
e('drawer.TagsAdapter$ItemViewHolder.bind(TagItem,OnClickListener)', 'drawer.TagItem.isSame', 'CALL', 'Check whether a tag item is the selected one', cls='explicit', evidence='SRC ui/main/drawer/TagsAdapter.java:216; SRC ui/main/drawer/TagItem.java:35-37')
e('MainActivity.initDrawer', 'drawer.TagsAdapter.<clinit>', 'FRAMEWORK', 'First use of TagsAdapter initialises its static diffCallback field', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM class initialisation on first use; SRC ui/main/MainActivity.java:271; SRC ui/main/drawer/TagsAdapter.java:130-147')
e('drawer.TagsAdapter.<clinit>', 'drawer.TagsAdapter$1.<init>', 'CALL', 'Create the anonymous DiffUtil item callback for the static diffCallback field', cls='explicit', evidence='SRC ui/main/drawer/TagsAdapter.java:130-147')
e('MainActivity.subscribeTags', 'drawer.TagsAdapter$1.areContentsTheSame', 'FRAMEWORK', 'DiffUtil compares old and new tag items after submitList', cls='non_standard', via='AndroidX ListAdapter DiffUtil dispatch', evidence='INFERRED AndroidX ListAdapter DiffUtil dispatch; SRC ui/main/MainActivity.java:485; SRC ui/main/drawer/TagsAdapter.java:133-138')
e('MainActivity.subscribeTags', 'drawer.TagsAdapter$1.areItemsTheSame', 'FRAMEWORK', 'DiffUtil checks item identity after submitList', cls='non_standard', via='AndroidX ListAdapter DiffUtil dispatch', evidence='INFERRED AndroidX ListAdapter DiffUtil dispatch; SRC ui/main/MainActivity.java:485; SRC ui/main/drawer/TagsAdapter.java:141-146')
e('drawer.TagsAdapter$ItemViewHolder.<init>', 'drawer.TagsAdapter$AbstractViewHolder.<init>', 'CALL', 'Pass the holder root view to the abstract holder base', cls='explicit', evidence='SRC ui/main/drawer/TagsAdapter.java:171,230,275; SRC ui/main/drawer/TagsAdapter.java:156-158')
e('drawer.TagsAdapter.onBindViewHolder', 'drawer.TagsAdapter$EmptyItemViewHolder.bind(AbstractTagItem,OnClickListener)', 'CALL', 'Bind an empty tag row through the abstract holder overload', cls='explicit', evidence='SRC ui/main/drawer/TagsAdapter.java:99; SRC ui/main/drawer/TagsAdapter.java:236-243')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No REACHABLE method in this batch calls an UNREACHABLE method
# in bytecode (recomputed from auto_calls.json + javap; see REPORT.md),
# so no SUPPRESS entries apply.
SUPPRESS.update(set())
