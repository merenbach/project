# Django settings for project project.

# Try to import common settings
try:
    from common.settings_base import *
except:
    raise SystemExit("Error reading common settings!")

SITE_ID = 2

ALLOWED_HOSTS = (
    'www.theromantics.net',
    'www.theromantics.dev',
    'theromantics.net',
    'theromantics.dev',
)

# We want to use SSL but NGINX proxies to Gunicorn
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_SCHEME', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# Set a caching key prefix to avoid collisions
CACHE_MIDDLEWARE_KEY_PREFIX = 'romantics'

ROOT_URLCONF = 'romantics.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'romantics.wsgi.application'

INSTALLED_APPS += (
    'romantics', # custom additions and utilities
    'maintenance.heartbeat',
    'contact',
    'rsvp',
)

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'romantics', 'static'),
) + STATICFILES_DIRS

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'romantics', 'templates'),
) + TEMPLATE_DIRS

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

