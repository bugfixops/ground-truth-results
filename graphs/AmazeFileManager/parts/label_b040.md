STATUS: RUNNING 23:28

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| ImmutableEntry.<init> | REACHABLE | | Constructed in SearchTextTask.doInBackground | SRC SearchTextTask.java:67-69 |
| ImmutableEntry.getKey | REACHABLE | | Called in SearchTextTask.onPostExecute | SRC SearchTextTask.java:88 |
| ImmutableEntry.getValue | REACHABLE | | Called in SearchTextTask.onPostExecute | SRC SearchTextTask.java:88 |
| ImmutableEntry.setValue | UNREACHABLE | no_trigger_in_app | Always throws UnsupportedOperationException, no caller attempts it | SRC ImmutableEntry.java:48-50 |
| Icons.<clinit> | REACHABLE | | Static initializer called at class load | SRC Icons.java:46-48 |
| Icons.<init> | UNREACHABLE | no_trigger_in_app | Icons has only static members, no instance ever created | SRC Icons.java:29 |
| Icons.checkType | REACHABLE | | Called from Icons.getTypeOfFile | SRC Icons.java:269-273, 278 |
| Icons.getTypeOfFile | REACHABLE | | Called from LayoutElementParcelable, CompressedObjectParcelable, FileUtils | SRC LayoutElementParcelable.java:79, CompressedObjectParcelable.java:53, FileUtils.java:539 |
| Icons.loadMimeIcon | REACHABLE | | Called from LayoutElementParcelable, CompressedObjectParcelable | SRC LayoutElementParcelable.java:80, CompressedObjectParcelable.java:55 |
| Icons.put | REACHABLE | | Called from Icons.putKeys | SRC Icons.java:35-37 |
| Icons.putKeys | REACHABLE | | Called from Icons.<clinit> | SRC Icons.java:38-40 |
| HybridFileParcelable.<clinit> | REACHABLE | | Static initializer for CREATOR field | SRC HybridFileParcelable.java:105 |
| HybridFileParcelable.<init>(Parcel) | REACHABLE | | Called from HybridFileParcelable$1.createFromParcel | SRC HybridFileParcelable.java:108 |
| HybridFileParcelable.<init>(String) | REACHABLE | | Called from AppsAdapter, HiddenAdapter, multiple locations | SRC AppsAdapter.java:188, HiddenAdapter.java:84-86 |
| HybridFileParcelable.<init>(String,String,long,long,boolean) | REACHABLE | | Called from LayoutElementParcelable, RootHelper, HybridFile | SRC LayoutElementParcelable.java:134, RootHelper.java:116-118, HybridFile.java:747 |
| HybridFileParcelable.describeContents | REACHABLE | | Framework calls for Parcelable contract | INFERRED from Parcelable mechanism at MainActivity.java:313 |
| HybridFileParcelable.equals | REACHABLE | | Used in collection contains checks | INFERRED from List/Set contains operations |
| HybridFileParcelable.getDate | REACHABLE | | Getter accessed throughout app | INFERRED from HybridFileParcelable usage pattern |
| HybridFileParcelable.getLink | REACHABLE | | Getter accessed for symlink display | INFERRED from HybridFileParcelable usage pattern |
| HybridFileParcelable.getMode | REACHABLE | | Getter accessed from parent HybridFile methods | INFERRED from HybridFile.compareFiles usage |
| HybridFileParcelable.getName | REACHABLE | | Override of parent method, polymorphically called | SRC HybridFileParcelable.java:35-38 |
| HybridFileParcelable.getPath | REACHABLE | | Getter accessed throughout app | INFERRED from HybridFileParcelable usage pattern |
| HybridFileParcelable.getPermission | REACHABLE | | Getter accessed for permission display | INFERRED from HybridFileParcelable usage pattern |
| HybridFileParcelable.getSize | REACHABLE | | Getter accessed for size display | INFERRED from HybridFileParcelable usage pattern |
| HybridFileParcelable.hashCode | REACHABLE | | Used in HashMap put operations | INFERRED from HashMap/HashSet usage |
| HybridFileParcelable.isDirectory | REACHABLE | | Checked throughout app | INFERRED from HybridFileParcelable usage pattern |
| HybridFileParcelable.isHidden | REACHABLE | | Checks if filename starts with dot | SRC HybridFileParcelable.java:77 |
| HybridFileParcelable.setDate | REACHABLE | | Called from HybridFile.listFiles | SRC HybridFile.java:751 |
| HybridFileParcelable.setDirectory | REACHABLE | | Called from HybridFile.listFiles | SRC HybridFile.java:750 |
| HybridFileParcelable.setLink | REACHABLE | | Called from FileUtils.putFileInArrayList | SRC FileUtils.java:941 |
| HybridFileParcelable.setName | REACHABLE | | Called after construction in multiple locations | SRC LayoutElementParcelable.java:137, RootHelper.java:119 |
| HybridFileParcelable.setPermission | REACHABLE | | Called from HybridFile.listFiles | SRC HybridFile.java:753 |
| HybridFileParcelable.setSize | REACHABLE | | Called from HybridFile.listFiles | SRC HybridFile.java:752 |
| HybridFileParcelable.toString | UNREACHABLE | no_trigger_in_app | Not explicitly called, only implicit via debugger | SRC HybridFileParcelable.java:139-145 |
| HybridFileParcelable.writeToParcel | REACHABLE | | Framework calls for Parcelable contract | INFERRED from Parcelable mechanism at MainActivity.java:313 |
| HybridFileParcelable$1.<init> | UNREACHABLE | framework_never_calls | Anonymous CREATOR constructor called once at class load | SRC HybridFileParcelable.java:105 |
| HybridFileParcelable$1.createFromParcel | REACHABLE | | Framework calls CREATOR.createFromParcel | INFERRED from Parcelable mechanism at MainActivity.java:313 |
| HybridFileParcelable$1.newArray | REACHABLE | | Framework calls CREATOR.newArray | INFERRED from Parcelable mechanism at MainActivity.java:313 |

STATUS: DONE 23:37
