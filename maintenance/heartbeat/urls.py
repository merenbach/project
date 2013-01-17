from django.conf.urls.defaults import patterns, url, include
from django.views.decorators.cache import never_cache
from maintenance.heartbeat.views import HeartbeatView

urlpatterns = patterns('',
    url(r'^status/$', never_cache(HeartbeatView.as_view()), name='maintenance-heartbeat'),
)