[app]
title = GBHSS KARAKH
package.name = gbhsskarakhfinal
package.domain = com.gbhss.karakh
source.dir = .
source.include_exts = py,json
version = 1.0
requirements = python3,kivy==2.2.0
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreements = True
android.archs = arm64-v8a, armeabi-v7a