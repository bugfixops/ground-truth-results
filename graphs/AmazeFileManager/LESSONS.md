# AmazeFileManager — LESSONS.md

- Manifest citations rot between schema versions: re-derive every ENTRY
  block range from the printed manifest; a systematic shift (here, all 8
  services plus the receiver) hides behind individually plausible ranges.
- One executor's AsyncTask edges got linked to every task in the graph
  (ZipService.execute -> 7 unrelated doInBackground/onPostExecute methods).
  Only route-level reading catches a builder heuristic error like that; a
  label count never will.
- Superclass-summary edges silently conflate instances: a shared
  BasicActivity.<init> node linked to one subclass's onCreate makes a
  DatabaseViewerActivity prefix "reach" TextEditorActivity. Always print
  the actual `extends` clause before trusting a lifecycle chain.
- Virtual dispatch decides Glide reachability, not the declared type: the
  receiver of `.listener()` is a GlideRequest at runtime (via
  GlideApp.with().asDrawable()), and a method reference is a call site
  when the receiver invokes it (setImageBroken via OnImageProcessed).
- Sibling stream classes must not be crossed: the SMB server reads a
  SmbStreamer StreamSource and the cloud server reads a CloudStreamSource.
  The server doing the reading determines the target, not the shared
  RandomAccessStream parent.
- Sample draws are route-sensitive: fixing edges redraws the sample, so
  the final table is only valid on the post-fix draw, and dropped routes'
  fixes still belong in the fix log.
- The checker's citation resolver needs the basename form for some paths
  (DecryptService): a correct line number with the wrong path form still
  fails check 2, so match the form passing citations already use.

## Re-audit lessons (Kiro, November 2026)

- Clearing a baseline gate can move many best routes onto an outside entry that was cheaper before; after every baseline edit, count the methods whose best route carries an env gate, not only the cleared texts.
- A gate edit changes the edge id (the id hashes the gate texts), so device route files and verification paths that name edge ids go stale; map old to new ids by src, dst and kind before a dry run.
- Check anonymous-class numbers with javap: javac numbers them in source order, and one skipped number shifts every later class.

- A CLASSIFY rule that matches a class name as a substring can catch app classes (GlideApp matched GlideApplication); match the class part of the node name exactly.
- When a filter drops INFERRED hand edges, check that each dropped creation edge has a real replacement: PreferencesActivity was left with only its env entry, so all its methods became library.
- Data that only an earlier network session can write (a saved SSH host key) is env network, not state.
- A hand CALL edge must cite a line inside its own src method. Run kiro_scripts/cited_line_in_caller.py after a batch of hand edges: the summary-style edges (an outer method "calling" what its helper, inner class or field initializer calls) can be the only route to a method, and cutting them can leave dead methods that looked reachable.
