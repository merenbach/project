from fabric.api import *
import os

PROJECT_PATH = os.path.join('/', 'srv', 'www', 'merenbach.com', 'django', 'den')

def pull():
    with cd(PROJECT_PATH):
        local('git pull origin master')
        local('python manage.py collectstatic --noinput')
	local('touch den/wsgi.py')

def collect():
    with cd(PROJECT_PATH):
        local('env PYTHONPATH=/srv/www/django/lib/python2.6/site-packages python manage.py collectstatic --noinput')
