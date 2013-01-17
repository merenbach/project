# Utilities for maintenance

def get_current_site_messages(request):
    from django.contrib.sites.models import get_current_site
    return get_site_messages(get_current_site(request))

def get_site_messages(site):
    """ Retrieve messages for the current site, updating the cache as necessary """
    from django.conf import settings
    from django.core.cache import cache
    from django.utils import timezone
    from maintenance.models import MaintenanceMessage
    from django.db.models import Q
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
