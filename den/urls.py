from django.conf.urls import patterns, include, url

# import site specific urls
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Dajaxice
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

# Haystack search
from haystack.forms import SearchForm
from haystack.views import SearchView
from haystack.views import search_view_factory

# Sitemaps

from django.contrib.sitemaps import FlatPageSitemap
from software.sitemaps import SoftwareSitemap
from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap
from photologue.sitemaps import PhotologueSitemap

sitemaps = {
    'pages': FlatPageSitemap,
    'tags': TagSitemap,
    'blog': EntrySitemap,
    'authors': AuthorSitemap,
    'categories': CategorySitemap,
    'software': SoftwareSitemap,
    'photologue': PhotologueSitemap,
}

# Examples:
# url(r'^$', 'project.views.home', name='home'),
# url(r'^project/', include('project.foo.urls')),
urlpatterns = patterns('',
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    (r'^contact/', include('contact.urls')),
    (r'^ciphers/', include('ciphers.urls')),
    (r'^software/', include('software.urls')),
    # (r'^search/', include('haystack.urls')),
    url(r'^search/', search_view_factory(
            view_class=SearchView,
            #searchqueryset=sqs,
            form_class=SearchForm
        ),
        name='haystack_search'
    ),
    url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc'),
    # Account for agents that may look for the PHP file first
    url(r'^xmlrpc.php$', 'django_xmlrpc.views.handle_xmlrpc'),
    (r'^robots\.txt$', include('robots.urls')),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.index', {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+)\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'', include('social_auth.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    (r'^', include('maintenance.heartbeat.urls')),
    (r'^', include('zinnia.urls')),
    (r'^', include('photologue.urls')),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^about/$', 'flatpage', {'url': '/about/'}, name='about'),
    url(r'^privacy/$', 'flatpage', {'url': '/privacy/'}, name='privacy'),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns = patterns('',
        (r'^500/$', 'django.views.defaults.server_error'),
        (r'^404/$', 'django.views.defaults.page_not_found'),
        (r'^403/$', 'django.views.defaults.permission_denied'),
        #(r'^503/$', 'views.maintenance.something'),  # use our custom view
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    ) + urlpatterns
