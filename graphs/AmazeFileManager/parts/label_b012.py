# ---- Helper batch 012 label part (2026-10-27)

# ColorPref methods
e('PreferencesActivity.<init>', 'ColorPref.<init>', 'EXPLICIT', 'instantiates ColorPref for color preferences',
  evidence='SRC PreferencesActivity.java:258')

e('ColorPref.onCreate', 'ColorPref.loadSection0', 'CALL', 'called from onCreate',
  evidence='SRC ColorPref.java:56-62')

e('ColorPref.onCreate', 'ColorPref.onRestoreInstanceState', 'CALL', 'called from onCreate when savedInstanceState is not null',
  evidence='SRC ColorPref.java:56-62')

e('ColorPref.onCreate', 'ColorPref.reloadListeners', 'CALL', 'called from onCreate',
  evidence='SRC ColorPref.java:56-62')

e('ColorPref.onPause', 'ColorPref.onPause', 'LIFECYCLE', 'lifecycle method',
  evidence='SRC ColorPref.java:66-68')

e('ColorPref.onOptionsItemSelected', 'ColorPref.switchSections', 'EXPLICIT', 'called when home button pressed in non-section-0',
  evidence='SRC ColorPref.java:74-79')

e('ColorPref.onBackPressed', 'ColorPref.switchSections', 'EXPLICIT', 'called when back button pressed in non-section-0',
  evidence='SRC ColorPref.java:85-88')

e('ColorPref.onPreferenceClick', 'ColorPref.colorChangeDialog', 'EXPLICIT', 'called for color preference clicks',
  evidence='SRC ColorPref.java:95-103')

e('ColorPref.onPreferenceClick', 'ColorPref.switchSections', 'EXPLICIT', 'called for selectcolorconfig click',
  evidence='SRC ColorPref.java:95-103')

e('ColorPref.colorChangeDialog', 'ColorPreference.<clinit>', 'EXPLICIT', 'accesses ColorPreference.availableColors static field',
  evidence='SRC ColorPref.java:134-137')

e('ColorPref.colorChangeDialog', 'ColorPref.lambda$colorChangeDialog$0', 'EXPLICIT', 'lambda callback for color selection',
  evidence='SRC ColorPref.java:136-163')

e('ColorPref.switchSections', 'ColorPref.loadSection0', 'EXPLICIT', 'called from switchSections when switching to section 0',
  evidence='SRC ColorPref.java:199-206')

e('ColorPref.switchSections', 'ColorPref.loadSection1', 'EXPLICIT', 'called from switchSections when switching to section 1',
  evidence='SRC ColorPref.java:199-206')

e('ColorPref.switchSections', 'ColorPref.reloadListeners', 'EXPLICIT', 'called after loading section',
  evidence='SRC ColorPref.java:199-206')

e('ColorPref.loadSection0', 'ColorPref.loadSection0', 'LIFECYCLE', 'loads preferences for section 0',
  evidence='SRC ColorPref.java:208-215')

e('ColorPref.loadSection1', 'ColorPref.invalidateColorPreference', 'EXPLICIT', 'called for selectedColors preference',
  evidence='SRC ColorPref.java:219-220')

e('ColorPref.invalidateEverything', 'ColorPref.invalidateColorPreference', 'EXPLICIT', 'called to invalidate preferences',
  evidence='SRC ColorPref.java:243-254')

e('ColorPref.onSaveInstanceState', 'ColorPref.onSaveInstanceState', 'LIFECYCLE', 'saves instance state',
  evidence='SRC ColorPref.java:270-273')

e('ColorPref.onRestoreInstanceState', 'ColorPref.loadSection0', 'EXPLICIT', 'loads section 0 on restore',
  evidence='SRC ColorPref.java:276-284')

e('ColorPref.onRestoreInstanceState', 'ColorPref.loadSection1', 'EXPLICIT', 'loads section 1 on restore',
  evidence='SRC ColorPref.java:276-284')

# ColorPref$1 - anonymous ButtonCallback
e('ColorPref.colorChangeDialog', 'ColorPref$1.<init>', 'EXPLICIT', 'creates anonymous ButtonCallback for dialog',
  evidence='SRC ColorPref.java:179-186')

e('ColorPref$1.onNeutral', 'ColorPref$1.onNeutral', 'EXPLICIT', 'callback method for neutral button',
  evidence='SRC ColorPref.java:181-186')

# ColorPreference static field access - clinit is already called above
# ColorPreference.<init> and <clinit> are reached through static field access

# ColorUtils
e('RecyclerAdapter.bindViewHolderAsFile', 'ColorUtils.<init>', 'EXPLICIT', 'ColorUtils is a utility class accessed statically',
  evidence='SRC ColorUtils.java:16-22')

e('RecyclerAdapter.bindViewHolderAsFile', 'ColorUtils.colorizeIcons', 'CALL', 'called from adapter to colorize file type icons',
  evidence='SRC RecyclerAdapter.java:668-670')

# UNREACHABLE entries
UNREACHABLE['ColorPref.checkCustomization'] = ('framework_never_calls', 'called only from loadSection1 which has conditional execution', 'SRC ColorPref.java:226-234', 'SOURCE')
UNREACHABLE['ColorPref.invalidateColorPreference'] = ('branch_never_taken', 'called from invalidateEverything and loadSection1, both conditional', 'SRC ColorPref.java:256-268', 'SOURCE')
UNREACHABLE['ColorPreference.<init>'] = ('framework_never_calls', 'ColorPreference only has static field, no instantiation in app', 'SRC ColorPreference.java:1-25', 'SOURCE')
UNREACHABLE['ColorUtils.<init>'] = ('framework_never_calls', 'ColorUtils is a utility class used statically, constructor never called', 'SRC ColorUtils.java:18-43', 'SOURCE')
