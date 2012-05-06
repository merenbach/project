from django.conf.urls import *
from django.conf import settings

from core.urls import urlpatterns, sitemaps

# Dajaxice
from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()

# sitemaps
from software.sitemaps import SoftwareSitemap
sitemaps.update({'software': SoftwareSitemap})

urlpatterns += patterns('',
        (r'^{}/'.format(settings.DAJAXICE_MEDIA_PREFIX), include('dajaxice.urls')),
        #url(r'^$', TemplateView.as_view(template_name='home.html'), name='home_url_name'),
        (r'^ciphers/', include('ciphers.urls')),
        (r'^software/', include('software.urls')),
        #(r'^google67b472340d465ad6.html$', 'test'),
        #url(r'^$', 'project.views.home', name='home'),
        # Examples:
        # url(r'^$', 'project.views.home', name='home'),
        # url(r'^project/', include('project.foo.urls')),
        )
