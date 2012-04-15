from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

urlpatterns = patterns('',
        url(r'^$', 'contact.views.send_message', name='contact'),
        (r'^thanks/$', 'contact.views.thanks'),
        )
