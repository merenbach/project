# Django settings for project project.

import os
from sys import path as sys_path
from urlparse import urljoin

# add to default paths
paths = (
        '/srv/www/merenbach.com/django',
        '/srv/www/merenbach.com/django/den',
        #'/srv/www/merenbach.com/django/lib/python2.7',
        )

for path in paths:
    if path not in sys_path:
        sys_path.insert(0, path)

# get the settinsg path
from django.utils import importlib
_SETTINGS_MODULE = importlib.import_module(os.environ.get('DJANGO_SETTINGS_MODULE'))

PROJECT_ROOT = os.path.realpath(os.path.dirname(_SETTINGS_MODULE.__file__))
PROJECT_PATH = os.path.abspath(PROJECT_ROOT)

if PROJECT_PATH not in sys_path:
    sys_path.insert(0, PROJECT_PATH)

# for core project files
CORE_PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
CORE_PROJECT_PATH = os.path.abspath(CORE_PROJECT_ROOT)

if CORE_PROJECT_PATH not in sys_path:
    sys_path.insert(0, CORE_PROJECT_PATH)

#OVERLOAD_SITE = os.environ.get('OVERLOAD_SITE')
#OVERLOAD_SITE_MODULE = "websites.{}".format(OVERLOAD_SITE)
#exec ("from {}.settings import *".format(OVERLOAD_SITE_MODULE))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

#for the contact form
CONTACT_RECIPIENTS = tuple()

#if SITE_CONTACT_RECIPIENTS:
#    CONTACT_RECIPIENTS += SITE_CONTACT_RECIPIENTS

PREPEND_WWW = True

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

#SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

## Absolute filesystem path to the directory that will hold user-uploaded files.
## Example: "/home/media/media.lawrence.com/media/"
#MEDIA_ROOT = '/home/merenbach/webapps/media/project/'

## URL that handles the media served from MEDIA_ROOT. Make sure to use a
## trailing slash.
## Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
#MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = '/home/merenbach/webapps/media/project/static/'
#STATIC_ROOT = os.path.join(MEDIA_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
#STATIC_URL = '/media/static/'
#STATIC_URL = urljoin(MEDIA_URL, 'static/')

#ADMIN_MEDIA_PREFIX = urljoin(STATIC_URL, 'admin/')

# Additional locations of static files
STATICFILES_DIRS = (
    #os.path.join(PROJECT_PATH, 'websites', OVERLOAD_SITE, 'static'),
    os.path.join(CORE_PROJECT_PATH, 'static'),
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
    'breadcrumbs.middleware.FlatpageFallbackMiddleware',
    'maintenance.middleware.MaintenanceMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

#ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATE_DIRS = (
    #'/home/merenbach/webapps/django/project/templates',
    os.path.join(CORE_PROJECT_PATH, 'templates'),
    os.path.join(PROJECT_PATH, 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        #'django.contrib.auth.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.request',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        #'cms.context_processors.media',
        'sekizai.context_processors.sekizai',
	'django.core.context_processors.csrf',
        'zinnia.context_processors.version',    # optional
        #'django_mobile.context_processors.flavour',
        #'admintools_bootstrap.context_processors.site',
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
    'appconf',
    #'admintools_bootstrap',
    #'admin_tools',
    #'admin_tools.theming',
    #'admin_tools.menu',
    #'admin_tools.dashboard',
    #'admin_bootstrap',
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
    'sekizai',
    'pytz',
    'compressor',
    'tagging',
    'mptt',
    'zinnia',
    'google_analytics',
    'contact',
    #'pagination',              # pagination (replaced)
    'linaro_django_pagination', # pagination
    'haystack',
    'whoosh',
    #'photologue',
    'den', # custom additions and utilities
    'maintenance',
    'breadcrumbs',
    #'articles',
    'django_xmlrpc',
    #'djcelery',
    #'djsupervisor',
    #'photologue',
    'dajaxice',
    'dajax',
    'software',
    'ciphers',
    'django_clicky',
)

# caching
CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
            #'LOCATION': 'unix:/var/run/memcached/memcached.pid',
            }
        }


#ADMIN_TOOLS_MEDIA_URL = 'http://media.merenbach.com/static/'

MAINTENANCE_DISABLE_FOR_SUPERUSER = True

BREADCRUMBS_AUTO_HOME = True
#BREADCRUMBS_HOME_TITLE = 'Home'

# articles settings
#ARTICLES_AUTO_TAG = False
#USE_ADDTHIS_BUTTON = False

# analytics settings
GOOGLE_ANALYTICS_MODEL = True
GOOGLE_ANALYTICS_TRACK_PAGE_LOAD_TIME = True


COMPRESS_PRECOMPILERS = (
        #('text/coffeescript', 'coffee --compile --stdio'),
        #('text/less', 'lessc {infile} {outfile}'),
        #('text/x-sass', 'sass {infile} {outfile}'),
        ('text/x-scss', 'sass --scss {infile} {outfile}'),
        )

#COMPRESS_OFFLINE = True
COMPRESS_OFFLINE = False
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'

HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
            'PATH': os.path.join(PROJECT_ROOT, 'whoosh_index'),
            #'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
            'TIMEOUT': 60 * 5,
            'INCLUDE_SPELLING': True,
            'BATCH_SIZE': 100,
            },
        #'default{}'.format(SITE_ID): {
        #    'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        #    'PATH': os.path.join(os.path.dirname(__file__), 'websites', OVERLOAD_SITE, 'whoosh_index'),
        #    #'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
        #    'TIMEOUT': 60 * 5,
        #    'INCLUDE_SPELLING': True,
        #    'BATCH_SIZE': 100,
        #    },
        }

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 5
#HAYSTACK_ROUTERS = ['core.routers.SiteRouter']

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

# formerly site-specific for merenbach.com

#MEDIA_CDN_DOMAIN = 'http://cdn.merenbach.com/'
#DJANGO_STATIC_FILE_PROXY = 'den.cdn.cdn_origin_pull_file_proxy'


from urlparse import urljoin
from os.path import join

SITE_ID = 1

# for the contact form
CONTACT_RECIPIENTS = ('andrew@merenbach.com',)

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = '/srv/www/merenbach.com/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
if not DEBUG:
    MEDIA_URL = 'http://cdn.merenbach.com/'
else:
    MEDIA_URL = 'http://media.merenbach.com'

# Absolute path to the directory static files should be collected to.
STATIC_ROOT = join(MEDIA_ROOT, 'static')

# URL prefix for static files.
STATIC_URL = urljoin(MEDIA_URL, 'static/')

# deprecated but apparently still necessary for some things
ADMIN_MEDIA_PREFIX = urljoin(STATIC_URL, 'admin/')

ROOT_URLCONF = 'den.urls'

# DISQUS
DISQUS_FORUM_SHORTNAME = 'merenbach'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'den.wsgi.application'

CLICKY_SITE_ID = '66628570'
#CLICKY_RENDER_NON_JS_CODE = False

DAJAXICE_MEDIA_PREFIX = 'dajaxice'
DAJAXICE_DEBUG = False
DAJAXICE_NOTIFY_EXCEPTIONS = True
#import logging
#logging.basicConfig(level=logging.DEBUG)

ZINNIA_MARKUP_LANGUAGE = 'markdown'
ZINNIA_WYSIWYG = False
from zinnia.xmlrpc import ZINNIA_XMLRPC_METHODS
XMLRPC_METHODS = ZINNIA_XMLRPC_METHODS

