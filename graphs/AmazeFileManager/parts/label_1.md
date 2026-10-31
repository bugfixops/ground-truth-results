STATUS: RUNNING 2026-10-27 20:52:57

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| GlideOptions.<init> | REACHABLE | | Generated class instantiated by Glide framework via GlideApp.with() chain | INFERRED: GlideApp.with() calls return GlideOptions per Glide framework pattern |
| GlideOptions.apply | REACHABLE | | Called on GlideRequest objects from AppsAdapterPreloadModel | SRC AppsAdapterPreloadModel.java:28 shows GlideApp.with(f).asDrawable().fitCenter() chain |
| GlideOptions.autoClone | REACHABLE | | Called by Glide framework during option chaining | INFERRED: Glide library internal method |
| GlideOptions.clone | REACHABLE | | Called explicitly in AppsAdapterPreloadModel.getPreloadRequestBuilder | SRC AppsAdapterPreloadModel.java:44 shows request.clone().load(item) |
| GlideOptions.lock | REACHABLE | | Called by Glide framework to finalize options | INFERRED: Glide library internal method |
| GlideRequest.addListener | REACHABLE | | Used in RecyclerAdapter for Glide load callbacks | SRC RecyclerAdapter.java has RequestListener implementations at lines 873-928 |
| GlideRequest.apply | REACHABLE | | Called to apply options on GlideRequest objects | INFERRED: part of Glide request building chain |
| GlideRequest.downsample | REACHABLE | | Called by Glide for image downsampling | INFERRED: Glide library transformation method |
| GlideRequest.listener | REACHABLE | | Used in RecyclerAdapter for image load callbacks | SRC RecyclerAdapter.java has RequestListener implementations |
| GlideRequest.optionalCenterInside | REACHABLE | | Glide transformation option | INFERRED: Glide transformation method |
| GlideRequest.optionalFitCenter | REACHABLE | | Glide transformation option | INFERRED: Glide transformation method |
| GlideRequest.set | REACHABLE | | Called to set Glide options | INFERRED: Glide option setter method |
| GlideRequest.transform(Transformation) | REACHABLE | | Glide transformation method | INFERRED: Glide transformation method |
| GlideRequests.as | REACHABLE | | Called by GlideApp.with().asDrawable() chain | SRC AppsAdapterPreloadModel.java:28, RecyclerPreloadModelProvider.java:30 show asDrawable() calls |
| GlideRequests.setRequestOptions | REACHABLE | | Sets default options on GlideRequests | INFERRED: Glide library method |
| GeneratedAppGlideModuleImpl.<init> | REACHABLE | | Instantiated by Glide annotation processor at build time | INFERRED: Glide-generated class instantiated by framework |
| GeneratedAppGlideModuleImpl.applyOptions | REACHABLE | | Called by Glide during initialization | INFERRED: Glide lifecycle method |
| GeneratedAppGlideModuleImpl.getExcludedModuleClasses | REACHABLE | | Called by Glide during module registration | INFERRED: Glide lifecycle method |
| GeneratedAppGlideModuleImpl.getRequestManagerFactory | REACHABLE | | Called by Glide to create request managers | INFERRED: Glide lifecycle method |
| GeneratedAppGlideModuleImpl.isManifestParsingEnabled | REACHABLE | | Called by Glide during initialization | INFERRED: Glide lifecycle method |
| GeneratedAppGlideModuleImpl.registerComponents | REACHABLE | | Called by Glide to register custom components | INFERRED: Glide lifecycle method |
| AppsAdapter.getView | REACHABLE | | ArrayAdapter lifecycle method called by ListView framework | SRC AppsAdapter.java:110-151 shows implementation, AppsListFragment.java:101 instantiates adapter |
| AppsAdapter.lambda$getView$0 | REACHABLE | | Lambda from getView onClick listener | SRC AppsAdapter.java:137-143 shows holder.rl.setOnClickListener lambda |
| AppsAdapter.lambda$null$1 | REACHABLE | | Lambda from showPopup menu item clicks | SRC AppsAdapter.java:169 shows popupMenu.setOnMenuItemClickListener lambda |
| AppsAdapter.lambda$null$2 | REACHABLE | | Lambda from showPopup menu item clicks | SRC AppsAdapter.java:169 shows popupMenu.setOnMenuItemClickListener lambda |
| AppsAdapter.lambda$null$3 | REACHABLE | | Lambda from showPopup menu item clicks | SRC AppsAdapter.java:169 shows popupMenu.setOnMenuItemClickListener lambda |
| AppsAdapter.lambda$showPopup$4 | REACHABLE | | Lambda from showPopup onClick | SRC AppsAdapter.java:167 shows v.setOnClickListener lambda |
| AppsAdapter.setData | REACHABLE | | Called from AppsListFragment.onLoadFinished | SRC AppsListFragment.java:182 shows adapter.setData(data.first) |
| AppsAdapter.showPopup | REACHABLE | | Called from getView | SRC AppsAdapter.java:128 shows showPopup(holder.about, rowItem) |
| AppsAdapterPreloadModel.getPreloadItems | REACHABLE | | ListPreloader.PreloadModelProvider interface method | SRC AppsAdapterPreloadModel.java:35-38, used in AppsListFragment.java:98 ListPreloader |
| AppsAdapterPreloadModel.loadApkImage | REACHABLE | | Called from AppsAdapter.getView | SRC AppsAdapter.java:124 shows modelProvider.loadApkImage(rowItem.path, holder.apkIcon) |
| AppsAdapterPreloadModel.setItemList | REACHABLE | | Called from AppsListFragment.onLoadFinished | SRC AppsListFragment.java:183 shows modelProvider.setItemList(data.second) |
| ColorAdapter.<init> | REACHABLE | | Constructor called to instantiate adapter | SRC shows public constructor, used in color preference dialogs |
| ColorAdapter.getColorResAt | REACHABLE | | Private method called from getView | SRC ColorAdapter.java:42,47 shows internal use |
| ColorAdapter.getView | REACHABLE | | ArrayAdapter lifecycle method | SRC ColorAdapter.java:44-57 shows implementation |
| ColorAdapter.onItemClick | REACHABLE | | OnItemClickListener interface method | SRC ColorAdapter.java:59-64 shows implementation |
| CompressedExplorerAdapter.<init> | REACHABLE | | Constructor called from CompressedExplorerFragment.createViews | SRC CompressedExplorerFragment.java:450 shows new CompressedExplorerAdapter |
| CompressedExplorerAdapter.animate | REACHABLE | | Called from onBindViewHolder | SRC CompressedExplorerAdapter.java shows animate(holder) call |
| CompressedExplorerAdapter.generateZip | REACHABLE | | Called to update adapter with new archive contents | SRC CompressedExplorerAdapter.java:139-145 shows method |
| CompressedExplorerAdapter.getCheckedItemPositions | REACHABLE | | Called from CompressedExplorerFragment ActionMode callback | SRC CompressedExplorerFragment.java shows usage in onPrepareActionMode |
| CompressedExplorerAdapter.getItemCount | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC CompressedExplorerAdapter.java shows override |
| CompressedExplorerAdapter.getItemId | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC CompressedExplorerAdapter.java:147-150 shows implementation |
| CompressedExplorerAdapter.getItemViewType | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC CompressedExplorerAdapter.java:152-157 shows implementation |
| CompressedExplorerAdapter.isPositionHeader | REACHABLE | | Called from getItemViewType | SRC CompressedExplorerAdapter.java:153 shows call |
| CompressedExplorerAdapter.lambda$onBindViewHolder$0 | REACHABLE | | Lambda from onBindViewHolder | SRC CompressedExplorerAdapter.java shows lambdas in onBindViewHolder |
| CompressedExplorerAdapter.lambda$onBindViewHolder$1 | REACHABLE | | Lambda from onBindViewHolder | SRC CompressedExplorerAdapter.java shows lambdas in onBindViewHolder |
| CompressedExplorerAdapter.lambda$onBindViewHolder$2 | REACHABLE | | Lambda from onBindViewHolder | SRC CompressedExplorerAdapter.java shows lambdas in onBindViewHolder |
| CompressedExplorerAdapter.onBindViewHolder | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC CompressedExplorerAdapter.java shows implementation |
| CompressedExplorerAdapter.onCreateViewHolder | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC CompressedExplorerAdapter.java:159-171 shows implementation |
| CompressedExplorerAdapter.onFailedToRecycleView | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC CompressedExplorerAdapter.java shows override |
| CompressedExplorerAdapter.onViewAttachedToWindow | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC CompressedExplorerAdapter.java shows override |
| CompressedExplorerAdapter.onViewDetachedFromWindow | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC CompressedExplorerAdapter.java shows override |
| CompressedExplorerAdapter.toggleChecked(int,ImageView) | REACHABLE | | Called from onBindViewHolder click listeners | SRC CompressedExplorerAdapter.java:102-129 shows implementation |
| CompressedExplorerAdapter.toggleChecked(boolean) | REACHABLE | | Called from CompressedExplorerFragment ActionMode | SRC CompressedExplorerAdapter.java:79-87 shows implementation |
| HiddenAdapter.getItemCount | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC HiddenAdapter.java shows implementation |
| HiddenAdapter.getItemId | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC HiddenAdapter.java shows implementation |
| HiddenAdapter.lambda$null$1 | REACHABLE | | Lambda from onBindViewHolder | SRC HiddenAdapter.java shows nested lambdas in deleteButton.setOnClickListener |
| HiddenAdapter.lambda$null$2 | REACHABLE | | Lambda from onBindViewHolder | SRC HiddenAdapter.java shows nested lambdas in row.setOnClickListener |
| HiddenAdapter.lambda$null$3 | REACHABLE | | Lambda from onBindViewHolder | SRC HiddenAdapter.java shows nested lambdas in row.setOnClickListener |
| HiddenAdapter.lambda$onBindViewHolder$0 | REACHABLE | | Lambda from onBindViewHolder | SRC HiddenAdapter.java:72 shows deleteButton.setOnClickListener lambda |
| HiddenAdapter.lambda$onBindViewHolder$4 | REACHABLE | | Lambda from onBindViewHolder | SRC HiddenAdapter.java:93 shows holder.row.setOnClickListener lambda |
| HiddenAdapter.onBindViewHolder | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC HiddenAdapter.java:66-112 shows implementation |
| HiddenAdapter.onCreateViewHolder | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC HiddenAdapter.java:58-64 shows implementation |
| RecyclerAdapter.addItem | REACHABLE | | Called to add items to adapter | SRC RecyclerAdapter.java shows method |
| RecyclerAdapter.areAllChecked | REACHABLE | | Called to check if all items selected | SRC RecyclerAdapter.java shows implementation |
| RecyclerAdapter.getCheckedItemsIndex | REACHABLE | | Called from MainFragment to get selected items | SRC RecyclerAdapter.java shows implementation |
| RecyclerAdapter.getCorrectView | REACHABLE | | RecyclerPreloadSizeProviderCallback interface method | SRC RecyclerAdapter.java implements interface |
| RecyclerAdapter.getItemId | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC RecyclerAdapter.java shows override |
| RecyclerAdapter.getItemViewType | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC RecyclerAdapter.java shows override |
| RecyclerAdapter.lambda$onBindViewHolder$0 | REACHABLE | | Lambda from onBindViewHolder | SRC RecyclerAdapter.java shows lambdas in onBindViewHolder |
| RecyclerAdapter.lambda$onBindViewHolder$1 | REACHABLE | | Lambda from onBindViewHolder | SRC RecyclerAdapter.java shows lambdas in onBindViewHolder |
| RecyclerAdapter.lambda$onBindViewHolder$2 | REACHABLE | | Lambda from onBindViewHolder | SRC RecyclerAdapter.java shows lambdas in onBindViewHolder |
| RecyclerAdapter.lambda$onBindViewHolder$3 | REACHABLE | | Lambda from onBindViewHolder | SRC RecyclerAdapter.java shows lambdas in onBindViewHolder |
| RecyclerAdapter.lambda$onBindViewHolder$4 | REACHABLE | | Lambda from onBindViewHolder | SRC RecyclerAdapter.java shows lambdas in onBindViewHolder |
| RecyclerAdapter.lambda$onBindViewHolder$5 | REACHABLE | | Lambda from onBindViewHolder | SRC RecyclerAdapter.java shows lambdas in onBindViewHolder |
| RecyclerAdapter.lambda$onBindViewHolder$6 | REACHABLE | | Lambda from onBindViewHolder | SRC RecyclerAdapter.java shows lambdas in onBindViewHolder |
| RecyclerAdapter.lambda$showPopup$7 | REACHABLE | | Lambda from showPopup | SRC RecyclerAdapter.java shows lambda in showPopup |
| RecyclerAdapter.onFailedToRecycleView | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC RecyclerAdapter.java shows override |
| RecyclerAdapter.onViewAttachedToWindow | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC RecyclerAdapter.java shows override |
| RecyclerAdapter.onViewDetachedFromWindow | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC RecyclerAdapter.java shows override |
| RecyclerAdapter.toggleChecked(boolean) | REACHABLE | | Called from MainFragment to select/deselect all | SRC RecyclerAdapter.java:246-261 shows implementation |
| RecyclerAdapter.toggleChecked(boolean,String) | REACHABLE | | Called from MainFragment to toggle selection | SRC RecyclerAdapter.java:220-242 shows implementation |
| RecyclerAdapter$1.lambda$onLoadFailed$0 | REACHABLE | | Lambda from RecyclerAdapter$1.onLoadFailed | SRC RecyclerAdapter.java shows lambda in RequestListener |
| RecyclerAdapter$1.onLoadFailed | REACHABLE | | RequestListener callback for Glide | SRC RecyclerAdapter.java shows RequestListener<Drawable> implementation |
| RecyclerAdapter$1.onResourceReady | REACHABLE | | RequestListener callback for Glide | SRC RecyclerAdapter.java shows RequestListener<Drawable> implementation |
| RecyclerAdapter$2.lambda$onLoadFailed$0 | REACHABLE | | Lambda from RecyclerAdapter$2.onLoadFailed | SRC RecyclerAdapter.java shows lambda in RequestListener |
| RecyclerAdapter$2.onLoadFailed | REACHABLE | | RequestListener callback for Glide | SRC RecyclerAdapter.java shows RequestListener<Drawable> implementation |
| RecyclerAdapter$2.onResourceReady | REACHABLE | | RequestListener callback for Glide | SRC RecyclerAdapter.java shows RequestListener<Drawable> implementation |
| RecyclerAdapter$ListItem.<init>(LayoutElementParcelable) | REACHABLE | | Constructor called in RecyclerAdapter.setItems | SRC RecyclerAdapter.java shows ListItem instantiation |
| RecyclerPreloadModelProvider.getPreloadItems | REACHABLE | | ListPreloader.PreloadModelProvider interface method | SRC RecyclerPreloadModelProvider.java:35-39 shows implementation |
| RecyclerPreloadSizeProvider.getPreloadSize | REACHABLE | | ListPreloader.PreloadSizeProvider interface method | SRC RecyclerPreloadSizeProvider.java:54-56 shows implementation |
| RecyclerPreloadSizeProvider.lambda$addView$0 | REACHABLE | | Lambda from addView method | SRC RecyclerPreloadSizeProvider.java:44 shows SizeViewTarget lambda |
| RecyclerPreloadSizeProvider$SizeViewTarget.onResourceReady | REACHABLE | | ViewTarget callback method | SRC RecyclerPreloadSizeProvider.java:71-74 shows implementation |
| CompressedItemViewHolder.<init> | REACHABLE | | Constructor called from CompressedExplorerAdapter.onCreateViewHolder | SRC CompressedItemViewHolder.java:26-40, CompressedExplorerAdapter.java:166,170 shows instantiation |
| CompressedHelperTask.<init> | REACHABLE | | Constructor called by subclasses | SRC CompressedHelperTask.java:43-46 shows constructor |
| CompressedHelperTask.doInBackground | REACHABLE | | AsyncTask lifecycle method | SRC CompressedHelperTask.java:48-62 shows implementation |
| CompressedHelperTask.onPostExecute | REACHABLE | | AsyncTask lifecycle method | SRC CompressedHelperTask.java:64-68 shows implementation |
| CompressedHelper.<init> | REACHABLE | | Abstract class constructor | SRC CompressedHelper.java shows abstract class |
| CompressedHelper.getExtractorInstance | REACHABLE | | Static factory method called from app code | SRC CompressedHelper.java:72-96 shows implementation |
| CompressedHelper.getFileName | REACHABLE | | Static utility method for archive names | SRC CompressedHelper.java:140-152 shows implementation |
| CompressedHelper.isEntryPathValid | REACHABLE | | Static utility method for path validation | SRC CompressedHelper.java:154-156 shows implementation |
| CompressedObjectParcelable.<clinit> | REACHABLE | | Static initializer for CREATOR | SRC CompressedObjectParcelable.java:100-108 shows CREATOR field |
| CompressedObjectParcelable.<init>() | REACHABLE | | Constructor for TYPE_GOBACK instances | SRC CompressedObjectParcelable.java:68-78 shows implementation |
| CompressedObjectParcelable.<init>(Parcel) | REACHABLE | | Parcelable constructor called by framework | SRC CompressedObjectParcelable.java:111-128 shows implementation |
| CompressedObjectParcelable.<init>(String,long,long,boolean) | REACHABLE | | Constructor for normal instances | SRC CompressedObjectParcelable.java:53-63 shows implementation |
| CompressedObjectParcelable.describeContents | REACHABLE | | Parcelable interface method | SRC CompressedObjectParcelable.java:80-83 shows implementation |
| CompressedObjectParcelable.equals | REACHABLE | | Object method override | SRC CompressedObjectParcelable.java:149-158 shows implementation |
| CompressedObjectParcelable.getNameForPath | REACHABLE | | Private method called from constructor | SRC CompressedObjectParcelable.java:139,59 shows call from constructor |
| CompressedObjectParcelable.writeToParcel | REACHABLE | | Parcelable interface method | SRC CompressedObjectParcelable.java:85-95 shows implementation |
| CompressedObjectParcelable$1.<init> | REACHABLE | | Creator instance initializer | SRC CompressedObjectParcelable.java:100 shows Creator instantiation |
| CompressedObjectParcelable$1.createFromParcel | REACHABLE | | Parcelable.Creator interface method | SRC CompressedObjectParcelable.java:102-104 shows implementation |
| CompressedObjectParcelable$1.newArray | REACHABLE | | Parcelable.Creator interface method | SRC CompressedObjectParcelable.java:106-108 shows implementation |
| CompressedObjectParcelable$Sorter.<init> | REACHABLE | | Constructor called when sorting archives | SRC CompressedObjectParcelable$Sorter.java:130 shows Comparator implementation |
| CompressedObjectParcelable$Sorter.compare | REACHABLE | | Comparator interface method | SRC CompressedObjectParcelable.java:132-140 shows implementation |
| AppsListFragment.onCreateLoader | REACHABLE | | LoaderManager.LoaderCallbacks interface method | SRC AppsListFragment.java:175-177 shows implementation |
| AppsListFragment.onLoadFinished | REACHABLE | | LoaderManager.LoaderCallbacks interface method | SRC AppsListFragment.java:179-191 shows implementation |
| AppsListFragment.onLoaderReset | REACHABLE | | LoaderManager.LoaderCallbacks interface method | SRC AppsListFragment.java:193-195 shows implementation |
| AppsListFragment.onSaveInstanceState | REACHABLE | | Fragment lifecycle method | SRC AppsListFragment.java:124-132 shows implementation |
| AppsListFragment.unin | REACHABLE | | Called from AppsAdapter when uninstalling app | SRC AppsAdapter.java shows app.unin() call in popup menu |
| CloudSheetFragment.<init> | REACHABLE | | Constructor called when fragment instantiated | SRC MainActivity.java:1953 shows new CloudSheetFragment() |
| CloudSheetFragment.onClick | REACHABLE | | View.OnClickListener interface method | SRC CloudSheetFragment.java:88,89,90,91,92,93 shows setOnClickListener(this) |
| CloudSheetFragment.onCreate | REACHABLE | | Fragment lifecycle method | SRC CloudSheetFragment.java:43-46 shows implementation |
| CloudSheetFragment.setupDialog | REACHABLE | | BottomSheetDialogFragment lifecycle method | SRC CloudSheetFragment.java:48-93 shows implementation |
| CompressedExplorerFragment.archiveCorruptOrUnsupportedToast | REACHABLE | | Called when archive open fails | SRC CompressedExplorerFragment.java shows error handling |
| CompressedExplorerFragment.canGoBack | REACHABLE | | Called to check if can navigate up | SRC CompressedExplorerFragment.java shows implementation |
| CompressedExplorerFragment.changePath | REACHABLE | | Called to navigate in archive | SRC CompressedExplorerFragment.java:225 shows called from onActivityCreated |
| CompressedExplorerFragment.createViews | REACHABLE | | Called to create adapter and setup views | SRC CompressedExplorerFragment.java shows implementation |
| CompressedExplorerFragment.goBack | REACHABLE | | Called to navigate up in archive | SRC CompressedExplorerFragment.java shows implementation |
| CompressedExplorerFragment.lambda$changePath$2 | REACHABLE | | Lambda from changePath | SRC CompressedExplorerFragment.java shows lambda in changePath |
| CompressedExplorerFragment.lambda$createViews$3 | REACHABLE | | Lambda from createViews | SRC CompressedExplorerFragment.java shows lambda in createViews |
| CompressedExplorerFragment.lambda$onActivityCreated$1 | REACHABLE | | Lambda from onActivityCreated | SRC CompressedExplorerFragment.java shows lambda in onActivityCreated |
| CompressedExplorerFragment.lambda$onCreateView$0 | REACHABLE | | Lambda from onCreateView | SRC CompressedExplorerFragment.java shows lambda in onCreateView |
| CompressedExplorerFragment.onActivityCreated | REACHABLE | | Fragment lifecycle method | SRC CompressedExplorerFragment.java:160-228 shows implementation |
| CompressedExplorerFragment.onCreate | REACHABLE | | Fragment lifecycle method | SRC CompressedExplorerFragment.java:135-138 shows implementation |
| CompressedExplorerFragment.onCreateView | REACHABLE | | Fragment lifecycle method | SRC CompressedExplorerFragment.java:140-158 shows implementation |
| CompressedExplorerFragment.onDestroyView | REACHABLE | | Fragment lifecycle method | SRC CompressedExplorerFragment.java shows implementation |
| CompressedExplorerFragment.onPause | REACHABLE | | Fragment lifecycle method | SRC CompressedExplorerFragment.java shows implementation |
| CompressedExplorerFragment.onRestoreInstanceState | REACHABLE | | Called from onActivityCreated to restore state | SRC CompressedExplorerFragment.java:237-245 shows implementation |
| CompressedExplorerFragment.onResume | REACHABLE | | Fragment lifecycle method | SRC CompressedExplorerFragment.java shows implementation |
| CompressedExplorerFragment.onSaveInstanceState | REACHABLE | | Fragment lifecycle method | SRC CompressedExplorerFragment.java:230-238 shows implementation |
| CompressedExplorerFragment.refresh | REACHABLE | | Called to refresh archive contents | SRC CompressedExplorerFragment.java shows implementation |
| CompressedExplorerFragment.stopAnim | REACHABLE | | Called to stop animations | SRC CompressedExplorerFragment.java:151-157 shows implementation |
| CompressedExplorerFragment.updateBottomBar | REACHABLE | | Called to update UI bottom bar | SRC CompressedExplorerFragment.java shows implementation |
| CompressedExplorerFragment$1.hideOption | REACHABLE | | Called from ActionMode.Callback methods | SRC CompressedExplorerFragment.java shows hideOption calls |
| CompressedExplorerFragment$1.onActionItemClicked | REACHABLE | | ActionMode.Callback interface method | SRC CompressedExplorerFragment.java shows implementation |
| CompressedExplorerFragment$1.onCreateActionMode | REACHABLE | | ActionMode.Callback interface method | SRC CompressedExplorerFragment.java shows implementation |
| CompressedExplorerFragment$1.onDestroyActionMode | REACHABLE | | ActionMode.Callback interface method | SRC CompressedExplorerFragment.java shows implementation |
| CompressedExplorerFragment$1.onPrepareActionMode | REACHABLE | | ActionMode.Callback interface method | SRC CompressedExplorerFragment.java shows implementation |
| CompressedExplorerFragment$1.showOption | REACHABLE | | Called from ActionMode.Callback methods | SRC CompressedExplorerFragment.java shows showOption calls |
| CompressedExplorerFragment$2.onServiceConnected | REACHABLE | | ServiceConnection interface method | SRC CompressedExplorerFragment.java shows ServiceConnection implementation |
| CompressedExplorerFragment$2.onServiceDisconnected | REACHABLE | | ServiceConnection interface method | SRC CompressedExplorerFragment.java shows ServiceConnection implementation |
| DbViewerFragment.<init> | REACHABLE | | Constructor called when fragment instantiated | SRC DatabaseViewerActivity.java:135 shows new DbViewerFragment() |
| DbViewerFragment.onActivityCreated | REACHABLE | | Fragment lifecycle method | SRC DbViewerFragment.java:50-61 shows implementation |
| DbViewerFragment.onCreateView | REACHABLE | | Fragment lifecycle method | SRC DbViewerFragment.java:32-48 shows implementation |
| DbViewerFragment.onDetach | REACHABLE | | Fragment lifecycle method | SRC DbViewerFragment.java:63-68 shows implementation |
| FtpServerFragment.changeFTPServerPath | REACHABLE | | Called to change FTP server path | SRC FtpServerFragment.java shows method |
| FtpServerFragment.changeFTPServerPort | REACHABLE | | Called to change FTP server port | SRC FtpServerFragment.java shows method |
| FtpServerFragment.getDefaultPathFromPreferences | REACHABLE | | Called to get FTP server path | SRC FtpServerFragment.java shows method |
| FtpServerFragment.getDefaultPortFromPreferences | REACHABLE | | Called to get FTP server port | SRC FtpServerFragment.java:163 shows usage in onOptionsItemSelected |
| FtpServerFragment.getFTPAddressString | REACHABLE | | Called to get FTP server address | SRC FtpServerFragment.java shows method |
| FtpServerFragment.getFTPTimeout | REACHABLE | | Called to get FTP timeout | SRC FtpServerFragment.java shows method |
| FtpServerFragment.getPasswordFromPreferences | REACHABLE | | Called to get FTP password | SRC FtpServerFragment.java shows method |
| FtpServerFragment.getSecurePreference | REACHABLE | | Called to get secure preference | SRC FtpServerFragment.java shows method |
| FtpServerFragment.getUsernameFromPreferences | REACHABLE | | Called to get FTP username | SRC FtpServerFragment.java shows method |
| FtpServerFragment.initLoginDialogViews | REACHABLE | | Called to init login dialog | SRC FtpServerFragment.java shows method |
| FtpServerFragment.lambda$initLoginDialogViews$8 | REACHABLE | | Lambda from initLoginDialogViews | SRC FtpServerFragment.java shows lambda |
| FtpServerFragment.lambda$onCreateView$0 | REACHABLE | | Lambda from onCreateView | SRC FtpServerFragment.java:138-146 shows ftpBtn.setOnClickListener lambda |
| FtpServerFragment.lambda$onOptionsItemSelected$1 | REACHABLE | | Lambda from onOptionsItemSelected | SRC FtpServerFragment.java shows lambda in MaterialDialog |
| FtpServerFragment.lambda$onOptionsItemSelected$2 | REACHABLE | | Lambda from onOptionsItemSelected | SRC FtpServerFragment.java shows lambda in MaterialDialog |
| FtpServerFragment.lambda$onOptionsItemSelected$3 | REACHABLE | | Lambda from onOptionsItemSelected | SRC FtpServerFragment.java shows lambda in MaterialDialog |
| FtpServerFragment.lambda$onOptionsItemSelected$4 | REACHABLE | | Lambda from onOptionsItemSelected | SRC FtpServerFragment.java shows lambda in MaterialDialog |
| FtpServerFragment.lambda$onOptionsItemSelected$5 | REACHABLE | | Lambda from onOptionsItemSelected | SRC FtpServerFragment.java shows lambda in MaterialDialog |
| FtpServerFragment.lambda$onOptionsItemSelected$6 | REACHABLE | | Lambda from onOptionsItemSelected | SRC FtpServerFragment.java shows lambda in MaterialDialog |
| FtpServerFragment.lambda$updateStatus$7 | REACHABLE | | Lambda from updateStatus | SRC FtpServerFragment.java shows lambda |
| FtpServerFragment.onActivityCreated | REACHABLE | | Fragment lifecycle method | SRC FtpServerFragment.java:149-162 shows implementation |
| FtpServerFragment.onCreateOptionsMenu | REACHABLE | | Fragment lifecycle method | SRC FtpServerFragment.java shows implementation |
| FtpServerFragment.onCreateView | REACHABLE | | Fragment lifecycle method | SRC FtpServerFragment.java:111-148 shows implementation |
| FtpServerFragment.onFtpReceiveActions | REACHABLE | | Called from broadcast receiver | SRC FtpServerFragment$1.java shows call |
| FtpServerFragment.onOptionsItemSelected | REACHABLE | | Fragment lifecycle method | SRC FtpServerFragment.java shows implementation |
| FtpServerFragment.onPause | REACHABLE | | Fragment lifecycle method | SRC FtpServerFragment.java shows implementation |
| FtpServerFragment.onResume | REACHABLE | | Fragment lifecycle method | SRC FtpServerFragment.java shows implementation |
| FtpServerFragment.setFTPPassword | REACHABLE | | Called to set FTP password | SRC FtpServerFragment.java shows method |
| FtpServerFragment.setFTPTimeout | REACHABLE | | Called to set FTP timeout | SRC FtpServerFragment.java shows method |
| FtpServerFragment.setFTPUsername | REACHABLE | | Called to set FTP username | SRC FtpServerFragment.java shows method |
| FtpServerFragment.setSecurePreference | REACHABLE | | Called to set secure preference | SRC FtpServerFragment.java shows method |
| FtpServerFragment.startServer | REACHABLE | | Called to start FTP server | SRC FtpServerFragment.java:142 shows startServer() call from lambda |
| FtpServerFragment.stopServer | REACHABLE | | Called to stop FTP server | SRC FtpServerFragment.java:144 shows stopServer() call from lambda |
| FtpServerFragment.updateSpans | REACHABLE | | Called to update UI spans | SRC FtpServerFragment.java shows method |
| FtpServerFragment.updateStatus | REACHABLE | | Called to update FTP status display | SRC FtpServerFragment.java:119 shows call from onCreateView |
| FtpServerFragment$1.onReceive | REACHABLE | | BroadcastReceiver callback method | SRC FtpServerFragment.java shows BroadcastReceiver implementation |
| MainFragment.addSearchResult | REACHABLE | | Called to add search result | SRC MainFragment.java shows method, called from SearchWorkerFragment callbacks |
| MainFragment.addShortcut | REACHABLE | | Called to add shortcut | SRC MainFragment.java shows method |
| MainFragment.addTo | REACHABLE | | Called to add bookmark | SRC MainFragment.java shows method |
| MainFragment.addToSmb | REACHABLE | | Called to add SMB connection | SRC MainFragment.java shows method |
| MainFragment.changePath | REACHABLE | | Called to navigate to path | SRC MainFragment.java shows method |
| MainFragment.computeScroll | REACHABLE | | Called to compute scroll position | SRC MainFragment.java shows method |
| MainFragment.findEncryptedEntry | REACHABLE | | Called to find encrypted entry | SRC MainFragment.java shows method |
| MainFragment.getElementsList | REACHABLE | | Called to get elements list | SRC MainFragment.java shows method |
| MainFragment.goBack | REACHABLE | | Called to navigate back | SRC MainFragment.java shows method |
| MainFragment.goBackItemClick | REACHABLE | | Called when go-back item clicked | SRC MainFragment.java shows method |
| MainFragment.hide | REACHABLE | | Called to hide files | SRC MainFragment.java shows method |
| MainFragment.lambda$initNoFileLayout$4 | REACHABLE | | Lambda from initNoFileLayout | SRC MainFragment.java shows lambda |
| MainFragment.lambda$loadlist$3 | REACHABLE | | Lambda from loadlist | SRC MainFragment.java shows lambda |
| MainFragment.lambda$onCreateView$0 | REACHABLE | | Lambda from onCreateView | SRC MainFragment.java shows lambda |
| MainFragment.lambda$onCreateView$1 | REACHABLE | | Lambda from onCreateView | SRC MainFragment.java shows lambda |
| MainFragment.lambda$onCreateView$2 | REACHABLE | | Lambda from onCreateView | SRC MainFragment.java shows lambda |
| MainFragment.lambda$reauthenticateSmb$10 | REACHABLE | | Lambda from reauthenticateSmb | SRC MainFragment.java shows lambda |
| MainFragment.lambda$reloadListElements$5 | REACHABLE | | Lambda from reloadListElements | SRC MainFragment.java shows lambda |
| MainFragment.lambda$reloadListElements$6 | REACHABLE | | Lambda from reloadListElements | SRC MainFragment.java shows lambda |
| MainFragment.lambda$rename$7 | REACHABLE | | Lambda from rename | SRC MainFragment.java shows lambda |
| MainFragment.lambda$rename$8 | REACHABLE | | Lambda from rename | SRC MainFragment.java shows lambda |
| MainFragment.lambda$rename$9 | REACHABLE | | Lambda from rename | SRC MainFragment.java shows lambda |
| MainFragment.launchSMB | REACHABLE | | Called to launch SMB connection | SRC MainFragment.java shows method |
| MainFragment.onDestroy | REACHABLE | | Fragment lifecycle method | SRC MainFragment.java shows implementation |
| MainFragment.onDetach | REACHABLE | | Fragment lifecycle method | SRC MainFragment.java shows implementation |
| MainFragment.onListItemClicked | REACHABLE | | Called when list item clicked | SRC MainFragment.java shows method |
| MainFragment.onPause | REACHABLE | | Fragment lifecycle method | SRC MainFragment.java shows implementation |
| MainFragment.onResume | REACHABLE | | Fragment lifecycle method | SRC MainFragment.java shows implementation |
| MainFragment.onSaveInstanceState | REACHABLE | | Fragment lifecycle method | SRC MainFragment.java shows implementation |
| MainFragment.onSearchCompleted | REACHABLE | | SearchWorkerFragment.HelperCallbacks interface method | SRC MainFragment.java shows implementation |
| MainFragment.onSearchPreExecute | REACHABLE | | SearchWorkerFragment.HelperCallbacks interface method | SRC MainFragment.java shows implementation |
| MainFragment.onStop | REACHABLE | | Fragment lifecycle method | SRC MainFragment.java shows implementation |
| MainFragment.reauthenticateSmb | REACHABLE | | Called to reauthenticate SMB | SRC MainFragment.java shows method |
| MainFragment.rename | REACHABLE | | Called to rename file | SRC MainFragment.java shows method |
| MainFragment.returnIntentResults | REACHABLE | | Called to return intent results | SRC MainFragment.java shows method |
| MainFragment.setListElements | REACHABLE | | Called to set list elements | SRC MainFragment.java shows method |
| MainFragment.updateList | REACHABLE | | Called to update list | SRC MainFragment.java shows method |
| MainFragment.updateTabWithDb | REACHABLE | | Called to update tab with database | SRC MainFragment.java shows method |
| MainFragment$1.onGlobalLayout | REACHABLE | | ViewTreeObserver.OnGlobalLayoutListener callback | SRC MainFragment.java shows implementation |
| MainFragment$2.getSpanSize | REACHABLE | | GridLayoutManager.SpanSizeLookup callback | SRC MainFragment.java shows implementation |
| MainFragment$3.hideOption | REACHABLE | | Called from ActionMode.Callback methods | SRC MainFragment.java shows hideOption calls |
| MainFragment$3.initMenu | REACHABLE | | Called from ActionMode.Callback | SRC MainFragment.java shows initMenu call |
| MainFragment$3.onActionItemClicked | REACHABLE | | ActionMode.Callback interface method | SRC MainFragment.java shows implementation |
| MainFragment$3.onCreateActionMode | REACHABLE | | ActionMode.Callback interface method | SRC MainFragment.java shows implementation |
| MainFragment$3.onDestroyActionMode | REACHABLE | | ActionMode.Callback interface method | SRC MainFragment.java shows implementation |
| MainFragment$3.onPrepareActionMode | REACHABLE | | ActionMode.Callback interface method | SRC MainFragment.java shows implementation |
| MainFragment$3.showOption | REACHABLE | | Called from ActionMode.Callback methods | SRC MainFragment.java shows showOption calls |
| MainFragment$4.onReceive | REACHABLE | | BroadcastReceiver callback method | SRC MainFragment.java shows BroadcastReceiver implementation |
| MainFragment$4$1.<init> | REACHABLE | | MediaScannerConnection.MediaScannerConnectionClient constructor | SRC MainFragment.java shows inner class instantiation |
| MainFragment$4$1.onMediaScannerConnected | REACHABLE | | MediaScannerConnection.MediaScannerConnectionClient callback | SRC MainFragment.java shows implementation |
| MainFragment$4$1.onScanCompleted | REACHABLE | | MediaScannerConnection.MediaScannerConnectionClient callback | SRC MainFragment.java shows implementation |
| MainFragment$5.onReceive | REACHABLE | | BroadcastReceiver callback method | SRC MainFragment.java shows BroadcastReceiver implementation |
| MainFragment$6.<init> | REACHABLE | | AsyncTask constructor | SRC MainFragment.java shows AsyncTask inner class |
| MainFragment$6.doInBackground | REACHABLE | | AsyncTask lifecycle method | SRC MainFragment.java shows implementation |
| MainFragment$6.onPostExecute | REACHABLE | | AsyncTask lifecycle method | SRC MainFragment.java shows implementation |
| MainFragment$7.<init> | REACHABLE | | Runnable constructor | SRC MainFragment.java shows Runnable inner class |
| MainFragment$7.lambda$run$0 | REACHABLE | | Lambda from run method | SRC MainFragment.java shows lambda |
| MainFragment$7.run | REACHABLE | | Runnable interface method | SRC MainFragment.java shows implementation |
| ProcessViewerFragment.addEntry | REACHABLE | | Called to add chart entry | SRC ProcessViewerFragment.java shows method |
| ProcessViewerFragment.cancelBroadcast | REACHABLE | | Called to cancel broadcast | SRC ProcessViewerFragment.java shows method |
| ProcessViewerFragment.chartInit | REACHABLE | | Called to initialize chart | SRC ProcessViewerFragment.java shows method |
| ProcessViewerFragment.createDataSet | REACHABLE | | Called to create chart dataset | SRC ProcessViewerFragment.java shows method |
| ProcessViewerFragment.lambda$cancelBroadcast$0 | REACHABLE | | Lambda from cancelBroadcast | SRC ProcessViewerFragment.java shows lambda |
| ProcessViewerFragment.onActivityCreated | REACHABLE | | Fragment lifecycle method | SRC ProcessViewerFragment.java shows implementation |
| ProcessViewerFragment.onCreateView | REACHABLE | | Fragment lifecycle method | SRC ProcessViewerFragment.java:70-125 shows implementation |
| ProcessViewerFragment.onPause | REACHABLE | | Fragment lifecycle method | SRC ProcessViewerFragment.java shows implementation |
| ProcessViewerFragment.onResume | REACHABLE | | Fragment lifecycle method | SRC ProcessViewerFragment.java:141-156 shows implementation |
| ProcessViewerFragment.processResults | REACHABLE | | Called to process service results | SRC ProcessViewerFragment.java:158 shows method |
| ProcessViewerFragment.setupDrawables | REACHABLE | | Called to setup drawable icons | SRC ProcessViewerFragment.java shows method |
| ProcessViewerFragment$CustomServiceConnection.<init> | REACHABLE | | ServiceConnection constructor | SRC ProcessViewerFragment.java:123 shows instantiation |
| ProcessViewerFragment$CustomServiceConnection.onServiceConnected | REACHABLE | | ServiceConnection interface method | SRC ProcessViewerFragment.java shows implementation |
| ProcessViewerFragment$CustomServiceConnection.onServiceDisconnected | REACHABLE | | ServiceConnection interface method | SRC ProcessViewerFragment.java shows implementation |
| ProcessViewerFragment$CustomServiceConnection$1.<init> | REACHABLE | | ProgressListener constructor | SRC ProcessViewerFragment.java shows inner class instantiation |
| ProcessViewerFragment$CustomServiceConnection$1.lambda$onUpdate$0 | REACHABLE | | Lambda from onUpdate | SRC ProcessViewerFragment.java shows lambda |
| ProcessViewerFragment$CustomServiceConnection$1.onUpdate | REACHABLE | | ProgressListener callback method | SRC ProcessViewerFragment.java shows implementation |
| ProcessViewerFragment$CustomServiceConnection$1.refresh | REACHABLE | | ProgressListener callback method | SRC ProcessViewerFragment.java shows implementation |
| SearchWorkerFragment.<init> | REACHABLE | | Constructor called when fragment instantiated | SRC MainFragment.java:1322, MainActivityHelper.java:607 shows new SearchWorkerFragment() |
| SearchWorkerFragment.onAttach | REACHABLE | | Fragment lifecycle method | SRC SearchWorkerFragment.java:39-44 shows implementation |
| SearchWorkerFragment.onCreate | REACHABLE | | Fragment lifecycle method | SRC SearchWorkerFragment.java:46-61 shows implementation |
| SearchWorkerFragment.onDetach | REACHABLE | | Fragment lifecycle method | SRC SearchWorkerFragment.java:63-68 shows implementation |
| ShareAdapter.<init> | REACHABLE | | Constructor called from ShareTask | SRC ShareAdapter.java:34-40 shows constructor |
| ShareAdapter.getItemCount | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC ShareAdapter.java:86-89 shows implementation |
| ShareAdapter.getItemId | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC ShareAdapter.java:82-85 shows implementation |
| ShareAdapter.onBindViewHolder | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC ShareAdapter.java:48-51 shows implementation |
| ShareAdapter.onCreateViewHolder | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC ShareAdapter.java:42-46 shows implementation |
| ShareAdapter.updateMatDialog | REACHABLE | | Called to update dialog reference | SRC ShareAdapter.java:28-30 shows implementation |
| ShareAdapter$ViewHolder.<init> | REACHABLE | | ViewHolder constructor called from onCreateViewHolder | SRC ShareAdapter.java:47 shows new ViewHolder(view) |
| ShareAdapter$ViewHolder.lambda$render$0 | REACHABLE | | Lambda from render method | SRC ShareAdapter.java:72 shows rootView.setOnClickListener lambda |
| ShareAdapter$ViewHolder.render | REACHABLE | | Called from onBindViewHolder | SRC ShareAdapter.java:50 shows holder.render(position) |
| SmbSearchDialog$ListViewAdapter.<init> | REACHABLE | | Constructor called from SmbSearchDialog | SRC SmbSearchDialog.java shows ListViewAdapter instantiation |
| SmbSearchDialog$ListViewAdapter.getItemCount | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC SmbSearchDialog.java shows implementation |
| SmbSearchDialog$ListViewAdapter.getItemId | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC SmbSearchDialog.java shows implementation |
| SmbSearchDialog$ListViewAdapter.getItemViewType | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC SmbSearchDialog.java shows implementation |
| SmbSearchDialog$ListViewAdapter.lambda$onBindViewHolder$0 | REACHABLE | | Lambda from onBindViewHolder | SRC SmbSearchDialog.java shows lambda |
| SmbSearchDialog$ListViewAdapter.onBindViewHolder | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC SmbSearchDialog.java shows implementation |
| SmbSearchDialog$ListViewAdapter.onCreateViewHolder | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC SmbSearchDialog.java shows implementation |
| TabFragment.getFragmentAtIndex | REACHABLE | | Called to get fragment at index | SRC TabFragment.java:344-347 shows implementation |
| TabFragment.onDestroyView | REACHABLE | | Fragment lifecycle method | SRC TabFragment.java:187-196 shows implementation |
| TabFragment.onPageScrollStateChanged | REACHABLE | | ViewPager.OnPageChangeListener callback | SRC TabFragment.java:266-268 shows implementation |
| TabFragment.onPageScrolled | REACHABLE | | ViewPager.OnPageChangeListener callback | SRC TabFragment.java:242-249 shows implementation |
| TabFragment.onPageSelected | REACHABLE | | ViewPager.OnPageChangeListener callback | SRC TabFragment.java:251-264 shows implementation |
| TabFragment.onSaveInstanceState | REACHABLE | | Fragment lifecycle method | SRC TabFragment.java:295-307 shows implementation |
| TabFragment.parsePathForName | REACHABLE | | Called to parse path to name | SRC TabFragment.java:217-228 shows implementation |
| TabFragment.parseSmbPath | REACHABLE | | Called to parse SMB path | SRC TabFragment.java:211-215 shows implementation |
| TabFragment$ScreenSlidePagerAdapter.getCount | REACHABLE | | FragmentStatePagerAdapter method | SRC TabFragment.java:277-280 shows implementation |
| TabFragment$ScreenSlidePagerAdapter.getItem | REACHABLE | | FragmentStatePagerAdapter method | SRC TabFragment.java:286-290 shows implementation |
| TabFragment$ScreenSlidePagerAdapter.getItemPosition | REACHABLE | | FragmentStatePagerAdapter method | SRC TabFragment.java:270-276 shows implementation |

STATUS: DONE
