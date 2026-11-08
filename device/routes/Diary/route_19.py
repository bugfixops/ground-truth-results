#!/usr/bin/env python3
"""Diary device route script: route_19.

Method: Diary.onRestoreInstanceState
Edge ids in order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E65bffa72 E003e3f4e
    Eb04234de E614e3b2e E18bac421 E70b5909f E7ada6d09 E5e8f27e8 E723d3724
    Ed1ef6d6e Ed9c145d5 E7c4aeb78 E0bdcb055 Ebe4557c8
Printed route file: graphs/Diary/scratch route print for
    Diary.onRestoreInstanceState, in
    ~/workspace/overnight/stream-D/Diary/scratch/route_steps.txt
    (section "Diary.onRestoreInstanceState", verdict REACHABLE) and
    route_judgements.txt line 19 (correct, SOURCE, Diary.java:523-533).
Permissions (ROUTES.csv): none.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): none (Diary row of work-emulator ci/apps.csv has an
    empty setup cell).

Route summary (from the printed route and the trigger graph): launch
Diary, open Settings, change the Theme to a different value, go back
to Diary. Diary.onResume sees pref_theme differs from the theme read
in onCreate and calls recreate() (Diary.java:541-548); the new
instance is created with the saved instance state, and onStart is
followed by onRestoreInstanceState (Diary.java:523-533).

Mapping notes:
- This route does NOT need a rotation. The harness (harness.py) has no
  rotation or configuration-change action -- only key(), tap(),
  start_intent() and friends -- but none is needed: the printed
  route's own mechanism, the theme change, drives recreate(), and
  every step of it is drivable with taps and Back. The route is
  therefore scripted, not an unscriptable candidate. (A rotation
  would be an alternative way to force recreation, but it is not the
  printed route and the harness cannot express it.)
- Overflow menu: "Settings" is showAsAction=never (res/menu/main.xml),
  so it is reached via the overflow affordance (content-desc
  "More options", the standard Android overflow description) and then
  the "Settings" menu text (res/values/strings.xml:45).
- Theme row: the ListPreference row titled "Theme"
  (res/xml/preferences.xml, key pref_theme; title
  res/values/strings.xml:71). Its dialog entries are Light / Dark /
  System (res/values/arrays.xml:23-27, values 0/1/2).
- "Dark" is picked because the fresh-install default theme is Light:
  default_theme is 0 (res/values/integers.xml:23), entry 0 is Light,
  and Diary.getPreferences defaults PREF_THEME to "0"
  (Diary.java:1262). run_app.sh runs pm clear first, so the default
  holds and Dark always differs from it, which is what makes
  onResume call recreate(). Note Diary.onResume skips recreate on
  SDK M (Diary.java:547: SDK_INT != M); a current emulator image is
  unaffected.
- Lifecycle, ENTERS and SYSTEM edges with no user action are logged
  with r.comment, per the D3 rules.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner

PKG = "org.billthefarmer.diary"
ROUTE = "route_19"
EDGES = ["Ee6b8aa80", "Edd0b9192", "Ee63879c9", "Ea885d6f1", "E002e1746",
         "E65bffa72", "E003e3f4e", "Eb04234de", "E614e3b2e", "E18bac421",
         "E70b5909f", "E7ada6d09", "E5e8f27e8", "E723d3724", "Ed1ef6d6e",
         "Ed9c145d5", "E7c4aeb78", "E0bdcb055", "Ebe4557c8"]
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
        # E5e8f27e8 -- Tap the Theme row: its dialog opens.
        # Trigger-graph gui: "Tap the Theme row".
        r.tap(edge="E5e8f27e8", text="Theme")
        # E723d3724 -- Enter or pick a different value and confirm.
        # Trigger-graph gui: "Pick a different theme (Light / Dark /
        # System)". Fresh-install default is Light (see header note),
        # so Dark differs and triggers recreate() on resume.
        r.tap(edge="E723d3724", text="Dark")
        # Ed1ef6d6e -- Settings stays shown with the new value
        # (SettingsFragment.java:146-208). No user action; the dialog
        # closes on the pick.
        r.comment("Settings stays shown with the new value",
                  edge="Ed1ef6d6e")
        # Ed9c145d5 -- Back finishes Settings; Diary resumes.
        # Trigger-graph gui: "Press Back".
        r.back(edge="Ed9c145d5")
        # E7c4aeb78 -- pref_theme differs from the theme read in
        # onCreate: recreate() (Diary.java:542-548). No user action;
        # driven by the theme change above, not by a rotation (the
        # harness has no rotation action and none is needed).
        r.comment("theme differs in onResume: recreate()",
                  edge="E7c4aeb78")
        # E0bdcb055 -- The system instantiates Diary, then onCreate
        # with the saved instance state (Diary.java:441-443).
        # No user action.
        r.comment("system recreates Diary, onCreate with saved state",
                  edge="E0bdcb055")
        # Ebe4557c8 -- Recreated with saved state: onStart, then
        # onRestoreInstanceState (the intent branch Diary.java:497-516
        # is skipped; Diary.java:523-533). No user action; this is the
        # route target.
        r.comment("onStart then onRestoreInstanceState with saved state",
                  edge="Ebe4557c8")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
