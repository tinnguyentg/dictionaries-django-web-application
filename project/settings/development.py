from .base import *  # noqa

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-g1z-2$zgr!88=(vk@v%b+^#xvoc@s*9vro*w1tze0!yly2r@_x"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Config django-debug-toolbar
# assert "django.contrib.staticfiles" in INSTALLED_APPS
# assert TEMPLATES[0]["APP_DIRS"]
INSTALLED_APPS += ["debug_toolbar"]  # noqa
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")  # noqa
INTERNAL_IPS = [
    "127.0.0.1",
]
