"""
    This is based on a fork of django-maintenancemode:

    <https://github.com/btaylordesign/django-maintenancemode/>

    This fork is being merged here with a fork of following module:

    <https://github.com/thinkjson/django-maintenance/>

    And some class based views.
"""

from django.http import HttpResponse
from django.views.generic import View
from maintenance.utils import get_current_site_messages

class HeartbeatView(View):
    """
    Heartbeat
    """
    def dispatch(self, request, *args, **kwargs):
        """ Return the view with a 503 status code """
        if not get_current_site_messages(request).count():
            # Status code 200
            return HttpResponse('OK')
        else:
            return HttpResponse('Service Unavailable', status=503)
