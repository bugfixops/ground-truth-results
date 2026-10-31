# LibreTorrent batch 85 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, batch 85 only. Exact count: 40.

Summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. This batch spans CreateTorrentViewModel and custom UI views. Source shows ViewModel builder/observable calls and custom RecyclerView observer callbacks, but no complete route from the app entry through those callbacks was verified for every row. Keep all OPEN.

| Plan row | JVM method | Descriptor | Status | Reason |
|---:|---|---|---|---|
| 1 | `CreateTorrentViewModel.getPieceSizeByIndex` | `(I)I` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 2 | `CreateTorrentViewModel.getState` | `()Landroidx/lifecycle/LiveData;` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 3 | `CreateTorrentViewModel.getTorrentVersionByIndex` | `(I)Lorg/proninyaroslav/libretorrent/core/TorrentBuilder$TorrentVersion;` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 4 | `CreateTorrentViewModel.lambda$downloadTorrent$3` | `(Landroid/net/Uri;Landroid/net/Uri;Lio/reactivex/CompletableEmitter;Ljava/lang/Boolean;)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 5 | `CreateTorrentViewModel.lambda$downloadTorrent$4` | `(Landroid/net/Uri;Landroid/net/Uri;Lio/reactivex/CompletableEmitter;)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 6 | `CreateTorrentViewModel.lambda$makeBuilder$2` | `(Ljava/lang/String;)Z` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 7 | `CreateTorrentViewModel.lambda$new$0` | `(Ljava/lang/Boolean;)Z` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 8 | `CreateTorrentViewModel.lambda$new$1` | `(Ljava/lang/Boolean;)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 9 | `CreateTorrentViewModel.makeBuilder` | `()Lorg/proninyaroslav/libretorrent/core/TorrentBuilder;` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 10 | `CreateTorrentViewModel.makeCreator` | `()Ljava/lang/String;` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 11 | `CreateTorrentViewModel.makePercentProgress` | `(Lorg/proninyaroslav/libretorrent/core/TorrentBuilder$Progress;)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 12 | `CreateTorrentViewModel.normalizeAndValidateUrl` | `(Ljava/lang/String;)Ljava/lang/String;` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 13 | `CreateTorrentViewModel.onBuildError` | `(Ljava/lang/Throwable;)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 14 | `CreateTorrentViewModel.onBuildSuccess` | `([B)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 15 | `CreateTorrentViewModel.onCleared` | `()V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 16 | `CreateTorrentViewModel.resetPercentProgress` | `()V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 17 | `CreateTorrentViewModel.setPiecesSizeIndex` | `(I)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 18 | `CreateTorrentViewModel.setTorrentVersionIndex` | `(I)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 19 | `CreateTorrentViewModel$1.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/createtorrent/CreateTorrentViewModel;)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 20 | `CreateTorrentViewModel$1.onPropertyChanged` | `(Landroidx/databinding/Observable;I)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 21 | `CreateTorrentViewModel$BuildState.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/createtorrent/CreateTorrentViewModel$BuildState$Status;Ljava/lang/Throwable;)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 22 | `CreateTorrentViewModel$BuildState$Status.<clinit>` | `()V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 23 | `CreateTorrentViewModel$InvalidTrackerException.<init>` | `(Ljava/lang/String;)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 24 | `CreateTorrentViewModel$InvalidWebSeedException.<init>` | `(Ljava/lang/String;)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 25 | `ColorView.<init>` | `(Landroid/content/Context;Landroid/util/AttributeSet;)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 26 | `ColorView.getColor` | `()I` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 27 | `ColorView.onDraw` | `(Landroid/graphics/Canvas;)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 28 | `ColorView.onSizeChanged` | `(IIII)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 29 | `ColorView.setColor` | `(I)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 30 | `EmptyRecyclerView.<init>(Context,AttributeSet)` | `(Landroid/content/Context;Landroid/util/AttributeSet;)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 31 | `EmptyRecyclerView.<init>(Context,AttributeSet,int)` | `(Landroid/content/Context;Landroid/util/AttributeSet;I)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 32 | `EmptyRecyclerView.checkEmpty` | `()V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 33 | `EmptyRecyclerView.setAdapter` | `(Landroidx/recyclerview/widget/RecyclerView$Adapter;)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 34 | `EmptyRecyclerView.setEmptyView` | `(Landroid/view/View;)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 35 | `EmptyRecyclerView$1.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/customviews/EmptyRecyclerView;)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 36 | `EmptyRecyclerView$1.onChanged` | `()V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 37 | `EmptyRecyclerView$1.onItemRangeInserted` | `(II)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 38 | `EmptyRecyclerView$1.onItemRangeRemoved` | `(II)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 39 | `ExpansionHeader.<init>(Context,AttributeSet)` | `(Landroid/content/Context;Landroid/util/AttributeSet;)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |
| 40 | `ExpansionHeader.<init>(Context,AttributeSet,int)` | `(Landroid/content/Context;Landroid/util/AttributeSet;I)V` | OPEN | Local ViewModel/custom-view implementation exists; complete entry and framework callback route not verified for each member. |

## Evidence
- `CreateTorrentViewModel.java`: class line 55, state at 126, builder/progress methods around 157-247, URL and index helpers around 252-338, download method at 352.
- `ColorView.java`: draw/size/color methods at 76-103.
- `EmptyRecyclerView.java`: observer callbacks invoke `checkEmpty` at lines 36-50; adapter and empty-view methods at 69-97.
- `ExpansionHeader.java` defines a custom FrameLayout, constructor lines present in scan.
Framework callback dispatch and complete UI route are unresolved.

