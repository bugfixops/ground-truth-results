# L5 summary — Room residuals + full-res greps + flagged-UNREACHABLE evidence

Branch `work-2026-10-31`, repo `bugfixops/ground-truth-results`, LibreTorrent
ONLY. No device work, no pushes, no branch edits, no tick written.
Verdict file: `phase3/verdicts/L5/batch48_batch4.md` (task-3 rows only).
Saved greps: `phase3/greps/L5/*.txt` (command + full output in each file).
Fetched res: `phase3/res/` (mirror of `src/main/res` relative path;
variants under `phase3/res/_variants/<debug|release>/res/...`).

## 1. Res completion sweep — PARTIAL: stopped by a fresh 429 (no retry)

**Fetch totals: 29 of 138 planned files fetched; 109 NOT fetched because
the fetch attempt stopped on a fresh 429 and was NOT retried (per the
brief's stop rule).** The 429 hit on `xml/searchable.xml` (the 30th
planned file); that file was NOT fetched. No connector call was made
after the 429 — no retry loop, no sleep/retry, no replacement fetch.
Listings (all completed before the 429, no 429 during listings) are
complete; only the file FETCH is partial.

Branch res root (`src/main/res`, 73 entries, saved in
`greps/L5/res_root_listing.txt`): animator, color, drawable,
drawable-hdpi/mdpi/v26/xhdpi/xxhdpi/xxxhdpi, layout, layout-large-land-
notouch, layout-sw600dp-land, menu, menu-large-land-notouch,
menu-sw600dp-land, mipmap-anydpi-v26/hdpi/xhdpi/xxhdpi/xxxhdpi,
values + values-<lang> (translation dirs), values-large-land-notouch,
values-sw360dp-v13, values-sw600dp, values-sw600dp-land, xml, xml-v26.
No debug/release dirs under `src/main/res` — they live under `src/debug`
and `src/release` (see below).

Listings saved (one at a time, ~30 s pauses, no 429 hit):
- `res_listings_menu_xml_values.txt`: menu (14 files),
  xml (14 files incl. 12 `pref_*.xml` + provider_paths + searchable),
  xml-v26 (pref_appearance.xml only), values base (14 files).
- `res_listings_other_consolidated.txt`: menu-large-land-notouch +
  menu-sw600dp-land (the original `res_listings_other.txt` captured
  only the final app-root listing due to a shell piping quirk; the
  consolidated file transcribes all listing outputs received)
  (detail_torrent.xml each), animator (3), color (1), drawable (72 XML +
  2 `.9.png`), drawable-v26 (splash_screen.xml), values-sw600dp /
  values-sw600dp-land / values-large-land-notouch (bool.xml +
  layouts.xml each), values-sw360dp-v13 (values-preference.xml),
  `src/` (androidTest, debug, main, play, release, test),
  app root (build.gradle, proguard-rules.pro, schemas, src).
- `res_listings_variants.txt`: src/debug (res only), src/release
  (res only), src/play (AndroidManifest.xml only).
- `res_listings_variant_res_files.txt`: debug/res/xml (shortcuts.xml),
  debug/res/xml-v25 (shortcuts.xml), debug/res/values (app_name.xml,
  ic_launcher_background.xml), debug/res/drawable
  (ic_banner.png + ic_launcher_foreground.xml); release/res/xml
  (shortcuts.xml), release/res/values (same two names),
  release/res/drawable (ic_banner.png + ic_launcher_foreground.xml).
- `res_listings_density_spotcheck.txt`: drawable-hdpi (18 png files
  only) and mipmap-hdpi (2 png files only) — spot-check confirming
  density/mipmap dirs are image-only; they were not descended further
  and no XML is expected there. The remaining density/mipmap dirs were
  not individually listed (same image-only shape; see "not fetched"
  below).

Fetched (fetch script `greps/L5/fetch_res.py`, one file at a time,
30 s pauses, state in `fetch_res_state.json`, log in `fetch_res.log`,
full list in `greps/L5/fetched_res_filelist.txt`) — 29 files:
- menu/ (14): add_torrent, detail_torrent,
  detail_torrent_files_action_mode, detail_torrent_trackers_action_mode,
  feed, feed_action_mode, feed_item_popup, feed_items, filemanager,
  log, main, main_action_mode, main_context, tag_item_popup.
- menu-large-land-notouch/detail_torrent.xml,
  menu-sw600dp-land/detail_torrent.xml.
- xml/ (13 of 14): pref_anonymous_mode, pref_appearance,
  pref_behavior, pref_feed, pref_headers, pref_limitations, pref_log,
  pref_network, pref_proxy, pref_scheduling, pref_storage,
  pref_streaming, provider_paths. NOT fetched: xml/searchable.xml
  (the file the 429 stopped on).

NOT fetched, with reasons:
- 109 planned files NOT fetched because of the 429 stop (see above):
  xml/searchable.xml; xml-v26/pref_appearance.xml; values base (14)
  + values-sw600dp/sw600dp-land/large-land-notouch (bool+layouts
  each) + values-sw360dp-v13/values-preference.xml; animator (3);
  color (1); drawable (72 XML); drawable-v26/splash_screen.xml;
  debug variant XML (5: xml + xml-v25 shortcuts, values app_name +
  ic_launcher_background, drawable ic_launcher_foreground);
  release variant XML (4: xml shortcuts, values app_name +
  ic_launcher_background, drawable ic_launcher_foreground).
  A later run (after the rate-limit window, by the coordinator, NOT
  by retrying now) would resume from `fetch_res_state.json`
  (29 fetched) — that resume is NOT done here.
- The 73 layout XMLs already in `corpus/res-layout/` (base layout +
  layout-large-land-notouch + layout-sw600dp-land) — already present,
  not re-fetched.
- `values-<lang>` translation dirs (strings.xml per locale): listed at
  root only, not individually fetched even before the 429. They
  contain translated UI strings only; no method name, preference
  key, binding, or include can be triggered from a translated
  string. This is a deliberate scope limit, stated not hidden.
- Raster images: `.9.png` files in drawable + all mipmap/density pngs
  (not XML, cannot contain code triggers).
- Directories that could NOT be listed: none. Every XML-bearing dir
  listed above was listed successfully; no listing failed and no
  429 was hit during listings. The 429 hit only the file fetch.

## 2. G-b1 + G-b2 greps (CORRECTED namespace — see below)

Saved in `greps/L5/grep_Gb_fetched_final.txt` (fetched-res scope) and
`greps/L5/grep_Gb_layout_scope.txt` + `grep_Gb_include_namespaces.txt`
(layout scope). Scope limitation from the 429 stop: G-b1/G-b2 results
below cover menu (all 3 dirs) + xml/ preference XML (13 of 14) ONLY.
NOT covered by any fetched file: xml-v26, values base + qualified
values, debug/release XML, drawable/animator/color XML. Those
targets are UNCHECKED in fetched res, not zero — the summary does
not claim them.

G-b1 (menu / xml-v26 / debug / release XML) — fetched subset:
- All flagged method names (getDhtNodes, getDownloadSpeedLimit,
  getUploadSpeedLimit, isDHTEnabled, isPeXEnabled, getItemKey,
  getItemPosition, setFileName, clearAllTables, dropAllTables,
  getAutoMigrations, getRequiredAutoMigrationSpecs, UriConverter,
  hashCode, toString, PiecesView, TagItem, TorrentStream, Selectable,
  KeyProvider, SelectionTracker): ZERO hits in all 29 fetched files.
- setVariable / onFieldChange: ZERO in all 29 fetched files.
- `bind:`: ZERO in all 29 fetched files. `app:viewModel`: ZERO in
  all 29 fetched files. `<include>`: ZERO elements in all 29
  fetched files (menu/preference XML has no includes, as expected).
- Context (not a target hit): fetched preference XML declares the
  custom preference classes — pref_anonymous_mode.xml contains
  SummaryPreference + SwitchBarPreference, pref_scheduling.xml
  contains TimePreference (×2). This corroborates that the
  preference classes ARE XML-declared (2-arg inflation path), but
  no flagged method name appears in any of these files.

G-b2 (preference / menu / values XML) — fetched subset: preference
XML (xml/ 13 files) + menu (16 files) results are the same ZERO
results above. Values XML: NOT fetched (429 stop) — G-b2 values
results are therefore NOT available; the per-target values check
is an open item for the coordinator's resume run, not a zero.

Layout-scope results (already complete, saved in
`greps/L5/grep_Gb_layout_scope.txt` and
`greps/L5/grep_Gb_include_namespaces.txt`):
- `setVariable(`: ZERO in all 281 app Java files; ZERO in 73 res-layout XML.
- `onFieldChange`: ZERO in all 281 app Java files; ZERO in 73 res-layout XML.
- `bind:`: ZERO in 73 res-layout XML (and no `xmlns:bind` declared in
  any layout file — only `android`, `app`, `tools` prefixes exist).
- CORRECTED namespace check (L3 correction, applied to every
  `<include>` element, multiline-aware): exactly 16 `<include>`
  elements exist in the 73 layout files. Only 3 carry a variable
  pass-through, all `app:viewModel="@{viewModel}"` to
  `@layout/add_torrent_info` (fragment_add_torrent_info.xml base +
  layout-large-land-notouch + layout-sw600dp-land variants).
  All other includes (toolbar, main_drawer_content,
  detail_torrent_appbar) carry NO variable in ANY namespace
  (`bind:` zero, `app:` variable zero, no other prefix exists).
  Consequence, stated as evidence not a verdict: the corrected check
  CONFIRMS the D4d parent route for AddTorrentInfoBinding.setVariable
  (59/32) and leaves every other child binding without any
  include pass-through in either namespace. `app:` attributes on
  non-include elements (app:fileSize, app:formatDate, app:color,
  app:srcCompat, etc.) are BindingAdapter/view attributes, NOT
  variable pass-throughs to a child binding.
- Flagged method names in res-layout: only PiecesView (layout
  declaration, fragment_detail_torrent_pieces.xml:73-77) — all other
  flagged names (getDhtNodes, getDownloadSpeedLimit,
  getUploadSpeedLimit, isDHTEnabled, isPeXEnabled, getItemKey,
  getItemPosition, setFileName, hashCode, clearAllTables,
  dropAllTables, getAutoMigrations, getRequiredAutoMigrationSpecs,
  UriConverter) are ZERO in res-layout.

## 3. Task-3 outcomes (verdict file: batch48_batch4.md)

Identities verified FIRST from the batch-48 and batch-4 files:
48/7 AppDatabase_Impl.clearAllTables (OPEN), 48/12
AppDatabase_Impl.getAutoMigrations(Map) (OPEN), 48/13
AppDatabase_Impl.getRequiredAutoMigrationSpecs() (OPEN), 48/19
AppDatabase_Impl$1.dropAllTables (OPEN), 4/11 UriConverter.<init> (OPEN).
No identity or premise failed for the three flips; the two OPEN stays
fail only on the missing Room print (named below).

FLIPS (3):
- 48/7 OPEN → UNREACHABLE no_trigger_in_app INFERRED (D31: zero
  clearAllTables in 281 Java + 73 res-layout + test/androidTest;
  Room print shows clearAllTables as abstract public API with no
  internal caller in the printed init path).
- 48/19 OPEN → UNREACHABLE closed_by_configuration INFERRED (D31:
  zero dropAllTables/fallback*/onDowngrade in 281 Java + 73
  res-layout + test/androidTest; buildDatabase uses addMigrations
  only, no destructive fallback configured).
- 4/11 OPEN → UNREACHABLE no_trigger_in_app INFERRED (D13/D32: all
  methods static, zero `new UriConverter` in 281 Java + 73
  res-layout + test/androidTest, no construction path printed).

STAYS OPEN (2):
- 48/12, 48/13: no deciding Room open-path print. App Room version
  is 2.6.1 (app/build.gradle, saved grep room_version.txt).
  Attempted print: RoomDatabase.android.kt, googlesource commit
  e07e805b1b62404193b376b80b3fcaa2051a4444 (current Room 3/KMP,
  NOT 2.6.1): init() calls validateAutoMigrations (:474) and the
  base getAutoMigrations (:686–694) / getRequiredAutoMigrationSpecs
  returning emptySet (:958–962) are shown, but the
  validateAutoMigrations BODY is unprinted (common code, not in
  that file), so unconditional-at-open vs declared-only is NOT
  decided for either row. Missing print named in the verdict file:
  the Room 2.6.1 Builder.build()/init/validateAutoMigrations path.

## 4. Task-4 evidence table (EVIDENCE ONLY — verdicts belong to L1)

Scope actually achieved: 281 app Java + 73 res-layout XML +
test/androidTest other-sourcesets (zero for all targets) + 29
fetched res files (zero for all targets, see §2). NOT in scope:
the 109 unfetched res XML files (429 stop) and androidx library /
generated sources (not in the local corpus, not on the branch for
this app). Every "SUPPORTS" below therefore means: no trigger in
any checked app source or checked res XML, and no plausible
unprinted dispatcher identified for the row's type. If the
coordinator's resume fetch finds a hit in an unfetched file, the
affected row revises to "undermines — recommend OPEN". Detail notes:
`greps/L5/task4_evidence_notes.md`.

| row | method | evidence outcome | hits |
| 41/36 | TorrentStream.hashCode | SUPPORTS UNREACHABLE | Zero receiver-typed hashCode on a TorrentStream var; zero TorrentStream hash collections; def TorrentStream.java:110-113 is a String call (`id.hashCode()`) |
| 41/37 | TorrentStream.toString | SUPPORTS UNREACHABLE | Zero stream.toString/log/concat of a TorrentStream var; TorrentStreamServer concatenates `stream.id`/`stream.fileSize` fields only (:153,:214,:248) |
| 11/7 | ui/tag TagItem.hashCode | SUPPORTS UNREACHABLE | DiffUtil equals/isSame only, bind reads info.name/info.color only; def :49-51 is a TagInfo call; drawer TagItem is a different class (trap avoided) |
| 11/8 | ui/tag TagItem.toString | SUPPORTS UNREACHABLE | Zero call/concat/log on a ui/tag TagItem outside its own body (:55-60); no TagItem databinding expression in res-layout |
| 39/9 | TorrentSessionImpl.getDhtNodes | SUPPORTS UNREACHABLE | Only TorrentSession.java:92 decl + def :712; handleStats uses super `dhtNodes()`, not this method |
| 39/11 | TorrentSessionImpl.getDownloadSpeedLimit | SUPPORTS UNREACHABLE | Only decl :86 + def :690; TorrentEngine:894-902 / ViewModel:377-379 / Fragment:754 are the per-task chain, not this method |
| 39/23 | TorrentSessionImpl.getUploadSpeedLimit | SUPPORTS UNREACHABLE | Only decl :88 + def :698; per-task chain at TorrentEngine:883-892 etc. is a different method |
| 39/28 | TorrentSessionImpl.isDHTEnabled | SUPPORTS UNREACHABLE | Only decl :112 + def :847 |
| 39/29 | TorrentSessionImpl.isPeXEnabled | SUPPORTS UNREACHABLE | Only decl :114 + def :855 |
| 94/7 | PeerListAdapter.getItemKey | SUPPORTS UNREACHABLE | Def :86-93; no peers KeyProvider, no peers SelectionTracker; other adapters' KeyProvider call sites are typed to other item types |
| 94/8 | PeerListAdapter.getItemPosition | SUPPORTS UNREACHABLE | Def :95-100; same as 94/7 |
| 94/31 | PiecesView 3-arg ctor | SUPPORTS UNREACHABLE | Def :64-69; 2-arg :57-63 does NOT chain to it; zero `new PiecesView(`; sole layout decl (pieces.xml:73-77) has NO style attr → inflation uses 2-arg |
| 96/40 | FeedItemsAdapter.getItemKey | SUPPORTS UNREACHABLE | Def :91-97; no feed-items KeyProvider/SelectionTracker; other KeyProviders typed to other types |
| 97/1 | FeedItemsAdapter.getItemPosition | SUPPORTS UNREACHABLE | Def :100-103 (indexOf, equals-only); same as 96/40 |
| 102/13 | FileManagerConfig.setFileName | SUPPORTS UNREACHABLE | Def :67-71; zero `.setFileName(` calls (only unrelated setFileNameFilter); callers assign `config.fileName` directly (DetailTorrentFragment:541, FeedActivity:269, LogActivity:311) |

Caveat for all task-4 rows: see the scope paragraph above §4's table
(109 res XML unfetched; androidx/generated sources unprinted).

## 5. Blockers / not claimed
- BLOCKER (fetch): fresh 429 stopped the res fetch at
  `xml/searchable.xml` (30th planned file). 29/138 files fetched.
  No retry was made, per the brief. Resume (after the rate-limit
  window) must start from `greps/L5/fetch_res_state.json` and still
  needs: xml/searchable.xml, xml-v26, all values, animator, color,
  drawable, drawable-v26, and debug/release variant XML. Until that
  resume runs, G-b1/G-b2 values + xml-v26 + debug/release results
  and the full-res half of task-4 evidence are OPEN items, not zeros.
- No build, sampler, grep-C1, or device check is claimed anywhere.
- Library-in-final_java_only scope: the branch `final_java_only`
  tree holds app Java only for this app; androidx Room/androidx
  library bodies were NOT fetched from the branch (they are not
  there) — the only library print used is the public RoomDatabase
  source cited above, with its version mismatch stated.
- No pushes, no branch edits, no tick written, no files written
  outside `phase3/verdicts/L5/`, `phase3/greps/L5/`, and
  `phase3/res/` (plus the fetch script/state/log inside greps/L5).
