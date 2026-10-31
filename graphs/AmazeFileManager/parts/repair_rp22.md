STATUS: START 21:38

| Method | Label | Kind | Reason | Evidence |
|--------|-------|------|--------|----------|
| InterestingConfigChange.<init> | UNREACHABLE | no_trigger_in_app | Utility class with only static methods; never instantiated | SRC utils/InterestingConfigChange.java:17-41 |
| InterestingConfigChange.recycle | REACHABLE | - | Already has route from AppListLoader.onStopLoading | graph_def.py:11004 |
| PreferenceUtils.<init> | UNREACHABLE | no_trigger_in_app | Utility class with only static methods; never instantiated | SRC utils/PreferenceUtils.java:9-33 |
| PreferenceUtils.getStatusColor(String) | REACHABLE | - | Called from MainActivity, DatabaseViewerActivity, PreferencesActivity, TextEditorActivity | SRC activities/MainActivity.java:1415 |
| StreamServer$Response.<init> | INCOMPLETE | - | Not in method_list.json; inner class of NanoHTTPD library | - |
| StreamServer$Response.addHeader | INCOMPLETE | - | Not in method_list.json; inner class of NanoHTTPD library | - |
| SubnetScanner$1.<init> | INCOMPLETE | - | Not in method_list.json; anonymous class | - |
| SubnetScanner$1.run | INCOMPLETE | - | Not in method_list.json; anonymous class | - |
| SubnetScanner$Task.<init> | INCOMPLETE | - | Not in method_list.json; inner class | - |
| SubnetScanner$Task.call | INCOMPLETE | - | Not in method_list.json; inner class | - |
| TinyDB.<init> | UNREACHABLE | no_trigger_in_app | Utility class with only static methods; never instantiated | SRC utils/TinyDB.java:27-67 |
| TinyDB.putBooleanArray | REACHABLE | - | Called from QuickAccessPref.onPreferenceClick | SRC fragments/preference_fragments/QuickAccessPref.java:60 |
| CloudStreamSource.read() | REACHABLE | - | Override of InputStream.read(); called when stream is used | SRC cloud/CloudStreamSource.java:61-65 |
| CloudStreamSource.read(byte[],int,int) | REACHABLE | - | Override of InputStream.read(); called when stream is used | SRC cloud/CloudStreamSource.java:68-72 |
| CloudStreamer.isStreamMedia | REACHABLE | - | Already has route in graph_def.py | graph_def.py:11645 |
| CloudStreamer.setStreamSrc | REACHABLE | - | Already has routes in graph_def.py | graph_def.py:1796,5535 |
| CloudUtil$1.doInBackground | INCOMPLETE | - | Not in method_list.json; anonymous AsyncTask inner class | - |
| CloudUtil$1.onPostExecute | INCOMPLETE | - | Not in method_list.json; anonymous AsyncTask inner class | - |
| CloudIconModelLoader.buildLoadData | REACHABLE | - | Already has multiple routes in graph_def.py | graph_def.py:1846,2120,5362 |
| CloudIconModelLoader.handles | REACHABLE | - | Already has route in graph_def.py | graph_def.py:7142 |
| DummyFileGenerator.<init> | UNREACHABLE | no_trigger_in_app | Test utility class annotated @RestrictTo(TESTS); not used in production | SRC utils/test/DummyFileGenerator.java:1-85 |
| DummyFileGenerator.createFile | UNREACHABLE | no_trigger_in_app | Test utility method annotated @RestrictTo(TESTS); not used in production | SRC utils/test/DummyFileGenerator.java:53-85 |
| RecyclerAdapter$ListItem.<init>(LayoutElementParcelable) | INCOMPLETE | - | Not in method_list.json; private inner class | - |
| AppDataParcelable$AppDataSorter.compare | INCOMPLETE | - | Not in method_list.json; inner class | - |
| CompressedObjectParcelable.writeToParcel | REACHABLE | - | Already has route in graph_def.py | graph_def.py:7538 |
| RecyclerPreloadModelProvider.getPreloadItems | REACHABLE | - | Called via Glide RecyclerViewPreloader | graph_def.py:402 |
| RecyclerPreloadSizeProvider$SizeViewTarget.onResourceReady | INCOMPLETE | - | Not in method_list.json; inner class | - |
| DonationViewHolder.<init> | UNREACHABLE | no_trigger_in_app | RecyclerView.ViewHolder subclass never instantiated by any adapter | SRC adapters/holders/DonationViewHolder.java:10-21 |
| MoveFiles.lambda$onPostExecute$0 | REACHABLE | - | Lambda passed to AppConfig.runInBackground | SRC asynchronous/asynctasks/MoveFiles.java:179-195 |
| PrepareCopyTask$DO_FOR_ALL_ELEMENTS.<clinit> | INCOMPLETE | - | Not in method_list.json; enum static initializer | - |
| SevenZipHelperTask.lambda$onProgressUpdate$0 | REACHABLE | - | Lambda for MaterialDialog positive button callback | SRC asynchronous/asynctasks/compress/SevenZipHelperTask.java:105-113 |
| PemToKeyPairTask$JcaPemToKeyPairConverter.throwingConvert | INCOMPLETE | - | Not in method_list.json; inner class | - |
| PemToKeyPairTask$OpenSshPemToKeyPairConverter.throwingConvert | INCOMPLETE | - | Not in method_list.json; inner class | - |
| PemToKeyPairTask$OpenSshV1PemToKeyPairConverter.throwingConvert | INCOMPLETE | - | Not in method_list.json; inner class | - |
| PemToKeyPairTask$PemToKeyPairConverter.convert | INCOMPLETE | - | Not in method_list.json; inner interface | - |
| PemToKeyPairTask$PuttyPrivateKeyToKeyPairConverter.throwingConvert | INCOMPLETE | - | Not in method_list.json; inner class | - |
| CopyService.setProgressListener | REACHABLE | - | Already has route in graph_def.py | graph_def.py:11745 |
| CopyService$DoInBackground.onPostExecute | INCOMPLETE | - | Not in method_list.json; inner AsyncTask class | - |
| DecryptService.onBind | REACHABLE | - | Already has route in graph_def.py | graph_def.py:2932 |
| EncryptService$1.onReceive | INCOMPLETE | - | Not in method_list.json; anonymous BroadcastReceiver | - |

STATUS: DONE 21:42
STATUS: INCOMPLETE StreamServer$Response.<init>, StreamServer$Response.addHeader, SubnetScanner$1.<init>, SubnetScanner$1.run, SubnetScanner$Task.<init>, SubnetScanner$Task.call, CloudUtil$1.doInBackground, CloudUtil$1.onPostExecute, RecyclerAdapter$ListItem.<init>(LayoutElementParcelable), AppDataParcelable$AppDataSorter.compare, RecyclerPreloadSizeProvider$SizeViewTarget.onResourceReady, PrepareCopyTask$DO_FOR_ALL_ELEMENTS.<clinit>, PemToKeyPairTask$JcaPemToKeyPairConverter.throwingConvert, PemToKeyPairTask$OpenSshPemToKeyPairConverter.throwingConvert, PemToKeyPairTask$OpenSshV1PemToKeyPairConverter.throwingConvert, PemToKeyPairTask$PemToKeyPairConverter.convert, PemToKeyPairTask$PuttyPrivateKeyToKeyPairConverter.throwingConvert, CopyService$DoInBackground.onPostExecute, EncryptService$1.onReceive
