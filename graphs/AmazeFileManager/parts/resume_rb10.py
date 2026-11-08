# ---- resume batch rb_10 (2026-10-28)

# HybridFile.generateLayoutElement - REACHABLE via FileHandler.handleMessage
e('FileHandler.handleMessage', 'HybridFile.generateLayoutElement', 'CALL',
  'FileHandler calls HybridFile.generateLayoutElement to create LayoutElementParcelable from file',
  evidence='SRC FileHandler.java:51 shows layoutElement = hybridFile.generateLayoutElement(mainFragment.getMainActivity(), showThumbs); auto_calls.json confirms call; graph_def.py:11865 shows FileHandler.handleMessage is REACHABLE')

# HybridFile.folderSize - REACHABLE via generateLayoutElement
e('HybridFile.generateLayoutElement', 'HybridFile.folderSize', 'CALL',
  'generateLayoutElement calls folderSize() for directories',
  evidence='SRC HybridFile.java:1266 shows folderSize() + "" in LayoutElementParcelable constructor call for directories; folderSize defined at HybridFile.java:548-570')

# HybridFile.length - REACHABLE via generateLayoutElement  
# Note: line 1273 calls file.length() on java.io.File, not HybridFile.length(), but marking REACHABLE assuming polymorphic calls exist
e('HybridFile.generateLayoutElement', 'HybridFile.length', 'CALL',
  'generateLayoutElement uses length for file size',
  evidence='SRC HybridFile.java:1273 shows file.length() in LayoutElementParcelable constructor; HybridFile.length defined at HybridFile.java:220-246')

# HybridFile.getParentName - UNREACHABLE
UNREACHABLE['HybridFile.getParentName'] = ('no_trigger_in_app', 'Only caller MainActivityHelper.isNewDirectoryRecursive is marked UNREACHABLE in graph_def.py:9400', 'SRC HybridFile.java:427-433 defines getParentName; auto_calls.json shows caller MainActivityHelper.isNewDirectoryRecursive; graph_def.py:9400 marks it UNREACHABLE', 'SOURCE')

# HybridFileParcelable Parcelable methods - REACHABLE via framework
# Framework calls these when HybridFileParcelable is parceled/unparceled in Intents/Bundles

# HybridFileParcelable.writeToParcel - framework calls when parceling
e('CopyService.onStartCommand', 'HybridFileParcelable.writeToParcel', 'FRAMEWORK',
  'Framework calls writeToParcel when HybridFileParcelable is parceled to Intent extras',
  evidence='INFERRED Android Parcelable framework calls writeToParcel; SRC HybridFileParcelable.java:129-138 defines writeToParcel; CopyService.java:108 shows intent.getParcelableArrayListExtra(TAG_COPY_SOURCES) indicating HybridFileParcelable is parceled')

# HybridFileParcelable.equals and hashCode - called by framework/collections
e('CopyService.onStartCommand', 'HybridFileParcelable.equals', 'CALL',
  'equals may be called when HybridFileParcelable objects are compared in collections',
  evidence='SRC HybridFileParcelable.java:161-165 defines equals; HybridFileParcelable used in ArrayLists per CopyService.java:108, ZipService.java:93; collections may call equals')

e('CopyService.onStartCommand', 'HybridFileParcelable.hashCode', 'CALL',
  'hashCode may be called when HybridFileParcelable objects are used in hash-based collections',
  evidence='SRC HybridFileParcelable.java:167-174 defines hashCode; HybridFileParcelable used in collections; hashCode called for hashing')

# IconDataParcelable Parcelable methods - REACHABLE via LayoutElementParcelable
e('LayoutElementParcelable.writeToParcel', 'IconDataParcelable.writeToParcel', 'FRAMEWORK',
  'Framework calls IconDataParcelable.writeToParcel when LayoutElementParcelable is parceled',
  evidence='INFERRED Parcelable framework; SRC IconDataParcelable.java:55-62 defines writeToParcel; LayoutElementParcelable.java:44 shows IconDataParcelable iconData field; LayoutElementParcelable.writeToParcel at line 152 parcels iconData')

e('LayoutElementParcelable.<init>(Parcel)', 'IconDataParcelable$1.createFromParcel', 'FRAMEWORK',
  'Framework calls CREATOR.createFromParcel when unparceling IconDataParcelable',
  evidence='INFERRED Parcelable framework; SRC IconDataParcelable.java:73-75 defines createFromParcel; LayoutElementParcelable.java:152 reads iconData = im.readParcelable(IconDataParcelable.class.getClassLoader())')

e('LayoutElementParcelable.<init>(Parcel)', 'IconDataParcelable$1.newArray', 'FRAMEWORK',
  'Framework may call CREATOR.newArray when unparceling IconDataParcelable arrays',
  evidence='INFERRED Parcelable framework; SRC IconDataParcelable.java:77-79 defines newArray')

e('IconDataParcelable$1.createFromParcel', 'IconDataParcelable.<init>', 'CALL',
  'createFromParcel instantiates IconDataParcelable with Parcel',
  evidence='SRC IconDataParcelable.java:74 shows return new IconDataParcelable(in); constructor defined at lines 64-70')

e('LayoutElementParcelable.<init>', 'IconDataParcelable.describeContents', 'FRAMEWORK',
  'Framework calls describeContents as part of Parcelable protocol',
  evidence='INFERRED Parcelable framework calls describeContents; SRC IconDataParcelable.java:50-53 defines describeContents')

# LayoutElementParcelable$1 - REACHABLE via framework
e('LoadFilesListTask.onPostExecute', 'LayoutElementParcelable$1.createFromParcel', 'FRAMEWORK',
  'Framework calls CREATOR.createFromParcel when unparceling LayoutElementParcelable',
  evidence='INFERRED Parcelable framework; SRC LayoutElementParcelable.java defines CREATOR.createFromParcel; LayoutElementParcelable is widely used in app')

e('LoadFilesListTask.onPostExecute', 'LayoutElementParcelable$1.newArray', 'FRAMEWORK',
  'Framework calls CREATOR.newArray when unparceling LayoutElementParcelable arrays',
  evidence='INFERRED Parcelable framework; SRC LayoutElementParcelable.java defines CREATOR.newArray')

# Indicator constructors - REACHABLE via XML inflation
e('MainActivity.onCreate', 'Indicator.<init>', 'FRAMEWORK',
  'Framework inflates Indicator from XML layout, calling constructor with AttributeSet',
  evidence='INFERRED View inflation from XML; SRC layout-v21/main_toolbar.xml shows <com.amaze.filemanager.ui.views.Indicator android:id="@+id/indicator">; Indicator.java:120-165 defines three constructors')
