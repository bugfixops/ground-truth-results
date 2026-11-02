#!/usr/bin/env python3
"""Omni-Notes route_12: IdeogramsWordCounter.<init>.

Method: IdeogramsWordCounter.<init>
Edge ids in order:
    Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 E7e3c321b E01d0dfd6 Ee5d1ab81 E8a16cf02 Edbf61bdc
    Ed31fd875 E0fba9459 E0e09a3d7 Ea429488c E74fa500c E200766cb
    E606cb25c E181a34d2 Eb6790f71
Printed route: CountFactory.java:28-44; LanguageHelper.java:94-104;
edge list identical to the Omni-Notes ROUTES.csv route_12 row and
to the trigger graph.
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none listed in ROUTES.csv. Setup (ROUTES.csv): push
fixtures/Pictures (app-level first-run setup, unchanged).
Standard configuration: run_app.sh starts from `pm clear` and grants
only the ROUTES.csv permissions (none here).

Mapping notes (printed source):
  - LOCALE GATE: CountFactory.getWordCounter() reads
    LanguageHelper.getCurrentLocaleAsString(app context) and
    switches on it: "ja_JP", "zh_CN", "zh_TW" -> new
    IdeogramsWordCounter(); default -> DefaultWordCounter
    (CountFactory.java:28-44). getCurrentLocale returns the
    system locale (LanguageHelper.java:94-104: getLocales().get(0)
    on N+, else configuration.locale). This script therefore sets
    the system locale to ja_JP BEFORE launching (fresh launch
    picks it up), so getCounterInstanceByLocale takes the
    ideogram branch. The locale string the switch sees is
    Locale.toString() ("ja_JP", underscore); set_locale takes
    "ja_JP" and puts the BCP-47 form ("ja-JP") into
    system_locales, which the system reports back as ja_JP.
  - LOCALE RESTORE: system_locales is GLOBAL and `pm clear` does
    NOT reset it, so the script restores en-US before done()
    (logged under the target edge as post-target cleanup); the
    next route's fresh launch then uses en-US. If the CI
    emulator image lacks the ja-JP locale, the setting may fall
    back and the target will not fire — that is a live-run
    uncertainty (JaCoCo decides; unclear, never wrong), not a
    script defect.
  - INFO MENU: the detail toolbar's Info item (menu_detail.xml:
    id menu_note_info, title @string/info, showAsAction="ifRoom",
    NO icon) shows its "Info" text either in the toolbar (if it
    fits) or in the overflow menu. The script first waits briefly
    for text "Info"; if that times out it opens the overflow
    (desc "More options") and taps text "Info" there. The failed
    wait line in the overflow case is expected and documented
    here (the tap that follows is what completes the edge).
  - FAB: long-press the + button (res/layout/fab.xml id fab),
    mirroring route_01's identical edge E01d0dfd6.
  - This route was unscriptable ("device locale cannot be set
    per-route without a restart") until the harness gained
    set_locale(); it converts on that primitive plus the app
    restart that a fresh launch already provides.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af '
            'Ef86ebfe1 E7e3c321b E01d0dfd6 Ee5d1ab81 E8a16cf02 Edbf61bdc '
            'Ed31fd875 E0fba9459 E0e09a3d7 Ea429488c E74fa500c E200766cb '
            'E606cb25c E181a34d2 Eb6790f71').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_12', EDGE_IDS, a.log,
               dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    # Ea7466154 (precondition): set the system locale to ja_JP
    # BEFORE launching, so the fresh launch picks it up and
    # CountFactory takes the ideogram branch. Then launch
    # MainActivity (MAIN/LAUNCHER).
    r.set_locale('Ea7466154', 'ja_JP')
    r.launch('it.feio.android.omninotes/.MainActivity', 'Ea7466154')
    # E89791c67 MainActivity.<init> -> MainActivity.onResume:
    # lifecycle, no action.
    r.comment('Activity lifecycle callback', 'E89791c67')
    # Edf932a3c MainActivity.onResume -> MainActivity.checkPassword:
    # cold start, no password gate, no action.
    r.comment('Cold start: isPasswordAccepted false, checkPassword runs',
              'Edf932a3c')
    # E075b4776 MainActivity.checkPassword -> MainActivity.init:
    # explicit call, no action.
    r.comment('No password gate: init()', 'E075b4776')
    # E2436b969 MainActivity.init -> ListFragment.<init>: explicit
    # call, no action.
    r.comment('init() adds the list fragment', 'E2436b969')
    # E54b170af ListFragment.<init> -> ListFragment.onActivityCreated:
    # lifecycle, no action.
    r.comment('Fragment lifecycle callback', 'E54b170af')
    # Ef86ebfe1 ListFragment.onActivityCreated -> ListFragment.init:
    # explicit call, no action.
    r.comment('init()', 'Ef86ebfe1')
    # E7e3c321b ListFragment.init -> S_LIST@NOTES: list set up on
    # the default Notes navigation, no action.
    r.comment('List set up on the default Notes navigation', 'E7e3c321b')
    # E01d0dfd6 S_LIST@NOTES -> Fab.lambda$init$1@LONG_NOTES:
    # long-press the + button (res/layout/fab.xml id fab).
    r.long_tap('E01d0dfd6', res_id='it.feio.android.omninotes:id/fab')
    # Ee5d1ab81 Fab long-press -> ListFragment.lambda$initFab$0@MAIN:
    # menu dispatch, no action.
    r.comment('onFabItemClick(fab_expand_menu_button)', 'Ee5d1ab81')
    # E8a16cf02 lambda$initFab$0@MAIN -> S_DETAIL@NEW: a new note
    # opens, no action.
    r.comment('A new note is opened', 'E8a16cf02')
    # Edbf61bdc S_DETAIL@NEW -> DetailFragment.onOptionsItemSelected
    # @NOTE_INFO: tap "Info" in the toolbar menu. Info shows its
    # text either in the toolbar or in the overflow (see header):
    # try the direct text tap first, fall back to the overflow.
    try:
        r.wait_for('Edbf61bdc', text='Info', timeout=5)
        r.tap('Edbf61bdc', text='Info')
    except TimeoutError:
        r.tap('Edbf61bdc', desc='More options')
        r.tap('Edbf61bdc', text='Info')
    # Ed31fd875 onOptionsItemSelected@NOTE_INFO -> showNoteInfo:
    # the note_info branch of the menu switch, no action.
    r.comment('The note_info branch of the menu switch', 'Ed31fd875')
    # E0fba9459 showNoteInfo -> NoteInfosActivity.<init>:
    # startActivity(NoteInfosActivity), no action.
    r.comment('startActivity(NoteInfosActivity)', 'E0fba9459')
    # E0e09a3d7 NoteInfosActivity.<init> -> onCreate: lifecycle.
    r.comment('Activity lifecycle callback', 'E0e09a3d7')
    # Ea429488c onCreate -> populateViews: direct call, no action.
    r.comment('populateViews()', 'Ea429488c')
    # E74fa500c populateViews -> NotesHelper.getNoteInfos: direct
    # call, no action.
    r.comment('getNoteInfos()', 'E74fa500c')
    # E200766cb getNoteInfos -> getChars: direct call, no action.
    r.comment('getChars()', 'E200766cb')
    # E606cb25c getChars -> CountFactory.getWordCounter: direct
    # call, no action.
    r.comment('getWordCounter()', 'E606cb25c')
    # E181a34d2 getWordCounter -> getCounterInstanceByLocale:
    # direct call; the locale switch takes the ideogram branch
    # (locale ja_JP, set before launch), no action.
    r.comment('getCounterInstanceByLocale(ja_JP) takes the ideogram branch',
              'E181a34d2')
    # Eb6790f71 getCounterInstanceByLocale -> IdeogramsWordCounter
    # .<init>: the ideogram counter is constructed. Automatic;
    # this is the target edge.
    r.comment('IdeogramsWordCounter constructed for ja_JP', 'Eb6790f71')
    # Post-target cleanup (same edge): restore the GLOBAL locale
    # to en-US so later routes run under the default locale.
    r.set_locale('Eb6790f71', 'en-US')
    r.done()


if __name__ == '__main__':
    main()
