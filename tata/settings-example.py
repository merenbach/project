# Django settings for project project.

# import central settings
from settings_base import *

# for url/path manipulation
from os.path import join

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/srv/www/example.com/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = join(MEDIA_ROOT, 'static')

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# Disqus
DISQUS_API_KEY = ''
DISQUS_WEBSITE_SHORTNAME = 'merenbach'

# Akismet
AKISMET_API_KEY = ''
AKISMET_BLOG_URL = 'http://www.merenbach.com'

# Clicky
CLICKY_SITE_ID = ''
# CLICKY_RENDER_NON_JS_CODE = False

# Google Analytics
GOOGLE_ANALYTICS_PROPERTY_ID = ''
# GOOGLE_ANALYTICS_SITE_SPEED = False

# Set your DSN value
RAVEN_CONFIG = {
    'dsn': 'https://public:secret@sentry.merenbach.com/#',
}

# caching
#CACHES = {
#        'default': {
#            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#            'LOCATION': '127.0.0.1:11211',
#            #'LOCATION': 'unix:/tmp/memcached.sock',
#            }
#        }

