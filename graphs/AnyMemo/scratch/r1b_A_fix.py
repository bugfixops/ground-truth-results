"""Round 1b Group A follow-up: Oauth2AccountActivity.onDestroy had no path (the one error left after r1b_A.py).
The real exit is DropboxOauth2AccountActivity.onAuthenticated, which calls finish() (DropboxOauth2AccountActivity.java:29).
Oauth2AccountActivity.onDestroy (Oauth2AccountActivity.java:53-55) is inherited by that subclass, so the edge goes to the base node."""
import sys
sys.path.insert(0, '/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch')
from r1b_tool import apply

OLD = "e('DropboxOauth2AccountActivity.onAuthenticated', 'DropboxListActivity.<init>', 'ENTRY', 'startActivity(DropboxListActivity); finish()', env=ENV_OAUTH_CALLBACK, evidence='SRC downloader/dropbox/DropboxOauth2AccountActivity.java:25-30')"
NEW = OLD + """
# A1 (round 1b): the same finish() in onAuthenticated destroys this activity. onDestroy is declared in Oauth2AccountActivity and inherited
# (DropboxOauth2AccountActivity does not override it), so the edge goes to the base node.
e('DropboxOauth2AccountActivity.onAuthenticated', 'Oauth2AccountActivity.onDestroy', 'LIFECYCLE', 'onAuthenticated: startActivity(DropboxListActivity), then finish(): this activity is destroyed (inherited Oauth2AccountActivity.onDestroy)',
  evidence=FW_ACTIVITY + '; SRC downloader/dropbox/DropboxOauth2AccountActivity.java:25-30 (finish at :29); downloader/oauth/Oauth2AccountActivity.java:53-55')"""

apply([(OLD, NEW)], 'round 1b group A follow-up (Oauth2 onDestroy)')
