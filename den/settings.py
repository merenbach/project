# Django settings for project project.

# import central settings
from settings_base import *

ADMINS = (
    ('Andrew Merenbach', 'andrew@merenbach.com'),
    ('Elizabeth Cheney', 'commonreader@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'merenbach_django',                      # Or path to database file if using sqlite3.
        'USER': 'merenbach_django',                      # Not used with sqlite3.
        'PASSWORD': 'M3aning42',                  # Not used with sqlite3.
        #'HOST': '/tmp',                      # Set to empty string for localhost. Not used with sqlite3.
        #'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'HOST': '/var/run/postgresql',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^g3e8ea-_n+a1@2fo3=s%s^dv#5z-ewu-_vdpc$(n1_p@-u%qb'

# DISQUS
DISQUS_USER_API_KEY = 'ilMQnWAuQka4zQAS538fOdR4ClMUyGKKXmpdoGk3QnM8QuJyPcKcbeuNMcypfEUJ'
#DISQUS_FORUM_SHORTNAME = None

# my customizations
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'noreply@merenbach.com'
EMAIL_HOST_PASSWORD = 'tHerEstiSsIlence'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'noreply@merenbach.com'
SERVER_EMAIL = 'noreply@merenbach.com'

# celery
#BROKER_HOST = "localhost"
#BROKER_PORT = 26210
#BROKER_USER = "merenbach"
#BROKER_PASSWORD = "M3aning42"
#BROKER_VHOST = "web309"
#CELERYD_CONCURRENCY = 1
#CELERYD_NODES="w1"
#CELERY_RESULT_BACKEND="amqp"

#import djcelery
#djcelery.setup_loader()

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
MEDIA_URL = 'http://cdn.merenbach.com/'
#MEDIA_URL = 'http://media.merenbach.com/'

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

INSTALLED_APPS += (
        #'photologue',
        'dajaxice',
        'dajax',
        'software',
        'ciphers',
        'django_clicky',
        )

CLICKY_SITE_ID = '66628570'
#CLICKY_RENDER_NON_JS_CODE = False

DAJAXICE_MEDIA_PREFIX = 'dajaxice'
DAJAXICE_DEBUG = False
DAJAXICE_NOTIFY_EXCEPTIONS = True
#import logging
#logging.basicConfig(level=logging.DEBUG)

