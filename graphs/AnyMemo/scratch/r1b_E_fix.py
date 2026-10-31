"""Round 1b Group E follow-up: the two ConvertIntentService notification CALLs started at the base onHandleIntent,
which no route reaches after E17 split the service into @IMPORT and @EXPORT. They are re-pointed to both variants."""
import sys
sys.path.insert(0, '/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch')
from r1b_tool import apply

OLD_S = ("e('ConvertIntentService.onHandleIntent', 'ConvertIntentService.showSuccessNotification', 'CALL', "
         "'the conversion succeeds', evidence='SRC service/ConvertIntentService.java:124-134')")
OLD_F = ("e('ConvertIntentService.onHandleIntent', 'ConvertIntentService.showFailureNotification', 'CALL', "
         "'the conversion throws', evidence='SRC service/ConvertIntentService.java:136-138')")

new_lines = ["# Round 1b E17 follow-up: the notification CALLs start at both variants (the base onHandleIntent is no longer reached)"]
for v in ['IMPORT', 'EXPORT']:
    new_lines.append("e('ConvertIntentService.onHandleIntent@%s', 'ConvertIntentService.showSuccessNotification', 'CALL', "
                     "'the conversion succeeds', evidence='SRC service/ConvertIntentService.java:124-134')" % v)
for v in ['IMPORT', 'EXPORT']:
    new_lines.append("e('ConvertIntentService.onHandleIntent@%s', 'ConvertIntentService.showFailureNotification', 'CALL', "
                     "'the conversion throws', evidence='SRC service/ConvertIntentService.java:136-138')" % v)
NEW = '\n'.join(new_lines)

# Replace the two base lines with the variant block; the first pair carries the header comment.
apply([(OLD_S + '\n' + OLD_F, NEW)], 'E17-notify')
