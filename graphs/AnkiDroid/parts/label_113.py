# AnkiDroid batch 113 (LABEL helper). wildplot rendering: Integral, LegendDrawable, Lines, LinesPoints (40 methods).
# The full row list is in graphs/AnkiDroid/parts/label_113.md. This batch has no e() edges.
# Each UNREACHABLE entry repeats its text inline (no module-level names, no imports).

UNREACHABLE['Integral.<init>(Function2D,PlotSheet,double,double)'] = ('no_trigger_in_app', "Class Integral is never instantiated in the app. grep -rn -w Integral over src/main/java finds only Integral.java (class at line 29, constructors at lines 59 and 75). No new Integral(...) exists, so this constructor has no caller.", 'SRC com/wildplot/android/rendering/Integral.java:59-65; com/wildplot/android/rendering/Integral.java:29', 'SOURCE')

UNREACHABLE['Integral.<init>(Function2D,Function2D,PlotSheet,double,double)'] = ('no_trigger_in_app', "Same grep result as the first Integral constructor: the class is never instantiated, so this constructor has no caller.", 'SRC com/wildplot/android/rendering/Integral.java:75-82', 'SOURCE')

UNREACHABLE['Integral.abortAndReset'] = ('no_trigger_in_app', "Empty body. No Integral object exists to receive the call. The only abortAndReset call in src/main/java is DrawableContainer.java:62, inside DrawableContainer.abortAndReset, which has no caller. PlotSheet.abortAndReset has no caller either.", 'SRC com/wildplot/android/rendering/Integral.java:127-130; com/wildplot/android/rendering/DrawableContainer.java:59-63; com/wildplot/android/rendering/PlotSheet.java:711-714', 'SOURCE')

UNREACHABLE['Integral.isClusterable'] = ('no_trigger_in_app', "Class never instantiated. The dispatch sites PlotSheet.java:500 and :519 only receive drawables that were added to a sheet, and no Integral is ever added.", 'SRC com/wildplot/android/rendering/Integral.java:132-135; com/wildplot/android/rendering/PlotSheet.java:500, 519', 'SOURCE')

UNREACHABLE['Integral.isCritical'] = ('no_trigger_in_app', "Class never instantiated. The call sites are PlotSheet.java:501, 507, 520 and 526, on drawables from a sheet; no Integral is ever added to a sheet.", 'SRC com/wildplot/android/rendering/Integral.java:137-140; com/wildplot/android/rendering/PlotSheet.java:501, 520', 'SOURCE')

UNREACHABLE['Integral.isOnFrame'] = ('no_trigger_in_app', "Class never instantiated. The call sites PlotSheet.java:357 and :499 only see drawables already in a sheet.", 'SRC com/wildplot/android/rendering/Integral.java:122-124; com/wildplot/android/rendering/PlotSheet.java:357, 499', 'SOURCE')

UNREACHABLE['Integral.paint'] = ('no_trigger_in_app', "Class never instantiated. The paint call sites PlotSheet.java:366 and :473 paint only drawables already in a sheet.", 'SRC com/wildplot/android/rendering/Integral.java:88-116; com/wildplot/android/rendering/PlotSheet.java:366, 473', 'SOURCE')

UNREACHABLE['Integral.setColor'] = ('no_trigger_in_app', "Class never instantiated, so no receiver can have type Integral. The 79 setColor( lines in src/main/java were grepped; the legend calls are ChartBuilder.java:184-186 on LegendDrawable receivers, and none is on an Integral.", 'SRC com/wildplot/android/rendering/Integral.java:48-50; com/ichi2/anki/stats/ChartBuilder.java:184-186', 'SOURCE')

UNREACHABLE['LegendDrawable.abortAndReset'] = ('no_trigger_in_app', "Empty body. The only abortAndReset call in src/main/java is DrawableContainer.java:62, inside DrawableContainer.abortAndReset, which has no caller. PlotSheet.abortAndReset has no caller. No path reaches LegendDrawable.abortAndReset.", 'SRC com/wildplot/android/rendering/LegendDrawable.java:43-46; com/wildplot/android/rendering/DrawableContainer.java:59-63; com/wildplot/android/rendering/PlotSheet.java:711-714', 'SOURCE')

UNREACHABLE['LegendDrawable.isCritical'] = ('branch_never_taken', "isCritical is called only inside clusterable branches: PlotSheet.java:501 and :507 (on-frame, guarded by isClusterable at :500), and PlotSheet.java:520 and :526 (off-frame, guarded by isClusterable at :519). LegendDrawable.isOnFrame is false (LegendDrawable.java:38-41) and LegendDrawable.isClusterable is false (LegendDrawable.java:48-51). The guard at PlotSheet.java:519 is therefore never true for a LegendDrawable, so isCritical is never called on one.", 'SRC com/wildplot/android/rendering/LegendDrawable.java:53-56; com/wildplot/android/rendering/PlotSheet.java:500-501, 507, 519-520, 526', 'SOURCE')

UNREACHABLE['Lines.abortAndReset'] = ('no_trigger_in_app', "Empty body. The only abortAndReset call in src/main/java is DrawableContainer.java:62, inside DrawableContainer.abortAndReset, which has no caller. PlotSheet.abortAndReset has no caller. No path reaches Lines.abortAndReset.", 'SRC com/wildplot/android/rendering/Lines.java:128-132; com/wildplot/android/rendering/DrawableContainer.java:59-63; com/wildplot/android/rendering/PlotSheet.java:711-714', 'SOURCE')

UNREACHABLE['Lines.drawPoint'] = ('no_trigger_in_app', "The only mention of a call is the commented line Lines.java:95. grep for drawPoint in src/main/java finds no live call of Lines.drawPoint.", 'SRC com/wildplot/android/rendering/Lines.java:111-118; com/wildplot/android/rendering/Lines.java:95', 'SOURCE')

UNREACHABLE['Lines.unsetShadow'] = ('no_trigger_in_app', "No call in src/main/java. Lines.java:98 is the commented line g.unsetShadow(). grep for unsetShadow finds only the declarations at Lines.java:170 and GraphicsWrap.java:177.", 'SRC com/wildplot/android/rendering/Lines.java:170-172; com/wildplot/android/rendering/Lines.java:97-99; com/wildplot/android/rendering/graphics/wrapper/GraphicsWrap.java:177', 'SOURCE')

UNREACHABLE['LinesPoints.<init>'] = ('no_trigger_in_app', "Class never instantiated. A word-boundary grep over src/main/java for Integral and LinesPoints finds LinesPoints only in LinesPoints.java and in the javadoc of Lines.java (lines 24-25). No new LinesPoints(...) exists.", 'SRC com/wildplot/android/rendering/LinesPoints.java:42-46; com/wildplot/android/rendering/Lines.java:24-25', 'SOURCE')

UNREACHABLE['LinesPoints.abortAndReset'] = ('no_trigger_in_app', "Empty body. The class is never instantiated. The only abortAndReset call in src/main/java is DrawableContainer.java:62, inside an uncalled method.", 'SRC com/wildplot/android/rendering/LinesPoints.java:93-97; com/wildplot/android/rendering/DrawableContainer.java:59-63', 'SOURCE')

UNREACHABLE['LinesPoints.drawPoint'] = ('no_trigger_in_app', "The only call of LinesPoints.drawPoint is LinesPoints.java:64, inside LinesPoints.paint, which is never reached because the class is never instantiated. PointDrawer2D.java:52 and the Whiteboard.java calls are on other classes.", 'SRC com/wildplot/android/rendering/LinesPoints.java:76-83; com/wildplot/android/rendering/LinesPoints.java:64', 'SOURCE')

UNREACHABLE['LinesPoints.isClusterable'] = ('no_trigger_in_app', "Class never instantiated. The dispatch sites PlotSheet.java:500 and :519 only receive drawables added to a sheet.", 'SRC com/wildplot/android/rendering/LinesPoints.java:99-102; com/wildplot/android/rendering/PlotSheet.java:500, 519', 'SOURCE')

UNREACHABLE['LinesPoints.isCritical'] = ('no_trigger_in_app', "Class never instantiated. The call sites PlotSheet.java:501 and :520 only see drawables added to a sheet.", 'SRC com/wildplot/android/rendering/LinesPoints.java:104-107; com/wildplot/android/rendering/PlotSheet.java:501, 520', 'SOURCE')

UNREACHABLE['LinesPoints.isOnFrame'] = ('no_trigger_in_app', "Class never instantiated. The call sites PlotSheet.java:357 and :499 only see drawables added to a sheet.", 'SRC com/wildplot/android/rendering/LinesPoints.java:89-91; com/wildplot/android/rendering/PlotSheet.java:357, 499', 'SOURCE')

UNREACHABLE['LinesPoints.paint'] = ('no_trigger_in_app', "Class never instantiated. The paint call sites PlotSheet.java:366 and :473 only paint drawables added to a sheet.", 'SRC com/wildplot/android/rendering/LinesPoints.java:51-67; com/wildplot/android/rendering/PlotSheet.java:366, 473', 'SOURCE')
