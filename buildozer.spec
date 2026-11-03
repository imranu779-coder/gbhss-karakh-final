[app]
title = GBHSS KARAKH
package.name = gbhsskarakhfinal
package.domain = com.gbhss.karakh
source.dir = .
source.include_exts = py,json
version = 1.0
requirements = python3,kivy==2.2.0
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreements = True