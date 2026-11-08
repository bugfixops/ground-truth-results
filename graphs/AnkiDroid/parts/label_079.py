# AnkiDroid batch 079 (LABEL helper). 38 methods; the full row list is in graphs/AnkiDroid/parts/label_079.md.
# This part writes only UNREACHABLE entries (8, all no_trigger_in_app) and no e() edges (0).
# Source paths are relative to final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/java.
# Text is repeated inline; no module-level names are defined.

UNREACHABLE['BitmapUtil.<init>'] = ('no_trigger_in_app', 'BitmapUtil has only static methods and no explicit constructor. A grep for new BitmapUtil under the source root finds no call site, so the default constructor is never invoked.', 'SRC com/ichi2/utils/BitmapUtil.java:35-93', 'SOURCE')

UNREACHABLE['ExifUtil.<init>'] = ('no_trigger_in_app', 'ExifUtil has only the static method rotateFromCamera and no explicit constructor. A grep for new ExifUtil under the source root finds no call site.', 'SRC com/ichi2/utils/ExifUtil.java:29-55', 'SOURCE')

UNREACHABLE['HttpUtility.<init>'] = ('no_trigger_in_app', 'HttpUtility has only the static method postReport and no explicit constructor. A grep for new HttpUtility under the source root finds no call site.', 'SRC com/ichi2/utils/HttpUtility.java:18-43', 'SOURCE')

UNREACHABLE['HttpUtility.postReport'] = ('no_trigger_in_app', 'postReport posts feedback reports with DefaultHttpClient. A grep for postReport under the source root finds no call site, so no in-app trigger reaches it.', 'SRC com/ichi2/utils/HttpUtility.java:19-42', 'SOURCE')

UNREACHABLE['LanguageUtil.<init>'] = ('no_trigger_in_app', 'LanguageUtil has only static members and no explicit constructor. A grep for new LanguageUtil under the source root finds no call site.', 'SRC com/ichi2/utils/LanguageUtil.java:27-67', 'SOURCE')

UNREACHABLE['LanguageUtil.getLocale()'] = ('no_trigger_in_app', 'The only caller under the source root is Utils.fmtPercentage(Double,int) at line 229. That method is called only from fmtPercentage(Double) at Utils.java:224, and no code under the source root calls fmtPercentage(Double), so the chain has no in-app trigger.', 'SRC com/ichi2/utils/LanguageUtil.java:41-43; SRC com/ichi2/libanki/Utils.java:223-232', 'SOURCE')

UNREACHABLE['DiffEngine$DiffAction.equals'] = ('no_trigger_in_app', 'The equals override runs only when a DiffAction is compared with equals, or through a collection contains, remove or indexOf. A grep under the source root finds no such comparison: the contains and remove calls act on Long sets and iterators, and DiffAction objects are compared by reference only.', 'SRC com/ichi2/utils/DiffEngine.java:1158-1164', 'SOURCE')

UNREACHABLE['DiffEngine$DiffAction.toString'] = ('no_trigger_in_app', 'The toString override runs only when a DiffAction is converted to a String implicitly (string concatenation, String.valueOf, print or log). A grep under the source root finds no such conversion; the diff results are read through the operation and text fields only.', 'SRC com/ichi2/utils/DiffEngine.java:1145-1148', 'SOURCE')
