from maintenance.models import MaintenanceMessage
from django.utils import timezone
from django.conf import settings
from django.core import urlresolvers
from django.db.models import Q
from maintenance.views import MaintenanceView
from django.middleware.common import CommonMiddleware
from django.contrib.sites.models import get_current_site

# from django.conf.urls import defaults

# defaults.handler503 = 'maintenance.views.MaintenanceView.as_view'
# defaults.__all__.append('handler503')

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
        elif self.is_privileged_request(request):
            # Allow privileged users (superusers and possibly staff) through
            return None
        else:
            try:
                view, args, kwargs = urlresolvers.resolve(request.path)
            except Exception:
                return None
            if 'django.contrib.admin' in view.__module__ or  'django.views.static' in view.__module__:
                return None

        messages = self.get_site_messages(get_current_site(request))
        if messages.count() > 0:
            return MaintenanceView.as_view()(request, messages=messages)
        else:
           return None

        ## Otherwise show the user the 503 page
        # resolver = urlresolvers.get_resolver(None)
        #
        # callback, param_dict = resolver._resolve_special('503')
        # return callback(request, **param_dict)

    def is_privileged_request(self, request):
        """
        Superusers get unconditional access. Staff by default do not. This is
        configurable in `settings.py`, but the setting is completely optional.
        """
        disable_for_staff = getattr(settings, 'MAINTENANCE_DISABLE_FOR_STAFF', False)
        # Allow access if the user doing the request is logged in and a
        # superuser or (if allowed) a staff member.
        if hasattr(request, 'user'):
            if request.user.is_superuser:
                return True
            elif request.user.is_staff and disable_for_staff:
                return True
        return False

    def get_site_messages(self, site):
        """ Retrieve messages for the current site, updating the cache as necessary """
        from django.core.cache import cache
        if getattr(settings, 'MAINTENANCE_CACHE_MESSAGES', False):
            messages = cache.get('maintenance_messages')
        else:
            """ This will otherwise be undefined """
            messages = None
        if not messages:
            messages = MaintenanceMessage.objects.filter(sites__id=site.id)\
                .filter(start_time__lt=timezone.now())\
                .filter(\
                Q(end_time__gte=timezone.now()) | Q(end_time__isnull=True) )
            cache.set('maintenance_messages', messages, getattr(settings, 'MAINTENANCE_CACHE_SECONDS', 3600))
        return messages
