# UNVERIFIED RE-CHECK — DO NOT RELY ON, MERGE, OR USE AS EVIDENCE YET

**Status: UNVERIFIED.** This is a re-check part from 2026-10-31, saved here so it is not lost. It has NOT passed a build, sampler, full-repo grep, or C1 checks on a full local checkout, and must be re-checked from printed source before any label, route, or graph change is relied on or merged. Batches 13-18 were unverified when the Claude run stopped.

**Branch rule:** work in progress is on work-2026-10-31 only, never main, and the 'result' branch is not used for work in progress unless the user says so.

---

# LibreTorrent batch 16 — PROPOSED PART (UNVERIFIED / INCOMPLETE)

- Repo: bugfixops/ground-truth-results, branch: work-2026-10-31
- Batch source: handoff/LIBRETORRENT_BATCH_PLAN.tsv, SHA 0104806dd666c840049b3db52823d4b384fa1c92, filtered batch=16. Plan status is a CANDIDATE, not evidence.
- Methods in batch: 40 (max 40, so batch size is compliant).
- Methods actually judged from printed source in this session: 0.
- Proposed labels: NONE completed. Every row below is OPEN / partial, not a complete verdict.
- No push, no edit to graph_def.py, out/, or any branch was made. No build, sampler, grep, or C1 count is claimed.
- Connector limitation: GitHub MCP returned HTTP 429 ("too many requests") during this session — first on handoff/CHATGPT_PROMPT_LIBRETORRENT_3.md, then on a re-fetch of the batch plan. Per the hard-stop rule, no further GitHub connector calls were made after the 429. Therefore the following were NOT read in this session and remain unverified:
  - handoff/CHATGPT_PROMPT_LIBRETORRENT_3.md (not read at all)
  - graphs/LibreTorrent/parts/b016.md (labels in it NOT reported here; a separate helper handles merge status — do not assume merged or unmerged)
  - graphs/LibreTorrent/scratch/b016* (not read)
  - Source root listing for final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/ (not listed)
  - Any NanoHTTPD source file, any fw_src/android-8.1.0_r1/ file, and any graphs/LibreTorrent/ file beyond AGENT_NOTES.md excerpts
  - search_code was not run; no full-repo grep is claimed. For any generated/library code, a real full-repo grep is still required.
- Prior AGENT_NOTES.md claim that batch 16 has "16 supported UNREACHABLE labels and 24 OPEN rows": treated as UNVERIFIED, not re-derived, not relied on.
- AGENT_NOTES.md section "## Stopped by the user" (2026-10-31, about 18:10 EDT), as read in this session: the Claude run was stopped mid-batch, handoff/STOP_CONVERT was written, last files written included scratch/b013 to scratch/b017 and parts/b016.md, batches 13–18 are unverified, and parts/b016.md merge into graph_def.py must be checked (handled by a separate helper).
- Rules files partially read (tool output was truncated at 12,000 chars per file, so full-text reading was not completed in this session): handoff/MUSE_HANDOVER.md (first ~20,000 chars), handoff/KIRO_CONVERT_APPS.md, handoff/KIRO_CORRECTIONS.md, handoff/SCHEMA_V2.md, handoff/AGENT_BRIEF_V2.md, handoff/CONVERSION_RECIPE.md.
- confirmed_by: none assigned. No row uses DYN, FW-MEMORY, or UNVERIFIED as a label confirmation. No UNREACHABLE kind is assigned in this proposal.
- What remains unverified and why, for every row: definition lines, call/route steps, caller search, configuration/API-level closure, and framework dispatch were not printed from connector-readable files, because GitHub connector access stopped at the 429. Each method must be re-checked from printed source before any REACHABLE/UNREACHABLE label is proposed.

## Per-method table — batch 16 (all OPEN)

| # | method | descriptor | proposed label | UNREACHABLE kind | reason | printed-source citations | confirmed_by |
|---|---|---|---|---|---|---|---|
| 1 | NanoHTTPD$CookieHandler.set(String,String,int) | (Ljava/lang/String;Ljava/lang/String;I)V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 2 | NanoHTTPD$CookieHandler.set(Cookie) | (Lorg/nanohttpd/NanoHTTPD$Cookie;)V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 3 | NanoHTTPD$CookieHandler.unloadQueue | (Lorg/nanohttpd/NanoHTTPD$Response;)V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 4 | NanoHTTPD$DefaultAsyncRunner.<init> | ()V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 5 | NanoHTTPD$DefaultAsyncRunner.closeAll | ()V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 6 | NanoHTTPD$DefaultAsyncRunner.closed | (Lorg/nanohttpd/NanoHTTPD$ClientHandler;)V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 7 | NanoHTTPD$DefaultAsyncRunner.exec | (Lorg/nanohttpd/NanoHTTPD$ClientHandler;)V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 8 | NanoHTTPD$DefaultServerSocketFactory.<init> | ()V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 9 | NanoHTTPD$DefaultServerSocketFactory.create | ()Ljava/net/ServerSocket; | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 10 | NanoHTTPD$DefaultTempFile.<init> | (Ljava/io/File;)V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 11 | NanoHTTPD$DefaultTempFile.delete | ()V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 12 | NanoHTTPD$DefaultTempFile.getName | ()Ljava/lang/String; | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 13 | NanoHTTPD$DefaultTempFileManager.<init> | ()V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 14 | NanoHTTPD$DefaultTempFileManager.clear | ()V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 15 | NanoHTTPD$DefaultTempFileManager.createTempFile | (Ljava/lang/String;)Lorg/nanohttpd/NanoHTTPD$TempFile; | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 16 | NanoHTTPD$DefaultTempFileManagerFactory.<init> | (Lorg/nanohttpd/NanoHTTPD;)V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 17 | NanoHTTPD$DefaultTempFileManagerFactory.create | ()Lorg/nanohttpd/NanoHTTPD$TempFileManager; | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 18 | NanoHTTPD$HTTPSession.<init>(NanoHTTPD,TempFileManager,InputStream,OutputStream,InetAddress) | (Lorg/nanohttpd/NanoHTTPD;Lorg/nanohttpd/NanoHTTPD$TempFileManager;Ljava/io/InputStream;Ljava/io/OutputStream;Ljava/net/InetAddress;)V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 19 | NanoHTTPD$HTTPSession.decodeHeader | (Ljava/io/BufferedReader;Ljava/util/Map;Ljava/util/Map;Ljava/util/Map;)V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 20 | NanoHTTPD$HTTPSession.decodeMultipartFormData | (Ljava/lang/String;Ljava/lang/String;Ljava/nio/ByteBuffer;Ljava/util/Map;Ljava/util/Map;)V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 21 | NanoHTTPD$HTTPSession.decodeParms | (Ljava/lang/String;Ljava/util/Map;)V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 22 | NanoHTTPD$HTTPSession.execute | ()V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 23 | NanoHTTPD$HTTPSession.findHeaderEnd | ([BI)I | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 24 | NanoHTTPD$HTTPSession.getAttributeFromContentHeader | (Ljava/lang/String;Ljava/util/regex/Pattern;Ljava/lang/String;)Ljava/lang/String; | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 25 | NanoHTTPD$HTTPSession.getBodySize | ()J | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 26 | NanoHTTPD$HTTPSession.getBoundaryPositions | (Ljava/nio/ByteBuffer;[B)[I | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 27 | NanoHTTPD$HTTPSession.getHeaders | ()Ljava/util/Map; | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 28 | NanoHTTPD$HTTPSession.getMethod | ()Lorg/nanohttpd/NanoHTTPD$Method; | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 29 | NanoHTTPD$HTTPSession.getParms | ()Ljava/util/Map; | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 30 | NanoHTTPD$HTTPSession.getQueryParameterString | ()Ljava/lang/String; | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 31 | NanoHTTPD$HTTPSession.getTmpBucket | ()Ljava/io/RandomAccessFile; | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 32 | NanoHTTPD$HTTPSession.getUri | ()Ljava/lang/String; | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 33 | NanoHTTPD$HTTPSession.parseBody | (Ljava/util/Map;)V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 34 | NanoHTTPD$HTTPSession.saveTmpFile | (Ljava/nio/ByteBuffer;IILjava/lang/String;)Ljava/lang/String; | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 35 | NanoHTTPD$HTTPSession.scipOverNewLine | ([BI)I | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 36 | NanoHTTPD$Method.<clinit> | ()V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 37 | NanoHTTPD$Method.lookup | (Ljava/lang/String;)Lorg/nanohttpd/NanoHTTPD$Method; | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 38 | NanoHTTPD$Response.<init> | (Lorg/nanohttpd/NanoHTTPD$Response$IStatus;Ljava/lang/String;Ljava/io/InputStream;J)V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 39 | NanoHTTPD$Response.addHeader | (Ljava/lang/String;Ljava/lang/String;)V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |
| 40 | NanoHTTPD$Response.close | ()V | OPEN (not judged) | — | Not re-checked; plan candidate only | None printed in this session | — |

## Counts

- Methods in batch 16: 40
- Methods actually judged: 0
- REACHABLE proposed: 0
- UNREACHABLE proposed: 0
- OPEN / partial: 40
- Plan-candidate status for all 40 rows (for reference only, not evidence): TODO_CANDIDATE_REACHABLE / "REACHABLE (generator candidate, no hand route yet)".

## Next steps required before any label can be proposed

1. After the GitHub connector 429 clears, re-fetch (not from this file's plan copy alone) and read in full: handoff/CHATGPT_PROMPT_LIBRETORRENT_3.md, graphs/LibreTorrent/parts/b016.md, graphs/LibreTorrent/scratch/b016*, and list the source root final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/.
2. Locate NanoHTTPD source (app source vs. library) and print each method's definition plus every caller/route step; run a real full-repo grep for generated/library callers and save it to scratch/ before any UNREACHABLE claim.
3. Only then assign REACHABLE (with a hand route from an entry point) or UNREACHABLE with exactly one kind, a reason, a source reference, and confirmed_by SOURCE or INFERRED.
4. Do not decide any Yang/user decision, and do not use tool coverage, old generated graphs, or build REACHABLE counts as evidence.
