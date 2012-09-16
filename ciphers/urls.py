from django.conf.urls import patterns, url
from ciphers.views import CiphersView

urlpatterns = patterns('',
    url(r'^$', CiphersView.as_view(), name='ciphers'),
)
