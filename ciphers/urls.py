from django.conf.urls import patterns, url
from ciphers.views import CiphersView
#from django.views.generic import TemplateView

urlpatterns = patterns('',
        url(r'^$', CiphersView.as_view(), name='ciphers'),
        #url(r'^$', TemplateView.as_view(template_name='ciphers/ciphers_index.html'), name='ciphers'),
        )
