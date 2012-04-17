from django.conf.urls import patterns, include, url

# import site specific urls
from django.conf import settings
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Haystack search
from haystack.forms import SearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView
from haystack.views import search_view_factory
from haystack.query import SQ

# sitemaps
from django.contrib.sitemaps import FlatPageSitemap
sitemaps = {
        'pages': FlatPageSitemap,
        }

handler500 = 'views.server_error'

sq1 = SQ(sites__id=settings.SITE_ID)
sq2 = SQ(pub_site=settings.SITE_ID)
sqs = SearchQuerySet().filter(sq1 | sq2)
# other possibilities and iterations (some more useful/illustrative than others):
#sqs = SearchQuerySet().filter(sites__id=settings.SITE_ID)
#sqs = SearchQuerySet().filter(site__id=1)
#sqs = SearchQuerySet().filter(sites__id=settings.SITE_ID).order_by("-pub_date")
#sqs = SearchQuerySet().filter(sites__id=settings.SITE_ID)
#sqs = SearchQuerySet().filter(site=1)
#sqs = SearchQuerySet().filter(SQ(sites__id=settings.SITE_ID) | SQ(model_name=u'software'))

if hasattr(settings, "OVERLOAD_SITE_MODULE"):
    exec ("from {}.urls import sitemaps as site_sitemaps".format(settings.OVERLOAD_SITE_MODULE))
    sitemaps.update(site_sitemaps)

urlpatterns = patterns('',
        #url(r'^$', 'project.views.home', name='home'),
        url(r'^contact/', include('contact.urls')),
        #url(r'^search/', include('haystack.urls')),
        url(r'^search/', search_view_factory(
            view_class=SearchView,
            searchqueryset=sqs,
            form_class=SearchForm),
            name='haystack_search'),
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

urlpatterns += patterns('django.contrib.flatpages.views',
        url(r'^$', 'flatpage', {'url': '/'}, name='home'),
        #url(r'^license/$', 'flatpage', {'url': '/license/'}, name='license'),
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

