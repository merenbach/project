# Django settings for project project.

### All sites share this exception block
# Import local settings
try:
    from settings_local import *
except Exception as e:
    raise SystemExit("Could not read settings: " + e.message)

SITE_ID = 1

ALLOWED_HOSTS = (
    'www.merenbach.com',
    'merenbach.com',
)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
if not DEBUG:
    MEDIA_URL = '//media.merenbach.com/'
else:
    MEDIA_URL = '/media/'

# We want to use SSL but NGINX proxies to Gunicorn
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_SCHEME', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# Haystack
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(MEDIA_ROOT, os.pardir, 'search', 'whoosh_index'),
        'TIMEOUT': 60 * 5,
        'INCLUDE_SPELLING': True,
        'BATCH_SIZE': 100,
        },
    }

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS += (
    'dajaxice.finders.DajaxiceFinder',
)

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
    #'pagination',              # pagination (replaced)
    'linaro_django_pagination', # pagination
    'haystack',
    'whoosh',
    'breadcrumbs',
    'django_xmlrpc',
    'photologue',
    'dajaxice',
    'dajax',
    'software',
    'ciphers',
    'social_auth',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
)

# For django-social-auth
# Keys are specified locally
SOCIAL_AUTH_FORCE_POST_DISCONNECT = True
SOCIAL_AUTH_CREATE_USERS = False
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
# SOCIAL_AUTH_SESSION_EXPIRATION = False
SOCIAL_AUTH_PROTECTED_USER_FIELDS = ('email',)
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/admin/'

# Breadcrumbs
BREADCRUMBS_AUTO_HOME = True
# BREADCRUMBS_HOME_TITLE = 'Home'

# HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 5

# Dajax/DajaxIce
DAJAXICE_MEDIA_PREFIX = 'dajaxice'
DAJAXICE_DEBUG = DEBUG
DAJAXICE_NOTIFY_EXCEPTIONS = True

# Zinnia
ZINNIA_MARKUP_LANGUAGE = 'markdown'
ZINNIA_MARKDOWN_EXTENSIONS = 'smartypants'
if not DEBUG:
    ZINNIA_PROTOCOL = 'https'
else:
    ZINNIA_PROTOCOL = 'http'    
DATE_FORMAT = 'Y.m.d'
YEAR_MONTH_FORMAT = 'Y.m'
#DATETIME_FORMAT = 'c'

# Override ZINNIA XMLRPC methods
from core.xmlrpc.wp import WP_ZINNIA_XMLRPC_METHODS as XMLRPC_METHODS
from zinnia.xmlrpc import ZINNIA_XMLRPC_PINGBACK
XMLRPC_METHODS += ZINNIA_XMLRPC_PINGBACK
XMLRPC_METHODS += (
    # Blogger
    ('zinnia.xmlrpc.metaweblog.get_users_blogs',
     'blogger.getUsersBlogs'),
    ('zinnia.xmlrpc.metaweblog.get_user_info',
     'blogger.getUserInfo'),
    ('zinnia.xmlrpc.metaweblog.delete_post',
     'blogger.deletePost'),
    # WordPress
    ('zinnia.xmlrpc.metaweblog.get_authors',
     'wp.getAuthors'),
    # MetaWeblog
    # ('zinnia.xmlrpc.metaweblog.get_categories',
    #  'metaWeblog.getCategories'),
    # ('zinnia.xmlrpc.metaweblog.new_category',
    #  'wp.newCategory'),
    # ('zinnia.xmlrpc.metaweblog.get_recent_posts',
    #  'metaWeblog.getRecentPosts'),
    # ('zinnia.xmlrpc.metaweblog.get_post',
    #  'metaWeblog.getPost'),
    # ('zinnia.xmlrpc.metaweblog.new_post',
    #  'metaWeblog.newPost'),
    # ('zinnia.xmlrpc.metaweblog.edit_post',
    #  'metaWeblog.editPost'),
    ('zinnia.xmlrpc.metaweblog.new_media_object',
     'metaWeblog.newMediaObject'),
    # Overrides
    ('zinnia.xmlrpc.metaweblog.get_categories',
     'mt.getCategoryList'),
    ('core.xmlrpc.wp.categories.new_category',
     'mt.addCategory'),
    ('core.xmlrpc.mt.get_recent_posts',
     'metaWeblog.getRecentPosts'),
    ('core.xmlrpc.mt.get_post',
     'metaWeblog.getPost'),
    ('core.xmlrpc.mt.new_post',
     'metaWeblog.newPost'),
    ('core.xmlrpc.mt.edit_post',
     'metaWeblog.editPost'),
    # Additions
    ('core.xmlrpc.mt.get_post_categories',
     'mt.getPostCategories'),
    ('core.xmlrpc.mt.set_post_categories',
     'mt.setPostCategories'),
 )

# Pagination
# http://packages.python.org/linaro-django-pagination/usage.html#how-to-use-linaro-django-pagination
PAGINATION_INVALID_PAGE_RAISES_404 = True
PAGINATION_CLEAN_URL = False

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
