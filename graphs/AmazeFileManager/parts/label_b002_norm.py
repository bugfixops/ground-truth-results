# ---- Helper batch_002 label part (2026-10-27)

e('AmazeFileManagerModule.registerComponents', 'ApkImageModelLoaderFactory.<init>', 'EXPLICIT', 'AmazeFileManagerModule.java:21 creates new ApkImageModelLoaderFactory(context.getPackageManager()

e('ApkImageModelLoaderFactory.<init>', 'ApkImageModelLoaderFactory.build', 'LIFECYCLE', 'build()

e('AppsListFragment.onActivityCreated', 'AppListLoader.<init>', 'FRAMEWORK', 'LoaderManager.initLoader at line 109 calls onCreateLoader which creates AppListLoader', evidence='SRC AppsListFragment.java:109, 162-164')

e('AppListLoader.<init>', 'AppListLoader.loadInBackground', 'LIFECYCLE', 'loadInBackground called by AsyncTaskLoader when load starts', evidence='INFERRED AsyncTaskLoader lifecycle (androidx.loader source not read)

e('AppListLoader.loadInBackground', 'AppListLoader.deliverResult', 'LIFECYCLE', 'deliverResult called by AsyncTaskLoader after loadInBackground completes', evidence='INFERRED AsyncTaskLoader lifecycle (androidx.loader source not read)

e('AppListLoader.deliverResult', 'AppListLoader.onReleaseResources', 'LIFECYCLE', 'deliverResult calls onReleaseResources to clean up old data', evidence='SRC AppListLoader.java:85-99')

e('AppListLoader.onStartLoading', 'AppListLoader.deliverResult', 'LIFECYCLE', 'onStartLoading may call deliverResult if data exists', evidence='SRC AppListLoader.java:104-115')

e('AppListLoader.onStopLoading', 'AppListLoader.onCanceled', 'LIFECYCLE', 'onStopLoading may result in onCanceled being called', evidence='INFERRED AsyncTaskLoader lifecycle (androidx.loader source not read)

e('AppListLoader.onCanceled', 'AppListLoader.onReleaseResources', 'LIFECYCLE', 'onCanceled calls onReleaseResources to clean up', evidence='SRC AppListLoader.java:137-139')

e('AppListLoader.onReset', 'AppListLoader.onStopLoading', 'LIFECYCLE', 'onReset calls onStopLoading before cleanup', evidence='SRC AppListLoader.java:141-156')

e('AppListLoader.loadInBackground', 'AppListLoader$AppsDataPair.<init>', 'EXPLICIT', 'loadInBackground returns new AppsDataPair at lines 52, 75', evidence='SRC AppListLoader.java:52, 75')

e('MainActivity.onCreate', 'AppConfig.getInstance', 'EXPLICIT', 'getInstance()

e('AppConfig.getInstance', 'AppConfig.getUtilsHandler', 'EXPLICIT', 'getUtilsHandler()

e('AppConfig.getInstance', 'AppConfig.setMainActivityContext', 'EXPLICIT', 'setMainActivityContext()

e('LeakCanaryApplication.onCreate', 'AppConfig.onCreate', 'LIFECYCLE', 'super.onCreate()

UNREACHABLE['AppConfig.<clinit>'] = (
    'closed_by_configuration',
    'Static initializer, no explicit entry',
    'SRC AppConfig.java:48-63',
    'SOURCE'
)

UNREACHABLE['AppConfig.<init>'] = (
    'no_trigger_in_app',
    'Constructor called only by framework or reflection',
    'SRC AppConfig.java:48-63',
    'INFERRED'
)

UNREACHABLE['AppConfig.getImageLoader'] = (
    'no_trigger_in_app',
    'Getter accessed only by reflection or external code',
    'SRC AppConfig.java:221-228',
    'INFERRED'
)

UNREACHABLE['AppConfig.getMainActivityContext'] = (
    'no_trigger_in_app',
    'Getter not called by reachable code',
    'SRC AppConfig.java:239-241',
    'INFERRED'
)

UNREACHABLE['AppConfig.getScreenUtils'] = (
    'no_trigger_in_app',
    'Getter not called by reachable code',
    'SRC AppConfig.java:237-238',
    'INFERRED'
)

UNREACHABLE['AppConfig.lambda$toast$0'] = (
    'no_trigger_in_app',
    'Lambda in toast(@StringRes int)

UNREACHABLE['AppConfig.lambda$toast$1'] = (
    'no_trigger_in_app',
    'Lambda in toast(String)

UNREACHABLE['AppConfig.onTerminate'] = (
    'framework_never_calls',
    'Application.onTerminate not reliably called; apps often killed without cleanup',
    'SRC AppConfig.java:85-87',
    'SOURCE'
)

UNREACHABLE['AppConfig.runInApplicationThread'] = (
    'no_trigger_in_app',
    'Public method not called by any reachable code',
    'SRC AppConfig.java:234-236',
    'INFERRED'
)

UNREACHABLE['AppConfig.runInBackground'] = (
    'no_trigger_in_app',
    'Static method not called by any reachable code',
    'SRC AppConfig.java:100-107',
    'INFERRED'
)

UNREACHABLE['AppConfig.runInParallel'] = (
    'no_trigger_in_app',
    'Static method not called by any reachable code',
    'SRC AppConfig.java:110-132',
    'INFERRED'
)

UNREACHABLE['AppConfig.toast'] = (
    'no_trigger_in_app',
    'Static method not called by any reachable code',
    'SRC AppConfig.java:158-172, 182-191',
    'INFERRED'
)

UNREACHABLE['AppConfig$1.<init>'] = (
    'no_trigger_in_app',
    'Anonymous AsyncTask created in runInParallel but never executed',
    'SRC AppConfig.java:125-132',
    'INFERRED'
)

UNREACHABLE['AppConfig$1.doInBackground'] = (
    'no_trigger_in_app',
    'Called only if AppConfig.runInParallel is called',
    'SRC AppConfig.java:128',
    'INFERRED'
)

UNREACHABLE['AppConfig$1.onPostExecute'] = (
    'no_trigger_in_app',
    'Called only if AppConfig.runInParallel is called',
    'SRC AppConfig.java:131',
    'INFERRED'
)

UNREACHABLE['AppConfig$1.onPreExecute'] = (
    'no_trigger_in_app',
    'Called only if AppConfig.runInParallel is called',
    'SRC AppConfig.java:127',
    'INFERRED'
)

UNREACHABLE['AppConfig$CustomAsyncCallbacks.<init>'] = (
    'no_trigger_in_app',
    'Abstract class constructor, only called by subclasses when they are instantiated',
    'SRC AppConfig.java:138-141',
    'INFERRED'
)

UNREACHABLE['AppConfig$CustomAsyncCallbacks.onPostExecute'] = (
    'no_trigger_in_app',
    'Framework callback only executed if AsyncTask runs',
    'SRC AppConfig.java:146-147',
    'INFERRED'
)

UNREACHABLE['AppConfig$CustomAsyncCallbacks.onPreExecute'] = (
    'no_trigger_in_app',
    'Framework callback only executed if AsyncTask runs',
    'SRC AppConfig.java:148-149',
    'INFERRED'
)

UNREACHABLE['ApkImageModelLoaderFactory.teardown'] = (
    'no_trigger_in_app',
    'Glide lifecycle teardown, framework-driven cleanup',
    'SRC ApkImageModelLoaderFactory.java:28-30',
    'INFERRED'
)

UNREACHABLE['AppListLoader.onReleaseResources'] = (
    'closed_by_configuration',
    'Empty TODO method with no implementation',
    'SRC AppListLoader.java:163-171',
    'SOURCE'
)

UNREACHABLE['AppListLoader$AppsDataPair.<init>'] = (
    'framework_never_calls',
    'Called only when loadInBackground completes successfully',
    'SRC AppListLoader.java:52, 75',
    'INFERRED'
)

UNREACHABLE['AppHolder.<init>'] = (
    'no_trigger_in_app',
    'ViewHolder constructor called by RecyclerView framework when binding items, not reachable by app code',
    'SRC AppHolder.java:24-34',
    'INFERRED'
)

