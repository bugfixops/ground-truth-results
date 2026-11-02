"""Device route script route_16 for Omni-Notes.

Method: BitmapHelper.getImageBitmap
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 E7e3c321b E01d0dfd6 Ee5d1ab81 E8a16cf02 E1a48ab1f E4455444c
    Eca06fe26 E67ba23d6 E5ccc83ff E142b6fe8 E59f83d06 Ee8501df3 Eef154c6b
    E3b82664d
Printed route: graphs/Omni-Notes/out/methods.csv chain for
    BitmapHelper.getImageBitmap (AlarmReceiver.java:120-125;
    BitmapHelper.java:52-57). This method was NOT among the 30 sampled
    routes in sample_30_routes.txt; its edge chain is the methods.csv
    shortest path, which matches the ROUTES.csv edge list exactly.
Permissions: none in ROUTES.csv. Fixtures: none. Setup (ROUTES.csv):
    push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the
fixture pushes, and the permission grants; this script starts from a fresh
process.

One block per route edge, in route order. Lifecycle, page, explicit-call,
and framework edges with no user action get a comment, not an action.
Every action names an edge id of this route (the harness enforces it).

Setup note (note with a sketch + a reminder, before the save edge): the
route's save chain starts at MainActivity.onBackPressed@DETAIL_SAVE, so
the note must already carry an attachment and a reminder when Back is
pressed. Those setup actions happen on the detail screen and are logged
under E8a16cf02 (entry to S_DETAIL@NEW, the screen they happen on); they
are NOT route edges, and the save chain itself then uses its own edges
in order.

Attachment choice: a Sketch (attachment_dialog "Sketch", DetailFragment
takeSketch -> SketchFragment; a long-press on the drawing view draws a
one-touch stroke, Back in the sketch saves it, and
DetailFragment.onResume adds it as a MIME_TYPE_SKETCH attachment, which
AlarmReceiver/BitmapHelper treat exactly like an image for
getImageBitmap). The stroke is REQUIRED, not cosmetic: with an untouched
canvas SketchView.paths stays empty, getBitmap() returns null
(SketchView.java:204-207), SketchFragment.save() writes nothing and
sets no sketchUri, so no attachment is added and the alarm path never
reaches getImageBitmap (auditor FAIL on the original script, fixed
here). This stays inside the app: no system picker and no
storage-permission prompt are involved.

Fixture note: ROUTES.csv lists Pictures/photo_1.jpg for this route
(merger amendment); the script never opens a picker, so that fixture
is unused under this fix — the merger may drop it from the row or
keep it (merger-side note, not a script change).

Reminder choice: the reminder row (fragment_detail_content.xml id
reminder_layout, hint "Add reminder") opens the SublimePicker dialog
whose preset for a new note is now + 60 seconds
(DateUtils.getPresetReminder -> getNextMinute), so confirming with the
preset gives a reminder a minute ahead. The alarm then fires about a
minute after the save, and AlarmReceiver.createNotification calls
BitmapHelper.getBitmapFromAttachment -> getImageBitmap for the first
(non-files) attachment.

UNCERTAIN selector (flagged, not grounded in app res): the SublimePicker
confirm control is library UI, not in the app's res/; the script taps
text "Ok" (the app's own ok string, used for MaterialDialog positives).
The first live run must verify the picker's confirm control in a UI dump
and adjust this tap if it differs; if it differs, no reminder is set and
the wait below times out instead of reaching the target.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af '
            'Ef86ebfe1 E7e3c321b E01d0dfd6 Ee5d1ab81 E8a16cf02 E1a48ab1f '
            'E4455444c Eca06fe26 E67ba23d6 E5ccc83ff E142b6fe8 E59f83d06 '
            'Ee8501df3 Eef154c6b E3b82664d').split()

NOTE_TITLE = 'Alarm image note'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_16', EDGE_IDS, a.log,
               dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    # Ea7466154 S_ENTRY -> MainActivity.<init>: launcher starts MainActivity.
    r.launch('it.feio.android.omninotes/.MainActivity', 'Ea7466154')
    # E89791c67 MainActivity.<init> -> MainActivity.onResume: lifecycle, no action.
    r.comment('Activity lifecycle callback', 'E89791c67')
    # Edf932a3c MainActivity.onResume -> MainActivity.checkPassword: cold start,
    # no password gate, no action.
    r.comment('Cold start: isPasswordAccepted false, checkPassword runs', 'Edf932a3c')
    # E075b4776 MainActivity.checkPassword -> MainActivity.init: explicit call, no action.
    r.comment('No password gate: init()', 'E075b4776')
    # E2436b969 MainActivity.init -> ListFragment.<init>: explicit call, no action.
    r.comment('init() adds the list fragment', 'E2436b969')
    # E54b170af ListFragment.<init> -> ListFragment.onActivityCreated: lifecycle, no action.
    r.comment('Fragment lifecycle callback', 'E54b170af')
    # Ef86ebfe1 ListFragment.onActivityCreated -> ListFragment.init: explicit call, no action.
    r.comment('init()', 'Ef86ebfe1')
    # E7e3c321b ListFragment.init -> S_LIST@NOTES: list set up, no action.
    r.comment('List set up on the default Notes navigation', 'E7e3c321b')
    # E01d0dfd6 S_LIST@NOTES -> Fab.lambda$init$1@LONG_NOTES: long-press the + button
    # (FloatingActionsMenu add button, res/layout/fab.xml id fab).
    r.long_tap('E01d0dfd6', res_id='it.feio.android.omninotes:id/fab')
    # Ee5d1ab81 Fab long-press -> ListFragment.lambda$initFab$0@MAIN: menu dispatch, no action.
    r.comment('onFabItemClick(fab_expand_menu_button)', 'Ee5d1ab81')
    # E8a16cf02 lambda$initFab$0@MAIN -> S_DETAIL@NEW: a new note opens, no action.
    r.comment('A new note is opened', 'E8a16cf02')
    # --- Setup on the detail screen (logged under E8a16cf02, see header) ---
    # Title and content (fragment_detail.xml ids detail_title/detail_content).
    r.tap('E8a16cf02', res_id='it.feio.android.omninotes:id/detail_title')
    r.type_text(NOTE_TITLE, 'E8a16cf02')
    r.tap('E8a16cf02', res_id='it.feio.android.omninotes:id/detail_content')
    r.type_text('Note with a sketch and a reminder.', 'E8a16cf02')
    # Attachment -> Sketch (menu_detail.xml "Attachment"; attachment_dialog
    # "Sketch"). Back in the sketch saves it (MainActivity.onBackPressed
    # calls SketchFragment.save) and returning to the detail screen adds
    # the MIME_TYPE_SKETCH attachment.
    r.tap('E8a16cf02', text='Attachment')
    r.tap('E8a16cf02', text='Sketch')
    # Stroke (REQUIRED — see header): long-press the drawing view
    # (res/layout/fragment_sketch.xml id drawing). SketchView.onTouch
    # ACTION_DOWN calls touch_start (SketchView.java:135-136), which
    # adds a one-touch path (moveTo + lineTo, :167-186) in default draw
    # mode, so getBitmap() is non-null, save() writes the file and sets
    # sketchUri, and onResume adds the MIME_TYPE_SKETCH attachment.
    # Without this stroke the save writes nothing (auditor FAIL fix).
    r.long_tap('E8a16cf02', res_id='it.feio.android.omninotes:id/drawing')
    r.back('E8a16cf02')
    # Reminder row -> SublimePicker dialog; confirm with the preset, which
    # for a new note is now + 60 seconds (see header). UNCERTAIN confirm
    # selector: library UI, not in app res (see header).
    r.tap('E8a16cf02', res_id='it.feio.android.omninotes:id/reminder_layout')
    r.tap('E8a16cf02', text='Ok')
    # E1a48ab1f S_DETAIL@NEW -> MainActivity.onBackPressed@DETAIL_SAVE:
    # press Back to save the note (saveAndExit).
    r.back('E1a48ab1f')
    # E4455444c onBackPressed@DETAIL_SAVE -> DetailFragment.saveAndExit@SAVE:
    # explicit call, no action.
    r.comment('saveAndExit()', 'E4455444c')
    # Eca06fe26 saveAndExit@SAVE -> DetailFragment.saveNote@SAVE: explicit call, no action.
    r.comment('saveNote()', 'Eca06fe26')
    # E67ba23d6 saveNote@SAVE -> SaveNoteTask.doInBackground: async task, no action.
    r.comment('SaveNoteTask.doInBackground', 'E67ba23d6')
    # E5ccc83ff doInBackground -> ReminderHelper.addReminder(Context,Note):
    # explicit call, no action.
    r.comment('ReminderHelper.addReminder(context, note)', 'E5ccc83ff')
    # E142b6fe8 addReminder(Context,Note) -> addReminder(Context,Note,long):
    # explicit call; AlarmManager.setExact schedules the alarm, no action.
    r.comment('AlarmManager.setExact schedules the alarm a minute ahead', 'E142b6fe8')
    # E59f83d06 addReminder -> AlarmReceiver.onReceive: the alarm fires.
    # Wait (up to 300 s, inside the 10-minute script budget) for the
    # notification, whose title is the note title. The wait returns as
    # soon as the notification appears (about a minute after the save).
    r.wait_for('E59f83d06', text=NOTE_TITLE, timeout=300)
    r.comment('The alarm fired: AlarmReceiver.onReceive', 'E59f83d06')
    # Ee8501df3 onReceive -> AlarmReceiver.createNotification: explicit call, no action.
    r.comment('createNotification builds the reminder notification', 'Ee8501df3')
    # Eef154c6b createNotification -> BitmapHelper.getBitmapFromAttachment:
    # first attachment is a sketch (not files), so the bitmap path runs.
    r.comment('First attachment is a sketch: getBitmapFromAttachment', 'Eef154c6b')
    # E3b82664d getBitmapFromAttachment -> BitmapHelper.getImageBitmap:
    # interface dispatch; the coverage lookup detects the target.
    r.comment('Sketch attachment dispatches to getImageBitmap', 'E3b82664d')
    # Tap the notification (post-target evidence, same edge): opens SnoozeActivity.
    r.tap('E3b82664d', text=NOTE_TITLE)
    r.done()


if __name__ == '__main__':
    main()
