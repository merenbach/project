"""
    This is based on a fork of django-maintenancemode:

    <https://github.com/btaylordesign/django-maintenancemode/>

    This fork is being merged here with a fork of following module:

    <https://github.com/thinkjson/django-maintenance/>

    And some class based views.
"""

from django.contrib.sites.models import get_current_site
from django.db.models import Q
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import View, TemplateView
from maintenance.models import MaintenanceMessage

class MaintenanceView(TemplateView):
    """
    Default 503 handler, which looks for the requested URL in the redirects
    table, redirects if found, and displays 404 page if not redirected.

    Templates: `503.html`
    Context:
        request_path
            The path of the requested URL (e.g., '/app/pages/bad_page/')
    """
    template_name = '503.html'

    def render_to_response(self, context):
        """ Return the view with a 503 status code """
        return super(MaintenanceView, self).render_to_response(context, status=503)

    #def dispatch(self, request, *args, **kwargs):
    #    return super(ContactView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MaintenanceView, self).get_context_data(**kwargs)
        messages = kwargs.get('messages', None)
        if messages is not None:
            context['maintenance_messages'] = messages
        return context

class HeartbeatView(View):
    """
    Heartbeat
    """
    def dispatch(self, request, *args, **kwargs):
        """ Return the view with a 503 status code """
        if not self.has_messages(request):
            return HttpResponse('OK')
        else:
            return HttpResponse('Service Unavailable', status=503)

    def has_messages(self, request):
        return MaintenanceMessage.objects.filter(sites__id=get_current_site(request).id)\
            .filter(start_time__lt=timezone.now())\
            .filter(\
                Q(end_time__gte=timezone.now()) | Q(end_time__isnull=True) ).count() > 0
