STATUS: RUNNING 22:51

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| DataUtils$DataUtilsHolder.<clinit> | REACHABLE | | Called from DataUtils.getInstance | SRC DataUtils.java:82-83 |
| DataUtils$DataUtilsHolder.<init> | UNREACHABLE | no_trigger_in_app | Private constructor never called; singleton uses static INSTANCE field | SRC DataUtils.java:78-80 |
| DatapointParcelable.<clinit> | REACHABLE | | Initializes CREATOR field accessed by framework | SRC DatapointParcelable.java:126-138 |
| DatapointParcelable.<init>(Ljava/lang/String;IJZ)V | REACHABLE | | Called from AbstractProgressiveService.addFirstDatapoint | SRC AbstractProgressiveService.java:178 |
| DatapointParcelable.<init>(Ljava/lang/String;IIJJJZ)V | REACHABLE | | Called from AbstractProgressiveService.publishResults | SRC AbstractProgressiveService.java:157-159 |
| DatapointParcelable.<init>(Ljava/lang/String;IIJJJZZ)V | REACHABLE | | Called from AbstractProgressiveService.publishResults | SRC AbstractProgressiveService.java:157-159 |
| DatapointParcelable.<init>(Landroid/os/Parcel;)V | UNREACHABLE | no_trigger_in_app | Constructor only called from createFromParcel which is never called | SRC DatapointParcelable.java:120-129 |
| DatapointParcelable.describeContents | UNREACHABLE | no_trigger_in_app | Parcelable method never called; DatapointParcelable stored in lists not parceled | SRC DatapointParcelable.java:142-144 |
| DatapointParcelable.writeToParcel | UNREACHABLE | no_trigger_in_app | Parcelable method never called; DatapointParcelable never parceled through Intents | SRC DatapointParcelable.java:147-155 |
| DatapointParcelable$1.<init> | REACHABLE | | Created by DatapointParcelable.<clinit> for CREATOR field | SRC DatapointParcelable.java:126-138 |
| DatapointParcelable$1.createFromParcel | UNREACHABLE | no_trigger_in_app | CREATOR method never called; DatapointParcelable never unparceled | SRC DatapointParcelable.java:129-131 |
| DatapointParcelable$1.newArray | UNREACHABLE | no_trigger_in_app | CREATOR method never called; DatapointParcelable arrays never unparceled | SRC DatapointParcelable.java:134-136 |
| DbViewerFragment.<init> | REACHABLE | | Instantiated in DatabaseViewerActivity listener | SRC DatabaseViewerActivity.java:135 |
| DbViewerFragment.onActivityCreated | REACHABLE | | Fragment lifecycle after onCreateView | SRC DbViewerFragment.java:54-57 |
| DbViewerFragment.onCreateView | REACHABLE | | Fragment lifecycle after instantiation | SRC DbViewerFragment.java:33-35 |
| DbViewerFragment.onDetach | REACHABLE | | Fragment lifecycle when fragment destroyed | SRC DbViewerFragment.java:69-73 |
| Decompressor.<init> | UNREACHABLE | no_trigger_in_app | Abstract constructor called only by subclasses; subclass edges cover this | SRC Decompressor.java:23-25 |
| Decompressor.decompress(Ljava/lang/String;)V | REACHABLE | | Called from MainActivityHelper.extractFile | SRC MainActivityHelper.java:529 |
| Decompressor.decompress(Ljava/lang/String;[Ljava/lang/String;)V | REACHABLE | | Called from CompressedExplorerFragment.extractFiles | SRC CompressedExplorerFragment.java:329 |
| Decompressor.realRelativeDirectory | REACHABLE | | Called from Decompressor.decompress with array parameter | SRC Decompressor.java:58-60 |
| Decompressor.setFilePath | REACHABLE | | Called from CompressedHelper.getCompressorInstance | SRC CompressedHelper.java:131 |
| DecryptService.<init> | REACHABLE | | Framework creates service instance when started via Intent | SRC EncryptDecryptUtils.java:67 |
| DecryptService.getDataPackages | REACHABLE | | Called by AbstractProgressiveService implementation | SRC DecryptService.java:217-219 |
| DecryptService.getNotificationBuilder | REACHABLE | | Called by AbstractProgressiveService implementation | SRC DecryptService.java:191-193 |
| DecryptService.getNotificationCustomViewBig | REACHABLE | | Called by AbstractProgressiveService implementation | SRC DecryptService.java:212-214 |
| DecryptService.getNotificationCustomViewSmall | REACHABLE | | Called by AbstractProgressiveService implementation | SRC DecryptService.java:207-209 |
| DecryptService.getNotificationId | REACHABLE | | Called by AbstractProgressiveService implementation | SRC DecryptService.java:196-198 |
| DecryptService.getNotificationManager | REACHABLE | | Called by AbstractProgressiveService implementation | SRC DecryptService.java:186-188 |
| DecryptService.getProgressHandler | REACHABLE | | Called by AbstractProgressiveService implementation | SRC DecryptService.java:222-224 |
| DecryptService.getProgressListener | REACHABLE | | Called when service updates progress | SRC DecryptService.java:231-233 |
| DecryptService.getTitle | REACHABLE | | Called by AbstractProgressiveService implementation | SRC DecryptService.java:202-204 |
| DecryptService.isDecryptService | REACHABLE | | Called by AbstractProgressiveService implementation | SRC DecryptService.java:227-229 |
| DecryptService.onBind | REACHABLE | | Called when ProcessViewerFragment binds to service | SRC ProcessViewerFragment.java:170 |
| DecryptService.onCreate | REACHABLE | | Service lifecycle before onStartCommand | SRC DecryptService.java:64-68 |
| DecryptService.onDestroy | REACHABLE | | Service lifecycle when service stopped | SRC DecryptService.java:238-241 |
| DecryptService.onStartCommand | REACHABLE | | Called when service started via startService | SRC EncryptDecryptUtils.java:67 |
| DecryptService.setProgressListener | REACHABLE | | Called by ProcessViewerFragment when bound | SRC DecryptService.java:233-235 |
| DecryptService$1.<init> | REACHABLE | | Created for cancelReceiver field in DecryptService | SRC DecryptService.java:214-221 |
| DecryptService$1.onReceive | REACHABLE | | Framework calls when cancel broadcast received | SRC DecryptService.java:217-220 |

STATUS: DONE 22:51
