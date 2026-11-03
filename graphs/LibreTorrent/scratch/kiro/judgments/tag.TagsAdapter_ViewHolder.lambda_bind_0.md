# Judgment: tag.TagsAdapter$ViewHolder.lambda$bind$0

Route print: graphs/LibreTorrent/scratch/route_print/tag.TagsAdapter_ViewHolder.lambda_bind_0.txt (26 steps). Judged by Kiro (lead), 2026-11-03, by Appendix D.

Steps 1-16: same nodes and edges as first-draw rows 1 and 16 (see SelectTagDialog.onTagClicked judgment); steps 17-26 identical to steps 17-26 of SelectTagDialog.onTagClicked. Graded TRUE on that judged prefix.

| step | edge | from -> to | action true? | condition true? | grade | printed file:lines / note |
|---|---|---|---|---|---|---|
| 1 | Ef4711e98 | S_ENTRY -> MainActivity.onCreate | yes | yes | TRUE | judged prefix; SRC AndroidManifest.xml:43-59; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215 |
| 2 | Ed8e7f5f9 | MainActivity.onCreate -> MainFragment.<init> | yes | yes | TRUE | judged prefix; SRC ui/main/MainActivity.java:182-185; res/values/layouts.xml:1-4; notouch/layouts.xml:1-4; res/layout/activity_main_drawer.xml:22-28; res/layout/activity_main_two_pane.xml:26-32; ui/main/MainFragment |
| 3 | Ee453d286 | MainFragment.<init> -> MainFragment.onAttach | yes | yes | TRUE | judged prefix; SRC ui/main/MainFragment.java:85-87,223-230 |
| 4 | E28c54333 | MainFragment.onAttach -> MainFragment.onCreateView | yes | yes | TRUE | judged prefix; SRC ui/main/MainFragment.java:223-230,113-122 |
| 5 | E2e46bfdf | MainFragment.onCreateView -> MainFragment.onViewCreated | yes | yes | TRUE | judged prefix; SRC ui/main/MainFragment.java:115-127 |
| 6 | E3b5adb16 | MainFragment.onViewCreated -> TorrentListAdapter.onBindViewHolder | yes | yes | TRUE | judged prefix; SRC ui/main/MainFragment.java:136-155; ui/main/TorrentListAdapter.java:74-104 |
| 7 | E9d948322 | TorrentListAdapter.onBindViewHolder -> TorrentListAdapter$ViewHolder.bind | yes | yes | TRUE | judged prefix; SRC ui/main/TorrentListAdapter.java:88-104,171-202 |
| 8 | Ef521ec44 | TorrentListAdapter$ViewHolder.bind -> TorrentListAdapter$ViewHolder.lambda$bind$0 | yes | yes | TRUE | judged prefix; SRC ui/main/TorrentListAdapter.java:189-196; FW-SRC core/java/android/view/View.java:6289-6305 |
| 9 | Efe87970e | TorrentListAdapter$ViewHolder.lambda$bind$0 -> MainFragment.onItemClicked | yes | yes | TRUE | judged prefix; SRC ui/main/TorrentListAdapter.java:189-196; ui/main/MainFragment.java:378-384 |
| 10 | Ee6073c26 | MainFragment.onItemClicked -> MsgMainViewModel.torrentDetailsOpened | yes | yes | TRUE | judged prefix; SRC ui/main/MainFragment.java:378-384 |
| 11 | E9fb4a1ea | MsgMainViewModel.torrentDetailsOpened -> MainActivity.showDetailTorrent | yes | yes | TRUE | judged prefix; SRC ui/main/MsgMainViewModel.java:30-40; ui/main/MainActivity.java:437-440; ui/main/MainFragment.java:378-384 |
| 12 | E883c34be | MainActivity.showDetailTorrent -> DetailTorrentActivity.onCreate | yes | yes | TRUE | judged prefix; SRC ui/main/MainActivity.java:669-673; AndroidManifest.xml:139; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215 |
| 13 | E87241f3c | DetailTorrentActivity.onCreate -> DetailTorrentFragment.onAttach | yes | yes | TRUE | judged prefix; SRC ui/detailtorrent/DetailTorrentActivity.java:53-78; SRC ui/detailtorrent/DetailTorrentFragment.java:139-145 |
| 14 | E2c864273 | DetailTorrentFragment.onAttach -> DetailTorrentFragment.onCreateView | yes | yes | TRUE | judged prefix; SRC ui/detailtorrent/DetailTorrentFragment.java:147-153 |
| 15 | Efd617da3 | DetailTorrentFragment.onCreateView -> DetailTorrentFragment.onViewCreated | yes | yes | TRUE | judged prefix; SRC ui/detailtorrent/DetailTorrentFragment.java:155-221 |
| 16 | E00bf2e7e | DetailTorrentFragment.onViewCreated -> DetailPagerAdapter.createFragment | yes | yes | TRUE | judged prefix; SRC ui/detailtorrent/DetailTorrentFragment.java:185-212; ui/detailtorrent/DetailPagerAdapter.java:48-73 |
| 17 | Ebbfdf083 | DetailPagerAdapter.createFragment -> DetailTorrentInfoFragment.onCreateView | yes | yes | TRUE | ViewPager2 creates page 0 = INFO first (DetailPagerAdapter.java:53-56) |
| 18 | E490f604c | DetailTorrentInfoFragment.onCreateView -> DetailTorrentInfoFragment$1.onAddTagClick | yes | yes | TRUE | tags list always holds the add-tag button (TorrentTagsList.java:35-37,51); listener set at DetailTorrentInfoFragment.java:112. Prints: judge_tags.txt |
| 19 | Ec2241c4e | DetailTorrentInfoFragment$1.onAddTagClick -> DetailTorrentInfoFragment$1.lambda$onAddTagClick$2 | yes | yes | TRUE | getTags() is a Single (DetailTorrentViewModel.java:143-145) that emits; flatMap/toList/subscribe at DetailTorrentInfoFragment.java:150-164 |
| 20 | E712eea39 | DetailTorrentInfoFragment$1.lambda$onAddTagClick$2 -> SelectTagActivity.onCreate | yes | yes | TRUE | selectTag.launch(i) with SelectTagActivity intent (DetailTorrentInfoFragment.java:158-163; AndroidManifest.xml:248-250) |
| 21 | E391e1d9b | SelectTagActivity.onCreate -> SelectTagDialog.newInstance | yes | yes | TRUE | first create: findFragmentByTag null (SelectTagActivity.java:47-53) |
| 22 | E91aec3ee | SelectTagDialog.newInstance -> SelectTagDialog.onAttach | yes | yes | TRUE | dialog.show commits the DialogFragment (SelectTagActivity.java:52; SelectTagDialog.java:73-80) |
| 23 | E585f6046 | SelectTagDialog.onAttach -> SelectTagDialog.onCreateDialog | yes | yes | TRUE | DialogFragment builds its dialog (SelectTagDialog.java:113-136) |
| 24 | E60d22865 | SelectTagDialog.onCreateDialog -> tag.TagsAdapter.onBindViewHolder | yes | no earlier step | UNCLEAR | the RecyclerView binds a row only if subscribeTags emits at least one tag not already on the torrent (SelectTagDialog.java:165-175; SelectTagViewModel.java:58-64). A fresh install has no tags and no earlier step of this route creates one |
| 25 | E76cd6c6f | tag.TagsAdapter.onBindViewHolder -> tag.TagsAdapter$ViewHolder.bind | yes | inherits 24 | UNCLEAR | TagsAdapter.java:57-63 |
| 26 | E71fb1ae3 | tag.TagsAdapter$ViewHolder.bind -> tag.TagsAdapter$ViewHolder.lambda$bind$0 | yes | STATE adapter.getItemCount() > 0 not produced on route | UNCLEAR | TagsAdapter.java:98-108 |

**Route verdict: UNCLEAR.** Step 24, edge E60d22865: needs an existing tag that no earlier step creates (STATE data, gate at step 26). No step is FALSE.
