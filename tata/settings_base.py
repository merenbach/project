# Django settings for project project.

### All sites share this exception block
# Import local settings
try:
    from settings_local import *
except Exception as e:
    raise SystemExit("Could not read settings: " + e.message)

SITE_ID = 3

ALLOWED_HOSTS = (
    'www.thetata.net',
    'thetata.net',
)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
if not DEBUG:
    MEDIA_URL = '//media.thetata.net/'
else:
    MEDIA_URL = '/media/'

### The following block is common to all projects.
## It should be abstracted out at some point

import os, sys

# This directory holds the settings
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

# The path to the enclosing folder
PROJECT_ROOT = os.path.dirname(SITE_ROOT)

# This is the directory name (e.g., 'den' or 'tata')
SITE_NAME = os.path.basename(SITE_ROOT)

# Ensure that this module and the project root are in the Python path
for p in (SITE_ROOT, PROJECT_ROOT):
    if p not in sys.path:
        sys.path.insert(0, p)

from urlparse import urljoin
from os.path import join

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = urljoin(MEDIA_URL, 'static/')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = join(MEDIA_ROOT, 'static/')

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'static'),
    os.path.join(os.path.dirname(SITE_ROOT), 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
    os.path.join(os.path.dirname(SITE_ROOT), 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# Set a caching key prefix to avoid collisions
CACHE_MIDDLEWARE_KEY_PREFIX = SITE_NAME
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

ROOT_URLCONF = SITE_NAME + '.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = SITE_NAME + '.wsgi.application'

# Caching
if not DEBUG:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'KEY_PREFIX': SITE_NAME,
            'LOCATION': 'unix:/tmp/memcached.sock',
            }
        }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
            }
        }
    # Don't send email in DEBUG mode, either
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Custom additions and utilities
# This may not be necessary in the future
INSTALLED_APPS += (
    SITE_NAME,
)

### End common block
