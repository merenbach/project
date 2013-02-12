from django.conf.urls import patterns, url, include
from rsvp.views import *

urlpatterns = patterns('',
    url(r'^$', CookieView.as_view(), name='rsvp-cookie'),
    url(r'^(?P<slug>[0-9a-fA-F]+)/$', EnvelopeView.as_view(), name='rsvp-envelope'),
    url(r'^(?P<slug>[0-9a-fA-F]+)/read/$', InvitationView.as_view(), name='rsvp-invitation'),
    url(r'^(?P<slug>[0-9a-fA-F]+)/respond/$', ResponseCardView.as_view(), name='rsvp-response-card'),
    url(r'^thanks/$', ResponseCardThanksView.as_view(), name='rsvp-response-thanks'),
)
