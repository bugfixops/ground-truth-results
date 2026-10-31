STATUS: START 21:25

| Method | Label | Kind | Reason | Evidence |
|--------|-------|------|--------|----------|
| SimpleTextWatcher.afterTextChanged | REACHABLE | CALL | Anonymous subclasses override and framework calls via TextWatcher interface | SRC ui/dialogs/RenameBookmark.java:86-93, SmbConnectDialog.java:116/125/134/143, SftpConnectDialog.java:267, GeneralDialogCreation.java:770, FoldersPref.java:236/246, WarnableTextInputValidator.java:14 |
| SimpleTextWatcher.beforeTextChanged | UNREACHABLE | framework_never_calls | Empty implementation; no subclass overrides this method | SRC utils/SimpleTextWatcher.java:13-16 (all 8 anonymous subclasses only override afterTextChanged) |
| SimpleTextWatcher.onTextChanged | UNREACHABLE | framework_never_calls | Empty implementation; no subclass overrides this method | SRC utils/SimpleTextWatcher.java:18-21 (all 8 anonymous subclasses only override afterTextChanged) |
| FileUtils.openFile(DocumentFile,MainActivity,SharedPreferences) | REACHABLE | CALL | Called from FileUtils.openFile(File...) via openunknown | SRC utils/files/FileUtils.java:816-823 (openunknown(f, m, false, useNewStack)) |
| FileUtils.openunknown(DocumentFile,Context,boolean,boolean) | REACHABLE | CALL | Called by FileUtils.openFile(DocumentFile...) and openWith | SRC utils/files/FileUtils.java:455-479, called at :819 and :822 |
| FileUtils.scanFile(Context,HybridFile[]) | REACHABLE | CALL | Called by Operations$3.onPostExecute after rename | SRC filesystem/Operations.java:491-493 (FileUtils.scanFile(context, hybridFiles)) |
| ShareAdapter$ViewHolder.<init> | REACHABLE | CALL | Called by ShareAdapter.onCreateViewHolder | SRC utils/share/ShareAdapter.java:44-46 (return new ViewHolder(view)) |
| ShareAdapter$ViewHolder.lambda$render$0 | REACHABLE | CALL | Lambda OnClickListener in render method | SRC utils/share/ShareAdapter.java:72-76 (rootView.setOnClickListener(v -> {...})) |
| ShareAdapter$ViewHolder.render | REACHABLE | CALL | Called by ShareAdapter.onBindViewHolder | SRC utils/share/ShareAdapter.java:50-52 (holder.render(position)) |
| ShareTask.appInstalledOrNot | REACHABLE | CALL | Called by ShareTask.doInBackground to check bluetooth | SRC utils/share/ShareTask.java:98 (appInstalledOrNot("com.android.bluetooth", packageManager)) |
| ShareTask.doInBackground | REACHABLE | FRAMEWORK | AsyncTask.execute triggers doInBackground | SRC utils/files/FileUtils.java:373 (new ShareTask(...).execute(mime)) |
| ShareTask.onPostExecute | REACHABLE | FRAMEWORK | AsyncTask framework calls after doInBackground | SRC utils/share/ShareTask.java:117-130, FW-SRC android/os/AsyncTask.java lifecycle |
| RandomAccessStream.available | UNREACHABLE | framework_never_calls | Method throws IOException to prevent calls; javadoc says "Use availableExact()" | SRC utils/streams/RandomAccessStream.java:46-48 (throws IOException("Use availableExact()!")) |
| RandomAccessStream.availableExact | REACHABLE | CALL | Called by StreamSource and CloudStreamSource subclasses | SRC utils/streams/RandomAccessStream.java:37-39, inherited by subclasses |
| RandomAccessStream.markSupported | REACHABLE | CALL | Returns true; called via InputStream interface | SRC utils/streams/RandomAccessStream.java:34-36 (return true) |
| DatabaseViewerActivity.onBackPressed | REACHABLE | CALL | Called by onOptionsItemSelected for toolbar back button | SRC activities/DatabaseViewerActivity.java:206-211 (onOptionsItemSelected calls onBackPressed) |
| DatabaseViewerActivity.onOptionsItemSelected | REACHABLE | FRAMEWORK | Framework delivers menu item selections | SRC activities/DatabaseViewerActivity.java:206-212, FW-SRC Activity menu handling |
| TextEditorActivity$1.<init> | REACHABLE | CALL | Anonymous TimerTask created in onTextChanged | SRC activities/TextEditorActivity.java:430-437 (mTimer.schedule(new TimerTask() {...})) |
| TextEditorActivity$1.run | REACHABLE | FRAMEWORK | Timer framework calls TimerTask.run | SRC activities/TextEditorActivity.java:432-437, FW-SRC java/util/Timer.java |
| TextEditorActivity$2.<init> | REACHABLE | CALL | Anonymous AnimatorListener for showSearchView animation | SRC activities/TextEditorActivity.java:481-488 (animator.addListener(new AnimatorListenerAdapter() {...})) |
| TextEditorActivity$2.onAnimationEnd | REACHABLE | FRAMEWORK | Animation framework calls listener callback | SRC activities/TextEditorActivity.java:481-488, FW-SRC android/animation/AnimatorListenerAdapter.java |
| TextEditorActivity$3.<init> | REACHABLE | CALL | Anonymous AnimatorListener for hideSearchView animation | SRC activities/TextEditorActivity.java:518-526 (animator.addListener(new AnimatorListenerAdapter() {...})) |
| TextEditorActivity$3.onAnimationEnd | REACHABLE | FRAMEWORK | Animation framework calls listener callback | SRC activities/TextEditorActivity.java:518-526, FW-SRC android/animation/AnimatorListenerAdapter.java |
| AppDataParcelable$1.createFromParcel | REACHABLE | CALL | CREATOR.createFromParcel constructs from Parcel | SRC adapters/data/AppDataParcelable.java:57-60 (return new AppDataParcelable(in)) |
| AppDataParcelable$1.newArray | UNREACHABLE | framework_never_calls | Parcelable.Creator.newArray rarely called; app uses createFromParcel only | SRC adapters/data/AppDataParcelable.java:63-66 (no app usage found via grep) |
| RecyclerPreloadSizeProvider.getPreloadSize | REACHABLE | CALL | Glide ListPreloader calls getPreloadSize | SRC adapters/glide/RecyclerPreloadSizeProvider.java:56-59 (implements ListPreloader.PreloadSizeProvider) |
| RecyclerPreloadSizeProvider.lambda$addView$0 | REACHABLE | CALL | Lambda callback in addView creates SizeViewTarget | SRC adapters/glide/RecyclerPreloadSizeProvider.java:43 ((width, height) -> viewSizes.append(...)) |
| CryptHandler.onCreate | REACHABLE | FRAMEWORK | SQLiteOpenHelper framework calls onCreate on first database access | SRC database/CryptHandler.java:37-42 (db.execSQL(CREATE_TABLE_ENCRYPTED)), FW-SRC android/database/sqlite/SQLiteOpenHelper.java |
| CryptHandler.onUpgrade | REACHABLE | FRAMEWORK | SQLiteOpenHelper framework calls onUpgrade when version changes | SRC database/CryptHandler.java:45-49 (db.execSQL("DROP TABLE...")), FW-SRC android/database/sqlite/SQLiteOpenHelper.java |
| OperationData.<init>(Operation,String,String,String,String,String) | REACHABLE | CALL | UtilsHandler calls SFTP constructor | SRC database/models/OperationData.java:63-73 (constructor for Operation.SFTP) |
| OperationData.toString | REACHABLE | CALL | Debug/logging calls toString | SRC database/models/OperationData.java:75-87 (toString() method) |
| CustomFileObserver.onEvent | REACHABLE | FRAMEWORK | FileObserver framework calls onEvent for filesystem changes | SRC filesystem/CustomFileObserver.java:84-126, FW-SRC android/os/FileObserver.java (inotify) |
| CustomFileObserver.sendMessages | REACHABLE | CALL | Called by onEvent and CustomFileObserver$1.run | SRC filesystem/CustomFileObserver.java:121 and :126 (sendMessages() calls) |
| CustomFileObserver$1.<init> | REACHABLE | CALL | Anonymous TimerTask created in onEvent | SRC filesystem/CustomFileObserver.java:117-125 (new Timer().schedule(new TimerTask() {...})) |
| CustomFileObserver$1.run | REACHABLE | FRAMEWORK | Timer framework calls TimerTask.run | SRC filesystem/CustomFileObserver.java:117-125, FW-SRC java/util/Timer.java |
| CustomFileObserver$FileTimerTask.compare | REACHABLE | CALL | Called by FileTimerTask.run to detect file changes | SRC filesystem/CustomFileObserver.java:191-197 (compare(newFiles, files) and compare(files, newFiles)) |
| CustomFileObserver$FileTimerTask.run | REACHABLE | FRAMEWORK | ScheduledExecutorService calls Runnable.run | SRC filesystem/CustomFileObserver.java:165-167, FW-SRC java/util/concurrent/ScheduledExecutorService.java |
| Operations$3.doInBackground | REACHABLE | FRAMEWORK | AsyncTask.execute triggers doInBackground | SRC filesystem/Operations.java:335-488 (new AsyncTask<Void,Void,Void>() {...}.executeOnExecutor(...)) |
| Operations$3.onPostExecute | REACHABLE | FRAMEWORK | AsyncTask framework calls onPostExecute after doInBackground | SRC filesystem/Operations.java:486-493, FW-SRC android/os/AsyncTask.java |

STATUS: DONE 21:25
