STATUS: RUNNING 23:20

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| GlideRequest.centerCrop | REACHABLE | | Called from RecyclerPreloadModelProvider constructor via GlideApp.with(fragment).asDrawable().centerCrop() | INFERRED RecyclerPreloadModelProvider.java:30 |
| GlideRequest.fitCenter | REACHABLE | | Called from AppsAdapterPreloadModel constructor via GlideApp.with(f).asDrawable().fitCenter() | INFERRED AppsAdapterPreloadModel.java:28 |
| GlideRequest.clone | REACHABLE | | Called from AppsAdapterPreloadModel.getPreloadRequestBuilder via request.clone().load(item) | INFERRED AppsAdapterPreloadModel.java:45 |
| GlideRequest.diskCacheStrategy | REACHABLE | | Called from RecyclerPreloadModelProvider.getPreloadRequestBuilder via request.load(...).diskCacheStrategy(...) | INFERRED RecyclerPreloadModelProvider.java:48 |
| GlideRequest.load(String) | REACHABLE | | Called from RecyclerPreloadModelProvider.getPreloadRequestBuilder where iconData.path is String | INFERRED RecyclerPreloadModelProvider.java:46,48 |
| GlideRequest.load(String) | REACHABLE | | Called from AppsAdapterPreloadModel methods where item parameter is String | INFERRED AppsAdapterPreloadModel.java:45,49 |
| GlideRequest.load(Integer) | REACHABLE | | Called from RecyclerPreloadModelProvider.getPreloadRequestBuilder where iconData.image is @DrawableRes int | INFERRED RecyclerPreloadModelProvider.java:50 |
| GlideRequest.<init>(Glide,RequestManager,Class,Context) | UNREACHABLE | no_trigger_in_app | Generated constructor; no direct instantiation in app code | INFERRED GlideRequest.java (generated) |
| GlideRequest.<init>(Class,RequestBuilder) | UNREACHABLE | no_trigger_in_app | Generated constructor; no direct instantiation in app code | INFERRED GlideRequest.java (generated) |
| GlideRequest.addListener | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.apply | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.centerInside | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.circleCrop | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.decode | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.disallowHardwareConfig | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.dontAnimate | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.dontTransform | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.downsample | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.encodeFormat | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.encodeQuality | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.error(int) | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.error(Drawable) | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.error(RequestBuilder) | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.fallback(int) | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.fallback(Drawable) | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.format | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.frame | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.getDownloadOnlyRequest | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.listener | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.load(Bitmap) | UNREACHABLE | no_trigger_in_app | Generated load() overload; app only calls load(String) and load(Integer) | INFERRED GlideRequest.java (generated) |
| GlideRequest.load(Drawable) | UNREACHABLE | no_trigger_in_app | Generated load() overload; app only calls load(String) and load(Integer) | INFERRED GlideRequest.java (generated) |
| GlideRequest.load(Uri) | UNREACHABLE | no_trigger_in_app | Generated load() overload; app only calls load(String) and load(Integer) | INFERRED GlideRequest.java (generated) |
| GlideRequest.load(File) | UNREACHABLE | no_trigger_in_app | Generated load() overload; app only calls load(String) and load(Integer) | INFERRED GlideRequest.java (generated) |
| GlideRequest.load(Object) | UNREACHABLE | no_trigger_in_app | Generated load() overload; app only calls load(String) and load(Integer) | INFERRED GlideRequest.java (generated) |
| GlideRequest.load(URL) | UNREACHABLE | no_trigger_in_app | Generated load() overload; app only calls load(String) and load(Integer) | INFERRED GlideRequest.java (generated) |
| GlideRequest.load(byte[]) | UNREACHABLE | no_trigger_in_app | Generated load() overload; app only calls load(String) and load(Integer) | INFERRED GlideRequest.java (generated) |
| GlideRequest.onlyRetrieveFromCache | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.optionalCenterCrop | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.optionalCenterInside | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.optionalCircleCrop | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.optionalFitCenter | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.optionalTransform(Transformation) | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.optionalTransform(Class,Transformation) | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.override(int) | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.override(int,int) | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.placeholder(int) | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.placeholder(Drawable) | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.priority | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.set | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.signature | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.sizeMultiplier | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.skipMemoryCache | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.theme | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.thumbnail(float) | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.thumbnail(RequestBuilder) | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.thumbnail(RequestBuilder[]) | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.timeout | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.transform(Transformation) | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.transform(Class,Transformation) | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.transform(Transformation[]) | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.transforms | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.transition | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called on GlideRequest objects in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.useAnimationPool | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |
| GlideRequest.useUnlimitedSourceGeneratorsPool | UNREACHABLE | no_trigger_in_app | Generated fluent API method never called in app | INFERRED GlideRequest.java (generated) |

STATUS: DONE 23:25
