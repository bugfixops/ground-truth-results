"""Device route script route_07 for Omni-Notes.

Method: RecurrenceHelper.nextReminderFromRecurrenceRule(long,long,String)
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 E7e3c321b Ef79712d5 E2c4c48d6 Ef9fd85cd E952f31c8 E112a1aa5
    E2632b1a3 E9b926ab3 E050a5e16 E7b616824 E4c2ac593 Ed9ed730e Ed4a4a1f1
    E6d04afda Eae44adee
Printed route: graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/sample_30_routes.txt
    (RecurrenceHelper.nextReminderFromRecurrenceRule(long,long,String), 22 steps;
    ListFragment.java:893-899; SnoozeActivity.java:55-60,138-150)
Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    none.
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

One block per route edge, in route order. Lifecycle, page, explicit-call, and
framework edges with no user action get a comment, not an action. Every action
names an edge id of this route (the harness enforces it). The note the route
needs (STATE "at least one note exists") is created as STATE steps folded
into the Ef79712d5 block, before that edge's own long-press, following the
precedent for STATE steps in other device scripts; it is marked STATE there,
not presented as the Ef79712d5 trigger itself.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af '
            'Ef86ebfe1 E7e3c321b Ef79712d5 E2c4c48d6 Ef9fd85cd E952f31c8 '
            'E112a1aa5 E2632b1a3 E9b926ab3 E050a5e16 E7b616824 E4c2ac593 '
            'Ed9ed730e Ed4a4a1f1 E6d04afda Eae44adee').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_07', EDGE_IDS, a.log,
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
    # Ef79712d5 S_LIST@NOTES -> ListFragment.lambda$initListView$3@START_NOTES:
    # long-press a note. STATE first (this edge needs a note to exist): create
    # one the way route_01 creates a note — long-press the + button
    # (FloatingActionsMenu add button, res/layout/fab.xml id fab), tap the
    # title field (res/layout/fragment_detail.xml id detail_title) and the
    # content field (res/layout/fragment_detail_content.xml id
    # detail_content), type, then Back saves the note and returns to the list.
    r.long_tap('Ef79712d5', res_id='it.feio.android.omninotes:id/fab')
    r.tap('Ef79712d5', res_id='it.feio.android.omninotes:id/detail_title')
    r.type_text('Route07 note', 'Ef79712d5')
    r.tap('Ef79712d5', res_id='it.feio.android.omninotes:id/detail_content')
    r.type_text('Route07 reminder note', 'Ef79712d5')
    r.back('Ef79712d5')
    # The edge's own trigger: long-press the note just created (its title is
    # the row text in res/layout/note_layout.xml, id note_title).
    r.long_tap('Ef79712d5', text='Route07 note')
    # E2c4c48d6 lambda$initListView$3@START_NOTES -> S_LIST_CAB@NOTES_1: one note
    # is selected, the contextual action bar replaces the toolbar, no action.
    r.comment('One note selected: the contextual action bar replaces the toolbar', 'E2c4c48d6')
    # Ef9fd85cd S_LIST_CAB@NOTES_1 -> ListFragment$ModeCallback.onActionItemClicked@REMINDER:
    # tap "Add reminder" in the action bar (menu_list.xml, title "Add reminder";
    # the item has no icon, so it shows as text).
    r.tap('Ef9fd85cd', text='Add reminder')
    # E952f31c8 onActionItemClicked@REMINDER -> performAction@C_REMINDER:
    # explicit call, no action.
    r.comment('performAction(item, mode)', 'E952f31c8')
    # E112a1aa5 performAction@C_REMINDER -> ListFragment.addReminders: the
    # reminder branch of the action switch, no action.
    r.comment('The reminder branch of the action switch', 'E112a1aa5')
    # E2632b1a3 ListFragment.addReminders -> SnoozeActivity.<init>: intent,
    # no action.
    r.comment('startActivityForResult(SnoozeActivity, ACTION_POSTPONE)', 'E2632b1a3')
    # E9b926ab3 SnoozeActivity.<init> -> SnoozeActivity.onCreate: lifecycle, no action.
    r.comment('Activity lifecycle callback', 'E9b926ab3')
    # E050a5e16 SnoozeActivity.onCreate -> SnoozeActivity.postpone: several notes
    # were sent from the list, so postpone(nextMinute) runs, no action.
    r.comment('Several notes sent from the list: postpone(nextMinute)', 'E050a5e16')
    # E7b616824 SnoozeActivity.postpone -> S_REMINDER_PICKER@SNOOZE: the picker
    # is shown over the list, no action.
    r.comment('The reminder picker is shown over the list', 'E7b616824')
    # E4c2ac593 S_REMINDER_PICKER@SNOOZE -> ReminderPickers$1.onDateTimeRecurrenceSet@SNOOZE:
    # pick a date and time and tap OK. UNCERTAINTY (see report): the picker is
    # the SublimePicker library dialog (ReminderPickers.java), not app XML, so
    # the recurrence-option label and the confirm-button label are not grounded
    # in app res. "Daily" is the recurrence option that makes
    # buildRecurrenceRuleByRecurrenceOptionAndRule return a non-empty rule
    # (any option other than DOES_NOT_REPEAT does), and "OK" follows the
    # trigger-graph gui text ("Pick a date and time and tap OK").
    r.tap('E4c2ac593', text='Daily')
    r.tap('E4c2ac593', text='OK')
    # Ed9ed730e onDateTimeRecurrenceSet@SNOOZE -> SnoozeActivity.onRecurrenceReminderPicked:
    # explicit call, no action.
    r.comment('OnReminderPickedListener.onRecurrenceReminderPicked', 'Ed9ed730e')
    # Ed4a4a1f1 onRecurrenceReminderPicked -> SnoozeActivity.setNextRecurrentReminder:
    # explicit call, no action.
    r.comment('setNextRecurrentReminder(note)', 'Ed4a4a1f1')
    # E6d04afda setNextRecurrentReminder -> RecurrenceHelper.nextReminderFromRecurrenceRule(long,String):
    # explicit call; the guard (the note has a recurrence rule, SnoozeActivity.java:55-60)
    # holds because a recurrence option was chosen in the picker, no action.
    r.comment('Guard holds: the note has a recurrence rule', 'E6d04afda')
    # Eae44adee nextReminderFromRecurrenceRule(long,String) ->
    # nextReminderFromRecurrenceRule(long,long,String): explicit call, no action;
    # the coverage lookup detects the target.
    r.comment('Direct call dispatching to the target overload', 'Eae44adee')
    r.done()


if __name__ == '__main__':
    main()
