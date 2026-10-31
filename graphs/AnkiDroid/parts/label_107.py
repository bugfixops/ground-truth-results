# AnkiDroid batch 107 (LABEL helper). MediaSyncer (3 methods), RemoteMediaServer (8) and RemoteServer (10): 21 methods, all REACHABLE.
# The full row list is in graphs/AnkiDroid/parts/label_107.md.
#
# No e() edges and no UNREACHABLE entries in this part. Every edge into or out of these 21 methods is an automatic
# CALL edge written by the builder (Connection.doInBackgroundSync and doInBackgroundLogin, Syncer.sync,
# HttpSyncer.req, and Syncer.throwExceptionIfCancelled), so none is repeated here.
# The AsyncTask launch edges that start the sync and login routes are owned by the Connection and DeckPicker batches.
