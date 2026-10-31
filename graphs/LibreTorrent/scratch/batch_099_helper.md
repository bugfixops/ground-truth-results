# LibreTorrent batch 99 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, batch 99 only. Exact count: 40.

Summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. This batch covers FeedActivity and FeedChannelListAdapter/FeedChannelItem. Source shows app menu/fragment navigation and RecyclerView/selection helpers, but complete route proof and external library dispatch were not audited for every target. Leave all OPEN.

| Plan row | JVM method | Descriptor | Status | Reason |
|---:|---|---|---|---|
| 1 | `FeedActivity.onCreateOptionsMenu` | `(Landroid/view/Menu;)Z` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 2 | `FeedActivity.onFragmentFinished` | `(Landroidx/fragment/app/Fragment;Landroid/content/Intent;Lorg/proninyaroslav/libretorrent/ui/FragmentCallback$ResultCode;)V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 3 | `FeedActivity.onOptionsItemSelected` | `(Landroid/view/MenuItem;)Z` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 4 | `FeedActivity.onStart` | `()V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 5 | `FeedActivity.onStop` | `()V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 6 | `FeedActivity.restoreFeedsBackup` | `(Landroid/net/Uri;)V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 7 | `FeedActivity.restoreFeedsBackupErrorDialog` | `(Ljava/lang/Throwable;)V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 8 | `FeedActivity.restoreFeedsChooseDialog` | `()V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 9 | `FeedActivity.sendErrorReport` | `(Landroid/app/Dialog;)V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 10 | `FeedActivity.showBlankFragment` | `()V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 11 | `FeedActivity.showFeedItems` | `(J)V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 12 | `FeedActivity.subscribeAlertDialog` | `()V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 13 | `FeedActivity.subscribeMsgViewModel` | `()V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 14 | `FeedChannelItem.<init>` | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedChannel;)V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 15 | `FeedChannelItem.compareTo` | `(Lorg/proninyaroslav/libretorrent/ui/feeds/FeedChannelItem;)I` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 16 | `FeedChannelItem.equals` | `(Ljava/lang/Object;)Z` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 17 | `FeedChannelItem.equalsContent` | `(Ljava/lang/Object;)Z` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 18 | `FeedChannelItem.hashCode` | `()I` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 19 | `FeedChannelListAdapter.<clinit>` | `()V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 20 | `FeedChannelListAdapter.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/feeds/FeedChannelListAdapter$ClickListener;)V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 21 | `FeedChannelListAdapter.getItemKey` | `(I)Lorg/proninyaroslav/libretorrent/ui/feeds/FeedChannelItem;` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 22 | `FeedChannelListAdapter.getItemPosition` | `(Lorg/proninyaroslav/libretorrent/ui/feeds/FeedChannelItem;)I` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 23 | `FeedChannelListAdapter.getOpenedItem` | `()Lorg/proninyaroslav/libretorrent/ui/feeds/FeedChannelItem;` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 24 | `FeedChannelListAdapter.markAsOpen` | `(Lorg/proninyaroslav/libretorrent/ui/feeds/FeedChannelItem;)V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 25 | `FeedChannelListAdapter.onBindViewHolder` | `(Lorg/proninyaroslav/libretorrent/ui/feeds/FeedChannelListAdapter$ViewHolder;I)V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 26 | `FeedChannelListAdapter.onCreateViewHolder` | `(Landroid/view/ViewGroup;I)Lorg/proninyaroslav/libretorrent/ui/feeds/FeedChannelListAdapter$ViewHolder;` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 27 | `FeedChannelListAdapter.setSelectionTracker` | `(Landroidx/recyclerview/selection/SelectionTracker;)V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 28 | `FeedChannelListAdapter.submitList` | `(Ljava/util/List;)V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 29 | `FeedChannelListAdapter$1.<init>` | `()V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 30 | `FeedChannelListAdapter$1.areContentsTheSame` | `(Lorg/proninyaroslav/libretorrent/ui/feeds/FeedChannelItem;Lorg/proninyaroslav/libretorrent/ui/feeds/FeedChannelItem;)Z` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 31 | `FeedChannelListAdapter$1.areItemsTheSame` | `(Lorg/proninyaroslav/libretorrent/ui/feeds/FeedChannelItem;Lorg/proninyaroslav/libretorrent/ui/feeds/FeedChannelItem;)Z` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 32 | `FeedChannelListAdapter$ItemDetails.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/feeds/FeedChannelItem;I)V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 33 | `FeedChannelListAdapter$ItemDetails.getPosition` | `()I` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 34 | `FeedChannelListAdapter$ItemDetails.getSelectionKey` | `()Lorg/proninyaroslav/libretorrent/ui/feeds/FeedChannelItem;` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 35 | `FeedChannelListAdapter$ItemLookup.<init>` | `(Landroidx/recyclerview/widget/RecyclerView;)V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 36 | `FeedChannelListAdapter$ItemLookup.getItemDetails` | `(Landroid/view/MotionEvent;)Landroidx/recyclerview/selection/ItemDetailsLookup$ItemDetails;` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 37 | `FeedChannelListAdapter$KeyProvider.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/Selectable;)V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 38 | `FeedChannelListAdapter$KeyProvider.getKey` | `(I)Lorg/proninyaroslav/libretorrent/ui/feeds/FeedChannelItem;` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 39 | `FeedChannelListAdapter$KeyProvider.getPosition` | `(Lorg/proninyaroslav/libretorrent/ui/feeds/FeedChannelItem;)I` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |
| 40 | `FeedChannelListAdapter$ViewHolder.<init>` | `(Lorg/proninyaroslav/libretorrent/databinding/ItemFeedChannelListBinding;)V` | OPEN | Activity/list adapter source shows local caller links; full route and AndroidX selection dispatch were not verified for all members. |

## Evidence
- `FeedActivity.java:111-203`: blank/feed-items navigation and subscriptions; menu callbacks and restore flows around 239-406.
- `FeedChannelItem.java:28-77`: item equality/hash/compare behavior.
- `FeedChannelListAdapter.java:55-169`: adapter, list and key helpers; nested SelectionTracker support through lines 274-341.
- AndroidX RecyclerView and Selection dispatch are not proven from app source in this bounded review.

