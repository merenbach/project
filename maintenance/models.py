from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.core.cache import cache
from django.utils.cache import get_cache_key
from django.conf import settings
from django.utils import timezone
from django.contrib.sites.models import Site

class MaintenanceMessage(models.Model):
    message = models.TextField()
    start_time = models.DateTimeField(default=timezone.now())
    end_time = models.DateTimeField(blank=True, null=True)
    sites = models.ManyToManyField(Site, blank=True, null=True, help_text='Makes item eligible to be published on selected sites.')

    def __unicode__(self):
        return self.message

# Invalidate the cache when a MaintenanceMessage is saved or deleted
@receiver(post_save, sender=MaintenanceMessage)
@receiver(post_delete, sender=MaintenanceMessage)
def invalidate_message_cache(sender, **kwargs):
    if getattr(settings, 'MAINTENANCE_CACHE_MESSAGES', False):
        cache.delete('maintenance_messages')
