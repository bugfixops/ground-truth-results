STATUS: START 20:49

| Method | Label | Kind | Reason | Evidence |
|--------|-------|------|--------|----------|
| TabFragment.onDestroyView | REACHABLE | LIFECYCLE | Fragment lifecycle method called by framework | FW-SRC Fragment.java:2744-2758, FragmentManager.java:1356 |
| TabFragment.onPageScrollStateChanged | REACHABLE | FRAMEWORK | ViewPager calls listener method | SRC TabFragment.java:45,99,311-313 |
| TabFragment.onPageScrolled | REACHABLE | FRAMEWORK | ViewPager calls listener method during scroll | SRC TabFragment.java:45,99,269-276 |
| TabFragment.onPageSelected | REACHABLE | CALL | Calls BottomBar.updatePath when page selected | SRC TabFragment.java:287 |
| TabFragment.onSaveInstanceState | REACHABLE | LIFECYCLE | Fragment lifecycle save state method | SRC TabFragment.java:260-271 |
| TabFragment.parsePathForName | UNREACHABLE | no_trigger_in_app | Never called in app code | SRC TabFragment.java:243-255, grep finds no callers |
| TabFragment.parseSmbPath | UNREACHABLE | no_trigger_in_app | Only called from unreachable parsePathForName | SRC TabFragment.java:237-241,248 |
| SmbSearchDialog$ListViewAdapter.<init> | REACHABLE | CALL | Created by SmbSearchDialog | SRC SmbSearchDialog.java:78 |
| SmbSearchDialog$ListViewAdapter.getItemCount | REACHABLE | FRAMEWORK | RecyclerView calls getItemCount on adapter | SRC SmbSearchDialog.java:179-181 |
| SmbSearchDialog$ListViewAdapter.getItemId | REACHABLE | FRAMEWORK | RecyclerView calls getItemId on adapter | SRC SmbSearchDialog.java:175-177 |
| SmbSearchDialog$ListViewAdapter.getItemViewType | REACHABLE | FRAMEWORK | RecyclerView calls getItemViewType on adapter | SRC SmbSearchDialog.java:165-173 |
| SmbSearchDialog$ListViewAdapter.lambda$onBindViewHolder$0 | REACHABLE | CALL | Lambda from onBindViewHolder click listener | SRC SmbSearchDialog.java:148-158 |
| SmbSearchDialog$ListViewAdapter.onBindViewHolder | REACHABLE | FRAMEWORK | RecyclerView calls onBindViewHolder on adapter | SRC SmbSearchDialog.java:144-162 |
| SmbSearchDialog$ListViewAdapter.onCreateViewHolder | REACHABLE | FRAMEWORK | RecyclerView calls onCreateViewHolder on adapter | SRC SmbSearchDialog.java:131-142 |
| RoundedImageView.<init> | REACHABLE | FRAMEWORK | Android inflates custom view from XML | SRC RoundedImageView.java:32-37 |
| RoundedImageView.drawableToBitmap | REACHABLE | CALL | Called by onDraw to convert drawable | SRC RoundedImageView.java:44 |
| RoundedImageView.drawableToBitmapRelative | REACHABLE | CALL | Called by onDraw for icon images | SRC RoundedImageView.java:55 |
| RoundedImageView.getRoundedCroppedBitmap | REACHABLE | CALL | Called by onDraw to create rounded bitmap | SRC RoundedImageView.java:47 |
| RoundedImageView.isImageAnIcon | REACHABLE | CALL | Called by onDraw to check icon type | SRC RoundedImageView.java:43 |
| RoundedImageView.onDraw | REACHABLE | FRAMEWORK | View framework calls onDraw to render | SRC RoundedImageView.java:40-58 |
| RoundedImageView.setBackgroundColor | UNREACHABLE | no_trigger_in_app | Never called on RoundedImageView instances | SRC RoundedImageView.java:65-67, grep finds no callers |
| SelectedColorsPreference.<init> | REACHABLE | FRAMEWORK | Created via ColorPickerDialog subclass from XML | SRC ColorPickerDialog.java:40, res/xml/conficolor_prefs.xml:3 |
| SelectedColorsPreference.invalidateColors | REACHABLE | CALL | Called by ColorPref to refresh display | SRC ColorPref.java:265,221 |
| SelectedColorsPreference.onBindView | REACHABLE | FRAMEWORK | Preference framework calls to bind data | SRC SelectedColorsPreference.java:38-46 |
| SelectedColorsPreference.onCreateView | REACHABLE | FRAMEWORK | Preference framework calls to create view | SRC SelectedColorsPreference.java:32-35 |
| SelectedColorsPreference.setColors | REACHABLE | CALL | Called by ColorPref to update colors | SRC ColorPref.java:281-283,272 |
| SelectedColorsPreference.setColorsVisibility | REACHABLE | CALL | Called by ColorPref to show/hide colors | SRC ColorPref.java:278,291,272 |
| SelectedColorsPreference.setDividerColor | REACHABLE | CALL | Called by ColorPref to set divider color | SRC ColorPref.java:286,288,272 |
| ZipService$CompressAsyncTask.compressFile | REACHABLE | CALL | Called by execute and recursively by itself | SRC ZipService.java:263,279 |
| ZipService$CompressAsyncTask.doInBackground | REACHABLE | ASYNC | AsyncTask framework calls on worker thread | SRC ZipService.java:218-234 |
| ZipService$CompressAsyncTask.execute | REACHABLE | CALL | Called by ZipService.onStartCommand | SRC ZipService.java:141 |
| ZipService$CompressAsyncTask.lambda$doInBackground$0 | REACHABLE | CALL | Lambda from doInBackground progress listener | SRC ZipService.java:227-228 |
| ZipService$CompressAsyncTask.onCancelled | REACHABLE | ASYNC | AsyncTask framework calls if cancelled | SRC ZipService.java:236-242 |
| ZipService$CompressAsyncTask.onPostExecute | REACHABLE | ASYNC | AsyncTask framework calls after completion | SRC ZipService.java:244-250 |
| SevenZOutputFile$OutputStreamWrapper.<init> | UNREACHABLE | no_trigger_in_app | Apache Commons Compress library class never used | grep finds no references to SevenZOutputFile or OutputStreamWrapper |
| SevenZOutputFile$OutputStreamWrapper.close | UNREACHABLE | no_trigger_in_app | Library class never instantiated | grep finds no references to OutputStreamWrapper |
| SevenZOutputFile$OutputStreamWrapper.flush | UNREACHABLE | no_trigger_in_app | Library class never instantiated | grep finds no references to OutputStreamWrapper |
| SevenZOutputFile$OutputStreamWrapper.write(int) | UNREACHABLE | no_trigger_in_app | Library class never instantiated | grep finds no references to OutputStreamWrapper |
| SevenZOutputFile$OutputStreamWrapper.write(byte[]) | UNREACHABLE | no_trigger_in_app | Library class never instantiated | grep finds no references to OutputStreamWrapper |
| SevenZOutputFile$OutputStreamWrapper.write(byte[],int,int) | UNREACHABLE | no_trigger_in_app | Library class never instantiated | grep finds no references to OutputStreamWrapper |

STATUS: DONE 20:59
