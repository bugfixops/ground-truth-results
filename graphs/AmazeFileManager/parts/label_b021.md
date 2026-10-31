STATUS: RUNNING 22:51

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| DecryptService$BackgroundTask.<init> | REACHABLE | | Created by DecryptService.onStartCommand, chained to AsyncTask constructor | SRC DecryptService.java:118, 123 |
| DecryptService$BackgroundTask.doInBackground | REACHABLE | | Called by AsyncTask framework on background thread | SRC DecryptService.java:127-158; FW-SRC core/java/android/os/AsyncTask.java:333 |
| DecryptService$BackgroundTask.lambda$doInBackground$0 | REACHABLE | | Lambda invoked from doInBackground as progress listener | SRC DecryptService.java:138-139 |
| DecryptService$BackgroundTask.onPostExecute | REACHABLE | | Called by AsyncTask framework when doInBackground completes | SRC DecryptService.java:162-171; FW-SRC core/java/android/os/AsyncTask.java:695 |
| DeltaDecoder.<init> | REACHABLE | | Instantiated in Coders static initializer for DELTA_FILTER | SRC sevenz/Coders.java:64; SRC sevenz/DeltaDecoder.java:28-30 |
| DeltaDecoder.decode | REACHABLE | | Called by Coders.addDecoder when processing 7z archives with delta encoding | SRC sevenz/Coders.java:73; SRC sevenz/DeltaDecoder.java:33-37 |
| DeltaDecoder.encode | REACHABLE | | Called by Coders.addEncoder when creating 7z archives with delta encoding | SRC sevenz/Coders.java:84; SRC sevenz/DeltaDecoder.java:40-48 |
| DeltaDecoder.getOptionsAsProperties | REACHABLE | | Called by Coders.addEncoder to serialize delta options | SRC sevenz/SevenZOutputFile.java:452; SRC sevenz/DeltaDecoder.java:51-55 |
| DeltaDecoder.getOptionsFromCoder | REACHABLE | | Public method called from SevenZFile.buildDecodingStream | SRC sevenz/SevenZFile.java:1033; SRC sevenz/DeltaDecoder.java:58-60 |
| DeltaDecoder.getOptionsFromCoder | REACHABLE | | Private overload called from decode and public getOptionsFromCoder | SRC sevenz/DeltaDecoder.java:36, 59, 63-68 |
| DisablableViewPager.<init> | REACHABLE | | Instantiated by LayoutInflater from tabfragment.xml layout | SRC res/layout/tabfragment.xml:20-36; SRC TabFragment.java:95; SRC DisablableViewPager.java:15-18 |
| DisablableViewPager.onInterceptTouchEvent | REACHABLE | | Called by ViewPager framework to determine touch interception | SRC DisablableViewPager.java:26-29; INFERRED androidx ViewPager touch event dispatch, source not read |
| DisablableViewPager.onTouchEvent | REACHABLE | | Called by ViewPager framework on touch events | SRC DisablableViewPager.java:21-23; INFERRED androidx ViewPager touch event dispatch, source not read |
| DisablableViewPager.setPagingEnabled | REACHABLE | | Public API called to enable/disable paging | SRC DisablableViewPager.java:31-33 |
| DividerItemDecoration.<clinit> | REACHABLE | | Static initializer defining ATTRS array | SRC DividerItemDecoration.java:19-21 |
| DividerItemDecoration.<init> | REACHABLE | | Instantiated by MainFragment and CompressedExplorerFragment | SRC MainFragment.java:304-305; SRC DividerItemDecoration.java:29-37 |
| DividerItemDecoration.drawVertical | REACHABLE | | Called by onDraw to draw divider lines | SRC DividerItemDecoration.java:48, 53-73 |
| DividerItemDecoration.getItemOffsets | REACHABLE | | Called by RecyclerView framework to compute item spacing | SRC DividerItemDecoration.java:77-88; INFERRED androidx RecyclerView ItemDecoration lifecycle, source not read |
| DividerItemDecoration.onDraw | REACHABLE | | Called by RecyclerView framework to render dividers | SRC DividerItemDecoration.java:41-49; INFERRED androidx RecyclerView ItemDecoration lifecycle, source not read |
| DonationViewHolder.<init> | UNREACHABLE | no_trigger_in_app | DonationViewHolder is never instantiated in any adapter; grep shows no references outside the class definition | SRC DonationViewHolder.java:1-20; grep output shows no usage |

STATUS: DONE 22:55
