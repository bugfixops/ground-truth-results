STATUS: START 21:36

| Method | Label | Kind | Reason | Evidence |
|--------|-------|------|--------|----------|
| ZipService$1.onReceive | REACHABLE | FRAMEWORK | BroadcastReceiver callback | SRC asynchronous/services/ZipService.java:86,307 |
| HybridFile$11$1.close | REACHABLE | CALL | InputStream.close() override | SRC filesystem/HybridFile.java:952-965 |
| HybridFile$9$1.close | REACHABLE | CALL | InputStream.close() override | SRC filesystem/HybridFile.java:909-920 |
| MediaStoreHack.mkfile | REACHABLE | - | Already in graph_def.py | - |
| Operations$1.doInBackground | REACHABLE | ASYNC | AsyncTask callback | SRC filesystem/Operations.java:83,88-194 |
| Operations$2.doInBackground | REACHABLE | ASYNC | AsyncTask callback | SRC filesystem/Operations.java:197,202-332 |
| Operations$3$1.<init> | REACHABLE | CALL | Anonymous class instantiated | SRC filesystem/Operations.java:369 |
| Coders.addEncoder | REACHABLE | - | Already in graph_def.py | - |
| Coders$BCJDecoder.encode | REACHABLE | - | Already in graph_def.py | - |
| Coders$BZIP2Decoder.encode | REACHABLE | - | Already in graph_def.py | - |
| Coders$CopyDecoder.encode | REACHABLE | - | Already in graph_def.py | - |
| Coders$DeflateDecoder.encode | REACHABLE | - | Already in graph_def.py | - |
| NID.<init> | UNREACHABLE | no_trigger_in_app | Library class not instantiated | class not in app source |
| SevenZMethod.getId | UNREACHABLE | no_trigger_in_app | Library method not called | class not in app source |
| StreamMap.toString | UNREACHABLE | no_trigger_in_app | Library toString not called | class not in app source |
| RarDecompressor.realRelativeDirectory | UNREACHABLE | no_trigger_in_app | Library method not called | class not in app source |
| SshClientTemplate.<init>(String) | INCOMPLETE | - | Single-param constructor delegates to two-param; needs verification if called directly | - |
| Statvfs.<init> | UNREACHABLE | no_trigger_in_app | Library class constructor | class not in app source |
| UsbOtgRepresentation.equals | INCOMPLETE | - | Needs grep to verify equals() usage in app | - |
| MainFragment$1.onGlobalLayout | REACHABLE | - | Already in graph_def.py | - |
| MainFragment$2.getSpanSize | REACHABLE | - | Already in graph_def.py | - |
| MainFragment$4.onReceive | REACHABLE | - | Already in graph_def.py | - |
| MainFragment$5.onReceive | REACHABLE | - | Already in graph_def.py | - |
| PreferencesConstants.<init> | UNREACHABLE | no_trigger_in_app | Constants class never instantiated | SRC fragments/preference_fragments/PreferencesConstants.java:8 |
| ColorPreference.<clinit> | REACHABLE | - | Already in graph_def.py | - |
| ColorPickerDialog$ColorItemPair.<init> | REACHABLE | - | Already in graph_def.py | - |
| SmbSearchDialog$ElementViewHolder.<init> | INCOMPLETE | - | RecyclerView ViewHolder; needs instantiation analysis | - |
| NotificationConstants.<init> | UNREACHABLE | no_trigger_in_app | Constants class never instantiated | SRC ui/notifications/NotificationConstants.java:18 |
| CircleGradientDrawable.<init>(String,AppTheme,DisplayMetrics) | INCOMPLETE | - | Custom view constructor; needs instantiation analysis | - |
| Indicator$PendingRevealAnimator.lambda$new$0 | INCOMPLETE | - | Lambda method; needs decompilation context | - |
| ThemedTextView.<init> | INCOMPLETE | - | Custom view; likely inflated from XML | - |
| WarnableTextInputLayout.<init> | INCOMPLETE | - | Custom view; likely inflated from XML | - |
| Drawer.lockIfNotOnTablet | REACHABLE | - | Already in graph_def.py | - |
| ComputerParcelable$1.<init> | INCOMPLETE | - | Parcelable CREATOR anonymous class; needs analysis | - |
| DataUtils$DataUtilsHolder.<init> | INCOMPLETE | - | Singleton holder pattern; needs analysis | - |
| MapEntry.<init> | REACHABLE | - | Already in graph_def.py | - |
| OTGUtil.<init> | UNREACHABLE | no_trigger_in_app | Utility class with static methods only | SRC utils/OTGUtil.java |
| ObtainableServiceBinder.getService | REACHABLE | - | Already in graph_def.py | - |
| ProgressHandler.<init>(int,long) | INCOMPLETE | - | Specific constructor overload; needs verification | - |
| ServiceWatcherUtil$1.run | INCOMPLETE | - | Runnable anonymous class; needs analysis | - |

STATUS: DONE 21:44

STATUS: INCOMPLETE SshClientTemplate.<init>(String) UsbOtgRepresentation.equals SmbSearchDialog$ElementViewHolder.<init> CircleGradientDrawable.<init>(String,AppTheme,DisplayMetrics) Indicator$PendingRevealAnimator.lambda$new$0 ThemedTextView.<init> WarnableTextInputLayout.<init> ComputerParcelable$1.<init> DataUtils$DataUtilsHolder.<init> ProgressHandler.<init>(int,long) ServiceWatcherUtil$1.run
