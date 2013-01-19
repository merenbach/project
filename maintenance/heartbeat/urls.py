# urls for optional maintenance add-on to monitor site uptime

from django.conf.urls import patterns, url, include
from django.views.decorators.cache import never_cache
from maintenance.heartbeat.views import HeartbeatView

urlpatterns = patterns('',
    (r'^status/$', never_cache(HeartbeatView.as_view())),
)