from django.conf import settings
from django.core import urlresolvers
from django.middleware.common import CommonMiddleware
from maintenance.utils import is_privileged_request, get_current_site_messages
from maintenance.views import MaintenanceView

"""
Possible settings and their defaults:

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
            except Exception:
                return None
            if 'django.contrib.admin' in view.__module__ or  'django.views.static' in view.__module__ or 'maintenance.heartbeat' in view.__module__:
                return None

        messages = get_current_site_messages(request)
        if messages.count() > 0:
            return MaintenanceView.as_view()(request, messages=messages)
        else:
           return None

        ## Otherwise show the user the 503 page
        # resolver = urlresolvers.get_resolver(None)
        #
        # callback, param_dict = resolver._resolve_special('503')
        # return callback(request, **param_dict)

 