STATUS: RUNNING 2026-10-27 21:07:10

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| CloudContract.<init> | UNREACHABLE | no_trigger_in_app | Constants class never instantiated | SRC grep shows no new CloudContract |
| CloudHandler.<init> | REACHABLE |  | Called from MainActivity.onCreate | SRC MainActivity.java:298 |
| CloudHandler.addEntry | REACHABLE |  | Called from CloudLoaderAsyncTask | SRC CloudLoaderAsyncTask.java:103 |
| CloudHandler.clear | REACHABLE |  | Called from MainActivity.deleteAccount | SRC MainActivity.java:1824 |
| CloudHandler.findEntry | REACHABLE |  | Called from CloudLoaderAsyncTask, MainActivity | SRC CloudLoaderAsyncTask.java:88,157,221,282; MainActivity.java:1796 |
| CloudHandler.getAllEntries | REACHABLE |  | Called from MainActivity.onPostCreate | SRC MainActivity.java:1863 |
| CloudHandler.onCreate | UNREACHABLE | framework_never_calls | SQLite onCreate only on first DB creation | SRC CloudHandler.java:48-70; INFERRED |
| CloudHandler.onUpgrade | UNREACHABLE | framework_never_calls | SQLite onUpgrade only when version increases | SRC CloudHandler.java:75-81; INFERRED |
| CloudHandler.updateEntry | REACHABLE |  | Called from CloudLoaderAsyncTask | SRC CloudLoaderAsyncTask.java:98 |
| CloudEntry.<init> | REACHABLE |  | No-arg constructor called from CloudHandler.findEntry | SRC CloudHandler.java:150 |
| CloudEntry.<init> | REACHABLE |  | Called from CloudLoaderAsyncTask | SRC CloudLoaderAsyncTask.java:98,103 |
| CloudEntry.getId | REACHABLE |  | Called from CloudHandler.updateEntry | SRC CloudHandler.java:124 |
| CloudEntry.getPersistData | REACHABLE |  | Called from CloudHandler.addEntry, updateEntry | SRC CloudHandler.java:91,128 |
| CloudEntry.getServiceType | REACHABLE |  | Called from CloudHandler.addEntry, updateEntry | SRC CloudHandler.java:87,125 |
| CloudEntry.setId | REACHABLE |  | Called from CloudHandler.findEntry, getAllEntries | SRC CloudHandler.java:151,187 |
| CloudEntry.setPersistData | REACHABLE |  | Called from CloudHandler.findEntry, getAllEntries | SRC CloudHandler.java:154,190 |
| CloudEntry.setServiceType | REACHABLE |  | Called from CloudHandler.findEntry, getAllEntries | SRC CloudHandler.java:152,188 |
| CLI$Mode.<clinit> | UNREACHABLE | no_trigger_in_app | CLI library tool never called | SRC grep shows no app call site |
| CLI$Mode.<init> | UNREACHABLE | no_trigger_in_app | Mode enum constructor only from CLI.main | SRC grep shows no app call site |
| CLI$Mode.getMessage | UNREACHABLE | no_trigger_in_app | Mode.getMessage only from CLI.main | SRC CLI.java:107 |
| CLI$Mode$1.<init> | UNREACHABLE | no_trigger_in_app | Mode$1 constructor only from enum init | SRC grep shows no app call site |
| CLI$Mode$1.getContentMethods | UNREACHABLE | no_trigger_in_app | getContentMethods helper for CLI.main | SRC CLI.java:43 |
| CLI$Mode$1.takeAction | UNREACHABLE | no_trigger_in_app | Mode$1.takeAction only from CLI.main | SRC CLI.java:120 |
| CLI$Mode$2.<init> | UNREACHABLE | no_trigger_in_app | Mode$2 constructor only from enum init | SRC grep shows no app call site |
| CLI$Mode$2.takeAction | UNREACHABLE | no_trigger_in_app | Mode$2.takeAction only from CLI.main | SRC CLI.java:120 |
| CheckableCircleView.<init> | REACHABLE |  | Inflated in ColorAdapter layout | SRC ColorAdapter.java:52 |
| CheckableCircleView.onDraw | REACHABLE |  | Framework calls after invalidate | SRC CheckableCircleView.java:31,36 invalidate |
| CheckableCircleView.setChecked | REACHABLE |  | Called from ColorAdapter.getView and onItemClick | SRC ColorAdapter.java:56,69 |
| CheckableCircleView.setColor | REACHABLE |  | Called from ColorAdapter.getView | SRC ColorAdapter.java:57 |
| CircleGradientDrawable.<init> | REACHABLE |  | Called from RecyclerAdapter, CompressedExplorerAdapter | SRC RecyclerAdapter.java:536,539; CompressedExplorerAdapter.java:204,207 |
| CircleGradientDrawable.<init> | REACHABLE |  | Base constructor called by other constructors | SRC CircleGradientDrawable.java:46; called from 29,42 |
| CircleGradientDrawable.<init> | REACHABLE |  | String color constructor, delegates to AppTheme constructor | SRC CircleGradientDrawable.java:29-31 |
| CircleGradientDrawable.dpToPx | REACHABLE |  | Called from constructor | SRC CircleGradientDrawable.java:51 |
| CircularColorsView.<init> | REACHABLE |  | Single-arg constructor calls init | SRC CircularColorsView.java:27 |
| CircularColorsView.<init> | REACHABLE |  | Inflated in ColorPickerDialog | SRC ColorPickerDialog.java:130 |
| CircularColorsView.init | REACHABLE |  | Called from constructors | SRC CircularColorsView.java:27,33 |
| CircularColorsView.onDraw | REACHABLE |  | Framework calls for drawing | SRC CircularColorsView.java:51,47 paint usage |
| CircularColorsView.setColors | REACHABLE |  | Called from ColorPickerDialog.onBindDialogView | SRC ColorPickerDialog.java:131 |
| CircularColorsView.setDividerColor | REACHABLE |  | Called from ColorPickerDialog.onBindDialogView | SRC ColorPickerDialog.java:132-133 |
| CheckBox.<init> | REACHABLE |  | Framework inflates from preference XML | SRC PrefFrag.java:102 |
| CheckBox.clearListenerInViewGroup | REACHABLE |  | Called from onBindView | SRC CheckBox.java:22 |
| CheckBox.onBindView | REACHABLE |  | Framework calls when binding preference | SRC CheckBox.java:19; INFERRED framework |
| CloudIconDataFetcher.<init> | REACHABLE |  | Called from CloudIconModelLoader.buildLoadData | SRC CloudIconModelLoader.java:30 |
| CloudIconDataFetcher.cancel | UNREACHABLE | no_trigger_in_app | Empty implementation, no effect | SRC CloudIconDataFetcher.java:58-60 |
| CloudIconDataFetcher.cleanup | REACHABLE |  | Glide calls after loadData | INFERRED Glide lifecycle |
| CloudIconDataFetcher.getDataClass | REACHABLE |  | Glide calls for type checking | INFERRED Glide contract |
| CloudIconDataFetcher.getDataSource | REACHABLE |  | Glide calls for caching decision | INFERRED Glide contract |
| CloudIconDataFetcher.loadData | REACHABLE |  | Glide calls to fetch cloud thumbnail | INFERRED Glide DataFetcher contract |
| CloudIconModelFactory.<init> | REACHABLE |  | Called from AmazeFileManagerModule | SRC AmazeFileManagerModule.java:22 |
| CloudIconModelFactory.build | REACHABLE |  | Glide calls to build ModelLoader | INFERRED Glide factory contract |
| CloudIconModelFactory.teardown | UNREACHABLE | framework_never_calls | Glide teardown only on explicit shutdown | SRC CloudIconModelFactory.java:29-30; INFERRED |
| CloudIconModelLoader.<init> | REACHABLE |  | Called from CloudIconModelFactory.build | SRC CloudIconModelFactory.java:24 |
| CloudIconModelLoader.buildLoadData | REACHABLE |  | Glide calls when loading cloud icons | INFERRED Glide ModelLoader contract |
| CloudIconModelLoader.handles | REACHABLE |  | Glide calls to check if loader handles path | INFERRED Glide ModelLoader contract |

STATUS: DONE 21:17
