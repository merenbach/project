from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from core.urls import urlpatterns

urlpatterns += patterns('',
        #(r'^contact/', include('contact.urls')),
        #(r'^contact/', include('contact.urls')),
        #(r'^search/', include('haystack.urls')),
        #url(r'^$', TemplateView.as_view(template_name='home.html'), name='home_url_name'),
        #url(r'^bio/$', TemplateView.as_view(template_name='about.html'), name='about_url_name'),
        # Examples:
        # url(r'^$', 'project.views.home', name='home'),
        # url(r'^project/', include('project.foo.urls')),

        # Uncomment the admin/doc line below to enable admin documentation:
        #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

        # Uncomment the next line to enable the admin:
        #url(r'^admin/', include(admin.site.urls)),
        )

urlpatterns += patterns('django.contrib.flatpages.views',
        url(r'^bio/$', 'flatpage', {'url': '/bio/'}, name='bio'),
        #url(r'^license/$', 'flatpage', {'url': '/license/'}, name='license'),
        )
