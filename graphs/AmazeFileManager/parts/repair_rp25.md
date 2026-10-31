# Repair Batch 25 Summary

STATUS: START 21:56
STATUS: DONE 21:59

## Methods Processed: 18 (20 methods in batch already had routes)

| Method | Status | Evidence |
|--------|--------|----------|
| AbstractProgressiveService.getDataPackage | REACHABLE | SRC ProcessViewerFragment.java:161-165; ProcessViewerFragment calls getDataPackage(i) in loop |
| AbstractProgressiveService.getDataPackageSize | REACHABLE | SRC ProcessViewerFragment.java:163; loop condition uses getDataPackageSize() |
| AbstractProgressiveService.isDecryptService | REACHABLE | SRC ServiceWatcherUtil.java:149; ServiceWatcherUtil checks isDecryptService for workaround |
| AppDataParcelable.describeContents | UNREACHABLE | SRC AppDataParcelable.java:32-34; Parcelable method returns 0, never called by app or framework for simple data |
| AppDataParcelable.writeToParcel | UNREACHABLE | SRC AppDataParcelable.java:37-44; Parcelable method not used, AppDataParcelable not parceled between processes |
| CheckBox.clearListenerInViewGroup | REACHABLE | SRC CheckBox.java:21; onBindView calls clearListenerInViewGroup to remove existing listener |
| CheckableCircleView.onDraw | REACHABLE | SRC CheckableCircleView.java:42-55; View framework calls onDraw when view renders |
| CircleGradientDrawable.<init>(String,AppTheme,DisplayMetrics) | UNREACHABLE | SRC CircleGradientDrawable.java:23-30; String color constructor overload not used, app uses int color variant |
| CircularColorsView.<init>(Context,AttributeSet) | REACHABLE | XML item_colorpicker.xml, selectedcolors_preference.xml; LayoutInflater inflates CircularColorsView from XML |
| CircularColorsView.init | REACHABLE | SRC CircularColorsView.java:32,37; both constructors call init() |
| CircularColorsView.onDraw | REACHABLE | SRC CircularColorsView.java:57-89; View framework calls onDraw, CircularColorsView used in layouts |
| CloudIconDataFetcher.cleanup | REACHABLE | SRC CloudIconDataFetcher.java:53-59; Glide framework calls DataFetcher.cleanup after loading |
| CloudIconDataFetcher.getDataClass | REACHABLE | SRC CloudIconDataFetcher.java:67-70; Glide framework calls getDataClass to determine data type |
| CloudIconDataFetcher.getDataSource | REACHABLE | SRC CloudIconDataFetcher.java:73-77; Glide framework calls getDataSource for caching strategy |
| CloudStreamer.isStreamMedia | UNREACHABLE | SRC CloudStreamer.java:44-46; static method for SmbFile pattern matching, not called from app |
| Coders$BCJDecoder.encode | REACHABLE | SRC Coders.java:85-92,59-65,119-128; addEncoder calls BCJDecoder.encode for BCJ_*_FILTER methods |
| Coders$BZIP2Decoder.encode | REACHABLE | SRC Coders.java:85-92,54,256-260; addEncoder calls BZIP2Decoder.encode for BZIP2 method |
| Coders$CopyDecoder.encode | REACHABLE | SRC Coders.java:85-92,51,107-110; addEncoder calls CopyDecoder.encode for COPY method |

## Counts
- REACHABLE: 14
- UNREACHABLE: 4
- INCOMPLETE: 0

