# Django settings for project project.

# import central settings
from settings_base import *

# for url/path manipulation
from urlparse import urljoin
from os.path import join

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Andrew Merenbach', 'andrew@merenbach.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'merenbach_django',                      # Or path to database file if using sqlite3.
        'USER': 'merenbach_django',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '/var/run/postgresql',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = '/srv/www/example.com/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
if not DEBUG:
    MEDIA_URL = 'http://cdn.example.com/'
else:
    MEDIA_URL = 'http://media.example.com/'

# Absolute path to the directory static files should be collected to.
STATIC_ROOT = join(MEDIA_ROOT, 'static')

# URL prefix for static files.
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
#CLICKY_RENDER_NON_JS_CODE = False

# my customizations
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'noreply@merenbach.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'noreply@merenbach.com'
SERVER_EMAIL = 'noreply@merenbach.com'

# caching
#CACHES = {
#        'default': {
#            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#            'LOCATION': '127.0.0.1:11211',
#            #'LOCATION': 'unix:/var/run/memcached/memcached.pid',
#            }
#        }

