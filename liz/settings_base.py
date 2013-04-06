# Django settings for project project.

### All sites share this exception block
# Import local settings
try:
    from settings_local import *
except Exception as e:
    raise SystemExit("Could not read settings: " + e.message)

SITE_ID = 4

ALLOWED_HOSTS = (
    'www.lizcheney.com',
    'lizcheney.com',
)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
if not DEBUG:
    MEDIA_URL = '//media.lizcheney.com/'
else:
    MEDIA_URL = '/media/'

TEMPLATE_CONTEXT_PROCESSORS += (
    'zinnia.context_processors.version',    # optional
)

INSTALLED_APPS += (
    'maintenance.heartbeat',
    'contact',
    'tagging',
    'mptt',
    'zinnia',
    'disqus',
)

# Zinnia
ZINNIA_MARKUP_LANGUAGE = 'markdown'

from zinnia.xmlrpc import ZINNIA_XMLRPC_METHODS
XMLRPC_METHODS = ZINNIA_XMLRPC_METHODS + [
    ('zinnia.xmlrpc.metaweblog.new_category',
     'mt.addCategory'),
    ('zinnia.xmlrpc.metaweblog.get_categories',
     'mt.getCategoryList'),
    ('den.xmlrpc.mt.get_post_categories',
     'mt.getPostCategories'),
    ('den.xmlrpc.mt.set_post_categories',
     'mt.setPostCategories'),
    ('den.xmlrpc.mt.new_post',
     'metaWeblog.newPost'),
    ('den.xmlrpc.mt.edit_post',
     'metaWeblog.editPost'),
    ('den.xmlrpc.mt.get_post',
     'metaWeblog.getPost'),
    ('den.xmlrpc.mt.get_recent_posts',
     'metaWeblog.getRecentPosts'),
]

# Pagination
# http://packages.python.org/linaro-django-pagination/usage.html#how-to-use-linaro-django-pagination
PAGINATION_INVALID_PAGE_RAISES_404 = True
# PAGINATION_PREVIOUS_LINK_DECORATOR = '&laquo;'
# PAGINATION_NEXT_LINK_DECORATOR = '&raquo;'
PAGINATION_CLEAN_URL = False

# Haystack
#HAYSTACK_CONNECTIONS = {
#        'default': {
#            'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
#            'PATH': os.path.join(PROJECT_ROOT, 'whoosh_index'),
#            # 'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
#            'TIMEOUT': 60 * 5,
#            'INCLUDE_SPELLING': True,
#            'BATCH_SIZE': 100,
#            },
#        }

#HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
##HAYSTACK_SEARCH_RESULTS_PER_PAGE = 5
##HAYSTACK_ROUTERS = ['core.routers.SiteRouter']


#MEDIA_CDN_DOMAIN = 'http://cdn.merenbach.com/'
#DJANGO_STATIC_FILE_PROXY = 'den.cdn.cdn_origin_pull_file_proxy'

#import logging
#logging.basicConfig(level=logging.DEBUG)

# Pagination
# http://packages.python.org/linaro-django-pagination/usage.html#how-to-use-linaro-django-pagination
#PAGINATION_INVALID_PAGE_RAISES_404 = True
## PAGINATION_PREVIOUS_LINK_DECORATOR = '&laquo;'
## PAGINATION_NEXT_LINK_DECORATOR = '&raquo;'
#PAGINATION_CLEAN_URL = False

# import warnings
# warnings.filterwarnings(
#         'error', r"DateTimeField received a naive datetime",
#         RuntimeWarning, r'django\.db\.models\.fields')

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
