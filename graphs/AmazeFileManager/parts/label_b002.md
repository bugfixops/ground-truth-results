STATUS: RUNNING 21:16

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| ApkImageModelLoaderFactory.\<init\> | REACHABLE | | Created in AmazeFileManagerModule.registerComponents line 21 | SRC AmazeFileManagerModule.java:21 |
| ApkImageModelLoaderFactory.build | REACHABLE | | Called by Glide framework during model loader initialization | INFERRED Glide ModelLoaderFactory lifecycle (source not read) |
| ApkImageModelLoaderFactory.teardown | UNREACHABLE | no_trigger_in_app | Glide lifecycle teardown, framework-driven cleanup | SRC ApkImageModelLoaderFactory.java:28-30 |
| AppConfig.\<clinit\> | UNREACHABLE | closed_by_configuration | Static initializer, no explicit entry point | SRC AppConfig.java:48-63 |
| AppConfig.\<init\> | UNREACHABLE | no_trigger_in_app | Constructor called only by framework or reflection | SRC AppConfig.java:48-63 |
| AppConfig.getInstance | REACHABLE | | Called from MainActivity.onCreate to get singleton instance | SRC MainActivity.java:287, 297 |
| AppConfig.getImageLoader | UNREACHABLE | no_trigger_in_app | Getter accessed only by reflection or external code | SRC AppConfig.java:221-228 |
| AppConfig.getMainActivityContext | UNREACHABLE | no_trigger_in_app | Getter not called by reachable code | SRC AppConfig.java:239-241 |
| AppConfig.getScreenUtils | UNREACHABLE | no_trigger_in_app | Getter not called by reachable code | SRC AppConfig.java:237-238 |
| AppConfig.getUtilsHandler | REACHABLE | | Called from AppConfig.getInstance in MainActivity.onCreate | SRC MainActivity.java:297 |
| AppConfig.getUtilsProvider | REACHABLE | | Called via BasicActivity methods inherited by MainActivity and other activities | SRC BasicActivity.java:20, 24, 28 |
| AppConfig.lambda$toast$0 | UNREACHABLE | no_trigger_in_app | Lambda in toast(@StringRes int), only executed if toast method is called, not in reachable code | SRC AppConfig.java:169-172 |
| AppConfig.lambda$toast$1 | UNREACHABLE | no_trigger_in_app | Lambda in toast(String), only executed if toast method is called, not in reachable code | SRC AppConfig.java:188-191 |
| AppConfig.onCreate | REACHABLE | | Called by framework when Application starts, via GlideApplication.onCreate | INFERRED Application lifecycle chain (android.app source not read) |
| AppConfig.onTerminate | UNREACHABLE | framework_never_calls | Application.onTerminate not reliably called; apps often killed without cleanup | SRC AppConfig.java:85-87 |
| AppConfig.runInApplicationThread | UNREACHABLE | no_trigger_in_app | Public method not called by any reachable code | SRC AppConfig.java:234-236 |
| AppConfig.runInBackground | UNREACHABLE | no_trigger_in_app | Static method not called by any reachable code | SRC AppConfig.java:100-107 |
| AppConfig.runInParallel | UNREACHABLE | no_trigger_in_app | Static method not called by any reachable code | SRC AppConfig.java:110-132 |
| AppConfig.setMainActivityContext | REACHABLE | | Called from AppConfig.getInstance in MainActivity.onCreate | SRC MainActivity.java:287 |
| AppConfig.toast | UNREACHABLE | no_trigger_in_app | Static method (int StringRes) not called by any reachable code | SRC AppConfig.java:158-172 |
| AppConfig.toast | UNREACHABLE | no_trigger_in_app | Static method (String) not called by any reachable code | SRC AppConfig.java:182-191 |
| AppConfig$1.\<init\> | UNREACHABLE | no_trigger_in_app | Anonymous AsyncTask created in runInParallel but never executed | SRC AppConfig.java:125-132 |
| AppConfig$1.doInBackground | UNREACHABLE | no_trigger_in_app | Called only if AppConfig.runInParallel is called | SRC AppConfig.java:128 |
| AppConfig$1.onPostExecute | UNREACHABLE | no_trigger_in_app | Called only if AppConfig.runInParallel is called | SRC AppConfig.java:131 |
| AppConfig$1.onPreExecute | UNREACHABLE | no_trigger_in_app | Called only if AppConfig.runInParallel is called | SRC AppConfig.java:127 |
| AppConfig$CustomAsyncCallbacks.\<init\> | UNREACHABLE | no_trigger_in_app | Abstract class constructor, only called by subclasses when instantiated | SRC AppConfig.java:138-141 |
| AppConfig$CustomAsyncCallbacks.onPostExecute | UNREACHABLE | no_trigger_in_app | Framework callback only executed if AsyncTask runs | SRC AppConfig.java:146-147 |
| AppConfig$CustomAsyncCallbacks.onPreExecute | UNREACHABLE | no_trigger_in_app | Framework callback only executed if AsyncTask runs | SRC AppConfig.java:148-149 |
| AppHolder.\<init\> | UNREACHABLE | no_trigger_in_app | ViewHolder constructor called by RecyclerView framework when binding items, not reachable by app code | SRC AppHolder.java:24-34 |
| AppListLoader.\<init\> | REACHABLE | | Created in AppsListFragment.onCreateLoader which is called by LoaderManager | SRC AppsListFragment.java:162-164, AppListLoader.java:33-40 |
| AppListLoader.deliverResult | REACHABLE | | Called by AsyncTaskLoader lifecycle after loadInBackground | INFERRED AsyncTaskLoader lifecycle (androidx.loader source not read) |
| AppListLoader.loadInBackground | REACHABLE | | Called by AsyncTaskLoader framework when load starts | INFERRED AsyncTaskLoader lifecycle (androidx.loader source not read) |
| AppListLoader.onCanceled | REACHABLE | | Called by AsyncTaskLoader when load is cancelled | INFERRED AsyncTaskLoader lifecycle (androidx.loader source not read) |
| AppListLoader.onReleaseResources | UNREACHABLE | closed_by_configuration | Empty TODO method with no implementation | SRC AppListLoader.java:163-171 |
| AppListLoader.onReset | REACHABLE | | Called by AsyncTaskLoader lifecycle during reset | INFERRED AsyncTaskLoader lifecycle (androidx.loader source not read) |
| AppListLoader.onStartLoading | REACHABLE | | Called by AsyncTaskLoader when loading starts | INFERRED AsyncTaskLoader lifecycle (androidx.loader source not read) |
| AppListLoader.onStopLoading | REACHABLE | | Called by AsyncTaskLoader when loading stops | INFERRED AsyncTaskLoader lifecycle (androidx.loader source not read) |
| AppListLoader$AppsDataPair.\<init\> | REACHABLE | | Created in AppListLoader.loadInBackground to wrap results | SRC AppListLoader.java:52, 75 |

STATUS: DONE 21:16
