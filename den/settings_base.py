# Django settings for project project.

# Try to import common settings
try:
    from common.settings_base import *
except:
    raise SystemExit("Error reading common settings!")

import os
import sys

# get the settings path
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
PROJECT_PATH = os.path.abspath(PROJECT_ROOT)

if PROJECT_PATH not in sys.path:
    sys.path.insert(0, PROJECT_PATH)

# add to default paths
#paths = (
#   PROJECT_PATH,
#        #os.path.realpath(os.path.dirname(PROJECT_PATH)),
#        )
#
#for path in paths:
#    if path not in sys_path:
#        sys_path.insert(0, path)

SITE_ID = 1

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS += (
    'dajaxice.finders.DajaxiceFinder',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'pagination.middleware.PaginationMiddleware',
    'linaro_django_pagination.middleware.PaginationMiddleware',
    'breadcrumbs.middleware.BreadcrumbsMiddleware',
    #'breadcrumbs.middleware.FlatpageFallbackMiddleware',
    'maintenance.middleware.MaintenanceMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

# Set a caching key prefix to avoid collisions
CACHE_MIDDLEWARE_KEY_PREFIX = 'den'

ROOT_URLCONF = 'den.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'den.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'zinnia.context_processors.version',    # optional
)

INSTALLED_APPS += (
    'den', # custom additions and utilities
    'maintenance.heartbeat',
    'contact',
    'tagging',
    'mptt',
    'zinnia',
    #'disqus',
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
)

# Breadcrumbs
BREADCRUMBS_AUTO_HOME = True
#BREADCRUMBS_HOME_TITLE = 'Home'

## Haystack
#HAYSTACK_CONNECTIONS = {
#        'default': {
#            'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
#            'PATH': os.path.join(PROJECT_ROOT, 'whoosh_index'),
#            'PATH': os.path.join(PROJECT_ROOT, 'whoosh_index'),
#            # 'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
#            'TIMEOUT': 60 * 5,
#            'INCLUDE_SPELLING': True,
#            'BATCH_SIZE': 100,
#            },
#        }

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
#HAYSTACK_SEARCH_RESULTS_PER_PAGE = 5
#HAYSTACK_ROUTERS = ['core.routers.SiteRouter']


#MEDIA_CDN_DOMAIN = 'http://cdn.merenbach.com/'
#DJANGO_STATIC_FILE_PROXY = 'den.cdn.cdn_origin_pull_file_proxy'

# Dajax/DajaxIce
DAJAXICE_MEDIA_PREFIX = 'dajaxice'
DAJAXICE_DEBUG = False
DAJAXICE_NOTIFY_EXCEPTIONS = True
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Zinnia
ZINNIA_MARKUP_LANGUAGE = 'markdown'
ZINNIA_WYSIWYG = False

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

# import warnings
# warnings.filterwarnings(
#         'error', r"DateTimeField received a naive datetime",
#         RuntimeWarning, r'django\.db\.models\.fields')
