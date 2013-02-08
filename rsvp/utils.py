from django.conf import settings
from django.utils import timezone
import hashlib

def create_token():
    """ Create a random token to use in RSVP urls """
    m = hashlib.md5()
    m.update(settings.SECRET_KEY + str(timezone.now()))
    return m.hexdigest()

def get_full_domain(request):
    from django.contrib.sites.models import get_current_site
    protocol = 'http'
    if request.is_secure:
        protocol += 's'
    return u'{0}://{1}'.format(protocol, get_current_site(request).domain)