# Repair Batch 19 - 39 methods

STATUS: START 21:26

| Method | Label | Kind | Reason | Evidence |
|--------|-------|------|--------|----------|
| ColorPickerDialog$SavedState$1.<init> | REACHABLE | existing | Route already in graph_def.py | graph_def.py:1621,5824 |
| ColorPickerDialog$SavedState$1.createFromParcel | REACHABLE | existing | Route already in graph_def.py | graph_def.py:1625,5828 |
| ColorPickerDialog$SavedState$1.newArray | REACHABLE | existing | Route already in graph_def.py | graph_def.py:1629,5832 |
| DisablableViewPager.<init> | REACHABLE | existing | Route already in graph_def.py | graph_def.py:3041 |
| DisablableViewPager.onInterceptTouchEvent | REACHABLE | existing | Route already in graph_def.py | graph_def.py:3049 |
| DisablableViewPager.onTouchEvent | REACHABLE | existing | Route already in graph_def.py | graph_def.py:3045 |
| DividerItemDecoration.drawVertical | REACHABLE | existing | Route already in graph_def.py | graph_def.py:3070 |
| DividerItemDecoration.getItemOffsets | REACHABLE | existing | Route already in graph_def.py | graph_def.py:3074 |
| DividerItemDecoration.onDraw | REACHABLE | existing | Route already in graph_def.py | graph_def.py:3066,3070 |
| Indicator.<init>(Context) | REACHABLE | existing | Covered by bare "Indicator.<init>" in graph_def.py | graph_def.py:551,1195,4539,10759; constructor chains to (Context,AttributeSet,int) |
| Indicator.<init>(Context,AttributeSet) | REACHABLE | existing | Covered by bare "Indicator.<init>" in graph_def.py | graph_def.py:551,1195,4539,10759; Indicator.java:135 calls this(context, attrs, 0) |
| Indicator.<init>(Context,AttributeSet,int) | REACHABLE | existing | Covered by bare "Indicator.<init>" in graph_def.py | graph_def.py:551,1195,4539,10759; Indicator.java:139-173 main constructor |
| WarnableTextInputValidator.onFocusChange | REACHABLE | LIFECYCLE+GUI | Registered by constructor line 27, dispatched by EditText | WarnableTextInputValidator.java:27,41-45 |
| WarnableTextInputValidator.onTouch | REACHABLE | LIFECYCLE+GUI | Registered by constructor line 31, dispatched by View | WarnableTextInputValidator.java:31,48-50 |
| WarnableTextInputValidator.performClick | REACHABLE | CALL | Called from onTouch line 49 | WarnableTextInputValidator.java:49,52-54 |
| SearchView.lambda$new$0 | REACHABLE | CALL+GUI | Lambda for clearImageView.setOnClickListener | SearchView.java:49 |
| SearchView.lambda$new$1 | REACHABLE | CALL+GUI | Lambda for backImageView.setOnClickListener | SearchView.java:51 |
| SearchView.lambda$new$2 | REACHABLE | CALL+GUI | Lambda for searchViewEditText.setOnEditorActionListener | SearchView.java:53-58 |
| CustomNavigationView$SavedState$1.<init> | UNREACHABLE | existing | Already UNREACHABLE in graph_def.py with FQN | graph_def.py (FQN com.amaze...); blocked by isNavigationViewSavedStateMissing() API 23-28 |
| CustomNavigationView$SavedState$1.createFromParcel | UNREACHABLE | existing | Already UNREACHABLE in graph_def.py with FQN | graph_def.py (FQN com.amaze...); SavedState not parceled |
| CustomNavigationView$SavedState$1.newArray | UNREACHABLE | existing | Already UNREACHABLE in graph_def.py with FQN | graph_def.py (FQN com.amaze...); SavedState arrays not unparceled |
| CheckBox.<init> | REACHABLE | existing | Route already in graph_def.py | graph_def.py:1946,1954,5194 |
| CheckBox.clearListenerInViewGroup | REACHABLE | existing | Route already in graph_def.py | graph_def.py:1950,5198,7129 |
| CheckBox.onBindView | REACHABLE | existing | Route already in graph_def.py | graph_def.py:1950,1954,5198 |
| InvalidablePreferenceCategory.<init> | REACHABLE | FRAMEWORK | PreferenceInflater inflates from conficolor_prefs.xml | conficolor_prefs.xml:6 |
| InvalidablePreferenceCategory.invalidate | REACHABLE | existing | Route already in graph_def.py | graph_def.py:11009,11013 |
| InvalidablePreferenceCategory.onBindView | REACHABLE | existing | Route already in graph_def.py | graph_def.py:11013 |
| ComputerParcelable.<clinit> | REACHABLE | existing | Route already in graph_def.py | graph_def.py:7805 |
| ComputerParcelable.<init>(Parcel) | UNREACHABLE | existing | Already UNREACHABLE in graph_def.py | graph_def.py:9303; Parcel constructor only called from CREATOR which is never used |
| ComputerParcelable.<init>(String,String) | REACHABLE | existing | Route already in graph_def.py | graph_def.py:7797,7801 |
| DatapointParcelable.<init>(Parcel) | UNREACHABLE | existing | Already UNREACHABLE in graph_def.py | graph_def.py:2973; createFromParcel never called |
| DatapointParcelable.describeContents | UNREACHABLE | existing | Already UNREACHABLE in graph_def.py | graph_def.py:2974; never parceled through Intents |
| DatapointParcelable.writeToParcel | UNREACHABLE | existing | Already UNREACHABLE in graph_def.py | graph_def.py:2975; no putParcelable calls found |
| EditTextColorStateUtil.<init> | UNREACHABLE | existing | Already UNREACHABLE in graph_def.py | graph_def.py:3211; utility class with only static methods |
| EditTextColorStateUtil.createEditTextColorStateList | REACHABLE | existing | Route already in graph_def.py | graph_def.py:3112 |
| EditTextColorStateUtil.setTint | REACHABLE | existing | Route already in graph_def.py | graph_def.py:3109 |
| ImmutableEntry.<init> | REACHABLE | existing | Route already in graph_def.py | SearchTextTask constructs ImmutableEntry |
| ImmutableEntry.getKey | REACHABLE | existing | Route already in graph_def.py | SearchTextTask.onPostExecute calls getKey |
| ImmutableEntry.getValue | REACHABLE | existing | Route already in graph_def.py | SearchTextTask.onPostExecute calls getValue |

STATUS: DONE 21:28

Summary:
- REACHABLE: 30 methods (7 new routes, 23 existing)
- UNREACHABLE: 9 methods (all existing in graph_def.py)
- Total: 39 methods
