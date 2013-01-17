# Utilities for maintenance

def get_current_site_messages(request):
    """ Cover for get_site_messages """
    from django.contrib.sites.models import get_current_site
    return get_site_messages(get_current_site(request))

def get_site_messages(site):
    """
    Retrieve messages for the current site, updating the cache as necessary.
    Adapted from inner logic of `thinkjson/django-maintenance` (on Github).
    """
    from django.conf import settings
    from django.core.cache import cache
    from django.utils import timezone
    from maintenance.models import MaintenanceMessage
    from django.db.models import Q
    if getattr(settings, 'MAINTENANCE_CACHE_MESSAGES', False):
        messages = cache.get('maintenance_messages')
    else:
        # This will otherwise be undefined
        messages = None
    if not messages:
        messages = MaintenanceMessage.objects.filter(sites__id=site.id)\
            .filter(start_time__lt=timezone.now())\
            .filter(\
            Q(end_time__gte=timezone.now()) | Q(end_time__isnull=True) )
        cache.set('maintenance_messages', messages, getattr(settings, 'MAINTENANCE_CACHE_SECONDS', 3600))
    return messages

def is_privileged_request(request):
    """
    Superusers get unconditional access. Staff by default do not. This is
    configurable in `settings.py`, but the setting is completely optional.
    This, too, is adapted from `thinkjson/django-maintenance` (on Github).
    """
    from django.conf import settings
    disable_for_staff = getattr(settings, 'MAINTENANCE_DISABLE_FOR_STAFF', False)
    # Allow access if the user doing the request is logged in and a
    # superuser or (if allowed) a staff member.
    if hasattr(request, 'user'):
        if request.user.is_superuser:
            return True
        elif request.user.is_staff and disable_for_staff:
            return True
    return False
