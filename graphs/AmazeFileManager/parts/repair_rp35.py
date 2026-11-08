# Repair batch 35 - AmazeFileManager
# Generated: 2025-01-20 22:48
# All methods from rp_35.txt checked

# Utils.<init> - Utility class constructor, never instantiated
UNREACHABLE['Utils.<init>'] = (
    'no_trigger_in_app',
    'Utility class with only static methods (clamp, getViewRawY, setTint, getDate, getColor, dpToPx, differenceStrings, disableScreenRotation, etc.); constructor never instantiated in app source',
    'SRC utils/Utils.java:59 public class Utils { ... public static float clamp... public static float getViewRawY... public static void setTint... (all methods are static, no instance methods)',
    'SOURCE'
)

# GREP PROOF for Utils.<init> being unreachable:
# Command: grep -rn "new Utils()" app/src/main/java --include="*.java"
# Result: No matches found (no instantiations in app code)
# The class at utils/Utils.java:59-300+ contains only static methods and private static constants.
# No calls to new Utils() exist in the application source.
