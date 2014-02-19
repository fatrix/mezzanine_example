import os
import settings
from golive.utils import get_var

DEBUG = True

TIME_ZONE = "Europe/Zurich"
ALLOWED_HOSTS = ['']

# Make these unique, and don't share it with anybody.
SECRET_KEY = get_var('SECRET_KEY')
NEVERCACHE_KEY = get_var('NEVERCACHE_KEY')

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

# _site app
TEMPLATE_DIRS = (os.path.join(settings.PROJECT_ROOT, "_site/templates"), ) + settings.TEMPLATE_DIRS 
ADDITIONAL_INSTALLED_APPS = ()
ADDITIONAL_INSTALLED_APPS += (u"_site",)

# debug toolbar
settings.MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
settings.INTERNAL_IPS = ['127.0.0.1']

def show_toolbar_for_admin(request):
    if request.user.is_authenticated():
        return request.user.is_staff
    else:
        return False

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'utils.show_toolbar_for_admin'
}

# nose
ADDITIONAL_INSTALLED_APPS += (u"nose",)
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# deploy
ADDITIONAL_INSTALLED_APPS += (u"golive",)
GOLIVE_CLEANUP_RESTORE = ['SELECT * FROM conf_setting;',
                          'UPDATE conf_setting SET value=\'\' WHERE name=\'GOOGLE_ANALYTICS_ID\'',
                          'UPDATE conf_setting SET value=\'\' WHERE name=\'BITLY_ACCESS_TOKEN\'',
                          'UPDATE conf_setting SET value=\'\' WHERE name=\'COMMENTS_DISQUS_API_PUBLIC_KEY\'',
                          'UPDATE conf_setting SET value=\'\' WHERE name=\'COMMENTS_DISQUS_API_SECRET_KEY\'',
                          'UPDATE conf_setting SET value=\'\' WHERE name=\'COMMENTS_DISQUS_SHORTNAME\'',
                          'UPDATE conf_setting SET value=\'\' WHERE name=\'COMMENTS_DISQUS_SHORTNAME\'',
                          'UPDATE conf_setting SET value=\'\' WHERE name=\'TWITTER_CONSUMER_SECRET\'',
                          'UPDATE conf_setting SET value=\'\' WHERE name=\'TWITTER_CONSUMER_KEY\'',
                          'UPDATE conf_setting SET value=\'\' WHERE name=\'TWITTER_ACCESS_TOKEN_KEY\'',
                          'UPDATE conf_setting SET value=\'\' WHERE name=\'TWITTER_ACCESS_TOKEN_SECRET\'',
                          'SELECT slug, short_url FROM blog_blogpost;'
                          'UPDATE blog_blogpost SET short_url=NULL;',

]

# logging
settings.MIDDLEWARE_CLASSES += ('xcore.core.middleware.LoggingMiddleware',)

# mail
EMAIL_USE_TLS = True
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_HOST_USER = get_var('AMAZON_SES_USER')
EMAIL_HOST_PASSWORD = get_var('AMAZON_SES_KEY')
EMAIL_PORT = 587

# caches
CACHES = {
    "default": {
        "BACKEND": "redis_cache.cache.RedisCache",
        "LOCATION": "127.0.0.1:6379:1",
        "OPTIONS": {
            "CLIENT_CLASS": "redis_cache.client.DefaultClient",
        }
    }
}

# S3 Storage
AWS_ACCESS_KEY_ID = get_var('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY= get_var('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = get_var('AWS_STORAGE_BUCKET_NAME')

DEFAULT_FILE_STORAGE = 'utils.FixedS3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_PRELOAD_METADATA = True
ADDITIONAL_INSTALLED_APPS += (u"storages", )

# Add collectfast
AWS_PRELOAD_METADATA = True
ADDITIONAL_INSTALLED_APPS += (u"collectfast", u"debug_toolbar", )
INSTALLED_APPS = settings.INSTALLED_APPS + ADDITIONAL_INSTALLED_APPS

# s3 host needed for static_proxy patch
S3_HOST = AWS_STORAGE_BUCKET_NAME + '.' + get_var('AWS_S3_HOST')
# mezzanine_tags stores a thumbnail only on s3 when MEDIA_URL includes ://
STATIC_URL = 'https://' + S3_HOST + '/'
MEDIA_URL = STATIC_URL+"media/"
# fix signature error and 403 from S3
AWS_QUERYSTRING_AUTH = False
# modify in templates/filebrowser/include/filelisting.html from MEDIA_URL to STATIC_URL for 
# the thumbnails

# import _site settings
from _site.settings import *