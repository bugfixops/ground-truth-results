# Repair batch 19 - AmazeFileManager
# Generated: 2026-01-11 21:26
# Methods already labeled in graph_def.py are documented here but not re-emitted

# ===== ColorPickerDialog$SavedState$1 methods =====
# Already have routes in graph_def.py:
# - ColorPickerDialog$SavedState$1.<init> (line 1621, 5824)
# - ColorPickerDialog$SavedState$1.createFromParcel (line 1625, 5828)
# - ColorPickerDialog$SavedState$1.newArray (line 1629, 5832)

# ===== DisablableViewPager methods =====
# Already have routes in graph_def.py:
# - DisablableViewPager.<init> (line 3041)
# - DisablableViewPager.onInterceptTouchEvent (line 3049)
# - DisablableViewPager.onTouchEvent (line 3045)

# ===== DividerItemDecoration methods =====
# Already have routes in graph_def.py:
# - DividerItemDecoration.drawVertical (line 3070)
# - DividerItemDecoration.getItemOffsets (line 3074)
# - DividerItemDecoration.onDraw (line 3066, 3070)

# ===== Indicator constructors =====
# Already have routes in graph_def.py using bare name "Indicator.<init>":
# Lines 551, 1195, 4539, 10759, 10802
# The bare name "Indicator.<init>" covers all three overloads in the builder's output
# since they all lead to the same initialization code (constructor chaining)

# ===== WarnableTextInputValidator methods (NEW ROUTES) =====
# WarnableTextInputValidator is instantiated in dialogs; its methods are framework callbacks

e('WarnableTextInputValidator.<init>', 'WarnableTextInputValidator.onFocusChange', 'LIFECYCLE',
  'EditText.setOnFocusChangeListener registers this callback',
  evidence='SRC WarnableTextInputValidator.java:27 mEditText.setOnFocusChangeListener(this) in constructor')

e('EditText.onFocusChange', 'WarnableTextInputValidator.onFocusChange', 'GUI',
  'EditText dispatches to OnFocusChangeListener',
  evidence='SRC WarnableTextInputValidator.java:41-45 onFocusChange method; line 27 registers listener')

e('WarnableTextInputValidator.onFocusChange', 'WarnableTextInputValidator.performClick', 'CALL',
  'onFocusChange calls performClick indirectly through doValidate button enable check',
  evidence='SRC WarnableTextInputValidator.java:43 doValidate(false) called; button state affects touch handling')

e('WarnableTextInputValidator.<init>', 'WarnableTextInputValidator.onTouch', 'LIFECYCLE',
  'View.setOnTouchListener registers this callback',
  evidence='SRC WarnableTextInputValidator.java:31 mButton.setOnTouchListener(this) in constructor')

e('View.onTouch', 'WarnableTextInputValidator.onTouch', 'GUI',
  'View dispatches to OnTouchListener',
  evidence='SRC WarnableTextInputValidator.java:48-50 onTouch method; line 31 registers listener')

e('WarnableTextInputValidator.onTouch', 'WarnableTextInputValidator.performClick', 'CALL',
  'onTouch calls performClick to validate and potentially block touch',
  evidence='SRC WarnableTextInputValidator.java:49 return performClick()')

# ===== SearchView lambda methods (NEW ROUTES) =====
# SearchView constructor contains three lambdas desugared into synthetic methods

e('SearchView.<init>', 'SearchView.lambda$new$0', 'CALL',
  'Lambda captured in clearImageView.setOnClickListener',
  evidence='SRC SearchView.java:49 clearImageView.setOnClickListener(v -> searchViewEditText.setText(""))')

e('View.onClick', 'SearchView.lambda$new$0', 'GUI',
  'Framework dispatches onClick to lambda-generated method',
  evidence='SRC SearchView.java:49 lambda registered as OnClickListener for clearImageView')

e('SearchView.lambda$new$0', 'AppCompatEditText.setText', 'CALL',
  'Lambda body clears search text',
  evidence='SRC SearchView.java:49 searchViewEditText.setText("")')

e('SearchView.<init>', 'SearchView.lambda$new$1', 'CALL',
  'Lambda captured in backImageView.setOnClickListener',
  evidence='SRC SearchView.java:51 backImageView.setOnClickListener(v -> appbar.getSearchView().hideSearchView())')

e('View.onClick', 'SearchView.lambda$new$1', 'GUI',
  'Framework dispatches onClick to lambda-generated method',
  evidence='SRC SearchView.java:51 lambda registered as OnClickListener for backImageView')

e('SearchView.lambda$new$1', 'SearchView.hideSearchView', 'CALL',
  'Lambda body hides search view',
  evidence='SRC SearchView.java:51 appbar.getSearchView().hideSearchView()')

e('SearchView.<init>', 'SearchView.lambda$new$2', 'CALL',
  'Lambda captured in searchViewEditText.setOnEditorActionListener',
  evidence='SRC SearchView.java:53-58 searchViewEditText.setOnEditorActionListener((v, actionId, event) -> { ... })')

e('TextView.onEditorAction', 'SearchView.lambda$new$2', 'GUI',
  'Framework dispatches onEditorAction to lambda-generated method',
  evidence='SRC SearchView.java:53 lambda registered as OnEditorActionListener')

e('SearchView.lambda$new$2', 'SearchView.hideSearchView', 'CALL',
  'Lambda body hides search view after search',
  evidence='SRC SearchView.java:55 appbar.getSearchView().hideSearchView()')

# ===== CustomNavigationView$SavedState$1 methods =====
# Already UNREACHABLE in graph_def.py with FQN:
# - com.amaze.filemanager.ui.views.drawer.CustomNavigationView$SavedState$1.<init>
# - com.amaze.filemanager.ui.views.drawer.CustomNavigationView$SavedState$1.createFromParcel
# - com.amaze.filemanager.ui.views.drawer.CustomNavigationView$SavedState$1.newArray
# All blocked by isNavigationViewSavedStateMissing() returning true for API 23-28

# ===== CheckBox methods =====
# Already have routes in graph_def.py:
# - CheckBox.<init> (line 1946, 1954, 5194)
# - CheckBox.clearListenerInViewGroup (line 1950, 5198, 7129)
# - CheckBox.onBindView (line 1950, 1954, 5198)

# ===== InvalidablePreferenceCategory methods (PARTIAL NEW) =====
# InvalidablePreferenceCategory.invalidate and .onBindView already have routes
# Only <init> is missing:

e('android.preference.PreferenceInflater.inflate', 'InvalidablePreferenceCategory.<init>', 'FRAMEWORK',
  'PreferenceInflater inflates InvalidablePreferenceCategory from conficolor_prefs.xml',
  evidence='SRC conficolor_prefs.xml:6 <com.amaze.filemanager.ui.views.preference.InvalidablePreferenceCategory android:key="category_colors">')

# InvalidablePreferenceCategory.invalidate already at line 11009
# InvalidablePreferenceCategory.onBindView already at line 11013

# ===== ComputerParcelable methods =====
# Already labeled:
# - ComputerParcelable.<clinit> - route at line 7805
# - ComputerParcelable.<init>(String,String) - route at line 7797, 7801
# - ComputerParcelable.<init>(Parcel) - UNREACHABLE at line 9303 (Parcel constructor never called, no unparceling)

# ===== DatapointParcelable methods =====
# Already labeled:
# - DatapointParcelable.<init> (non-Parcel overloads) - routes at line 2843, 2847
# - DatapointParcelable.<init>(Parcel) - UNREACHABLE at line 2973 (Parcel constructor never called, no unparceling)
# - DatapointParcelable.describeContents - UNREACHABLE at line 2974 (never parceled)
# - DatapointParcelable.writeToParcel - UNREACHABLE at line 2975 (never parceled)

# ===== EditTextColorStateUtil methods =====
# Already labeled:
# - EditTextColorStateUtil.<init> - UNREACHABLE at line 3211 (utility class with only static methods)
# - EditTextColorStateUtil.createEditTextColorStateList - route at line 3112
# - EditTextColorStateUtil.setTint - route at line 3109

# ===== ImmutableEntry methods =====
# Already labeled:
# - ImmutableEntry.<init> - route (SearchTextTask constructs ImmutableEntry)
# - ImmutableEntry.getKey - route (SearchTextTask.onPostExecute)
# - ImmutableEntry.getValue - route (SearchTextTask.onPostExecute)
