#!/usr/bin/env python3
"""AnkiDroid route_18: Sched.sortCards(long[],int,int,boolean,boolean).

Target: Sched.sortCards(long[],int,int,boolean,boolean).
Table verdict: CORRECT (final-draw verdict; this script drives the
    printed BFS route, 19 edges, unchanged).
Route followed: printed route: fragment -> exportDeck -> export
    dialog -> exportApkg -> EXPORT_APKG task -> exportInto ->
    exportFiltered -> super exportInto -> resetCards -> forgetCards
    -> sortCards -> sortCards 5-arg.
Preconditions: collection open; tablet/fragmented layout, so the
    fragment toolbar shows the export item; a deck with cards to
    export (deck id non-null, so the export dialog defaults
    "Include scheduling" unchecked).
Mapping notes:
  - No old first-draw script targets this method; the export-dialog
    walk is newly written from ExportDialog.java:58-100, with the
    dialog default (deck export -> scheduling unchecked) verified
    in source, so no checkbox tap is scripted.
  - "More options" is the standard AppCompat overflow description;
    verify it against a live uiautomator dump before a real run.
Launcher: com.ichi2.anki/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh already does pm clear, permission
    grants, fixture pushes, and per-app setup before this script, so
    the script performs only the route actions starting from launch.
Draft status: final-draw device draft for the merger; dry/static
    checks only. No live run has been performed with this script, and
    nothing in this file claims one.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "E5906a191", "Ef3e13961",
    "Eae89b47b", "Ea73b74da", "Ec39ae90b", "E8d6724a8", "E3e8831e9",
    "E5e4e8c54", "Eb2e355d4", "Ea376a2dd", "E087771e4", "E87da187c",
    "Ebf658596", "E43fe9c4c", "E5d61e25c", "E1bf5f73b",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_18")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_18", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate: launch MAIN/LAUNCHER.
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init> (else branch).
    r.comment("IntentHandler else branch starts DeckPicker",
              edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # E5906a191 DeckPicker.onCreate -> showStartupScreensAndDialogs.
    r.comment("showStartupScreensAndDialogs", edge="E5906a191")
    # Ef3e13961 -> onFinishedStartup.
    r.comment("onFinishedStartup", edge="Ef3e13961")
    # Eae89b47b -> loadStudyOptionsFragment.
    r.comment("loadStudyOptionsFragment", edge="Eae89b47b")
    # Ea73b74da -> S_STUDYOPTIONS_FRAG.
    r.comment("study-options fragment page shown", edge="Ea73b74da")
    # Ec39ae90b S_STUDYOPTIONS_FRAG -> DeckPicker.exportDeck:
    # action_export case (StudyOptionsFragment.java:334-335).
    # Guard: the export item is visible only in fragmented
    # (tablet) mode (:364-370), so the run needs a tablet layout.
    # Open the fragment toolbar menu, then tap the item. String
    # verified in res: export_deck = "Export deck".
    r.tap(edge="Ec39ae90b", desc="More options")
    r.tap(edge="Ec39ae90b", text="Export deck")
    # E8d6724a8 exportDeck -> S_DLG_EXPORT (ExportDialog).
    r.comment("export dialog shown", edge="E8d6724a8")
    # E3e8831e9 S_DLG_EXPORT -> DeckPicker.exportApkg: tap OK
    # (ExportDialog positiveText is android.R.string.ok). The
    # single consistent guard is includeSched=false: for a deck
    # export the dialog defaults "Include scheduling" unchecked
    # (ExportDialog.java:58-61, did != -1), so no checkbox tap is
    # needed; if the dialog shows it checked, the live run must
    # uncheck it first or the exportFiltered/resetCards branch
    # will not run.
    r.tap(edge="E3e8831e9", text="OK")
    # E5e4e8c54 exportApkg -> DeckTask.doInBackground@EXPORT_APKG.
    r.comment("EXPORT_APKG task launched", edge="E5e4e8c54")
    # Eb2e355d4 -> doInBackgroundExportApkg.
    r.comment("doInBackgroundExportApkg", edge="Eb2e355d4")
    # Ea376a2dd -> AnkiPackageExporter.exportInto.
    r.comment("exportInto", edge="Ea376a2dd")
    # E087771e4 exportInto -> exportFiltered (filtered path, since
    # the export is not the verbatim full-export case).
    r.comment("exportFiltered", edge="E087771e4")
    # E87da187c exportFiltered -> AnkiExporter.exportInto.
    r.comment("super exportInto", edge="E87da187c")
    # Ebf658596 AnkiExporter.exportInto -> Sched.resetCards (the
    # !mIncludeSched branch, AnkiPackageExporter.java:142-149).
    # Wait for the export to reach the reset.
    r.dwell(edge="Ebf658596", seconds=10)
    # E43fe9c4c resetCards -> forgetCards.
    r.comment("forgetCards", edge="E43fe9c4c")
    # E5d61e25c forgetCards -> sortCards(long[],int).
    r.comment("sortCards(long[],int)", edge="E5d61e25c")
    # E1bf5f73b sortCards(long[],int) ->
    # sortCards(long[],int,int,boolean,boolean) (target; :2204).
    r.comment("sortCards 5-arg reached (target)", edge="E1bf5f73b")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
