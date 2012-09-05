from django.conf import settings
from django.http import HttpResponseServerError
from django.template import Context, loader
from sekizai.context import SekizaiContext

def server_error(request, template_name='500.html'):
    """
    500 error handler.

    Templates: `500.html`
    Context:
    MEDIA_URL
    Path of static media (e.g. "media.example.org")
    """
    t = loader.get_template(template_name) # You need to create a 500.html template.
    return HttpResponseServerError(t.render(SekizaiContext({
        'MEDIA_URL': settings.MEDIA_URL,
        'STATIC_URL': settings.STATIC_URL,
        })))
