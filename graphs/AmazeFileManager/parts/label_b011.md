STATUS: RUNNING 21:31

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| ColorCircleDrawable.<init> | REACHABLE | EXPLICIT | Direct instantiation in TabFragment, line 386 | SRC TabFragment.java:386 |
| ColorCircleDrawable.draw | REACHABLE | FRAMEWORK | Overridden Drawable.draw, called by Android framework | FW-SRC android-8.1.0_r1/android/graphics/drawable/Drawable.java:source not read |
| ColorCircleDrawable.onBoundsChange | REACHABLE | FRAMEWORK | Overridden Drawable.onBoundsChange, called by Android framework | FW-SRC android-8.1.0_r1/android/graphics/drawable/Drawable.java:source not read |
| ColorCircleDrawable.setAlpha | REACHABLE | FRAMEWORK | Overridden Drawable.setAlpha, called by Android framework | FW-SRC android-8.1.0_r1/android/graphics/drawable/Drawable.java:source not read |
| ColorCircleDrawable.setColorFilter | REACHABLE | FRAMEWORK | Overridden Drawable.setColorFilter, called by Android framework | FW-SRC android-8.1.0_r1/android/graphics/drawable/Drawable.java:source not read |
| ColorCircleDrawable.getOpacity | REACHABLE | FRAMEWORK | Overridden Drawable.getOpacity, called by Android framework | FW-SRC android-8.1.0_r1/android/graphics/drawable/Drawable.java:source not read |
| ColorPickerDialog.<clinit> | REACHABLE | FRAMEWORK | Static initialization, class loaded when ColorPickerDialog is first used | SRC ColorPickerDialog.java:44-51 |
| ColorPickerDialog.<init> | REACHABLE | FRAMEWORK | Instantiated by Android PreferenceManager from XML in conficolor_prefs.xml | SRC ColorPickerDialog.java:68 |
| ColorPickerDialog.getColor | REACHABLE | EXPLICIT | Called from onBindDialogView and onDialogClosed | SRC ColorPickerDialog.java:132, 182 |
| ColorPickerDialog.getSummary | REACHABLE | FRAMEWORK | Lifecycle method called by Preference framework | SRC ColorPickerDialog.java:94 |
| ColorPickerDialog.inflateItem | REACHABLE | EXPLICIT | Called from onBindDialogView loop for each color item | SRC ColorPickerDialog.java:122 |
| ColorPickerDialog.lambda$inflateItem$0 | REACHABLE | EXPLICIT | Lambda click listener created in inflateItem, calls select() | SRC ColorPickerDialog.java:156 |
| ColorPickerDialog.onBindDialogView | REACHABLE | FRAMEWORK | Lifecycle method called by DialogPreference framework | SRC ColorPickerDialog.java:108 |
| ColorPickerDialog.onDialogClosed | REACHABLE | FRAMEWORK | Lifecycle method called by DialogPreference framework | SRC ColorPickerDialog.java:168 |
| ColorPickerDialog.onGetDefaultValue | REACHABLE | FRAMEWORK | Lifecycle method called by Preference framework for default values | SRC ColorPickerDialog.java:89 |
| ColorPickerDialog.onRestoreInstanceState | REACHABLE | FRAMEWORK | Lifecycle method called by Preference framework | SRC ColorPickerDialog.java:229 |
| ColorPickerDialog.onSaveInstanceState | REACHABLE | FRAMEWORK | Lifecycle method called by Preference framework for state persistence | SRC ColorPickerDialog.java:220 |
| ColorPickerDialog.select | REACHABLE | EXPLICIT | Called from onBindDialogView, onRestoreInstanceState, and lambda in inflateItem | SRC ColorPickerDialog.java:156, 158, 244 |
| ColorPickerDialog.setColorPreference | REACHABLE | EXPLICIT | Called from ColorPref.onCreate, sets up color preferences | SRC ColorPickerDialog.java:75 |
| ColorPickerDialog.setListener | REACHABLE | EXPLICIT | Called from ColorPref to set the OnAcceptedConfig listener | SRC ColorPickerDialog.java:80 |
| ColorPickerDialog.showDialog | REACHABLE | FRAMEWORK | Lifecycle method called by DialogPreference framework to show dialog | SRC ColorPickerDialog.java:200 |
| ColorPickerDialog$ColorItemPair.<init> | REACHABLE | EXPLICIT | Called in COLORS static array initialization | SRC ColorPickerDialog.java:48-51 |
| ColorPickerDialog$SavedState.<clinit> | REACHABLE | FRAMEWORK | Static initialization of CREATOR field, called on class load | SRC ColorPickerDialog.java:252-276 |
| ColorPickerDialog$SavedState.<init> | REACHABLE | FRAMEWORK | Constructor from Parcel, called by Parcelable.Creator.createFromParcel | SRC ColorPickerDialog.java:277-280 |
| ColorPickerDialog$SavedState.<init> | REACHABLE | EXPLICIT | Constructor from Parcelable superstate, called from onSaveInstanceState | SRC ColorPickerDialog.java:256, 286-288 |
| ColorPickerDialog$SavedState.writeToParcel | REACHABLE | FRAMEWORK | Called by Parcelable framework during state serialization | SRC ColorPickerDialog.java:282-285 |
| ColorPickerDialog$SavedState$1.<init> | REACHABLE | EXPLICIT | Anonymous inner class instantiated during SavedState static init | SRC ColorPickerDialog.java:268 |
| ColorPickerDialog$SavedState$1.createFromParcel | REACHABLE | FRAMEWORK | Called by Parcelable.Creator framework during deserialization | SRC ColorPickerDialog.java:271 |
| ColorPickerDialog$SavedState$1.newArray | REACHABLE | FRAMEWORK | Called by Parcelable.Creator framework during array allocation | SRC ColorPickerDialog.java:274 |

STATUS: DONE 21:31

