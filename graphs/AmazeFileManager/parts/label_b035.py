# ---- Batch 035: GlideOptions (generated Glide library class)
# Helper label part for batch_035.txt
# Date: 2026-10-27
# Methods: 73 (4 REACHABLE via app call sites, 1 unreachable constructor, 68 unreachable fluent API methods)

# REACHABLE GlideOptions methods (called via GlideApp fluent API)

e('RecyclerPreloadModelProvider.<init>', 'GlideOptions.centerCrop', 'CALL',
  'RecyclerPreloadModelProvider constructor creates GlideRequest with centerCrop()',
  evidence='SRC RecyclerPreloadModelProvider.java:30: request = GlideApp.with(fragment).asDrawable().centerCrop();')

e('AppsAdapterPreloadModel.<init>', 'GlideOptions.fitCenter', 'CALL',
  'AppsAdapterPreloadModel constructor creates GlideRequest with fitCenter()',
  evidence='SRC AppsAdapterPreloadModel.java:28: request = GlideApp.with(f).asDrawable().fitCenter();')

e('AppsAdapterPreloadModel.getPreloadRequestBuilder', 'GlideOptions.clone', 'CALL',
  'AppsAdapterPreloadModel clones the request for each preload item',
  evidence='SRC AppsAdapterPreloadModel.java:45: return request.clone().load(item);')

e('RecyclerPreloadModelProvider.getPreloadRequestBuilder', 'GlideOptions.diskCacheStrategy', 'CALL',
  'RecyclerPreloadModelProvider sets disk cache strategy for cloud images',
  evidence='SRC RecyclerPreloadModelProvider.java:48: requestBuilder = request.load(iconData.path).diskCacheStrategy(DiskCacheStrategy.NONE);')

# UNREACHABLE methods: GlideOptions is a generated Glide fluent API class.
# Most methods are never invoked by the app at GlideApp call sites.

UNREACHABLE['GlideOptions.<init>'] = (
    'no_trigger_in_app',
    'GlideOptions is a generated Glide library class providing fluent API methods. No direct instantiation found in app source. grep -rn "new GlideOptions" returns empty.',
    'INFERRED GlideOptions (generated class, no source in app)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.apply'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.autoClone'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.bitmapTransform'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.centerCropTransform'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.centerInside'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.centerInsideTransform'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.circleCrop'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.circleCropTransform'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.decode'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.decodeTypeOf'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.disallowHardwareConfig'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.diskCacheStrategyOf'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.dontAnimate'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.dontTransform'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.downsample'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.downsampleOf'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.encodeFormat'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.encodeFormatOf'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.encodeQuality'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.encodeQualityOf'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.error(I)'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method. Overload: error(int)',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.error(Drawable)'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method. Overload: error(Drawable)',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.errorOf(I)'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method. Overload: errorOf(int)',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.errorOf(Drawable)'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method. Overload: errorOf(Drawable)',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.fallback(I)'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method. Overload: fallback(int)',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.fallback(Drawable)'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method. Overload: fallback(Drawable)',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.fitCenterTransform'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.format'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.formatOf'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.frame'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.frameOf'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.lock'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.noAnimation'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.noTransformation'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.onlyRetrieveFromCache'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.option'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.optionalCenterCrop'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.optionalCenterInside'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.optionalCircleCrop'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.optionalFitCenter'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.optionalTransform(Transformation)'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method. Overload: optionalTransform(Transformation)',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.optionalTransform(Class,Transformation)'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method. Overload: optionalTransform(Class, Transformation)',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.override(I)'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method. Overload: override(int)',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.override(II)'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method. Overload: override(int, int)',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.overrideOf(I)'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method. Overload: overrideOf(int)',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.overrideOf(II)'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method. Overload: overrideOf(int, int)',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.placeholder(I)'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method. Overload: placeholder(int)',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.placeholder(Drawable)'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method. Overload: placeholder(Drawable)',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.placeholderOf(I)'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method. Overload: placeholderOf(int)',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.placeholderOf(Drawable)'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method. Overload: placeholderOf(Drawable)',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.priority'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.priorityOf'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.set'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.signature'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.signatureOf'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.sizeMultiplier'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.sizeMultiplierOf'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.skipMemoryCache'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.skipMemoryCacheOf'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.theme'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.timeout'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.timeoutOf'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.transform(Transformation)'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method. Overload: transform(Transformation)',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.transform(Class,Transformation)'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method. Overload: transform(Class, Transformation)',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.transform(Transformation[])'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method. Overload: transform(Transformation[])',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.transforms'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.useAnimationPool'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)

UNREACHABLE['GlideOptions.useUnlimitedSourceGeneratorsPool'] = (
    'no_trigger_in_app',
    'Generated Glide fluent API method never called by app at GlideApp call sites. grep in GlideApp usage files returns no matches for this method.',
    'INFERRED GlideOptions (generated class)',
    'INFERRED'
)
