# Django settings for project project.

# Datetime fix
# http://stackoverflow.com/questions/2427240/thread-safe-equivalent-to-pythons-time-strptime
from datetime import datetime
datetime.strptime("1986-07-01", "%Y-%m-%d")
#datetime.datetime(1986, 7, 1, 0, 0)


import os
import sys

# get the settings path
PROJECT_ROOT = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))
PROJECT_PATH = os.path.abspath(PROJECT_ROOT)

if PROJECT_PATH not in sys.path:
    sys.path.insert(0, PROJECT_PATH)

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

PREPEND_WWW = True

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

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

# MIDDLEWARE_CLASSES = (
#     'django.middleware.cache.UpdateCacheMiddleware',
#     'django.middleware.gzip.GZipMiddleware',
#     'django.middleware.http.ConditionalGetMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
#     # Uncomment the next line for simple clickjacking protection:
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'maintenance.middleware.MaintenanceMiddleware',
#     'django.middleware.transaction.TransactionMiddleware',
#     'django.middleware.cache.FetchFromCacheMiddleware',
# )

# Cache only anonymous requests
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
# Cache each page for 5 minutes (default)
# CACHE_MIDDLEWARE_SECONDS = 600

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'sekizai.context_processors.sekizai',
    'common.context_processors.site',
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
    'common', # my common extensions
    'south',
    'appconf',
    'sekizai',
    'pytz',
    'markdown_deux', # the built-in mechanism is deprecated
    'compressor',
    'maintenance',
    #'maintenance.heartbeat',
    'analytical',
    'memcache_status',
    'django_extensions',
    'widget_tweaks', # modify form widgets
)

# Trying to emulate the legacy Markdown from Django
MARKDOWN_DEUX_STYLES = {
    "default": {
        "extras": {
            "code-friendly": None,
        },
        "safe_mode": False,
    },
}

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

# Maintenance
## Caching on a multi-site install with differing key prefixes
## (what one would expect) makes it hard to clear caches and
## turn off maintenance mode for sites other than the one whose
## interface is being accessed to change the message.  A separate
## cache backend would help, but might be overkill.
# MAINTENANCE_CACHE_MESSAGES = True
# MAINTENANCE_DISABLE_FOR_STAFF = True

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
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter', 'compressor.filters.cssmin.CSSMinFilter']
