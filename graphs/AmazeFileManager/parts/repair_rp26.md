# Repair Batch 26 Summary
STATUS: START 21:56

## Methods Processed: 40

| Method | Status | Evidence |
|--------|--------|----------|
| Coders$DeflateDecoder$DeflateDecoderInputStream.close | REACHABLE | SRC Coders.java:179-185; called via InputStream interface when DeflateDecoder stream is closed |
| Coders$DeflateDecoder$DeflateDecoderInputStream.read() | REACHABLE | SRC Coders.java:167-169; called via InputStream interface when reading from DeflateDecoder stream |
| Coders$DeflateDecoder$DeflateDecoderInputStream.read(byte[]) | REACHABLE | SRC Coders.java:175-177; called via InputStream interface when reading from DeflateDecoder stream |
| Coders$DeflateDecoder$DeflateDecoderInputStream.read(byte[],int,int) | REACHABLE | SRC Coders.java:171-173; called via InputStream interface when reading from DeflateDecoder stream |
| Coders$DeflateDecoder$DeflateDecoderOutputStream.<init> | INCOMPLETE | Caller Coders$DeflateDecoder.encode has no route (not in this batch) |
| Coders$DeflateDecoder$DeflateDecoderOutputStream.close | INCOMPLETE | Depends on Coders$DeflateDecoder.encode being REACHABLE first |
| Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[]) | INCOMPLETE | Depends on Coders$DeflateDecoder.encode being REACHABLE first |
| Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[],int,int) | INCOMPLETE | Depends on Coders$DeflateDecoder.encode being REACHABLE first |
| Coders$DeflateDecoder$DeflateDecoderOutputStream.write(int) | INCOMPLETE | Depends on Coders$DeflateDecoder.encode being REACHABLE first |
| ColorAdapter.<init> | INCOMPLETE | Caller ColorPref.colorChangeDialog → ColorPref.onPreferenceClick needs REGISTER edge from reloadListeners |
| ColorAdapter.getColorResAt | INCOMPLETE | Depends on ColorAdapter route |
| ColorAdapter.getView | INCOMPLETE | Depends on ColorAdapter route |
| ColorAdapter.onItemClick | INCOMPLETE | Depends on ColorAdapter route |
| ColorCircleDrawable.draw | INCOMPLETE | Caller TabFragment.updateIndicator needs route |
| ColorCircleDrawable.getOpacity | INCOMPLETE | Depends on ColorCircleDrawable route |
| ColorCircleDrawable.onBoundsChange | INCOMPLETE | Depends on ColorCircleDrawable route |
| ColorCircleDrawable.setAlpha | INCOMPLETE | Depends on ColorCircleDrawable route |
| ColorCircleDrawable.setColorFilter | INCOMPLETE | Depends on ColorCircleDrawable route |
| ColorPickerDialog.<clinit> | INCOMPLETE | Existing edge from undefined 'PreferenceScreen' node |
| ColorPickerDialog.<init> | INCOMPLETE | Depends on ColorPickerDialog.<clinit> route |
| ColorPickerDialog.getColor | INCOMPLETE | Depends on ColorPickerDialog route |
| ColorPickerDialog.getSummary | INCOMPLETE | Depends on ColorPickerDialog route |
| ColorPickerDialog.inflateItem | INCOMPLETE | Depends on ColorPickerDialog route |
| ColorPickerDialog.lambda$inflateItem$0 | INCOMPLETE | Depends on ColorPickerDialog route |
| ColorPickerDialog.onBindDialogView | INCOMPLETE | Depends on ColorPickerDialog route |
| ColorPickerDialog.onDialogClosed | INCOMPLETE | Depends on ColorPickerDialog route |
| ColorPickerDialog.onGetDefaultValue | INCOMPLETE | Depends on ColorPickerDialog route |
| ColorPickerDialog.onRestoreInstanceState | INCOMPLETE | Depends on ColorPickerDialog route |
| ColorPickerDialog.onSaveInstanceState | INCOMPLETE | Depends on ColorPickerDialog route |
| ColorPickerDialog.select | INCOMPLETE | Depends on ColorPickerDialog route |
| ColorPickerDialog.showDialog | INCOMPLETE | Depends on ColorPickerDialog route |
| ColorPickerDialog$ColorItemPair.<init> | INCOMPLETE | Depends on ColorPickerDialog route |
| ColorPickerDialog$SavedState.<clinit> | INCOMPLETE | Depends on ColorPickerDialog route |
| ColorPickerDialog$SavedState.<init>(Parcel) | INCOMPLETE | Depends on ColorPickerDialog route |
| ColorPickerDialog$SavedState.<init>(Parcelable) | INCOMPLETE | Depends on ColorPickerDialog route |
| ColorPickerDialog$SavedState.writeToParcel | INCOMPLETE | Depends on ColorPickerDialog route |
| ColorPickerDialog$SavedState$1.<init> | INCOMPLETE | Depends on ColorPickerDialog route |
| ColorPickerDialog$SavedState$1.createFromParcel | INCOMPLETE | Depends on ColorPickerDialog route |
| ColorPickerDialog$SavedState$1.newArray | INCOMPLETE | Depends on ColorPickerDialog route |

STATUS: DONE 22:05

## Counts
- REACHABLE: 4
- UNREACHABLE: 0
- INCOMPLETE: 36

STATUS: INCOMPLETE Coders$DeflateDecoder$DeflateDecoderOutputStream.<init> Coders$DeflateDecoder$DeflateDecoderOutputStream.close Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[]) Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[],int,int) Coders$DeflateDecoder$DeflateDecoderOutputStream.write(int) ColorAdapter.<init> ColorAdapter.getColorResAt ColorAdapter.getView ColorAdapter.onItemClick ColorCircleDrawable.draw ColorCircleDrawable.getOpacity ColorCircleDrawable.onBoundsChange ColorCircleDrawable.setAlpha ColorCircleDrawable.setColorFilter ColorPickerDialog.<clinit> ColorPickerDialog.<init> ColorPickerDialog.getColor ColorPickerDialog.getSummary ColorPickerDialog.inflateItem ColorPickerDialog.lambda$inflateItem$0 ColorPickerDialog.onBindDialogView ColorPickerDialog.onDialogClosed ColorPickerDialog.onGetDefaultValue ColorPickerDialog.onRestoreInstanceState ColorPickerDialog.onSaveInstanceState ColorPickerDialog.select ColorPickerDialog.showDialog ColorPickerDialog$ColorItemPair.<init> ColorPickerDialog$SavedState.<clinit> ColorPickerDialog$SavedState.<init>(Parcel) ColorPickerDialog$SavedState.<init>(Parcelable) ColorPickerDialog$SavedState.writeToParcel ColorPickerDialog$SavedState$1.<init> ColorPickerDialog$SavedState$1.createFromParcel ColorPickerDialog$SavedState$1.newArray
