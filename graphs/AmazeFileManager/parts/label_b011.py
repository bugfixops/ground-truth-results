# ---- batch_011 label part (2026-10-27)

# ColorCircleDrawable methods
e('TabFragment.updatePathColors', 'ColorCircleDrawable.<init>',
  'EXPLICIT', 'Direct instantiation in TabFragment',
  evidence='SRC TabFragment.java:386')

e('Drawable', 'ColorCircleDrawable.draw',
  'FRAMEWORK', 'Overridden framework method, called by Android Drawable framework',
  evidence='FW-SRC android-8.1.0_r1/android/graphics/drawable/Drawable.java:source not read')

e('Drawable', 'ColorCircleDrawable.onBoundsChange',
  'FRAMEWORK', 'Overridden framework method, called by Android Drawable lifecycle',
  evidence='FW-SRC android-8.1.0_r1/android/graphics/drawable/Drawable.java:source not read')

e('Drawable', 'ColorCircleDrawable.setAlpha',
  'FRAMEWORK', 'Overridden framework method, called by Android drawable operations',
  evidence='FW-SRC android-8.1.0_r1/android/graphics/drawable/Drawable.java:source not read')

e('Drawable', 'ColorCircleDrawable.setColorFilter',
  'FRAMEWORK', 'Overridden framework method, called by Android drawable operations',
  evidence='FW-SRC android-8.1.0_r1/android/graphics/drawable/Drawable.java:source not read')

e('Drawable', 'ColorCircleDrawable.getOpacity',
  'FRAMEWORK', 'Overridden framework method, called by Android drawable operations',
  evidence='FW-SRC android-8.1.0_r1/android/graphics/drawable/Drawable.java:source not read')

# ColorPickerDialog methods
e('PreferenceScreen', 'ColorPickerDialog.<init>',
  'FRAMEWORK', 'Instantiated by Android PreferenceManager from XML via framework',
  evidence='SRC ColorPickerDialog.java:68')

e('DialogPreference', 'ColorPickerDialog.<clinit>',
  'FRAMEWORK', 'Static initialization block called by class loader on first access',
  evidence='SRC ColorPickerDialog.java:44-49')

e('DialogPreference', 'ColorPickerDialog.onBindDialogView',
  'FRAMEWORK', 'Lifecycle method called by DialogPreference framework',
  evidence='SRC ColorPickerDialog.java:108')

e('DialogPreference', 'ColorPickerDialog.onDialogClosed',
  'FRAMEWORK', 'Lifecycle method called by DialogPreference framework',
  evidence='SRC ColorPickerDialog.java:168')

e('DialogPreference', 'ColorPickerDialog.onSaveInstanceState',
  'FRAMEWORK', 'Lifecycle method called by Preference framework for state persistence',
  evidence='SRC ColorPickerDialog.java:220')

e('DialogPreference', 'ColorPickerDialog.onRestoreInstanceState',
  'FRAMEWORK', 'Lifecycle method called by Preference framework for state restoration',
  evidence='SRC ColorPickerDialog.java:229')

e('DialogPreference', 'ColorPickerDialog.onGetDefaultValue',
  'FRAMEWORK', 'Lifecycle method called by Preference framework',
  evidence='SRC ColorPickerDialog.java:89')

e('DialogPreference', 'ColorPickerDialog.getSummary',
  'FRAMEWORK', 'Lifecycle method called by Preference framework to get display text',
  evidence='SRC ColorPickerDialog.java:94')

e('DialogPreference', 'ColorPickerDialog.showDialog',
  'FRAMEWORK', 'Lifecycle method called by DialogPreference framework',
  evidence='SRC ColorPickerDialog.java:200')

e('ColorPickerDialog.onBindDialogView', 'ColorPickerDialog.inflateItem',
  'EXPLICIT', 'Called directly from onBindDialogView in loop',
  evidence='SRC ColorPickerDialog.java:122')

e('ColorPickerDialog.onBindDialogView', 'ColorPickerDialog.select',
  'EXPLICIT', 'Called directly from onBindDialogView',
  evidence='SRC ColorPickerDialog.java:128')

e('ColorPickerDialog.onBindDialogView', 'ColorPickerDialog.getColor',
  'EXPLICIT', 'Called directly from onBindDialogView',
  evidence='SRC ColorPickerDialog.java:132')

e('ColorPickerDialog.onDialogClosed', 'ColorPickerDialog.getColor',
  'EXPLICIT', 'Called directly from onDialogClosed',
  evidence='SRC ColorPickerDialog.java:182')

e('ColorPickerDialog.inflateItem', 'ColorPickerDialog.select',
  'EXPLICIT', 'Called from inflateItem lambda via select()',
  evidence='SRC ColorPickerDialog.java:156')

e('ColorPickerDialog.onRestoreInstanceState', 'ColorPickerDialog.select',
  'EXPLICIT', 'Called directly from onRestoreInstanceState',
  evidence='SRC ColorPickerDialog.java:244')

# ColorPickerDialog$ColorItemPair (inner static class)
e('ColorPickerDialog.<clinit>', 'ColorPickerDialog$ColorItemPair.<init>',
  'EXPLICIT', 'Called during static initialization of COLORS array',
  evidence='SRC ColorPickerDialog.java:48-51')

# ColorPickerDialog$SavedState
e('ColorPickerDialog.onSaveInstanceState', 'ColorPickerDialog$SavedState.<init>',
  'EXPLICIT', 'Called directly to create SavedState instance from Parcelable',
  evidence='SRC ColorPickerDialog.java:256')

# SavedState second constructor
e('DialogPreference', 'ColorPickerDialog$SavedState.<init>',
  'FRAMEWORK', 'Constructor from Parcel, called by Parcelable framework',
  evidence='SRC ColorPickerDialog.java:277')

# SavedState second constructor (from Parcelable deserialization)
e('Parcelable.Creator', 'ColorPickerDialog$SavedState.<init>',
  'FRAMEWORK', 'Constructor from Parcel called by Parcelable.Creator.createFromParcel',
  evidence='SRC ColorPickerDialog.java:295')

e('ColorPickerDialog$SavedState.<init>', 'ColorPickerDialog$SavedState.<clinit>',
  'FRAMEWORK', 'Static initialization called by class loader',
  evidence='SRC ColorPickerDialog.java:253')

e('BaseSavedState', 'ColorPickerDialog$SavedState.writeToParcel',
  'FRAMEWORK', 'Called by Parcelable framework during state serialization',
  evidence='SRC ColorPickerDialog.java:263')

# ColorPickerDialog$SavedState$1 (Creator inner class)
e('ColorPickerDialog$SavedState.<clinit>', 'ColorPickerDialog$SavedState$1.<init>',
  'EXPLICIT', 'Called during static initialization of CREATOR',
  evidence='SRC ColorPickerDialog.java:268')

e('Parcelable.Creator', 'ColorPickerDialog$SavedState$1.createFromParcel',
  'FRAMEWORK', 'Called by Parcelable framework during deserialization',
  evidence='SRC ColorPickerDialog.java:271')

e('Parcelable.Creator', 'ColorPickerDialog$SavedState$1.newArray',
  'FRAMEWORK', 'Called by Parcelable framework during array allocation',
  evidence='SRC ColorPickerDialog.java:274')

