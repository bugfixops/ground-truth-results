STATUS: RUNNING 17:57

Batch 084 (LABEL helper): com.ichi2.libanki.Collection, part 1 of 2, 40 methods from graphs/AnkiDroid/scratch/batches/batch_084.txt. Source: com/ichi2/libanki/Collection.java (declarations at lines 129-1651). Every callsite was found with grep -rn over the app source root and printed with sed -n before the row was written. Most methods are reached through automatic CALL edges from app code (for example DeckTask, CardContentProvider, CardBrowser, Syncer); those routes are not repeated as e() calls. Gate ids: none needed; this batch writes no e() edges. UNREACHABLE entries are in graphs/AnkiDroid/parts/label_084.py.

| item | label | kind | reason | source |
|---|---|---|---|---|
| Collection.<init>(Context,DB,String) | UNREACHABLE | no_trigger_in_app | The 3-argument constructor is called by no code. The only creation of a Collection in the app is Storage.Collection, which calls the 5-argument constructor (Storage.java:63). A grep for new Collection( finds no other call. | com/ichi2/libanki/Collection.java:129-131; com/ichi2/libanki/Storage.java:63 |
| Collection.<init>(Context,DB,String,boolean) | UNREACHABLE | no_trigger_in_app | The 4-argument constructor is called only from the 3-argument constructor (Collection.java:130), and that constructor has no caller (see the row above). The 5-argument constructor it chains to is the one Storage uses. | com/ichi2/libanki/Collection.java:129-135; com/ichi2/libanki/Storage.java:63 |
