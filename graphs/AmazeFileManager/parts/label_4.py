# ---- Helper 4 label part (2026-10-27)

# AppDataParcelable edges
e('AppListLoader.loadInBackground', 'AppDataParcelable.<init>(String,String,String,String,String,long,long)', 'INVOKE_SPECIAL', 
  'AppListLoader creates AppDataParcelable for each installed app',
  evidence='SRC AppListLoader.java:70-76')

e('AppListLoader.loadInBackground', 'AppDataParcelable$AppDataSorter.<init>', 'INVOKE_SPECIAL',
  'AppListLoader sorts app list using AppDataSorter',
  evidence='SRC AppListLoader.java:79')

# IconDataParcelable edges
e('CompressedObjectParcelable.<init>', 'IconDataParcelable.<init>(int,int)', 'INVOKE_SPECIAL',
  'CompressedObjectParcelable creates icon data for compressed file entries',
  evidence='SRC CompressedObjectParcelable.java:54-55')

e('LayoutElementParcelable.<init>', 'IconDataParcelable.<init>(int,String,int)', 'INVOKE_SPECIAL',
  'LayoutElementParcelable creates icon data for cloud files',
  evidence='SRC LayoutElementParcelable.java:91')
  
e('LayoutElementParcelable.<init>', 'IconDataParcelable.<init>(int,int)', 'INVOKE_SPECIAL',
  'LayoutElementParcelable creates icon data for regular files',
  evidence='SRC LayoutElementParcelable.java:93')

e('IconDataParcelable$1.createFromParcel', 'IconDataParcelable.<init>(Parcel)', 'INVOKE_SPECIAL',
  'CREATOR.createFromParcel calls Parcel constructor',
  evidence='SRC IconDataParcelable.java:72')

# AppDataParcelable$1 (CREATOR) edges  
e('AppDataParcelable$1.createFromParcel', 'AppDataParcelable.<init>(Parcel)', 'INVOKE_SPECIAL',
  'CREATOR.createFromParcel calls private Parcel constructor',
  evidence='SRC AppDataParcelable.java:57-58')

# UNREACHABLE methods from this batch
UNREACHABLE_PART_4 = {
    # Manifest (Android framework class, never instantiated)
    'Manifest.<init>': ('framework_never_calls', 'Android framework Manifest class is never instantiated, only holds nested permission constants class', 'INFERRED source not in dataset', 'INFERRED'),
    
    # Manifest$permission (Android framework class, never instantiated)
    'Manifest$permission.<init>': ('framework_never_calls', 'Android framework Manifest.permission class holds only static constants, never instantiated', 'INFERRED source not in dataset', 'INFERRED'),
    
    # AppDataParcelable - <clinit> is unreachable (no static initializers in the class)
    'AppDataParcelable.<clinit>': ('no_trigger_in_app', 'Class has no static initializer block and CREATOR field is initialized inline', 'SRC AppDataParcelable.java:13-67 shows no static{} block', 'SOURCE'),
}
