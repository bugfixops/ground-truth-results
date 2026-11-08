STATUS: START 21:23
STATUS: DONE 21:29

| Method | Label | Kind | Reason | Evidence |
|--------|-------|------|--------|----------|
| RecyclerAdapter$2.lambda$onLoadFailed$0 | REACHABLE | CALL | Lambda created in onLoadFailed for UI thread update | RecyclerAdapter.java:925 |
| RecyclerAdapter$2.onLoadFailed | REACHABLE | FRAMEWORK | Glide RequestListener callback on image load failure | RecyclerAdapter.java:924 |
| RecyclerAdapter$2.onResourceReady | REACHABLE | FRAMEWORK | Glide RequestListener callback on image load success | RecyclerAdapter.java:934 |
| AppDataParcelable.describeContents | REACHABLE | FRAMEWORK | Android Parcelable contract method | AppDataParcelable.java:26-28 |
| AppDataParcelable.writeToParcel | REACHABLE | FRAMEWORK | Android Parcelable serialization | AppDataParcelable.java:31-38 |
| IconDataParcelable.setImageBroken | UNREACHABLE | no_trigger_in_app | Setter never called from app code | GREP no calls |
| PemToKeyPairTask$1.<init> | REACHABLE | CALL | PasswordFinder created when password required | PemToKeyPairTask.java:169 |
| PemToKeyPairTask$1.reqPassword | REACHABLE | FRAMEWORK | SSHJ PasswordFinder interface callback | PemToKeyPairTask.java:171-173 |
| PemToKeyPairTask$1.shouldRetry | REACHABLE | FRAMEWORK | SSHJ PasswordFinder interface callback | PemToKeyPairTask.java:175-177 |
| ZipService.onBind | REACHABLE | LIFECYCLE | Service bound from ProcessViewerFragment | ProcessViewerFragment.java:165 |
| ZipService.onDestroy | REACHABLE | LIFECYCLE | Service lifecycle cleanup method | ZipService.java:318-320 |
| ZipService.setProgressListener | REACHABLE | CALL | ProcessViewerFragment sets progress listener | ProcessViewerFragment.java:416 |
| SortHandler.getAllEntries | REACHABLE | CALL | Query all sort preferences from database | SortHandler.java:109-131 |
| SortHandler.onCreate | REACHABLE | LIFECYCLE | SQLiteOpenHelper creates database tables | SortHandler.java:47-51 |
| SortHandler.onUpgrade | REACHABLE | LIFECYCLE | SQLiteOpenHelper upgrades database schema | SortHandler.java:54-56 |
| TabHandler.onCreate | REACHABLE | LIFECYCLE | SQLiteOpenHelper creates database tables | TabHandler.java:57-81 |
| TabHandler.onDowngrade | REACHABLE | LIFECYCLE | SQLiteOpenHelper downgrades database | TabHandler.java:89-91 |
| TabHandler.onUpgrade | REACHABLE | LIFECYCLE | SQLiteOpenHelper upgrades database schema | TabHandler.java:84-86 |
| StreamNotFoundException.<init>(String) | UNREACHABLE | no_trigger_in_app | Constructor overload not used by app | WriteFileAbstraction.java:65,88 |
| StreamNotFoundException.<init>(String,Throwable) | UNREACHABLE | no_trigger_in_app | Constructor overload not used by app | StreamNotFoundException.java:11 |
| StreamNotFoundException.<init>(Throwable) | UNREACHABLE | no_trigger_in_app | Constructor overload not used by app | WriteFileAbstraction.java |
| HybridFile.getParent() | UNREACHABLE | no_trigger_in_app | Parameterless overload; app uses Context version | HybridFile.java:376-399 |
| HybridFile.length() | UNREACHABLE | no_trigger_in_app | Parameterless overload; app uses Context version | HybridFile.java:220,252 |
| Operations.<init> | REACHABLE | CALL | Operations utility class instantiated | Operations.java:30 |
| Operations.checkFolder | UNREACHABLE | no_trigger_in_app | Private static helper method | Operations.java:491 |
| Operations.isFileSystemFAT | UNREACHABLE | no_trigger_in_app | Private static helper method | Operations.java:549 |
| PasteHelper.<init>(Parcel) | REACHABLE | CALL | Parcelable CREATOR constructs from Parcel | PasteHelper.java:38 |
| PasteHelper.describeContents | REACHABLE | FRAMEWORK | Android Parcelable contract method | PasteHelper.java:27-29 |
| PasteHelper.writeToParcel | REACHABLE | FRAMEWORK | Android Parcelable serialization | PasteHelper.java:32-35 |
