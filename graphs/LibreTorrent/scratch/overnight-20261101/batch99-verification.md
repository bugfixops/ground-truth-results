# Batch 99 strict-entry verification — 2026-11-01

Question: Decision D2 ordered rows 14–40 → OPEN (row 18 already OPEN) on the
grounds that the chain link into FeedFragment was unevidenced — FeedActivity.java
never names FeedFragment, and no activity_feed.xml was found in the 69-file
res/layout listing. The application worker then found activity_feed_portrait.xml
and activity_feed_two_pane.xml and held the revert. This note settles it on
printed branch evidence.

Branch: work-2026-10-31, repo bugfixops/ground-truth-results. All branch reads
via the GitHub connector, one file at a time with ~30 s pauses. No fresh 429.
No token used. No push. Base path for all files below:
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/`.

## 1. Layout directories (fresh branch listing of res/)

res/ contains exactly three layout* directories:
- `res/layout/` — 69 files
- `res/layout-large-land-notouch/` — 2 files (detail_torrent_appbar.xml,
  fragment_add_torrent_info.xml)
- `res/layout-sw600dp-land/` — 2 files (detail_torrent_appbar.xml,
  fragment_add_torrent_info.xml)

`activity_feed.xml` exists in NONE of them. `activity_feed_portrait.xml` and
`activity_feed_two_pane.xml` both exist in base `res/layout/`. The absence of
`activity_feed.xml` is now explained, not a gap: `activity_feed` is a layout
ALIAS defined in values XML (see §4), not a layout file.

## 2. FeedActivity.java (fresh branch fetch, 412 lines, SHA-256 of content
a8716080dc2140118424448d1e0194a63bc6a665f748ae — byte-identical to the local
copy and to the SHA recorded in batch99-merge-ready.md)

- Line 101: `setContentView(R.layout.activity_feed);` — the only layout it
  inflates.
- Fragment transactions touch ONLY `R.id.feed_items_fragmentContainer`:
  showBlankFragment :197 (BlankFragment), showFeedItems :208/:216
  (FeedItemsFragment), getCurrentFeedItemsFragment :233.
- It NEVER names FeedFragment, NEVER uses `R.id.feed_fragmentContainer`, and
  NEVER references activity_feed_portrait or activity_feed_two_pane.
- Confirmed: the D2 premise about FeedActivity.java itself was correct — the
  link is not in the Java file. It is in the layout-alias XML (§4).

## 3. References to activity_feed_portrait / activity_feed_two_pane

- Printed XML references (fresh branch fetches, §4): the four `layouts.xml`
  alias files below are the references that resolve the inflated layout.
- Direct Java references: a grep of the local 252-file app-Java reconstruction
  plus layout XML found zero `R.layout.activity_feed_portrait` /
  `R.layout.activity_feed_two_pane` references. A connector search_code query
  for `activity_feed_portrait` returned 0 items with `incomplete_results: true`,
  so that 0 is NOT used as absence evidence (per project rule); the verdict
  does not rest on it.
- No Java reference is needed: the alias mechanism (§4) is itself the printed
  XML reference that inflates portrait/two_pane from `R.layout.activity_feed`.

## 4. The two layouts (fresh branch fetches, byte-identical to local copies)

### activity_feed_portrait.xml (fresh)
- Root RelativeLayout, `tools:context=".ui.feeds.FeedActivity"`.
- One FragmentContainerView: `class="org.proninyaroslav.libretorrent.ui.feeds.FeedFragment"`,
  `android:id="@+id/feed_fragmentContainer"`.
- Also `<include layout="@layout/toolbar" />`.

### activity_feed_two_pane.xml (fresh)
- Root LinearLayout, `tools:context=".ui.feeds.FeedActivity"`.
- FragmentContainerView: `class="org.proninyaroslav.libretorrent.ui.feeds.FeedFragment"`,
  `android:id="@+id/feed_fragmentContainer"`.
- Second FragmentContainerView (no class): `android:id="@+id/feed_items_fragmentContainer"`
  — the container FeedActivity's Java transactions target (§2). This confirms
  the two files belong to the same activity.
- Also `<include layout="@layout/toolbar" />`.

### tools:context distinction (stated explicitly)
`tools:context` is a DESIGN-TIME attribute: it does not inflate anything by
itself and is NOT relied on here. The operative inflation mechanism is the
`class` attribute on `androidx.fragment.app.FragmentContainerView`, which
instantiates the named fragment when the layout is inflated.

### The closing link — layout aliases (fresh branch fetches)
- `res/values/layouts.xml:4`:
  `<item name="activity_feed" type="layout">@layout/activity_feed_portrait</item>`
- `res/values-sw600dp/layouts.xml:4`:
  `<item name="activity_feed" type="layout">@layout/activity_feed_portrait</item>`
- `res/values-sw600dp-land/layouts.xml:4`:
  `<item name="activity_feed" type="layout">@layout/activity_feed_two_pane</item>`
- `res/values-large-land-notouch/layouts.xml:4`:
  `<item name="activity_feed" type="layout">@layout/activity_feed_two_pane</item>`
- The same files also alias activity_main → drawer/two_pane and
  activity_settings → portrait/two_pane, which explains why MainActivity's
  `R.layout.activity_main` and SettingsActivity's `R.layout.activity_settings`
  likewise have no same-named layout file — the alias pattern is project-wide,
  not a FeedActivity anomaly.

## 5. Printed route (complete, launcher to FeedFragment)

MainActivity feed menu → FeedActivity (already printed in batch 99) →
FeedActivity.onCreate :101 `setContentView(R.layout.activity_feed)` →
alias resolves `activity_feed` → `activity_feed_portrait` (base / sw600dp) or
`activity_feed_two_pane` (sw600dp-land / large-land-notouch) → inflated layout's
FragmentContainerView instantiates `FeedFragment` in `feed_fragmentContainer`
→ FeedFragment.onViewCreated builds the adapter/SelectionTracker that rows
14–40 run through.

## OUTCOME: CLOSED — D2's batch-99 revert does NOT apply

The gap is closed by a printed route link: an actually-inflated layout
(the alias-resolved layout for `R.layout.activity_feed`) names FeedFragment,
via a printed XML reference (the `layouts.xml` aliases) that inflates
activity_feed_portrait / activity_feed_two_pane. No label changes.
batch99-merge-ready.md is left unchanged except for the appended dated note
recording this evidence.

Residual note (does not affect the outcome): not every one of the ~50 locale
values-* directories was listed for a layouts.xml file. This cannot reopen the
gap: the base alias already guarantees a FeedFragment-naming layout on any
configuration, and every alias override found also resolves to a
FeedFragment-naming layout (portrait or two_pane); any further override could
only swap portrait ↔ two_pane, both of which name FeedFragment.

Counts (mechanically verified from the label column, unchanged):
40 rows = 39 REACHABLE proposed / 0 UNREACHABLE / 1 OPEN (row 18 only).
