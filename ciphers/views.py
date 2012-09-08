# Render the ciphers view

from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

class CiphersView(TemplateView):
    template_name = 'ciphers/ciphers_index.html'
    
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs('Ciphers', reverse('ciphers'))
        return super(CiphersView, self).dispatch(request, *args, **kwargs)

