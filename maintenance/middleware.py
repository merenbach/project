from django.conf import settings
from django.core import urlresolvers
from django.middleware.common import CommonMiddleware
from django.template.response import TemplateResponse
from maintenance.utils import is_privileged_request, get_current_site_messages

"""
Adapted from inner logic of `thinkjson/django-maintenance` (on Github),
along with some inspiration from `btaylordesign/django-maintenancemode`
(also on Github).

A minor change: all superusers may access content during a maintenance
period. Staff, however, may or may not (at administrator discretion)
have this ability.

# Allow staff to bypass maintenance mode pages.
# Superusers automatically receive this privilege.
MAINTENANCE_DISABLE_FOR_STAFF = False
"""
class MaintenanceMiddleware(CommonMiddleware):
    def process_request(self, request):
        if request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS:
            # Allow access if remote ip is in INTERNAL_IPS
            return None
        elif is_privileged_request(request):
            # Allow privileged users (superusers and possibly staff) through
            return None
        else:
            try:
                view, args, kwargs = urlresolvers.resolve(request.path)
            except:
                return None
            if 'django.contrib.admin' in view.__module__ or  'django.views.static' in view.__module__ or 'maintenance.heartbeat' in view.__module__:
                return None

        messages = get_current_site_messages(request)
        if messages.count() > 0:
            return TemplateResponse(request, '503.html', context={'maintenance_messages': messages}, status=503)
        else:
           return None
