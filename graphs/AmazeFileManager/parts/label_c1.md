STATUS: RUNNING 2025-01-10

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| AES256SHA256Decoder.<init> | UNREACHABLE | framework_never_calls | Apache Commons Compress sevenz library class; no app call sites | grep -rn "AES256SHA256Decoder" in app/src/main/java: no matches |
| AES256SHA256Decoder.decode | UNREACHABLE | framework_never_calls | Apache Commons Compress sevenz library class; no app call sites | grep -rn "AES256SHA256Decoder" in app/src/main/java: no matches |
| AES256SHA256Decoder$1.<init> | UNREACHABLE | framework_never_calls | Apache Commons Compress sevenz library class; no app call sites | grep -rn "AES256SHA256Decoder" in app/src/main/java: no matches |
| AES256SHA256Decoder$1.close | UNREACHABLE | framework_never_calls | Apache Commons Compress sevenz library class; no app call sites | grep -rn "AES256SHA256Decoder" in app/src/main/java: no matches |
| AES256SHA256Decoder$1.init | UNREACHABLE | framework_never_calls | Apache Commons Compress sevenz library class; no app call sites | grep -rn "AES256SHA256Decoder" in app/src/main/java: no matches |
| AES256SHA256Decoder$1.read | UNREACHABLE | framework_never_calls | Apache Commons Compress sevenz library class; no app call sites (one overload) | grep -rn "AES256SHA256Decoder" in app/src/main/java: no matches |
| AES256SHA256Decoder$1.read | UNREACHABLE | framework_never_calls | Apache Commons Compress sevenz library class; no app call sites (second overload) | grep -rn "AES256SHA256Decoder" in app/src/main/java: no matches |
| AdvancedSearchPref.<init> | REACHABLE | | Called from PreferencesActivity.selectItem | SRC PreferencesActivity.java:267 "loadPrefFragment(new AdvancedSearchPref(), R.string.advanced_search);" |
| AdvancedSearchPref.onCreate | REACHABLE | | Framework calls onCreate on PreferenceFragment | SRC AdvancedSearchPref.java:16-20 shows onCreate method; INFERRED framework lifecycle |
| AmazeFileManagerModule.<init> | REACHABLE | | Glide framework instantiates @GlideModule classes | SRC AmazeFileManagerModule.java:18 "@GlideModule"; INFERRED Glide annotation processor |
| AmazeFileManagerModule.registerComponents | REACHABLE | | Glide framework calls registerComponents on AppGlideModule | SRC AmazeFileManagerModule.java:20-23 shows method; INFERRED Glide framework lifecycle |
| AnimUtils.<init> | UNREACHABLE | no_trigger_in_app | Utility class with only static methods; constructor never called | SRC AnimUtils.java:30 shows class structure; no constructor calls in app |
| AnimUtils.getFastOutSlowInInterpolator | REACHABLE | | Called from app code | SRC Indicator.java:153 "interpolator = AnimUtils.getFastOutSlowInInterpolator(context);" |
| AnimUtils.marqueeAfterDelay | REACHABLE | | Called from adapters | SRC AppsAdapter.java:139 "AnimUtils.marqueeAfterDelay(2000, holder.txtTitle);"; RecyclerAdapter.java:316; CompressedExplorerAdapter.java:316 |
| AnimUtils.lambda$marqueeAfterDelay$0 | REACHABLE | | Lambda from marqueeAfterDelay | SRC AnimUtils.java:47-49 shows lambda "() -> { marqueeView.setSelected(true); }" |
| ApkImageDataFetcher.<init> | REACHABLE | | Called from ApkImageModelLoader.buildLoadData | SRC ApkImageModelLoader.java:27 "new ApkImageDataFetcher(packageManager, s)" |
| ApkImageDataFetcher.loadData | REACHABLE | | Glide framework calls loadData on DataFetcher | SRC ApkImageDataFetcher.java:27-32 shows method; INFERRED Glide framework calls |
| ApkImageDataFetcher.cleanup | REACHABLE | | Glide framework calls cleanup on DataFetcher | SRC ApkImageDataFetcher.java:35-37 shows method; INFERRED Glide framework lifecycle |
| ApkImageDataFetcher.cancel | REACHABLE | | Glide framework calls cancel on DataFetcher | SRC ApkImageDataFetcher.java:40-42 shows method; INFERRED Glide framework lifecycle |
| ApkImageDataFetcher.getDataClass | REACHABLE | | Glide framework calls getDataClass | SRC ApkImageDataFetcher.java:45-48 shows method; INFERRED Glide framework |
| ApkImageDataFetcher.getDataSource | REACHABLE | | Glide framework calls getDataSource | SRC ApkImageDataFetcher.java:51-54 shows method; INFERRED Glide framework |
| ApkImageModelLoader.<init> | REACHABLE | | Called from ApkImageModelLoaderFactory.build | SRC ApkImageModelLoaderFactory.java:23 "return new ApkImageModelLoader(packageManager);" |
| ApkImageModelLoader.buildLoadData | REACHABLE | | Glide framework calls buildLoadData on ModelLoader | SRC ApkImageModelLoader.java:24-27 shows method; INFERRED Glide framework calls |
| ApkImageModelLoader.handles | REACHABLE | | Glide framework calls handles on ModelLoader | SRC ApkImageModelLoader.java:30-33 shows method; INFERRED Glide framework calls |
| ApkImageModelLoaderFactory.<init> | REACHABLE | | Called from AmazeFileManagerModule.registerComponents | SRC AmazeFileManagerModule.java:22 "new ApkImageModelLoaderFactory(context.getPackageManager())" |
| ApkImageModelLoaderFactory.build | REACHABLE | | Glide framework calls build on ModelLoaderFactory | SRC ApkImageModelLoaderFactory.java:22-24 shows method; INFERRED Glide framework calls |
| ApkImageModelLoaderFactory.teardown | REACHABLE | | Glide framework calls teardown on ModelLoaderFactory | SRC ApkImageModelLoaderFactory.java:27-28 shows method; INFERRED Glide framework lifecycle |
| AppHolder.<init> | REACHABLE | | Called from AppsAdapter.onCreateViewHolder | SRC AppsAdapter.java:114 "final AppHolder vholder = new AppHolder(view);" |
| AppConfig.<clinit> | REACHABLE | | Static initializer called when class loaded | SRC AppConfig.java:51 shows "private static Handler mApplicationHandler = new Handler();" |
| AppConfig.<init> | REACHABLE | | Application class instantiated by Android framework | INFERRED framework creates Application instance |
| AppConfig.onCreate | REACHABLE | | Framework calls onCreate on Application | INFERRED framework lifecycle for Application |
| AppConfig.onTerminate | REACHABLE | | Framework calls onTerminate on Application | SRC AppConfig.java:82-85 shows method; INFERRED framework lifecycle |
| AppConfig.getInstance | REACHABLE | | Called from many places in app | SRC SftpConnectDialog.java:97 "AppConfig.getInstance().getUtilsProvider()"; Drawer.java:156, etc |
| AppConfig.getUtilsProvider | REACHABLE | | Called via getInstance | SRC AppConfig.java:59-61 shows method; called from SftpConnectDialog.java:97 |
| AppConfig.getUtilsHandler | REACHABLE | | Called via getInstance | SRC AppConfig.java:217 shows method; called from SftpConnectDialog.java:98 |
| AppConfig.getImageLoader | REACHABLE | | Called via getInstance | SRC AppConfig.java:205-212 shows method; called from Drawer.java:156 |
| AppConfig.getScreenUtils | REACHABLE | | Called via getInstance | SRC AppConfig.java:225-227 shows method; called from Drawer.java:243 |
| AppConfig.getMainActivityContext | REACHABLE | | Called via getInstance | SRC AppConfig.java:230-232 shows method; called from GeneralDialogCreation.java:889 |
| AppConfig.setMainActivityContext | REACHABLE | | Called to set main activity context | SRC AppConfig.java:221-224 shows method |
| AppConfig.runInBackground | REACHABLE | | Static method called from many places | SRC AppConfig.java:98-102 shows method; called from SftpConnectDialog.java:249, UtilsHandler.java:179, etc |
| AppConfig.toast | REACHABLE | | Static method called from many places (int overload) | SRC AppConfig.java:152-166 shows method; called from LoadFilesListTask.java:189 |
| AppConfig.toast | REACHABLE | | Static method called from many places (String overload) | SRC AppConfig.java:174-188 shows method |
| AppConfig.runInApplicationThread | REACHABLE | | Called internally by toast methods | SRC AppConfig.java:195-197 shows method; called from AppConfig.java:161, 183 |
| AppConfig.runInParallel | REACHABLE | | Static method for async tasks | SRC AppConfig.java:109-128 shows method |
| AppConfig.lambda$toast$0 | REACHABLE | | Lambda from toast(Context, int) | SRC AppConfig.java:160-162 shows lambda |
| AppConfig.lambda$toast$1 | REACHABLE | | Lambda from toast(Context, String) | SRC AppConfig.java:182-184 shows lambda |
| AppConfig$1.<init> | REACHABLE | | Anonymous inner class from runInParallel | SRC AppConfig.java:110-127 shows AsyncTask anonymous class |
| AppConfig$1.doInBackground | REACHABLE | | AsyncTask framework calls doInBackground | SRC AppConfig.java:118-120 shows method; INFERRED AsyncTask lifecycle |
| AppConfig$1.onPostExecute | REACHABLE | | AsyncTask framework calls onPostExecute | SRC AppConfig.java:123-126 shows method; INFERRED AsyncTask lifecycle |
| AppConfig$1.onPreExecute | REACHABLE | | AsyncTask framework calls onPreExecute | SRC AppConfig.java:113-116 shows method; INFERRED AsyncTask lifecycle |
| AppConfig$CustomAsyncCallbacks.<init> | REACHABLE | | Abstract class instantiated by subclasses | SRC AppConfig.java:137-139 shows constructor |
| AppConfig$CustomAsyncCallbacks.doInBackground | REACHABLE | | Called by AppConfig$1.doInBackground | SRC AppConfig.java:141 shows abstract method; AppConfig.java:119 shows call |
| AppConfig$CustomAsyncCallbacks.onPostExecute | REACHABLE | | Called by AppConfig$1.onPostExecute | SRC AppConfig.java:143 shows method; AppConfig.java:125 shows call |
| AppConfig$CustomAsyncCallbacks.onPreExecute | REACHABLE | | Called by AppConfig$1.onPreExecute | SRC AppConfig.java:145 shows method; AppConfig.java:115 shows call |

STATUS: DONE 21:17
