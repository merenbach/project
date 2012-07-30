# Django settings for project www.merenbach.com.

from settings_private import *

from core.settings import *
from urlparse import urljoin
from os.path import join

SITE_ID = 1

# for the contact form
CONTACT_RECIPIENTS = ('andrew@merenbach.com',)

# Absolute path to the directory static files should be collected to.
STATIC_ROOT = join(MEDIA_ROOT, 'static')

# URL prefix for static files.
STATIC_URL = urljoin(MEDIA_URL, 'static/')

# deprecated but apparently still necessary for some things
ADMIN_MEDIA_PREFIX = urljoin(STATIC_URL, 'admin/')

ROOT_URLCONF = 'sites.merenbach.urls'

# DISQUS
DISQUS_FORUM_SHORTNAME = 'merenbach'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'sites.merenbach.wsgi.application'

INSTALLED_APPS += (
        'photologue',
        'dajaxice',
        'dajax',
        'software',
        'ciphers',
        )

DAJAXICE_MEDIA_PREFIX = 'dajaxice'
DAJAXICE_DEBUG = False
DAJAXICE_NOTIFY_EXCEPTIONS = True
#import logging
#logging.basicConfig(level=logging.DEBUG)

