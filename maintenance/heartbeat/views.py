# views for optional maintenance add-on to monitor site uptime

from django.http import HttpResponse
from django.views.generic import View
from maintenance.utils import get_current_site_messages

class HeartbeatView(View):
    def dispatch(self, request, *args, **kwargs):
        """ Return the view with a 503 status code """
        if not get_current_site_messages(request).count():
            # Status code 200: OK
            return HttpResponse('OK')
        else:
            # Status code 503: Service Unavailable
            return HttpResponse('Service Unavailable', status=503)
