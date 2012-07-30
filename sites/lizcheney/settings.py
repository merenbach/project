# Django settings for project www.lizcheney.com.
#import warnings
#warnings.filterwarnings(
#        'error', r"DateTimeField received a naive datetime",
#        RuntimeWarning, r'django\.db\.models\.fields')

from settings_private import *

from core.settings import *
from urlparse import urljoin
from os.path import join

SITE_ID = 2

# for the contact form
CONTACT_RECIPIENTS = ('andrew@merenbach.com', 'commonreader@gmail.com')

# Absolute path to the directory static files should be collected to.
STATIC_ROOT = join(MEDIA_ROOT, 'static')

# URL prefix for static files.
STATIC_URL = urljoin(MEDIA_URL, 'static/')

# deprecated but apparently still necessary for some things
ADMIN_MEDIA_PREFIX = urljoin(STATIC_URL, 'admin/')

ROOT_URLCONF = 'sites.lizcheney.urls'

# DISQUS
DISQUS_FORUM_SHORTNAME = 'lizcheney'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'sites.lizcheney.wsgi.application'

INSTALLED_APPS += (
    'photologue',
)

