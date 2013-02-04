from django.conf.urls import patterns, url, include
from rsvp.views import RespondezView, RespondezThanksView

urlpatterns = patterns('',
    url(r'^(?P<token>[0-9a-fA-F]+)/$', RespondezView.as_view(), name='respondez'),
    url(r'^(?P<token>[0-9a-fA-F]+)/thanks/$', RespondezThanksView.as_view(), name='respondez-thanks'),
)
