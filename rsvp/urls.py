from django.conf.urls import patterns, url, include
from rsvp.views import RespondezView

urlpatterns = patterns('',
    # url(r'^$', ContactView.as_view(), name='contact'),
    url(r'^(?P<token>[0-9a-fA-F]+)$', RespondezView.as_view(), name='respondez'),
)
