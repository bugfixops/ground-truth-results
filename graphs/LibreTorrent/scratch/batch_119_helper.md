# LibreTorrent batch 119 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, batch 119 only. Exact count: 40.

Summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. SelectTagDialog has lifecycle and tag-selection handlers; SelectTagViewModel filters/observes tags; TagsAdapter and TorrentTagsList have local item/click construction code. This bounded review did not verify each route from its host fragment and AndroidX dispatch, so all members remain OPEN.

| Plan row | JVM method | Descriptor | Status | Reason |
|---:|---|---|---|---|
| 1 | `SelectTagDialog.<init>` | `()V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 2 | `SelectTagDialog.finish` | `(Landroid/content/Intent;Lorg/proninyaroslav/libretorrent/ui/FragmentCallback$ResultCode;)V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 3 | `SelectTagDialog.initAlertDialog` | `(Landroid/view/View;)V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 4 | `SelectTagDialog.initLayoutView` | `()V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 5 | `SelectTagDialog.lambda$initAlertDialog$1` | `(Landroid/view/View;)V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 6 | `SelectTagDialog.lambda$initAlertDialog$2` | `(Landroid/view/View;)V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 7 | `SelectTagDialog.lambda$initAlertDialog$3` | `(Landroid/content/DialogInterface;)V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 8 | `SelectTagDialog.lambda$onResume$0` | `(Landroid/content/DialogInterface;ILandroid/view/KeyEvent;)Z` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 9 | `SelectTagDialog.lambda$subscribeTags$4` | `(Ljava/util/List;)Lio/reactivex/SingleSource;` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 10 | `SelectTagDialog.newInstance` | `([J)Lorg/proninyaroslav/libretorrent/ui/tag/SelectTagDialog;` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 11 | `SelectTagDialog.onAttach` | `(Landroid/content/Context;)V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 12 | `SelectTagDialog.onBackPressed` | `()V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 13 | `SelectTagDialog.onCreateDialog` | `(Landroid/os/Bundle;)Landroid/app/Dialog;` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 14 | `SelectTagDialog.onResume` | `()V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 15 | `SelectTagDialog.onStart` | `()V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 16 | `SelectTagDialog.onStop` | `()V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 17 | `SelectTagDialog.onTagClicked` | `(Lorg/proninyaroslav/libretorrent/ui/tag/TagItem;)V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 18 | `SelectTagDialog.subscribeTags` | `()V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 19 | `SelectTagViewModel.<init>` | `(Landroid/app/Application;)V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 20 | `SelectTagViewModel.filterExcludeTags` | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)Z` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 21 | `SelectTagViewModel.observeTags` | `()Lio/reactivex/Flowable;` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 22 | `SelectTagViewModel.setExcludeTagsId` | `([J)V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 23 | `tag.TagItem.<init>` | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 24 | `tag.TagItem.equals` | `(Ljava/lang/Object;)Z` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 25 | `tag.TagItem.isSame` | `(Lorg/proninyaroslav/libretorrent/ui/tag/TagItem;)Z` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 26 | `tag.TagsAdapter.<clinit>` | `()V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 27 | `tag.TagsAdapter.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/tag/TagsAdapter$OnClickListener;)V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 28 | `tag.TagsAdapter.onBindViewHolder` | `(Lorg/proninyaroslav/libretorrent/ui/tag/TagsAdapter$ViewHolder;I)V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 29 | `tag.TagsAdapter.onCreateViewHolder` | `(Landroid/view/ViewGroup;I)Lorg/proninyaroslav/libretorrent/ui/tag/TagsAdapter$ViewHolder;` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 30 | `tag.TagsAdapter$1.<init>` | `()V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 31 | `tag.TagsAdapter$1.areContentsTheSame` | `(Lorg/proninyaroslav/libretorrent/ui/tag/TagItem;Lorg/proninyaroslav/libretorrent/ui/tag/TagItem;)Z` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 32 | `tag.TagsAdapter$1.areItemsTheSame` | `(Lorg/proninyaroslav/libretorrent/ui/tag/TagItem;Lorg/proninyaroslav/libretorrent/ui/tag/TagItem;)Z` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 33 | `tag.TagsAdapter$ViewHolder.<init>` | `(Lorg/proninyaroslav/libretorrent/databinding/TagsListItemBinding;)V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 34 | `tag.TagsAdapter$ViewHolder.bind` | `(Lorg/proninyaroslav/libretorrent/ui/tag/TagItem;Lorg/proninyaroslav/libretorrent/ui/tag/TagsAdapter$OnClickListener;)V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 35 | `tag.TagsAdapter$ViewHolder.lambda$bind$0` | `(Lorg/proninyaroslav/libretorrent/ui/tag/TagsAdapter$OnClickListener;Lorg/proninyaroslav/libretorrent/ui/tag/TagItem;Landroid/view/View;)V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 36 | `TorrentTagsList.<init>(Context,AttributeSet)` | `(Landroid/content/Context;Landroid/util/AttributeSet;)V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 37 | `TorrentTagsList.buildAddTagButton` | `(Landroid/content/Context;)Lorg/proninyaroslav/libretorrent/ui/tag/AddTagButton;` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 38 | `TorrentTagsList.buildChip` | `(Landroid/content/Context;Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)Lcom/google/android/material/chip/Chip;` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 39 | `TorrentTagsList.init` | `(Landroid/content/Context;)V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |
| 40 | `TorrentTagsList.lambda$buildAddTagButton$1` | `(Landroid/view/View;)V` | OPEN | Dialog/adapter/custom view source contains local callbacks; full host route and AndroidX dispatch were not verified per target. |

## Evidence
- `SelectTagDialog.java:51-191`: dialog factory/lifecycle, subscriptions, tag selection and finish callback.
- `SelectTagViewModel.java:37-62`: exclude-tag setup/filter and tag stream.
- `TagsAdapter.java:34-98`: adapter creation/binding/diff and view holder callback.
- `TorrentTagsList.java:18-78`: custom ChipGroup setup and add-tag button construction.
This source-local evidence is partial and does not complete the entry/callback routes.

