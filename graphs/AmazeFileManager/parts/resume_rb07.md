STATUS: RUNNING 18:46

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| DatabaseViewerActivity.onBackPressed | REACHABLE | | Called from onOptionsItemSelected when home button pressed | SRC DatabaseViewerActivity.java:206-207 onOptionsItemSelected calls onBackPressed; line 213-216 onBackPressed implementation |
| DatabaseViewerActivity.onDestroy | REACHABLE | | Activity lifecycle callback | SRC DatabaseViewerActivity.java:189-195 onDestroy closes database resources |
| DatabaseViewerActivity.onOptionsItemSelected | REACHABLE | | Already labeled in graph_def.py | SRC DatabaseViewerActivity.java:204-210 |
| DatabaseViewerActivity.onPrepareOptionsMenu | REACHABLE | | Activity menu lifecycle callback | SRC DatabaseViewerActivity.java:198-201 onPrepareOptionsMenu sets toolbar title |
| DatapointParcelable$1.createFromParcel | UNREACHABLE | | Already labeled in graph_def.py UNREACHABLE_PART_B020 | SRC DatapointParcelable.java:129-131 |
| DatapointParcelable$1.newArray | UNREACHABLE | | Already labeled in graph_def.py UNREACHABLE_PART_B020 | SRC DatapointParcelable.java:134-136 |
| DatapointParcelable.<init>(Parcel) | UNREACHABLE | no_trigger_in_app | Parcel constructor only called from createFromParcel which is UNREACHABLE | SRC DatapointParcelable.java:120-127 constructor reads from Parcel; createFromParcel is only caller |
| DatapointParcelable.<init>(String,int,int,long,long,long,boolean) | UNREACHABLE | no_trigger_in_app | 7-parameter constructor never called in app | SRC DatapointParcelable.java:78-88 constructor; AbstractProgressiveService.java:157-158 uses 8-param, line 178 uses 4-param |
| DatapointParcelable.describeContents | UNREACHABLE | | Already labeled in graph_def.py UNREACHABLE_PART_B020 | SRC DatapointParcelable.java:142-144 |
| DatapointParcelable.writeToParcel | UNREACHABLE | | Already labeled in graph_def.py UNREACHABLE_PART_B020 | SRC DatapointParcelable.java:147-155 |
| DecryptService$BackgroundTask.doInBackground | REACHABLE | | Already labeled in graph_def.py batch_021 | SRC DecryptService.java:123-159 |
| DecryptService$BackgroundTask.lambda$doInBackground$0 | REACHABLE | | Already labeled in graph_def.py batch_021 | SRC DecryptService.java:138-139 |
| DecryptService$BackgroundTask.onPostExecute | REACHABLE | | Already labeled in graph_def.py batch_021 | SRC DecryptService.java:162-172 |
| DecryptService.onBind | REACHABLE | | Already labeled in graph_def.py | SRC DecryptService.java:228-230 |
| DeltaDecoder.encode | UNREACHABLE | | Already labeled in graph_def.py | Apache Commons Compress library for 7z |
| DeltaDecoder.getOptionsAsProperties | UNREACHABLE | | Already labeled in graph_def.py | Apache Commons Compress library for 7z |
| DisablableViewPager.<init> | REACHABLE | | Already labeled in graph_def.py | SRC DisablableViewPager.java:14-17 |
| DisablableViewPager.onInterceptTouchEvent | REACHABLE | | Already labeled in graph_def.py | SRC DisablableViewPager.java:23-26 |
| DisablableViewPager.onTouchEvent | REACHABLE | | Already labeled in graph_def.py | SRC DisablableViewPager.java:19-21 |
| DividerItemDecoration.drawVertical | REACHABLE | | Already labeled in graph_def.py | SRC DividerItemDecoration.java:49-70 |
| DividerItemDecoration.getItemOffsets | REACHABLE | | Already labeled in graph_def.py | SRC DividerItemDecoration.java:72-82 |
| DividerItemDecoration.onDraw | REACHABLE | | Already labeled in graph_def.py | SRC DividerItemDecoration.java:37-43 |
| DonationViewHolder.<init> | REACHABLE | | Already labeled in graph_def.py | SRC DonationViewHolder.java:11-17 |
| Drawer.isOpen | REACHABLE | | Already labeled in graph_def.py | SRC Drawer.java:530-532 |
| Drawer.isSomethingSelected | REACHABLE | | Already labeled in graph_def.py | SRC Drawer.java:662-664 |
| Drawer.lambda$addNewItem$5 | REACHABLE | | Lambda for menu item onClick; called from onNavigationItemSelected | SRC Drawer.java:402-439 addNewItem creates MenuMetadata with lambdas; line 597 meta.onClickListener.onClick() calls lambda |
| Drawer.lockIfNotOnTablet | REACHABLE | | Already labeled in graph_def.py | SRC Drawer.java:750-756 |
| Drawer.onActivityResult | REACHABLE | | Already labeled in graph_def.py | SRC Drawer.java:489-498 |
| Drawer.onConfigurationChanged | REACHABLE | | Already labeled in graph_def.py | SRC Drawer.java:727-729 |
| Drawer.resetPendingPath | REACHABLE | | Called from onDrawerClosed to clear pending path | SRC Drawer.java:719-721 resetPendingPath sets pendingPath = null |
| Drawer.syncState | REACHABLE | | Already labeled in graph_def.py | SRC Drawer.java:723-725 |
| DummyFileGenerator.<init> | UNREACHABLE | | Already labeled in graph_def.py | Test utility marked @RestrictTo(TESTS) |
| DummyFileGenerator.createFile | UNREACHABLE | | Already labeled in graph_def.py | Test utility marked @RestrictTo(TESTS) |
| EditTextColorStateUtil.<init> | UNREACHABLE | | Already labeled in graph_def.py | Utility class with all static methods |
| EditTextColorStateUtil.createEditTextColorStateList | REACHABLE | | Already labeled in graph_def.py | SRC EditTextColorStateUtil.java:29-40 |
| EditTextColorStateUtil.setTint | REACHABLE | | Already labeled in graph_def.py | SRC EditTextColorStateUtil.java:21-28 |
| EncryptDecryptUtils.<init> | UNREACHABLE | | Already labeled in graph_def.py | Utility class with all static methods |
| EncryptService$1.onReceive | REACHABLE | | Already labeled in graph_def.py | SRC EncryptService.java:226-231 |

STATUS: DONE 18:52
