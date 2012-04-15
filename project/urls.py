from django.conf.urls import patterns, include, url

# import site specific urls
from django.conf import settings
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# sitemaps
from django.contrib.sitemaps import FlatPageSitemap
sitemaps = {
        'pages': FlatPageSitemap,
        }

handler500 = 'views.server_error'

if hasattr(settings, "OVERLOAD_SITE_MODULE"):
    exec ("from {}.urls import sitemaps as site_sitemaps".format(settings.OVERLOAD_SITE_MODULE))
    sitemaps.update(site_sitemaps)

urlpatterns = patterns('',
    (r'^contact/', include('contact.urls')),
    #(r'^search/', include('haystack.urls')),
    #url('^googlever.html$', direct_to_template, {'template': 'google67b472340d465ad6.html'}),
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if hasattr(settings, "OVERLOAD_SITE_MODULE"):
    exec ("from {}.urls import urlpatterns as site_urls".format(settings.OVERLOAD_SITE_MODULE))
    urlpatterns = site_urls + urlpatterns

if settings.DEBUG:
    urlpatterns = patterns('',
            #(r'^500/$', handler500),
            #(r'^500/$', 'django.views.defaults.server_error'),
            (r'^404/$', 'django.views.defaults.page_not_found'),
            (r'^500/$', 'views.server_error'),  # use our custom view*
            url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
            url(r'', include('django.contrib.staticfiles.urls')),
            ) + urlpatterns

