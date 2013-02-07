from django.conf.urls import patterns, url, include
from rsvp.views import InvitationView, ResponseCardView, ResponseCardThanksView

urlpatterns = patterns('',
    url(r'^(?P<slug>[0-9a-fA-F]+)/$', InvitationView.as_view(), name='rsvp-invitation'),
    url(r'^(?P<slug>[0-9a-fA-F]+)/respond/$', ResponseCardView.as_view(), name='rsvp-response-card'),
    url(r'^thanks/$', ResponseCardThanksView.as_view(), name='rsvp-response-thanks'),
)
