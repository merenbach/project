from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

urlpatterns = patterns('',
        url(r'^$', TemplateView.as_view(template_name='ciphers/ciphers_index.html')),
        #(r'^$', CiphersView.as_view()),
        #(r'^.*$', 'project.websites.merenbach.ciphers.views.ciphers_index'),
        #(r'^$', direct_to_template, {'template': 'ciphers_index.html'}),
        )
