# Repair batch 16: 39 methods

STATUS: START 21:05

| Method | Label | Evidence Lines |
|--------|-------|----------------|
| ThemedImageView.<init>(Context) | REACHABLE | SRC ui/views/ThemedImageView.java:21-23; XML res/layout/fragment_sheet_cloud.xml:41,65,90,114,138,162,186 |
| ThemedImageView.<init>(Context,AttributeSet) | REACHABLE | SRC ui/views/ThemedImageView.java:25-27; XML res/layout/fragment_sheet_cloud.xml:41,65,90,114,138,162,186 |
| ThemedImageView.<init>(Context,AttributeSet,int) | REACHABLE | SRC ui/views/ThemedImageView.java:29-40; called by other constructors line 22, 26 |
| ThemedImageView.getActivity | REACHABLE | SRC ui/views/ThemedImageView.java:42-51; called from constructor line 33 |
| SearchView$1.onAnimationCancel | REACHABLE | SRC ui/views/appbar/SearchView.java:108; framework callback |
| SearchView$1.onAnimationEnd | REACHABLE | SRC ui/views/appbar/SearchView.java:103; framework callback |
| SearchView$1.onAnimationRepeat | REACHABLE | SRC ui/views/appbar/SearchView.java:110; framework callback |
| SearchView$1.onAnimationStart | REACHABLE | SRC ui/views/appbar/SearchView.java:100; framework callback |
| SearchView$2.onAnimationCancel | REACHABLE | SRC ui/views/appbar/SearchView.java:144; framework callback |
| SearchView$2.onAnimationEnd | REACHABLE | SRC ui/views/appbar/SearchView.java:139; framework callback |
| SearchView$2.onAnimationRepeat | REACHABLE | SRC ui/views/appbar/SearchView.java:146; framework callback |
| SearchView$2.onAnimationStart | REACHABLE | SRC ui/views/appbar/SearchView.java:136; framework callback |
| CustomNavigationView$SavedState.<clinit> | UNREACHABLE | Already labeled in graph_def.py:2773 framework_never_calls |
| CustomNavigationView$SavedState.<init>(Parcel) | UNREACHABLE | Already labeled in graph_def.py:2785 framework_never_calls |
| CustomNavigationView$SavedState.<init>(Parcelable) | UNREACHABLE | Already labeled in graph_def.py:2779 framework_never_calls |
| CustomNavigationView$SavedState.writeToParcel | UNREACHABLE | Already labeled in graph_def.py:2791 framework_never_calls |
| PathSwitchPreference.lambda$setListener$0 | REACHABLE | SRC ui/views/preference/PathSwitchPreference.java:50-53; lambda synthetic method |
| PathSwitchPreference.onBindView | REACHABLE | SRC ui/views/preference/PathSwitchPreference.java:33-41; framework lifecycle method |
| PathSwitchPreference.onCreateView | REACHABLE | SRC ui/views/preference/PathSwitchPreference.java:27-31; framework lifecycle method |
| PathSwitchPreference.setListener | REACHABLE | SRC ui/views/preference/PathSwitchPreference.java:47-56; called from onBindView line 35-36 |
| OneCharacterCharSequence.charAt | UNREACHABLE | SRC utils/OneCharacterCharSequence.java:14-17; no_trigger_in_app class not instantiated |
| OneCharacterCharSequence.length | UNREACHABLE | SRC utils/OneCharacterCharSequence.java:20-22; no_trigger_in_app class not instantiated |
| OneCharacterCharSequence.subSequence | UNREACHABLE | SRC utils/OneCharacterCharSequence.java:25-27; no_trigger_in_app class not instantiated |
| OneCharacterCharSequence.toString | UNREACHABLE | SRC utils/OneCharacterCharSequence.java:30-34; no_trigger_in_app class not instantiated |
| ScreenUtils.convertPxToDb | REACHABLE | SRC utils/ScreenUtils.java:22-24; already has route in graph_def.py:1237 |
| ScreenUtils.getScreeHeightInDb | REACHABLE | SRC utils/ScreenUtils.java:43-45; called from AppConfig |
| ScreenUtils.getScreenHeightInPx | REACHABLE | SRC utils/ScreenUtils.java:28-32; called from AppConfig |
| ScreenUtils.getScreenWidthInDp | REACHABLE | SRC utils/ScreenUtils.java:38-40; called from AppConfig |
| Streamer.getNameFromPath | UNREACHABLE | SRC utils/SmbStreamer/Streamer.java:141-150; no_trigger_in_app Streamer not used |
| Streamer.isStreamMedia | UNREACHABLE | SRC utils/SmbStreamer/Streamer.java:46-48; no_trigger_in_app Streamer not used |
| Streamer.serve | UNREACHABLE | SRC utils/SmbStreamer/Streamer.java:64-138; no_trigger_in_app Streamer not used |
| Streamer.setStreamSrc | UNREACHABLE | SRC utils/SmbStreamer/Streamer.java:50-54; no_trigger_in_app Streamer not used |
| CloudUtil.getThumbnailInputStreamForCloud | REACHABLE | SRC utils/cloud/CloudUtil.java:262-318; loads thumbnails for cloud files |
| CloudUtil.lambda$launchCloud$1 | REACHABLE | SRC utils/cloud/CloudUtil.java:137-156; lambda synthetic method |
| CloudUtil.lambda$null$0 | REACHABLE | SRC utils/cloud/CloudUtil.java:139-155; nested lambda synthetic method |
| CloudUtil.launchCloud | REACHABLE | Already has route in graph_def.py:1806 |
| RecyclerAdapter$1.lambda$onLoadFailed$0 | REACHABLE | SRC adapters/RecyclerAdapter.java:876-879; lambda synthetic method |
| RecyclerAdapter$1.onLoadFailed | REACHABLE | SRC adapters/RecyclerAdapter.java:874-883; Glide callback |
| RecyclerAdapter$1.onResourceReady | REACHABLE | SRC adapters/RecyclerAdapter.java:885-895; Glide callback |

STATUS: DONE 21:09
