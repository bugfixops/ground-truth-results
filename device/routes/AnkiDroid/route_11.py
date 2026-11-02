#!/usr/bin/env python3
"""AnkiDroid route_11: FilteredDeckOptions.onSharedPreferenceChanged.

Target: FilteredDeckOptions.onSharedPreferenceChanged (fires when
    the DeckPreferenceHack Editor commits).
Table verdict: FIXED (first-draw verdict; this script drives the
    final BFS route from methods.csv, 15 edges).
Route followed: final BFS route. The F2 fixes are in the graph and
    the script satisfies them, including the shared step-4 edge with
    route 10 (applied once) and the :958 final-else branch edge for
    the step-5 call site (no second call-site edge for :855-858).
Preconditions/fixtures:
  - Tablet/large-screen config, so mFragmented is true and
    loadStudyOptionsFragment runs.
  - A filtered (dyn) deck exists and is selected: the guard on the
    study-options -> FilteredDeckOptions step is "selected deck is
    dyn, and the user opens deck options"
    (StudyOptionsFragment.java:296-297). Set FIXTURE_DYN_DECK to
    the dyn deck name created by setup.
  - The Reschedule checkbox (key resched, default true) must
    actually change value when tapped; toggling it from its setup
    value guarantees that.
Mapping notes:
  - The deck-row tap that selects the dyn deck is a preamble action
    logged under E5aa9573a with a comment; the edge's own action is
    the following "Deck options" menu tap.
  - The "Deck options" menu item in the study-options fragment menu
    is titled "Deck options" (study_options string).
  - The "More options" content description is the standard AppCompat
    overflow description; verify it against a live uiautomator dump
    before a real run.
Launcher: com.ichi2.anki/.IntentHandler (AndroidManifest.xml:81-89).
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "E5906a191", "Ef3e13961",
    "Eae89b47b", "Ea73b74da", "E5aa9573a", "Ecacc1269", "E52232377",
    "E0760f245", "E86b609e2", "E6ae5bcda", "Ec300e3cc", "E8ee307a3",
]

# Dyn (filtered) deck name created by setup.
FIXTURE_DYN_DECK = "FIXTURE_DYN_DECK"


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_11")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_11", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate: launch MAIN/LAUNCHER.
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init>.
    r.comment("IntentHandler else branch starts DeckPicker",
              edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # E5906a191 onCreate -> showStartupScreensAndDialogs
    # (guard: colOpen).
    r.comment("colOpen branch shows startup screens", edge="E5906a191")
    # Ef3e13961 showStartupScreensAndDialogs -> onFinishedStartup.
    r.comment("nothing-special-required branch", edge="Ef3e13961")
    # Eae89b47b onFinishedStartup -> loadStudyOptionsFragment
    # (guard: mFragmented, tablet layout).
    r.comment("fragmented layout loads study options fragment",
              edge="Eae89b47b")
    # Ea73b74da loadStudyOptionsFragment -> S_STUDYOPTIONS_FRAG.
    r.comment("study options fragment shown", edge="Ea73b74da")
    # PREAMBLE (logged under E5aa9573a): select the dyn deck so the
    # study options fragment shows it.
    r.tap(edge="E5aa9573a", text=FIXTURE_DYN_DECK)
    # E5aa9573a S_STUDYOPTIONS_FRAG -> FilteredDeckOptions.<init>:
    # open the options menu, then tap Deck options; the dyn guard
    # sends this to FilteredDeckOptions, not DeckOptions.
    r.tap(edge="E5aa9573a", desc="More options")
    r.tap(edge="E5aa9573a", text="Deck options")
    # Ecacc1269 FilteredDeckOptions.<init> -> onCreate.
    r.comment("FilteredDeckOptions onCreate", edge="Ecacc1269")
    # E52232377 onCreate -> S_FILTEREDDECKOPTIONS.
    r.comment("filtered deck options page shown", edge="E52232377")
    # E0760f245 S_FILTEREDDECKOPTIONS -> DeckPreferenceHack.edit:
    # toggle the Reschedule checkbox (a persisted cram preference;
    # the value must actually change).
    r.tap(edge="E0760f245", text="Reschedule")
    # E86b609e2 edit -> Editor.putBoolean.
    r.comment("hack editor putBoolean", edge="E86b609e2")
    # E6ae5bcda putBoolean -> apply (guard: mAllowCommit true;
    # false only inside updateSummaries).
    r.comment("editor apply", edge="E6ae5bcda")
    # Ec300e3cc apply -> commit.
    r.comment("editor commit", edge="Ec300e3cc")
    # E8ee307a3 commit -> onSharedPreferenceChanged (target).
    r.comment("commit fires onSharedPreferenceChanged (target)",
              edge="E8ee307a3")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
