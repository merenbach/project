from django.conf.urls.defaults import url, patterns, include
from software.views import SoftwareIndexView, SoftwareDetailView, SoftwareTagView

urlpatterns = patterns('',
    url(r'^$', SoftwareIndexView.as_view(), name='software'),
    url(r'^(?P<slug>[-a-z0-9]+)/$', SoftwareDetailView.as_view(), name='software_detail'),
    url(r'^tagged/(?P<tag>[^/]+)/$', SoftwareTagView.as_view(), name='software_tag_detail'),
    #(r'^tags/$', 'software.views.tags'),
)