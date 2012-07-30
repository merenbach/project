"""
WSGI config for project www.merenbach.com.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sites.merenbach.settings')

# determine the path to the project, which will be two parent directories up
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir)))

from core.wsgi import *
