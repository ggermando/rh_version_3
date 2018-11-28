import dj_database_url

from rh_version_3.settings import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATES_DEBUG = False

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['spx-rh.herokuapp.com']

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
