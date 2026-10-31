# ---- Helper batch_036 label part (2025-01-XX)
# GlideRequest class - Generated Glide library class (fluent API)
# Most methods are UNREACHABLE (generated variants never called by app)
# Only methods explicitly invoked at GlideRequest call sites are REACHABLE

# REACHABLE GlideRequest methods (confirmed_by=INFERRED for library code)

# centerCrop: called at RecyclerPreloadModelProvider.java:30
e('RecyclerPreloadModelProvider.<init>', 'GlideRequest.centerCrop', 'CALL', 
  'RecyclerPreloadModelProvider constructor calls GlideApp.with(fragment).asDrawable().centerCrop() to initialize request field',
  evidence='INFERRED RecyclerPreloadModelProvider.java:30: request = GlideApp.with(fragment).asDrawable().centerCrop()')

# fitCenter: called at AppsAdapterPreloadModel.java:28  
e('AppsAdapterPreloadModel.<init>', 'GlideRequest.fitCenter', 'CALL',
  'AppsAdapterPreloadModel constructor calls GlideApp.with(f).asDrawable().fitCenter() to initialize request field',
  evidence='INFERRED AppsAdapterPreloadModel.java:28: request = GlideApp.with(f).asDrawable().fitCenter()')

# clone: called at AppsAdapterPreloadModel.java:45
e('AppsAdapterPreloadModel.getPreloadRequestBuilder', 'GlideRequest.clone', 'CALL',
  'getPreloadRequestBuilder calls request.clone().load(item) where request is GlideRequest<Drawable>',
  evidence='INFERRED AppsAdapterPreloadModel.java:45: return request.clone().load(item)')

# diskCacheStrategy: called at RecyclerPreloadModelProvider.java:48
e('RecyclerPreloadModelProvider.getPreloadRequestBuilder', 'GlideRequest.diskCacheStrategy', 'CALL',
  'getPreloadRequestBuilder calls request.load(iconData.path).diskCacheStrategy(DiskCacheStrategy.NONE)',
  evidence='INFERRED RecyclerPreloadModelProvider.java:48: requestBuilder = request.load(iconData.path).diskCacheStrategy(DiskCacheStrategy.NONE)')

# load(String): called at RecyclerPreloadModelProvider.java:46,48 and AppsAdapterPreloadModel.java:45,49
e('RecyclerPreloadModelProvider.getPreloadRequestBuilder', 'GlideRequest.load(Ljava/lang/String;)Lcom/amaze/filemanager/GlideRequest;', 'CALL',
  'getPreloadRequestBuilder calls request.load(iconData.path) where path is String',
  evidence='INFERRED RecyclerPreloadModelProvider.java:46,48: request.load(iconData.path); path field is String per IconDataParcelable.java')

e('AppsAdapterPreloadModel.getPreloadRequestBuilder', 'GlideRequest.load(Ljava/lang/String;)Lcom/amaze/filemanager/GlideRequest;', 'CALL',
  'getPreloadRequestBuilder calls request.clone().load(item) where item param is String',
  evidence='INFERRED AppsAdapterPreloadModel.java:45: return request.clone().load(item); method signature shows String param')

e('AppsAdapterPreloadModel.loadApkImage', 'GlideRequest.load(Ljava/lang/String;)Lcom/amaze/filemanager/GlideRequest;', 'CALL',
  'loadApkImage calls request.load(item).into(v) where item param is String',
  evidence='INFERRED AppsAdapterPreloadModel.java:49: request.load(item).into(v); method signature shows String param')

# load(Integer): called at RecyclerPreloadModelProvider.java:50
e('RecyclerPreloadModelProvider.getPreloadRequestBuilder', 'GlideRequest.load(Ljava/lang/Integer;)Lcom/amaze/filemanager/GlideRequest;', 'CALL',
  'getPreloadRequestBuilder calls request.load(iconData.image) where image is @DrawableRes int',
  evidence='INFERRED RecyclerPreloadModelProvider.java:50: requestBuilder = request.load(iconData.image); image field is @DrawableRes int per IconDataParcelable.java')

# UNREACHABLE methods - all other GlideRequest methods
# These are generated API methods never invoked by the app
UNREACHABLE_B036 = {
    'GlideRequest.<init>(Lcom/bumptech/glide/Glide;Lcom/bumptech/glide/RequestManager;Ljava/lang/Class;Landroid/content/Context;)V': 
        ('no_trigger_in_app', 'Generated constructor; no direct instantiation in app code, grep shows no "new GlideRequest" in app source', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.<init>(Ljava/lang/Class;Lcom/bumptech/glide/RequestBuilder;)V': 
        ('no_trigger_in_app', 'Generated constructor; no direct instantiation in app code, grep shows no "new GlideRequest" in app source', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.addListener(Lcom/bumptech/glide/request/RequestListener;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.addListener(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.apply(Lcom/bumptech/glide/request/BaseRequestOptions;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.apply(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.centerInside()Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.centerInside(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.circleCrop()Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.circleCrop(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.decode(Ljava/lang/Class;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.decode(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.disallowHardwareConfig()Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.disallowHardwareConfig(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.dontAnimate()Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.dontAnimate(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.dontTransform()Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.dontTransform(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.downsample(Lcom/bumptech/glide/load/resource/bitmap/DownsampleStrategy;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.downsample(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.encodeFormat(Landroid/graphics/Bitmap$CompressFormat;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.encodeFormat(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.encodeQuality(I)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.encodeQuality(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.error(I)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.error(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.error(Landroid/graphics/drawable/Drawable;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.error(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.error(Lcom/bumptech/glide/RequestBuilder;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.error(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.fallback(I)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.fallback(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.fallback(Landroid/graphics/drawable/Drawable;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.fallback(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.format(Lcom/bumptech/glide/load/DecodeFormat;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.format(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.frame(J)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.frame(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.getDownloadOnlyRequest()Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.getDownloadOnlyRequest(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.listener(Lcom/bumptech/glide/request/RequestListener;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.listener(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.load(Landroid/graphics/Bitmap;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated load() overload for Bitmap parameter; app only calls load(String) and load(Integer) on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.load(Landroid/graphics/drawable/Drawable;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated load() overload for Drawable parameter; app only calls load(String) and load(Integer) on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.load(Landroid/net/Uri;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated load() overload for Uri parameter; app only calls load(String) and load(Integer) on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.load(Ljava/io/File;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated load() overload for File parameter; app only calls load(String) and load(Integer) on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.load(Ljava/lang/Object;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated load() overload for Object parameter; app only calls load(String) and load(Integer) on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.load(Ljava/net/URL;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated load() overload for URL parameter; app only calls load(String) and load(Integer) on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.load([B)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated load() overload for byte[] parameter; app only calls load(String) and load(Integer) on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.onlyRetrieveFromCache(Z)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.onlyRetrieveFromCache(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.optionalCenterCrop()Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.optionalCenterCrop(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.optionalCenterInside()Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.optionalCenterInside(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.optionalCircleCrop()Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.optionalCircleCrop(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.optionalFitCenter()Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.optionalFitCenter(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.optionalTransform(Lcom/bumptech/glide/load/Transformation;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.optionalTransform(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.optionalTransform(Ljava/lang/Class;Lcom/bumptech/glide/load/Transformation;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.optionalTransform(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.override(I)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.override(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.override(II)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.override(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.placeholder(I)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.placeholder(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.placeholder(Landroid/graphics/drawable/Drawable;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.placeholder(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.priority(Lcom/bumptech/glide/Priority;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.priority(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.set(Lcom/bumptech/glide/load/Option;Ljava/lang/Object;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.set(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.signature(Lcom/bumptech/glide/load/Key;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.signature(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.sizeMultiplier(F)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.sizeMultiplier(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.skipMemoryCache(Z)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.skipMemoryCache(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.theme(Landroid/content/res/Resources$Theme;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.theme(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.thumbnail(F)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.thumbnail(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.thumbnail(Lcom/bumptech/glide/RequestBuilder;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.thumbnail(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.thumbnail([Lcom/bumptech/glide/RequestBuilder;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.thumbnail(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.timeout(I)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.timeout(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.transform(Lcom/bumptech/glide/load/Transformation;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.transform(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.transform(Ljava/lang/Class;Lcom/bumptech/glide/load/Transformation;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.transform(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.transform([Lcom/bumptech/glide/load/Transformation;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.transform(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.transforms([Lcom/bumptech/glide/load/Transformation;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.transforms(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.transition(Lcom/bumptech/glide/TransitionOptions;)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.transition(" in app source shows no calls on GlideRequest objects', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.useAnimationPool(Z)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.useAnimationPool(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
    
    'GlideRequest.useUnlimitedSourceGeneratorsPool(Z)Lcom/amaze/filemanager/GlideRequest;': 
        ('no_trigger_in_app', 'Generated fluent API method; grep -rn "\\.useUnlimitedSourceGeneratorsPool(" in app source shows no matches', 'INFERRED GlideRequest.java (generated)', 'INFERRED'),
}
