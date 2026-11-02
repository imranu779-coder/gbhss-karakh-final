[app]
title = GBHSS KARKH
package.name = gbhsskarkh
package.domain = com.gbhss.karkh
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==1.1.1
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

# (str) Supported orientation (one of sensort, sensor, portrait, landscape)
# by default, the application will be full screen

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private-data-dir ?
# (to be used with the new Android storage system)
android.private_storage = True

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements PythonActivity
# use that one to uncomment
# android.entrypoint_class = org.kivy.android.PythonActivity
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreements = True
android.build_tools_version = 33.0.2