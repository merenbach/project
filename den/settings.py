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

