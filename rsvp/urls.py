from django.conf.urls import patterns, url, include
from rsvp.views import InvitationView, ResponseCardThanksView

urlpatterns = patterns('',
    url(r'^(?P<slug>[0-9a-fA-F]+)/$', InvitationView.as_view(), name='respondez'),
    url(r'^(?P<slug>[0-9a-fA-F]+)/thanks/$', ResponseCardThanksView.as_view(), name='respondez-thanks'),
)
