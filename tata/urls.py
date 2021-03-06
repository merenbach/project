from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView

# import site specific urls
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Sitemaps

from django.contrib.sitemaps import FlatPageSitemap

sitemaps = {
    'pages': FlatPageSitemap,
}

# Examples:
# url(r'^$', 'project.views.home', name='home'),
# url(r'^project/', include('project.foo.urls')),
urlpatterns = patterns('',
    #(r'^contact/', include('contact.urls')),
    #(r'^contact/', include('contact.urls')),
    #url(r'^search/', search_view_factory(
    #        view_class=SearchView,
    #        #searchqueryset=sqs,
    #        form_class=SearchForm
    #    ),
    #    name='haystack_search'
    #),
    #url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc'),
    (r'^robots\.txt$', include('robots.urls')),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.index', {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+)\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #(r'^$', TemplateView.as_view(template_name='index.html')),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^$', 'flatpage', {'url': '/'}, name='home'),
    #url(r'^about/$', 'flatpage', {'url': '/about/'}, name='about'),
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
