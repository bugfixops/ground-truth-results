# Markor — ROUTES notes

Source rows: `graphs/Markor/verification.csv` path rows, in file order
(`route_01` = first path row). `env_kinds`/`state_kinds` copied verbatim
from `graphs/Markor/out/methods.csv` for each method. Fixture paths below
are relative to `work-emulator/fixtures/` (so `Documents/notes.md` means
`work-emulator/fixtures/Documents/notes.md`); every listed fixture was
checked to exist. `setup` on every row is the apps.csv setup text for
Markor verbatim: "push fixtures/Documents; first-run tutorial can trap
a tool". Package: `net.gsantner.markor_test`.

## Permissions

Only one route carries an ENV permission gate. The trigger-graph edges
for route_05 say "the runtime storage permission is not granted yet" /
"The storage permission is missing" without naming a constant; the
constant is grounded in app source: `GsContextUtils.
requestExternalStoragePermission` (GsContextUtils.java:2401) requests
`Manifest.permission.WRITE_EXTERNAL_STORAGE`, which is declared in
`app/src/main/AndroidManifest.xml` (alongside READ_EXTERNAL_STORAGE).
So route_05 lists WRITE_EXTERNAL_STORAGE only. MANAGE_EXTERNAL_STORAGE
is also declared but is a special all-files access, not a dangerous
runtime permission, so it is not listed. No other route has a permission
ENV gate; INTERNET / ACCESS_NETWORK_STATE are install-time and never
listed (neither appears in any route's gates here). Manifest checked:
main manifest at `final_java_only/Markor/app/Markor-#v2.16.1/app/src/
main/AndroidManifest.xml` declares BIND_REMOTEVIEWS, INTERNET,
MANAGE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, REQUEST_INSTALL_PACKAGES,
WRITE_EXTERNAL_STORAGE.

## Per-row judgments

- route_01 (ActionButtonSettingsActivity.lambda$saveNewOrder$0): pure
  settings navigation (More -> Settings -> action-button order, leave
  screen). No file, no permission. Scripted.
- route_02 (SyntaxHighlighterBase.isFixupOverlap): tap a file in the
  notebook list, open the editor, type text. Fixture Documents/notes.md
  is the tapped notebook file. Scripted.
- route_03 (SyntaxHighlighterBase$1.draw): todo-page format-menu switch
  to the key-value format (state=file). Fixture Documents/todo.txt is
  the open todo document; the format is chosen from the format menu, so
  no key-value-specific fixture file is needed. Scripted.
- route_04 (DocumentShareIntoFragment...getLinkTitle): other-app SEND
  share entry. Scripted by sending an ACTION_SEND intent with text
  containing a web link (Patterns.WEB_URL guard); no file fixture.
  Scripted.
- route_05 (StoragePermissionActivity.processPermissionState): the
  storage-permission flow. Permission WRITE_EXTERNAL_STORAGE (see
  above). Scripted by starting with the permission revoked, answering
  the system dialog (Allow or Deny both reach
  onRequestPermissionsResult), and confirming processPermissionState.
  No file fixture. Scripted.
- route_06 (FlexmarkKatexExtension$KatexInlineMath.getText): notebook
  toolbar copy-to-clipboard needs a selected file. Fixture
  Documents/notes.md is the selected file. Scripted.
- route_07 (DocumentEditAndViewFragment$2.lambda$search$0): search in
  preview (view) mode on the todo/quick-note page (state=session).
  Fixture Documents/todo.txt is the open document. Scripted.
- route_08 (FileSearchEngine.isEncryptedFile): notebook toolbar filter
  search over the notebook directory. Fixture Documents/notes.md stands
  for the searched notebook contents (the setup pushes the whole
  Documents folder, so the search scans all of it). Scripted.
- route_09 (CsvConfig.findChar): CSV-format document (state=file).
  Fixture Documents/table.csv is the exact-format match. Scripted.
- route_10 (WikitextLinkResolver.findNotebookRootDir): todo-page
  insert-image/link browse in the wikitext branch (state=file).
  Fixture Documents/todo.txt is the open todo document; the file picked
  in the browse dialog can be any pushed Documents file and is not
  pinned by the route. Scripted.
- route_11 (WikitextLinkResolver.wikitextPagePathToRelativeFilePath):
  quick-note page wikitext button (state=file). The quick-note file is
  created by the app on demand and the wikitext format is chosen from
  the format menu, so no pushed fixture is needed. Scripted.
- route_12 (WrFilesWidgetFactory.getLoadingView): notebook widget.
  Scripted via launcher UI automation: place the Markor files widget,
  let the launcher bind the widget service, read the loading view.
  Hard but scriptable; no file fixture (the loading view is fixed).
  Scripted.
- route_13 (TodoWidgetRemoteViewsFactory.getCount): todo widget.
  Scripted via launcher UI automation: place the todo widget, let the
  service run onDataSetChanged, read the count. The count method runs
  regardless of item count, so no file fixture is pinned. Scripted.
- route_14 (AppSettings.getAttachmentFolder): todo-page action-bar
  long press -> insert camera photo -> camera result listener
  (env=other_app). Fixture Documents/todo.txt is the open todo
  document. Scripted by driving the emulator camera app (virtual
  camera) and accepting the capture result. Scripted.
- route_15 (DocumentShareIntoFragment...lambda$hasLinks$1): other-app
  SEND share entry, fragment creation with null saved state. Scripted
  by sending an ACTION_SEND intent; no file fixture. Scripted.
- route_16 (MarkorContextUtils.getIntentFile): todo-widget tap ->
  OpenFromShortcutOrWidgetActivity. Scripted via launcher UI automation
  (place widget, tap it); no file fixture. Scripted.
- route_17 (WrWidgetConfigure$1.<init>): widget configure activity
  started from outside the package. Scripted via launcher widget
  configuration flow; no file fixture. Scripted.
- route_18 (GsPreferenceFragmentBase.tintPrefIconsRecursive): More page
  preference fragment. No file, no permission. Scripted.
- route_19 (GsFileBrowserListAdapter.createDirectoryHere): notebook
  menu move-or-copy -> folder dialog -> new-folder dialog.
  Fixture Documents/notes.md is the selected notebook item being
  moved/copied. Scripted.
- route_20 (AppSettings.lambda$getPopularDocumentsSorted$1): todo-page
  info dialog with the recents checkbox ticked. Fixture
  Documents/todo.txt is the open todo document. Scripted.
- route_21 (SyntaxHighlighterBase$SpanGroup.compareTo): todo-page
  search producing matches. Fixture Documents/todo.txt is the searched
  document (contains searchable text). Scripted.
- route_22 (GsFileBrowserListAdapter.lambda$scrollToAndFlash$3):
  notebook folder tap -> load folder -> scroll-to-and-flash chain.
  Fixture Documents/notes.md stands for the notebook contents being
  listed/scrolled. Scripted.
- route_23 (GsSharedPreferencesPropertyBackend.getStringListOne):
  cold-start notebook creation reading the popular-files list. The
  method runs on the preference read regardless of list contents, so no
  file fixture is pinned. Scripted.
- route_24 (GsSharedPreferencesPropertyBackend.gp): cold-start
  AppSettings init (editor colours). No file. Scripted.
- route_25 (GsSharedPreferencesPropertyBackend.rstr): cold-start
  AppSettings init (int preference read). No file. Scripted.
- route_26 (GsContextUtils.<init>): cold-start AppSettings init
  (context utils singleton). No file. Scripted.
- route_27 (GsContextUtils.setChooserTitle): cold-start AppSettings
  init (MarkorContextUtils constructor). No file. Scripted.
- route_28 (GsSharedPreferencesPropertyBackend.getInt): cold-start
  AppSettings init (int preference read). No file. Scripted.
- route_29 (GsSharedPreferencesPropertyBackend.rcolor): cold-start
  AppSettings init (editor colour read). No file. Scripted.
- route_30 (GsSharedPreferencesPropertyBackend.<init>): cold-start
  AppSettings init (preference backend creation). No file. Scripted.

## Status summary

30 rows, 30 scripted, 0 unscriptable (0%, within the 10% limit). No
route was marked unscriptable: widget placement (route_12, 13, 16, 17),
the camera result (route_14), and other-app share intents (route_04,
15) are all creatable on an AOSP emulator via launcher UI automation,
the virtual camera app, and adb-sent intents respectively — hard, but
not unscriptable. No fixture needed by any route is missing, so no
fixture-missing row exists.

## Blocked items

None. No permission named in gate prose is absent from the manifest
(the only gated permission, WRITE_EXTERNAL_STORAGE, is declared), and
no needed fixture is missing.
