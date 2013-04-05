# Django settings for project project.

# Try to import common settings
try:
    from common.settings_base import *
except:
    raise SystemExit("Error reading common settings!")

SITE_ID = 4

ALLOWED_HOSTS = (
    'www.lizcheney.com',
    'lizcheney.com',
)

from urlparse import urljoin

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
if not DEBUG:
    MEDIA_URL = '//media.lizcheney.com/'
else:
    MEDIA_URL = '/media/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = urljoin(MEDIA_URL, 'static/')

# Set a caching key prefix to avoid collisions
CACHE_MIDDLEWARE_KEY_PREFIX = 'liz'

ROOT_URLCONF = 'liz.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'liz.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS += (
    'zinnia.context_processors.version',    # optional
)

INSTALLED_APPS += (
    'liz', # custom additions and utilities
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

