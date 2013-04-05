# Django settings for project project.

# import central settings
from settings_base import *

# for url/path manipulation
from urlparse import urljoin
from os.path import join

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# For Django social auth
GOOGLE_OAUTH2_CLIENT_ID      = ''
GOOGLE_OAUTH2_CLIENT_SECRET  = ''
GOOGLE_OAUTH2_USE_UNIQUE_USER_ID = True
GOOGLE_DISPLAY_NAME = "My Cool Site"
GOOGLE_WHITE_LISTED_DOMAINS = ('example.com',)
GOOGLE_WHITE_LISTED_EMAILS = tuple(e[1] for e in ADMINS)

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

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
if not DEBUG:
    MEDIA_URL = 'http://cdn.example.com/'
else:
    MEDIA_URL = 'http://media.example.com/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = join(MEDIA_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = urljoin(MEDIA_URL, 'static/')

# deprecated but apparently still necessary for some things
ADMIN_MEDIA_PREFIX = urljoin(STATIC_URL, 'admin/')

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

# my customizations
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'noreply@merenbach.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'noreply@merenbach.com'
SERVER_EMAIL = 'noreply@merenbach.com'

# Set your DSN value
RAVEN_CONFIG = {
    'dsn': 'https://public:secret@sentry.merenbach.com/#',
}

#if DEBUG:
#    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# caching
#CACHES = {
#        'default': {
#            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#            'LOCATION': '127.0.0.1:11211',
#            #'LOCATION': 'unix:/tmp/memcached.sock',
#            }
#        }

# Haystack
HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
            #'PATH': os.path.join(PROJECT_ROOT, 'whoosh_index'),
            'PATH': os.path.join(MEDIA_ROOT, 'whoosh_index'),
            # 'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
            'TIMEOUT': 60 * 5,
            'INCLUDE_SPELLING': True,
            'BATCH_SIZE': 100,
            },
        }
