# LibreTorrent — lessons (what found real errors)

- Trace a SAF/file:// dispatch back to where the Uri is stored: the resolver picks SafFsModule only for scheme content, and every save path LibreTorrent writes is file://, so three final routes (5, 20, 22) and two first-draw routes are WRONG at that one dispatch step (`FsModuleResolverImpl.java:42-49`, `SafFileSystem.java:197`, `StorageSettingsFragment.java:267`).
- A REGISTER edge is not a route: 85 of the last 86 UNRESOLVED methods had a REGISTER edge from a REACHABLE caller but no delivery edge (Handler post, AlarmManager, TextWatcher, Observable, RxJava, click, ActivityResult); adding the delivery edge, cited to the printed registration, was enough (part b121).
- Check 2 checks only framework citations, so wrong app line numbers pass it: 17 hand-written select-tag edges cited lines from an older SelectTagDialog.java, 6 of them past the end of the 195-line file. Compare cited ranges with the file length whenever a part puts old edges on new routes.
- Read which object a call really receives: `setFragment(AppearanceSettingsFragment.newInstance(), ...)` cannot create NetworkSettingsFragment (route 12), and an interface call resolved by bytecode to one implementation (`SelectTagActivity.onFragmentFinished` from every dialog) can join screens that never meet.
- Count STATE honestly: a row tap needs a row, and a row needs data that the route must create; with no earlier step creating a tag, the select-tag routes are UNCLEAR, not CORRECT.
- Generated-code citations are a citation-form problem, not a route problem: 134 check-4 lines cited data-binding/Room files that are not in the upload, and rewriting them as INFERRED generated code (with the 7 try-with-resources closes cited by block) took check 4 from 141 to 0 without changing a label.

## Re-audit lessons (Kiro, November 2026)

- Clearing a baseline gate can move many best routes onto an outside entry that was cheaper before; after every baseline edit, count the methods whose best route carries an env gate, not only the cleared texts.
- A gate edit changes the edge id (the id hashes the gate texts), so device route files and verification paths that name edge ids go stale; map old to new ids by src, dst and kind before a dry run.
- Check anonymous-class numbers with javap: javac numbers them in source order, and one skipped number shifts every later class.

- A system broadcast delivered to a receiver the app registered is a standard edge with an env system_event gate, not non_standard.
- Framework dispatch (fragment lifecycle, View clicks, dialog callbacks) is standard; the library class of a route should come from a real library step (FragmentContainerView or ViewModelProvider reflection, data binding, Room, WorkManager, Rx).
