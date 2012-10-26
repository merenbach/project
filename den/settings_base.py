# Django settings for project project.

import os
import sys

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'den.wsgi.application'

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

PREPEND_WWW = True

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
    'dajaxice.finders.DajaxiceFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'pagination.middleware.PaginationMiddleware',
    'linaro_django_pagination.middleware.PaginationMiddleware',
    'breadcrumbs.middleware.BreadcrumbsMiddleware',
    #'breadcrumbs.middleware.FlatpageFallbackMiddleware',
    'maintenance.middleware.MaintenanceMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'den.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'den.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        # 'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.request',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'sekizai.context_processors.sekizai',
        'django.core.context_processors.csrf',
        'zinnia.context_processors.version',    # optional
        'django.contrib.messages.context_processors.messages',
        )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'django.contrib.sitemaps',
    'django.contrib.markup',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'django.contrib.syndication',
    'django.contrib.comments',
    'south',
    'appconf',
    'sekizai',
    'pytz',
    'compressor',
    'tagging',
    'mptt',
    'zinnia',
    'disqus',
    'contact',
    #'pagination',              # pagination (replaced)
    'linaro_django_pagination', # pagination
    'haystack',
    'whoosh',
    'den', # custom additions and utilities
    'maintenance',
    'breadcrumbs',
    'django_xmlrpc',
    'photologue',
    'dajaxice',
    'dajax',
    'software',
    'ciphers',
    'analytical',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Maintenance (currently having no effect)
MAINTENANCE_DISABLE_FOR_SUPERUSER = True

# Breadcrumbs
BREADCRUMBS_AUTO_HOME = True
#BREADCRUMBS_HOME_TITLE = 'Home'

# Django Compressor
# COMPRESS_PRECOMPILERS = (
#     ('text/coffeescript', 'coffee --compile --stdio'),
#     ('text/less', 'lessc {infile} {outfile}'),
#     ('text/x-sass', 'sass {infile} {outfile}'),
#     ('text/x-scss', 'sass --scss {infile} {outfile}'),
# )

# COMPRESS_ENABLED = False
# COMPRESS_OFFLINE = False
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'
#COMPRESS_PARSER = 'compressor.parser.Html5LibParser'
#COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter', 'compressor.filters.cssmin.CSSMinFilter']

# Haystack
HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
            'PATH': os.path.join(PROJECT_ROOT, 'whoosh_index'),
            # 'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
            'TIMEOUT': 60 * 5,
            'INCLUDE_SPELLING': True,
            'BATCH_SIZE': 100,
            },
        }

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
#HAYSTACK_SEARCH_RESULTS_PER_PAGE = 5
#HAYSTACK_ROUTERS = ['core.routers.SiteRouter']


#MEDIA_CDN_DOMAIN = 'http://cdn.merenbach.com/'
#DJANGO_STATIC_FILE_PROXY = 'den.cdn.cdn_origin_pull_file_proxy'

# Contact form
CONTACT_RECIPIENTS = ('andrew@merenbach.com',)

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
    # ('zinnia.xmlrpc.metaweblog.new_category',
    #  'mt.newCategory'),
    ('zinnia.xmlrpc.metaweblog.get_categories',
     'mt.getCategoryList'),
    ('den.xmlrpc.mt.get_post_categories',
     'mt.getPostCategories'),
    ('den.xmlrpc.mt.set_post_categories',
     'mt.setPostCategories'),
    ('den.xmlrpc.mt.new_post',
     'mt.newPost'),
    ('den.xmlrpc.mt.edit_post',
     'mt.editPost'),
    ('den.xmlrpc.mt.get_post',
     'mt.getPost'),
    ('den.xmlrpc.mt.get_recent_posts',
     'mt.getRecentPosts'),
]

# Pagination
# http://packages.python.org/linaro-django-pagination/usage.html#how-to-use-linaro-django-pagination
PAGINATION_INVALID_PAGE_RAISES_404 = True
# PAGINATION_PREVIOUS_LINK_DECORATOR = '&laquo;'
# PAGINATION_NEXT_LINK_DECORATOR = '&raquo;'
PAGINATION_CLEAN_URL = False

# Override zinnia.xmlrpc with our own
# (If this stops working, try moving to top of file)
#import zinnia_xmlrpc
#sys.modules['zinnia.xmlrpc'] = zinnia_xmlrpc
