STATUS: RUNNING 18:33

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| Coders$DeflateDecoder$DeflateDecoderInputStream.close | REACHABLE | CALL | Called from wrapper to close stream and end Inflater | SRC commons_compress_7z/.../Coders.java:159-165 (already in graph_def.py line 1744, 5709) |
| Coders$DeflateDecoder$DeflateDecoderInputStream.read() | REACHABLE | CALL | Delegates to InflaterInputStream.read for decompression | SRC commons_compress_7z/.../Coders.java:154 (already in graph_def.py line 1741, 5706) |
| Coders$DeflateDecoder$DeflateDecoderInputStream.read(byte[]) | REACHABLE | CALL | Delegates to InflaterInputStream.read overload | SRC commons_compress_7z/.../Coders.java:162 (covered by .read edge in graph_def.py) |
| Coders$DeflateDecoder$DeflateDecoderInputStream.read(byte[],int,int) | REACHABLE | CALL | Delegates to InflaterInputStream.read overload | SRC commons_compress_7z/.../Coders.java:158 (covered by .read edge in graph_def.py) |
| Coders$DeflateDecoder$DeflateDecoderOutputStream.<init> | REACHABLE | CALL | Constructed by DeflateDecoder.encode for compression | SRC commons_compress_7z/.../Coders.java:147, 176 (already in graph_def.py line 1735, 5701) |
| Coders$DeflateDecoder$DeflateDecoderOutputStream.close | REACHABLE | CALL | Called to close stream and end Deflater | SRC commons_compress_7z/.../Coders.java:183-189 (already in graph_def.py line 1750, 5718) |
| Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[]) | REACHABLE | CALL | Delegates to DeflaterOutputStream.write overload | SRC commons_compress_7z/.../Coders.java:209 (covered by .write edge in graph_def.py) |
| Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[],int,int) | REACHABLE | CALL | Delegates to DeflaterOutputStream.write overload | SRC commons_compress_7z/.../Coders.java:214 (covered by .write edge in graph_def.py) |
| Coders$DeflateDecoder$DeflateDecoderOutputStream.write(int) | REACHABLE | CALL | Delegates to DeflaterOutputStream.write overload | SRC commons_compress_7z/.../Coders.java:204 (covered by .write edge in graph_def.py) |
| Coders$DeflateDecoder.encode | REACHABLE | CALL | Called via Coders.addEncoder for 7z compression | SRC commons_compress_7z/.../Coders.java:145-147 (already in graph_def.py line 1722, 5690) |
| Coders.addEncoder | REACHABLE | CALL | Registers encoder for given compression method | SRC commons_compress_7z/.../Coders.java:82-89 (already in graph_def.py via Coders edges) |
| ColorAdapter.<init> | REACHABLE | CALL | Constructed by ColorPref.showColorChooser for color selection dialog | SRC ColorAdapter.java:31-37 (already in graph_def.py line 1758, 5721) |
| ColorAdapter.getColorResAt | REACHABLE | CALL | Called by ColorAdapter.getView to retrieve color resource at position | SRC ColorAdapter.java:40-42, called at line 55 (already in graph_def.py line 1762, 5725) |
| ColorAdapter.getView | REACHABLE | FRAMEWORK | ArrayAdapter callback: GridView renders items by calling adapter.getView | SRC ColorAdapter.java:45-61 (already in graph_def.py line 1766, 5729) |
| ColorAdapter.onItemClick | REACHABLE | GUI | AdapterView.OnItemClickListener: GridView dispatches item click | SRC ColorAdapter.java:63-67 (already in graph_def.py line 1770, 5733) |
| ColorCircleDrawable.draw | REACHABLE | FRAMEWORK | Drawable.draw overridden: called by Android view rendering | SRC ColorCircleDrawable.java:43-46 (already in graph_def.py line 1511, 5507) |
| ColorCircleDrawable.getOpacity | REACHABLE | FRAMEWORK | Drawable.getOpacity overridden: called by Android drawable framework | SRC ColorCircleDrawable.java:64-66 (already in graph_def.py line 1527, 5527) |
| ColorCircleDrawable.onBoundsChange | REACHABLE | FRAMEWORK | Drawable.onBoundsChange overridden: called when bounds set by framework | SRC ColorCircleDrawable.java:49-52 (already in graph_def.py line 1515, 5511) |
| ColorCircleDrawable.setAlpha | REACHABLE | FRAMEWORK | Drawable.setAlpha overridden: called by Android drawable operations | SRC ColorCircleDrawable.java:55-57 (already in graph_def.py line 1519, 5515) |
| ColorCircleDrawable.setColorFilter | REACHABLE | FRAMEWORK | Drawable.setColorFilter overridden: called by Android drawable operations | SRC ColorCircleDrawable.java:60-62 (already in graph_def.py line 1523, 5519) |
| ColorPickerDialog$ColorItemPair.<init> | REACHABLE | CALL | Constructed during ColorPickerDialog static COLORS array initialization | SRC ColorPickerDialog.java:244-246 (constructor), called at 48-55 (already in graph_def.py line 1593, 5827) |
| ColorPickerDialog$SavedState$1.<init> | REACHABLE | CALL | Anonymous Parcelable.Creator constructed during SavedState.<clinit> | SRC ColorPickerDialog.java:293-301 (already in graph_def.py line 1621, 5851) |
| ColorPickerDialog$SavedState$1.createFromParcel | REACHABLE | FRAMEWORK | Parcelable.Creator.createFromParcel called by Android during deserialization | SRC ColorPickerDialog.java:295-297 (already in graph_def.py line 1625, 5855) |
| ColorPickerDialog$SavedState$1.newArray | REACHABLE | FRAMEWORK | Parcelable.Creator.newArray called by Android for array allocation | SRC ColorPickerDialog.java:298-300 (already in graph_def.py line 1629, 5859) |
| ColorPickerDialog$SavedState.<clinit> | REACHABLE | FRAMEWORK | Static initialization triggered when SavedState class first accessed | SRC ColorPickerDialog.java:275-301 (CREATOR field, already in graph_def.py line 1612, 5843) |
| ColorPickerDialog$SavedState.<init>(Parcel) | REACHABLE | FRAMEWORK | Parcel constructor called by createFromParcel during deserialization | SRC ColorPickerDialog.java:277-280 (already in graph_def.py line 1603, 1608, 5835, 5839) |
| ColorPickerDialog$SavedState.<init>(Parcelable) | REACHABLE | CALL | Parcelable constructor called by ColorPickerDialog.onSaveInstanceState | SRC ColorPickerDialog.java:288-290 (constructor), called at 255-256 (already in graph_def.py line 1598, 5831) |
| ColorPickerDialog$SavedState.writeToParcel | REACHABLE | FRAMEWORK | Parcelable.writeToParcel called by Android state serialization framework | SRC ColorPickerDialog.java:282-285 (already in graph_def.py line 1616, 5847) |

STATUS: DONE 18:33
