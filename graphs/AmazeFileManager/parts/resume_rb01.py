# ---- resume batch rb_01 (2025-01-15 18:36)
# 40 methods from build_resume_01 UNRESOLVED list
# Library classes (sevenz), flavor-only (AboutActivity), and app source methods

# NOTE: Many methods in this batch already have edges in graph_def.py
# This file documents new/confirmed labels only

# ===== Library classes: UNREACHABLE =====
# These are Apache Commons Compress 7-Zip library classes
# Source not in app src/main/java, no calls from app code

UNREACHABLE['AES256SHA256Decoder$1.read()'] = ('no_trigger_in_app', 'sevenz library class (Apache Commons Compress), grep -rn "AES256SHA256Decoder" in app src/main/java shows no calls', 'INFERRED library source not in dataset', 'INFERRED')

UNREACHABLE['AES256SHA256Decoder$1.read(byte[],int,int)'] = ('no_trigger_in_app', 'sevenz library class (Apache Commons Compress), grep -rn "AES256SHA256Decoder" in app src/main/java shows no calls', 'INFERRED library source not in dataset', 'INFERRED')

UNREACHABLE['BoundedFileChannelInputStream.read()'] = ('no_trigger_in_app', 'sevenz library class (Apache Commons Compress), grep -rn "BoundedFileChannelInputStream" in app src/main/java shows no calls', 'INFERRED library source not in dataset', 'INFERRED')

UNREACHABLE['BoundedFileChannelInputStream.read(byte[],int,int)'] = ('no_trigger_in_app', 'sevenz library class (Apache Commons Compress), grep -rn "BoundedFileChannelInputStream" in app src/main/java shows no calls', 'INFERRED library source not in dataset', 'INFERRED')

UNREACHABLE['BoundedFileChannelInputStream.read(int)'] = ('no_trigger_in_app', 'sevenz library class (Apache Commons Compress), grep -rn "BoundedFileChannelInputStream" in app src/main/java shows no calls', 'INFERRED library source not in dataset', 'INFERRED')

UNREACHABLE['Archive.lengthOf(Object[])'] = ('no_trigger_in_app', 'sevenz library class (Apache Commons Compress), grep -rn "Archive\\\\.lengthOf" in app src/main/java shows no calls', 'INFERRED library source not in dataset', 'INFERRED')

UNREACHABLE['Archive.lengthOf(long[])'] = ('no_trigger_in_app', 'sevenz library class (Apache Commons Compress), grep -rn "Archive\\\\.lengthOf" in app src/main/java shows no calls', 'INFERRED library source not in dataset', 'INFERRED')

# ===== AboutActivity: INCOMPLETE (flavor-only source) =====
# AboutActivity source exists only in src/fdroid and src/play, not in src/main
# DATASET.txt does not name a flavor (KIRO_CONVERT_APPS section 2.3)
# Documented in graphs/AmazeFileManager/scratch/conflicts.md
# Methods: AboutActivity.<init>, AboutActivity.onClick, AboutActivity.onOptionsItemSelected, AboutActivity.openURL

