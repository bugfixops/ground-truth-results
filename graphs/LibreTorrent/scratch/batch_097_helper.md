# LibreTorrent batch 97 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, batch 97 only. Exact count: 40.

Summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. FeedItemsAdapter source connects list binding to click callbacks, and FeedItemsFragment subscribes to feed data and passes lists to the adapter. This bounded review does not establish the complete host activity/fragment route and all guards for every member, so all remain OPEN.

| Plan row | JVM method | Descriptor | Status | Reason |
|---:|---|---|---|---|
| 1 | `FeedItemsAdapter.getItemPosition` | `(Lorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsListItem;)I` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 2 | `FeedItemsAdapter.onBindViewHolder` | `(Lorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsAdapter$ViewHolder;I)V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 3 | `FeedItemsAdapter.onCreateViewHolder` | `(Landroid/view/ViewGroup;I)Lorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsAdapter$ViewHolder;` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 4 | `FeedItemsAdapter.submitList` | `(Ljava/util/List;)V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 5 | `FeedItemsAdapter$1.<init>` | `()V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 6 | `FeedItemsAdapter$1.areContentsTheSame` | `(Lorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsListItem;Lorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsListItem;)Z` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 7 | `FeedItemsAdapter$1.areItemsTheSame` | `(Lorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsListItem;Lorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsListItem;)Z` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 8 | `FeedItemsAdapter$ViewHolder.<init>` | `(Lorg/proninyaroslav/libretorrent/databinding/ItemFeedItemsListBinding;)V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 9 | `FeedItemsAdapter$ViewHolder.bind` | `(Lorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsListItem;Lorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsAdapter$ClickListener;)V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 10 | `FeedItemsAdapter$ViewHolder.lambda$bind$0` | `(Lorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsAdapter$ClickListener;Lorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsListItem;Landroid/view/MenuItem;)Z` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 11 | `FeedItemsAdapter$ViewHolder.lambda$bind$1` | `(Lorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsListItem;Lorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsAdapter$ClickListener;Landroid/view/View;)V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 12 | `FeedItemsAdapter$ViewHolder.lambda$bind$2` | `(Lorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsAdapter$ClickListener;Lorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsListItem;Landroid/view/View;)V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 13 | `FeedItemsFragment.<clinit>` | `()V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 14 | `FeedItemsFragment.<init>` | `()V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 15 | `FeedItemsFragment.finish` | `(Landroid/content/Intent;Lorg/proninyaroslav/libretorrent/ui/FragmentCallback$ResultCode;)V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 16 | `FeedItemsFragment.getAllFeedItemsSingle` | `()V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 17 | `FeedItemsFragment.getFeedId` | `()J` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 18 | `FeedItemsFragment.lambda$getAllFeedItemsSingle$4` | `(Ljava/util/List;)Lio/reactivex/SingleSource;` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 19 | `FeedItemsFragment.lambda$getAllFeedItemsSingle$5` | `(Ljava/lang/Throwable;)V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 20 | `FeedItemsFragment.lambda$observeFeedItems$2` | `(Ljava/util/List;)Lio/reactivex/SingleSource;` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 21 | `FeedItemsFragment.lambda$observeFeedItems$3` | `(Ljava/lang/Throwable;)V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 22 | `FeedItemsFragment.lambda$onViewCreated$0` | `(Landroid/view/View;)V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 23 | `FeedItemsFragment.lambda$onViewCreated$1` | `()V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 24 | `FeedItemsFragment.newInstance` | `(J)Lorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsFragment;` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 25 | `FeedItemsFragment.observeFeedItems` | `()Lio/reactivex/disposables/Disposable;` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 26 | `FeedItemsFragment.onAttach` | `(Landroid/content/Context;)V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 27 | `FeedItemsFragment.onBackPressed` | `()V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 28 | `FeedItemsFragment.onCreateOptionsMenu` | `(Landroid/view/Menu;Landroid/view/MenuInflater;)V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 29 | `FeedItemsFragment.onCreateView` | `(Landroid/view/LayoutInflater;Landroid/view/ViewGroup;Landroid/os/Bundle;)Landroid/view/View;` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 30 | `FeedItemsFragment.onItemClicked` | `(Lorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsListItem;)V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 31 | `FeedItemsFragment.onItemMenuClicked` | `(ILorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsListItem;)V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 32 | `FeedItemsFragment.onOptionsItemSelected` | `(Landroid/view/MenuItem;)Z` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 33 | `FeedItemsFragment.onResume` | `()V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 34 | `FeedItemsFragment.onSaveInstanceState` | `(Landroid/os/Bundle;)V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 35 | `FeedItemsFragment.onStart` | `()V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 36 | `FeedItemsFragment.onStop` | `()V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 37 | `FeedItemsFragment.onViewCreated` | `(Landroid/view/View;Landroid/os/Bundle;)V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 38 | `FeedItemsFragment.onViewStateRestored` | `(Landroid/os/Bundle;)V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 39 | `FeedItemsFragment.openArticle` | `(Lorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsListItem;)V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |
| 40 | `FeedItemsFragment.openDownloadUrl` | `(Lorg/proninyaroslav/libretorrent/ui/feeditems/FeedItemsListItem;)V` | OPEN | Adapter/fragment source shows local list and click callbacks; complete route from app entry was not audited for every target. |

## Evidence
- `FeedItemsAdapter.java:48-166`: adapter creation/binding, list updates, diff callbacks, item click/menu listeners.
- `FeedItemsFragment.java:80-218`: factory, lifecycle, creation and list subscriptions; lines 246-280 handle clicked/menu items and URL/article routes.
- These local calls indicate candidate chains but are not complete entry-route verification.

