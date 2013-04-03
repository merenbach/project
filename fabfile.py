from fabric.api import *
import os

SERVER_BASE = os.path.join('/', 'srv', 'www')
DJANGO_BASE = os.path.join(SERVER_BASE, 'django')

PYTHON_PATH = os.path.join(DJANGO_BASE, 'lib', 'python2.6' , 'site-packages')
PYTHON_EXEC = os.path.join(DJANGO_BASE, 'bin', 'python')
MANAGE_FILE = os.path.join(os.path.dirname(__file__), 'manage.py')
MANAGE_CMD='env PYTHONPATH={0} {1} {2}'.format(PYTHON_PATH, PYTHON_EXEC, MANAGE_FILE)

#def pull():
#    with cd(PROJECT_PATH):
#        local('git pull origin master')
#        local('python manage.py collectstatic --noinput')
#	local('touch den/wsgi.py')

def compress(settings=None):
    if settings is not None:
        cmd = 'sudo -u www-data {0} compress --settings={1}.settings'.format(MANAGE_CMD, settings)
        print('[+] Running the following command:')
        print('# {0}'.format(cmd))
        local(cmd)
    else:
        print('Please specify a project.')

def collect(settings=None):
    if settings is not None:
        cmd = 'sudo -u www-data {0} collectstatic --noinput --settings={1}.settings'.format(MANAGE_CMD, settings)
        print('[+] Running the following command:')
        print('# {0}'.format(cmd))
        local(cmd)
        compress(settings=settings)
    else:
        print('Please specify a project.')

def rebuild_index(settings=None):
    if settings is not None:
        cmd = 'echo y | sudo -u www-data {0} rebuild_index --settings={1}.settings'.format(MANAGE_CMD, settings)
        print('[+] Running the following command:')
        print('# {0}'.format(cmd))
        local(cmd)
    else:
        print('Please specify a project.')

def update_index(settings=None):
    if settings is not None:
        cmd = 'sudo -u www-data {0} update_index --settings={1}.settings'.format(MANAGE_CMD, settings)
        print('[+] Running the following command:')
        print('# {0}'.format(cmd))
        local(cmd)
    else:
        print('Please specify a project.')

