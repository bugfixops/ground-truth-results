#!/usr/bin/env python3
"""Diary device route script: route_20.

Method: Diary.dateCheck(CharSequence,String,Date)
Edge ids in order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E65bffa72 E003e3f4e
    Eb04234de E614e3b2e E18bac421 E70b5909f E7ada6d09 Eb6b6550a Ea4546a61
    E974860c5 E00abed65 Ec59307d8 E5a9c7ed0 E08d0b7cb
Printed route file: graphs/Diary/scratch route print for
    Diary.dateCheck(CharSequence,String,Date), in
    ~/workspace/overnight/stream-D/Diary/scratch/route_steps.txt
    (section "Diary.dateCheck(CharSequence,String,Date)", verdict
    REACHABLE) and route_judgements.txt line 20 (correct, SOURCE,
    Diary.java:2642-2644).
Permissions (ROUTES.csv): none.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): none (Diary row of work-emulator ci/apps.csv has an
    empty setup cell).

Route summary (from the printed route and the trigger graph): launch
Diary, open Settings from the overflow menu, tick "Use index", go back
to Diary, then choose "Add link" from the overflow menu. addIndexLink
calls dateCheck(pref_index_template, "EEEE d MMMM yyyy", linkDate)
(Diary.java:2644).

Mapping notes:
- Overflow menu: "Settings" and "Add link" are both showAsAction=never
  (res/menu/main.xml), so both are reached via the overflow affordance
  (content-desc "More options", the standard Android overflow
  description) and then the menu text: "Settings"
  (res/values/strings.xml:45) and "Add link"
  (res/values/strings.xml:27).
- "Use index" (res/xml/preferences.xml, key pref_use_index; title
  res/values/strings.xml:74) defaults to false, both in the preference
  XML (defaultValue=false) and in code (Diary.java:248, 1270 default
  false). run_app.sh runs pm clear first, so the fresh-install default
  holds and one tap on the row ticks it, which is what the printed
  route needs ("Use index is ticked on the route itself"). If the
  script were run against a dirty install where the row was already
  ticked, the tap would untick it; pm clear is what keeps this
  deterministic.
- "Add link" is visible only with Use index ticked
  (Diary.onPrepareOptionsMenu, Diary.java:634: link visible =
  useIndex), which is why the Settings step must come first.
- addIndexLink's early return (Diary.java:2637-2638, if !useIndex)
  is avoided by the same tick.
- Lifecycle, CALL, INTENT, ENTERS and SYSTEM edges with no user action
  are logged with r.comment, per the D3 rules.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner

PKG = "org.billthefarmer.diary"
ROUTE = "route_20"
EDGES = ["Ee6b8aa80", "Edd0b9192", "Ee63879c9", "Ea885d6f1", "E002e1746",
         "E65bffa72", "E003e3f4e", "Eb04234de", "E614e3b2e", "E18bac421",
         "E70b5909f", "E7ada6d09", "Eb6b6550a", "Ea4546a61", "E974860c5",
         "E00abed65", "Ec59307d8", "E5a9c7ed0", "E08d0b7cb"]
DIARY = "org.billthefarmer.diary/org.billthefarmer.diary.Diary"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", default=".")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    a = ap.parse_args()
    r = Runner(package=a.package, route=ROUTE, edge_ids=EDGES,
               log_path=a.log, dry_run=a.dry_run, adb=a.adb,
               outdir=a.outdir)
    try:
        # Ee6b8aa80 -- Tap the Diary icon in the launcher (MAIN/LAUNCHER
        # intent filter, AndroidManifest.xml:52-59). Launched by
        # component, the adb equivalent of the launcher tap.
        r.launch(DIARY, edge="Ee6b8aa80")
        # Edd0b9192 -- The system instantiates Diary, then onCreate
        # (Diary.java:441-443). No user action.
        r.comment("system instantiates Diary, then onCreate",
                  edge="Edd0b9192")
        # Ee63879c9 -- onStart -> onResume (Diary.java:539-541).
        # No user action.
        r.comment("onStart then onResume", edge="Ee63879c9")
        # Ea885d6f1 -- Diary visible with the MarkdownView
        # (Diary.java:570, 1696-1709). No user action.
        r.comment("Diary visible with the MarkdownView", edge="Ea885d6f1")
        # E002e1746 -- Tap an action bar icon or an item under More
        # options. Open the overflow menu (res/menu/main.xml:22-118;
        # Diary.java:659-726).
        r.tap(edge="E002e1746", desc="More options")
        # E65bffa72 -- switch case R.id.settings (Diary.java:714-715).
        # Trigger-graph gui: "Tap More options -> Settings".
        r.tap(edge="E65bffa72", text="Settings")
        # E003e3f4e -- startActivity(new Intent(this, Settings.class))
        # (Diary.java:1976-1979). No user action.
        r.comment("settings() starts the Settings activity",
                  edge="E003e3f4e")
        # Eb04234de -- The system instantiates Settings, then onCreate
        # (theme from pref_theme, Up arrow enabled; Settings.java:53-104).
        # No user action.
        r.comment("system instantiates Settings, then onCreate",
                  edge="Eb04234de")
        # E614e3b2e -- replace(android.R.id.content, new
        # SettingsFragment()).commit() (Settings.java:91-94).
        # No user action.
        r.comment("Settings replaces content with SettingsFragment",
                  edge="E614e3b2e")
        # E18bac421 -- The fragment transaction commits: fragment
        # onCreate. No user action.
        r.comment("fragment transaction commits: fragment onCreate",
                  edge="E18bac421")
        # E70b5909f -- The fragment resumes with the activity.
        # No user action.
        r.comment("fragment resumes with the activity", edge="E70b5909f")
        # E7ada6d09 -- Settings list shown (SettingsFragment.java:107-113).
        # No user action.
        r.comment("Settings list shown", edge="E7ada6d09")
        # Eb6b6550a -- Tap the Use index checkbox row: the value flips
        # and the listener fires. Fresh-install default is false (see
        # header note), so this tap ticks it.
        r.tap(edge="Eb6b6550a", text="Use index")
        # Ea4546a61 -- Settings stays shown with the new value (Index
        # page / Index template rows enabled;
        # SettingsFragment.java:146-208; res/xml/preferences.xml:93, 100).
        # No user action.
        r.comment("Settings stays shown, index rows enabled",
                  edge="Ea4546a61")
        # E974860c5 -- Back finishes Settings; Diary resumes.
        # Trigger-graph gui: "Press Back".
        r.back(edge="E974860c5")
        # E00abed65 -- Back in Diary with the changed preference
        # (getPreferences in onResume; Diary.java:539-571, 1259-1287).
        # No user action.
        r.comment("back in Diary with the changed preference",
                  edge="E00abed65")
        # Ec59307d8 -- Tap an action bar icon or an item under More
        # options. Open the overflow menu again.
        r.tap(edge="Ec59307d8", desc="More options")
        # E5a9c7ed0 -- switch case R.id.link (Diary.java:684-685).
        # Trigger-graph gui: "Tap More options -> Add link". Visible
        # only with Use index ticked (Diary.java:634).
        r.tap(edge="E5a9c7ed0", text="Add link")
        # E08d0b7cb -- title = dateCheck(pref_index_template,
        # "EEEE d MMMM yyyy", linkDate) (Diary.java:2644). No user
        # action; this is the route target.
        r.comment("addIndexLink calls dateCheck with the link date",
                  edge="E08d0b7cb")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
