from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from core.urls import urlpatterns

urlpatterns += patterns('',
        (r'^photologue/', include('photologue.urls')),
        #url(r'^$', TemplateView.as_view(template_name='home.html'), name='home_url_name'),
        # Examples:
        # url(r'^$', 'project.views.home', name='home'),
        # url(r'^project/', include('project.foo.urls')),

        # Uncomment the admin/doc line below to enable admin documentation:
        #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

        # Uncomment the next line to enable the admin:
        #url(r'^admin/', include(admin.site.urls)),
        )

urlpatterns += patterns('django.contrib.flatpages.views',
        url(r'^events/$', 'flatpage', {'url': '/events/'}, name='events'),
        url(r'^friends-and-family/$', 'flatpage', {'url': '/friends-and-family/'}, name='friends_and_family'),
        url(r'^our-story/$', 'flatpage', {'url': '/our-story/'}, name='our_story'),
        #url(r'^gallery/$', 'flatpage', {'url': '/gallery/'}, name='gallery'),
        url(r'^registry/$', 'flatpage', {'url': '/registry/'}, name='registry'),
        )
