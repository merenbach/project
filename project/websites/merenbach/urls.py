from django.conf.urls import *
from django.conf import settings
from django.views.generic import TemplateView

# Dajaxice
from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()

# sitemaps
from django.contrib.sitemaps import Sitemap
from software.sitemaps import SoftwareSitemap
sitemaps = {
        'software': SoftwareSitemap,
        }

urlpatterns = patterns('',
        (r'^{}/'.format(settings.DAJAXICE_MEDIA_PREFIX), include('dajaxice.urls')),
        #url(r'^$', TemplateView.as_view(template_name='home.html'), name='home_url_name'),
        (r'^ciphers/$', include('ciphers.urls')),
        (r'^software/', include('software.urls')),
        #(r'^google67b472340d465ad6.html$', 'test'),
        #url(r'^$', 'project.views.home', name='home'),
        # Examples:
        # url(r'^$', 'project.views.home', name='home'),
        # url(r'^project/', include('project.foo.urls')),

        # Uncomment the admin/doc line below to enable admin documentation:
        #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

        # Uncomment the next line to enable the admin:
        #url(r'^admin/', include(admin.site.urls)),
        )
