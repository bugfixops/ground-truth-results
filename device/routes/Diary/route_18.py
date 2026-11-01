#!/usr/bin/env python3
"""Diary device route script: route_18.

Method: Diary.onDateSet(DatePicker,int,int,int)
Edge ids in order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E65bffa72 E003e3f4e
    Eb04234de E614e3b2e E18bac421 E70b5909f E7ada6d09 E870a9cdb E9be34d27
    E6ab32328 E35c0023a Ec7c01fd2 E31280764 E6555ab30 E0d08d3f0 Ebfc59ea4
Printed route file: graphs/Diary/scratch route print for
    Diary.onDateSet(DatePicker,int,int,int), in
    ~/workspace/overnight/stream-D/Diary/scratch/route_steps.txt
    (section "Diary.onDateSet(DatePicker,int,int,int)", verdict
    REACHABLE) and route_judgements.txt line 18 (correct, SOURCE,
    Diary.java:818-825).
Permissions (ROUTES.csv): none.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): none (Diary row of work-emulator ci/apps.csv has an
    empty setup cell).

Route summary (from the printed route and the trigger graph): launch
Diary, open Settings from the overflow menu, untick "Use custom
calendar", go back to Diary, then open "Go to date..." which -- with
the custom calendar unticked -- shows the framework DatePickerDialog
(Diary.java:1726-1727, 1761-1769); tapping OK calls onDateSet
(Diary.java:818-825).

Mapping notes:
- Overflow menu: "Settings" is showAsAction=never (res/menu/main.xml),
  so it is reached via the overflow affordance (content-desc
  "More options", the standard Android overflow description) and then
  the "Settings" menu text (res/values/strings.xml:45).
- "Use custom calendar" (res/xml/preferences.xml, key pref_custom;
  title res/values/strings.xml:47) defaults to true, both in the
  preference XML (defaultValue=true) and in code (Diary.java:244, 1266
  default true). run_app.sh runs pm clear first, so the fresh-install
  default holds and one tap on the row unticks it, which is what the
  printed route needs ("Use custom calendar is unticked on the route
  itself"). If the script were run against a dirty install where the
  row was already unticked, the tap would re-tick it; pm clear is what
  keeps this deterministic.
- "Go to date..." (res/menu/main.xml, showAsAction=ifRoom; title
  res/values/strings.xml:26) may appear as an action-bar icon (then its
  content-desc is the title) or, when it does not fit, as overflow
  menu text. The script first tries the content-desc tap and, only if
  the node is absent, opens the overflow menu and taps the text. In
  dry-run mode the first tap is only planned, never fails, so the
  fallback never runs there.
- The date picker is left on the date it shows (the current entry
  date); no date change is needed, because tapping OK on any shown
  date calls onDateSet (DatePickerDialog OK -> OnDateSetListener, per
  the trigger-graph evidence for Ebfc59ea4).
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
ROUTE = "route_18"
EDGES = ["Ee6b8aa80", "Edd0b9192", "Ee63879c9", "Ea885d6f1", "E002e1746",
         "E65bffa72", "E003e3f4e", "Eb04234de", "E614e3b2e", "E18bac421",
         "E70b5909f", "E7ada6d09", "E870a9cdb", "E9be34d27", "E6ab32328",
         "E35c0023a", "Ec7c01fd2", "E31280764", "E6555ab30", "E0d08d3f0",
         "Ebfc59ea4"]
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
        # E870a9cdb -- Tap the Use custom calendar checkbox row: the
        # value flips and the listener fires. Fresh-install default is
        # true (see header note), so this tap unticks it.
        r.tap(edge="E870a9cdb", text="Use custom calendar")
        # E9be34d27 -- Settings stays shown with the new value
        # (SettingsFragment.java:146-208). No user action.
        r.comment("Settings stays shown with the new value",
                  edge="E9be34d27")
        # E6ab32328 -- Back finishes Settings; Diary resumes.
        # Trigger-graph gui: "Press Back".
        r.back(edge="E6ab32328")
        # E35c0023a -- Back in Diary with the changed preference
        # (getPreferences in onResume; Diary.java:539-571, 1259-1287).
        # No user action.
        r.comment("back in Diary with the changed preference",
                  edge="E35c0023a")
        # Ec7c01fd2 -- Tap an action bar icon or an item under More
        # options. Open the overflow menu again.
        r.tap(edge="Ec7c01fd2", desc="More options")
        # E31280764 -- switch case R.id.goToDate (Diary.java:678-679).
        # Trigger-graph gui: "Tap Go to date... (icon, or More options
        # -> Go to date... when it does not fit)". The overflow menu
        # is already open from the previous step; try the action-bar
        # icon description first, else the overflow text.
        try:
            r.tap(edge="E31280764", desc="Go to date\u2026")
        except LookupError:
            r.tap(edge="E31280764", text="Go to date\u2026")
        # E6555ab30 -- Use custom calendar unticked:
        # showDatePickerDialog(currEntry) (Diary.java:1726-1727).
        # No user action.
        r.comment("custom calendar unticked: showDatePickerDialog",
                  edge="E6555ab30")
        # E0d08d3f0 -- dialog.show(): framework DatePickerDialog
        # (Diary.java:1761-1769). No user action.
        r.comment("framework DatePickerDialog shown", edge="E0d08d3f0")
        # Ebfc59ea4 -- Set the date and tap OK. The shown date is kept;
        # OK calls onDateSet (Diary.java:818-825).
        r.tap(edge="Ebfc59ea4", text="OK")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
