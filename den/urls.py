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
from den.sitemaps import ArticleSitemap
sitemaps = {
        'pages': FlatPageSitemap,
        'articles': ArticleSitemap,
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

#if hasattr(settings, "OVERLOAD_SITE_MODULE"):
#    exec ("from {}.urls import sitemaps as site_sitemaps".format(settings.OVERLOAD_SITE_MODULE))
#    sitemaps.update(site_sitemaps)

urlpatterns = patterns('',
        #url(r'^$', 'project.views.home', name='home'),
        url(r'^blog/', include('articles.urls')),
        url(r'^contact/', include('contact.urls')),
        #url(r'^search/', include('haystack.urls')),
        url(r'^search/', search_view_factory(
            view_class=SearchView,
            searchqueryset=sqs,
            form_class=SearchForm),
            name='haystack_search'),
        url(r'^weblog/', include('zinnia.urls')),
	url(r'^comments/', include('django.contrib.comments.urls')),
        #url('^googlever.html$', direct_to_template, {'template': 'google67b472340d465ad6.html'}),
        # Examples:
        # url(r'^$', 'project.views.home', name='home'),
        # url(r'^project/', include('project.foo.urls')),
        url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
        url(r'^admin_tools/', include('admin_tools.urls')),
        # Uncomment the admin/doc line below to enable admin documentation:
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

        # Uncomment the next line to enable the admin:
        url(r'^admin/', include(admin.site.urls)),
        )

#urlpatterns += patterns('django.contrib.flatpages.views',
#        url(r'^$', 'flatpage', {'url': '/'}, name='home'),
#        #url(r'^license/$', 'flatpage', {'url': '/license/'}, name='license'),
#        )

#if hasattr(settings, "OVERLOAD_SITE_MODULE"):
#    exec ("from {}.urls import urlpatterns as site_urls".format(settings.OVERLOAD_SITE_MODULE))
#    urlpatterns = site_urls + urlpatterns

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

# Dajaxice
from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()

# sitemaps
from software.sitemaps import SoftwareSitemap
sitemaps.update({'software': SoftwareSitemap})

urlpatterns += patterns('',
        url(r'^$', include('articles.urls'), name='home'),
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

urlpatterns += patterns('django.contrib.flatpages.views',
        url(r'^about/$', 'flatpage', {'url': '/about/'}, name='about'),
        )

